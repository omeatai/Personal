## +LinkedIn - React Essential Training

## [COURSE](https://www.linkedin.com/learning/react-js-essential-training-14836121/building-modern-user-interfaces-with-react?resume=false)

<details>
<summary>1. Spin up React Dev Environment with React.new </summary>

# Spin up React Dev Environment with React.new

## Enter in browser

```x
react.new
```

### index.js

```js
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import App from "./App";

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(
  <StrictMode>
    <App />
  </StrictMode>
);

```

### App.js

```js
import "./styles.css";

export default function App() {
  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
    </div>
  );
}

```

### styles.css

```js
.App {
  font-family: sans-serif;
  text-align: center;
}
```

<img width="960" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/30e5b937-1ea4-4c35-b05d-699a75139d03">

# #End</details>
  
<details>
<summary>2. React Manually with CDN - Basic Setup </summary>

# React  Manually with CDN - Basic Setup

## Basic Setup

```js
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script
      src="https://unpkg.com/react@17/umd/react.development.js"
      crossorigin
    ></script>
    <script
      src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"
      crossorigin
    ></script>
    <title>React ⚛️</title>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/javascript">
      ReactDOM.render(
        React.createElement("h1", null, "Getting Started with React!"),
        document.getElementById("root")
      );
    </script>
  </body>
</html>

```

<img width="1411" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/a59e3cc3-e2c2-45f6-9a9f-dcd88c3adb44">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/559f23f1-bab7-42a3-8629-c5028cf8d58d)

## Setup using Variables

```js
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script
      src="https://unpkg.com/react@17/umd/react.development.js"
      crossorigin
    ></script>
    <script
      src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"
      crossorigin
    ></script>
    <title>React ⚛️</title>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/javascript">
      let heading = React.createElement(
        "h1",
        { style: { color: "blue" } },
        "Heyyyy Everyone!"
      );

      ReactDOM.render(heading, document.getElementById("root"));
    </script>
  </body>
</html>

```

<img width="1411" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/86971e4d-8420-4f7d-b8ce-a8148aeb6b2b">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/a149800a-f2c5-4df8-92d5-ab74becba43b)

## Setup with multiple elements

```js
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script
      src="https://unpkg.com/react@17/umd/react.development.js"
      crossorigin
    ></script>
    <script
      src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"
      crossorigin
    ></script>
    <title>React ⚛️</title>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/javascript">
      let heading = React.createElement(
        "ul",
        { style: { color: "blue", fontSize: "50px" } },
        React.createElement("li", null, "Monday😊"),
        React.createElement("li", null, "Tuesday🤓"),
        React.createElement("li", null, "Wednesday🤪")
      );

      ReactDOM.render(heading, document.getElementById("root"));
    </script>
  </body>
</html>

```

<img width="1411" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5799d71c-aff6-4389-91b6-82bea8f3c576">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d235efd4-8dd6-4f34-8c78-a068cbd3eba1)

# #End</details>
  
<details>
<summary>3. React Manually with CDN - JSX implementation using Babel </summary>

# React Manually with CDN - JSX implementation using Babel

```js
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script
      src="https://unpkg.com/react@17/umd/react.development.js"
      crossorigin
    ></script>
    <script
      src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"
      crossorigin
    ></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <title>React ⚛️</title>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/babel">
      let robot = "🤖";
      let cowboy = "🤠";
      let moon = "🌝";
      let name = "React";

      ReactDOM.render(
        <ul style={{ fontSize: "50px" }}>
          <li>Monday {robot}</li>
          <li>Tuesday {cowboy}</li>
          <li>Wednesday {moon}</li>
          <li>Name: {name.toUpperCase()}</li>
          <li>Name Length: {name.length}</li>
        </ul>,
        document.getElementById("root")
      );
    </script>
  </body>
</html>

```

<img width="1411" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/757b8961-8577-4ae8-a086-88e22388b4d8">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/5c9e26b3-39f3-4fce-92ad-6f00844d337d)

# #End</details>
  
<details>
<summary>4. React Manually with CDN - Using JSX Components </summary>

# React Manually with CDN - Using JSX Components

```js
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script
      src="https://unpkg.com/react@17/umd/react.development.js"
      crossorigin
    ></script>
    <script
      src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"
      crossorigin
    ></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <title>React ⚛️</title>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/babel">
      function Header() {
        return (
          <header>
            <h1>Eve's Kitchen</h1>
          </header>
        );
      }
      function Main() {
        return (
          <section>
            <p>We serve the most delicious food around</p>
          </section>
        );
      }
      function App() {
        return (
          <div>
            <Header />
            <Main />
          </div>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>
</html>

```

<img width="1411" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5262e05d-237c-48c2-b944-3ad2182141d9">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/fa23738a-862b-4fcf-8997-8e80a64579aa)

# #End</details>
  
<details>
<summary>5. React Manually with CDN - Adding JSX Props </summary>

# React Manually with CDN - Adding JSX Props

```js
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script
      src="https://unpkg.com/react@17/umd/react.development.js"
      crossorigin
    ></script>
    <script
      src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"
      crossorigin
    ></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <title>React ⚛️</title>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/babel">
      function Header(props) {
        return (
          <header>
            <h1>{props.name}'s Kitchen</h1>
          </header>
        );
      }
      function Main(props) {
        return (
          <section>
            <p>We serve the most {props.adjective} food around.</p>
          </section>
        );
      }

      function Footer(props) {
        return (
          <footer>
            <p>Copyright {props.year}</p>
          </footer>
        );
      }

      function App() {
        return (
          <div>
            <Header name="Cindy" />
            <Main adjective="amazing" />
            <Footer year={new Date().getFullYear()} />
          </div>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>
</html>

```

<img width="1411" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/95e5e987-b388-4346-88de-be34ced9f302">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/c97f4483-6c1d-40b8-9991-3469b8ea6e0d)

# #End</details>
  
<details>
<summary>6. React Manually with CDN - Workng with Arrays </summary>

# React Manually with CDN - Workng with Arrays

```js
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script
      src="https://unpkg.com/react@17/umd/react.development.js"
      crossorigin
    ></script>
    <script
      src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"
      crossorigin
    ></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <title>React ⚛️</title>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/babel">
      function Header(props) {
        return (
          <header>
            <h1>{props.name}'s Kitchen</h1>
          </header>
        );
      }
      function Main(props) {
        return (
          <section>
            <ul>
              {props.dishes.map((dish) => (
                <li key={dish.id}>{dish.title}</li>
              ))}
            </ul>
          </section>
        );
      }

      function Footer(props) {
        return (
          <footer>
            <p>Copyright {props.year}</p>
          </footer>
        );
      }

      const dishes = [
        "Black Bean Soup",
        "Macaroni and Cheese",
        "Salmon and Potatoes",
        "Pizza",
      ];
      const dishObjects = dishes.map((dish, i) => ({
        id: i,
        title: dish,
      }));

      function App() {
        return (
          <div>
            <Header name="Cindy" />
            <Main adjective="amazing" dishes={dishObjects} />
            <Footer year={new Date().getFullYear()} />
          </div>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>
</html>

```

<img width="1367" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/678f7797-f5df-4576-87f0-dc71008d51ee">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/bdd76dea-cd39-4b36-b8df-7d7b97999b72)

# #End</details>
  
<details>
<summary>7. React Manually with CDN - Displaying Images </summary>

# React Manually with CDN - Displaying Images

```js
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script
      src="https://unpkg.com/react@17/umd/react.development.js"
      crossorigin
    ></script>
    <script
      src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"
      crossorigin
    ></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <title>React ⚛️</title>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/babel">
      function Header(props) {
        return (
          <header>
            <h1>{props.name}'s Kitchen</h1>
          </header>
        );
      }
      function Main(props) {
        return (
          <section>
            <img
              height={200}
              src="https://images.pexels.com/photos/1058277/pexels-photo-1058277.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
              alt="A fancy restaurant"
            />
            <ul>
              {props.dishes.map((dish) => (
                <li key={dish.id}>{dish.title}</li>
              ))}
            </ul>
          </section>
        );
      }

      function Footer(props) {
        return (
          <footer>
            <p>Copyright {props.year}</p>
          </footer>
        );
      }

      const dishes = [
        "Black Bean Soup",
        "Macaroni and Cheese",
        "Salmon and Potatoes",
        "Pizza",
      ];
      const dishObjects = dishes.map((dish, i) => ({
        id: i,
        title: dish,
      }));

      function App() {
        return (
          <div>
            <Header name="Cindy" />
            <Main adjective="amazing" dishes={dishObjects} />
            <Footer year={new Date().getFullYear()} />
          </div>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>
</html>

```

<img width="1520" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/be9519b8-2fba-4802-8443-527a01696507">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9717eb3a-0298-4575-a677-a1e2161442ee)

### [https://www.pexels.com/](https://www.pexels.com/)

<img width="960" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/c88ac4ab-14f0-4fb4-8735-0b1b3909f59e">
<img width="960" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/765bf001-1988-45a4-be4b-8a5e9a16a5a0">

# #End</details>
  
<details>
<summary>8. React Manually with CDN - Using React Fragments </summary>

# React Manually with CDN - Using React Fragments

```js
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script
      src="https://unpkg.com/react@17/umd/react.development.js"
      crossorigin
    ></script>
    <script
      src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"
      crossorigin
    ></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <title>React ⚛️</title>
  </head>
  <body>
    <div id="root"></div>

    <script type="text/babel">
      function Header(props) {
        return (
          <header>
            <h1>{props.name}'s Kitchen</h1>
          </header>
        );
      }
      function Main(props) {
        return (
          <section>
            <img
              height={200}
              src="https://images.pexels.com/photos/1058277/pexels-photo-1058277.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
              alt="A fancy restaurant"
            />
            <ul>
              {props.dishes.map((dish) => (
                <li key={dish.id}>{dish.title}</li>
              ))}
            </ul>
          </section>
        );
      }

      function Footer(props) {
        return (
          <footer>
            <p>Copyright {props.year}</p>
          </footer>
        );
      }

      const dishes = [
        "Black Bean Soup",
        "Macaroni and Cheese",
        "Salmon and Potatoes",
        "Pizza",
      ];
      const dishObjects = dishes.map((dish, i) => ({
        id: i,
        title: dish,
      }));

      function App() {
        return (
          <React.Fragment>
            <Header name="Cindy" />
            <Main adjective="amazing" dishes={dishObjects} />
            <Footer year={new Date().getFullYear()} />
          </React.Fragment>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>
</html>

```

<img width="1520" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/14c33af8-4113-4c0c-aa5d-80ad5bc81da0">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b90a0046-76ad-4e15-ab5a-3f2d0f0050f5)

# #End</details>
  
<details>
<summary>9. Using Create React App </summary>

# Using Create React App

## Check Node and NPM versions

```x
node -v
npm -v
```

## Create React App

```x
npx create-react-app my-app
```

## Start React App

```x
cd my-app
npm start

#npm install
```

### src-AI-Software/my_projects/02_react_ess_proj/my-app/package.json:

```js
{
  "name": "my-app",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
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
  }
}
```

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

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

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

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

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.css:

```js
.App {
  text-align: center;
}

.App-logo {
  height: 40vmin;
  pointer-events: none;
}

@media (prefers-reduced-motion: no-preference) {
  .App-logo {
    animation: App-logo-spin infinite 20s linear;
  }
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
}

@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

```

<img width="1497" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/656df0a5-1704-4ee4-bfa9-0bc144b9fbf8">
<img width="960" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/1657d3bc-2df2-4ffb-8416-7811221a155a">

# #End</details>
  
<details>
<summary>10. Destructing Arrays and Objects </summary>

# Destructing Arrays and Objects

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
const cities = ["Tokyo", "New York", "London", "Paris"];

root.render(
  <React.StrictMode>
    <App library="React" cities={cities} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

```

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import "./App.css";

function App(props) {
  const [firstCity, secondCity] = props.cities;

  return (
    <div className="App">
      <h1>Hello from {props.library}</h1>
      <h2>First City: {firstCity}</h2>
      <h2>Second City: {secondCity}</h2>
    </div>
  );
}

export default App;

```

<img width="1497" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/6c93a2c7-c277-4a6d-b801-88e0afa8197e">

<img width="960" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/c7cb3667-73c2-4d4e-a83b-8841711585ed">

# #End</details>
  
<details>
<summary>11. Using UseState Hook </summary>

# Using UseState Hook

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

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

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import React, { useState } from "react";
import "./App.css";

function App() {
  const [emotion, setEmotion] = useState("happy😁");
  return (
    <div className="App">
      <h1>Current Emotion is {emotion}</h1>
      <button
        onClick={() =>
          setEmotion((prev) => (prev === "happy😁" ? "sad😢" : "happy😁"))
        }
      >
        Change Emotion
      </button>
      <button onClick={() => setEmotion("proud🤩")}>Proud</button>
      <button onClick={() => setEmotion("angry😡")}>Angry</button>
    </div>
  );
}

export default App;

```

<img width="1497" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/aae092b3-723b-4d89-8ce8-380006151f8b">
<img width="960" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/a57d3da5-ff19-489f-9e4f-bd22197e0be9">
<img width="960" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/4d06293f-8303-4119-91d3-b919ba18b757">

# #End</details>
  
<details>
<summary>12. Using UseEffect Hook </summary>

# Using UseEffect Hook

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

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

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [emotion, setEmotion] = useState("happy😁");
  const [secondary, setSecondary] = useState("tired🥱");

  useEffect(() => {
    console.log(`It's ${emotion} around here!`);
  }, [emotion]);

  useEffect(() => {
    console.log(`It's ${secondary} around here!`);
  }, [secondary]);

  return (
    <div className="App">
      <h1>Current Emotion is {emotion}</h1>
      <h2>Current Secondary Emotion is {secondary}.</h2>
      <button
        onClick={() =>
          setEmotion((prev) => (prev === "happy😁" ? "sad😢" : "happy😁"))
        }
      >
        Change Emotion
      </button>
      <button onClick={() => setEmotion("proud🤩")}>Proud</button>
      <button onClick={() => setEmotion("angry😡")}>Angry</button>
      <button onClick={() => setSecondary("grateful🥹")}>Grateful</button>
    </div>
  );
}

export default App;

```

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/e1d113bd-b11f-4f41-bb29-a8c59f04badd">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9ba3b516-262f-43ae-98e9-af24604975f8)

# #End</details>
  
<details>
<summary>13. Using UseReducer Hook </summary>

# Using UseReducer Hook

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

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

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import React, { useState } from "react";
import "./App.css";

function App() {
  const [checked, setChecked] = useState(false);
  // const [checked, setChecked] = useReducer((checked) => !checked, false);

  return (
    <div className="App">
      <input
        type="checkbox"
        value={checked}
        onChange={() => setChecked((prev) => !prev)}
      />
      <label>{checked ? "checked" : "not checked"}</label>
    </div>
  );
}

export default App;

```

```js
import React, { useReducer } from "react";
import "./App.css";

function App() {
  // const [checked, setChecked] = useState(false);
  const [checked, setChecked] = useReducer((checked) => !checked, false);

  return (
    <div className="App">
      <input type="checkbox" value={checked} onChange={setChecked} />
      <label>{checked ? "checked" : "not checked"}</label>
    </div>
  );
}

export default App;

```

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/bb2295f4-eb4c-4b95-b0a2-3b08a7801e26">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/0cb7369f-fdf7-483e-a48e-79fbe05015e5)


# #End</details>
  
<details>
<summary>14. Using Uncontrolled Components with UseRef </summary>

# Using Uncontrolled Components with UseRef

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

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

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import { useRef } from "react";
import "./App.css";

function App() {
  const txtTitle = useRef();
  const hexColor = useRef();

  const submit = (e) => {
    e.preventDefault();
    const title = txtTitle.current.value;
    const color = hexColor.current.value;
    alert(`${title}, ${color}`);
    txtTitle.current.value = "";
    hexColor.current.value = "";
  };

  return (
    <form onSubmit={submit}>
      <input ref={txtTitle} type="text" placeholder="color title..." />
      <input ref={hexColor} type="color" />
      <button>ADD</button>
    </form>
  );
}

export default App;

```

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/8bb23453-407e-4279-8ec4-013cedddb820">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/a091b3cf-daa1-4ea0-b421-b14c02c6ed02)


# #End</details>
  
<details>
<summary>15. Using Controlled Form Elements with UseState </summary>

# Using Controlled Form Elements with UseState

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

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

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import { useState } from "react";
import "./App.css";

function App() {
  const [title, setTitle] = useState("");
  const [color, setColor] = useState("#000000");

  const submit = (e) => {
    e.preventDefault();
    alert(`${title}, ${color}`);
    setTitle("");
    setColor("#000000");
  };

  return (
    <form onSubmit={submit}>
      <input
        type="text"
        placeholder="color title..."
        onChange={(e) => setTitle(e.target.value)}
        value={title}
      />
      <input
        type="color"
        value={color}
        onChange={(e) => setColor(e.target.value)}
      />
      <button>ADD</button>
    </form>
  );
}

export default App;

```

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d9909665-945f-4959-84b7-ff66a3738e46">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9c9b2487-1bbf-4a81-b775-8eebf46c0315)

# #End</details>
  
<details>
<summary>16. Building a Custom Hook </summary>

# Building a Custom Hook

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

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

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import "./App.css";
import { useState } from "react";

function useInput(initialValue) {
  const [value, setValue] = useState(initialValue);

  return [
    {
      value,
      onChange: (e) => setValue(e.target.value),
    },
    () => setValue(initialValue),
  ];
}

function App() {
  const [titleProps, resetTitle] = useInput("");
  const [colorProps, resetColor] = useInput("#000000");

  const submit = (e) => {
    e.preventDefault();
    alert(`${titleProps.value}, ${colorProps.value}`);
    resetTitle();
    resetColor();
  };
  return (
    <form onSubmit={submit}>
      <input {...titleProps} type="text" placeholder="color title..." />
      <input {...colorProps} type="color" />
      <button>ADD</button>
    </form>
  );
}

export default App;

```

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/18514b81-663b-4b6f-8515-b37e9842f6ca">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/2cb82151-9c52-4c89-8dac-b875ae7a2369)

# #End</details>
  
<details>
<summary>17. Async React - Fetching Data with Hooks </summary>

# Async React - Fetching Data with Hooks

GITHUB API: [https://api.github.com/users/omeatai](https://api.github.com/users/omeatai)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/fec0b0ca-1a64-42d1-a0e6-806911cf6f1a)

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

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

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import "./App.css";
import { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(`https://api.github.com/users/omeatai`)
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  if (data) return <pre>{JSON.stringify(data, null, 2)}</pre>;

  return <h1>Data</h1>;
}

export default App;

```

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/52576a7e-d59e-4215-8e8d-37aaf5738f4a">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/cf6ab97b-8afb-4e02-a446-0f5cf10fd990)

# #End</details>
  
<details>
<summary>18. Async React - Display Fetched Data in Component </summary>

# Async React - Display Fetched Data in Component

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import "./App.css";
import { useState, useEffect } from "react";

function GithubUser({ name, location, avatar }) {
  return (
    <div style={{ textAlign: "center" }}>
      <h1>{name}</h1>
      <p>{location}</p>
      <img src={avatar} height={100} alt={name} />
    </div>
  );
}

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(`https://api.github.com/users/omeatai`)
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  if (data)
    return (
      <GithubUser
        name={data.name}
        location={data.location}
        avatar={data.avatar_url}
      />
    );

  return <h1>Data</h1>;
}

export default App;
```

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/38f0dc14-f1ff-4d65-a160-c4cff8782c3e">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/c34dd6a4-72b3-480f-8794-4589437c2cea)

# #End</details>
  
<details>
<summary>19. Async React - Handling Loading of states </summary>

# Async React - Handling Loading of states

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import "./App.css";
import { useState, useEffect } from "react";

function GithubUser({ name, location, avatar }) {
  return (
    <div style={{ textAlign: "center" }}>
      <h1>{name}</h1>
      <p>{location}</p>
      <img src={avatar} height={100} alt={name} />
    </div>
  );
}

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    fetch(`https://api.github.com/users/omeatai`)
      .then((response) => response.json())
      .then(setData)
      .then(() => setLoading(false))
      .catch((error) => setError(error));
  }, []);

  if (loading) return <h1>Loading...</h1>;
  if (error) return <pre>{JSON.stringify(error)}</pre>;
  if (!data) return null;
  return (
    <GithubUser
      name={data.name}
      location={data.location}
      avatar={data.avatar_url}
    />
  );
}

export default App;

```

<img width="1535" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/c5cd74d6-82d5-4039-a76a-605071551c57">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/f048be5f-afdd-4d91-aa3b-dd64992334ee)

# #End</details>
  
<details>
<summary>20. Async React - Fetching Data with GraphQL </summary>

# Async React - Fetching Data with GraphQL

GRAPHQL API: [https://snowtooth.moonhighway.com/](https://snowtooth.moonhighway.com/)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/3a82fb27-4340-46be-8d27-4f2fbd5106c4)

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import "./App.css";
import { useState, useEffect } from "react";

const query = `
query {
  allLifts {
    name
    elevationGain
    status
  }
}
`;

const opts = {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ query }),
};

function Lift({ name, elevationGain, status }) {
  return (
    <div>
      <h1>{name}</h1>
      <p>
        {elevationGain} {status}
      </p>
    </div>
  );
}

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    fetch(`https://snowtooth.moonhighway.com/`, opts)
      .then((response) => response.json())
      .then(setData)
      .then(() => setLoading(false))
      .catch(setError);
  }, []);

  if (loading) return <h1>Loading...</h1>;
  if (error) return <pre>{JSON.stringify(error)}</pre>;
  if (!data) return null;
  return (
    <div>
      {data.data.allLifts.map((lift) => (
        <Lift
          key={lift.name}
          name={lift.name}
          elevationGain={lift.elevationGain}
          status={lift.status}
        />
      ))}
    </div>
  );
}

export default App;

```

<img width="1535" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/2cdffe83-6c99-486d-8a30-a95470104417">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/5ffd1178-72a7-4488-9336-f968d60f0baf)

# #End</details>
  
<details>
<summary>21. Async React - Working with Render Props </summary>

# Async React - Working with Render Props

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

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

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import "./App.css";

const tahoe_peaks = [
  { name: "Freel", elevation: 10891 },
  { name: "Monument", elevation: 10067 },
  { name: "Pyramid", elevation: 9983 },
  { name: "Tallac", elevation: 9735 },
];

function List({ data, renderItem, renderEmpty }) {
  return !data.length ? (
    renderEmpty
  ) : (
    <ul>
      {data.map((item) => (
        <li key={item.name}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}

function App() {
  return (
    <List
      data={tahoe_peaks}
      renderEmpty={<p>This list is empty</p>}
      renderItem={(item) => (
        <>
          {item.name} - {item.elevation} ft.
        </>
      )}
    />
  );
}

export default App;

```

<img width="1535" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/8aa30e22-109b-4367-9427-9b9749da7c82">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/393171a1-e8c2-4a34-aefe-e4d4cff5975d)

# #End</details>
  
<details>
<summary>22. React Router - Configuring React Router v6 </summary>

# React Router - Configuring React Router v6

## Install React Router DOM

```js
npm install react-router-dom@6
```

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { App, About, Contact } from "./App";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

```

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import "./App.css";

function Home() {
  return (
    <div>
      <h1>My Website</h1>
    </div>
  );
}

export function About() {
  return (
    <div>
      <h1>About Us</h1>
    </div>
  );
}

export function Contact() {
  return (
    <div>
      <h1>Contact Us</h1>
    </div>
  );
}

export function App() {
  return <Home />;
}

```

<img width="1493" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/de99cf93-3aa5-4f46-a79b-a3a27c074e8e">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/01f7da17-1f30-45a2-a845-e15b650398a0)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b4ce122d-e90d-4c42-a812-2c4c13a5fac9)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b0043e45-5734-46db-a774-a80b6982abd7)

# #End</details>
  
<details>
<summary>23. React Router - Using the Link Component </summary>

# React Router - Using the Link Component

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { App, About, Contact } from "./App";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

```

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import "./App.css";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <nav>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <h1>My Website</h1>
    </div>
  );
}

export function About() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <h1>About Us</h1>
    </div>
  );
}

export function Contact() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <h1>Contact Us</h1>
    </div>
  );
}

export function App() {
  return <Home />;
}

```

<img width="1493" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/a027738c-32bf-4873-ba9d-509d03076853">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/046f2ee2-2a76-4894-ac18-9d702531de42)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/5abe2e65-9afd-422d-b54f-ef684a0d1b67)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/7df8032b-470b-44c9-a7a2-bb950f5ebb30)

# #End</details>
  
<details>
<summary>24. React Router - Nesting Links with React Router v6 and Outlet </summary>

# React Router - Nesting Links with React Router v6 and Outlet

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { App, About, Contact, History } from "./App";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/about" element={<About />}>
          <Route path="history" element={<History />} />
        </Route>
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

```

### src-AI-Software/my_projects/02_react_ess_proj/my-app/src/App.js:

```js
import "./App.css";
import { Link, Outlet } from "react-router-dom";

function Home() {
  return (
    <div>
      <nav>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <h1>My Website</h1>
    </div>
  );
}

export function About() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <h1>About Us</h1>
      <Outlet />
    </div>
  );
}

export function History() {
  return (
    <div>
      <h1>Our History</h1>
    </div>
  );
}

export function Contact() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <h1>Contact Us</h1>
    </div>
  );
}

export function App() {
  return <Home />;
}

```

<img width="1493" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d49b90cf-30fa-4586-bf1e-add124fa2367">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b0d242df-6bae-469e-934a-ffcaa110c8fb)

# #End</details>
  
<details>
<summary>25. React Router - Testing small functions with jest </summary>

# React Router - Testing small functions with jest

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
