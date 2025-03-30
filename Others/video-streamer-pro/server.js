const http = require("http");
const app = require("./app");
const dbmysql = require("./services/mysql/db");
const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

async function startServer() {
  //Connect to the DB
  await dbmysql.connectDB();

  server.listen(PORT, () => {
    console.log(`Server is listening on ${PORT}...`);
  });
}

startServer();
