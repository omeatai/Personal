# REACT & NODE.JS CRASH COURSE TUTORIAL

## [COURSE](https://www.youtube.com/playlist?list=PL4cUxeGkcC9jsz4LDYc6kv3ymONOKxwBU)

# REACT

+INTRODUCTION

<details>
  <summary>1. Check Node Version</summary>

```bash
node -v
```

</details>

<details>
  <summary>2. Create React App</summary>

```bash
npx create-react-app dojo-blog
```

</details>

<details>
  <summary>3. Setup Files</summary>

Index.js:

```Javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
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
import logo from './logo.svg';
import './App.css';

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

Index.html:

```HTML
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
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  </body>
</html>

```

</details>

<details>
  <summary>4. Start Local Server</summary>

```bash
npm run start
```

```Javascript
// Compiled successfully!

// You can now view dojo-blog in the browser.

//   Local:            http://localhost:3000
//   On Your Network:  http://192.168.178.68:3000

// Note that the development build is not optimized.
// To create a production build, use npm run build.

// webpack compiled successfully

```

</details>

<details>
  <summary>5. Install all dependencies from Package.json</summary>

```bash
npm install
```

</details>

<details>
  <summary>6. App Component</summary>

App.js:

```Javascript
import './App.css';

function App() {
  const title = 'Welcome to the new blog';
  const likes = 50;
  const person = { name: 'yoshi' , age: 30 };
  const link = 'http://www.google.com';

  return (
    <div className="App">
      <header className="App-header">
        <h1>App Component</h1>
        <h2>{ title}</h2>
        <p>Liked { likes } times</p>
        <p>{ person.name }</p>
        <p>{ 10 }</p>
        <p>{ "hello, ninjas" }</p>
        <p>{ [1,2,3,4,5] }</p>
        <p>{Math.random() * 10 }</p>

        <a href={link}>Google Site</a>
      </header>
    </div>
  );
}

export default App;
```

</details>

<details>
  <summary>7. Importing Multiple Components</summary>

App.js:

```Javascript
import './App.css';
import Navbar from './components/Navbar';
import Home from './components/Home';

function App() {

  return (
    <div className="App">
      <Navbar />
      <header className="content">
        <Home />
      </header>
    </div>
  );
}

export default App;
```

Navbar.js:

```Javascript
const Navbar = () => {
    return (
        <nav className="navbar">
            <h1>The Dojo Blog</h1>
            <div className="links">
                <a href="/">Home</a>
                <a href="/create" style={{
                    color: "white",
                    backgroundColor: "#f1356d",
                    borderRadius: "8px",
                    padding: "5px",
                    textDecoration: "none"
                }}>New Blog</a>
            </div>
        </nav>
    );
}

export default Navbar;
```

Home.js:

```Javascript
const Home = ()=> {
    return (
        <div className="home">
            <h2>This is the Homepage</h2>
        </div>
    );
}

export default Home;
```

</details>

<details>
  <summary>8. Global Styling from Index</summary>

Index.js:

```Javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
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
import Navbar from './components/Navbar';
import Home from './components/Home';

function App() {

  return (
    <div className="App">
      <Navbar />
      <header className="content">
        <Home />
      </header>
    </div>
  );
}

export default App;
```

Index.css:

```CSS
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap');

/* base styles */
* {
  margin: 0;
  font-family: "Quicksand";
  color: #333;
}
.navbar {
  padding: 20px;
  display: flex;
  align-items: center;
  max-width: 600px;
  margin: 0 auto;
  border-bottom: 1px solid #f2f2f2;
}
.navbar h1 {
  color: #f1356d;
}
.navbar .links {
  margin-left: auto;
}
.navbar a {
  margin-left: 16px;
  text-decoration: none;
  padding: 6px;
}
.navbar a:hover {
  color: #f1356d;
}
.content {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
}

```

</details>

<details>
  <summary>9. Click Events</summary>

Home.js:

```Javascript
const Home = ()=> {

    const handleClick = (e) => {
        console.log('hello, ninjas', e.target);
    }

    return (
        <div className="home">
            <h2>This is the Homepage</h2>
            <button onClick={handleClick}>Click me</button>
        </div>
    );
}

export default Home;
```

```Javascript
// hello, ninjas <button>Click me Again</button>
```

```Javascript
const Home = ()=> {

    const handleClick = (e) => {
        console.log('hello, ninjas', e.target);
    }

    const handleClickAgain = (e, name) => {
        console.log('hello ' + name);
        console.log(e.target);
    }

    return (
        <div className="home">
            <h2>This is the Homepage</h2>
            <button onClick={handleClick}>Click me</button>
            <button onClick={(e)=>handleClickAgain(e, 'Ben')}>Click me Again</button>
        </div>
    );
}

export default Home;
```

```Javascript
// hello Ben
// <button>Click me Again</button>
```

</details>

<details>
  <summary>10. Using State</summary>

Home.js:

```Javascript
import {useState} from 'react';

const Home = () => {

    const [name, setName] = useState('Andrew');

    const handleClick = (e) => {
        setName(e.target.value);
    }

    return (
        <div className="home">
            <h2>This is the Homepage</h2>
            <p>{name}</p>
            <button value='Mike' onClick={handleClick}>Click me</button>
        </div>
    );
}

export default Home;
```

```Javascript
import {useState} from 'react';

const Home = () => {

    const [name, setName] = useState('Andrew');
    const [age, setAge] = useState(25);

    const handleClick = (e) => {
        setName('Mike');
        setAge(30);
    }

    return (
        <div className="home">
            <h2>This is the Homepage</h2>
            <p>{ name } is { age } years old</p>
            <button onClick={handleClick}>Click me</button>
        </div>
    );
}

export default Home;
```

</details>

<details>
  <summary>11. Outputting Lists</summary>

Home.js:

```Javascript
import {useState} from 'react';

const Home = () => {

    const [blogs, setBlogs] = useState([
        {title: 'My new website', body: 'lorem ipsum...', author: 'mario', id: 1},
        {title: 'Welcome party!', body: 'lorem ipsum...', author: 'yoshi', id: 2},
        {title: 'Web dev top tips', body: 'lorem ipsum...', author: 'mario', id: 3}
    ]);

    return (
        <div className="home">
            {blogs.map((blog) => (
                <div className="blog-preview" key={blog.id}>
                    <h2>{ blog.title }</h2>
                    <p>Written by { blog.author }</p>
                </div>
            ))}
        </div>
    );
}

export default Home;
```

Index.css:

```css
/* blog previews / list */
.blog-preview {
  padding: 10px 16px;
  margin: 20px 0;
  border-bottom: 1px solid #fafafa;
}
.blog-preview:hover {
  box-shadow: 1px 3px 5px rgba(0, 0, 0, 0.1);
}
.blog-preview h2 {
  font-size: 20px;
  color: #f1356d;
  margin-bottom: 8px;
}
```

</details>

<details>
  <summary>12. Reusable Components and Props</summary>

Home.js:

```Javascript
import {useState} from 'react';
import BlogList from './BlogList';

const Home = () => {

    const [blogs, setBlogs] = useState([
        {title: 'My new website', body: 'lorem ipsum...', author: 'mario', id: 1},
        {title: 'Welcome party!', body: 'lorem ipsum...', author: 'yoshi', id: 2},
        {title: 'Web dev top tips', body: 'lorem ipsum...', author: 'mario', id: 3}
    ]);

    return (
        <BlogList blogs={blogs} title="All Blogs!" />
    );
}

export default Home;
```

BlogList.js:

```Javascript
import React from 'react';

const BlogList = ({blogs, title}) => {
    // const blogs = props.blogs;
    // const title = props.title;

    return (
        <div className="home">
            <h2>{ title }</h2>
            {blogs.map((blog) => (
                <div className="blog-preview" key={blog.id}>
                    <h2>{ blog.title }</h2>
                    <p>Written by { blog.author }</p>
                </div>
            ))}
        </div>
     );
}

export default BlogList;
```

</details>

<details>
  <summary>13. Filtering Props</summary>

Home.js:

```Javascript
import {useState} from 'react';
import BlogList from './BlogList';

const Home = () => {

    const [blogs, setBlogs] = useState([
        {title: 'My new website', body: 'lorem ipsum...', author: 'mario', id: 1},
        {title: 'Welcome party!', body: 'lorem ipsum...', author: 'yoshi', id: 2},
        {title: 'Web dev top tips', body: 'lorem ipsum...', author: 'mario', id: 3}
    ]);

    return (
        <BlogList blogs={blogs.filter((blog) => blog.author === 'mario')} title="All Blogs!" />
    );
}

export default Home;
```

</details>

<details>
  <summary>14. Handle Delete Blog</summary>

Home.js:

```Javascript
import {useState} from 'react';
import BlogList from './BlogList';

const Home = () => {

    const [blogs, setBlogs] = useState([
        {title: 'My new website', body: 'lorem ipsum...', author: 'mario', id: 1},
        {title: 'Welcome party!', body: 'lorem ipsum...', author: 'yoshi', id: 2},
        {title: 'Web dev top tips', body: 'lorem ipsum...', author: 'mario', id: 3}
    ]);

    const handleDelete = (id)=> {
        const newBlogs = blogs.filter(blog => blog.id !== id);
        setBlogs(newBlogs);
    }

    return (
        <div className="home">
            <BlogList blogs={blogs} title="All Blogs!" handleDelete={handleDelete}/>
        </div>
    );
}

export default Home;
```

BlogList.js:

```Javascript
import React from 'react';

const BlogList = ({blogs, title, handleDelete}) => {

    return (
        <div className="blog-list">
            <h2>{ title }</h2>
            {blogs.map((blog) => (
                <div className="blog-preview" key={blog.id}>
                    <h2>{ blog.title }</h2>
                    <p>Written by { blog.author }</p>
                    <button onClick={()=>handleDelete(blog.id)}>Delete Blog</button>
                </div>
            ))}
        </div>
     );
}

export default BlogList;
```

</details>

<details>
  <summary>15. UseEffect Dependency</summary>

Home.js:

```Javascript
import { useEffect, useState } from "react";
import BlogList from "./BlogList";

const Home = () => {
    const [blogs, setBlogs] = useState([
        { title: "My new website", body: "lorem ipsum...", author: "mario", id: 1 },
        { title: "Welcome party!", body: "lorem ipsum...", author: "yoshi", id: 2 },
        { title: "Web dev top tips", body: "lorem ipsum...", author: "mario", id: 3},
    ]);

    const [name, setName] = useState('mario');

    const handleDelete = (id) => {
        const newBlogs = blogs.filter((blog) => blog.id !== id);
        setBlogs(newBlogs);
    };

    useEffect(() => {
        console.log("use effect ran");
        console.log(name);
    },[name]);

    return (
        <div className="home">
            <BlogList blogs={blogs} title="All Blogs!" handleDelete={handleDelete} />
            <button onClick={() => setName('luigi')}>change name</button>
            <p>{ name }</p>
        </div>
    );
};

export default Home;
```

</details>

+JSON-SERVER

<details>
  <summary>16. JSON Server - Setup Files</summary>

index.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>JSON Server</title>
  </head>
  <body>
    <nav>
      <h1>All Blogs</h1>
      <a href="/create.html">Add a new blog</a>
    </nav>

    <div class="blogs">
      <!-- inject blogs here from js -->
    </div>

    <script src="js/index.js"></script>
  </body>
</html>
```

create.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>JSON Server</title>
  </head>
  <body>
    <h1>Create a New Blog</h1>

    <form>
      <input type="text" name="title" required placeholder="Blog title" />
      <textarea name="body" required placeholder="Blog body"></textarea>
      <button>Create</button>
    </form>

    <script src="js/create.js"></script>
  </body>
</html>
```

details.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>JSON Server</title>
  </head>
  <body>
    <div class="details">
      <!-- inject blog details here -->
    </div>

    <script src="js/details.js"></script>
  </body>
</html>
```

styles.css:

```css
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap");

/* base styles */
body {
  background: #eee;
  font-family: "Roboto";
  color: #444;
  max-width: 960px;
  margin: 100px auto;
  padding: 10px;
}
nav {
  display: flex;
  justify-content: space-between;
}
nav h1 {
  margin: 0;
}
nav a {
  color: white;
  text-decoration: none;
  background: #36cca2;
  padding: 10px;
  border-radius: 10px;
}
form {
  max-width: 500px;
}
input,
textarea {
  display: block;
  margin: 16px 0;
  padding: 6px 10px;
  width: 100%;
  border: 1px solid #ddd;
  font-family: "Roboto";
}
textarea {
  min-height: 200px;
}
```

js/index.js

```Javascript
// javascript for index.html
```

js/create.js:

```Javascript
// javascript for create.html
```

js/details.js:

```Javascript
// javascript for details.html
```

</details>

<details>
  <summary>17. JSON Server - Install Server</summary>

```bash
# Install JSON Server Globally
npm install -g json-server

# #Install JSON Server Locally
npm install json-server

# Check JSON Server version
json-server --version

# Run JSON server
json-server --watch db.json
json-server --watch db.json --port 3004
```

</details>

<details>
  <summary>18. JSON Server - Create a Database</summary>

data/db.json:

```Json
{
  "posts": [
    {
      "id": 1,
      "likes": 30,
      "title": "Welcome to the new blog",
      "body": "Lorem ninja ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat."
    },
    {
      "id": 2,
      "likes": 15,
      "title": "How to be a Net Ninja",
      "body": "Lorem ninja ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat."
    },
    {
      "title": "New Vue course coming soon!",
      "body": "Lorem ninja ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.",
      "likes": 20,
      "id": 3
    },
    {
      "title": "Mario Kart Live review",
      "body": "Lorem ninja ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.",
      "likes": 69,
      "id": 4
    }
  ],
  "polls": [
    {
      "id": 1,
      "question": "Do you prefer Vue or React?",
      "answerA": "Vue",
      "answerB": "React"
    }
  ]
}

```

</details>

<details>
  <summary>19. JSON Server - Run Server/Watch Database</summary>

```bash
# Run JSON server
json-server --watch data/db.json
json-server --watch data/db.json --port 3004
```

```javascript
// \{^_^}/ hi!

//   Loading data/db.json
//   Done

//   Resources
//   http://localhost:3000/posts
//   http://localhost:3000/polls

//   Home
//   http://localhost:3000

//   Type s + enter at any time to create a snapshot of the database
//   Watching...
```

</details>

<details>
  <summary>20. JSON Server - Fetch All Data</summary>

Index.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>JSON Server</title>
  </head>
  <body>
    <nav>
      <h1>All Blogs</h1>
      <a href="/create.html">Add a new blog</a>
    </nav>

    <div class="blogs">
      <!-- inject blogs here from js -->
    </div>

    <script src="js/index.js"></script>
  </body>
</html>
```

js/index.js:

```javascript
// javascript for index.html
const container = document.querySelector(".blogs");
const pathname = window.location.pathname;
const filename = pathname.slice(pathname.lastIndexOf("/") + 1);
const dirname = pathname.slice(0, pathname.lastIndexOf("/"));

const renderPosts = async () => {
  let uri = "http://localhost:3000/posts";

  const res = await fetch(uri);
  const posts = await res.json();

  let template = "";
  posts.forEach((post) => {
    template += `
      <div class="post">
        <h2>${post.title}</h2>
        <p><small>${post.likes} likes</small></p>
        <p>${post.body.slice(0, 200)}...</p>
        <a href="${dirname}/details.html?id=${post.id}">Read more</a>
      </div>
    `;
  });

  container.innerHTML = template;
};

window.addEventListener("DOMContentLoaded", () => renderPosts());
```

styles.css:

```css
/* post list */
.post {
  padding: 16px;
  background: white;
  border-radius: 10px;
  margin: 20px 0;
}
.post h2 {
  margin: 0;
}
.post p {
  margin-top: 0;
}
.post a {
  color: #36cca2;
}
```

</details>

<details>
  <summary>21. JSON Server - Fetch Single Post </summary>

details.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>JSON Server</title>
  </head>
  <body>
    <div class="details">
      <!-- inject blog details here -->
    </div>

    <script src="js/details.js"></script>
  </body>
</html>
```

js/details.js:

```javascript
// javascript for details.html
const id = new URLSearchParams(window.location.search).get("id");
const container = document.querySelector(".details");
const pathname = window.location.pathname;
const filename = pathname.slice(pathname.lastIndexOf("/") + 1);
const dirname = pathname.slice(0, pathname.lastIndexOf("/"));

const renderDetails = async () => {
  const res = await fetch("http://localhost:3000/posts/" + id);
  if (!res.ok) {
    window.location.replace(`${dirname}/index.html`);
  }
  const post = await res.json();

  const template = `
    <h1>${post.title}</h1>
    <p>${post.body}</p>
  `;

  container.innerHTML = template;
};

window.addEventListener("DOMContentLoaded", renderDetails);
```

</details>

<details>
  <summary>22. JSON Server - Window location</summary>

```javascript
// window.location.href returns the href (URL) of the current page
// window.location.hostname returns the domain name of the web host
// window.location.pathname returns the path and filename of the current page
// window.location.protocol returns the web protocol used (http: or https:)
// window.location.assign() loads a new document
```

```Javascript
const pathname = window.location.pathname;
const filename = pathname.slice(pathname.lastIndexOf('/') + 1);
const dirname = pathname.slice(0, pathname.lastIndexOf('/'));
```

</details>

<details>
  <summary>23. JSON Server - Sorting Posts</summary>

```Javascript
let uri = 'http://localhost:3000/posts?_sort=likes&_order=desc';
```

Index.js:

```Javascript
// javascript for index.html
const container = document.querySelector('.blogs');
const pathname = window.location.pathname;
const filename = pathname.slice(pathname.lastIndexOf('/') + 1);
const dirname = pathname.slice(0, pathname.lastIndexOf('/'));

const renderPosts = async () => {
  let uri = 'http://localhost:3000/posts?_sort=likes&_order=desc';

  const res = await fetch(uri);
  const posts = await res.json();

  let template = '';
  posts.forEach(post => {
    template += `
      <div class="post">
        <h2>${post.title}</h2>
        <p><small>${post.likes} likes</small></p>
        <p>${post.body.slice(0, 200)}...</p>
        <a href="${dirname}/details.html?id=${post.id}">Read more</a>
      </div>
    `
  });

  container.innerHTML = template;
}

window.addEventListener('DOMContentLoaded', () => renderPosts());
```

</details>

<details>
  <summary>24. JSON Server - Add Posts to JSON DB</summary>

create.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>JSON Server</title>
  </head>
  <body>
    <h1>Create a New Blog</h1>

    <form>
      <input type="text" name="title" required placeholder="Blog title" />
      <textarea name="body" required placeholder="Blog body"></textarea>
      <button>Create</button>
    </form>

    <script src="js/create.js"></script>
  </body>
</html>
```

create.js:

```javascript
// javascript for create.html

const form = document.querySelector("form");

const pathname = window.location.pathname;
const filename = pathname.slice(pathname.lastIndexOf("/") + 1);
const dirname = pathname.slice(0, pathname.lastIndexOf("/"));

const createPost = async (e) => {
  e.preventDefault();

  const doc = {
    title: form.title.value,
    body: form.body.value,
    likes: 0,
  };

  await fetch("http://localhost:3000/posts", {
    method: "POST",
    body: JSON.stringify(doc),
    headers: { "Content-Type": "application/json" },
  });

  window.location.replace(`${dirname}/index.html`);
};

form.addEventListener("submit", createPost);
```

</details>

<details>
  <summary>25. JSON Server - Delete Post from DB</summary>

details.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>JSON Server</title>
  </head>
  <body>
    <div class="details">
      <!-- inject blog details here -->
    </div>
    <button class="delete">delete</button>

    <script src="js/details.js"></script>
  </body>
</html>
```

details.js:

```javascript
// javascript for details.html
const id = new URLSearchParams(window.location.search).get("id");
const container = document.querySelector(".details");
const deleteBtn = document.querySelector(".delete");

const pathname = window.location.pathname;
const filename = pathname.slice(pathname.lastIndexOf("/") + 1);
const dirname = pathname.slice(0, pathname.lastIndexOf("/"));

const renderDetails = async () => {
  const res = await fetch("http://localhost:3000/posts/" + id);
  if (!res.ok) {
    window.location.replace(`${dirname}/index.html`);
  }
  const post = await res.json();

  const template = `
    <h1>${post.title}</h1>
    <p>${post.body}</p>
  `;

  container.innerHTML = template;
};

deleteBtn.addEventListener("click", async () => {
  const res = await fetch("http://localhost:3000/posts/" + id, {
    method: "DELETE",
  });
  window.location.replace(`${dirname}/index.html`);
});

window.addEventListener("DOMContentLoaded", renderDetails);
```

</details>

<details>
  <summary>26. JSON Server - Search for Posts Keywords</summary>

index.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>JSON Server</title>
  </head>
  <body>
    <nav>
      <h1>All Blogs</h1>
      <a href="/Cloud/Json-Server/create.html">Add a new blog</a>
    </nav>

    <form class="search">
      <input type="text" placeholder="search term" name="term" />
    </form>

    <div class="blogs">
      <!-- inject blogs here from js -->
    </div>

    <script src="js/index.js"></script>
  </body>
</html>
```

js/index.js:

```Javascript
// javascript for index.html
const container = document.querySelector('.blogs');
const searchForm = document.querySelector('.search');

const pathname = window.location.pathname;
const filename = pathname.slice(pathname.lastIndexOf('/') + 1);
const dirname = pathname.slice(0, pathname.lastIndexOf('/'));

const renderPosts = async (term) => {
  let uri = 'http://localhost:3000/posts?_sort=likes&_order=desc';
  if (term) {
    uri += `&q=${term}`
  }

  const res = await fetch(uri);
  const posts = await res.json();

  let template = '';
  posts.forEach(post => {
    template += `
      <div class="post">
        <h2>${post.title}</h2>
        <p><small>${post.likes} likes</small></p>
        <p>${post.body.slice(0, 200)}...</p>
        <a href="${dirname}/details.html?id=${post.id}">Read more</a>
      </div>
    `
  });

  container.innerHTML = template;
}

// search
searchForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  renderPosts(searchForm.term.value.trim());
})

window.addEventListener('DOMContentLoaded', () => renderPosts());
```

</details>

+BUILDING REST API FOR BLOG

<details>
  <summary>27. Using JSON Server for REST API</summary>

data/db.json:

```json
{
  "blogs": [
    {
      "title": "My First Blog",
      "body": "Why do we use it?\nIt is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
      "author": "mario",
      "id": 1
    },
    {
      "title": "Opening Party!",
      "body": "Why do we use it?\nIt is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
      "author": "yoshi",
      "id": 2
    }
  ]
}
```

Run JSON Server:

```bash
json-server --watch data/db.json --port 8000
```

API Endpoints:

```bash
/blogs        GET     Fetch all blogs
/blogs/{id}   GET     Fetch a single blog
/blogs        POST    Add a new blog
/blogs/{id}   DELETE  Delete a blog
```

</details>

<details>
  <summary>28. Fetch All Blogs with UseEffect</summary>

Home.js:

```javascript
import { useEffect, useState } from "react";
import BlogList from "./BlogList";

const Home = () => {
  const [blogs, setBlogs] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/blogs")
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setBlogs(data);
      });
  }, []);

  return (
    <div className="home">
      {blogs && <BlogList blogs={blogs} title="All Blogs!" />}
    </div>
  );
};

export default Home;
```

BlogList.js:

```javascript
import React from "react";

const BlogList = ({ blogs, title }) => {
  return (
    <div className="blog-list">
      <h2>{title}</h2>
      {blogs.map((blog) => (
        <div className="blog-preview" key={blog.id}>
          <h2>{blog.title}</h2>
          <p>Written by {blog.author}</p>
        </div>
      ))}
    </div>
  );
};

export default BlogList;
```

</details>

<details>
  <summary>29. Set Loading Delay Message</summary>

Home.js:

```javascript
import { useEffect, useState } from "react";
import BlogList from "./BlogList";

const Home = () => {
  const [blogs, setBlogs] = useState(null);
  const [isPending, setIsPending] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      fetch("http://localhost:8000/blogs")
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          setIsPending(false);
          setBlogs(data);
        });
    }, 1000);
  }, []);

  return (
    <div className="home">
      {isPending && <div>Loading...</div>}
      {blogs && <BlogList blogs={blogs} title="All Blogs!" />}
    </div>
  );
};

export default Home;
```

</details>

<details>
  <summary>30. Catching Fetch Errors</summary>

Home.js:

```javascript
import { useEffect, useState } from "react";
import BlogList from "./BlogList";

const Home = () => {
  const [blogs, setBlogs] = useState(null);
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setTimeout(() => {
      fetch("http://localhost:8000/blogs")
        .then((res) => {
          if (!res.ok) {
            // error coming back from server
            throw Error("could not fetch the data for that resource");
          }
          return res.json();
        })
        .then((data) => {
          setIsPending(false);
          setBlogs(data);
          setError(null);
        })
        .catch((err) => {
          // auto catches network / connection error
          setIsPending(false);
          setError(err.message);
          setBlogs(null);
        });
    }, 1000);
  }, []);

  return (
    <div className="home">
      {error && <div>{error}</div>}
      {isPending && <div>Loading...</div>}
      {blogs && <BlogList blogs={blogs} title="All Blogs!" />}
    </div>
  );
};

export default Home;
```

</details>

<details>
  <summary>31. Creating Custom Hooks</summary>

Home.js:

```Javascript
import BlogList from "./BlogList";
import useFetch from "./useFetch";

const Home = () => {
    const { error, isPending, data: blogs } = useFetch('http://localhost:8000/blogs');

    return (
        <div className="home">
        { error && <div>{ error }</div> }
        { isPending && <div>Loading...</div> }
        {blogs && <BlogList blogs={blogs} title="All Blogs!" />}
        </div>
    );
}

export default Home;

```

useFetch.js:

```javascript
import { useState, useEffect } from "react";

const useFetch = (url) => {
  const [data, setData] = useState(null);
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setTimeout(() => {
      fetch(url)
        .then((res) => {
          if (!res.ok) {
            // error coming back from server
            throw Error("could not fetch the data for that resource");
          }
          return res.json();
        })
        .then((data) => {
          setIsPending(false);
          setData(data);
          setError(null);
        })
        .catch((err) => {
          // auto catches network / connection error
          setIsPending(false);
          setError(err.message);
          setData(null);
        });
    }, 1000);
  }, [url]);

  return { data, isPending, error };
};

export default useFetch;
```

</details>

<details>
  <summary>32. Using React Router for Routes</summary>

Install React Router:

```bash
npm install react-router-dom@5
```

Import BrowserRouter:

App.js:

```Javascript
import Navbar from './components/Navbar';
import Home from './components/Home';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Switch>
            <Route path="/">
              <Home />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
```

</details>

<details>
  <summary>33. Create Route for Create Page</summary>

App.js:

```Javascript
import Navbar from './components/Navbar';
import Home from './components/Home';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Create from './components/Create';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route path="/create">
              <Create />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
```

Create.js:

```Javascript
const Create = () => {
        return (
        <div className="create">
            <h2>Add a New Blog</h2>
        </div>
        );
    }

export default Create;
```

</details>

<details>
  <summary>34. Using Route Links</summary>

Navbar.js:

```Javascript
import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <nav className="navbar">
          <h1>The Dojo Blog</h1>
          <div className="links">
            <Link to="/">Home</Link>
            <Link to="/create" style={{
              color: 'white',
              backgroundColor: '#f1356d',
              borderRadius: '8px'
            }}>New Blog</Link>
          </div>
        </nav>
    );
}

export default Navbar;
```

</details>

<details>
  <summary>35. UseEffect Cleanup using Abort Controller</summary>

useEffect.js:

```Javascript
import { useState, useEffect } from 'react';

const useFetch = (url) => {
    const [data, setData] = useState(null);
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const abortCont = new AbortController();

        setTimeout(() => {
            fetch(url, { signal: abortCont.signal })
                .then(res => {
                    if (!res.ok) { // error coming back from server
                        throw Error('could not fetch the data for that resource');
                    }
                    return res.json();
                })
                .then(data => {
                    setIsPending(false);
                    setData(data);
                    setError(null);
                })
                .catch(err => {
                    if (err.name === 'AbortError') {
                        console.log('fetch aborted')
                    } else {
                        // auto catches network / connection error
                        setIsPending(false);
                        setError(err.message);
                        setData(null);
                    }
                })
        }, 1000);

        // abort the fetch
        return () => abortCont.abort();
    }, [url])

    return { data, isPending, error };
}

export default useFetch;
```

Index.js:

```Javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  //<React.StrictMode>
    <App />
  //</React.StrictMode>
);

```

</details>

<details>
  <summary>36. Using Route Parameters for Blog Details Page</summary>

BlogDetails.js:

```Javascript
import { useParams } from "react-router-dom";

const BlogDetails = () => {
  const { id } = useParams();

  return (
    <div className="blog-details">
      <h2>Blog details - { id }</h2>
    </div>
  );
}

export default BlogDetails;

```

App.js:

```Javascript
import Navbar from './components/Navbar';
import Home from './components/Home';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Create from './components/Create';
import BlogDetails from './components/BlogDetails';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route path="/create">
              <Create />
            </Route>
            <Route path="/blogs/:id">
              <BlogDetails />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;

```

BlogList.js:

```Javascript
import { Link } from 'react-router-dom';

const BlogList = ({ blogs }) => {
    return (
        <div className="blog-list">
        {blogs.map(blog => (
            <div className="blog-preview" key={blog.id} >
            <Link to={`/blogs/${blog.id}`}>
                <h2>{ blog.title }</h2>
                <p>Written by { blog.author }</p>
            </Link>
            </div>
        ))}
        </div>
    );
}

export default BlogList;
```

Index.css:

```CSS
.blog-preview a{
  text-decoration: none;
}
```

</details>

<details>
  <summary>37. Reusing Custom Hooks for BlogDetails Page</summary>

BlogDetails.js:

```Javascript
import { useParams } from "react-router-dom";
import useFetch from "./useFetch";

const BlogDetails = () => {
    const { id } = useParams();
    const { data: blog, error, isPending } = useFetch('http://localhost:8000/blogs/' + id);

    return (
        <div className="blog-details">
        { isPending && <div>Loading...</div> }
        { error && <div>{ error }</div> }
        { blog && (
            <article>
            <h2>{ blog.title }</h2>
            <p>Written by { blog.author }</p>
            <div>{ blog.body }</div>
            </article>
        )}
        </div>
    );
}

export default BlogDetails;
```

index.css:

```CSS
/* blog details page */
.blog-details h2 {
  font-size: 20px;
  color: #f1356d;
  margin-bottom: 10px;
}
.blog-details div {
  margin: 20px 0;
}

.blog-details button {
  background: #f1356d;
  color: #fff;
  border: 0;
  padding: 8px;
  border-radius: 8px;
  cursor: pointer;
}

```

</details>

<details>
  <summary>38. Using Controlled Form Inputs for Create Page</summary>

Create.js:

```Javascript
import { useState } from "react";

const Create = () => {
    const [title, setTitle] = useState('');
    const [body, setBody] = useState('');
    const [author, setAuthor] = useState('mario');

    return (
            <div className="create">
              <h2>Add a New Blog</h2>
              <form>
                  <label>Blog title:</label>
                  <input
                  type="text"
                  required
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  />
                  <label>Blog body:</label>
                  <textarea
                  required
                  value={body}
                  onChange={(e) => setBody(e.target.value)}
                  ></textarea>
                  <label>Blog author:</label>
                  <select
                  value={author}
                  onChange={(e) => setAuthor(e.target.value)}
                  >
                  <option value="mario">mario</option>
                  <option value="yoshi">yoshi</option>
                  </select>
                  <button>Add Blog</button>
              </form>
            </div>
    );
}

export default Create;
```

index.css:

```css
/* create new blog form */
.create {
  max-width: 400px;
  margin: 0 auto;
  text-align: center;
}
.create label {
  text-align: left;
  display: block;
}
.create h2 {
  font-size: 20px;
  color: #f1356d;
  margin-bottom: 30px;
}
.create input,
.create textarea,
.create select {
  width: 100%;
  padding: 6px 10px;
  margin: 10px 0;
  border: 1px solid #ddd;
  box-sizing: border-box;
  display: block;
}
.create button {
  background: #f1356d;
  color: #fff;
  border: 0;
  padding: 8px;
  border-radius: 8px;
  cursor: pointer;
}
```

</details>

<details>
  <summary>39. Submitting Form Events</summary>

Create.js:

```Javascript
import { useState } from "react";

const Create = () => {
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const [author, setAuthor] = useState('mario');

  const handleSubmit = (e) => {
    e.preventDefault();
    const blog = { title, body, author };

    console.log(blog);
  }

  return (
    <div className="create">
      <h2>Add a New Blog</h2>
      <form onSubmit={handleSubmit}>
        <label>Blog title:</label>
        <input
          type="text"
          required
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <label>Blog body:</label>
        <textarea
          required
          value={body}
          onChange={(e) => setBody(e.target.value)}
        ></textarea>
        <label>Blog author:</label>
        <select
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
        >
          <option value="mario">mario</option>
          <option value="yoshi">yoshi</option>
        </select>
        <button>Add Blog</button>
      </form>
    </div>
  );
}

export default Create;
```

</details>

<details>
  <summary>40. Creating Post Request for Create Page</summary>

Create.js:

```Javascript
import { useState } from "react";

const Create = () => {
    const [title, setTitle] = useState('');
    const [body, setBody] = useState('');
    const [author, setAuthor] = useState('mario');
    const [isPending, setIsPending] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        const blog = { title, body, author };

        setIsPending(true);

        fetch('http://localhost:8000/blogs/', {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(blog)
        }).then(() => {
        console.log('new blog added');
        setIsPending(false);
        })
    }

    return (
        <div className="create">
        <h2>Add a New Blog</h2>
        <form onSubmit={handleSubmit}>
            <label>Blog title:</label>
            <input
            type="text"
            required
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            />
            <label>Blog body:</label>
            <textarea
            required
            value={body}
            onChange={(e) => setBody(e.target.value)}
            ></textarea>
            <label>Blog author:</label>
            <select
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            >
            <option value="mario">mario</option>
            <option value="yoshi">yoshi</option>
            </select>
            {!isPending ? <button>Add Blog</button> : <button disabled>Adding Blog...</button>}
        </form>
        </div>
    );
}

export default Create;
```

</details>

<details>
  <summary>41. Redirecting with useHistory()</summary>

Create.js:

```Javascript
import { useState } from "react";
import { useHistory } from "react-router-dom";

const Create = () => {
    const [title, setTitle] = useState('');
    const [body, setBody] = useState('');
    const [author, setAuthor] = useState('mario');
    const history = useHistory();

    const handleSubmit = (e) => {
        e.preventDefault();
        const blog = { title, body, author };

        fetch('http://localhost:8000/blogs/', {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(blog)
        }).then(() => {
        // history.go(-1);
        history.push('/');
        })
    }

    return (
        <div className="create">
        <h2>Add a New Blog</h2>
        <form onSubmit={handleSubmit}>
            <label>Blog title:</label>
            <input
            type="text"
            required
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            />
            <label>Blog body:</label>
            <textarea
            required
            value={body}
            onChange={(e) => setBody(e.target.value)}
            ></textarea>
            <label>Blog author:</label>
            <select
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            >
            <option value="mario">mario</option>
            <option value="yoshi">yoshi</option>
            </select>
            <button>Add Blog</button>
        </form>
        </div>
    );
}

export default Create;
```

</details>

<details>
  <summary>42. Deleting Blogs</summary>

BlogDetails.js:

```Javascript
import { useHistory, useParams } from "react-router-dom";
import useFetch from "./useFetch";

const BlogDetails = () => {
    const { id } = useParams();
    const { data: blog, error, isPending } = useFetch('http://localhost:8000/blogs/' + id);
    const history = useHistory();

    const handleClick = () => {
        fetch('http://localhost:8000/blogs/' + blog.id, {
        method: 'DELETE'
        }).then(() => {
        history.push('/');
        })
    }

    return (
        <div className="blog-details">
        { isPending && <div>Loading...</div> }
        { error && <div>{ error }</div> }
        { blog && (
            <article>
            <h2>{ blog.title }</h2>
            <p>Written by { blog.author }</p>
            <div>{ blog.body }</div>
            <button onClick={handleClick}>delete</button>
            </article>
        )}
        </div>
    );
}

export default BlogDetails;
```

Index.css:

```css
.blog-details button {
  background: #f1356d;
  color: #fff;
  border: 0;
  padding: 8px;
  border-radius: 8px;
  cursor: pointer;
}
```

</details>

<details>
  <summary>43. Redirect to 404 Page</summary>

NotFound.js:

```Javascript
import { Link } from "react-router-dom"

const NotFound = () => {
    return (
        <div className="not-found">
        <h2>Sorry</h2>
        <p>That page cannot be found</p>
        <Link to="/">Back to the homepage...</Link>
        </div>
    );
}

export default NotFound;

```

App.js:

```Javascript
import Navbar from './components/Navbar';
import Home from './components/Home';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Create from './components/Create';
import BlogDetails from './components/BlogDetails';
import NotFound from './components/NotFound';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route path="/create">
              <Create />
            </Route>
            <Route path="/blogs/:id">
              <BlogDetails />
            </Route>
            <Route path="*">
              <NotFound />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
```

</details>


# NODE

+INTRODUCTION

<details>
  <summary>1. Check for Node Version</summary>

```Javascript
node -v
```

</details>

<details>
  <summary>2. Run Node File</summary>

```Javascript
node index.js
```

</details>

<details>
  <summary>3. The Global Object</summary>

Test.js:

```Javascript
let count = 0

const program = global.setInterval(()=>{
    count++
    console.log(count)
}, 1000)

global.setTimeout(()=>{
    console.log("Setting timeout")
    clearInterval(program)
}, 3000)
```

Absolute Path

```Javascript
console.log(__dirname)
```

```Javascript
// ~/Desktop/SERVER/Cloud/node
```

Absolute Path + Filename

```Javascript
console.log(__filename)
```

```Javascript
// ~/Desktop/SERVER/Cloud/node/test.js
```

</details>

<details>
  <summary>4. Modules and Require</summary>

require.js:

```Javascript
const people = ['yoshi' , 'ryu', ' chun-li' , ' mario'];
const ages = [20, 25, 30, 35];

module.exports = {
    people,
    ages
};

```

modules.js:

```Javascript
const {people, ages} = require('./require.js');

console.log(people, ages);
```

```Javascript
// [ 'yoshi', 'ryu', ' chun-li', ' mario' ] [ 20, 25, 30, 35 ]
```

</details>

<details>
  <summary>5. OS module</summary>

```Javascript
const os = require('os');

console.log(os.platform(), os.homedir());

```

```Javascript
// darwin /Users/ifeanyiomeata
```

</details>

<details>
  <summary>6. Reading Files</summary>

```Javascript
const fs = require("fs");

// reading files
fs.readFile('./docs/blog1.txt', (err, data) => {
    if(err){
    console.log(err);
    }
    console.log(data.toString());
});

console.log('last line');
```

```Javascript
// last line
// Hello World!
// Hello World 2!
```

</details>

<details>
  <summary>7. Writing Files</summary>

```Javascript
const fs = require("fs");

// writing files
fs.writeFile('./docs/blog1.txt', 'hello, world', () => {
    console.log('file was written');
});
fs.writeFile('./docs/blog2.txt', 'hello, again' , () => {
    console.log('file was written');
});
```

```Javascript
// file was written
// file was written
```

</details>

<details>
  <summary>8. Create and Delete Folder/Directory</summary>

```Javascript
const fs = require("fs");

// Create and Delete directories/Folders
if(!fs.existsSync('./assets')) {
    fs.mkdir('./assets', (err) => {
        if (err) {
            console.error(err);
        }
        console.log('folder created');
    });
} else {
    fs.rmdir('./assets', (err) => {
        if(err) {
            console.log(err)
        }
        console.log('folder deleted');
    })
}
```

```Javascript
// folder created
// folder deleted
```

</details>

<details>
  <summary>9. Delete Files</summary>

```Javascript
const fs = require("fs");

// deleting files
if (fs.existsSync('./docs/blog1.txt')) {
    fs.unlink('./docs/blog1.txt', (err) => {
        if(err) {
            console.log(err)
        }
        console.log('file deleted');
    })
}
```

```Javascript
// file deleted
```

</details>

<details>
  <summary>10. Read Stream</summary>

```Javascript
const fs = require("fs");

const readStream = fs.createReadStream('./docs/blog2.txt', { encoding: 'utf8' });

readStream.on('data', (chunk) => {
    console.log('-------- NEW CHUNK -----');
    console.log(chunk);
});

```

```Javascript
// -------- NEW CHUNK -----
// <Buffer 4c 6f 72 65 6d 20 69 70 73 75 6d 20 64 6f 6c 6f 72 20 73 69 74 20 61 6d 65 74 2c 20 63 6f 6e 73 65 63 74 65 74 75 65 72 20 61 64 69 70 69 73 63 69 6e ... 65486 more bytes>
// -------- NEW CHUNK -----
// <Buffer 20 56 69 76 61 6d 75 73 20 69 6e 20 65 72 61 74 20 75 74 20 75 72 6e 61 20 63 75 72 73 75 73 20 76 65 73 74 69 62 75 6c 75 6d 2e 20 46 75 73 63 65 20 ... 65486 more bytes>
// -------- NEW CHUNK -----
// <Buffer 53 75 73 70 65 6e 64 69 73 73 65 20 66 65 75 67 69 61 74 2e 20 53 75 73 70 65 6e 64 69 73 73 65 20 65 6e 69 6d 20 74 75 72 70 69 73 2c 20 64 69 63 74 ... 65486 more bytes>
// -------- NEW CHUNK -----
// <Buffer 69 62 75 6c 75 6d 20 65 74 2c 20 74 65 6d 70 6f 72 20 61 75 63 74 6f 72 2c 20 6a 75 73 74 6f 2e 20 49 6e 20 61 63 20 66 65 6c 69 73 20 71 75 69 73 20 ... 65486 more bytes>
// -------- NEW CHUNK -----
// <Buffer 6c 61 6d 63 6f 72 70 65 72 20 75 6c 74 72 69 63 69 65 73 20 6e 69 73 69 2e 20 4e 61 6d 20 65 67 65 74 20 64 75 69 2e 20 45 74 69 61 6d 20 72 68 6f 6e ... 11132 more bytes>
```

</details>

<details>
  <summary>11. Write Stream</summary>

```Javascript
const fs = require("fs");

const readStream = fs.createReadStream('./docs/blog2.txt',{ encoding: 'utf8' });
const writeStream = fs.createWriteStream('./docs/blog3.txt');

readStream.on('data' , (chunk) => {
    console.log('------ NEW CHUNK -----');
    console.log(chunk);
    writeStream.write('\nNEW CHUNK\n');
    writeStream.write(chunk);
});
```

</details>

<details>
  <summary>12. Piping</summary>

```Javascript
const fs = require("fs");

const readStream = fs.createReadStream('./docs/blog2.txt',{ encoding: 'utf8' });
const writeStream = fs.createWriteStream('./docs/blog3.txt');

// readStream.on('data' , (chunk) => {
//     console.log('------ NEW CHUNK -----');
//     console.log(chunk);
//     writeStream.write('\nNEW CHUNK\n');
//     writeStream.write(chunk);
// });

// piping
readStream.pipe(writeStream);
```

</details>

+REQUESTS & RESPONSES

<details>
  <summary>13. Create a Server</summary>

```Javascript
const http = require('http');

const server = http.createServer((req, res) =>{
    console.log('request made');
});

server.listen(3000, 'localhost', () => {
    console.log('listening for requests on port 3000')
})
```

```Javascript
// listening for requests on port 3000
// request made
```

</details>

<details>
  <summary>14. Get Request URL and Method</summary>

```Javascript

const http = require('http');

const server = http.createServer((req, res) =>{
    console.log('request made');
    console.log("Url: ", req.url);
    console.log("Method: ", req.method);
    console.log("Headers: ", req.headers);
    console.log("Body: ", req.body);
});

server.listen(3000, 'localhost', () => {
    console.log('listening for requests on port 3000')
})
```

```Javascript
// listening for requests on port 3000
// request made
// Url:  /
// Method:  GET
// Headers:  {
//   host: 'localhost:3000',
//   connection: 'keep-alive',
//   'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
//   'sec-ch-ua-mobile': '?0',
//   'sec-ch-ua-platform': '"macOS"',
//   'upgrade-insecure-requests': '1',
//   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
//   accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
//   'sec-fetch-site': 'none',
//   'sec-fetch-mode': 'navigate',
//   'sec-fetch-user': '?1',
//   'sec-fetch-dest': 'document',
//   'accept-encoding': 'gzip, deflate, br',
//   'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
// }
// Body:  undefined
```

</details>

<details>
  <summary>15. Response - Set Header Content Type </summary>

```Javascript

const http = require('http');

const server = http.createServer((req, res) => {
    console.log('request made');
    console.log("Url: ", req.url);
    console.log("Method: ", req.method);
    console.log("Headers: ", req.headers);
    console.log("Body: ", req.body);

    // set header content type
    res.setHeader('Content-Type', 'text/plain');
    res.write('hello, ninjas');
    res.end();
});

server.listen(3000, 'localhost', () => {
    console.log('listening for requests on port 3000')
})
```

```Javascript
const http = require('http');

const server = http.createServer((req, res) => {
    console.log('request made');
    // console.log("Url: ", req.url);
    // console.log("Method: ", req.method);
    // console.log("Headers: ", req.headers);
    // console.log("Body: ", req.body);

    // set header content type
    res.setHeader('Content-Type', 'text/html');
    res.write('<head><link rel="stylesheet" href="#"></head>');
    res.write('<h1>Welcome!</h1>');
    res.write('<h2>hello, ninjas</h2>');
    res.end();
});

server.listen(3000, 'localhost', () => {
    console.log('listening for requests on port 3000')
})
```

</details>

<details>
  <summary>16. Returning HTML Pages </summary>

```Javascript
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    console.log('request made');

    // set header content type
    res.setHeader('Content-Type', 'text/html');

    // send an html file.
    fs.readFile('./views/index.html', (err, data) => {
        if(err) {
            console.log(err);
            res.end();
        } else {
            res.write(data);
            res.end();
            // OR
            // res.end(data);
        }
    })

});

server.listen(3000, 'localhost', () => {
    console.log('listening for requests on port 3000')
})
```

</details>

<details>
  <summary>17. Routing HTML Pages</summary>

```Javascript
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    console.log('request made');

    // set header content type
    res.setHeader('Content-Type', 'text/html');

    // get path from request
    let path = './views/';
    switch (req.url) {
        case '/':
            path += 'index.html';
            break;
        case '/about':
            path += 'about.html';
            break;
        default:
            path += '404.html';
            break;
    }

    // send an html file.
    fs.readFile(path, (err, data) => {
        if(err) {
            console.log(err);
            res.end();
        } else {
            res.end(data);
        }
    })
});

server.listen(3000, 'localhost', () => {
    console.log('listening for requests on port 3000')
})
```

</details>

<details>
  <summary>18. Set Status Codes </summary>

Status codes describe the type of response sent to the browser.

```markdown
200- OK
301- Resource moved
404- Not found
500- Internal server error
```

```markdown
100 Range- Informational Responses
200 Range- Success codes
300 Range- Codes for redirects
400 Range- User or client error codes
500 Range- Server error codes
```

```Javascript
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    console.log('request made');

    // set header content type
    res.setHeader('Content-Type', 'text/html');

    // get path from request
    let path = './views/';
    switch (req.url) {
        case '/':
            path += 'index.html';
            res.statusCode = 200;
            break;
        case '/about':
            path += 'about.html';
            res.statusCode = 200;
            break;
        default:
            path += '404.html';
            res.statusCode = 404;
            break;
    }

    // send an html file.
    fs.readFile(path, (err, data) => {
        if(err) {
            console.log(err);
            res.end();
        } else {
            res.end(data);
        }
    })
});

server.listen(3000, 'localhost', () => {
    console.log('listening for requests on port 3000')
})
```

</details>

<details>
  <summary>19. HTTP Redirects</summary>

```Javascript

const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    console.log('request made');

    // set header content type
    res.setHeader('Content-Type', 'text/html');

    // get path from request
    let path = './views/';
    switch (req.url) {
        case '/':
            path += 'index.html';
            res.statusCode = 200;
            break;
        case '/about':
            path += 'about.html';
            res.statusCode = 200;
            break;
        case '/about-me':
            res.statusCode = 301;
            res.setHeader('Location', '/about');
            res.end();
            break;
        default:
            path += '404.html';
            res.statusCode = 404;
            break;
    }

    // send an html file.
    fs.readFile(path, (err, data) => {
        if(err) {
            console.log(err);
            res.end();
        } else {
            res.end(data);
        }
    })
});

server.listen(3000, 'localhost', () => {
    console.log('listening for requests on port 3000')
})
```

</details>

+NODE PACKAGE MANAGER (NPM)

<details>
  <summary>20. Install Nodemon </summary>

```Javascript
npm install -g nodemon

yarn global add nodemon
```

```Javascript
nodemon server
```

</details>

<details>
  <summary>21. Create Package.json dependencies locally </summary>

```Javascript
npm init
```

```Javascript
{
  "name": "node",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "directories": {
    "doc": "docs"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "author": "",
  "license": "ISC"
}

```

</details>

<details>
  <summary>22. Install Lodash</summary>

```Javascript
npm i --save lodash
```

package.json:

```Javascript
{
  "name": "node",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "directories": {
    "doc": "docs"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "lodash": "^4.17.21"
  }
}
```

package-lock.json:

```Javascript
{
  "name": "node",
  "version": "1.0.0",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "node",
      "version": "1.0.0",
      "license": "ISC",
      "dependencies": {
        "lodash": "^4.17.21"
      }
    },
    "node_modules/lodash": {
      "version": "4.17.21",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz",
      "integrity": "sha512-v2kDEe57lecTulaDIuNTPy3Ry4gLGJ6Z1O3vE1krgXZNrsQ+LFTGHVxVjcXPs17LhbZVGedAJv8XZ1tvj5FvSg=="
    }
  },
  "dependencies": {
    "lodash": {
      "version": "4.17.21",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz",
      "integrity": "sha512-v2kDEe57lecTulaDIuNTPy3Ry4gLGJ6Z1O3vE1krgXZNrsQ+LFTGHVxVjcXPs17LhbZVGedAJv8XZ1tvj5FvSg=="
    }
  }
}

```

</details>

<details>
  <summary>23. Install all dependencies in Package.json</summary>

```Javascript
npm install
```

</details>

+EXPRESS

<details>
  <summary>24. Express Introduction</summary>

```Javascript
// We can use express as shown as below
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
```

</details>

<details>
  <summary>25. Install Express</summary>

```Javascript
npm install express --save
```

```Javascript
{
  "name": "node",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "directories": {
    "doc": "docs"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2",
    "lodash": "^4.17.21"
  }
}
```

</details>

<details>
  <summary>26. Display Home Page</summary>

app.js:

```Javascript
const express = require('express');

// express app
const app = express();

// listen for requests
app.listen(3000);

// get home page
app.get('/', (req, res) => {
    res.send('<h1>Home page</h1>');
});
```

</details>

<details>
  <summary>27. Routing HTML Pages</summary>

app.js:

```Javascript
const express = require('express');
const path = require('path');

const homePage = path.join(__dirname, 'views/index.html')
const aboutPage = path.join(__dirname, 'views/about.html')
const _404Page = path.join(__dirname, 'views/404.html')

// express app
const app = express();

// listen for requests
app.listen(3000);

// get home page
app.get('/', (req, res) => {
    res.sendFile(homePage);
    // res.sendFile('./views/index.html' , { root: __dirname });
});

// get about page
app.get('/about', (req, res) => {
    res.sendFile(aboutPage);
    // res.sendFile('./views/about.html' , { root: __dirname });
});
```

</details>

<details>
  <summary>28. Create Nav Links</summary>

Index.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Node.js Crash Course</title>
  </head>
  <body>
    <nav>
      <a href="/"> Homepage </a>
      <a href="/about"> About page </a>
    </nav>
    <h1>Home</h1>
    <h2>Your path to becoming a Node.js ninja!</h2>
  </body>
</html>
```

about.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Node.js Crash Course</title>
  </head>
  <body>
    <nav>
      <a href="/"> Homepage </a>
      <a href="/about"> About page </a>
    </nav>
    <h1>About</h1>
    <h2>Your path to becoming a Node.js ninja!</h2>
  </body>
</html>
```

</details>

<details>
  <summary>29. Redirects & 404's</summary>

app.js:

```Javascript
const express = require('express');
const path = require('path');

const homePage = path.join(__dirname, 'views/index.html')
const aboutPage = path.join(__dirname, 'views/about.html')
const _404Page = path.join(__dirname, 'views/404.html')

// express app
const app = express();

// listen for requests
app.listen(3000);

// get home page
app.get('/', (req, res) => {
    res.sendFile(homePage);
});

// get about page
app.get('/about', (req, res) => {
    res.sendFile(aboutPage);
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// 404 page
app.use((req, res) => {
    res.status(404).sendFile(_404Page);
    // res.sendFile('./views/404.html', { root: __dirname });
});
```

</details>

+VIEW ENGINES

<details>
  <summary>30. Install EJS</summary>

```Javascript
npm install ejs
```

</details>

<details>
  <summary>31. EJS Sample</summary>

```Javascript
let ejs = require('ejs');
let people = ['geddy', 'neil', 'alex'];
let html = ejs.render('<%= people.join(", "); %>', {people: people});
```

```bash
ejs ./template_file.ejs -f data_file.json -o ./output.html
```

```html
<script src="ejs.js"></script>
<script>
  let people = ["geddy", "neil", "alex"];
  let html = ejs.render('<%= people.join(", "); %>', { people: people });
</script>
```

```html
<% if (user) { %>
<h2><%= user.name %></h2>
<% } %>
```

```Javascript
let template = ejs.compile(str, options);
template(data);
// => Rendered HTML string

ejs.render(str, data, options);
// => Rendered HTML string

ejs.renderFile(filename, data, options, function(err, str){
    // str => Rendered HTML string
});
```

</details>

<details>
  <summary>32. Create EJS Pages</summary>

Index.ejs:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width-device-width, initial-scale=1.0" />
    <title>Blog Ninja</title>
  </head>
  <body>
    <nav>
      <div class="site-title">
        <a href="/"><h1>Blog Ninja</h1></a>
        <p>A Net Ninja Site</p>
      </div>
      <ul>
        <li><a href="/">Blogs</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/blogs/create">New Blog</a></li>
      </ul>
    </nav>
    <div class="blogs content">
      <h2>All Blogs</h2>
    </div>
  </body>
</html>
```

About.ejs:

```Javascript
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Ninja</title>
</head>
<body>
    <nav>
        <div class="site-title">
            <a href="/"><h1>Blog Ninja</h1></a>
            <p>A Net Ninja Site</p>
        </div>
        <ul>
            <li><a href="/">Blogs</a></1li>
            <li><a href="/about">About</a></1li>
            <li><a href="/blogs/create">New Blog</a></1li>
        </ul>
    </nav>
    <div class="about content">
        <h2>About Us</h2>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quia quibusdam quaerat illo a </p>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quia quibusdam quaerat illo a </p>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quia quibusdam quaerat illo a </p>
    </div>
</body>
</html>

```

404.ejs:

```Javascript
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Ninja</title>
</head>
<body>
    <nav>
        <div class="site-title">
            <a href="/"><h1>Blog Ninja</h1></a>
            <p>A Net Ninja Site</p>
        </div>
        <ul>
            <li><a href="/">Blogs</a></1li>
            <li><a href="/about">About</a></1li>
            <li><a href="/blogs/create">New Blog</a></1li>
        </ul>
    </nav>
    <div class="not-found content">
        <h2>OOPS, page not found :)</h2>
    </div>
</body>
</html>

```

</details>

<details>
  <summary>33. Render EJS Template</summary>

```Javascript
const express = require('express');
const path = require('path');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');
// app.set('views', 'myviews');

// listen for requests
app.listen(3000);

// get home page
app.get('/', (req, res) => {
    //res.sendFile(homePage);
    res.render('index');
});

// get about page
app.get('/about', (req, res) => {
    res.render('about');
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404');
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

</details>

<details>
  <summary>34. Render Create Blog</summary>

app.js:

```Javascript
const express = require('express');
const path = require('path');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');
// app.set('views', 'myviews');

// listen for requests
app.listen(3000);

// get home page
app.get('/', (req, res) => {
    //res.sendFile(homePage);
    res.render('index');
});

// get about page
app.get('/about', (req, res) => {
    res.render('about');
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create');
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404');
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

create.ejs:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width-device-width, initial-scale=1.0" />
    <title>Blog Ninja</title>
  </head>
  <body>
    <nav>
      <div class="site-title">
        <a href="/"><h1>Blog Ninja</h1></a>
        <p>A Net Ninja Site</p>
      </div>
      <ul>
        <li><a href="/">Blogs</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/blogs/create">New Blog</a></li>
      </ul>
    </nav>

    <div class="create-blog content">
      <form>
        <label for="title">Blog Title:</label>
        <input type="text" id="title" name="title" required />
        <label for="snippet">Blog Snippet:</label>
        <input type="text" id="snippet" name="snippet" required />
        <label for="body">Blog Body:</label>
        <textarea id="body" name="body" required></textarea>
        <button type="submit">Submit</button>
      </form>
    </div>
  </body>
</html>
```

</details>

<details>
  <summary>35. Displaying Internal Dynamic content</summary>

```html
<div class="site-title">
  <a href="/"><h1>Blog Ninja</h1></a>
  <p>A Net Ninja Site</p>
  <% const firstName = 'Fred' %>
  <p>His First Name is <%= firstName %>.</p>
</div>
```

</details>

<details>
  <summary>36. Displaying Context Dynamic content</summary>

```Javascript
// get home page
app.get('/', (req, res) => {
    //res.sendFile(homePage);
    res.render('index', { title: 'Home' });
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Blog Ninja | <%= title %></title>
</head>
```

</details>

<details>
  <summary>37. Iterate through Blogs Array</summary>

```Javascript
const express = require('express');
const path = require('path');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');
// app.set('views', 'myviews');

// listen for requests
app.listen(3000);

// get home page
app.get('/', (req, res) => {
    const blogs = [
        { title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'How to defeat bowser', snippet: 'Lorem ipsum dolor sit amet consectetur' },
    ];
    res.render('index', { title: 'Home', blogs });
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width-device-width, initial-scale=1.0" />
    <title>Blog Ninja | <%= title %></title>
  </head>
  <body>
    <nav>
      <div class="site-title">
        <a href="/"><h1>Blog Ninja</h1></a>
        <p>A Net Ninja Site</p>
      </div>
      <ul>
        <li><a href="/">Blogs</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/blogs/create">New Blog</a></li>
      </ul>
    </nav>
    <div class="blogs content">
      <h2>All Blogs</h2>
      <% if(blogs.length > 0){ %> <% blogs.forEach(blog => { %>
      <div class="blog-preview">
        <h3 class="title">
          <a href="/blogs/<%= blog._id %>"><%= blog.title %></a>
        </h3>
        <p class="author">Written by <%= blog.author %></p>
        <p class="snippet"><%= blog.snippet %></p>
      </div>
      <% }) %> <% }else{ %>
      <p>No blogs to show</p>
      <% } %>
    </div>
  </body>
</html>
```

</details>

<details>
  <summary>38. Include Partials</summary>

Index.ejs:

```html
<html lang="en">
  <%- include('./partials/head.ejs') %>
  <body>
    <%- include('./partials/nav.ejs') %>
    <div class="blogs content">
      <h2>All Blogs</h2>
      <% if(blogs.length > 0){ %> <% blogs.forEach(blog => { %>
      <div class="blog-preview">
        <h3 class="title">
          <a href="/blogs/<%= blog._id %>"><%= blog.title %></a>
        </h3>
        <p class="author">Written by <%= blog.author %></p>
        <p class="snippet"><%= blog.snippet %></p>
      </div>
      <% }) %> <% }else{ %>
      <p>No blogs to show</p>
      <% } %>
    </div>
    <%- include('./partials/footer.ejs') %>
  </body>
</html>
```

Nav.ejs:

```html
<nav>
  <div class="site-title">
    <a href="/"><h1>Blog Ninja</h1></a>
    <p>A Net Ninja Site</p>
  </div>
  <ul>
    <li><a href="/">Blogs</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/blogs/create">New Blog</a></li>
  </ul>
</nav>
```

Head.ejs:

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width-device-width, initial-scale=1.0" />
  <title>Blog Ninja | <%= title %></title>
</head>
```

Footer.ejs:

```html
<footer>Copyright &copy; 2022</footer>
```

</details>

<details>
  <summary>39. Styling Head</summary>

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Blog Ninja | <%= title %></title>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Noto+Serif:wght@400;700&display=swap");
    body {
      max-width: 1200px;
      margin: 20px auto;
      padding: 0 20px;
      font-family: "Noto Serif", serif;
      max-width: 1200px;
    }
    p,
    h1,
    h2,
    h3,
    a,
    ul {
      margin: 0;
      padding: 0;
      text-decoration: none;
      color: #222;
    }

    /* nav & footer styles */
    nav {
      display: flex;
      justify-content: space-between;
      margin-bottom: 60px;
      padding-bottom: 10px;
      border-bottom: 1px solid #ddd;
      text-transform: uppercase;
    }
    nav ul {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    nav li {
      list-style-type: none;
      margin-left: 20px;
    }
    nav h1 {
      font-size: 3em;
    }
    nav p,
    nav a {
      color: #777;
      font-weight: 300;
    }
    footer {
      color: #777;
      text-align: center;
      margin: 80px auto 20px;
    }
    h2 {
      margin-bottom: 40px;
    }
    h3 {
      text-transform: capitalize;
      margin-bottom: 8px;
    }
    .content {
      margin-left: 20px;
    }

    /* index styles */

    /* details styles */

    /* create styles */
    .create-blog form {
      max-width: 400px;
      margin: 0 auto;
    }
    .create-blog input,
    .create-blog textarea {
      display: block;
      width: 100%;
      margin: 10px 0;
      padding: 8px;
    }
    .create-blog label {
      display: block;
      margin-top: 24px;
    }
    textarea {
      height: 120px;
    }
    .create-blog button {
      margin-top: 20px;
      background: crimson;
      color: white;
      padding: 6px;
      border: 0;
      font-size: 1.2em;
      cursor: pointer;
    }
  </style>
</head>
```

</details>

+MIDDLEWARES

<details>
  <summary>40. Create Middleware</summary>

```Javascript
// middleware
app.use((req, res, next) => {
    console.log('new request made:');
    console.log('host: ', req.hostname);
    console.log('path: ', req.path);
    console.log('method: ', req.method);
    next();
});
```

```markdown
new request made:
host: localhost
path: /
method: GET
```

```Javascript
const express = require('express');
const path = require('path');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');
// app.set('views', 'myviews');

// listen for requests
app.listen(3000);

// middleware
app.use((req, res, next) => {
    console.log('new request made:');
    console.log('host: ', req.hostname);
    console.log('path: ', req.path);
    console.log('method: ', req.method);
    next();
});

// get home page
app.get('/', (req, res) => {
    const blogs = [
        { title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'How to defeat bowser', snippet: 'Lorem ipsum dolor sit amet consectetur' },
    ];
    res.render('index', { title: 'Home', blogs });
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

</details>

<details>
  <summary>41. Use Morgan Middleware</summary>

```markdown
npm install morgan --save
```

Index.ejs:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');
// app.set('views', 'myviews');

// listen for requests
app.listen(3000);

// middleware
app.use((req, res, next) => {
    console.log('new request made:');
    console.log('host: ', req.hostname);
    console.log('path: ', req.path);
    console.log('method: ', req.method);
    next();
});

app.use(morgan('dev'));

// get home page
app.get('/', (req, res) => {
    const blogs = [
        { title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'How to defeat bowser', snippet: 'Lorem ipsum dolor sit amet consectetur' },
    ];
    res.render('index', { title: 'Home', blogs });
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

```markdown
new request made:
host: localhost
path: /
method: GET
GET / 304 19.124 ms - -
```

</details>

<details>
  <summary>42. Use Style.css Static File</summary>

```Javascript
// static files
app.use(express.static('public'));
```

app.js:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');
// app.set('views', 'myviews');

// listen for requests
app.listen(3000);

// middleware
app.use((req, res, next) => {
    console.log('new request made:');
    console.log('host: ', req.hostname);
    console.log('path: ', req.path);
    console.log('method: ', req.method);
    next();
});

app.use(morgan('dev'));

// static files
app.use(express.static('public'));

// get home page
app.get('/', (req, res) => {
    const blogs = [
        { title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'How to defeat bowser', snippet: 'Lorem ipsum dolor sit amet consectetur' },
    ];
    res.render('index', { title: 'Home', blogs });
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

head.ejs:

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Blog Ninja | <%= title %></title>
  <link rel="stylesheet" href="/styles.css" />
</head>
```

public/styles.css:

```Javascript
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif:wght@400;700&display=swap');
      body{
        max-width: 1200px;
        margin: 20px auto;
        padding: 0 20px;
        font-family: 'Noto Serif', serif;
        max-width: 1200px;
      }
      p, h1, h2, h3, a, ul{
        margin: 0;
        padding: 0;
        text-decoration: none;
        color: #222;
      }

      /* nav & footer styles */
      nav{
        display: flex;
        justify-content: space-between;
        margin-bottom: 60px;
        padding-bottom: 10px;
        border-bottom: 1px solid #ddd;
        text-transform: uppercase;
      }
      nav ul{
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
      }
      nav li{
        list-style-type: none;
        margin-left: 20px;
      }
      nav h1{
        font-size: 3em;
      }
      nav p, nav a{
        color: #777;
        font-weight: 300;
      }
      footer{
        color: #777;
        text-align: center;
        margin: 80px auto 20px;
      }
      h2{
        margin-bottom: 40px;
      }
      h3{
        text-transform: capitalize;
        margin-bottom: 8px;
      }
      .content{
        margin-left: 20px;
      }

      /* index styles */

      /* details styles */

      /* create styles */
      .create-blog form{
        max-width: 400px;
        margin: 0 auto;
      }
      .create-blog input,
      .create-blog textarea{
        display: block;
        width: 100%;
        margin: 10px 0;
        padding: 8px;
      }
      .create-blog label{
        display: block;
        margin-top: 24px;
      }
      textarea{
        height: 120px;
      }
      .create-blog button{
        margin-top: 20px;
        background: crimson;
        color: white;
        padding: 6px;
        border: 0;
        font-size: 1.2em;
        cursor: pointer;
      }
```

</details>

+MONGODB

<details>
  <summary>43. Connect to MongoDB</summary>

```markdown
Mongodb Atlas
https://www.mongodb.com/cloud/atlas
```

```Javascript
const dbURI = 'mongodb+srv://admin:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority';
```

```Javascript
const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });
client.connect(err => {
  const collection = client.db("test").collection("devices");
  // perform actions on the collection object
  client.close();
});
```

</details>

<details>
  <summary>44. Connect with Mongoose</summary>

```markdown
npm install mongoose --save
```

```Javascript
const mongoose = require('mongoose');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));
```

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');
// app.set('views', 'myviews');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// middleware
app.use((req, res, next) => {
    console.log('new request made:');
    console.log('host: ', req.hostname);
    console.log('path: ', req.path);
    console.log('method: ', req.method);
    next();
});

app.use(morgan('dev'));

// static files
app.use(express.static('public'));

// get home page
app.get('/', (req, res) => {
    const blogs = [
        { title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'How to defeat bowser', snippet: 'Lorem ipsum dolor sit amet consectetur' },
    ];
    res.render('index', { title: 'Home', blogs });
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

```Javascript
// connected to db
```

</details>

<details>
  <summary>45. Create Database Model and Schema</summary>

models/blog.js:

```Javascript
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const blogSchema = new Schema({
    title: {
        type: String,
        required: true
    },
    snippet: {
        type: String,
        required: true
    },
    body: {
        type: String,
        required: true
    }
}, { timestamps: true });

const Blog = mongoose.model('Blog', blogSchema);
module.exports = Blog;
```

</details>

<details>
  <summary>46. Saving a Single Blog</summary>

```Javascript
const Blog = require('./models/blog');

// mongoose sandbox routes
app.get('/add-blog', (req, res) => {
    const blog = new Blog({
        title: 'new blog 2',
        snippet: 'about my new blog',
        body: 'more about my new blog'
    });

    blog.save()
        .then((result) => {
            res.send(result);
        })
        .catch((err) => {
            console.log(err);
        });
});
```

app.js:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');
const Blog = require('./models/blog');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');
// app.set('views', 'myviews');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// static files
app.use(express.static('public'));

// mongoose sandbox routes
app.get('/add-blog', (req, res) => {
    const blog = new Blog({
        title: 'new blog 2',
        snippet: 'about my new blog',
        body: 'more about my new blog'
    });

    blog.save()
        .then((result) => {
            res.send(result);
        })
        .catch((err) => {
            console.log(err);
        });
});

// get home page
app.get('/', (req, res) => {
    const blogs = [
        { title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'How to defeat bowser', snippet: 'Lorem ipsum dolor sit amet consectetur' },
    ];
    res.render('index', { title: 'Home', blogs });
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

```Javascript
// {
// "title": "new blog 2",
// "snippet": "about my new blog",
// "body": "more about my new blog",
// "_id": "635bd60ce18a55b9822dc59a",
// "createdAt": "2022-10-28T13:15:56.807Z",
// "updatedAt": "2022-10-28T13:15:56.807Z",
// "__v": 0
// }
```

</details>

<details>
  <summary>47. Get all Blogs</summary>

```Javascript
//get all blogs
app.get('/all-blogs', (req, res) => {
    Blog.find()
        .then((result) => {
            res.send(result);
        })
        .catch((err) => {
            console.log(err);
        });
});

```

app.js:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');
const Blog = require('./models/blog');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');
// app.set('views', 'myviews');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// static files
app.use(express.static('public'));

// mongoose sandbox routes
// add blog
app.get('/add-blog', (req, res) => {
    const blog = new Blog({
        title: 'new blog 2',
        snippet: 'about my new blog',
        body: 'more about my new blog'
    });

    blog.save()
        .then((result) => {
            res.send(result);
        })
        .catch((err) => {
            console.log(err);
        });
});

//get all blogs
app.get('/all-blogs', (req, res) => {
    Blog.find()
        .then((result) => {
            res.send(result);
        })
        .catch((err) => {
            console.log(err);
        });
});

// get home page
app.get('/', (req, res) => {
    const blogs = [
        { title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'How to defeat bowser', snippet: 'Lorem ipsum dolor sit amet consectetur' },
    ];
    res.render('index', { title: 'Home', blogs });
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

```Javascript
// [
//   {
//   "_id": "635bd60ce18a55b9822dc59a",
//   "title": "new blog 2",
//   "snippet": "about my new blog",
//   "body": "more about my new blog",
//   "createdAt": "2022-10-28T13:15:56.807Z",
//   "updatedAt": "2022-10-28T13:15:56.807Z",
//   "__v": 0
//   },
//   {
//   "_id": "635bd7cfe18a55b9822dc59c",
//   "title": "new blog 2",
//   "snippet": "about my new blog",
//   "body": "more about my new blog",
//   "createdAt": "2022-10-28T13:23:27.292Z",
//   "updatedAt": "2022-10-28T13:23:27.292Z",
//   "__v": 0
//   }
// ]
```

</details>

<details>
  <summary>48. Get a Single Blog</summary>

```Javascript
//get single blog
app.get('/single-blog', (req, res) => {
    Blog.findById('635bd60ce18a55b9822dc59a')
        .then((result) => {
            res.send(result);
        })
        .catch((err) => {
            console.log(err);
        });
});
```

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');
const Blog = require('./models/blog');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');
// app.set('views', 'myviews');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// static files
app.use(express.static('public'));

// mongoose sandbox routes
// add blog
app.get('/add-blog', (req, res) => {
    const blog = new Blog({
        title: 'new blog 2',
        snippet: 'about my new blog',
        body: 'more about my new blog'
    });

    blog.save()
        .then((result) => {
            res.send(result);
        })
        .catch((err) => {
            console.log(err);
        });
});

//get all blogs
app.get('/all-blogs', (req, res) => {
    Blog.find()
        .then((result) => {
            res.send(result);
        })
        .catch((err) => {
            console.log(err);
        });
});

//get single blog
app.get('/single-blog', (req, res) => {
    Blog.findById('635bd60ce18a55b9822dc59a')
        .then((result) => {
            res.send(result);
        })
        .catch((err) => {
            console.log(err);
        });
});

// get home page
app.get('/', (req, res) => {
    const blogs = [
        { title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur' },
        { title: 'How to defeat bowser', snippet: 'Lorem ipsum dolor sit amet consectetur' },
    ];
    res.render('index', { title: 'Home', blogs });
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// redirects
app.get('/about-us' , (req, res) => {
    res.redirect('/about');
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

```Javascript
// {
// "_id": "635bd60ce18a55b9822dc59a",
// "title": "new blog 2",
// "snippet": "about my new blog",
// "body": "more about my new blog",
// "createdAt": "2022-10-28T13:15:56.807Z",
// "updatedAt": "2022-10-28T13:15:56.807Z",
// "__v": 0
// }
```

</details>

+REQUESTS

<details>
  <summary>49. List of Requests</summary>

```Javascript
// localhost:3000/blogs        -----> GET (Get a list of blogs)
// localhost:3000/blogs/create -----> GET (Render a form to create a new blog)
// localhost:3000/blogs        -----> POST (Create a new blog)
// localhost:3000/blogs/:id    -----> GET (Get a single blog)
// localhost:3000/blogs/:id    -----> DELETE (Delete a single blog)
// localhost:3000/blogs/:id    -----> PUT  (Update a single blog)
```

</details>

<details>
  <summary>50. Get Request with Route [/blogs]</summary>

```Javascript
// blogs routes
app.get('/blogs' , (req, res) => {
    Blog.find({}).sort({ createdAt: -1 })
        .then((result) => {
            res.render('index', { title: 'All Blogs', blogs: result });
        })
        .catch((err) => {
            console.log(err);
        });
});
```

app.js:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');
const Blog = require('./models/blog');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// static files
app.use(express.static('public'));

// get home page
app.get('/', (req, res) => {
    res.redirect('/blogs');
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// blogs routes
// Get all Blogs
app.get('/blogs' , (req, res) => {
    Blog.find({}).sort({ createdAt: -1 })
        .then((result) => {
            res.render('index', { title: 'All Blogs', blogs: result });
        })
        .catch((err) => {
            console.log(err);
        });
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

</details>

<details>
  <summary>51. Post Request with Route [/blogs]</summary>

Create.ejs:

```Javascript
<html lang="en">
    <%- include('./partials/head.ejs')  %>
    <body>
        <%- include('./partials/nav.ejs')  %>
        <div class= "create-blog content">
            <form action="/blogs" method="POST">
                <label for="title">Blog Title:</label>
                <input type="text" id="title" name="title" required>
                <label for="snippet">Blog Snippet:</label>
                <input type="text" id="snippet" name="snippet" required>
                <label for="body">Blog Body:</label>
                <textarea id="body" name="body" required></textarea>
                <button type="submit">Submit</button>
            </form>
        </div>
        <%- include('./partials/footer.ejs')  %>
    </body>
</html>
```

```Javascript
// static files
app.use(express.urlencoded({ extended: true }));

// Post a new blog
app.post('/blogs', (req, res) => {
    const blog = new Blog(req.body);
    blog.save()
        .then((result) => {
            res.redirect('/blogs');
        })
        .catch((err) => {
            console.log(err);
        });
});
```

app.js:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');
const Blog = require('./models/blog');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// static files
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev'));

// Routes
// get home page
app.get('/', (req, res) => {
    res.redirect('/blogs');
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// Blogs routes
// Get all Blogs
app.get('/blogs' , (req, res) => {
    Blog.find({}).sort({ createdAt: -1 })
        .then((result) => {
            res.render('index', { title: 'All Blogs', blogs: result });
        })
        .catch((err) => {
            console.log(err);
        });
});

// Post a new blog
app.post('/blogs', (req, res) => {
    const blog = new Blog(req.body);
    blog.save()
        .then((result) => {
            res.redirect('/blogs');
        })
        .catch((err) => {
            console.log(err);
        });
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

</details>

<details>
  <summary>52. Get a Single blog with Route [/blogs/:id]</summary>

index.ejs:

```html
<html lang="en">
  <%- include('./partials/head.ejs') %>
  <body>
    <%- include('./partials/nav.ejs') %>
    <div class="blogs content">
      <h2>All Blogs</h2>
      <% if(blogs.length > 0){ %> <% blogs.forEach(blog => { %>
      <div class="blog-preview">
        <a class="single" href="/blogs/<%= blog._id %>">
          <h3 class="title"><%= blog.title %></h3>
          <p class="author">Written by <%= blog.author %></p>
          <p class="snippet"><%= blog.snippet %></p>
        </a>
      </div>
      <% }) %> <% }else{ %>
      <p>No blogs to show</p>
      <% } %>
    </div>
    <%- include('./partials/footer.ejs') %>
  </body>
</html>
```

details.ejs:

```html
<html lang="en">
  <%- include("./partials/head.ejs") %>

  <body>
    <%- include("./partials/nav.ejs") %>

    <div class="details content">
      <h2><%= blog.title %></h2>
      <div class="content">
        <p><%= blog.body %></p>
      </div>
      <a class="delete" data-doc="<%= blog._id %>">delete</a>
    </div>

    <%- include("./partials/footer.ejs") %>
  </body>
</html>
```

style.css:

```css
/* index styles */
.blogs a {
  display: block;
  margin: 40px 0;
  padding-left: 30px;
  border-left: 6px solid crimson;
}
.blogs a:hover h3 {
  color: crimson;
}
```

```Javascript
// Get a single blog
app.get('/blogs/:id', (req, res) => {
    const id = req.params.id;
    Blog.findById(id)
        .then((result) => {
            res.render('details', { blog: result, title: 'Blog Details' });
        })
        .catch((err) => {
            console.log(err);
        });
});
```

app.js:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');
const Blog = require('./models/blog');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// static files
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev'));

// Routes
// get home page
app.get('/', (req, res) => {
    res.redirect('/blogs');
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// Blogs routes
// Get all Blogs
app.get('/blogs' , (req, res) => {
    Blog.find({}).sort({ createdAt: -1 })
        .then((result) => {
            res.render('index', { title: 'All Blogs', blogs: result });
        })
        .catch((err) => {
            console.log(err);
        });
});

// Post a new blog
app.post('/blogs', (req, res) => {
    const blog = new Blog(req.body);
    blog.save()
        .then((result) => {
            res.redirect('/blogs');
        })
        .catch((err) => {
            console.log(err);
        });
});

// Get a single blog
app.get('/blogs/:id', (req, res) => {
    const id = req.params.id;
    Blog.findById(id)
        .then((result) => {
            res.render('details', { blog: result, title: 'Blog Details' });
        })
        .catch((err) => {
            console.log(err);
        });
});

// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

</details>

<details>
  <summary>53. Delete a Single blog with Route [/blogs/:id] </summary>

details.ejs:

```html
<html lang="en">
  <%- include("./partials/head.ejs") %>

  <body>
    <%- include("./partials/nav.ejs") %>

    <div class="details content">
      <h2><%= blog.title %></h2>
      <div class="content">
        <p><%= blog.body %></p>
      </div>
      <a class="delete" data-doc="<%= blog._id %>">delete</a>
    </div>

    <%- include("./partials/footer.ejs") %>

    <script>
      const trashcan = document.querySelector("a.delete");

      trashcan.addEventListener("click", (e) => {
        const endpoint = `/blogs/${trashcan.dataset.doc}`;

        fetch(endpoint, {
          method: "DELETE",
        })
          .then((response) => response.json())
          .then((data) => (window.location.href = data.redirect))
          .catch((err) => console.log(err));
      });
    </script>
  </body>
</html>
```

style.css:

```css
/* details styles */
.details {
  position: relative;
}
.delete {
  position: absolute;
  top: 0;
  right: 0;
  border-radius: 50%;
  padding: 8px;
}
.delete:hover {
  cursor: pointer;
  box-shadow: 1px 2px 3px rgba(0, 0, 0, 0.2);
}
```

```Javascript
app.delete('/blogs/:id', (req, res) => {
  const id = req.params.id;

  Blog.findByIdAndDelete(id)
    .then(result => {
      res.json({ redirect: '/blogs' });
    })
    .catch(err => {
      console.log(err);
    });
});
```

app.js:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');
const Blog = require('./models/blog');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// static files
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev'));

// Routes
// get home page
app.get('/', (req, res) => {
    res.redirect('/blogs');
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// Blogs routes
// render create blog page
app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// Get all Blogs
app.get('/blogs' , (req, res) => {
    Blog.find({}).sort({ createdAt: -1 })
        .then((result) => {
            res.render('index', { title: 'All Blogs', blogs: result });
        })
        .catch((err) => {
            console.log(err);
        });
});

// Post a new blog
app.post('/blogs', (req, res) => {
    const blog = new Blog(req.body);
    blog.save()
        .then((result) => {
            res.redirect('/blogs');
        })
        .catch((err) => {
            console.log(err);
        });
});

// Get a single blog
app.get('/blogs/:id', (req, res) => {
    const id = req.params.id;
    Blog.findById(id)
        .then((result) => {
            res.render('details', { blog: result, title: 'Blog Details' });
        })
        .catch((err) => {
            console.log(err);
        });
});

//Delete a single blog
app.delete('/blogs/:id', (req, res) => {
    const id = req.params.id;
    Blog.findByIdAndDelete(id)
        .then(result => {
        res.json({ redirect: '/blogs' });
        })
        .catch(err => {
        console.log(err);
        });
});

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

</details>

+EXPRESS ROUTER & MVC

<details>
  <summary>54. Create Express Router</summary>

routes/blogRoutes.js:

```Javascript
const express = require('express');
const Blog = require('../models/blog');

const router = express.Router();

// render create blog page
router.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// Get all Blogs
router.get('/blogs' , (req, res) => {
    Blog.find({}).sort({ createdAt: -1 })
        .then((result) => {
            res.render('index', { title: 'All Blogs', blogs: result });
        })
        .catch((err) => {
            console.log(err);
        });
});

// Post a new blog
router.post('/blogs', (req, res) => {
    const blog = new Blog(req.body);
    blog.save()
        .then((result) => {
            res.redirect('/blogs');
        })
        .catch((err) => {
            console.log(err);
        });
});

// Get a single blog
router.get('/blogs/:id', (req, res) => {
    const id = req.params.id;
    Blog.findById(id)
        .then((result) => {
            res.render('details', { blog: result, title: 'Blog Details' });
        })
        .catch((err) => {
            console.log(err);
        });
});

//Delete a single blog
router.delete('/blogs/:id', (req, res) => {
    const id = req.params.id;
    Blog.findByIdAndDelete(id)
        .then(result => {
        res.json({ redirect: '/blogs' });
        })
        .catch(err => {
        console.log(err);
        });
});

module.exports = router;
```

app.js:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');
const blogRoutes = require('./routes/blogRoutes');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// static files
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev'));

// Routes
// get home page
app.get('/', (req, res) => {
    res.redirect('/blogs');
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// Blogs routes
app.use(blogRoutes);

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});
```

</details>

<details>
  <summary>55. Scoping the URL (Routing)</summary>

```Javascript
// Blogs routes
app.use('/blogs', blogRoutes);
```

app.js:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');
const blogRoutes = require('./routes/blogRoutes');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// static files
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev'));

// Routes
// get home page
app.get('/', (req, res) => {
    res.redirect('/blogs');
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// Blogs routes
app.use('/blogs', blogRoutes);

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

routes/blogRoutes.js:

```Javascript
const express = require('express');
const Blog = require('../models/blog');

const router = express.Router();

// render create blog page
router.get('/create', (req, res) => {
    res.render('create', { title: 'Create a new blog' });
});

// Get all Blogs
router.get('/' , (req, res) => {
    Blog.find({}).sort({ createdAt: -1 })
        .then((result) => {
            res.render('index', { title: 'All Blogs', blogs: result });
        })
        .catch((err) => {
            console.log(err);
        });
});

// Post a new blog
router.post('/', (req, res) => {
    const blog = new Blog(req.body);
    blog.save()
        .then((result) => {
            res.redirect('/blogs');
        })
        .catch((err) => {
            console.log(err);
        });
});

// Get a single blog
router.get('/:id', (req, res) => {
    const id = req.params.id;
    Blog.findById(id)
        .then((result) => {
            res.render('details', { blog: result, title: 'Blog Details' });
        })
        .catch((err) => {
            console.log(err);
        });
});

//Delete a single blog
router.delete('/:id', (req, res) => {
    const id = req.params.id;
    Blog.findByIdAndDelete(id)
        .then(result => {
        res.json({ redirect: '/blogs' });
        })
        .catch(err => {
        console.log(err);
        });
});

module.exports = router;
```

</details>

<details>
  <summary>56. The MVC Structure</summary>

app.js:

```Javascript
const express = require('express');
const path = require('path');
const morgan = require('morgan')
const mongoose = require('mongoose');
const blogRoutes = require('./routes/blogRoutes');

// express app
const app = express();

// register view engine
app.set('view engine', 'ejs');

const dbURI = "mongodb+srv://<accountName>:<password>@cluster0.ujjnbjl.mongodb.net/<dbname>?retryWrites=true&w=majority";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => {
        // listen for requests
        app.listen(3000);
        console.log('connected to db');
    })
    .catch((err) => console.log(err));

// static files
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev'));

// Routes
// get home page
app.get('/', (req, res) => {
    res.redirect('/blogs');
});

// get about page
app.get('/about', (req, res) => {
    res.render('about', { title: 'About' });
});

// Blogs routes
app.use('/blogs', blogRoutes);

// 404 page
app.use((req, res) => {
    res.status(404).render('404', { title: '404' });
    // res.sendFile('./views/404.html', { root: __dirname });
});

```

routes/blogRoutes.js:

```Javascript
const express = require('express');
const blogController = require('../controllers/blogController');

const router = express.Router();

// render create blog page
router.get('/create', blogController.blog_create_get);

// Get all Blogs
router.get('/', blogController.blog_index);

// Post a new blog
router.post('/', blogController.blog_create_post);

// Get a single blog
router.get('/:id', blogController.blog_details);

//Delete a single blog
router.delete('/:id', blogController.blog_delete);

module.exports = router;
```

controllers/blogController.js:

```Javascript
const Blog = require('../models/blog');

// Get all Blogs
const blog_index = (req, res) => {
    Blog.find({}).sort({ createdAt: -1 })
        .then((result) => {
            res.render('index', { title: 'All Blogs', blogs: result });
        })
        .catch((err) => {
            console.log(err);
        });
}

// Get a single blog
const blog_details = (req, res) => {
    const id = req.params.id;
    Blog.findById(id)
        .then((result) => {
            res.render('details', { blog: result, title: 'Blog Details' });
        })
        .catch((err) => {
            console.log(err);
        });
}

// render create blog page
const blog_create_get = (req, res) => {
    res.render('create', { title: 'Create a new blog' });
}

// post a new blog
const blog_create_post = (req, res) => {
    const blog = new Blog(req.body);
    blog.save()
        .then((result) => {
            res.redirect('/blogs');
        })
        .catch((err) => {
            console.log(err);
        });
}

//Delete a single blog
const blog_delete = (req, res) => {
    const id = req.params.id;
    Blog.findByIdAndDelete(id)
        .then(result => {
        res.json({ redirect: '/blogs' });
        })
        .catch(err => {
        console.log(err);
        });
}


module.exports = {
    blog_index,
    blog_details,
    blog_create_get,
    blog_create_post,
    blog_delete
}
```

</details>

<details>
  <summary>57. Add Trash Can for Delete Button</summary>

```Javascript
<div class="details content">
    <h2><%= blog.title %></h2>
    <div class="content">
        <p><%= blog.body %></p>
    </div>
    <a class="delete" data-doc="<%= blog._id %>">
        <img src="/trashcan.svg" alt="delete icon">
    </a>
</div>
```

views/details.ejs:

```Javascript
<html lang="en">
<%- include("./partials/head.ejs") %>

<body>
  <%- include("./partials/nav.ejs") %>

  <div class="details content">
    <h2><%= blog.title %></h2>
    <div class="content">
      <p><%= blog.body %></p>
    </div>
    <a class="delete" data-doc="<%= blog._id %>">
        <img src="/trashcan.svg" alt="delete icon">
    </a>
  </div>

  <%- include("./partials/footer.ejs") %>

  <script>
    const trashcan = document.querySelector('a.delete');

    trashcan.addEventListener('click', (e) => {
      const endpoint = `/blogs/${trashcan.dataset.doc}`;

      fetch(endpoint, {
        method: 'DELETE',
      })
      .then(response => response.json())
      .then(data => window.location.href = data.redirect)
      .catch(err => console.log(err));
    });

  </script>
</body>
</html>
```

</details>

<details>
  <summary>58. Correct 404 page rendering</summary>

```Javascript
// Get a single blog
const blog_details = (req, res) => {
    const id = req.params.id;
    Blog.findById(id)
        .then((result) => {
            res.render('details', { blog: result, title: 'Blog Details' });
        })
        .catch((err) => {
            res.status(404).render('404', { title: 'Blog not found' });
        });
}
```

controllers/blogController.js:

```Javascript
// blog_index, blog_details, blog_create_get, blog_create_post, blog_delete

const Blog = require('../models/blog');

// Get all Blogs
const blog_index = (req, res) => {
    Blog.find({}).sort({ createdAt: -1 })
        .then((result) => {
            res.render('index', { title: 'All Blogs', blogs: result });
        })
        .catch((err) => {
            console.log(err);
        });
}

// Get a single blog
const blog_details = (req, res) => {
    const id = req.params.id;
    Blog.findById(id)
        .then((result) => {
            res.render('details', { blog: result, title: 'Blog Details' });
        })
        .catch((err) => {
            res.status(404).render('404', { title: 'Blog not found' });
        });
}

// render create blog page
const blog_create_get = (req, res) => {
    res.render('create', { title: 'Create a new blog' });
}

// post a new blog
const blog_create_post = (req, res) => {
    const blog = new Blog(req.body);
    blog.save()
        .then((result) => {
            res.redirect('/blogs');
        })
        .catch((err) => {
            console.log(err);
        });
}

//Delete a single blog
const blog_delete = (req, res) => {
    const id = req.params.id;
    Blog.findByIdAndDelete(id)
        .then(result => {
        res.json({ redirect: '/blogs' });
        })
        .catch(err => {
        console.log(err);
        });
}


module.exports = {
    blog_index,
    blog_details,
    blog_create_get,
    blog_create_post,
    blog_delete
}
```

</details>

# #END