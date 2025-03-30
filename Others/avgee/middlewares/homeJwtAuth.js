const jwt = require("jsonwebtoken");
const {
  PRIVATE_KEY,
  JWT_EXPIRY,
  JWT_HTTPS,
  RES_FORMAT,
} = require("../services/mysql/keys");

//##################################
// homeJwtAuth Middleware
//##################################

module.exports = async function (req, res, next) {
  // console.log("HOME JWT AUTHENTICATION");

  //get token from cookies
  const { homeToken } = req.cookies;
  // console.log("tokenfromcookies: ", homeToken);

  //check if jwt token exists
  if (!homeToken) {
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("/login");
    }
    return res
      .status(401)
      .json({ msg: "Access Denied. No Token provided.", token });
  }

  // check if jwt token is valid
  try {
    const user = jwt.verify(homeToken, PRIVATE_KEY);
    // console.log("userfromtoken: ", user);

    if (!user) {
      //clear all cookie token
      res.clearCookie("loginToken", { httpOnly: true });
      res.clearCookie("homeToken", { httpOnly: true });

      if (RES_FORMAT == "render") {
        return res.status(401).redirect("/login");
      }
      return res.status(401).json({ msg: "Token is invalid or expired" });
    }

    const currentTime = new Date().getTime();
    // console.log("currentTime: ", currentTime);
    // console.log("userExpiryTime: ", user.user.expiry);
    // console.log(
    //   "User subscription has ended: ",
    //   currentTime > user.user.expiry
    // );

    if (currentTime > user.user.expiry) {
      if (RES_FORMAT == "render") {
        return res.status(403).render("pages/login", {
          errors: [
            { msg: "User Subscription has expired. Please contact Admin." },
          ],
          msg: "",
        });
      }
      return res.status(403).json({ msg: "User Subscription has expired." });
    }

    //create a new token
    const payload = { user: user.user };
    // console.log("payloadfornewtoken: ", payload);

    //clear all cookie token
    res.clearCookie("loginToken", { httpOnly: true });
    res.clearCookie("homeToken", { httpOnly: true });

    //generate newtoken with payload
    const newtoken = await new Promise((resolve, reject) => {
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
    // console.log("newtoken: ", newtoken);

    res.cookie("homeToken", newtoken, {
      httpOnly: true,
      secure: JWT_HTTPS,
      maxAge: JWT_EXPIRY,
    });

    req.user = user.user;
    // console.log("req.user: ", req.user);

    next();
  } catch (err) {
    //clear all cookie token
    res.clearCookie("loginToken", { httpOnly: true });
    res.clearCookie("homeToken", { httpOnly: true });
    //console.log(err.message);
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("/login");
    }
    return res
      .status(401)
      .json({ msg: "Token is invalid or expired", error: err.message });
  }
};
