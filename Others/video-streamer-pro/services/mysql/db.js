const mysql = require("mysql");
const { DBNAME, HOST, USER, PASSWORD } = require("./keys");

// create connection
const db = mysql.createConnection({
  host: HOST,
  user: USER,
  password: PASSWORD,
  database: DBNAME,
});

// connect to database
async function connectDB() {
  db.connect((err) => {
    if (err) {
      console.error(err.message);
      throw err;
    }
    console.log("MySql DB is Connected...");
  });
}

// disconnect connection
async function disconnectDB() {
  db.end();
}

module.exports = {
  db,
  connectDB,
  disconnectDB,
};
