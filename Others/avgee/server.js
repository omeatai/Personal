//const https = require("https");
//const path = require('path');

const http = require("http");
const app = require("./app");
const dbmysql = require("./services/mysql/db");

//const PORT = process.env.PORT || 443;
const PORT = process.env.PORT || 8000;

const fs = require("fs");

// const https_options = {
// key: fs.readFileSync(path.join(__dirname, "..","..", "etc/ssl/avgeemasterclass.co.uk.key" )),
// cert: fs.readFileSync(path.join(__dirname, "..","..", "etc/ssl/avgeemasterclass.co.uk.crt")),
// }
//const server = https.createServer(https_options,app);

const server = http.createServer(app);

async function startServer() {
  //Connect to the DB
  await dbmysql.connectDB();

  server.listen(PORT, () => {
    console.log(`Server is listening on ${PORT}...`);
  });
}
//Start the server
startServer();
