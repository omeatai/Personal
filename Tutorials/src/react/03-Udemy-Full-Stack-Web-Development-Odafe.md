# UDEMY-FULL STACK WEB DEVELOPMENT USING THE MERN STACK AND DEVOPS - ODAFE

## [COURSE](https://www.udemy.com/course/full-stack-web-development-using-the-mern-stack-and-devops/)

<details>
  <summary>1. Introduction to Express </summary>

# Initialize npm

```jsbs
npm init -y
```

# Install express

```jsbs
npm install express --save
```

# install nodemon

```jsbs
npm install nodemon --save-dev
```

### x-odafe-project/package.json:

```js
{
  "name": "x-odafe-project",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "dev": "nodemon app.js",
    "start": "node app.js",
    "start-server": "node server.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^2.0.22"
  }
}

```

### x-odafe-project/app.js:

```js
const express = require("express");
const app = express();
const PORT = 8080;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/996baee6-1791-47b6-adff-bf5eb5554310)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/3188767c-b7fd-4c00-954f-ec9afe9427c0)

</details>

<details>
  <summary>2. Returning JSON response </summary>

# Returning JSON response

### x-odafe-project/app.js:

```js
const express = require("express");
const app = express();
const PORT = 8080;

app.get("/", (req, res) => {
  res.status(200).send("Hello World!");
});

app.get("/test", (req, res) => {
  res.status(200).json({ msg: "This is a JSON response..." });
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/792e6f99-d01b-4698-b69b-677e6c150341)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/c939498e-18a1-44ea-95fa-b9243ae58fa5)

</details>

<details>
  <summary>3. Using Middlewares to Log requests </summary>

# Using Middleware to Log requests

### x-odafe-project/app.js:

```js
const express = require("express");
const app = express();
const PORT = 8080;

app.use((req, res, next) => {
  console.log(req.method, req.url, req.path, req.ip, req.headers.host);
  next();
});

app.get("/", (req, res) => {
  res.status(200).send("Hello World!");
});

app.get("/test", (req, res) => {
  res.status(200).json({ msg: "This is a JSON response..." });
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});
```

# output:

```js
// [nodemon] restarting due to changes...
// [nodemon] starting `node app.js`
// Server listening on port 8080...
// GET /test /test ::1 localhost:8080
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/1abed75a-6dc1-46cd-b33c-3480633e36a3)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/f7cf903d-f9c3-4a04-ae2c-e39254b94130)

</details>

<details>
  <summary>4. Setup Shopy Express Server </summary>

# Initialize npm

```jsbs
npm init -y
```

# Initialize git

```jsbs
git init
```

# Install express, bcryptjs, jsonwebtoken, mongoose, and nodemon

```jsbs
npm i express --save
npm i bcryptjs --save
npm i jsonwebtoken --save
npm i mongoose --save
npm i nodemon --save-dev

npm i express bcryptjs jsonwebtoken mongoose --save
npm i nodemon --save-dev
```

### x-shopy-ecommerce-app/package.json:

```js
{
  "name": "x-shopy-ecommerce-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "nodemon": "^2.0.22"
  },
  "dependencies": {
    "bcryptjs": "^2.4.3",
    "express": "^4.18.2",
    "jsonwebtoken": "^9.0.0",
    "mongoose": "^7.2.1"
  }
}

```

### x-shopy-ecommerce-app/server.js:

```js
const express = require("express");
const app = express();
const PORT = process.env.PORT || 8000;

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

# output:

```js
// [nodemon] restarting due to changes...
// [nodemon] starting `node server.js`
// Server is listening on 8000...
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/c183df84-952d-402c-8989-1204b70e7930)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/49f92c54-3c4d-4ccd-98f4-fb483692fb1b)

</details>

<details>
  <summary>5. Setup and Connect to MongoDB Database </summary>

# Install mongoDB

```jsbs
npm install mongodb --save
```

# Connect to MongoDB

```jsbs
mongodb+srv://<username>:<password>@cluster0.qfv7ifn.mongodb.net/<dbname>?retryWrites=true&w=majority
```

```js
const { MongoClient, ServerApiVersion } = require("mongodb");
const uri =
  "mongodb+srv://<username>:<password>@cluster0.qfv7ifn.mongodb.net/?retryWrites=true&w=majority";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  },
});

async function run() {
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log(
      "Pinged your deployment. You successfully connected to MongoDB!"
    );
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);
```

# Install Mongoose

```jsbs
npm install mongoose --save
```

# Connect to Mongoose

```js
const mongoose = require("mongoose");
mongoose.connect("mongodb://127.0.0.1:27017/test");

const Cat = mongoose.model("Cat", { name: String });

const kitty = new Cat({ name: "Zildjian" });
kitty.save().then(() => console.log("meow"));
```

### x-shopy-ecommerce-app/server.js:

```js
const express = require("express");
const app = express();
const connectDB = require("./config/db");
const PORT = process.env.PORT || 8000;

connectDB();

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

### x-shopy-ecommerce-app/config/db.js:

```js
const mongoose = require("mongoose");
const config = require("./keys");
const db = config.mongoURI;

const connectDB = async () => {
  try {
    await mongoose.connect(db, {
      // useNewUrlParser: true,
      // useUnifiedTopology: true,
      // useCreateIndex: true,
    });
    console.log("Connected to DATABASE...");
  } catch (err) {
    console.log("Error connecting to DATABASE");
    process.exit(1);
  }
};

module.exports = connectDB;
```

### x-shopy-ecommerce-app/config/keys.js:

```js
const mongoURI =
  "mongodb+srv://<username>:<password>@cluster0.qfv7ifn.mongodb.net/<dbname>?retryWrites=true&w=majority";

module.exports = { mongoURI };
```

# run:

```jsbs
npm start
```

# output:

```js
// [nodemon] restarting due to changes...
// [nodemon] starting `node server.js`
// Server is listening on 8000...
// Connected to DATABASE...
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/08b49b29-85bb-4cee-8f79-48663746cba9)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/70afedc0-759b-4e44-a248-711f19368eb6)

</details>

<details>
  <summary>6. Creating and Managing API Routes </summary>

# Creating and Managing API Routes

### x-shopy-ecommerce-app/server.js:

```js
const express = require("express");
const app = express();
const connectDB = require("./config/db");
const PORT = process.env.PORT || 8000;

//Connect to the DB
connectDB();

//Define routes and API
app.use("/api/users", require("./routes/userApi"));
app.use("/api/products", require("./routes/productApi"));

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

### x-shopy-ecommerce-app/routes/productApi.js:

```js
const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
  res.send("Product route");
});

module.exports = router;
```

### x-shopy-ecommerce-app/routes/userApi.js:

```js
const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
  res.send("Users route");
});

module.exports = router;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/e379fdea-e3f0-4216-b143-7667f5505a57)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2afa9402-e3bf-4af7-8388-bf7e933c935f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/027e91a2-3027-4efc-98d2-06ab4825f1bd)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/991c48a9-bf7b-435b-89f3-71eec7ec8420)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/fda1cbd2-a3ee-4ffd-9fb4-a289b91ea544)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/cd9762c8-df54-4a4c-8f2e-db8f2653c04c)

</details>

<details>
  <summary>7. Separate Server and Client Folders </summary>

# Separate Server and Client Folders

![](https://github.com/omeatai/React-Tutorial/assets/32337103/2764623c-b162-413a-b2d8-ff40d979c4c7)

</details>

<details>
  <summary>8. Create User Model </summary>

# Mongoose Sample Model

```js
const Model = mongoose.model("Test", schema);

const doc = new Model();
doc._id instanceof mongoose.Types.ObjectId; // true
```

```js
const schema = new Schema({ _id: Number });
const Model = mongoose.model("Test", schema);

const doc = new Model();
await doc.save(); // Throws "document must have an _id before saving"

doc._id = 1;
await doc.save(); // works
```

### x-shopy-ecommerce-app/server/server.js:

```js
const express = require("express");
const app = express();
const connectDB = require("./config/db");
const PORT = process.env.PORT || 8000;

//Connect to the DB
connectDB();

//Define routes and API
app.use("/api/users", require("./routes/userApi"));
app.use("/api/products", require("./routes/productApi"));

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

### x-shopy-ecommerce-app/server/models/User.js:

```js
const mongoose = require("mongoose");
const UserSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    required: true,
  },
  role: {
    type: String,
    default: "customer",
  },
  date: {
    type: Date,
    default: Date.now(),
  },
});

const User = mongoose.model("User", UserSchema);
module.exports = User;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/817d08b3-2385-43a8-8dbb-118c3ccf47f0)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/68380893-ad5a-4c7f-84b8-dc6d417fb248)

</details>

<details>
  <summary>9. Validating Fields with Express-Validator </summary>

# Install express validator

```jsbs
npm install express-validator --save
```

# Express Validator Sample - https://express-validator.github.io/docs/

### req.body:

- the body of the HTTP request.
- Can be any value, however objects, arrays and other JavaScript primitives work better.

### req.cookies:

- the Cookie header parsed as an object from cookie name to its value.

### req.headers:

- the headers sent along with the HTTP request.

### req.params:

- an object from name to value.
- In express.js, this is parsed from the request path and matched with route definition path.
- But it can really be anything meaningful coming from the HTTP request.

### req.query:

- the portion after the ? in the HTTP request's path, parsed as an object from query parameter name to value.

# Example URL

```jsbs
http://localhost:3000/hello?person=John //with Query Field
http://localhost:3000/hello //without Query Field
```

# Example Code

```js
const express = require("express");
const { query, matchedData, validationResult } = require("express-validator");
const app = express();

app.use(express.json());
app.get("/hello", query("person").notEmpty().escape(), (req, res) => {
  const result = validationResult(req);
  if (result.isEmpty()) {
    const data = matchedData(req);
    return res.send(`Hello, ${data.person}!`);
  }

  res.send({ errors: result.array() });
});

app.listen(3000);
```

# Without Query Field result:

```js
{
  "errors": [
    {
      "location": "query",
      "msg": "Invalid value",
      "path": "person",
      "type": "field"
    }
  ]
}
```

# With Query Field result:

```js
"Hello, John!";
```

# Custom Validation:

```js
app.post(
  "/create-user",
  body("email").custom(async (value) => {
    const user = await UserCollection.findUserByEmail(value);
    if (user) {
      throw new Error("E-mail already in use");
    }
  }),
  (req, res) => {
    // Handle the request
  }
);
```

```js
app.post(
  "/create-user",
  body("password").isLength({ min: 5 }),
  body("passwordConfirmation").custom((value, { req }) => {
    return value === req.body.password;
  }),
  (req, res) => {
    // Handle request
  }
);
```

# Allow body to be passed with requests

### x-shopy-ecommerce-app/server/server.js:

```jsbs
app.use(express.json({ extended: false })); // allow req.body
```

```js
const express = require("express");
const app = express();
const connectDB = require("./config/db");
const PORT = process.env.PORT || 8000;

//Connect to the DB
connectDB();

//Define routes and API
app.use(express.json({ extended: false })); // allow req.body
app.use("/api/users", require("./routes/userApi"));
app.use("/api/products", require("./routes/productApi"));

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

### x-shopy-ecommerce-app/server/routes/userApi.js:

```js
const express = require("express");
const router = express.Router();
const { check, validationResult } = require("express-validator");

router.get("/", (req, res) => {
  res.send("Users route");
});

const postUserValidation = [
  check("name", "Name is required").not().isEmpty(),
  check("email", "Please enter a valid email").isEmail(),
  check(
    "password",
    "please password should have at least 5 characters"
  ).isLength({ min: 5 }),
];

router.post("/", postUserValidation, (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }
  res.json(req.body);
});

module.exports = router;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/ecaebdc2-23b6-4c78-b944-18e4affb5c6b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/5b5fc7c7-8e78-442c-b300-e74eafcc3e64)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b2da9650-510b-4a6d-8b8d-cf931ac8cc48)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/ad8a89b5-cebb-4214-828e-2ea241663809)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/18d2650b-9b32-4166-a1c1-68e0717fcf07)

</details>

<details>
  <summary>10. Save Post User to Database </summary>

# Save Post User to Database

### x-shopy-ecommerce-app/server/server.js:

```js
const express = require("express");
const app = express();
const connectDB = require("./config/db");
const PORT = process.env.PORT || 8000;

//Connect to the DB
connectDB();

//Define routes and API
app.use(express.json({ extended: false })); // allow req.body
app.use("/api/users", require("./routes/userApi"));
app.use("/api/products", require("./routes/productApi"));

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

### x-shopy-ecommerce-app/server/routes/userApi.js:

```js
const express = require("express");
const router = express.Router();
const { check, validationResult } = require("express-validator");
const User = require("../models/User");

router.get("/", (req, res) => {
  res.send("Users route");
});

const postUserValidation = [
  check("name", "Name is required").not().isEmpty(),
  check("email", "Please enter a valid email").isEmail(),
  check(
    "password",
    "please password should have at least 5 characters"
  ).isLength({ min: 5 }),
];

router.post("/", postUserValidation, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  //Save User to db
  try {
    const { name, email, password } = req.body;
    let user = await User.findOne({ email: email });

    if (user) {
      return res.status(400).json({ errors: { msg: "User already Exists!" } });
    }
    user = new User({ name, email, password });
    user.save();
    console.log(user);
    return res
      .status(201)
      .json({ result: req.body, message: "User created successfully" });
  } catch (err) {
    console.error(err);
    return res.status(400).json({ errors: err });
  }
});

module.exports = router;
```

# output:

```js
// [nodemon] restarting due to changes...
// [nodemon] starting `node server.js`
// Server is listening on 8000...
// Connected to DATABASE...
// {
//   name: 'Ifeanyi Omeata',
//   email: 'ifeanyi@gmail.com',
//   password: '123456',
//   role: 'customer',
//   date: 2023-05-30T13:50:33.810Z,
//   _id: new ObjectId("6475ff39e59c7b38d4b6b2e6")
// }
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/dcf6d55c-ed2b-4fbb-bc86-ca4161a2a092)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/3ad5d2d9-ad06-4f7e-a1b3-97c2685bebe2)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/0e64c1a1-2549-4b79-a4c9-7693e9038b78)

</details>

<details>
  <summary>11. Using bcrypt to hash passwords </summary>

# Install bcryptjs

```jsbs
npm install bcryptjs --save
```

# Encrypting(Hashing) with bcrypt - Sync

```js
const password = "romeo123";
const bcrypt = require("bcryptjs");
const salt = bcrypt.genSaltSync(10);
const hash = bcrypt.hashSync(password, salt);
// Store hash in your password DB.
```

# Encrypting(Hashing) with bcrypt - Async

```js
async () => {
  const password = "romeo123";
  const bcrypt = require("bcryptjs");
  const salt = await bcrypt.genSalt(10);
  const hash = await bcrypt.hash(password, salt);
  // Store hash in your password DB.
};
```

# To check a password

```js
async () => {
  const password = "romeo123";
  const hash = "$2a$10$Fya8LisEl1HTihZad56WpOTpPGXNfwv1SwLryXPtP1OijgzsGzjj2";
  const result = await bcrypt.compare(password, hash);
  // Check if result is true
};
```

### x-shopy-ecommerce-app/server/routes/userApi.js:

```js
const express = require("express");
const router = express.Router();
const bcrypt = require("bcryptjs");
const { check, validationResult } = require("express-validator");
const User = require("../models/User");

router.get("/", (req, res) => {
  res.send("Users route");
});

const postUserValidation = [
  check("name", "Name is required").not().isEmpty(),
  check("email", "Please enter a valid email").isEmail(),
  check(
    "password",
    "please password should have at least 5 characters"
  ).isLength({ min: 5 }),
];

router.post("/", postUserValidation, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  //Save User to db
  try {
    const { name, email, password } = req.body;
    let user = await User.findOne({ email: email });

    if (user) {
      return res.status(400).json({ errors: { msg: "User already Exists!" } });
    }

    user = new User({ name, email, password });

    //encrypt(hash) password
    const salt = await bcrypt.genSalt(10);
    const hash = await bcrypt.hash(password, salt);
    user.password = hash;
    user.save();
    console.log(user);

    return res
      .status(201)
      .json({ result: user, message: "User created successfully" });
  } catch (err) {
    console.error(err);
    return res.status(500).json({ errors: err });
  }
});

module.exports = router;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/d0410803-2f0f-49fb-993b-f7098e56bc17)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/bd212cd6-af50-4f65-bc34-1cce431cf03b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/cfe68738-62b7-4ab0-946d-238f888f2cd0)

</details>

<details>
  <summary>12. Generating JWT Tokens </summary>

# Install jsonwebtoken

```jsbs
npm install jsonwebtoken --save
```

# Generating JWT Token

```js
const privateKey = "12345";

jwt.sign({ id: 30 }, privateKey, function (err, token) {
  console.log(token);
});
```

# Verifying JWT token

```js
const privateKey = "12345";

jwt.verify(token, privateKey, function (err, decoded) {
  console.log(decoded.id); // 30
});
```

### x-shopy-ecommerce-app/server/config/keys.js:

```js
const mongoURI =
  "mongodb+srv://<username>:<password>@cluster0.qfv7ifn.mongodb.net/?retryWrites=true&w=majority";
const privateKey = "************";

module.exports = { mongoURI, privateKey };
```

### x-shopy-ecommerce-app/server/routes/userApi.js:

```jsbs
//generate token with payload
jwt.sign(
  payload,
  config.privateKey,
  {
    expiresIn: "1d", //3600 * 24
  },
  (err, token) => {
    if (err) {
      throw err;
    }
    return res.status(201).json({ token, msg: "User created successfully" });
  }
);
```

```js
const express = require("express");
const router = express.Router();
const { check, validationResult } = require("express-validator");
const bcrypt = require("bcryptjs");
const User = require("../models/User");
const jwt = require("jsonwebtoken");
const config = require("../config/keys");

router.get("/", (req, res) => {
  res.send("Users route");
});

const postUserValidation = [
  check("name", "Name is required").not().isEmpty(),
  check("email", "Please enter a valid email").isEmail(),
  check(
    "password",
    "please password should have at least 5 characters"
  ).isLength({ min: 5 }),
];

router.post("/", postUserValidation, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  //Save User to db
  try {
    const { name, email, password } = req.body;
    let user = await User.findOne({ email: email });

    if (user) {
      return res.status(400).json({ errors: { msg: "User already Exists!" } });
    }

    user = new User({ name, email, password });

    //encrypt password
    const salt = await bcrypt.genSalt(10);
    const hash = await bcrypt.hash(password, salt);
    user.password = hash;
    user.save();

    const payload = {
      user: {
        id: user.id,
        username: user.name,
      },
    };

    //generate token with payload
    jwt.sign(
      payload,
      config.privateKey,
      {
        expiresIn: "1d", //3600 * 24
      },
      (err, token) => {
        if (err) {
          throw err;
        }
        return res
          .status(201)
          .json({ token, msg: "User created successfully" });
      }
    );
  } catch (err) {
    console.error(err);
    return res.status(500).json({ errors: `Error creating user...${err}` });
  }
});

module.exports = router;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/c10bd937-65d5-4211-970d-43a1dbd7240c)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/38dd0f56-d711-4181-b4c7-7ece57891f44)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/c0723707-1ae2-4dd2-8b68-c0ee18f1fe21)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/3423af91-67b0-4448-860e-a7e18d4a2ff7)

</details>

<details>
  <summary>13. Protecting Routes with Auth Middleware </summary>

# Protecting Routes with Auth Middleware

### x-shopy-ecommerce-app/server/server.js:

```js
const express = require("express");
const app = express();
const connectDB = require("./config/db");
const PORT = process.env.PORT || 8000;

//Connect to the DB
connectDB();

//Define routes and API
app.use(express.json({ extended: false })); // allow req.body
app.use("/api/users", require("./routes/userApi"));
app.use("/api/products", require("./routes/productApi"));
app.use("/api/auth", require("./routes/authApi"));

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

### x-shopy-ecommerce-app/server/routes/authApi.js:

```js
const express = require("express");
const router = express.Router();
const auth = require("../middlewares/authMiddleware");
const User = require("../models/User");

router.get("/", auth, async (req, res) => {
  try {
    console.log(req.user);
    const user = await User.findById(req.user.id).select("-password");
    console.log(user);
    res.json(user);
  } catch (err) {
    if (err) {
      console.error(err.message);
      throw err;
    }
  }
  res.send("Auth route");
});

module.exports = router;
```

### x-shopy-ecommerce-app/server/middlewares/authMiddleware.js:

```js
const jwt = require("jsonwebtoken");
const config = require("../config/keys");

module.exports = function (req, res, next) {
  //get the token from the header if present
  // const token = req.headers["x-access-token"] || req.headers["authorization"];
  const token = req.header("x-auth-token");

  if (!token) {
    return res.status(401).json({ msg: "Access Denied. No Token provided." });
  }

  try {
    //if can verify the token, set req.user and pass to next middleware
    const decoded = jwt.verify(token, config.privateKey);
    console.log(decoded);
    req.user = decoded.user;
    next();
  } catch (err) {
    //if invalid token
    console.error(err);
    res.status(401).json({ msg: `Invalid Token. ${err.message}` });
  }
};
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/88e605b8-6a81-47cd-821f-d6cec971fb86)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/14e71b0e-c16d-4cde-9123-501d172736c5)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/0c899d2c-a716-469c-8e25-1249c2161e46)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/19127274-a9eb-40c9-9c8a-949c598ece2e)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b22c6622-2988-454e-ba68-6e578799e361)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/5cf7e07e-22e6-4bb0-a5f2-ea786e22faf2)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/99d59799-1786-48ea-b488-fe39d9254464)

</details>

<details>
  <summary>14. User Login Authentication </summary>

# User Login Authentication

### x-shopy-ecommerce-app/server/server.js:

```js
const express = require("express");
const app = express();
const connectDB = require("./config/db");
const PORT = process.env.PORT || 8000;

//Connect to the DB
connectDB();

//Define routes and API
app.use(express.json({ extended: false })); // allow req.body
app.use("/api/users", require("./routes/userApi"));
app.use("/api/products", require("./routes/productApi"));
app.use("/api/auth", require("./routes/authApi"));

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

### x-shopy-ecommerce-app/server/routes/authApi.js:

```js
const express = require("express");
const router = express.Router();
const { check, validationResult } = require("express-validator");
const auth = require("../middlewares/authMiddleware");
const User = require("../models/User");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const config = require("../config/keys");

router.get("/", auth, async (req, res) => {
  try {
    // console.log(req.user);
    const user = await User.findById(req.user.id).select("-password");
    // console.log(user);
    res.json(user);
  } catch (err) {
    if (err) {
      console.error(err.message);
      throw err;
    }
  }
  res.send("Auth route");
});

const postAuthValidation = [
  check("email", "Please enter a valid email").isEmail(),
  check("password", "password is required").exists(),
];

router.post("/", postAuthValidation, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const { email, password } = req.body;
    let user = await User.findOne({ email: email });

    if (!user) {
      return res
        .status(400)
        .json({ errors: { msg: "Invalid username or password!" } });
    }

    const match = await bcrypt.compare(password, user.password);

    if (!match) {
      return res
        .status(400)
        .json({ errors: { msg: "Invalid username or password!" } });
    }

    const payload = {
      user: {
        id: user.id,
      },
    };

    //generate token with payload
    jwt.sign(
      payload,
      config.privateKey,
      {
        expiresIn: "1d", //3600 * 24
      },
      (err, token) => {
        if (err) {
          throw err;
        }
        return res.status(200).json({ token });
      }
    );
  } catch (err) {
    console.error(err);
    return res.status(500).json({ errors: `Error logging in user...${err}` });
  }
});

module.exports = router;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/e9b928e3-a559-4b8e-b7d2-c90e92738d80)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/8ecd2032-f4a5-41c1-881b-6cb37ef3fcda)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b9d5418b-ea4a-4c6b-8b26-1b865b7faf9e)

</details>

<details>
  <summary>15. Creating Products Model </summary>

# Creating Products Model

### x-shopy-ecommerce-app/server/server.js:

```js
const express = require("express");
const app = express();
const connectDB = require("./config/db");
const PORT = process.env.PORT || 8000;

//Connect to the DB
connectDB();

//Define routes and API
app.use(express.json({ extended: false })); // allow req.body
app.use("/api/users", require("./routes/userApi"));
app.use("/api/products", require("./routes/productApi"));
app.use("/api/auth", require("./routes/authApi"));

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

### x-shopy-ecommerce-app/server/models/Product.js:

```js
const mongoose = require("mongoose");
const { Schema } = mongoose;
const ProductSchema = new Schema({
  userId: {
    type: Schema.Types.ObjectId,
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  category: {
    type: String,
    required: true,
  },
  price: {
    type: Number,
    required: true,
  },
  brand: {
    type: String,
  },
  quantity: {
    type: Number,
    required: true,
  },
  created: {
    type: Date,
    default: Date.now(),
  },
  updated: {
    type: Date,
    default: Date.now(),
  },
});

const Product = mongoose.model("Product", ProductSchema);
module.exports = Product;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/53884fd7-fe59-41de-b1a1-796ed73c289c)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/761e44dc-1a3d-48e9-b89f-2cf6ccf02af9)

</details>

<details>
  <summary>16. Validating and Creating Products API </summary>

# Validating and Creating Products API

### x-shopy-ecommerce-app/server/server.js:

```js
const express = require("express");
const app = express();
const connectDB = require("./config/db");
const PORT = process.env.PORT || 8000;

//Connect to the DB
connectDB();

//Define routes and API
app.use(express.json({ extended: false })); // allow req.body
app.use("/api/users", require("./routes/userApi"));
app.use("/api/products", require("./routes/productApi"));
app.use("/api/auth", require("./routes/authApi"));

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

### x-shopy-ecommerce-app/server/routes/productApi.js:

```js
const express = require("express");
const router = express.Router();
const { check, validationResult } = require("express-validator");
const auth = require("../middlewares/authMiddleware");
const Product = require("../models/Product");

router.get("/", (req, res) => {
  res.send("Product route");
});

const postProductValidation = [
  check("name", "Name is required").not().isEmpty(),
  check("description", "Description is required").not().isEmpty(),
  check("category", "Category is required").not().isEmpty(),
  check("price", "Price is required").not().isEmpty(),
  check("quantity", "Quantity is required").not().isEmpty(),
];

router.post("/", [auth, postProductValidation], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  //Save Products to db
  try {
    const { name, description, category, price, brand, quantity } = req.body;

    const newProduct = new Product({
      userId: req.user.id,
      name,
      description,
      category,
      price,
      brand,
      quantity,
    });

    const product = await newProduct.save();
    return res.status(200).json({ product });
  } catch (err) {
    console.error(err.message);
    return res
      .status(500)
      .json({ errors: `Error creating products...${err.message}` });
  }
});

module.exports = router;
```

### x-shopy-ecommerce-app/server/models/Product.js:

```js
const mongoose = require("mongoose");
const { Schema } = mongoose;
const ProductSchema = new Schema({
  userId: {
    type: Schema.Types.ObjectId,
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  category: {
    type: String,
    required: true,
  },
  price: {
    type: Number,
    required: true,
  },
  brand: {
    type: String,
  },
  quantity: {
    type: Number,
    required: true,
  },
  created: {
    type: Date,
    default: Date.now(),
  },
  updated: {
    type: Date,
    default: Date.now(),
  },
});

const Product = mongoose.model("Product", ProductSchema);
module.exports = Product;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/6e209482-4a2a-4690-9dbe-9be2deb21f3e)

</details>

<details>
  <summary>17. Get and Post Products API </summary>

# Get and Post Products API

### x-shopy-ecommerce-app/server/server.js:

```js
const express = require("express");
const app = express();
const connectDB = require("./config/db");
const PORT = process.env.PORT || 8000;

//Connect to the DB
connectDB();

//Define routes and API
app.use(express.json({ extended: false })); // allow req.body
app.use("/api/users", require("./routes/userApi"));
app.use("/api/products", require("./routes/productApi"));
app.use("/api/auth", require("./routes/authApi"));

app.get("/", (req, res) => {
  res.send("My App is running...");
});

app.listen(PORT, () => {
  console.log(`Server is listening on ${PORT}...`);
});
```

### x-shopy-ecommerce-app/server/routes/productApi.js:

```js
const express = require("express");
const router = express.Router();
const { check, validationResult } = require("express-validator");
const auth = require("../middlewares/authMiddleware");
const Product = require("../models/Product");

router.get("/", async (req, res) => {
  try {
    const products = await Product.find();
    res.status(200).json(products);
  } catch (err) {
    console.error(err.message);
    return res
      .status(500)
      .json({ errors: `Error fetching products...${err.message}` });
  }
});

router.get("/:id", async (req, res) => {
  try {
    const product = await Product.findById(req.params.id);
    if (!product) {
      return res.status(404).json({ msg: "Product not found" });
    }
    res.status(200).json(product);
  } catch (err) {
    console.error(err.message);
    return res
      .status(500)
      .json({ errors: `Error fetching product...${err.message}` });
  }
});

const postProductValidation = [
  check("name", "Name is required").not().isEmpty(),
  check("description", "Description is required").not().isEmpty(),
  check("category", "Category is required").not().isEmpty(),
  check("price", "Price is required").not().isEmpty(),
  check("quantity", "Quantity is required").not().isEmpty(),
];

router.post("/", [auth, postProductValidation], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  //Save Products to db
  try {
    const { name, description, category, price, brand, quantity } = req.body;

    const newProduct = new Product({
      userId: req.user.id,
      name,
      description,
      category,
      price,
      brand,
      quantity,
    });

    const product = await newProduct.save();
    return res.status(200).json({ product });
  } catch (err) {
    console.error(err.message);
    return res
      .status(500)
      .json({ errors: `Error creating products...${err.message}` });
  }
});

module.exports = router;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/a901f88d-4519-47c2-97e2-9e60fb6aba9b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/81be8782-604b-45d7-a316-f6deabdef03f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/e95937dd-c29b-4fb5-a30c-232cf6427072)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/e5d29326-73e9-40fa-a31e-5f9dafc3e1a3)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/6c3625bf-b47b-468f-bc4a-cbff26e7a7c8)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/505aea72-20b2-4142-b2ba-65e15d6ee78a)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/ab7264a9-eef9-488c-864b-cca9fd00c836)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/80a74388-061a-4f34-95a8-dc3f6e5f7c5e)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/c7352ae5-a2e8-43a3-8e0a-0dd1521db3c3)

</details>

+REACT FRONTEND

<details>
  <summary>18. Introduction </summary>

# Create React App

```jsbs
npx create-react-app client
```

# Start react app

```jsbs
cd client
npm run start 3000
```

### x-shopy-ecommerce-app/client/package.json:

```js
{
  "name": "client",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "@babel/plugin-proposal-private-property-in-object": "^7.21.10"
  }
}

```

### x-shopy-ecommerce-app/client/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

### x-shopy-ecommerce-app/client/src/App.js:

```js
import "./App.css";

function App() {
  return (
    <div className="App">
      <h1>E-Commerce Front end</h1>
    </div>
  );
}

export default App;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/c3d828d8-1064-4781-a27b-e74a84d75854)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/8035ad6b-837e-4c5b-80e8-260fe8ea7a67)

</details>

<details>
  <summary>19. Setup Redux and Redux Store </summary>

# Install Redux and Redux-thunk

```jsbs
npm i redux redux-thunk
npm install redux redux-thunk
```

### x-shopy-ecommerce-app/client/package.json:

```js
{
  "name": "client",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "redux": "^4.2.1",
    "redux-thunk": "^2.4.2",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "@babel/plugin-proposal-private-property-in-object": "^7.21.10"
  }
}

```

### x-shopy-ecommerce-app/client/src/store.js:

```js
import {
  legacy_createStore as createStore,
  applyMiddleware,
  compose,
} from "redux";
import thunk from "redux-thunk";
import rootReducer from "./reducers";

const initialState = {};
const middleware = [thunk];

let store;

try {
  store = createStore(
    rootReducer,
    initialState,
    compose(applyMiddleware(...middleware))
  );
} catch (error) {
  store = createStore(
    rootReducer,
    initialState,
    compose(applyMiddleware(...middleware))
  );
}

export default store;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/185e5d43-7165-44fd-84b5-5701106d6008)

</details>

<details>
  <summary>20. Setup Reducers and Actions </summary>

# Install Lodash

```jsbs
npm i lodash
```

```js

```

</details>
