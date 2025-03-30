## +Linkedin-Building RESTful APIs with Node.js and Express

## [COURSE](https://www.linkedin.com/learning/building-restful-apis-with-node-js-and-express-16069959/restful-apis-with-node-and-express)

<details>
<summary>1. Install Node and Express </summary>

# Install Node and Express

## Check Node Version

```x
node --version
npm --version
```

## Create Project Folder

```x
mkdir crm
ls
```

## Initialise npm

```x
cd crm
npm init -y
```

```js
{
  "name": "crm",
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

## Install Express

```x
npm i express
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/a52e046a-9e61-4d71-9302-01612a15153a)

<img width="1505" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/8f2e9309-246d-4076-b3c8-182e9f14e3f6">

# #END</details>

<details>
<summary>2. Install and Configure MongoDB </summary>

# Install and Configure MongoDB

## Install Homebrew

```x
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## [MongoDB Website](https://www.mongodb.com/)

## [Install MongoDB on Mac](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)

## [Mongoose Website ](https://mongoosejs.com/)

Mongodb.com --> Products --> Community Edition --> Download

## Install MongoDB

```x
xcode-select --install
brew tap mongodb/brew
brew update
brew install mongodb-community@7.0
```

## To Run MongoDB:

```py
brew services start mongodb-community@7.0
```

## To stop a mongod running:

```py
brew services stop mongodb-community@7.0
```

## To verify that MongoDB is running:

```py
brew services list
```

## Connect and Use MongoDB:

```py
mongosh
```

## Install Mongoose

```x
npm i mongoose
```

```js
{
  "name": "crm",
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
    "mongoose": "^8.4.5"
  }
}

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/dfb00874-456e-4941-a9ea-fb6e22662824)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/4ca66a64-2c45-4ff9-8572-fc0066f878fb)

<img width="1505" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ccf17fa2-1b89-4c02-b268-7b9dc2ceb205">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/1c0f54b5-5b8d-44aa-9b0d-216988f2423a)

# #END</details>

<details>
<summary>3. Install and Configure Babel </summary>

# Install and Configure Babel

```x
npm install --save-dev @babel/cli @babel/core @babel/node @babel/preset-env
```

## Install Nodemon and Body-Parser

```js
npm i nodemon body-parser
```

```js
touch .babelrc
```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/.babelrc:

```js
{
    "presets": [
        "@babel/preset-env"
    ]
}
```

```js
{
  "presets": [
    ["@babel/env", {
      "targets": {
        "node": "current"
      }
    }]
  ],
  "plugins": [
    "@babel/plugin-proposal-class-properties",
    "@babel/plugin-proposal-object-rest-spread"
  ]
}
```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/package.json:

```js
{
  "name": "crm",
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
    "body-parser": "^1.20.2",
    "express": "^4.19.2",
    "mongoose": "^8.4.5",
    "nodemon": "^3.1.4"
  },
  "devDependencies": {
    "@babel/cli": "^7.24.7",
    "@babel/core": "^7.24.7",
    "@babel/node": "^7.24.7",
    "@babel/preset-env": "^7.24.7"
  }
}

```

<img width="1521" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/dc2fbb4e-c55a-4f27-b186-fcab5eb9afa3">
<img width="1521" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/aa1801fe-a818-4c49-ad35-d98af4765bb4">

# #END</details>

<details>
<summary>4. Setup a basic Express Server </summary>

# Setup a basic Express Server

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/package.json:

```js
{
  "name": "crm",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon ./index.js --exec babel-node"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "body-parser": "^1.20.2",
    "express": "^4.19.2",
    "mongoose": "^8.4.5",
    "nodemon": "^3.1.4"
  },
  "devDependencies": {
    "@babel/cli": "^7.24.7",
    "@babel/core": "^7.24.7",
    "@babel/node": "^7.24.7",
    "@babel/preset-env": "^7.24.7"
  }
}
```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/index.js:

```js
import express from "express";

const app = express();
const PORT = 3001;

app.get("/", (req, res) =>
  res.send(`<h1>Your server is running on port ${PORT}</h1>`)
);

app.listen(PORT, () => console.log(`Your server is running on port ${PORT}`));

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d6b461eb-98a5-434e-b143-6a4bd707525f)

<img width="1521" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/b0a6d7fa-a1d1-4a73-8b19-f4b59dc97271">

# #END</details>

<details>
<summary>5. Setup Routing Endpoints </summary>

# Setup Routing Endpoints

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/index.js:

```js
import express from "express";
import routes from "./src/routes/crmRoute";

const app = express();
const PORT = 3001;

routes(app);

app.get("/", (req, res) =>
  res.send(`<h1>Your server is running on port ${PORT}</h1>`)
);

app.listen(PORT, () => console.log(`Your server is running on port ${PORT}`));

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/routes/crmRoute.js:

```js
const routes = (app) => {
  app
    .route("/contact")
    .get((req, res) => {
      res.send("GET request successful!");
    })
    .post((req, res) => {
      res.send("POST request successful!");
    });

  app
    .route("/contact/:contactId")
    .put((req, res) =>
      res.send("PUT request successful!" + " ID: " + req.params.contactId)
    )

    .delete((req, res) =>
      res.send("DELETE request successful!" + " ID: " + req.params.contactId)
    );
};

export default routes;

```

## Test EndPoints with Postman

```x
GET http://localhost:3001/contact
```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/cc149242-a871-41a9-aa00-ae5be44e14a9">

```x
POST http://localhost:3001/contact
```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/95a8ebc0-ba1b-460d-bbb4-be61e534cd1e">

```js
PUT http://localhost:3001/contact/2
```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/6840a185-ef77-4884-8254-e114fe0846e4">

```js
DELETE http://localhost:3001/contact/4
```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/720ecea7-5cda-4248-8f59-d4fb7ba8f408">

<img width="1398" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/a3275a13-bad3-421a-bc12-7850642e8e57">

<img width="1398" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/80944b49-21cf-47b6-8581-ac78417f4a94">

# #END</details>

<details>
<summary>6. Setup Middlewares </summary>

# Setup Middlewares

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/index.js:

```js
import express from "express";
import routes from "./src/routes/crmRoute";
import basicLogger from "./src/middlewares/basicLoggerMiddleware";
import checkAuth from "./src/middlewares/checkAuthMiddleware";
import errorHandler from "./src/middlewares/errorHandlerMiddleware";

const app = express();
const PORT = 3001;

// middleware to log basic request info
app.use(basicLogger);

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

routes(app, checkAuth);

app.get("/", (req, res) =>
  res.send(`<h1>Your server is running on port ${PORT}</h1>`)
);

// middleware to log Errors
app.use(errorHandler);

app.listen(PORT, () => console.log(`Your server is running on port ${PORT}`));

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/middlewares/basicLoggerMiddleware.js:

```js
const basicLogger = (req, res, next) => {
  console.log(`Basic Logger: ${req.method} request for '${req.url}'`);
  next();
};

export default basicLogger;

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/middlewares/checkAuthMiddleware.js:

```js
const checkAuth = (req, res, next) => {
  const isLoggedIn = false; // Replace with real authentication check
  if (isLoggedIn) {
    next();
  } else {
    res.status(401).send("Unauthorized Access!");
  }
};

export default checkAuth;

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/middlewares/errorHandlerMiddleware.js:

```js
const errorHandler = (err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send("Something broke!");
};

export default errorHandler;

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/routes/crmRoute.js:

```js
const routes = (app, checkAuth) => {
  app
    .route("/contact")
    .get(
      (req, res, next) => {
        console.log("Request from: " + req.originalUrl);
        console.log("Request type: " + req.method);
        next();
      },
      (req, res) => {
        res.send("GET request successful!");
      }
    )
    .post(checkAuth, (req, res) => {
      res.send("POST request successful!");
    });

  app
    .route("/contact/:contactId")
    .put(checkAuth, (req, res) =>
      res.send("PUT request successful!" + " ID: " + req.params.contactId)
    )

    .delete(checkAuth, (req, res) =>
      res.send("DELETE request successful!" + " ID: " + req.params.contactId)
    );
};

export default routes;

```

## Test GET Contact Route

```x
GET http://localhost:3001/contact
```

```x
[nodemon] restarting due to changes...
[nodemon] starting `babel-node ./index.js`
Your server is running on port 3001

Basic Logger: GET request for '/contact'
Request from: /contact
Request type: GET
```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/7c973224-2d2e-47fa-9b4b-9e8647c0b0a7">

## Test POST Contact Route (with checkAuth[isLoggedIn] === false )

```x
POST http://localhost:3001/contact
```

```x
Basic Logger: POST request for '/contact'
```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ca27c995-5a75-42ca-aeb8-58e2377a49db">

## Test POST Contact Route (with checkAuth[isLoggedIn] === true )

```x
POST http://localhost:3001/contact
```

```x
Basic Logger: POST request for '/contact'
```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/62671629-9dd3-4196-ba21-f57f66981fd1">

## Test UPDATE Contact Route (with checkAuth[isLoggedIn] === true )

```x
PUT http://localhost:3001/contact
```

```x
Basic Logger: PUT request for '/contact'
```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/dd37c138-8d33-4d77-8d46-855d48af1710">

<img width="1398" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ca7c0dd4-b4a9-48cb-8765-82a65dd5d334">
<img width="1398" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/10d17f95-6767-4cfb-96c7-c3320d53f922">
<img width="1398" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/6f786507-8808-45c3-ab57-2ab690c1e478">
<img width="1398" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9a20f8cd-f345-4aa3-aa84-7f6b859ca27b">
<img width="1398" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/c8e27259-78eb-4ded-9a15-11687ce5a095">

# #END</details>

<details>
<summary>7. Setup Studio3T (MongoDB Studio) </summary>

# Setup Studio3T (MongoDB Studio)

## To Run MongoDB:

```py
brew services start mongodb-community@7.0
```

## To stop a mongod running:

```py
brew services stop mongodb-community@7.0
```

## To verify that MongoDB is running:

```py
brew services list
```

## Connect and Use MongoDB:

```py
mongosh
```

## Download and Install Studio3T

## [https://robomongo.org/](https://robomongo.org/)

```js
localhost:27017
```

<img width="1366" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ec8d31c0-8982-450a-96a6-0256792666d6">
<img width="1322" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ca9c23a0-78db-40ae-8379-2173034b8da7">
<img width="1366" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5d2537cf-0ce3-4abf-ab72-273a73edee58">

# #END</details>

<details>
<summary>8. Setup MongoDB Database and Schema </summary>

# Setup MongoDB Database and Schema

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/index.js:

```js
import express from "express";
import mongoose from "mongoose";
import bodyParser from "body-parser";

import routes from "./src/routes/crmRoute";
import basicLogger from "./src/middlewares/basicLoggerMiddleware";
import checkAuth from "./src/middlewares/checkAuthMiddleware";
import errorHandler from "./src/middlewares/errorHandlerMiddleware";

const app = express();
const PORT = 3001;

// middleware to log basic request info
app.use(basicLogger);

// mongoose connection
mongoose.Promise = global.Promise;
// mongoose.connect("mongodb://localhost:27017/crm", { useNewUrlParser: true });
mongoose.connect("mongodb://localhost/CRMdb", { useNewUrlParser: true });

// middleware to parse request body
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// app.use(express.json());
// app.use(express.urlencoded({ extended: true }));

routes(app, checkAuth);

app.get("/", (req, res) =>
  res.send(`<h1>Your server is running on port ${PORT}</h1>`)
);

// middleware to log Errors
app.use(errorHandler);

app.listen(PORT, () => console.log(`Your server is running on port ${PORT}`));

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/models/crmModel.js:

```js
import mongoose from "mongoose";

const Schema = mongoose.Schema;

export const ContactSchema = new Schema({
  firstName: {
    type: String,
    required: "Enter a first name",
  },
  lastName: {
    type: String,
    required: "Enter a last name",
  },
  email: {
    type: String,
  },
  company: {
    type: String,
  },
  phone: {
    type: Number,
  },
  created_date: {
    type: Date,
    default: Date.now,
  },
});

```

<img width="1407" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/a135d3e4-4791-45e3-8b96-d4b73e3f02de">
<img width="1407" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9db858b5-9ee8-451a-b297-30b8b68776dc">

# #END</details>

<details>
<summary>9. Create POST Endpoint </summary>

# Create POST Endpoint

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/routes/crmRoute.js:

```js
import { addNewContact } from "../controllers/crmController";

const routes = (app, checkAuth) => {
  app
    .route("/contact")
    .get(
      (req, res, next) => {
        console.log("Request from: " + req.originalUrl);
        console.log("Request type: " + req.method);
        next();
      },
      (req, res) => {
        res.send("GET request successful!");
      }
    )
    .post(checkAuth, addNewContact);

  app
    .route("/contact/:contactId")
    .put(checkAuth, (req, res) =>
      res.send("PUT request successful!" + " ID: " + req.params.contactId)
    )

    .delete(checkAuth, (req, res) =>
      res.send("DELETE request successful!" + " ID: " + req.params.contactId)
    );
};

export default routes;

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/controllers/crmController.js:

```js
import mongoose from "mongoose";
import { ContactSchema } from "../models/crmModel";

const Contact = mongoose.model("Contact", ContactSchema);

export const addNewContact = async (req, res) => {
  try {
    const newContact = new Contact(req.body);
    const savedContact = await newContact.save();
    res.json(savedContact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/models/crmModel.js:

```js
import mongoose from "mongoose";

const Schema = mongoose.Schema;

export const ContactSchema = new Schema({
  firstName: {
    type: String,
    required: "Enter a first name",
  },
  lastName: {
    type: String,
    required: "Enter a last name",
  },
  email: {
    type: String,
  },
  company: {
    type: String,
  },
  phone: {
    type: Number,
  },
  created_date: {
    type: Date,
    default: Date.now,
  },
});

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/index.js:

```js
import express from "express";
import mongoose from "mongoose";
import bodyParser from "body-parser";

import routes from "./src/routes/crmRoute";
import basicLogger from "./src/middlewares/basicLoggerMiddleware";
import checkAuth from "./src/middlewares/checkAuthMiddleware";
import errorHandler from "./src/middlewares/errorHandlerMiddleware";

const app = express();
const PORT = 3001;

// middleware to log basic request info
app.use(basicLogger);

// mongoose connection
mongoose.Promise = global.Promise;
// mongoose.connect("mongodb://localhost:27017/crm", { useNewUrlParser: true });
mongoose.connect("mongodb://localhost/CRMdb");

// middleware to parse request body
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// app.use(express.json());
// app.use(express.urlencoded({ extended: true }));

routes(app, checkAuth);

app.get("/", (req, res) =>
  res.send(`<h1>Your server is running on port ${PORT}</h1>`)
);

// middleware to log Errors
app.use(errorHandler);

app.listen(PORT, () => console.log(`Your server is running on port ${PORT}`));

```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/28dba0f0-a3fd-4d54-ae17-e71d20d0a62b">
<img width="1431" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d95b34ea-892d-4211-b2c8-101073479646">

<img width="1407" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/2a7747f1-892f-42a6-b4d3-dca8225e2f59">
<img width="1407" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/7570326c-4985-47b4-aa87-f2858c623c12">

# #END</details>

<details>
<summary>10. Create GET Endpoint </summary>

# Create GET Endpoint

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/routes/crmRoute.js:

```js
import { addNewContact, getContacts } from "../controllers/crmController";

const routes = (app, checkAuth) => {
  app
    .route("/contact")
    .get((req, res, next) => {
      console.log("Request from: " + req.originalUrl);
      console.log("Request type: " + req.method);
      next();
    }, getContacts)

    .post(checkAuth, addNewContact);

  app
    .route("/contact/:contactId")
    .put(checkAuth, (req, res) =>
      res.send("PUT request successful!" + " ID: " + req.params.contactId)
    )

    .delete(checkAuth, (req, res) =>
      res.send("DELETE request successful!" + " ID: " + req.params.contactId)
    );
};

export default routes;

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/controllers/crmController.js:

```js
import mongoose from "mongoose";
import { ContactSchema } from "../models/crmModel";

const Contact = mongoose.model("Contact", ContactSchema);

export const addNewContact = async (req, res) => {
  try {
    const newContact = new Contact(req.body);
    const savedContact = await newContact.save();
    res.json(savedContact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

export const getContacts = async (req, res) => {
  try {
    const contact = await Contact.find({});
    res.json(contact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

// export const getContact = async (req, res) => {
//   try {
//     const contact = await Contact.findById(req.params.contactId);
//     res.json(contact);
//   } catch (err) {
//     res.status(400).json({ error: err.message });
//   }
// };

```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/cd7c5057-26ae-4572-8a81-bc2b2af045bd">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/244c4822-2dcf-4e52-9c5f-8affda619f43)

<img width="1407" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/c9245b4c-7348-44d4-961a-ec73190622da">
<img width="1407" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/115ce2ce-f48d-4165-9e36-70865c2ba97b">

# #END</details>

<details>
<summary>11. Create GET (Single) Endpoint </summary>

# Create GET (Single) Endpoint

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/routes/crmRoute.js:

```js
import {
  addNewContact,
  getContacts,
  getContactWithId,
} from "../controllers/crmController";

const routes = (app, checkAuth) => {
  app
    .route("/contact")
    // get all contacts
    .get((req, res, next) => {
      console.log("Request from: " + req.originalUrl);
      console.log("Request type: " + req.method);
      next();
    }, getContacts)
    // post a new contact
    .post(checkAuth, addNewContact);

  app
    .route("/contact/:contactId")
    // get a specific contact
    .get(checkAuth, getContactWithId)

    .put(checkAuth, (req, res) =>
      res.send("PUT request successful!" + " ID: " + req.params.contactId)
    )

    .delete(checkAuth, (req, res) =>
      res.send("DELETE request successful!" + " ID: " + req.params.contactId)
    );
};

export default routes;

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/controllers/crmController.js:

```js
import mongoose from "mongoose";
import { ContactSchema } from "../models/crmModel";

const Contact = mongoose.model("Contact", ContactSchema);

export const addNewContact = async (req, res) => {
  try {
    const newContact = new Contact(req.body);
    const savedContact = await newContact.save();
    res.json(savedContact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

export const getContacts = async (req, res) => {
  try {
    const contact = await Contact.find({});
    res.json(contact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

export const getContactWithId = async (req, res) => {
  try {
    const contact = await Contact.findById(req.params.contactId);
    res.json(contact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/40b5025f-3c49-42c6-a63b-aba8a9897e6c)
<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ed293157-530e-43fd-a8b3-228fda2bd1ad">

<img width="1407" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9382160f-0c3e-47f3-80d1-d43837bc5613">
<img width="1407" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/911c6b68-755f-4157-8be0-5e7caf4f70dd">

# #END</details>

<details>
<summary>12. Create PUT Endpoint </summary>

# Create PUT Endpoint

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/routes/crmRoute.js:

```js
import {
  addNewContact,
  getContacts,
  getContactWithId,
  updateContact,
} from "../controllers/crmController";

const routes = (app, checkAuth) => {
  app
    .route("/contact")
    // get all contacts
    .get((req, res, next) => {
      console.log("Request from: " + req.originalUrl);
      console.log("Request type: " + req.method);
      next();
    }, getContacts)
    // post a new contact
    .post(checkAuth, addNewContact);

  app
    .route("/contact/:contactId")
    // get a specific contact
    .get(checkAuth, getContactWithId)
    // update a specific contact
    .put(checkAuth, updateContact)

    .delete(checkAuth, (req, res) =>
      res.send("DELETE request successful!" + " ID: " + req.params.contactId)
    );
};

export default routes;

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/controllers/crmController.js:

```js
import mongoose from "mongoose";
import { ContactSchema } from "../models/crmModel";

const Contact = mongoose.model("Contact", ContactSchema);

export const addNewContact = async (req, res) => {
  try {
    const newContact = new Contact(req.body);
    const savedContact = await newContact.save();
    res.json(savedContact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

export const getContacts = async (req, res) => {
  try {
    const contact = await Contact.find({});
    res.json(contact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

export const getContactWithId = async (req, res) => {
  try {
    const contact = await Contact.findById(req.params.contactId);
    res.json(contact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

export const updateContact = async (req, res) => {
  try {
    const updatedContact = await Contact.findByIdAndUpdate(
      req.params.contactId,
      req.body,
      { new: true }
    );
    res.json(updatedContact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/78cd5b03-4eab-4a54-93a6-c16d4e56b259">
<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/10a239ad-4bec-412d-afbe-8d9f182efbfa">

<img width="1407" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/cdd8ef9f-9855-4743-a957-f7160488458a">
<img width="1407" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/b551e481-6411-483e-b38a-4562d1b701ec">

# #END</details>

<details>
<summary>13. Create DELETE Endpoint </summary>

# Create DELETE Endpoint

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/routes/crmRoute.js:

```js
import {
  addNewContact,
  getContacts,
  getContactWithId,
  updateContact,
  deleteContact,
} from "../controllers/crmController";

const routes = (app, checkAuth) => {
  app
    .route("/contact")
    // get all contacts
    .get((req, res, next) => {
      console.log("Request from: " + req.originalUrl);
      console.log("Request type: " + req.method);
      next();
    }, getContacts)
    // post a new contact
    .post(checkAuth, addNewContact);

  app
    .route("/contact/:contactId")
    // get a specific contact
    .get(checkAuth, getContactWithId)
    // update a specific contact
    .put(checkAuth, updateContact)
    // delete a specific contact
    .delete(checkAuth, deleteContact);
};

export default routes;

```

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/src/controllers/crmController.js:

```js
import mongoose from "mongoose";
import { ContactSchema } from "../models/crmModel";

const Contact = mongoose.model("Contact", ContactSchema);

export const addNewContact = async (req, res) => {
  try {
    const newContact = new Contact(req.body);
    const savedContact = await newContact.save();
    res.json(savedContact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

export const getContacts = async (req, res) => {
  try {
    const contact = await Contact.find({});
    res.json(contact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

export const getContactWithId = async (req, res) => {
  try {
    const contact = await Contact.findById(req.params.contactId);
    res.json(contact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

export const updateContact = async (req, res) => {
  try {
    const updatedContact = await Contact.findByIdAndUpdate(
      req.params.contactId,
      req.body,
      { new: true }
    );
    res.json(updatedContact);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

export const deleteContact = async (req, res) => {
  try {
    const deletedContact = await Contact.findByIdAndDelete(
      req.params.contactId
    );
    if (!deletedContact) {
      return res.status(404).json({ message: "Contact not found" });
    }
    res.json({ message: "Contact deleted successfully", deletedContact });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/c7eaf1fb-4c50-425e-b73f-f92d49705eed">
<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ea21780c-db29-42ee-89ad-e2e22aa413fa">
<img width="1431" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9e35e7c0-10f2-42f1-97b0-1c18022f8e35">

<img width="1409" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/06e51efd-095a-4d28-8243-ef78edb63c4e">
<img width="1409" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/dd68fe93-d8c8-464c-b432-d2fa6f313f9c">

# #END</details>

<details>
<summary>14. Serving Static Files </summary>

# Serving Static Files 

### src-AI-Software/my_projects/08_APIs_with_Node_Express/APP/crm/index.js:

```js
import path from "path";
import express from "express";
import mongoose from "mongoose";
import bodyParser from "body-parser";

import routes from "./src/routes/crmRoute";
import basicLogger from "./src/middlewares/basicLoggerMiddleware";
import checkAuth from "./src/middlewares/checkAuthMiddleware";
import errorHandler from "./src/middlewares/errorHandlerMiddleware";

const app = express();
const PORT = 3001;

// middleware to log basic request info
app.use(basicLogger);

// mongoose connection
mongoose.Promise = global.Promise;
// mongoose.connect("mongodb://localhost:27017/crm", { useNewUrlParser: true });
mongoose.connect("mongodb://localhost/CRMdb");

// middleware to parse request body
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// app.use(express.json());
// app.use(express.urlencoded({ extended: true }));

// serving static files
app.use(express.static(path.join(__dirname, "public")));

routes(app, checkAuth);

app.get("/", (req, res) =>
  res.send(`<h1>Your server is running on port ${PORT}</h1>`)
);

// middleware to log Errors
app.use(errorHandler);

app.listen(PORT, () => console.log(`Your server is running on port ${PORT}`));

```

## [http://localhost:3001/football.jpeg](http://localhost:3001/football.jpeg)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/42bb0e09-0eb0-481e-a41c-5f8c7bb57e44)

## [http://localhost:3001/sky.jpeg](http://localhost:3001/sky.jpeg)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/edf351e4-d5e0-4496-8920-6d0d3aa41adc)

# #END</details>

# #END
