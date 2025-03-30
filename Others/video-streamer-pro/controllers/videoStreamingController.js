const path = require("path");
const fs = require("fs");
const _ = require("lodash");
const bcrypt = require("bcryptjs");
const nodemailer = require("nodemailer");
const randomstring = require("randomstring");
const jwt = require("jsonwebtoken");
const { validationResult } = require("express-validator");
const {
  PRIVATE_KEY,
  JWT_EXPIRY,
  JWT_HTTPS,
  EMAIL_ADDRESS,
  EMAIL_PASSWORD,
  RES_FORMAT,
  WEB_NAME,
} = require("../services/mysql/keys");
const VIDEO_FOLDER = path.join(__dirname, "..", "videos");
const {
  getVideoFileNamesFromFolder,
  dbEmptyDatabaseTable,
  dbPopulateDatabasetableWithFilenames,
  dbUpdateOnDuplicateUserRecordsInDatabase,
  dbCheckIfRecordExistsInTable,
  dbUpdateUserPasscodeInDatabase,
  dbGetTableRecordsfromDatabase,
} = require("../models/HomeModel");

// #######################################
//  Home Controller - httpGetHomePage
// #######################################

async function httpGetHomePage(req, res) {
  const queryResult = req.data;
  const reqQuery = req.query["search"];
  if (reqQuery) {
    const filteredQueryResult = queryResult.data.filter((query) => {
      return query.name.toLowerCase().includes(`${reqQuery.toLowerCase()}`);
    });
    queryResult.data = filteredQueryResult;
  }
  const context = {
    pagename: "HOME",
    title: "AvGEE Limited",
    subtitle: "Helping You Develop, Improve & Evolve",
    member: req.user?.firstname || "admin",
    webname: WEB_NAME,
  };

  return res.render("pages/home", Object.assign(queryResult, context));
}

// #######################################
//   Home Controller - httpPostHomePage
// #######################################

async function httpPostHomePage(req, res) {
  const searchQuery = req.body.searchvalue;
  return res.redirect("?search=" + searchQuery);
}

// #######################################
//  Home Controller - httpGetVideoPlayer
// #######################################

function httpGetVideoPlayer(req, res) {
  const name = req.query["videoname"];
  const { range } = req.headers;

  // Ensure there is a range for the video
  if (!range) {
    res.status(400).send("Requires Range header");
  }

  // Get the video stats
  const videoPath = path.join(__dirname, "..", "videos", `${name}`);
  const videoSize = fs.statSync(videoPath).size;

  // Parse Range
  // Example: "bytes=6750208-"
  const CHUNK_SIZE = 5 * 10 ** 5; // 500KB
  const start = Number(range.replace(/\D/g, "")); // 'bytes=6750208-' => 6750208
  const end = Math.min(start + CHUNK_SIZE, videoSize - 1);

  // Create headers
  const contentLength = end - start + 1;
  const headers = {
    "Content-Range": `bytes ${start}-${end}/${videoSize}`,
    "Accept-Ranges": "bytes",
    "Content-Length": contentLength,
    "Content-Type": "video/mp4",
  };

  // HTTP Status 206 for Partial Content
  res.writeHead(206, headers);

  // create video read stream for this particular chunk
  const videoStream = fs.createReadStream(videoPath, { start, end });

  videoStream.pipe(res);
}

// ##############################################
//  Home Controller - httpGetVideoStreamingPage
// ##############################################

function httpGetVideoStreamingPage(req, res) {
  //get the param 4 digit video number
  let { id } = req.query;
  if (!id) {
    id = allVideoFilesNos[0];
  }

  fs.readdir(VIDEO_FOLDER, (err, files) => {
    //read the folder to get video filenames
    const { allVideoFileNames: allFiles, allVideoFilesNos: allFilesNo } =
      getVideoFileNamesFromFolder(files);

    //check if id is the first 4 digits of a video file in the folder
    const isIncluded = allFilesNo.includes(`${id}`);
    if (isIncluded) {
      //if it is in the folder, get the exact filename
      const filename = allFiles.find((file) => {
        return file.slice(0, 4) === id;
      });

      //get the video title from the filename
      let filenameWithoutExt = path.parse(filename).name;
      let videoTitle = filenameWithoutExt.slice(5);
      //path.parse(filename).name; //=> "hello"
      //path.parse(filename).ext; //=> ".html"
      //path.parse(filename).base; //=> "hello.html"

      res.status(200).render("pages/videostreamer", {
        videoTitle,
        filename,
        filenameWithoutExt,
      });
    } else {
      res.status(404).render("pages/error");
    }
  });
}

// #######################################
//  Home Controller - httpGetUserLogout
// #######################################

async function httpGetUserLogout(req, res) {
  //clear cookie token
  res.clearCookie("token", { httpOnly: true });

  if (RES_FORMAT == "render") {
    return res.status(200).redirect("/login");
  }
  return res.status(200).json({ msg: "Redirecting to User Login Page" });
}

// #######################################
//   Login Controller - httpGetLoginPage
// #######################################

function httpGetLoginPage(req, res) {
  if (RES_FORMAT == "render") {
    return res
      .status(200)
      .render("pages/login", { title: "Login", errors: [] });
  }
  return res.status(200).json({ title: "Login" });
}

// ##############################################
//  Login Controller - verifyLoginCredentials
// ##############################################

async function verifyLoginCredentials(req, res) {
  //Handle validation errors
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    if (RES_FORMAT === "render") {
      return res.status(400).render("pages/login", { errors: errors.array() });
    }
    return res.status(400).json({ errors: errors.array() });
  }

  const { username, password } = req.body;
  let user = await dbCheckIfRecordExistsInTable(username, "users");

  //if the username is not in the database, return error
  if (_.isEmpty(user)) {
    if (RES_FORMAT === "render") {
      return res.status(401).render("pages/login", {
        errors: [
          {
            msg: "Invalid username or password!",
          },
        ],
      });
    }
    return res.status(401).json({
      errors: [
        {
          msg: "Invalid username or password!",
        },
      ],
    });
  }

  user = user[0];

  //if the user password does not match the database password, return error
  const match = await bcrypt.compare(password, user.password);
  if (!match) {
    if (RES_FORMAT === "render") {
      return res.status(401).render("pages/login", {
        errors: [
          {
            msg: "Invalid username or password!",
          },
        ],
      });
    }
    return res.status(401).json({
      errors: [
        {
          msg: "Invalid username or password!",
        },
      ],
    });
  }

  try {
    //set new passcode
    const newpasscode = randomstring.generate(6);
    const { id } = user;
    const dbresult = await dbUpdateUserPasscodeInDatabase(id, newpasscode);
    user.passcode = newpasscode;

    //clear cookie token
    res.clearCookie("token", { httpOnly: true });

    const payload = {
      user: {
        id: user.id,
        firstname: user.firstname,
        lastname: user.lastname,
        username: user.username,
        passcode: user.passcode,
        created: user.created,
        duration: user.duration,
        expiry: user.expiry,
        role: "user",
        access: false,
      },
    };

    //generate token with payload
    const token = await new Promise((resolve, reject) => {
      jwt.sign(
        payload,
        PRIVATE_KEY,
        {
          expiresIn: JWT_EXPIRY,
        },
        (err, token) => {
          if (err) {
            reject(err);
          }
          resolve(token);
        }
      );
    });

    res.cookie("token", token, {
      httpOnly: true,
      secure: JWT_HTTPS,
      maxAge: JWT_EXPIRY,
      // signed: true,
    });

    // console.log({ payload });

    //send email notification with passcode
    const transporter = nodemailer.createTransport({
      port: 465,
      host: "smtp.gmail.com",
      auth: {
        user: EMAIL_ADDRESS,
        pass: EMAIL_PASSWORD,
      },
      secure: true,
    });

    const mailData = {
      from: EMAIL_ADDRESS, // sender address
      to: username, // list of receivers
      subject: "Your Login Passcode",
      text: "Your Login Passcode",
      html: `<b>Hello ${user.firstname},</b>
              <br><br>
              This is your Login Passcode: <b>${user.passcode}</b>
              <br/><br>
              Regards,
              <br>
              <b>Avgee Limited</b>
              `,
    };

    return transporter.sendMail(mailData, function (err, info) {
      if (err) {
        console.log(err);
      } else {
        if (RES_FORMAT == "render") {
          return res.status(200).render("pages/loginPasscode", { errors: [] });
        }
        return res.status(200).json({
          msg: "User passcode sent successfully!",
          info,
        });
      }
    });
  } catch (err) {
    if (RES_FORMAT == "render") {
      return res.status(500).render("pages/login", {
        errors: [{ msg: `Server Error...${err.message}` }],
      });
    }
    return res.status(500).json({
      errors: [{ msg: `Server Error...${err.message}` }],
    });
  }
}

// ###################################################
//  Login Controller - verifyLoginPasscodeCredentials
// ###################################################

async function verifyLoginPasscodeCredentials(req, res) {
  //Handle validation errors
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    if (RES_FORMAT == "render") {
      return res
        .status(400)
        .render("pages/loginPasscode", { errors: errors.array() });
    }
    return res.status(400).json({ errors: errors.array() });
  }

  //verify token
  const cookie_token = req.cookies["token"];
  let user = jwt.verify(cookie_token, PRIVATE_KEY);

  //Get passcode from body
  const { passcode } = req.body;

  //check if token user is valid
  if (!cookie_token || !user) {
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("pages/login");
    }
    return res
      .status(401)
      .json({ msg: "Incorrect Token, User redirected to Login Page..." });
  }

  user = user.user;

  if (passcode !== user.passcode) {
    if (RES_FORMAT == "render") {
      return res.status(401).render("pages/loginPasscode", {
        errors: [{ msg: "Sorry passcode is incorrect! Try Again!" }],
      });
    }
    return res.status(401).json({
      msg: "Sorry passcode is incorrect! Try Again!",
    });
  }

  //clear cookie token
  res.clearCookie("token", { httpOnly: true });

  user.access = true;
  const payload = { user };

  //generate token with payload
  const token = await new Promise((resolve, reject) => {
    jwt.sign(
      payload,
      PRIVATE_KEY,
      {
        expiresIn: JWT_EXPIRY,
      },
      (err, token) => {
        if (err) {
          reject(err);
        }
        resolve(token);
      }
    );
  });

  res.cookie("token", token, {
    httpOnly: true,
    secure: JWT_HTTPS,
    maxAge: JWT_EXPIRY,
    // signed: true,
  });

  // console.log({ payload });

  if (RES_FORMAT == "render") {
    return res.status(200).redirect("/");
  }
  return res.status(200).json({ msg: "Redirect to Home Page.." });
}

// #######################################
//  Admin Controller - httpGetAdminPage
// #######################################

function httpGetAdminPage(req, res) {
  if (RES_FORMAT == "render") {
    return res.status(200).render("pages/admin", { errors: [], msg: "" });
  }
  return res.status(200).json({});
}

// #######################################
//  Admin Controller - verifyAdminCredentials
// #######################################

async function verifyAdminCredentials(req, res) {
  //Handle validation errors
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    if (RES_FORMAT == "render") {
      return res.status(400).render("pages/admin", { errors: errors.array() });
    }
    return res.status(400).json({ errors: errors.array() });
  }

  //Get username and password from body
  const { username, password } = req.body;

  let user = await dbCheckIfRecordExistsInTable(username, "admins");

  //if the username is not in the database, return error
  if (_.isEmpty(user)) {
    if (RES_FORMAT === "render") {
      return res.status(401).render("pages/admin", {
        errors: [
          {
            msg: "Invalid username or password!",
          },
        ],
      });
    }
    return res.status(401).json({
      errors: [
        {
          msg: "Invalid username or password!",
        },
      ],
    });
  }

  user = user[0];

  //if the user password does not match the database password, return error
  // const match = await bcrypt.compare(password, user.password);
  if (user.password !== password) {
    if (RES_FORMAT === "render") {
      return res.status(401).render("pages/admin", {
        errors: [
          {
            msg: "Invalid username or password!",
          },
        ],
      });
    }
    return res.status(401).json({
      errors: [
        {
          msg: "Invalid username or password!",
        },
      ],
    });
  }

  try {
    //clear cookie token
    res.clearCookie("admintoken", { httpOnly: true });

    const payload = {
      user: {
        id: user.id,
        firstname: user.firstname,
        lastname: user.lastname,
        username: user.username,
        role: "admin",
        access: true,
      },
    };

    //generate token with payload
    const admintoken = await new Promise((resolve, reject) => {
      jwt.sign(
        payload,
        PRIVATE_KEY,
        {
          expiresIn: JWT_EXPIRY,
        },
        (err, token) => {
          if (err) {
            reject(err);
          }
          resolve(token);
        }
      );
    });

    res.cookie("admintoken", admintoken, {
      httpOnly: true,
      secure: JWT_HTTPS,
      maxAge: JWT_EXPIRY,
      // signed: true,
    });

    // console.log({ payload });

    if (RES_FORMAT == "render") {
      return res.status(200).redirect("/dashboard");
    }
    return res.status(200).json({
      msg: `Redirecting to Dashboard Page...`,
    });
  } catch (err) {
    if (RES_FORMAT == "render") {
      return res.status(500).render("pages/admin", {
        errors: [{ msg: `Server Error...${err.message}` }],
      });
    }
    return res.status(500).json({
      errors: [{ msg: `Server Error...${err.message}` }],
    });
  }
}

// #######################################
//  Admin Controller - httpGetDashboardPage
// #######################################

function httpGetDashboardPage(req, res) {
  if (RES_FORMAT == "render") {
    return res.status(200).render("pages/dashboard", { errors: [], msg: "" });
  }
  return res.status(200).json({ title: "Dashboard Page" });
}

// #######################################
//  Admin Controller - httpGetUserListPage
// #######################################

async function httpGetUserListPage(req, res) {
  const result = await dbGetTableRecordsfromDatabase("users");
  let count = 0;
  result.forEach((prev) => {
    prev["created"] = new Date(+prev["created"]);
    prev["expiry"] = new Date(+prev["expiry"]);
    count++;
    prev["count"] = count;
  });

  // res.json({ result });

  if (RES_FORMAT == "render") {
    return res.status(200).render("pages/dashboarduserlist", {
      title: "AvGEE Admin",
      result,
    });
  }
  return res.status(200).json({ title: "User List Page" });
}

// #######################################
//  Admin Controller - httpGetVideoListPage
// #######################################

async function httpGetUserListPage(req, res) {
  const result = await dbGetTableRecordsfromDatabase("users");
  let count = 0;
  result.forEach((prev) => {
    prev["created"] = new Date(+prev["created"]);
    prev["expiry"] = new Date(+prev["expiry"]);
    count++;
    prev["count"] = count;
  });

  if (RES_FORMAT == "render") {
    return res.status(200).render("pages/dashboarduserlist", {
      title: "AvGEE Admin",
      result,
    });
  }
  return res.status(200).json({ title: "User List Page" });
}

// #######################################
//  Admin Controller - httpGetVideoListPage
// #######################################

async function httpGetVideoListPage(req, res) {
  const result = await dbGetTableRecordsfromDatabase("videos");
  let count = 0;
  result.forEach((prev) => {
    count++;
    prev["count"] = count;
  });

  if (RES_FORMAT == "render") {
    return res.status(200).render("pages/dashboardvideolist", {
      result,
    });
  }
  return res.status(200).json({ title: "Video List Page" });
}

// #######################################
//  Admin Controller - httpGetUpdateDBPage
// #######################################

async function httpGetUpdateDBPage(req, res) {
  if (RES_FORMAT == "render") {
    return res.status(200).render("pages/dashboarddbupdate", {
      errors: [],
      msg: "",
    });
  }
  return res.status(200).json({ title: "Update DB Page" });
}

// #######################################
//  Admin Controller - httpPostVideosToDB
// #######################################

async function httpPostVideosToDB(req, res) {
  fs.readdir(VIDEO_FOLDER, (err, files) => {
    try {
      //read the folder to get video filenames
      const { allVideoFileNames, allVideoFilesNos } =
        getVideoFileNamesFromFolder(files);

      //Empty DB Table
      dbEmptyDatabaseTable("videos");

      //Populate DB Table with all filenames
      dbPopulateDatabasetableWithFilenames({
        allVideoFileNames,
        allVideoFilesNos,
      });

      if (RES_FORMAT == "render") {
        return res.status(200).render("pages/dashboarddbupdate", {
          errors: [],
          msg: "Update on Video details was successful.",
        });
      }
      return res.status(200).json({ msg: "Videos added to DB..." });
    } catch (err) {
      console.log(err);
      if (RES_FORMAT == "render") {
        return res.status(400).render("pages/dashboarddbupdate", {
          errors: [{ msg: "Error Updating videos data in database..." }],
          msg: "",
        });
      }
      return res.status(400).json({
        errors: [{ msg: "Error Updating videos data in database..." }],
      });
    }
  });
}

// ##############################################
//  Admin Controller - httpGetUserCreatePage
// ##############################################

function httpGetUserCreatePage(req, res) {
  if (RES_FORMAT == "render") {
    return res
      .status(200)
      .render("pages/dashboardusercreate", { errors: [], msg: "", data: {} });
  }
  return res.status(200).json({ title: "User Create Page" });
}

// #######################################
//   Admin Controller - httpCreateUser
// #######################################

async function httpCreateUser(req, res) {
  let {
    firstname,
    lastname,
    username,
    password,
    durationnum,
    durationperiod,
    status,
  } = req.body;

  //Handle validation errors
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    if (RES_FORMAT == "render") {
      return res.status(400).render("pages/dashboardusercreate", {
        errors: errors.array(),
        msg: "",
        data: {
          firstname,
          lastname,
          username,
          password,
          durationnum,
          durationperiod,
          status,
        },
      });
    }
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    firstname = _.startCase(_.toLower(firstname));
    lastname = _.startCase(_.toLower(lastname));
    username = _.toLower(username);

    const ipaddress = req.ip;
    let created = new Date().getTime();
    if (Number(durationnum) != durationnum) {
      return res
        .status(400)
        .json({ errors: [{ msg: "Enter only number values for duration." }] });
    }

    let durationRealTime;
    switch (durationperiod) {
      case "s":
        durationRealTime = durationnum * 1000;
        break;
      case "m":
        durationRealTime = durationnum * 60 * 1000;
        break;
      case "h":
        durationRealTime = durationnum * 60 * 60 * 1000;
        break;
      case "d":
        durationRealTime = durationnum * 60 * 60 * 24 * 1000;
        break;
      case "w":
        durationRealTime = durationnum * 60 * 60 * 24 * 7 * 1000;
        break;
      case "w":
        durationRealTime = durationnum * 60 * 60 * 24 * 7 * 1000;
        break;
      case "mo":
        durationRealTime = durationnum * 60 * 60 * 24 * 7 * 30 * 1000;
        break;
      default:
        durationRealTime = durationnum * 60 * 60 * 24 * 1000;
    }
    let expiry = new Date(created + durationRealTime).getTime();
    const duration = `${durationnum}${durationperiod}`;

    //encrypt(hash) password
    const salt = await bcrypt.genSalt(10);
    const hash = await bcrypt.hash(password, salt);
    const passwordhash = hash;
    const passcode = "000000";
    // const passcode = randomstring.generate(6);

    //Insert user into Database
    const data = {
      firstname,
      lastname,
      username,
      passwordhash,
      passcode,
      ipaddress,
      created,
      duration,
      expiry,
      status,
    };
    const dbresult = await dbUpdateOnDuplicateUserRecordsInDatabase(data);

    if (status === "ON") {
      //send Email notification
      // create reusable transporter object using the default SMTP transport
      const transporter = nodemailer.createTransport({
        port: 465, // true for 465, false for other ports
        host: "smtp.gmail.com",
        auth: {
          user: EMAIL_ADDRESS,
          pass: EMAIL_PASSWORD,
        },
        secure: true,
      });

      const mailData = {
        from: EMAIL_ADDRESS, // sender address
        to: username, // list of receivers
        subject: "Your Login Details",
        text: "Your Login Details",
        html: `<b>Hello ${firstname},</b>
           <br><br>
           This is your Login Username: <b>${username}</b>
           <br>
           This is your Login Password: <b>${password}</b>
           <br/><br>
           Regards,
           <br>
           <b>Avgee Limited</b>
           `,
      };

      return transporter.sendMail(mailData, function (err, info) {
        if (err) {
          console.log(err);
        } else {
          console.log(info);
          if (RES_FORMAT == "render") {
            return res.status(201).render("pages/dashboardusercreate", {
              msg: "User created successfully",
              errors: [],
              data: "",
            });
          }
          return res.status(201).json({ msg: "User created successfully" });
        }
      });
    }
    if (RES_FORMAT == "render") {
      return res.status(201).render("pages/dashboardusercreate", {
        msg: "User created successfully",
        errors: [],
        data: "",
      });
    }
    return res.status(201).json({ msg: "User created successfully" });
  } catch (err) {
    console.error(err);
    return res
      .status(500)
      .json({ errors: `Error creating user...${err.message}` });
  }
}

// #######################################
//  Admin Controller - httpGetAdminLogout
// #######################################

async function httpGetAdminLogout(req, res) {
  //clear cookie token
  res.clearCookie("admintoken", { httpOnly: true });

  if (RES_FORMAT == "render") {
    return res.status(200).redirect("/admin");
  }
  return res.status(200).json({ msg: "Redirecting to Admin Login Page" });
}

module.exports = {
  httpPostVideosToDB,
  httpGetHomePage,
  httpPostHomePage,
  httpGetLoginPage,
  verifyLoginCredentials,
  verifyLoginPasscodeCredentials,
  httpGetVideoStreamingPage,
  httpGetVideoPlayer,
  httpGetAdminPage,
  verifyAdminCredentials,
  httpGetDashboardPage,
  httpCreateUser,
  httpGetUserListPage,
  httpGetVideoListPage,
  httpGetUserCreatePage,
  httpGetUpdateDBPage,
  httpGetAdminLogout,
  httpGetUserLogout,
};
