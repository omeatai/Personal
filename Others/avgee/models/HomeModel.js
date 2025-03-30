const { db } = require("../services/mysql/db");

// #####################################################
//         dbCheckIfRecordExistsInTable
// #####################################################

async function dbCheckIfRecordExistsInTable(username, table) {
  let sql = `SELECT * FROM ${table} WHERE username = "${username}"`;
  return await new Promise((resolve, reject) => {
    db.query(sql, (err, result) => {
      if (err) {
        reject(new Error(err));
      }
      resolve(result);
    });
  });
}

// #####################################################
//         dbUpdateUserPasscodeInDatabase
// #####################################################

async function dbUpdateUserPasscodeInDatabase(id, newPasscode) {
  let sql = `UPDATE users SET passcode = "${newPasscode}" WHERE id = ${id}`;
  return await new Promise((resolve, reject) => {
    db.query(sql, (err, result) => {
      if (err) {
        reject(new Error(err));
      }
      resolve(result);
    });
  });
}

// #######################################
//         getPagination
// #######################################

async function getPagination(req, res, next) {
  //read filenames from DB
  let sql = "SELECT * FROM videos";
  const result = await new Promise((resolve, reject) => {
    db.query(sql, (err, result) => {
      if (err) {
        reject(new Error(err));
      }
      // console.log(result);
      resolve(result);
    });
  });

  //How many posts we want show on each page
  const resultsPerPage = 6;

  const numberOfResults = result.length;
  const numberOfPages = Math.ceil(numberOfResults / resultsPerPage);
  let page = req.query.page ? Number(req.query.page) : 1;
  if (page > numberOfPages) {
    return res.redirect("/?page=" + encodeURIComponent(numberOfPages));
  } else if (page < 1) {
    return res.redirect("/?page=" + encodeURIComponent(1));
  }
  //Determine the SQL LIMIT starting number
  const startingLimit = (page - 1) * resultsPerPage;

  //Get the relevant number of POSTS for this starting page
  sql = `SELECT * FROM videos LIMIT ${startingLimit},${resultsPerPage}`;
  const queryResult = await new Promise((resolve, reject) => {
    db.query(sql, (err, result) => {
      if (err) {
        reject(new Error(err));
      }
      let iterator = page - 5 < 1 ? 1 : page - 5;
      let endingLink =
        iterator + 9 <= numberOfPages
          ? iterator + 9
          : page + (numberOfPages - page);
      if (endingLink < page + 4) {
        iterator -= page + 4 - numberOfPages;
      }
      resolve({
        data: result,
        page,
        iterator,
        endingLink,
        numberOfPages,
      });
    });
  });
  // req.query["data"] = queryResult;
  req.data = queryResult;
  next();
}

// #######################################
//         getVideoFileNamesFromFolder
// #######################################

function getVideoFileNamesFromFolder(files) {
  let allVideoFileNames = []; //all filenames with extension
  let allVideoFilesNos = []; //all first 4 digits of filenames

  //read the video filenames from the folder
  files.forEach((file) => {
    allVideoFileNames.push(file);
    const num = file.slice(0, 3);
    allVideoFilesNos.push(num);
  });
  if (allVideoFileNames.includes(".DS_Store")) {
    const dsIndex = allVideoFileNames.indexOf(".DS_Store");
    allVideoFileNames.splice(dsIndex, 1);
    allVideoFilesNos.splice(dsIndex, 1);
  }

  return { allVideoFileNames, allVideoFilesNos };
}

// #######################################
//         dbEmptyDatabaseTable
// #######################################

function dbEmptyDatabaseTable(table) {
  let sql = `TRUNCATE TABLE ${table};`;
  db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
  });
}

// #####################################################
//         dbPopulateDatabasetableWithFilenames
// #####################################################

function dbPopulateDatabasetableWithFilenames(filenames) {
  for (let i = 0; i < filenames.allVideoFileNames.length; i++) {
    let record = {
      name: filenames.allVideoFileNames[i],
      digit: filenames.allVideoFilesNos[i],
    };
    let sql = "INSERT INTO videos SET ?";
    db.query(sql, record, (err, result) => {
      if (err) {
        throw err;
      }
    });
  }
}

// #####################################################
//         dbGetVideoFilenamesfromDatabase
// #####################################################

async function dbGetVideoFilenamesfromDatabase(table) {
  let sql = `SELECT * FROM ${table}`;
  return await new Promise((resolve, reject) => {
    db.query(sql, (err, result) => {
      if (err) {
        reject(new Error(err));
      }
      // console.log(result);
      resolve(result);
    });
  });
}

// #####################################################
//         dbGetTableRecordsfromDatabase
// #####################################################

async function dbGetTableRecordsfromDatabase(table) {
  let sql = `SELECT * FROM ${table}`;
  return await new Promise((resolve, reject) => {
    db.query(sql, (err, result) => {
      if (err) {
        reject(new Error(err));
      }
      // console.log(result);
      resolve(result);
    });
  });
}

// #####################################################
//         dbPostUserRecordsIntoDatabase
// #####################################################

async function dbPostUserRecordsIntoDatabase(record, table) {
  let sql = `INSERT INTO ${table} SET ?`;
  return await new Promise((resolve, reject) => {
    db.query(sql, record, (err, result) => {
      if (err) {
        reject(new Error(err));
      }
      resolve(result);
    });
  });
}

// #####################################################
//         dbUpdateOnDuplicateUserRecordsInDatabase
// #####################################################

async function dbUpdateOnDuplicateUserRecordsInDatabase(record) {
  const {
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
  } = record;
  let sql = `
  INSERT INTO users (firstname, lastname, username, password, passcode, ipaddress, created, duration, expiry, status)
  VALUES("${firstname}", "${lastname}", "${username}", "${passwordhash}", "${passcode}", "${ipaddress}", "${created}",
  "${duration}", "${expiry}", "${status}")
  ON DUPLICATE KEY UPDATE
  password="${passwordhash}",
  passcode="${passcode}",
  ipaddress="${ipaddress}",
  created="${created}",
  duration="${duration}",
  expiry="${expiry}",
  status="${status}"
  `;

  return await new Promise((resolve, reject) => {
    db.query(sql, (err, result) => {
      if (err) {
        reject(err);
      }
      resolve(result);
    });
  });
}

module.exports = {
  getPagination,
  getVideoFileNamesFromFolder,
  dbEmptyDatabaseTable,
  dbPopulateDatabasetableWithFilenames,
  dbGetVideoFilenamesfromDatabase,
  dbGetTableRecordsfromDatabase,
  dbCheckIfRecordExistsInTable,
  dbPostUserRecordsIntoDatabase,
  dbUpdateUserPasscodeInDatabase,
  dbUpdateOnDuplicateUserRecordsInDatabase,
};
