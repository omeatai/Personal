const express = require("express");

const videoStreamingRouter = require("../routes/videoStreamingRouter");

const apiv1 = express.Router();

apiv1.use("/", videoStreamingRouter);

module.exports = apiv1;
