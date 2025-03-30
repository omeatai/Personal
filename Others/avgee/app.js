require("dotenv").config();
const path = require("path");
const express = require("express");
const cors = require("cors");
// const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
//const enforce = require('express-sslify');
const apiv1 = require("./apis/apiv1");
const app = express();

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

//app.use(enforce.HTTPS());

// app.use(bodyParser.json());
app.use(express.json({ extended: false }));

// app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.urlencoded({ extended: false }));

app.use(cookieParser());

app.use(cors({ origin: "https://www.avgeemasterclass.co.uk" }));

app.use("/web", express.static(path.join(__dirname, "public")));

app.use("/", apiv1);

module.exports = app;
