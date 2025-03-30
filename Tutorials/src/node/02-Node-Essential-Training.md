## +Linkedin-Node Essential Training

## [COURSE](https://www.linkedin.com/learning/node-js-essential-training-14888164/learning-the-node-js-basics?resume=false)

<details>
<summary>1. Node Global Objects </summary>

# Node Global Objects

## [https://nodejs.org/api/globals.html](https://nodejs.org/api/globals.html)

![image](https://github.com/user-attachments/assets/e03b672a-ef3a-4bef-8a55-e7efdb5be969)

## Check Node Version

```js
node -v
```

### src-AI-Software/my_projects/10_Node_Essential_Training/global.js:

```js
const path = require("path");

global.console.log("This is the global.js File.");
console.log(__dirname);
console.log(__filename);

console.log(path.basename(__filename));
console.log(path.dirname(__filename));
console.log(path.join(__dirname, "index.js"));

for (let key in global) {
  console.log(key);
}
```

```x
This is the global.js File.
/Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/10_Node_Essential_Training
/Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/10_Node_Essential_Training/global.js

global.js
/Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/10_Node_Essential_Training
/Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/10_Node_Essential_Training/index.js

global
clearImmediate
setImmediate
clearInterval
clearTimeout
setInterval
setTimeout
queueMicrotask
structuredClone
atob
btoa
performance
fetch
navigator
crypto
```

# #END</details>

<details>
<summary>2. Node Process Objects </summary>

# Node Process Objects

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/global.js:

```js
console.log(process.argv);

function grab(flag) {
  let indexAfterFlag = process.argv.indexOf(flag) + 1;
  return process.argv[indexAfterFlag];
}

let username = grab("--username");
let password = grab("--password");

console.log(username);
console.log(password);

```

```x
[
  '/opt/homebrew/Cellar/node/22.4.0/bin/node',
  '/Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/10_Node_Essential_Training/APP/global.js',
  '--username',
  'admin',
  '--password',
  'admin123'
]


admin
admin123
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/0df1b0e1-27a6-4e4f-af32-360eb038d016">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/d5ce2817-d413-4ad3-82da-a769b5f9e037">

# #END</details>

<details>
<summary>3. Working with Standard Input and Output </summary>

# Working with Standard Input and Output 

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/global.js:

```js
// Write an output to Terminal
process.stdout.write("Hello World\n\n");
process.stdout.write("My name is:\nHenry");

// Quiz Example
const questions = [
  "What is your name?",
  "Where do you live?",
  "What is your preferred programming language",
];

const answers = [];

function ask(i = 0) {
  process.stdout.write(`\n\n\nQuestion ${i + 1}: ${questions[i]}`);
  process.stdout.write(` > `);
  process.stdout.write(`\nAnswer: `);
}

ask();

process.stdin.on("data", function (data) {
  let trimmedData = data.toString().trim();
  answers.push(trimmedData);
  process.stdout.write(trimmedData);

  if (questions.length > answers.length) {
    ask(answers.length);
  } else {
    process.stdout.write(`\n\n\nAnswers: ${answers.join(" | ")}`);
    process.exit();
  }
});

process.on("exit", function () {
  console.log("\nThank you!");
  console.log("Goodbye.");
});

```

```x
Hello World

My name is:
Henry


Question 1: What is your name? > 
Answer: Ifeanyi
Ifeanyi


Question 2: Where do you live? > 
Answer: Calgary
Calgary


Question 3: What is your preferred programming language > 
Answer: Python
Python


Answers: Ifeanyi | Calgary | Python
Thank you!
Goodbye.
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/1b2eb462-5f7b-45a4-90bb-18cdab5e6036">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/a0cc2c41-88ee-4f7d-9493-cb1a10e0c675">

# #END</details>

<details>
<summary>4. Using SetTimeout - Creating a Delay </summary>

# Using SetTimeout - Creating a Delay

```js
//setTimeout Global Method
const waitTime = 3000;

console.log(`setting a ${waitTime / 1000} second delay`);
const timerFinished = () => console.log("done");

setTimeout(timerFinished, waitTime);

```

```x
setting a 3 second delay
done
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/0cae78ba-a1c7-4ed5-bfcc-7342b60cbda4">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/59b54e2f-44d7-4f5e-aae1-8bee325dbb29">

# #END</details>

<details>
<summary>5. Using SetInterval Method with SetTimeout </summary>

# Using SetInterval Method with SetTimeout

```js
//setTimeout Global Method
const waitTime = 5000;
console.log(`setting a ${waitTime / 1000} second delay`);

const timerFinished = () => {
  clearInterval(interval);
  console.log(
    "Sorry, Time Limit Exceeded. You have to hang up or call back later."
  );
};

setTimeout(timerFinished, waitTime);

//setInterval Global Method
const waitInterval = 1000;
let currentTime = 0;

const incTime = () => {
  currentTime += waitInterval;
  console.log(`waiting on ${currentTime / 1000} seconds`);
};

const interval = setInterval(incTime, waitInterval);

```

```x
➜  APP git:(main) ✗ node global.js
setting a 5 second delay
waiting on 1 seconds
waiting on 2 seconds
waiting on 3 seconds
waiting on 4 seconds
Sorry, Time Limit Exceeded. You have to hang up or call back later.
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/053d56b9-e53f-4616-831d-c985f1b76e01">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/9ad27497-83a0-42e1-b5d3-81bda2758c8d">

# #END</details>

<details>
<summary>6. Reporting Progress for SetInterval </summary>

# Reporting Progress for SetInterval

```js
//setTimeout Global Method
const waitTime = 10000;
console.log(`setting a ${waitTime / 1000} second delay`);

const timerFinished = () => {
  clearInterval(interval);
  console.log("\nProcess Completed! Thank you!");
};

setTimeout(timerFinished, waitTime);

//setInterval Global Method
const waitInterval = 1000;
let currentTime = 0;

const incTime = () => {
  currentTime += waitInterval;
  const p = Math.floor((currentTime / waitTime) * 100);
  process.stdout.clearLine();
  process.stdout.cursorTo(0);
  process.stdout.write(`waiting.... ${p}%`);
};

const interval = setInterval(incTime, waitInterval);

```

```x
➜  APP git:(main) ✗ node global.js
setting a 10 second delay
waiting.... 90%
Process Completed! Thank you!

```

# #END</details>

<details>
<summary>7. Understanding Core Node Modules </summary>

# Understanding Core Node Modules

```js
const path = require("path");
const util = require("util");
const v8 = require("v8");

console.log(path.basename(__filename));
console.log(path.dirname(__filename));
console.log(path.extname(__filename));
console.log(path.parse(__filename));
console.log(path.resolve(__filename));
console.log(path.sep);
console.log(path.delimiter);

const dirUploads = path.join(__dirname, "www", "files", "uploads");

console.log(dirUploads);
util.log(dirUploads);
util.log(path.basename(__filename));
util.log(v8.getHeapStatistics());
```

### console.log(path.parse(__filename));

```x
{
  root: '/',
  dir: '/Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/10_Node_Essential_Training/APP',
  base: 'global.js',
  ext: '.js',
  name: 'global'
}
```

### console.log(path.basename(__filename));

```x
global.js
```

### console.log(path.dirname(__filename));

```x
/Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/10_Node_Essential_Training/APP
```

### console.log(path.extname(__filename));

```x
.js
```

### console.log(path.resolve(__filename));

```x
/Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/10_Node_Essential_Training/APP/global.js
```

### console.log(path.sep);

```x
/
```

### console.log(path.delimiter);

```x
:
```

```js
const dirUploads = path.join(__dirname, "www", "files", "uploads");

console.log(dirUploads);
util.log(dirUploads);
util.log(path.basename(__filename));
util.log(v8.getHeapStatistics());
```

```x
/Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/10_Node_Essential_Training/APP/www/files/uploads
13 Jul 12:34:38 - /Users/ifeanyiomeata/Desktop/SERVER/projects/src-AI-Software/my_projects/10_Node_Essential_Training/APP/www/files/uploads
13 Jul 12:34:38 - global.js
13 Jul 12:34:38 - {
  total_heap_size: 4947968,
  total_heap_size_executable: 524288,
  total_physical_size: 4702208,
  total_available_size: 2195260616,
  used_heap_size: 3386856,
  heap_size_limit: 2197815296,
  malloced_memory: 163968,
  peak_malloced_memory: 253952,
  does_zap_garbage: 0,
  number_of_native_contexts: 1,
  number_of_detached_contexts: 0,
  total_global_handles_size: 8192,
  used_global_handles_size: 2336,
  external_memory: 1399967
}
```

# #END</details>

<details>
<summary>8. Collecting Information with Readline </summary>

# Collecting Information with Readline

```js
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// rl.question("How do you like Node?", (answer) => {
//   console.log(`Your answer: ${answer}`);
// });

function collectAnswers(questions, done) {
  const answers = [];
  const [firstQuestion] = questions;

  const questionAnswered = (answer) => {
    answers.push(answer.trim());
    if (answers.length < questions.length) {
      rl.question(questions[answers.length], questionAnswered);
    } else {
      return done(answers);
    }
  };

  rl.question(firstQuestion, questionAnswered);
}

const questions = [
  "What is your name?",
  "Where do you live?",
  "What are you going to do with Node.js?",
];

collectAnswers(questions, (answers) => {
  console.log("Thank you for your answers!");
  console.log(answers);
  process.exit();
});

```

```x
➜  APP git:(main) ✗ node global.js
What is your name? Ifeanyi
Where do you live? Calgary
What are you going to do with Node.js? Code
Thank you for your answers!
[ 'Ifeanyi', 'Calgary', 'Code' ]
```

# #END</details>

<details>
<summary>9. Exporting Custom Modules </summary>

# Exporting Custom Modules

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/myModule.js:

```js
let count = 0;

const inc = () => ++count;
const dec = () => --count;

const getCount = () => count;

module.exports = {
  anything: true,
  who: "Bill",
  count,
  inc,
  dec,
  getCount,
};

```

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const myModule = require("./myModule");
const { inc, dec, getCount } = require("./myModule");

inc();
inc();
inc();

console.log(myModule.anything);
console.log(myModule.who);
console.log(`the count is ${getCount()}`);

```

```x
➜  APP git:(main) ✗ node app
true
Bill
the count is 3
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/27215543-4159-4004-81c3-6e996ea1bef0">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/19977baf-2b46-470a-aeea-3a83c3a71a1c">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/392dad82-ded3-4582-a632-69e2c1922e0c">

# #END</details>

<details>
<summary>10. Using EventEmmiters to create Listeners for Custom Events </summary>

# Using EventEmmiters to create Listeners for Custom Events

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const events = require("events");

let emitter = new events.EventEmitter();

emitter.on("customEvent", (user, message) => {
  console.log(`${user}: ${message}`);
});

emitter.emit("customEvent", "Computer", "Hello World");
emitter.emit("customEvent", "Eve", "That's pretty cool");

process.stdin.on("data", (data) => {
  const input = data.toString().trim();
  if (input === "exit") {
    emitter.emit("customEvent", "process", "Goodbye!");
    process.exit();
  }
  emitter.emit("customEvent", "terminal", data.toString().trim());
});

```

```x
➜  APP git:(main) ✗ node app
Computer: Hello World
Eve: That's pretty cool
Hello
terminal: Hello
How are you?
terminal: How are you?
It's me Ifeanyi
terminal: It's me Ifeanyi
exit
process: Goodbye!
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/ec494ec4-522c-4314-931c-e3e576826442">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/94799bff-9690-4213-932b-d85c87d293bc">

# #END</details>

<details>
<summary>11. Setup Custom Modules with Exports </summary>

# Setup Custom Modules with Exports

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/lib/collectAnswers.js:

```js
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

module.exports = (questions, done) => {
  const answers = [];
  const [firstQuestion] = questions;

  const questionAnswered = (answer) => {
    answers.push(answer.trim());
    if (answers.length < questions.length) {
      rl.question(questions[answers.length], questionAnswered);
    } else {
      return done(answers);
    }
  };

  rl.question(firstQuestion, questionAnswered);
};

```

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const collectAnswers = require("./lib/collectAnswers");

const questions = [
  "What is your name?",
  "Where do you live?",
  "What are you going to do with Node.js?",
];

collectAnswers(questions, (answers) => {
  console.log("Thank you for your answers!");
  console.log(answers);
  process.exit();
});

```

```x
➜  APP git:(main) ✗ node app
What is your name? Ifeanyi
Where do you live? Calgary
What are you going to do with Node.js? Code all Day
Thank you for your answers!
[ 'Ifeanyi', 'Calgary', 'Code all Day' ]
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/a23335d9-c440-4489-b660-10fd5cf082c9">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/eabe455c-1ed1-4efe-9e90-71558d18ebe2">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/a91dd7a3-1884-4ccf-8aef-89dd50f806a4">

# #END</details>

<details>
<summary>12. Setup Custom Event Modules with EventEmitters </summary>

# Setup Custom Event Modules with EventEmitters

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/lib/collectAnswers.js:

```js
const readline = require("readline");
const { EventEmitter } = require("events");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

module.exports = (questions, done) => {
  const answers = [];
  const [firstQuestion] = questions;

  const emitter = new EventEmitter();

  const questionAnswered = (answer) => {
    emitter.emit("answer", answer);
    answers.push(answer.trim());
    if (answers.length < questions.length) {
      rl.question(questions[answers.length], questionAnswered);
    } else {
      return done(answers);
    }
  };

  rl.question(firstQuestion, questionAnswered);
  return emitter;
};

```

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const collectAnswers = require("./lib/collectAnswers");

const questions = [
  "What is your name?",
  "Where do you live?",
  "What are you going to do with Node.js?",
];

const answerEvents = collectAnswers(questions, (answers) => {
  console.log("Thank you for your answers!");
  console.log(answers);
  process.exit();
});

answerEvents.on("answer", (answer) => console.log(`The answer is ${answer}`));

```

```x
➜  APP git:(main) ✗ node app
What is your name? Ifeanyi
The answer is  Ifeanyi
Where do you live? Calgary
The answer is  Calgary
What are you going to do with Node.js? Code Everyday
The answer is  Code Everyday
Thank you for your answers!
[ 'Ifeanyi', 'Calgary', 'Code Everyday' ]
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/7c6c12e1-f62c-4aed-bea1-ea429f5ea873">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/8b3ce17f-90e8-4d81-8e48-b499b8d0298b">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/f06f1203-9806-4e38-b01c-74ec76a56c57">

# #END</details>

<details>
<summary>13. Files - Listing Directory Files </summary>

# Files - Listing Directory Files

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const fs = require("fs");
const { readdir } = fs.promises;

async function listFiles() {
  try {
    const files = await readdir("./");
    console.log(files);
  } catch (err) {
    throw err;
  }
}

listFiles();
console.log("listing files...");
```

### With CallBack Function

```js
const fs = require("fs");

fs.readdir("./", function (err, files) {
  if (err) {
    throw err;
  }
  console.log(files);
});

console.log("listing files...");
```

```x
➜  APP git:(main) ✗ node app
listing files...
[ 'app.js', 'lib', 'myModule.js' ]
```

# #END</details>

<details>
<summary>14. Files - Reading from Directory Files </summary>

# Files - Reading from Directory Files

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/readme.md:

```md
# Publisher: District Homes

## Topic: The Ocean Tides Project

Description: This project is a simple demonstration of how to use Node.js to read a file from the file system and write it to the console.
The project uses the fs module to read the file and the console.log method to write it to the console.

```

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const fs = require("fs");
const { readFile } = fs.promises;

async function readFiles() {
  try {
    let file = await readFile("./readme.md", "UTF-8");
    console.log(file);
  } catch (err) {
    // console.log(err);
    throw err;
  }
}

readFiles();
console.log("reading the file...");

```

### With Callback Function

```js
const fs = require("fs");

// let ipsum = fs.readFileSync("./readme.md", "UTF-8");

fs.readFile("./readme.md", "UTF-8", (err, ipsum) => {
  if (err) {
    throw err;
  }
  console.log(ipsum);
});

console.log("reading the file...");
```

```x
➜  APP git:(main) ✗ node app
reading the file...
# Publisher: District Homes

## Topic: The Ocean Tides Project

Description: This project is a simple demonstration of how to use Node.js to read a file from the file system and write it to the console.
The project uses the fs module to read the file and the console.log method to write it to the console.
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/d3b1214a-75c5-43da-8d3e-4b5d5ff59e4b">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/bc5f75d4-8d36-4ddf-a400-4dc20f72ccc1">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/992a307a-af5c-4c7f-9a82-6cc72a57e135">

# #END</details>

<details>
<summary>15. Files - Writing and Appending Files </summary>

# Files - Writing and Appending Files

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const fs = require("fs");
const { writeFile, appendFile } = fs.promises;

let message = `
    This is a New File
    ==================

    ES6 Template Strings are cool. They honor whitespace.

    * Template Strings
    * Node File System
    * Readline CLIs
`;

async function createFile() {
  try {
    await writeFile("newReadme.md", message.trim());
    console.log("Markdown Created");
    await appendFile("newReadme.md", "\n\n### Node.js Everyone!");
    console.log("Markdown Modified");
  } catch (err) {
    console.log(err);
  }
}

createFile();

```

### With Callback Function

```js
const fs = require("fs");

let message = `
    This is a New File
    ==================

    ES6 Template Strings are cool. They honor whitespace.

    * Template Strings
    * Node File System
    * Readline CLIs
`;

fs.writeFile("newReadme.md", message.trim(), function (err) {
  if (err) {
    throw err;
  }
  fs.appendFileSync("newReadme.md", "\n\n### Node.js Everyone!");
  console.log("Markdown Created");
});

```

```x
➜  APP git:(main) ✗ node app
Markdown Created
Markdown Modified
```

```x
This is a New File
    ==================

    ES6 Template Strings are cool. They honor whitespace.

    * Template Strings
    * Node File System
    * Readline CLIs

### Node.js Everyone!
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/7aded802-861d-4e48-97f2-8f13adf4a277">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/3a3aab5f-71d1-4068-bfd9-7c74ed56cf87">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/684b3907-86db-4269-9b4c-129032cdf45e">

# #END</details>

<details>
<summary>16. Files - Creating Directories </summary>

# Files - Creating Directories

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const fs = require("fs");
const path = require("path");
const { access, mkdir } = fs.promises;

async function createDir(dir) {
  dir = path.join(__dirname, dir);
  try {
    await access(dir);
    console.log("Directory is already there!");
    return true;
  } catch (err) {
    try {
      console.log("Creating new directory...");
      return await mkdir(dir);
    } catch (err) {
      console.log(`ERROR: ${err}`);
    }
  }
}

createDir("your-files-here");

```

### With CallBack Function

```js
const fs = require("fs");

if (fs.existsSync("your-files-here")) {
  console.log("already there!");
} else {
  fs.mkdir("your-files-here", function (err) {
    if (err) {
      console.log(`ERROR: ${err}`);
    } else {
      console.log("directory created");
    }
  });
}

```

```x
➜  APP git:(main) ✗ node app
Directory is already there!
➜  APP git:(main) ✗ node app
Creating new directory...
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/32304031-25ec-45e3-8489-1fa4533468ef">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/55c0fd93-160b-440c-bb56-66fd41576099">

# #END</details>

<details>
<summary>17. Files - Renaming, Moving and Removing Files </summary>

# Files - Renaming, Moving and Removing Files

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const fs = require("fs");

//Rename Files
fs.renameSync("./newReadme.md", "./firstReadme.md");

console.log("Markdown file renamed");

//Move Files
fs.rename("./readme.md", "./your-files-here/readme.md", function (err) {
  if (err) {
    throw err;
  }
  console.log("Markdown file moved");
});

//Remove Files
fs.unlinkSync("./your-files-here/test1.txt");

fs.unlink("./your-files-here/test2.txt", function (err) {
  if (err) {
    throw err;
  }
  console.log("Notes are gone");
});

```

```x
➜  APP git:(main) ✗ node app
Markdown file renamed
Markdown file moved
Notes are gone
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/6ae50f3f-256d-4404-888c-51cadced4022">

# #END</details>

<details>
<summary>18. Files - Renaming, Moving and Removing Directories </summary>

# Files - Renaming, Moving and Removing Directories

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const fs = require("fs");

//Move Folder
fs.renameSync("./assets/logs", "accounts/logs");
console.log("logs folder moved");

//Remove Folder
fs.rmdir("./assets", function (err) {
  if (err) {
    console.log(err);
  } else {
    console.log("assets directory removed");
  }
});

//Remove Folder that has files or folders in it
fs.readdirSync("./accounts").forEach((file) => {
  fs.renameSync(`./accounts/${file}`, `./bin/${file}`);
});
console.log("Files Removed");
fs.rmdirSync("./accounts");
console.log("Folder Removed");

```

```js
➜  APP git:(main) ✗ node app
logs folder moved
Files Removed
Folder Removed
assets directory removed
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/e97e4e6c-18a6-4e92-941d-3a026cbfec43">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/03193c83-c18e-4676-b414-be351c12d89c">

# #END</details>

<details>
<summary>19. Files - Readable file streams </summary>

# Files - Readable file streams

## Reading Without Streams

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const fs = require("fs");

fs.readFile("./chat-logs/team-chat.log", "UTF-8", (err, chatLog) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(`File Read ${chatLog.length}`);
  console.log("==========");
  console.log(chatLog);
});

console.log("Reading the file");

```

```x
➜  APP git:(main) ✗ node app
Reading the file
File Read 106
==========
Hello George!
Hello Ben!
What's happening?
Not much, just discovering electricity.
That's rad. Keep it up.
```

## Reading With Streams

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const fs = require("fs");

let stream = fs.createReadStream("./chat-logs/team-chat.log", "UTF-8");

let data;

stream.once("data", (chunk) => {
  console.log("read stream started");
  console.log("==========");
  console.log(chunk);
});

stream.on("data", (chunk) => {
  console.log(`chunk: ${chunk.length}`);
  data += chunk;
});

stream.on("end", () => {
  console.log(`finished ${data.length}`);
});

console.log("Reading the file");

```

```x
➜  APP git:(main) ✗ node app
Reading the file
read stream started
==========
Hello George!
Hello Ben!
What's happening?
Not much, just discovering electricity.
That's rad. Keep it up.
chunk: 106
finished 115
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/48f318d3-f204-4f9d-b25c-b9e3c05e7753">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/1f37c179-946c-4ff9-ac82-d213d872afcf">

# #END</details>

<details>
<summary>20. Files - Writable file streams </summary>

# Files - Writable file streams

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/app.js:

```js
const fs = require("fs");

let answerStream;

let questions = [
  "What is your name?",
  "What would you rather be doing?",
  "What is your preferred programming language?",
];

let answers = [];

function ask(i) {
  process.stdout.write(`\n\n\n\n  ${questions[i]}`);
  process.stdout.write(`  >  `);
}

process.stdin.once("data", (data) => {
  let name = data.toString().trim();
  let fileName = `./${name}.md`;
  if (fs.existsSync(fileName)) {
    fs.unlinkSync(fileName);
  }
  answerStream = fs.createWriteStream(fileName);
  answerStream.write(`Question Answers for ${name}\n========\n`);
});

process.stdin.on("data", function (data) {
  let answer = data.toString().trim();

  answerStream.write(`Question: ${questions[answers.length]}\n`);

  answerStream.write(`Answer: ${answer}\n`, function () {
    if (answers.length < questions.length) {
      ask(answers.length);
    } else {
      process.exit();
    }
  });

  answers.push(answer);
});

process.on("exit", function () {
  answerStream.close();
  process.stdout.write("\n\n\n\n  ");
  process.stdout.write(
    `Go ${answers[1]} ${answers[0]} you can finish writing ${answers[2]} later!`
  );
  process.stdout.write("\n\n\n\n");
});

ask(answers.length);

```

```x
➜  APP git:(main) ✗ node app

  What is your name?  >  Ifeanyi

  What would you rather be doing?  >  Studying

  What is your preferred programming language?  >  Python

  Go Studying Ifeanyi you can finish writing Python later!
```

### src-AI-Software/my_projects/10_Node_Essential_Training/APP/Ifeanyi.md:

```md
Question Answers for Ifeanyi
========
Question: What is your name?
Answer: Ifeanyi
Question: What would you rather be doing?
Answer: Studying
Question: What is your preferred programming language?
Answer: Python
```

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/cf205b95-5b12-45c0-b9fa-8bc167ec74e0">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/446e38ef-580a-4fa0-8be9-1c8c78da908d">
<img width="1491" alt="image" src="https://github.com/user-attachments/assets/dc98b147-6650-42ee-b1a6-ace5e2ac37f0">

# #END</details>

# #END
