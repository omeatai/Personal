const jwt = require("jsonwebtoken");
const { PRIVATE_KEY, RES_FORMAT } = require("../services/mysql/keys");

//##################################
// loginJwtAuth Middleware
//##################################

module.exports = function (req, res, next) {
  // console.log("LOGIN JWT AUTHENTICATION");

  const { loginToken } = req.cookies;
  // console.log("loginTokenfromcookies: ", loginToken);

  if (!loginToken) {
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("/login");
    }
    return res.status(401).json({ msg: "Access Denied. No Token provided." });
  }

  try {
    const user = jwt.verify(loginToken, PRIVATE_KEY);
    req.user = user;
    // console.log("req.user: ", user);
    next();
  } catch (err) {
    res.clearCookie("loginToken", { httpOnly: true });
    //console.log(err.message);
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("/login");
    }
    return res.status(401).json({ msg: "Token is invalid or expired" });
  }
};
