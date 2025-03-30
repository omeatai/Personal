# REACT-NODE-EXPRESS-TUTORIAL - DAVE GRAY

## [COURSE](https://www.youtube.com/playlist?list=PL0Zuz27SZ-6PrE9srvEn8nbhOOyxnWXfp)

# REACT

+REACT INTRODUCTION

<details>
  <summary>1. Create React App</summary>

# Create React App

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/72c7bd60-0dec-408f-aa2b-cb68733d52e9">
<img width="1159" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/733b183d-9c73-450c-b930-befb787dd6e4">

# Check node version

```bs
node -v


# Create App myapp

```bs
npx create-react-app .
npx create-react-app myapp
```

# Start App:

```bs
cd myapp
npm start
```

# Stop App:

```bs
ctrl + c
```

### x-dave-gray/myapp/src/index.js:

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

### x-dave-gray/myapp/src/App.js:

```js
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to see changes.
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

# #End  </details>

<details>
  <summary>2. HandleNameChange Function</summary>

# HandleNameChange Function

<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0a7de29b-3ae6-45fb-82bb-d64439e6727e">
<img width="1158" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/167cea6a-feab-42d9-8515-2d12b419a4df">

### x-dave-gray/myapp/src/App.js:

```js
import logo from "./logo.svg";
import "./App.css";

function App() {
  const handleNameChange = () => {
    const names = ["Dave", "Sally", "Ben", "Andrew"];
    const int = Math.floor(Math.random() * names.length);
    return names[int];
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Hello {handleNameChange()}!</p>
      </header>
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>3. Using React Functional Components</summary>

# Using React Functional Components

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4f7308fd-a44f-40b8-bd92-fb6bff029db5">
<img width="1158" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4b461b3b-04ec-4154-8861-8f07e2b82756">

### x-dave-gray/myapp/src/App.js:

```js
import "./App.css";
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  return (
    <div className="App">
      <Header />
      <Content />
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/myapp/src/Header.js:

```js
import React from "react";

const Header = () => {
  return (
    <header>
      <h1>Groceries List</h1>
    </header>
  );
};

export default Header;

```

### x-dave-gray/myapp/src/Content.js:

```js
import React from "react";

const Content = () => {
  const handleChange = () => {
    const names = ["Dave", "Sally", "Ben", "Andrew"];
    const indexPos = Math.floor(Math.random() * names.length);
    return names[indexPos];
  };

  return (
    <main>
      <p>Hello, {handleChange()}!</p>
    </main>
  );
};

export default Content;

```

### x-dave-gray/myapp/src/Footer.js:

```js
import React from "react";

const Footer = () => {
  const today = new Date();

  return (
    <footer>
      <p>Copyright &copy; {today.getFullYear()}</p>
    </footer>
  );
};

export default Footer;

```

# #End  </details>

<details>
  <summary>4. Styling Components</summary>

# Styling Components

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e1b5995b-e3e3-40f7-bf81-54c2f026f81a">
<img width="1157" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4d1abe89-e81f-4270-9aac-fe0f619e3719">

### x-dave-gray/myapp/src/index.js:

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

### x-dave-gray/myapp/src/App.js:

```js
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  return (
    <div className="App">
      <Header />
      <Content />
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/myapp/src/Header.js:

```js
import React from "react";

const Header = () => {
  const headerStyle = {
    backgroundColor: "royalblue",
    color: "#fff",
  };

  return (
    <header style={headerStyle}>
      <h1>Groceries List</h1>
    </header>
  );
};

export default Header;
```

### x-dave-gray/myapp/src/index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 22px;
}

body {
  min-height: 100vh;
  font-family: "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans",
    "Droid Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  max-width: 500px;
  border: 1px solid mediumblue;
  margin: auto;
}

header {
  width: 100%;
  padding: 0 0.25em;
  background-color: mediumblue;
  color: aliceblue;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

main {
  width: 100%;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  justify-content: flex-start;
  align-items: space-around;
  overflow-y: auto;
}

footer {
  width: 100%;
  padding: 0.25em;
  background-color: mediumblue;
  color: aliceblue;
  display: grid;
  place-content: center;
}

```

# #End  </details>

<details>
  <summary>5. React onClick Events</summary>

# React onClick Events

<img width="978" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/899644b5-a98c-4d77-ad8f-beb82c98307e">
<img width="1157" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c57decdf-91d2-4ef2-bfd8-7c6557e8b01f">

### x-dave-gray/myapp/src/App.js:

```js
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  return (
    <div className="App">
      <Header />
      <Content />
      <Footer />
    </div>
  );
}

export default App;

```

### x-dave-gray/myapp/src/Content.js:

```js
import React from "react";

const Content = () => {
  const handleChange = () => {
    const names = ["Dave", "Sally", "Ben", "Andrew"];
    const int = Math.floor(Math.random() * names.length);
    return names[int];
  };

  const handleClick = () => {
    console.log("Click 1 button was clicked.");
  };

  const handleClick2 = (name) => {
    console.log(`Click 2 button with name "${name}" was clicked.`);
  };

  const handleClick3 = (e) => {
    console.log(e.target.innerText);
  };

  const handleDoubleClick = () => {
    console.log("The Item was clicked twice!");
  };

  return (
    <main>
      <p onDoubleClick={handleDoubleClick}>Hello, {handleChange()}!</p>
      <button onClick={handleClick}>Click 1</button>
      <button onClick={() => handleClick2("David")}>Click 2</button>
      <button onClick={(e) => handleClick3(e)}>Click 3</button>
    </main>
  );
};

export default Content;
```

# Other applications of Single And DoubleClick function

```js
import { useState, useEffect } from "react";

function useSingleAndDoubleClick(
  actionSimpleClick,
  actionDoubleClick,
  delay = 250
) {
  const [click, setClick] = useState(0);

  useEffect(() => {
    const timer = setTimeout(() => {
      // simple click
      if (click === 1) actionSimpleClick();
      setClick(0);
    }, delay);

    // the duration between this click and the previous one
    // is less than the value of delay = double-click
    if (click === 2) actionDoubleClick();

    return () => clearTimeout(timer);
  }, [click]);

  return () => setClick((prev) => prev + 1);
}

const click = useSingleAndDoubleClick(callbackClick, callbackDoubleClick);

<button onClick={click}>click</button>;

```

```js
const handleClick = (e) => {
  switch (e.detail) {
    case 1:
      console.log("click");
      break;
    case 2:
      console.log("double click");
      break;
    case 3:
      console.log("triple click");
      break;
  }
};

return <button onClick={handleClick}>Click me</button>;
```

# #End  </details>

<details>
  <summary>6. Using React useState Hooks</summary>

# Using React useState Hooks

<img width="978" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ffd66132-3a7f-4186-a704-218f34e4d3b5">
<img width="1158" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/85aa594a-6c2a-4393-b031-c89b58108218">

### x-dave-gray/myapp/src/App.js:

```js
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  return (
    <div className="App">
      <Header />
      <Content />
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/myapp/src/Content.js:

```js
import React, { useState } from "react";

const Content = () => {
  const [name, setName] = useState("Dave");
  const [count, setCount] = useState(0);

  const handleNameChange = () => {
    const names = ["Dave", "Sally", "Ben", "Andrew"];
    const int = Math.floor(Math.random() * names.length);
    setName(names[int]);
  };

  const handleCount = () => {
    setCount((count) => count + 1);
  };

  const handleReset = () => {
    setCount(0);
  };

  return (
    <main>
      <h1>Hello, {name}!</h1>
      <h2>Count: {count}</h2>
      <button onClick={handleNameChange}>Change Name</button>
      <button onClick={handleCount}>Count</button>
      <button onClick={handleReset}>Reset</button>
    </main>
  );
};

export default Content;
```

# #End  </details>

<details>
  <summary>7. Rendering Lists + adding Items to LocalStorage</summary>

# Rendering Lists + adding Items to LocalStorage

<img width="976" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c9fb229d-23d4-41f3-951f-b6d22950050c">
<img width="1158" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/87a3d8d1-4575-4b76-b031-e8c853787111">

# Install React-Icons

```bs
npm i react-icons -D
npm install react-icons --save
```

### x-dave-gray/myapp/src/App.js:

```js
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  return (
    <div className="App">
      <Header />
      <Content />
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/myapp/src/Content.js:

```js
import React, { useState } from "react";
import { FaTrashAlt } from "react-icons/fa";

const Content = () => {
  const [items, setItems] = useState([
    {
      id: 1,
      checked: false,
      item: "Item 1",
    },
    {
      id: 2,
      checked: false,
      item: "Item 2",
    },
    {
      id: 3,
      checked: false,
      item: "Item 3",
    },
  ]);

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);
    localStorage.setItem("shoppinglist", JSON.stringify(listItems));
  };

  return (
    <main>
      {items.map((item) => (
        <li className="item" key={item.id}>
          <input
            onChange={() => handleCheck(item.id)}
            type="checkbox"
            checked={item.checked}
          />
          <label
            style={
              item.checked
                ? { textDecoration: "line-through" }
                : { textDecoration: "none" }
            }
            onDoubleClick={() => handleCheck(item.id)}
          >
            {item.item}
          </label>
          <FaTrashAlt role="button" tabIndex="0" />
        </li>
      ))}
    </main>
  );
};

export default Content;
```

### x-dave-gray/myapp/src/index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 22px;
}

body {
  min-height: 100vh;
  font-family: "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans",
    "Droid Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  max-width: 500px;
  border: 1px solid mediumblue;
  margin: auto;
}

header {
  width: 100%;
  padding: 0 0.25em;
  background-color: mediumblue;
  color: aliceblue;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

main {
  width: 100%;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  justify-content: flex-start;
  align-items: space-around;
  overflow-y: auto;
}

footer {
  width: 100%;
  padding: 0.25em;
  background-color: mediumblue;
  color: aliceblue;
  display: grid;
  place-content: center;
}

ul {
  width: 100%;
  list-style: none;
  padding: 0 0.25rem 0.25rem;
}

ul li::before {
  content: "\200B";
}

.item {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 0.5rem 0 0.5rem 0.5rem;
  margin: 0.25rem 0;
  background-color: #eee;
}

.item:first-child {
  margin: 0;
}

.item input[type="checkbox"] {
  text-align: center;
  width: 2.5rem;
  width: 48px;
  min-width: 48px;
  height: 2.5rem;
  height: 48px;
  min-height: 48px;
  cursor: pointer;
  margin-right: 0.5rem;
}

.item input[type="checkbox"]:focus + label {
  text-decoration: underline;
}

.item > label {
  font-size: 0.75rem;
  flex-grow: 1;
}

.item svg {
  width: 48px;
  min-width: 48px;
  height: 36px;
  font-size: 1rem;
  color: steelblue;
  cursor: pointer;
}

.item svg:focus,
.item svg:hover {
  color: red;
  outline: none;
}

```

# #End  </details>

<details>
  <summary>8. Deleting Items + Removing Items from LocalStorage </summary>

# Deleting Items + Removing Items from LocalStorage

<img width="976" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ab504664-b70b-4ab1-a351-cf59aa4260a8">
<img width="1161" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e087edfc-dd7c-4e10-ac79-48ae3cc5655b">
<img width="1161" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7c26bf09-bb4a-44e9-9fc3-700077ee39e7">

### x-dave-gray/myapp/src/App.js:

```js
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  return (
    <div className="App">
      <Header />
      <Content />
      <Footer />
    </div>
  );
}

export default App;

```

### x-dave-gray/myapp/src/Content.js:

```js
import React, { useState } from "react";
import { FaTrashAlt } from "react-icons/fa";

const Content = () => {
  const [items, setItems] = useState([
    {
      id: 1,
      checked: false,
      item: "Item 1",
    },
    {
      id: 2,
      checked: false,
      item: "Item 2",
    },
    {
      id: 3,
      checked: false,
      item: "Item 3",
    },
  ]);

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);
    localStorage.setItem("shoppinglist", JSON.stringify(listItems));
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);
    localStorage.setItem("shoppinglist", JSON.stringify(listItems));
  };

  return (
    <main>
      {items.length ? (
        <ul>
          {items.map((item) => (
            <li className="item" key={item.id}>
              <input
                onChange={() => handleCheck(item.id)}
                type="checkbox"
                checked={item.checked}
              />
              <label
                style={
                  item.checked
                    ? { textDecoration: "line-through" }
                    : { textDecoration: "none" }
                }
                onDoubleClick={() => handleCheck(item.id)}
              >
                {item.item}
              </label>
              <FaTrashAlt
                onClick={() => handleDelete(item.id)}
                role="button"
                tabIndex="0"
              />
            </li>
          ))}
        </ul>
      ) : (
        <p style={{ textAlign: "center" }}>No Items to display!</p>
      )}
    </main>
  );
};

export default Content;
```

# #End  </details>

<details>
  <summary>9. Passing Props to Components</summary>

# Passing Props to Components

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/faa23f27-fc82-4f83-9e90-8540ae36743b">
<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ab42f489-6408-49f9-a440-516c020603ad">
<img width="1161" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/df5fe0a7-da44-4a9d-a3d6-dc2e5bd68b73">

### x-dave-gray/myapp/src/App.js:

```js
import React, { useState } from "react";

import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  const [items, setItems] = useState([
    {
      id: 1,
      checked: false,
      item: "Item 1",
    },
    {
      id: 2,
      checked: false,
      item: "Item 2",
    },
    {
      id: 3,
      checked: false,
      item: "Item 3",
    },
  ]);

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);
    localStorage.setItem("shoppinglist", JSON.stringify(listItems));
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);
    localStorage.setItem("shoppinglist", JSON.stringify(listItems));
  };

  return (
    <div className="App">
      <Header title="My Grocery List" />
      <Content
        items={items}
        handleCheck={handleCheck}
        handleDelete={handleDelete}
      />
      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;
```

### x-dave-gray/myapp/src/Header.js:

```js
import React from "react";

const Header = ({ title }) => {
  return (
    <header>
      <h1>{title}</h1>
    </header>
  );
};

Header.defaultProps = {
  title: "Default Title",
};

export default Header;
```

### x-dave-gray/myapp/src/Content.js:

```js
import React from "react";
import { FaTrashAlt } from "react-icons/fa";

const Content = ({ items, handleCheck, handleDelete }) => {
  return (
    <main>
      {items.length ? (
        <ul>
          {items.map((item) => (
            <li className="item" key={item.id}>
              <input
                onChange={() => handleCheck(item.id)}
                type="checkbox"
                checked={item.checked}
              />
              <label
                style={
                  item.checked
                    ? { textDecoration: "line-through" }
                    : { textDecoration: "none" }
                }
                onDoubleClick={() => handleCheck(item.id)}
              >
                {item.item}
              </label>
              <FaTrashAlt
                onClick={() => handleDelete(item.id)}
                role="button"
                tabIndex="0"
              />
            </li>
          ))}
        </ul>
      ) : (
        <p style={{ textAlign: "center" }}>No Items to display!</p>
      )}
    </main>
  );
};

export default Content;
```

### x-dave-gray/myapp/src/Footer.js:

```js
import React from "react";

const Footer = ({ itemLength }) => {
  const today = new Date();

  const centerText = {
    textAlign: "center",
  };

  return (
    <footer>
      <p style={centerText}>
        {itemLength} List {itemLength === 1 ? "item" : "items"}
      </p>
      <p style={centerText}>Copyright &copy; {today.getFullYear()}</p>
    </footer>
  );
};

export default Footer;
```

# #End  </details>

<details>
  <summary>10. Create ItemList and LineItem Components </summary>

# Create ItemList and LineItem Components

App.js -> Content.js -> ItemList.js -> LineItem.js

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7c640ba2-1c7f-42a1-bfc7-4a2ca2861371">
<img width="1162" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5d19c5b0-5df0-44a7-8a69-d5a89aa285a6">

### x-dave-gray/myapp/src/App.js:

```js
import React, { useState } from "react";

import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  const [items, setItems] = useState([
    {
      id: 1,
      checked: false,
      item: "Item 1",
    },
    {
      id: 2,
      checked: false,
      item: "Item 2",
    },
    {
      id: 3,
      checked: false,
      item: "Item 3",
    },
  ]);

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);
    localStorage.setItem("shoppinglist", JSON.stringify(listItems));
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);
    localStorage.setItem("shoppinglist", JSON.stringify(listItems));
  };

  return (
    <div className="App">
      <Header title="My Grocery List" />
      <Content
        items={items}
        handleCheck={handleCheck}
        handleDelete={handleDelete}
      />
      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;
```

### x-dave-gray/myapp/src/Content.js:

```js
import React from "react";
import ItemList from "./ItemList";

const Content = ({ items, handleCheck, handleDelete }) => {
  return (
    <main>
      {items.length ? (
        <ItemList
          items={items}
          handleCheck={handleCheck}
          handleDelete={handleDelete}
        />
      ) : (
        <p style={{ textAlign: "center" }}>No Items to display!</p>
      )}
    </main>
  );
};

export default Content;
```

### x-dave-gray/myapp/src/ItemList.js:

```js
import React from "react";
import LineItem from "./LineItem";

const ItemList = ({ items, handleCheck, handleDelete }) => {
  return (
    <ul>
      {items.map((item) => (
        <LineItem
          key={item.id}
          item={item}
          handleCheck={handleCheck}
          handleDelete={handleDelete}
        />
      ))}
    </ul>
  );
};

export default ItemList;
```

### x-dave-gray/myapp/src/LineItem.js:

```js
import React from "react";
import { FaTrashAlt } from "react-icons/fa";

const LineItem = ({ item, handleCheck, handleDelete }) => {
  return (
    <li className="item">
      <input
        onChange={() => handleCheck(item.id)}
        type="checkbox"
        checked={item.checked}
      />
      <label
        style={
          item.checked
            ? { textDecoration: "line-through" }
            : { textDecoration: "none" }
        }
        onDoubleClick={() => handleCheck(item.id)}
      >
        {item.item}
      </label>
      <FaTrashAlt
        onClick={() => handleDelete(item.id)}
        role="button"
        tabIndex="0"
        aria-label={`Delete ${item.id}`}
      />
    </li>
  );
};

export default LineItem;
```

# #End  </details>

<details>
  <summary>11. Controlled Input - Add Items with React Auths </summary>

# Add Items with React Auths

<img width="978" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/082a9e01-2931-4329-8dcc-9800fe8dcfb1">
<img width="978" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/cb3acfad-a2f2-4032-bdc6-b73e005fc8a9">
<img width="1100" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a859efee-774f-4ba9-bdd0-c633aff33d5d">

# Move React icons to Production Dependency:

```bs
npm i react-icons --save-prod
```

### x-dave-gray/myapp/src/App.js:

```js
import React, { useState } from "react";
import AddItem from "./AddItem";
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  const [items, setItems] = useState([
    {
      id: 1,
      checked: false,
      item: "Item 1",
    },
    {
      id: 2,
      checked: false,
      item: "Item 2",
    },
    {
      id: 3,
      checked: false,
      item: "Item 3",
    },
  ]);

  const [newItem, setNewItem] = useState("");

  const setAndSaveItems = (newItems) => {
    setItems(newItems);
    localStorage.setItem("shoppinglist", JSON.stringify(newItems));
  };

  const addItem = (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setAndSaveItems(listItems);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItem) return;
    addItem(newItem);
    setNewItem("");
  };

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setAndSaveItems(listItems);
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setAndSaveItems(listItems);
  };

  return (
    <div className="App">
      <Header title="My Grocery List" />
      <AddItem
        newItem={newItem}
        setNewItem={setNewItem}
        handleSubmit={handleSubmit}
      />
      <Content
        items={items}
        handleCheck={handleCheck}
        handleDelete={handleDelete}
      />
      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;

```

### x-dave-gray/myapp/src/AddItem.js:

```js
import React from "react";
import { FaPlus } from "react-icons/fa";

const AddItem = ({ newItem, setNewItem, handleSubmit }) => {
  return (
    <form onSubmit={handleSubmit} className="addForm">
      <label htmlFor="addItem">Add Item</label>
      <input
        type="text"
        id="addItem"
        placeholder="Add Item"
        autoFocus
        required
        value={newItem}
        onChange={(e) => setNewItem(e.target.value)}
      />
      <button type="submit" arai-label="Add Item">
        <FaPlus />
      </button>
    </form>
  );
};

export default AddItem;

```

### x-dave-gray/myapp/src/index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 22px;
}

body {
  min-height: 100vh;
  font-family: "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans",
    "Droid Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  max-width: 500px;
  border: 1px solid mediumblue;
  margin: auto;
}

header {
  width: 100%;
  padding: 0 0.25em;
  background-color: mediumblue;
  color: aliceblue;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

main {
  width: 100%;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  justify-content: flex-start;
  align-items: space-around;
  overflow-y: auto;
}

footer {
  width: 100%;
  padding: 0.25em;
  background-color: mediumblue;
  color: aliceblue;
  display: grid;
  place-content: center;
}

ul {
  width: 100%;
  list-style: none;
  padding: 0 0.25rem 0.25rem;
}

ul li::before {
  content: "\200B";
}

.item {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 0.5rem 0 0.5rem 0.5rem;
  margin: 0.25rem 0;
  background-color: #eee;
}

.item:first-child {
  margin: 0;
}

.item input[type="checkbox"] {
  text-align: center;
  width: 2.5rem;
  width: 48px;
  min-width: 48px;
  height: 2.5rem;
  height: 48px;
  min-height: 48px;
  cursor: pointer;
  margin-right: 0.5rem;
}

.item input[type="checkbox"]:focus + label {
  text-decoration: underline;
}

.item > label {
  font-size: 0.75rem;
  flex-grow: 1;
}

.item svg {
  width: 48px;
  min-width: 48px;
  height: 36px;
  font-size: 1rem;
  color: steelblue;
  cursor: pointer;
}

.item svg:focus,
.item svg:hover {
  color: red;
  outline: none;
}

.addForm {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  margin: 0.5rem 0 0;
  padding: 0 0.5rem 0.25rem;
  border-bottom: 1px solid #eee;
}

.addForm label {
  position: absolute;
  left: -99999px;
}

.addForm input[type="text"] {
  flex-grow: 1;
  max-width: calc(100% - 50px);
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  margin-right: 0.25rem;
  outline: none;
}

button {
  height: 48px;
  min-width: 48px;
  border-radius: 0.25rem;
  padding: 0.5rem;
  font-size: 1rem;
  background-color: aliceblue;
  color: mediumblue;
  cursor: pointer;
}

button:focus,
button:hover {
  color: white;
  background-color: limegreen;
  outline: none;
}

```

# #End  </details>

<details>
  <summary>12. Fetch Items from LocalStorage Database</summary>

# Fetch Items from LocalStorage Database

<img width="976" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/89eb2c7f-6455-4c1a-938a-e5dd93751bcc">
<img width="1100" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9e3bdfb8-b4c2-435f-a95e-5c3af7f260d3">

### x-dave-gray/myapp/src/App.js:

```jsbs
const [items, setItems] = useState(
  JSON.parse(localStorage.getItem("shoppinglist"))
);
```

```js
import React, { useState } from "react";
import AddItem from "./AddItem";
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  const [items, setItems] = useState(
    JSON.parse(localStorage.getItem("shoppinglist"))
  );

  const [newItem, setNewItem] = useState("");

  const setAndSaveItems = (newItems) => {
    setItems(newItems);
    localStorage.setItem("shoppinglist", JSON.stringify(newItems));
  };

  const addItem = (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setAndSaveItems(listItems);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItem) return;
    addItem(newItem);
    setNewItem("");
  };

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setAndSaveItems(listItems);
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setAndSaveItems(listItems);
  };

  return (
    <div className="App">
      <Header title="My Grocery List" />
      <AddItem
        newItem={newItem}
        setNewItem={setNewItem}
        handleSubmit={handleSubmit}
      />
      <Content
        items={items}
        handleCheck={handleCheck}
        handleDelete={handleDelete}
      />
      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;

```

# #End  </details>

<details>
  <summary>13. Search Functionality with SearchItem Component </summary>

# Search Functionality with SearchItem Component

<img width="976" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/44e9a8a1-9e58-4c49-a2b5-b959d4dad1cd">
<img width="1108" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/cb582bcf-a589-4bad-aeb2-58b8d418d7ad">
<img width="1108" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/74315192-c3a5-46f6-9795-ce5e07337a89">

### x-dave-gray/myapp/src/App.js:

```js
import React, { useState } from "react";
import AddItem from "./AddItem";
import SearchItem from "./SearchItem";
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

function App() {
  const [items, setItems] = useState(
    JSON.parse(localStorage.getItem("shoppinglist"))
  );

  const [newItem, setNewItem] = useState("");
  const [search, setSearch] = useState("");

  const setAndSaveItems = (newItems) => {
    setItems(newItems);
    localStorage.setItem("shoppinglist", JSON.stringify(newItems));
  };

  const addItem = (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setAndSaveItems(listItems);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItem) return;
    addItem(newItem);
    setNewItem("");
  };

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setAndSaveItems(listItems);
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setAndSaveItems(listItems);
  };

  return (
    <div className="App">
      <Header title="My Grocery List" />
      <AddItem
        newItem={newItem}
        setNewItem={setNewItem}
        handleSubmit={handleSubmit}
      />
      <SearchItem search={search} setSearch={setSearch} />
      <Content
        items={items.filter((item) =>
          item.item.toLowerCase().includes(search.toLowerCase())
        )}
        handleCheck={handleCheck}
        handleDelete={handleDelete}
      />
      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;

```

### x-dave-gray/myapp/src/SearchItem.js:

```js
import React from "react";

const SearchItem = ({ search, setSearch }) => {
  return (
    <form className="searchForm" onSubmit={(e) => e.preventDefault()}>
      <label htmlFor="search">Search</label>
      <input
        type="text"
        id="search"
        role="searchbox"
        placeholder="Search Items"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
    </form>
  );
};

export default SearchItem;

```

### x-dave-gray/myapp/src/index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 22px;
}

body {
  min-height: 100vh;
  font-family: "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans",
    "Droid Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  max-width: 500px;
  border: 1px solid mediumblue;
  margin: auto;
}

header {
  width: 100%;
  padding: 0 0.25em;
  background-color: mediumblue;
  color: aliceblue;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

main {
  width: 100%;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  justify-content: flex-start;
  align-items: space-around;
  overflow-y: auto;
}

footer {
  width: 100%;
  padding: 0.25em;
  background-color: mediumblue;
  color: aliceblue;
  display: grid;
  place-content: center;
}

ul {
  width: 100%;
  list-style: none;
  padding: 0 0.25rem 0.25rem;
}

ul li::before {
  content: "\200B";
}

.item {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 0.5rem 0 0.5rem 0.5rem;
  margin: 0.25rem 0;
  background-color: #eee;
}

.item:first-child {
  margin: 0;
}

.item input[type="checkbox"] {
  text-align: center;
  width: 2.5rem;
  width: 48px;
  min-width: 48px;
  height: 2.5rem;
  height: 48px;
  min-height: 48px;
  cursor: pointer;
  margin-right: 0.5rem;
}

.item input[type="checkbox"]:focus + label {
  text-decoration: underline;
}

.item > label {
  font-size: 0.75rem;
  flex-grow: 1;
}

.item svg {
  width: 48px;
  min-width: 48px;
  height: 36px;
  font-size: 1rem;
  color: steelblue;
  cursor: pointer;
}

.item svg:focus,
.item svg:hover {
  color: red;
  outline: none;
}

.addForm {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  margin: 0.5rem 0 0;
  padding: 0 0.5rem 0.25rem;
  border-bottom: 1px solid #eee;
}

.addForm label {
  position: absolute;
  left: -99999px;
}

.addForm input[type="text"] {
  flex-grow: 1;
  max-width: calc(100% - 50px);
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  margin-right: 0.25rem;
  outline: none;
}

button {
  height: 48px;
  min-width: 48px;
  border-radius: 0.25rem;
  padding: 0.5rem;
  font-size: 1rem;
  background-color: aliceblue;
  color: mediumblue;
  cursor: pointer;
}

button:focus,
button:hover {
  color: white;
  background-color: limegreen;
  outline: none;
}

.searchForm {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  margin: 0.25rem 0 0;
  padding: 0 0.5rem 0.25rem;
  border-bottom: 1px solid #eee;
}

.searchForm label {
  position: absolute;
  left: -99999px;
}

.searchForm input[type="text"] {
  flex-grow: 1;
  max-width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  outline: none;
}

```

# #End  </details>

<details>
  <summary>14. Using useRef Hook to manage Input Focus</summary>

# Using useRef Hook to manage Input Focus

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dc3f40c5-c753-4d91-aa0d-6c87b1a05819">
<img width="1108" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/641eaab1-c4ce-46da-ae31-247a712ad266">

### x-dave-gray/myapp/src/AddItem.js:

```js
import React, { useRef } from "react";
import { FaPlus } from "react-icons/fa";

const AddItem = ({ newItem, setNewItem, handleSubmit }) => {
  const inputRef = useRef();

  return (
    <form onSubmit={handleSubmit} className="addForm">
      <label htmlFor="addItem">Add Item</label>
      <input
        type="text"
        ref={inputRef}
        id="addItem"
        placeholder="Add Item"
        autoFocus
        required
        value={newItem}
        onChange={(e) => setNewItem(e.target.value)}
      />
      <button
        type="submit"
        arai-label="Add Item"
        onClick={() => inputRef.current.focus()}
      >
        <FaPlus />
      </button>
    </form>
  );
};

export default AddItem;

```

# #End  </details>

+COLOR SELECTOR APP

<details>
  <summary>15. Color Selector App - Introduction</summary>

# Introduction

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/42a12964-6cd8-4818-993a-0909425c3fa3">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/238d607f-5a91-49b9-8226-d3f2cafc0639">

# Install React App:

```bs
npx create-react-app .
npx create-react-app color-selector
```

### x-dave-gray/color-selector/src/index.js:

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

### x-dave-gray/color-selector/src/App.js:

```js
import React from "react";

import Square from "./Square";
import Input from "./Input";

function App() {
  return (
    <div className="App">
      <Square />
      <Input />
    </div>
  );
}

export default App;

```

### x-dave-gray/color-selector/src/Square.js:

```js
import React from "react";

const Square = () => {
  return <h2>Square</h2>;
};

export default Square;
```

### x-dave-gray/color-selector/src/Input.js:

```js
import React from "react";

const Input = () => {
  return <h2>Input</h2>;
};

export default Input;
```

# #End  </details>

<details>
  <summary>16. Color Selector App - Style Square and Input Components</summary>

# Style Square and Input Components

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/43c4a2a5-9901-4333-81a2-20ab98620a51">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9e6ccaea-36c5-4bf1-862a-be1ec92ce507">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/60ee5c1a-b01b-41f9-8645-c1e6233e0003">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/50ac974d-54dc-44f6-9f9e-f13e5d0dea20">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/91f76af7-31d7-4e3b-bc52-da67a928a64e">

### x-dave-gray/color-selector/src/colors.json:

```json
{
  "lilac": "#c8a2c8"
}
```

### x-dave-gray/color-selector/src/App.js:

```js
import React, { useState } from "react";
import Square from "./Square";
import Input from "./Input";
import colors from "./colors.json";

function App() {
  const [colorValue, setColorValue] = useState("");

  return (
    <div className="App">
      <Square colorValue={colorValue} colors={colors} />
      <Input colorValue={colorValue} setColorValue={setColorValue} />
    </div>
  );
}

export default App;
```

### x-dave-gray/color-selector/src/Square.js:

```js
import React from "react";

const Square = ({ colorValue, colors }) => {
  return (
    <section
      className="square"
      style={{ backgroundColor: colors[colorValue] || colorValue }}
    >
      <p>{colorValue ? colorValue : "Empty Value"}</p>
    </section>
  );
};

Square.defaultProps = {
  colorValue: "Empty Color Value",
};

export default Square;
```

### x-dave-gray/color-selector/src/Input.js:

```js
import React from "react";

const Input = ({ colorValue, setColorValue }) => {
  return (
    <form onSubmit={(e) => e.preventDefault()}>
      <label htmlFor="">Add Color Name:</label>
      <input
        type="text"
        placeholder="Add color name"
        value={colorValue}
        onChange={(e) => setColorValue(e.target.value)}
        autoFocus
        required
      />
    </form>
  );
};

export default Input;
```

### x-dave-gray/color-selector/src/index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 36px;
}

body {
  min-height: 100vh;
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.square {
  width: 400px;
  height: 400px;
  border: 2px solid #000;
  box-shadow: 2px 2px 5px #000;
  border-radius: 0.25rem;
  display: grid;
  place-content: center;
}

.square p {
  text-align: center;
}

form {
  width: 400px;
}

label {
  position: absolute;
  left: -99999px;
}

input[type="text"] {
  margin-top: 0.5rem;
  padding: 0.25rem;
  width: 100%;
  font-size: 1rem;
  box-shadow: 2px 2px 5px #000;
  border-radius: 0.25rem;
  outline: none;
}

button {
  width: 100%;
  min-height: 48px;
  margin-top: 0.5rem;
  font-size: 1rem;
  border-radius: 0.25rem;
  box-shadow: 2px 2px 5px #000;
  padding: 0.25rem;
}
```

# #End  </details>

<details>
  <summary>17. Color Selector App - Color Names to Hex Values</summary>

# Color Names to Hex Values

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8ee4ccb6-e9f9-4ab8-933d-36ac57a45e85">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/39610ac3-ac87-49d7-b5be-b46fdb4445ae">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7ba4e921-15f5-4c8e-8806-4b08c4ac5168">


# Install Colornames module

```bs
npm i colornames -S
```

### x-dave-gray/color-selector/src/App.js:

```js
import React, { useState } from "react";

import Square from "./Square";
import Input from "./Input";
import colors from "./colors.json";

function App() {
  const [colorValue, setColorValue] = useState("");
  const [hexValue, setHexValue] = useState("");

  return (
    <div className="App">
      <Square colorValue={colorValue} hexValue={hexValue} colors={colors} />
      <Input
        colorValue={colorValue}
        setColorValue={setColorValue}
        setHexValue={setHexValue}
        colors={colors}
      />
    </div>
  );
}

export default App;

```

### x-dave-gray/color-selector/src/Square.js:

```js
import React from "react";

const Square = ({ colorValue, colors, hexValue }) => {
  return (
    <section
      className="square"
      style={{ backgroundColor: colors[colorValue] || colorValue }}
    >
      <p>{colorValue ? colorValue : "Empty Value"}</p>
      <p>{hexValue && hexValue}</p>
    </section>
  );
};

Square.defaultProps = {
  colorValue: "Empty Color Value",
};

export default Square;
```

### x-dave-gray/color-selector/src/Input.js:

```js
import React from "react";
import colorNames from "colornames";

const Input = ({ colorValue, setColorValue, setHexValue, colors }) => {
  return (
    <form onSubmit={(e) => e.preventDefault()}>
      <label htmlFor="">Add Color Name:</label>
      <input
        type="text"
        placeholder="Add color name"
        value={colorValue}
        onChange={(e) => {
          setColorValue(e.target.value);
          setHexValue(colorNames(e.target.value) || colors[e.target.value]);
        }}
        autoFocus
        required
      />
    </form>
  );
};

export default Input;
```

### x-dave-gray/color-selector/src/colors.json:

```js
{
  "lilac": "#c8a2c8",
  "rose": "#ff007f"
}
```

# #End  </details>

<details>
  <summary>18. Color Selector App - Toggling Black and White Text</summary>

# Toggling Black and White Text

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3a244918-d021-4571-a17e-a72c71d7e43f">
<img width="1106" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bb740896-2e7a-467a-bb4b-fe6c662337d1">
<img width="1106" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ce3a9399-e1f9-4f77-8456-87dcb7a21a88">

### x-dave-gray/color-selector/src/App.js:

```js
import React, { useState } from "react";
import Square from "./Square";
import Input from "./Input";
import colors from "./colors.json";

function App() {
  const [colorValue, setColorValue] = useState("");
  const [hexValue, setHexValue] = useState("");
  const [isDarktext, setIsDarktext] = useState(true);

  return (
    <div className="App">
      <Square
        colorValue={colorValue}
        hexValue={hexValue}
        colors={colors}
        isDarktext={isDarktext}
      />
      <Input
        colorValue={colorValue}
        setColorValue={setColorValue}
        setHexValue={setHexValue}
        colors={colors}
        isDarktext={isDarktext}
        setIsDarktext={setIsDarktext}
      />
    </div>
  );
}

export default App;
```

### x-dave-gray/color-selector/src/Square.js:

```js
import React from "react";

const Square = ({ colorValue, colors, hexValue, isDarktext }) => {
  return (
    <section
      className="square"
      style={{
        backgroundColor: colors[colorValue] || colorValue,
        color: isDarktext ? "#000" : "#fff",
      }}
    >
      <p>{colorValue ? colorValue : "Empty Value"}</p>
      <p>{hexValue && hexValue}</p>
    </section>
  );
};

Square.defaultProps = {
  colorValue: "Empty Color Value",
};

export default Square;
```

### x-dave-gray/color-selector/src/Input.js:

```js
import React from "react";
import colorNames from "colornames";

const Input = ({
  colorValue,
  setColorValue,
  setHexValue,
  colors,
  isDarktext,
  setIsDarktext,
}) => {
  return (
    <form onSubmit={(e) => e.preventDefault()}>
      <label htmlFor="">Add Color Name:</label>
      <input
        type="text"
        placeholder="Add color name"
        value={colorValue}
        onChange={(e) => {
          setColorValue(e.target.value);
          setHexValue(colorNames(e.target.value) || colors[e.target.value]);
        }}
        autoFocus
        required
      />
      <button type="button" onClick={() => setIsDarktext(!isDarktext)}>
        Toggle Text Color
      </button>
    </form>
  );
};

export default Input;
```

### x-dave-gray/color-selector/src/index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 36px;
}

body {
  min-height: 100vh;
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.square {
  width: 400px;
  height: 400px;
  border: 2px solid #000;
  box-shadow: 2px 2px 5px #000;
  border-radius: 0.25rem;
  display: grid;
  place-content: center;
}

.square p {
  text-align: center;
}

form {
  width: 400px;
}

label {
  position: absolute;
  left: -99999px;
}

input[type="text"] {
  margin-top: 0.5rem;
  padding: 0.25rem;
  width: 100%;
  font-size: 1rem;
  box-shadow: 2px 2px 5px #000;
  border-radius: 0.25rem;
  outline: none;
}

button {
  width: 100%;
  min-height: 48px;
  margin-top: 0.5rem;
  font-size: 1rem;
  border-radius: 0.25rem;
  box-shadow: 2px 2px 5px #000;
  padding: 0.25rem;
}

```

# #End  </details>

+JSON-SERVER

<details>
  <summary>19. Using useEffect to set Data</summary>

<img width="978" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/085ec7e9-1b3c-44da-b53c-8954f4b343ff">

<img width="1244" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6b6d24d5-18cd-4861-a02b-06e0b2ad369b">

### x-dave-gray/myapp/src/App.js:

```js
import Header from "./Header";
import AddItem from "./AddItem";
import SearchItem from "./SearchItem";
import Content from "./Content";
import Footer from "./Footer";
import React, { useState, useEffect } from "react";

function App() {
  const [items, setItems] = useState(
    JSON.parse(localStorage.getItem("shoppinglist")) || []
  );
  const [newItem, setNewItem] = useState("");
  const [search, setSearch] = useState("");

  useEffect(() => {
    localStorage.setItem("shoppinglist", JSON.stringify(items));
  }, [items]);

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);
  };

  const addItem = (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setItems(listItems);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItem) return;
    // addItem
    addItem(newItem);
    setNewItem("");
  };

  return (
    <div className="App">
      <Header title="Groceries List" />
      <AddItem
        newItem={newItem}
        setNewItem={setNewItem}
        handleSubmit={handleSubmit}
      />
      <SearchItem search={search} setSearch={setSearch} />
      <Content
        items={items.filter((item) =>
          item.item.toLowerCase().includes(search.toLowerCase())
        )}
        handleCheck={handleCheck}
        handleDelete={handleDelete}
      />
      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;

```

# #End  </details>

<details>
  <summary>20. JSON sever - Using JSON Server</summary>

# Using JSON Server

<img width="978" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/88054acd-04c3-4785-a2c7-57c701d4244b">
<img width="1243" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d958c0fe-6638-4922-b266-99991b98337d">
<img width="1243" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/722df0fe-272b-41c8-b653-041cfa969e6d">

# Install and start JSON Server:

```bs
npm i json-server
json-server -p 3500 --watch data/db.json
```

```bs
npx json-server -p 3500 -w data/db.json
```

### x-dave-gray/myapp/data/db.json:

```json
{
  "items": [
    {
      "id": 1,
      "checked": false,
      "item": "Almonds, Unsalted, in the blue bag"
    },
    {
      "id": 2,
      "checked": false,
      "item": "Pizza"
    },
    {
      "id": 3,
      "checked": false,
      "item": "Bread"
    }
  ]
}
```

# Fetch JSON Server for item 1:

```bs
http://localhost:3500/items/1
```

```js
// {
// "id": 1,
// "checked": false,
// "item": "Almonds, Unsalted, in the blue bag"
// }
```

# #End  </details>

<details>
  <summary>21. JSON sever - Fetch JSON API Data </summary>

# Fetch JSON API Data

<img width="978" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4d55270a-cf52-4d43-ab27-47886d9879f0">
<img width="1243" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c6755f13-a965-43c9-a612-c2c9136ae96d">
<img width="1244" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6a933933-68b5-4338-9403-65f095644b07">

### x-dave-gray/myapp/src/App.js:

```js
import Header from "./Header";
import AddItem from "./AddItem";
import SearchItem from "./SearchItem";
import Content from "./Content";
import Footer from "./Footer";
import React, { useState, useEffect } from "react";

function App() {
  const API_URL = "http://localhost:3500/items";

  const [items, setItems] = useState(
    JSON.parse(localStorage.getItem("shoppinglist")) || []
  );
  const [newItem, setNewItem] = useState("");
  const [search, setSearch] = useState("");
  const [fetchError, setFetchError] = useState(null);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Did not receive Data from API");
        const listItems = await response.json();
        console.log(listItems);
        setItems(listItems);
        setFetchError(null);
      } catch (err) {
        // console.log(err.stack);
        // console.log(err.message);
        setFetchError(err.message);
      }
    };

    fetchItems();
    //(async () => await fetchItems())();
  }, []);

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);
  };

  const addItem = (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setItems(listItems);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItem) return;
    // addItem
    addItem(newItem);
    setNewItem("");
  };

  return (
    <div className="App">
      <Header title="Groceries List" />
      <AddItem
        newItem={newItem}
        setNewItem={setNewItem}
        handleSubmit={handleSubmit}
      />
      <SearchItem search={search} setSearch={setSearch} />
      <main>
        {fetchError && (
          <p
            style={{ color: "red", textAlign: "center" }}
          >{`Error: ${fetchError}`}</p>
        )}
        {!fetchError && (
          <Content
            items={items.filter((item) =>
              item.item?.toLowerCase().includes(search.toLowerCase())
            )}
            handleCheck={handleCheck}
            handleDelete={handleDelete}
          />
        )}
      </main>
      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;

```

### x-dave-gray/myapp/src/Content.js:

```js
import ItemList from "./ItemList";

const Content = ({ items, handleCheck, handleDelete }) => {
  return (
    <>
      {items.length ? (
        <ItemList
          items={items}
          handleCheck={handleCheck}
          handleDelete={handleDelete}
        />
      ) : (
        <p style={{ marginTop: "2rem" }}>Your List is empty!</p>
      )}
    </>
  );
};

export default Content;
```

# #End  </details>

<details>
  <summary>22. JSON sever - SetTimeout to simulate a slow REST API Response</summary>

# SetTimeout to simulate a slow REST API Response

<img width="980" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ed1656cd-48a6-4834-b8a2-8ce45b3d0b6b">

### x-dave-gray/myapp/src/App.js:

```bs
setTimeout(() => {
  fetchItems();
  //(async () => await fetchItems())();
}, 2000);
```

```js
import Header from "./Header";
import AddItem from "./AddItem";
import SearchItem from "./SearchItem";
import Content from "./Content";
import Footer from "./Footer";
import React, { useState, useEffect } from "react";

function App() {
  const API_URL = "http://localhost:3500/items";

  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState("");
  const [search, setSearch] = useState("");
  const [fetchError, setFetchError] = useState(null);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("No Data Found");
        const listItems = await response.json();
        setItems(listItems);
        setFetchError(null);
      } catch (err) {
        //console.log(err.message);
        setFetchError(err.message);
      }
    };

    setTimeout(() => {
      fetchItems();
      //(async () => await fetchItems())();
    }, 2000);
  }, []);

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);
  };

  const addItem = (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setItems(listItems);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItem) return;
    // addItem
    addItem(newItem);
    setNewItem("");
  };

  return (
    <div className="App">
      <Header title="Groceries List" />
      <AddItem
        newItem={newItem}
        setNewItem={setNewItem}
        handleSubmit={handleSubmit}
      />
      <SearchItem search={search} setSearch={setSearch} />
      <main>
        {fetchError && <p style={{ color: "red" }}>{`Error: ${fetchError}`}</p>}
        {!fetchError && (
          <Content
            items={items.filter((item) =>
              item.item?.toLowerCase().includes(search.toLowerCase())
            )}
            handleCheck={handleCheck}
            handleDelete={handleDelete}
          />
        )}
      </main>

      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>23. JSON sever - Set isLoading Hook</summary>

# Set isLoading Hook

<img width="980" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/72166225-d84d-4589-9ffb-116c3ffca57d">
<img width="1244" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/de26770d-1cca-47d6-a579-f050d8679b8d">

### x-dave-gray/myapp/src/App.js:

```js
import Header from "./Header";
import AddItem from "./AddItem";
import SearchItem from "./SearchItem";
import Content from "./Content";
import Footer from "./Footer";
import React, { useState, useEffect } from "react";

function App() {
  const API_URL = "http://localhost:3500/items";

  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState("");
  const [search, setSearch] = useState("");
  const [fetchError, setFetchError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("No Data Found");
        const listItems = await response.json();
        setItems(listItems);
        setFetchError(null);
      } catch (err) {
        //console.log(err.message);
        setFetchError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    setTimeout(() => {
      fetchItems();
      //(async () => await fetchItems())();
    }, 2000);
  }, []);

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);
  };

  const addItem = (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setItems(listItems);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItem) return;
    // addItem
    addItem(newItem);
    setNewItem("");
  };

  return (
    <div className="App">
      <Header title="Groceries List" />
      <AddItem
        newItem={newItem}
        setNewItem={setNewItem}
        handleSubmit={handleSubmit}
      />
      <SearchItem search={search} setSearch={setSearch} />
      <main>
        {isLoading && <p>Loading Items...</p>}
        {fetchError && <p style={{ color: "red" }}>{`Error: ${fetchError}`}</p>}
        {!fetchError && !isLoading && (
          <Content
            items={items.filter((item) =>
              item.item?.toLowerCase().includes(search.toLowerCase())
            )}
            handleCheck={handleCheck}
            handleDelete={handleDelete}
          />
        )}
      </main>

      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>24. JSON server - Building API Request Function for CRUD </summary>

# Building API Request Function for CRUD

<img width="974" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1c56e19d-bed8-4f87-8034-d5d4a16912c4">

### x-dave-gray/myapp/src/apiRequest.js:

```js
const apiRequest = async (url = "", optionsObj = null, errMsg = null) => {
  try {
    const response = await fetch(url, optionsObj);
    if (!response.ok) throw Error("Error, Please reload the app");
  } catch (err) {
    errMsg = err.message;
  } finally {
    return errMsg;
  }
};

export default apiRequest;
```

# #End  </details>

<details>
  <summary>25. JSON server - Create or POST a new Item to DB </summary>

# Create or POST a new Item to DB

<img width="971" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1c979fbd-abc6-474c-bb39-b5f1a705c1bf">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2b049c94-c8a2-4efa-a342-08804dc29821">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e07cc1b7-6b65-45a2-a942-7415ca267616">

### x-dave-gray/myapp/src/App.js:

```bs
//Create/POST a new item to DB
  const addItem = async (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setItems(listItems);

    const postOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(myNewItem),
    };

    const result = await apiRequest(API_URL, postOptions);
    if (result) setFetchError(result);
  };
```

```js
import Header from "./Header";
import AddItem from "./AddItem";
import SearchItem from "./SearchItem";
import Content from "./Content";
import Footer from "./Footer";
import React, { useState, useEffect } from "react";
import apiRequest from "./apiRequest";

function App() {
  const API_URL = "http://localhost:3500/items";

  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState("");
  const [search, setSearch] = useState("");
  const [fetchError, setFetchError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("No Data Found");
        const listItems = await response.json();
        setItems(listItems);
        setFetchError(null);
      } catch (err) {
        setFetchError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    setTimeout(() => {
      fetchItems();
    }, 2000);
  }, []);

  const handleCheck = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);
  };

  //Create/POST a new item to DB
  const addItem = async (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setItems(listItems);

    const postOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(myNewItem),
    };

    const result = await apiRequest(API_URL, postOptions);
    if (result) setFetchError(result);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItem) return;
    addItem(newItem);
    setNewItem("");
  };

  return (
    <div className="App">
      <Header title="Groceries List" />
      <AddItem
        newItem={newItem}
        setNewItem={setNewItem}
        handleSubmit={handleSubmit}
      />
      <SearchItem search={search} setSearch={setSearch} />
      <main>
        {isLoading && <p>Loading Items...</p>}
        {fetchError && <p style={{ color: "red" }}>{`Error: ${fetchError}`}</p>}
        {!fetchError && !isLoading && (
          <Content
            items={items.filter((item) =>
              item.item?.toLowerCase().includes(search.toLowerCase())
            )}
            handleCheck={handleCheck}
            handleDelete={handleDelete}
          />
        )}
      </main>

      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;
```

### x-dave-gray/myapp/data/db.json:

```json
{
  "items": [
    {
      "id": 1,
      "checked": false,
      "item": "Almonds, Unsalted, in the blue bag"
    },
    {
      "id": 2,
      "checked": false,
      "item": "Pizza"
    },
    {
      "id": 3,
      "checked": false,
      "item": "Bread"
    },
    {
      "id": 4,
      "checked": false,
      "item": "See the Doctor"
    }
  ]
}
```

# #End  </details>

<details>
  <summary>26. JSON server - Update an Item in DB</summary>

# Update an Item in DB

<img width="976" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9606f17a-b9c5-4e08-8ae3-dd23609710b2">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f3817c3f-cd3a-4f13-8e86-513ececce3d0">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6942de4b-ad48-4bbe-877a-d9ccc86c3974">

### x-dave-gray/myapp/src/App.js:

```bs
//Update an item in DB
  const handleCheck = async (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);

    const myItem = listItems.filter((item) => item.id === id);
    const updateOptions = {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ checked: myItem[0].checked }),
    };
    const reqUrl = `${API_URL}/${id}`;
    const result = await apiRequest(reqUrl, updateOptions);
    if (result) setFetchError(result);
  };
```

```js
import Header from "./Header";
import AddItem from "./AddItem";
import SearchItem from "./SearchItem";
import Content from "./Content";
import Footer from "./Footer";
import React, { useState, useEffect } from "react";
import apiRequest from "./apiRequest";

function App() {
  const API_URL = "http://localhost:3500/items";

  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState("");
  const [search, setSearch] = useState("");
  const [fetchError, setFetchError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("No Data Found");
        const listItems = await response.json();
        setItems(listItems);
        setFetchError(null);
      } catch (err) {
        setFetchError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    setTimeout(() => {
      fetchItems();
    }, 2000);
  }, []);

  //Update an item in DB
  const handleCheck = async (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);

    const myItem = listItems.filter((item) => item.id === id);
    const updateOptions = {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ checked: myItem[0].checked }),
    };
    const reqUrl = `${API_URL}/${id}`;
    const result = await apiRequest(reqUrl, updateOptions);
    if (result) setFetchError(result);
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);
  };

  //Create/POST a new item to DB
  const addItem = async (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setItems(listItems);

    const postOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(myNewItem),
    };

    const result = await apiRequest(API_URL, postOptions);
    if (result) setFetchError(result);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItem) return;
    addItem(newItem);
    setNewItem("");
  };

  return (
    <div className="App">
      <Header title="Groceries List" />
      <AddItem
        newItem={newItem}
        setNewItem={setNewItem}
        handleSubmit={handleSubmit}
      />
      <SearchItem search={search} setSearch={setSearch} />
      <main>
        {isLoading && <p>Loading Items...</p>}
        {fetchError && <p style={{ color: "red" }}>{`Error: ${fetchError}`}</p>}
        {!fetchError && !isLoading && (
          <Content
            items={items.filter((item) =>
              item.item?.toLowerCase().includes(search.toLowerCase())
            )}
            handleCheck={handleCheck}
            handleDelete={handleDelete}
          />
        )}
      </main>

      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;
```

### x-dave-gray/myapp/data/db.json:

```json
{
  "items": [
    {
      "id": 1,
      "checked": false,
      "item": "Almonds, Unsalted, in the blue bag"
    },
    {
      "id": 2,
      "checked": false,
      "item": "Pizza"
    },
    {
      "id": 3,
      "checked": false,
      "item": "Bread"
    },
    {
      "id": 4,
      "checked": true,
      "item": "See the Doctor"
    }
  ]
}
```

# #End  </details>

<details>
  <summary>27. JSON server - Delete an Item in DB</summary>

# Delete an Item in DB

<img width="976" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f1f11c84-6714-4540-8f47-e84aee44e68b">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/42e27550-3300-4cc0-86be-a53083a68394">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ac903aa0-f461-4252-8a65-8b7c5c0adb47">

### x-dave-gray/myapp/src/App.js:

```bs
//Delete an item in DB
  const handleDelete = async (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);

    const deleteOptions = { method: "DELETE" };
    const reqUrl = `${API_URL}/${id}`;
    const result = await apiRequest(reqUrl, deleteOptions);
    if (result) setFetchError(result);
  };
```

```js
import Header from "./Header";
import AddItem from "./AddItem";
import SearchItem from "./SearchItem";
import Content from "./Content";
import Footer from "./Footer";
import React, { useState, useEffect } from "react";
import apiRequest from "./apiRequest";

function App() {
  const API_URL = "http://localhost:3500/items";

  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState("");
  const [search, setSearch] = useState("");
  const [fetchError, setFetchError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("No Data Found");
        const listItems = await response.json();
        setItems(listItems);
        setFetchError(null);
      } catch (err) {
        setFetchError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    setTimeout(() => {
      fetchItems();
    }, 2000);
  }, []);

  //Delete an item in DB
  const handleDelete = async (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);

    const deleteOptions = { method: "DELETE" };
    const reqUrl = `${API_URL}/${id}`;
    const result = await apiRequest(reqUrl, deleteOptions);
    if (result) setFetchError(result);
  };

  //Update an item in DB
  const handleCheck = async (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);

    const myItem = listItems.filter((item) => item.id === id);
    const updateOptions = {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ checked: myItem[0].checked }),
    };
    const reqUrl = `${API_URL}/${id}`;
    const result = await apiRequest(reqUrl, updateOptions);
    if (result) setFetchError(result);
  };

  //Create/POST a new item to DB
  const addItem = async (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const myNewItem = { id, checked: false, item };
    const listItems = [...items, myNewItem];
    setItems(listItems);

    const postOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(myNewItem),
    };

    const result = await apiRequest(API_URL, postOptions);
    if (result) setFetchError(result);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItem) return;
    addItem(newItem);
    setNewItem("");
  };

  return (
    <div className="App">
      <Header title="Groceries List" />
      <AddItem
        newItem={newItem}
        setNewItem={setNewItem}
        handleSubmit={handleSubmit}
      />
      <SearchItem search={search} setSearch={setSearch} />
      <main>
        {isLoading && <p>Loading Items...</p>}
        {fetchError && <p style={{ color: "red" }}>{`Error: ${fetchError}`}</p>}
        {!fetchError && !isLoading && (
          <Content
            items={items.filter((item) =>
              item.item?.toLowerCase().includes(search.toLowerCase())
            )}
            handleCheck={handleCheck}
            handleDelete={handleDelete}
          />
        )}
      </main>

      <Footer itemLength={items.length} />
    </div>
  );
}

export default App;
```

### x-dave-gray/myapp/data/db.json:

```json
{
  "items": [
    {
      "id": 1,
      "checked": false,
      "item": "Almonds, Unsalted, in the blue bag"
    },
    {
      "id": 2,
      "checked": false,
      "item": "Pizza"
    },
    {
      "id": 3,
      "checked": false,
      "item": "Bread"
    }
  ]
}
```

# #End  </details>

+FETCH API TASK WITH JSONPLACEHOLDER

<details>
  <summary>28. Fetch API Task with JSONPLACEHOLDER - Introduction </summary>

# Fetch API Task with JSONPLACEHOLDER - Introduction

<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/59f95f15-11e3-4a51-9851-e1cc664bad31">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1d3cd93c-63de-47c0-b6d6-1ba5c276bbeb">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/321c2427-ab8d-49fe-9bd8-488f58974ec3">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0e4ad0b2-1c1e-48a8-a2f6-3cb1977b5d4b">

# Endpoints

```bs
https://jsonplaceholder.typicode.com/
https://jsonplaceholder.typicode.com/users
https://jsonplaceholder.typicode.com/posts
https://jsonplaceholder.typicode.com/comments
https://jsonplaceholder.typicode.com/albums
https://jsonplaceholder.typicode.com/photos
https://jsonplaceholder.typicode.com/todos
```

```bs
/posts	  100 posts
/comments	500 comments
/albums	  100 albums
/photos	  5000 photos
/todos	  200 todos
/users	  10 users
```

# HTTP Methods

```bs
GET	    /posts
GET	    /posts/1
GET	    /posts/1/comments
GET	    /comments?postId=1
POST	  /posts
PUT	    /posts/1
PATCH	  /posts/1
DELETE	/posts/1
```

# Fetch a Todo Item

```bs
fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(json => console.log(json))
```

# #End  </details>

<details>
  <summary>29. Fetch API Task with JSONPLACEHOLDER - Create Challenge App</summary>

# Create Challenge App

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dabbec9b-89a9-42c3-a8bf-bdf257f5af0b">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/07821a44-4640-48fd-b0d7-f82fb12e6bdb">

# Install React App

```jsbs
npx create-react-app challenge
yarn create react-app challenge
```

### x-dave-gray/challenge/src/index.js:

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

### x-dave-gray/challenge/src/App.js:

```js
import React from "react";

function App() {
  return (
    <div className="App">
      <h1>Challenge Page</h1>
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>30. Fetch API Task with JSONPLACEHOLDER - Challenge 1</summary>

# Challenge 1 - Fetch and display users, posts and comments data

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/54325a43-d917-4677-8df5-7ee7deb12c1c">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/089fd607-9e1e-412a-8994-239f5eb619c9">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ce4a79d9-238a-428b-8b7e-f3afff4c1335">
<img width="1245" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7b54df53-9ab6-41db-852f-fe9cebfe6c72">

### x-dave-gray/challenge/src/App.js:

```js
import { useState, useEffect } from "react";

function App() {
  const API_URL = "https://jsonplaceholder.typicode.com/";
  const [reqType, setReqType] = useState("users");
  const [items, setItems] = useState([]);
  const [errMsg, setErrMsg] = useState("");

  useEffect(() => {
    const fetchItems = async () => {
      try {
        setErrMsg("");
        const response = await fetch(`${API_URL}${reqType}`);
        if (!response.ok) throw new Error("No Data!");
        const data = await response.json();
        setItems(data);
      } catch (err) {
        setErrMsg(`Error: ${err.message}`);
      } finally {
        //
      }
    };

    fetchItems();
  }, [reqType]);

  return (
    <div className="App">
      <header className="header">
        <button onClick={(e) => setReqType(e.target.innerHTML)}>users</button>
        <button onClick={(e) => setReqType(e.target.innerHTML)}>posts</button>
        <button onClick={(e) => setReqType(e.target.innerHTML)}>
          comments
        </button>
      </header>
      <main>
        <h2 style={{ color: "red" }}>{errMsg}</h2>
        <ul>
          {!errMsg && items.map((item) => <li>{JSON.stringify(item)}</li>)}
        </ul>
      </main>
    </div>
  );
}

export default App;
```

### x-dave-gray/challenge/src/index.css:

```css
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto",
    "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans",
    "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, "Courier New",
    monospace;
}

.header {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.header > button {
  cursor: pointer;
  padding: 1rem;
}

button:focus,
button:active,
button:hover {
  background-color: #141414;
  color: #fff;
}
```

# #End  </details>

<details>
  <summary>31. Fetch API Task with JSONPLACEHOLDER - Challenge 2</summary>

# Challenge 2 - Create Components to organise app

<img width="976" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ff368da4-9ff6-4b17-8eac-9aabe35c5023">
<img width="1226" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dc2bc101-e160-4ee0-bfd4-485580f4caf9">
<img width="1226" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ecb2344c-b8dd-44c7-977e-102f20e10b02">
<img width="1226" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f28e3340-73ab-4cab-b953-2dbd83a1269e">

### x-dave-gray/challenge/src/App.js:

```js
import { useState, useEffect } from "react";
import Form from "./Form";
import List from "./List";

function App() {
  const API_URL = "https://jsonplaceholder.typicode.com/";
  const [reqType, setReqType] = useState("users");
  const [items, setItems] = useState([]);
  const [errMsg, setErrMsg] = useState("");

  useEffect(() => {
    const fetchItems = async () => {
      try {
        setErrMsg("");
        const response = await fetch(`${API_URL}${reqType}`);
        if (!response.ok) throw new Error("No Data!");
        const data = await response.json();
        setItems(data);
      } catch (err) {
        setErrMsg(`Error: ${err.message}`);
      } finally {
        //
      }
    };

    fetchItems();
  }, [reqType]);

  return (
    <div className="App">
      <Form reqType={reqType} setReqType={setReqType} />
      <List items={items} errMsg={errMsg} />
    </div>
  );
}

export default App;
```

### x-dave-gray/challenge/src/Form.js:

```js
import React from "react";
import Button from "./Button";

const Form = ({ reqType, setReqType }) => {
  return (
    <form onSubmit={(e) => e.preventDefault()}>
      <Button buttonText="users" reqType={reqType} setReqType={setReqType} />
      <Button buttonText="posts" reqType={reqType} setReqType={setReqType} />
      <Button buttonText="comments" reqType={reqType} setReqType={setReqType} />
    </form>
  );
};

export default Form;
```

### x-dave-gray/challenge/src/Button.js:

```js
import React from "react";

const Button = ({ buttonText, reqType, setReqType }) => {
  return (
    <button
      className={buttonText === reqType ? "selected" : null}
      type="button"
      onClick={(e) => setReqType(buttonText)}
    >
      {buttonText}
    </button>
  );
};

export default Button;
```

### x-dave-gray/challenge/src/List.js:

```js
import React from "react";
import ListItem from "./ListItem";

const List = ({ items, errMsg }) => {
  return (
    <main>
      <h2 style={{ color: "red" }}>{errMsg}</h2>
      <ul>
        {!errMsg && items.map((item) => <ListItem key={item.id} item={item} />)}
      </ul>
    </main>
  );
};

export default List;
```

### x-dave-gray/challenge/src/ListItem.js:

```js
import React from "react";

const ListItem = ({ item }) => {
  return <li>{JSON.stringify(item)}</li>;
};

export default ListItem;
```

### x-dave-gray/challenge/src/index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 22px;
}

body {
  min-height: 100vh;
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

form {
  width: 100%;
  position: fixed;
}

button {
  width: 33.33%;
  padding: 0.5rem;
  font-size: 1rem;
}

button.selected {
  background-color: #000;
  color: #fff;
}

ul {
  padding: 3rem 2rem 1rem;
}

li {
  margin-bottom: 1rem;
}

.table-container {
  width: 100%;
  overflow-y: auto;
  padding-top: 52px;
}

td {
  border: 1px solid #000;
  padding: 0.25rem;
}
```

# #End  </details>

<details>
  <summary>32. Fetch API Task with JSONPLACEHOLDER - Challenge 3</summary>

# Challenge 3 - Sort data into Table

<img width="977" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/94989216-6930-48cc-b096-22e3138f227f">
<img width="1214" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/71a3a101-def4-41ab-8c01-0781b35f7c94">
<img width="1214" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9a43f1d5-4b28-4073-929d-58a1545c7541">
<img width="1214" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0710751b-2bfc-4953-abfe-cb81306f29ac">

### x-dave-gray/challenge/src/App.js:

```js
import { useState, useEffect } from "react";
import Form from "./Form";
// import List from "./List";
import Table from "./Table";

function App() {
  const API_URL = "https://jsonplaceholder.typicode.com/";
  const [reqType, setReqType] = useState("users");
  const [items, setItems] = useState([]);
  const [errMsg, setErrMsg] = useState("");

  useEffect(() => {
    const fetchItems = async () => {
      try {
        setErrMsg("");
        const response = await fetch(`${API_URL}${reqType}`);
        if (!response.ok) throw new Error("No Data!");
        const data = await response.json();
        setItems(data);
      } catch (err) {
        setErrMsg(`Error: ${err.message}`);
      } finally {
        //
      }
    };

    fetchItems();
  }, [reqType]);

  return (
    <div className="App">
      <Form reqType={reqType} setReqType={setReqType} />
      {/* <List items={items} errMsg={errMsg} /> */}
      <Table items={items} errMsg={errMsg} />
    </div>
  );
}

export default App;
```

### x-dave-gray/challenge/src/Table.js:

```js
import React from "react";
import Row from "./Row";

const Table = ({ items, errMsg }) => {
  return (
    <div className="table-container">
      <h2 style={{ color: "red" }}>{errMsg}</h2>
      <table>
        <tbody>
          {items.map((item) => (
            <Row key={item.id} item={item} />
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
```

### x-dave-gray/challenge/src/Row.js:

```js
import React from "react";
import Cell from "./Cell";

const Row = ({ item }) => {
  return (
    <tr>
      {Object.entries(item).map(([key, value]) => (
        <Cell key={key} cellData={JSON.stringify(value)} />
      ))}
    </tr>
  );
};

export default Row;
```

### x-dave-gray/challenge/src/Cell.js:

```js
import React from "react";

const Cell = ({ cellData }) => {
  return <td>{cellData}</td>;
};

export default Cell;
```

### x-dave-gray/challenge/src/index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 22px;
}

body {
  min-height: 100vh;
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

form {
  width: 100%;
  position: fixed;
}

button {
  width: 33.33%;
  padding: 0.5rem;
  font-size: 1rem;
}

button.selected {
  background-color: #000;
  color: #fff;
}

ul {
  padding: 3rem 2rem 1rem;
}

li {
  margin-bottom: 1rem;
}

.table-container {
  width: 100%;
  overflow-y: auto;
  padding-top: 52px;
}

td {
  border: 1px solid #000;
  padding: 0.25rem;
}
```

# #End  </details>

+BLOG APP

<details>
  <summary>33. Blog App - Setup App with React-Router-DOM</summary>

# Setup App with React-Router-DOM

<img width="976" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/eb868864-0055-41cd-9413-0c9ac46e7660">
<img width="1215" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f7786ca5-5dee-42e9-94f2-9efba3e50a6a">

# Create React App:

```bs
npx create-react-app .
npx create-react-app blogapp
yarn create react-app blogapp
```

# Install React-Router-DOM:

```bs
npm i react-router-dom -S
npm i react-router-dom@6 -S
```

# Update React-Router-DOM:

```bs
npm update react-router-dom
```

# Run React Server:

```bs
npm start
npm run start
```

### x-dave-gray/blogapp/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/*" element={<App />} />
      </Routes>
    </Router>
  </React.StrictMode>
);

```

### x-dave-gray/blogapp/src/App.js:

```js
import React from "react";

function App() {
  return (
    <div className="App">
      <h1>Blog App</h1>
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>34. Blog App - Routing Components</summary>

# Routing Components

<img width="979" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3103c4bc-e046-4033-ba52-48199bcf3f83">

# http://localhost:3000/

<img width="1215" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7c7a0ba5-f7a0-4b54-a56f-a4014c06165b">

# http://localhost:3000/post

<img width="1215" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9d0c07fb-e0c4-4c7d-aae8-5105cf5eacb0">

# http://localhost:3000/post/1

<img width="1215" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/069d8785-3ae1-4ca2-afbc-4cbf8a81d764">

# http://localhost:3000/about

<img width="1215" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/20cda8b3-0783-49fc-9b22-6c2675458a28">

### x-dave-gray/blogapp/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/*" element={<App />} />
      </Routes>
    </Router>
  </React.StrictMode>
);
```

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  return (
    <div className="App">
      <Header />
      <Nav />
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/post" element={<NewPost />} />
        <Route path="/post/:id" element={<PostPage />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/Header.js:

```js
import React from "react";

const Header = () => {
  return (
    <header>
      <h1>Header</h1>
    </header>
  );
};

export default Header;
```

### x-dave-gray/blogapp/src/Nav.js:

```js
import React from "react";

const Nav = () => {
  return (
    <nav>
      <h1>Nav</h1>
    </nav>
  );
};

export default Nav;
```

### x-dave-gray/blogapp/src/Home.js:

```js
import React from "react";

const Home = () => {
  return (
    <main>
      <h1>Home</h1>
    </main>
  );
};

export default Home;
```

### x-dave-gray/blogapp/src/NewPost.js:

```js
import React from "react";

const NewPost = () => {
  return (
    <main>
      <h1>NewPost</h1>
    </main>
  );
};

export default NewPost;
```

### x-dave-gray/blogapp/src/PostPage.js:

```js
import React from "react";

const PostPage = () => {
  return (
    <main>
      <h1>PostPage</h1>
    </main>
  );
};

export default PostPage;
```

### x-dave-gray/blogapp/src/About.js:

```js
import React from "react";

const About = () => {
  return (
    <main>
      <h1>About</h1>
    </main>
  );
};

export default About;
```

### x-dave-gray/blogapp/src/Missing.js:

```js
import React from "react";

const Missing = () => {
  return (
    <main>
      <h1>Missing</h1>
    </main>
  );
};

export default Missing;
```

### x-dave-gray/blogapp/src/Footer.js:

```js
import React from "react";

const Footer = () => {
  return (
    <footer>
      <h1>Footer</h1>
    </footer>
  );
};

export default Footer;
```

# #End  </details>

<details>
  <summary>35. Blog App - Customising Header Component </summary>

# Customising Header Component

<img width="979" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0667513d-9f8f-4f4c-a520-8a18c0afc7ce">
<img width="1215" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4b87395d-c3de-42a1-bccc-851ea67d71e9">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav />
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/post" element={<NewPost />} />
        <Route path="/post/:id" element={<PostPage />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/Header.js:

```js
import React from "react";

const Header = ({ title }) => {
  return (
    <header className="Header">
      <h1>{title}</h1>
    </header>
  );
};

export default Header;
```

### x-dave-gray/blogapp/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  min-height: 100vh;
  font-family: "Open Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  background-color: #efefef;
}

#root {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.App {
  width: 100%;
  max-width: 800px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 1px solid #333;
  box-shadow: 0px 0px 15px gray;
}

.Header,
.Footer {
  width: 100%;
  background-color: #66d8f5;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.Header h1 {
  font-size: 1.5rem;
}

.Header svg {
  font-size: 2rem;
}

.Footer {
  padding: 0.75rem;
  display: grid;
  place-content: center;
}

.Nav {
  width: 100%;
  background-color: #333;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.searchForm {
  width: 80%;
  padding: 1rem 0 0 0.75rem;
}

.searchForm input[type="text"] {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  outline: none;
}

.searchForm label {
  position: absolute;
  left: -99999px;
}

.Nav ul {
  color: #fff;
  list-style-type: none;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
}

.Nav li {
  padding: 1rem;
}

.Nav li:hover,
.Nav li:focus {
  padding: 1rem;
}

.Nav li a {
  color: #fff;
  text-decoration: none;
}

.Nav li:hover,
.Nav li:focus,
.Nav li:hover a,
.Nav li:focus a {
  background-color: #eee;
  color: #333;
}

.Nav li:hover a,
.Nav li:focus a {
  cursor: pointer;
}

.Home,
.NewPost,
.PostPage,
.About,
.Missing {
  width: 100%;
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
  background-color: #fff;
}

.post {
  margin-top: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid lightgray;
}

.Home .post a {
  text-decoration: none;
}

.Home .post a,
.Home .post a:visited {
  color: #000;
}

.post:first-child {
  margin-top: 0;
}

.post:last-child {
  border-bottom: none;
}

.postDate {
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

.postBody {
  margin: 1rem 0;
}

.newPostForm {
  display: flex;
  flex-direction: column;
}

.newPostForm label {
  margin-top: 1rem;
}

.newPostForm input[type="text"],
.newPostForm textarea {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  margin-right: 0.25rem;
  outline: none;
}

.newPostForm textarea {
  height: 100px;
}

.newPostForm button {
  margin-top: 1rem;
  height: 48px;
  min-width: 48px;
  border-radius: 10px;
  padding: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
}

.Missing h2,
.PostPage h2,
.Missing p,
.PostPage p {
  margin-bottom: 1rem;
}

.PostPage button {
  height: 48px;
  min-width: 48px;
  border-radius: 0.25rem;
  padding: 0.5rem;
  font-size: 1rem;
  background-color: red;
  color: #fff;
  cursor: pointer;
}

.statusMsg {
  margin-top: 2rem;
}

@media only screen and (min-width: 610px) {
  html {
    font-size: 22px;
  }

  .Header h1 {
    font-size: 2rem;
  }

  .Nav {
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
  }

  .Nav ul {
    text-align: right;
  }

  .Nav li:hover,
  .Nav li:focus,
  .Nav li:hover a,
  .Nav li:focus a {
    background-color: #eee;
    color: #333;
  }

  .searchForm {
    width: 50%;
    padding: 0.5rem 0;
  }

  .searchForm input[type="text"] {
    margin-left: 0.5rem;
  }

  .newPostForm textarea {
    height: 300px;
  }
}

@media only screen and (min-width: 992px) {
  .Header svg {
    font-size: 3rem;
  }
}
```

# #End  </details>

<details>
  <summary>36. Blog App - Customizing Nav Component</summary>

# Customizing Nav Component

<img width="978" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7b590a02-0c18-4ac6-813e-5abcc149489e">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ef3a3b91-7c5a-4a2a-a36d-a3d59d380e27">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: "My First Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 2,
      title: "My 2nd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 3,
      title: "My 3rd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 4,
      title: "My Fourth Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
  ]);

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/post" element={<NewPost />} />
        <Route path="/post/:id" element={<PostPage />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/Nav.js:

```js
import React from "react";
import { Link } from "react-router-dom";

const Nav = ({ search, setSearch }) => {
  return (
    <nav className="Nav">
      <form className="searchForm" onSubmit={(e) => e.preventDefault()}>
        <label htmlFor="search">Search Posts</label>
        <input
          id="search"
          type="text"
          placeholder="Search Posts"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </form>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/post">Post</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Nav;
```

### x-dave-gray/blogapp/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  min-height: 100vh;
  font-family: "Open Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  background-color: #efefef;
}

#root {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.App {
  width: 100%;
  max-width: 800px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 1px solid #333;
  box-shadow: 0px 0px 15px gray;
}

.Header,
.Footer {
  width: 100%;
  background-color: #66d8f5;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.Header h1 {
  font-size: 1.5rem;
}

.Header svg {
  font-size: 2rem;
}

.Footer {
  padding: 0.75rem;
  display: grid;
  place-content: center;
}

.Nav {
  width: 100%;
  background-color: #333;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.searchForm {
  width: 80%;
  padding: 1rem 0 0 0.75rem;
}

.searchForm input[type="text"] {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  outline: none;
}

.searchForm label {
  position: absolute;
  left: -99999px;
}

.Nav ul {
  color: #fff;
  list-style-type: none;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
}

.Nav li {
  padding: 1rem;
}

.Nav li:hover,
.Nav li:focus {
  padding: 1rem;
}

.Nav li a {
  color: #fff;
  text-decoration: none;
}

.Nav li:hover,
.Nav li:focus,
.Nav li:hover a,
.Nav li:focus a {
  background-color: #eee;
  color: #333;
}

.Nav li:hover a,
.Nav li:focus a {
  cursor: pointer;
}

.Home,
.NewPost,
.PostPage,
.About,
.Missing {
  width: 100%;
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
  background-color: #fff;
}

.post {
  margin-top: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid lightgray;
}

.Home .post a {
  text-decoration: none;
}

.Home .post a,
.Home .post a:visited {
  color: #000;
}

.post:first-child {
  margin-top: 0;
}

.post:last-child {
  border-bottom: none;
}

.postDate {
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

.postBody {
  margin: 1rem 0;
}

.newPostForm {
  display: flex;
  flex-direction: column;
}

.newPostForm label {
  margin-top: 1rem;
}

.newPostForm input[type="text"],
.newPostForm textarea {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  margin-right: 0.25rem;
  outline: none;
}

.newPostForm textarea {
  height: 100px;
}

.newPostForm button {
  margin-top: 1rem;
  height: 48px;
  min-width: 48px;
  border-radius: 10px;
  padding: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
}

.Missing h2,
.PostPage h2,
.Missing p,
.PostPage p {
  margin-bottom: 1rem;
}

.PostPage button {
  height: 48px;
  min-width: 48px;
  border-radius: 0.25rem;
  padding: 0.5rem;
  font-size: 1rem;
  background-color: red;
  color: #fff;
  cursor: pointer;
}

.statusMsg {
  margin-top: 2rem;
}

@media only screen and (min-width: 610px) {
  html {
    font-size: 22px;
  }

  .Header h1 {
    font-size: 2rem;
  }

  .Nav {
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
  }

  .Nav ul {
    text-align: right;
  }

  .Nav li:hover,
  .Nav li:focus,
  .Nav li:hover a,
  .Nav li:focus a {
    background-color: #eee;
    color: #333;
  }

  .searchForm {
    width: 50%;
    padding: 0.5rem 0;
  }

  .searchForm input[type="text"] {
    margin-left: 0.5rem;
  }

  .newPostForm textarea {
    height: 300px;
  }
}

@media only screen and (min-width: 992px) {
  .Header svg {
    font-size: 3rem;
  }
}

```

# #End  </details>

<details>
  <summary>37. Blog App - Customising Home, Feed and Post Components (Displaying all Posts) </summary>

# Customising Home, Feed and Post Components (Displaying all Posts)

<img width="975" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e859a990-c46a-47f1-af00-30b879c47af7">
<img width="1214" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/253130cb-9958-4bab-9700-5c2ba8181097">
<img width="1214" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4d19cde0-a110-4c82-b66a-b71886886653">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: "My First Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 2,
      title: "My 2nd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 3,
      title: "My 3rd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 4,
      title: "My Fourth Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
  ]);

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={posts} />} />
        <Route exact path="/post" element={<NewPost />} />
        <Route path="/post/:id" element={<PostPage />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/Home.js:

```js
import React from "react";
import Feed from "./Feed";

const Home = ({ posts }) => {
  return (
    <main className="Home">
      {posts.length ? (
        <Feed posts={posts} />
      ) : (
        <p style={{ marginTop: "2rem" }}>No Posts to display.</p>
      )}
    </main>
  );
};

export default Home;
```

### x-dave-gray/blogapp/src/Feed.js:

```js
import React from "react";
import Post from "./Post";

const Feed = ({ posts }) => {
  return (
    <>{posts.map((post) => <Post key={post.id} post={post} />).reverse()}</>
  );
};

export default Feed;
```

### x-dave-gray/blogapp/src/Post.js:

```js
import React from "react";
import { Link } from "react-router-dom";

const Post = ({ post }) => {
  return (
    <article className="post">
      <Link to={`/post/${post.id}`}>
        <h2>{post.title}</h2>
        <p className="postDate">{post.datetime}</p>
      </Link>
      <p>
        {post.body.length <= 25 ? post.body : `${post.body.slice(0, 25)}...`}
      </p>
    </article>
  );
};

export default Post;
```

### x-dave-gray/blogapp/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  min-height: 100vh;
  font-family: "Open Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  background-color: #efefef;
}

#root {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.App {
  width: 100%;
  max-width: 800px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 1px solid #333;
  box-shadow: 0px 0px 15px gray;
}

.Header,
.Footer {
  width: 100%;
  background-color: #66d8f5;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.Header h1 {
  font-size: 1.5rem;
}

.Header svg {
  font-size: 2rem;
}

.Footer {
  padding: 0.75rem;
  display: grid;
  place-content: center;
}

.Nav {
  width: 100%;
  background-color: #333;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.searchForm {
  width: 80%;
  padding: 1rem 0 0 0.75rem;
}

.searchForm input[type="text"] {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  outline: none;
}

.searchForm label {
  position: absolute;
  left: -99999px;
}

.Nav ul {
  color: #fff;
  list-style-type: none;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
}

.Nav li {
  padding: 1rem;
}

.Nav li:hover,
.Nav li:focus {
  padding: 1rem;
}

.Nav li a {
  color: #fff;
  text-decoration: none;
}

.Nav li:hover,
.Nav li:focus,
.Nav li:hover a,
.Nav li:focus a {
  background-color: #eee;
  color: #333;
}

.Nav li:hover a,
.Nav li:focus a {
  cursor: pointer;
}

.Home,
.NewPost,
.PostPage,
.About,
.Missing {
  width: 100%;
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
  background-color: #fff;
}

.post {
  margin-top: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid lightgray;
}

.Home .post a {
  text-decoration: none;
}

.Home .post a,
.Home .post a:visited {
  color: #000;
}

.post:first-child {
  margin-top: 0;
}

.post:last-child {
  border-bottom: none;
}

.postDate {
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

.postBody {
  margin: 1rem 0;
}

.newPostForm {
  display: flex;
  flex-direction: column;
}

.newPostForm label {
  margin-top: 1rem;
}

.newPostForm input[type="text"],
.newPostForm textarea {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  margin-right: 0.25rem;
  outline: none;
}

.newPostForm textarea {
  height: 100px;
}

.newPostForm button {
  margin-top: 1rem;
  height: 48px;
  min-width: 48px;
  border-radius: 10px;
  padding: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
}

.Missing h2,
.PostPage h2,
.Missing p,
.PostPage p {
  margin-bottom: 1rem;
}

.PostPage button {
  height: 48px;
  min-width: 48px;
  border-radius: 0.25rem;
  padding: 0.5rem;
  font-size: 1rem;
  background-color: red;
  color: #fff;
  cursor: pointer;
}

.statusMsg {
  margin-top: 2rem;
}

@media only screen and (min-width: 610px) {
  html {
    font-size: 22px;
  }

  .Header h1 {
    font-size: 2rem;
  }

  .Nav {
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
  }

  .Nav ul {
    text-align: right;
  }

  .Nav li:hover,
  .Nav li:focus,
  .Nav li:hover a,
  .Nav li:focus a {
    background-color: #eee;
    color: #333;
  }

  .searchForm {
    width: 50%;
    padding: 0.5rem 0;
  }

  .searchForm input[type="text"] {
    margin-left: 0.5rem;
  }

  .newPostForm textarea {
    height: 300px;
  }
}

@media only screen and (min-width: 992px) {
  .Header svg {
    font-size: 3rem;
  }
}
```

# #End  </details>

<details>
  <summary>38. Blog App - Customising PostPage Component with useParams Hook (Displaying a single Post)</summary>

# Customising PostPage Component with useParams Hook (Displaying a single Post)

<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/989f28a3-e3b1-48f4-9ca6-3dbd68e3e5d3">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/783046fe-c232-4959-a0ff-dcdbaf420ea2">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: "My First Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 2,
      title: "My 2nd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 3,
      title: "My 3rd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 4,
      title: "My Fourth Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
  ]);

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={posts} />} />
        <Route exact path="/post" element={<NewPost />} />
        <Route path="/post/:id" element={<PostPage posts={posts} />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/PostPage.js:

```js
import React from "react";
import { useParams, Link } from "react-router-dom";

const PostPage = ({ posts }) => {
  const { id } = useParams();
  const post = posts.find((post) => post.id.toString() === id);

  return (
    <main className="PostPage">
      <article className="post">
        {post ? (
          <>
            <h2>{post.title}</h2>
            <p className="postDate">{post.datetime}</p>
            <p className="postBody">{post.body}</p>
          </>
        ) : (
          <>
            <h2>Post Not Found</h2>
            <p>Well, that's disappointing.</p>
            <p>
              <Link to="/">Visit our Home Page</Link>
            </p>
          </>
        )}
      </article>
    </main>
  );
};

export default PostPage;
```

### x-dave-gray/blogapp/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  min-height: 100vh;
  font-family: "Open Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  background-color: #efefef;
}

#root {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.App {
  width: 100%;
  max-width: 800px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 1px solid #333;
  box-shadow: 0px 0px 15px gray;
}

.Header,
.Footer {
  width: 100%;
  background-color: #66d8f5;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.Header h1 {
  font-size: 1.5rem;
}

.Header svg {
  font-size: 2rem;
}

.Footer {
  padding: 0.75rem;
  display: grid;
  place-content: center;
}

.Nav {
  width: 100%;
  background-color: #333;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.searchForm {
  width: 80%;
  padding: 1rem 0 0 0.75rem;
}

.searchForm input[type="text"] {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  outline: none;
}

.searchForm label {
  position: absolute;
  left: -99999px;
}

.Nav ul {
  color: #fff;
  list-style-type: none;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
}

.Nav li {
  padding: 1rem;
}

.Nav li:hover,
.Nav li:focus {
  padding: 1rem;
}

.Nav li a {
  color: #fff;
  text-decoration: none;
}

.Nav li:hover,
.Nav li:focus,
.Nav li:hover a,
.Nav li:focus a {
  background-color: #eee;
  color: #333;
}

.Nav li:hover a,
.Nav li:focus a {
  cursor: pointer;
}

.Home,
.NewPost,
.PostPage,
.About,
.Missing {
  width: 100%;
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
  background-color: #fff;
}

.post {
  margin-top: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid lightgray;
}

.Home .post a {
  text-decoration: none;
}

.Home .post a,
.Home .post a:visited {
  color: #000;
}

.post:first-child {
  margin-top: 0;
}

.post:last-child {
  border-bottom: none;
}

.postDate {
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

.postBody {
  margin: 1rem 0;
}

.newPostForm {
  display: flex;
  flex-direction: column;
}

.newPostForm label {
  margin-top: 1rem;
}

.newPostForm input[type="text"],
.newPostForm textarea {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  margin-right: 0.25rem;
  outline: none;
}

.newPostForm textarea {
  height: 100px;
}

.newPostForm button {
  margin-top: 1rem;
  height: 48px;
  min-width: 48px;
  border-radius: 10px;
  padding: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
}

.Missing h2,
.PostPage h2,
.Missing p,
.PostPage p {
  margin-bottom: 1rem;
}

.PostPage button {
  height: 48px;
  min-width: 48px;
  border-radius: 0.25rem;
  padding: 0.5rem;
  font-size: 1rem;
  background-color: red;
  color: #fff;
  cursor: pointer;
}

.statusMsg {
  margin-top: 2rem;
}

@media only screen and (min-width: 610px) {
  html {
    font-size: 22px;
  }

  .Header h1 {
    font-size: 2rem;
  }

  .Nav {
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
  }

  .Nav ul {
    text-align: right;
  }

  .Nav li:hover,
  .Nav li:focus,
  .Nav li:hover a,
  .Nav li:focus a {
    background-color: #eee;
    color: #333;
  }

  .searchForm {
    width: 50%;
    padding: 0.5rem 0;
  }

  .searchForm input[type="text"] {
    margin-left: 0.5rem;
  }

  .newPostForm textarea {
    height: 300px;
  }
}

@media only screen and (min-width: 992px) {
  .Header svg {
    font-size: 3rem;
  }
}
```

# #End  </details>

<details>
  <summary>39. Blog App - Deleting a Blog and useNavigate()</summary>

#  Deleting a Blog and useNavigate()

<img width="976" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/452133db-2300-487d-bada-20b47cdbf9c6">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/eaa26d79-8349-445c-93c7-fc29a1b4ee0f">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2467e41c-6615-4d1a-95fa-6435396b2fc8">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: "My First Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 2,
      title: "My 2nd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 3,
      title: "My 3rd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 4,
      title: "My Fourth Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
  ]);

  const navigate = useNavigate();

  const handleDelete = (id) => {
    const postList = posts.filter((post) => post.id !== id);
    setPosts(postList);
    navigate("/");
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={posts} />} />
        <Route exact path="/post" element={<NewPost />} />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/PostPage.js:

```js
import React from "react";
import { useParams, Link } from "react-router-dom";

const PostPage = ({ posts, handleDelete }) => {
  const { id } = useParams();
  const post = posts.find((post) => post.id.toString() === id);

  return (
    <main className="PostPage">
      <article className="post">
        {post ? (
          <>
            <h2>{post.title}</h2>
            <p className="postDate">{post.datetime}</p>
            <p className="postBody">{post.body}</p>
            <button onClick={() => handleDelete(post.id)}>Delete Post</button>
          </>
        ) : (
          <>
            <h2>Post Not Found</h2>
            <p>Well, that's disappointing.</p>
            <p>
              <Link to="/">Visit our Home Page</Link>
            </p>
          </>
        )}
      </article>
    </main>
  );
};

export default PostPage;
```

### x-dave-gray/blogapp/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  min-height: 100vh;
  font-family: "Open Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  background-color: #efefef;
}

#root {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.App {
  width: 100%;
  max-width: 800px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 1px solid #333;
  box-shadow: 0px 0px 15px gray;
}

.Header,
.Footer {
  width: 100%;
  background-color: #66d8f5;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.Header h1 {
  font-size: 1.5rem;
}

.Header svg {
  font-size: 2rem;
}

.Footer {
  padding: 0.75rem;
  display: grid;
  place-content: center;
}

.Nav {
  width: 100%;
  background-color: #333;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.searchForm {
  width: 80%;
  padding: 1rem 0 0 0.75rem;
}

.searchForm input[type="text"] {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  outline: none;
}

.searchForm label {
  position: absolute;
  left: -99999px;
}

.Nav ul {
  color: #fff;
  list-style-type: none;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
}

.Nav li {
  padding: 1rem;
}

.Nav li:hover,
.Nav li:focus {
  padding: 1rem;
}

.Nav li a {
  color: #fff;
  text-decoration: none;
}

.Nav li:hover,
.Nav li:focus,
.Nav li:hover a,
.Nav li:focus a {
  background-color: #eee;
  color: #333;
}

.Nav li:hover a,
.Nav li:focus a {
  cursor: pointer;
}

.Home,
.NewPost,
.PostPage,
.About,
.Missing {
  width: 100%;
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
  background-color: #fff;
}

.post {
  margin-top: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid lightgray;
}

.Home .post a {
  text-decoration: none;
}

.Home .post a,
.Home .post a:visited {
  color: #000;
}

.post:first-child {
  margin-top: 0;
}

.post:last-child {
  border-bottom: none;
}

.postDate {
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

.postBody {
  margin: 1rem 0;
}

.newPostForm {
  display: flex;
  flex-direction: column;
}

.newPostForm label {
  margin-top: 1rem;
}

.newPostForm input[type="text"],
.newPostForm textarea {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  margin-right: 0.25rem;
  outline: none;
}

.newPostForm textarea {
  height: 100px;
}

.newPostForm button {
  margin-top: 1rem;
  height: 48px;
  min-width: 48px;
  border-radius: 10px;
  padding: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
}

.Missing h2,
.PostPage h2,
.Missing p,
.PostPage p {
  margin-bottom: 1rem;
}

.PostPage button {
  height: 48px;
  min-width: 48px;
  border-radius: 0.25rem;
  padding: 0.5rem;
  font-size: 1rem;
  background-color: red;
  color: #fff;
  cursor: pointer;
}

.statusMsg {
  margin-top: 2rem;
}

@media only screen and (min-width: 610px) {
  html {
    font-size: 22px;
  }

  .Header h1 {
    font-size: 2rem;
  }

  .Nav {
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
  }

  .Nav ul {
    text-align: right;
  }

  .Nav li:hover,
  .Nav li:focus,
  .Nav li:hover a,
  .Nav li:focus a {
    background-color: #eee;
    color: #333;
  }

  .searchForm {
    width: 50%;
    padding: 0.5rem 0;
  }

  .searchForm input[type="text"] {
    margin-left: 0.5rem;
  }

  .newPostForm textarea {
    height: 300px;
  }
}

@media only screen and (min-width: 992px) {
  .Header svg {
    font-size: 3rem;
  }
}
```

# #End  </details>

<details>
  <summary>40. Blog App - Customise NewPost Component</summary>

# Customise NewPost Component

<img width="976" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5614fde7-bb18-4fab-9e0a-9bb06af20bcb">
<img width="1215" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ab80483d-fe05-4a06-b108-038f51d3cd70">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: "My First Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 2,
      title: "My 2nd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 3,
      title: "My 3rd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 4,
      title: "My Fourth Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
  ]);

  const navigate = useNavigate();

  const handleDelete = (id) => {
    const postList = posts.filter((post) => post.id !== id);
    setPosts(postList);
    navigate("/");
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={posts} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/NewPost.js:

```js
import React from "react";

const NewPost = ({ postTitle, setPostTitle, postBody, setPostBody }) => {
  return (
    <main className="NewPost">
      <h2>NewPost</h2>
      <form className="newPostForm">
        <label htmlFor="postTitle">Title:</label>
        <input
          type="text"
          id="postTitle"
          value={postTitle}
          onChange={(e) => setPostTitle(e.target.value)}
          required
        />
        <label htmlFor="postBody">Post:</label>
        <textarea
          id="postBody"
          value={postBody}
          onChange={(e) => setPostBody(e.target.value)}
          // cols="10"
          // rows="30"
          required
        />
        <button type="submit">Submit</button>
      </form>
    </main>
  );
};

export default NewPost;
```

```css
@import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  min-height: 100vh;
  font-family: "Open Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  background-color: #efefef;
}

#root {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.App {
  width: 100%;
  max-width: 800px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 1px solid #333;
  box-shadow: 0px 0px 15px gray;
}

.Header,
.Footer {
  width: 100%;
  background-color: #66d8f5;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.Header h1 {
  font-size: 1.5rem;
}

.Header svg {
  font-size: 2rem;
}

.Footer {
  padding: 0.75rem;
  display: grid;
  place-content: center;
}

.Nav {
  width: 100%;
  background-color: #333;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.searchForm {
  width: 80%;
  padding: 1rem 0 0 0.75rem;
}

.searchForm input[type="text"] {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  outline: none;
}

.searchForm label {
  position: absolute;
  left: -99999px;
}

.Nav ul {
  color: #fff;
  list-style-type: none;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
}

.Nav li {
  padding: 1rem;
}

.Nav li:hover,
.Nav li:focus {
  padding: 1rem;
}

.Nav li a {
  color: #fff;
  text-decoration: none;
}

.Nav li:hover,
.Nav li:focus,
.Nav li:hover a,
.Nav li:focus a {
  background-color: #eee;
  color: #333;
}

.Nav li:hover a,
.Nav li:focus a {
  cursor: pointer;
}

.Home,
.NewPost,
.PostPage,
.About,
.Missing {
  width: 100%;
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
  background-color: #fff;
}

.post {
  margin-top: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid lightgray;
}

.Home .post a {
  text-decoration: none;
}

.Home .post a,
.Home .post a:visited {
  color: #000;
}

.post:first-child {
  margin-top: 0;
}

.post:last-child {
  border-bottom: none;
}

.postDate {
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

.postBody {
  margin: 1rem 0;
}

.newPostForm {
  display: flex;
  flex-direction: column;
}

.newPostForm label {
  margin-top: 1rem;
}

.newPostForm input[type="text"],
.newPostForm textarea {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  margin-right: 0.25rem;
  outline: none;
}

.newPostForm textarea {
  height: 100px;
}

.newPostForm button {
  margin-top: 1rem;
  height: 48px;
  min-width: 48px;
  border-radius: 10px;
  padding: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
}

.Missing h2,
.PostPage h2,
.Missing p,
.PostPage p {
  margin-bottom: 1rem;
}

.PostPage button {
  height: 48px;
  min-width: 48px;
  border-radius: 0.25rem;
  padding: 0.5rem;
  font-size: 1rem;
  background-color: red;
  color: #fff;
  cursor: pointer;
}

.statusMsg {
  margin-top: 2rem;
}

@media only screen and (min-width: 610px) {
  html {
    font-size: 22px;
  }

  .Header h1 {
    font-size: 2rem;
  }

  .Nav {
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
  }

  .Nav ul {
    text-align: right;
  }

  .Nav li:hover,
  .Nav li:focus,
  .Nav li:hover a,
  .Nav li:focus a {
    background-color: #eee;
    color: #333;
  }

  .searchForm {
    width: 50%;
    padding: 0.5rem 0;
  }

  .searchForm input[type="text"] {
    margin-left: 0.5rem;
  }

  .newPostForm textarea {
    height: 300px;
  }
}

@media only screen and (min-width: 992px) {
  .Header svg {
    font-size: 3rem;
  }
}
```

# #End  </details>

<details>
  <summary>41. Blog App - Adding New Post (handleSubmit) Functionality </summary>

# Blog App - Adding New Post (handleSubmit) Functionality

<img width="974" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ec6e53c1-4569-46af-a3c8-86fc6d0b3424">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1c357e57-2ec1-4ab4-9cc7-3a150c6e9581">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c503845c-bb3a-41e5-81bd-29f31ac44d80">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/563a2b4a-30e3-4e02-ada3-3afd81841f18">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/866228f4-9f43-408a-b7c8-c186e2b1b720">

# Install Date-Functions Module:

```bs
npm i date-fns -S
```

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: "My First Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 2,
      title: "My 2nd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 3,
      title: "My 3rd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 4,
      title: "My Fourth Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
  ]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const navigate = useNavigate();

  const handleDelete = (id) => {
    const postList = posts.filter((post) => post.id !== id);
    setPosts(postList);
    navigate("/");
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    const allPosts = [...posts, newPost];
    setPosts(allPosts);
    setPostTitle("");
    setPostBody("");
    navigate("/");
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={posts} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/NewPost.js:

```js
import React from "react";

const NewPost = ({
  handleSubmit,
  postTitle,
  setPostTitle,
  postBody,
  setPostBody,
}) => {
  return (
    <main className="NewPost">
      <h2>NewPost</h2>
      <form className="newPostForm" onSubmit={handleSubmit}>
        <label htmlFor="postTitle">Title:</label>
        <input
          type="text"
          id="postTitle"
          value={postTitle}
          onChange={(e) => setPostTitle(e.target.value)}
          required
        />
        <label htmlFor="postBody">Post:</label>
        <textarea
          id="postBody"
          value={postBody}
          onChange={(e) => setPostBody(e.target.value)}
          // cols="10"
          // rows="30"
          required
        />
        <button type="submit">Submit</button>
      </form>
    </main>
  );
};

export default NewPost;
```

# #End  </details>

<details>
  <summary>42. Blog App - Adding Search Functionality with useEffect</summary>

# Adding Search Functionality with useEffect

<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1cbba03e-ec58-4b43-80b3-27277e8ca89b">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/04b75d28-dfea-4230-8168-e3327da5e5b0">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/008f8191-19f8-46cf-9d54-e639c88bc773">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: "My First Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 2,
      title: "My 2nd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 3,
      title: "My 3rd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 4,
      title: "My Fourth Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
  ]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    const allPosts = [...posts, newPost];
    setPosts(allPosts);
    setPostTitle("");
    setPostBody("");
    navigate("/");
  };

  const handleDelete = (id) => {
    const postList = posts.filter((post) => post.id !== id);
    setPosts(postList);
    navigate("/");
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={searchResults} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>43. Blog App - Customise Page Not Found (Missing) Component</summary>

# Customise Page Not Found (Missing) Component

<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1e7c825e-fa92-416f-b07f-98265e0841b8">
<img width="1215" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e057f8f8-abfb-484f-9353-d19aacb7eacb">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: "My First Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 2,
      title: "My 2nd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 3,
      title: "My 3rd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 4,
      title: "My Fourth Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
  ]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    const allPosts = [...posts, newPost];
    setPosts(allPosts);
    setPostTitle("");
    setPostBody("");
    navigate("/");
  };

  const handleDelete = (id) => {
    const postList = posts.filter((post) => post.id !== id);
    setPosts(postList);
    navigate("/");
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={searchResults} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/Missing.js:

```js
import React from "react";
import { Link } from "react-router-dom";

const Missing = () => {
  return (
    <main className="Missing">
      <h2>Page Not Found</h2>
      <p>Well, that's disappointing.</p>
      <p>
        <Link to="/">Visit Our Homepage</Link>
      </p>
    </main>
  );
};

export default Missing;
```

# #End  </details>

<details>
  <summary>44. Blog App - Customise Footer Component</summary>

# Customise Footer Component

<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1e00db3a-c6b7-4898-acde-0f3ec4223711">
<img width="1215" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5fe9654f-624c-43c4-876c-2ed5c0c1fd7c">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: "My First Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 2,
      title: "My 2nd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 3,
      title: "My 3rd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 4,
      title: "My Fourth Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
  ]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    const allPosts = [...posts, newPost];
    setPosts(allPosts);
    setPostTitle("");
    setPostBody("");
    navigate("/");
  };

  const handleDelete = (id) => {
    const postList = posts.filter((post) => post.id !== id);
    setPosts(postList);
    navigate("/");
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={searchResults} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/Footer.js:

```js
import React from "react";

const Footer = () => {
  const today = new Date();

  return (
    <footer className="Footer">
      <p>Copyright &copy; {today.getFullYear()}</p>
    </footer>
  );
};

export default Footer;
```

# #End  </details>

<details>
  <summary>45. Blog App - Customise About Component</summary>

# Customise About Component

<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/603a5c37-6bd1-470b-8611-4209116f9a4d">
<img width="1213" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/92960296-8bff-4fdd-bfd9-a63b52bf3a90">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [posts, setPosts] = useState([
    {
      id: 1,
      title: "My First Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 2,
      title: "My 2nd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 3,
      title: "My 3rd Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
    {
      id: 4,
      title: "My Fourth Post",
      datetime: "July 01, 2021 11:17:36 AM",
      body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!",
    },
  ]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    const allPosts = [...posts, newPost];
    setPosts(allPosts);
    setPostTitle("");
    setPostBody("");
    navigate("/");
  };

  const handleDelete = (id) => {
    const postList = posts.filter((post) => post.id !== id);
    setPosts(postList);
    navigate("/");
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={searchResults} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/About.js:

```js
import React from "react";

const About = () => {
  return (
    <main className="About">
      <h2>About</h2>
      <p style={{ marginTop: "1rem" }}>
        This is a Blog app project in Learn React App Series.
      </p>
    </main>
  );
};

export default About;
```

# #End  </details>

<details>
  <summary>46. Blog App - Customise CSS Width and Height Properties</summary>

# Customise CSS Width and Height Properties

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4d2c9bc6-506a-4823-ad2f-0db7d95d1c58">
<img width="1214" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6a2af6da-7794-40e4-9037-f944d1455bce">

### x-dave-gray/blogapp/src/index.css:

```bs
body {
  min-height: 100vh;
  font-family: "Open Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  background-color: #efefef;
}

#root {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.App {
  width: 100%;
  max-width: 800px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 1px solid #333;
  box-shadow: 0px 0px 15px gray;
}
```

```css
@import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  min-height: 100vh;
  font-family: "Open Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  background-color: #efefef;
}

#root {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.App {
  width: 100%;
  max-width: 800px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 1px solid #333;
  box-shadow: 0px 0px 15px gray;
}

.Header,
.Footer {
  width: 100%;
  background-color: #66d8f5;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.Header h1 {
  font-size: 1.5rem;
}

.Header svg {
  font-size: 2rem;
}

.Footer {
  padding: 0.75rem;
  display: grid;
  place-content: center;
}

.Nav {
  width: 100%;
  background-color: #333;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.searchForm {
  width: 80%;
  padding: 1rem 0 0 0.75rem;
}

.searchForm input[type="text"] {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  outline: none;
}

.searchForm label {
  position: absolute;
  left: -99999px;
}

.Nav ul {
  color: #fff;
  list-style-type: none;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
}

.Nav li {
  padding: 1rem;
}

.Nav li:hover,
.Nav li:focus {
  padding: 1rem;
}

.Nav li a {
  color: #fff;
  text-decoration: none;
}

.Nav li:hover,
.Nav li:focus,
.Nav li:hover a,
.Nav li:focus a {
  background-color: #eee;
  color: #333;
}

.Nav li:hover a,
.Nav li:focus a {
  cursor: pointer;
}

.Home,
.NewPost,
.PostPage,
.About,
.Missing {
  width: 100%;
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
  background-color: #fff;
}

.post {
  margin-top: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid lightgray;
}

.Home .post a {
  text-decoration: none;
}

.Home .post a,
.Home .post a:visited {
  color: #000;
}

.post:first-child {
  margin-top: 0;
}

.post:last-child {
  border-bottom: none;
}

.postDate {
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

.postBody {
  margin: 1rem 0;
}

.newPostForm {
  display: flex;
  flex-direction: column;
}

.newPostForm label {
  margin-top: 1rem;
}

.newPostForm input[type="text"],
.newPostForm textarea {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  margin-right: 0.25rem;
  outline: none;
}

.newPostForm textarea {
  height: 100px;
}

.newPostForm button {
  margin-top: 1rem;
  height: 48px;
  min-width: 48px;
  border-radius: 10px;
  padding: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
}

.Missing h2,
.PostPage h2,
.Missing p,
.PostPage p {
  margin-bottom: 1rem;
}

.PostPage button {
  height: 48px;
  min-width: 48px;
  border-radius: 0.25rem;
  padding: 0.5rem;
  font-size: 1rem;
  background-color: red;
  color: #fff;
  cursor: pointer;
}

.statusMsg {
  margin-top: 2rem;
}

@media only screen and (min-width: 610px) {
  html {
    font-size: 22px;
  }

  .Header h1 {
    font-size: 2rem;
  }

  .Nav {
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
  }

  .Nav ul {
    text-align: right;
  }

  .Nav li:hover,
  .Nav li:focus,
  .Nav li:hover a,
  .Nav li:focus a {
    background-color: #eee;
    color: #333;
  }

  .searchForm {
    width: 50%;
    padding: 0.5rem 0;
  }

  .searchForm input[type="text"] {
    margin-left: 0.5rem;
  }

  .newPostForm textarea {
    height: 300px;
  }
}

@media only screen and (min-width: 992px) {
  .Header svg {
    font-size: 3rem;
  }
}
```

# #End  </details>

+BLOG APP WITH JSON SERVER & AXIOS

<details>
  <summary>47. Blog App - Setup data/db.json file for JSON Server and Axios</summary>

# Setup data/db.json file for JSON Server and Axios

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c6033862-3116-47c4-a67d-393c6f61208d">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3a6f5086-0e8a-4d98-9d69-b5d6d1265432">
<img width="1106" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/74aab502-53fa-47a0-b7da-5519b7f369a9">

# Install Axios:

```bs
npm i axios -S
```

# Install and start JSON Server:

```bs
npm i json-server
json-server -p 3500 --watch data/db.json
```

```bs
npx json-server -p 3500 -w data/db.json
```

### x-dave-gray/blogapp/data/db.json:

```json
{
  "posts": [
    {
      "id": 1,
      "title": "My First Post",
      "datetime": "July 01, 2021 11:17:36 AM",
      "body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!"
    },
    {
      "id": 2,
      "title": "My 2nd Post",
      "datetime": "July 01, 2021 11:17:36 AM",
      "body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!"
    },
    {
      "id": 3,
      "title": "My 3rd Post",
      "datetime": "July 01, 2021 11:17:36 AM",
      "body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!"
    },
    {
      "id": 4,
      "title": "My Fourth Post",
      "datetime": "July 01, 2021 11:17:36 AM",
      "body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis consequatur expedita, assumenda similique non optio! Modi nesciunt excepturi corrupti atque blanditiis quo nobis, non optio quae possimus illum exercitationem ipsa!"
    }
  ]
}
```

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";

function App() {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    const allPosts = [...posts, newPost];
    setPosts(allPosts);
    setPostTitle("");
    setPostBody("");
    navigate("/");
  };

  const handleDelete = (id) => {
    const postList = posts.filter((post) => post.id !== id);
    setPosts(postList);
    navigate("/");
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={searchResults} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>48. Blog App - Setting Base URL for Axios</summary>

# Setting Base URL for Axios

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2f8f2a8b-171f-479a-8756-0f1717bf72bd">

### x-dave-gray/blogapp/src/api/posts.js:

```js
import axios from "axios";

export default axios.create({ baseURL: "http://localhost:3500" });
```

# #End  </details>

<details>
  <summary>49. Blog App - Fetch Data with Axios</summary>

# Fetch Data with Axios

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e3737711-757f-4c4d-bb8a-6a49e8ee4ab7">
<img width="1106" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e792aa73-1d65-4fa9-93b1-343c2453db67">

### x-dave-gray/blogapp/src/App.js:

```bs
useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await api.get("/posts");
        setPosts(response.data);
        // if (response && response.data) {
        //   setPosts(response.data);
        // }
      } catch (err) {
        if (err.response) {
          // Got Data Error response
          console.log(err.response.data.message);
          console.log(err.response.data);
          console.log(err.response.status);
          console.log(err.response.headers);
        } else {
          //Got No Data Error response, if (err.code === 404)
          console.log(`Error: ${err.message}`);
        }
      }
    };

    fetchPosts();
  }, []);
```

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import api from "./api/posts";

function App() {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await api.get("/posts");
        setPosts(response.data);
        // if (response && response.data) {
        //   setPosts(response.data);
        // }
      } catch (err) {
        if (err.response) {
          // Got Data Error response
          console.log(err.response.data.message);
          console.log(err.response.data);
          console.log(err.response.status);
          console.log(err.response.headers);
        } else {
          //Got No Data Error response, if (err.code === 404)
          console.log(`Error: ${err.message}`);
        }
      }
    };

    fetchPosts();
  }, []);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    const allPosts = [...posts, newPost];
    setPosts(allPosts);
    setPostTitle("");
    setPostBody("");
    navigate("/");
  };

  const handleDelete = (id) => {
    const postList = posts.filter((post) => post.id !== id);
    setPosts(postList);
    navigate("/");
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={searchResults} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>50. Blog App - Post/Create Data with Axios</summary>

# Post/Create Data with Axios

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/24f42308-5bd1-4146-9e8f-be910a5eec60">
<img width="1106" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/43c47a2b-d019-40f5-bfe5-fff6f5941466">
<img width="1106" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2818fb71-2202-4957-8767-c99fbfd9ea2d">
<img width="1105" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/69c26b00-3093-47b3-9e5b-c7d1671ddf9d">

### x-dave-gray/blogapp/src/App.js:

```bs
const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };
```

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import api from "./api/posts";

function App() {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await api.get("/posts");
        setPosts(response.data);
        // if (response && response.data) {
        //   setPosts(response.data);
        // }
      } catch (err) {
        if (err.response) {
          // Got Data Error response
          console.log(err.response.data.message);
          console.log(err.response.data);
          console.log(err.response.status);
          console.log(err.response.headers);
        } else {
          //Got No Data Error response, if (err.code === 404)
          console.log(`Error: ${err.message}`);
        }
      }
    };

    fetchPosts();
  }, []);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = (id) => {
    const postList = posts.filter((post) => post.id !== id);
    setPosts(postList);
    navigate("/");
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={searchResults} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>51. Blog App - Delete Data with Axios</summary>

# Delete Data with Axios

<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/40cd3dbd-40cb-4225-a03a-71e005a9738f">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d53176fd-40be-47c9-ad68-6815c751fc6e">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/17d0785b-c4e8-47af-92a1-1895d32b82a1">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ab8feb90-693d-40e7-ad71-5d9103946b13">
<img width="1107" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5c7cbfb9-9962-4e53-8984-96b61540f803">

### x-dave-gray/blogapp/src/App.js:

```bs
const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };
```

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import api from "./api/posts";

function App() {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await api.get("/posts");
        setPosts(response.data);
        // if (response && response.data) {
        //   setPosts(response.data);
        // }
      } catch (err) {
        if (err.response) {
          // Got Data Error response
          console.log(err.response.data.message);
          console.log(err.response.data);
          console.log(err.response.status);
          console.log(err.response.headers);
        } else {
          //Got No Data Error response, if (err.code === 404)
          console.log(`Error: ${err.message}`);
        }
      }
    };

    fetchPosts();
  }, []);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={searchResults} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>52. Blog App - Update/Edit Post with Axios</summary>

# Update/Edit Post with Axios

<img width="971" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c66b0892-3d93-43f0-905d-09705d462412">
<img width="1105" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f37240e0-43ea-4724-8b3f-a7b06fc73734">
<img width="1105" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f5e7a2f6-b464-4fe4-a829-1add12b9f01f">
<img width="1105" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e8b02b87-da55-4fb9-a39c-4921878d81c0">
<img width="1105" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/39dd736b-3aa9-46cf-a641-7d8cf16237cc">
<img width="1105" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8c3060e3-8e52-4fa4-b0b7-b9de2c957539">

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import api from "./api/posts";
import EditPost from "./EditPost";

function App() {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const [editTitle, setEditTitle] = useState("");
  const [editBody, setEditBody] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await api.get("/posts");
        setPosts(response.data);
        // if (response && response.data) {
        //   setPosts(response.data);
        // }
      } catch (err) {
        if (err.response) {
          // Got Data Error response
          console.log(err.response.data.message);
          console.log(err.response.data);
          console.log(err.response.status);
          console.log(err.response.headers);
        } else {
          //Got No Data Error response, if (err.code === 404)
          console.log(`Error: ${err.message}`);
        }
      }
    };

    fetchPosts();
  }, []);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleEdit = async (id) => {
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const updatedPost = { id, title: editTitle, datetime, body: editBody };
    try {
      const response = await api.put(`/posts/${id}`, updatedPost);
      setPosts(
        posts.map((post) => (post.id === id ? { ...response.data } : post))
      );
      setEditTitle("");
      setEditBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={searchResults} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/edit/:id"
          element={
            <EditPost
              posts={posts}
              handleEdit={handleEdit}
              editTitle={editTitle}
              setEditTitle={setEditTitle}
              editBody={editBody}
              setEditBody={setEditBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/EditPost.js:

```js
import React, { useEffect } from "react";
import { useParams, Link } from "react-router-dom";

const EditPost = ({
  posts,
  handleEdit,
  editBody,
  setEditBody,
  editTitle,
  setEditTitle,
}) => {
  const { id } = useParams();
  const post = posts.find((post) => post.id.toString() === id);

  useEffect(() => {
    if (post) {
      setEditTitle(post.title);
      setEditBody(post.body);
    }
  }, [post, setEditTitle, setEditBody]);

  return (
    <main className="NewPost">
      {editTitle ? (
        <>
          <h2>EditPost</h2>
          <form className="newPostForm" onSubmit={(e) => e.preventDefault()}>
            <label htmlFor="postTitle">Title:</label>
            <input
              type="text"
              id="postTitle"
              value={editTitle}
              onChange={(e) => setEditTitle(e.target.value)}
              required
            />
            <label htmlFor="postBody">Post:</label>
            <textarea
              id="postBody"
              value={editBody}
              onChange={(e) => setEditBody(e.target.value)}
              // cols="10"
              // rows="30"
              required
            />
            <button type="submit" onClick={() => handleEdit(post.id)}>
              Submit
            </button>
          </form>
        </>
      ) : (
        <>
          <h2>Post Not Found</h2>
          <p>Well, that's disappointing.</p>
          <p>
            <Link to="/">Visit our Homepage</Link>
          </p>
        </>
      )}
    </main>
  );
};

export default EditPost;
```

### x-dave-gray/blogapp/src/PostPage.js:

```js
import React from "react";
import { useParams, Link } from "react-router-dom";

const PostPage = ({ posts, handleDelete }) => {
  const { id } = useParams();
  const post = posts.find((post) => post.id.toString() === id);

  return (
    <main className="PostPage">
      <article className="post">
        {post ? (
          <>
            <h2>{post.title}</h2>
            <p className="postDate">{post.datetime}</p>
            <p className="postBody">{post.body}</p>
            <Link to={`/edit/${post.id}`}>
              <button className="editButton">Edit Post</button>
            </Link>
            <button
              className="deleteButton"
              onClick={() => handleDelete(post.id)}
            >
              Delete Post
            </button>
          </>
        ) : (
          <>
            <h2>Post Not Found</h2>
            <p>Well, that's disappointing.</p>
            <p>
              <Link to="/">Visit our Home Page</Link>
            </p>
          </>
        )}
      </article>
    </main>
  );
};

export default PostPage;
```

### x-dave-gray/blogapp/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  min-height: 100vh;
  font-family: "Open Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  background-color: #efefef;
}

#root {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.App {
  width: 100%;
  max-width: 800px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 1px solid #333;
  box-shadow: 0px 0px 15px gray;
}

.Header,
.Footer {
  width: 100%;
  background-color: #66d8f5;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.Header h1 {
  font-size: 1.5rem;
}

.Header svg {
  font-size: 2rem;
}

.Footer {
  padding: 0.75rem;
  display: grid;
  place-content: center;
}

.Nav {
  width: 100%;
  background-color: #333;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.searchForm {
  width: 80%;
  padding: 1rem 0 0 0.75rem;
}

.searchForm input[type="text"] {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  outline: none;
}

.searchForm label {
  position: absolute;
  left: -99999px;
}

.Nav ul {
  color: #fff;
  list-style-type: none;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
}

.Nav li {
  padding: 1rem;
}

.Nav li:hover,
.Nav li:focus {
  padding: 1rem;
}

.Nav li a {
  color: #fff;
  text-decoration: none;
}

.Nav li:hover,
.Nav li:focus,
.Nav li:hover a,
.Nav li:focus a {
  background-color: #eee;
  color: #333;
}

.Nav li:hover a,
.Nav li:focus a {
  cursor: pointer;
}

.Home,
.NewPost,
.PostPage,
.About,
.Missing {
  width: 100%;
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
  background-color: #fff;
}

.post {
  margin-top: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid lightgray;
}

.Home .post a {
  text-decoration: none;
}

.Home .post a,
.Home .post a:visited {
  color: #000;
}

.post:first-child {
  margin-top: 0;
}

.post:last-child {
  border-bottom: none;
}

.postDate {
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

.postBody {
  margin: 1rem 0;
}

.newPostForm {
  display: flex;
  flex-direction: column;
}

.newPostForm label {
  margin-top: 1rem;
}

.newPostForm input[type="text"],
.newPostForm textarea {
  font-family: "Open Sans", sans-serif;
  width: 100%;
  min-height: 48px;
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.25rem;
  margin-right: 0.25rem;
  outline: none;
}

.newPostForm textarea {
  height: 100px;
}

.newPostForm button {
  margin-top: 1rem;
  height: 48px;
  min-width: 48px;
  border-radius: 10px;
  padding: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
}

.Missing p,
.PostPage p,
.NewPost p {
  margin-top: 1rem;
}

.PostPage button {
  height: 48px;
  min-width: 48px;
  border-radius: 0.25rem;
  padding: 0.5rem;
  margin-right: 0.5rem;
  font-size: 1rem;
  color: #fff;
  cursor: pointer;
}

.deleteButton {
  background-color: red;
}

.editButton {
  background-color: #333;
}

.statusMsg {
  margin-top: 2rem;
}

@media only screen and (min-width: 610px) {
  html {
    font-size: 22px;
  }

  .Header h1 {
    font-size: 2rem;
  }

  .Nav {
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
  }

  .Nav ul {
    text-align: right;
  }

  .Nav li:hover,
  .Nav li:focus,
  .Nav li:hover a,
  .Nav li:focus a {
    background-color: #eee;
    color: #333;
  }

  .searchForm {
    width: 50%;
    padding: 0.5rem 0;
  }

  .searchForm input[type="text"] {
    margin-left: 0.5rem;
  }

  .newPostForm textarea {
    height: 300px;
  }
}

@media only screen and (min-width: 992px) {
  .Header svg {
    font-size: 3rem;
  }
}
```

# #End  </details>

+BLOG APP WITH CUSTOM HOOKS

<details>
  <summary>53. Blog App - Create useWindowSize Custom Hook</summary>

# Create useWindowSize Custom Hook

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5725f4a5-e949-4df9-9f71-2cfbe3d9063f">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b04c3380-2f74-4846-b48e-15b4e61fbbe4">
<img width="1272" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/855bb9b4-8f10-4d10-8bd8-6f868d437cf7">
<img width="1272" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3be88ba0-0211-45a8-9e82-59eeef2285a5">
<img width="1272" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5160161b-d1ca-45a6-b2d2-5fdb25719caf">

# Install react-icons:

```bs
npm i react-icons -S
```

### x-dave-gray/blogapp/src/hooks/useWindowSize.js:

```js
import React, { useState, useEffect } from "react";

const useWindowSize = () => {
  const [windowSize, setWindowSize] = useState({
    width: undefined,
    height: undefined,
  });

  useEffect(() => {
    const handleResize = () => {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    };

    handleResize();

    window.addEventListener("resize", handleResize);

    const cleanUp = () => {
      //console.log("runs if a useEffect dep changes");
      window.removeEventListener("resize", handleResize);
    };
    return cleanUp;

    // () => window.removeEventListener("resize", handleResize);
  }, []);
  return windowSize;
};

export default useWindowSize;
```

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import api from "./api/posts";
import EditPost from "./EditPost";
import useWindowSize from "./hooks/useWindowSize";

function App() {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const [editTitle, setEditTitle] = useState("");
  const [editBody, setEditBody] = useState("");
  const navigate = useNavigate();
  const { width } = useWindowSize();

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await api.get("/posts");
        setPosts(response.data);
      } catch (err) {
        if (err.response) {
          // Got Data Error but Not in the 200 response range
          console.log(err.response.data.message);
          console.log(err.response.data);
          console.log(err.response.status);
          console.log(err.response.headers);
        } else {
          //No Data Error, if (err.code === 404)
          console.log(`Error: ${err.message}`);
        }
      }
    };
    fetchPosts();
  }, []);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleEdit = async (id) => {
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const updatedPost = { id, title: editTitle, datetime, body: editBody };
    try {
      const response = await api.put(`/posts/${id}`, updatedPost);
      setPosts(
        posts.map((post) => (post.id === id ? { ...response.data } : post))
      );
      setEditTitle("");
      setEditBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  return (
    <div className="App">
      <Header title="React JS Blog" width={width} />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route exact path="/" element={<Home posts={searchResults} />} />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/edit/:id"
          element={
            <EditPost
              posts={posts}
              handleEdit={handleEdit}
              editTitle={editTitle}
              setEditTitle={setEditTitle}
              editBody={editBody}
              setEditBody={setEditBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/Header.js:

```js
import React from "react";
import { FaLaptop, FaTabletAlt, FaMobileAlt } from "react-icons/fa";

const Header = ({ title, width }) => {
  return (
    <header className="Header">
      <h1>{title}</h1>
      {width < 768 ? (
        <FaMobileAlt />
      ) : width < 992 ? (
        <FaTabletAlt />
      ) : (
        <FaLaptop />
      )}
    </header>
  );
};

export default Header;
```

# #End  </details>

<details>
  <summary>54. Blog App - Create useAxiosFetch Custom Hook</summary>

# Create useAxiosFetch Custom Hook

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/20f4babd-182e-4bad-a2d3-f1dc519faa6f">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/32345a40-5557-48dd-b869-85c244328676">
<img width="1271" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8c9e7af0-c9f7-4bf3-a885-5da907bc8554">
<img width="1271" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/55efd625-b297-45a9-ade1-50b7dab951c5">

### x-dave-gray/blogapp/src/hooks/useAxiosFetch.js:

```js
import React, { useState, useEffect } from "react";
import axios from "axios";

const useAxiosFetch = (dataUrl) => {
  const [data, setData] = useState([]);
  const [fetchError, setFetchError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    let isMounted = true;
    const source = axios.CancelToken.source();

    const fetchData = async (url) => {
      setIsLoading(true);
      try {
        const response = await axios.get(url, { cancelToken: source.token });
        if (isMounted) {
          setData(response.data);
          setFetchError(null);
        }
      } catch (err) {
        if (isMounted) {
          setFetchError(err.message);
          setData([]);
        }
      } finally {
        isMounted && setTimeout(() => setIsLoading(false), 1000);
      }
    };

    fetchData(dataUrl);

    const cleanUp = () => {
      //console.log("clean up function");
      isMounted = false;
      source.cancel();
    };

    return cleanUp;
  }, [dataUrl]);

  return { data, fetchError, isLoading };
};

export default useAxiosFetch;
```

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import api from "./api/posts";
import EditPost from "./EditPost";
import useWindowSize from "./hooks/useWindowSize";
import useAxiosFetch from "./hooks/useAxiosFetch";

function App() {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const [editTitle, setEditTitle] = useState("");
  const [editBody, setEditBody] = useState("");
  const navigate = useNavigate();
  const { width } = useWindowSize();
  const { data, fetchError, isLoading } = useAxiosFetch(
    "http://localhost:3500/posts"
  );

  useEffect(() => {
    setPosts(data);
  }, [data]);

  // useEffect(() => {
  //   const fetchPosts = async () => {
  //     try {
  //       const response = await api.get("/posts");
  //       setPosts(response.data);
  //     } catch (err) {
  //       if (err.response) {
  //         // Got Data Error but Not in the 200 response range
  //         console.log(err.response.data.message);
  //         console.log(err.response.data);
  //         console.log(err.response.status);
  //         console.log(err.response.headers);
  //       } else {
  //         //No Data Error, if (err.code === 404)
  //         console.log(`Error: ${err.message}`);
  //       }
  //     }
  //   };
  //   fetchPosts();
  // }, []);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleEdit = async (id) => {
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const updatedPost = { id, title: editTitle, datetime, body: editBody };
    try {
      const response = await api.put(`/posts/${id}`, updatedPost);
      setPosts(
        posts.map((post) => (post.id === id ? { ...response.data } : post))
      );
      setEditTitle("");
      setEditBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  return (
    <div className="App">
      <Header title="React JS Blog" width={width} />
      <Nav search={search} setSearch={setSearch} />
      <Routes>
        <Route
          exact
          path="/"
          element={
            <Home
              posts={searchResults}
              fetchError={fetchError}
              isLoading={isLoading}
            />
          }
        />
        <Route
          exact
          path="/post"
          element={
            <NewPost
              handleSubmit={handleSubmit}
              postTitle={postTitle}
              setPostTitle={setPostTitle}
              postBody={postBody}
              setPostBody={setPostBody}
            />
          }
        />
        <Route
          path="/edit/:id"
          element={
            <EditPost
              posts={posts}
              handleEdit={handleEdit}
              editTitle={editTitle}
              setEditTitle={setEditTitle}
              editBody={editBody}
              setEditBody={setEditBody}
            />
          }
        />
        <Route
          path="/post/:id"
          element={<PostPage posts={posts} handleDelete={handleDelete} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/Home.js:

```js
import React from "react";
import Feed from "./Feed";

const Home = ({ posts, fetchError, isLoading }) => {
  return (
    <main className="Home">
      {isLoading && <p className="statusMsg">Loading posts...</p>}
      {!isLoading && fetchError && (
        <p className="statusMsg" style={{ color: "red" }}>
          {fetchError}
        </p>
      )}
      {!isLoading &&
        !fetchError &&
        (posts.length ? (
          <Feed posts={posts} />
        ) : (
          <p className="statusMsg">No Posts to display.</p>
        ))}
    </main>
  );
};

export default Home;
```

# #End  </details>

+BLOG APP WITH CONTEXT API

<details>
  <summary>55. Blog App - Create Context API</summary>

#  Create Context API

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dab789fa-a85a-4cd2-b38e-055f17e78768">
<img width="1271" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ef13f9e6-cded-4cb1-ac25-1d2082b7d37d">

### x-dave-gray/blogapp/src/context/DataContext.js:

```js
import React, { createContext, useState, useEffect } from "react";

const DataContext = createContext({});

export const DataProvider = ({ children }) => {
  return <DataContext.Provider value={{}}>{children}</DataContext.Provider>;
};

export default DataContext;
```

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import api from "./api/posts";
import EditPost from "./EditPost";
import useWindowSize from "./hooks/useWindowSize";
import useAxiosFetch from "./hooks/useAxiosFetch";
import { DataProvider } from "./context/DataContext";

function App() {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const [editTitle, setEditTitle] = useState("");
  const [editBody, setEditBody] = useState("");
  const navigate = useNavigate();
  const { width } = useWindowSize();
  const { data, fetchError, isLoading } = useAxiosFetch(
    "http://localhost:3500/posts"
  );

  useEffect(() => {
    setPosts(data);
  }, [data]);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleEdit = async (id) => {
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const updatedPost = { id, title: editTitle, datetime, body: editBody };
    try {
      const response = await api.put(`/posts/${id}`, updatedPost);
      setPosts(
        posts.map((post) => (post.id === id ? { ...response.data } : post))
      );
      setEditTitle("");
      setEditBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  return (
    <div className="App">
      <DataProvider>
        <Header title="React JS Blog" width={width} />
        <Nav search={search} setSearch={setSearch} />
        <Routes>
          <Route
            exact
            path="/"
            element={
              <Home
                posts={searchResults}
                fetchError={fetchError}
                isLoading={isLoading}
              />
            }
          />
          <Route
            exact
            path="/post"
            element={
              <NewPost
                handleSubmit={handleSubmit}
                postTitle={postTitle}
                setPostTitle={setPostTitle}
                postBody={postBody}
                setPostBody={setPostBody}
              />
            }
          />
          <Route
            path="/edit/:id"
            element={
              <EditPost
                posts={posts}
                handleEdit={handleEdit}
                editTitle={editTitle}
                setEditTitle={setEditTitle}
                editBody={editBody}
                setEditBody={setEditBody}
              />
            }
          />
          <Route
            path="/post/:id"
            element={<PostPage posts={posts} handleDelete={handleDelete} />}
          />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<Missing />} />
        </Routes>
        <Footer />
      </DataProvider>
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>56. Blog App - Refactor Header with Context API</summary>

# Refactor Header with Context API

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/214639db-2fea-4eee-9b5f-05069da59280">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4fee8db9-3c10-4cca-a3c7-f3aaa9b3350e">
<img width="1250" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c4f0bb70-bfbe-480a-8f9a-67ab28467f52">

### x-dave-gray/blogapp/src/context/DataContext.js:

```js
import React, { createContext, useState, useEffect } from "react";
import useWindowSize from "../hooks/useWindowSize";

const DataContext = createContext({});

export const DataProvider = ({ children }) => {
  const { width } = useWindowSize();

  return (
    <DataContext.Provider value={{ width }}>{children}</DataContext.Provider>
  );
};

export default DataContext;
```

### x-dave-gray/blogapp/src/App.js:

```js
import { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import api from "./api/posts";
import EditPost from "./EditPost";
import useAxiosFetch from "./hooks/useAxiosFetch";

import { DataProvider } from "./context/DataContext";

function App() {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const [editTitle, setEditTitle] = useState("");
  const [editBody, setEditBody] = useState("");
  const navigate = useNavigate();

  const { data, fetchError, isLoading } = useAxiosFetch(
    "http://localhost:3500/posts"
  );

  useEffect(() => {
    setPosts(data);
  }, [data]);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleEdit = async (id) => {
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const updatedPost = { id, title: editTitle, datetime, body: editBody };
    try {
      const response = await api.put(`/posts/${id}`, updatedPost);
      setPosts(
        posts.map((post) => (post.id === id ? { ...response.data } : post))
      );
      setEditTitle("");
      setEditBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  return (
    <div className="App">
      <DataProvider>
        <Header title="React JS Blog" />
        <Nav search={search} setSearch={setSearch} />
        <Routes>
          <Route
            exact
            path="/"
            element={
              <Home
                posts={searchResults}
                fetchError={fetchError}
                isLoading={isLoading}
              />
            }
          />
          <Route
            exact
            path="/post"
            element={
              <NewPost
                handleSubmit={handleSubmit}
                postTitle={postTitle}
                setPostTitle={setPostTitle}
                postBody={postBody}
                setPostBody={setPostBody}
              />
            }
          />
          <Route
            path="/edit/:id"
            element={
              <EditPost
                posts={posts}
                handleEdit={handleEdit}
                editTitle={editTitle}
                setEditTitle={setEditTitle}
                editBody={editBody}
                setEditBody={setEditBody}
              />
            }
          />
          <Route
            path="/post/:id"
            element={<PostPage posts={posts} handleDelete={handleDelete} />}
          />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<Missing />} />
        </Routes>
        <Footer />
      </DataProvider>
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/Header.js:

```js
import React, { useContext } from "react";
import { FaLaptop, FaTabletAlt, FaMobileAlt } from "react-icons/fa";
import DataContext from "./context/DataContext";

const Header = ({ title }) => {
  const { width } = useContext(DataContext);

  return (
    <header className="Header">
      <h1>{title}</h1>
      {width < 768 ? (
        <FaMobileAlt />
      ) : width < 992 ? (
        <FaTabletAlt />
      ) : (
        <FaLaptop />
      )}
    </header>
  );
};

export default Header;
```

# #End  </details>

<details>
  <summary>57. Blog App - Refactor Nav and Home with Context API</summary>

# Refactor Nav and Home with Context API

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/66acee86-e8f0-4702-a333-fcc049923188">
<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/740808b3-b398-453e-ac0d-76d44178ef79">
<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a7496d22-4ef5-4bb3-b7d7-63584276793d">
<img width="1249" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2561a649-8010-452f-a6fc-2b375d24cebf">

### x-dave-gray/blogapp/src/context/DataContext.js:

```js
import React, { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { format } from "date-fns";
import api from "../api/posts";
import useAxiosFetch from "../hooks/useAxiosFetch";
import useWindowSize from "../hooks/useWindowSize";

const DataContext = createContext({});

export const DataProvider = ({ children }) => {
  const { width } = useWindowSize();
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const [editTitle, setEditTitle] = useState("");
  const [editBody, setEditBody] = useState("");
  const navigate = useNavigate();

  const { data, fetchError, isLoading } = useAxiosFetch(
    "http://localhost:3500/posts"
  );

  useEffect(() => {
    setPosts(data);
  }, [data]);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleEdit = async (id) => {
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const updatedPost = { id, title: editTitle, datetime, body: editBody };
    try {
      const response = await api.put(`/posts/${id}`, updatedPost);
      setPosts(
        posts.map((post) => (post.id === id ? { ...response.data } : post))
      );
      setEditTitle("");
      setEditBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  return (
    <DataContext.Provider
      value={{
        width,
        search,
        setSearch,
        searchResults,
        fetchError,
        isLoading,
      }}
    >
      {children}
    </DataContext.Provider>
  );
};

export default DataContext;
```

### x-dave-gray/blogapp/src/App.js:

```js
import React from "react";
import { Route, Routes } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import EditPost from "./EditPost";

import { DataProvider } from "./context/DataContext";

function App() {
  const {
    handleSubmit,
    postTitle,
    setPostTitle,
    postBody,
    setPostBody,
    posts,
    handleEdit,
    editTitle,
    setEditTitle,
    editBody,
    setEditBody,
    handleDelete,
  } = {};
  return (
    <div className="App">
      <DataProvider>
        <Header title="React JS Blog" />
        <Nav />
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route
            exact
            path="/post"
            element={
              <NewPost
                handleSubmit={handleSubmit}
                postTitle={postTitle}
                setPostTitle={setPostTitle}
                postBody={postBody}
                setPostBody={setPostBody}
              />
            }
          />
          <Route
            path="/edit/:id"
            element={
              <EditPost
                posts={posts}
                handleEdit={handleEdit}
                editTitle={editTitle}
                setEditTitle={setEditTitle}
                editBody={editBody}
                setEditBody={setEditBody}
              />
            }
          />
          <Route
            path="/post/:id"
            element={<PostPage posts={posts} handleDelete={handleDelete} />}
          />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<Missing />} />
        </Routes>
        <Footer />
      </DataProvider>
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/Nav.js:

```js
import React, { useContext } from "react";
import { Link } from "react-router-dom";
import DataContext from "./context/DataContext";

const Nav = () => {
  const { search, setSearch } = useContext(DataContext);

  return (
    <nav className="Nav">
      <form className="searchForm" onSubmit={(e) => e.preventDefault()}>
        <label htmlFor="search">Search Posts</label>
        <input
          id="search"
          type="text"
          placeholder="Search Posts"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </form>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/post">Post</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Nav;
```

### x-dave-gray/blogapp/src/Home.js:

```js
import React, { useContext } from "react";
import DataContext from "./context/DataContext";
import Feed from "./Feed";

const Home = () => {
  const { searchResults, fetchError, isLoading } = useContext(DataContext);
  return (
    <main className="Home">
      {isLoading && <p className="statusMsg">Loading posts...</p>}
      {!isLoading && fetchError && (
        <p className="statusMsg" style={{ color: "red" }}>
          {fetchError}
        </p>
      )}
      {!isLoading &&
        !fetchError &&
        (searchResults?.length ? (
          <Feed posts={searchResults} />
        ) : (
          <p className="statusMsg">No Posts to display.</p>
        ))}
    </main>
  );
};

export default Home;
```

# #End  </details>

<details>
  <summary>58. Blog App - Refactor NewPost with Context API</summary>

# Blog App - Refactor NewPost with Context API

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/590f94f6-9ab9-4573-89f9-df6fe7b56399">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/626f728c-b737-4481-92dd-5c2d27c7c7e2">
<img width="1250" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/28c8a081-fdf7-4573-8bc3-c28e95c31f83">

### x-dave-gray/blogapp/src/context/DataContext.js:

```js
import React, { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { format } from "date-fns";
import api from "../api/posts";
import useAxiosFetch from "../hooks/useAxiosFetch";
import useWindowSize from "../hooks/useWindowSize";

const DataContext = createContext({});

export const DataProvider = ({ children }) => {
  const { width } = useWindowSize();
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const [editTitle, setEditTitle] = useState("");
  const [editBody, setEditBody] = useState("");
  const navigate = useNavigate();

  const { data, fetchError, isLoading } = useAxiosFetch(
    "http://localhost:3500/posts"
  );

  useEffect(() => {
    setPosts(data);
  }, [data]);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleEdit = async (id) => {
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const updatedPost = { id, title: editTitle, datetime, body: editBody };
    try {
      const response = await api.put(`/posts/${id}`, updatedPost);
      setPosts(
        posts.map((post) => (post.id === id ? { ...response.data } : post))
      );
      setEditTitle("");
      setEditBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  return (
    <DataContext.Provider
      value={{
        width,
        search,
        setSearch,
        searchResults,
        fetchError,
        isLoading,
        handleSubmit,
        postTitle,
        setPostTitle,
        postBody,
        setPostBody,
      }}
    >
      {children}
    </DataContext.Provider>
  );
};

export default DataContext;
```

### x-dave-gray/blogapp/src/App.js:

```js
import React from "react";
import { Route, Routes } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import EditPost from "./EditPost";

import { DataProvider } from "./context/DataContext";

function App() {
  const {
    posts,
    handleEdit,
    editTitle,
    setEditTitle,
    editBody,
    setEditBody,
    handleDelete,
  } = {};
  return (
    <div className="App">
      <DataProvider>
        <Header title="React JS Blog" />
        <Nav />
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/post" element={<NewPost />} />
          <Route
            path="/edit/:id"
            element={
              <EditPost
                posts={posts}
                handleEdit={handleEdit}
                editTitle={editTitle}
                setEditTitle={setEditTitle}
                editBody={editBody}
                setEditBody={setEditBody}
              />
            }
          />
          <Route
            path="/post/:id"
            element={<PostPage posts={posts} handleDelete={handleDelete} />}
          />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<Missing />} />
        </Routes>
        <Footer />
      </DataProvider>
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/NewPost.js:

```js
import React, { useContext } from "react";
import DataContext from "./context/DataContext";

const NewPost = () => {
  const { handleSubmit, postTitle, setPostTitle, postBody, setPostBody } =
    useContext(DataContext);

  return (
    <main className="NewPost">
      <h2>NewPost</h2>
      <form className="newPostForm" onSubmit={handleSubmit}>
        <label htmlFor="postTitle">Title:</label>
        <input
          type="text"
          id="postTitle"
          value={postTitle}
          onChange={(e) => setPostTitle(e.target.value)}
          required
        />
        <label htmlFor="postBody">Post:</label>
        <textarea
          id="postBody"
          value={postBody}
          onChange={(e) => setPostBody(e.target.value)}
          // cols="10"
          // rows="30"
          required
        />
        <button type="submit">Submit</button>
      </form>
    </main>
  );
};

export default NewPost;
```

# #End  </details>

<details>
  <summary>59. Blog App - Refactor PostPage and EditPost with Context API</summary>

# Refactor PostPage and EditPost with Context API

<img width="965" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/722a1c50-bcdd-44d8-94ac-b51b859296be">
<img width="965" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ccece9ac-ce22-480f-bc5a-88e4306924da">
<img width="965" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5a0c1c0e-8088-4055-ae84-5863543e4d23">
<img width="1248" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/498fdbd3-cfb0-44f1-aff8-4ddc08432f0c">
<img width="1248" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ba221715-f4f7-4cea-99e0-679ca528ce9d">
<img width="1248" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9f1834ff-eb1d-4f42-b61d-74df2c08dd08">
<img width="1248" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/276b6d71-1994-4007-ada0-cc8a7e2c2b33">

### x-dave-gray/blogapp/src/context/DataContext.js:

```js
import React, { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { format } from "date-fns";
import api from "../api/posts";
import useAxiosFetch from "../hooks/useAxiosFetch";
import useWindowSize from "../hooks/useWindowSize";

const DataContext = createContext({});

export const DataProvider = ({ children }) => {
  const { width } = useWindowSize();
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const [editTitle, setEditTitle] = useState("");
  const [editBody, setEditBody] = useState("");
  const navigate = useNavigate();

  const { data, fetchError, isLoading } = useAxiosFetch(
    "http://localhost:3500/posts"
  );

  useEffect(() => {
    setPosts(data);
  }, [data]);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleEdit = async (id) => {
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const updatedPost = { id, title: editTitle, datetime, body: editBody };
    try {
      const response = await api.put(`/posts/${id}`, updatedPost);
      setPosts(
        posts.map((post) => (post.id === id ? { ...response.data } : post))
      );
      setEditTitle("");
      setEditBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  return (
    <DataContext.Provider
      value={{
        width,
        search,
        setSearch,
        searchResults,
        fetchError,
        isLoading,
        handleSubmit,
        postTitle,
        setPostTitle,
        postBody,
        setPostBody,
        posts,
        handleEdit,
        editBody,
        setEditBody,
        editTitle,
        setEditTitle,
        handleDelete,
      }}
    >
      {children}
    </DataContext.Provider>
  );
};

export default DataContext;
```

### x-dave-gray/blogapp/src/App.js:

```js
import React from "react";
import { Route, Routes } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import EditPost from "./EditPost";

import { DataProvider } from "./context/DataContext";

function App() {
  return (
    <div className="App">
      <DataProvider>
        <Header title="React JS Blog" />
        <Nav />
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/post" element={<NewPost />} />
          <Route path="/edit/:id" element={<EditPost />} />
          <Route path="/post/:id" element={<PostPage />} />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<Missing />} />
        </Routes>
        <Footer />
      </DataProvider>
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/PostPage.js:

```js
import React, { useContext } from "react";
import DataContext from "./context/DataContext";
import { useParams, Link } from "react-router-dom";

const PostPage = () => {
  const { posts, handleDelete } = useContext(DataContext);
  const { id } = useParams();
  const post = posts.find((post) => post.id.toString() === id);

  return (
    <main className="PostPage">
      <article className="post">
        {post ? (
          <>
            <h2>{post.title}</h2>
            <p className="postDate">{post.datetime}</p>
            <p className="postBody">{post.body}</p>
            <Link to={`/edit/${post.id}`}>
              <button className="editButton">Edit Post</button>
            </Link>
            <button
              className="deleteButton"
              onClick={() => handleDelete(post.id)}
            >
              Delete Post
            </button>
          </>
        ) : (
          <>
            <h2>Post Not Found</h2>
            <p>Well, that's disappointing.</p>
            <p>
              <Link to="/">Visit our Home Page</Link>
            </p>
          </>
        )}
      </article>
    </main>
  );
};

export default PostPage;
```

### x-dave-gray/blogapp/src/EditPost.js:

```js
import React, { useEffect, useContext } from "react";
import DataContext from "./context/DataContext";
import { useParams, Link } from "react-router-dom";

const EditPost = () => {
  const { posts, handleEdit, editBody, setEditBody, editTitle, setEditTitle } =
    useContext(DataContext);
  const { id } = useParams();
  const post = posts.find((post) => post.id.toString() === id);

  useEffect(() => {
    if (post) {
      setEditTitle(post.title);
      setEditBody(post.body);
    }
  }, [post, setEditTitle, setEditBody]);

  return (
    <main className="NewPost">
      {post ? (
        <>
          <h2>EditPost</h2>
          <form className="newPostForm" onSubmit={(e) => e.preventDefault()}>
            <label htmlFor="postTitle">Title:</label>
            <input
              type="text"
              id="postTitle"
              value={editTitle}
              onChange={(e) => setEditTitle(e.target.value)}
              required
            />
            <label htmlFor="postBody">Post:</label>
            <textarea
              id="postBody"
              value={editBody}
              onChange={(e) => setEditBody(e.target.value)}
              // cols="10"
              // rows="30"
              required
            />
            <button type="submit" onClick={() => handleEdit(post.id)}>
              Submit
            </button>
          </form>
        </>
      ) : (
        <>
          <h2>Post Not Found</h2>
          <p>Well, that's disappointing.</p>
          <p>
            <Link to="/">Visit our Homepage</Link>
          </p>
        </>
      )}
    </main>
  );
};

export default EditPost;
```

# #End  </details>

<details>
  <summary>60. Blog App - Isolating Header and Footer Component State from Shared Context API</summary>

# Isolating Header and Footer Component State from Shared Context API

<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bd5e60d4-a09c-4ec9-8025-5a26983c2408">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e3cb586f-c66d-4ac3-a205-69b58355a628">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/375e30db-9404-42a7-8602-fcb6d0e9592c">
<img width="1249" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/04252edc-fa61-4b55-b1cc-38f0d485a46c">

### x-dave-gray/blogapp/src/App.js:

```js
import React from "react";
import { Route, Routes } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import About from "./About";
import Missing from "./Missing";
import EditPost from "./EditPost";

import { DataProvider } from "./context/DataContext";

function App() {
  return (
    <div className="App">
      <Header title="React JS Blog" />
      <DataProvider>
        <Nav />
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/post" element={<NewPost />} />
          <Route path="/edit/:id" element={<EditPost />} />
          <Route path="/post/:id" element={<PostPage />} />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<Missing />} />
        </Routes>
      </DataProvider>
      <Footer />
    </div>
  );
}

export default App;
```

### x-dave-gray/blogapp/src/context/DataContext.js:

```js
import React, { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { format } from "date-fns";
import api from "../api/posts";
import useAxiosFetch from "../hooks/useAxiosFetch";

const DataContext = createContext({});

export const DataProvider = ({ children }) => {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [postTitle, setPostTitle] = useState("");
  const [postBody, setPostBody] = useState("");
  const [editTitle, setEditTitle] = useState("");
  const [editBody, setEditBody] = useState("");
  const navigate = useNavigate();

  const { data, fetchError, isLoading } = useAxiosFetch(
    "http://localhost:3500/posts"
  );

  useEffect(() => {
    setPosts(data);
  }, [data]);

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    //const datetime = format(new Date(), "yyyy-MM-dd HH:mm:ss");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    try {
      const response = await api.post("/posts", newPost);
      const allPosts = [...posts, response.data];
      setPosts(allPosts);
      setPostTitle("");
      setPostBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleEdit = async (id) => {
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const updatedPost = { id, title: editTitle, datetime, body: editBody };
    try {
      const response = await api.put(`/posts/${id}`, updatedPost);
      setPosts(
        posts.map((post) => (post.id === id ? { ...response.data } : post))
      );
      setEditTitle("");
      setEditBody("");
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/posts/${id}`);
      const postList = posts.filter((post) => post.id !== id);
      setPosts(postList);
      navigate("/");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  };

  return (
    <DataContext.Provider
      value={{
        search,
        setSearch,
        searchResults,
        fetchError,
        isLoading,
        handleSubmit,
        postTitle,
        setPostTitle,
        postBody,
        setPostBody,
        posts,
        handleEdit,
        editBody,
        setEditBody,
        editTitle,
        setEditTitle,
        handleDelete,
      }}
    >
      {children}
    </DataContext.Provider>
  );
};

export default DataContext;
```

### x-dave-gray/blogapp/src/Header.js:

```js
import React from "react";
import { FaLaptop, FaTabletAlt, FaMobileAlt } from "react-icons/fa";
import useWindowSize from "./hooks/useWindowSize";
// import DataContext from "./context/DataContext";

const Header = ({ title }) => {
  // const { width } = useContext(DataContext);
  const { width } = useWindowSize();

  return (
    <header className="Header">
      <h1>{title}</h1>
      {width < 768 ? (
        <FaMobileAlt />
      ) : width < 992 ? (
        <FaTabletAlt />
      ) : (
        <FaLaptop />
      )}
    </header>
  );
};

export default Header;
```

### x-dave-gray/blogapp/src/Footer.js:

```js
import React from "react";

const Footer = () => {
  const today = new Date();

  return (
    <footer className="Footer">
      <p>Copyright &copy; {today.getFullYear()}</p>
    </footer>
  );
};

export default Footer;
```

# #End  </details>

+BLOG APP WITH EASY PEASY REDUX

<details>
  <summary>61. Blog App - Using Easy Peasy v5 for State Management</summary>

# Using Easy Peasy v5 for State Management

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/74393f20-f162-463d-b863-13228f0612ce">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/62c8b5d9-ceef-43de-9716-4f2327409d51">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3313233f-d1ca-4567-8171-cc9ad54e1b4f">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/58893951-edfd-417f-98a9-136522fad77c">

# Install Easy Peasy

```bs
npm install easy-peasy
```

# Create your store

### x-dave-gray/blogapp/src/store.js:

```js
import { createStore, action } from "easy-peasy";

export const store = createStore({
  todos: ["Create store", "Wrap application", "Use store"],

  addTodo: action((state, payload) => {
    state.todos.push(payload);
  }),
});
```

# Wrap your application

### x-dave-gray/blogapp/src/App.js:

```js
import { StoreProvider } from "easy-peasy";
import { store } from "./store";
import TodoList from "./TodoList";

function App() {
  return (
    <StoreProvider store={store}>
      <TodoList />
    </StoreProvider>
  );
}

export default App;
```

# Use the store state in your components

### x-dave-gray/blogapp/src/TodoList.js:

```js
import { useStoreState, useStoreActions } from "easy-peasy";
import AddTodo from "./AddTodo";

function TodoList() {
  const todos = useStoreState((state) => state.todos);
  const addTodo = useStoreActions((actions) => actions.addTodo);

  return (
    <div>
      {todos.map((todo, idx) => (
        <div key={idx}>
          <h2>{todo}</h2>
        </div>
      ))}
      <AddTodo onAdd={addTodo} />
    </div>
  );
}

export default TodoList;
```

### x-dave-gray/blogapp/src/AddTodo.js:

```js
import React, { useState } from "react";

const AddTodo = ({ onAdd }) => {
  const [todo, setTodo] = useState("");

  return (
    <div>
      <input
        onChange={(e) => {
          setTodo(e.target.value);
        }}
        type="text"
      />
      <button onClick={() => onAdd(todo)}>Add Item</button>

      <div>{todo}</div>
    </div>
  );
};

export default AddTodo;
```

# #End  </details>

<details>
  <summary>62. Blog App - Create Easy Peasy store </summary>

# Create Easy Peasy store

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ef7a4b22-04a2-4c95-a449-907a065f73cc">

# Remove unused packages

```bs
npm uninstall @testing-library/jest-dom @testing-library/react @testing-library/user-event web-vitals
```

# Install Easy Peasy v5 Redux

```bs
npm install easy-peasy
```

# Start npx server:

```bs
npx json-server -p 3500 -w data/db.json
```

### x-dave-gray/blogapp/src/store.js:

```js
import { createStore, action, thunk, computed } from "easy-peasy";
import api from "./api/posts";

export default createStore({
  posts: [],
  setPosts: action((state, payload) => {
    state.posts = payload;
  }),
  postTitle: "",
  setPostTitle: action((state, payload) => {
    state.postTitle = payload;
  }),
  postBody: "",
  setPostBody: action((state, payload) => {
    state.postBody = payload;
  }),
  editTitle: "",
  setEditTitle: action((state, payload) => {
    state.editTitle = payload;
  }),
  editBody: "",
  setEditBody: action((state, payload) => {
    state.editBody = payload;
  }),
  search: "",
  setSearch: action((state, payload) => {
    state.search = payload;
  }),
  searchResults: [],
  setSearchResults: action((state, payload) => {
    state.searchResults = payload;
  }),
  postCount: computed((state) => state.posts.length),
  getPostById: computed((state) => {
    return (id) => state.posts.find((post) => post.id.toString() === id);
  }),
  savePost: thunk(async (actions, newPost, helpers) => {
    const { posts } = helpers.getState();
    try {
      const response = await api.post("/posts", newPost);
      actions.setPosts([...posts, response.data]);
      actions.setPostTitle("");
      actions.setPostBody("");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  }),
  deletePost: thunk(async (actions, id, helpers) => {
    const { posts } = helpers.getState();
    try {
      await api.delete(`/posts/${id}`);
      actions.setPosts(posts.filter((post) => post.id !== id));
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  }),
  editPost: thunk(async (actions, updatedPost, helpers) => {
    const { posts } = helpers.getState();
    const { id } = updatedPost;
    try {
      const response = await api.put(`/posts/${id}`, updatedPost);
      actions.setPosts(
        posts.map((post) => (post.id === id ? { ...response.data } : post))
      );
      actions.setEditTitle("");
      actions.setEditBody("");
    } catch (err) {
      console.log(`Error: ${err.message}`);
    }
  }),
});
```

# #End  </details>

<details>
  <summary>63.  Blog App - Refactoring Index.js and App.js </summary>

# Refactoring Index.js and App.js

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/14ec7db0-6a12-4a6d-b46e-97daf70d8753">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/53552fe8-d4d9-41af-a35c-1bf378b2e697">

### x-dave-gray/blogapp/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { StoreProvider } from "easy-peasy";
import store from "./store";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <StoreProvider store={store}>
      <Router>
        <Routes>
          <Route path="/*" element={<App />} />
        </Routes>
      </Router>
    </StoreProvider>
  </React.StrictMode>
);
```

### x-dave-gray/blogapp/src/App.js:

```js
import Header from "./Header";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "./Home";
import NewPost from "./NewPost";
import PostPage from "./PostPage";
import EditPost from "./EditPost";
import About from "./About";
import Missing from "./Missing";
import { Route, Routes } from "react-router-dom";
import { useEffect } from "react";
import useAxiosFetch from "./hooks/useAxiosFetch";
import { useStoreActions } from "easy-peasy";

function App() {
  const setPosts = useStoreActions((actions) => actions.setPosts);

  const { data, fetchError, isLoading } = useAxiosFetch(
    "http://localhost:3500/posts"
  );

  useEffect(() => {
    setPosts(data);
  }, [data, setPosts]);

  return (
    <div className="App">
      <Header title="React JS Blog" />
      <Nav />
      <Routes>
        <Route
          exact
          path="/"
          element={<Home isLoading={isLoading} fetchError={fetchError} />}
        />
        <Route exact path="/post" element={<NewPost />} />
        <Route path="/edit/:id" element={<EditPost />} />
        <Route path="/post/:id" element={<PostPage />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Missing />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>64. Blog App - Refactoring Nav.js</summary>

# Refactoring Nav.js

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/acaf99a4-38ba-4de9-83a0-a1c5499fa8d4">

### x-dave-gray/blogapp/src/Nav.js:

```js
import { Link } from "react-router-dom";
import { useEffect } from "react";
import { useStoreState, useStoreActions } from "easy-peasy";

const Nav = () => {
  const posts = useStoreState((state) => state.posts);
  const search = useStoreState((state) => state.search);
  const setSearch = useStoreActions((actions) => actions.setSearch);
  const setSearchResults = useStoreActions(
    (actions) => actions.setSearchResults
  );

  useEffect(() => {
    const filteredResults = posts.filter(
      (post) =>
        post.body.toLowerCase().includes(search.toLowerCase()) ||
        post.title.toLowerCase().includes(search.toLowerCase())
    );

    setSearchResults(filteredResults.reverse());
  }, [posts, search, setSearchResults]);

  return (
    <nav className="Nav">
      <form className="searchForm" onSubmit={(e) => e.preventDefault()}>
        <label htmlFor="search">Search Posts</label>
        <input
          id="search"
          type="text"
          placeholder="Search Posts"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </form>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/post">Post</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Nav;
```

# #End  </details>

<details>
  <summary>65. Blog App - Refactoring Home.js</summary>

# Refactoring Home.js

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9a2e02b6-cca1-4b3e-82f1-a134de518399">
<img width="1251" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bdcf0183-77db-4d21-a7f8-36711fd3bb43">

### x-dave-gray/blogapp/src/Home.js:

```js
import Feed from "./Feed";
import { useStoreState } from "easy-peasy";

const Home = ({ isLoading, fetchError }) => {
  const searchResults = useStoreState((state) => state.searchResults);

  return (
    <main className="Home">
      {isLoading && <p className="statusMsg">Loading posts...</p>}
      {!isLoading && fetchError && (
        <p className="statusMsg" style={{ color: "red" }}>
          {fetchError}
        </p>
      )}
      {!isLoading &&
        !fetchError &&
        (searchResults.length ? (
          <Feed posts={searchResults} />
        ) : (
          <p className="statusMsg">No posts to display.</p>
        ))}
    </main>
  );
};

export default Home;
```

# #End  </details>

<details>
  <summary>66. Blog App - Refactoring PostPage.js</summary>

# Refactoring PostPage.js

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2fb64ee5-a723-4d67-b3b2-263041167885">
<img width="1247" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6cdf8638-9bd7-4fb9-8512-7c4ee7f7e8aa">

### x-dave-gray/blogapp/src/PostPage.js:

```js
import { useParams, Link, useNavigate } from "react-router-dom";
import { useStoreState, useStoreActions } from "easy-peasy";

const PostPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const deletePost = useStoreActions((actions) => actions.deletePost);
  const getPostById = useStoreState((state) => state.getPostById);
  const post = getPostById(id);

  const handleDelete = (id) => {
    deletePost(id);
    navigate("/");
  };

  return (
    <main className="PostPage">
      <article className="post">
        {post && (
          <>
            <h2>{post.title}</h2>
            <p className="postDate">{post.datetime}</p>
            <p className="postBody">{post.body}</p>
            <Link to={`/edit/${post.id}`}>
              <button className="editButton">Edit Post</button>
            </Link>
            <button
              className="deleteButton"
              onClick={() => handleDelete(post.id)}
            >
              Delete Post
            </button>
          </>
        )}
        {!post && (
          <>
            <h2>Post Not Found</h2>
            <p>Well, that's disappointing.</p>
            <p>
              <Link to="/">Visit Our Homepage</Link>
            </p>
          </>
        )}
      </article>
    </main>
  );
};

export default PostPage;
```

# #End  </details>

<details>
  <summary>67. Blog App - Refactoring NewPost.js</summary>

# Refactoring NewPost.js

<img width="1247" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/68918bc3-cdc3-4edb-a4b7-4da1945c4db6">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/960abae2-6393-474b-98b0-f449982b91ab">

### x-dave-gray/blogapp/src/NewPost.js:

```js
import { useNavigate } from "react-router-dom";
import { format } from "date-fns";
import { useStoreState, useStoreActions } from "easy-peasy";

const NewPost = () => {
  const navigate = useNavigate();

  const posts = useStoreState((state) => state.posts);
  const postTitle = useStoreState((state) => state.postTitle);
  const postBody = useStoreState((state) => state.postBody);

  const savePost = useStoreActions((actions) => actions.savePost);
  const setPostTitle = useStoreActions((actions) => actions.setPostTitle);
  const setPostBody = useStoreActions((actions) => actions.setPostBody);

  const handleSubmit = (e) => {
    e.preventDefault();
    const id = posts.length ? posts[posts.length - 1].id + 1 : 1;
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const newPost = { id, title: postTitle, datetime, body: postBody };
    savePost(newPost);
    navigate("/");
  };

  return (
    <main className="NewPost">
      <h2>New Post</h2>
      <form className="newPostForm" onSubmit={handleSubmit}>
        <label htmlFor="postTitle">Title:</label>
        <input
          id="postTitle"
          type="text"
          required
          value={postTitle}
          onChange={(e) => setPostTitle(e.target.value)}
        />
        <label htmlFor="postBody">Post:</label>
        <textarea
          id="postBody"
          required
          value={postBody}
          onChange={(e) => setPostBody(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
    </main>
  );
};

export default NewPost;
```

# #End  </details>

<details>
  <summary>68. Blog App - Refactoring EditPost.js</summary>

# Refactoring EditPost.js

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/48d9383c-93c4-412f-89d8-86bba818aa0e">
<img width="1249" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b9d99e8b-41d0-4fc4-880e-bb7e5ec2c6a0">

### x-dave-gray/blogapp/src/EditPost.js:

```js
import { useEffect } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import { format } from "date-fns";
import { useStoreState, useStoreActions } from "easy-peasy";

const EditPost = () => {
  const navigate = useNavigate();
  const { id } = useParams();

  const editTitle = useStoreState((state) => state.editTitle);
  const editBody = useStoreState((state) => state.editBody);

  const editPost = useStoreActions((actions) => actions.editPost);
  const setEditTitle = useStoreActions((actions) => actions.setEditTitle);
  const setEditBody = useStoreActions((actions) => actions.setEditBody);

  const getPostById = useStoreState((state) => state.getPostById);
  const post = getPostById(id);

  useEffect(() => {
    if (post) {
      setEditTitle(post.title);
      setEditBody(post.body);
    }
  }, [post, setEditTitle, setEditBody]);

  const handleEdit = (id) => {
    const datetime = format(new Date(), "MMMM dd, yyyy pp");
    const updatedPost = { id, title: editTitle, datetime, body: editBody };
    editPost(updatedPost);
    navigate(`/post/${id}`);
  };

  return (
    <main className="NewPost">
      {editTitle && (
        <>
          <h2>Edit Post</h2>
          <form className="newPostForm" onSubmit={(e) => e.preventDefault()}>
            <label htmlFor="postTitle">Title:</label>
            <input
              id="postTitle"
              type="text"
              required
              value={editTitle}
              onChange={(e) => setEditTitle(e.target.value)}
            />
            <label htmlFor="postBody">Post:</label>
            <textarea
              id="postBody"
              required
              value={editBody}
              onChange={(e) => setEditBody(e.target.value)}
            />
            <button type="button" onClick={() => handleEdit(post.id)}>
              Submit
            </button>
          </form>
        </>
      )}
      {!editTitle && (
        <>
          <h2>Post Not Found</h2>
          <p>Well, that's disappointing.</p>
          <p>
            <Link to="/">Visit Our Homepage</Link>
          </p>
        </>
      )}
    </main>
  );
};

export default EditPost;
```

# #End  </details>

<details>
  <summary>69. Blog App - Refactoring Footer.js</summary>

# Refactoring Footer.js

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/217e3b05-057d-47c9-910b-07445d960faf">
<img width="1249" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f6e7ae23-cc45-4f37-9019-e2783b4bb946">

### x-dave-gray/blogapp/src/Footer.js:

```js
import { useStoreState } from "easy-peasy";

const Footer = () => {
  const postCount = useStoreState((state) => state.postCount);
  return (
    <footer className="Footer">
      <p>{postCount} Blog Posts</p>
    </footer>
  );
};

export default Footer;
```

# #End  </details>

+DEPLOY REACT

<details>
  <summary>70. Deploy React App to Netlify and Github Pages</summary>

# Deploy React App to Netlify and Github Pages

# Uninstall unused modules

```bs
npm uninstall @testing-library/jest-dom @testing-library/react @testing-library/user-event web-vitals
```

# Install JSON Server to Production

```bs
npm i json-server -S
json-server -p 3500 --watch data/db.json
json-server -p 3500 -w data/db.json
```

```bs
 npx json-server -p 3500 -w data/db.json
```

# Setup GIT & GitHub:

```bs
echo "# deploy_react_task_app" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/omeatai/deploy_react_task_app.git
git push -u origin main

OR

git remote add origin https://github.com/omeatai/deploy_react_task_app.git
git branch -M main
git push -u origin main
```

<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5c9b7ce8-e0ed-4404-a7f4-b4c5b25f4a36">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dc233f08-f535-4b43-a665-8f499b007837">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/75bb3b82-c0d8-48bf-bbd0-93f41b6d40a7">

# For Github-Pages:

```bs
npm i gh-pages -D
```

```bs
"homepage": "https://omeatai.github.io/deploy_react_blog_gh",

"predeploy": "npm run build",
"deploy": "gh-pages -d build",

"devDependencies": {
  "gh-pages": "^4.0.0"
}
```

```json
{
  "name": "blog",
  "version": "0.1.0",
  "homepage": "https://omeatai.github.io/deploy_react_blog_gh",
  "private": true,
  "dependencies": {
    "axios": "^1.2.1",
    "date-fns": "^2.29.3",
    "easy-peasy": "^5.2.0",
    "json-server": "^0.17.1",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-icons": "^4.7.1",
    "react-router-dom": "^6.5.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "predeploy": "npm run build",
    "deploy": "gh-pages -d build",
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": ["react-app", "react-app/jest"]
  },
  "browserslist": {
    "production": [">0.2%", "not dead", "not op_mini all"],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "gh-pages": "^4.0.0"
  }
}
```

```bs
echo "# deploy_react_blog_gh" >> README.md
git init
git add README.md OR git add .
git commit -m "first commit"
git branch -M main
git remote set-url origin https://github.com/omeatai/deploy_react_blog_gh.git
OR
git remote add origin https://github.com/omeatai/deploy_react_blog_gh.git
git push -u origin main
```

# Deploy App on GitHub Pages:

```bs
npm run deploy
```

```bs
Go to https://omeatai.github.io/deploy_react_blog_gh to view site.
```

# #End  </details>

+REACT-HOOKS

<details>
  <summary>71. Using PrevState to update React State Hooks </summary>

# Using PrevState to update React State Hooks

```js
import React, { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);
  const [values, setValues] = useState([]);
  const [names, setNames] = useState({
    firstName: "John",
    lastName: "Mcgrill",
  });

  const add = () => setCount((prevState) => prevState + 1);
  const subtract = () => setCount((prevState) => prevState - 1);
  const updateValue = (newVal) =>
    setValues((prevState) => [...prevState, newVal]);
  const updateName = (first, last) =>
    setNames((prevState) => ({
      ...prevState,
      firstName: first,
      lastName: last,
    }));

  return (
    <div className="Counter">
      <h1>Counter</h1>
      <h1>{count}</h1>
      <div className="row">
        <button onClick={add}>+</button>
        <button onClick={subtract}>-</button>
      </div>
      <div className="row">
        <button onClick={() => setCount(0)}>Reset</button>
      </div>
      <div>
        <h2>{values}</h2>
        <button onClick={() => updateValue(count)}>Update Value</button>
      </div>
      <div>
        <h2>
          {names.firstName} {names.lastName}
        </h2>
        <button onClick={() => updateName("Bob", "Ashley")}>Update Name</button>
      </div>
    </div>
  );
};

export default Counter;
```

# #End  </details>

<details>
  <summary>72. useCallback Hook</summary>

# Referential Equality

<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e379b602-25be-489b-af51-d42df311afd6">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1b8b3c39-1da9-467e-9b72-0ce952d94ab0">

# useCallback Hook

- useCallback provides a memoized function.
- useCallback is usually used when a function is used within a dependency array.
- The 'sum' function makes the dependencies of useEffect Hook change on every render.
- Move it inside the useEffect callback.
- Alternatively, wrap the definition of 'sum' in its own useCallback() Hook.

# Example 1 (no useCallback):

<img width="962" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3c117618-3ba3-428d-a986-e0140f1eab0f">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2f187652-7480-45bd-8458-bf1fa6ecaf36">

```js
import { useState, useEffect } from "react";

const Input = () => {
  const [userInput, setUserInput] = useState("");
  const [result, setResult] = useState(0);
  const [num1] = useState(4);
  const [num2] = useState(5);

  const sum = () => num1 + num2;

  useEffect(() => {
    console.log(`New sum. Value: ${sum()}`);
    setResult(sum());
  }, [sum]);

  return (
    <main className="App">
      <input
        type="text"
        placeholder="input"
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
      />
      <h1>Output: {userInput || "--"}</h1>
      <h2>{result}</h2>
    </main>
  );
};

export default Input;
```

# Example 2:

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b83c332a-991a-4d38-8911-8e54a835dcf6">
<img width="1177" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0faaa15c-84ff-4ee0-ab8e-21806177b5f9">

```js
import { useState, useEffect, useCallback } from "react";

const Input = () => {
  const [userInput, setUserInput] = useState("");
  const [result, setResult] = useState(0);
  const [num1] = useState(4);
  const [num2] = useState(5);

  const sum = useCallback(() => num1 + num2, [num1, num2]);

  useEffect(() => {
    console.log(`New sum. Value: ${sum()}`);
    setResult(sum());
  }, [sum]);

  return (
    <main className="App">
      <input
        type="text"
        placeholder="input"
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
      />
      <h1>Output: {userInput || "--"}</h1>
      <h2>{result}</h2>
    </main>
  );
};

export default Input;
```

# Example 3:

```js
import { useState, useEffect, useCallback } from "react";

const Input = () => {
  const [userInput, setUserInput] = useState("");
  const [result, setResult] = useState(0);
  const [num1] = useState(4);
  const [num2] = useState(5);

  const buildArray = useCallback(() => [num1, num2], [num1, num2]);

  useEffect(() => {
    console.log(`New sum. Value: ${buildArray()}`);
    setResult(buildArray());
  }, [buildArray]);

  return (
    <main className="Input">
      <input
        type="text"
        placeholder="input"
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
      />
      <h1>Output: {userInput || "--"}</h1>
      <h2>{result}</h2>
    </main>
  );
};

export default Input;
```

# Example 4:

```js
import { useState, useEffect, useCallback } from "react";

const App = () => {
  const [userInput, setUserInput] = useState("");
  const [result, setResult] = useState(0);
  const [num1] = useState(4);
  const [num2] = useState(5);

  //const sum = useCallback(() => num1 + num2, [num1, num2]);
  const buildArray = useCallback(() => [num1, num2], [num1, num2]);

  useEffect(() => {
    console.log(`New array: ${buildArray()}`);
    setResult(buildArray());
  }, [buildArray]);

  return (
    <main className="App">
      <input
        type="text"
        placeholder="input"
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
      />
      <h1>Output: {userInput || "--"}</h1>
      <p>Result: {JSON.stringify(result)}</p>
    </main>
  );
};

export default App;
```

### Index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 22px;
}

body {
  background-color: #000;
  color: #fff;
  min-height: 100vh;
  font-family: "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans",
    "Droid Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 1rem;
}

h1 {
  margin-bottom: 1rem;
}

button {
  min-width: 50px;
  padding: 1em;
  margin: 0.25em;
  border-radius: 0.5em;
}

input {
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.5em;
  margin-bottom: 1rem;
  outline: none;
}
```

# #End  </details>

<details>
  <summary>73. useMemo Hook</summary>

# useMemo Hook

- useMemo provides a memorized result.

### x-dave-gray/react-hooks/src/App.js:

```js
import UseMemo from "./Memo";

function App() {
  return (
    <div className="App">
      <UseMemo />
    </div>
  );
}

export default App;
```

### x-dave-gray/react-hooks/src/Memo.js:

# Example 1 (Without useMemo):

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c1abf3c6-849b-4cae-b883-5d62d8af8bb4">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/24e2c53d-66d2-4bcf-9a53-21916accaaae">

```js
import { useState, useEffect, useCallback } from "react";

const UseMemo = () => {
  const [userNumber, setUserNumber] = useState("");
  const [randomInput, setRandomInput] = useState("");

  const fib = useCallback((n) => {
    return n <= 1 ? n : fib(n - 1) + fib(n - 2);
  }, []);

  const getArray = () => {
    for (let i = 0; i < 1000000000; i++) {
      //do something expensive
    }
    return ["Dave", "Gray"];
  };

  const fibNumber = fib(userNumber);

  const myArray = getArray();

  useEffect(() => {
    console.log("new number");
    console.log("my Array");
  }, [fibNumber, fib, myArray]);

  return (
    <main className="App">
      <label>Fibonacci Sequence: </label>
      <input
        type="number"
        value={userNumber}
        placeholder="Position"
        onChange={(e) => setUserNumber(e.target.value)}
      />
      <p>Number: {fibNumber || "--"}</p>
      <br />
      <br />
      <label>Random Input: </label>
      <input
        type="text"
        value={randomInput}
        placeholder="Random Input"
        onChange={(e) => setRandomInput(e.target.value)}
      />
      <p>{randomInput}</p>
    </main>
  );
};

export default UseMemo;
```

# Example 2:

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5a35b2f0-c4f3-4f59-ace3-cf50f513af26">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/001321b1-9494-4b9f-833a-9fc2babc7674">

```js
import { useCallback } from "react";
import { useState, useEffect, useMemo } from "react";

const UseMemo = () => {
  const [userNumber, setUserNumber] = useState("");
  const [randomInput, setRandomInput] = useState("");

  const fib = useCallback((n) => {
    return n <= 1 ? n : fib(n - 1) + fib(n - 2);
  }, []);

  const getArray = () => {
    for (let i = 0; i < 1000000000; i++) {
      //do something expensive
    }
    return ["Dave", "Gray"];
  };

  const fibNumber = useMemo(() => fib(userNumber), [fib, userNumber]);

  const myArray = useMemo(() => getArray(), []);

  useEffect(() => {
    console.log("new number");
    console.log("my Array");
  }, [fibNumber, fib, myArray]);

  return (
    <main className="App">
      <label>Fibonacci Sequence: </label>
      <input
        type="number"
        value={userNumber}
        placeholder="Position"
        onChange={(e) => setUserNumber(e.target.value)}
      />
      <p>Number: {fibNumber || "--"}</p>
      <br />
      <br />
      <label>Random Input: </label>
      <input
        type="text"
        value={randomInput}
        placeholder="Random Input"
        onChange={(e) => setRandomInput(e.target.value)}
      />
      <p>{randomInput}</p>
    </main>
  );
};

export default UseMemo;
```

# Example 3:

```js
import { useState, useEffect, useMemo, useCallback } from "react";

const getArray = () => {
  for (let i = 0; i < 1000000000; i++) {
    //do something expensive
  }
  return ["Dave", "Gray"];
};

const UseMemo = () => {
  const [userNumber, setUserNumber] = useState("");
  const [randomInput, setRandomInput] = useState("");

  const fib = useCallback((n) => {
    return n <= 1 ? n : fib(n - 1) + fib(n - 2);
  }, []);

  const fibNumber = useMemo(() => fib(userNumber), [userNumber, fib]);

  const myArray = useMemo(() => getArray(), []);

  useEffect(() => {
    console.log("New array");
  }, [myArray]);

  return (
    <main className="App">
      <label>Fibonacci Sequence:</label>
      <input
        type="number"
        value={userNumber}
        placeholder="Position"
        onChange={(e) => setUserNumber(e.target.value)}
      />
      <p>Number: {fibNumber || "--"}</p>
      <br />
      <br />
      <label>Random Input:</label>
      <input
        type="text"
        value={randomInput}
        placeholder="Random Input"
        onChange={(e) => setRandomInput(e.target.value)}
      />
      <p>{randomInput}</p>
    </main>
  );
};

export default UseMemo;
```

Index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 22px;
}

body {
  background-color: #000;
  color: #fff;
  min-height: 100vh;
  font-family: "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans",
    "Droid Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 1rem;
}

h1 {
  margin-bottom: 1rem;
}

button {
  min-width: 50px;
  padding: 1em;
  margin: 0.25em;
  border-radius: 0.5em;
}

input {
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.5em;
  margin-bottom: 1rem;
  outline: none;
}
```

# #End  </details>

<details>
  <summary>74. useRef Hook</summary>

# useRef Hook

- useRef value persists (stays the same btw renders.
- A change in useRef value does not trigger a rerender.

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/cf56c225-6dff-4166-a81b-fd033af83483">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fba6347f-2ff7-4a8d-af69-8e11e8dd1fe3">

# Example 1:

```js
import { useState, useRef } from "react";

const UseRef = () => {
  const [randomInput, setRandomInput] = useState("");
  const [seconds, setSeconds] = useState(0);

  const renders = useRef(0);
  const inputRef = useRef();
  const timerId = useRef();

  const handleChange = (e) => {
    setRandomInput(e.target.value);
    renders.current++;
  };

  const startTimer = () => {
    timerId.current = setInterval(() => {
      renders.current++;
      setSeconds((prev) => prev + 1);
    }, 1000);
    inputRef.current.focus();
  };

  const stopTimer = () => {
    clearInterval(timerId.current);
    timerId.current = 0;
    inputRef.current.focus();
  };

  const resetTimer = () => {
    stopTimer();
    if (seconds) {
      renders.current++;
      setSeconds(0);
    }
    inputRef.current.focus();
  };

  return (
    <main className="App">
      <input
        ref={inputRef}
        type="text"
        value={randomInput}
        placeholder="Random Input"
        onChange={handleChange}
      />
      <p>Renders: {renders.current}</p>
      <br />
      <br />
      <section>
        <button onClick={startTimer}>Start</button>
        <button onClick={stopTimer}>Stop</button>
        <button onClick={resetTimer}>Reset</button>
      </section>
      <br />
      <br />
      <p>Seconds: {seconds}</p>
      <br />
      <br />
      <p>{randomInput}</p>
    </main>
  );
};

export default UseRef;
```

# Example 2:

```js
import { useState, useRef } from "react";

function UseRef() {
  const [randomInput, setRandomInput] = useState("");
  const [seconds, setSeconds] = useState(0);

  const renders = useRef(0);
  const inputRef = useRef();
  const timerId = useRef();

  const handleChange = (e) => {
    setRandomInput(e.target.value);
    renders.current++;
  };

  const startTimer = () => {
    timerId.current = setInterval(() => {
      renders.current++;
      setSeconds((prev) => prev + 1);
    }, 1000);
    inputRef.current.focus();
  };

  const stopTimer = () => {
    clearInterval(timerId.current);
    timerId.current = 0;
    inputRef.current.focus();
  };

  const resetTimer = () => {
    stopTimer();
    if (seconds) {
      renders.current++;
      setSeconds(0);
    }
    inputRef.current.focus();
  };

  return (
    <main className="App">
      <input
        ref={inputRef}
        type="text"
        value={randomInput}
        placeholder="Random Input"
        onChange={handleChange}
      />
      <p>Renders: {renders.current}</p>
      <br />
      <br />
      <section>
        <button onClick={startTimer}>Start</button>
        <button onClick={stopTimer}>Stop</button>
        <button onClick={resetTimer}>Reset</button>
      </section>
      <br />
      <br />
      <p>Seconds: {seconds}</p>
      <br />
      <br />
      <p>{randomInput}</p>
    </main>
  );
}

export default UseRef;
```

# Index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 36px;
}

body {
  background-color: #000;
  color: #fff;
  min-height: 100vh;
  font-family: "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans",
    "Droid Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 1rem;
}

h1 {
  margin-bottom: 1rem;
}

section {
  display: flex;
  justify-content: center;
  align-items: center;
}

button {
  font-size: 1rem;
  width: 150px;
  padding: 1em;
  margin: 0.25em;
  border-radius: 0.5em;
  display: grid;
  place-content: center;
}

input {
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.5em;
  margin-bottom: 1rem;
  outline: none;
}
```

# #End  </details>

<details>
  <summary>75. useReducer Hook</summary>

# useReducer Hook

<img width="965" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/251f5da9-88ad-458f-843a-6ba74c353fc5">
<img width="1177" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f4916527-57ca-4b48-ba4a-dff264d2bb21">

# Example 1:

```js
import { useReducer } from "react";

const ACTION = {
  INCREMENT: "increment",
  DECREMENT: "decrement",
  NEW_USER_INPUT: "newUserInput",
  TG_COLOR: "tgColor",
};

const reducer = (state, action) => {
  switch (action.type) {
    case ACTION.INCREMENT:
      return { ...state, count: state.count + 1 };
    case ACTION.DECREMENT:
      return { ...state, count: state.count - 1 };
    case ACTION.NEW_USER_INPUT:
      return { ...state, userInput: action.payload };
    case ACTION.TG_COLOR:
      return { ...state, color: !state.color };
    default:
      throw new Error();
  }
};

const UseReducer = () => {
  const [state, dispatch] = useReducer(reducer, {
    count: 0,
    userInput: "",
    color: false,
  });

  return (
    <main className="App" style={{ color: state.color ? "#FFF" : "#FFF952" }}>
      <input
        type="text"
        value={state.userInput}
        onChange={(e) =>
          dispatch({ type: ACTION.NEW_USER_INPUT, payload: e.target.value })
        }
      />
      <br />
      <br />
      <p>{state.count}</p>
      <section>
        <button onClick={() => dispatch({ type: ACTION.DECREMENT })}>-</button>
        <button onClick={() => dispatch({ type: ACTION.INCREMENT })}>+</button>
        <button onClick={() => dispatch({ type: ACTION.TG_COLOR })}>
          Color
        </button>
      </section>
      <br />
      <br />
      <p>{state.userInput}</p>
    </main>
  );
};

export default UseReducer;
```

# Index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 36px;
}

body {
  background-color: #000;
  color: #fff;
  min-height: 100vh;
  font-family: "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans",
    "Droid Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 1rem;
}

h1 {
  margin-bottom: 1rem;
}

section {
  display: flex;
  justify-content: center;
  align-items: center;
}

button {
  font-size: 1rem;
  min-width: 100px;
  padding: 0.25rem;
  margin: 0.25em;
  border-radius: 0.5em;
  display: grid;
  place-content: center;
}

input {
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.5em;
  margin-bottom: 1rem;
  outline: none;
}
```

# #End  </details>

<details>
  <summary>76. useLayoutEffect Hook</summary>

# useLayoutEffect Hook

- useLayoutEffect is Synchorous, which means it will delay running the DOM to the browser until it has concluded its operation;
- unlike useEffect, which is Asynchronous, it will allow changes to the DOM while processing its operation.
- useLayoutEffect denies the user from observing changes to state on the browser unlike useEffect which makes the changes noticable on the browser.

# Example 1:

```js
import { useState, useRef, useEffect, useLayoutEffect } from "react";

function UseLayoutEffect() {
  const [number, setNumber] = useState(0);
  const [sectionStyle, setSectionStyle] = useState({});
  const sectionRef = useRef();

  /*
  useEffect is asynchronous.
  You see the number change in the DOM before the padding changes.

  useLayoutEffect is synchronous.
  You see the number change only after the padding has changed.
  */

  // change to useLayoutEffect to see the difference
  useLayoutEffect(() => {
    const random = Math.floor(Math.random() * 500);

    /* loop is just to make the changes in this example slow enough to be observable */
    for (let i = 0; i <= 100000000; i++) {
      if (i === 100000000) setSectionStyle({ paddingTop: `${random}px` });
    }
  }, [number]);

  return (
    <main className="App">
      <section ref={sectionRef} style={sectionStyle}>
        <p>{number}</p>
        <div>
          <button onClick={() => setNumber((prev) => prev - 1)}>-</button>
          <button onClick={() => setNumber((prev) => prev + 1)}>+</button>
        </div>
      </section>
    </main>
  );
}

export default UseLayoutEffect;
```

# Index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 48px;
}

body {
  background-color: #000;
  color: #fff;
  min-height: 100vh;
  font-family: "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans",
    "Droid Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#root {
  min-height: inherit;
}

.App {
  min-height: inherit;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 1rem;
}

h1 {
  margin-bottom: 1rem;
}

button {
  min-width: 75px;
  padding: 1em;
  margin: 0.25em;
  border-radius: 0.5em;
  font-size: 0.5rem;
}

input {
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.5em;
  margin-bottom: 1rem;
  outline: none;
}

p {
  text-align: center;
}
```

# #End  </details>

<details>
  <summary>77. useImperativeHandle Hook</summary>

# useImperativeHandle Hook

- useImperativeHandle enables the Child state to be changed by the Parent. It calls a function from the Parent component that is defined in the Child component.

# UseImperativeHandle.js:

```js
import { useRef } from "react";
import Modal from "./Modal";

function UseImperativeHandle() {
  const modalRef = useRef();

  const handleOpenModal = () => {
    modalRef.current.openModal();
  };

  console.log("parent rendered");

  return (
    <main className="App">
      <p>Parent Component</p>
      <Modal ref={modalRef} />
      <button onClick={handleOpenModal}>Open</button>
    </main>
  );
}

export default UseImperativeHandle;
```

# Modal.js:

```js
import { forwardRef, useImperativeHandle, useState } from "react";

const Modal = (props, ref) => {
  const [modalState, setModalState] = useState(false);

  useImperativeHandle(ref, () => ({
    openModal: () => setModalState(true),
  }));

  console.log("child rendered");

  if (!modalState) return null;

  return (
    <div className="modal">
      <p>This is my modal!</p>
      <button onClick={() => setModalState(false)}>Close</button>
    </div>
  );
};

export default forwardRef(Modal);
```

# Index.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 48px;
}

body {
  background-color: #000;
  color: #fff;
  min-height: 100vh;
  font-family: "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans",
    "Droid Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#root {
  min-height: inherit;
}

.App {
  min-height: inherit;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

h1 {
  margin-bottom: 1rem;
}

button {
  min-width: 75px;
  padding: 1em;
  margin: 0.25em;
  border-radius: 0.5em;
  font-size: 0.5rem;
}

input {
  font-size: 1rem;
  padding: 0.25rem;
  border-radius: 0.5em;
  margin-bottom: 1rem;
  outline: none;
}

p {
  text-align: center;
}

.modal {
  z-index: 1;
  position: absolute;
  top: 50;
  left: 50;
  display: grid;
  place-content: center;
  min-height: 400px;
  min-width: 400px;
  border-radius: 1.5rem;
  background-color: papayawhip;
  color: #000;
  box-shadow: 0 0 40px #fff;
  margin: 1rem;
  padding: 0.25rem;
}
```

# #End  </details>

<details>
  <summary>78. useTransition vs useDeferredValue</summary>

# useTransition vs useDeferredValue

# App.js:

```js
import Example1 from "./Example1";
import Example2 from "./Example2";

const App = () => {
  return <Example1 />;
};

export default App;
```

# Example 1:

```js
import { useState, useTransition, useDeferredValue } from "react";

const Example1 = () => {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState([]);
  const [isPending, startTransition] = useTransition();
  const deferredCount = useDeferredValue(count);

  const handleClick = () => {
    // urgent update
    setCount(count + 1);
    // transition update
    startTransition(() => {
      const myArr = Array(20000)
        .fill(1)
        .map((el, i) => count + 20000 - i);
      setItems(myArr);
    });
  };

  const content = (
    <div className="App">
      <button onClick={handleClick}>{count}</button>
      {isPending ? <p>Loading...</p> : null}
      <p>Deferred: {deferredCount}</p>
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  );

  return content;
};
export default Example1;
```

# Example2 :

```js
import { useDeferredValue, useState, useTransition, useEffect } from "react";

const bigArray = [...Array(20000).keys()];

const Example2 = () => {
  const [inputValue, setInputValue] = useState("");
  const [list, setList] = useState(bigArray);
  const [isPending, startTransition] = useTransition();
  const deferredInput = useDeferredValue(inputValue);

  const handleInput = (e) => {
    setInputValue(e.target.value);
  };

  useEffect(() => {
    startTransition(() => {
      console.log(deferredInput);
      const filtered = bigArray.filter((item) =>
        item.toString().includes(deferredInput)
      );
      setList(filtered);
    });
  }, [deferredInput]);

  const content = (
    <section style={isPending ? { opacity: 0.4 } : null}>
      <p>Searching for: {deferredInput || "All"}</p>
      {isPending ? <p>Loading...</p> : null}
      <ul>
        {list.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </section>
  );

  return (
    <div className="App">
      <input type="text" val={inputValue} onChange={handleInput} />
      {content}
    </div>
  );
};
export default Example2;
```

# Index.css:

```css
body {
  background-color: #333;
  color: whitesmoke;
  font-size: 2rem;
  padding: 2rem;
}

input,
button {
  font: inherit;
  padding: 1rem;
}

button {
  display: block;
  margin-bottom: 1rem;
}
```

# #End  </details>

# NODE

+NODE INTRODUCTION

<details>
  <summary>79. Node - Introduction </summary>

# Node - Introduction

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/328bbab0-7318-4f9d-9b5b-9b62f1fc245d">

# Install and Check Node Version

```jsbs
nvm install <version>
nvm use <version>
nvm ls
node -v
```

### server.js:

```js
console.log("Hello world!");
console.log(global);
```

# Run Node Server

```jsbs
node server
```

# output

```js
// Hello world!
//
// <ref *1> Object [global] {
//   global: [Circular *1],
//   clearInterval: [Function: clearInterval],
//   clearTimeout: [Function: clearTimeout],
//   setInterval: [Function: setInterval],
//   setTimeout: [Function: setTimeout] {
//     [Symbol(nodejs.util.promisify.custom)]: [Getter]
//   },
//   queueMicrotask: [Function: queueMicrotask],
//   performance: Performance {
//     nodeTiming: PerformanceNodeTiming {
//       name: 'node',
//       entryType: 'node',
//       startTime: 0,
//       duration: 115.58020782470703,
//       nodeStart: 26.828166007995605,
//       v8Start: 44.619500160217285,
//       bootstrapComplete: 102.09924983978271,
//       environment: 61.474082946777344,
//       loopStart: -1,
//       loopExit: -1,
//       idleTime: 0
//     },
//     timeOrigin: 1672901956430.907
//   },
//   clearImmediate: [Function: clearImmediate],
//   setImmediate: [Function: setImmediate] {
//     [Symbol(nodejs.util.promisify.custom)]: [Getter]
//   }
// }
```

# #End </details>

<details>
  <summary>80. Node - The OS Object, dirname and filename </summary>

# OS Object, dirname and filename

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1b7304d1-08e9-408a-a488-d661fd1d4147">

### server.js:

```js
const os = require("os");

console.log(1, __dirname);
console.log(2, __filename);

console.log(3, os.type());
console.log(4, os.version());
console.log(5, os.homedir());

console.log(6, os.hostname());
console.log(7, os.platform());
console.log(8, os.userInfo());
console.log(9, os.release());
console.log(10, os.uptime());

// console.log(os.arch());
// console.log(os.cpus());
// console.log(os.endianness());
// console.log(os.freemem());
// console.log(os.getPriority());
// console.log(os.loadavg());
// console.log(os.networkInterfaces());
// console.log(os.totalmem());
```

# Run Node Server

```jsbs
node server
```

# output

```js
// 1 /Users/ifeanyi/Desktop/SERVER/Cloud/Labs/nodeproj
// 2 /Users/ifeanyi/Desktop/SERVER/Cloud/Labs/nodeproj/server.js
// 3 Darwin
// 4 Darwin Kernel Version 19.2.0: Mon Feb 19 20:36:53 PST 2020; root:xnu-4030.151.4~2
// 5 /Users/ifeanyi
// 6 Gmais-MacBook-Air.local
// 7 darwin
// 8  {
//      uid: 503,
//      gid: 25,
//      username: 'ifeanyi',
//      homedir: '/Users/ifeanyi',
//      shell: '/bin/zsh'
//    }
// 9 19.4.0
// 10 1939936
```

# #End </details>

<details>
  <summary>81. Node - The Path Object</summary>

# The Path Object

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7e9e3fde-7314-47bb-82ec-e175f5b9b441">

### server.js:

```js
const os = require("os");
const path = require("path");

console.log(1, __dirname);
console.log(2, __filename);

console.log(3, path.dirname(__filename));
console.log(4, path.basename(__filename));
console.log(5, path.extname(__filename));
console.log(6, path.parse(__filename));
```

# Run Node Server

```jsbs
node server
```

# output

```js
// 1 /Users/ifeanyiomeata/Desktop/SERVER/Cloud/Labs/nodeproj
// 2 /Users/ifeanyiomeata/Desktop/SERVER/Cloud/Labs/nodeproj/server.js

// 3 /Users/ifeanyiomeata/Desktop/SERVER/Cloud/Labs/nodeproj
// 4 server.js
// 5 .js
// 6 {
//   root: '/',
//   dir: '/Users/ifeanyiomeata/Desktop/SERVER/Cloud/Labs/nodeproj',
//   base: 'server.js',
//   ext: '.js',
//   name: 'server'
// }
```

# #End </details>

<details>
  <summary>82. Node - Export Modules </summary>

# Export Modules Object

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0d555cbd-4161-46d3-8b39-6108aa763842">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/047052e0-1935-4e71-be4d-ecef590ee968">

### math.js:

```js
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;
const multiply = (a, b) => a * b;
const divide = (a, b) => a / b;

module.exports = { add, subtract, multiply, divide };

// exports.add = (a, b) => a + b;
// exports.subtract = (a, b) => a - b;
// exports.multiply = (a, b) => a * b;
// exports.divide = (a, b) => a / b;
```

### server.js:

```js
const os = require("os");
const path = require("path");

const { add, subtract, multiply, divide } = require("./math");

console.log(add(3, 2));
console.log(subtract(3, 2));
console.log(multiply(3, 2));
console.log(divide(3, 2));
```

# Run Node Server

```jsbs
node server
```

# output

```js
// 5
// 1
// 6
// 1.5
```

# #End </details>

<details>
  <summary>83. Node - Read File with fs.readFile()</summary>

# Read File with fs.readFile()

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9bef1b9c-65cc-47a3-b4b1-ecb5c6667318">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1be14a09-a251-4f34-a489-85fa3961b841">

### x-dave-gray/node-app/files/starter.txt:

```txt
Hello, my name is Ifeanyi.
```

### x-dave-gray/node-app/index.js:

```js
const fs = require("fs");

fs.readFile("./files/starter.txt", "utf8", (err, data) => {
  if (err) throw err;
  console.log(data);
  //console.log(data.toString());
});

// exit on uncaught errors
process.on("uncaughtException", (err) => {
  console.error(`There was an uncaught error: ${err}`);
  process.exit(1);
});
```

# Run Node Server

```jsbs
node index
```

# output

```js
// Hello, my name is Ifeanyi.
```

# #End </details>

<details>
  <summary>84. Node - Read File with path.join() and fs.readFile() </summary>

# Read File with path.join() and fs.readFile()

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/76e62665-d552-4eb3-8f0a-1c0a394f2a7a">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/72deaf06-a161-4a26-b2a6-ebc946b988e2">

### x-dave-gray/node-app/files/starter.txt:

```txt
Hello, my name is Ifeanyi.
```

### x-dave-gray/node-app/index.js:

```js
const fs = require("fs");
const path = require("path");

fs.readFile(
  path.join(__dirname, "files", "starter.txt"),
  "utf8",
  (err, data) => {
    if (err) throw err;
    console.log(data);
    //console.log(data.toString());
  }
);

// exit on uncaught errors
process.on("uncaughtException", (err) => {
  console.error(`There was an uncaught error: ${err}`);
  process.exit(1);
});
```

# Run Node Server

```jsbs
node index
```

# output

```js
// Hello, my name is Ifeanyi.
```

# #End </details>

<details>
  <summary>85. Node - Write File with fs.writeFile() </summary>

# Write File with fs.writeFile()

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8e4f295b-9fbe-4abe-85d8-e23f29980f3e">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ed62ebfe-3500-4f52-ae6d-1c72a51b2ef1">

### x-dave-gray/node-app/index.js:

```js
const fs = require("fs");
const path = require("path");

fs.writeFile(
  path.join(__dirname, "files", "reply.txt"),
  "Nice to meet you!",
  (err) => {
    if (err) throw err;
    console.log("Write Complete.");
  }
);

// exit on uncaught errors
process.on("uncaughtException", (err) => {
  console.error(`There was an uncaught error: ${err}`);
  process.exit(1);
});
```

# Run Node Server

```jsbs
node index
```

# output

```js
// Write Complete.
```

# #End </details>

<details>
  <summary>86. Node - Update File with fs.appendFile()</summary>

# Update File with fs.appendFile()

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/cab4e172-d5b4-486d-94b5-65dbf0d921ed">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c587d78f-a7b0-40d7-8dbf-b0c403a9aa77">

### x-dave-gray/node-app/index.js:

```js
const fs = require("fs");
const path = require("path");

fs.appendFile(
  path.join(__dirname, "files", "reappend.txt"),
  "Hello, Nice to meet you Again!",
  (err) => {
    if (err) throw err;
    console.log("Append Complete.");
  }
);

// exit on uncaught errors
process.on("uncaughtException", (err) => {
  console.error(`There was an uncaught error: ${err}`);
  process.exit(1);
});
```

# Run Node Server

```jsbs
node index
```

# output

```js
// Append Complete.
```

# #End </details>

<details>
  <summary>87. Node - Write + Update (Append) File Sync order</summary>

# Write + Update File Sync order

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2bd8b530-f1ca-47e0-a702-99c6e99467e8">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/075f0590-dee1-45c3-9af7-9712b5596f1e">

### x-dave-gray/node-app/index.js:

```js
const fs = require("fs");
const path = require("path");

//Write File
fs.writeFile(
  path.join(__dirname, "files", "reply.txt"),
  "Nice to meet you Bob!",
  (err) => {
    if (err) throw err;
    console.log("Write Complete.");

    //Append to File
    fs.appendFile(
      path.join(__dirname, "files", "reply.txt"),
      "\n\nYou really have a great car!",
      (err) => {
        if (err) throw err;
        console.log("Append Complete.");
      }
    );
  }
);

// exit on uncaught errors
process.on("uncaughtException", (err) => {
  console.error(`There was an uncaught error: ${err}`);
  process.exit(1);
});
```

# Run Node Server

```jsbs
node index
```

# output

```js
// Write Complete.
// Append Complete.
```

# #End </details>

<details>
  <summary>88. Node - Write + Update + Rename File Sync order</summary>

# Write + Update + Rename File Sync order

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/afa736d9-d332-424b-bbff-2e19377e0487">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e04243e1-72fe-4330-b9ce-3399230c52aa">

### x-dave-gray/node-app/index.js:

```js
const fs = require("fs");
const path = require("path");

//Write File
fs.writeFile(
  path.join(__dirname, "files", "reply.txt"),
  "Nice to meet you Bob!",
  (err) => {
    if (err) throw err;
    console.log("Write Complete.");

    //Append to File
    fs.appendFile(
      path.join(__dirname, "files", "reply.txt"),
      "\n\nYou really have a great car!",
      (err) => {
        if (err) throw err;
        console.log("Append Complete.");

        //Rename File
        fs.rename(
          path.join(__dirname, "files", "reply.txt"),
          path.join(__dirname, "files", "newReply.txt"),
          (err) => {
            if (err) throw err;
            console.log("Rename Complete.");
          }
        );
      }
    );
  }
);

// exit on uncaught errors
process.on("uncaughtException", (err) => {
  console.error(`There was an uncaught error: ${err}`);
  process.exit(1);
});
```

# Run Node Server

```jsbs
node index
```

# output

```js
// Write Complete.
// Append Complete.
// Rename Complete.
```

# #End </details>

<details>
  <summary>89. Node - Read File with Promises</summary>

# Read File with Promises

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f54a4295-5de6-419a-baf9-7c45e7843b96">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c2af22a1-eb7c-47cf-b46a-8b6337a77f52">

### x-dave-gray/node-app/files/starter.txt:

```txt
Hello, my name is Ifeanyi.
```

### x-dave-gray/node-app/index.js:

```js
const fsPromises = require("fs").promises;
const path = require("path");

const fileOps = async () => {
  try {
    const data = await fsPromises.readFile(
      path.join(__dirname, "files", "starter.txt"),
      "utf8"
    );
    console.log(data);
  } catch (err) {
    console.error(err);
  }
};

fileOps();
```

# Run Node Server

```jsbs
node index
```

# output

```js
// Hello, my name is Ifeanyi.
```

# #End </details>

<details>
  <summary>90. Node - Read + Delete + Write + Update + Rename File with Promises</summary>

# Read + Delete + Write + Update + Rename File with Promises

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/409a25d1-5472-4001-8542-bc5366f86e4e">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/958c35b7-d1c1-4ab1-baea-12fe8c1eab1d">

### x-dave-gray/node-app/files/starter.txt:

```txt
Hello, my name is Ifeanyi.
```

### x-dave-gray/node-app/index.js:

```js
const fsPromises = require("fs").promises;
const path = require("path");

const fileOps = async () => {
  try {
    //Read File
    const data = await fsPromises.readFile(
      path.join(__dirname, "files", "starter.txt"),
      "utf8"
    );
    console.log("#### OLD ####");
    console.log(data);

    //Delete old File
    await fsPromises.unlink(path.join(__dirname, "files", "starter.txt"));

    //Write new File
    await fsPromises.writeFile(
      path.join(__dirname, "files", "promiseWrite.txt"),
      data
    );

    //Update new File
    await fsPromises.appendFile(
      path.join(__dirname, "files", "promiseWrite.txt"),
      "\n\nNice to meet you."
    );

    //Rename new File
    await fsPromises.rename(
      path.join(__dirname, "files", "promiseWrite.txt"),
      path.join(__dirname, "files", "promiseComplete.txt")
    );

    //Read the new File
    const newData = await fsPromises.readFile(
      path.join(__dirname, "files", "promiseComplete.txt"),
      "utf8"
    );
    console.log("#### NEW ####");
    console.log(newData);
  } catch (err) {
    console.error(err);
  }
};

fileOps();
```

# Run Node Server

```jsbs
node index
```

# output

```js
// #### OLD ####
// Hello, my name is Ifeanyi.
// #### NEW ####
// Hello, my name is Ifeanyi.
//
// Nice to meet you.
```

# #End </details>

<details>
  <summary>91. Node - Read and Write streams for large files with DataChunks</summary>

# Read and Write streams for large files with DataChunks

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/11d11af2-2a36-4c08-a4ce-b786ce270c48">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/439e4317-4ad4-4ec9-9279-635c26154d69">

### x-dave-gray/node-app/files/lorem.txt:

```js
Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis
obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam
nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,
tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit,
quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos
sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
recusandae alias error harum maxime adipisci amet laborum.
```

### x-dave-gray/node-app/stream.js:

```js
const fs = require("fs");
const path = require("path");

const rs = fs.createReadStream(path.join(__dirname, "files", "lorem.txt"), {
  encoding: "utf8",
});

const ws = fs.createWriteStream(path.join(__dirname, "files", "new-lorem.txt"));
let count = 0;

rs.on("data", (dataChunk) => {
  try {
    ws.write(dataChunk);
    count += 1;
    //   console.log(dataChunk);
  } catch (err) {
    console.error(err);
  } finally {
    console.log(`Completed Chunk: ${count}`);
  }
});
```

# Run Node Server

```bs
node stream
```

# output

```js
// Completed Chunk: 1
// Completed Chunk: 2
// Completed Chunk: 3
// Completed Chunk: 4
```

# #End </details>

<details>
  <summary>92. Node - Read and Write streams for large files with Pipes </summary>

# Read and Write streams for large files with Pipes

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4aefcb6b-378c-49e0-b42d-3b11d3c22c7b">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/70ccbdf1-898f-4e8d-80ba-acd23f20072a">

### x-dave-gray/node-app/files/lorem.txt:

```js
Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis
obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam
nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,
tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit,
quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos
sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
recusandae alias error harum maxime adipisci amet laborum.
```

### x-dave-gray/node-app/stream.js:

```js
const fs = require("fs");
const path = require("path");

const rs = fs.createReadStream(path.join(__dirname, "files", "lorem.txt"), {
  encoding: "utf8",
});

const ws = fs.createWriteStream(path.join(__dirname, "files", "new-lorem.txt"));

try {
  rs.pipe(ws);
} catch (err) {
  console.error(err);
} finally {
  console.log(`Completed Streaming.`);
}
```

# Run Node Server

```bs
node stream
```

# output

```js
// Completed Streaming.
```

# #End </details>

<details>
  <summary>93. Node - Create Folder/Directory </summary>

# Create Folder/Directory

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d56c2223-a4ab-4833-9021-32946218c8a1">

### x-dave-gray/node-app/index.js:

```js
const fs = require("fs");

fs.mkdir("./newdir", (err) => {
  if (err) throw err;
  console.log("Directory created");
});
```

# Run Node Server

```bs
node index
```

# output

```js
// Directory created
```

# #End </details>

<details>
  <summary>94. Node - Find out if Folder Directory Exists</summary>

# Find out if Folder Directory Exists

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/135ec961-0598-4cc1-a41f-0f74ebec9ab1">

### x-dave-gray/node-app/index.js:

```js
const fs = require("fs");

if (!fs.existsSync("./newdir")) {
  fs.mkdir("./newdir", (err) => {
    if (err) throw err;
    console.log("Directory created");
  });
} else {
  console.log("Directory already exists");
}
```

# Run Node Server

```bs
node index
```

# output

```js
// Directory already exists
```

# #End </details>

<details>
  <summary>95. Node - Delete Folder Directory</summary>

# Delete Folder Directory

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f6ae5c4b-07bd-44c8-905a-d55f394f9663">

### x-dave-gray/node-app/index.js:

```js
const fs = require("fs");

if (fs.existsSync("./newdir")) {
  fs.rmdir("./newdir", (err) => {
    if (err) throw err;
    console.log("Directory deleted successfully");
  });
}
```

# Run Node Server

```bs
node index
```

# output

```js
// Directory deleted successfully
```

# #End </details>

+NODE NPM

<details>
  <summary>96. Node NPM - Nodemon</summary>

# Nodemon

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c2778f6e-2791-4e28-9bd5-cebdf2c4a16d">

# NPM Initialization:

```bs
npm init -y
```

# Setup .gitignore

.gitignore:

```bs
node_modules
```

# Install Nodemon:

```bs
<!-- Global Dependency  -->
npm install -g nodemon

<!-- Production  -->
npm install --save nodemon
npm install -S nodemon

<!-- Development -->
npm install --save-dev nodemon
npm install -D nodemon
```

# Set Scripts

### x-dave-gray/node-app/package.json:

```json
{
  "name": "app",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server",
    "dev": "nodemon server"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "nodemon": "^3.0.1"
  }
}
```

### x-dave-gray/node-app/server.js:

```bs
console.log(3 + 2);
console.log(3 - 2);
console.log(3 * 2);
console.log(3 / 2);
```

# Start Nodemon Server:

```bs
npm run dev
OR
nodemon server.js
```

# output

```js
// [nodemon] 3.0.1
// [nodemon] to restart at any time, enter `rs`
// [nodemon] watching path(s): *.*
// [nodemon] watching extensions: js,mjs,cjs,json
// [nodemon] starting `node server.js`
// 5
// 1
// 6
// 1.5
// [nodemon] clean exit - waiting for changes before restart
```

# #End </details>

<details>
  <summary>97. Node NPM - Date-fns </summary>

# Date-fns

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/81c16523-9d44-4fd7-8f7b-177504b32c99">

# Install date-fns:

```bs
npm install date-fns --save
npm install date-fns --S
```

### x-dave-gray/node-app/server.js:

```js
const { compareAsc, format } = require("date-fns");

console.log(format(new Date(), "yyyyMMdd\tHH:mm:ss")); // 20230717  14:01:24
console.log(format(new Date(2014, 1, 11), "yyyy-MM-dd")); // '2014-01-11'

const dates = [
  new Date(1995, 6, 2),
  new Date(1987, 1, 11),
  new Date(1989, 6, 10),
];

console.log(dates.sort(compareAsc));

// [
//     1987-02-10T23:00:00.000Z,
//     1989-07-09T23:00:00.000Z,
//     1995-07-01T23:00:00.000Z
// ]
```

# output

```js
// 20230105        15:11:20
```

# #End </details>

<details>
  <summary>98. Node NPM - NPM UUID</summary>

# NPM UUID

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/58150c46-1407-4032-ac46-ca8b191c364d">

# Install UUID:

```bs
npm i uuid
npm i uuid@8.3.2
npm i uuid@latest
```

### x-dave-gray/node-app/server.js:

```js
const { format } = require("date-fns");
const { v4: uuidv4 } = require("uuid");

uuidv4(); // ⇨ '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d'
uuidv4(); // ⇨ '1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed'

console.log(format(new Date(), "yyyyMMdd\tHH:mm:ss")); // 20230717  14:10:33
console.log(uuidv4()); // 274dc2cd-093d-45ed-8bc5-6d99d7eaa998
```

# output

```js
// 20230717        14:10:33
// 274dc2cd-093d-45ed-8bc5-6d99d7eaa998
```

# #End </details>

<details>
  <summary>99. Node NPM - Uninstalling NPM Packages</summary>

# Uninstalling NPM Packages

```bs
npm uninstall nodemon -D
npm uninstall uuid
npm rm uuid
```

# #End </details>

+NODE-SERVER

<details>
  <summary>100. Node Server - Creating Node Log Events</summary>

# Creating Node Log Events

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c8232382-1ec1-478f-b059-95e80736fea2">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c3808440-1a46-48b9-98ae-97d6ee1f2097">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fb8c631e-ae96-4894-b4ee-2930618af4fa">

### x-dave-gray/node-app/package.json:

```js
{
  "name": "app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node index",
    "dev": "nodemon index"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "nodemon": "^3.0.1"
  },
  "dependencies": {
    "date-fns": "^2.30.0",
    "uuid": "^9.0.0"
  }
}
```

### x-dave-gray/node-app/event.js:

```js
const fs = require("fs");
const fsPromises = require("fs").promises;
const path = require("path");
const { format } = require("date-fns");
const { v4: uuid } = require("uuid");

const logEvents = async (message) => {
  const dateTime = `${format(new Date(), "yyyyMMdd\tHH:mm:ss")}`;
  const logItem = `${dateTime}\t${uuid()}\t${message}\n`;
  console.log(logItem);

  try {
    if (!fs.existsSync(path.join(__dirname, "logs"))) {
      await fsPromises.mkdir(path.join(__dirname, "logs"));
    }
    await fsPromises.appendFile(
      path.join(__dirname, "logs", "eventLog.txt"),
      logItem
    );
  } catch (err) {
    console.error(err);
  }
};

module.exports = logEvents;
```

### x-dave-gray/node-app/index.js:

```js
const EventEmitter = require("events");
class MyEmitter extends EventEmitter {}
// initialize object
const myEmitter = new MyEmitter();

const logEvents = require("./event");

// add listener for the log event
myEmitter.on("log", (msg) => logEvents(msg));

setTimeout(() => {
  //Emit event
  myEmitter.emit("log", "Log event emitted!");
}, 2000);
```

# Start Node Server

```bs
npm run dev
```

### x-dave-gray/node-app/logs/eventLog.txt:

```txt
20230717	20:51:03	32e53958-0d2f-43a7-9bfd-659a5631763f	Log event emitted!
20230717	20:54:19	bc3f31cc-4d38-4889-a520-610fff930ff5	Log event emitted!
20230717	20:54:31	7b578935-c6c1-43a0-b4f9-43e7ab6296d3	Log event emitted!
```

# #End </details>

<details>
  <summary>101. Node Server - Initializing Server</summary>

# Initializing Server

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d8783e4c-bc36-4fb5-963f-ad6f61a46a51">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/612dc018-e00f-4dec-bad3-79ebaeb111a3">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5c1f4069-83ba-40a3-abaa-7ef3f8c2e9fa">

### x-dave-gray/node-app/package.json:

```json
{
  "name": "project",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "nodemon": "^3.0.1"
  },
  "dependencies": {
    "date-fns": "^2.30.0",
    "uuid": "^9.0.0"
  }
}
```

### x-dave-gray/node-app/server.js:

```js
const http = require("http");
const path = require("path");
const fs = require("fs");
const fsPromises = require("fs").promises;

const logEvents = require("./logEvents");
const EventEmitter = require("events");
class Emitter extends EventEmitter {}

// initialize object
const myEmitter = new Emitter();
myEmitter.on("log", (msg, fileName) => logEvents(msg, fileName));

const PORT = process.env.PORT || 3500;

const server = http.createServer((req, res) => {
  console.log(req.url);
  console.log(req.method);
});

server.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/logEvents.js:

```js
const fs = require("fs");
const fsPromises = require("fs").promises;
const path = require("path");
const { format } = require("date-fns");
const { v4: uuid } = require("uuid");

const logEvents = async (message) => {
  const dateTime = `${format(new Date(), "yyyyMMdd\tHH:mm:ss")}`;
  const logItem = `${dateTime}\t${uuid()}\t${message}\n`;
  console.log(logItem);

  try {
    if (!fs.existsSync(path.join(__dirname, "logs"))) {
      await fsPromises.mkdir(path.join(__dirname, "logs"));
    }
    await fsPromises.appendFile(
      path.join(__dirname, "logs", "eventLog.txt"),
      logItem
    );
  } catch (err) {
    console.error(err);
  }
};

module.exports = logEvents;
```

# output

```bs
> project@1.0.0 dev
> nodemon server.js

[nodemon] 2.0.20
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `node server.js`
Server running on port 3500
/
GET
```

# #End </details>

<details>
  <summary>102. Node Server - Create Node Server</summary>

# Create Node Server

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c55e6261-bea3-4fda-96f2-ca9307d54218">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d62b6999-054e-4c1f-ada3-3a57996562b0">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b83e60a3-8e8d-484b-a9ba-9e0038c5a07b">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/84410202-440a-4325-9686-8bff7e3cfe0d">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ff41be0b-2f3e-4283-a2b4-776699782299">

### x-dave-gray/node-app/server.js:

```js
const http = require("http");
const path = require("path");
const fs = require("fs");
const fsPromises = require("fs").promises;

const logEvents = require("./logEvents");
const EventEmitter = require("events");
class Emitter extends EventEmitter {}

// initialize object
const myEmitter = new Emitter();
myEmitter.on("log", (msg, fileName) => logEvents(msg, fileName));
const PORT = process.env.PORT || 3500;

const serveFile = async (filePath, contentType, response) => {
  try {
    const rawData = await fsPromises.readFile(
      filePath,
      !contentType.includes("image") ? "utf8" : ""
    );
    const data =
      contentType === "application/json" ? JSON.parse(rawData) : rawData;
    response.writeHead(filePath.includes("404.html") ? 404 : 200, {
      "Content-Type": contentType,
    });
    response.end(
      contentType === "application/json" ? JSON.stringify(data) : data
    );
  } catch (err) {
    console.log(err);
    myEmitter.emit("log", `${err.name}: ${err.message}`, "errLog.txt");
    response.statusCode = 500;
    response.end();
  }
};

const server = http.createServer((req, res) => {
  console.log(req.url);
  console.log(req.method);
  myEmitter.emit("log", `${req.url}\t${req.method}`, "reqLog.txt");

  const extension = path.extname(req.url);

  let contentType;

  switch (extension) {
    case ".css":
      contentType = "text/css";
      break;
    case ".js":
      contentType = "text/javascript";
      break;
    case ".json":
      contentType = "application/json";
      break;
    case ".jpg":
      contentType = "image/jpeg";
      break;
    case ".png":
      contentType = "image/png";
      break;
    case ".txt":
      contentType = "text/plain";
      break;
    default:
      contentType = "text/html";
  }

  let filePath =
    contentType === "text/html" && req.url === "/"
      ? path.join(__dirname, "views", "index.html")
      : contentType === "text/html" && req.url.slice(-1) === "/"
      ? path.join(__dirname, "views", req.url, "index.html")
      : contentType === "text/html"
      ? path.join(__dirname, "views", req.url)
      : path.join(__dirname, req.url);

  // makes .html extension not required in the browser
  if (!extension && req.url.slice(-1) !== "/") filePath += ".html";

  const fileExists = fs.existsSync(filePath);

  if (fileExists) {
    serveFile(filePath, contentType, res);
  } else {
    switch (path.parse(filePath).base) {
      case "old-page.html":
        res.writeHead(301, { Location: "/new-page.html" });
        res.end();
        break;
      case "www-page.html":
        res.writeHead(301, { Location: "/" });
        res.end();
        break;
      default:
        serveFile(path.join(__dirname, "views", "404.html"), "text/html", res);
    }
  }
});

server.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/logEvents.js:

```js
const { format } = require("date-fns");
const { v4: uuid } = require("uuid");

const fs = require("fs");
const fsPromises = require("fs").promises;
const path = require("path");

const logEvents = async (message, logName) => {
  const dateTime = `${format(new Date(), "yyyyMMdd\tHH:mm:ss")}`;
  const logItem = `${dateTime}\t${uuid()}\t${message}\n`;

  try {
    if (!fs.existsSync(path.join(__dirname, "logs"))) {
      await fsPromises.mkdir(path.join(__dirname, "logs"));
    }

    await fsPromises.appendFile(path.join(__dirname, "logs", logName), logItem);
  } catch (err) {
    console.log(err);
  }
};

module.exports = logEvents;
```

### x-dave-gray/node-app/views/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home</title>
  </head>
  <body>
    <h1>Welcome! This is the Index Home Page.</h1>
  </body>
</html>
```

### x-dave-gray/node-app/views/404.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>404 Page</title>
  </head>
  <body>
    <h1>404 Page!</h1>
  </body>
</html>
```

### x-dave-gray/node-app/views/new-page.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>New Page</title>
  </head>
  <body>
    <h1>This is the New Page!</h1>
  </body>
</html>
```

### x-dave-gray/node-app/data/data.json:

```js
[
  {
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "firstname": "John",
    "lastname": "Smith"
  }
]
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
/index
GET
/css/style.css
GET
/new-page
GET
/css/style.css
GET
/img/img1.jpg
GET
```

# logs/reqLog.txt:

```txt
20230106	19:37:43	c5104bff-35f1-4346-b26c-67aee49052a0	/index	GET
20230106	19:37:43	11d0a0bf-8c5f-43d5-9df9-a70d4b32d7ae	/css/style.css	GET
20230106	19:38:27	c01a67e8-1255-4d21-9615-d7877282c4a5	/new-page	GET
20230106	19:38:27	c2307b43-c81e-44ff-930c-1b0682e74232	/css/style.css	GET
20230106	19:38:27	106b8afc-4352-4c80-bcaa-9e7434cb0bde	/img/img1.jpg	GET
20230718	07:35:08	753ae74d-c8e8-477c-b823-976e4d4d05df	/	GET
20230718	07:35:33	80c56abf-255d-4870-8bbd-1b67dce6c2c8	/	GET
20230718	07:35:34	994baac5-2681-43a7-9758-21af56e47563	/favicon.ico	GET
20230718	07:35:41	444ba75e-719e-4141-9eb1-d468473c7d35	/bj	GET
20230718	07:35:50	56fbae1d-96c7-4b23-9383-e2d6fa54b50b	/bj	GET
20230718	07:35:54	6c4f8944-eb5f-4a80-83e4-f0adc5135050	/bbbf	GET
20230718	07:35:59	c4e30c7f-e80f-4b4c-ae49-1b768f4f6bef	/aedad	GET
20230718	07:36:08	420ce001-792b-4840-bb6c-a8ac905e6569	/	GET
20230718	07:38:42	2957ddf2-11ec-49d6-89e7-a083d92858c9	/data/data.json	GET
```

# #End </details>

+EXPRESS

<details>
  <summary>103. Express - Send Simple Data to Page</summary>

# Send Simple Data to Page

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ff8b32ea-dd8a-4043-b437-1a39e34195d0">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/49acbcaf-4c85-48ec-a755-8036dc319b67">

# Install Express:

```bs
npm install express --save
```

### x-dave-gray/node-app/server.js:

```js
const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 3500;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# output

```bs
> project@1.0.0 dev
> nodemon server.js

[nodemon] 2.0.20
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `node server.js`
Server running on port 3500
```

# #End </details>

<details>
  <summary>104. Express - Send HTML page to render</summary>

# Send HTML page to render

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8f4605f4-6cca-4e3c-a40b-4aec444ad1cf">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1b44fda0-c8a8-40aa-b09e-e387678b2e40">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b64f035a-3730-4a67-8762-e2304e8d9327">

### x-dave-gray/node-app/server.js:

```js
const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 3500;

app.get("/", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/views/index.html:

```js
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home</title>
  </head>
  <body>
    <h1>Welcome! This is the Index Home Page.</h1>
  </body>
</html>
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
```

# #End </details>

<details>
  <summary>105. Express - Adding more routes</summary>

# Adding more routes

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b56fbe3b-0091-4a4d-9510-ad77aec0404d">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/37deec4e-98c2-4ba9-80aa-be626d5a9c60">
<img width="1181" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/83cebcd8-4833-4fac-af5a-ad29a9946cc7">

### x-dave-gray/node-app/server.js:

```js
const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 3500;

app.get("/", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page.html", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/views/new-page.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>New Page</title>
  </head>
  <body>
    <h1>This is the New Page!</h1>
  </body>
</html>
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
```

# #End </details>

<details>
  <summary>106. Express - Applying RegEx to routes </summary>

# Applying RegEx to routes

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9001390f-f46e-4d76-9f91-6de62114423d">
<img width="1181" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/971da8f1-6385-46e1-8313-7d73e9ae7b8e">
<img width="1181" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ffb6c6db-6811-47e1-b2ea-a390dd24a9c9">

# "^/$|/index(.html)?" means:

```bs
^/ - it must begin with a slash
/$ - it must end with a slash
| - or
/index(.html)? - it must look like /index or /index.html
```

### x-dave-gray/node-app/server.js:

```js
const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 3500;

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/views/new-page.html:

```js
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>New Page</title>
  </head>
  <body>
    <h1>This is the New Page!</h1>
  </body>
</html>
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
```

# #End </details>

<details>
  <summary>107. Express - Redirect routes</summary>

# Redirect routes

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/12bd5444-a3a1-4781-85d8-9d5f55fa9c7f">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ac541ad8-42db-46ce-9d61-084a2de71e59">

### x-dave-gray/node-app/server.js:

```js
const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 3500;

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/views/new-page.html:

```js
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>New Page</title>
  </head>
  <body>
    <h1>This is the New Page!</h1>
  </body>
</html>
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
```

# #End </details>

<details>
  <summary>108. Express - Adding Custom 404 route</summary>

# Adding Custom 404 route

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d888f52f-5ec2-4a31-8df8-fe7b8182fc2d">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/905472bd-cfb8-4066-a30a-9a1bc6d9f6d0">
<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3197077d-8af8-4f86-8862-cb486da419e7">

### x-dave-gray/node-app/server.js:

```js
const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 3500;

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

//Custom 404 Page
app.get("/*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/views/404.html:

```js
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>404 Page</title>
  </head>
  <body>
    <h1>404 Page!</h1>
  </body>
</html>
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
```

# #End </details>

<details>
  <summary>109. Express - Next Route handlers</summary>

# Next Route handlers

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/be44ed91-cf7d-4009-861c-115a1d14134a">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/15f01fbb-ec08-406d-80bc-763f836bbbc3">

### x-dave-gray/node-app/server.js:

```bs
// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);
```

```js
const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 3500;

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

//Custom 404 Page
app.get("/*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
loading hello.html...
```

# #End </details>

<details>
  <summary>110. Express - Chaining Route handlers</summary>

# Chaining Route handlers

<img width="963" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/61206d42-870e-43ff-b49a-22cfb3c1d8ba">


### x-dave-gray/node-app/server.js:

```bs
// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);
```

```js
const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 3500;

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.get("/*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
one
two
three
```

# #End </details>

<details>
  <summary>111. Express - Built-in Middleware</summary>

# Built-in Middleware

<img width="963" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4c9c9d5f-d0b8-479e-a008-ca1da3a290f5">
<img width="963" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2c21b3fc-5531-4c65-9c5a-abc3d2ec808a">
<img width="963" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/87afbfab-2e19-44d9-a5bc-ab022acc1dda">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/858c0116-004a-400a-862e-f5f655090938">

### x-dave-gray/node-app/server.js:

```bs
// built-in middleware to handle urlencoded data, in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use(express.static(path.join(__dirname, "/public")));
```

```js
const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 3500;

// built-in middleware to handle urlencoded data, in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use(express.static(path.join(__dirname, "/public")));

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.get("/*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/views/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home</title>
    <link rel="stylesheet" href="css/style.css" />
  </head>
  <body>
    <h1>Welcome! This is the Index Home Page.</h1>
  </body>
</html>
```

### x-dave-gray/node-app/public/css/style.css:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-size: 36px;
  min-height: 100vh;
  color: #fff;
  background-color: #000;
  display: grid;
  place-content: center;
}
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
```

# #End </details>

<details>
  <summary>112. Express - Custom Middleware Logger</summary>

# Custom Middleware Logger

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f4a3e2f4-8def-4988-ae2e-ac2f861d03df">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e2522e9d-e274-40a8-822d-330a21c891ca">

### x-dave-gray/node-app/server.js:

```bs
// custom middleware logger
app.use((req, res, next) => {
  console.log(`${req.method} ${req.path}`);
  next();
});
```

```js
const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use((req, res, next) => {
  console.log(`${req.method} ${req.path}`);
  next();
});

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use(express.static(path.join(__dirname, "/public")));

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.get("/*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
GET /sfd
GET /css/style.css
```

# #End </details>

<details>
  <summary>113. Express - Custom Middleware with logEvents.js</summary>

#  Custom Middleware with logEvents.js

<img width="965" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9bfb7c02-8010-4469-a051-7827c2b4841a">
<img width="965" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6074e688-894a-46b1-9dfc-d4e6837ba8c2">
<img width="965" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9c325b3e-8712-454e-b32e-557cf6fe8df6">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a654cf50-e200-4ec9-9ec7-0418425a2aef">

### x-dave-gray/node-app/server.js:

```bs
// custom middleware logger
app.use((req, res, next) => {
  logEvents(`${req.method}\t${req.headers.origin}\t${req.url}`, "reqLog.txt");
  console.log(`${req.method} ${req.path}`);
  next();
});
```

```js
const express = require("express");
const app = express();
const path = require("path");
const logEvents = require("./middleware/logEvents");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use((req, res, next) => {
  logEvents(`${req.method}\t${req.headers.origin}\t${req.url}`, "reqLog.txt");
  console.log(`${req.method} ${req.path}`);
  next();
});

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use(express.static(path.join(__dirname, "/public")));

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.get("/*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/middleware/logEvents.js:

```js
const { format } = require("date-fns");
const { v4: uuid } = require("uuid");

const fs = require("fs");
const fsPromises = require("fs").promises;
const path = require("path");

const logEvents = async (message, logName) => {
  const dateTime = `${format(new Date(), "yyyyMMdd\tHH:mm:ss")}`;
  const logItem = `${dateTime}\t${uuid()}\t${message}\n`;

  try {
    if (!fs.existsSync(path.join(__dirname, "..", "logs"))) {
      await fsPromises.mkdir(path.join(__dirname, "..", "logs"));
    }

    await fsPromises.appendFile(
      path.join(__dirname, "..", "logs", logName),
      logItem
    );
  } catch (err) {
    console.log(err);
  }
};

module.exports = logEvents;
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
GET /
GET /css/style.css
```

### ### x-dave-gray/node-app/server.js:

```txt
20230718	10:42:57	5341272e-8e15-431d-96a8-9ea1a2e4cb21	GET	undefined	/
20230718	10:42:57	83aac56a-4a44-4436-ad13-4f8f0ba93a0e	GET	undefined	/css/style.css
```

# #End </details>

<details>
  <summary>114. Express - Custom Middleware with logEvents.js (Refactored)</summary>

# Custom Middleware with logEvents.js (Refactored)

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d1b88d23-09d2-492e-8ec8-89caa6663fa2">
<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/be15d8ca-9dd3-4056-8976-a738d91ac206">
<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/84b74b8e-57c2-475b-b104-16b27a5d21ef">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/da3d8000-df46-4a74-b8dc-7481f4959bed">

### x-dave-gray/node-app/server.js:

```bs
// custom middleware logger
app.use(logger);
```

```js
const express = require("express");
const app = express();
const path = require("path");
const { logger } = require("./middleware/logEvents");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use(express.static(path.join(__dirname, "/public")));

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.get("/*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/middleware/logEvents.js:

```js
const { format } = require("date-fns");
const { v4: uuid } = require("uuid");

const fs = require("fs");
const fsPromises = require("fs").promises;
const path = require("path");

const logEvents = async (message, logName) => {
  const dateTime = `${format(new Date(), "yyyyMMdd\tHH:mm:ss")}`;
  const logItem = `${dateTime}\t${uuid()}\t${message}\n`;

  try {
    if (!fs.existsSync(path.join(__dirname, "..", "logs"))) {
      await fsPromises.mkdir(path.join(__dirname, "..", "logs"));
    }

    await fsPromises.appendFile(
      path.join(__dirname, "..", "logs", logName),
      logItem
    );
  } catch (err) {
    console.log(err);
  }
};

const logger = (req, res, next) => {
  logEvents(`${req.method}\t${req.headers.origin}\t${req.url}`, "reqLog.txt");
  console.log(`${req.method} ${req.path}`);
  next();
};

module.exports = { logger, logEvents };
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
GET /about
GET /css/style.css
```

### x-dave-gray/node-app/logs/reqLog.txt:

```txt
20230106	23:06:50	5eb41bdb-5938-46ec-b764-59cd9796fb4c	GET	undefined	/
20230106	23:06:50	ac65dbd1-916a-42e2-9664-7f1ea2fc62e3	GET	undefined	/css/style.css
20230106	23:16:29	d14a07b1-fd03-4a9c-b65a-1704551b5516	GET	undefined	/about
20230106	23:16:29	c23db065-ae38-4994-ac7a-f669fc9a60d6	GET	undefined	/css/style.css
```

# #End </details>

<details>
  <summary>115. Express - Third-Party Middleware (Cors)</summary>

# Third-Party Middleware (Cors)

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4aa1e5e9-17e1-43f2-ab62-31863c5bdd8f">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8a299f04-d68b-4ffb-a610-e9ee6958c579">

# Install Cors:

```bs
npm i cors --save
```

### x-dave-gray/node-app/server.js:

```bs
// Cross Origin Resource Sharing
app.use(cors());
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const { logger } = require("./middleware/logEvents");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
app.use(cors());

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use(express.static(path.join(__dirname, "/public")));

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.get("/*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# Fetch external domain

```bs
google.com -> fetch('http://localhost:3500');
```

# output

```bs
[nodemon] 2.0.20
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `node server.js`
Server running on port 3500
OPTIONS /
GET /
```

### x-dave-gray/node-app/logs/reqLog.txt:

```bs
20230106	23:06:50	5eb41bdb-5938-46ec-b764-59cd9796fb4c	GET	undefined	/
20230106	23:06:50	ac65dbd1-916a-42e2-9664-7f1ea2fc62e3	GET	undefined	/css/style.css
20230106	23:16:29	d14a07b1-fd03-4a9c-b65a-1704551b5516	GET	undefined	/about
20230106	23:16:29	c23db065-ae38-4994-ac7a-f669fc9a60d6	GET	undefined	/css/style.css
20230106	23:26:00	f45458b3-760b-417f-9652-c4f433fc0e93	OPTIONS	https://www.google.com	/
20230106	23:26:00	dba79f61-9cc7-461c-82ab-3a23fa42a3f2	GET	https://www.google.com	/
```

# #End </details>

<details>
  <summary>116. Express -  Third-Party Middleware (Protected Cors with Whitelist) </summary>

# Third-Party Middleware (Protected Cors with Whitelist)

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1e3dfc04-7b42-4ee3-9d1b-cbb27d7c3b06">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f138c052-37ad-4e0a-8e61-a94dcbef63a5">

### x-dave-gray/node-app/server.js:

```bs
// Cross Origin Resource Sharing
const whitelist = [
  "https://www.reactsite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
];
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
  optionsSuccessStatus: 200,
};
app.use(cors(corsOptions));
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const { logger } = require("./middleware/logEvents");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
const whitelist = [
  "https://www.reactsite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
];
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
  optionsSuccessStatus: 200,
};
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use(express.static(path.join(__dirname, "/public")));

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.get("/*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/middleware/logEvents.js:

```js
const { format } = require("date-fns");
const { v4: uuid } = require("uuid");

const fs = require("fs");
const fsPromises = require("fs").promises;
const path = require("path");

const logEvents = async (message, logName) => {
  const dateTime = `${format(new Date(), "yyyyMMdd\tHH:mm:ss")}`;
  const logItem = `${dateTime}\t${uuid()}\t${message}\n`;

  try {
    if (!fs.existsSync(path.join(__dirname, "..", "logs"))) {
      await fsPromises.mkdir(path.join(__dirname, "..", "logs"));
    }

    await fsPromises.appendFile(
      path.join(__dirname, "..", "logs", logName),
      logItem
    );
  } catch (err) {
    console.log(err);
  }
};

const logger = (req, res, next) => {
  logEvents(`${req.method}\t${req.headers.origin}\t${req.url}`, "reqLog.txt");
  console.log(`${req.method} ${req.path}`);
  next();
};

module.exports = { logger, logEvents };
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
```

# #End </details>

<details>
  <summary>117. Express - Custom Error Handler</summary>

# Custom Error Handler

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f5323f98-1f99-416e-b428-98062c6aaef1">
<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2a5ad5d4-2df6-449d-bdd0-3d309bcefdc7">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fa249090-a25c-4acf-8c63-8105a97bf7b4">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/38c54398-7243-4c38-b8e8-145565e5f52f">

### x-dave-gray/node-app/server.js:

```bs
 // Include no origin (undefined) for "development" server
 if (whitelist.indexOf(origin) !== -1 || !origin) {
      callback(null, true);
    }
```

```bs
//Custom Error Handler
app.use(errorHandler);

//Custom Error Handler
app.use(function (err, req, res, next) {
  console.error(err.stack);
  res.status(500).send(err.message);
});
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
const whitelist = [
  "https://www.reactsite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
];
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1 || !origin) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
  optionsSuccessStatus: 200,
};
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use(express.static(path.join(__dirname, "/public")));

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.get("/*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

//Custom Error Handler
app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/middleware/errorHandler.js:

```js
const { logEvents } = require("./logEvents");

const errorHandler = (err, req, res, next) => {
  logEvents(`${err.name}: ${err.message}`, "errLog.txt");
  console.error(err.stack);
  res.status(500).send(err.message);
};
module.exports = errorHandler;
```

### x-dave-gray/node-app/middleware/logEvents.js:

```js
const { format } = require("date-fns");
const { v4: uuid } = require("uuid");

const fs = require("fs");
const fsPromises = require("fs").promises;
const path = require("path");

const logEvents = async (message, logName) => {
  const dateTime = `${format(new Date(), "yyyyMMdd\tHH:mm:ss")}`;
  const logItem = `${dateTime}\t${uuid()}\t${message}\n`;

  try {
    if (!fs.existsSync(path.join(__dirname, "..", "logs"))) {
      await fsPromises.mkdir(path.join(__dirname, "..", "logs"));
    }

    await fsPromises.appendFile(
      path.join(__dirname, "..", "logs", logName),
      logItem
    );
  } catch (err) {
    console.log(err);
  }
};

const logger = (req, res, next) => {
  logEvents(`${req.method}\t${req.headers.origin}\t${req.url}`, "reqLog.txt");
  console.log(`${req.method} ${req.path}`);
  next();
};

module.exports = { logger, logEvents };
```

# output

```bs
[nodemon] starting `node server.js`
Server running on port 3500
GET /
GET /css/style.css
```

### x-dave-gray/node-app/logs/errLog.txt:

```txt
20230107	08:30:49	8b0bdd90-1ff8-41ad-b498-e77659453812	Error: Not allowed by CORS
```

### x-dave-gray/node-app/logs/reqLog.txt:

```txt
20230107	08:30:56	f1914109-16d7-48ec-bd64-3dcffb0ae53e	GET	undefined	/
20230107	08:30:56	a1fb6427-e7a9-468a-aa01-aba9f5f93c3e	GET	undefined	/css/style.css
```

# #End </details>

<details>
  <summary>118. Express - Using app.all() for Custom 404 route</summary>

# Using app.all() for Custom 404 route

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/af530d36-b776-4394-bf8d-17a69c78e55b">
<img width="1181" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e6b7b4e0-580d-4af7-8b40-e06060a8138e">

### x-dave-gray/node-app/server.js:

```bs
//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
const whitelist = [
  "https://www.reactsite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
];
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1 || !origin) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
  optionsSuccessStatus: 200,
};
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use(express.static(path.join(__dirname, "/public")));

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404).sendFile(path.join(__dirname, "views", "404.html"));
});

//Custom Error Handler
app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
GET /dsfdf
GET /css/style.css
```

# #End </details>

<details>
  <summary>119. Express - Protecting Custom 404 route</summary>

# Protecting Custom 404 route

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0c823e0b-4bbe-4159-a166-3b968ed13fad">
<img width="1181" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2a7bbc6a-30f0-4a53-bf59-4bb614b26400">

### x-dave-gray/node-app/server.js:

```bs
//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
const whitelist = [
  "https://www.reactsite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
];
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1 || !origin) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
  optionsSuccessStatus: 200,
};
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use(express.static(path.join(__dirname, "/public")));

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

//Custom Error Handler
app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
GET /dsfdf
GET /css/style.css
```

# #End </details>

<details>
  <summary>120. Express - Creating Routes with Router for subdir</summary>

# Creating Routes with Router for subdir

<img width="1181" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8ee8b5e8-daf2-421f-aff0-2651650c8648">
<img width="1181" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f9ef427f-db6f-42a0-b34b-4c31030830a5">

### x-dave-gray/node-app/routes/subdir.js:

```js
const express = require("express");
const router = express.Router();
const path = require("path");

router.get("^/$|/index(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "views", "subdir", "index.html"));
});

router.get("/test(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "views", "subdir", "test.html"));
});

module.exports = router;
```

### x-dave-gray/node-app/server.js:

```bs
//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));
app.use("/subdir", express.static(path.join(__dirname, "/public")));
app.use("/subdir", require("./routes/subdir"));
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
const whitelist = [
  "https://www.reactsite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
];
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1 || !origin) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
  optionsSuccessStatus: 200,
};
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));
app.use("/subdir", express.static(path.join(__dirname, "/public")));

app.use("/subdir", require("./routes/subdir"));

app.get("^/$|/index(.html)?", (req, res) => {
  // res.sendFile("./views/index.html", { root: __dirname });
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-page.html"));
});

//redirect route
app.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

// Next Route handlers
app.get(
  "/hello(.html)?",
  (req, res, next) => {
    console.log("loading hello.html...");
    next();
  },
  (req, res) => {
    res.send("Hello World!");
  }
);

// chaining route handlers
const one = (req, res, next) => {
  console.log("one");
  next();
};
const two = (req, res, next) => {
  console.log("two");
  next();
};
const three = (req, res) => {
  console.log("three");
  res.send("Finished!");
};

app.get("/chain(.html)?", [one, two, three]);

//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

//Custom Error Handler
app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
GET /subdir/index,html
GET /subdir/css/style.css
GET /subdir/index.html
GET /subdir/test
```

# #End </details>

<details>
  <summary>121. Express - Creating Routes with Router for index page </summary>

# Creating Routes with Router for index page

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9c13cd89-6fa7-4391-b78d-ef5423531c72">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/28c3e327-3a46-4c73-aa0c-19888e559669">
<img width="1181" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bffa8571-265f-4fb1-add8-b7253e123fde">
<img width="1181" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c3c2f0d5-35a1-40f3-830a-96eb4a8143fb">

### x-dave-gray/node-app/routes/root.js:

```js
const express = require("express");
const router = express.Router();
const path = require("path");

router.get("^/$|/index(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "views", "index.html"));
});

router.get("/new-page(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "views", "new-page.html"));
});

//redirect route
router.get("/old-page(.html)?", (req, res) => {
  res.redirect(301, "/new-page.html"); //302 by default
});

module.exports = router;
```

### x-dave-gray/node-app/server.js:

```bs
//Routes
app.use("/", require("./routes/root"));
app.use("/subdir", require("./routes/subdir"));
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
const whitelist = [
  "https://www.reactsite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
];
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1 || !origin) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
  optionsSuccessStatus: 200,
};
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));
app.use("/subdir", express.static(path.join(__dirname, "/public")));

//Routes
app.use("/", require("./routes/root"));
app.use("/subdir", require("./routes/subdir"));

//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

//Custom Error Handler
app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
GET /
GET /css/style.css
GET /new-page
GET /css/style.css
GET /img/img1.jpg
```

# #End </details>

<details>
  <summary>122. Express - Creating REST API Router </summary>

#  Creating REST API Router

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4c71d80c-5f5e-4a3f-a392-95923eeeb121">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/20e0cf2c-c7da-46e0-8e75-a5703e4b3e9a">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f942f53e-225d-4217-81be-79f33775c64f">

### x-dave-gray/node-app/server.js:

```bs
//Routes
app.use("/employees", require("./routes/api/employees"));
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
const whitelist = [
  "https://www.reactsite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
];
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1 || !origin) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
  optionsSuccessStatus: 200,
};
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded data
// in other words, form data:
// 'content-type: application/x-www-form-urlencoded'
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));
app.use("/subdir", express.static(path.join(__dirname, "/public")));

//Routes
app.use("/", require("./routes/root"));
app.use("/subdir", require("./routes/subdir"));
app.use("/employees", require("./routes/api/employees"));

//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

//Custom Error Handler
app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/routes/api/employees.js:

```js
const express = require("express");
const router = express.Router();
const data = {};
data.employees = require("../../data/employees.json");

router
  .route("/")
  .get((req, res) => {
    res.json(data.employees);
  })
  .post((req, res) => {
    res.json({
      firstname: req.body.firstname,
      lastname: req.body.lastname,
    });
  })
  .put((req, res) => {
    res.json({
      firstname: req.body.firstname,
      lastname: req.body.lastname,
    });
  })
  .delete((req, res) => {
    res.json({ id: req.body.id });
  });

router.route("/:id").get((req, res) => {
  res.json({ id: req.params.id });
});

module.exports = router;
```

### x-dave-gray/node-app/data/employees.json:

```js
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "John",
    "lastname": "Smith"
  }
]
```

# GET: http://localhost:3500/employees

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "John",
    "lastname": "Smith"
  }
]
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7b79f409-92e8-4d8e-bae7-db8d7b1e979b">

# POST: http://localhost:3500/employees

### Body: {"firstname":"John", "lastname":"Doe"}

```bs
{
  "firstname": "John",
  "lastname": "Doe"
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b0ac1e50-291a-4d80-9e26-6c82167abcce">

# PUT: http://localhost:3500/employees

### Body: {"id":2, "firstname":"David"}

```bs
{
  "firstname": "David"
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5cda41da-df3c-4e52-87f6-4e0f3422779f">

# DELETE: http://localhost:3500/employees

### Body: {"id": 3}

```bs
{
  "id": 3
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ede482fa-8903-43ba-a091-25d4a01f9d9f">

# GET: http://localhost:3500/employees/1

```bs
{
  "id": "1"
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e63e215a-4716-49d2-af04-61ed43de63f8">

# #End </details>

<details>
  <summary>123. Express - Refactoring REST API to MVC Pattern </summary>

# Refactoring REST API to MVC Pattern

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/63e18f1c-dc7f-4084-998e-e422f373cea7">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/26f74e65-1aec-4bdc-8792-64cbf3dadabf">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c51a0af4-3dce-4562-908d-fc7b62230e0c">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f5c71f98-667b-4570-9d00-c87b60836e6a">

### x-dave-gray/node-app/model/employees.json:

```js
[
  {
    id: 1,
    firstname: "Dave",
    lastname: "Gray",
  },
  {
    id: 2,
    firstname: "John",
    lastname: "Smith",
  },
];
```

### x-dave-gray/node-app/server.js:

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const corsOptions = require("./config/corsOptions");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded form data
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));

//Routes
app.use("/", require("./routes/root"));
app.use("/employees", require("./routes/api/employees"));

//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

//Custom Error Handler
app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/routes/root.js:

```js
const express = require("express");
const router = express.Router();
const path = require("path");

router.get("^/$|/index(.html)?", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "views", "index.html"));
});

module.exports = router;
```

### x-dave-gray/node-app/routes/api/employees.js:

```js
const express = require("express");
const router = express.Router();
const employeesController = require("../../controllers/employeesController");

router
  .route("/")
  .get(employeesController.getAllEmployees)
  .post(employeesController.createNewEmployee)
  .put(employeesController.updateEmployee)
  .delete(employeesController.deleteEmployee);

//router.route("/:id").get(employeesController.getEmployee);
router.get("/:id", employeesController.getEmployee);

module.exports = router;
```

### x-dave-gray/node-app/controllers/employeesController.js:

```js
const data = {};
data.employees = require("../model/employees.json");

//GET /employees
const getAllEmployees = (req, res) => {
  res.json(data.employees);
};

//POST /employees
const createNewEmployee = (req, res) => {
  res.json({
    firstname: req.body.firstname,
    lastname: req.body.lastname,
  });
};

//PUT /employees/:id
const updateEmployee = (req, res) => {
  res.json({
    firstname: req.body.firstname,
    lastname: req.body.lastname,
  });
};

//DELETE /employees/:id
const deleteEmployee = (req, res) => {
  res.json({ id: req.body.id });
};

//GET /employees/:id
const getEmployee = (req, res) => {
  res.json({ id: req.params.id });
};

module.exports = {
  getAllEmployees,
  createNewEmployee,
  updateEmployee,
  deleteEmployee,
  getEmployee,
};
```

### x-dave-gray/node-app/config/corsOptions.js:

```js
const whitelist = [
  "https://www.reactsite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
];

const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1 || !origin) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
  optionsSuccessStatus: 200,
};

module.exports = corsOptions;
```

# GET: http://localhost:3500/employees

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "John",
    "lastname": "Smith"
  }
]
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7b79f409-92e8-4d8e-bae7-db8d7b1e979b">

# POST: http://localhost:3500/employees

### Body: {"firstname":"John", "lastname":"Doe"}

```bs
{
  "firstname": "John",
  "lastname": "Doe"
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b0ac1e50-291a-4d80-9e26-6c82167abcce">

# PUT: http://localhost:3500/employees

### Body: {"id":2, "firstname":"David"}

```bs
{
  "firstname": "David"
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5cda41da-df3c-4e52-87f6-4e0f3422779f">

# DELETE: http://localhost:3500/employees

### Body: {"id": 3}

```bs
{
  "id": 3
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ede482fa-8903-43ba-a091-25d4a01f9d9f">

# GET: http://localhost:3500/employees/1

```bs
{
  "id": "1"
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e63e215a-4716-49d2-af04-61ed43de63f8">


# #End </details>

<details>
  <summary>124. Express - Simulating a REST API db with Controllers </summary>

# Simulating a REST API db with Controllers

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8785a251-8af6-429a-a2d4-7f6c0de6faa3">
<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7ff70752-774b-405d-8bc0-c47ea1385e4a">

### x-dave-gray/node-app/server.js:

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const corsOptions = require("./config/corsOptions");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded form data
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));

//Routes
app.use("/", require("./routes/root"));
app.use("/employees", require("./routes/api/employees"));

//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

//Custom Error Handler
app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

controllers/employeesController.js:

```js
// const data = {};
// data.employees = require("../model/employees.json");

const data = {
  employees: require("../model/employees.json"),
  setEmployees: function (data) {
    this.employees = data;
  },
};

//GET /employees
const getAllEmployees = (req, res) => {
  res.json(data.employees);
};

//POST /employees
const createNewEmployee = (req, res) => {
  const newEmployee = {
    id: data.employees?.length
      ? data.employees[data.employees.length - 1].id + 1
      : 1,
    firstname: req.body.firstname,
    lastname: req.body.lastname,
  };

  if (!newEmployee.firstname || !newEmployee.lastname) {
    return res
      .status(400)
      .json({ message: "First and last names are required." });
  }

  data.setEmployees([...data.employees, newEmployee]);
  res.status(201).json(data.employees);
};

//PUT /employees/:id
const updateEmployee = (req, res) => {
  const employee = data.employees.find(
    (emp) => emp.id === parseInt(req.body.id)
  );
  if (!employee) {
    return res
      .status(400)
      .json({ message: `Employee ID ${req.body.id} not found` });
  }
  if (req.body.firstname) employee.firstname = req.body.firstname;
  if (req.body.lastname) employee.lastname = req.body.lastname;
  const filteredArray = data.employees.filter(
    (emp) => emp.id !== parseInt(req.body.id)
  );
  const unsortedArray = [...filteredArray, employee];
  data.setEmployees(
    unsortedArray.sort((a, b) => (a.id > b.id ? 1 : a.id < b.id ? -1 : 0))
  );
  res.json(data.employees);
};

//DELETE /employees/:id
const deleteEmployee = (req, res) => {
  const employee = data.employees.find(
    (emp) => emp.id === parseInt(req.body.id)
  );
  if (!employee) {
    return res
      .status(400)
      .json({ message: `Employee ID ${req.body.id} not found` });
  }
  const filteredArray = data.employees.filter(
    (emp) => emp.id !== parseInt(req.body.id)
  );
  data.setEmployees([...filteredArray]);
  res.json(data.employees);
};

//GET /employees/:id
const getEmployee = (req, res) => {
  const employee = data.employees.find(
    (emp) => emp.id === parseInt(req.params.id)
  );
  if (!employee) {
    return res
      .status(400)
      .json({ message: `Employee ID ${req.params.id} not found` });
  }
  res.json(employee);
};

module.exports = {
  getAllEmployees,
  createNewEmployee,
  updateEmployee,
  deleteEmployee,
  getEmployee,
};
```

# GET: http://localhost:3500/employees

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "John",
    "lastname": "Smith"
  }
]
```

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9c21b1c4-39d9-478d-b5af-7336a17578ec">

# POST: http://localhost:3500/employees

### Body: {"firstname":"John", "lastname":"Doe"}

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "John",
    "lastname": "Smith"
  },
  {
    "id": 3,
    "firstname": "John",
    "lastname": "Doe"
  }
]
```

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e96518d9-c56b-4d11-874f-bddae6775c1b">

# PUT: http://localhost:3500/employees

### Body: {"id":2, "firstname":"David"}

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "David",
    "lastname": "Smith"
  },
  {
    "id": 3,
    "firstname": "John",
    "lastname": "Doe"
  }
]
```

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/87a6f2a0-a065-4fea-b9ab-20a40c31e24c">

# DELETE: http://localhost:3500/employees

### Body: {"id": 3}

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "David",
    "lastname": "Smith"
  }
]
```

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/15bcc812-64a3-4204-a5e1-46b61e2bd66b">

# GET: http://localhost:3500/employees/1

```bs
{
  "id": 1,
  "firstname": "Dave",
  "lastname": "Gray"
}
```

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1303c598-d360-403a-a4c8-876457071136">

# #End </details>

<details>
  <summary>125. Express - User Password Registration </summary>

# User Password Registration

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/298e83c9-2608-457c-adef-94ab1e3f3d62">
<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7c628fbd-cd7c-4d66-b25b-bab7b3145445">
<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2451c74e-3d58-484a-a1cc-119f133fa051">
<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7001d5ff-b298-4794-bf2d-b6a9067d2880">

# Install bcrypt to hash passwords:

```bs
npm install bcrypt --save
npm i bcrypt
```

### x-dave-gray/node-app/model/users.json:

```js
[]
```

### x-dave-gray/node-app/server.js:

```bs
//Routes
app.use("/", require("./routes/root"));
app.use("/register", require("./routes/register"));
app.use("/employees", require("./routes/api/employees"));
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const corsOptions = require("./config/corsOptions");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded form data
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));

//Routes
app.use("/", require("./routes/root"));
app.use("/register", require("./routes/register"));
app.use("/employees", require("./routes/api/employees"));

//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

//Custom Error Handler
app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/routes/register.js:

```js
const express = require("express");
const router = express.Router();
const registerController = require("../controllers/registerController");

router.post("/", registerController.handleNewUser);

module.exports = router;
```

### x-dave-gray/node-app/controllers/registerController.js:

```js
const fsPromises = require("fs").promises;
const path = require("path");
const bcrypt = require("bcrypt");

const usersDB = {
  users: require("../model/users.json"),
  setUsers: function (data) {
    this.users = data;
  },
};

const handleNewUser = async (req, res) => {
  const { user, pwd } = req.body;

  if (!user || !pwd)
    return res
      .status(400)
      .json({ message: "Username and password are required." });

  // check for duplicate usernames in the db
  const duplicate = usersDB.users.find((person) => person.username === user);

  if (duplicate) return res.sendStatus(409); //Conflict
  try {
    //encrypt the password
    const hashedPwd = await bcrypt.hash(pwd, 10);
    //store the new user
    const newUser = { username: user, password: hashedPwd };
    usersDB.setUsers([...usersDB.users, newUser]);
    await fsPromises.writeFile(
      path.join(__dirname, "..", "model", "users.json"),
      JSON.stringify(usersDB.users)
    );
    console.log(usersDB.users);
    res.status(201).json({ success: `New user ${user} created!` });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

module.exports = { handleNewUser };
```


# POST: http://localhost:3500/register

### Body: { "user": "walt1", "pwd": "Aa$12345"}

```bs
{
  "success": "New user walter1 created!"
}
```

```bs
[nodemon] starting `node server.js`
Server running on port 3500
GET /
GET /css/style.css
POST /register
[
  {
    username: 'walt1',
    password: '$2b$10$y0LX.oJg3RhMRcTeIaE0t.ox5rQI1KkcYq5quHHk8AeuUsQNzyv7C'
  }
]
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9f4b1cd4-93af-46c2-b77e-eafa120924bd">

# POST: http://localhost:3500/register

### Body = { "user": "walt2", "pwd": "Aa$12345"}

```bs
{
  "success": "New user walt2 created!"
}
```

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
POST /register
[
  {
    username: 'walt1',
    password: '$2b$10$y0LX.oJg3RhMRcTeIaE0t.ox5rQI1KkcYq5quHHk8AeuUsQNzyv7C'
  },
  {
    username: 'walt2',
    password: '$2b$10$00/fPnvsJ8iAckSBoPzTNeoKKizI3Gtm/FU5cx0yxPBaTDgbO9qJq'
  }
]
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c6013cb8-773e-4081-9029-fa82bb419436">


# POST: http://localhost:3500/register (Already Created)

### Body = { "user": "walt2", "pwd": "Aa$12345"}

```bs
Conflict
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0389e6fd-074b-4692-8064-dd7060c5a8b9">


# #End </details>

<details>
  <summary>126. Express - User Login Authentication </summary>

# User Login Authentication

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e65da411-7b9d-4cc2-bbde-dcd354f2e277">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c054f1b8-c4ed-4b3c-a85d-a4be69ae9411">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4fad52e4-87f6-42ed-a44a-9781c59e8655">

### x-dave-gray/node-app/server.js:

```bs
//Routes
app.use("/", require("./routes/root"));
app.use("/register", require("./routes/register"));
app.use("/auth", require("./routes/auth"));
app.use("/employees", require("./routes/api/employees"));
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const corsOptions = require("./config/corsOptions");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded form data
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));

//Routes
app.use("/", require("./routes/root"));
app.use("/register", require("./routes/register"));
app.use("/auth", require("./routes/auth"));
app.use("/employees", require("./routes/api/employees"));

//Custom 404 Page
app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

//Custom Error Handler
app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/routes/auth.js:

```js
const express = require("express");
const router = express.Router();
const authController = require("../controllers/authController");

router.post("/", authController.handleLogin);

module.exports = router;
```

### x-dave-gray/node-app/controllers/authController.js:

```js
const bcrypt = require("bcrypt");

const usersDB = {
  users: require("../model/users.json"),
  setUsers: function (data) {
    this.users = data;
  },
};

const handleLogin = async (req, res) => {
  const { user, pwd } = req.body;
  if (!user || !pwd)
    return res
      .status(400)
      .json({ message: "Username and password are required." });

  const foundUser = usersDB.users.find((person) => person.username === user);

  if (!foundUser) return res.sendStatus(401); //Unauthorized

  // evaluate password
  const match = await bcrypt.compare(pwd, foundUser.password);

  if (match) {
    // create JWTs
    res.json({ success: `User ${user} is logged in!` });
  } else {
    res.sendStatus(401);
  }
};

module.exports = { handleLogin };
```

# POST: http://localhost:3500/auth

### Body: { "user": "walt1", "pwd": "Aa$12345"}

```bs
{
  "success": "User walt1 is logged in!"
}
```

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
POST /auth
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e554973e-b65f-40b3-abdf-a4a3f814b469">

# POST: http://localhost:3500/auth (Wrong password)

### Body: { "user": "walt1", "pwd": "Aa$12345pwdssss"}

```bs
Unauthorized
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5553b7c6-ab29-4a19-9e65-130c9c71a266">

# POST: http://localhost:3500/auth (Wrong username)

### Body: { "user": "walt100", "pwd": "Aa$12345"}

```bs
Unauthorized
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b95ded09-98f3-448b-bf5c-ad2e72dc28b1">

# #End </details>

+EXPRESS JWT AUTHENTICATION

<details>
  <summary>127. Express JWT Authentication - Creating .dotenv Secrets</summary>

# Creating .dotenv Secrets

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/66a4f867-22dc-48a5-bf04-999731eb3ef6">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/419512d2-031b-488e-802c-285f6fc9121d">

# Install Dependencies:

```bs
npm i dotenv jsonwebtoken cookie-parser --save

npm i dotenv
npm i jsonwebtoken
npm i cookie-parser
```

### x-dave-gray/node-app/package.json:

```js
{
  "name": "project",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "nodemon": "^3.0.1"
  },
  "dependencies": {
    "bcrypt": "^5.1.0",
    "cookie-parser": "^1.4.6",
    "cors": "^2.8.5",
    "date-fns": "^2.30.0",
    "dotenv": "^16.3.1",
    "express": "^4.18.2",
    "jsonwebtoken": "^9.0.1",
    "uuid": "^9.0.0"
  }
}
```

# Generate Refresh and Access Token Secret Keys:

```bs
$ node
$ require("crypto").randomBytes(64).toString("Hex")
```

```js
// f69ac98ba015a05a1043b4c9536c2b0ce47d3f1dc71dd65f96db8e5e062ad5fcbe5440fabef0ecf2475bbb869b1741f37094804dde65d1f08bcd9e762b9e6479
// da009bd39b9455f84e4c55544587c8166b976d666bb5d7b79b3f77d0504500e02a0c01e9fe49d299acdd8d9f66df9b3258d083b38915d1a172842daacbca34f9
```

### x-dave-gray/node-app/.env:

```bs
ACCESS_TOKEN_SECRET=f69ac98ba015a05a1043b4c9536c2b0ce47d3f1dc71dd65f96db8e5e062ad5fcbe5440fabef0ecf2475bbb869b1741f37094804dde65d1f08bcd9e762b9e6479
REFRESH_TOKEN_SECRET=da009bd39b9455f84e4c55544587c8166b976d666bb5d7b79b3f77d0504500e02a0c01e9fe49d299acdd8d9f66df9b3258d083b38915d1a172842daacbca34f9
```

### x-dave-gray/node-app/.gitignore:

```bs
node_modules
.env
```

# #End </details>

<details>
  <summary>128. Express JWT Authentication - Creating JWT tokens and verification at Login Authorization</summary>

# Creating JWT tokens and verification at Login Authorization

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f152d95a-63a6-46f8-9f03-1097ab01016e">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8a627df2-d0f5-4c2f-931d-8020e26df9dd">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c7e57349-b8a5-4b7b-8b34-537fe9548295">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7fd50654-f533-4755-ab19-f691cbcb627a">

### x-dave-gray/node-app/controllers/authController.js:

```js
require("dotenv").config();
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const fsPromises = require("fs").promises;
const path = require("path");

const usersDB = {
  users: require("../model/users.json"),
  setUsers: function (data) {
    this.users = data;
  },
};

const handleLogin = async (req, res) => {
  const { user, pwd } = req.body;
  if (!user || !pwd)
    return res
      .status(400)
      .json({ message: "Username and password are required." });

  const foundUser = usersDB.users.find((person) => person.username === user);
  if (!foundUser) return res.sendStatus(401); //Unauthorized

  // evaluate password
  const match = await bcrypt.compare(pwd, foundUser.password);

  if (match) {
    // create JWTs
    const accessToken = jwt.sign(
      { username: foundUser.username },
      process.env.ACCESS_TOKEN_SECRET,
      { expiresIn: "30s" }
    );
    const refreshToken = jwt.sign(
      { username: foundUser.username },
      process.env.REFRESH_TOKEN_SECRET,
      { expiresIn: "1d" }
    );
    // Saving refreshToken with current user
    const otherUsers = usersDB.users.filter(
      (person) => person.username !== foundUser.username
    );
    const currentUser = { ...foundUser, refreshToken };
    usersDB.setUsers([...otherUsers, currentUser]);
    await fsPromises.writeFile(
      path.join(__dirname, "..", "model", "users.json"),
      JSON.stringify(usersDB.users)
    );
    res.cookie("jwt", refreshToken, {
      httpOnly: true,
      sameSite: "None",
      secure: true, // false for development
      maxAge: 24 * 60 * 60 * 1000,
    });
    res.json({ accessToken });
  } else {
    res.sendStatus(401);
  }
};

module.exports = { handleLogin };
```

# Creating JWT verification middleware

### x-dave-gray/node-app/middleware/verifyJWT.js:

```js
require("dotenv").config();
const jwt = require("jsonwebtoken");

const verifyJWT = (req, res, next) => {
  const authHeader = req.headers["authorization"];
  if (!authHeader) return res.sendStatus(401);

  console.log(authHeader); // Bearer <token>
  const token = authHeader.split(" ")[1];

  jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, decoded) => {
    if (err) return res.sendStatus(403); //invalid token
    req.user = decoded.username;
    next();
  });
};

module.exports = verifyJWT;
```

# Placing verification middleware in GET Route

### x-dave-gray/node-app/routes/api/employees.js:

```bs
.get(verifyJWT, employeesController.getAllEmployees)
```

```js
const express = require("express");
const router = express.Router();
const employeesController = require("../../controllers/employeesController");
const verifyJWT = require("../../middleware/verifyJWT");

router
  .route("/")
  .get(verifyJWT, employeesController.getAllEmployees)
  .post(employeesController.createNewEmployee)
  .put(employeesController.updateEmployee)
  .delete(employeesController.deleteEmployee);

//router.route("/:id").get(employeesController.getEmployee);
router.get("/:id", employeesController.getEmployee);

module.exports = router;
```

# POST: http://localhost:3500/auth

### Body: { "user": "walt1", "pwd": "Aa$12345"}

```bs
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHRlcjEiLCJpYXQiOjE2NzM1NTA4MTgsImV4cCI6MTY3MzU1MDg0OH0.62Z_EOMV1FQJ7-bG84hApAWePKPkgynivA3zfXhs3KM"
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/16d8d843-bae8-47c1-bc8f-09717027df49">

# GET: http://localhost:3500/employees (Auth -> Bearer Token)

```bs
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHQxIiwiaWF0IjoxNjg5NzY1MDk4LCJleHAiOjE2ODk3NjUxMjh9.zLzjxZm9TSFQABCdjDDrPDXJSNNE0bKAfNWt6G6FnYc
```

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "John",
    "lastname": "Smith"
  }
]
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7c050d3e-057c-4f3b-991f-fa4f694a13ec">

# GET: http://localhost:3500/employees (No Bearer Token)

### If No Bearer Token is supplied -> 401 Unauthorized (From verifyJWT middleware)

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8033fdee-843b-49d6-b93d-fe91606754d5">

# GET: http://localhost:3500/employees (Expired Bearer Token)

### If old Bearer Token is supplied (expired after 30secs) -> 403 Forbidden (From verifyJWT middleware)

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ad5aa3fb-3ef1-44c2-8de7-1a33facfd7bc">

# #End </details>

<details>
  <summary>129. Express JWT Authentication - Protect all routes with JWT verification</summary>

# Protect all routes with JWT verification

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/47ffe6aa-066a-4945-bb51-8eab3ba56357">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7f7dde56-429b-46c1-9816-49d53f7e3885">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1eed128c-d19b-4fe8-98de-8efb141f5cee">

### x-dave-gray/node-app/server.js:

```bs
app.use(verifyJWT);
app.use("/employees", require("./routes/api/employees"));
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const corsOptions = require("./config/corsOptions");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const verifyJWT = require("./middleware/verifyJWT");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded form data
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));

// routes
app.use("/", require("./routes/root"));
app.use("/register", require("./routes/register"));
app.use("/auth", require("./routes/auth"));

app.use(verifyJWT);
app.use("/employees", require("./routes/api/employees"));

app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### x-dave-gray/node-app/routes/api/employees.js:

```js
const express = require("express");
const router = express.Router();
const employeesController = require("../../controllers/employeesController");

router
  .route("/")
  .get(employeesController.getAllEmployees)
  .post(employeesController.createNewEmployee)
  .put(employeesController.updateEmployee)
  .delete(employeesController.deleteEmployee);

//router.route("/:id").get(employeesController.getEmployee);
router.get("/:id", employeesController.getEmployee);

module.exports = router;
```

### x-dave-gray/node-app/middleware/verifyJWT.js:

```js
require("dotenv").config();
const jwt = require("jsonwebtoken");

const verifyJWT = (req, res, next) => {
  const authHeader = req.headers["authorization"];
  if (!authHeader) return res.sendStatus(401);

  console.log(authHeader); // Bearer <token>
  const token = authHeader.split(" ")[1];

  jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, decoded) => {
    if (err) return res.sendStatus(403); //invalid token
    req.user = decoded.username;
    next();
  });
};

module.exports = verifyJWT;
```

# POST: http://localhost:3500/employees

### Body: {"firstname":"John", "lastname": "Doe"}

```bs
401 Unauthorized
```

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/db21e964-7a2b-4fa9-88c0-6488d9fd4399">


# #End </details>

<details>
  <summary>130. Express JWT Authentication -  Adding cookie parser middleware</summary>

# Adding cookie parser middleware

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3ce02049-6cc6-49f9-ad9f-ed30d6e2c6bb">

### x-dave-gray/node-app/server.js:

```bs
const cookieParser = require('cookie-parser');

//middleware for cookies
app.use(cookieParser());
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const corsOptions = require("./config/corsOptions");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const verifyJWT = require("./middleware/verifyJWT");
const cookieParser = require("cookie-parser");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded form data
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//middleware for cookies
app.use(cookieParser());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));

// routes
app.use("/", require("./routes/root"));
app.use("/register", require("./routes/register"));
app.use("/auth", require("./routes/auth"));

app.use(verifyJWT);
app.use("/employees", require("./routes/api/employees"));

app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# #End </details>

<details>
  <summary>131. Express JWT Authentication - Creating Refresh Token Controller and Route </summary>

# Creating Refresh Token Controller and Route

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d83088dc-a701-4f6d-b181-5a438662492b">
<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6c1daf05-3034-4d27-aadb-a1761c1f0ec9">
<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/39f5d1da-d260-4269-b5d2-0e711b5d1b30">

### x-dave-gray/node-app/controllers/refreshTokenController.js:

```js
require("dotenv").config();
const jwt = require("jsonwebtoken");

const usersDB = {
  users: require("../model/users.json"),
  setUsers: function (data) {
    this.users = data;
  },
};

const handleRefreshToken = (req, res) => {
  // console.log(req.cookies);
  const cookies = req.cookies;

  if (!cookies?.jwt) return res.sendStatus(401);
  const refreshToken = cookies.jwt;

  const foundUser = usersDB.users.find(
    (person) => person.refreshToken === refreshToken
  );

  if (!foundUser) return res.sendStatus(403); //Forbidden

  // evaluate jwt
  jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET, (err, decoded) => {
    if (err || foundUser.username !== decoded.username)
      return res.sendStatus(403);

    const accessToken = jwt.sign(
      { username: decoded.username },
      process.env.ACCESS_TOKEN_SECRET,
      { expiresIn: "30s" }
    );
    res.json({ accessToken });
  });
};

module.exports = { handleRefreshToken };
```

### x-dave-gray/node-app/routes/refresh.js:

```js
const express = require("express");
const router = express.Router();
const refreshTokenController = require("../controllers/refreshTokenController");

router.get("/", refreshTokenController.handleRefreshToken);

module.exports = router;
```

### x-dave-gray/node-app/server.js:

```bs
// routes
app.use('/auth', require('./routes/auth'));
app.use('/refresh', require('./routes/refresh'));
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const corsOptions = require("./config/corsOptions");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const verifyJWT = require("./middleware/verifyJWT");
const cookieParser = require("cookie-parser");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded form data
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//middleware for cookies
app.use(cookieParser());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));

// routes
app.use("/", require("./routes/root"));
app.use("/register", require("./routes/register"));
app.use("/auth", require("./routes/auth"));
app.use("/refresh", require("./routes/refresh"));

app.use(verifyJWT);
app.use("/employees", require("./routes/api/employees"));

app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# POST: http://localhost:3500/auth

### Body: { "user": "walt1", "pwd": "Aa$12345"}

```bs
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHRlcjEiLCJpYXQiOjE2NzM1OTg3MDgsImV4cCI6MTY3MzU5ODczOH0.JiNd0MtbgB1zfE6KxujV-VZtBTXnc55V8xJNV_m4aik"
}
```

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1b698a83-32be-4317-a8f0-765fe99673c3">

Cookies -> jwt:

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/141b1945-09d6-400d-89d8-8075a1253877">

# GET: http://localhost:3500/refresh

```bs
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHRlcjEiLCJpYXQiOjE2NzM2MDM4NTUsImV4cCI6MTY3MzYwMzg4NX0.5wYLi2FL4bdsr8jKY7UU6Gd3hs-MaQpcSe5mYP81otA"
}
```

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/719e1347-bcdd-466a-a256-e36722e468c8">


# #End </details>

<details>
  <summary>132. Express JWT Authentication - Creating Logout Controller and Route </summary>

# Creating Logout Controller and Route

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/af7421a3-0754-4e0b-b1ad-9d4e10552e57">
<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/605b02ad-82f6-4fe4-8b17-ea8b879dabcd">
<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/067e68e4-10ea-4917-8d9c-73ecc8098290">

### x-dave-gray/node-app/controllers/logoutController.js:

```js
const usersDB = {
  users: require("../model/users.json"),
  setUsers: function (data) {
    this.users = data;
  },
};
const fsPromises = require("fs").promises;
const path = require("path");

const handleLogout = async (req, res) => {
  // On client, also delete the accessToken

  const cookies = req.cookies;
  if (!cookies?.jwt) return res.sendStatus(204); //No content
  const refreshToken = cookies.jwt;

  // Is refreshToken in db?
  const foundUser = usersDB.users.find(
    (person) => person.refreshToken === refreshToken
  );
  if (!foundUser) {
    res.clearCookie("jwt", { httpOnly: true, sameSite: "None", secure: true }); //secure: true only on https (prod)
    return res.sendStatus(204);
  }

  // Delete refreshToken in db
  const otherUsers = usersDB.users.filter(
    (person) => person.refreshToken !== foundUser.refreshToken
  );
  const currentUser = { ...foundUser, refreshToken: "" };
  usersDB.setUsers([...otherUsers, currentUser]);
  await fsPromises.writeFile(
    path.join(__dirname, "..", "model", "users.json"),
    JSON.stringify(usersDB.users)
  );

  res.clearCookie("jwt", { httpOnly: true, sameSite: "None", secure: true }); //secure: true only on https (prod)
  res.sendStatus(204);
};

module.exports = { handleLogout };
```

### x-dave-gray/node-app/routes/logout.js:

```js
const express = require("express");
const router = express.Router();
const logoutController = require("../controllers/logoutController");

router.get("/", logoutController.handleLogout);

module.exports = router;
```

### x-dave-gray/node-app/server.js:

```bs
// routes
app.use("/auth", require("./routes/auth"));
app.use("/refresh", require("./routes/refresh"));
app.use("/logout", require("./routes/logout"));
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const cookieParser = require("cookie-parser");
const corsOptions = require("./config/corsOptions");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const verifyJWT = require("./middleware/verifyJWT");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Cross Origin Resource Sharing
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded form data
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//middleware for cookies
app.use(cookieParser());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));

// routes
app.use("/", require("./routes/root"));
app.use("/register", require("./routes/register"));
app.use("/auth", require("./routes/auth"));
app.use("/refresh", require("./routes/refresh"));
app.use("/logout", require("./routes/logout"));

app.use(verifyJWT);
app.use("/employees", require("./routes/api/employees"));

app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# POST: http://localhost:3500/auth

### Body: { "user": "walt1", "pwd": "Aa$12345"}

```bs
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHQxIiwiaWF0IjoxNjg5ODM5MjQzLCJleHAiOjE2ODk4MzkyNzN9.MgV1rzgjgEN0Aa-FUG-eqREyRH0CvUBVk0bOa1e-SDU"
}
```

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ad967464-551a-4038-88e5-0a12fb0339f3">


### Cookies -> jwt:

```bs
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHQxIiwiaWF0IjoxNjg5ODM5MjQzLCJleHAiOjE2ODk5MjU2NDN9.mCMzB1FGu35a2GCNbb9K8Jln_NkPqtzaQWd0sWNoapQ
```

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/66f5975a-e958-4a22-9014-6d12133e8c40">


# GET: http://localhost:3500/refresh

```bs
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHRlcjEiLCJpYXQiOjE2NzM2MjU3MjgsImV4cCI6MTY3MzYyNTc1OH0.yXMCjTG0ugca0Nx1HqqgAK-ZEKWNEzLSEypfV46b6c8"
}
```

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8242274c-d0a2-4752-a9cc-717478ea7de0">

# GET: http://localhost:3500/logout

```bs
204 No Content
```

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5cf24a6e-d3cb-45aa-9f5d-05b1cc1629d5">

### Cookies -> jwt:

```bs
<null>
```

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d28d37b3-b870-4536-98aa-8ed49e448059">

# GET: http://localhost:3500/refresh

```bs
401 Unauthorized
```

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d808e5fe-a31e-40ea-a5e9-011a04300daf">


# #End </details>

<details>
  <summary>133. Express JWT Authentication - Front-End/Back-End Modifications </summary>

# Front-End/Back-End Modifications

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bb99f83f-db5d-430b-a653-dd9506913797">
<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/db52a5dd-a447-43a7-9333-9acbb065078d">
<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a5442202-4485-44bd-b576-5552d893706e">
<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/97ee6e52-d174-4fbf-8cb8-3a62919f392f">
<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/92df3ba8-a5eb-40c5-8aac-b54b83ffb6c3">

# FRONT END

- Use credentials option when using fetch

### main.js:

```bs
credentials: 'include',
```

```js
const sendLogin = async () => {
  const user = document.getElementById("user").value;
  const pwd = document.getElementById("pwd").value;
  try {
    const response = await fetch("http://localhost:3500/auth", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ user, pwd }),
    });
    if (!response.ok) {
      if (response.status === 401) {
        return await sendRefreshToken();
      }
    }
    throw new Error(`${response.status} ${response.statusText}`);
    return await response.json();
  } catch (err) {
    console.log(err.stack);
    displayErr();
  }
};
```

# BACK END

- Modify CORS Options config files

### x-dave-gray/node-app/config/corsOptions.js:

```js
const allowedOrigins = require("./allowedOrigins");

const corsOptions = {
  origin: (origin, callback) => {
    if (allowedOrigins.indexOf(origin) !== -1 || !origin) {
      callback(null, true);
    } else {
      callback(new Error("Not allowed by CORS"));
    }
  },
  optionsSuccessStatus: 200,
};

module.exports = corsOptions;
```

### x-dave-gray/node-app/config/allowedOrigins.js:

```js
const allowedOrigins = [
  "https://www.yoursite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
];

module.exports = allowedOrigins;
```

- Create credentials middleware

### x-dave-gray/node-app/middleware/credentials.js:

```js
const allowedOrigins = require("../config/allowedOrigins");

const credentials = (req, res, next) => {
  const origin = req.headers.origin;
  if (allowedOrigins.includes(origin)) {
    res.header("Access-Control-Allow-Credentials", true);
  }
  next();
};

module.exports = credentials;
```

### x-dave-gray/node-app/server.js:

```bs
const credentials = require('./middleware/credentials');

// Handle options credentials check - before CORS!
// and fetch cookies credentials requirement
app.use(credentials);
```

```js
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const cookieParser = require("cookie-parser");
const corsOptions = require("./config/corsOptions");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const verifyJWT = require("./middleware/verifyJWT");
const credentials = require("./middleware/credentials");
const PORT = process.env.PORT || 3500;

// custom middleware logger
app.use(logger);

// Handle options credentials check - before CORS!
// and fetch cookies credentials requirement
app.use(credentials);

// Cross Origin Resource Sharing
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded form data
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//middleware for cookies
app.use(cookieParser());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));

// routes
app.use("/", require("./routes/root"));
app.use("/register", require("./routes/register"));
app.use("/auth", require("./routes/auth"));
app.use("/refresh", require("./routes/refresh"));
app.use("/logout", require("./routes/logout"));

app.use(verifyJWT);
app.use("/employees", require("./routes/api/employees"));

app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

app.use(errorHandler);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

# Confirm sameSite and secure options in cookie creation

### x-dave-gray/node-app/controllers/authController.js:

```bs
res.cookie("jwt", refreshToken, {
  httpOnly: true,
  sameSite: "None", // None for production
  secure: false, // true for production
  maxAge: 24 * 60 * 60 * 1000,
});
```

```js
const usersDB = {
  users: require("../model/users.json"),
  setUsers: function (data) {
    this.users = data;
  },
};
const bcrypt = require("bcrypt");

const jwt = require("jsonwebtoken");
require("dotenv").config();
const fsPromises = require("fs").promises;
const path = require("path");

const handleLogin = async (req, res) => {
  const { user, pwd } = req.body;
  if (!user || !pwd)
    return res
      .status(400)
      .json({ message: "Username and password are required." });
  const foundUser = usersDB.users.find((person) => person.username === user);
  if (!foundUser) return res.sendStatus(401); //Unauthorized
  // evaluate password
  const match = await bcrypt.compare(pwd, foundUser.password);
  if (match) {
    // create JWTs
    const accessToken = jwt.sign(
      { username: foundUser.username },
      process.env.ACCESS_TOKEN_SECRET,
      { expiresIn: "30s" }
    );
    const refreshToken = jwt.sign(
      { username: foundUser.username },
      process.env.REFRESH_TOKEN_SECRET,
      { expiresIn: "1d" }
    );
    // Saving refreshToken with current user
    const otherUsers = usersDB.users.filter(
      (person) => person.username !== foundUser.username
    );
    const currentUser = { ...foundUser, refreshToken };
    usersDB.setUsers([...otherUsers, currentUser]);
    await fsPromises.writeFile(
      path.join(__dirname, "..", "model", "users.json"),
      JSON.stringify(usersDB.users)
    );
    res.cookie("jwt", refreshToken, {
      httpOnly: true,
      sameSite: "None", // None for production
      secure: false, // true for production
      maxAge: 24 * 60 * 60 * 1000,
    });
    res.json({ accessToken });
  } else {
    res.sendStatus(401);
  }
};

module.exports = { handleLogin };
```

# #End </details>

<details>
  <summary>134. Express JWT Authentication - Authentication VS Authorization </summary>

# Authentication VS Authorization

### Authentication

- The Process of verifying who someone is.
- Confirm authentication with JWT
- Allow access to API endpoints
- Endpoints provide data resources

### Authorization

- The Process of verifying what specific resources a user has access to.
- Use Authorization header to restrict access

### User Roles & Permissions

- Provide different levels of access
- Sent in access token payload
- Verified with middleware

# #End </details>

<details>
  <summary>135. Express JWT Authorization - Create User ROLES </summary>

# Create User ROLES

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7c57d7b1-1483-4712-9f30-423edebd41f1">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/406ec967-2a4b-426c-aa62-feca11a69436">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e4e2d7f5-f81e-4555-9972-b4b73a9f0c06">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2b40ce6a-30e4-4692-ab10-ef0a99fbef3b">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1d5087e6-88e2-4040-8cf6-4a9b4b6b2718">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/74932bf2-53ef-4583-a674-ce5a2a349c57">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8b4ab2b8-7bce-4dae-82b3-e61b26037139">

### x-dave-gray/node-app/config/roles_list.js:

```js
const ROLES_LIST = {
  Admin: 5150,
  Editor: 1984,
  User: 2001,
};

module.exports = ROLES_LIST;
```

### x-dave-gray/node-app/model/users.json:

```bs
[
  {
    "username": "dave1",
    "roles": { "User": 2001 },
    "password": "$2b$10$oEbHZlazDHE1YnnJ4XdpGuGh9a/JZOO7Xe6WZtRRsSMgprxMXnKza",
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImRhdmUxIiwiaWF0IjoxNjMzOTkyMjkwLCJleHAiOjE2MzQwNzg2OTB9.U85HVX_gcDZkHHSRWeo7AHfIe7q9i03dGW2ed3fHqAk"
  },
  {
    "username": "walt2",
    "roles": { "User": 2001, "Editor": 1984 },
    "password": "$2b$10$cvfmz./teMWDccIMChAxZ.HqgL3eoQGYTm1z9lGy5iRf8D7NNargC",
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHQyIiwiaWF0IjoxNjMzOTkyNDU2LCJleHAiOjE2MzQwNzg4NTZ9.wRVJbN7_67JyTW9PALMWWEsO4BMkehyy5kXq6WilvWc"
  },
  {
    "username": "walt1",
    "roles": { "User": 2001, "Editor": 1984, "Admin": 5150 },
    "password": "$2b$10$33Q9jtAoaXC4aUX9Bjihxum2BHG.ENB6JyoCvPjnuXpITtUd8x8/y",
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHQxIiwiaWF0IjoxNjMzOTkyNTY0LCJleHAiOjE2MzQwNzg5NjR9.gE2CgbtEuqE42LeJ4dP6APmqyGTNBh53WXVyDdP47yM"
  }
]
```

# Add Roles to User on registration

### x-dave-gray/node-app/controllers/registerController.js:

```bs
//store the new user
const newUser = {
    "username": user,
    "roles": { "User": 2001 },
    "password": hashedPwd
};
```

```js
const fsPromises = require("fs").promises;
const path = require("path");
const bcrypt = require("bcrypt");

const usersDB = {
  users: require("../model/users.json"),
  setUsers: function (data) {
    this.users = data;
  },
};

const handleNewUser = async (req, res) => {
  const { user, pwd } = req.body;
  if (!user || !pwd)
    return res
      .status(400)
      .json({ message: "Username and password are required." });

  // check for duplicate usernames in the db
  const duplicate = usersDB.users.find((person) => person.username === user);
  if (duplicate) return res.sendStatus(409); //Conflict

  try {
    //encrypt the password
    const hashedPwd = await bcrypt.hash(pwd, 10);
    //store the new user
    const newUser = {
      username: user,
      roles: { User: 2001 },
      password: hashedPwd,
    };
    usersDB.setUsers([...usersDB.users, newUser]);
    await fsPromises.writeFile(
      path.join(__dirname, "..", "model", "users.json"),
      JSON.stringify(usersDB.users)
    );
    console.log(usersDB.users);
    res.status(201).json({ success: `New user ${user} created!` });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

module.exports = { handleNewUser };
```

# Add user roles to access token at authentication

### x-dave-gray/node-app/controllers/authController.js:

```bs
const roles = Object.values(foundUser.roles);
// create JWTs
const accessToken = jwt.sign(
    {
        "UserInfo": {
            "username": foundUser.username,
            "roles": roles
        }
    },
    process.env.ACCESS_TOKEN_SECRET,
    { expiresIn: '30s' }
);
```

```js
require("dotenv").config();
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const fsPromises = require("fs").promises;
const path = require("path");

const usersDB = {
  users: require("../model/users.json"),
  setUsers: function (data) {
    this.users = data;
  },
};

const handleLogin = async (req, res) => {
  const { user, pwd } = req.body;
  if (!user || !pwd)
    return res
      .status(400)
      .json({ message: "Username and password are required." });

  const foundUser = usersDB.users.find((person) => person.username === user);
  if (!foundUser) return res.sendStatus(401); //Unauthorized

  // evaluate password
  const match = await bcrypt.compare(pwd, foundUser.password);

  if (match) {
    const roles = Object.values(foundUser.roles);
    // create JWTs
    const accessToken = jwt.sign(
      {
        UserInfo: {
          username: foundUser.username,
          roles: roles,
        },
      },
      process.env.ACCESS_TOKEN_SECRET,
      { expiresIn: "30s" }
    );
    const refreshToken = jwt.sign(
      { username: foundUser.username },
      process.env.REFRESH_TOKEN_SECRET,
      { expiresIn: "1d" }
    );
    // Saving refreshToken with current user
    const otherUsers = usersDB.users.filter(
      (person) => person.username !== foundUser.username
    );
    const currentUser = { ...foundUser, refreshToken };
    usersDB.setUsers([...otherUsers, currentUser]);
    await fsPromises.writeFile(
      path.join(__dirname, "..", "model", "users.json"),
      JSON.stringify(usersDB.users)
    );
    res.cookie("jwt", refreshToken, {
      httpOnly: true,
      sameSite: "None",
      secure: true,
      maxAge: 24 * 60 * 60 * 1000,
    });
    res.json({ accessToken });
  } else {
    res.sendStatus(401);
  }
};

module.exports = { handleLogin };
```

# Add user roles to access token when refreshed

### x-dave-gray/node-app/controllers/refreshTokenController.js:

```bs
// evaluate jwt
jwt.verify(
    refreshToken,
    process.env.REFRESH_TOKEN_SECRET,
    (err, decoded) => {
        if (err || foundUser.username !== decoded.username) return res.sendStatus(403);
        const roles = Object.values(foundUser.roles);
        const accessToken = jwt.sign(
            {
                "UserInfo": {
                    "username": decoded.username,
                    "roles": roles
                }
            },
            process.env.ACCESS_TOKEN_SECRET,
            { expiresIn: '30s' }
        );
        res.json({ accessToken })
    }
);
```

```js
require("dotenv").config();
const jwt = require("jsonwebtoken");

const usersDB = {
  users: require("../model/users.json"),
  setUsers: function (data) {
    this.users = data;
  },
};

const handleRefreshToken = (req, res) => {
  const cookies = req.cookies;
  if (!cookies?.jwt) return res.sendStatus(401);
  const refreshToken = cookies.jwt;

  const foundUser = usersDB.users.find(
    (person) => person.refreshToken === refreshToken
  );
  if (!foundUser) return res.sendStatus(403); //Forbidden
  // evaluate jwt
  jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET, (err, decoded) => {
    if (err || foundUser.username !== decoded.username)
      return res.sendStatus(403);
    const roles = Object.values(foundUser.roles);
    const accessToken = jwt.sign(
      {
        UserInfo: {
          username: decoded.username,
          roles: roles,
        },
      },
      process.env.ACCESS_TOKEN_SECRET,
      { expiresIn: "30s" }
    );
    res.json({ accessToken });
  });
};

module.exports = { handleRefreshToken };
```

# Update the verifyJWT middleware to include roles

### x-dave-gray/node-app/middleware/verifyJWT.js:

```js
require("dotenv").config();
const jwt = require("jsonwebtoken");

const verifyJWT = (req, res, next) => {
  const authHeader = req.headers["authorization"];
  if (!authHeader) return res.sendStatus(401);

  //console.log(authHeader); // Bearer <token>
  const token = authHeader.split(" ")[1];

  jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, decoded) => {
    if (err) return res.sendStatus(403); //invalid token
    req.user = decoded.UserInfo.username;
    req.roles = decoded.UserInfo.roles;
    next();
  });
};

module.exports = verifyJWT;
```

# #End </details>

<details>
  <summary>136. Express JWT Authorization - Create verifyRoles middleware </summary>

# Create verifyRoles middleware

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/df0d0cc0-7c47-4a9b-9768-9a0af947bf6c">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f1d141a6-21b1-48ac-8b3d-0ab471da11dc">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ad27d476-7f8c-4ff6-8197-b63af3eb62e8">

### x-dave-gray/node-app/middleware/verifyRoles.js:

```js
const verifyRoles = (...allowedRoles) => {
  return (req, res, next) => {
    if (!req?.roles) return res.sendStatus(401);
    const rolesArray = [...allowedRoles];
    console.log(rolesArray);
    console.log(req.roles);
    const result = req.roles
      .map((role) => rolesArray.includes(role))
      .find((val) => val === true);
    if (!result) return res.sendStatus(401);
    next();
  };
};

module.exports = verifyRoles;
```

# Add verifyRoles middleware to routes

### x-dave-gray/node-app/routes/api/employees.js:

```js
const express = require("express");
const router = express.Router();
const employeesController = require("../../controllers/employeesController");
const ROLES_LIST = require("../../config/roles_list");
const verifyRoles = require("../../middleware/verifyRoles");

router
  .route("/")
  .get(employeesController.getAllEmployees)
  .post(
    verifyRoles(ROLES_LIST.Admin, ROLES_LIST.Editor),
    employeesController.createNewEmployee
  )
  .put(
    verifyRoles(ROLES_LIST.Admin, ROLES_LIST.Editor),
    employeesController.updateEmployee
  )
  .delete(verifyRoles(ROLES_LIST.Admin), employeesController.deleteEmployee);

router.route("/:id").get(employeesController.getEmployee);

module.exports = router;
```

# 1. Use dave1 (user) to create an Employee

# POST: (Login) http://localhost:3500/auth

### Body: { "user": "dave1", "pwd": "Aa$12345" }

```bs
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6ImRhdmUxIiwicm9sZXMiOlsyMDAxXX0sImlhdCI6MTY3Mzg2MzcxMCwiZXhwIjoxNjczODYzNzQwfQ.jWYqwGkmRO05oEjoKtveY8axuuxOigvFSG04_cJNudc"
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d8839bd9-573d-4452-a0e7-e38029d95a66">

# GET: (Get Employees) http://localhost:3500/employees

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "John",
    "lastname": "Smith"
  }
]
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8c868872-ce86-4592-921b-7e29e2f4d1a7">

# POST: (Create a new Employee) http://localhost:3500/employees

### Body: {"firstname":"John", "lastname": "Doe"}

- dave1 is only a "user - 2001" not an "Editor - 1984" or "Admin - 5150", so he will not have authorized access to create a new Employee.

```bs
401 Unauthorized
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2792b0ff-147a-4c26-90a3-ee55503bd48d">

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
GET /employees
POST /employees
[ 5150, 1984 ]
[ 2001 ]
```

# 2. Use walt2 (user & Editor) to create and Delete an Employee

# POST: (Login) http://localhost:3500/auth

### Body: { "user": "walt2", "pwd": "Aa$12345" }

```bs
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6IndhbHQyIiwicm9sZXMiOlsyMDAxLDE5ODRdfSwiaWF0IjoxNjczODY0NTY3LCJleHAiOjE2NzM4NjQ1OTd9.MLgiODweaqP8hpbM_CwITfRzMvTXWIQlF03HJYCIgRk"
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b2a9ecdc-947d-4d32-b16e-ccd9d5205040">

# POST: (Create a new Employee) http://localhost:3500/employees

### Body: {"firstname":"John", "lastname": "Doe"}

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "John",
    "lastname": "Smith"
  },
  {
    "id": 3,
    "firstname": "John",
    "lastname": "Doe"
  }
]
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/95cd3e88-66c2-4c5f-b5e6-523e6697385b">

# DELETE: (Delete Employee) http://localhost:3500/employees

### Body: {"id":3}

- walt2 is only a "user - 2001" and "Editor - 1984", but not an "Admin - 5150", so he will be able to create a new Employee but not have authorized access to delete an Employee.

```bs
401 Unauthorized
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ce7bbc0a-81cb-4536-bb4a-485e02436235">

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
DELETE /employees
[ 5150 ]
[ 2001, 1984 ]
```

# 3. Use walt1 (user, Editor & Admin) to Create and Delete an Employee

# POST: (Login) http://localhost:3500/auth

### Body: { "user": "walt1", "pwd": "Aa$12345" }

```bs
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6IndhbHQxIiwicm9sZXMiOlsyMDAxLDE5ODQsNTE1MF19LCJpYXQiOjE2NzM4NjUyMTQsImV4cCI6MTY3Mzg2NTI0NH0.4MqeWhS8GFjCL4_H6kDfLmt8pmz_zGdt1GF3hQU8AAc"
}
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b27cfdbc-928d-483a-b45e-5816a6aeec95">

# POST: (Create a new Employee) http://localhost:3500/employees

### Body: {"firstname":"John", "lastname": "Doe"}

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "John",
    "lastname": "Smith"
  },
  {
    "id": 3,
    "firstname": "John",
    "lastname": "Doe"
  }
]
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2a3f6a38-2e88-4b6a-b208-570d3fb705a4">

# DELETE: (Delete Employee) http://localhost:3500/employees

### Body: {"id":3}

- walt1 has all previledges as a "user - 2001", "Editor - 1984" and "Admin - 5150", so he will be able to create a new Employee and delete an Employee.

```bs
[
  {
    "id": 1,
    "firstname": "Dave",
    "lastname": "Gray"
  },
  {
    "id": 2,
    "firstname": "John",
    "lastname": "Smith"
  }
]
```

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6671b21d-0d6b-4d62-b435-38a78781bd1d">

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Server running on port 3500
POST /employees
[ 5150, 1984 ]
[ 2001, 1984, 5150 ]
DELETE /employees
[ 5150 ]
[ 2001, 1984, 5150 ]
```

# #End </details>

+MONGODB

<details>
  <summary>137. MongoDB - Connect MongoDB to Application </summary>

# Connect MongoDB to Application

<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5bbf5256-a20d-4d05-ac0e-77f807aaae75">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/eac628ff-058f-414e-82e7-9f574e743c20">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7967880a-d7e0-4f70-aa23-65c138debd8b">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6c199410-07a8-45a4-993e-83e769f473f5">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/43903bb5-a825-452c-9763-05277a347334">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fab7f9a7-ed91-4b8f-af3f-7468dd882116">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/64483999-bf0d-40d2-804e-7284ff9d1347">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9bf74552-c91d-4a24-bd6b-5d8630fba94d">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/24668cfb-ce04-40ec-8ce8-1010fbeeafb7">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f498c066-ba68-4fa0-82d2-857e0918792f">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/177515ba-29e3-4688-af71-9820fbda132e">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/76fad565-0c9c-47d3-be2f-bc1986d6b31f">
<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b0db5242-2025-499a-836d-0866a9beee64">
<img width="1175" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e39776d6-ebfb-440d-b1ee-2d4db487ae9b">
<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/66609f84-9b60-4fbd-b472-e6c468baa555">
<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6141c5fa-6fc7-4b1b-99fb-dddca50f048d">

# Install Mongoose:

```bs
npm i mongoose --save
```

# Connect to MongoDB from Application (Sample Code):

```bs
mongodb+srv://monogtut:<password>@cluster0.jliermf.mongodb.net/<DBNAME>?retryWrites=true&w=majority
```

```bs

const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://monogtut:<password>@cluster0.jliermf.mongodb.net/?retryWrites=true&w=majority";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function run() {
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("Pinged your deployment. You successfully connected to MongoDB!");
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);
```

# Add MongoDB Database URI

### x-dave-gray/node-app/.env:

```dotenv
ACCESS_TOKEN_SECRET=f69ac98ba015a05a1043b4c9536c2b0ce47d3f1dc71dd65f96db8e5e062ad5fcbe5440fabef0ecf2475bbb869b1741f37094804dde65d1f08bcd9e762b9e6479
REFRESH_TOKEN_SECRET=da009bd39b9455f84e4c55544587c8166b976d666bb5d7b79b3f77d0504500e02a0c01e9fe49d299acdd8d9f66df9b3258d083b38915d1a172842daacbca34f9
DATABASE_URI=mongodb+srv://monogtut:testing123@cluster0.jliermf.mongodb.net/CompanyDB?retryWrites=true&w=majority
```

# Create connection configuration

### x-dave-gray/node-app/config/dbConn.js:

```js
const mongoose = require("mongoose");

const connectDB = async () => {
  try {
    await mongoose.connect(process.env.DATABASE_URI, {
      useUnifiedTopology: true,
      useNewUrlParser: true,
    });
  } catch (err) {
    console.error(err);
  }
};

module.exports = connectDB;
```

### x-dave-gray/node-app/server.js:

```bs
require("dotenv").config();
const mongoose = require("mongoose");
const connectDB = require("./config/dbConn");

// Connect to MongoDB
connectDB();

mongoose.connection.once("open", () => {
  console.log("Connected to MongoDB");
  app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
});
```

```js
require("dotenv").config();
const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");
const corsOptions = require("./config/corsOptions");
const { logger } = require("./middleware/logEvents");
const errorHandler = require("./middleware/errorHandler");
const verifyJWT = require("./middleware/verifyJWT");
const cookieParser = require("cookie-parser");
const credentials = require("./middleware/credentials");
const mongoose = require("mongoose");
const connectDB = require("./config/dbConn");
const PORT = process.env.PORT || 3500;

// Connect to MongoDB
connectDB();

// custom middleware logger
app.use(logger);

// Handle options credentials check - before CORS!
// and fetch cookies credentials requirement
app.use(credentials);

// Cross Origin Resource Sharing
app.use(cors(corsOptions));

// built-in middleware to handle urlencoded form data
app.use(express.urlencoded({ extended: false }));

// built-in middleware for json
app.use(express.json());

//middleware for cookies
app.use(cookieParser());

//serve static files
app.use("/", express.static(path.join(__dirname, "/public")));

// routes
app.use("/", require("./routes/root"));
app.use("/register", require("./routes/register"));
app.use("/auth", require("./routes/auth"));
app.use("/refresh", require("./routes/refresh"));
app.use("/logout", require("./routes/logout"));

app.use(verifyJWT);
app.use("/employees", require("./routes/api/employees"));

app.all("*", (req, res) => {
  res.status(404);
  if (req.accepts("html")) {
    res.sendFile(path.join(__dirname, "views", "404.html"));
  } else if (req.accepts("json")) {
    res.json({ error: "404 Not Found" });
  } else {
    res.type("txt").send("404 Not Found");
  }
});

app.use(errorHandler);

mongoose.connection.once("open", () => {
  console.log("Connected to MongoDB");
  app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
});
```

# output:

```bs
[nodemon] 3.0.1
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `node server.js`
Connected to MongoDB
Server running on port 3500
```

# #End </details>

<details>
  <summary>138. MongoDB - Understanding Mongoose Schema </summary>

# Mongoose Website

https://mongoosejs.com/

<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dd277f1a-a9b5-4746-ad3e-e01d7507c819">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bf3b8ff7-175f-4e90-ad8a-d8c620d51de3">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/395dc246-8fac-46fa-94e6-3e1affeddc47">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0b0a0cb0-6ac9-40f2-aa51-42698a6ac407">

# Defining your schema

- Everything in Mongoose starts with a Schema.
- Each schema maps to a MongoDB collection and defines the shape of the documents within that collection.
- When you call mongoose.model() on a schema, Mongoose compiles a model for you.
- The first argument is the singular name of the collection your model is for.
- Mongoose automatically looks for the plural lowercased version of your model name.
- Thus, for the example below, the model Tank is for the tanks collection in the database.
- Note: The .model() function makes a copy of schema.
- Make sure that you've added everything you want to schema, including hooks, before calling .model()!

# Sample

```bs
import mongoose from "mongoose";
const { Schema } = mongoose;

const blogSchema = new Schema({
  title: String, // String is shorthand for {type: String}
  author: String,
  body: String,
  comments: [{ body: String, date: Date }],
  date: { type: Date, default: Date.now },
  hidden: Boolean,
  meta: {
    votes: Number,
    favs: Number,
  },
});

module.exports = mongoose.model("Blog", blogSchema);
```

```bs
const schema = new mongoose.Schema({ name: 'string', size: 'string' });
const Tank = mongoose.model('Tank', schema);
```

# #End </details>

<details>
  <summary>139. MongoDB - Create Mongoose Employee Schema </summary>

# Create Mongoose Employee Schema

<img width="907" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7d99c071-9c4b-4c4c-8107-cc27b8cf6171">

### x-dave-gray/node-app/model/Employee.js:

```js
const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const employeeSchema = new Schema({
  firstname: {
    type: String,
    required: true,
  },
  lastname: {
    type: String,
    required: true,
  },
});

module.exports = mongoose.model("Employee", employeeSchema);
```

# #End </details>

<details>
  <summary>140. MongoDB - Create Mongoose User Schema </summary>

# Create Mongoose User Schema

<img width="907" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/49ce57f4-4c2c-4617-ad92-6728bced34c8">

### x-dave-gray/node-app/model/User.js:

```js
const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const userSchema = new Schema({
  username: {
    type: String,
    required: true,
  },
  roles: {
    User: {
      type: Number,
      default: 2001,
    },
    Editor: Number,
    Admin: Number,
  },
  password: {
    type: String,
    required: true,
  },
  refreshToken: String,
});

module.exports = mongoose.model("User", userSchema);
```

# #End </details>

<details>
  <summary>141. MongoDB - Include Mongoose User data model in registerController  </summary>

# Include Mongoose User data model in registerController

<img width="907" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4e339f9d-01b9-4731-85ba-5f62b1b186a9">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/89978081-16b5-4f50-8c3d-cb5214e32906">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/80072c1a-6442-488f-86d4-b0927f23bd40">
<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/453b9cfd-92e6-41ca-989a-8c00f99934bf">

controller/registerController.js:

```js
const User = require("../model/User");
const bcrypt = require("bcrypt");

const handleNewUser = async (req, res) => {
  const { user, pwd } = req.body;
  if (!user || !pwd)
    return res
      .status(400)
      .json({ message: "Username and password are required." });

  // check for duplicate usernames in the db
  const duplicate = await User.findOne({ username: user }).exec();
  if (duplicate) return res.sendStatus(409); //Conflict

  try {
    //encrypt the password
    const hashedPwd = await bcrypt.hash(pwd, 10);

    //create and store the new user
    const result = await User.create({
      username: user,
      password: hashedPwd,
    });

    // const newUser = new User();
    // newUser.username = user;
    // newUser.password = hashedPwd;
    // const result = await newUser.save();

    console.log(result);

    res.status(201).json({ success: `New user ${user} created!` });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

module.exports = { handleNewUser };
```

# Register new Users

# POST: register user 1 - http://localhost:3500/register

### Body = { "user": "steve1", "pwd": "Aa$12345"}

```bs
{
  "success": "New user steve1 created!"
}
```

```bs
[nodemon] 3.0.1
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `node server.js`
Connected to MongoDB
Server running on port 3500
POST /register
{
  username: 'steve1',
  roles: { User: 2001 },
  password: '$2b$10$5nKyZwiDtnSEIdpWos50JOvPx67U6KvG1GgITV3ktDADNufhBkrFy',
  _id: new ObjectId("64bfd969d2a988dc06e287b2"),
  __v: 0
}
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/aeb9c73b-4283-4cb2-b9e1-f59a34c0d455">


# POST: register user 2 - http://localhost:3500/register

### Body = { "user": "walt1", "pwd": "Aa$12345"}

```bs
{
  "success": "New user walt1 created!"
}
```

```bs
Server running on port 3500
POST /register
{
  username: 'walt1',
  roles: { User: 2001 },
  password: '$2b$10$wcbn1zHGkpyElQ89.dFBTOEFQsK/UwesVf05NVy8hOjtasMNwP83y',
  _id: new ObjectId("64bfd9ded2a988dc06e287b5"),
  __v: 0
}
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b05f109b-9732-431e-a62b-f716119ab341">

# Confirm Users Data in MongoDB

### Mongodb.com -> CompanyDB -> users (Manually Add Admin and Editor roles to walt1)

```js
{
  "_id": {"$oid":"63c6e6dea56c2166c20704ec"},
  "username":"steve1",
  "roles":{
    "User":{"$numberInt":"2001"}
  },
  "password":"$2b$10$4Br2uwwFDIyOtQWag6KqMO7P9UhHxt2F37BiWPR8JkYyYDW96EU0G",
  "__v":{"$numberInt":"0"}
}

{
  "_id":{"$oid":"63c6e768a56c2166c20704ef"},
  "username":"walt1",
  "roles":{
    "User":{"$numberInt":"2001"},
    "Admin":{"$numberInt":"5150"},
    "Editor":{"$numberInt":"1984"}
  },
  "password":"$2b$10$Bat8X9qoWpqt7..ZSkAYPOsxsTb7dXk7n/U2kfodmHIaxjyM363u.",
  "__v":{"$numberInt":"0"}
}
```

<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/59acf65c-f99f-49a0-8d63-6cf4208bcb3f">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9a9e7499-eaf4-44f6-9fe8-287ba46b39bc">

# #End </details>

<details>
  <summary>142. MongoDB - Include Mongoose User data model in refreshTokenController </summary>

# Include Mongoose User data model in refreshTokenController

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/98a5bc59-2b95-478f-a358-667b3dacbcd6">

### x-dave-gray/node-app/controllers/refreshTokenController.js:

```js
const User = require("../model/User");
const jwt = require("jsonwebtoken");

const handleRefreshToken = async (req, res) => {
  const cookies = req.cookies;
  if (!cookies?.jwt) return res.sendStatus(401);
  const refreshToken = cookies.jwt;

  const foundUser = await User.findOne({ refreshToken }).exec();
  if (!foundUser) return res.sendStatus(403); //Forbidden
  // evaluate jwt
  jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET, (err, decoded) => {
    if (err || foundUser.username !== decoded.username)
      return res.sendStatus(403);
    const roles = Object.values(foundUser.roles);
    const accessToken = jwt.sign(
      {
        UserInfo: {
          username: decoded.username,
          roles: roles,
        },
      },
      process.env.ACCESS_TOKEN_SECRET,
      { expiresIn: "10s" }
    );
    res.json({ roles, accessToken });
  });
};

module.exports = { handleRefreshToken };
```

# #End </details>

<details>
  <summary>143. MongoDB - Include Mongoose User data model in logoutController </summary>

# Include Mongoose User data model in logoutController

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/74244022-ca6f-447b-8917-06a0b5343a91">

### x-dave-gray/node-app/controllers/logoutController.js:

```js
const User = require("../model/User");

const handleLogout = async (req, res) => {
  // On client, also delete the accessToken

  const cookies = req.cookies;
  if (!cookies?.jwt) return res.sendStatus(204); //No content
  const refreshToken = cookies.jwt;

  // Is refreshToken in db?
  const foundUser = await User.findOne({ refreshToken }).exec();
  if (!foundUser) {
    res.clearCookie("jwt", { httpOnly: true, sameSite: "None", secure: true });
    return res.sendStatus(204);
  }

  // Delete refreshToken in db
  foundUser.refreshToken = "";
  const result = await foundUser.save();
  console.log(result);

  res.clearCookie("jwt", { httpOnly: true, sameSite: "None", secure: true });
  res.sendStatus(204);
};

module.exports = { handleLogout };
```

# #End </details>

<details>
  <summary>144. MongoDB - Include Mongoose User data model in authController </summary>

# Include Mongoose User data model in authController

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b90562d0-35db-47df-906f-35dd75db9d3c">

### x-dave-gray/node-app/controllers/authController.js:

```js
const User = require("../model/User");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

const handleLogin = async (req, res) => {
  const { user, pwd } = req.body;
  if (!user || !pwd)
    return res
      .status(400)
      .json({ message: "Username and password are required." });

  const foundUser = await User.findOne({ username: user }).exec();
  if (!foundUser) return res.sendStatus(401); //Unauthorized
  // evaluate password
  const match = await bcrypt.compare(pwd, foundUser.password);
  if (match) {
    const roles = Object.values(foundUser.roles).filter(Boolean);
    // create JWTs
    const accessToken = jwt.sign(
      {
        UserInfo: {
          username: foundUser.username,
          roles: roles,
        },
      },
      process.env.ACCESS_TOKEN_SECRET,
      { expiresIn: "10s" }
    );
    const refreshToken = jwt.sign(
      { username: foundUser.username },
      process.env.REFRESH_TOKEN_SECRET,
      { expiresIn: "1d" }
    );
    // Saving refreshToken with current user
    foundUser.refreshToken = refreshToken;
    const result = await foundUser.save();
    console.log(result);
    console.log(roles);

    // Creates Secure Cookie with refresh token
    res.cookie("jwt", refreshToken, {
      httpOnly: true,
      secure: true,
      sameSite: "None",
      maxAge: 24 * 60 * 60 * 1000,
    });

    // Send authorization roles and access token to user
    res.json({ roles, accessToken });
  } else {
    res.sendStatus(401);
  }
};

module.exports = { handleLogin };
```

# #End </details>

<details>
  <summary>145. MongoDB - Testing updated Mongoose Controllers connections </summary>

# Testing updated Mongoose Controllers connections

# POST: register user walt1 (Already Registered) - http://localhost:3500/register

### Body = { "user": "walt1", "pwd": "Aa$12345"}

```bs
Conflict
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/14840d2f-00c5-49d4-9e71-797ed79e3cc5">

# POST: register user tom1 - http://localhost:3500/register

### Body = { "user": "tom1", "pwd": "Aa$12345"}

```bs
{
  "success": "New user tom1 created!"
}
```

# output

```bs
[nodemon] restarting due to changes...
[nodemon] starting `node server.js`
Connected to MongoDB
Server running on port 3500
POST /register
POST /register
{
  username: 'tom1',
  roles: { User: 2001 },
  password: '$2b$10$YKRH9OrF2X/B6XnKKUl6Au93H7NIQtLghkCzUZNXgV7MqTLCO38zu',
  _id: new ObjectId("64c00d7599481bd58c78867f"),
  __v: 0
}
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/24feca03-ca01-4f71-a32c-eb76d8d456da">

# POST: login user walt1 - http://localhost:3500/auth

### Body = { "user": "walt1", "pwd": "Aa$12345"}

# output

```bs
POST /auth
{
  roles: { User: 2001, Admin: 5150, Editor: 1984 },
  _id: new ObjectId("64bfd9ded2a988dc06e287b5"),
  username: 'walt1',
  password: '$2b$10$wcbn1zHGkpyElQ89.dFBTOEFQsK/UwesVf05NVy8hOjtasMNwP83y',
  __v: 0,
  refreshToken: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHQxIiwiaWF0IjoxNjkwMzA4MTAwLCJleHAiOjE2OTAzOTQ1MDB9.JQbSU7MUG6w_QlpE4YWvDsOr5vJlnFj_QtP0DP6OmDc'
}
[ 2001, 1984, 5150 ]
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ea747535-d4bc-4fb1-b10b-131bb9076faf">

# Remember to change secure to false in Dev

### x-dave-gray/node-app/controllers/authController.js:

```bs
// Creates Secure Cookie with refresh token
  res.cookie("jwt", refreshToken, {
    httpOnly: true,
    secure: false, ---> Change to false in development
    sameSite: "None",
    maxAge: 24 * 60 * 60 * 1000,
  });
```

# GET: refresh token for user - http://localhost:3500/refresh

```bs
GET /refresh
POST /auth
{
  roles: { User: 2001, Admin: 5150, Editor: 1984 },
  _id: new ObjectId("64bfd9ded2a988dc06e287b5"),
  username: 'walt1',
  password: '$2b$10$wcbn1zHGkpyElQ89.dFBTOEFQsK/UwesVf05NVy8hOjtasMNwP83y',
  __v: 0,
  refreshToken: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhbHQxIiwiaWF0IjoxNjkwMzA4NTgxLCJleHAiOjE2OTAzOTQ5ODF9.ekITJjCcyyZT-M-qbq2yvXBUApfPn7AxQ4Sb9rp7Fws'
}
[ 2001, 1984, 5150 ]
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/60185943-d5cb-4519-a94a-12d3fc215118">

# GET: logoout user - http://localhost:3500/logout

```bs
204 No Content
```

```bs
GET /logout
{
  roles: { User: 2001, Admin: 5150, Editor: 1984 },
  _id: new ObjectId("64bfd9ded2a988dc06e287b5"),
  username: 'walt1',
  password: '$2b$10$wcbn1zHGkpyElQ89.dFBTOEFQsK/UwesVf05NVy8hOjtasMNwP83y',
  __v: 0,
  refreshToken: ''
}
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e2706fd0-05cd-4dcf-8241-73c9fcbe1795">

# #End </details>

<details>
  <summary>146. MongoDB - (CRUD) Include Mongoose User data model in employeesController </summary>

# (CRUD) Include Mongoose User data model in employeesController

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/359594af-16c9-440e-a106-e08d759b804b">

# Get all employees:

```bs
const getAllEmployees = async (req, res) => {
  const employees = await Employee.find();
  if (!employees)
    return res.status(204).json({ message: "No employees found." });
  res.json(employees);
};
```

# Create a new employee:

```bs
const createNewEmployee = async (req, res) => {
  if (!req?.body?.firstname || !req?.body?.lastname) {
    return res
      .status(400)
      .json({ message: "First and last names are required" });
  }

  try {
    const result = await Employee.create({
      firstname: req.body.firstname,
      lastname: req.body.lastname,
    });

    res.status(201).json(result);
  } catch (err) {
    console.error(err);
  }
};
```

# Update an employee:

```bs
const updateEmployee = async (req, res) => {
  if (!req?.body?.id) {
    return res.status(400).json({ message: "ID parameter is required." });
  }

  const employee = await Employee.findOne({ _id: req.body.id }).exec();
  if (!employee) {
    return res
      .status(204)
      .json({ message: `No employee matches ID ${req.body.id}.` });
  }
  if (req.body?.firstname) employee.firstname = req.body.firstname;
  if (req.body?.lastname) employee.lastname = req.body.lastname;
  const result = await employee.save();
  res.json(result);
};
```

# Delete an employee:

```bs
const deleteEmployee = async (req, res) => {
  if (!req?.body?.id)
    return res.status(400).json({ message: "Employee ID required." });

  const employee = await Employee.findOne({ _id: req.body.id }).exec();
  if (!employee) {
    return res
      .status(204)
      .json({ message: `No employee matches ID ${req.body.id}.` });
  }
  const result = await employee.deleteOne(); //{ _id: req.body.id }
  res.json(result);
};
```

# Get a single employee:

```bs
const getEmployee = async (req, res) => {
  if (!req?.params?.id)
    return res.status(400).json({ message: "Employee ID required." });

  const employee = await Employee.findOne({ _id: req.params.id }).exec();
  if (!employee) {
    return res
      .status(204)
      .json({ message: `No employee matches ID ${req.params.id}.` });
  }
  res.json(employee);
};
```

### x-dave-gray/node-app/controllers/employeesController.js:

```js
const Employee = require("../model/Employee");

const getAllEmployees = async (req, res) => {
  const employees = await Employee.find();
  if (!employees)
    return res.status(204).json({ message: "No employees found." });
  res.json(employees);
};

const createNewEmployee = async (req, res) => {
  if (!req?.body?.firstname || !req?.body?.lastname) {
    return res
      .status(400)
      .json({ message: "First and last names are required" });
  }

  try {
    const result = await Employee.create({
      firstname: req.body.firstname,
      lastname: req.body.lastname,
    });

    res.status(201).json(result);
  } catch (err) {
    console.error(err);
  }
};

const updateEmployee = async (req, res) => {
  if (!req?.body?.id) {
    return res.status(400).json({ message: "ID parameter is required." });
  }

  const employee = await Employee.findOne({ _id: req.body.id }).exec();
  if (!employee) {
    return res
      .status(204)
      .json({ message: `No employee matches ID ${req.body.id}.` });
  }
  if (req.body?.firstname) employee.firstname = req.body.firstname;
  if (req.body?.lastname) employee.lastname = req.body.lastname;
  const result = await employee.save();
  res.json(result);
};

const deleteEmployee = async (req, res) => {
  if (!req?.body?.id)
    return res.status(400).json({ message: "Employee ID required." });

  const employee = await Employee.findOne({ _id: req.body.id }).exec();
  if (!employee) {
    return res
      .status(204)
      .json({ message: `No employee matches ID ${req.body.id}.` });
  }
  const result = await employee.deleteOne(); //{ _id: req.body.id }
  res.json(result);
};

const getEmployee = async (req, res) => {
  if (!req?.params?.id)
    return res.status(400).json({ message: "Employee ID required." });

  const employee = await Employee.findOne({ _id: req.params.id }).exec();
  if (!employee) {
    return res
      .status(204)
      .json({ message: `No employee matches ID ${req.params.id}.` });
  }
  res.json(employee);
};

module.exports = {
  getAllEmployees,
  createNewEmployee,
  updateEmployee,
  deleteEmployee,
  getEmployee,
};
```

# #End </details>

<details>
  <summary>147. MongoDB - Testing updated Mongoose EmployeesController </summary>

# Testing updated Mongoose EmployeesController

# Remember to set the jwt secure to "false" in Dev

### x-dave-gray/node-app/controllers/authController.js:

```bs
 // Creates Secure Cookie with refresh token
    res.cookie("jwt", refreshToken, {
      httpOnly: true,
      secure: false, ---> Change to false in development
      sameSite: "None",
      maxAge: 24 * 60 * 60 * 1000,
    });
```

# POST: login user walt1 - http://localhost:3500/auth

### Body = { "user": "walt1", "pwd": "Aa$12345"}

# output

```bs
{
  "roles": [
    2001,
    1984,
    5150
  ],
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6IndhbHQxIiwicm9sZXMiOlsyMDAxLDE5ODQsNTE1MF19LCJpYXQiOjE2NzQwMzkwMDAsImV4cCI6MTY3NDAzOTAxMH0.2yKx7OzrT_PpMc4zWdJxkEXllLcH432ZkAbbSWDtiSQ"
}
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/809b3311-ae7e-4097-b609-2b9104a39756">

# GET: Get all Employees - http://localhost:3500/employees

### Bearer Token =>

```bs
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6IndhbHQxIiwicm9sZXMiOlsyMDAxLDE5ODQsNTE1MF19LCJpYXQiOjE2NzQwMzkwMDAsImV4cCI6MTY3NDAzOTAxMH0.2yKx7OzrT_PpMc4zWdJxkEXllLcH432ZkAbbSWDtiSQ
```

# output

```bs
[]
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/30d918bf-106c-49b4-82ed-2914e2d2eeca">

# POST: Create a new employee - http://localhost:3500/employees

### Body = {"firstname":"John", "lastname": "Doe"}

### Bearer Token =>

```bs
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6IndhbHQxIiwicm9sZXMiOlsyMDAxLDE5ODQsNTE1MF19LCJpYXQiOjE2NzQwMzkwMDAsImV4cCI6MTY3NDAzOTAxMH0.2yKx7OzrT_PpMc4zWdJxkEXllLcH432ZkAbbSWDtiSQ
```

# output

```bs
{
  "firstname": "John",
  "lastname": "Doe",
  "_id": "63c7d00ccb083a12a95cbfc5",
  "__v": 0
}
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9740a1d3-3cc2-45d4-ae24-51f23bd850e6">

# GET: Get an employee by ID - http://localhost:3500/employees/64c01484432419298d655b7c

### Bearer Token =>

```bs
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6IndhbHQxIiwicm9sZXMiOlsyMDAxLDE5ODQsNTE1MF19LCJpYXQiOjE2OTAzMDk5MTEsImV4cCI6MTY5MDMwOTkyMX0.njUgPooaA7UUSdy6oyT3_A2TWcjt3Pu7XMvU7cg4M-8
```

```bs
Status: 200 OK
```

# output

```bs
{
  "_id": "64c01484432419298d655b7c",
  "firstname": "John",
  "lastname": "Doe",
  "__v": 0
}
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/08b56ead-aedf-4692-bc49-d550ee8621a9">

# PUT: Update an employee by ID - http://localhost:3500/employees

### Body = {"id": "64c01484432419298d655b7c", "lastname": "Brown"}

### Bearer Token =>

```bs
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6IndhbHQxIiwicm9sZXMiOlsyMDAxLDE5ODQsNTE1MF19LCJpYXQiOjE2NzQwMzkwMDAsImV4cCI6MTY3NDAzOTAxMH0.2yKx7OzrT_PpMc4zWdJxkEXllLcH432ZkAbbSWDtiSQ
```

```bs
Status: 200 OK
```

# output

```bs
{
  "_id": "64c01484432419298d655b7c",
  "firstname": "John",
  "lastname": "Brown",
  "__v": 0
}
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/083f287e-490f-4818-88c3-0da0a2dcefdd">

# DEL: Delete an employee by ID - http://localhost:3500/employees

### Body = {"id": "64c01484432419298d655b7c"}

### Bearer Token =>

```bs
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6IndhbHQxIiwicm9sZXMiOlsyMDAxLDE5ODQsNTE1MF19LCJpYXQiOjE2NzQwMzkwMDAsImV4cCI6MTY3NDAzOTAxMH0.2yKx7OzrT_PpMc4zWdJxkEXllLcH432ZkAbbSWDtiSQ
```

```bs
Status: 200 OK
```

```bs
{
  "_id": "63c7d00ccb083a12a95cbfc5",
  "firstname": "John",
  "lastname": "Brown",
  "__v": 0
}
```

<img width="909" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a509ba81-c731-4016-a45c-98f3846c48c1">

# #End </details>

<details>
  <summary>148.  MongoDB - Create User Admin routes </summary>

# Create User Admin routes

<img width="1068" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/942f9563-7593-45c9-b2b5-cf9b958b2569">
<img width="1068" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/93918923-afc2-4b88-9a1b-ec7f603588aa">
<img width="1068" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3ed4ff97-e338-4a36-ba3c-2580a0507dae">
<img width="1068" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/18b38a57-cfd9-470e-9b57-398bf6fdd431">
<img width="1068" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/39e348a9-2201-44d4-bd52-54f9072fc0c3">
<img width="1068" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e12db01d-1625-4d24-a1a7-8282d1eb0963">

### x-dave-gray/node-app/routes/api/users.js:

```js
const express = require("express");
const router = express.Router();
const usersController = require("../../controllers/usersController");
const ROLES_LIST = require("../../config/roles_list");
const verifyRoles = require("../../middleware/verifyRoles");

router
  .route("/")
  .get(verifyRoles(ROLES_LIST.Admin), usersController.getAllUsers)
  .delete(verifyRoles(ROLES_LIST.Admin), usersController.deleteUser);

router
  .route("/:id")
  .get(verifyRoles(ROLES_LIST.Admin), usersController.getUser);

module.exports = router;
```

### x-dave-gray/node-app/controllers/usersController.js:

```js
const User = require("../model/User");

const getAllUsers = async (req, res) => {
  const users = await User.find();
  if (!users) return res.status(204).json({ message: "No users found" });
  res.json(users);
};

const deleteUser = async (req, res) => {
  if (!req?.body?.id)
    return res.status(400).json({ message: "User ID required" });
  const user = await User.findOne({ _id: req.body.id }).exec();
  if (!user) {
    return res
      .status(204)
      .json({ message: `User ID ${req.body.id} not found` });
  }
  const result = await user.deleteOne({ _id: req.body.id });
  res.json(result);
};

const getUser = async (req, res) => {
  if (!req?.params?.id)
    return res.status(400).json({ message: "User ID required" });
  const user = await User.findOne({ _id: req.params.id }).exec();
  if (!user) {
    return res
      .status(204)
      .json({ message: `User ID ${req.params.id} not found` });
  }
  res.json(user);
};

module.exports = {
  getAllUsers,
  deleteUser,
  getUser,
};
```

### x-dave-gray/node-app/routes/api/employees.js:

```js
const express = require("express");
const router = express.Router();
const employeesController = require("../../controllers/employeesController");
const ROLES_LIST = require("../../config/roles_list");
const verifyRoles = require("../../middleware/verifyRoles");

router
  .route("/")
  .get(employeesController.getAllEmployees)
  .post(
    verifyRoles(ROLES_LIST.Admin, ROLES_LIST.Editor),
    employeesController.createNewEmployee
  )
  .put(
    verifyRoles(ROLES_LIST.Admin, ROLES_LIST.Editor),
    employeesController.updateEmployee
  )
  .delete(verifyRoles(ROLES_LIST.Admin), employeesController.deleteEmployee);

router.route("/:id").get(employeesController.getEmployee);

module.exports = router;
```

### x-dave-gray/node-app/controllers/employeesController.js:

```js
const Employee = require("../model/Employee");

const getAllEmployees = async (req, res) => {
  const employees = await Employee.find();
  if (!employees)
    return res.status(204).json({ message: "No employees found." });
  res.json(employees);
};

const createNewEmployee = async (req, res) => {
  if (!req?.body?.firstname || !req?.body?.lastname) {
    return res
      .status(400)
      .json({ message: "First and last names are required" });
  }

  try {
    const result = await Employee.create({
      firstname: req.body.firstname,
      lastname: req.body.lastname,
    });

    res.status(201).json(result);
  } catch (err) {
    console.error(err);
  }
};

const updateEmployee = async (req, res) => {
  if (!req?.body?.id) {
    return res.status(400).json({ message: "ID parameter is required." });
  }

  const employee = await Employee.findOne({ _id: req.body.id }).exec();
  if (!employee) {
    return res
      .status(204)
      .json({ message: `No employee matches ID ${req.body.id}.` });
  }
  if (req.body?.firstname) employee.firstname = req.body.firstname;
  if (req.body?.lastname) employee.lastname = req.body.lastname;
  const result = await employee.save();
  res.json(result);
};

const deleteEmployee = async (req, res) => {
  if (!req?.body?.id)
    return res.status(400).json({ message: "Employee ID required." });

  const employee = await Employee.findOne({ _id: req.body.id }).exec();
  if (!employee) {
    return res
      .status(204)
      .json({ message: `No employee matches ID ${req.body.id}.` });
  }
  const result = await employee.deleteOne(); //{ _id: req.body.id }
  res.json(result);
};

const getEmployee = async (req, res) => {
  if (!req?.params?.id)
    return res.status(400).json({ message: "Employee ID required." });

  const employee = await Employee.findOne({ _id: req.params.id }).exec();
  if (!employee) {
    return res
      .status(204)
      .json({ message: `No employee matches ID ${req.params.id}.` });
  }
  res.json(employee);
};

module.exports = {
  getAllEmployees,
  createNewEmployee,
  updateEmployee,
  deleteEmployee,
  getEmployee,
};
```

### x-dave-gray/node-app/config/roles_list.js:

```js
const ROLES_LIST = {
  Admin: 5150,
  Editor: 1984,
  User: 2001,
};

module.exports = ROLES_LIST;
```

### x-dave-gray/node-app/middleware/verifyRoles.js:

```js
const verifyRoles = (...allowedRoles) => {
  return (req, res, next) => {
    if (!req?.roles) return res.sendStatus(401);
    const rolesArray = [...allowedRoles];
    const result = req.roles
      .map((role) => rolesArray.includes(role))
      .find((val) => val === true);
    if (!result) return res.sendStatus(401);
    next();
  };
};

module.exports = verifyRoles;
```

# #End </details>

+DEPLOY REACT

<details>
  <summary>149. Deploy Node Server to Glitch </summary>

# Git Commands:

```bs
#Just follow next steps in console terminal ;)
git init	#Initialize git in folder
git add .	#add all files of folder to be pushed
git commit -m "First commit"	#add first commit
git remote add origin remote_repository_URL #replace with your remote repo url
git remote -v	#verify that your remote repository url is properly found
git branch -M main  #change main branch name to main
git push --force origin main	#force pushing your project into github repo

git remote set-url origin https://[token]@github.com/[username]/[repository]
git remote set-url origin https://[token]@github.com/omeatai/deploy_node_server.git
https://github.com/omeatai/deploy_node_server.git

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
```

# Create Glitch Remix Button:

```bs
[<img src="https://cdn.gomix.com/2bdfb3f8-05ef-4035-a06e-2043962a3a13%2Fremix-button.svg" width="163px" />](https://glitch.com/edit/#!/import/github/omeatai/deploy_node_server)
```

```bs
https://glitch.com/
```

# #End </details>

# REACT AUTH

+REACT AUTH

<details>
  <summary>150. React Auth - Create Register Component with Custom Validation</summary>

# Create Register Component with Custom Validation

<img width="966" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7697bb56-5a92-40c2-9b80-773e286a454d">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1fff523e-4d8c-4d1f-94a1-165bc9e4ee07">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bd3c5d98-b150-4251-aa91-154c81d1b243">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/630162af-e43d-4b2a-9216-ccdad0ffc2a4">
<img width="1180" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8524ab0c-22c7-4b55-b084-1649da2c1d3f">
<img width="1288" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/30794101-a191-42b0-a2e2-3ccc80e87f8c">

### Add Font-Awesome SVG Core and Icon Packages

```bs
npm --save @fortawesome/fontawesome-svg-core @fortawesome/free-solid-svg-icons @fortawesome/react-fontawesome@latest
npm i --save @fortawesome/fontawesome-svg-core
npm i --save @fortawesome/free-solid-svg-icons
npm i --save @fortawesome/react-fontawesome@latest

yarn add --save @fortawesome/fontawesome-svg-core @fortawesome/free-solid-svg-icons @fortawesome/react-fontawesome@latest
```

### x-dave-gray/react-auth/src/App.js:

```js
import Register from "./Register";

function App() {
  return (
    <div className="App">
      <Register />
    </div>
  );
}

export default App;
```

### x-dave-gray/react-auth/src/Register.js:

```js
import { useRef, useState, useEffect } from "react";
import {
  faCheck,
  faTimes,
  faInfoCircle,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const USER_REGEX = /^[A-z][A-z0-9-_]{3,23}$/;
const PWD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;

const Register = () => {
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [validName, setValidName] = useState(false);
  const [userFocus, setUserFocus] = useState(false);

  const [pwd, setPwd] = useState("");
  const [validPwd, setValidPwd] = useState(false);
  const [pwdFocus, setPwdFocus] = useState(false);

  const [matchPwd, setMatchPwd] = useState("");
  const [validMatch, setValidMatch] = useState(false);
  const [matchFocus, setMatchFocus] = useState(false);

  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    const result = USER_REGEX.test(user);
    console.log(result);
    console.log(user);
    setValidName(result);
    //setValidName(USER_REGEX.test(user));
  }, [user]);

  useEffect(() => {
    const result = PWD_REGEX.test(pwd);
    console.log(result);
    console.log(pwd);
    setValidPwd(result);
    //setValidPwd(PWD_REGEX.test(pwd));
    const match = pwd === matchPwd;
    setValidMatch(match);
    //setValidMatch(pwd === matchPwd);
  }, [pwd, matchPwd]);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd, matchPwd]);

  return (
    <section>
      <p
        ref={errRef}
        className={errMsg ? "errmsg" : "offscreen"}
        aria-live="assertive"
      >
        {errMsg}
      </p>
      <h1>Register</h1>
      <form>
        {/* Username */}
        <label htmlFor="username">
          Username:
          <FontAwesomeIcon
            icon={faCheck}
            className={validName ? "valid" : "hide"}
          />
          <FontAwesomeIcon
            icon={faTimes}
            className={validName || !user ? "hide" : "invalid"}
          />
        </label>
        <input
          type="text"
          id="username"
          ref={userRef}
          autoComplete="off"
          onChange={(e) => setUser(e.target.value)}
          value={user}
          required
          aria-invalid={validName ? "false" : "true"}
          aria-describedby="uidnote"
          onFocus={() => setUserFocus(true)}
          onBlur={() => setUserFocus(false)}
        />
        <p
          id="uidnote"
          className={
            userFocus && user && !validName ? "instructions" : "offscreen"
          }
        >
          <FontAwesomeIcon icon={faInfoCircle} />
          4 to 24 characters.
          <br />
          Must begin with a letter.
          <br />
          Letters, numbers, underscores, hyphens allowed.
        </p>

        {/* Password */}
        <label htmlFor="password">
          Password:
          <FontAwesomeIcon
            icon={faCheck}
            className={validPwd ? "valid" : "hide"}
          />
          <FontAwesomeIcon
            icon={faTimes}
            className={validPwd || !pwd ? "hide" : "invalid"}
          />
        </label>
        <input
          type="password"
          id="password"
          onChange={(e) => setPwd(e.target.value)}
          value={pwd}
          required
          aria-invalid={validPwd ? "false" : "true"}
          aria-describedby="pwdnote"
          onFocus={() => setPwdFocus(true)}
          onBlur={() => setPwdFocus(false)}
        />
        <p
          id="pwdnote"
          className={pwdFocus && !validPwd ? "instructions" : "offscreen"}
        >
          <FontAwesomeIcon icon={faInfoCircle} />
          8 to 24 characters.
          <br />
          Must include uppercase and lowercase letters, a number and a special character.
          <br />
          Allowed special characters: <span aria-label="exclamation mark">
            !
          </span> <span aria-label="at symbol">@</span> <span aria-label="hashtag">
            #
          </span> <span aria-label="dollar sign">$</span> <span aria-label="percent">%</span>
        </p>

        {/* Confirm Password */}
        <label htmlFor="confirm_pwd">
          Confirm Password:
          <FontAwesomeIcon
            icon={faCheck}
            className={validMatch && matchPwd ? "valid" : "hide"}
          />
          <FontAwesomeIcon
            icon={faTimes}
            className={validMatch || !matchPwd ? "hide" : "invalid"}
          />
        </label>
        <input
          type="password"
          id="confirm_pwd"
          onChange={(e) => setMatchPwd(e.target.value)}
          value={matchPwd}
          required
          aria-invalid={validMatch ? "false" : "true"}
          aria-describedby="confirmnote"
          onFocus={() => setMatchFocus(true)}
          onBlur={() => setMatchFocus(false)}
        />
        <p
          id="confirmnote"
          className={matchFocus && !validMatch ? "instructions" : "offscreen"}
        >
          <FontAwesomeIcon icon={faInfoCircle} />
          Must match the first password input field.
        </p>

        <button
          disabled={!validName || !validPwd || !validMatch ? true : false}
        >
          Sign Up
        </button>
      </form>
      <p>
        Already registered?
        <br />
        <span className="line">
          {/*put router link here*/}
          <a href="#">Sign In</a>
        </span>
      </p>
    </section>
  );
};

export default Register;
```

### x-dave-gray/react-auth/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Nunito&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-family: "Nunito", sans-serif;
  font-size: 22px;
  color: #fff;
}

body {
  min-height: 100vh;
  background-color: dodgerblue;
}

.App {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 1rem 0.5rem;
}

section {
  width: 100%;
  max-width: 420px;
  min-height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 1rem;
  background-color: rgba(0, 0, 0, 0.4);
}

form {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  flex-grow: 1;
  padding-bottom: 1rem;
}

a,
a:visited {
  color: #fff;
}

input[type="text"],
input[type="password"],
button,
textarea {
  font-family: "Nunito", sans-serif;
  font-size: 22px;
  padding: 0.25rem;
  border-radius: 0.5rem;
}

label,
button {
  margin-top: 1rem;
}

button {
  padding: 0.5rem;
}

.instructions {
  font-size: 0.75rem;
  border-radius: 0.5rem;
  background: #000;
  color: #fff;
  padding: 0.25rem;
  position: relative;
  bottom: -10px;
}

.instructions > svg {
  margin-right: 0.25rem;
}

.offscreen {
  position: absolute;
  left: -9999px;
}

.hide {
  display: none;
}

.valid {
  color: limegreen;
  margin-left: 0.25rem;
}

.invalid {
  color: red;
  margin-left: 0.25rem;
}

.errmsg {
  background-color: lightpink;
  color: firebrick;
  font-weight: bold;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
}

.line {
  display: inline-block;
}
```

# #End  </details>

<details>
  <summary>151. React Auth - Handle Submit with Axios to Register Inputs</summary>

# Handle Submit with Axios to Register Inputs

<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8562bebf-bb49-465d-8d14-690693dcea54">
<img width="967" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7ab439a9-b2ac-4079-b145-c06289dcedf7">
<img width="1178" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c4f474d2-0aca-4042-b0a3-9f9dde315792">
<img width="1106" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1619ac39-da9a-409b-9b19-ae402274f793">
<img width="1106" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7a37ae8b-e8cf-46fa-bd00-4051718c640c">
<img width="1106" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/cccbdda4-468e-4b6e-a198-b6f21a0b88b7">
<img width="1106" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9cd6151f-46d0-4b83-a466-e75c9c20be4f">
<img width="1294" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7ccaf28c-3a0f-49ff-ab10-2ae530275761">

# Install Axios:

```bs
npm install axios -S
```

### x-dave-gray/react-auth/src/api/axios.js:

```js
import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:3500",
});
```

### x-dave-gray/react-auth/src/App.js:

```js
import Register from "./Register";

function App() {
  return (
    <div className="App">
      <Register />
    </div>
  );
}

export default App;
```

### x-dave-gray/react-auth/src/Register.js:

```js
import React, { useRef, useState, useEffect } from "react";
import {
  faCheck,
  faTimes,
  faInfoCircle,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import axios from "./api/axios";

const USER_REGEX = /^[A-z][A-z0-9-_]{3,23}$/;
const PWD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;
const REGISTER_URL = "/register";

const Register = () => {
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [validName, setValidName] = useState(false);
  const [userFocus, setUserFocus] = useState(false);

  const [pwd, setPwd] = useState("");
  const [validPwd, setValidPwd] = useState(false);
  const [pwdFocus, setPwdFocus] = useState(false);

  const [matchPwd, setMatchPwd] = useState("");
  const [validMatch, setValidMatch] = useState(false);
  const [matchFocus, setMatchFocus] = useState(false);

  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    const result = USER_REGEX.test(user);
    //console.log(result);
    //console.log(user);
    setValidName(result);
    //setValidName(USER_REGEX.test(user));
  }, [user]);

  useEffect(() => {
    const result = PWD_REGEX.test(pwd);
    //console.log(result);
    //console.log(pwd);
    setValidPwd(result);
    //setValidPwd(PWD_REGEX.test(pwd));
    const match = pwd === matchPwd;
    setValidMatch(match);
    //setValidMatch(pwd === matchPwd);
  }, [pwd, matchPwd]);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd, matchPwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    // if button enabled with JS hack
    const v1 = USER_REGEX.test(user);
    const v2 = PWD_REGEX.test(pwd);
    if (!v1 || !v2) {
      setErrMsg("Invalid Entry");
      return;
    }
    //console.log(user, pwd);
    //setSuccess(true);
    try {
      const response = await axios.post(
        REGISTER_URL,
        JSON.stringify({ user, pwd }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      console.log(response?.data);
      console.log(response?.accessToken);
      console.log(JSON.stringify(response));
      setSuccess(true);
      //clear state and controlled inputs
      //need value attrib on inputs for this
      setUser("");
      setPwd("");
      setMatchPwd("");
    } catch (err) {
      if (!err?.response) {
        setErrMsg("No Server Response");
      } else if (err.response?.status === 409) {
        setErrMsg("Username Taken");
      } else {
        setErrMsg("Registration Failed");
      }
      errRef.current.focus();
    }
  };

  return (
    <React.Fragment>
      {/* {success ? () : ()} */}
      {success ? (
        <section>
          <h1>Success!</h1>
          <p>
            <a href="#">Sign In</a>
          </p>
        </section>
      ) : (
        <section>
          <p
            ref={errRef}
            className={errMsg ? "errmsg" : "offscreen"}
            aria-live="assertive"
          >
            {errMsg}
          </p>
          <h1>Register</h1>
          <form onSubmit={handleSubmit}>
            {/* Username */}
            <label htmlFor="username">
              Username:
              <FontAwesomeIcon
                icon={faCheck}
                className={validName ? "valid" : "hide"}
              />
              <FontAwesomeIcon
                icon={faTimes}
                className={validName || !user ? "hide" : "invalid"}
              />
            </label>
            <input
              type="text"
              id="username"
              ref={userRef}
              autoComplete="off"
              onChange={(e) => setUser(e.target.value)}
              value={user}
              required
              aria-invalid={validName ? "false" : "true"}
              aria-describedby="uidnote"
              onFocus={() => setUserFocus(true)}
              onBlur={() => setUserFocus(false)}
            />
            <p
              id="uidnote"
              className={
                userFocus && user && !validName ? "instructions" : "offscreen"
              }
            >
              <FontAwesomeIcon icon={faInfoCircle} />
              4 to 24 characters.
              <br />
              Must begin with a letter.
              <br />
              Letters, numbers, underscores, hyphens allowed.
            </p>

            {/* Password */}
            <label htmlFor="password">
              Password:
              <FontAwesomeIcon
                icon={faCheck}
                className={validPwd ? "valid" : "hide"}
              />
              <FontAwesomeIcon
                icon={faTimes}
                className={validPwd || !pwd ? "hide" : "invalid"}
              />
            </label>
            <input
              type="password"
              id="password"
              onChange={(e) => setPwd(e.target.value)}
              value={pwd}
              required
              aria-invalid={validPwd ? "false" : "true"}
              aria-describedby="pwdnote"
              onFocus={() => setPwdFocus(true)}
              onBlur={() => setPwdFocus(false)}
            />
            <p
              id="pwdnote"
              className={pwdFocus && !validPwd ? "instructions" : "offscreen"}
            >
              <FontAwesomeIcon icon={faInfoCircle} />
              8 to 24 characters.
              <br />
              Must include uppercase and lowercase letters, a number and a special
              character.
              <br />
              Allowed special characters: <span aria-label="exclamation mark">
                !
              </span> <span aria-label="at symbol">@</span> <span aria-label="hashtag">
                #
              </span> <span aria-label="dollar sign">$</span> <span aria-label="percent">%</span>
            </p>

            {/* Confirm Password */}
            <label htmlFor="confirm_pwd">
              Confirm Password:
              <FontAwesomeIcon
                icon={faCheck}
                className={validMatch && matchPwd ? "valid" : "hide"}
              />
              <FontAwesomeIcon
                icon={faTimes}
                className={validMatch || !matchPwd ? "hide" : "invalid"}
              />
            </label>
            <input
              type="password"
              id="confirm_pwd"
              onChange={(e) => setMatchPwd(e.target.value)}
              value={matchPwd}
              required
              aria-invalid={validMatch ? "false" : "true"}
              aria-describedby="confirmnote"
              onFocus={() => setMatchFocus(true)}
              onBlur={() => setMatchFocus(false)}
            />
            <p
              id="confirmnote"
              className={
                matchFocus && !validMatch ? "instructions" : "offscreen"
              }
            >
              <FontAwesomeIcon icon={faInfoCircle} />
              Must match the first password input field.
            </p>

            <button
              disabled={!validName || !validPwd || !validMatch ? true : false}
            >
              Sign Up
            </button>
          </form>
          <p>
            Already registered?
            <br />
            <span className="line">
              {/*put router link here*/}
              <a href="#">Sign In</a>
            </span>
          </p>
        </section>
      )}
    </React.Fragment>
  );
};

export default Register;
```

# Add React Frontend to Node backend Server -

### allowedOrigins.js (in backend server):

### x-dave-gray/node-app/config/allowedOrigins.js:

```js
const allowedOrigins = [
  "https://www.yoursite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
  "http://localhost:3000",
];

module.exports = allowedOrigins;
```

### x-dave-gray/react-auth/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Nunito&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-family: "Nunito", sans-serif;
  font-size: 22px;
  color: #fff;
}

body {
  min-height: 100vh;
  background-color: dodgerblue;
}

.App {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 1rem 0.5rem;
}

section {
  width: 100%;
  max-width: 420px;
  min-height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 1rem;
  background-color: rgba(0, 0, 0, 0.4);
}

form {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  flex-grow: 1;
  padding-bottom: 1rem;
}

a,
a:visited {
  color: #fff;
}

input[type="text"],
input[type="password"],
button,
textarea {
  font-family: "Nunito", sans-serif;
  font-size: 22px;
  padding: 0.25rem;
  border-radius: 0.5rem;
}

label,
button {
  margin-top: 1rem;
}

button {
  padding: 0.5rem;
}

.instructions {
  font-size: 0.75rem;
  border-radius: 0.5rem;
  background: #000;
  color: #fff;
  padding: 0.25rem;
  position: relative;
  bottom: -10px;
}

.instructions > svg {
  margin-right: 0.25rem;
}

.offscreen {
  position: absolute;
  left: -9999px;
}

.hide {
  display: none;
}

.valid {
  color: limegreen;
  margin-left: 0.25rem;
}

.invalid {
  color: red;
  margin-left: 0.25rem;
}

.errmsg {
  background-color: lightpink;
  color: firebrick;
  font-weight: bold;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
}

.line {
  display: inline-block;
}
```

# #End  </details>

<details>
  <summary>152. React Auth - Create User Login Component </summary>

# Create User Login Component

<img width="1099" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ca3a38b8-978e-497f-adda-fac9f4dddffa">
<img width="1102" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a3ca7eec-7773-4020-84a5-ab8ea675c058">
<img width="1102" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a54b7587-88fe-4a3f-a65b-7d9d7d6d1674">
<img width="1102" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b3bf8e81-8af8-4e58-92dd-49aaeabd8a19">
<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/91ecb8c5-5af7-4917-ba1a-e1cab23c5eec">

### x-dave-gray/react-auth/src/App.js:

```js
import Register from "./Register";
import Login from "./Login";

function App() {
  return (
    <main className="App">
      <Login />
    </main>
  );
}

export default App;
```

### x-dave-gray/react-auth/src/Login.js:

```js
import { useRef, useState, useEffect, useContext } from "react";

const Login = () => {
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd]);

  const handleSubmit = () => {};

  return (
    <section>
      <p
        ref={errRef}
        className={errMsg ? "errmsg" : "offscreen"}
        aria-live="assertive"
      >
        {errMsg}
      </p>
      <h1>Sign In</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          ref={userRef}
          autoComplete="off"
          onChange={(e) => setUser(e.target.value)}
          value={user}
          required
        />

        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          onChange={(e) => setPwd(e.target.value)}
          value={pwd}
          required
        />
        <button>Sign In</button>
      </form>
      <p>
        Need an Account?
        <br />
        <span className="line">
          {/*put router link here*/}
          <a href="#">Sign Up</a>
        </span>
      </p>
    </section>
  );
};

export default Login;
```

### x-dave-gray/react-auth/src/index.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Nunito&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-family: "Nunito", sans-serif;
  font-size: 22px;
  color: #fff;
}

body {
  min-height: 100vh;
  background-color: dodgerblue;
}

.App {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 1rem 0.5rem;
}

section {
  width: 100%;
  max-width: 420px;
  min-height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 1rem;
  background-color: rgba(0, 0, 0, 0.4);
}

form {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  flex-grow: 1;
  padding-bottom: 1rem;
}

a,
a:visited {
  color: #fff;
}

input[type="text"],
input[type="password"],
button,
textarea {
  font-family: "Nunito", sans-serif;
  font-size: 22px;
  padding: 0.25rem;
  border-radius: 0.5rem;
}

label,
button {
  margin-top: 1rem;
}

button {
  padding: 0.5rem;
}

.instructions {
  font-size: 0.75rem;
  border-radius: 0.5rem;
  background: #000;
  color: #fff;
  padding: 0.25rem;
  position: relative;
  bottom: -10px;
}

.instructions > svg {
  margin-right: 0.25rem;
}

.offscreen {
  position: absolute;
  left: -9999px;
}

.hide {
  display: none;
}

.valid {
  color: limegreen;
  margin-left: 0.25rem;
}

.invalid {
  color: red;
  margin-left: 0.25rem;
}

.errmsg {
  background-color: lightpink;
  color: firebrick;
  font-weight: bold;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
}

.line {
  display: inline-block;
}
```



# #End  </details>

<details>
  <summary>153. React Auth - Handle Submit to Login Input </summary>

# Handle Submit to Login Input

<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2aa1dbf4-ad55-4c52-9379-7df99a4cdbf5">
<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8879c69e-bcd0-4ede-b8eb-fbffd07196b6">
<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/817d515b-0c6a-4676-8c67-036d98f3b69b">
<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6451c950-63c1-4b2c-b68e-458897cb2621">

### x-dave-gray/react-auth/src/Login.js:

```js
import { useRef, useState, useEffect, useContext } from "react";

const Login = () => {
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(user, pwd);
    setUser("");
    setPwd("");
    setSuccess(true);
  };

  return (
    <>
      {success ? (
        <section>
          <h1>You are logged in!</h1>
          <br />
          <p>
            <a href="#">Go to Home</a>
          </p>
        </section>
      ) : (
        <section>
          <p
            ref={errRef}
            className={errMsg ? "errmsg" : "offscreen"}
            aria-live="assertive"
          >
            {errMsg}
          </p>
          <h1>Sign In</h1>
          <form onSubmit={handleSubmit}>
            <label htmlFor="username">Username:</label>
            <input
              type="text"
              id="username"
              ref={userRef}
              autoComplete="off"
              onChange={(e) => setUser(e.target.value)}
              value={user}
              required
            />

            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              onChange={(e) => setPwd(e.target.value)}
              value={pwd}
              required
            />
            <button>Sign In</button>
          </form>
          <p>
            Need an Account?
            <br />
            <span className="line">
              {/*put router link here*/}
              <a href="#">Sign Up</a>
            </span>
          </p>
        </section>
      )}
    </>
  );
};

export default Login;
```

# #End  </details>

<details>
  <summary>154. React Auth -  Using Context API to create Auth Provider</summary>

# Using Context API to create Auth Provider

<img width="1028" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c3bcdfdf-476a-4e21-bac0-ada0d2ddcf42">
<img width="1028" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/38e2cabe-4810-4fdd-b565-5c25764919ea">
<img width="1028" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0fb19fb2-7bf3-46df-92df-e6fd3092820c">
<img width="1028" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/38d19df8-3164-4a99-80ba-c7d4807ae681">
<img width="1290" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1c7caa77-9108-4012-a718-80d10729e83c">

### x-dave-gray/react-auth/src/context/AuthProvider.js:

```js
import { createContext, useState } from "react";

const AuthContext = createContext({});

export const AuthProvider = ({ children }) => {
  const [auth, setAuth] = useState({});

  return (
    <AuthContext.Provider value={{ auth, setAuth }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
```

### x-dave-gray/react-auth/src/index.js:

```js
import React from "react";
import { createRoot } from "react-dom/client";
// import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { AuthProvider } from "./context/AuthProvider";

const root = createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <AuthProvider>
      <App />
    </AuthProvider>
  </React.StrictMode>
);
```

### x-dave-gray/react-auth/src/App.js:

```bs
import Login from "./Login";

function App() {
  return (
    <main className="App">
      <Login />
    </main>
  );
}

export default App;
```

### x-dave-gray/react-auth/src/Login.js:

```bs
import AuthContext from "./context/AuthProvider";

const Login = () => {
  const { setAuth } = useContext(AuthContext);

```

```js
import { useRef, useState, useEffect, useContext } from "react";
import AuthContext from "./context/AuthProvider";

const Login = () => {
  const { setAuth } = useContext(AuthContext);
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(user, pwd);
    setUser("");
    setPwd("");
    setSuccess(true);
  };

  return (
    <>
      {success ? (
        <section>
          <h1>You are logged in!</h1>
          <br />
          <p>
            <a href="#">Go to Home</a>
          </p>
        </section>
      ) : (
        <section>
          <p
            ref={errRef}
            className={errMsg ? "errmsg" : "offscreen"}
            aria-live="assertive"
          >
            {errMsg}
          </p>
          <h1>Sign In</h1>
          <form onSubmit={handleSubmit}>
            <label htmlFor="username">Username:</label>
            <input
              type="text"
              id="username"
              ref={userRef}
              autoComplete="off"
              onChange={(e) => setUser(e.target.value)}
              value={user}
              required
            />

            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              onChange={(e) => setPwd(e.target.value)}
              value={pwd}
              required
            />
            <button>Sign In</button>
          </form>
          <p>
            Need an Account?
            <br />
            <span className="line">
              {/*put router link here*/}
              <a href="#">Sign Up</a>
            </span>
          </p>
        </section>
      )}
    </>
  );
};

export default Login;
```

# #End  </details>

<details>
  <summary>155. React Auth - Using Axios to handle Login Submit to NodeJS Server</summary>

# Using Axios to handle Login Submit to NodeJS Server

<img width="1028" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ed14c8a5-c138-4643-ad1a-58676f33e94a">
<img width="1028" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2bfcc5ac-172f-47d6-8679-846e9fbf642f">

# Install Axios

```bs
npm i axios
```

### x-dave-gray/react-auth/src/api/axios.js:

```js
import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:3500",
});
```

### x-dave-gray/react-auth/src/Login.js:

```bs
import axios from './api/axios';
const LOGIN_URL = '/auth';
```

```js
import { useRef, useState, useEffect, useContext } from "react";
import AuthContext from "./context/AuthProvider";

import axios from "./api/axios";
const LOGIN_URL = "/auth";

const Login = () => {
  const { setAuth } = useContext(AuthContext);
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        LOGIN_URL,
        JSON.stringify({ user, pwd }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      console.log(JSON.stringify(response?.data));
      //console.log(JSON.stringify(response));
      const accessToken = response?.data?.accessToken;
      const roles = response?.data?.roles;
      setAuth({ user, pwd, roles, accessToken });
      setUser("");
      setPwd("");
      setSuccess(true);
    } catch (err) {
      if (!err?.response) {
        setErrMsg("No Server Response");
      } else if (err.response?.status === 400) {
        setErrMsg("Missing Username or Password");
      } else if (err.response?.status === 401) {
        setErrMsg("Unauthorized");
      } else {
        setErrMsg("Login Failed");
      }
      errRef.current.focus();
    }
  };

  return (
    <>
      {success ? (
        <section>
          <h1>You are logged in!</h1>
          <br />
          <p>
            <a href="#">Go to Home</a>
          </p>
        </section>
      ) : (
        <section>
          <p
            ref={errRef}
            className={errMsg ? "errmsg" : "offscreen"}
            aria-live="assertive"
          >
            {errMsg}
          </p>
          <h1>Sign In</h1>
          <form onSubmit={handleSubmit}>
            <label htmlFor="username">Username:</label>
            <input
              type="text"
              id="username"
              ref={userRef}
              autoComplete="off"
              onChange={(e) => setUser(e.target.value)}
              value={user}
              required
            />

            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              onChange={(e) => setPwd(e.target.value)}
              value={pwd}
              required
            />
            <button>Sign In</button>
          </form>
          <p>
            Need an Account?
            <br />
            <span className="line">
              {/*put router link here*/}
              <a href="#">Sign Up</a>
            </span>
          </p>
        </section>
      )}
    </>
  );
};

export default Login;
```

# #End  </details>

<details>
  <summary>156. React Auth - Setup Node Server and Test</summary>

# Setup Node Server and Test

<img width="1099" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/372025b8-85c7-46e4-a0d2-36f4f68a6434">

<img width="1099" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bc36b01e-5c37-4f08-b9f3-d536680c4f2b">

# Backend

### x-dave-gray/node-app/config/allowedOrigins.js:

```js
const allowedOrigins = [
  "https://www.yoursite.com",
  "http://127.0.0.1:5500",
  "http://localhost:3500",
  "http://localhost:3000", // include React URL for CORS to allow
];

module.exports = allowedOrigins;
```

### x-dave-gray/node-app/controllers/authController.js:

```bs
// Get rid of nulls with Boolean
if (match) {
    const roles = Object.values(foundUser.roles).filter(Boolean);

// Send authorization roles and access token to user
res.json({ roles, accessToken });
```

```js
const User = require("../model/User");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

const handleLogin = async (req, res) => {
  const { user, pwd } = req.body;
  if (!user || !pwd)
    return res
      .status(400)
      .json({ message: "Username and password are required." });

  const foundUser = await User.findOne({ username: user }).exec();

  if (!foundUser) return res.sendStatus(401); //Unauthorized

  // evaluate password
  const match = await bcrypt.compare(pwd, foundUser.password);

  // Get rid of nulls with Boolean
  if (match) {
    const roles = Object.values(foundUser.roles).filter(Boolean);

    // create JWTs
    const accessToken = jwt.sign(
      {
        UserInfo: {
          username: foundUser.username,
          roles: roles,
        },
      },
      process.env.ACCESS_TOKEN_SECRET,
      { expiresIn: "10s" }
    );
    const refreshToken = jwt.sign(
      { username: foundUser.username },
      process.env.REFRESH_TOKEN_SECRET,
      { expiresIn: "1d" }
    );

    // Saving refreshToken with current user
    foundUser.refreshToken = refreshToken;
    const result = await foundUser.save();
    console.log(result);
    console.log(roles);

    // Creates Secure Cookie with refresh token
    res.cookie("jwt", refreshToken, {
      httpOnly: true,
      secure: false,
      sameSite: "None",
      maxAge: 24 * 60 * 60 * 1000,
    });

    // Send authorization roles and access token to user
    res.json({ roles, accessToken });
  } else {
    res.sendStatus(401);
  }
};

module.exports = { handleLogin };
```

# Currently Saved in MongoDB:

```bs
UN: dave1
PW: Aa$12345
[User: 2001]

UN: jane1
PW: Aa$12345
[User: 2001, Editor: 1984]

UN: walt1
PW: Aa$12345
[User: 2001, Editor: 1984, Admin: 5150]
```

<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3a33cbf8-fcf4-47e1-96c2-ac575f3abbb4">
<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3a267380-d0c5-4fb8-b3c1-233aa0f0e726">

# Login with james:  POST http://localhost:3500/auth 401 (Unauthorized)

```bs
UN: james
PW: password123
```

<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2bdfdf03-d8f3-4bfe-9ce4-216280a0dbe7">
<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/604b7e35-73c1-4ce9-a75f-851ac8ff5f99">

# Login with dave1: POST http://localhost:3500/auth 200 (Success)

```bs
UN: dave1
PW: Aa$12345
```

```bs
{"roles":[2001],"accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6ImRhdmUxIiwicm9sZXMiOlsyMDAxXX0sImlhdCI6MTY5MDQ4MjAwMSwiZXhwIjoxNjkwNDgyMDExfQ.pkY8hCdRQIw_3R5fEG6m2spY1aN3N7QElwkZec4qML0"}
```

<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5cb44753-e43e-4453-9c1b-9269be43430f">
<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1226b8a2-0ae6-46c7-aa71-f12f6c895fd5">

# Login with jane1: POST http://localhost:3500/auth 200 (Success)

```bs
UN: jane1
PW: Aa$12345
```

```bs
{"roles":[2001,1984],"accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6ImphbmUxIiwicm9sZXMiOlsyMDAxLDE5ODRdfSwiaWF0IjoxNjkwNDgyMjA3LCJleHAiOjE2OTA0ODIyMTd9.Rv5O5gQl1sUTSRQYfAGoBK4cvq2r6yx-9NAFzRw3TQo"}
```

<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/53b4c459-8cae-4b7c-9b88-dd9c76699790">
<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6658f795-c7f2-4400-a9da-42529dbd85b3">

# Login with walt1: POST http://localhost:3500/auth 200 (Success)

```bs
UN: walt1
PW: Aa$12345
```

```bs
{"roles":[2001,1984,5150],"accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJ1c2VybmFtZSI6IndhbHQxIiwicm9sZXMiOlsyMDAxLDE5ODQsNTE1MF19LCJpYXQiOjE2OTA0ODIzNTQsImV4cCI6MTY5MDQ4MjM2NH0.AIQnoFnCgIoTYkuTKZOUpfg3Zc2-BgliVE1oRjQeWps"}
```

<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ae019e88-4fe2-4b64-86a4-29681a037069">
<img width="1289" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/65cd954e-b3ce-48bc-9282-92f452d5e164">


# #End  </details>

<details>
  <summary>157. React Auth (Role-Based Authorization) - Setup Routes and Components</summary>

# Setup Routes and Components

<img width="1053" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8c0b63d7-9d04-4a45-8d87-5723b3f933b5">
<img width="1053" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bd7abcf4-75cc-4761-a926-04288c6f3a7e">
<img width="1053" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/30fc40c1-086f-47f8-97d5-67f3f5c8ff70">
<img width="1053" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2b9790f6-ac36-4d95-ac3c-b107ec58f3f2">
<img width="1053" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/08500541-dd77-4fb4-ac96-f49bdf777f1b">
<img width="1053" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c5a9ab56-c014-4ed6-88c8-2445e9d25619">
<img width="1053" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dbb191f8-2594-4eaf-884c-f629d9cee686">
<img width="1225" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5a47c094-6c4c-43a7-8e8e-216efb2cee46">
<img width="1225" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7e40d565-a5ab-4f55-972d-135dc5b4b02e">
<img width="1225" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a19a8369-1f46-4a06-83f2-1cc9044dc7dc">
<img width="1225" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/032f57cf-3802-400c-b5cf-c5cf62841919">
<img width="1225" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7bce3c75-9065-453f-9c2d-a7bd9a8b3b61">
<img width="1225" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5c3738a7-5e56-4a05-90ff-f5d128e5f93f">
<img width="1225" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0d403e21-abb2-4acb-83e1-36e952212089">

# Install react-router-dom@6:

```bs
npm i react-router-dom@6
yarn add react-router-dom@6
```

### x-dave-gray/react-auth/src/hooks/useAuth.js:

```js
import { useContext } from "react";
import AuthContext from "../context/AuthProvider";

const useAuth = () => {
  return useContext(AuthContext);
};

export default useAuth;
```

### x-dave-gray/react-auth/src/index.js:

```js
import React from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App";
import { AuthProvider } from "./context/AuthProvider";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const root = createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/*" element={<App />} />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
```

### x-dave-gray/react-auth/src/App.js:

```js
import Register from "./components/Register";
import Login from "./components/Login";
import Home from "./components/Home";
import Layout from "./components/Layout";
import Editor from "./components/Editor";
import Admin from "./components/Admin";
import Missing from "./components/Missing";
import Unauthorized from "./components/Unauthorized";
import Lounge from "./components/Lounge";
import LinkPage from "./components/LinkPage";
// import RequireAuth from "./components/RequireAuth";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        {/* public routes */}
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="linkpage" element={<LinkPage />} />
        <Route path="unauthorized" element={<Unauthorized />} />

        {/* we want to protect these routes */}
        <Route path="/" element={<Home />} />
        <Route path="editor" element={<Editor />} />
        <Route path="admin" element={<Admin />} />
        <Route path="lounge" element={<Lounge />} />

        {/* catch all */}
        <Route path="*" element={<Missing />} />
      </Route>
    </Routes>
  );
}

export default App;
```

### x-dave-gray/react-auth/src/components/Layout.js:

```js
import { Outlet } from "react-router-dom";

const Layout = () => {
  return (
    <main className="App">
      <Outlet />
    </main>
  );
};

export default Layout;
```

### x-dave-gray/react-auth/src/components/Login.js:

```js
import { useRef, useState, useEffect } from "react";
import useAuth from "../hooks/useAuth";
import { Link, useNavigate, useLocation } from "react-router-dom";

import axios from "../api/axios";
const LOGIN_URL = "/auth";

const Login = () => {
  const { setAuth } = useAuth();

  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from?.pathname || "/";

  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        LOGIN_URL,
        JSON.stringify({ user, pwd }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      console.log(JSON.stringify(response?.data));
      //console.log(JSON.stringify(response));
      const accessToken = response?.data?.accessToken;
      const roles = response?.data?.roles;
      setAuth({ user, pwd, roles, accessToken });
      setUser("");
      setPwd("");
      navigate(from, { replace: true });
    } catch (err) {
      if (!err?.response) {
        setErrMsg("No Server Response");
      } else if (err.response?.status === 400) {
        setErrMsg("Missing Username or Password");
      } else if (err.response?.status === 401) {
        setErrMsg("Unauthorized");
      } else {
        setErrMsg("Login Failed");
      }
      errRef.current.focus();
    }
  };

  return (
    <section>
      <p
        ref={errRef}
        className={errMsg ? "errmsg" : "offscreen"}
        aria-live="assertive"
      >
        {errMsg}
      </p>
      <h1>Sign In</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          ref={userRef}
          autoComplete="off"
          onChange={(e) => setUser(e.target.value)}
          value={user}
          required
        />

        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          onChange={(e) => setPwd(e.target.value)}
          value={pwd}
          required
        />
        <button>Sign In</button>
      </form>
      <p>
        Need an Account?
        <br />
        <span className="line">
          <Link to="/register">Sign Up</Link>
        </span>
      </p>
    </section>
  );
};

export default Login;
```

### x-dave-gray/react-auth/src/components/Register.js:

```js
import { useRef, useState, useEffect } from "react";
import {
  faCheck,
  faTimes,
  faInfoCircle,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import axios from "../api/axios";
import { Link } from "react-router-dom";

const USER_REGEX = /^[A-z][A-z0-9-_]{3,23}$/;
const PWD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;
const REGISTER_URL = "/register";

const Register = () => {
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [validName, setValidName] = useState(false);
  const [userFocus, setUserFocus] = useState(false);

  const [pwd, setPwd] = useState("");
  const [validPwd, setValidPwd] = useState(false);
  const [pwdFocus, setPwdFocus] = useState(false);

  const [matchPwd, setMatchPwd] = useState("");
  const [validMatch, setValidMatch] = useState(false);
  const [matchFocus, setMatchFocus] = useState(false);

  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    setValidName(USER_REGEX.test(user));
  }, [user]);

  useEffect(() => {
    setValidPwd(PWD_REGEX.test(pwd));
    setValidMatch(pwd === matchPwd);
  }, [pwd, matchPwd]);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd, matchPwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    // if button enabled with JS hack
    const v1 = USER_REGEX.test(user);
    const v2 = PWD_REGEX.test(pwd);
    if (!v1 || !v2) {
      setErrMsg("Invalid Entry");
      return;
    }
    try {
      const response = await axios.post(
        REGISTER_URL,
        JSON.stringify({ user, pwd }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      // TODO: remove console.logs before deployment
      console.log(JSON.stringify(response?.data));
      //console.log(JSON.stringify(response))
      setSuccess(true);
      //clear state and controlled inputs
      setUser("");
      setPwd("");
      setMatchPwd("");
    } catch (err) {
      if (!err?.response) {
        setErrMsg("No Server Response");
      } else if (err.response?.status === 409) {
        setErrMsg("Username Taken");
      } else {
        setErrMsg("Registration Failed");
      }
      errRef.current.focus();
    }
  };

  return (
    <>
      {success ? (
        <section>
          <h1>Success!</h1>
          <p>
            <a href="#">Sign In</a>
          </p>
        </section>
      ) : (
        <section>
          <p
            ref={errRef}
            className={errMsg ? "errmsg" : "offscreen"}
            aria-live="assertive"
          >
            {errMsg}
          </p>
          <h1>Register</h1>
          <form onSubmit={handleSubmit}>
            <label htmlFor="username">
              Username:
              <FontAwesomeIcon
                icon={faCheck}
                className={validName ? "valid" : "hide"}
              />
              <FontAwesomeIcon
                icon={faTimes}
                className={validName || !user ? "hide" : "invalid"}
              />
            </label>
            <input
              type="text"
              id="username"
              ref={userRef}
              autoComplete="off"
              onChange={(e) => setUser(e.target.value)}
              value={user}
              required
              aria-invalid={validName ? "false" : "true"}
              aria-describedby="uidnote"
              onFocus={() => setUserFocus(true)}
              onBlur={() => setUserFocus(false)}
            />
            <p
              id="uidnote"
              className={
                userFocus && user && !validName ? "instructions" : "offscreen"
              }
            >
              <FontAwesomeIcon icon={faInfoCircle} />
              4 to 24 characters.
              <br />
              Must begin with a letter.
              <br />
              Letters, numbers, underscores, hyphens allowed.
            </p>

            <label htmlFor="password">
              Password:
              <FontAwesomeIcon
                icon={faCheck}
                className={validPwd ? "valid" : "hide"}
              />
              <FontAwesomeIcon
                icon={faTimes}
                className={validPwd || !pwd ? "hide" : "invalid"}
              />
            </label>
            <input
              type="password"
              id="password"
              onChange={(e) => setPwd(e.target.value)}
              value={pwd}
              required
              aria-invalid={validPwd ? "false" : "true"}
              aria-describedby="pwdnote"
              onFocus={() => setPwdFocus(true)}
              onBlur={() => setPwdFocus(false)}
            />
            <p
              id="pwdnote"
              className={pwdFocus && !validPwd ? "instructions" : "offscreen"}
            >
              <FontAwesomeIcon icon={faInfoCircle} />
              8 to 24 characters.
              <br />
              Must include uppercase and lowercase letters, a number and a special
              character.
              <br />
              Allowed special characters: <span aria-label="exclamation mark">
                !
              </span> <span aria-label="at symbol">@</span> <span aria-label="hashtag">
                #
              </span> <span aria-label="dollar sign">$</span> <span aria-label="percent">%</span>
            </p>

            <label htmlFor="confirm_pwd">
              Confirm Password:
              <FontAwesomeIcon
                icon={faCheck}
                className={validMatch && matchPwd ? "valid" : "hide"}
              />
              <FontAwesomeIcon
                icon={faTimes}
                className={validMatch || !matchPwd ? "hide" : "invalid"}
              />
            </label>
            <input
              type="password"
              id="confirm_pwd"
              onChange={(e) => setMatchPwd(e.target.value)}
              value={matchPwd}
              required
              aria-invalid={validMatch ? "false" : "true"}
              aria-describedby="confirmnote"
              onFocus={() => setMatchFocus(true)}
              onBlur={() => setMatchFocus(false)}
            />
            <p
              id="confirmnote"
              className={
                matchFocus && !validMatch ? "instructions" : "offscreen"
              }
            >
              <FontAwesomeIcon icon={faInfoCircle} />
              Must match the first password input field.
            </p>

            <button
              disabled={!validName || !validPwd || !validMatch ? true : false}
            >
              Sign Up
            </button>
          </form>
          <p>
            Already registered?
            <br />
            <span className="line">
              <Link to="/">Sign In</Link>
            </span>
          </p>
        </section>
      )}
    </>
  );
};

export default Register;
```

### x-dave-gray/react-auth/src/components/LinkPage.js:

```js
import { Link } from "react-router-dom";

const LinkPage = () => {
  return (
    <section>
      <h1>Links</h1>
      <br />
      <h2>Public</h2>
      <Link to="/login">Login</Link>
      <Link to="/register">Register</Link>
      <br />
      <h2>Private</h2>
      <Link to="/">Home</Link>
      <Link to="/editor">Editors Page</Link>
      <Link to="/admin">Admin Page</Link>
    </section>
  );
};

export default LinkPage;
```

### x-dave-gray/react-auth/src/components/Unauthorized.js:

```js
import { useNavigate } from "react-router-dom";

const Unauthorized = () => {
  const navigate = useNavigate();

  const goBack = () => navigate(-1);

  return (
    <section>
      <h1>Unauthorized</h1>
      <br />
      <p>You do not have access to the requested page.</p>
      <div className="flexGrow">
        <button onClick={goBack}>Go Back</button>
      </div>
    </section>
  );
};

export default Unauthorized;
```

### x-dave-gray/react-auth/src/components/Home.js:

```js
import { useNavigate, Link } from "react-router-dom";
import { useContext } from "react";
import AuthContext from "../context/AuthProvider";

const Home = () => {
  const { setAuth } = useContext(AuthContext);
  const navigate = useNavigate();

  const logout = async () => {
    // if used in more components, this should be in context
    // axios to /logout endpoint
    setAuth({});
    navigate("/linkpage");
  };

  return (
    <section>
      <h1>Home</h1>
      <br />
      <p>You are logged in!</p>
      <br />
      <Link to="/editor">Go to the Editor page</Link>
      <br />
      <Link to="/admin">Go to the Admin page</Link>
      <br />
      <Link to="/lounge">Go to the Lounge</Link>
      <br />
      <Link to="/linkpage">Go to the link page</Link>
      <div className="flexGrow">
        <button onClick={logout}>Sign Out</button>
      </div>
    </section>
  );
};

export default Home;
```

### x-dave-gray/react-auth/src/components/Editor.js:

```js
import { Link } from "react-router-dom";

const Editor = () => {
  return (
    <section>
      <h1>Editors Page</h1>
      <br />
      <p>You must have been assigned an Editor role.</p>
      <div className="flexGrow">
        <Link to="/">Home</Link>
      </div>
    </section>
  );
};

export default Editor;
```

### x-dave-gray/react-auth/src/components/Admin.js:

```js
import { Link } from "react-router-dom";

const Admin = () => {
  return (
    <section>
      <h1>Admins Page</h1>
      <br />
      <p>You must have been assigned an Admin role.</p>
      <div className="flexGrow">
        <Link to="/">Home</Link>
      </div>
    </section>
  );
};

export default Admin;
```

### x-dave-gray/react-auth/src/components/Lounge.js:

```js
import { Link } from "react-router-dom";

const Lounge = () => {
  return (
    <section>
      <h1>The Lounge</h1>
      <br />
      <p>Admins and Editors can hang out here.</p>
      <div className="flexGrow">
        <Link to="/">Home</Link>
      </div>
    </section>
  );
};

export default Lounge;
```

### x-dave-gray/react-auth/src/components/Missing.js:

```js
import { Link } from "react-router-dom";

const Missing = () => {
  return (
    <article style={{ padding: "100px" }}>
      <h1>Oops!</h1>
      <p>Page Not Found</p>
      <div className="flexGrow">
        <Link to="/">Visit Our Homepage</Link>
      </div>
    </article>
  );
};

export default Missing;
```

# #End  </details>

<details>
  <summary>158. React Auth (Role-Based Authorization) - Require Auth Component 1 </summary>

# Require Auth Component 1

<img width="1052" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5b42a761-0c25-4a7f-8d07-be583f58d5b1">
<img width="1052" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ea67c9bc-7253-431d-bf00-d5234f5cacbb">
<img width="1052" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4fa73edd-7e9b-4230-a64e-fbd4548ffe0c">
<img width="1052" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e39f7dfe-a9f2-479e-9ddd-ce53a22c91f0">
<img width="1052" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/194229f7-55ba-425a-835d-fec71027e4b6">

### x-dave-gray/react-auth/src/hooks/useAuth.js:

```js
import { useContext } from "react";
import AuthContext from "../context/AuthProvider";

const useAuth = () => {
  return useContext(AuthContext);
};

export default useAuth;
```

### x-dave-gray/react-auth/src/components/RequireAuth.js:

```js
import { useLocation, Navigate, Outlet } from "react-router-dom";
import useAuth from "../hooks/useAuth";

const RequireAuth = () => {
  const { auth } = useAuth();
  const location = useLocation();

  return auth?.user ? (
    <Outlet />
  ) : (
    <Navigate to="/login" state={{ from: location }} replace />
  );
};

export default RequireAuth;
```

### x-dave-gray/react-auth/src/index.js:

```js
import React from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App";
import { AuthProvider } from "./context/AuthProvider";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const root = createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/*" element={<App />} />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
```

### x-dave-gray/react-auth/src/App.js:

```js
import Register from "./components/Register";
import Login from "./components/Login";
import Home from "./components/Home";
import Layout from "./components/Layout";
import Editor from "./components/Editor";
import Admin from "./components/Admin";
import Missing from "./components/Missing";
import Unauthorized from "./components/Unauthorized";
import Lounge from "./components/Lounge";
import LinkPage from "./components/LinkPage";
import RequireAuth from "./components/RequireAuth";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        {/* public routes */}
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="linkpage" element={<LinkPage />} />
        <Route path="unauthorized" element={<Unauthorized />} />

        {/* we want to protect these routes */}
        <Route element={<RequireAuth />}>
          <Route path="/" element={<Home />} />
          <Route path="editor" element={<Editor />} />
          <Route path="admin" element={<Admin />} />
          <Route path="lounge" element={<Lounge />} />
        </Route>

        {/* catch all */}
        <Route path="*" element={<Missing />} />
      </Route>
    </Routes>
  );
}

export default App;
```

### x-dave-gray/react-auth/src/components/Login.js:

```js
import { useRef, useState, useEffect } from "react";
import useAuth from "../hooks/useAuth";
import { Link, useNavigate, useLocation } from "react-router-dom";

import axios from "../api/axios";
const LOGIN_URL = "/auth";

const Login = () => {
  const { setAuth } = useAuth();

  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from?.pathname || "/";

  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        LOGIN_URL,
        JSON.stringify({ user, pwd }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      console.log(JSON.stringify(response?.data));
      //console.log(JSON.stringify(response));
      const accessToken = response?.data?.accessToken;
      const roles = response?.data?.roles;
      setAuth({ user, pwd, roles, accessToken });
      setUser("");
      setPwd("");
      navigate(from, { replace: true });
    } catch (err) {
      if (!err?.response) {
        setErrMsg("No Server Response");
      } else if (err.response?.status === 400) {
        setErrMsg("Missing Username or Password");
      } else if (err.response?.status === 401) {
        setErrMsg("Unauthorized");
      } else {
        setErrMsg("Login Failed");
      }
      errRef.current.focus();
    }
  };

  return (
    <section>
      <p
        ref={errRef}
        className={errMsg ? "errmsg" : "offscreen"}
        aria-live="assertive"
      >
        {errMsg}
      </p>
      <h1>Sign In</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          ref={userRef}
          autoComplete="off"
          onChange={(e) => setUser(e.target.value)}
          value={user}
          required
        />

        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          onChange={(e) => setPwd(e.target.value)}
          value={pwd}
          required
        />
        <button>Sign In</button>
      </form>
      <p>
        Need an Account?
        <br />
        <span className="line">
          <Link to="/register">Sign Up</Link>
        </span>
      </p>
    </section>
  );
};

export default Login;
```

# #End  </details>

<details>
  <summary>159. React Auth (Role-Based Authorization) - Require Auth Component 2 with Route Auth </summary>

# Require Auth Component 2 with Route Auth

<img width="1052" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/843c5472-6a87-4ec8-ae27-37bdbbe7064c">
<img width="1052" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a2d5a315-6f76-4dfe-8f84-853799c33b6b">
<img width="1052" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/abbb2025-f04c-44c0-aa03-436fcf129606">
<img width="1052" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e093c74f-64b2-4add-9914-70f1c62794f1">
<img width="1052" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bac2a16f-0380-41cf-b264-2bb84a00d4d5">

### x-dave-gray/react-auth/src/components/RequireAuth.js:

```js
import { useLocation, Navigate, Outlet } from "react-router-dom";
import useAuth from "../hooks/useAuth";

const RequireAuth = ({ allowedRoles }) => {
  const { auth } = useAuth();
  const location = useLocation();

  return auth?.roles?.find((role) => allowedRoles?.includes(role)) ? (
    <Outlet />
  ) : auth?.user ? (
    <Navigate to="/unauthorized" state={{ from: location }} replace />
  ) : (
    <Navigate to="/login" state={{ from: location }} replace />
  );
};

export default RequireAuth;
```

### x-dave-gray/react-auth/src/index.js:

```js
import React from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App";
import { AuthProvider } from "./context/AuthProvider";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const root = createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/*" element={<App />} />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
```

### x-dave-gray/react-auth/src/App.js:

```js
import Register from "./components/Register";
import Login from "./components/Login";
import Home from "./components/Home";
import Layout from "./components/Layout";
import Editor from "./components/Editor";
import Admin from "./components/Admin";
import Missing from "./components/Missing";
import Unauthorized from "./components/Unauthorized";
import Lounge from "./components/Lounge";
import LinkPage from "./components/LinkPage";
import RequireAuth from "./components/RequireAuth";
import { Routes, Route } from "react-router-dom";

const ROLES = {
  User: 2001,
  Editor: 1984,
  Admin: 5150,
};

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        {/* public routes */}
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="linkpage" element={<LinkPage />} />
        <Route path="unauthorized" element={<Unauthorized />} />

        {/* we want to protect these routes */}
        <Route element={<RequireAuth allowedRoles={[ROLES.User]} />}>
          <Route path="/" element={<Home />} />
        </Route>

        <Route element={<RequireAuth allowedRoles={[ROLES.Editor]} />}>
          <Route path="editor" element={<Editor />} />
        </Route>

        <Route element={<RequireAuth allowedRoles={[ROLES.Admin]} />}>
          <Route path="admin" element={<Admin />} />
        </Route>

        <Route
          element={<RequireAuth allowedRoles={[ROLES.Editor, ROLES.Admin]} />}
        >
          <Route path="lounge" element={<Lounge />} />
        </Route>

        {/* catch all */}
        <Route path="*" element={<Missing />} />
      </Route>
    </Routes>
  );
}

export default App;
```

### x-dave-gray/react-auth/src/components/Login.js:

```js
import { useRef, useState, useEffect } from "react";
import useAuth from "../hooks/useAuth";
import { Link, useNavigate, useLocation } from "react-router-dom";

import axios from "../api/axios";
const LOGIN_URL = "/auth";

const Login = () => {
  const { setAuth } = useAuth();

  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from?.pathname || "/";

  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        LOGIN_URL,
        JSON.stringify({ user, pwd }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      console.log(JSON.stringify(response?.data));
      //console.log(JSON.stringify(response));
      const accessToken = response?.data?.accessToken;
      const roles = response?.data?.roles;
      setAuth({ user, pwd, roles, accessToken });
      setUser("");
      setPwd("");
      navigate(from, { replace: true });
    } catch (err) {
      if (!err?.response) {
        setErrMsg("No Server Response");
      } else if (err.response?.status === 400) {
        setErrMsg("Missing Username or Password");
      } else if (err.response?.status === 401) {
        setErrMsg("Unauthorized");
      } else {
        setErrMsg("Login Failed");
      }
      errRef.current.focus();
    }
  };

  return (
    <section>
      <p
        ref={errRef}
        className={errMsg ? "errmsg" : "offscreen"}
        aria-live="assertive"
      >
        {errMsg}
      </p>
      <h1>Sign In</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          ref={userRef}
          autoComplete="off"
          onChange={(e) => setUser(e.target.value)}
          value={user}
          required
        />

        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          onChange={(e) => setPwd(e.target.value)}
          value={pwd}
          required
        />
        <button>Sign In</button>
      </form>
      <p>
        Need an Account?
        <br />
        <span className="line">
          <Link to="/register">Sign Up</Link>
        </span>
      </p>
    </section>
  );
};

export default Login;
```

### x-dave-gray/react-auth/src/components/Unauthorized.js:

```js
import { useNavigate } from "react-router-dom";

const Unauthorized = () => {
  const navigate = useNavigate();

  const goBack = () => navigate(-1);

  return (
    <section>
      <h1>Unauthorized</h1>
      <br />
      <p>You do not have access to the requested page.</p>
      <div className="flexGrow">
        <button onClick={goBack}>Go Back</button>
      </div>
    </section>
  );
};

export default Unauthorized;
```

# #End  </details>

<details>
  <summary>160. React Auth (Role-Based Authorization) - Testing Protected Routes </summary>

# Testing Protected Routes

# Users in MongoDB

```bs
UN: dave1
PW: Aa$12345
ROLE: 2001 (User)

UN: jane1
PW: Aa$12345
ROLE: 2001 (User), 1984 (Editor)

UN: walt1
PW: Aa$12345
ROLE: 2001 (User), 1984 (Editor), 5150 (Admin)
```

# Login with mike: Unauthorized to all! Cannot Access any Routes!

```bs
UN: mike
PW: Aa$12345
ROLE: None
```

<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a67d038b-e60c-4c8d-b2b7-bf85babd3708">

# Login with dave1: Unauthorized access to Editor, Admin and Lounge Pages! Can only Access Home Route.

```bs
UN: dave1
PW: Aa$12345
ROLE: 2001 (User)
```

<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4a7d4003-410e-4bdd-9faf-2315f5db7693">
<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bcd0c297-1a53-4b11-b258-f494bf800ba9">

# Login with jane1: Unauthorized access to Admin Route! Can Access Home, Editor and Lounge Routes.

```bs
UN: jane1
PW: Aa$12345
ROLE: 2001 (User), 1984 (Editor)
```

<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bb48ff92-dfcd-4a25-80b1-98a7d65aca0b">
<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/32a344c2-d8f1-4907-aaff-8ef037e681d8">
<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/66777b6a-3de9-463b-8745-f2288a46005c">
<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c304df01-60b0-4c51-affb-423595cfc964">

# Login with walt1: Can Access all routes - Home, Editor, Lounge and Admin Routes!

```bs
UN: walt1
PW: Aa$12345
ROLE: 2001 (User), 1984 (Editor), 5150 (Admin)
```

<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d0634bb4-f9fd-40ca-bd15-2cc27ef15024">
<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/44eee0f8-5ba9-4ec7-b281-a4fdef77baf0">
<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/35f324b1-fd65-43d2-8a41-5d3e6062e2bd">
<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c8ebd30b-a38f-4727-8e36-a09d1cb3c576">

# #End  </details>

<details>
  <summary>161. React Auth - Authentication with JWT Access, Refresh Tokens, Cookies and Axios</summary>

```bs
npm update
```

components/Users.js:

```js
import { useState, useEffect, useRef } from "react";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import { useNavigate, useLocation } from "react-router-dom";

const Users = () => {
  const [users, setUsers] = useState();
  const axiosPrivate = useAxiosPrivate();
  const navigate = useNavigate();
  const location = useLocation();
  const effectRun = useRef(false);

  useEffect(() => {
    let isMounted = true;
    const controller = new AbortController();

    const getUsers = async () => {
      try {
        const response = await axiosPrivate.get("/users", {
          signal: controller.signal,
        });
        console.log(response.data);
        isMounted && setUsers(response.data);
      } catch (err) {
        console.error(err);
        navigate("/login", { state: { from: location }, replace: true });
      }
    };

    // Check if useEffect has run the first time
    if (effectRun.current) {
      getUsers();
    }

    return () => {
      isMounted = false;
      controller.abort();
      effectRun.current = true; // update the value of effectRun to true
    };
  }, []);

  return (
    <article>
      <h2>Users List</h2>
      {users?.length ? (
        <ul>
          {users.map((user, i) => (
            <li key={i}>{user?.username}</li>
          ))}
        </ul>
      ) : (
        <p>No users to display</p>
      )}
    </article>
  );
};

export default Users;
```

component/Admin.js:

```js
import { Link } from "react-router-dom";
import Users from "./Users";

const Admin = () => {
  return (
    <section>
      <h1>Admins Page</h1>
      <br />
      <Users />
      <br />
      <div className="flexGrow">
        <Link to="/">Home</Link>
      </div>
    </section>
  );
};

export default Admin;
```

hooks/useRefreshToken.js:

```js
import axios from "../api/axios";
import useAuth from "./useAuth";

const useRefreshToken = () => {
  const { setAuth } = useAuth();

  const refresh = async () => {
    const response = await axios.get("/refresh", {
      withCredentials: true,
    });
    setAuth((prev) => {
      console.log(JSON.stringify(prev));
      console.log(response.data.accessToken);
      return { ...prev, accessToken: response.data.accessToken };
    });
    return response.data.accessToken;
  };
  return refresh;
};

export default useRefreshToken;
```

api/axios.js:

```js
import axios from "axios";
const BASE_URL = "http://localhost:3500";

export default axios.create({
  baseURL: BASE_URL,
});

export const axiosPrivate = axios.create({
  baseURL: BASE_URL,
  headers: { "Content-Type": "application/json" },
  withCredentials: true,
});
```

hooks/useAxiosPrivate.js:

```js
import { axiosPrivate } from "../api/axios";
import { useEffect } from "react";
import useRefreshToken from "./useRefreshToken";
import useAuth from "./useAuth";

const useAxiosPrivate = () => {
  const refresh = useRefreshToken();
  const { auth } = useAuth();

  useEffect(() => {
    const requestIntercept = axiosPrivate.interceptors.request.use(
      (config) => {
        if (!config.headers["Authorization"]) {
          config.headers["Authorization"] = `Bearer ${auth?.accessToken}`;
        }
        return config;
      },
      (error) => Promise.reject(error)
    );

    const responseIntercept = axiosPrivate.interceptors.response.use(
      (response) => response,
      async (error) => {
        const prevRequest = error?.config;
        if (error?.response?.status === 403 && !prevRequest?.sent) {
          prevRequest.sent = true;
          const newAccessToken = await refresh();
          prevRequest.headers["Authorization"] = `Bearer ${newAccessToken}`;
          return axiosPrivate(prevRequest);
        }
        return Promise.reject(error);
      }
    );

    return () => {
      axiosPrivate.interceptors.request.eject(requestIntercept);
      axiosPrivate.interceptors.response.eject(responseIntercept);
    };
  }, [auth, refresh]);

  return axiosPrivate;
};

export default useAxiosPrivate;
```

hooks/useAuth.js:

```js
import { useContext, useDebugValue } from "react";
import AuthContext from "../context/AuthProvider";

const useAuth = () => {
  const { auth } = useContext(AuthContext);
  useDebugValue(auth, (auth) => (auth?.user ? "Logged In" : "Logged Out"));
  return useContext(AuthContext);
};

export default useAuth;
```

# #End  </details>

<details>
  <summary>162. React Auth - Persistent User Login Authentication with JWT Tokens</summary>

components/PersistLogin.js:

```js
import { Outlet } from "react-router-dom";
import { useState, useEffect } from "react";
import useRefreshToken from "../hooks/useRefreshToken";
import useAuth from "../hooks/useAuth";

const PersistLogin = () => {
  const [isLoading, setIsLoading] = useState(true);
  const refresh = useRefreshToken();
  const { auth, persist } = useAuth();

  useEffect(() => {
    let isMounted = true;

    const verifyRefreshToken = async () => {
      try {
        await refresh();
      } catch (err) {
        console.error(err);
      } finally {
        isMounted && setIsLoading(false);
      }
    };

    // Avoids unwanted call to verifyRefreshToken
    !auth?.accessToken && persist ? verifyRefreshToken() : setIsLoading(false);

    return () => (isMounted = false);
  }, []);

  useEffect(() => {
    console.log(`isLoading: ${isLoading}`);
    console.log(`aT: ${JSON.stringify(auth?.accessToken)}`);
  }, [isLoading, auth]);

  return (
    <>{!persist ? <Outlet /> : isLoading ? <p>Loading...</p> : <Outlet />}</>
  );
};

export default PersistLogin;
```

hooks/useRefreshToken.js:

```js
import axios from "../api/axios";
import useAuth from "./useAuth";

const useRefreshToken = () => {
  const { setAuth } = useAuth();

  const refresh = async () => {
    const response = await axios.get("/refresh", {
      withCredentials: true,
    });
    setAuth((prev) => {
      console.log(JSON.stringify(prev));
      console.log(response.data.accessToken);
      return {
        ...prev,
        roles: response.data.roles,
        accessToken: response.data.accessToken,
      };
    });
    return response.data.accessToken;
  };
  return refresh;
};

export default useRefreshToken;
```

App.js:

```js
import Register from "./components/Register";
import Login from "./components/Login";
import Home from "./components/Home";
import Layout from "./components/Layout";
import Editor from "./components/Editor";
import Admin from "./components/Admin";
import Missing from "./components/Missing";
import Unauthorized from "./components/Unauthorized";
import Lounge from "./components/Lounge";
import LinkPage from "./components/LinkPage";
import RequireAuth from "./components/RequireAuth";
import PersistLogin from "./components/PersistLogin";
import { Routes, Route } from "react-router-dom";

const ROLES = {
  User: 2001,
  Editor: 1984,
  Admin: 5150,
};

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        {/* public routes */}
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="linkpage" element={<LinkPage />} />
        <Route path="unauthorized" element={<Unauthorized />} />

        {/* we want to protect these routes */}
        <Route element={<PersistLogin />}>
          <Route element={<RequireAuth allowedRoles={[ROLES.User]} />}>
            <Route path="/" element={<Home />} />
          </Route>

          <Route element={<RequireAuth allowedRoles={[ROLES.Editor]} />}>
            <Route path="editor" element={<Editor />} />
          </Route>

          <Route element={<RequireAuth allowedRoles={[ROLES.Admin]} />}>
            <Route path="admin" element={<Admin />} />
          </Route>

          <Route
            element={<RequireAuth allowedRoles={[ROLES.Editor, ROLES.Admin]} />}
          >
            <Route path="lounge" element={<Lounge />} />
          </Route>
        </Route>

        {/* catch all */}
        <Route path="*" element={<Missing />} />
      </Route>
    </Routes>
  );
}

export default App;
```

# #End  </details>

<details>
  <summary>163. sample</summary>

```bs

```

```js

```

```js

```

```js

```

```js

```

# #End  </details>

