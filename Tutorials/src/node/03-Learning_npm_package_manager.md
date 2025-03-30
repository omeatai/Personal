## +Linkedin-Learning_npm_package_manager

## [COURSE](https://www.linkedin.com/learning/learning-npm-a-package-manager/learning-npm?resume=false)

<details>
<summary>1. Initializing Node Packages </summary>

# Initializing Node Packages

```x
npm init -y
```

```x
➜  01_learning_npm git:(main) npm init -y
Wrote to /Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/01_learning_npm/package.json:

{
  "name": "01_learning_npm",
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

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/db6e67b7-658e-4582-91ab-35dcc38066c7">

# #END</details>

<details>
<summary>2. Installing Dependencies </summary>

# Installing Dependencies

## Installing Main Dependencies

```x
npm install express
npm install --save express
npm install -S express
```

## Installing Dev Dependencies

```x
npm install --save-dev babel cli
npm install -D babel cli 
```

```json
{
  "name": "01_learning_npm",
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
    "express": "^4.19.2"
  },
  "devDependencies": {
    "babel": "^6.23.0",
    "cli": "^1.0.1"
  }
}

```

## Installing Dependencies globally to use in your projects

```x
npm install -g create-react-app 
create-react-app crud-app 
cd crud-app
npm install --save axios react-bootstrap bootstrap
```

## Installing Dependencies globally temporarily (use once)

```x
npx create-react-app crud-app 
```

# #END</details>

<details>
<summary>3. Updating a Dependency </summary>

# Updating a Dependency

### Checking packages that are outdated

```x
npm outdated
npm outdated -g
```

### Installing latest versions

```x
npm install eslint@8.32.0
npm install eslint@latest
 
npm install -g npm@10.8.2
npm install -g npm@latest 
```

# #END</details>

<details>
<summary>4. Removing a Dependency </summary>

# Removing a Dependency

```x
npm install eslint
npm uninstall eslint

npm install --save-dev nodemon
npm uninstall --save-dev nodemon
```

# #END</details>

<details>
<summary>5. Semantic Versioning </summary>

# Semantic Versioning

![image](https://github.com/user-attachments/assets/ec509056-a85c-4d16-b6b0-c57b064ef563)
![image](https://github.com/user-attachments/assets/76089f2d-12fd-4037-9559-8a9d5f1f3dd8)
![image](https://github.com/user-attachments/assets/6369203a-e99a-46cd-9ac0-98b199548ed3)
![image](https://github.com/user-attachments/assets/93f9237a-1f26-4ffe-bf9e-0951c51e68df)

# #END</details>

<details>
<summary>6. Publishing Packages to npm.js </summary>

# Publishing Packages to npm.js

## Publishing an unscoped Package

```x
# Check if the path installs on another directory in your local system
npm install /Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/01_learning_npm/

# Publish unscoped Package
npm publish
```

## Publishing a scoped Package

```x
# Initializing npm package
npm init -scope=@ifeanyiomeata
npm publish -access public
```

## Publishing a private Package

```x
# Initializing npm package
npm init -scope=@ifeanyiomeata
npm publish
```

# #END</details>

<details>
<summary>7. Optimizing npm Cache </summary>

# Optimizing npm Cache

## Verify that there is no problem with the cache

```x
npm cache verify
```

## Clean the Cache

```x
npm cache clean --force
```

# #END</details>

<details>
<summary>8. Audit npm </summary>

# Audit npm

```x
npm install socket.io
npm audit
```

```x
npm audit fix
```

# #END</details>

<details>
<summary>9. Scripting in package.json </summary>

# Scripting in package.json

## Install babel Packages

```js
npm uninstall --save-dev babel cli
npm install --save-dev @babel/cli @babel/core @babel/node @babel/preset-env
```

## Install nodemon

```js
npm install --save-dev nodemon
```

### src-AI-Software/my_projects/01_learning_npm/package.json:

```json
{
  "name": "01_learning_npm",
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
    "express": "^4.19.2",
    "socket.io": "^4.7.5"
  },
  "devDependencies": {
    "@babel/cli": "^7.24.8",
    "@babel/core": "^7.24.9",
    "@babel/node": "^7.24.8",
    "@babel/preset-env": "^7.24.8",
    "nodemon": "^3.1.4"
  }
}
```

### src-AI-Software/my_projects/01_learning_npm/index.js:

```js
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("<h1>This is the Index App: Hello World!</h1>");
});

app.listen(3000, () => {
  console.log("Index app listening on port 3000!");
});

```

![image](https://github.com/user-attachments/assets/b95dbeb3-be8c-4bac-8ff5-ae98a6912677)

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/0a277873-9119-43a7-ba72-bc9799bd5216">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/8f0fe5ed-e7ec-4aa9-99c3-bb98db637d56">

# #END</details>

<details>
<summary>10. Running npx with package and scripts </summary>

# Running npx with package and scripts

### src-AI-Software/my_projects/01_learning_npm/package.json:

```json
{
  "name": "01_learning_npm",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon ./index.js --exec babel-node",
    "create-angular-app": "npx -p @angular/cli ng new myapp"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2",
    "socket.io": "^4.7.5"
  },
  "devDependencies": {
    "@babel/cli": "^7.24.8",
    "@babel/core": "^7.24.9",
    "@babel/node": "^7.24.8",
    "@babel/preset-env": "^7.24.8",
    "nodemon": "^3.1.4"
  }
}
```

```x
npm run create-angular-app
```

```js
npx -p @angular/cli ng new myapp
cd myapp
```

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/f364ef74-bb70-4978-adcc-b266730e5b34">

# #END</details>

# #END
