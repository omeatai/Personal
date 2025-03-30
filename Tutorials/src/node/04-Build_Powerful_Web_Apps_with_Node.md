## +Linkedin-Build Powerful Web Apps with Node.js

## [COURSE](https://www.linkedin.com/learning/express-essentials-build-powerful-web-apps-with-node-js)

<details>
<summary>1. Check Node and npm version </summary>

# Check Node and npm version

```x
node -v
npm -v
```

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/fd768588-8a3e-4251-b35c-42a9963b381e">


# #END</details>

<details>
<summary>2. Using Express Application Generator to creact an Example Project </summary>

# Using Express Application Generator to creact an Example Project

## [https://expressjs.com/en/starter/generator.html](https://expressjs.com/en/starter/generator.html)

![image](https://github.com/user-attachments/assets/2e952a6c-be2a-4ce6-b136-e4b362e2c02a)

## Create Project Folder

```x
mkdir example_project
cd example_project
```

## Create Express App with Application Generator

```x
npx express-generator --git --view=hbs example_app
```

```x
npm install express-generator
express --git --view=hbs example_app
```

## Install dependencies

```x
cd example_app
npm install
```

## On MacOS or Linux, run the app with this command

```x
DEBUG=example_app:* npm start
```

## Create Script to Run App

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/example_project/example_app/package.json:

```json
{
  "name": "example-app",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "start": "node ./bin/www",
    "dev": "DEBUG=example_app:* npm start"
  },
  "dependencies": {
    "cookie-parser": "^1.4.4",
    "debug": "^2.6.9",
    "express": "^4.16.1",
    "hbs": "^4.0.4",
    "http-errors": "^1.6.3",
    "morgan": "^1.9.1"
  }
}
```

## Run App

```x
npm run dev
```

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/example_project/example_app/app.js:

```js
var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'hbs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;

```

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/example_project/example_app/routes/index.js:

```js
var express = require("express");
var router = express.Router();

/* GET home page. */
router.get("/", function (req, res, next) {
  res.render("index", { title: "Express" });
});

module.exports = router;

```

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/example_project/example_app/views/index.hbs:

```hbs
<h1>{{title}}</h1>
<p>Welcome to {{title}}</p>

```

![image](https://github.com/user-attachments/assets/53ad2975-7e46-41f8-97fb-78c6c5a5e3eb)

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/57232fde-e820-44c4-adeb-048532b84bd9">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/42cb7369-acba-4039-9565-92ee0a269a49">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/8e5c90cb-1026-4d9f-975d-b89221f9c9c9">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/3e9523a7-e376-4756-be30-e8ec718799d8">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/94935ea0-e41d-49cc-9cf7-71b097b5b86d">

# #END</details>

<details>
<summary>3. Setup Basic Express Project - express_project </summary>

# Setup Basic Express Project - express_project

## Create Project Folder

```x
mkdir express_project
cd express_project
```

## Initialize npm Project

```x
npm init -y
```

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/package.json:

```json
{
  "name": "express_project",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": ""
}

```

## install Dependencies - Express and Nodemon, @babel/core, @babel/cli, @babel/preset-env and @babel/node

```x
npm install --save express nodemon
npm install --save-dev @babel/core @babel/cli @babel/preset-env @babel/node
```

```x
{
  "name": "express_project",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2",
    "nodemon": "^3.1.4"
  },
  "devDependencies": {
    "@babel/cli": "^7.24.8",
    "@babel/core": "^7.24.9",
    "@babel/node": "^7.24.8",
    "@babel/preset-env": "^7.24.8"
  }
}
```

## Create babel file

```x
touch .babelrc
```

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/.babelrc:

```x
{
    "presets": [
        "@babel/preset-env"
    ]
}
```

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/5fe7b8e8-ca9f-46e2-83d5-c23b8ee2b1eb">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/05afcdc8-d29b-48aa-99f1-338ec35eb9be">

# #END</details>

<details>
<summary>4. Setup Package.json file with ES6 module and scripts </summary>

# Setup Package.json file with ES6 module and scripts

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/package.json:

```js
{
  "name": "express_project",
  "type": "module",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon --experimental-json-modules --exec babel-node index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2",
    "nodemon": "^3.1.4"
  },
  "devDependencies": {
    "@babel/cli": "^7.24.8",
    "@babel/core": "^7.24.9",
    "@babel/node": "^7.24.8",
    "@babel/preset-env": "^7.24.8"
  }
}
```

## Create Entry File: index.js

```x
touch index.js
```

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";

const app = express();

const PORT = 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

```

## Run Server:

```x
npm run start
```

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/f91afc08-cb4b-479c-aa82-d6656f20fa67">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/9929c67d-d63e-4544-a601-bf08155941b1">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/867a7fdf-3be7-4695-88e9-c9f975ff4dcf">

# #END</details>

<details>
<summary>5. Generating Mock Data for Server </summary>

# Generating Mock Data for Server

## [https://www.mockaroo.com/](https://www.mockaroo.com/)

![image](https://github.com/user-attachments/assets/0d716a52-796d-49a3-aabd-c263da6b3a10)

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/3b15ad81-6c6e-4b48-a2b1-d589462982fc">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/c2588be1-677a-43de-9837-cb021dc2351f">

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/data/mock.json:

```x
[
    {
        "id": 1,
        "first_name": "Eada",
        "last_name": "Parren",
        "email": "eparren0@tuttocitta.it"
    },
    {
        "id": 2,
        "first_name": "Renato",
        "last_name": "Sutherby",
        "email": "rsutherby1@bigcartel.com"
    },
    {
        "id": 3,
        "first_name": "Joshuah",
        "last_name": "Abercrombie",
        "email": "jabercrombie2@blog.com"
    },
    {
        "id": 4,
        "first_name": "Sutton",
        "last_name": "Ferronier",
        "email": "sferronier3@yale.edu"
    },
    ...........
]
```

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";
import data from "./data/mock.json" with { type: "json" };

const app = express();

const PORT = 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Press CTRL+C to stop server");
  console.log(data);
});

```

```x
➜  express_project git:(main) ✗ npm run start

> express_project@1.0.0 start
> nodemon --experimental-json-modules --exec babel-node index.js

[nodemon] 3.1.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `babel-node --experimental-json-modules index.js`
(node:31564) ExperimentalWarning: Importing JSON modules is an experimental feature and might change at any time
(Use `node --trace-warnings ...` to show where the warning was created)
Server running on port 3000
Press CTRL+C to stop server
[
  {
    id: 1,
    first_name: 'Eada',
    last_name: 'Parren',
    email: 'eparren0@tuttocitta.it'
  },
  {
    id: 2,
    first_name: 'Renato',
    last_name: 'Sutherby',
    email: 'rsutherby1@bigcartel.com'
  },
  {
    id: 3,
    first_name: 'Joshuah',
    last_name: 'Abercrombie',
    email: 'jabercrombie2@blog.com'
  },
  {
    id: 4,
    first_name: 'Sutton',
    last_name: 'Ferronier',
    email: 'sferronier3@yale.edu'
  },
  ..........
]
```

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/7709ec54-6201-4eec-a4ca-decf6f350d4a">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/431e37e6-cfc2-4a56-b984-ea2bb6a8d1f7">

![image](https://github.com/user-attachments/assets/a51f9afd-23d2-4350-b866-be1c27ed48d7)

# #END</details>

<details>
<summary>6. Create Basic HTTP Routes for Server Endpoints </summary>

# Create Basic HTTP Routes for Server Endpoints

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";
// import data from "./data/mock.json" with { type: "json" };

const app = express();

const PORT = 3000;

//GET
app.get("/", (req, res) => {
  res.send("This is a GET request at '/'!");
});

//POST
app.post("/", (req, res) => {
  res.send("This is a POST request at '/'!");
});

//PUT
app.put("/:id", (req, res) => {
  const id = req.params.id;
  res.send(`This is a PUT request with id ${id}`);
});

//DELETE
app.delete("/:id", (req, res) => {
  const id = req.params.id;
  res.send(`This is a DELETE request with id ${id}`);
});

// USERS CRUD

app
  .route("/users")
  .get((req, res) => {
    res.send("GET ALL USERS at '/'!");
  })
  .post((req, res) => {
    res.send("CREATE A USER at '/'!");
  });

app
  .route("/users/:id")
  .put((req, res) => {
    const id = req.params.id;
    res.send(`UPDATE USER at '/users/:id' with id ${id}!`);
  })
  .delete((req, res) => {
    const id = req.params.id;
    res.send(`DELETE USER at '/users/:id' with id ${id}!`);
  });

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Press CTRL+C to stop server");
  //   console.log(data);
});

```

```x
GET http://localhost:3000
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/b2aa7a44-2e42-4820-8e00-99e3b690d78d">

![image](https://github.com/user-attachments/assets/13f5d170-eb31-4902-8fa2-c01ab37c6d97)

```x
POST http://localhost:3000
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/519e1d55-5109-4f66-8d27-dd0865bcd9d4">


```x
PUT http://localhost:3000/2
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/4f058006-0572-45ae-bf9e-993c8a852a48">


```x
DELETE http://localhost:3000/4
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/fb130b1f-b2fa-4092-9c52-087d0a93d299">


```x
GET http://localhost:3000/users
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/27f91a91-b40c-45b1-9185-ad8203037acd">

![image](https://github.com/user-attachments/assets/36946cf0-84ab-43da-b5d5-d3ef49ba6f63)


```x
PUT http://localhost:3000/users/2
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/62ecdbaa-4959-4d81-b92d-23580f4c31b1">

# #END</details>

<details>
<summary>7. Create HTTP Routes for Data Endpoints </summary>

# Create HTTP Routes for Data Endpoints

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";
import data from "./data/mock.json" with { type: "json" };

const app = express();
const PORT = 3000;
let db = data;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//GET
app.get("/", (req, res) => {
  res.send("This is a GET request at '/'!");
});

//POST
app.post("/", (req, res) => {
  res.send("This is a POST request at '/'!");
});

//PUT
app.put("/:id", (req, res) => {
  const id = req.params.id;
  res.send(`This is a PUT request with id ${id}`);
});

//DELETE
app.delete("/:id", (req, res) => {
  const id = req.params.id;
  res.send(`This is a DELETE request with id ${id}`);
});

// USERS CRUD

app
  .route("/users")
  .get((req, res) => {
    res.json({"db": db});
  })
  .post((req, res) => {
    const lastDataId = db[db.length - 1].id;
    const new_id = lastDataId + 1;
    let user = req.body;
    user.id = new_id;
    db.push(user);
    res.json({"user": user});
  });

app
  .route("/users/:id")
  .put((req, res) => {
    const id = req.params.id;
    let new_user = req.body;
    if(!new_user.first_name || !new_user.last_name ||!new_user.email) {
        res.json({"msg": "Please enter all the fields!"});
    }
    req.body.id = id;
    db = db.map((user) => {
        if (user.id === parseInt(id)) {
            return req.body;
        } else {
            return user;
        }
    });
    res.json({"msg": "User updated successfully!", "user": new_user});
  })
  .delete((req, res) => {
    const id = req.params.id;
    db = db.filter((user) => user.id !== parseInt(id));
    res.json({"msg": "User deleted successfully!"});
  });

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Press CTRL+C to stop server");
  //   console.log(db);
});

```

```x
GET http://localhost:3000/users
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/5ffb9854-df67-4aa1-9312-a12fde7176cb">

![image](https://github.com/user-attachments/assets/b68eb79e-789a-4f55-948c-3bd0dd5df566)


```x
POST http://localhost:3000/users
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/388c179f-8136-4e83-8da6-cfc7518429ce">

![image](https://github.com/user-attachments/assets/6053312b-f72a-491f-8fad-9a5651892b33)

```x
PUT http://localhost:3000/users/2
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/3f30c7c7-3042-4396-9cb6-e58c1ef953b8">

![image](https://github.com/user-attachments/assets/874f59fc-7149-47ce-8e57-10de2a014bb5)

```x
DELETE http://localhost:3000/users/3
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/54a3648f-f1ca-448a-a84a-84587e67a254">

![image](https://github.com/user-attachments/assets/5a073fa8-af0b-41c3-9e42-0f834a4d5708)

# #END</details>

<details>
<summary>8. Serving Static Files with Express </summary>

# Serving Static Files with Express

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";
import data from "./data/mock.json" with { type: "json" };

const app = express();
const PORT = 3000;
let db = data;

//Using the Public folder
app.use(express.static("public"));

//Using the images folder with route: /images
app.use("/images", express.static("images"));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//GET
app.get("/", (req, res) => {
  res.send("This is a GET request at '/'!");
});

//POST
app.post("/", (req, res) => {
  res.send("This is a POST request at '/'!");
});

//PUT
app.put("/:id", (req, res) => {
  const id = req.params.id;
  res.send(`This is a PUT request with id ${id}`);
});

//DELETE
app.delete("/:id", (req, res) => {
  const id = req.params.id;
  res.send(`This is a DELETE request with id ${id}`);
});

// USERS CRUD

app
  .route("/users")
  .get((req, res) => {
    res.json({"db": db});
  })
  .post((req, res) => {
    const lastDataId = db[db.length - 1].id;
    const new_id = lastDataId + 1;
    let user = req.body;
    user.id = new_id;
    db.push(user);
    res.json({"user": user});
  });

app
  .route("/users/:id")
  .put((req, res) => {
    const id = req.params.id;
    let new_user = req.body;
    if(!new_user.first_name || !new_user.last_name ||!new_user.email) {
        res.json({"msg": "Please enter all the fields!"});
    }
    req.body.id = id;
    db = db.map((user) => {
        if (user.id === parseInt(id)) {
            return req.body;
        } else {
            return user;
        }
    });
    res.json({"msg": "User updated successfully!", "user": new_user});
  })
  .delete((req, res) => {
    const id = req.params.id;
    db = db.filter((user) => user.id !== parseInt(id));
    res.json({"msg": "User deleted successfully!"});
  });

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Press CTRL+C to stop server");
  //   console.log(db);
});

```

```x
http://localhost:3000/mountains_1.jpeg
```

![image](https://github.com/user-attachments/assets/4a0dabba-071f-4935-a0c2-96f427548749)

```x
http://localhost:3000/images/mountains_2.jpeg
```

![image](https://github.com/user-attachments/assets/16e4dc5e-84e8-4c26-bc38-f327e63b785c)

<img width="1353" alt="image" src="https://github.com/user-attachments/assets/ca54d338-b07b-4e30-80bb-02daf76bbc7e">

# #END</details>

<details>
<summary>9. Routing with next() functions </summary>

# Routing with next() functions

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";
import data from "./data/mock.json" with { type: "json" };

const app = express();
const PORT = 3000;
let db = data;

//Using the Public folder
app.use(express.static("public"));

//Using the images folder with route: /images
app.use("/images", express.static("images"));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//GET
app.get("/", (req, res) => {
  res.send("This is a GET request at '/'!");
});

//GET with next()
app.get("/next", (req, res, next) => {
  console.log("The response will be sent by the next function");
  next();
},(req, res) => {
  res.send("This is a GET request callback at '/next'!");
});

//POST
app.post("/", (req, res) => {
  res.send("This is a POST request at '/'!");
});

//PUT
app.put("/:id", (req, res) => {
  const id = req.params.id;
  res.send(`This is a PUT request with id ${id}`);
});

//DELETE
app.delete("/:id", (req, res) => {
  const id = req.params.id;
  res.send(`This is a DELETE request with id ${id}`);
});

// USERS CRUD

app
  .route("/users")
  .get((req, res) => {
    res.json({"db": db});
  })
  .post((req, res) => {
    const lastDataId = db[db.length - 1].id;
    const new_id = lastDataId + 1;
    let user = req.body;
    user.id = new_id;
    db.push(user);
    res.json({"user": user});
  });

app
  .route("/users/:id")
  .put((req, res) => {
    const id = req.params.id;
    let new_user = req.body;
    if(!new_user.first_name || !new_user.last_name ||!new_user.email) {
        res.json({"msg": "Please enter all the fields!"});
    }
    req.body.id = Number(id);
    db = db.map((user) => {
        if (user.id === parseInt(id)) {
            return req.body;
        } else {
            return user;
        }
    });
    res.json({"msg": "User updated successfully!", "user": new_user});
  })
  .delete((req, res) => {
    const id = req.params.id;
    db = db.filter((user) => user.id !== parseInt(id));
    res.json({"msg": "User deleted successfully!"});
  });

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Press CTRL+C to stop server");
  //   console.log(db);
});

```

![image](https://github.com/user-attachments/assets/2de80170-4e4f-49a3-a883-08f0678f50af)

<img width="645" alt="image" src="https://github.com/user-attachments/assets/535988bf-fcf6-4960-9b13-384a2d80b61a">

# #END</details>

<details>
<summary>10. Common Methods for Express Response (Download and Redirect) </summary>

# Common Methods for Express Response (Download and Redirect)

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";
import data from "./data/mock.json" with { type: "json" };

const app = express();
const PORT = 3000;
let db = data;

//Using the Public folder
app.use(express.static("public"));

//Using the images folder with route: /images
app.use("/images", express.static("images"));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//GET
app.get("/", (req, res) => {
  res.send("This is a GET request at '/'!");
});

//GET - download method
app.get("/download", (req, res) => {
  res.download("images/mountains_2.jpeg");
});

//GET - redirect method
app.get("/redirect", (req, res) => {
  res.redirect("https://www.google.com/");
});

//GET with next()
app.get("/next", (req, res, next) => {
  console.log("The response will be sent by the next function");
  next();
},(req, res) => {
  res.send("This is a GET request callback at '/next'!");
});

//POST
app.post("/", (req, res) => {
  res.send("This is a POST request at '/'!");
});

//PUT
app.put("/:id", (req, res) => {
  const id = req.params.id;
  res.send(`This is a PUT request with id ${id}`);
});

//DELETE
app.delete("/:id", (req, res) => {
  const id = req.params.id;
  res.send(`This is a DELETE request with id ${id}`);
});

// USERS CRUD

app
  .route("/users")
  .get((req, res) => {
    res.json({"db": db});
  })
  .post((req, res) => {
    const lastDataId = db[db.length - 1].id;
    const new_id = lastDataId + 1;
    let user = req.body;
    user.id = new_id;
    db.push(user);
    res.json({"user": user});
  });

app
  .route("/users/:id")
  .put((req, res) => {
    const id = req.params.id;
    let new_user = req.body;
    if(!new_user.first_name || !new_user.last_name ||!new_user.email) {
        res.json({"msg": "Please enter all the fields!"});
    }
    req.body.id = Number(id);
    db = db.map((user) => {
        if (user.id === parseInt(id)) {
            return req.body;
        } else {
            return user;
        }
    });
    res.json({"msg": "User updated successfully!", "user": new_user});
  })
  .delete((req, res) => {
    const id = req.params.id;
    db = db.filter((user) => user.id !== parseInt(id));
    res.json({"msg": "User deleted successfully!"});
  });

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Press CTRL+C to stop server");
  //   console.log(db);
});

```

```x
GET http://localhost:3000/download
```

![image](https://github.com/user-attachments/assets/d2c5ad67-4d39-47e0-a671-2bb4ac31d5c0)

```x
GET http://localhost:3000/redirect
```

![image](https://github.com/user-attachments/assets/f35a74d5-ff2e-4f90-8029-c4bad4f61cd2)

![image](https://github.com/user-attachments/assets/56b6020f-8714-4554-8a4a-451d55069bf6)

# #END</details>

<details>
<summary>11. Route Chaining in Express </summary>

# Route Chaining in Express

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";
import data from "./data/mock.json" with { type: "json" };

const app = express();
const PORT = 3000;
let db = data;

//Using the Public folder
app.use(express.static("public"));

//Using the images folder with route: /images
app.use("/images", express.static("images"));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//GET, POST
app
  .route("/class")
  .get((req, res) => {
    res.send("This is a GET request at '/class'!");
  })
  .post((req, res) => {
    res.send("This is a POST request at '/class'!");
  });

//PUT & DELETE
app
  .route("/class/:id")
  .put((req, res) => {
    const id = req.params.id;
    res.send(`This is a PUT request with id ${id}`);
  })
  .delete((req, res) => {
    const id = req.params.id;
    res.send(`This is a DELETE request with id ${id}`);
  });

//GET - download method
app.get("/download", (req, res) => {
  res.download("images/mountains_2.jpeg");
});

//GET - redirect method
app.get("/redirect", (req, res) => {
  res.redirect("https://www.google.com/");
});

//GET with next()
app.get(
  "/next",
  (req, res, next) => {
    console.log("The response will be sent by the next function");
    next();
  },
  (req, res) => {
    res.send("This is a GET request callback at '/next'!");
  }
);

// USERS CRUD

app
  .route("/users")
  .get((req, res) => {
    res.json({ db: db });
  })
  .post((req, res) => {
    const lastDataId = db[db.length - 1].id;
    const new_id = lastDataId + 1;
    let user = req.body;
    user.id = new_id;
    db.push(user);
    res.json({ user: user });
  });

app
  .route("/users/:id")
  .put((req, res) => {
    const id = req.params.id;
    let new_user = req.body;
    if (!new_user.first_name || !new_user.last_name || !new_user.email) {
      res.json({ msg: "Please enter all the fields!" });
    }
    req.body.id = Number(id);
    db = db.map((user) => {
      if (user.id === parseInt(id)) {
        return req.body;
      } else {
        return user;
      }
    });
    res.json({ msg: "User updated successfully!", user: new_user });
  })
  .delete((req, res) => {
    const id = req.params.id;
    db = db.filter((user) => user.id !== parseInt(id));
    res.json({ msg: "User deleted successfully!" });
  });

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Press CTRL+C to stop server");
  //   console.log(db);
});

```

```x
GET http://localhost:3000/class
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/c1d4fd70-4678-4ee5-a5a5-5eb7722ce0ad">


```x
POST http://localhost:3000/class
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/544e7a2f-1ca7-46a5-b6a2-1b3216fc5977">

```x
PUT http://localhost:3000/class/2
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/0f7e1555-5e30-43da-a21d-45c2460b1631">

```x
DELETE http://localhost:3000/4
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/a007f0a9-768a-40ad-8639-02145969ea04">

# #END</details>

<details>
<summary>12. Using Middlewares - Built-in Middlewares </summary>

# Using Middlewares - Built-in Middlewares

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";
import data from "./data/mock.json" with { type: "json" };

const app = express();
const PORT = 3000;
let db = data;

//Using the Public folder
app.use(express.static("public"));

//Using the images folder with route: /images
app.use("/images", express.static("images"));

//Built-in Middlewares using express.json() and express.urlencoded()
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//POST - testing middlewares express.json() and express.urlencoded()
app.post("/item", (req, res) => {
  console.log(req.body);
  res.send(req.body);
});

//GET, POST
app
  .route("/class")
  .get((req, res) => {
    res.send("This is a GET request at '/class'!");
  })
  .post((req, res) => {
    res.send("This is a POST request at '/class'!");
  });

//PUT & DELETE
app
  .route("/class/:id")
  .put((req, res) => {
    const id = req.params.id;
    res.send(`This is a PUT request with id ${id}`);
  })
  .delete((req, res) => {
    const id = req.params.id;
    res.send(`This is a DELETE request with id ${id}`);
  });

//GET - download method
app.get("/download", (req, res) => {
  res.download("images/mountains_2.jpeg");
});

//GET - redirect method
app.get("/redirect", (req, res) => {
  res.redirect("https://www.google.com/");
});

//GET with next()
app.get(
  "/next",
  (req, res, next) => {
    console.log("The response will be sent by the next function");
    next();
  },
  (req, res) => {
    res.send("This is a GET request callback at '/next'!");
  }
);

// USERS CRUD

app
  .route("/users")
  .get((req, res) => {
    res.json({ db: db });
  })
  .post((req, res) => {
    const lastDataId = db[db.length - 1].id;
    const new_id = lastDataId + 1;
    let user = req.body;
    user.id = new_id;
    db.push(user);
    res.json({ user: user });
  });

app
  .route("/users/:id")
  .put((req, res) => {
    const id = req.params.id;
    let new_user = req.body;
    if (!new_user.first_name || !new_user.last_name || !new_user.email) {
      res.json({ msg: "Please enter all the fields!" });
    }
    req.body.id = Number(id);
    db = db.map((user) => {
      if (user.id === parseInt(id)) {
        return req.body;
      } else {
        return user;
      }
    });
    res.json({ msg: "User updated successfully!", user: new_user });
  })
  .delete((req, res) => {
    const id = req.params.id;
    db = db.filter((user) => user.id !== parseInt(id));
    res.json({ msg: "User deleted successfully!" });
  });

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Press CTRL+C to stop server");
  //   console.log(db);
});

```

![image](https://github.com/user-attachments/assets/fc4ee7fd-51b3-4975-a385-a912da22db7b)
![image](https://github.com/user-attachments/assets/9481f169-7c02-4a67-8b25-7c4e0f8cc4d8)

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/49385b98-84e8-4508-8c45-4fcc39f6ea73">
<img width="1313" alt="image" src="https://github.com/user-attachments/assets/237b8d31-de21-4f3d-bebc-f33876fdfda0">
<img width="1313" alt="image" src="https://github.com/user-attachments/assets/60d14bb2-49a7-4d6f-b988-7acebf73eb1d">
<img width="1313" alt="image" src="https://github.com/user-attachments/assets/509519da-3ad3-427e-a792-fec65f21a2c1">
<img width="241" alt="image" src="https://github.com/user-attachments/assets/8c2bd321-e5a9-4717-afcf-836c49a679f7">

# #END</details>

<details>
<summary>13. Using Middlewares - Catching Errors with Middlewares </summary>

# Using Middlewares - Catching Errors with Middlewares

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";
// import data from "./data/mock.json" with { type: "json" };

const app = express();
const PORT = 3000;
// let db = data;

//Using the Public folder
app.use(express.static("public"));

//Using the images folder with route: /images
app.use("/images", express.static("images"));

//Built-in Middlewares using express.json() and express.urlencoded()
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//POST - testing middlewares express.json() and express.urlencoded()
app.post("/item", (req, res) => {
  console.log(req.body);
  res.send(req.body);
});

//GET, POST
app
  .route("/class")
  .get((req, res) => {
    // res.send("This is a GET request at '/class'!");
    //Throw new Error to test error handling in middleware
    throw new Error("Error in GET request at '/class'!");
  })
  .post((req, res) => {
    res.send("This is a POST request at '/class'!");
  });

//PUT & DELETE
app
  .route("/class/:id")
  .put((req, res) => {
    const id = req.params.id;
    res.send(`This is a PUT request with id ${id}`);
  })
  .delete((req, res) => {
    const id = req.params.id;
    res.send(`This is a DELETE request with id ${id}`);
  });

//GET - download method
app.get("/download", (req, res) => {
  res.download("images/mountains_2.jpeg");
});

//GET - redirect method
app.get("/redirect", (req, res) => {
  res.redirect("https://www.google.com/");
});

//GET with next()
app.get(
  "/next",
  (req, res, next) => {
    console.log("The response will be sent by the next function");
    next();
  },
  (req, res) => {
    res.send("This is a GET request callback at '/next'!");
  }
);

// Catching Errors with Middleware
app.use((err, req, res, next) => {
  //   const error = new Error("Not Found");
  //   error.status = 404;
  //   next(error);
  console.error(err.stack);
  res.status(500).send("Something is broken!");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Press CTRL+C to stop server");
});

```

```x
GET http://localhost:3000/class
```

![image](https://github.com/user-attachments/assets/3a9cbeae-3220-4a86-817c-51b157f25eb8)

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/31a5d686-8f14-499b-a059-d081da3e2335">
<img width="1353" alt="image" src="https://github.com/user-attachments/assets/7874a32e-78cc-4fb9-82e5-2dc10b03d356">

# #END</details>

<details>
<summary>14. Using Middlewares - Third Party Middlewares </summary>

# Using Middlewares - Third Party Middlewares

## [https://expressjs.com/en/resources/middleware.html](https://expressjs.com/en/resources/middleware.html)

![image](https://github.com/user-attachments/assets/8c3a3441-ac3f-467b-af77-e22d18d3f2b4)

# #END</details>

<details>
<summary>15. Debugging Express Applications </summary>

# Debugging Express Applications

## [https://expressjs.com/en/guide/debugging.html](https://expressjs.com/en/guide/debugging.html) 

![image](https://github.com/user-attachments/assets/695dddc0-0379-4366-b0e5-5a75b4d6bb72)

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/index.js:

```js
import express from "express";
// import data from "./data/mock.json" with { type: "json" };

const app = express();
const PORT = 3000;
// let db = data;

//Using the Public folder
app.use(express.static("public"));

//Using the images folder with route: /images
app.use("/images", express.static("images"));

//Built-in Middlewares using express.json() and express.urlencoded()
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//POST - testing middlewares express.json() and express.urlencoded()
app.post("/item", (req, res) => {
  console.log(req.body);
  res.send(req.body);
});

//GET, POST
app
  .route("/class")
  .get((req, res) => {
    res.send("This is a GET request at '/class'!");
    //Throw new Error to test error handling in middleware
    // throw new Error("Error in GET request at '/class'!");
  })
  .post((req, res) => {
    res.send("This is a POST request at '/class'!");
  });

//PUT & DELETE
app
  .route("/class/:id")
  .put((req, res) => {
    const id = req.params.id;
    res.send(`This is a PUT request with id ${id}`);
  })
  .delete((req, res) => {
    const id = req.params.id;
    res.send(`This is a DELETE request with id ${id}`);
  });

//GET - download method
app.get("/download", (req, res) => {
  res.download("images/mountains_2.jpeg");
});

//GET - redirect method
app.get("/redirect", (req, res) => {
  res.redirect("https://www.google.com/");
});

//GET with next()
app.get(
  "/next",
  (req, res, next) => {
    console.log("The response will be sent by the next function");
    next();
  },
  (req, res) => {
    res.send("This is a GET request callback at '/next'!");
  }
);

// Catching Errors with Middleware
app.use((err, req, res, next) => {
  //   const error = new Error("Not Found");
  //   error.status = 404;
  //   next(error);
  console.error(err.stack);
  res.status(500).send("Something is broken!");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Press CTRL+C to stop server");
});

```

### src-AI-Software/my_projects/01_Build_Powerful_Web_Apps_with_Node/express_project/package.json:

```json
{
  "name": "express_project",
  "type": "module",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon --experimental-json-modules --exec babel-node index.js",
    "debug": "DEBUG=express:* nodemon --experimental-json-modules index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2",
    "nodemon": "^3.1.4"
  },
  "devDependencies": {
    "@babel/cli": "^7.24.8",
    "@babel/core": "^7.24.9",
    "@babel/node": "^7.24.8",
    "@babel/preset-env": "^7.24.8"
  }
}
```

## Debug Application

```x
npm run debug
```

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/eb6290f5-85d7-4519-81b3-7d5377e6ae12">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/4c9f7ff2-6ca6-4b3e-ade8-1b0a8be397fd">

![image](https://github.com/user-attachments/assets/5dad5adf-8a91-4639-b344-d883f33afca2)

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/176ae746-fdf4-440a-b796-0f61d389199e">

# #END</details>

<details>
<summary>16. Using Express with a Database </summary>

# Using Express with a Database

## [https://expressjs.com/en/guide/database-integration.html](https://expressjs.com/en/guide/database-integration.html)

![image](https://github.com/user-attachments/assets/76e8deb3-d71f-42bc-a93c-8a0c1391e3bf)

![image](https://github.com/user-attachments/assets/63021b77-b2f8-43ca-a7e3-9401b9842715)

![image](https://github.com/user-attachments/assets/6b5622d5-cf68-4c3d-9535-d61b7f568ae6)

# #END</details>

# #END


