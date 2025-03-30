const express = require("express");

const testRouter = require("../routes/testRouter");
const videoStreamingRouter = require("../routes/videoStreamingRouter");

const apiv1 = express.Router();

apiv1.use("/test", testRouter);
apiv1.use("/", videoStreamingRouter);

module.exports = apiv1;
