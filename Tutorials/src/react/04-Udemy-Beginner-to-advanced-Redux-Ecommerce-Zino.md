# UDEMY-REACT - BEGINNER TO ADVANCED (REDUX & ECOMMERCE APP) - ZINO ACADEMY

## [COURSE](https://www.udemy.com/course/react-beginner-to-advanced-with-redux-ecommerce-app/)
# Basic html site

### x-zino/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World!</h1>
    <script src="./js/script.js"></script>
  </body>
</html>
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/d02b5ab2-f439-46dc-b6e5-8e1aeb7d6a64)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/4d30a3c3-6294-483b-8453-ef6f53e7dfad)

</details>

<details>
  <summary>2. Map function  </summary>

# Map function

### x-zino/js/script.js:

```js
// Map
const numbers = [1, 2, 3, 4, 5];

const newNumbers = numbers.map((number) => {
  return number * 2;
});

console.log(newNumbers);
```

```js
// [2, 4, 6, 8, 10]
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/21c94ee5-cedc-4e21-bbe2-c6d8e13896df)

</details>

<details>
  <summary>3. Filter function  </summary>

# Filter function

### x-zino/js/script.js:

```js
// Filter
const ages = [16, 18, 14, 32, 33, 12];

const newAges = ages.filter((number) => {
  return number > 30;
});

console.log(newAges);
```

```js
// [32, 33]
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/b0a5afe6-86b2-40ca-bb53-8a7fec9f3448)

</details>

<details>
  <summary>4. Spread Operator </summary>

# Spread Operator

### x-zino/js/script.js:

```js
// Spread Operator (...)
const numbers = [1, 2, 3];
const newNumbers = [...numbers, 4, 5, 6];

const person = {
  name: "zino",
  sex: "male",
};
const newPerson = {
  ...person,
  age: 28,
};

console.log(newNumbers);
console.log(newPerson);
```

```js
// [1, 2, 3, 4, 5, 6]
// {name: 'zino', sex: 'male', age: 28}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/d271e45f-884e-41fe-9437-407703fe3cd8)

</details>

<details>
  <summary>5. Rest Parameter </summary>

# Rest Parameter

```js
// Rest Parameter
const user = (name, age, ...hobbies) => {
  console.log(name);
  console.log(age);
  console.log(hobbies);
};

user("zino", 28, "Coding", "Tennis", "Reading");
```

```js
// zino
// 28
// ["Coding", "Tennis", "Reading"]
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/391acc9e-61c8-4021-91d9-5418e97f3ca7)

</details>

<details>
  <summary>6. Destructuring </summary>

# Destructuring

### x-zino/js/script.js:

```js
// Destructuring
const user = (name, age, ...hobbies) => {
  console.log(name);
  console.log(age);
  console.log(hobbies);
};

user("zino", 28, "Coding", "Tennis", "Reading");
// Destructuring
const person = ["zino", 28, "developer"];
const [name, age, job] = person;

const personObj = {
  myname: "bella",
  myage: 32,
  myjob: "Singer",
};
const { myname, myage, myjob } = personObj;

console.log(name);
console.log(age);
console.log(job);

console.log(myname);
console.log(myage);
console.log(myjob);
```

# output:

```js
// zino
// 28
// developer

// bella
// 32
// Singer
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/b1cc41de-bcec-4e68-a3ca-4e7d2b7fd242)

</details>

<details>
  <summary>7. ES5 Prototype Inheritance </summary>

# Prototype Inheritance

### x-zino/js/script.js:

```js
// Prototype Inheritance
function Person(firstName, lastName, age) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.age = age;
  this.currentYear = new Date().getFullYear();
}

// Greet Prototype
Person.prototype.greet = function () {
  return `Hello, my name is ${this.firstName} ${this.lastName}.`;
};

// Create another object
function User(firstName, lastName, username, password) {
  Person.call(this, firstName, lastName);
  this.username = username;
  this.password = password;
}

const person1 = new Person("John", "Smith", 24);
console.log(person1);
console.log(person1.firstName);
console.log(person1.greet());

const user1 = new User("John", "Smith", "johnsmith@gmail.com", 12345);
console.log(user1);
```

# output:

```js
// Person {firstName: 'John', lastName: 'Smith', age: 24, currentYear: 2023}
// John
// Hello, my name is John Smith.

// User {firstName: 'John', lastName: 'Smith', age: undefined, currentYear: 2023, username: 'johnsmith@gmail.com', …}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/08f68beb-1a61-4940-a9dd-2c78aacc96dd)

</details>

<details>
  <summary>8. ES6 Classes </summary>

# ES6 Classes

### x-zino/js/script.js:

```js
// ES6 Classes
class Person {
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }
  greet() {
    return `Hello, my name is ${this.firstName} ${this.lastName}.`;
  }
}

const zino = new Person("Zino", "Akpareva", 27);
const mary = new Person("Mary", "Doe", 25);

console.log(zino);
console.log(zino.greet());
console.log(mary);
console.log(mary.greet());
```

# output:

```js
// {
//   age: 27;
//   firstName: "Zino";
//   lastName: "Akpareva";
// }

// Hello, my name is Zino Akpareva.

// {
//   age: 25;
//   firstName: "Mary";
//   lastName: "Doe";
// }

// Hello, my name is Mary Doe.
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/b4aee31a-6107-4582-8d4c-f5c8aa18e445)

</details>

<details>
  <summary>9. Module Import and Export </summary>

# Module Import and Export

### x-zino/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World!</h1>
    <script type="module" src="./main.js"></script>
  </body>
</html>
```

### x-zino/main.js:

```js
import num1, { num2 } from "./js/variable.js";
import * as nums from "./js/variable.js";
import add from "./js/functions.js";

console.log(num1);
console.log(num2);
console.log(nums.num1, nums.num2);
const result = add(num1, num2);
console.log(result);
```

### x-zino/js/variable.js:

```js
// export const num1 = 10;
// export const num2 = 5;

const num1 = 10;
const num2 = 5;

export { num1, num2 };
export default num1;
```

### x-zino/js/functions.js:

```js
export default function add(a, b) {
  return a + b;
}
```

# output:

```js
// 10
// 5
// 10 5
// 15
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/d9eaaed8-4c37-4f62-82fe-58dff0a4b85a)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b4e9fd15-d700-4599-9f04-f91caf7014e7)

</details>

<details>
  <summary>10. Create React App </summary>

# Create React App

```jsbs
npx create-react-app my-first-app
cd my-first-app
```

```jsbs
npm i @babel/plugin-proposal-private-property-in-object --save-dev
```

```jsbs
npm run start
```

### x-zino/my-first-app/public/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
```

### x-zino/my-first-app/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
```

### x-zino/my-first-app/src/App.js:

```js
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/47655a58-51b3-40db-9908-00e2a5e88bc8)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/48d73ba2-dadd-4470-964e-1559ea2ec3ed)

</details>

<details>
  <summary>11. Hello World Component </summary>

# Hello World Component

### x-zino/my-first-app/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

### x-zino/my-first-app/src/App.js:

```js
import "./App.css";
import HelloWorld from "./components/HelloWorld";

function App() {
  return (
    <div className="App">
      <HelloWorld />
    </div>
  );
}

export default App;
```

### x-zino/my-first-app/src/components/HelloWorld.jsx:

```js
import React from "react";

const HelloWorld = () => {
  //   const title = React.createElement("h1", null, "Hello People...");
  //   return <div>{title}</div>;
  return <h1>Hello World - Component</h1>;
};

export default HelloWorld;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/3eddbd1c-0c04-406a-9418-def0205f44f7)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/a576b185-d6f1-4d9a-af72-dedd9578340c)

</details>

<details>
  <summary>12. Outputting Dynamic Values </summary>

# Outputting Dynamic Values

### x-zino/my-first-app/src/App.js:

```js
import "./App.css";
import HelloWorld from "./components/HelloWorld";

function App() {
  return (
    <div className="App">
      <HelloWorld />
    </div>
  );
}

export default App;
```

### x-zino/my-first-app/src/components/HelloWorld.jsx:

```js
import React from "react";

const HelloWorld = () => {
  const name = "Zino";
  const age = 28;
  const person = { name: "Zino" };
  const ages = [10, 30, 49];
  const link = "http://google.com";

  return (
    <div className="heading">
      <h1>{name}</h1>
      <h2>I am {age} years old</h2>
      <h2>Person: {person.name}</h2>
      <h2>{JSON.stringify(person)}</h2>
      <h2>{JSON.stringify(ages)}</h2>
      <h2>
        {ages.map((age, index) => {
          return (
            <p>
              Age {index + 1}: {age}
            </p>
          );
        })}
      </h2>
      <a href={link} target="_blank" rel="noopener noreferrer">
        Google
      </a>
    </div>
  );
};

export default HelloWorld;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/252a07eb-6310-413c-9030-fb3a345705d5)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/f48beca1-da39-424b-800b-af492c01ac8d)

</details>

<details>
  <summary>13. Inline Styling </summary>

# Inline Styling

### x-zino/my-first-app/src/App.js:

```js
import "./App.css";
import HelloWorld from "./components/HelloWorld";

function App() {
  return (
    <div className="App">
      <HelloWorld />
    </div>
  );
}

export default App;
```

### x-zino/my-first-app/src/components/HelloWorld.jsx:

```js
import React from "react";

const headerStyle = {
  color: "red",
  backgroundColor: "black",
};

const HelloWorld = () => {
  return (
    // <div style={{ color: "red", backgroundColor: "#000" }}>
    <div style={headerStyle}>
      <h1>Hello World!</h1>
    </div>
  );
};

export default HelloWorld;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/0edf5081-c723-4da0-8489-7c896f1afc5e)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/fe1393b1-d82e-4fee-a762-c9a68a4751bf)

</details>

<details>
  <summary>14. External Styling </summary>

# External Styling

### x-zino/my-first-app/src/App.js:

```js
import "./App.css";
import HelloWorld from "./components/HelloWorld";

function App() {
  return (
    <div className="App">
      <HelloWorld />
    </div>
  );
}

export default App;
```

### x-zino/my-first-app/src/components/HelloWorld.jsx:

```js
import React from "react";
import "./HelloWorld.css";

const HelloWorld = () => {
  return (
    <div className="headerStyle">
      <h1>Hello World!</h1>
    </div>
  );
};

export default HelloWorld;
```

### x-zino/my-first-app/src/components/HelloWorld.css:

```css
.headerStyle {
  color: crimson;
  background-color: yellow;
  border: 5px solid #000;
}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/2010c22c-66f1-40ad-bc67-556997f06f34)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/fa33e15f-b777-4112-955b-57770b095398)

</details>

<details>
  <summary>15. Scoping Styling using CSS modules </summary>

# Scoping Styling using CSS modules

### x-zino/my-first-app/src/App.js:

```js
// import styles from "./App.module.css";
import HelloWorld from "./components/HelloWorld";

function App() {
  return (
    <div>
      <HelloWorld />
    </div>
  );
}

export default App;
```

### x-zino/my-first-app/src/components/HelloWorld.jsx:

```js
import React from "react";
import styles from "./HelloWorld.module.css";

const HelloWorld = () => {
  return (
    <>
      <div className={styles["app--header"]}>
        <h1>Hello World!</h1>
      </div>
      <div className={styles["helloworld--body"]}>
        <h2>The Body</h2>
      </div>
    </>
  );
};

export default HelloWorld;
```

### x-zino/my-first-app/src/App.module.css:

```css
.app--header {
  color: crimson;
  background-color: black;
}
```

### x-zino/my-first-app/src/components/HelloWorld.module.css:

```css
.app--header {
  color: white;
  background-color: green;
}

.helloworld--body {
  color: crimson;
  background-color: black;
}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/afccfcfd-9b89-4b14-90b8-e16bf5968d19)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/85eed106-94ce-4aae-8732-62eb98b1a183)

</details>

<details>
  <summary>16. Defining and Passing Props </summary>

# Defining and Passing Props

### x-zino/my-first-app/src/App.js:

```js
import Users from "./components/Users";

function App() {
  return (
    <div>
      <h1>List of Users</h1>
      <div className="container">
        <Users name="Ifeanyi Omeata" job="Developer" />
        <Users name="John Stones" job="Artist" />
        <Users name="Ken Braham" job="Designer" />
      </div>
    </div>
  );
}

export default App;
```

### x-zino/my-first-app/src/components/Users.jsx:

```js
import React from "react";

const Users = (props) => {
  return (
    <div className="user">
      <h2>Name: {props.name}</h2>
      <h3>Job: {props.job}</h3>
    </div>
  );
};

export default Users;
```

### x-zino/my-first-app/src/index.css:

```css
* {
  background-color: #000;
  color: #fff;
}

h1 {
  text-align: center;
}

.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.user {
  border: 1px solid #777;
  border-radius: 3px;
  margin: 10px;
  padding: 10px;
  width: 320px;
}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/86f5a331-e9c0-4542-bf43-25826fc47cc0)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2a8b4291-e4ed-4407-ad40-46243a76cdd7)

</details>

<details>
  <summary>17. Setting Default Props </summary>

# Setting Default Props

### x-zino/my-first-app/src/App.js:

```js
import Users from "./components/Users";

function App() {
  return (
    <div>
      <h1>List of Users</h1>
      <div className="container">
        <Users />
        <Users name="John Stones" job="Artist" />
        <Users name="Ken Braham" job="Designer" />
      </div>
    </div>
  );
}

export default App;
```

### x-zino/my-first-app/src/components/Users.jsx:

```js
import React from "react";

const Users = (props) => {
  return (
    <div className="user">
      <h2>Name: {props.name}</h2>
      <h3>Job: {props.job}</h3>
      {/* <h2>Name: {props.name || "Default name"}</h2> */}
      {/* <h3>Job: {props.job || "Default job"}</h3> */}
    </div>
  );
};

Users.defaultProps = {
  name: "Default name",
  job: "Default job",
};

export default Users;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/84a87e7b-bbd0-4213-ace0-628ef0a98a58)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/5879c231-90c9-48d4-ad25-d8a4d8e4cdb7)

</details>

<details>
  <summary>18. Props Destructuring </summary>

# Props Destructuring

### x-zino/my-first-app/src/App.js:

```js
import Users from "./components/Users";

function App() {
  return (
    <div>
      <h1>List of Users</h1>
      <div className="container">
        <Users />
        <Users name="John Stones" job="Artist" />
        <Users name="Ken Braham" job="Designer" />
      </div>
    </div>
  );
}

export default App;
```

### x-zino/my-first-app/src/components/Users.jsx:

```js
import React from "react";

const Users = ({ name, job }) => {
  return (
    <div className="user">
      <h2>Name: {name}</h2>
      <h3>Job: {job}</h3>
    </div>
  );
};

Users.defaultProps = {
  name: "Default name",
  job: "Default job",
};

export default Users;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/fd22fbfd-13d1-4b50-b70b-3d88f9d40506)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/5879c231-90c9-48d4-ad25-d8a4d8e4cdb7)

</details>

<details>
  <summary>19. Using Children Props </summary>

# Using Children Props

### x-zino/my-first-app/src/App.js:

```js
import Users from "./components/Users";
import Card from "./components/Card";

function App() {
  return (
    <div className="app">
      <h1>List of Users</h1>
      <Card>
        <h2>This is a Card.</h2>
        <p>
          Pariatur dolore culpa voluptate proident voluptate ipsum qui sunt
          aute. Anim fugiat duis do consectetur magna aliquip et ea dolor magna
          eu reprehenderit occaecat. Aliquip magna eiusmod Loerem culpa. Enim
          culpa laborum enim laboris sit esse quis dolor. proident nostrud.
        </p>
      </Card>
      <div className="container">
        <Users />
        <Users name="John Stones" job="Artist" />
        <Users name="Ken Braham" job="Designer" />
      </div>
    </div>
  );
}

export default App;
```

### x-zino/my-first-app/src/components/Users.jsx:

```js
import React from "react";
import Button from "./Button";
import Card from "./Card";

const Users = ({ name, job }) => {
  return (
    <>
      <Card>
        <h2>Name: {name}</h2>
        <h3>Job: {job}</h3>
        <Button>Learn More...</Button>
      </Card>
    </>
  );
};

Users.defaultProps = {
  name: "Default name",
  job: "Default job",
};

export default Users;
```

### x-zino/my-first-app/src/components/Card.jsx:

```js
import React from "react";

const Card = ({ children }) => {
  return <div className="card">{children}</div>;
};

export default Card;
```

### x-zino/my-first-app/src/components/Button.jsx:

```js
import React from "react";

const Button = ({ children }) => {
  return (
    <>
      <button>{children}</button>
    </>
  );
};
export default Button;
```

### x-zino/my-first-app/src/index.css:

```css
* {
  background-color: #000;
  color: #fff;
}

h1 {
  text-align: center;
}

.app {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.card {
  border: 1px solid #777;
  border-radius: 3px;
  margin: 10px;
  padding: 10px;
  width: 320px;
}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/d36f54d8-f854-41de-a4a1-f453ccef3088)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/827fbb4f-4cf3-48cd-9b1c-d98f5a8943cd)

</details>

<details>
  <summary>20. Rendering a List </summary>

# Rendering a List

### x-zino/my-first-app/src/App.js:

```js
import Users from "./components/Users";
import Card from "./components/Card";
import { users } from "./components/Data";

function App() {
  return (
    <div className="app">
      <h1>List of Users</h1>
      <div className="container">
        {users.map((user) => {
          return (
            <Card key={user.id}>
              <Users name={user.name} job={user.job} />
            </Card>
          );
        })}
      </div>
    </div>
  );
}

export default App;
```

### x-zino/my-first-app/src/components/Data.js:

```js
export const users = [
  {
    id: 1,
    name: "John Doe",
    job: "Developer",
  },
  {
    id: 2,
    name: "Sarah Conner",
    job: "UI/UX Designer",
  },
  {
    id: 3,
    name: "Bob Michael",
    job: "Manager",
  },
];
```

### x-zino/my-first-app/src/components/Users.jsx:

```js
import React from "react";
import Button from "./Button";

const Users = ({ name, job }) => {
  return (
    <div>
      <h2>Name: {name}</h2>
      <h3>Job: {job}</h3>
      <Button>Learn More...</Button>
    </div>
  );
};

Users.defaultProps = {
  name: "Default name",
  job: "Default job",
};

export default Users;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/5b8b991e-23d9-4181-a911-453a875ad36c)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/a9e4ec60-41c4-4279-a2b8-a9149ac4d805)

</details>

+PROFILE APP

<details>
  <summary>21. Introduction - Setup Project </summary>

# Introduction - Setup Project

```jsbs
npx create-react-app .
npx create-react-app profile-app

yarn create react-app profile-app
cd profile-app
npm start
```

### x-zino/profile-app/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

### x-zino/profile-app/src/App.js:

```js
import styles from "./App.module.css";
import ProfileList from "./components/profile/ProfileList";

function App() {
  return (
    <div className={styles}>
      <ProfileList />
    </div>
  );
}

export default App;
```

### x-zino/profile-app/src/components/profile/ProfileList.jsx:

```js
import React from "react";
import styles from "./ProfileList.module.css";

const ProfileList = () => {
  return (
    <div>
      <h1>ProfileList</h1>
    </div>
  );
};

export default ProfileList;
```

### x-zino/profile-app/src/components/profile/Profile.jsx:

```js
import React from "react";
import styles from "./Profile.module.css";

const Profile = () => {
  return (
    <div>
      <h1>Profile</h1>
    </div>
  );
};

export default Profile;
```

### x-zino/profile-app/src/components/ui/card/Card.jsx:

```js
import React from "react";
import styles from "./Card.module.css";

const Card = () => {
  return (
    <div>
      <h1>Card</h1>
    </div>
  );
};

export default Card;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/e1a7c4f1-8383-45b9-af1d-0e85b9fcbd70)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/d3dc6d5e-e0a8-4d5b-b634-009c1afceae9)

</details>

<details>
  <summary>22. Installing React-Icons </summary>

# Installing React-Icons

```jsbs
npm i react-icons
npm install react-icons --save

yarn add react-icons
```

# Sample usage

```js
import { FaBeer } from "react-icons/fa";

function Question() {
  return (
    <h3>
      Lets go for a <FaBeer />?
    </h3>
  );
}
```

### x-zino/profile-app/src/components/profile/ProfileList.jsx:

```js
import React from "react";
import styles from "./ProfileList.module.css";
import { FaBeer } from "react-icons/fa";
import { FaAmazon } from "react-icons/fa";

const ProfileList = () => {
  return (
    <div>
      <h1>ProfileList</h1>
      <FaBeer />
      <FaAmazon />
    </div>
  );
};

export default ProfileList;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/45b976ff-cabe-4f68-95f4-a8d06c5094ce)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/727084cc-53bf-4d3e-b59d-3f843a0b27e5)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/30f96e06-da32-4a37-a1cd-9785475610d0)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/bf1748e7-7973-4325-87cf-7d5a17fc7c96)

</details>

<details>
  <summary>23. Global Style Variables </summary>

# Global Style Variables

### x-zino/profile-app/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap");

:root {
  --font-family: "Poppins", sans-serif;
  --dark-blue: #0a1930;
  --light-blue: #1f93ff;

  --color-white: #fff;
  --color-dark: #333;

  --color-grey: #eae6eb;
  --box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);

  --color-purple: #660099;
  --color-orange: #ff7722;

  --color-primary: #007bff;
  --color-success: #28a745;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: #222;
  color: var(--color-white);
  font-family: var(--font-family);
}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/45a76bac-f5a3-49ad-9471-cc4616ccba91)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/f63d36a7-9d6b-4786-b2e2-e956d0f1887f)

</details>

<details>
  <summary>24. ProfileList JSX </summary>

# ProfileList JSX

### x-zino/profile-app/src/App.js:

```js
import styles from "./App.module.css";
import ProfileList from "./components/profile/ProfileList";

function App() {
  return (
    <div className={styles}>
      <ProfileList />
    </div>
  );
}

export default App;
```

### x-zino/profile-app/src/components/profile/ProfileList.jsx:

```js
import React from "react";
import styles from "./ProfileList.module.css";
import Profile from "./Profile";

const ProfileList = () => {
  return (
    <section className={styles.center}>
      <div>
        <h1>Team Members</h1>
      </div>
      <div className={styles["profile-container"]}>
        <Profile />
      </div>
    </section>
  );
};

export default ProfileList;
```

### x-zino/profile-app/src/components/profile/ProfileList.module.css:

```css
.center {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
  font-size: 34px;
  line-height: 1.4;
  color: #fff;
  text-align: center;
  padding-top: 20px;
}

.profile-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/b1f4ba37-1da5-46a4-9e9d-ba2ea7000e02)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/eceabd56-d3fd-432a-b8db-cc499bc6c46c)

</details>

<details>
  <summary>25. Profile JSX </summary>

# Profile JSX

### x-zino/profile-app/src/App.js:

```js
import styles from "./App.module.css";
import ProfileList from "./components/profile/ProfileList";

function App() {
  return (
    <div className={styles}>
      <ProfileList />
    </div>
  );
}

export default App;
```

### x-zino/profile-app/src/components/profile/Profile.jsx:

```js
import React from "react";
import styles from "./Profile.module.css";
import profile1 from "../../assets/profile1.png";
import {
  AiOutlineTwitter,
  AiOutlineGithub,
  AiOutlineGooglePlus,
} from "react-icons/ai";

const Profile = () => {
  return (
    <div className={styles.profile}>
      <img src={profile1} alt="profile"></img>
      <div className={styles["profile-content"]}>
        <h3>My Profile</h3>
        <div className={styles.text}>
          <p>Name:</p>
          <p>Adaora Nwodo</p>
        </div>
        <div className={styles.text}>
          <p>Job:</p>
          <p>Cloud Engineer</p>
        </div>
        <div className={styles.text}>
          <p>Company:</p>
          <p>Microsoft</p>
        </div>
      </div>

      <div className={styles.icons}>
        <AiOutlineTwitter color="#777" size={20} />
        <AiOutlineGithub color="#777" size={20} />
        <AiOutlineGooglePlus color="#777" size={20} />
      </div>

      <div className={styles.btn}>
        <a href="#" target="_blank" rel="noopener noreferrer">
          View Profile
        </a>
      </div>
    </div>
  );
};

export default Profile;
```

### x-zino/profile-app/src/components/profile/Profile.module.css:

```css
.profile {
  width: 300px;
  background-color: #fff;
  color: #222;
}

.profile img {
  width: 300px;
  height: 40%;
}

.profile-content {
  padding: 10px;
}

h3 {
  font-size: 20px;
  line-height: 1.2;
  margin-bottom: 10px;
}

.text {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.text::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -5px;
  width: 100%;
  height: 0.5px;
  background: var(--color-orange);
}

.icons,
.btn {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px 0;
}

.icons > {
  margin: 0 3px;
  cursor: pointer;
}

.btn a {
  font-size: 14px;
  font-weight: 400;
  padding: 7px 10px;
  margin-bottom: 10px;
  border: 1px solid transparent;
  border-radius: 50px;
  outline: none;
  text-decoration: none;
  color: #fff;
  background: rgb(9, 9, 121);
  background: linear-gradient(
    90deg,
    rgba(9, 9, 121, 1) 21%,
    rgba(2, 0, 36, 1) 73%,
    rgba(187, 10, 90, 1) 93%,
    rgba(190, 109, 81, 1) 100%,
    rgba(0, 212, 255, 1) 100%
  );
  cursor: pointer;
  transform: translateY(0);
  transition: all 0.3s;
}

.btn a:hover {
  transform: translateY(-5px);
}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/733bdc8b-3d83-454f-9a50-307512f0cc41)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/d675a9c5-d606-4219-88f2-27a7ab76a237)

</details>

<details>
  <summary>26. Using React Icon Context </summary>

# Using React Icon Context

### x-zino/profile-app/src/components/profile/Profile.jsx:

```jsbs
import {IconContext} from "react-icons"

<IconContext.Provider value={{ color: "#777", size: "20px" }}>
    <div className={styles.icons}>
        <AiOutlineTwitter />
        <AiOutlineGithub />
        <AiOutlineGooglePlus />
    </div>
</IconContext.Provider>
```

```js
import React from "react";
import styles from "./Profile.module.css";
import profile1 from "../../assets/profile1.png";
import {
  AiOutlineTwitter,
  AiOutlineGithub,
  AiOutlineGooglePlus,
} from "react-icons/ai";
import { IconContext } from "react-icons";

const Profile = () => {
  return (
    <div className={styles.profile}>
      <img src={profile1} alt="profile"></img>
      <div className={styles["profile-content"]}>
        <h3>My Profile</h3>
        <div className={styles.text}>
          <p>Name:</p>
          <p>Adaora Nwodo</p>
        </div>
        <div className={styles.text}>
          <p>Job:</p>
          <p>Cloud Engineer</p>
        </div>
        <div className={styles.text}>
          <p>Company:</p>
          <p>Microsoft</p>
        </div>
      </div>

      <IconContext.Provider value={{ color: "#777", size: "20px" }}>
        <div className={styles.icons}>
          <AiOutlineTwitter />
          <AiOutlineGithub />
          <AiOutlineGooglePlus />
        </div>
      </IconContext.Provider>

      <div className={styles.btn}>
        <a href="#" target="_blank" rel="noopener noreferrer">
          View Profile
        </a>
      </div>
    </div>
  );
};

export default Profile;
```

</details>

<details>
  <summary>27. Card Component </summary>

# Card Component

### x-zino/profile-app/src/components/profile/Profile.jsx:

```js
import React from "react";
import styles from "./Profile.module.css";
import profile1 from "../../assets/profile1.png";
import Card from "../UI/Card";
import {
  AiOutlineTwitter,
  AiOutlineGithub,
  AiOutlineGooglePlus,
} from "react-icons/ai";
import { IconContext } from "react-icons";

const Profile = () => {
  return (
    <Card>
      <div className={styles.profile}>
        <img src={profile1} alt="profile"></img>
        <div className={styles["profile-content"]}>
          <h3>My Profile</h3>
          <div className={styles.text}>
            <p>Name:</p>
            <p>Adaora Nwodo</p>
          </div>
          <div className={styles.text}>
            <p>Job:</p>
            <p>Cloud Engineer</p>
          </div>
          <div className={styles.text}>
            <p>Company:</p>
            <p>Microsoft</p>
          </div>
        </div>

        <IconContext.Provider value={{ color: "#777", size: "20px" }}>
          <div className={styles.icons}>
            <AiOutlineTwitter />
            <AiOutlineGithub />
            <AiOutlineGooglePlus />
          </div>
        </IconContext.Provider>

        <div className={styles.btn}>
          <a href="#" target="_blank" rel="noopener noreferrer">
            View Profile
          </a>
        </div>
      </div>
    </Card>
  );
};

export default Profile;
```

### x-zino/profile-app/src/components/UI/Card.jsx:

```js
import React from "react";
import styles from "./Card.module.css";

const Card = ({ children }) => {
  return <div className={styles.card}>{children}</div>;
};

export default Card;
```

### x-zino/profile-app/src/components/UI/Card.module.css:

```css
.card {
  border: 1px solid transparent;
  border-radius: 8px;
  overflow: hidden;
  margin: 20px;
  box-shadow: var(--box-shadow);
}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/f34b963b-6657-4565-96c1-0fe031ceffaa)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/89f7517d-9388-404e-b141-18c0f3075173)

</details>

<details>
  <summary>28. Passing Profile Props </summary>

# Passing Profile Props

### x-zino/profile-app/src/App.js:

```js
import styles from "./App.module.css";
import ProfileList from "./components/profile/ProfileList";

function App() {
  return (
    <div className={styles}>
      <ProfileList />
    </div>
  );
}

export default App;
```

### x-zino/profile-app/src/components/profile/ProfileList.jsx:

```js
import React from "react";
import styles from "./ProfileList.module.css";
import Profile from "./Profile";
import profile1 from "../../assets/profile1.png";
import profile2 from "../../assets/profile2.png";
import profile3 from "../../assets/profile3.png";

const ProfileList = () => {
  return (
    <section className={styles.center}>
      <div>
        <h1>Team Members</h1>
      </div>
      <div className={styles["profile-container"]}>
        <Profile
          image={profile1}
          name={"Adaora Nwodo"}
          job={"Cloud Engineer"}
          company={"Microsoft"}
          link={"https://twitter.com/AdoraNwodo"}
        />
      </div>
      <div className={styles["profile-container"]}>
        <Profile
          image={profile2}
          name={"John Doe"}
          job={"Web Developer"}
          company={"Google"}
          link={"#"}
        />
      </div>
      <div className={styles["profile-container"]}>
        <Profile
          image={profile3}
          name={"Fisayo Tinuke"}
          job={"Mobile Developer"}
          company={"ZinoTrust"}
          link={"#"}
        />
      </div>
    </section>
  );
};

export default ProfileList;
```

### x-zino/profile-app/src/components/profile/Profile.jsx:

```js
import React from "react";
import styles from "./Profile.module.css";
import Card from "../UI/Card";
import {
  AiOutlineTwitter,
  AiOutlineGithub,
  AiOutlineGooglePlus,
} from "react-icons/ai";
import { IconContext } from "react-icons";

const Profile = ({ image, name, job, company, link }) => {
  return (
    <Card>
      <div className={styles.profile}>
        <img src={image} alt="profile"></img>
        <div className={styles["profile-content"]}>
          <h3>My Profile</h3>
          <div className={styles.text}>
            <p>Name:</p>
            <p>{name}</p>
          </div>
          <div className={styles.text}>
            <p>Job:</p>
            <p>{job}</p>
          </div>
          <div className={styles.text}>
            <p>Company:</p>
            <p>{company}</p>
          </div>
        </div>

        <IconContext.Provider value={{ color: "#777", size: "20px" }}>
          <div className={styles.icons}>
            <AiOutlineTwitter />
            <AiOutlineGithub />
            <AiOutlineGooglePlus />
          </div>
        </IconContext.Provider>

        <div className={styles.btn}>
          <a href={link} target="_blank" rel="noopener noreferrer">
            View Profile
          </a>
        </div>
      </div>
    </Card>
  );
};

export default Profile;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/0fda4bc0-339f-4734-be0b-0fa70dba0ee3)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/6c6880a3-9f92-4c85-8294-437e51f78534)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b0a3d4b2-8884-4617-b741-16d9bc3a3bfe)

</details>

<details>
  <summary>29. Mapping through Data </summary>

# Mapping through Data

### x-zino/profile-app/src/data/profile-data.js:

```js
export const profiles = [
  {
    id: 1,
    img: "https://i.ibb.co/gvwfFJK/profile1.png",
    name: "Adaora Nwodo",
    job: "Cloud Engineer",
    company: "Microsoft",
    link: "https://twitter.com/AdoraNwodo",
  },
  {
    id: 2,
    img: "https://i.ibb.co/7W7rV8v/profile2.png",
    name: "John Doe",
    job: "Web Developer",
    company: "Google",
    link: "#",
  },
  {
    id: 3,
    img: "https://i.ibb.co/tKn71dn/profile3.png",
    name: "Fisayo Tinuke",
    job: "Mobile Developer",
    company: "ZinoTrust",
    link: "#",
  },
];
```

### x-zino/profile-app/src/App.js:

```js
import styles from "./App.module.css";
import ProfileList from "./components/profile/ProfileList";

function App() {
  return (
    <div className={styles}>
      <ProfileList />
    </div>
  );
}

export default App;
```

### x-zino/profile-app/src/components/profile/ProfileList.jsx:

```js
import React from "react";
import styles from "./ProfileList.module.css";
import Profile from "./Profile";
import { profiles } from "../../data/profile-data";

const ProfileList = () => {
  return (
    <section className={styles.center}>
      <div>
        <h1>Team Members</h1>
      </div>
      {profiles.map((profile) => {
        const { id, img, name, job, company, link } = profile;
        return (
          <div className={styles["profile-container"]}>
            <Profile
              key={id}
              image={img}
              name={name}
              job={job}
              company={company}
              link={link}
            />
          </div>
        );
      })}
    </section>
  );
};

export default ProfileList;
```

### x-zino/profile-app/src/components/profile/Profile.jsx:

```js
import React from "react";
import styles from "./Profile.module.css";
import Card from "../UI/Card";
import {
  AiOutlineTwitter,
  AiOutlineGithub,
  AiOutlineGooglePlus,
} from "react-icons/ai";
import { IconContext } from "react-icons";

const Profile = ({ image, name, job, company, link }) => {
  return (
    <Card>
      <div className={styles.profile}>
        <img src={image} alt="profile"></img>
        <div className={styles["profile-content"]}>
          <h3>My Profile</h3>
          <div className={styles.text}>
            <p>Name:</p>
            <p>{name}</p>
          </div>
          <div className={styles.text}>
            <p>Job:</p>
            <p>{job}</p>
          </div>
          <div className={styles.text}>
            <p>Company:</p>
            <p>{company}</p>
          </div>
        </div>

        <IconContext.Provider value={{ color: "#777", size: "20px" }}>
          <div className={styles.icons}>
            <AiOutlineTwitter />
            <AiOutlineGithub />
            <AiOutlineGooglePlus />
          </div>
        </IconContext.Provider>

        <div className={styles.btn}>
          <a href={link} target="_blank" rel="noopener noreferrer">
            View Profile
          </a>
        </div>
      </div>
    </Card>
  );
};

export default Profile;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/4e3d4e57-6370-4022-a013-9784dcf61607)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/480a2e17-443a-4ead-a832-01a13621f442)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/78abe916-9dd1-4bf2-a27d-404647246846)

</details>

+COUNTER APP

<details>
  <summary>30. UseState Hook </summary>

# Download Default Template

```jsbs
git clone https://github.com/zinotrust/react-starter-template.git ./

npm create-react-app counter-app
yarn create react-app counter-app
```

# Install dependencies

```jsbs
npm install

npm i sass
npm i react-icons
```

### x-zino/counter-app/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

### x-zino/counter-app/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap");

:root {
  --font-family: "Poppins", sans-serif;
  --dark-blue: #0a1930;
  --light-blue: #1f93ff;

  --color-white: #fff;
  --color-dark: #333;

  --color-grey: #eee;
  --box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);

  --color-purple: #9d0191;
  --color-orange: #ff7722;

  --color-primary: #007bff;
  --color-success: #28a745;
  --color-danger: orangered;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  scroll-behavior: smooth;
}

html {
  font-size: 10px;
}

body {
  font-family: var(--font-family);
}

section {
  width: 100%;
  padding: 8rem 0;
}

.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
}

/* UTILITY CLASSES */

/* Flex */
.--flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
.--flex-start {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
}
.--flex-end {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
.--flex-between {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.--dir-column {
  flex-direction: column;
}

.--flex-dir-column {
  display: flex;
}

.--align-center {
  display: flex;
  align-items: center;
}

.--100vh {
  height: 100vh;
}

.--mh-100vh {
  min-height: 100vh;
}

/* Grid */
.--grid-15 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  row-gap: 1rem;
  column-gap: 1rem;
}
.--grid-25 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(24rem, 1fr));
  row-gap: 1rem;
  column-gap: 1rem;
}

/* Center All */
.--center-all {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  margin: auto;
  text-align: center;
}

/* Heading */
h1,
h2,
h3,
h4 {
  font-weight: 500;
  line-height: 1.2;
  color: var(--color-dark);
  margin-bottom: 1rem;
}
h1 {
  font-size: 4rem;
}
h2 {
  font-size: 3rem;
}
h3 {
  font-size: 2.5rem;
}
h4 {
  font-size: 2rem;
}

p {
  font-size: 1.5rem;
  font-weight: 300;
  line-height: 1.3;
  color: var(--color-dark);
}
.--text-xl {
  font-size: 4.5rem;
}
.--text-lg {
  font-size: 4rem;
}

.--text-md {
  font-size: 3rem;
}

.--text-sm {
  font-size: 1.2rem;
  font-weight: 300;
}

.--text-p {
  font-size: 1.5rem;
  font-weight: 300;
  line-height: 1.3;
  color: var(--color-dark);
}

.--fw-bold {
  font-weight: 600;
}
.--fw-thin {
  font-weight: 200;
}

/* Text Color */
.--text-light {
  color: #fff;
}

.--color-primary {
  color: #007bff;
}
.--color-danger {
  color: orangered;
}
.--color-success {
  color: #28a745;
}

.--color-white {
  color: #fff;
}

/* Center Text */
.--text-center {
  text-align: center;
}

/* Card */
.--card {
  border: 1px solid transparent;
  border-radius: 5px;
  box-shadow: var(--box-shadow);
  overflow: hidden;
}

/* Margin */
.--m {
  margin: 1rem;
}
.--ml {
  margin-left: 1rem;
}
.--mr {
  margin-right: 1rem;
}

.--mb {
  margin-bottom: 1rem;
}

.--my {
  margin: 1rem 0;
}
.--mx {
  margin: 0 1rem;
}

.--m2 {
  margin: 2rem;
}

.--ml2 {
  margin-left: 2rem;
}
.--mr2 {
  margin-right: 2rem;
}

.--mb2 {
  margin-bottom: 2rem;
}

.--my2 {
  margin: 2rem 0;
}

.--mx2 {
  margin: 0 2rem;
}

/* Padding */
.--p {
  padding: 1rem;
}
.--p2 {
  padding: 2rem;
}
.--py {
  padding: 1rem 0;
}
.--py2 {
  padding: 2rem 0;
}
.--px {
  padding: 0 1rem;
}
.--px2 {
  padding: 0 2rem;
}

.--btn {
  font-size: 1.6rem;
  font-weight: 400;
  padding: 6px 8px;
  margin: 0 5px 0 0;
  border: 1px solid transparent;
  border-radius: 3px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.3s;
}

.--btn:hover {
  transform: translateY(-2px);
}

.--btn-lg {
  padding: 8px 10px;
}

.--btn-block {
  width: 100%;
}

.--btn-primary {
  color: #fff;
  background: #007bff;
}
.--btn-secondary {
  color: #fff;
  border: 1px solid #fff;
  background: transparent;
}
.--btn-danger {
  color: #fff;
  background: orangered;
}

.--btn-success {
  color: #fff;
  background: #28a745;
}

/* Background */
.--bg-light {
  background: #fff;
}
.--bg-dark {
  background: var(--color-dark);
}
.--bg-primary {
  background: var(--color-primary);
}
.--bg-success {
  background: var(--color-success);
}
.--bg-grey {
  background: var(--color-grey);
}

.--form-control {
  font-size: 1.6rem;
  font-weight: 300;
}

.--form-control > * {
  margin: 5px 0;
}

.--form-control input {
  font-size: 1.6rem;
  font-weight: 300;
  padding: 8px 1rem;
  border: 1px solid #777;
  border-radius: 3px;
  outline: none;
}
.--form-control select {
  font-size: 1.4rem;
  font-weight: 400;
  padding: 8px 1rem;
  border: 1px solid #777;
  border-radius: 3px;
}

.--form-control label {
  font-size: 1.6rem;
  font-weight: 400;
  display: inline-block;
  min-width: 7rem;
  color: var(--color-dark);
  margin-right: 1rem;
}

@media screen and (max-width: 600px) {
  .--flex-dir-column {
    flex-direction: column;
  }
}

.--block {
  display: block;
}
.--inline-block {
  display: inline-block;
}

.--width-100 {
  width: 100%;
}

.--width-500px {
  width: 500px;
}

.--line {
  position: relative;
}
.--line::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: -5px;
  transform: translateX(-50%);
  width: 5rem;
  height: 3px;
  margin-bottom: 1rem;

  background: rgb(217, 8, 170);
  background: linear-gradient(
    135deg,
    rgba(163, 1, 191, 1) 44%,
    rgba(217, 8, 170, 1) 57%
  );
}

.--list-style-none {
  list-style: none;
}

.--profile-img {
  width: 6rem;
  height: 6rem;
  border: 1px solid #ccc;
  border-radius: 50%;
}

a {
  font-size: 1.4rem;
  color: var(--dark-blue);
  text-decoration: none;
  transition: all 0.2s;
}

a:hover {
  color: var(--color-dark);
  font-size: 1.5rem;
}
```

### x-zino/counter-app/src/App.js:

```js
import "./App.scss";
import UseState from "./components/UseState";

function App() {
  return (
    <div>
      <UseState />
    </div>
  );
}

export default App;
```

### x-zino/counter-app/src/components/UseState.js:

```js
import React, { useState } from "react";

const UseState = () => {
  const [greet, setGreet] = useState("Goodmorning");

  const handleClick = () => {
    setGreet((prev) => {
      return prev === "Goodmorning" ? "Goodevening" : "Goodmorning";
    });
  };

  return (
    <section className="--flex-center --10vh">
      <div className="container --center-all">
        <h3>React Page</h3>
        <h1>{greet}...</h1>
        <button onClick={handleClick} className="--btn --btn-primary --btn-lg">
          Change Text
        </button>
      </div>
    </section>
  );
};

export default UseState;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/e46f469c-0b69-4a0d-b8e2-f7d2d44091dc)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/13ab0abf-8694-43c8-b480-9020927481eb)

</details>

<details>
  <summary>31. Counter App </summary>

# Initial JS DOM manipulation

```html
<section class="--flex-center --100vh --bg-primary">
  <div class="container --bg-light --p2 --m2 --center-all">
    <h3>React Counter</h3>
    <h1 class="count">0</h1>
    <div class="buttons --flex-center">
      <button class="subtract --btn --btn-danger">Subtract</button>
      <button class="reset --btn">Reset</button>
      <button class="add --btn --btn-primary">Add</button>
    </div>
  </div>
</section>

<script>
  const count = document.querySelector(".count");
  const add = document.querySelector(".add");
  const subtract = document.querySelector(".subtract");
  const reset = document.querySelector(".reset");

  add.addEventListener("click", () => {
    count.innerHTML++;
  });

  subtract.addEventListener("click", () => {
    count.innerHTML--;
  });

  reset.addEventListener("click", () => {
    count.innerHTML = 0;
  });
</script>
```

### x-zino/counter-app/src/App.js:

```js
import "./App.scss";
import Counter from "./components/Counter";

function App() {
  return (
    <div>
      <Counter />
    </div>
  );
}

export default App;
```

### x-zino/counter-app/src/components/Counter.jsx:

```js
import React, { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);

  const handleSubtract = () => {
    setCount((prev) => prev - 1);
  };

  const handleReset = () => {
    setCount(0);
  };

  const handleAdd = () => {
    setCount((prev) => prev + 1);
  };

  return (
    <section classNameName="--flex-center --100vh --bg-primary">
      <div className="container --bg-light --p2 --m2 --center-all">
        <h3>React Counter</h3>
        <h1>{count}</h1>
        <div className="buttons --flex-center">
          <button onClick={handleSubtract} className="--btn --btn-danger">
            Subtract
          </button>
          <button onClick={handleReset} className="--btn">
            Reset
          </button>
          <button onClick={handleAdd} className="--btn --btn-primary">
            Add
          </button>
        </div>
      </div>
    </section>
  );
};

export default Counter;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/f0fc4158-e463-472a-925f-9454b23c9619)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/0749189e-afd8-40b1-912c-4a8757214bbf)

</details>

<details>
  <summary>32. useState Array </summary>

# useState Array

```js

```

```js

```


</details>
