# REACTJS COURSE - PEDROTECH

## [COURSE](https://www.youtube.com/playlist?list=PLpPqplz6dKxW5ZfERUPoYTtNUNvrEebAR)

+INTRODUCTION

<details>
  <summary>1. Initialize React App</summary>

# Initialize React App

<img width="958" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6f8f88e6-8db2-4f86-80f5-01b56246df87">
<img width="958" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/031d0e5b-3e5c-4493-8da0-89b5ffbf5df3">
<img width="1305" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/43a68d9f-5584-42f9-a4ce-557b9828bdef">

NPM Version:

```bash
npm -v
```

Node Version:

```bash
node -v
```

Install React App:

```bash
npx create-react-app .
npx create-react-app reactjs-course
npx create-react-app reactjs-course --template typescript
npx create-react-app reactjs-course --template redux
npx create-react-app reactjs-course --template redux-typescript
```

Run React App:

```bash
cd reactjs-course

yarn start
npm start
```

### NXT/reactjs-course/src/index.js:

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

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

### NXT/reactjs-course/src/App.js:

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

</details>

<details>
  <summary>2. Setup Files</summary>

# Setup Files

<img width="961" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f67aa509-d5ac-4f9b-905a-a9ccac2bfd0c">
<img width="961" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5654005a-5d53-4efb-99fe-7f24204ab530">
<img width="1306" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/18240a58-3a81-4697-9e3b-6caed98aa9b8">

Index.js:

```Javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

App.js:

```Javascript
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Home</h1>
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>3. JSX and Components</summary>

# JSX and Components

<img width="962" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4d4f7bff-b582-4e47-af18-c3889c593d73">
<img width="962" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/98fe735f-fa08-4157-a202-21a07ff15a65">
<img width="1307" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f383e2e4-4bd2-43fb-b838-215bbb67f3b5">

### NXT/reactjs-course/src/App.js:

```Javascript
import "./App.css";
import User from "./components/User";

function App() {
  return (
    <div className="App">
      <h1>Home</h1>
      <User />
      <User />
      <User />
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/User.jsx:

```js
import React from "react";

export default function User() {
  return (
    <div>
      <h1>Pedro</h1>
      <h2>21</h2>
      <h2>pedro@pedro.com</h2>
    </div>
  );
}
```

</details>

<details>
  <summary>4. Props</summary>

# Props

<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c29841ab-1afa-45dc-ab0f-652672357be8">
<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dd01db7d-91e8-41cd-9ed0-264aaa94ebc8">
<img width="1307" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a535cf05-5c4c-48b3-b53e-5cab5eac66d8">

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import Job from "./components/Job";

function App() {
  return (
    <div className="App">
      <Job salary={90000} position="Senior SDE" company="Amazon" />
      <Job salary={12000} position="Junior SDE" company="Google" />
      <Job salary={10000} position="Project Manager" company="Netflix" />
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/Job.jsx:

```js
import React from "react";

export default function Job(props) {
  const { salary, position, company } = props;

  return (
    <div>
      <h2> {salary}</h2>
      <h2> {position}</h2>
      <h2> {company}</h2>
    </div>
  );
}
```

</details>

<details>
  <summary>5. CSS Module Stylesheets</summary>

# CSS Module Stylesheets

<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/99b574aa-5d46-4bef-863b-94824726330c">
<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/446d9983-a307-4b6d-9c06-1787becbe2bd">
<img width="1306" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/da669038-b788-4ac8-81a1-044e25a99620">

### NXT/reactjs-course/src/App.module.css:

```css
.App {
  text-align: center;
}

.name {
  color: red;
}
```

### NXT/reactjs-course/src/App.js:

```js
import styles from "./App.module.css";

function App() {
  return (
    <div className={styles.App}>
      <h1 className={styles.name}> Pedro </h1>
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>6. Ternary Operator</summary>

# Ternary Operator

<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6679ed24-0f30-4e27-8344-02275baf8988">
<img width="1306" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5dbc12a4-31b2-4f98-9d7c-314fa01aedca">

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";

// const age = 19;

// if(age >= 18) {
//   console.log("IS OVER AGE");
//   } else {
//   console.log("IS UNDER AGE");
// }

// age >= 18 ? console.log("IS OVER AGE") : console.log("IS UNDER AGE");

function App() {
  const age = 19;

  return (
    <div className="App">
      {age >= 18 ? <h1> OVER AGE</h1> : <h1> UNDER AGE</h1>}
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>7. Inline Styling</summary>

# Inline Styling

<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6d53384a-1e86-45e7-bb3d-bebfd9411cbb">
<img width="1307" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2b432998-1b4a-4085-bef2-c6d7b6fefa43">

### NXT/reactjs-course/src/App.js:

```Javascript
import "./App.css";

function App() {
  const age = 19;
  const isGreen = true;

  return (
    <div className="App">
      {age >= 18 ? <h1> OVER AGE</h1> : <h1> UNDER AGE</h1>}
      <h2 style={{ color: "red", backgroundColor: "black" }}>COLOR 1</h2>
      <h2
        style={{ color: isGreen ? "green" : "red", backgroundColor: "black" }}
      >
        COLOR 2
      </h2>
    </div>
  );
}
export default App;
```

</details>

<details>
  <summary>8. Conditional Rendering</summary>

# Conditional Rendering

<img width="962" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/309227b2-f59a-47dc-8d95-06d9429c53d6">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/2c56f89a-f9ce-4310-ad11-05a544facf4d)

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";

function App() {
  const age = 19;
  const isActive = true;

  return (
    <div className="App">
      {age >= 18 ? <h1> OVER AGE</h1> : <h1> UNDER AGE</h1>}
      {isActive &&  <button>Continue Registration</button>}
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>9. Lists in React</summary>

# Lists in React

<img width="962" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/165dc6a1-95af-4e24-8f08-19c5f103b6ed">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/ae6af9ef-340a-4799-abb5-d6a4585ce2c6)

### NXT/reactjs-course/src/App.js:

```Javascript
import "./App.css";

function App() {
  const planets = [
    { name: "Mars", isGasPlanet: false },
    { name: "Earth", isGasPlanet: false },
    { name: "Jupiter", isGasPlanet: true },
    { name: "Venus", isGasPlanet: false },
    { name: "Neptune", isGasPlanet: true },
    { name: "Uranus", isGasPlanet: true },
  ];

  return (
    <div className="App">
      <h2>Not Gas Planets:</h2>
      {planets.map(
        (planet, key, arr) => !planet.isGasPlanet && <h1 key={key}> {planet.name} </h1>
      )}
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>10. Importing Components</summary>

# Importing Components

<img width="962" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5ab5ce6a-d05c-4ead-93ef-281f4064b51e">
<img width="962" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0c8f63be-b837-4dbf-9fc1-9aa6a63c12e6">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/3cefa0e9-08a8-48a5-9fb2-a79c11b0769b)

### NXT/reactjs-course/src/App.js:

```Javascript
import "./App.css";
import User from "./components/User";

function App() {
  const users = [
    { name: "Pedro", age: 21 },
    { name: "Jake", age: 25 },
    { name: "Jessica", age: 45 },
  ];

  return (
    <div className="App">
      {users.map((user, key, arr) => {
        return <User name={user.name} age={user.age} />;
      })}
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/User.jsx:

```Javascript
import React from "react";

export default function User(props) {
  return (
    <div>
      <h2>
        {props.name} - {props.age}
      </h2>
    </div>
  );
}
```

</details>

<details>
  <summary>11. Exercise - Digital Clock and Counter</summary>

# Exercise - Digital Clock and Counter

<img width="962" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/24f6fa74-c66a-4356-a1e9-e48c59f369d9">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/1bef88ca-1eec-4f0c-9ba3-7e73aab25aec)

###NXT/reactjs-course/src/App.js:

```Javascript
import "./App.css";
import {useState} from 'react';

function App() {
    const [age, setAge] = useState(0);
    const [time, setTime] = useState('00:00:00 AM');

    setInterval(() => {
      const date = new Date();
      setTime(date.toLocaleTimeString("en-us"));
    }, 1000);

    return (
      <div className="App">
        <h1>Age: {age}</h1>
        <h1 style={{color: "grey"}}>Time: {time}</h1>
        <button onClick={() => setAge(age => age + 1)}>Increase</button>
        <button onClick={() => setAge(age => age - 1)}>Decrease</button>
      </div>
    );
}

export default App;
```

</details>

<details>
  <summary>12. Exercise - Digital Clock with Start/Stop Control </summary>

# Exercise - Digital Clock with Start/Stop Control

<img width="962" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e30c01b4-a2ee-4b42-acb7-70c4fd296a00">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/877dbbb4-2c56-4205-b63f-51b7af43c128)

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { useState, useEffect} from 'react';

function App() {

    const [time, setTime] = useState('00:00:00 AM');
    const [isON, setIsON] = useState(true);

    useEffect(() => {
      if(isON) {
        const interval = setInterval(myTimer, 1000);
        return () => clearInterval(interval);
      }
    }, [isON])

    function myTimer() {
        const date = new Date();
        setTime(date.toLocaleTimeString('en-US'));
    }

    const handleStop = () => {
      console.log('Stopping...');
      setIsON(false);
    }

    const handleStart = () => {
      console.log('Starting...');
      setIsON(true);
    }

    const myStyle = {
      padding: '10px 20px',
      marginRight: '10px',
    }

    return (
      <div className="App">
        <h1>My Digital Clock</h1>
        <h2 style={{fontSize: "3rem", color: "gray"}}>{time}</h2>
        <button onClick={handleStart} style={myStyle }>Start</button>
        <button onClick={handleStop} style={myStyle }>Stop</button>
      </div>
    );
}

export default App;
```

</details>

<details>
  <summary>13. Deploy React App to Github Pages</summary>

# Deploy React App to Github Pages

# Create a new repository on the command line:

```bash
echo "# my-project" >> README.md
git init
git add .
# git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/machadop1487/my-project.git
git push -u origin main
```

# Push an existing repository from the command line:

```bash
git remote add origin https://github.com/machadop1487/my-project.git
git branch -M main
git push -u origin main
```

# Use Access Token to connect to Github -
### Generate a personal access token. This can be done in the application settings of your GitHub account.

```bash
git remote -v
git remote remove origin
git remote add origin https://<your-username>:<token>@github.com/<username>/<repo-name>.git
```

# Install dependencies:

```bash
npm install gh-pages --save-dev

yarn add -D gh-pages
```

# Set homepage in package.json:

```bash
"homepage": "http://<username>.github.io/<repo-name>/"
"homepage": "http://machadop1487.github.io/my-project/"
```

```json
{
  "homepage": "http://omeatai.github.io/Digital-Clock-Project/",
  "name": "digital-clock-project",
  "version": "0.1.0",
  "private": true
}
```

# Add Scripts to package.json:

```bash
"predeploy": "npm run build",
"deploy": "gh-pages -d build",
```

```json
{
  "homepage": "http://omeatai.github.io/Digital-Clock-Project/",
  "name": "digital-clock-project",
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
    "predeploy": "npm run build",
    "deploy": "gh-pages -d build",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

# Make Commit:

```bash
git add .
git commit -m "Deploy to Github Pages"
git push -u origin main

# git push origin main
# git push
```

# Deploy github pages branch:

```bash
npm run deploy
```

```bash
Settings -> Pages -> Source -> Branch (gh-pages) -> /(root) folder
```

```bash
Click on the publish link to see the app.
```

</details>

+REACT API

<details>
  <summary>14. Using State Hooks</summary>

# Using State Hooks

<img width="962" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b2aba2fc-935c-4032-9139-4a82ea6b9aec">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/d4bc06df-028f-46f1-aab1-13a61df7a3fd)

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  const increase = () => {
    setCount((count) => count + 1);
  };
  const decrease = () => {
    setCount((count) => count - 1);
  };
  const setToZero = () => {
    setCount(0);
  };

  return (
    <div className="App">
      <div>
        <button onClick={increase}>Increase</button>
      </div>
      <div>
        <button onClick={decrease}>Decrease</button>
      </div>
      <div>
        <button onClick={setToZero}>Set to Zero</button>
      </div>
      <div>{count}</div>
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>15. Exercise - TodoList </summary>

# Exercise - TodoList

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9f533536-7862-4184-8851-7722acffdd6a">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ee5a8418-f029-4673-8376-2ca1f77543dd">
<img width="1303" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3693f27b-a0c5-4381-bad9-b674a090c7f6">

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { useState } from "react";
import Task from "./components/Task";

function App() {
  const [todoList, setTodoList] = useState([]);
  const [newTask, setNewTask] = useState("");

  const handleChange = (event) => {
    setNewTask(event.target.value);
  };

  const addTask = () => {
    const task = {
      id: todoList.length === 0 ? 1 : todoList[todoList.length - 1].id + 1,
      taskName: newTask,
      completed: false,
      pending: false,
    };
    setTodoList(task.taskName !== "" ? [...todoList, task] : todoList);
  };

  const deleteTask = (id) => {
    setTodoList(todoList.filter((task) => task.id !== id));
  };

  const completeTask = (id) => {
    setTodoList(
      todoList.map((task) => {
        if (task.id === id) {
          return { ...task, completed: true, pending: false };
        } else {
          return task;
        }
      })
    );
  };

  const pendingTask = (id) => {
    setTodoList(
      todoList.map((task) => {
        if (task.id === id) {
          return { ...task, completed: false, pending: true };
        } else {
          return task;
        }
      })
    );
  };

  return (
    <div className="App">
      <div className="addTask">
        <input onChange={handleChange} />
        <button onClick={addTask}> Add Task</button>
      </div>
      <div className="list">
        {todoList.map((task) => {
          return (
            <Task
              key={task.id}
              taskName={task.taskName}
              id={task.id}
              completed={task.completed}
              pending={task.pending}
              deleteTask={deleteTask}
              completeTask={completeTask}
              pendingTask={pendingTask}
            />
          );
        })}
      </div>
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/Task.jsx:

```js
import React from "react";

export default function Task(props) {
  return (
    <div
      className="task"
      style={{
        backgroundColor: props.completed
          ? "green"
          : props.pending
          ? "red"
          : "white",
      }}
    >
      <h1>{props.taskName}</h1>
      <button onClick={() => props.completeTask(props.id)}> Complete </button>
      <button onClick={() => props.pendingTask(props.id)}> Pending </button>
      <button onClick={() => props.deleteTask(props.id)}> X </button>
    </div>
  );
}
```

</details>

<details>
  <summary>16. React Component Lifecycle</summary>

# React Component Lifecycle

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a4c04199-4965-4385-b4dd-2a85e6dd33e7">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5e064ee2-456a-4702-a3c9-16cdf9676734">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/a7603144-6860-4bcb-a0d7-d6bef31b2e2f)

```bash
- mounting
- updating
- unmounting
```

### NXT/reactjs-course/src/App.js:

```Javascript
import "./App.css";
import { useState } from "react";
import { Text } from "./Text";

function App() {
  const [showText, setShowText] = useState(false);

  return (
    <div className="App">
      <button
        onClick={() => {
          setShowText(!showText);
        }}
      >
        Show Text
      </button>

      {showText && <Text />}
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/Text.jsx:

```Javascript
import React from "react";
import { useState, useEffect } from "react";

export const Text = () => {
  const [text, setText] = useState("");

  useEffect(() => {
    console.log("COMPONENT MOUNTED");

    return () => {
      console.log("COMPONENT UNMOUNTED");
    };
  }, []);

  return (
    <div>
      <input
        onChange={(event) => {
          setText(event.target.value);
        }}
      />

      <h1> {text}</h1>
    </div>
  );
};
```

</details>

<details>
  <summary>17. Fetching Data from API</summary>

# Fetching Data from API

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ad337952-9f97-4a3c-9b15-f47760676a83">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/34d57def-d67b-49df-a977-8dc4728af3d6)

### NXT/reactjs-course/src/App.js:

```Javascript
import "./App.css";
import { useEffect, useState } from "react";

function App() {

  const [fact, setFact] = useState("");

  useEffect(() => {
    handleNewFact();
  }, []);

  const handleNewFact = () => {
    fetch("https://catfact.ninja/fact")
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setFact(data.fact);
      });
  };

  return (
    <div className="App">
      <button onClick={handleNewFact}>Generate Cat Fact</button>
      <p>{fact}</p>
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>18. Using Axios to Fetch catfact API</summary>

# Using Axios to Fetch catfact API

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ae18551d-03fc-4529-82ef-7f88d9518545">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/00987b19-0fe4-4571-9daf-875319c68ccf)

# Install Axios:

```bash
yarn add axios
npm install axios
```

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { useEffect, useState } from "react";
import Axios from "axios";

function App() {
  const [fact, setFact] = useState("");

  useEffect(() => {
    handleNewFact();
  }, []);

  const handleNewFact = () => {
    Axios.get("https://catfact.ninja/fact")
      .then((res) => {
        setFact(res.data.fact);
        console.log(res.data.fact);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="App">
      <button onClick={handleNewFact}>Generate Cat Fact</button>
      <p>{fact}</p>
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>19. Using Axios to Fetch agify API</summary>

# Using Axios to Fetch agify API

### NXT/reactjs-course/src/App.js:

With https://api.agify.io?name=

```js
import "./App.css";
import { useState } from "react";
import Axios from "axios";

function App() {
  const [person, setPerson] = useState({name: "", age: ""});
  const [show, setShow] = useState(false);

  const fetchData = () => {
    if(person?.name){
      Axios.get(`https://api.agify.io?name=${person?.name}`)
      .then((res) => {
        setPerson(res.data);
        console.log(res.data);
        setShow(true);
      })
      .catch((err) => {
        console.log(err);
      });
    }

  };

  const handleChange = (e) => {
    setPerson({ ...person, name: e.target.value });
    setShow(false);
  };

  return (
    <div className="App">
      <br/>
      <input onChange={handleChange} type="text" placeholder="Charles..." value={person?.name} />
      <br/>
      <button onClick={fetchData}>Generate Age</button>
      <p>{person?.name || "Charles"} is {show ? person?.age : "___"} years old.</p>
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>20. Using Axios to Fetch excuser API</summary>

# Using Axios to Fetch excuser API

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c924ef4c-78eb-4bfa-bb59-deb8d6ae7c2d">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/6bf267e6-4de6-4597-9f0a-54ee55f8d2df)

### NXT/reactjs-course/src/App.js:

With https://excuser-three.vercel.app/v1/excuse

```js
import "./App.css";
import Axios from "axios";
import { useState } from "react";

function App() {
  const [generatedExcuse, setGeneratedExcuse] = useState("");

  const fetchExcuse = (excuse) => {
    Axios.get(`https://excuser-three.vercel.app/v1/excuse/${excuse}`).then(
      (res) => {
        setGeneratedExcuse(res.data[0].excuse);
      }
    );
  };

  return (
    <div className="App">
      <h1> Generate An Excuse </h1>
      <button onClick={() => fetchExcuse("party")}> Party</button>
      <button onClick={() => fetchExcuse("family")}> Family</button>
      <button onClick={() => fetchExcuse("office")}> Office </button>

      <p> {generatedExcuse} </p>
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>21. React Router DOM</summary>

# React Router DOM

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/188bd9ed-0948-491a-8acb-4100a0c2943b">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4722da27-8776-4776-9094-137dc6510f99">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c7dd42be-c1b4-4279-b424-9eb242b4bc5e">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f0efd9e9-39d9-45a0-9fcd-9d52f50a4d9e">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/431aae6d-f1d9-4e3b-95aa-c1c3b63e9325">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/92d23736-2a86-4f7d-9ad8-9da62f20e0fb)

# Install React Router DOM

```bash
yarn add react-router-dom
npm install react-router-dom
```

### NXT/reactjs-course/src/App.js:

```Javascript
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Home } from "./components/Home";
import { Menu } from "./components/Menu";
import { Contact } from "./components/Contact";
import { Navbar } from "./components/Navbar";

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/menu" element={<Menu />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="*" element={<h1> PAGE NOT FOUND</h1>} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/Navbar.jsx:

```js
import { Link } from "react-router-dom";

export const Navbar = () => {
  return (
    <div>
      <Link to="/"> Home </Link>
      <Link to="/menu"> Menu </Link>
      <Link to="/contact"> Contact </Link>
    </div>
  );
};
```

### NXT/reactjs-course/src/components/Home.jsx:

```Javascript
export const Home = () => {
    return <h1> THIS IS THE HOME PAGE</h1>;
  };
```

### NXT/reactjs-course/src/components/Menu.jsx:

```Javascript
export const Menu = () => {
    return <h1> THIS IS THE MENU PAGE</h1>;
  };
```

### NXT/reactjs-course/src/components/Contact.jsx:

```Javascript
export const Contact = () => {
    return <h1> THIS IS THE CONTACT PAGE</h1>;
  };
```

</details>

<details>
  <summary>22. React Router Dom Version 6</summary>

# React Router Dom Version 6

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/868483ab-fb5d-461e-a5e1-329561253585">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5dae0e33-0347-4b30-8ae4-199d5af1dee5">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/be30f181-4efa-4aa0-9658-26bb4457d9ff">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b5c3a8f5-9b1c-44f2-a7b3-412bfc4faded">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/be22b81f-d458-47ef-84a0-59d87c43f487">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/ad5e5e04-eb1b-458f-ad19-1da1c039a206)

# Install React Router Dom Version 6

```bash
npm install react-router-dom@6

yarn add react-router-dom@6
```

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import Profile from "./pages/Profile";
import ErrorPage from "./pages/ErrorPage";

function App() {
  return (
    <Router>
      <nav>
        <Link to="/"> Home </Link>
        <Link to="/about"> About </Link>
        <Link to="/profile"> Profile </Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/profile/" element={<Profile />} />
        <Route path="/profile/:username" element={<Profile />} />
        <Route path="*" element={<ErrorPage />} />
      </Routes>
      <div> Footer </div>
    </Router>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/Home.jsx:

```Javascript
import React from "react";

function Home() {
  return <div> THIS IS THE HOME PAGE</div>;
}

export default Home;
```

### NXT/reactjs-course/src/components/About.jsx:

```Javascript
import React from "react";

function About() {
  return <div>THIS IS THE ABOUT PAGE</div>;
}

export default About;
```

### NXT/reactjs-course/src/components/Profile.jsx:

```Javascript
import React from "react";
import { useNavigate, useParams } from "react-router-dom";

function Profile() {
  let navigate = useNavigate();
  let { username } = useParams();
  return (
    <div>
      THIS IS THE PROFILE PAGE FOR {username || "Admin"}!
      <button
        onClick={() => {
          navigate("/about");
        }}
      >
        {" "}
        Change to about page
      </button>
    </div>
  );
}

export default Profile;
```

</details>

<details>
  <summary>23. useContext Hook (Context API)</summary>

# useContext Hook (Context API)

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f236b31f-b15d-4f58-b15c-04d05d4367b7">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/974a65cc-0c4b-494e-bc18-3f4cf65e6069">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e20ba6d0-b346-408f-b18b-171c4778f825">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1b0c087a-7fca-4667-b7e6-e09819a6426a">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/b46a80eb-360d-4213-ad36-3056dfa7b6fe)

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Home } from "./components/Home";
import { Profile } from "./components/Profile";
import { Contact } from "./components/Contact";
import { Navbar } from "./components/Navbar";
import {useState, createContext } from "react";

export const AppContext = createContext();

function App() {
  const [username, setUsername] = useState("Pedro");

  return (
    <div className="App">
      <AppContext.Provider value={{username, setUsername}}>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home username={username}/>} />
          <Route path="/profile" element={<Profile username={username} setUsername={setUsername}/>} />
          <Route path="/contact" element={<Contact username={username} />} />
          <Route path="*" element={<h1> PAGE NOT FOUND</h1>} />
        </Routes>
      </Router>
      </AppContext.Provider>
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/Home.jsx:

```Javascript
import { useContext } from 'react';
import { AppContext } from '../App';

export const Home = () => {
  const { username } = useContext(AppContext);
  return <h1> THIS IS THE HOME PAGE for {username}.</h1>;
};
```

### NXT/reactjs-course/src/components/Profile.jsx:

```Javascript
import { ChangeProfile } from "./changeProfile";
import { useContext } from 'react';
import { AppContext } from '../App';

export const Profile = (props) => {
  const { username } = useContext(AppContext);

  return (
    <div>
      PROFILE, user is: {username}
      <ChangeProfile />
    </div>
  );
};
```

### NXT/reactjs-course/src/components/ChangeProfile.jsx:

```Javascript
import { useState } from "react";
import { useContext } from 'react';
import { AppContext } from '../App';

export const ChangeProfile = (props) => {
    const [newUsername, setNewUsername] = useState("");
    const { setUsername } = useContext(AppContext);

    return (
        <div>
            <input
                onChange={(event) => {
                    setNewUsername(event.target.value);
                }}
            />
            <button onClick={()=>{setUsername(newUsername)}}> Change Username</button>
        </div>
    );
};

```

</details>

<details>
  <summary>24. React Query Library</summary>

# React Query Library

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/240011a9-5c38-419e-bb37-794459c3fd10">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0fda52e3-3af1-47df-86cc-0bb3f46f6a5e">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/ce394b63-a496-46ab-bc0a-42ee9a0387c3)

# Install React Query:

```bash
npm install @tanstack/react-query
```

# Install Axios:

```bash
npm install axios
```

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Home } from "./components/Home";
import { Profile } from "./components/Profile";
import { Contact } from "./components/Contact";
import { Navbar } from "./components/Navbar";
import { useState, createContext } from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

export const AppContext = createContext();

function App() {
  const [username, setUsername] = useState("Pedro");
  const [newUsername, setNewUsername] = useState("");
  const client = new QueryClient({
    defaultOptions: {
      queries: {
        refetchOnWindowFocus: true,
      },
    },
  });

  return (
    <div className="App">
      <QueryClientProvider client={client}>
        <AppContext.Provider
          value={{ username, setUsername, newUsername, setNewUsername }}
        >
          <Router>
            <Navbar />
            <Routes>
              <Route path="/" element={<Home username={username} />} />
              <Route
                path="/profile"
                element={
                  <Profile username={username} setUsername={setUsername} />
                }
              />
              <Route
                path="/contact"
                element={<Contact username={username} />}
              />
              <Route path="*" element={<h1> PAGE NOT FOUND</h1>} />
            </Routes>
          </Router>
        </AppContext.Provider>
      </QueryClientProvider>
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/Home.jsx:

```Javascript
import { useContext } from "react";
import { AppContext } from "../App";
import { useQuery } from "@tanstack/react-query";
import Axios from "axios";

export const Home = () => {
  const { username } = useContext(AppContext);
  const {
    data: catData,
    isLoading,
    isError,
    error,
    refetch,
  } = useQuery(["cat"], () => {
    return Axios.get("https://catfact.ninja/fact").then((res) => res.data);
    //.catch((err) => console.log(`There was an error: ${err}`));
  });

  return (
    <section className="home">
      <h1> THIS IS THE HOME PAGE for {username}.</h1>
      <h2>Quote:</h2>
      <p>
        {isLoading && "Loading..."}
        {isError ? error.message : catData?.fact}
      </p>
      <button onClick={() => refetch()}>Update Data</button>
    </section>
  );
};
```

</details>

<details>
  <summary>25. React-Hook-Form & Yup</summary>

# React-Hook-Form & Yup

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/25dd8812-d949-4a50-9bda-eb0f23bfd447">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7ccbaff7-025a-42cc-b0d1-14b775058fc0">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/ec45cabc-8989-45bc-9e96-1605ba6a29ed)

# Install React-Hook-Form and Yup:

```bash
npm install react-hook-form yup
```

# Install @hookform/resolvers:

```bash
npm install @hookform/resolvers
```

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { Form } from "./pages/Form";

function App() {
  return (
    <div className="App">
      <Form />
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/Form.jsx:

```js
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";

export const Form = () => {
    const schema = yup.object().shape({
        fullName: yup.string().required("Your Full Name is Required!"),
        email: yup.string().email().required(),
        age: yup.number().positive().integer().min(18).required(),
        password: yup.string().min(4).max(20).required(),
        confirmPassword: yup
            .string()
            .oneOf([yup.ref("password"), null], "Passwords Don't Match")
            .required(),
    });

    const {register, handleSubmit, formState: { errors }, } = useForm({
        resolver: yupResolver(schema),
    });

    const onSubmit = (data) => {
        console.log(data);
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <input type="text" placeholder="Full Name..." {...register("fullName")} />
            <p>{errors.fullName?.message}</p>
            <input type="text" placeholder="Email..." {...register("email")} />
            <p>{errors.email?.message}</p>
            <input type="number" placeholder="Age..." {...register("age")} />
            <p>{errors.age?.message}</p>
            <input
                type="password"
                placeholder="Password..."
                {...register("password")}
            />
            <p>{errors.password?.message}</p>
            <input
                type="password"
                placeholder="Confirm Password..."
                {...register("confirmPassword")}
            />
            <p>{errors.confirmPassword?.message}</p>
            <input type="submit" />
        </form>
    );
};

```

</details>

<details>
  <summary>26. Custom Hooks</summary>

# Custom Hooks

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a04bc5e6-d41d-45c1-aefd-7034df61d77b">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1221da44-2758-4a50-8f23-72f710cc10b3">

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { useToggle } from "./useToggle";

function App() {
  const [isVisible, toggle] = useToggle();
  const [isVisible2, toggle2] = useToggle();

  return (
    <div className="App">
      <button onClick={toggle}>{isVisible ? "Hide" : "Show"}</button>
      {isVisible && <h1> Hidden text</h1>}

      <button onClick={toggle2}>{isVisible2 ? "Hide" : "Show"}</button>
      {isVisible2 && <h1> Hidden text</h1>}
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/hooks/useToggle.jsx:

```js
import { useState } from "react";

export const useToggle = (initialVal = false) => {
    const [state, setState] = useState(initialVal);

    const toggle= () => {
        setState((prev) => !prev);
    };
    return [state, toggle];
};

```

</details>

<details>
  <summary>27. Example - Cat.js Custom Hook </summary>

# Example - Cat.js Custom Hook

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b77fed0f-7c4d-4168-bfb4-e292b44139a9">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2c1e3002-6651-4ff3-b05e-f0d631d5f9ba">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/03390514-2b0f-46cf-9bcb-da7f0ac516c0">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/bacd22b6-1235-4772-af0f-54275f6f9631)

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { Cat } from "./components/Cat";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

function App() {
  const client = new QueryClient({
    defaultOptions: {
      queries: {
        refetchOnWindowFocus: true,
      },
    },
  });

  return (
    <div className="App">
      <QueryClientProvider client={client}>
        <Cat />
      </QueryClientProvider>
    </div>
  );
}
export default App;
```

### NXT/reactjs-course/src/components/Cat.jsx:

```js
import useGetCat from "../hooks/useGetCat";

export const Cat = () => {
  const { data: catData, refetchData: refresh, isCatLoading } = useGetCat();

  if (isCatLoading) {
    return <h1>Loading...</h1>;
  }

  return (
    <div>
      <h1> {isCatLoading ? "Loading..." : catData?.fact}</h1>
      <button onClick={refresh}>Refresh</button>
    </div>
  );
};

```

### NXT/reactjs-course/src/hooks/useGetCat.jsx:

```js
import { useQuery } from "@tanstack/react-query";
import Axios from "axios";

const useGetCat = () => {
    const { data, refetch, isLoading: isCatLoading } = useQuery(["cat"] , async () => {
        return Axios.get("https://catfact.ninja/fact").then((res) => res.data);
    });

    const refetchData = () => {
        console.log("DATA REFRESHED");
        refetch();
    };

    return { data, refetchData, isCatLoading };
};

export default useGetCat;
```

</details>

<details>
  <summary>28. Example - Counter Custom Hook </summary>

# Example - Counter Custom Hook

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f599fce5-2971-45e5-aeb0-cf87b8ced3c6">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/cdb677c3-ee3d-45cb-809b-44b908f5a329">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/35e7a8b9-ecbc-4b32-98b2-3f3e4b8e16e1">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/2c952047-f621-4e8c-a453-96f2dda2a63f)

### NXT/reactjs-course/src/App.js:

```js
import "./App.css";
import { Counter } from "./components/Counter";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

function App() {
  const client = new QueryClient({
    defaultOptions: {
      queries: {
        refetchOnWindowFocus: true,
      },
    },
  });

  return (
    <div className="App">
      <QueryClientProvider client={client}>
        <Counter />
      </QueryClientProvider>
    </div>
  );
}
export default App;
```

### NXT/reactjs-course/src/components/Counter.jsx:

```js
import { useCounter } from "../hooks/useCounter";

export const Counter = () => {
  const { state: count, increment, decrement, reset } = useCounter();

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={increment}>Increment</button>
      <button onClick={reset}>Reset</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
};
```

### NXT/reactjs-course/src/hooks/useCounter.js:

```Javascript
import { useState } from "react";

export const useCounter = (initialCount = 0) => {
  const [state, setState] = useState(initialCount);

  const increment = () => {
    setState(state + 1);
  };

  const decrement = () => {
    setState(state - 1);
  };

  const reset = () => {
    setState(0);
  };

  return { state, increment, decrement, reset };
};

```

</details>

<details>
  <summary>29. React Type Safety (PropTypes)</summary>

# React Type Safety (PropTypes)

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/09cfa61e-5ad9-4235-908f-a9e2bf9a8402">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/54f7a158-e95b-49a6-a55b-5a3ee2f8d6dd">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/94ab1ed1-8e0c-48d2-9fd3-9e44b34021d8)

# Install PropTypes:

```bash
yarn add prop-types
npm install prop-types
```

### NXT/reactjs-course/src/App.js:

```Javascript
import "./App.css";
import { Person } from "./components/Person";

function App() {
  return (
    <div className="App">
      <Person
        name="Pedro"
        email="pedro@gmail.com"
        age={21}
        isMarried={true}
        friends={["jessica", "jake", "jerry", "jasmine"]}
      />
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/Person.jsx:

```Javascript
import PropTypes from "prop-types";

export const Person = (props) => {
    return (
        <div>
            <h1>Name: {props.name}</h1>
            <h1>Email: {props.email}</h1>
            <h1>Age: {props.age}</h1>
            <h1>This person {props.isMarried ? "is" : "is not"} MARRIED</h1>
            <h1>Friends:</h1>
            <ol>
            {props.friends.map((friend, index) => (
                <li key={index}>{`${friend.charAt(0).toUpperCase()}${friend.slice(1)}`}</li>
            ))}
            </ol>
        </div>
    );
};

Person.propTypes = {
    name: PropTypes.string.isRequired,
    email: PropTypes.string.isRequired,
    age: PropTypes.number.isRequired,
    isMarried: PropTypes.bool.isRequired,
    friends: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default Person;
```

</details>

<details>
  <summary>30. React Type Safety (TypeScript)</summary>

# React Type Safety (TypeScript)

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5403b731-4706-45da-b544-65a6c99ab812">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d51b152a-693d-419f-950b-93c5caa74080">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fa9bb219-3bf7-4733-9f68-1c832155e595">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/61d9b41a-b8a7-4a8d-9976-423a4ce4b0ff)

# Install TypeScript:

```bash
sudo npm install -g typescript

npx create-react-app . --template typescript
```

### NXT/reactjs-course/src/App.tsx:

```typescript
import { Person, Country } from "./components/Person";

function App() {
  return (
    <div className="App">
      <Person
        name="Pedro"
        email="pedro@gmail.com"
        age={21}
        isMarried={true}
        friends={["jessica", "jake", "jerry", "jasmine"]}
        country={Country.Nigeria}
      />
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/components/Person.tsx:

```typescript
import { useState } from "react";

interface Props {
  name: string;
  email: string;
  age: number;
  isMarried: boolean;
  friends: string[];
  country: string;
}

export enum Country {
  Brazil = "Brazil",
  Nigeria = "Nigeria",
  USA = "USA",
}

export const Person = (props: Props) => {
  const firstName: string = "Dave";
  const [name, setName] = useState<string>("Adam");
  const getAge = (name: string): number => {
    return props.age;
  };

  return (
    <div>
      <h1>Name: {props.name}</h1>
      <h1>Email: {props.email}</h1>
      <h1>Age: {props.age}</h1>
      <h1>This person {props.isMarried ? "is" : "is not"} MARRIED</h1>
      <h1>{firstName}</h1>
      <h1>{name}</h1>
      <h1>{typeof String(getAge(props.name))}</h1>
      <h1>Friends:</h1>
      <ol>
        {props.friends.map((friend: string, index: number) => (
          <li key={index}>{`${friend.charAt(0).toUpperCase()}${friend.slice(
            1
          )}`}</li>
        ))}
      </ol>
      <h1>Country: {props.country}</h1>
    </div>
  );
};

export default Person;
```

### NXT/reactjs-course/tsconfig.json:

```js
// tsconfig.json
{
  "compilerOptions": {
    "jsx": "react-jsx"
  }
}
```

</details>

<details>
  <summary>31. Redux Toolkit</summary>

# Redux Toolkit

<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2faba1ba-10d0-465f-ab8f-6f53fea9d25c">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/15bb7c22-0ae7-4afb-b0be-a3b382db298d">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dc353970-7128-4be2-89da-5418fc1c69f6">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0706796f-8497-41a7-8b01-c985dc6d82cc">
<img width="992" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/940400ce-0b10-405d-8c5a-d715fddc170c">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/1f2fb075-de64-4fa2-807d-a71e91fc732f)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/af13a0ef-b306-425d-9c66-63218123d9e9)

# Install Redux Toolkit Packages:

```bash
npm install @reduxjs/toolkit react-redux
```

### NXT/reactjs-course/src/App.tsx:

```typescript
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { Home } from "./components/Home";
import { Contact } from "./components/Contact";
import { Login } from "./components/Login";
import { Provider } from "react-redux";
import { store } from "./store";

function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <Router>
          <Link to="/">Home</Link>
          <Link to="/login">Login</Link>
          <Link to="/contact">Contact</Link>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </Router>
      </Provider>
    </div>
  );
}

export default App;
```

### NXT/reactjs-course/src/store.ts:

```typescript
import { configureStore, createSlice, PayloadAction } from "@reduxjs/toolkit";

interface UserStateValue {
  username: string;
}

interface UserState {
  value: UserStateValue;
}

const initialState = { value: { username: "" } } as UserState;

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    login: (state: UserState, action: PayloadAction<UserStateValue>) => {
      state.value = action.payload;
    },
    logout: (state: UserState) => {
      state.value = initialState.value;
    },
  },
});

export const { login, logout } = userSlice.actions;

export const store = configureStore({
  reducer: {
    user: userSlice.reducer,
  },
});

```

### NXT/reactjs-course/src/components/Login.tsx:

```typescript
import { useState } from "react";
import { login, logout } from "../store";
import { useDispatch, useSelector } from "react-redux";

export const Login = () => {
  const [newUsername, setNewUsername] = useState<string>("");
  const dispatch = useDispatch();
  const username = useSelector((state: any) => state.user.value.username);

  return (
    <div>
      <h1>Login</h1>
      <h2>Username: {username}</h2>
      <input
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setNewUsername(e.target.value)
        }
        type="text"
        placeholder="username"
      />
      <button onClick={() => dispatch(login({ username: newUsername }))}>
        Submit Login
      </button>
      <button onClick={() => dispatch(logout())}>Logout</button>
    </div>
  );
};
```

### NXT/reactjs-course/src/components/Home.tsx:

```typescript
import { useDispatch, useSelector } from "react-redux";

export const Home = () => {
  const username = useSelector((state: any) => state.user.value.username);

  return (
    <div>
      <h1>Home</h1>
      <h2>Username: {username}</h2>
    </div>
  );
};
```

### NXT/reactjs-course/src/components/Contact.tsx:

```typescript
export const Contact = () => {
  return <h1>Contact</h1>;
};
```

</details>

+FIREBASE SOCIAL MEDIA PROJECT

<details>
  <summary>32. Introduction</summary>

Create React Project:

```bash
npx create-react-app . --template typescript
```

Run Project:

```bash
npm start
```

index.tsx:

```typescript
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

App.tsx:

```typescript
import React from "react";
import "./App.css";

function App() {
  return (
    <div className="App">
      <h1>React App</h1>
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>73. Setting up Components</summary>

Install React Router DOM

```bash
npm install react-router-dom
```

App.tsx:

```typescript
import React from "react";
import "./App.css";
import { Main } from "./pages/Main";
import { Login } from "./pages/Login";
import { Navbar } from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
```

Navbar.tsx:

```typescript
import { Link } from "react-router-dom";

export const Navbar = () => {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/login">Login</Link>
    </nav>
  );
};
```

Main.tsx:

```ts
export const Main = () => {
  return <h1>Home Page</h1>;
};
```

Login.tsx:

```ts
export const Login = () => {
  return <h1> Login Page</h1>;
};
```

</details>

<details>
  <summary>74. Integrate Firebase</summary>

Install Firebase:

```bash
npm install firebase
```

config.ts:

```ts
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDdFw8SFSfGwmm3S5CBX5nFi7KMxd8GyyQ",
  authDomain: "pedro-app-8bd3b.firebaseapp.com",
  projectId: "pedro-app-8bd3b",
  storageBucket: "pedro-app-8bd3b.appspot.com",
  messagingSenderId: "679821378683",
  appId: "1:679821378683:web:54f00cc4f7433907150ede",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const provider = new GoogleAuthProvider();
```

</details>

<details>
  <summary>75. Login Google Authentication</summary>

```bs
npm install react-firebase-hooks
```

Login.tsx:

```tsx
import { auth, provider } from "../config/firebase";
import { signInWithPopup } from "firebase/auth";
import { useNavigate } from "react-router-dom";

export const Login = () => {
  const navigate = useNavigate();

  const signInWithGoogle = async () => {
    const result = await signInWithPopup(auth, provider);
    if (result) {
      navigate("/");
    }
  };

  return (
    <div>
      <h1> Login Page</h1>
      <p>Sign In With Google To Continue</p>
      <button onClick={signInWithGoogle}>Sign In With Google</button>
    </div>
  );
};
```

Navbar.tsx:

```tsx
import { Link } from "react-router-dom";
import { auth } from "../config/firebase";
import { useAuthState } from "react-firebase-hooks/auth";
import { signOut } from "firebase/auth";

export const Navbar = () => {
  const [user, loading, error] = useAuthState(auth);

  const signUserOut = async () => {
    await signOut(auth);
  };

  return (
    <nav className="navbar">
      <div className="links">
        <Link to="/">Home</Link>
        <Link to="/login">Login</Link>
      </div>
      <div className="user">
        {user ? (
          <>
            <p>{user?.displayName}</p>
            <img
              src={user?.photoURL || ""}
              alt="photoURL"
              width="20"
              height="20"
            />
            <button onClick={signUserOut}> Log Out</button>
          </>
        ) : null}
      </div>
    </nav>
  );
};
```

App.css:

```css
.App {
  text-align: center;
}

body {
  margin: 0;
  padding: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.navbar {
  width: 100%;
  height: 80px;
  background-color: slateblue;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.navbar .links {
  text-align: center;
  margin-right: 50px;
}

.links a {
  color: white;
  text-decoration: none;
  border-bottom: 3px solid white;
  padding-bottom: 2px;
  margin: 10px;
}

.navbar .user {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 50px;
}

.user p {
  font-size: 15px;
  margin-right: 10px;
  color: white;
}

.user img {
  font-size: 15px;
  border-radius: 50%;
}
```

</details>

<details>
  <summary>76. Create Firebase Collection</summary>

```bs
Firebase -> Build -> Firestore Database -> Collection -> "Posts"
```

```bs
description -> "Hello, people." -> (string)
id -> "pedrotech01" -> (string)
title -> "the first post" -> (string)
username -> "PedroTech" -> (string)
```

</details>

<details>
  <summary>77. Controlling Login availability</summary>

Navbar.tsx:

```tsx
import { Link } from "react-router-dom";
import { auth } from "../config/firebase";
import { useAuthState } from "react-firebase-hooks/auth";
import { signOut } from "firebase/auth";

export const Navbar = () => {
  const [user, loading, error] = useAuthState(auth);

  const signUserOut = async () => {
    await signOut(auth);
  };

  return (
    <nav className="navbar">
      <div className="links">
        <Link to="/">Home</Link>
        {!user ? (
          <Link to="/login">Login</Link>
        ) : (
          <Link to="/createpost">Create Post</Link>
        )}
      </div>
      <div className="user">
        {user ? (
          <>
            <p>{user?.displayName}</p>
            <img src={user?.photoURL || ""} alt="" width="20" height="20" />
            <button onClick={signUserOut}> Log Out</button>
          </>
        ) : null}
      </div>
    </nav>
  );
};
```

</details>

<details>
  <summary>78. Create Post route and Component</summary>

App.tsx:

```tsx
import React from "react";
import "./App.css";
import { Main } from "./pages/Main";
import { Login } from "./pages/Login";
import { CreatePost } from "./pages/createpost/CreatePost";
import { Navbar } from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/login" element={<Login />} />
          <Route path="/createpost" element={<CreatePost />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
```

CreatePost.tsx:

```tsx
export const CreatePost = () => {
  return <div>Create Post</div>;
};
```

</details>

<details>
  <summary>79. Create Post Form</summary>

```bs
npm install react-hook-form yup @hookform/resolvers
```

CreatePost.tsx:

```tsx
import { CreateForm } from "./CreateForm";

export const CreatePost = () => {
  return (
    <div>
      <h1>Create Post</h1>
      <CreateForm />
    </div>
  );
};
```

CreateForm.tsx:

```tsx
import { useForm } from "react-hook-form";
import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";

export const CreateForm = () => {
  interface CreateFormData {
    title: string;
    description: string;
  }

  const schema = yup.object().shape({
    title: yup.string().required("You must add a Title."),
    description: yup.string().required("You must add a Description."),
  });

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<CreateFormData>({
    resolver: yupResolver(schema),
  });

  const onCreatePost = (data: CreateFormData) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onCreatePost)}>
      <input placeholder="Title..." {...register("title")} />
      <p style={{ color: "red" }}>{errors.title?.message}</p>
      <textarea placeholder="Description..." {...register("description")} />
      <p style={{ color: "red" }}>{errors.description?.message}</p>
      <input type="submit" />
    </form>
  );
};
```

</details>

<details>
  <summary>80. Send data to Firebase</summary>

config/firebase.ts:

```tsx
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDdFw8SFSfGwmm3S5CBX5nFi7KMxd8GyyQ",
  authDomain: "pedro-app-8bd3b.firebaseapp.com",
  projectId: "pedro-app-8bd3b",
  storageBucket: "pedro-app-8bd3b.appspot.com",
  messagingSenderId: "679821378683",
  appId: "1:679821378683:web:54f00cc4f7433907150ede",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const provider = new GoogleAuthProvider();
export const db = getFirestore(app);
```

CreateForm.tsx:

```tsx
import { useForm } from "react-hook-form";
import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";
import { addDoc, collection } from "firebase/firestore";
import { auth, db } from "../../config/firebase";
import { useAuthState } from "react-firebase-hooks/auth";
import { useNavigate } from "react-router-dom";

export const CreateForm = () => {
  const [user] = useAuthState(auth);
  const navigate = useNavigate();

  interface CreateFormData {
    title: string;
    description: string;
  }

  const schema = yup.object().shape({
    title: yup.string().required("You must add a Title."),
    description: yup.string().required("You must add a Description."),
  });

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<CreateFormData>({
    resolver: yupResolver(schema),
  });

  const postsRef = collection(db, "posts");

  const onCreatePost = async (data: CreateFormData) => {
    await addDoc(postsRef, {
      ...data,
      username: user?.displayName,
      userId: user?.uid,
    });

    navigate("/");
  };

  return (
    <form onSubmit={handleSubmit(onCreatePost)}>
      <input placeholder="Title..." {...register("title")} />
      <p style={{ color: "red" }}>{errors.title?.message}</p>
      <textarea placeholder="Description..." {...register("description")} />
      <p style={{ color: "red" }}>{errors.description?.message}</p>
      <input type="submit" />
    </form>
  );
};
```

</details>

<details>
  <summary>81. Set Firebase Rules (Permissions)</summary>

```bs
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
```

```bs
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow write, delete, update: if request.auth != null && request.auth.uid == request.resource.data.userId;
      allow read: if request.auth != null;
    }
  }
}
```

</details>

<details>
  <summary>82. Adding Styling to Form</summary>

App.css:

```css
.App {
  text-align: center;
}

body {
  margin: 0;
  padding: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.navbar {
  width: 100%;
  height: 80px;
  background-color: slateblue;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.navbar .links {
  text-align: center;
  margin-right: 50px;
}

.links a {
  color: white;
  text-decoration: none;
  border-bottom: 3px solid white;
  padding-bottom: 2px;
  margin: 10px;
}

.navbar .user {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 50px;
}

.user p {
  font-size: 15px;
  margin-right: 10px;
  color: white;
}

.user img {
  font-size: 15px;
  border-radius: 50%;
}

input,
textarea {
  font-family: "Nunito", sans-serif;
}

.create-post {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
}

form {
  margin-top: 50px;
  padding: 30px 20px;
  width: 320px;
  border-radius: 7px;
  background-color: white;
  backdrop-filter: blur(5px);
  background-color: rgba(43, 0, 255, 0.588);
  overflow: hidden;
}

input,
textarea {
  padding: 8px 10px;
  margin: 3px 8px 16px 8px;
  background-color: rgba(222, 239, 248, 0.877);
  border: 0px transparent;
  border-radius: 5px;
  color: rgb(97, 4, 184);
  font-size: 16px;
  z-index: 1;
}

.submitForm:hover {
  cursor: pointer;
}

.main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
```

</details>

<details>
  <summary>83. Rendering Contents in Home Page</summary>

main/Main.tsx:

```tsx
import { getDocs, collection } from "firebase/firestore";
import { useEffect, useState } from "react";
import { db } from "../../config/firebase";
import { Post } from "./Post";

export interface Posts {
  id: string;
  userId: string;
  title: string;
  username: string;
  description: string;
}

export const Main = () => {
  const [postsList, setPostsList] = useState<Posts[] | null>(null);
  const postsRef = collection(db, "posts");

  const getPosts = async () => {
    const data = await getDocs(postsRef);
    setPostsList(
      data.docs.map((doc) => ({ ...doc.data(), id: doc.id })) as Posts[]
    );
  };

  useEffect(() => {
    getPosts();
  }, []);

  return (
    <div>
      {postsList?.map((post) => (
        <Post post={post} key={post.id} />
      ))}
    </div>
  );
};
```

main/Post.tsx:

```tsx
import {
  addDoc,
  getDocs,
  collection,
  query,
  where,
  deleteDoc,
  doc,
} from "firebase/firestore";
import { useEffect, useState } from "react";
import { useAuthState } from "react-firebase-hooks/auth";
import { db, auth } from "../../config/firebase";
import { Posts as IPost } from "./Main";

interface Props {
  post: IPost;
}

interface Like {
  likeId: string;
  userId: string;
}

export const Post = (props: Props) => {
  const { post } = props;
  const [user] = useAuthState(auth);

  const [likes, setLikes] = useState<Like[] | null>(null);

  const likesRef = collection(db, "likes");

  const likesDoc = query(likesRef, where("postId", "==", post.id));

  const getLikes = async () => {
    const data = await getDocs(likesDoc);
    setLikes(
      data.docs.map((doc) => ({ userId: doc.data().userId, likeId: doc.id }))
    );
  };
  const addLike = async () => {
    try {
      const newDoc = await addDoc(likesRef, {
        userId: user?.uid,
        postId: post.id,
      });
      if (user) {
        setLikes((prev) =>
          prev
            ? [...prev, { userId: user.uid, likeId: newDoc.id }]
            : [{ userId: user.uid, likeId: newDoc.id }]
        );
      }
    } catch (err) {
      console.log(err);
    }
  };

  const removeLike = async () => {
    try {
      const likeToDeleteQuery = query(
        likesRef,
        where("postId", "==", post.id),
        where("userId", "==", user?.uid)
      );

      const likeToDeleteData = await getDocs(likeToDeleteQuery);
      const likeId = likeToDeleteData.docs[0].id;
      const likeToDelete = doc(db, "likes", likeId);
      await deleteDoc(likeToDelete);
      if (user) {
        setLikes(
          (prev) => prev && prev.filter((like) => like.likeId !== likeId)
        );
      }
    } catch (err) {
      console.log(err);
    }
  };

  const hasUserLiked = likes?.find((like) => like.userId === user?.uid);

  useEffect(() => {
    getLikes();
  }, []);

  return (
    <div>
      <div className="title">
        <h1> {post.title}</h1>
      </div>
      <div className="body">
        <p> {post.description} </p>
      </div>

      <div className="footer">
        <p> @{post.username} </p>
        <button onClick={hasUserLiked ? removeLike : addLike}>
          {hasUserLiked ? <>&#128078;</> : <>&#128077;</>}{" "}
        </button>
        {likes && <p> Likes: {likes?.length} </p>}
      </div>
    </div>
  );
};
```

Firebase Auth:

```bs
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow write, delete, update: if request.auth != null && request.auth.uid == request.resource.data.userId;
      allow read, delete: if request.auth != null;
    }
  }
}
```

</details>

<details>
  <summary>84. Deploy Firebase</summary>

```bs
Firebase -> Build -> Hosting -> Get Started
```

```bs
npm install -g firebase-tools
```

```bs
npm run build
```

Git:

```bs
#Just follow next steps in console terminal ;)
git init	#Initialize git in folder
git add .	#add all files of folder to be pushed
git commit -m "First commit"	#add first commit
git remote add origin remote_repository_URL #replace with your remote repo url
git remote -v	#verify that your remote repository url is properly found
git branch -M main  #change main branch name to main
git push --force origin main	#force pushing your project into github repo

//make sure you're on the local branch, then:
git pull origin YourRemoteBranch
//which is the same as:
git fetch origin YourRemoteBranch
git merge origin/YourRemoteBranch

git push origin --delete feature/login
git push origin --delete master

# Push newly created local branch to remote
git push --set-upstream origin <branch name>
git push --force origin main //force pushing to remote github repo
git push -u origin new_branch

github@branch/c/remote/push  (new-branch)
git clone https://github.com/learn-git-fast/git-branch-examples.git
cd git*
git checkout -b new-branch

github@branch/c/remote/push (new-branch)
git branch -a
touch devolution.jpg
git add .
git commit -m "Are we not gender neutral people? We are Devo?"
git push --set-upstream origin new-branch

git pull --rebase origin main
# Resolve merge conflicts if needed
git push origin main
```

```bs
firebase login
```

```bs
firebase init
```

```bs
firebase deploy
```

</details>
