# TYPESCRIPT TUTORIAL - TRAVESY MEDIA

## [COURSE](https://www.youtube.com/watch?v=BCg4U1FzODs&ab_channel=TraversyMedia)

<details>
  <summary>1. Introduction </summary>

# Introduction

# Install Typescript globally

```x
sudo npm i -g typescript
```

# Get current Typescript Version

```x
tsc -v
```

<img width="1211" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/058ab52d-783f-4cfc-8961-5a4dacee5f5a">
<img width="1211" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/721c660a-353a-4112-ab67-e952b85c84a2">


# #END </details>

<details>
  <summary>2. Compiling to javascript </summary>

# Compiling to javascript

```x
tsc index
tsc --watch index
```

### TS/crash-course/index.ts:

```ts
let personId: number = 12;
let firstName: string = "John";
let isDeleted: boolean = false;
```

### TS/crash-course/index.js:

```ts
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var personId = 12;
var firstName = "John";
var isDeleted = false;
```

<img width="1385" alt="image" src="https://github.com/user-attachments/assets/7dd3427d-772f-401f-8aad-ae493362343c">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/33cb7d56-9060-4f3e-beda-7b46db55f170">

# #END </details>

<details>
  <summary>3. Setup Typescript Config File </summary>

# Setup Typescript Config File

## Initialize File

```x
tsc --init
```

```x
➜  02_ts_proj tsc --init

Created a new tsconfig.json with:                                                                                       
                                                                                                                     TS 
  target: es2016
  module: commonjs
  strict: true
  esModuleInterop: true
  skipLibCheck: true
  forceConsistentCasingInFileNames: true

You can learn more at https://aka.ms/tsconfig
```

# Make changes to Config Options

### dev_projects/02_ts_proj/tsconfig.json:

```json
"target": "ES6" /* Set the JavaScript language version for emitted JavaScript and include compatible library declarations. */,
"rootDir": "./src" /* Specify the root folder within your source files. */,
 "outDir": "./dist" /* Specify an output folder for all emitted files. */,
```

### dev_projects/02_ts_proj/src/index.ts:

```ts
let personId: number = 12;
let firstName: string = "John";
let isDeleted: boolean = false;
let age: number | null = null;

console.log({ personId, firstName, isDeleted, age });
```

### dev_projects/02_ts_proj/dist/index.js:

```js
"use strict";
let personId = 12;
let firstName = "John";
let isDeleted = false;
let age = null;
console.log({ personId, firstName, isDeleted, age });
```

### dev_projects/02_ts_proj/dist/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Website</title>
  </head>
  <body>
    <h1>Welcome, World!</h1>
    <script src="./index.js"></script>
  </body>
</html>
```

# Run to Compile

```x
tsc --watch
```

![image](https://github.com/user-attachments/assets/3e5756c6-d765-4df8-a043-2c9929c8b6a6)

<img width="1341" alt="image" src="https://github.com/user-attachments/assets/266eb74f-2d2e-4db8-81a6-67f8a20edc15">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/0ff85a6b-5ec7-4b97-b7b1-43e5d5b16a5e">

# #END </details>

<details>
  <summary>4. Basic Typescript Types </summary>

# Basic Typescript Types

### dev_projects/02_ts_proj/src/index.ts:

```ts
// TS Simple Variables
let personId: number = 5;
let firstName: string = "John";
let isDeleted: boolean = false;
let age: number | null = null;
let x: any = "Hello";

// TS Objects
let personObj: {
  personId: number;
  firstName: string;
  isDeleted: boolean;
  age: number | null;
} = {
  personId: 1,
  firstName: "John",
  isDeleted: false,
  age: null,
};

// TS Arrays/Lists
let peopleArr: Array<string> = ["John", "Jane", "Jenny"];
let peopleArr2: string[] = ["John", "Jane", "Jenny"];
let personArr: [number, string, boolean, number | null] = [
  5,
  "John",
  false,
  null,
];

// TS Arrays/Lists of Objects
let peopleArr3: {
  personId: number;
  firstName: string;
  isDeleted: boolean;
  age: number | null;
}[] = [
  {
    personId: 1,
    firstName: "John",
    isDeleted: false,
    age: null,
  },
  {
    personId: 2,
    firstName: "Jane",
    isDeleted: false,
    age: null,
  },
];

// TS Arrays/Lists of Arrays (Tuple Array)
let peopleArr4: [number, string, boolean, number | null][] = [
  [5, "John", false, null],
  [6, "Jane", false, null],
];

```

### dev_projects/02_ts_proj/dist/index.js:

```js
"use strict";
// TS Simple Variables
let personId = 5;
let firstName = "John";
let isDeleted = false;
let age = null;
let x = "Hello";
// TS Objects
let personObj = {
    personId: 1,
    firstName: "John",
    isDeleted: false,
    age: null,
};
// TS Arrays/Lists
let peopleArr = ["John", "Jane", "Jenny"];
let peopleArr2 = ["John", "Jane", "Jenny"];
let personArr = [
    5,
    "John",
    false,
    null,
];
// TS Arrays/Lists of Objects
let peopleArr3 = [
    {
        personId: 1,
        firstName: "John",
        isDeleted: false,
        age: null,
    },
    {
        personId: 2,
        firstName: "Jane",
        isDeleted: false,
        age: null,
    },
];
// TS Arrays/Lists of Arrays (Tuple Array)
let peopleArr4 = [
    [5, "John", false, null],
    [6, "Jane", false, null],
];

```

<img width="1341" alt="image" src="https://github.com/user-attachments/assets/9ed9d74f-fda6-4a6c-a5d1-5247a9dfc732">


# #END </details>

<details>
  <summary>5. Using TS Unions and Enums </summary>

# Using TS Unions and Enums

### dev_projects/02_ts_proj/src/index.ts:

```ts
// Union
let pid: string | number;
pid = "22";
pid = 22;

// Enum
enum Direction1 {
  Up = 1,
  Down,
  Left,
  Right,
}

console.log(Direction1.Up); // 1
console.log(Direction1.Down); // 2

enum Direction2 {
  Up = "Up",
  Down = "Down",
  Left = "Left",
  Right = "Right",
}

console.log(Direction2.Up); // Up
console.log(Direction2.Down); // Down
```

### TS/crash-course/dist/index.js:

```ts
"use strict";
// Union
let pid;
pid = "22";
pid = 22;
// Enum
var Direction1;
(function (Direction1) {
    Direction1[Direction1["Up"] = 1] = "Up";
    Direction1[Direction1["Down"] = 2] = "Down";
    Direction1[Direction1["Left"] = 3] = "Left";
    Direction1[Direction1["Right"] = 4] = "Right";
})(Direction1 || (Direction1 = {}));
console.log(Direction1.Up); // 1
console.log(Direction1.Down); // 2
var Direction2;
(function (Direction2) {
    Direction2["Up"] = "Up";
    Direction2["Down"] = "Down";
    Direction2["Left"] = "Left";
    Direction2["Right"] = "Right";
})(Direction2 || (Direction2 = {}));
console.log(Direction2.Up); // Up
console.log(Direction2.Down); // Down
```

![image](https://github.com/user-attachments/assets/fb93ec8d-b0e1-4285-86c4-1576f9eeeb9a)
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/94a6bcb8-a031-4080-92e2-5941a5e777d5">

# #END </details>

<details>
  <summary>6. Typescript Objects </summary>

# Typescript Objects

### dev_projects/02_ts_proj/src/index.ts:

```ts
// Objects

const user1: {
  id: number;
  name: string;
} = {
  id: 1,
  name: "John",
};

// Setting Type
type User = {
  id: number;
  name: string;
};

const user2: User = {
  id: 1,
  name: "John",
};
```

### dev_projects/02_ts_proj/dist/index.js:

```ts
"use strict";
// Objects
const user1 = {
    id: 1,
    name: "John",
};
const user2 = {
    id: 1,
    name: "John",
};
```

<img width="1385" alt="image" src="https://github.com/user-attachments/assets/dae85c76-6d4f-46b1-9fe8-0774aed49133">

# #END </details>

<details>
  <summary>7. Type Assertion on Any-Type </summary>

# Type Assertion on Any-Type

### dev_projects/02_ts_proj/src/index.ts:

```ts
// Type Assertion
let cid: any = 1;

let customerId1 = <number>cid;
let customerId2 = cid as number;

customerId1 = 2;
customerId2 = 3;
```

### dev_projects/02_ts_proj/dist/index.js:

```ts
"use strict";
// Type Assertion
let cid = 1;
let customerId1 = cid;
let customerId2 = cid;
customerId1 = 2;
customerId2 = 3;
```

<img width="1341" alt="image" src="https://github.com/user-attachments/assets/e798ae1e-aec8-4054-b2ed-683f1c6237c1">


# #END </details>

<details>
  <summary>8. Typescript Functions </summary>

# Typescript Functions

### TS/crash-course/src/index.ts:

```ts
// Type Assertion
// Functions
function addNum(x: number, y: number): number {
  return x + y;
}

console.log(addNum(1, 2));

// Void
function log(message: string | number): void {
  console.log(message);
}

log("Hello");

```

### TS/crash-course/dist/index.js:

```ts
"use strict";
// Type Assertion
// Functions
function addNum(x, y) {
    return x + y;
}
console.log(addNum(1, 2));
// Void
function log(message) {
    console.log(message);
}
log("Hello");

```

![image](https://github.com/user-attachments/assets/93154194-8ab0-48b6-b1dd-accfe054d765)

<img width="1385" alt="image" src="https://github.com/user-attachments/assets/669f922c-5da0-40b8-8e23-ddb6e1e7b9a6">

# #END </details>

<details>
  <summary>9. Typescript Interfaces </summary>

# Typescript Interfaces

### TS/crash-course/src/index.ts:

```ts
// Interfaces
interface UserInterface {
  readonly id: number;
  name: string;
  age?: number;
}

const user1: UserInterface = {
  id: 1,
  name: "John",
};

//Type
type Point = number | string;
const p1: Point = 1;

// Interface with Functions
interface MathFunc {
  (x: number, y: number): number;
}

const add: MathFunc = (x: number, y: number): number => x + y;
const sub: MathFunc = (x: number, y: number): number => x - y;
```

### TS/crash-course/dist/index.js:

```ts
"use strict";
const user1 = {
    id: 1,
    name: "John",
};
const p1 = 1;
const add = (x, y) => x + y;
const sub = (x, y) => x - y;
```

<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ca4211fc-8bd2-4aa7-a93c-cb9ccf6c813a">
<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c4efcf6d-3c40-44af-8723-62c3867a700e">

# #END </details>

<details>
  <summary>10. Typescript Classes </summary>

# Typescript Classes

### TS/crash-course/src/index.ts:

```ts
//Class Interface
interface PersonInterface {
  age: number;
  register(): string;
}

// Classes
class Person implements PersonInterface {
  private id: number;
  protected name: string;
  public age: number;

  constructor(id: number, name: string, age: number) {
    this.id = id;
    this.name = name;
    this.age = age;
    console.log(this.id, this.name, this.age);
  }

  register() {
    return `${this.name} is now registered`;
  }
}

const brad = new Person(1, "Brad Traddy", 30);
const mike = new Person(2, "Mike Jordan", 25);

console.log(brad, mike);
console.log(brad.age);
console.log(brad.register());

//SubClass
class Employee extends Person {
  position: string;

  constructor(id: number, name: string, age: number, position: string) {
    super(id, name, age);
    this.position = position;
  }
}

const emp = new Employee(3, "Shawn", 34, "Developer");
console.log(emp);
```

### TS/crash-course/dist/index.js:

```ts
"use strict";
// Classes
class Person {
    constructor(id, name, age) {
        this.id = id;
        this.name = name;
        this.age = age;
        console.log(this.id, this.name, this.age);
    }
    register() {
        return `${this.name} is now registered`;
    }
}
const brad = new Person(1, "Brad Traddy", 30);
const mike = new Person(2, "Mike Jordan", 25);
console.log(brad, mike);
console.log(brad.age);
console.log(brad.register());
//SubClass
class Employee extends Person {
    constructor(id, name, age, position) {
        super(id, name, age);
        this.position = position;
    }
}
const emp = new Employee(3, "Shawn", 34, "Developer");
console.log(emp);
```

<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/096f49aa-2c0d-47c8-9e7b-a96aa27350ec">
<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9f960bdf-a3ac-49e6-99d6-5d9b90726d8f">

# #END </details>

<details>
  <summary>11. Typescript Generics </summary>

# Typescript Generics

### TS/crash-course/src/index.ts:

```ts
function getArray(items: any[]): any[] {
  return new Array().concat(items);
}

let numArray = getArray([1, 2, 3, 4]);
let strArray = getArray(["brad", "John", "Jill"]);

numArray.push("hello");
strArray.push(3);

// Generics
function getArray2<T>(items: T[]): T[] {
  return new Array().concat(items);
}

let numArray2 = getArray2<number>([1, 2, 3, 4]);
let strArray2 = getArray2<string>(["brad", "John", "Jill"]);

numArray2.push(5);
strArray2.push("Jane");
```

### TS/crash-course/dist/index.js:

```ts
"use strict";
function getArray(items) {
    return new Array().concat(items);
}
let numArray = getArray([1, 2, 3, 4]);
let strArray = getArray(["brad", "John", "Jill"]);
numArray.push("hello");
strArray.push(3);
// Generics
function getArray2(items) {
    return new Array().concat(items);
}
let numArray2 = getArray2([1, 2, 3, 4]);
let strArray2 = getArray2(["brad", "John", "Jill"]);
numArray2.push(5);
strArray2.push("Jane");
```

<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/eaab4b2d-2292-4284-9417-3c88b344cf46">
<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bb4100ea-1da2-4103-b8d5-301231afcfea">

# #END </details>

<details>
  <summary>12. Typescript with React </summary>

# Typescript with React

<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4e98c78b-1a2a-46a4-b031-39459420168d">
<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/16226a7c-5d30-4751-bc55-f91248094dbd">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3baaaaa8-f263-4717-bfe5-b711fe98fd46">

# Install React App with Typescript

```tsbs
npx create-react-app . --template typescript
npx create-react-app reactts-app --template typescript
OR
yarn create react-app reactts-app --template typescript
OR
yarn create react-app reactts-app
yarn add typescript @types/node @types/react @types/react-dom @types/jest
```

### TS/reactts-app/src/App.tsx:

```ts
import "./App.css";
import Header from "./Header";

function App() {
  return (
    <div className="App">
      <Header title="Hello World" color="red" />
    </div>
  );
}

export default App;
```

### TS/reactts-app/src/Header.tsx:

```ts
import React from "react";

export interface Props {
  title: string;
  color?: string;
}

const Header = (props: Props) => {
  return (
    <header>
      <h1 style={{ color: props.color ? props.color : "blue" }}>
        {props.title}
      </h1>
    </header>
  );
};

export default Header;
```

# #END </details>

# #END
