## +Linkedin-Advanced Express

## [COURSE](https://www.linkedin.com/learning/advanced-express/tackle-any-project-with-express?resume=false)

<details>
<summary>1. Introduction </summary>

# Introduction

## Check Node Version

```x
node -v
```

## Check NPM Version

```x
npm -v
```

## Install NPM

```x
sudo npm install -g npm@latest
```

## Initialize npm

```x
npm init -y
```

## Install Express and Nodemon

```x
npm install --save express nodemon
```

## Setup package.json file

```json
{
  "name": "app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2",
    "nodemon": "^3.1.4"
  }
}
```

## Run Server

```x
npm run start
```

<img width="1379" alt="image" src="https://github.com/user-attachments/assets/43636f19-0809-451f-8ac4-5ce545fcaac7">


# #END</details>

<details>
<summary>2. Setup Hello World Route </summary>

# Setup Hello World Route

### src-AI-Software/my_projects/03_advanced_express/APP/server.js:

```js
const express = require("express");
const app = express();
const PORT = 3000;

function handler(req, res) {
  return res.send("<h1>Hello World</h1>");
}

app.get("/", handler);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
  console.log("Press Ctrl-C to stop the server");
});

```

![image](https://github.com/user-attachments/assets/9d6634e3-463a-4e1c-9741-2c665f095412)

<img width="1379" alt="image" src="https://github.com/user-attachments/assets/91e6df03-cbe9-4bac-b074-98e08f6b7846">

# #END</details>

<details>
<summary>3. Creating a markdown-to-html template engine </summary>

# Creating a markdown-to-html template engine

## Install marked

```js
npm install marked
```

```json
{
  "name": "app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2",
    "marked": "^13.0.2",
    "nodemon": "^3.1.4"
  }
}

```

### src-AI-Software/my_projects/03_advanced_express/APP/server.js:

```js
const express = require("express");
const fs = require("fs");
const util = require("util");
const { marked } = require("marked");

const app = express();
const PORT = 3000;

const fsreadfile = util.promisify(fs.readFile);

app.engine("md", async (filePath, options, callback) => {
  try {
    const content = await fsreadfile(filePath, "utf-8");
    const rendered = content.toString().replace(`{headline}`, options.headline);
    return callback(null, marked(rendered));
  } catch (err) {
    return callback(err);
  }
});

app.set("views", "views");
app.set("view engine", "md");

function handler(req, res) {
  //   return res.send("<h1>Hello World</h1>");
  return res.render("index", { headline: "Hello World" });
}

app.get("/", handler);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
  console.log("Press Ctrl-C to stop the server");
});

```

### src-AI-Software/my_projects/03_advanced_express/APP/views/index.md:

```md
# {headline}
* List Item 1
* **List Item 2**
* __List Item 3__

## h2 sub-headline

### h3 sub-headline
```

![image](https://github.com/user-attachments/assets/8ab5acd0-8c06-43de-bb6c-d6c28caaa7dc)
![image](https://github.com/user-attachments/assets/b6fd126a-b217-4fa7-9aa7-c898cfaa3bb2)

<img width="1379" alt="image" src="https://github.com/user-attachments/assets/2a8b4e00-4dbd-43f4-b2e8-97326f14801f">
<img width="1379" alt="image" src="https://github.com/user-attachments/assets/916ccace-6a2d-4452-96b9-38829d026de2">

# #END</details>

<details>
<summary>4. Setting up MongoDB </summary>

# Setting up MongoDB

## Install dotenv

```x
npm install dotenv
```

```json
{
  "name": "app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "dotenv": "^16.4.5",
    "express": "^4.19.2",
    "marked": "^13.0.2",
    "nodemon": "^3.1.4"
  }
}

```

### src-AI-Software/my_projects/03_advanced_express/APP/.env:

```js
DEVELOPMENT_DB_URL=mongodb+srv://<username>:<password>@cluster0.vrabuaf.mongodb.net/development?retryWrites=true&w=majority&appName=Cluster0
PRODUCTION_DB_URL=mongodb+srv://<username>:<password>@cluster0.vrabuaf.mongodb.net/production?retryWrites=true&w=majority&appName=Cluster0
TEST_DB_URL=mongodb+srv://<username>:<password>@cluster0.vrabuaf.mongodb.net/test?retryWrites=true&w=majority&appName=Cluster0
```

### src-AI-Software/my_projects/03_advanced_express/APP/server.js:

```js
const dotenv = require("dotenv");
dotenv.config();

const express = require("express");
const fs = require("fs");
const util = require("util");
const { marked } = require("marked");

const app = express();
const PORT = 3000;

const fsreadfile = util.promisify(fs.readFile);

app.engine("md", async (filePath, options, callback) => {
  try {
    const content = await fsreadfile(filePath, "utf-8");
    const rendered = content.toString().replace(`{headline}`, options.headline);
    return callback(null, marked(rendered));
  } catch (err) {
    return callback(err);
  }
});

app.set("views", "views");
app.set("view engine", "md");

function handler(req, res) {
  //   return res.send("<h1>Hello World</h1>");
  return res.render("index", { headline: "Hello World" });
}

app.get("/", handler);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
  console.log("Press Ctrl-C to stop the server");
});

```

![image](https://github.com/user-attachments/assets/4ac18238-48cb-43cb-a1ed-5e03196f077e)
![image](https://github.com/user-attachments/assets/0d272e60-7832-4745-9539-f1e90022e4b3)
![image](https://github.com/user-attachments/assets/ed799881-b62e-48aa-92d1-7cebc16b3ff2)
![image](https://github.com/user-attachments/assets/8af52616-cdc3-4a94-91e8-1822a40b49e4)
![image](https://github.com/user-attachments/assets/39bf9663-c4ea-4d64-8659-326de364355f)

<img width="1379" alt="image" src="https://github.com/user-attachments/assets/0fddfcc4-e09b-4b2c-b0dc-17f400ce66f7">

# #END</details>

<details>
<summary>5. Connecting to MongoDB with mongoose </summary>

# Connecting to MongoDB with mongoose

## Install Mongoose

```js
npm install --save mongoose
```

### src-AI-Software/my_projects/03_advanced_express/APP/.env:

```js
DEVELOPMENT_DB_URL=mongodb+srv://<username>:<password>@cluster0.vrabuaf.mongodb.net/development?retryWrites=true&w=majority&appName=Cluster0
PRODUCTION_DB_URL=mongodb+srv://<username>:<password>@cluster0.vrabuaf.mongodb.net/production?retryWrites=true&w=majority&appName=Cluster0
TEST_DB_URL=mongodb+srv://<username>:<password>@cluster0.vrabuaf.mongodb.net/test?retryWrites=true&w=majority&appName=Cluster0
```

### src-AI-Software/my_projects/03_advanced_express/APP/server.js:

```js
const dotenv = require("dotenv");
dotenv.config();

const express = require("express");
const fs = require("fs");
const util = require("util");
const { marked } = require("marked");

const app = express();
const PORT = 3000;
const db = require("./lib/db");

const fsreadfile = util.promisify(fs.readFile);

app.engine("md", async (filePath, options, callback) => {
  try {
    const content = await fsreadfile(filePath, "utf-8");
    const rendered = content.toString().replace(`{headline}`, options.headline);
    return callback(null, marked(rendered));
  } catch (err) {
    return callback(err);
  }
});

app.set("views", "views");
app.set("view engine", "md");

function handler(req, res) {
  //   return res.send("<h1>Hello World</h1>");
  return res.render("index", { headline: "Hello World" });
}

app.get("/", handler);

app.listen(PORT, () => {
  db(); // Connect to mongo database
  console.log(`Server is running on port ${PORT}`);
  console.log("Press Ctrl-C to stop the server");
});

```

### src-AI-Software/my_projects/03_advanced_express/APP/lib/db.js:

```js
const mongoose = require("mongoose");

module.exports = async function () {
  try {
    await mongoose
      .connect(process.env.DEVELOPMENT_DB_URL, {})
      .then(() => console.log("Connected to MongoDB..."))
      .catch((err) => console.error("Could not connect to MongoDB...", err));
  } catch (err) {
    console.log(err);
  }
};

```

```x
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server is running on port 3000
Press Ctrl-C to stop the server
Connected to MongoDB...

```

![image](https://github.com/user-attachments/assets/e5592c97-ce31-444f-9413-56b799850ef7)

<img width="1379" alt="image" src="https://github.com/user-attachments/assets/918adb4b-354e-41c0-bc8a-7d82dd43cc6b">
<img width="1379" alt="image" src="https://github.com/user-attachments/assets/07772138-f24d-4de6-8f54-29863ba1e9cb">

# #END</details>

<details>
<summary>6. Creating mongoose User Schema </summary>

# Creating mongoose User Schema

## Install Email Validator

```x
npm install --save email-validator
```

### src-AI-Software/my_projects/03_advanced_express/APP/server.js:

```js
const dotenv = require("dotenv");
dotenv.config();

const express = require("express");
const fs = require("fs");
const util = require("util");
const { marked } = require("marked");

const app = express();
const PORT = 3000;
const db = require("./lib/db");

const fsreadfile = util.promisify(fs.readFile);

app.engine("md", async (filePath, options, callback) => {
  try {
    const content = await fsreadfile(filePath, "utf-8");
    const rendered = content.toString().replace(`{headline}`, options.headline);
    return callback(null, marked(rendered));
  } catch (err) {
    return callback(err);
  }
});

app.set("views", "views");
app.set("view engine", "md");

function handler(req, res) {
  //   return res.send("<h1>Hello World</h1>");
  return res.render("index", { headline: "Hello World" });
}

app.get("/", handler);

app.listen(PORT, () => {
  db(); // Connect to mongo database
  console.log(`Server is running on port ${PORT}`);
  console.log("Press Ctrl-C to stop the server");
});

```

### src-AI-Software/my_projects/03_advanced_express/APP/models/UserModel.js:

```js
const mongoose = require("mongoose");
const emailValidator = require("email-validator");

const UserSchema = mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      minlength: 3,
      maxlength: 50,
      trim: true,
      // unique: true,
      index: { unique: true },
    },
    email: {
      type: String,
      required: true,
      trim: true,
      lowercase: true,
      index: { unique: true },
      validate: {
        validator: (email) => emailValidator.validate(email),
        message: (props) => `${props.value} is not a valid email address!`,
      },
    },
    password: {
      type: String,
      required: true,
      minlength: 8,
      maxlength: 50,
      trim: true,
      index: { unique: true },
      // match: /^[a-zA-Z0-9]+$/,
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("User", UserSchema);

```

<img width="1379" alt="image" src="https://github.com/user-attachments/assets/0e6dc3d4-2ecf-465f-91db-fa56b89da21f">


# #END</details>

<details>
<summary>7. Using bcrypt to hash and validate passwords (password encryption) </summary>

# Using bcrypt to hash and validate passwords

## Install Bcrypt

```js
npm install --save bcrypt
```

### src-AI-Software/my_projects/03_advanced_express/APP/server.js:

```js
const dotenv = require("dotenv");
dotenv.config();

const express = require("express");
const fs = require("fs");
const util = require("util");
const { marked } = require("marked");

const app = express();
const PORT = 3000;
const db = require("./lib/db");

const fsreadfile = util.promisify(fs.readFile);

app.engine("md", async (filePath, options, callback) => {
  try {
    const content = await fsreadfile(filePath, "utf-8");
    const rendered = content.toString().replace(`{headline}`, options.headline);
    return callback(null, marked(rendered));
  } catch (err) {
    return callback(err);
  }
});

app.set("views", "views");
app.set("view engine", "md");

function handler(req, res) {
  //   return res.send("<h1>Hello World</h1>");
  return res.render("index", { headline: "Hello World" });
}

app.get("/", handler);

app.listen(PORT, () => {
  db(); // Connect to mongo database
  console.log(`Server is running on port ${PORT}`);
  console.log("Press Ctrl-C to stop the server");
});

```

### src-AI-Software/my_projects/03_advanced_express/APP/models/UserModel.js:

```js
const mongoose = require("mongoose");
const emailValidator = require("email-validator");
const bcrypt = require("bcrypt");
const SALT_ROUNDS = 12;

const UserSchema = mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      minlength: 3,
      maxlength: 50,
      trim: true,
      // unique: true,
      index: { unique: true },
    },
    email: {
      type: String,
      required: true,
      trim: true,
      lowercase: true,
      index: { unique: true },
      validate: {
        validator: (email) => emailValidator.validate(email),
        message: (props) => `${props.value} is not a valid email address!`,
      },
    },
    password: {
      type: String,
      required: true,
      minlength: 8,
      maxlength: 50,
      trim: true,
      index: { unique: true },
      // match: /^[a-zA-Z0-9]+$/,
    },
  },
  {
    timestamps: true,
  }
);

UserSchema.pre("save", async function preSave(next) {
  const user = this;
  if (!user.isModified("password")) return next();
  try {
    const salt = await bcrypt.genSalt(SALT_ROUNDS);
    const hash = await bcrypt.hash(user.password, salt);
    user.password = hash;
    next();
  } catch (err) {
    next(err);
  }
});

UserSchema.methods.comparePassword = async function comparePassword(
  candidatePassword
) {
  return await bcrypt.compare(candidatePassword, this.password);
};

module.exports = mongoose.model("User", UserSchema);

```

![image](https://github.com/user-attachments/assets/4a08fa69-346c-4379-9886-65aab54aeb06)
![image](https://github.com/user-attachments/assets/2e961187-6003-4de2-b5ed-1d618534afdb)

<img width="1379" alt="image" src="https://github.com/user-attachments/assets/1a93ab22-cf3e-4b60-92ac-9520ae898ba1">

# #END</details>

<details>
<summary>8. Creating User Registration Form and Route </summary>

# Creating User Registration Form and Route

## Install EJS

```x
npm install ejs
```

### src-AI-Software/my_projects/03_advanced_express/APP/server.js:

```js
const dotenv = require("dotenv");
dotenv.config();

const path = require("path");
const express = require("express");
const fs = require("fs");
const util = require("util");
const fsreadfile = util.promisify(fs.readFile);

const app = express();
const PORT = 3000;
const db = require("./lib/db");
const User = require("./models/UserModel");
const { error } = require("console");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "./views"));

function handler(req, res) {
  //   return res.send("<h1>Hello World</h1>");
  return res.render("base", {
    template: "index",
    headline: "This is the Home Page!",
  });
}

app.get("/", handler);

app
  .route("/register")
  .get((req, res) => {
    return res.render("base", {
      template: "register",
      headline: "Register Now!",
      error: null,
      message: null,
    });
  })
  .post(async (req, res, next) => {
    try {
      const { name, email, password, confirm_password } = req.body;
      const data = {
        template: "register",
        headline: "Register Now!",
        error: null,
        message: null,
      };

      if (password !== confirm_password) {
        return res.render("base", { ...data, error: "Passwords do not match" });
      }

      const user = new User({ name, email, password });
      const savedUser = await user.save();

      if (savedUser) {
        return res.render("base", {
          ...data,
          message: "User registered successfully!",
        });
      } else {
        return res.render("base", {
          ...data,
          error: "Failed to register user!",
        });
        // return next(new Error("Couldn't register user!"));
      }
    } catch (err) {
      console.log(err);
      next(err);
    }
  });

app.listen(PORT, () => {
  db(); // Connect to mongo database
  console.log(`Server is running on port ${PORT}`);
  console.log("Press Ctrl-C to stop the server");
});

```

### src-AI-Software/my_projects/03_advanced_express/APP/models/UserModel.js:

```js
const mongoose = require("mongoose");
const emailValidator = require("email-validator");
const bcrypt = require("bcrypt");
const SALT_ROUNDS = 12;

const UserSchema = mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      minlength: 3,
      maxlength: 50,
      trim: true,
      // unique: true,
      index: { unique: true },
      //   match: /^[a-zA-Z0-9]+$/,
    },
    email: {
      type: String,
      required: true,
      trim: true,
      lowercase: true,
      index: { unique: true },
      validate: {
        validator: (email) => emailValidator.validate(email),
        message: (props) => `${props.value} is not a valid email address!`,
      },
    },
    password: {
      type: String,
      required: true,
      minlength: 8,
      maxlength: 50,
      trim: true,
      index: { unique: true },
    },
  },
  {
    timestamps: true,
  }
);

UserSchema.pre("save", async function preSave(next) {
  const user = this;
  if (!user.isModified("password")) return next();
  try {
    const salt = await bcrypt.genSalt(SALT_ROUNDS);
    const hash = await bcrypt.hash(user.password, salt);
    user.password = hash;
    next();
  } catch (err) {
    next(err);
  }
});

UserSchema.methods.comparePassword = async function comparePassword(
  candidatePassword
) {
  return await bcrypt.compare(candidatePassword, this.password);
};

module.exports = mongoose.model("User", UserSchema);

```

### src-AI-Software/my_projects/03_advanced_express/APP/views/register.ejs:

```ejs
<!--
    ==================================================
    block - Content
    ==================================================
    -->

<h2><%= headline %></h2>

<% if(error) {%>
<div class="alert alert-danger" role="alert">
  <li><%= error %></li>
</div>
<% } %> <% if(message) {%>
<div class="alert alert-success" role="alert">
  <li><%= message %></li>
</div>
<% } %>

<form action="/register" method="POST">
  <div class="mb-3">
    <label for="name" class="form-label">Name</label>
    <input
      type="text"
      class="form-control"
      id="name"
      name="name"
      placeholder="Bob White"
    />
  </div>
  <div class="mb-3">
    <label for="email" class="form-label">Email address</label>
    <input
      type="email"
      class="form-control"
      id="email"
      name="email"
      placeholder="name@example.com"
    />
  </div>
  <div class="mb-3">
    <label for="password" class="form-label">Password</label>
    <input
      type="password"
      class="form-control"
      id="password"
      name="password"
      placeholder="*********"
    />
  </div>
  <div class="mb-3">
    <label for="confirm_password" class="form-label">Confirm Password</label>
    <input
      type="password"
      class="form-control"
      id="confirm_password"
      name="confirm_password"
      placeholder="*********"
    />
  </div>
  <button type="submit" class="btn btn-success btn-lg">Submit</button>
</form>
<!--
    ==================================================
    endblock - Content
    ==================================================
    -->

```

### src-AI-Software/my_projects/03_advanced_express/APP/views/base.ejs:

```ejs
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>My App</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <main class="container py-4">
      <h1>Welcome to my App!</h1>
      <hr />
      <!--
    ==================================================
    block - Content
    ==================================================
    -->

      <%- include(`./${template}`) %>

      <!--
    ==================================================
    endblock - Content
    ==================================================
    --></main>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
      crossorigin="anonymous"
    ></script>
  </body>
</html>

```

### src-AI-Software/my_projects/03_advanced_express/APP/views/index.ejs:

```ejs
<!--
    ==================================================
    block - Content
    ==================================================
    -->

<h2><%= headline %></h2>
<!--
    ==================================================
    endblock - Content
    ==================================================
    -->

```

![image](https://github.com/user-attachments/assets/183764c5-9ff1-4383-a22b-17f1c8ebd6ce)
![image](https://github.com/user-attachments/assets/46ba8c32-24a7-4c92-9707-f52938d18b22)
![image](https://github.com/user-attachments/assets/d9700e0e-c8b5-49b7-a672-4a54bbfa1ff7)
![image](https://github.com/user-attachments/assets/7222feef-18ce-4ee5-88d4-d2e170397910)
![image](https://github.com/user-attachments/assets/a979d145-a99f-41c1-a181-0abe6d4e2126)

# #END</details>

<details>
<summary>9. Adding Cookies and Sessions to Express </summary>

# Adding Cookies and Sessions to Express

## Install cookie-parser

```x
npm install cookie-parser
```

## Install express-session, connect-mongo, mongoose

```x
npm install express-session connect-mongo mongoose
```

```json
{
  "name": "app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "bcrypt": "^5.1.1",
    "connect-mongo": "^5.1.0",
    "cookie-parser": "^1.4.6",
    "dotenv": "^16.4.5",
    "ejs": "^3.1.10",
    "email-validator": "^2.0.4",
    "express": "^4.19.2",
    "express-session": "^1.18.0",
    "marked": "^13.0.2",
    "mongoose": "^8.5.1",
    "nodemon": "^3.1.4"
  }
}

```

### src-AI-Software/my_projects/03_advanced_express/APP/server.js:

```js
const dotenv = require("dotenv");
dotenv.config();

const path = require("path");
const express = require("express");
const fs = require("fs");
const util = require("util");
const fsreadfile = util.promisify(fs.readFile);

const cookieParser = require("cookie-parser");
const session = require("express-session");
const mongoose = require("mongoose");
const MongoStore = require("connect-mongo");

const app = express();
const PORT = 3000;
const db = require("./lib/db");
const User = require("./models/UserModel");
const { error } = require("console");

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "./views"));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(cookieParser());
app.use(
  session({
    secret: "my_secret_key123",
    resave: true,
    saveUninitialized: false,
    store: MongoStore.create({
      mongoUrl: process.env.DEVELOPMENT_DB_URL,
      ttl: 14 * 24 * 60 * 60 // = 14 days. Default
    }),
  })
);

app.use(async (req, res, next) => {
  try {
    req.session.visits = req.session.visits ? req.session.visits + 1 : 1;
    console.log("visits: " + req.session.visits);
    return next();
    // if (req.session.user) {
    //   const user = await User.findById(req.session.user);
    //   req.user = user;
    // }
    // next();
  } catch (error) {
    next(error);
  }
});

function handler(req, res) {
  //   return res.send("<h1>Hello World</h1>");
  return res.render("base", {
    template: "index",
    headline: "This is the Home Page!",
  });
}

app.get("/", handler);

app
  .route("/register")
  .get((req, res) => {
    return res.render("base", {
      template: "register",
      headline: "Register Now!",
      error: null,
      message: null,
    });
  })
  .post(async (req, res, next) => {
    try {
      const { name, email, password, confirm_password } = req.body;
      const data = {
        template: "register",
        headline: "Register Now!",
        error: null,
        message: null,
      };

      if (password !== confirm_password) {
        return res.render("base", { ...data, error: "Passwords do not match" });
      }

      const user = new User({ name, email, password });
      const savedUser = await user.save();

      if (savedUser) {
        return res.render("base", {
          ...data,
          message: "User registered successfully!",
        });
      } else {
        return res.render("base", {
          ...data,
          error: "Failed to register user!",
        });
        // return next(new Error("Couldn't register user!"));
      }
    } catch (err) {
      console.log(err);
      next(err);
    }
  });

app.listen(PORT, () => {
  db(); // Connect to mongo database
  console.log(`Server is running on port ${PORT}`);
  console.log("Press Ctrl-C to stop the server");
});

```

```x
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server is running on port 3000
Press Ctrl-C to stop the server
Connected to MongoDB...
visits: 1
visits: 2
visits: 3
visits: 4
visits: 5
visits: 6
visits: 7
visits: 8
```

![image](https://github.com/user-attachments/assets/70b03b87-a8af-434b-b464-4fb253d916fa)
![image](https://github.com/user-attachments/assets/f1b952df-875e-4f01-ae32-f100bbc21c43)
![image](https://github.com/user-attachments/assets/7d348989-ecd9-407e-af7e-ea489bce06f9)
![image](https://github.com/user-attachments/assets/f891aa85-9099-4e50-9c25-abc32bd4d664)
![image](https://github.com/user-attachments/assets/a9db5f67-c22d-4437-a94e-e8d31240fc03)

<img width="1406" alt="image" src="https://github.com/user-attachments/assets/28fb522b-75d3-4d75-b0cc-b14a4d87dfc0">

# #END</details>

<details>
<summary>10. Adding Passport to Express - Authentication with LocalStrategy </summary>

# Adding Passport to Express - Authentication with LocalStrategy

## Install Passport, passport-local 

```x
npm install --save passport passport-local
```

```json
{
  "name": "app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "bcrypt": "^5.1.1",
    "connect-mongo": "^5.1.0",
    "cookie-parser": "^1.4.6",
    "dotenv": "^16.4.5",
    "ejs": "^3.1.10",
    "email-validator": "^2.0.4",
    "express": "^4.19.2",
    "express-session": "^1.18.0",
    "marked": "^13.0.2",
    "mongoose": "^8.5.1",
    "nodemon": "^3.1.4",
    "passport": "^0.7.0",
    "passport-local": "^1.0.0"
  }
}

```

### src-AI-Software/my_projects/03_advanced_express/APP/server.js:

```js
const dotenv = require("dotenv");
dotenv.config();

const path = require("path");
const express = require("express");
const fs = require("fs");
const util = require("util");
const fsreadfile = util.promisify(fs.readFile);

const cookieParser = require("cookie-parser");
const session = require("express-session");
const mongoose = require("mongoose");
const MongoStore = require("connect-mongo");

const app = express();
const PORT = 3000;
const db = require("./lib/db");
const User = require("./models/UserModel");
const auth = require("./lib/auth");

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "./views"));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(cookieParser());
app.use(
  session({
    secret: "my_secret_key123",
    resave: true,
    saveUninitialized: false,
    store: MongoStore.create({
      mongoUrl: process.env.DEVELOPMENT_DB_URL,
      ttl: 14 * 24 * 60 * 60, // = 14 days. Default
    }),
  })
);

app.use(auth.initialize);
app.use(auth.session);
app.use(auth.setUser);

app.use(async (req, res, next) => {
  try {
    req.session.visits = req.session.visits ? req.session.visits + 1 : 1;
    console.log("visits: " + req.session.visits);
    return next();
  } catch (error) {
    next(error);
  }
});

function handler(req, res) {
  return res.render("base", {
    template: "index",
    headline: "This is the Home Page!",
  });
}

app.get("/", handler);

app
  .route("/register")
  .get((req, res) => {
    return res.render("base", {
      template: "register",
      headline: "Register Now!",
      error: null,
      message: null,
    });
  })
  .post(async (req, res, next) => {
    try {
      const { name, email, password, confirm_password } = req.body;
      const data = {
        template: "register",
        headline: "Register Now!",
        error: null,
        message: null,
      };

      if (password !== confirm_password) {
        return res.render("base", { ...data, error: "Passwords do not match" });
      }

      const user = new User({ name, email, password });
      const savedUser = await user.save();

      if (savedUser) {
        return res.render("base", {
          ...data,
          message: "User registered successfully!",
        });
      } else {
        return res.render("base", {
          ...data,
          error: "Failed to register user!",
        });
        // return next(new Error("Couldn't register user!"));
      }
    } catch (err) {
      console.log(err);
      next(err);
    }
  });

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  var err = new Error("Not Found");
  err.status = 404;
  next(err);
});

// *** error handlers *** //

// development error handler
// will print stacktrace
if (app.get("env") === "development") {
  app.use(function (err, req, res, next) {
    res.status(err.status || 500);
    res.render("error", {
      message: err.message,
      error: err,
    });
  });
}

// production error handler
// no stacktraces leaked to user
app.use(function (err, req, res, next) {
  res.status(err.status || 500);
  res.render("error", {
    message: err.message,
    error: {},
  });
});

app.listen(PORT, () => {
  db(); // Connect to mongo database
  console.log(`Server is running on port ${PORT}`);
  console.log("Press Ctrl-C to stop the server");
});

```

### src-AI-Software/my_projects/03_advanced_express/APP/lib/auth.js:

```js
const passport = require("passport");
const LocalStrategy = require("passport-local").Strategy;
const UserModel = require("../models/UserModel");

passport.use(
  new LocalStrategy(
    {
      usernameField: "email",
      passwordField: "password",
    },
    async (username, password, done) => {
      try {
        const user = await UserModel.findOne({ email: username }).exec();
        if (!user) {
          return done(null, false, {
            message: "Invalid username or password.",
          });
        }

        const isMatch = await user.comparePassword(password);
        if (!isMatch) {
          return done(null, false, {
            message: "Invalid username or password.",
          });
        }

        return done(null, user);
      } catch (err) {
        return done(err);
      }
    }
  )
);

module.exports = {
  initialize: passport.initialize(),
  session: passport.session(),
  setUser: (req, res, next) => {
    res.locals.user = req.user;
    return next();
  },
};

```

### src-AI-Software/my_projects/03_advanced_express/APP/models/UserModel.js:

```js
const mongoose = require("mongoose");
const emailValidator = require("email-validator");
const bcrypt = require("bcrypt");
const SALT_ROUNDS = 12;

const UserSchema = mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      minlength: 3,
      maxlength: 50,
      trim: true,
      // unique: true,
      index: { unique: true },
    },
    email: {
      type: String,
      required: true,
      trim: true,
      lowercase: true,
      index: { unique: true },
      validate: {
        validator: (email) => emailValidator.validate(email),
        message: (props) => `${props.value} is not a valid email address!`,
      },
    },
    password: {
      type: String,
      required: true,
      minlength: 8,
      maxlength: 50,
      trim: true,
      index: { unique: true },
      //   match: /^[a-zA-Z0-9]+$/,
    },
  },
  {
    timestamps: true,
  }
);

UserSchema.pre("save", async function preSave(next) {
  const user = this;
  if (!user.isModified("password")) return next();
  try {
    const salt = await bcrypt.genSalt(SALT_ROUNDS);
    const hash = await bcrypt.hash(user.password, salt);
    user.password = hash;
    next();
  } catch (err) {
    next(err);
  }
});

UserSchema.methods.comparePassword = async function comparePassword(
  candidatePassword
) {
  return await bcrypt.compare(candidatePassword, this.password);
};

module.exports = mongoose.model("User", UserSchema);

```

![image](https://github.com/user-attachments/assets/c86686ab-0cd6-4c83-a7c0-eac540736b3e)
![image](https://github.com/user-attachments/assets/6ddffb49-4cfa-4da2-a3bd-7eeaaff1c119)

<img width="1450" alt="image" src="https://github.com/user-attachments/assets/097673db-257f-49b4-b8e2-962c680b9d24">

# #END</details>

<details>
<summary>11. Adding Passport to Express - Serializing and Deserializing Users </summary>

# Adding Passport to Express - Serializing and Deserializing Users

### src-AI-Software/my_projects/03_advanced_express/APP/lib/auth.js:

```js
const passport = require("passport");
const LocalStrategy = require("passport-local").Strategy;
const UserModel = require("../models/UserModel");

passport.use(
  new LocalStrategy(
    {
      usernameField: "email",
      passwordField: "password",
    },
    async (username, password, done) => {
      try {
        const user = await UserModel.findOne({ email: username }).exec();
        if (!user) {
          return done(null, false, {
            message: "Invalid username or password.",
          });
        }

        const isMatch = await user.comparePassword(password);
        if (!isMatch) {
          return done(null, false, {
            message: "Invalid username or password.",
          });
        }

        return done(null, user);
      } catch (err) {
        return done(err);
      }
    }
  )
);

passport.serializeUser((user, done) => {
  done(null, user._id);
});

passport.deserializeUser(async (id, done) => {
  try {
    const user = await UserModel.findById(id).exec();
    return done(null, user);
  } catch (err) {
    return done(err);
  }
});

module.exports = {
  initialize: passport.initialize(),
  session: passport.session(),
  setUser: (req, res, next) => {
    res.locals.user = req.user;
    return next();
  },
};

```

<img width="1348" alt="image" src="https://github.com/user-attachments/assets/e1255d34-8b53-4f70-a157-a659fc079c2b">

# #END</details>

<details>
<summary>12. Adding Passport to Express - Create Login Form with passport </summary>

# Adding Passport to Express - Create Login Form with passport

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

# #END</details>
