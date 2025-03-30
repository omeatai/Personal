# USING MYSQL WITH NODE.JS - TRAVESY MEDIA

## [COURSE]()

<details>
  <summary>1. Introduction </summary>

# Initialize npm

```jsbs
npm init -y
```

# Install mysql and express

```jsbs
npm install --save mysql express
```

# Install nodemon

```jsbs
npm install nodemon --save-dev
```

### x-mysqlnode-project/package.json:

```js
{
  "name": "x-mysqlnode-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "nodemon app.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2",
    "mysql": "^2.18.1"
  },
  "devDependencies": {
    "nodemon": "^2.0.22"
  }
}
```

### x-mysqlnode-project/app.js:

```js
const express = require("express");
const mysql = require("mysql");

const app = express();

app.listen("3000", () => {
  console.log("Server started on port 3000");
});
```

# run server:

```jsbs
npm run dev
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/3452f90e-b4c2-429f-9dca-a94f1067881d)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/a25db0be-6c5f-4561-a832-ca9107cd392d)

</details>

<details>
  <summary>2. Connect to MySQL Server </summary>

# Connect to MySQL Server

### x-mysqlnode-project/app.js:

```js
const express = require("express");
const mysql = require("mysql");

const app = express();

// create connection
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  //   database: "nodemysql",
});

// Connect
db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log("MySql Connected...");
});

// query db
db.query("SELECT 1 + 1 AS solution", function (error, results, fields) {
  if (error) {
    throw error;
  }
  console.log(results);
  console.log("The solution is: ", results[0].solution);
});

//close connection
db.end();

app.listen("3000", () => {
  console.log("Server started on port 3000");
});
```

# output:

```js
// MacBook-Air x-mysqlnode-project % npm run dev

// > x-mysqlnode-project@1.0.0 dev
// > nodemon app.js

// [nodemon] 2.0.22
// [nodemon] to restart at any time, enter `rs`
// [nodemon] watching path(s): *.*
// [nodemon] watching extensions: js,mjs,json
// [nodemon] starting `node app.js`
// Server started on port 3000
// MySql Connected...
// [ RowDataPacket { solution: 2 } ]
// The solution is:  2
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/c924fab0-f998-47e7-b707-cbf9bd12476c)

</details>

<details>
  <summary>3. Create Database </summary>

# Create Database

### x-mysqlnode-project/app.js:

```jsbs
// Create DB
app.get("/createdb", (req, res) => {
  let sql = "CREATE DATABASE IF NOT EXISTS nodemysql";
  db.query(sql, (err, result) => {
    if (err) {
      return res.json({ err });
    }
    res.json({ result, message: "Database created..." });
  });
});
```

```js
const express = require("express");
const mysql = require("mysql");

const app = express();

// create connection
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  //   database: "nodemysql",
});

// Connect
db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log("MySql Connected...");
});

// Create DB
app.get("/createdb", (req, res) => {
  let sql = "CREATE DATABASE IF NOT EXISTS nodemysql";
  db.query(sql, (err, result) => {
    if (err) {
      return res.json({ err });
    }
    res.json({ result, message: "Database created..." });
  });
});

// query db
// db.query("SELECT 1 + 1 AS solution", function (error, results, fields) {
//   if (error) {
//     throw error;
//   }
//   console.log(results);
//   console.log("The solution is: ", results[0].solution);
// });

//close connection
// db.end();

app.listen("3000", () => {
  console.log("Server started on port 3000");
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/b94d00a0-27b4-4750-92d3-35988450e088)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/4b2060c8-0933-4bf4-b85d-b73a79925ed7)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2b44638a-3054-49ff-9063-0d1132b75f99)

</details>

<details>
  <summary>4. Create Posts Table </summary>

# Create Posts Table

### x-mysqlnode-project/app.js:

```jsbs
// Create table
app.get("/createpoststable", (req, res) => {
  let sql =
    "CREATE TABLE posts(id int AUTO_INCREMENT, title VARCHAR(255), body VARCHAR(255), PRIMARY KEY(id) )";
  db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Posts table created..." });
  });
});
```

```js
const express = require("express");
const mysql = require("mysql");

const app = express();

// create connection
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "nodemysql",
});

// Connect
db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log("MySql Connected...");
});

// Create table
app.get("/createpoststable", (req, res) => {
  let sql =
    "CREATE TABLE posts(id int AUTO_INCREMENT, title VARCHAR(255), body VARCHAR(255), PRIMARY KEY(id) )";
  db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Posts table created..." });
  });
});

//Create DB
// app.get("/createdb", (req, res) => {
//   let sql = "CREATE DATABASE IF NOT EXISTS nodemysql";
//   db.query(sql, (err, result) => {
//     if (err) {
//       return res.json({ err });
//     }
//     res.json({ result, message: "Database created..." });
//   });
// });

// query db
// db.query("SELECT 1 + 1 AS solution", function (error, results, fields) {
//   if (error) {
//     throw error;
//   }
//   console.log(results);
//   console.log("The solution is: ", results[0].solution);
// });

//close connection
// db.end();

app.listen("3000", () => {
  console.log("Server started on port 3000");
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/755134fb-c519-4dfb-80bc-60ece1937b7e)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/f5cbfdb7-4e96-4cc2-b0b6-635d268ed2be)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/55b403a2-e731-49cc-b217-ba6c9a16eaa6)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/bf53f287-08e1-4c88-aed4-f2f858a9e89e)

</details>

<details>
  <summary>5. Create Post record </summary>

# Create Post record

### x-mysqlnode-project/app.js:

```jsbs
// Insert post
app.get("/addpost", (req, res) => {
  let post = { title: "Post One", body: "This is post number one" };
  let sql = "INSERT INTO posts SET ?";
  let query = db.query(sql, post, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post added..." });
  });
});
```

```js
const express = require("express");
const mysql = require("mysql");

const app = express();

// create connection
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "nodemysql",
});

// Connect
db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log("MySql Connected...");
});

// Insert post
app.get("/addpost", (req, res) => {
  let post = { title: "Post One", body: "This is post number one" };
  let sql = "INSERT INTO posts SET ?";
  let query = db.query(sql, post, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post added..." });
  });
});

// Create table
// app.get("/createpoststable", (req, res) => {
//   let sql =
//     "CREATE TABLE posts(id int AUTO_INCREMENT, title VARCHAR(255), body VARCHAR(255), PRIMARY KEY(id) )";
//   db.query(sql, (err, result) => {
//     if (err) {
//       throw err;
//     }
//     res.json({ result, message: "Posts table created..." });
//   });
// });

// Create DB
// app.get("/createdb", (req, res) => {
//   let sql = "CREATE DATABASE IF NOT EXISTS nodemysql";
//   db.query(sql, (err, result) => {
//     if (err) {
//       return res.json({ err });
//     }
//     res.json({ result, message: "Database created..." });
//   });
// });

// query db
// db.query("SELECT 1 + 1 AS solution", function (error, results, fields) {
//   if (error) {
//     throw error;
//   }
//   console.log(results);
//   console.log("The solution is: ", results[0].solution);
// });

//close connection
// db.end();

app.listen("3000", () => {
  console.log("Server started on port 3000");
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/0da8f426-2b6a-4dcc-a82e-ef832c72571a)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b34a297c-1b4c-4b2c-b450-5cd429633ea8)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/e39f3edd-ec09-42a2-b827-9b55a53bd7ab)

</details>

<details>
  <summary>6. Fetch Posts records </summary>

# Fetch posts Table records

### x-mysqlnode-project/app.js:

```jsbs
//Select post
app.get("/getposts", (req, res) => {
  let sql = "SELECT * FROM posts";
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post fetched..." });
  });
});

app.listen("3000", () => {
  console.log("Server started on port 3000");
});
```

```js
const express = require("express");
const mysql = require("mysql");

const app = express();

// create connection
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "nodemysql",
});

// Connect
db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log("MySql Connected...");
});

//Select post
app.get("/getposts", (req, res) => {
  let sql = "SELECT * FROM posts";
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post fetched..." });
  });
});

app.listen("3000", () => {
  console.log("Server started on port 3000");
});

// Insert post
app.get("/addpost", (req, res) => {
  let post = { title: "Post Two", body: "This is post number two" };
  let sql = "INSERT INTO posts SET ?";
  let query = db.query(sql, post, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post added..." });
  });
});

// Create table
// app.get("/createpoststable", (req, res) => {
//   let sql =
//     "CREATE TABLE posts(id int AUTO_INCREMENT, title VARCHAR(255), body VARCHAR(255), PRIMARY KEY(id) )";
//   db.query(sql, (err, result) => {
//     if (err) {
//       throw err;
//     }
//     res.json({ result, message: "Posts table created..." });
//   });
// });

// Create DB
// app.get("/createdb", (req, res) => {
//   let sql = "CREATE DATABASE IF NOT EXISTS nodemysql";
//   db.query(sql, (err, result) => {
//     if (err) {
//       return res.json({ err });
//     }
//     res.json({ result, message: "Database created..." });
//   });
// });

// query db
// db.query("SELECT 1 + 1 AS solution", function (error, results, fields) {
//   if (error) {
//     throw error;
//   }
//   console.log(results);
//   console.log("The solution is: ", results[0].solution);
// });

//close connection
// db.end();
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/3e7f9d7e-7d22-450e-8d92-824b87ec0e1b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/e374f27e-dc1f-468b-b4b4-c7898a12522f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/a99db33c-b956-4fa2-9927-69b398cb8a16)

</details>

<details>
  <summary>7. Fetch a Post record </summary>

# Fetch a Post record

### x-mysqlnode-project/app.js:

```jsbs
//Select a post
app.get("/getpost/:id", (req, res) => {
  const { id } = req.params;
  let sql = `SELECT * FROM posts WHERE id = ${id}`;
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post fetched..." });
  });
});
```

```js
const express = require("express");
const mysql = require("mysql");

const app = express();

// create connection
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "nodemysql",
});

// Connect
db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log("MySql Connected...");
});

//Select a post
app.get("/getpost/:id", (req, res) => {
  const { id } = req.params;
  let sql = `SELECT * FROM posts WHERE id = ${id}`;
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post fetched..." });
  });
});

//Select posts
app.get("/getposts", (req, res) => {
  let sql = "SELECT * FROM posts";
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post fetched..." });
  });
});

app.listen("3000", () => {
  console.log("Server started on port 3000");
});

//Insert post
app.get("/addpost", (req, res) => {
  let post = { title: "Post Two", body: "This is post number two" };
  let sql = "INSERT INTO posts SET ?";
  let query = db.query(sql, post, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post added..." });
  });
});

// Create table
// app.get("/createpoststable", (req, res) => {
//   let sql =
//     "CREATE TABLE posts(id int AUTO_INCREMENT, title VARCHAR(255), body VARCHAR(255), PRIMARY KEY(id) )";
//   db.query(sql, (err, result) => {
//     if (err) {
//       throw err;
//     }
//     res.json({ result, message: "Posts table created..." });
//   });
// });

// Create DB
// app.get("/createdb", (req, res) => {
//   let sql = "CREATE DATABASE IF NOT EXISTS nodemysql";
//   db.query(sql, (err, result) => {
//     if (err) {
//       return res.json({ err });
//     }
//     res.json({ result, message: "Database created..." });
//   });
// });

// query db
// db.query("SELECT 1 + 1 AS solution", function (error, results, fields) {
//   if (error) {
//     throw error;
//   }
//   console.log(results);
//   console.log("The solution is: ", results[0].solution);
// });

//close connection
// db.end();
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/1399341f-0338-4348-adcb-e1acfee68e18)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/f34de5c0-6991-4894-9574-458e19c9a26a)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/cd557320-980e-45c2-bb37-01d02600c627)

</details>

<details>
  <summary>8. Update a Post record </summary>

# Update a Post record

### x-mysqlnode-project/app.js:

```jsbs
//Update a post
app.get("/updatepost/:id", (req, res) => {
  const { id } = req.params;
  const newTitle = "Updated Title";
  let sql = `UPDATE posts SET title = "${newTitle}" WHERE id = ${id}`;
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post updated..." });
  });
});

```

```js
const express = require("express");
const mysql = require("mysql");

const app = express();

// create connection
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "nodemysql",
});

// Connect
db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log("MySql Connected...");
});

//Update a post
app.get("/updatepost/:id", (req, res) => {
  const { id } = req.params;
  const newTitle = "Updated Title";
  let sql = `UPDATE posts SET title = "${newTitle}" WHERE id = ${id}`;
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post updated..." });
  });
});

//Select a post
app.get("/getpost/:id", (req, res) => {
  const { id } = req.params;
  let sql = `SELECT * FROM posts WHERE id = ${id}`;
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post fetched..." });
  });
});

//Select posts
app.get("/getposts", (req, res) => {
  let sql = "SELECT * FROM posts";
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post fetched..." });
  });
});

app.listen("3000", () => {
  console.log("Server started on port 3000");
});

//Insert post
app.get("/addpost", (req, res) => {
  let post = { title: "Post Two", body: "This is post number two" };
  let sql = "INSERT INTO posts SET ?";
  let query = db.query(sql, post, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post added..." });
  });
});

// Create table
// app.get("/createpoststable", (req, res) => {
//   let sql =
//     "CREATE TABLE posts(id int AUTO_INCREMENT, title VARCHAR(255), body VARCHAR(255), PRIMARY KEY(id) )";
//   db.query(sql, (err, result) => {
//     if (err) {
//       throw err;
//     }
//     res.json({ result, message: "Posts table created..." });
//   });
// });

// Create DB
// app.get("/createdb", (req, res) => {
//   let sql = "CREATE DATABASE IF NOT EXISTS nodemysql";
//   db.query(sql, (err, result) => {
//     if (err) {
//       return res.json({ err });
//     }
//     res.json({ result, message: "Database created..." });
//   });
// });

// query db
// db.query("SELECT 1 + 1 AS solution", function (error, results, fields) {
//   if (error) {
//     throw error;
//   }
//   console.log(results);
//   console.log("The solution is: ", results[0].solution);
// });

//close connection
// db.end();
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/66c2c039-ab56-47f9-9bff-b6664fda66b1)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/04bcd2f3-b4c7-45d9-a8e0-b44bce57964d)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/23fcad68-18d1-4062-bde0-235fbffe8009)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/dbb2774b-6452-4a04-9378-22b0ac38468f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2af53b58-7945-418d-989f-3bc7ead4a80e)

</details>

<details>
  <summary>9. Delete a Post record </summary>

# Delete a Post record

### x-mysqlnode-project/app.js:

```jsbs
//Delete a post
app.get("/deletepost/:id", (req, res) => {
  const { id } = req.params;
  let sql = `DELETE FROM posts WHERE id = ${id}`;
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post deleted..." });
  });
});
```

```js
const express = require("express");
const mysql = require("mysql");

const app = express();

// create connection
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "nodemysql",
});

// Connect
db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log("MySql Connected...");
});

//Delete a post
app.get("/deletepost/:id", (req, res) => {
  const { id } = req.params;
  let sql = `DELETE FROM posts WHERE id = ${id}`;
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post deleted..." });
  });
});

//Update a post
app.get("/updatepost/:id", (req, res) => {
  const { id } = req.params;
  const newTitle = "Updated Title";
  let sql = `UPDATE posts SET title = "${newTitle}" WHERE id = ${id}`;
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post updated..." });
  });
});

//Select a post
app.get("/getpost/:id", (req, res) => {
  const { id } = req.params;
  let sql = `SELECT * FROM posts WHERE id = ${id}`;
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post fetched..." });
  });
});

//Select posts
app.get("/getposts", (req, res) => {
  let sql = "SELECT * FROM posts";
  let query = db.query(sql, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post fetched..." });
  });
});

app.listen("3000", () => {
  console.log("Server started on port 3000");
});

//Insert post
app.get("/addpost", (req, res) => {
  let post = { title: "Post Two", body: "This is post number two" };
  let sql = "INSERT INTO posts SET ?";
  let query = db.query(sql, post, (err, result) => {
    if (err) {
      throw err;
    }
    res.json({ result, message: "Post added..." });
  });
});

// Create table
// app.get("/createpoststable", (req, res) => {
//   let sql =
//     "CREATE TABLE posts(id int AUTO_INCREMENT, title VARCHAR(255), body VARCHAR(255), PRIMARY KEY(id) )";
//   db.query(sql, (err, result) => {
//     if (err) {
//       throw err;
//     }
//     res.json({ result, message: "Posts table created..." });
//   });
// });

// Create DB
// app.get("/createdb", (req, res) => {
//   let sql = "CREATE DATABASE IF NOT EXISTS nodemysql";
//   db.query(sql, (err, result) => {
//     if (err) {
//       return res.json({ err });
//     }
//     res.json({ result, message: "Database created..." });
//   });
// });

// query db
// db.query("SELECT 1 + 1 AS solution", function (error, results, fields) {
//   if (error) {
//     throw error;
//   }
//   console.log(results);
//   console.log("The solution is: ", results[0].solution);
// });

//close connection
// db.end();
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/e1668b4e-2563-4823-b358-fa43d360c7a1)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/874d2f0d-9b88-4b27-b4a9-69819eb20bcc)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/bb047692-88ba-42e8-a014-cd22bb1fb03b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/66191d76-f327-4627-8061-6de6c4845d9b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/d310609f-dbca-4d31-b9c2-a6c5706e648e)

</details>

# # END
