# REACTJS TUTORIAL FOR BEGINNERS

## [COURSES](https://www.youtube.com/playlist?list=PLC3y8-rFHvwgg3vaYJgHGnModB54rxOk3)

# REACTJS

+INTRODUCTION

<details>
  <summary>1. Introduction </summary>

# Introduction

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/2e0b3796-4cb3-41ee-b8c3-ab865d94aeb5)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/3a91495e-3224-4348-942f-cf8ac1b45218)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/0dd3e53e-23d6-4744-8d15-1d734441142c)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/75e8e385-04a6-43e9-92ec-648b1982d67d)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/c02f5ae6-98b1-4543-9712-ee6064738926)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/c6093d2a-e7f2-498f-b160-4912041b92ad)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/d7061f93-db7c-40a4-8416-228a4b6f50ff)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/cdb3ca21-56bd-48ba-9a66-1f3b76bcc1c3)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/fd14c0ac-80d7-43b7-ac81-5d6376379bfb)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/4a85c1ce-a870-41d9-a73e-1e29c39facb5)
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5f8d46ca-0ab7-493e-aff7-63e2ede8fccb">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b5d5d8b5-8e8a-43ca-9f35-c023c7cdf022">
<img width="1218" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/64d8998b-38c5-4a8f-9568-6bac904516f5">

# Create React App

```jsbs
npx create-react-app hello-world
yarn create react-app hello-world

cd hello-world

npm start
yarn start
```

### NXT/hello-world/src/index.js:

```js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
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

### NXT/hello-world/src/App.js:

```js
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Hello World!</h1>
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
  <summary>2. Functional Components </summary>

# Functional Components

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/acd8aec6-368a-45da-91b5-e14ce571358e)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/1b339541-dcd9-4ed0-ade2-8edf168b30b1)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/54be2ae7-cf62-4000-b857-5d8fceac9331)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/6a5811e8-1dce-437f-a409-354487f46c38)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/41a4ce18-483a-426d-beea-9d5232c667aa)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/7a043526-789d-466c-82ed-dfb35978a810)
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/086d7ce9-4043-4a2e-9c9b-798f021ff65a">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3e569aa6-ad96-431b-b721-ae36bb1efc2a">
<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/43f3108c-480a-43d8-b5f8-fe83a6b5156d">
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/ba749ea0-1533-4a32-acd7-aad60bfd8ad5)

### NXT/hello-world/src/App.js:

```js
import logo from "./logo.svg";
import "./App.css";
import Greet from "./components/Greet";

function App() {
  return (
    <div className="App">
      <Greet />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/Greet.jsx:

```js
import React from "react";

const Greet = () => {
  return <h1>Hello Ifeanyi!</h1>;
};

export default Greet;

// export default function Greet() {
//   return (
//     <div>
//       <h1>Hello Ifeanyi!</h1>
//     </div>
//   )
// }
```

</details>

<details>
  <summary>3. Class Components </summary>

# Class Components

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/04df1003-0c5d-4879-9cf2-5f03fa8cbc99)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/dffd4362-87a3-4076-b5b6-1109531f261d)
<img width="971" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a4a7a9df-daa7-4b04-8798-68a3a25e4786">
<img width="971" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5f38f8b0-ee7e-4285-bc73-61a9d7b9b276">
<img width="1230" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dcadd2bf-857d-437e-b585-7f36384328f1">
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/aa7ea6d9-f4a5-4ef0-abe8-8ae55cd79ae4)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/6a18f984-8155-4759-a63f-3b6aff3060e3)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Greet from "./components/Greet";
import Welcome from "./components/Welcome";

function App() {
  return (
    <div className="App">
      <Greet />
      <Welcome />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/Welcome.jsx:

```js
import React, { Component } from "react";

class Welcome extends Component {
  render() {
    return <h2>Welcome to Class Component</h2>;
  }
}

export default Welcome;
```

</details>

<details>
  <summary>4. JSX </summary>

# JSX

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/97309b0b-4837-423b-bd29-f7b05fbb6999)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/6cf8423b-aff6-40e9-9fb4-35d1af42bc53)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/e7793a10-925d-452a-b33b-8ff36c5ea2b9)
<img width="1294" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8d6e8b8c-fd46-45fb-97bb-061123f6acee">
<img width="1294" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/01a831cd-5c6b-4d1c-8a39-3c2d811e2f59">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Greet from "./components/Greet";
import Welcome from "./components/Welcome";
import HelloWithJSX from "./components/HelloWithJSX";
import HelloWithoutJSX from "./components/HelloWithoutJSX";

function App() {
  return (
    <div className="App">
      <HelloWithJSX />
      <HelloWithoutJSX />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/HelloWithJSX.js:

```js
import React from "react";

const HelloWithJSX = () => {
  return (
    <div>
      <h1>Hello With JSX</h1>
    </div>
  );
};

export default HelloWithJSX;
```

### NXT/hello-world/src/components/HelloWithoutJSX.js:

```js
import React from "react";

const HelloWithoutJSX = () => {
  //   return (
  //     <div>
  //       <h2 id="content" className="content-class">Hello Without JSX!</h2>
  //     </div>
  //   );

  const h2Node = React.createElement(
    "h2",
    { id: "content", className: "content-class" },
    "Hello Without JSX!"
  );

  const divNode = React.createElement("div", null, h2Node);

  return divNode;
};

export default HelloWithoutJSX;
```

</details>

<details>
  <summary>5. Props with Functional Components </summary>

# Props with Functional Components

<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8b17cf75-dd7e-43da-8a1a-585a897bde35">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/55174ba5-ff3d-4013-a891-6b880c2e8bab">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/ad8ab623-60d3-447a-a682-f97e02dfc90a)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Greet from "./components/Greet";

function App() {
  return (
    <div className="App">
      <Greet name="Bruce" heroName="Batman">
        <button>View Batman</button>
      </Greet>
      <Greet name="Clark" heroName="Superman" />
      <Greet name="Diana" heroName="Wonder Woman" />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/Greet.jsx:

```js
import React from "react";

const Greet = (props) => {
  console.log(props);
  return (
    <>
      <h1>
        Hello {props.name} a.k.a {props.heroName} !
      </h1>
      {props.children}
    </>
  );
};

export default Greet;
```

</details>

<details>
  <summary>6. Props with Class Components </summary>

# Props with Class Components

<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1cdcba2c-1a7c-4fbf-a9b5-de718467751e">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/83227b98-825d-48a7-b3e1-d61d9bff1e8e">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/b0f4fe9e-4265-416a-9e11-b67c5427dfb1)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Greet from "./components/Greet";
import GreetClass from "./components/GreetClass";

function App() {
  return (
    <div className="App">
      <GreetClass name="Bruce" heroName="Batman">
        <button>View Batman</button>
      </GreetClass>
      <GreetClass name="Clark" heroName="Superman" />
      <GreetClass name="Diana" heroName="Wonder Woman" />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/GreetClass.jsx:

```js
import React, { Component } from "react";

class GreetClass extends Component {
  render() {
    return (
      <>
        <h1>
          Hello {this.props.name} a.k.a {this.props.heroName} !
        </h1>
        {this.props.children}
      </>
    );
  }
}

export default GreetClass;
```

</details>

<details>
  <summary>7. State Hook </summary>

# State Hook

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/dd3f0cf8-df74-4062-91c5-e3b71bee0191)
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/400a9d2f-36bf-45cc-8035-8a656c3a699a">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0234b344-0819-4033-b513-a30c572dd45e">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/a736e784-8849-408a-8495-efb79599cc43)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/6a08205e-1064-403b-b346-61b7905b5a49)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Message from "./components/Message";

function App() {
  return (
    <div className="App">
      <Message />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/Message.js:

```js
import React, { Component } from "react";

class Message extends Component {
  constructor() {
    super();
    this.state = {
      message: "Welcome Visitor!",
    };
  }

  changeMessage() {
    this.setState({ message: "Thank you for subscribing!" });
  }

  render() {
    return (
      <>
        <h1>Hello, {this.state.message}</h1>
        <button onClick={() => this.changeMessage()}>Subscribe</button>
      </>
    );
  }
}

export default Message;
```

</details>

<details>
  <summary>8. SetState Function </summary>

# setState Function

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/a961c3f5-375b-4307-8d03-4155431e0ba4)
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/af2f5957-ccae-41fb-af9d-cca40b2f7299">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d456377e-a6e8-4e9c-9df7-5913f30a3c8f">
<img width="1291" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/274be041-9990-4c39-af40-713520d0c790">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Counter from "./components/Counter";

function App() {
  return (
    <div className="App">
      <Counter />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/Counter.js:

```js
import React, { Component } from "react";
class Counter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
    };
  }

  increment() {
    this.setState(
      (prev, props) => {
        return { count: prev.count + 1 };
      },
      () => {
        console.log("Callback Value: ", this.state.count);
      }
    );
    console.log("Output: ", this.state.count);
  }

  render() {
    return (
      <div>
        <h1>count: {this.state.count}</h1>
        <button onClick={() => this.increment()}>Increment</button>
      </div>
    );
  }
}

export default Counter;
```

</details>

<details>
  <summary>9. Destructuring Props and State </summary>

# Destructuring Props and State

<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b50880af-4148-4399-9bf9-f58f59898640">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/527bea48-082e-4e5c-9e1c-d791756f851e">
<img width="968" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1178b366-9807-441e-bcfd-86146c4161aa">
<img width="1294" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/06ff8b05-4929-46e1-83e1-c15470086391">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Greet from "./components/Greet";
import GreetClass from "./components/GreetClass";

function App() {
  return (
    <div className="App">
      <Greet name="Parker" heroName="Spiderman" />
      <Greet name="Bruce" heroName="Batman">
        <button>Find Out More about Batman...</button>
      </Greet>
      <GreetClass name="Clark" heroName="Superman" />
      <GreetClass name="Diana" heroName="Wonder Woman">
        <button>Find Out More about Wonder Woman...</button>
      </GreetClass>
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/Greet.jsx:

```js
import React from "react";

const Greet = (props) => {
  const { name, heroName } = props;
  return (
    <>
      <h1>
        Hello {name} a.k.a {heroName} !
      </h1>
      {props.children}
    </>
  );
};

export default Greet;
```

### NXT/hello-world/src/components/GreetClass.jsx:

```js
import React, { Component } from "react";

class GreetClass extends Component {
  render() {
    const { name, heroName, children } = this.props;
    // const { state1, state2 } = this.state;

    return (
      <>
        <h1>
          Hello {name} a.k.a {heroName} !
        </h1>
        {children}
      </>
    );
  }
}

export default GreetClass;
```

</details>

<details>
  <summary>10. Event Handling </summary>

# Event Handling

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bc92715a-e662-46cf-81f4-3bda8b52d291">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ec263a97-a24f-45a2-b0a8-796cbd2214b3">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b0ec0472-81f3-44d1-927a-5aa4950d4067">
<img width="1291" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8a8a7eb3-d202-4267-97b7-661b213606b7">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Event from "./components/Event";
import EventClass from "./components/EventClass";

function App() {
  return (
    <div className="App">
      <Event />
      <EventClass />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/Event.jsx:

```js
import React from "react";

const Event = () => {
  const clickHandler = () => {
    console.log("Event Button Clicked");
  };

  return (
    <div>
      <button onClick={clickHandler}>Click</button>
    </div>
  );
};

export default Event;
```

### NXT/hello-world/src/components/EventClass.jsx:

```js
import React, { Component } from "react";

export class EventClass extends Component {
  clickHandler() {
    console.log("EventClass Button Clicked");
  }

  render() {
    return (
      <div>
        <button onClick={this.clickHandler}>Click Me</button>
      </div>
    );
  }
}

export default EventClass;
```

</details>

<details>
  <summary>11. Binding Event Handlers </summary>

# Binding Event Handlers

<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/07882793-5865-4e6c-9c39-2510155a853e">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/9be2717a-1f9a-49f1-8b49-f62af9cb804f)

<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5eb8eb53-6179-4dbd-954b-ec216c80896d">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import EventBind from "./components/EventBind";

function App() {
  return (
    <div className="App">
      <EventBind />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/EventBind.jsx:

```js
import React, { Component } from "react";

class EventBind extends Component {
  constructor(props) {
    super(props);

    this.state = { message: "Hello" };
    this.clickHandler = this.clickHandler.bind(this);
  }

  clickHandler = () => {
    this.setState({ message: "Goodbye!" });
  };

  render() {
    return (
      <div>
        <div>{this.state.message}</div>
        <button onClick={this.clickHandler}>Click</button>
      </div>
    );
  }
}

export default EventBind;
```

</details>

<details>
  <summary>12. Methods as Props </summary>

# Methods as Props

<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/12e74ac4-35d7-49da-bad4-21cd4a0e895d">
<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/40a97d07-797b-41d7-93f8-a62eee9afc13">
<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9dd49658-10af-40de-8c56-364e02489bb4">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/410795fd-2115-465c-b972-3de83b92db4b)

<img width="1294" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ebc8cb05-2983-437d-9f76-7ac37dc91741">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import ParentComponent from "./components/ParentComponent";

function App() {
  return (
    <div className="App">
      <ParentComponent />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/ParentComponent.jsx:

```js
import React, { Component } from "react";
import ChildComponent from "./ChildComponent";

class ParentComponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      parentName: "Parent",
    };

    this.greetParent = this.greetParent.bind(this);
  }

  greetParent = (childName) => {
    alert(`Hello, ${this.state.parentName} from ${childName}.`);
  };

  render() {
    return (
      <div>
        <h1>Hi</h1>
        <ChildComponent greetHandler={this.greetParent} />
      </div>
    );
  }
}

export default ParentComponent;
```

### NXT/hello-world/src/components/ChildComponent.jsx:

```js
import React from "react";

export default function ChildComponent({ greetHandler }) {
  return (
    <div>
      <button onClick={() => greetHandler("First Child")}>Greet Parent</button>
    </div>
  );
}
```

</details>

<details>
  <summary>13. Conditional Rendering </summary>

# Conditional Rendering

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/54852c25-f385-488a-9eaa-0df053895a22)
<img width="971" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f3d31dca-2a7f-41fd-8c32-0ceccc26649e">
<img width="971" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f88ec3d1-d8d7-4b73-95c8-1293adfa3be2">
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/9209c081-8ec1-4dbc-8c2d-5255b733857e)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/1de53b24-6f2a-4f9b-a3b6-912bbc96f2ce)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import UserGreeting from "./components/UserGreeting";

function App() {
  return (
    <div className="App">
      <UserGreeting />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/UserGreeting.jsx:

```js
import React, { Component } from "react";

class UserGreeting extends Component {
  constructor(props) {
    super(props);

    this.state = { isLoggedIn: false };
  }

  toggleSwitch = () => {
    return this.setState((prev) => {
      return {
        isLoggedIn: !prev.isLoggedIn,
      };
    });
  };

  render() {
    return (
      <div>
        <h1>Welcome, {this.state.isLoggedIn ? "User1!" : "Guest!"}</h1>
        <button onClick={this.toggleSwitch}>
          {this.state.isLoggedIn ? "Logout" : "Login"}
        </button>
      </div>
    );
  }
}

export default UserGreeting;
```

</details>

<details>
  <summary>14. List Rendering </summary>

# List Rendering

<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/89b7f9c0-b1f5-4bf0-a61b-98b71dadd754">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/725775a1-3000-49a4-9a2e-d250beb3f03b">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/37a578d6-6775-4799-a545-6c244fabd4a5">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/c58fba98-8813-473d-8f1b-762995c2b003)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import NameList from "./components/NameList";

function App() {
  return (
    <div className="App">
      <NameList />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/NameList.jsx:

```js
import React from "react";
import Person from "./Person";

const NameList = () => {
  const names = ["Bruce", "Clark", "Diana"];
  const persons = [
    {
      id: 1,
      name: "Bruce",
      age: 30,
      skill: "React",
    },
    {
      id: 2,
      name: "Clark",
      age: 25,
      skill: "Angular",
    },
    {
      id: 3,
      name: "Diana",
      age: 28,
      skill: "Vue",
    },
  ];

  const nameList = names.map((name, index) => (
    <h2 key={index}>
      {index}-{name}
    </h2>
  ));
  const personList = persons.map((person) => (
    <Person key={person.id} person={person} />
  ));

  return (
    <div>
      {nameList}
      {personList}
    </div>
  );
};

export default NameList;
```

### NXT/hello-world/src/components/Person.jsx:

```js
import React from "react";

const Person = ({ person }) => {
  const { name, age, skill } = person;

  return (
    <div>
      <h2>
        I am {name}. I am {age} years old. I know {skill}.
      </h2>
    </div>
  );
};

export default Person;
```

</details>

<details>
  <summary>15. Styling and CSS Basics - CSS Stylesheets </summary>

# CSS Stylesheets

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/225a5f5e-287b-4fec-a915-148f2ec81ba6)
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5780c656-8dd0-4322-b3b2-6b4ad3b88c67">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/332dc793-2d75-4d21-b12b-f82707037a48">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9bb53b97-74eb-4391-83e1-6578a5b4a527">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Stylesheet from "./components/Stylesheet";
import { useState } from "react";

function App() {
  const [isPrimary, setIsPrimary] = useState(false);

  return (
    <div className="App">
      <Stylesheet isPrimary={isPrimary} setIsPrimary={setIsPrimary} />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/Stylesheet.js:

```js
import React from "react";
import "./myStyles.css";

const Stylesheet = (props) => {
  const className = props.isPrimary ? "primary" : "secondary";

  return (
    <div>
      <h1
        onClick={() => props.setIsPrimary((prev) => !prev)}
        className={`${className} font-xl pointer`}
      >
        Stylesheet
      </h1>
    </div>
  );
};

export default Stylesheet;
```

### NXT/hello-world/src/components/myStyles.css:

```css
.primary {
  color: orange;
}
.secondary {
  color: green;
}

.font-xl {
  font-size: 4rem;
}

.pointer {
  cursor: pointer;
}
```

</details>

<details>
  <summary>16. Styling and CSS Basics - Inline Styling </summary>

# Inline Styling

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/225a5f5e-287b-4fec-a915-148f2ec81ba6)
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1d21e7c2-00f5-45e9-a962-2d9758f193a4">
<img width="970" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/598a5f2e-1a6d-492d-accc-be33a0fb83af">
<img width="1233" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9e824009-2f16-42c0-9723-8285f1392271">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Inline from "./components/Inline";

function App() {
  return (
    <div className="App">
      <Inline />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/Inline.js:

```js
import React from "react";

const heading = {
  fontSize: "72px",
  color: "blue",
};

const Inline = () => {
  return (
    <div>
      <h1 style={heading}>Inline</h1>
    </div>
  );
};

export default Inline;
```

</details>

<details>
  <summary>17. Styling and CSS Basics - CSS Modules </summary>

# CSS Modules

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/225a5f5e-287b-4fec-a915-148f2ec81ba6)
<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/377abaeb-5459-4ab7-b9b8-b9385f530c03">
<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0c60eb9a-9705-41e6-9300-18db3b59f1b3">
<img width="972" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fa376435-6f71-472d-a115-87833fe09a66">
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/3e87e0f1-43bb-48c9-b41b-bcf9da1f7d8a)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import styles from "./appStyles.module.css";
import "./appStyles.css";

function App() {
  return (
    <div className="App">
      <h2 className="error">Error</h2>
      <h2 className={styles.success}>Success</h2>
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/appStyles.css:

```css
.error {
  color: red;
}
```

### NXT/hello-world/src/appStyles.module.css:

```js
.success {
  color: green;
}
```

</details>

<details>
  <summary>18. Form Handling </summary>

# Form Handling

<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e6fa7061-7d54-4ab7-89e2-58d02afa4741">
<img width="969" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e1edc71e-ea13-469b-a020-20e617ec6bf2">
<img width="1233" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3300b21e-cc5b-417b-9d4e-c9fcb6b20a4a">
<img width="1233" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ef4b5705-9ff4-4716-9fa6-f8819a1b69fd">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import Form from "./components/Form";

function App() {
  return (
    <div className="App">
      <Form />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/Form.jsx:

```js
import React, { Component } from "react";

class Form extends Component {
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      comments: "",
      topic: "react",
    };

    this.handleUsernameChange = this.handleUsernameChange.bind(this);
    this.handleCommentsChange = this.handleCommentsChange.bind(this);
  }

  handleUsernameChange = (event) => {
    this.setState({ username: event.target.value });
  };

  handleCommentsChange = (event) => {
    this.setState({ comments: event.target.value });
  };

  handleTopicChange = (event) => {
    this.setState({ topic: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    alert(
      `${this.state.username} - ${this.state.comments} - ${this.state.topic}`
    );
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <div>
          <h1>Form Component</h1>
          <label htmlFor="username">Username</label>
          <input
            id="username"
            type="text"
            value={this.state.username}
            onChange={this.handleUsernameChange}
          />
        </div>
        <div>
          <label htmlFor="comments">Comments</label>
          <textarea
            id="comments"
            cols="30"
            rows="10"
            value={this.state.comments}
            onChange={this.handleCommentsChange}
          ></textarea>
        </div>
        <div>
          <label>Topic</label>
          <select value={this.state.topic} onChange={this.handleTopicChange}>
            <option value="react" selected>
              React
            </option>
            <option value="angular">Angular</option>
            <option value="vue">Vue option</option>
          </select>
        </div>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
    );
  }
}

export default Form;
```

</details>

<details>
  <summary>19. Component Lifecycle Methods - Mounting  </summary>

# Component Lifecycle Methods - Mounting

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/69b9df31-991b-4893-88ed-f23076ef3a9f)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/1f6d176b-adeb-4844-80c8-3f60ff4e6d81)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/2e625562-32e6-4784-8614-06bb4f328dc3)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/6f48b0ae-ca2c-46b7-85a6-b204f82204c7)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/e12090ff-5aad-4ec6-9613-a3bd2df06041)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/d12b5288-0b33-4f7c-b44c-0869daa98029)
<img width="1023" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/89610a81-5b9b-42cd-983e-522e7955724a">
<img width="1023" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fc3ff690-6f5d-4a66-81cb-c3f6d7fc0afe">
<img width="1183" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/48ccf02e-a785-455d-9571-c24bf91bc633">
<img width="1193" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/74393f77-e9cb-4bea-8886-aabe4d8973e7">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/e94a8b7c-fe16-4663-9f3c-572444741fc2)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import LifecycleA from "./components/LifecycleA";

function App() {
  return (
    <div className="App">
      <LifecycleA />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/LifecycleA.jsx:

```js
import React, { Component } from "react";

class LifecycleA extends Component {
  constructor(props) {
    super(props);

    this.state = {
      name: "Ifeanyi",
    };
    console.log("LifecycleA constructor");
  }

  static getDerivedStateFromProps(props, state) {
    console.log("LifecycleA getDerivedStateFromProps");
    return null;
  }

  componentDidMount() {
    console.log("LifecycleA component DidMount");
  }

  render() {
    console.log("LifecycleA render");
    return (
      <div>
        <h1>LifecycleA</h1>
      </div>
    );
  }
}

export default LifecycleA;
```

</details>

<details>
  <summary>20. Component Lifecycle Methods - Updating  </summary>

# Component Lifecycle Methods - Updating

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/69b9df31-991b-4893-88ed-f23076ef3a9f)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/1f6d176b-adeb-4844-80c8-3f60ff4e6d81)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/13ebbcbc-18a7-44e7-b968-4b56179b8b2d)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/7bd27903-4ed9-4920-aa7a-fb27b9a24405)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/cc2f9d5a-d717-428c-aca5-2efe9aa35918)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/c48f1d74-37a4-4ac6-b8f5-6ba41b8f3664)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/bea83ad1-0358-4ded-b3bf-7ffe1368506d)

<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/95dbe180-3190-4bbb-a8c3-3a5af4968489">
<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ba5e419b-a953-43a2-af6c-8b0363d3c650">
<img width="1193" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b93551eb-bd9f-4f03-9c1d-9fdcf8b48cef">
<img width="1193" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a5b64ce7-1a95-450f-acc4-493688a1230e">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import LifecycleA from "./components/LifecycleA";

function App() {
  return (
    <div className="App">
      <LifecycleA />
    </div>
  );
}

export default App;
```

### NXT/hello-world/src/components/LifecycleA.jsx:

```js
import React, { Component } from "react";

class LifecycleA extends Component {
  constructor(props) {
    super(props);

    this.state = {
      name: "Ifeanyi",
    };
    console.log("LifecycleA constructor");
  }

  static getDerivedStateFromProps(props, state) {
    console.log("LifecycleA getDerivedStateFromProps");
    return null;
  }

  componentDidMount() {
    console.log("LifecycleA component DidMount");
  }

  shouldComponentUpdate() {
    console.log("LifecycleA shouldComponentUpdate");
    return true;
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log("LifecycleA getSnapshotBeforeUpdate");
    return null;
  }

  componentDidUpdate() {
    console.log("LifecycleA componentDidUpdate");
  }

  changeState = () => {
    this.setState({
      name: "Codevolution",
    });
  };

  render() {
    console.log("LifecycleA render");
    return (
      <div>
        <h1>LifecycleA</h1>
        <button onClick={this.changeState}>Change state</button>
      </div>
    );
  }
}

export default LifecycleA;
```

</details>

<details>
  <summary>21. Component Lifecycle Methods - Unmounting  </summary>

# Component Lifecycle Methods - Unmounting

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/642db6de-1b19-417f-952c-9e99c2f1c524)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/b581a4a4-cbaa-4c0b-8425-56857f8d9398)

</details>

<details>
  <summary>22. Fragments  </summary>

# Fragments

<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/930f2d28-0b6f-43e5-97f4-cc4f85b464a5">
<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0987da58-f1e6-4b51-8aad-da1df6b4e50a">
<img width="1188" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/870b61d3-7a94-4ba9-9f8c-fdc4546c735c">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import FragmentDemo from "./components/FragmentDemo";

class App extends Component {
  render() {
    return (
      <div>
        <FragmentDemo />
        <br />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/FragmentDemo.jsx:

```js
import React from "react";

export default function FragmentDemo() {
  return (
    <React.Fragment>
      <h1>FragmentDemo</h1>
      <p>This describes the Fragment Demo Component</p>
    </React.Fragment>
  );
}
```

</details>

<details>
  <summary>23. Pure Components </summary>

# Pure Components

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/21c34488-3e55-494a-8249-6da29d8005d3)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/e45dc775-40a1-479b-8375-32bab6fc781d)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/6fd29301-dba3-45ad-8665-4321994cf5d9)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/8b0b41f3-c932-434a-8474-4f9045aceb42)
<img width="959" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/661e7d82-1b18-4e5c-8158-ddb1c63a7b4b">
<img width="959" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ba3368a3-c776-4754-a574-64fa0e2917bd">
<img width="1193" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/34d27d3a-9ed1-4bf5-877a-34f684309a2f">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import PureComp from "./components/PureComp";

class App extends Component {
  render() {
    return (
      <div>
        <PureComp />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/PureComp.jsx:

```js
import React, { PureComponent } from "react";

class PureComp extends PureComponent {
  render() {
    return (
      <div>
        <h1>Pure Component</h1>
      </div>
    );
  }
}

export default PureComp;
```

</details>

<details>
  <summary>24. Memo </summary>

# Memo

<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8fa07f67-b97d-49c6-8335-b7bfcff3c0ff">
<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3ae763a8-db37-4e18-9703-d6b51573a046">
<img width="1155" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d017b8d6-66ff-4ad6-a8f4-8ecc8ab01cc1">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import MemoComp from "./components/MemoComp";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      name: "Jonny",
    };
  }

  componentDidMount() {
    setInterval(() => {
      this.setState({
        name: "Jonny",
      });
    }, 2000);
  }

  render() {
    console.log("- App Component Rendering -");
    return (
      <div>
        <MemoComp name={this.state.name} />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/MemoComp.jsx:

```js
import React from "react";

function MemoComp({ name }) {
  console.log("Rendering Memo Component");

  return (
    <div>
      <h1>{name}</h1>
    </div>
  );
}

export default React.memo(MemoComp);
```

</details>

<details>
  <summary>25. Refs Input Focus </summary>

# Refs Input Focus

<img width="958" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/96749ba6-dbb6-422a-b480-f707435611ff">
<img width="958" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9c7e13b3-0945-4c6b-b612-fcab41512d62">
<img width="1154" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b87396b0-ac4f-45bd-a732-2a9ecbd6e5cc">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import RefsDemo from "./components/RefsDemo";

class App extends Component {
  render() {
    return (
      <div>
        <RefsDemo />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/RefsDemo.jsx:

```js
import React, { Component } from "react";

class RefsDemo extends Component {
  constructor(props) {
    super(props);

    this.state = {
      name: "Jonny",
    };

    this.inputRef = React.createRef();
  }

  componentDidMount() {
    console.log(this.inputRef);
    this.inputRef.current.focus();
  }

  clickHandler = () => {
    alert(this.inputRef.current.value);
  };

  render() {
    return (
      <div>
        <input ref={this.inputRef} type="text" />
        <button onClick={this.clickHandler}>Click</button>
      </div>
    );
  }
}

export default RefsDemo;
```

</details>

<details>
  <summary>26. Refs from Child to Parent </summary>

# Refs from Child to Parent

<img width="959" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e0a9d153-01e3-47fd-9f28-75c244d96aba">
<img width="959" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9eb31db7-4b42-4741-8dd2-9a003fca351e">
<img width="959" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/82076a9b-ddee-43e0-98bd-b3118a584431">
<img width="1154" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fd554d49-ae9e-4812-9225-36fdfd108c88">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import InputParent from "./components/InputParent";

class App extends Component {
  render() {
    return (
      <div>
        <InputParent />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/InputParent.jsx:

```js
import React, { Component } from "react";
import Input from "./Input";

class InputParent extends Component {
  constructor(props) {
    super(props);
    this.componentRef = React.createRef();
  }

  clickHandler = () => {
    this.componentRef.current.focusInput();
  };

  render() {
    return (
      <div>
        <Input ref={this.componentRef} />
        <button onClick={this.clickHandler}>Focus Input</button>
      </div>
    );
  }
}

export default InputParent;
```

### NXT/hello-world/src/components/Input.jsx:

```js
import React, { Component } from "react";

class Input extends Component {
  constructor(props) {
    super(props);

    this.state = {};

    this.inputRef = React.createRef();
  }

  focusInput() {
    this.inputRef.current.focus();
  }

  render() {
    return (
      <div>
        <input type="text" ref={this.inputRef} />
      </div>
    );
  }
}

export default Input;
```

</details>

<details>
  <summary>27. Forwarding Refs from Parent to Child </summary>

# Forwarding Refs from Parent to Child

<img width="961" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fb4535ae-e910-4bfa-9c2e-df1f59928105">
<img width="961" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e0404c03-6b10-4cd2-8da6-226e48da0cd0">
<img width="961" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0be43fa3-9236-4948-92a7-780757bc43d7">
<img width="1154" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fe30826c-2800-4a14-a63c-93589ed17c22">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import InputParent from "./components/InputParent";

class App extends Component {
  render() {
    return (
      <div>
        <InputParent />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/InputParent.jsx:

```js
import React, { Component } from "react";
import Input from "./Input";

class InputParent extends Component {
  constructor(props) {
    super(props);
    this.inputRef = React.createRef();
  }

  clickHandler = () => {
    this.inputRef.current.focus();
  };

  render() {
    return (
      <div>
        <Input ref={this.inputRef} />
        <button onClick={this.clickHandler}>Focus Input</button>
      </div>
    );
  }
}

export default InputParent;
```

### NXT/hello-world/src/components/Input.jsx:

```js
import React from "react";

const Input = React.forwardRef((props, ref) => {
  return (
    <div>
      <input type="text" ref={ref} />
    </div>
  );
});

export default Input;
```

</details>

<details>
  <summary>28. Portals </summary>

# Portals

<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/90df2f16-1c32-45fa-bed7-ae47d1dee42e">
<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a301fa0c-cd5c-429b-8a16-014685c139f7">
<img width="960" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/95477c86-5b19-46f7-ae35-4753d7e63ba9">
<img width="1307" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4afdf863-6159-4a10-97e8-846edbed2d61">

### NXT/hello-world/public/index.html:

```js
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
    <div id="portal-root"></div>
  </body>
</html>
```

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import PortalDemo from "./components/PortalDemo";

class App extends Component {
  render() {
    return (
      <div>
        <PortalDemo />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/PortalDemo.jsx:

```js
import React from "react";
import ReactDOM from "react-dom";

function PortalDemo() {
  return ReactDOM.createPortal(
    <h1>Portals Demo</h1>,
    document.getElementById("portal-root")
  );
}

export default PortalDemo;
```

</details>

<details>
  <summary>29. Error Boundaries </summary>

# Error Boundaries

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/f04a24c8-f903-41af-827f-b5eb3b97fad2)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/376c458b-84a6-4de7-8f21-30a572ade69d)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/c7e9d5a6-f25b-4b59-a1a1-a20794732bca)
<img width="1286" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/df60873b-269d-4766-ae25-a960e68610d6">
<img width="1286" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4413380c-929c-4705-b3d5-f2e8b28d7ef5">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/db1d430f-a95c-40b8-9157-c70978e5352a)
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6921f4d5-d8ca-4b2c-a847-7eaebaf14c5f">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3ebe980a-7923-441a-ad05-a1d73f8d764f">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f0e33760-243e-405d-acbd-56ac924d19d8">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import Hero from "./components/Hero";
import ErrorBoundary from "./components/ErrorBoundary";

class App extends Component {
  render() {
    return (
      <div className="App">
        <ErrorBoundary>
          <Hero heroName="Batman" />
        </ErrorBoundary>

        <ErrorBoundary>
          <Hero heroName="Superman" />
        </ErrorBoundary>

        <ErrorBoundary>
          <Hero heroName="Joker" />
        </ErrorBoundary>
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/ErrorBoundary.jsx:

```js
import React, { Component } from "react";

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = {
      hasError: false,
    };
  }

  static getDerivedStateFromError(error) {
    return {
      hasError: true,
    };
  }

  componentDidCatch(error, info) {
    console.log(error);
    console.log(info);
  }

  render() {
    if (this.state.hasError) return <h2>Something went Wrong!</h2>;
    return this.props.children;
  }
}

export default ErrorBoundary;
```

### NXT/hello-world/src/components/Hero.jsx:

```js
import React from "react";

function Hero({ heroName }) {
  if (heroName === "Joker") {
    throw new Error("Not a hero!");
  }

  return (
    <div>
      <h2>{heroName}</h2>
    </div>
  );
}

export default Hero;
```

</details>

<details>
  <summary>30. Higher Order Components </summary>

# Higher Order Components

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/77f4cb3e-b037-462f-bb58-c95db9411e67)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/5a2a0967-4880-428d-a1be-50884c8ecf90)
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1da256df-6c15-473f-a47e-4c20050ed7cc">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/30ec04e9-c290-487f-9222-4a1717f3ba3d">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d5c043e5-6d88-422e-bcc6-8fb42b696c16">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/a410ecbf-29c9-49b6-9693-c8dc902e5234">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/939c29bf-0bb2-458a-bb36-fda3b0238e45)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import ClickCounter from "./components/ClickCounter";
import HoverCounter from "./components/HoverCounter";

class App extends Component {
  render() {
    return (
      <div className="App">
        <ClickCounter />
        <HoverCounter />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/withCounter.jsx:

```js
import React from "react";

const withCounter = (WrappedComponent) => {
  class NewComponent extends React.Component {
    constructor(props) {
      super(props);

      this.state = { count: 0 };
    }

    incrementCount = () => {
      this.setState((prevState) => {
        return { count: ++prevState.count };
      });
    };

    render() {
      return (
        <WrappedComponent
          name="Ifeanyi"
          count={this.state.count}
          incrementCount={this.incrementCount}
        />
      );
    }
  }
  return NewComponent;
};

export default withCounter;
```

### NXT/hello-world/src/components/ClickCounter.jsx:

```js
import React, { Component } from "react";
import withCounter from "./withCounter";

class ClickCounter extends Component {
  render() {
    const { name, count, incrementCount } = this.props;

    return (
      <div>
        <button onClick={incrementCount}>
          {name} Clicked {count} times
        </button>
      </div>
    );
  }
}

export default withCounter(ClickCounter);
```

### NXT/hello-world/src/components/HoverCounter.jsx:

```js
import React, { Component } from "react";
import withCounter from "./withCounter";

class HoverCounter extends Component {
  render() {
    const { name, count, incrementCount } = this.props;

    return (
      <div>
        <h1 onMouseOver={incrementCount}>
          {name} touched this {count} times
        </h1>
      </div>
    );
  }
}

export default withCounter(HoverCounter);
```

</details>

<details>
  <summary>31. Render Props </summary>

# Render Props

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/b03e6d7a-e855-4065-9734-66dab2f47b07)
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/49a9a409-740e-4967-b82f-55986139056c">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5d2c77c1-05e7-41ce-af34-912528380fd6">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4444c6f6-1a91-4439-ace0-ac07146da7aa">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0f4bb898-e6a5-45f4-a72f-bf633039e3d1">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bac0ef98-d69d-4fb1-b2e1-19e356a8998b">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/2aa99a82-b537-4fbc-85bf-28daf8f51366)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import ClickCounter from "./components/ClickCounter";
import HoverCounter from "./components/HoverCounter";
import User from "./components/User";
import Counter from "./components/Counter";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Counter
          render={(count, incrementCount) => (
            <ClickCounter count={count} incrementCount={incrementCount} />
          )}
        />
        <Counter
          render={(count, incrementCount) => (
            <HoverCounter count={count} incrementCount={incrementCount} />
          )}
        />
        <User render={(isLoggedIn) => (isLoggedIn ? "Ifeanyi" : "Guest")} />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/Counter.jsx:

```js
import React, { Component } from "react";

class Counter extends Component {
  constructor(props) {
    super(props);

    this.state = { count: 0 };
  }

  incrementCount = () => {
    this.setState((prevState) => {
      return { count: ++prevState.count };
    });
  };

  render() {
    return (
      <div>{this.props.render(this.state.count, this.incrementCount)}</div>
    );
  }
}

export default Counter;
```

### NXT/hello-world/src/components/ClickCounter.jsx:

```js
import React, { Component } from "react";
import withCounter from "./withCounter";

class ClickCounter extends Component {
  render() {
    const { count, incrementCount } = this.props;

    return (
      <div>
        <button onClick={incrementCount}>Clicked {count} times</button>
      </div>
    );
  }
}

export default withCounter(ClickCounter);
```

### NXT/hello-world/src/components/HoverCounter.jsx:

```js
import React, { Component } from "react";
import withCounter from "./withCounter";

class HoverCounter extends Component {
  render() {
    const { count, incrementCount } = this.props;

    return (
      <div>
        <h1 onMouseOver={incrementCount}>Touched this {count} times</h1>
      </div>
    );
  }
}

export default withCounter(HoverCounter);
```

### NXT/hello-world/src/components/User.jsx:

```js
import React, { Component } from "react";

class User extends Component {
  render() {
    return (
      <div>
        <h1>{this.props.render(false)}</h1>
      </div>
    );
  }
}

export default User;
```

</details>

<details>
  <summary>32. React Context </summary>

# React Context

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/cada774c-b76e-422b-af67-aedcfef90a7a)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/5a51325d-1f17-4546-b6c4-5c1e9ccc8616)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/ff4d377b-1a23-4696-86ec-84b7853b8061)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/7a8f0423-5018-4645-85f4-8e6d411a06d3)
![image](https://github.com/omeatai/My-Tutorials/assets/32337103/4db23154-dda4-490b-8475-eeeb94bf6026)
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/66b7d672-c266-40c3-84a6-bebdf87a682d">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b809b446-2a00-4ae5-9f6d-02a4c3d8e1c5">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/96b9aae8-c7ad-4117-bbcb-9af94523abbe">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/28f2453b-a1eb-4532-af9d-44f92e1d48c8">
<img width="991" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f0ead32f-8fa3-42e5-80b8-536010d9c4b6">

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/4fca0923-5d95-4b06-9743-d39892fcb9fe)

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import ComponentC from "./components/ComponentC";
import { UserProvider } from "./components/userContext";

class App extends Component {
  render() {
    return (
      <div className="App">
        <UserProvider value={{ username: "Bayo", age: 16 }}>
          <ComponentC />
        </UserProvider>
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/userContext.jsx:

```js
import React from "react";

const UserContext = React.createContext();

const UserProvider = UserContext.Provider;
const UserConsumer = UserContext.Consumer;

export { UserProvider, UserConsumer };
export default UserContext;
```

### NXT/hello-world/src/components/ComponentC.jsx:

```js
import React, { Component } from "react";
import ComponentE from "./ComponentE";

class ComponentC extends Component {
  render() {
    return <ComponentE />;
  }
}
export default ComponentC;
```

### NXT/hello-world/src/components/ComponentE.jsx:

```js
import React, { Component } from "react";
import ComponentF from "./ComponentF";
import UserContext from "./userContext";

class ComponentE extends Component {
  static contextType = UserContext;
  render() {
    return (
      <div>
        <h2>ComponentE Context - {this.context.username}</h2>
        <ComponentF />
      </div>
    );
  }
}

// ComponentE.contextType = UserContext;

export default ComponentE;
```

### NXT/hello-world/src/components/ComponentF.jsx:

```js
import React, { Component } from "react";
import { UserConsumer } from "./userContext";

class ComponentF extends Component {
  render() {
    return (
      <div>
        <UserConsumer>
          {(value) => (
            <h2>
              Hello, {value.username}. You are {value.age} years old.
            </h2>
          )}
        </UserConsumer>
      </div>
    );
  }
}

export default ComponentF;
```

</details>

<details>
  <summary>33. React HTTP GET Request </summary>

# React HTTP GET Request

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/e419f115-5f0c-405a-9fce-ace395953556)
<img width="1221" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/41127f82-6ffa-4ba1-8d4b-48b5041a02d4">
<img width="1221" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d464666e-6c72-473c-b276-5b3d4239c7c7">
<img width="1221" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/9a9c5865-6660-4716-860c-4fc44bb84961">
<img width="988" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7574c3a3-4a10-4e76-bfa6-5bf1402e7758">
<img width="988" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/bc177585-a3b5-476f-a023-da2b8814fd20">
<img width="1221" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/8de12bdc-4feb-43f9-9b91-c3f8d4f7332e">
<img width="1221" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/36f64295-129e-425c-bd97-9b8f60a8431b">

# Install Axios

```js
yarn add axios
npm install axios
```

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import PostList from "./components/PostList";

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Home Page</h1>
        <PostList />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/PostList.jsx:

```js
import React, { Component } from "react";
import axios from "axios";

class PostList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      posts: [],
      errorMsg: "",
    };
  }

  componentDidMount() {
    axios
      .get("https://jsonplaceholder.typicode.com/posts")
      .then((response) => {
        console.log(response.data);
        this.setState({ posts: response.data });
      })
      .catch((error) => {
        console.log(error);
        this.setState({ errorMsg: "Error retrieving Data..." });
      });
  }

  render() {
    const { posts, errorMsg } = this.state;

    return (
      <div>
        <h1>List of Posts</h1>
        <div>
          {posts.length
            ? posts.map((post) => (
                <div key={post.id}>
                  {post.id}. {post.title}
                </div>
              ))
            : "No Posts Available"}
        </div>
        <div>{errorMsg ? <div>{errorMsg}</div> : null}</div>
      </div>
    );
  }
}

export default PostList;
```

</details>

<details>
  <summary>34. React HTTP POST Request </summary>

# React HTTP POST Request

![image](https://github.com/omeatai/My-Tutorials/assets/32337103/a6c2f8af-8a72-40d6-a408-2b575fb17528)
<img width="990" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/b0179c23-99e8-4b35-a3fd-8b57910a7533">
<img width="990" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/21381dde-e079-46b7-b671-241269d2a32c">
<img width="990" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/658ac85a-d220-4d84-b6f7-0734b947a984">
<img width="1219" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3a7efe5f-4daf-49bd-b7c7-8d25ee34b892">
<img width="1219" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/436bc7f5-a008-4a89-85b1-c6f094cca650">

### NXT/hello-world/src/App.js:

```js
import "./App.css";
import React, { Component } from "react";
import PostList from "./components/PostList";
import PostForm from "./components/PostForm";

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Home Page</h1>
        <PostForm />
        <PostList />
      </div>
    );
  }
}

export default App;
```

### NXT/hello-world/src/components/PostList.jsx:

```js
import React, { Component } from "react";
import axios from "axios";

class PostList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      posts: [],
      errorMsg: "",
    };
  }

  componentDidMount() {
    axios
      .get("https://jsonplaceholder.typicode.com/posts")
      .then((response) => {
        // console.log(response.data);
        this.setState({ posts: response.data });
      })
      .catch((error) => {
        console.log(error);
        this.setState({ errorMsg: "Error retrieving Data..." });
      });
  }

  render() {
    const { posts, errorMsg } = this.state;

    return (
      <div>
        <h1>List of Posts</h1>
        <div>
          {posts.length
            ? posts.map((post) => (
                <div key={post.id}>
                  {post.id}. {post.title}
                </div>
              ))
            : "No Posts Available"}
        </div>
        <div>{errorMsg ? <div>{errorMsg}</div> : null}</div>
      </div>
    );
  }
}

export default PostList;
```

### NXT/hello-world/src/components/PostForm.jsx:

```js
import React, { Component } from "react";
import axios from "axios";

class PostForm extends Component {
  constructor(props) {
    super(props);

    this.state = {
      userId: "",
      title: "",
      body: "",
    };
  }

  changeHandler = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  componentDidUpdate() {
    // console.log(this.state);
  }

  submitHandler = (e) => {
    e.preventDefault();
    if (!this.state.userId || !this.state.title || !this.state.body) {
      console.log("Enter value to all fields...");
      return;
    }
    console.log(this.state);
    axios
      .post("https://jsonplaceholder.typicode.com/posts", this.state)
      .then((response) => console.log(response))
      .catch((error) => console.log(error));
  };

  render() {
    const { userId, title, body } = this.state;

    return (
      <div>
        <form onSubmit={this.submitHandler}>
          <div>
            <label htmlFor="userId">UserID</label>
            <input
              type="text"
              id="userId"
              name="userId"
              value={userId}
              onChange={this.changeHandler}
            />
          </div>
          <div>
            <label htmlFor="title">Title</label>
            <input
              type="text"
              id="title"
              name="title"
              value={title}
              onChange={this.changeHandler}
            />
          </div>
          <div>
            <label htmlFor="body">Body</label>
            <input
              type="text"
              id="body"
              name="body"
              value={body}
              onChange={this.changeHandler}
            />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default PostForm;
```

</details>

+REACT HOOKS

<details>
  <summary>35. React Hooks - useState Hook </summary>

# React Hooks - useState Hook

```js

```

```js

```



</details>
