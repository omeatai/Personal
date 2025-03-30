const express = require("express");
const { check } = require("express-validator");
const auth = require("../middlewares/cookieJwtAuth");
const adminauth = require("../middlewares/adminCookieJwtAuth");
const loginauth = require("../middlewares/loginpasscodeMiddleware");
const { getPagination } = require("../models/HomeModel");
const videoStreamingController = require("../controllers/videoStreamingController");
const videoStreamingRouter = express.Router();

//#########################################
// Login Controller - Get Login Page
//#########################################

videoStreamingRouter.get("/login", videoStreamingController.httpGetLoginPage);

//###################################################
// Login Controller - Verify Login Credentials
//###################################################

const postLoginValidation = [
  check("username", "Email is required").not().isEmpty(),
  check("username", "Enter a valid email").isEmail(),
  check("password", "Password should have at least 4 characters").isLength({
    min: 4,
  }),
];

videoStreamingRouter.post(
  "/login",
  postLoginValidation,
  videoStreamingController.verifyLoginCredentials
);

//#####################################################
// Login Controller - Verify Login PasscodeCredentials
//#####################################################

const postLoginPasscodeValidation = [
  check("passcode", "Passcode should have at least 4 characters").isLength({
    min: 4,
  }),
];

videoStreamingRouter.post(
  "/loginpasscode",
  loginauth,
  postLoginPasscodeValidation,
  videoStreamingController.verifyLoginPasscodeCredentials
);

//##########################################
// Admin Controller - Get Admin Page
//##########################################

videoStreamingRouter.get("/admin", videoStreamingController.httpGetAdminPage);

//###################################################
// Admin Controller  - Verify Admin Credentials
//###################################################

const postAdminValidation = [
  check("username", "Username is required").not().isEmpty(),
  check("password", "Password should have at least 4 characters").isLength({
    min: 4,
  }),
];

videoStreamingRouter.post(
  "/admin",
  postAdminValidation,
  videoStreamingController.verifyAdminCredentials
);

//##########################################
// Admin Controller - Get Dashboard Page
//##########################################

videoStreamingRouter.get(
  "/dashboard",
  adminauth,
  videoStreamingController.httpGetDashboardPage
);

//##########################################
// Admin Controller - Get UserList Page
//##########################################

videoStreamingRouter.get(
  "/userlist",
  adminauth,
  videoStreamingController.httpGetUserListPage
);

//##########################################
// Admin Controller - Get VideoList Page
//##########################################

videoStreamingRouter.get(
  "/videolist",
  adminauth,
  videoStreamingController.httpGetVideoListPage
);

//##########################################
// Admin Controller - Get Create User Page
//##########################################

videoStreamingRouter.get(
  "/usercreate",
  adminauth,
  videoStreamingController.httpGetUserCreatePage
);

//######################################
// Admin Controller - Create User
//######################################

const postUserValidation = [
  check("firstname", "Firstname is required").not().isEmpty(),
  check("lastname", "Lastname is required").not().isEmpty(),
  check("username", "Email is required").not().isEmpty(),
  check("username", "Enter a valid email").isEmail(),
  check("password", "Password should have at least 4 characters").isLength({
    min: 4,
  }),
  check(
    "durationnum",
    "Duration should have at most 3 characters and at least 1 character"
  ).isLength({ max: 3, min: 1 }),
];

videoStreamingRouter.post(
  "/users",
  adminauth,
  postUserValidation,
  videoStreamingController.httpCreateUser
);

//##########################################
// Admin Controller - Get Update DB Page
//##########################################

videoStreamingRouter.get(
  "/updatedb",
  adminauth,
  videoStreamingController.httpGetUpdateDBPage
);

//##########################################
// Admin Controller - Insert into DB
//##########################################

videoStreamingRouter.post(
  "/videostodb",
  adminauth,
  videoStreamingController.httpPostVideosToDB
);

//##########################################
// Admin Controller - Admin Logout
//##########################################

videoStreamingRouter.get(
  "/adminlogout",
  adminauth,
  videoStreamingController.httpGetAdminLogout
);

//##########################################
// Home Controller - Video single streaming Page
//##########################################

videoStreamingRouter.get(
  "/video",
  auth,
  videoStreamingController.httpGetVideoStreamingPage
);

//##########################################
// Home Controller - Video Player
//##########################################

videoStreamingRouter.get(
  "/videoplayer",
  auth,
  videoStreamingController.httpGetVideoPlayer
);

//##########################################
// Home Controller - Search for videos
//##########################################

videoStreamingRouter.post("/", auth, videoStreamingController.httpPostHomePage);
// videoStreamingRouter.post("/", videoStreamingController.httpPostHomePage);

//##########################################
// Home Controller - User Logout
//##########################################

videoStreamingRouter.get(
  "/logout",
  auth,
  videoStreamingController.httpGetUserLogout
);

//##########################################
// Home Controller - Get all Videos
//##########################################

videoStreamingRouter.get(
  "/*",
  auth,
  getPagination,
  videoStreamingController.httpGetHomePage
);

module.exports = videoStreamingRouter;
