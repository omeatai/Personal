const { db } = require("../services/mysql/db");

function testDB() {
  let sql = "SELECT 1 + 1 AS solution";
  return new Promise((resolve, reject) => {
    db.query(sql, function (error, results, fields) {
      if (error) {
        console.error(error.message);
        reject(new Error(`Query Error. ${error}`));
      }
      resolve({ results, message: "Database ok" });
    });
  });
}

module.exports = testDB;

// Test Database
// function testDB(req, res, callback) {
//   let sql = "SELECT 1 + 1 AS solution";
//   db.query(sql, function (error, results, fields) {
//     if (error) {
//       throw error;
//     }
//     return callback({ results, message: "Database ok" });
//   });
// }

// testDB(req, res, function (result) {
//   res.send(result);
// });
