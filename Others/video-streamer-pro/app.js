require("dotenv").config();
const path = require("path");
const express = require("express");
const cors = require("cors");
const morgan = require("morgan");
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
const session = require("express-session");
const { SESSION_SECRET } = require("./services/mysql/keys");

const apiv1 = require("./apis/apiv1");

const app = express();

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// parse application/json
app.use(bodyParser.json());
app.use(express.json({ extended: false }));
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.urlencoded({ extended: false }));

app.use(cookieParser());
app.use(cors({ origin: "http://localhost:3000" }));
app.use(morgan("short")); //combined | common | dev | short
app.use("/web", express.static(path.join(__dirname, "public")));
// app.set("trust proxy", 1); // trust first proxy
app.use(
  session({
    secret: SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    // store: redisStore,
    // cookie: {
    //   path: "/",
    //   httpOnly: true,
    //   secure: false,
    //   maxAge: 15 * 60 * 1000,
    // },
  })
);

app.use("/v1", apiv1);
app.use("/", apiv1);

///////

module.exports = app;
