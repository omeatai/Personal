const jwt = require("jsonwebtoken");
const { PRIVATE_KEY, RES_FORMAT } = require("../services/mysql/keys");

//##################################
// adminCookieJwtAuth Middleware
//##################################

module.exports = async function (req, res, next) {
  //get token from cookies
  const { admintoken } = req.cookies;
  //check if jwt token exists
  if (!admintoken) {
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("/admin");
    }
    return res
      .status(401)
      .json({ msg: "Access Denied. No Token provided.", token });
  }

  // check if jwt token is valid
  try {
    const user = jwt.verify(admintoken, PRIVATE_KEY);

    if (!user || user.user.role !== "admin") {
      res.clearCookie("admintoken", { httpOnly: true });
      if (RES_FORMAT == "render") {
        return res.status(401).redirect("/admin");
      }
      return res.status(401).json({ msg: "Token is invalid or expired" });
    }

    req.user = user.user;
    next();
  } catch (err) {
    res.clearCookie("admintoken", { httpOnly: true });
    console.log(err.message);
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("/admin");
    }
    return res
      .status(401)
      .json({ msg: "Token is invalid or expired", error: err.message });
  }
};
