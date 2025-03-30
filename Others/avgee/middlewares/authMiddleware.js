const jwt = require("jsonwebtoken");
const { PRIVATE_KEY } = require("../services/mysql/keys");

//######################
// Auth Middleware
//######################

module.exports = function (req, res, next) {
  //get the token from the header if present
  // const token = req.headers["x-access-token"] || req.headers["authorization"];
  const token = req.header("x-auth-token");

  if (!token) {
    return res.status(401).json({ msg: "Access Denied. No Token provided." });
  }

  try {
    //if can verify the token, set req.user and pass to next middleware
    const decoded = jwt.verify(token, PRIVATE_KEY);
    console.log(decoded);
    req.user = decoded.user;
    next();
  } catch (err) {
    //if invalid token
    console.error(err);
    res.status(401).json({ msg: `Invalid Token. ${err.message}` });
  }
};
