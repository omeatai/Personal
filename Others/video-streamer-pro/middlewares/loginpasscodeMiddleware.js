const jwt = require("jsonwebtoken");
const { PRIVATE_KEY, RES_FORMAT } = require("../services/mysql/keys");

//##################################
// loginpasscode Middleware
//##################################

module.exports = function (req, res, next) {
  const { token } = req.cookies;
  if (!token) {
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("/login");
    }
    return res.status(401).json({ msg: "Access Denied. No Token provided." });
  }
  try {
    // The important part
    const user = jwt.verify(token, PRIVATE_KEY);
    req.user = user;
    next();
  } catch (err) {
    res.clearCookie("token", { httpOnly: true });
    console.log(err.message);
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("/login");
    }
    return res.status(401).json({ msg: "Token is invalid or expired" });
  }
};
