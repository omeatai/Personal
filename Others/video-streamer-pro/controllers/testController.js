const testDB = require("../models/Test");

// #######################################
//         httpGetTestDatabase
// #######################################

async function httpGetTestDatabase(req, res) {
  const result = await testDB();
  console.log(result);
  res.send(result);
}

module.exports = {
  httpGetTestDatabase,
};
