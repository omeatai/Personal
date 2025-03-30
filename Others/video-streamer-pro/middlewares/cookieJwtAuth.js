const jwt = require("jsonwebtoken");
const {
  PRIVATE_KEY,
  JWT_EXPIRY,
  JWT_HTTPS,
  RES_FORMAT,
} = require("../services/mysql/keys");

//##################################
// cookieJwtAuth Middleware
//##################################

module.exports = async function (req, res, next) {
  //get token from cookies
  const { token } = req.cookies;

  //check if jwt token exists
  if (!token) {
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("/login");
    }
    return res
      .status(401)
      .json({ msg: "Access Denied. No Token provided.", token });
  }

  // check if jwt token is valid
  try {
    const user = jwt.verify(token, PRIVATE_KEY);

    if (!user || user.user.access === "false") {
      res.clearCookie("token", { httpOnly: true });
      if (RES_FORMAT == "render") {
        return res.status(401).redirect("/login");
      }
      return res.status(401).json({ msg: "Token is invalid or expired" });
    }

    const currentTime = new Date().getTime();
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

    res.clearCookie("token", { httpOnly: true });

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

    res.cookie("token", newtoken, {
      httpOnly: true,
      secure: JWT_HTTPS,
      maxAge: JWT_EXPIRY,
      // signed: true,
    });

    req.user = user.user;
    next();
  } catch (err) {
    res.clearCookie("token", { httpOnly: true });
    console.log(err.message);
    if (RES_FORMAT == "render") {
      return res.status(401).redirect("/login");
    }
    return res
      .status(401)
      .json({ msg: "Token is invalid or expired", error: err.message });
  }
};
