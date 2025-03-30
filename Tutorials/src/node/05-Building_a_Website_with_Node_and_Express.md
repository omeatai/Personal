## +Linkedin-Building a Website with Node.js and Express.js

## [COURSE](https://www.linkedin.com/learning/building-a-website-with-node-js-and-express-js-3/dynamic-websites-with-node-and-express?resume=false)

<details>
<summary>1. Clone Project Directory </summary>

# Clone Project Directory

## [https://github.com/danielkhan/building-website-nodejs-express/tree/master](https://github.com/danielkhan/building-website-nodejs-express/tree/master)

```x
git clone --bare https://github.com/danielkhan/building-website-nodejs-express.git
cd building-website-nodejs-express.git
git config --bool core.bare false
git reset --hard
git branch
q
```

# #END</details>

<details>
<summary>2. Setup Node Environment </summary>

# Setup Node Environment

## Initialize npm

```x
npm init -y
```

## Install Express and Nodemon

```x
npm install --save express nodemon
```

### src-AI-Software/my_projects/01_building_a_website/package.json:

```x
{
  "name": "01_building_a_website",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2",
    "nodemon": "^3.1.4"
  }
}

```

# #END</details>

<details>
<summary>3. Setup Express Server </summary>

# Setup Express Server

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require("express");

const app = express();

const PORT = 3000;

app.get("/", (req, res) => {
  res.send("Hello Express :)");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Ctrl + C to stop");
});

```

### src-AI-Software/my_projects/01_building_a_website/package.json:

```x
{
  "name": "01_building_a_website",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon --ignore feedback.json server.js"
  },
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2",
    "nodemon": "^3.1.4"
  }
}
```

## Run Server

```x
npm run start
```

```x
➜  01_building_a_website git:(main) ✗ npm run start

> 01_building_a_website@1.0.0 start
> nodemon server.js

[nodemon] 3.1.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,cjs,json
[nodemon] starting `node server.js`
Server running on port 3000
Ctrl + C to stop
```

![image](https://github.com/user-attachments/assets/61bc6bf1-d244-466e-ab70-4d7b63bace60)

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/73d72bb0-fb1b-4033-86a5-e495d60c32ad">

# #END</details>

<details>
<summary>4. Setup HTML Static Template </summary>

# Setup HTML Static Template

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require("express");
const path = require("path");

const app = express();

const PORT = 3000;

app.use(express.static(path.join(__dirname, "./static")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "./static/index.html"));
});

app.get("/speakers", (req, res) => {
  res.sendFile(path.join(__dirname, "./static/speakers.html"));
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Ctrl + C to stop");
});

```

### src-AI-Software/my_projects/01_building_a_website/static/index.html:

```html
<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">
  <head>
    <script src="./assets/js/color-modes.js"></script>

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Roux Meetups--Home</title>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/@docsearch/css@3"
    />
    <link href="./assets/dist/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Custom styles for this template -->
    <link href="./css/carousel.css" rel="stylesheet" />
  </head>
  <body>
    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
      <symbol id="check2" viewBox="0 0 16 16">
        <path
          d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"
        />
      </symbol>
      <symbol id="circle-half" viewBox="0 0 16 16">
        <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
      </symbol>
      <symbol id="moon-stars-fill" viewBox="0 0 16 16">
        <path
          d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z"
        />
        <path
          d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z"
        />
      </symbol>
      <symbol id="sun-fill" viewBox="0 0 16 16">
        <path
          d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z"
        />
      </symbol>
    </svg>

    <div
      class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle"
    >
      <button
        class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center"
        id="bd-theme"
        type="button"
        aria-expanded="false"
        data-bs-toggle="dropdown"
        aria-label="Toggle theme (auto)"
      >
        <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
          <use href="#circle-half"></use>
        </svg>
        <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
      </button>
      <ul
        class="dropdown-menu dropdown-menu-end shadow"
        aria-labelledby="bd-theme-text"
      >
        <li>
          <button
            type="button"
            class="dropdown-item d-flex align-items-center"
            data-bs-theme-value="light"
            aria-pressed="false"
          >
            <svg class="bi me-2 opacity-50" width="1em" height="1em">
              <use href="#sun-fill"></use>
            </svg>
            Light
            <svg class="bi ms-auto d-none" width="1em" height="1em">
              <use href="#check2"></use>
            </svg>
          </button>
        </li>
        <li>
          <button
            type="button"
            class="dropdown-item d-flex align-items-center"
            data-bs-theme-value="dark"
            aria-pressed="false"
          >
            <svg class="bi me-2 opacity-50" width="1em" height="1em">
              <use href="#moon-stars-fill"></use>
            </svg>
            Dark
            <svg class="bi ms-auto d-none" width="1em" height="1em">
              <use href="#check2"></use>
            </svg>
          </button>
        </li>
        <li>
          <button
            type="button"
            class="dropdown-item d-flex align-items-center active"
            data-bs-theme-value="auto"
            aria-pressed="true"
          >
            <svg class="bi me-2 opacity-50" width="1em" height="1em">
              <use href="#circle-half"></use>
            </svg>
            Auto
            <svg class="bi ms-auto d-none" width="1em" height="1em">
              <use href="#check2"></use>
            </svg>
          </button>
        </li>
      </ul>
    </div>

    <header data-bs-theme="dark">
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Roux Meetups</a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarCollapse"
            aria-controls="navbarCollapse"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav me-auto mb-2 mb-md-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">All Speakers</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Feedback</a>
              </li>
            </ul>
            <form class="d-flex" role="search">
              <input
                class="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
              <button class="btn btn-outline-success" type="submit">
                Search
              </button>
            </form>
          </div>
        </div>
      </nav>
    </header>

    <main>
      <!-- Carousel Slider
  ================================================== -->
      <div id="myCarousel" class="carousel slide mb-6" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button
            type="button"
            data-bs-target="#myCarousel"
            data-bs-slide-to="0"
            class="active"
            aria-current="true"
            aria-label="Slide 1"
          ></button>
          <button
            type="button"
            data-bs-target="#myCarousel"
            data-bs-slide-to="1"
            aria-label="Slide 2"
            class="btn btn-light"
          ></button>
          <button
            type="button"
            data-bs-target="#myCarousel"
            data-bs-slide-to="2"
            aria-label="Slide 3"
          ></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="./images/background.jpg" alt="carousel 1" width="100%" />
            <div class="container">
              <div class="carousel-caption text-start text-light">
                <h1>The Art of Abstract</h1>
                <p class="opacity-75">
                  The Roux Academy gets thousands of submissions every year for artists interesting in participating in the
            CAC exhibits, and selects approximately 200 distinct pieces of contemporary art for display in their
            collective exhibit.
                </p>
                <p>
                  <a class="btn btn-lg btn-primary" href="#">Sign up today</a>
                </p>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <img src="./images/background2.jpg" alt="carousel 2" width="100%" />
            <div class="container">
              <div class="carousel-caption text-light">
                <h1>Art in Full Bloom</h1>
                <p>
                  Each Featured Artist has an opportunity to speak at one of our meetups and share his or her vision,
            perspective, and techniques with attendees on a more personal level than at our large conference.
                </p>
                <p><a class="btn btn-lg btn-primary" href="#">Learn more</a></p>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <img src="./images/background3.jpg" alt="carousel 3" width="100%" />
            <div class="container">
              <div class="carousel-caption text-end text-light">
                <h1>Deep Sea Wonders</h1>
                <p>
                  CAC Featured Artist and many past students artists who were featured at CAC have gone on to brilliant
            careers in art.
                </p>
                <p>
                  <a class="btn btn-lg btn-primary" href="#">Browse gallery</a>
                </p>
              </div>
            </div>
          </div>
        </div>
        <button
          class="carousel-control-prev btn btn-primary opacity-25"
          type="button"
          data-bs-target="#myCarousel"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button
          class="carousel-control-next btn btn-primary opacity-25"
          type="button"
          data-bs-target="#myCarousel"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>

      <!-- Marketing messaging and featurettes
  ================================================== -->
      <!-- Wrap the rest of the page in another container to center all the content. -->

      <div class="container marketing">
        <!-- Three columns of text below the carousel -->
        <div class="row">
          <div class="col-lg-4">
            <img
              src="./images/Hillary_Goldwynn_tn.jpg"
              alt="carousel 2"
              width="50%"
              class="bd-placeholder-img rounded-circle"
            />
            <h2 class="fw-normal">Hilliary Goldwynn</h2>
            <p>
              Some representative placeholder content for the three columns of
              text below the carousel. This is the first column.
            </p>
            <p>
              <a class="btn btn-secondary" href="#">View details &raquo;</a>
            </p>
          </div>
          <!-- /.col-lg-4 -->
          <div class="col-lg-4">
            <img
              src="./images/Lorenzo_Garcia_tn.jpg"
              alt="carousel 2"
              width="50%"
              class="bd-placeholder-img rounded-circle"
            />
            <h2 class="fw-normal">Lorenzo Garcia</h2>
            <p>
              Another exciting bit of representative placeholder content. This
              time, we've moved on to the second column.
            </p>
            <p>
              <a class="btn btn-secondary" href="#">View details &raquo;</a>
            </p>
          </div>
          <!-- /.col-lg-4 -->
          <div class="col-lg-4">
            <img
              src="./images/Riley_Rewington_tn.jpg"
              alt="carousel 2"
              width="50%"
              class="bd-placeholder-img rounded-circle"
            />
            <h2 class="fw-normal">Riley Rewington</h2>
            <p>
              And lastly this, the third column of representative placeholder
              content.
            </p>
            <p>
              <a class="btn btn-secondary" href="#">View details &raquo;</a>
            </p>
          </div>
          <!-- /.col-lg-4 -->
        </div>
        <!-- /.row -->

        <!-- START THE FEATURETTES -->

        <hr class="featurette-divider" />

        <div class="row featurette">
          <div class="col-md-7">
            <h2 class="featurette-heading fw-normal lh-1">
              Who are we?
              <span class="text-body-secondary">It’ll blow your mind.</span>
            </h2>
            <p class="lead">
              The Roux Academy gets thousands of submissions every year for
              artists interesting in participating in the CAC exhibits, and
              selects approximately 200 distinct pieces of contemporary art for
              display in their collective exhibit.
            </p>
          </div>
          <div class="col-md-5">
            <img src="./images/artwork/Hillary_Goldwynn_03.jpg" alt="carousel 1" width="500" height="500"  class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"/>
          </div>
        </div>

        <hr class="featurette-divider" />

        <div class="row featurette">
          <div class="col-md-7 order-md-2">
            <h2 class="featurette-heading fw-normal lh-1">
              What we do.
              <span class="text-body-secondary">See for yourself.</span>
            </h2>
            <p class="lead">
              Each Featured Artist has an opportunity to speak at one of our
              meetups and share his or her vision, perspective, and techniques
              with attendees on a more personal level than at our large
              conference. While you attend the conference, head over to our gallery where you can check out some
            of the work from our speakers.
            </p>
          </div>
          <div class="col-md-5">
            <img src="./images/artwork/Hillary_Goldwynn_07.jpg" alt="carousel 1" width="500" height="500"  class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"/>
          </div>
        </div>

        <hr class="featurette-divider" />

        <div class="row featurette">
          <div class="col-md-7">
            <h2 class="featurette-heading fw-normal lh-1">
              And lastly, Who should come?
              <span class="text-body-secondary">Checkmate.</span>
            </h2>
            <p class="lead">
            <ul class="sidebar-body">
                <li>Anybody interested in art and the creative industry</li>
                <li>Painters, sculptors, photographers and graphic artists</li>
                <li>Those interested in meeting and making a connection with others in the local art scene.</li>
            </ul>
            </p>
          </div>
            <div class="col-md-5">
                <img src="./images/artwork/Hillary_Goldwynn_02.jpg" alt="carousel 1" width="500" height="500"  class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"/>
            </div>
            </div>

        <hr class="featurette-divider" />

        <!-- /END THE FEATURETTES -->
      </div>
      <!-- /.container -->

      <!-- FOOTER -->
      <footer class="container">
        <p class="float-end"><a href="#">Back to top</a></p>
        <p>
          &copy; 2024 Company, Inc. &middot;
          <a href="#">Privacy</a> &middot; <a href="#">Terms</a>
        </p>
      </footer>
    </main>
    <script src="./assets/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>

```


![image](https://github.com/user-attachments/assets/471551d2-6e1b-4f94-b74d-644bd4096ccd)
![image](https://github.com/user-attachments/assets/21a67aad-4049-4f87-b23a-1cadfb4054b1)

![image](https://github.com/user-attachments/assets/1af87bb2-3cd8-4a00-b4cb-5a4b7d97f4e9)
![image](https://github.com/user-attachments/assets/08641379-d1a2-44e7-bb17-e52ab6d47e6b)
![image](https://github.com/user-attachments/assets/1821684e-8684-426c-a499-4564df2afdab)
![image](https://github.com/user-attachments/assets/9530e051-75e6-4ab2-a25d-b7b1e9618f00)

# #END</details>

<details>
<summary>5. Install and Initialize ESLint and Prettier </summary>

# Install and Initialize ESLint and Prettier

```x
npm install --save-dev eslint
```

## Initialize eslint

```x
npx eslint --init
```

<img width="733" alt="image" src="https://github.com/user-attachments/assets/39d77d18-b2e0-4ce2-b071-cf2c81aa49ad">

## Install Prettier

```x
npm install --save-dev prettier eslint-config-prettier eslint-plugin-prettier
#npm install --save-dev eslint-airbnb-base eslint-plugin-import
```

### src-AI-Software/my_projects/01_building_a_website/eslint.config.mjs:

```mjs
import globals from "globals";
import pluginJs from "@eslint/js";

export default [
  {
    files: ["**/*.js"],
    languageOptions: { sourceType: "commonjs" },
    plugins: ["prettier"],
    extends: ["prettier"],
  },
  { languageOptions: { globals: globals.browser } },
  pluginJs.configs.recommended,
];

```

### src-AI-Software/my_projects/01_building_a_website/.prettierrc:

```prettierrc
{
    "trailingComma": "es5",
    "printWidth": 100,
    "singleQuote": true
}
```

### src-AI-Software/my_projects/01_building_a_website/package.json:

```js
{
  "name": "01_building_a_website",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon --ignore feedback.json server.js"
  },
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2",
    "nodemon": "^3.1.4"
  },
  "devDependencies": {
    "@eslint/js": "^9.7.0",
    "eslint": "^9.7.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-prettier": "^5.2.1",
    "globals": "^15.8.0",
    "prettier": "^3.3.3"
  }
}
```

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');

const app = express();

const PORT = 3000;

app.use(express.static(path.join(__dirname, './static')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, './static/index.html'));
});

app.get('/speakers', (req, res) => {
  res.sendFile(path.join(__dirname, './static/speakers.html'));
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/35db9c25-11d7-447f-84df-35470287dff1">
<img width="1353" alt="image" src="https://github.com/user-attachments/assets/ed8701a8-4ac8-4aeb-b62f-7bfc6a3cd4c0">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/0da1c614-1dce-45d8-8def-3790274c6f22">

<img width="1353" alt="image" src="https://github.com/user-attachments/assets/21177cbc-4fe6-4e52-aeae-d9e46f545053">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/b1e3ae4b-99b2-4994-9835-0d5c902f88df">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/88e19c11-88de-4e6c-ba65-848d2668602c">

# #END</details>

<details>
<summary>6. Using Express Template Engine - EJS </summary>

# Using Express Template Engine - EJS

## [https://ejs.co/](https://ejs.co/)

![image](https://github.com/user-attachments/assets/0465790c-6fb4-44c3-973d-0525f59aeb87)
![image](https://github.com/user-attachments/assets/9c93a2bc-2035-41da-a302-47e18c6ad26a)

# Install EJS

```js
npm install ejs
```

### src-AI-Software/my_projects/01_building_a_website/package.json:

```json
{
  "name": "01_building_a_website",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon --ignore feedback.json server.js"
  },
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "ejs": "^3.1.10",
    "express": "^4.19.2",
    "nodemon": "^3.1.4"
  },
  "devDependencies": {
    "@eslint/js": "^9.7.0",
    "eslint": "^9.7.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-prettier": "^5.2.1",
    "globals": "^15.8.0",
    "prettier": "^3.3.3"
  }
}

```

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');

const app = express();

const PORT = 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.get('/', (req, res) => {
  //   res.sendFile(path.join(__dirname, './static/index.html'));
  const context = {
    pageTitle: 'Welcome',
    name: 'Roux Meetups',
  };
  res.render('pages/index', context);
});

app.get('/speakers', (req, res) => {
  res.sendFile(path.join(__dirname, './static/speakers.html'));
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/index.ejs:

```ejs
<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">
  <head>
    <script src="./assets/js/color-modes.js"></script>

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title><%= name %>--<%= pageTitle %></title>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/@docsearch/css@3"
    />
    <link href="./assets/dist/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Custom styles for this template -->
    <link href="./css/carousel.css" rel="stylesheet" />
  </head>
  <body>
    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
      <symbol id="check2" viewBox="0 0 16 16">
        <path
          d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"
        />
      </symbol>
      <symbol id="circle-half" viewBox="0 0 16 16">
        <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
      </symbol>
      <symbol id="moon-stars-fill" viewBox="0 0 16 16">
        <path
          d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z"
        />
        <path
          d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z"
        />
      </symbol>
      <symbol id="sun-fill" viewBox="0 0 16 16">
        <path
          d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z"
        />
      </symbol>
    </svg>

    <div
      class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle"
    >
      <button
        class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center"
        id="bd-theme"
        type="button"
        aria-expanded="false"
        data-bs-toggle="dropdown"
        aria-label="Toggle theme (auto)"
      >
        <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
          <use href="#circle-half"></use>
        </svg>
        <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
      </button>
      <ul
        class="dropdown-menu dropdown-menu-end shadow"
        aria-labelledby="bd-theme-text"
      >
        <li>
          <button
            type="button"
            class="dropdown-item d-flex align-items-center"
            data-bs-theme-value="light"
            aria-pressed="false"
          >
            <svg class="bi me-2 opacity-50" width="1em" height="1em">
              <use href="#sun-fill"></use>
            </svg>
            Light
            <svg class="bi ms-auto d-none" width="1em" height="1em">
              <use href="#check2"></use>
            </svg>
          </button>
        </li>
        <li>
          <button
            type="button"
            class="dropdown-item d-flex align-items-center"
            data-bs-theme-value="dark"
            aria-pressed="false"
          >
            <svg class="bi me-2 opacity-50" width="1em" height="1em">
              <use href="#moon-stars-fill"></use>
            </svg>
            Dark
            <svg class="bi ms-auto d-none" width="1em" height="1em">
              <use href="#check2"></use>
            </svg>
          </button>
        </li>
        <li>
          <button
            type="button"
            class="dropdown-item d-flex align-items-center active"
            data-bs-theme-value="auto"
            aria-pressed="true"
          >
            <svg class="bi me-2 opacity-50" width="1em" height="1em">
              <use href="#circle-half"></use>
            </svg>
            Auto
            <svg class="bi ms-auto d-none" width="1em" height="1em">
              <use href="#check2"></use>
            </svg>
          </button>
        </li>
      </ul>
    </div>

    <header data-bs-theme="dark">
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="#"><%= name %></a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarCollapse"
            aria-controls="navbarCollapse"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav me-auto mb-2 mb-md-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">All Speakers</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Feedback</a>
              </li>
            </ul>
            <form class="d-flex" role="search">
              <input
                class="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
              <button class="btn btn-outline-success" type="submit">
                Search
              </button>
            </form>
          </div>
        </div>
      </nav>
    </header>

    <main>
      <!-- Carousel Slider
  ================================================== -->
      <div id="myCarousel" class="carousel slide mb-6" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button
            type="button"
            data-bs-target="#myCarousel"
            data-bs-slide-to="0"
            class="active"
            aria-current="true"
            aria-label="Slide 1"
          ></button>
          <button
            type="button"
            data-bs-target="#myCarousel"
            data-bs-slide-to="1"
            aria-label="Slide 2"
            class="btn btn-light"
          ></button>
          <button
            type="button"
            data-bs-target="#myCarousel"
            data-bs-slide-to="2"
            aria-label="Slide 3"
          ></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="./images/background.jpg" alt="carousel 1" width="100%" />
            <div class="container">
              <div class="carousel-caption text-start text-light">
                <h1>The Art of Abstract</h1>
                <p class="opacity-75">
                  The Roux Academy gets thousands of submissions every year for artists interesting in participating in the
            CAC exhibits, and selects approximately 200 distinct pieces of contemporary art for display in their
            collective exhibit.
                </p>
                <p>
                  <a class="btn btn-lg btn-primary" href="#">Sign up today</a>
                </p>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <img src="./images/background2.jpg" alt="carousel 2" width="100%" />
            <div class="container">
              <div class="carousel-caption text-light">
                <h1>Art in Full Bloom</h1>
                <p>
                  Each Featured Artist has an opportunity to speak at one of our meetups and share his or her vision,
            perspective, and techniques with attendees on a more personal level than at our large conference.
                </p>
                <p><a class="btn btn-lg btn-primary" href="#">Learn more</a></p>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <img src="./images/background3.jpg" alt="carousel 3" width="100%" />
            <div class="container">
              <div class="carousel-caption text-end text-light">
                <h1>Deep Sea Wonders</h1>
                <p>
                  CAC Featured Artist and many past students artists who were featured at CAC have gone on to brilliant
            careers in art.
                </p>
                <p>
                  <a class="btn btn-lg btn-primary" href="#">Browse gallery</a>
                </p>
              </div>
            </div>
          </div>
        </div>
        <button
          class="carousel-control-prev btn btn-primary opacity-25"
          type="button"
          data-bs-target="#myCarousel"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button
          class="carousel-control-next btn btn-primary opacity-25"
          type="button"
          data-bs-target="#myCarousel"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>

      <!-- Marketing messaging and featurettes
  ================================================== -->
      <!-- Wrap the rest of the page in another container to center all the content. -->

      <div class="container marketing">
        <!-- Three columns of text below the carousel -->
        <div class="row">
          <div class="col-lg-4">
            <img
              src="./images/Hillary_Goldwynn_tn.jpg"
              alt="carousel 2"
              width="50%"
              class="bd-placeholder-img rounded-circle"
            />
            <h2 class="fw-normal">Hilliary Goldwynn</h2>
            <p>
              Some representative placeholder content for the three columns of
              text below the carousel. This is the first column.
            </p>
            <p>
              <a class="btn btn-secondary" href="#">View details &raquo;</a>
            </p>
          </div>
          <!-- /.col-lg-4 -->
          <div class="col-lg-4">
            <img
              src="./images/Lorenzo_Garcia_tn.jpg"
              alt="carousel 2"
              width="50%"
              class="bd-placeholder-img rounded-circle"
            />
            <h2 class="fw-normal">Lorenzo Garcia</h2>
            <p>
              Another exciting bit of representative placeholder content. This
              time, we've moved on to the second column.
            </p>
            <p>
              <a class="btn btn-secondary" href="#">View details &raquo;</a>
            </p>
          </div>
          <!-- /.col-lg-4 -->
          <div class="col-lg-4">
            <img
              src="./images/Riley_Rewington_tn.jpg"
              alt="carousel 2"
              width="50%"
              class="bd-placeholder-img rounded-circle"
            />
            <h2 class="fw-normal">Riley Rewington</h2>
            <p>
              And lastly this, the third column of representative placeholder
              content.
            </p>
            <p>
              <a class="btn btn-secondary" href="#">View details &raquo;</a>
            </p>
          </div>
          <!-- /.col-lg-4 -->
        </div>
        <!-- /.row -->

        <!-- START THE FEATURETTES -->

        <hr class="featurette-divider" />

        <div class="row featurette">
          <div class="col-md-7">
            <h2 class="featurette-heading fw-normal lh-1">
              Who are we?
              <span class="text-body-secondary">It’ll blow your mind.</span>
            </h2>
            <p class="lead">
              The Roux Academy gets thousands of submissions every year for
              artists interesting in participating in the CAC exhibits, and
              selects approximately 200 distinct pieces of contemporary art for
              display in their collective exhibit.
            </p>
          </div>
          <div class="col-md-5">
            <img src="./images/artwork/Hillary_Goldwynn_03.jpg" alt="carousel 1" width="500" height="500"  class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"/>
          </div>
        </div>

        <hr class="featurette-divider" />

        <div class="row featurette">
          <div class="col-md-7 order-md-2">
            <h2 class="featurette-heading fw-normal lh-1">
              What we do.
              <span class="text-body-secondary">See for yourself.</span>
            </h2>
            <p class="lead">
              Each Featured Artist has an opportunity to speak at one of our
              meetups and share his or her vision, perspective, and techniques
              with attendees on a more personal level than at our large
              conference. While you attend the conference, head over to our gallery where you can check out some
            of the work from our speakers.
            </p>
          </div>
          <div class="col-md-5">
            <img src="./images/artwork/Hillary_Goldwynn_07.jpg" alt="carousel 1" width="500" height="500"  class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"/>
          </div>
        </div>

        <hr class="featurette-divider" />

        <div class="row featurette">
          <div class="col-md-7">
            <h2 class="featurette-heading fw-normal lh-1">
              And lastly, Who should come?
              <span class="text-body-secondary">Checkmate.</span>
            </h2>
            <p class="lead">
            <ul class="sidebar-body">
                <li>Anybody interested in art and the creative industry</li>
                <li>Painters, sculptors, photographers and graphic artists</li>
                <li>Those interested in meeting and making a connection with others in the local art scene.</li>
            </ul>
            </p>
          </div>
            <div class="col-md-5">
                <img src="./images/artwork/Hillary_Goldwynn_02.jpg" alt="carousel 1" width="500" height="500"  class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"/>
            </div>
            </div>

        <hr class="featurette-divider" />

        <!-- /END THE FEATURETTES -->
      </div>
      <!-- /.container -->

      <!-- FOOTER -->
      <footer class="container">
        <p class="float-end"><a href="#">Back to top</a></p>
        <p>
          &copy; 2024 Company, Inc. &middot;
          <a href="#">Privacy</a> &middot; <a href="#">Terms</a>
        </p>
      </footer>
    </main>
    <script src="./assets/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>

```

![image](https://github.com/user-attachments/assets/226ccc6a-76a9-4da7-a963-d5ce93df43ae)

<img width="1349" alt="image" src="https://github.com/user-attachments/assets/e82f2b43-3055-4016-a243-3eb078c55314">

# #END</details>

<details>
<summary>7. Setup Express Route for HomePage </summary>

# Setup Express Route for HomePage

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use('/', routes());

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/homeRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = () => {
  router.get('/', (req, res) => {
    const context = {
      pageTitle: 'Welcome',
      name: 'Roux Meetups',
    };
    res.render('pages/index', context);
  });

  return router;
};

```

![image](https://github.com/user-attachments/assets/9559a394-f76b-483d-8f57-d96ab54232eb)

<img width="1349" alt="image" src="https://github.com/user-attachments/assets/d593c096-9852-4258-b276-cac520e6fc4d">
<img width="1349" alt="image" src="https://github.com/user-attachments/assets/e909b1f2-8dbf-43f7-9cfa-988228a58b1f">

# #END</details>

<details>
<summary>8. Setup Express Routes for Sub Pages - feedback and speakers </summary>

# Setup Express Routes for Sub Pages - feedback and speakers

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use('/', routes());

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/homeRoutes.js:

```js
const express = require('express');

const speakersRoutes = require('./speakersRoutes');
const feedbackRoutes = require('./feedbackRoutes');

const router = express.Router();

module.exports = () => {
  router.get('/', (req, res) => {
    const context = {
      pageTitle: 'Welcome',
      name: 'Roux Meetups',
    };
    res.render('pages/index', context);
  });

  router.use('/speakers', speakersRoutes());
  router.use('/feedback', feedbackRoutes());

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/routes/speakersRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = () => {
  router.get('/', (req, res) => {
    // const context = {
    //   pageTitle: 'Welcome',
    //   name: 'Roux Meetups',
    // };
    // res.render('pages/index', context);
    return res.send('This is the Speakers List Page.');
  });

  router.get('/:shortname', (req, res) => {
    const speakerName = req.params.shortname;
    return res.send(`This is the Speakers Detail Page for speaker: ${speakerName}.`);
  });

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/routes/feedbackRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = () => {
  router.get('/', (req, res) => {
    // const context = {
    //   pageTitle: 'Welcome',
    //   name: 'Roux Meetups',
    // };
    // res.render('pages/index', context);
    return res.send('This is the Feedback Page.');
  });

  router.post('/', (req, res) => {
    const feedback = req.body.feedback;
    return res.send(`Thanks for your posted feedback: ${feedback}`);
  });

  return router;
};

```

```x
GET http://localhost:3000/
```

![image](https://github.com/user-attachments/assets/4cc7ef60-179c-4da0-b1d7-ffd0f8001061)

```x
GET http://localhost:3000/speakers
```

![image](https://github.com/user-attachments/assets/afae2ce5-04e9-4429-8986-a2d0200745a9)

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/4452ab35-9986-42fc-8362-cf1e16eef863">

```x
GET http://localhost:3000/speakers/Ifeanyi
```

![image](https://github.com/user-attachments/assets/be113e7e-5658-49a4-8e39-22b7a787e5ea)

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/d2a40a03-5774-438c-8548-20af2fc8e93c">

```x
GET http://localhost:3000/feedback
```

![image](https://github.com/user-attachments/assets/e40fbf19-d66e-4542-9208-d0dc00e78fb1)

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/0c16c925-4395-44fb-83b5-086c8792215a">

```x
POST http://localhost:3000/feedback
```

<img width="1313" alt="image" src="https://github.com/user-attachments/assets/ce3d7318-f859-43de-b6ef-41c9b8d5fbf6">

# #END</details>

<details>
<summary>9. Setup Model (Business Logic) for feedback and speakers routes </summary>

# Setup Model (Business Logic) for feedback and speakers routes

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use('/', routes({ feedbackModel, speakersModel }));

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/homeRoutes.js:

```js
const express = require('express');

const speakersRoutes = require('./speakersRoutes');
const feedbackRoutes = require('./feedbackRoutes');

const router = express.Router();

module.exports = (db) => {
  router.get('/', (req, res) => {
    const context = {
      pageTitle: 'Welcome',
      name: 'Roux Meetups',
    };
    res.render('pages/index', context);
  });

  router.use('/speakers', speakersRoutes(db));
  router.use('/feedback', feedbackRoutes(db));

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/routes/speakersRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = (db) => {
  const { speakersModel } = db;

  router.get('/', async (req, res) => {
    const speakers = await speakersModel.getList();
    return res.json({ data: speakers });
  });

  router.get('/:shortname', (req, res) => {
    const speakerName = req.params.shortname;
    return res.send(`This is the Speakers Detail Page for speaker: ${speakerName}.`);
  });

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/routes/feedbackRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = (db) => {
  const { feedbackModel } = db;

  router.get('/', async (req, res) => {
    const feedback = await feedbackModel.getList();
    return res.json({ data: feedback });
  });

  router.post('/', (req, res) => {
    const feedback = req.body.feedback;
    if (!feedback) {
      return res.send('You must provide feedback.');
    }
    return res.send(`Thanks for your posted feedback: ${feedback}`);
  });

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/models/FeedbackModel.js:

```js
const fs = require('fs');
const util = require('util');

const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);

/**
 * Logic for reading and writing feedback data
 */
class FeedbackModel {
  /**
   * Constructor
   * @param {*} datafile Path to a JSOn file that contains the feedback data
   */
  constructor(datafile) {
    this.datafile = datafile;
  }

  /**
   * Get all feedback items
   */
  async getList() {
    const data = await this.getData();
    return data;
  }

  /**
   * Add a new feedback item
   * @param {*} name The name of the user
   * @param {*} title The title of the feedback message
   * @param {*} message The feedback message
   */
  async addEntry(name, email, title, message) {
    const data = (await this.getData()) || [];
    data.unshift({ name, email, title, message });
    return writeFile(this.datafile, JSON.stringify(data));
  }

  /**
   * Fetches feedback data from the JSON file provided to the constructor
   */
  async getData() {
    const data = await readFile(this.datafile, 'utf8');
    if (!data) return [];
    return JSON.parse(data);
  }
}

module.exports = FeedbackModel;

```

### src-AI-Software/my_projects/01_building_a_website/models/SpeakerModel.js:

```js
const fs = require('fs');
const util = require('util');

/**
 * We want to use async/await with fs.readFile - util.promisfy gives us that
 */
const readFile = util.promisify(fs.readFile);

/**
 * Logic for fetching speakers information
 */
class SpeakerModel {
  /**
   * Constructor
   * @param {*} datafile Path to a JSOn file that contains the speakers data
   */
  constructor(datafile) {
    this.datafile = datafile;
  }

  /**
   * Returns a list of speakers name and short name
   */
  async getNames() {
    const data = await this.getData();

    // We are using map() to transform the array we get into another one
    return data.map((speaker) => {
      return { name: speaker.name, shortname: speaker.shortname };
    });
  }

  /**
   * Get all artwork
   */
  async getAllArtwork() {
    const data = await this.getData();

    // Array.reduce() is used to traverse all speakers and
    // create an array that contains all artwork
    const artwork = data.reduce((acc, elm) => {
      if (elm.artwork) {
        // eslint-disable-next-line no-param-reassign
        acc = [...acc, ...elm.artwork];
      }
      return acc;
    }, []);
    return artwork;
  }

  /**
   * Get all artwork of a given speaker
   * @param {*} shortname The speakers short name
   */
  async getArtworkForSpeaker(shortname) {
    const data = await this.getData();
    const speaker = data.find((elm) => {
      return elm.shortname === shortname;
    });
    if (!speaker || !speaker.artwork) return null;
    return speaker.artwork;
  }

  /**
   * Get speaker information provided a shortname
   * @param {*} shortname
   */
  async getSpeaker(shortname) {
    const data = await this.getData();
    const speaker = data.find((elm) => {
      return elm.shortname === shortname;
    });
    if (!speaker) return null;
    return {
      title: speaker.title,
      name: speaker.name,
      shortname: speaker.shortname,
      description: speaker.description,
    };
  }

  /**
   * Returns a list of speakers with only the basic information
   */
  async getListShort() {
    const data = await this.getData();
    return data.map((speaker) => {
      return {
        name: speaker.name,
        shortname: speaker.shortname,
        title: speaker.title,
      };
    });
  }

  /**
   * Get a list of speakers
   */
  async getList() {
    const data = await this.getData();
    return data.map((speaker) => {
      return {
        name: speaker.name,
        shortname: speaker.shortname,
        title: speaker.title,
        summary: speaker.summary,
      };
    });
  }

  /**
   * Fetches speakers data from the JSON file provided to the constructor
   */
  async getData() {
    const data = await readFile(this.datafile, 'utf8');
    return JSON.parse(data).speakers;
  }
}

module.exports = SpeakerModel;

```

### src-AI-Software/my_projects/01_building_a_website/data/feedback.json:

```json
[
    {
        "name": "Frank",
        "email": "frank-smith@gmail.com",
        "title": "Best Meetup Ever",
        "message": "I really love this meetup. Please don't let it end."
    },
    {
        "name": "Jane",
        "email": "jane-miller@gmail.com",
        "title": "Meeting Time",
        "message": "Would you consider moving the meeting time 30 minutes to about 6pm. It's tough to make it to the meetings on time right after work."
    },
    {
        "name": "Roy",
        "email": "roy-jones@gmail.com",
        "title": "Great Speaker",
        "message": "I really enjoyed the speaker this month. Would love to hear another presentation."
    }
]
```

### src-AI-Software/my_projects/01_building_a_website/data/speakers.json:

```json
{
    "speakers": [
        {
            "title": "Art in Full Bloom",
            "name": "Lorenzo Garcia",
            "shortname": "Lorenzo_Garcia",
            "summary": "Drawing and painting flowers may seem like a first-year art student's assignment, but Lorenzo Garcia brings depth, shadows, light, form and color to new heights with his unique and revolutionary technique of painting on canvas with ceramic glaze. This session is sure to be a hit with mixed media buffs.",
            "description": "<p>Lorenzo was born in Mexico, but grew up in Southern California after his mother immigrated to Los Angeles when he was a year old. His mother worked as a seamstress in the Fashion District and brought home scrap materials for Lorenzo to create his early mixed media art. From that point on, Lorenzo became hooked on creating art from scrap metals, fabrics, wood, canvas, and many others. During his junior year at Bischon Art School in Los Angeles, he perfected his own proprietary method of painting on canvas with ceramic glaze, which he will demonstrate on Monday in his session, 'Art in Full Bloom'.</p><p>Lorenzo paints with an extraordinary amount of color, and prefers to create art centered around nature, animals, and science. Now in his senior year at Bischon, Lorenzo has been creating mixed media totem poles made from old telephone poles, and other recycled materials, and is already planning his next new technique that will likely inspire a trend for years to come.</p>",
            "artwork": [
                "Lorenzo_Garcia_01_tn.jpg",
                "Lorenzo_Garcia_02_tn.jpg",
                "Lorenzo_Garcia_03_tn.jpg",
                "Lorenzo_Garcia_04_tn.jpg"
            ]
        },
        {
            "title": "Deep Sea Wonders",
            "name": "Hilary Goldywynn Post",
            "shortname": "Hillary_Goldwynn",
            "summary": "Hillary is a sophomore art sculpture student at New York University, and has won the major international prizes for painters, including the Divinity Circle and the International Painter's Medal. Hillary's exhibit features paintings that contain only water including waves, deep sea, and river.",
            "description": "<p>Hillary is a sophomore art sculpture student at New York University, and has already won all the major international prizes for new painters, including the Divinity Circle, the International Painter's Medal, and the Academy of Paris Award. Hillary's CAC exhibit features paintings that contain only water images including waves, deep sea, and river.</p><p>An avid water sports participant, Hillary understands the water in many ways in which others do not, or may not ever have the opportunity. Her goal in creating the CAC exhibit was to share with others the beauty, power, and flow of natural bodies of water throughout the world. In addition to the display, Hilary also hosts a session on Tuesday called Deep Sea Wonders, which combines her love of deep sea diving and snorkeling, with instruction for capturing the beauty of underwater explorations on canvas.</p>",
            "artwork": [
                "Hillary_Goldwynn_01_tn.jpg",
                "Hillary_Goldwynn_02_tn.jpg",
                "Hillary_Goldwynn_03_tn.jpg",
                "Hillary_Goldwynn_04_tn.jpg",
                "Hillary_Goldwynn_05_tn.jpg",
                "Hillary_Goldwynn_06_tn.jpg",
                "Hillary_Goldwynn_07_tn.jpg"
            ]
        },
        {
            "title": "The Art of Abstract",
            "name": "Riley Rudolph Rewington",
            "shortname": "Riley_Rewington",
            "summary": "The leader of the MMA artistic movement in his hometown of Portland, Riley Rudolph Rewington draws a crowd wherever he goes. Mixing street performance, video, music, and traditional art, Riley has created some of the most unique and deeply poignant abstract works of his generation.",
            "description": "<p>Riley started out as musician and street performance artist, and now blends painting and photography with audio, video, and computer multimedia to create what he calls 'Music and Multimedia Artworks.' Riley's innovations in using multimedia to express art have created a youth culture movement in his town of Portland, in which he remains at the forefront. In his role as the founder of the MMA art form, Riley has become an inspiration to many up and coming artists. However, the part Riley insists is most important to him, is that he's helped many troubled youth take control of their lives, and create their own unique, positive futuresponse. Seeing kids he's mentored graduate from high school and enroll in college, gives art the purpose that Riley so craves.</p><p>A first-year student at the Roux Academy of Art, Media, and Design, Riley is already changing the face of modern art at the university. Riley's exquisite abstract pieces have no intention of ever being understood, but instead beg the viewer to dream, create, pretend, and envision with their mind's eye. Riley will be speaking on the 'Art of Abstract' during Thursday's schedule.</p>",
            "artwork": [
                "Riley_Rewington_01_tn.jpg",
                "Riley_Rewington_02_tn.jpg",
                "Riley_Rewington_03_tn.jpg",
                "Riley_Rewington_04_tn.jpg",
                "Riley_Rewington_05_tn.jpg",
                "Riley_Rewington_06_tn.jpg"
            ]
        }
    ]
}
```

![image](https://github.com/user-attachments/assets/a6f2fc32-7ba0-4f46-9bdb-342078bf08fa)
![image](https://github.com/user-attachments/assets/eac92e6e-069a-4472-a0ef-adbff6602620)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/3890dc07-eec2-4fd3-8b34-1e266af0ba26">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/81064c5b-fdc4-4504-846a-784b3c80005b">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/d647ef1e-0e9d-45da-b86b-469af2dde404">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/834b7ca1-29ae-4080-94ec-4e0382ae18bc">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/16936dac-8573-467a-a200-a0dbd1d67769">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/de4ff443-3877-4e0c-8562-2573d954c9a2">

# #END</details>

<details>
<summary>10. Add a Session Management Middleware </summary>

# Add a Session Management Middleware

## Install cookie-session

```js
npm install cookie-session
```

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use('/', routes({ feedbackModel, speakersModel }));

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/homeRoutes.js:

```js
const express = require('express');

const speakersRoutes = require('./speakersRoutes');
const feedbackRoutes = require('./feedbackRoutes');

const router = express.Router();

module.exports = (db) => {
  router.get('/', (req, res) => {
    if (!req.session.visitcount) {
      req.session.visitcount = 0;
    }
    req.session.visitcount += 1;
    console.log(`Number of visits: ${req.session.visitcount}`);

    const context = {
      pageTitle: 'Welcome',
      name: 'Roux Meetups',
    };
    res.render('pages/index', context);
  });

  router.use('/speakers', speakersRoutes(db));
  router.use('/feedback', feedbackRoutes(db));

  return router;
};

```

![image](https://github.com/user-attachments/assets/765e3f6b-23ac-4a8a-86e0-1c74f3e95e88)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/4827a3c6-588e-4d07-bb42-edfc54cbc26c">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/ad304c1d-1b9f-4661-8828-8210b1898251">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/899e3649-a49c-4cd3-8557-1b12d3fa072e">

# #END</details>

<details>
<summary>11. EJS - Create a Base Template with Partials </summary>

# EJS - Create a Base Template with Partials

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use('/', routes({ feedbackModel, speakersModel }));

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/homeRoutes.js:

```js
const express = require('express');

const speakersRoutes = require('./speakersRoutes');
const feedbackRoutes = require('./feedbackRoutes');

const router = express.Router();

module.exports = (db) => {
  router.get('/', (req, res) => {
    const context = {
      pageTitle: 'Welcome',
      name: 'Roux Meetups',
      template: 'index',
    };
    res.render('layouts/base', context);
  });

  router.use('/speakers', speakersRoutes(db));
  router.use('/feedback', feedbackRoutes(db));

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/views/layouts/base.ejs:

```ejs
<!doctype html>
<html lang="en" data-bs-theme="auto">
  <head>
    <script src="/assets/js/color-modes.js"></script>

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title><%= name %>--<%= pageTitle %></title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3" />
    <link href="/assets/dist/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Custom styles for this template -->
    <link href="/css/carousel.css" rel="stylesheet" />
  </head>
  <body>
    <!--
    ==================================================
    block - Toggle Button
    ==================================================
    -->

    <%- include(`./base__partials/base__toggle`) %>

    <!--
    ==================================================
    endblock - Toggle Button
    ==================================================
    -->

    <!--
    ==================================================
    block - Navbar
    ==================================================
    -->

    <%- include(`./base__partials/base__nav`) %>

    <!--
    ==================================================
    endblock - Navbar
    ==================================================
    -->

    <main>
      <!--
    ==================================================
    block - Content
    ==================================================
    -->

    <%- include(`../pages/${template}`) %>

      <!--
    ==================================================
    endblock - Content
    ==================================================
    -->

      <!--
    ==================================================
    block - Footer
    ==================================================
    -->

    <%- include(`./base__partials/base__footer`) %>

      <!--
    ==================================================
    endblock - Footer
    ==================================================
    --></main>
    <script src="/assets/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/index.ejs:

```ejs
<!--
==================================================
block - Carousel Slider
==================================================
-->

<%- include(`./index__partials/index__carousel`) %>

<!--
==================================================
endblock - Carousel Slider
==================================================
-->

<!--
==================================================
block - Speakers
==================================================
-->

<%- include(`./index__partials/index__speakers.ejs`) %>

<!--
==================================================
endblock - Speakers
==================================================
-->

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/index__partials/index__speakers.ejs:

```ejs
<!--
==================================================
block - Speakers
==================================================
-->

<div class="container marketing">
  <!-- Three columns of text below the carousel -->
  <div class="row">
    <!-- /.col-lg-4 -->
    <div class="col-lg-4">
      <img
        src="./images/Hillary_Goldwynn_tn.jpg"
        alt="carousel 2"
        width="50%"
        class="bd-placeholder-img rounded-circle"
      />
      <h2 class="fw-normal">Hilliary Goldwynn</h2>
      <p>
        Some representative placeholder content for the three columns of text below the carousel.
        This is the first column.
      </p>
      <p>
        <a class="btn btn-secondary" href="#">View details &raquo;</a>
      </p>
    </div>
    <!-- /.col-lg-4 -->
    <div class="col-lg-4">
      <img
        src="./images/Lorenzo_Garcia_tn.jpg"
        alt="carousel 2"
        width="50%"
        class="bd-placeholder-img rounded-circle"
      />
      <h2 class="fw-normal">Lorenzo Garcia</h2>
      <p>
        Another exciting bit of representative placeholder content. This time, we've moved on to the
        second column.
      </p>
      <p>
        <a class="btn btn-secondary" href="#">View details &raquo;</a>
      </p>
    </div>
    <!-- /.col-lg-4 -->
    <div class="col-lg-4">
      <img
        src="./images/Riley_Rewington_tn.jpg"
        alt="carousel 2"
        width="50%"
        class="bd-placeholder-img rounded-circle"
      />
      <h2 class="fw-normal">Riley Rewington</h2>
      <p>And lastly this, the third column of representative placeholder content.</p>
      <p>
        <a class="btn btn-secondary" href="#">View details &raquo;</a>
      </p>
    </div>
  </div>

  <!--
  ==================================================
  block - Features
  ==================================================
  -->

  <%- include(`./index__features`) %>

  <!--
  ==================================================
  endblock - Features
  ==================================================
  -->
</div>
<!--
==================================================
endblock - Speakers
==================================================
-->

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/index__partials/index__features.ejs:

```ejs
<!--
  ==================================================
  block - Features
  ==================================================
  -->
  <hr class="featurette-divider" />

  <div class="row featurette">
    <div class="col-md-7">
      <h2 class="featurette-heading fw-normal lh-1">
        Who are we?
        <span class="text-body-secondary">It’ll blow your mind.</span>
      </h2>
      <p class="lead">
        The Roux Academy gets thousands of submissions every year for
        artists interesting in participating in the CAC exhibits, and
        selects approximately 200 distinct pieces of contemporary art for
        display in their collective exhibit.
      </p>
    </div>
    <div class="col-md-5">
      <img src="./images/artwork/Hillary_Goldwynn_03.jpg" alt="carousel 1" width="500" height="500"  class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"/>
    </div>
  </div>

  <hr class="featurette-divider" />

  <div class="row featurette">
    <div class="col-md-7 order-md-2">
      <h2 class="featurette-heading fw-normal lh-1">
        What we do.
        <span class="text-body-secondary">See for yourself.</span>
      </h2>
      <p class="lead">
        Each Featured Artist has an opportunity to speak at one of our
        meetups and share his or her vision, perspective, and techniques
        with attendees on a more personal level than at our large
        conference. While you attend the conference, head over to our gallery where you can check out some
      of the work from our speakers.
      </p>
    </div>
    <div class="col-md-5">
      <img src="./images/artwork/Hillary_Goldwynn_07.jpg" alt="carousel 1" width="500" height="500"  class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"/>
    </div>
  </div>

  <hr class="featurette-divider" />

  <div class="row featurette">
    <div class="col-md-7">
      <h2 class="featurette-heading fw-normal lh-1">
        And lastly, Who should come?
        <span class="text-body-secondary">Checkmate.</span>
      </h2>
      <p class="lead">
      <ul class="sidebar-body">
          <li>Anybody interested in art and the creative industry</li>
          <li>Painters, sculptors, photographers and graphic artists</li>
          <li>Those interested in meeting and making a connection with others in the local art scene.</li>
      </ul>
      </p>
    </div>
      <div class="col-md-5">
          <img src="./images/artwork/Hillary_Goldwynn_02.jpg" alt="carousel 1" width="500" height="500"  class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"/>
      </div>
      </div>

  <hr class="featurette-divider" />

  <!--
  ==================================================
  endblock - Features
  ==================================================
  -->
```

![image](https://github.com/user-attachments/assets/c9ac5612-e4ff-4e0f-8c04-4eafe185cbcd)
![image](https://github.com/user-attachments/assets/fe5b2ba9-60dd-495f-9106-e511b7a39503)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/ab547ee5-5dc0-4afb-96bc-0e03a49835e4">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/8a35d699-5c1b-4a0b-8b47-51218d6138a9">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/a9be5e53-015a-44e4-9035-52fde6b0634b">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/a0ccd4ad-b071-4912-8cab-57bdbb0290af">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/897ce6cf-0df0-4daa-ab05-e7b2441782a3">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/973e5174-5616-4817-a73e-5208b4a11770">

# #END</details>

<details>
<summary>12. EJS - Create Global Template Variables using Middlewares and app.locals </summary>

# EJS - Create Global Template Variables using Middlewares and app.locals

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    console.log(res.locals.speakersNames);
    return next();
  } catch (err) {
    return next(err);
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/homeRoutes.js:

```js
const express = require('express');

const speakersRoutes = require('./speakersRoutes');
const feedbackRoutes = require('./feedbackRoutes');

const router = express.Router();

module.exports = (db) => {
  router.get('/', (req, res) => {
    const context = {
      pageTitle: 'Welcome',
      name: 'Roux Meetups',
      template: 'index',
    };
    res.render('layouts/base', context);
  });

  router.use('/speakers', speakersRoutes(db));
  router.use('/feedback', feedbackRoutes(db));

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/views/layouts/base.ejs:

```ejs
<!doctype html>
<html lang="en" data-bs-theme="auto">
  <head>
    <script src="/assets/js/color-modes.js"></script>

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title><%= siteName %>--<%= pageTitle %></title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3" />
    <link href="/assets/dist/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Custom styles for this template -->
    <link href="/css/carousel.css" rel="stylesheet" />
  </head>
  <body>
    <!--
    ==================================================
    block - Toggle Button
    ==================================================
    -->

    <%- include(`./base__partials/base__toggle`) %>

    <!--
    ==================================================
    endblock - Toggle Button
    ==================================================
    -->

    <!--
    ==================================================
    block - Navbar
    ==================================================
    -->

    <%- include(`./base__partials/base__nav`) %>

    <!--
    ==================================================
    endblock - Navbar
    ==================================================
    -->

    <main>
      <!--
    ==================================================
    block - Content
    ==================================================
    -->

    <%- include(`../pages/${template}`) %>

      <!--
    ==================================================
    endblock - Content
    ==================================================
    -->

      <!--
    ==================================================
    block - Footer
    ==================================================
    -->

    <%- include(`./base__partials/base__footer`) %>

      <!--
    ==================================================
    endblock - Footer
    ==================================================
    --></main>
    <script src="/assets/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/index.ejs:

```ejs
<!--
==================================================
block - Carousel Slider
==================================================
-->

<%- include(`./index__partials/index__carousel`) %>

<!--
==================================================
endblock - Carousel Slider
==================================================
-->

<h2><%= siteName %></h2>
<h3><%= newGreeting %>, Welcome to our site!</h3>

<!--
==================================================
block - Speakers
==================================================
-->

<%- include(`./index__partials/index__speakers.ejs`) %>

<!--
==================================================
endblock - Speakers
==================================================
-->

```

![image](https://github.com/user-attachments/assets/7b65e79c-bbe5-4e28-b9f0-1f3369578897)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/a3167d4a-4a66-4fb6-a475-b892f9e4299c">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/305b68b0-9e16-4922-b067-eaaab17ba603">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/4857d046-c970-4dca-8df8-84924042680c">

# #END</details>

<details>
<summary>13. EJS - Looping through Lists in Templates </summary>

# EJS - Looping through Lists in Templates

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    // console.log(res.locals.speakersNames);
    return next();
  } catch (err) {
    return next(err);
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/homeRoutes.js:

```js
const express = require('express');

const speakersRoutes = require('./speakersRoutes');
const feedbackRoutes = require('./feedbackRoutes');

const router = express.Router();

module.exports = (db) => {
  const { speakersModel } = db;

  router.get('/', async (req, res) => {
    const topSpeakers = await speakersModel.getList();
    console.log(topSpeakers);

    const context = {
      pageTitle: 'Welcome',
      name: 'Roux Meetups',
      template: 'index',
      topSpeakers,
    };
    res.render('layouts/base', context);
  });

  router.use('/speakers', speakersRoutes(db));
  router.use('/feedback', feedbackRoutes(db));

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/views/layouts/base__partials/base__nav.ejs:

```ejs
<!--
    ==================================================
    block - Navbar
    ==================================================
    -->

<header data-bs-theme="dark">
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="/"><%= name %></a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarCollapse"
        aria-controls="navbarCollapse"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/">Home</a>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Speakers
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="/speakers">All Speakers</a></li>
              <li><hr class="dropdown-divider" /></li>

              <% speakersNames.forEach(speaker => { %>
                <li><a class="dropdown-item" href="/speakers/<%= speaker.shortname %>"><%= speaker.name %></a></li>
              <% }) %>

            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Feedback</a>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
</header>
<!--
    ==================================================
    endblock - Navbar
    ==================================================
    -->

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/index__partials/index__speakers.ejs:

```ejs
<!--
==================================================
block - Speakers
==================================================
-->

<div class="container marketing">
  <!-- Three columns of text below the carousel -->
  <div class="row">
    <% topSpeakers.forEach(speaker => { %>
    <!-- /.col-lg-4 -->
    <div class="col-lg-4">
      <a href="/speakers/<%= speaker.shortname %>">
        <img
          src="/images/<%= speaker.shortname %>_tn.jpg"
          alt="Photo of <%= speaker.name %>"
          width="50%"
          class="bd-placeholder-img rounded-circle"
        />
      </a>

      <h2 class="fw-normal"><%= speaker.name %></h2>
      <p>
        <%= speaker.summary %>
      </p>
      <p>
        <a class="btn btn-secondary" href="/speakers/<%= speaker.shortname %>">View details &raquo;</a>
      </p>
    </div>
    <% }) %>
  </div>

  <!--
  ==================================================
  block - Features
  ==================================================
  -->

  <%- include(`./index__features`) %>

  <!--
  ==================================================
  endblock - Features
  ==================================================
  -->
</div>
<!--
==================================================
endblock - Speakers
==================================================
-->

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/index.ejs:

```ejs
<!--
==================================================
block - Carousel Slider
==================================================
-->

<%- include(`./index__partials/index__carousel`) %>

<!--
==================================================
endblock - Carousel Slider
==================================================
-->

<!--
==================================================
block - Speakers
==================================================
-->

<%- include(`./index__partials/index__speakers.ejs`) %>

<!--
==================================================
endblock - Speakers
==================================================
-->

```

### src-AI-Software/my_projects/01_building_a_website/data/speakers.json:

```json
{
    "speakers": [
        {
            "title": "Art in Full Bloom",
            "name": "Lorenzo Garcia III",
            "shortname": "Lorenzo_Garcia",
            "summary": "Drawing and painting flowers may seem like a first-year art student's assignment, but Lorenzo Garcia brings depth, shadows, light, form and color to new heights with his unique and revolutionary technique of painting on canvas with ceramic glaze. This session is sure to be a hit with mixed media buffs.",
            "description": "<p>Lorenzo was born in Mexico, but grew up in Southern California after his mother immigrated to Los Angeles when he was a year old. His mother worked as a seamstress in the Fashion District and brought home scrap materials for Lorenzo to create his early mixed media art. From that point on, Lorenzo became hooked on creating art from scrap metals, fabrics, wood, canvas, and many others. During his junior year at Bischon Art School in Los Angeles, he perfected his own proprietary method of painting on canvas with ceramic glaze, which he will demonstrate on Monday in his session, 'Art in Full Bloom'.</p><p>Lorenzo paints with an extraordinary amount of color, and prefers to create art centered around nature, animals, and science. Now in his senior year at Bischon, Lorenzo has been creating mixed media totem poles made from old telephone poles, and other recycled materials, and is already planning his next new technique that will likely inspire a trend for years to come.</p>",
            "artwork": [
                "Lorenzo_Garcia_01_tn.jpg",
                "Lorenzo_Garcia_02_tn.jpg",
                "Lorenzo_Garcia_03_tn.jpg",
                "Lorenzo_Garcia_04_tn.jpg"
            ]
        },
        {
            "title": "Deep Sea Wonders",
            "name": "Hilary Goldywynn Post",
            "shortname": "Hillary_Goldwynn",
            "summary": "Hillary is a sophomore art sculpture student at New York University, and has won the major international prizes for painters, including the Divinity Circle and the International Painter's Medal. Hillary's exhibit features paintings that contain only water including waves, deep sea, and river.",
            "description": "<p>Hillary is a sophomore art sculpture student at New York University, and has already won all the major international prizes for new painters, including the Divinity Circle, the International Painter's Medal, and the Academy of Paris Award. Hillary's CAC exhibit features paintings that contain only water images including waves, deep sea, and river.</p><p>An avid water sports participant, Hillary understands the water in many ways in which others do not, or may not ever have the opportunity. Her goal in creating the CAC exhibit was to share with others the beauty, power, and flow of natural bodies of water throughout the world. In addition to the display, Hilary also hosts a session on Tuesday called Deep Sea Wonders, which combines her love of deep sea diving and snorkeling, with instruction for capturing the beauty of underwater explorations on canvas.</p>",
            "artwork": [
                "Hillary_Goldwynn_01_tn.jpg",
                "Hillary_Goldwynn_02_tn.jpg",
                "Hillary_Goldwynn_03_tn.jpg",
                "Hillary_Goldwynn_04_tn.jpg",
                "Hillary_Goldwynn_05_tn.jpg",
                "Hillary_Goldwynn_06_tn.jpg",
                "Hillary_Goldwynn_07_tn.jpg"
            ]
        },
        {
            "title": "The Art of Abstract",
            "name": "Riley Rudolph Rewington",
            "shortname": "Riley_Rewington",
            "summary": "The leader of the MMA artistic movement in his hometown of Portland, Riley Rudolph Rewington draws a crowd wherever he goes. Mixing street performance, video, music, and traditional art, Riley has created some of the most unique and deeply poignant abstract works of his generation.",
            "description": "<p>Riley started out as musician and street performance artist, and now blends painting and photography with audio, video, and computer multimedia to create what he calls 'Music and Multimedia Artworks.' Riley's innovations in using multimedia to express art have created a youth culture movement in his town of Portland, in which he remains at the forefront. In his role as the founder of the MMA art form, Riley has become an inspiration to many up and coming artists. However, the part Riley insists is most important to him, is that he's helped many troubled youth take control of their lives, and create their own unique, positive futuresponse. Seeing kids he's mentored graduate from high school and enroll in college, gives art the purpose that Riley so craves.</p><p>A first-year student at the Roux Academy of Art, Media, and Design, Riley is already changing the face of modern art at the university. Riley's exquisite abstract pieces have no intention of ever being understood, but instead beg the viewer to dream, create, pretend, and envision with their mind's eye. Riley will be speaking on the 'Art of Abstract' during Thursday's schedule.</p>",
            "artwork": [
                "Riley_Rewington_01_tn.jpg",
                "Riley_Rewington_02_tn.jpg",
                "Riley_Rewington_03_tn.jpg",
                "Riley_Rewington_04_tn.jpg",
                "Riley_Rewington_05_tn.jpg",
                "Riley_Rewington_06_tn.jpg"
            ]
        }
    ]
}
```

![image](https://github.com/user-attachments/assets/2784800d-c283-4b6d-8aab-f74b2901335b)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/cfd2626f-bd45-4ae5-a84e-dd631c49e75a">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/5825644b-b6ea-4577-a911-3c0640f87b92">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/96fd5f56-a296-4154-97a7-c8db16cc6e5a">

# #END</details>

<details>
<summary>14. EJS - Create a Speakers List Page </summary>

# EJS - Create a Speakers List Page

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    // console.log(res.locals.speakersNames);
    return next();
  } catch (err) {
    return next(err);
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/homeRoutes.js:

```js
const express = require('express');

const speakersRoutes = require('./speakersRoutes');
const feedbackRoutes = require('./feedbackRoutes');

const router = express.Router();

module.exports = (db) => {
  const { speakersModel } = db;

  router.get('/', async (req, res) => {
    const topSpeakers = await speakersModel.getList();
    // console.log(topSpeakers);

    const context = {
      pageTitle: 'Welcome',
      name: 'Roux Meetups',
      template: 'index',
      topSpeakers,
    };
    res.render('layouts/base', context);
  });

  router.use('/speakers', speakersRoutes(db));
  router.use('/feedback', feedbackRoutes(db));

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/routes/speakersRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = (db) => {
  const { speakersModel } = db;

  router.get('/', async (req, res) => {
    const speakers = await speakersModel.getList();

    const context = {
      pageTitle: 'Speakers',
      name: 'Roux Meetups',
      template: 'speakers',
      speakers,
    };
    res.render('layouts/base', context);
  });

  router.get('/:shortname', (req, res) => {
    const speakerName = req.params.shortname;
    return res.send(`This is the Speakers Detail Page for speaker: ${speakerName}.`);
  });

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/speakers.ejs:

```ejs
<!--
==================================================
block - Speakers
==================================================
-->

<%- include(`./speakers__partials/speakers__speakers.ejs`) %>

<!--
==================================================
endblock - Speakers
==================================================
-->

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/speakers__partials/speakers__speakers.ejs:

```ejs
<!--
==================================================
block - Speakers
==================================================
-->

<div class="container marketing">
  <!-- Three columns of text below the carousel -->
  <div class="row">
    <% speakers.forEach(speaker => { %>
    <!-- /.col-lg-4 -->
    <div class="col-lg-4">
      <a href="/speakers/<%= speaker.shortname %>">
        <img
          src="/images/<%= speaker.shortname %>_tn.jpg"
          alt="Photo of <%= speaker.name %>"
          width="50%"
          class="bd-placeholder-img rounded-circle"
        />
      </a>

      <h2 class="fw-normal"><%= speaker.name %></h2>
      <p>
        <%= speaker.summary %>
      </p>
      <p>
        <a class="btn btn-secondary" href="/speakers/<%= speaker.shortname %>">View details &raquo;</a>
      </p>
    </div>
    <% }) %>
  </div>

</div>
<!--
==================================================
endblock - Speakers
==================================================
-->

```

### src-AI-Software/my_projects/01_building_a_website/models/SpeakerModel.js:

```js
const fs = require('fs');
const util = require('util');

/**
 * We want to use async/await with fs.readFile - util.promisfy gives us that
 */
const readFile = util.promisify(fs.readFile);

/**
 * Logic for fetching speakers information
 */
class SpeakerModel {
  /**
   * Constructor
   * @param {*} datafile Path to a JSOn file that contains the speakers data
   */
  constructor(datafile) {
    this.datafile = datafile;
  }

  /**
   * Returns a list of speakers name and short name
   */
  async getNames() {
    const data = await this.getData();

    // We are using map() to transform the array we get into another one
    return data.map((speaker) => {
      return { name: speaker.name, shortname: speaker.shortname };
    });
  }

  /**
   * Get all artwork
   */
  async getAllArtwork() {
    const data = await this.getData();

    // Array.reduce() is used to traverse all speakers and
    // create an array that contains all artwork
    const artwork = data.reduce((acc, elm) => {
      if (elm.artwork) {
        // eslint-disable-next-line no-param-reassign
        acc = [...acc, ...elm.artwork];
      }
      return acc;
    }, []);
    return artwork;
  }

  /**
   * Get all artwork of a given speaker
   * @param {*} shortname The speakers short name
   */
  async getArtworkForSpeaker(shortname) {
    const data = await this.getData();
    const speaker = data.find((elm) => {
      return elm.shortname === shortname;
    });
    if (!speaker || !speaker.artwork) return null;
    return speaker.artwork;
  }

  /**
   * Get speaker information provided a shortname
   * @param {*} shortname
   */
  async getSpeaker(shortname) {
    const data = await this.getData();
    const speaker = data.find((elm) => {
      return elm.shortname === shortname;
    });
    if (!speaker) return null;
    return {
      title: speaker.title,
      name: speaker.name,
      shortname: speaker.shortname,
      description: speaker.description,
    };
  }

  /**
   * Returns a list of speakers with only the basic information
   */
  async getListShort() {
    const data = await this.getData();
    return data.map((speaker) => {
      return {
        name: speaker.name,
        shortname: speaker.shortname,
        title: speaker.title,
      };
    });
  }

  /**
   * Get a list of speakers
   */
  async getList() {
    const data = await this.getData();
    return data.map((speaker) => {
      return {
        name: speaker.name,
        shortname: speaker.shortname,
        title: speaker.title,
        summary: speaker.summary,
      };
    });
  }

  /**
   * Fetches speakers data from the JSON file provided to the constructor
   */
  async getData() {
    const data = await readFile(this.datafile, 'utf8');
    return JSON.parse(data).speakers;
  }
}

module.exports = SpeakerModel;

```

### src-AI-Software/my_projects/01_building_a_website/data/speakers.json:

```json
{
    "speakers": [
        {
            "title": "Art in Full Bloom",
            "name": "Lorenzo Garcia III",
            "shortname": "Lorenzo_Garcia",
            "summary": "Drawing and painting flowers may seem like a first-year art student's assignment, but Lorenzo Garcia brings depth, shadows, light, form and color to new heights with his unique and revolutionary technique of painting on canvas with ceramic glaze. This session is sure to be a hit with mixed media buffs.",
            "description": "<p>Lorenzo was born in Mexico, but grew up in Southern California after his mother immigrated to Los Angeles when he was a year old. His mother worked as a seamstress in the Fashion District and brought home scrap materials for Lorenzo to create his early mixed media art. From that point on, Lorenzo became hooked on creating art from scrap metals, fabrics, wood, canvas, and many others. During his junior year at Bischon Art School in Los Angeles, he perfected his own proprietary method of painting on canvas with ceramic glaze, which he will demonstrate on Monday in his session, 'Art in Full Bloom'.</p><p>Lorenzo paints with an extraordinary amount of color, and prefers to create art centered around nature, animals, and science. Now in his senior year at Bischon, Lorenzo has been creating mixed media totem poles made from old telephone poles, and other recycled materials, and is already planning his next new technique that will likely inspire a trend for years to come.</p>",
            "artwork": [
                "Lorenzo_Garcia_01_tn.jpg",
                "Lorenzo_Garcia_02_tn.jpg",
                "Lorenzo_Garcia_03_tn.jpg",
                "Lorenzo_Garcia_04_tn.jpg"
            ]
        },
        {
            "title": "Deep Sea Wonders",
            "name": "Hilary Goldywynn Post",
            "shortname": "Hillary_Goldwynn",
            "summary": "Hillary is a sophomore art sculpture student at New York University, and has won the major international prizes for painters, including the Divinity Circle and the International Painter's Medal. Hillary's exhibit features paintings that contain only water including waves, deep sea, and river.",
            "description": "<p>Hillary is a sophomore art sculpture student at New York University, and has already won all the major international prizes for new painters, including the Divinity Circle, the International Painter's Medal, and the Academy of Paris Award. Hillary's CAC exhibit features paintings that contain only water images including waves, deep sea, and river.</p><p>An avid water sports participant, Hillary understands the water in many ways in which others do not, or may not ever have the opportunity. Her goal in creating the CAC exhibit was to share with others the beauty, power, and flow of natural bodies of water throughout the world. In addition to the display, Hilary also hosts a session on Tuesday called Deep Sea Wonders, which combines her love of deep sea diving and snorkeling, with instruction for capturing the beauty of underwater explorations on canvas.</p>",
            "artwork": [
                "Hillary_Goldwynn_01_tn.jpg",
                "Hillary_Goldwynn_02_tn.jpg",
                "Hillary_Goldwynn_03_tn.jpg",
                "Hillary_Goldwynn_04_tn.jpg"
            ]
        },
        {
            "title": "The Art of Abstract",
            "name": "Riley Rudolph Rewington",
            "shortname": "Riley_Rewington",
            "summary": "The leader of the MMA artistic movement in his hometown of Portland, Riley Rudolph Rewington draws a crowd wherever he goes. Mixing street performance, video, music, and traditional art, Riley has created some of the most unique and deeply poignant abstract works of his generation.",
            "description": "<p>Riley started out as musician and street performance artist, and now blends painting and photography with audio, video, and computer multimedia to create what he calls 'Music and Multimedia Artworks.' Riley's innovations in using multimedia to express art have created a youth culture movement in his town of Portland, in which he remains at the forefront. In his role as the founder of the MMA art form, Riley has become an inspiration to many up and coming artists. However, the part Riley insists is most important to him, is that he's helped many troubled youth take control of their lives, and create their own unique, positive futuresponse. Seeing kids he's mentored graduate from high school and enroll in college, gives art the purpose that Riley so craves.</p><p>A first-year student at the Roux Academy of Art, Media, and Design, Riley is already changing the face of modern art at the university. Riley's exquisite abstract pieces have no intention of ever being understood, but instead beg the viewer to dream, create, pretend, and envision with their mind's eye. Riley will be speaking on the 'Art of Abstract' during Thursday's schedule.</p>",
            "artwork": [
                "Riley_Rewington_01_tn.jpg",
                "Riley_Rewington_02_tn.jpg",
                "Riley_Rewington_03_tn.jpg",
                "Riley_Rewington_04_tn.jpg",
                "Riley_Rewington_05_tn.jpg"
            ]
        }
    ]
}
```


![image](https://github.com/user-attachments/assets/5773c1ff-00c1-4dd2-bbe3-f784627a36ed)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/7eb5ef05-2761-42d3-81f0-917f25424c93">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/f74c94ea-bb5a-4f7a-b8a5-8b3a4ecd6dcc">

# #END</details>

<details>
<summary>15. EJS - Create Speaker Details Page </summary>

# EJS - Create Speaker Details Page

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    // console.log(res.locals.speakersNames);
    return next();
  } catch (err) {
    return next(err);
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/speakersRoutes.js

```js
const express = require('express');

const router = express.Router();

module.exports = (db) => {
  const { speakersModel } = db;

  router.get('/', async (req, res) => {
    const speakers = await speakersModel.getList();

    const context = {
      pageTitle: 'Speakers',
      name: 'Roux Meetups',
      template: 'speakers',
      speakers,
    };
    res.render('layouts/base', context);
  });

  router.get('/:shortname', async (req, res) => {
    const speaker = await speakersModel.getSpeaker(req.params.shortname);
    console.log(speaker);
    const context = {
      pageTitle: 'Speaker Detail',
      name: 'Roux Meetups',
      template: 'speaker-detail',
      speaker,
    };
    res.render('layouts/base', context);
    // return res.send(`This is the Speakers Detail Page for speaker: ${req.params.shortname}.`);
  });

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/speaker-detail.ejs:

```ejs
<!--
  ==================================================
  block - Features
  ==================================================
  -->
<hr class="featurette-divider" />

<div class="row featurette">
  <div class="col-md-7">
    <h2 class="featurette-heading fw-normal lh-1">
      <%= speaker.name %>
      <span class="text-body-secondary"><%= speaker.title %>.</span>
    </h2>
    <p class="lead"><%- speaker.description %>.</p>
  </div>
  <div class="col-md-5">
    <img
      src="/images/<%= speaker.shortname %>.jpg"
      alt="carousel 1"
      width="500"
      height="500"
      class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"
    />
  </div>
</div>

<hr class="featurette-divider" />

<!--
  ==================================================
  endblock - Features
  ==================================================
  -->

```

### src-AI-Software/my_projects/01_building_a_website/models/SpeakerModel.js:

```js
const fs = require('fs');
const util = require('util');

/**
 * We want to use async/await with fs.readFile - util.promisfy gives us that
 */
const readFile = util.promisify(fs.readFile);

/**
 * Logic for fetching speakers information
 */
class SpeakerModel {
  /**
   * Constructor
   * @param {*} datafile Path to a JSOn file that contains the speakers data
   */
  constructor(datafile) {
    this.datafile = datafile;
  }

  /**
   * Returns a list of speakers name and short name
   */
  async getNames() {
    const data = await this.getData();

    // We are using map() to transform the array we get into another one
    return data.map((speaker) => {
      return { name: speaker.name, shortname: speaker.shortname };
    });
  }

  /**
   * Get all artwork
   */
  async getAllArtwork() {
    const data = await this.getData();

    // Array.reduce() is used to traverse all speakers and
    // create an array that contains all artwork
    const artwork = data.reduce((acc, elm) => {
      if (elm.artwork) {
        // eslint-disable-next-line no-param-reassign
        acc = [...acc, ...elm.artwork];
      }
      return acc;
    }, []);
    return artwork;
  }

  /**
   * Get all artwork of a given speaker
   * @param {*} shortname The speakers short name
   */
  async getArtworkForSpeaker(shortname) {
    const data = await this.getData();
    const speaker = data.find((elm) => {
      return elm.shortname === shortname;
    });
    if (!speaker || !speaker.artwork) return null;
    return speaker.artwork;
  }

  /**
   * Get speaker information provided a shortname
   * @param {*} shortname
   */
  async getSpeaker(shortname) {
    const data = await this.getData();
    const speaker = data.find((elm) => {
      return elm.shortname === shortname;
    });
    if (!speaker) return null;
    return {
      title: speaker.title,
      name: speaker.name,
      shortname: speaker.shortname,
      description: speaker.description,
    };
  }

  /**
   * Returns a list of speakers with only the basic information
   */
  async getListShort() {
    const data = await this.getData();
    return data.map((speaker) => {
      return {
        name: speaker.name,
        shortname: speaker.shortname,
        title: speaker.title,
      };
    });
  }

  /**
   * Get a list of speakers
   */
  async getList() {
    const data = await this.getData();
    return data.map((speaker) => {
      return {
        name: speaker.name,
        shortname: speaker.shortname,
        title: speaker.title,
        summary: speaker.summary,
      };
    });
  }

  /**
   * Fetches speakers data from the JSON file provided to the constructor
   */
  async getData() {
    const data = await readFile(this.datafile, 'utf8');
    return JSON.parse(data).speakers;
  }
}

module.exports = SpeakerModel;

```

### src-AI-Software/my_projects/01_building_a_website/data/speakers.json:

```js
{
    "speakers": [
        {
            "title": "Art in Full Bloom",
            "name": "Lorenzo Garcia III",
            "shortname": "Lorenzo_Garcia",
            "summary": "Drawing and painting flowers may seem like a first-year art student's assignment, but Lorenzo Garcia brings depth, shadows, light, form and color to new heights with his unique and revolutionary technique of painting on canvas with ceramic glaze. This session is sure to be a hit with mixed media buffs.",
            "description": "<p>Lorenzo was born in Mexico, but grew up in Southern California after his mother immigrated to Los Angeles when he was a year old. His mother worked as a seamstress in the Fashion District and brought home scrap materials for Lorenzo to create his early mixed media art. From that point on, Lorenzo became hooked on creating art from scrap metals, fabrics, wood, canvas, and many others. During his junior year at Bischon Art School in Los Angeles, he perfected his own proprietary method of painting on canvas with ceramic glaze, which he will demonstrate on Monday in his session, 'Art in Full Bloom'.</p><p>Lorenzo paints with an extraordinary amount of color, and prefers to create art centered around nature, animals, and science. Now in his senior year at Bischon, Lorenzo has been creating mixed media totem poles made from old telephone poles, and other recycled materials, and is already planning his next new technique that will likely inspire a trend for years to come.</p>",
            "artwork": [
                "Lorenzo_Garcia_01_tn.jpg",
                "Lorenzo_Garcia_02_tn.jpg",
                "Lorenzo_Garcia_03_tn.jpg",
                "Lorenzo_Garcia_04_tn.jpg"
            ]
        },
        {
            "title": "Deep Sea Wonders",
            "name": "Hilary Goldywynn Post",
            "shortname": "Hillary_Goldwynn",
            "summary": "Hillary is a sophomore art sculpture student at New York University, and has won the major international prizes for painters, including the Divinity Circle and the International Painter's Medal. Hillary's exhibit features paintings that contain only water including waves, deep sea, and river.",
            "description": "<p>Hillary is a sophomore art sculpture student at New York University, and has already won all the major international prizes for new painters, including the Divinity Circle, the International Painter's Medal, and the Academy of Paris Award. Hillary's CAC exhibit features paintings that contain only water images including waves, deep sea, and river.</p><p>An avid water sports participant, Hillary understands the water in many ways in which others do not, or may not ever have the opportunity. Her goal in creating the CAC exhibit was to share with others the beauty, power, and flow of natural bodies of water throughout the world. In addition to the display, Hilary also hosts a session on Tuesday called Deep Sea Wonders, which combines her love of deep sea diving and snorkeling, with instruction for capturing the beauty of underwater explorations on canvas.</p>",
            "artwork": [
                "Hillary_Goldwynn_01_tn.jpg",
                "Hillary_Goldwynn_02_tn.jpg",
                "Hillary_Goldwynn_03_tn.jpg",
                "Hillary_Goldwynn_04_tn.jpg"
            ]
        },
        {
            "title": "The Art of Abstract",
            "name": "Riley Rudolph Rewington",
            "shortname": "Riley_Rewington",
            "summary": "The leader of the MMA artistic movement in his hometown of Portland, Riley Rudolph Rewington draws a crowd wherever he goes. Mixing street performance, video, music, and traditional art, Riley has created some of the most unique and deeply poignant abstract works of his generation.",
            "description": "<p>Riley started out as musician and street performance artist, and now blends painting and photography with audio, video, and computer multimedia to create what he calls 'Music and Multimedia Artworks.' Riley's innovations in using multimedia to express art have created a youth culture movement in his town of Portland, in which he remains at the forefront. In his role as the founder of the MMA art form, Riley has become an inspiration to many up and coming artists. However, the part Riley insists is most important to him, is that he's helped many troubled youth take control of their lives, and create their own unique, positive futuresponse. Seeing kids he's mentored graduate from high school and enroll in college, gives art the purpose that Riley so craves.</p><p>A first-year student at the Roux Academy of Art, Media, and Design, Riley is already changing the face of modern art at the university. Riley's exquisite abstract pieces have no intention of ever being understood, but instead beg the viewer to dream, create, pretend, and envision with their mind's eye. Riley will be speaking on the 'Art of Abstract' during Thursday's schedule.</p>",
            "artwork": [
                "Riley_Rewington_01_tn.jpg",
                "Riley_Rewington_02_tn.jpg",
                "Riley_Rewington_03_tn.jpg",
                "Riley_Rewington_04_tn.jpg",
                "Riley_Rewington_05_tn.jpg"
            ]
        }
    ]
}
```

![image](https://github.com/user-attachments/assets/8eb39bcc-4395-4bd4-8ee8-0575995e17cd)
![image](https://github.com/user-attachments/assets/f2091722-5e40-4925-89a9-90bb33516acb)
![image](https://github.com/user-attachments/assets/b6456dd5-7b91-4f35-90ad-f031eb2c128c)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/97b9e5c5-ace3-4631-bb42-ad406c318d22">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/0c55c09c-34c4-4a03-9399-a5043edd4662">

# #END</details>

<details>
<summary>16. Express Errors - Error Handling in Express </summary>

# Express Errors - Error Handling in Express

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.get('/throw', (req, res, next) => {
  // const err = new Error('Not Found');
  // err.status = 404;
  // next(err);

  // throw new Error('This is a test error'); // This will crash the server, don't throw errors directly without next

  setTimeout(() => {
    return next(new Error('This is a test error'));
  }, 500);
});

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    return next();
  } catch (err) {
    return next(err); // Good practice to catch errors and pass them to the next middleware
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log('Ctrl + C to stop');
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/homeRoutes.js:

```js
const express = require('express');

const speakersRoutes = require('./speakersRoutes');
const feedbackRoutes = require('./feedbackRoutes');

const router = express.Router();

module.exports = (db) => {
  const { speakersModel } = db;

  router.get('/', async (req, res, next) => {
    try {
      const topSpeakers = await speakersModel.getList();
      const context = {
        pageTitle: 'Welcome',
        name: 'Roux Meetups',
        template: 'index',
        topSpeakers,
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  router.use('/speakers', speakersRoutes(db));
  router.use('/feedback', feedbackRoutes(db));

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/routes/speakersRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = (db) => {
  const { speakersModel } = db;

  router.get('/', async (req, res, next) => {
    try {
      const speakers = await speakersModel.getList();
      const context = {
        pageTitle: 'Speakers',
        name: 'Roux Meetups',
        template: 'speakers',
        speakers,
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  router.get('/:shortname', async (req, res, next) => {
    try {
      const speaker = await speakersModel.getSpeaker(req.params.shortname);
      console.log(speaker);
      const context = {
        pageTitle: 'Speaker Detail',
        name: 'Roux Meetups',
        template: 'speaker-detail',
        speaker,
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/routes/feedbackRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = (db) => {
  const { feedbackModel } = db;

  router.get('/', async (req, res, next) => {
    try {
      const feedback = await feedbackModel.getList();
      return res.json({ data: feedback });
    } catch (err) {
      return next(err);
    }
  });

  router.post('/', (req, res, next) => {
    try {
      const feedback = req.body.feedback;
      if (!feedback) {
        return res.send('You must provide feedback.');
      }
      return res.send(`Thanks for your posted feedback: ${feedback}`);
    } catch (err) {
      return next(err);
    }
  });

  return router;
};

```

![image](https://github.com/user-attachments/assets/7f714261-7491-43d9-af8f-6484821e3f4e)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/e8a2e0c8-aad7-4237-8ee4-712dd871570d">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/604443a6-75f8-494c-a704-a1b51929617a">
<img width="1442" alt="image" src="https://github.com/user-attachments/assets/ea4b2af4-b778-40bc-aab5-8b50ec0e9226">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/9b1ee10e-253d-49ed-bd54-8aacaeabe129">

# #END</details>

<details>
<summary>17. Express Errors - Create an Error Page with Error-handling Middleware </summary>

# Express Errors - Create an Error Page with Error-handling Middleware

## Install http-errors

```x
npm install http-errors
```

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');
const createError = require('http-errors');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    return next();
  } catch (err) {
    return next(err);
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

// createError middleware
app.use((req, res, next) => {
  // console.error(err.stack);
  // res.status(404).send('Page not Found!');
  return next(createError(404, 'Page not found'));
});

// Error-handling middleware
app.use((err, req, res, next) => {
  res.locals.message = err.message || 'The page you requested was not found.';
  const status = err.status || 500;
  res.locals.status = status;
  return res.status(status).render('404');
});

app.listen(PORT, () => {
  try {
    console.log(`Server running on port ${PORT}`);
    console.log('Ctrl + C to stop');
  } catch (err) {
    console.error(err.stack);
    throw new Error(`Something broke: ${err}`);
  }
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/homeRoutes.js:

```js
const express = require('express');

const speakersRoutes = require('./speakersRoutes');
const feedbackRoutes = require('./feedbackRoutes');

const router = express.Router();

module.exports = (db) => {
  const { speakersModel } = db;

  router.get('/', async (req, res, next) => {
    // return next(new Error('some Error'));
    try {
      const topSpeakers = await speakersModel.getList();
      const context = {
        pageTitle: 'Welcome',
        name: 'Roux Meetups',
        template: 'index',
        topSpeakers,
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  router.use('/speakers', speakersRoutes(db));
  router.use('/feedback', feedbackRoutes(db));

  // Register the unhandled route middleware
  function handleUnhandledRoutes(req, res, next) {
    // res.status(404).send('Page not found');
    return next(new Error('The Route does not Exist!'));
  }
  router.use(handleUnhandledRoutes);

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/routes/speakersRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = (db) => {
  const { speakersModel } = db;

  router.get('/', async (req, res, next) => {
    try {
      const speakers = await speakersModel.getList();
      const context = {
        pageTitle: 'Speakers',
        name: 'Roux Meetups',
        template: 'speakers',
        speakers,
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  router.get('/:shortname', async (req, res, next) => {
    try {
      const speaker = await speakersModel.getSpeaker(req.params.shortname);
      console.log(speaker);
      const context = {
        pageTitle: 'Speaker Detail',
        name: 'Roux Meetups',
        template: 'speaker-detail',
        speaker,
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  // Register the unhandled route middleware
  function handleUnhandledRoutes(req, res, next) {
    // res.status(404).send('Page not found');
    return next(new Error('The Route does not Exist!'));
  }
  router.use(handleUnhandledRoutes);

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/routes/feedbackRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = (db) => {
  const { feedbackModel } = db;

  router.get('/', async (req, res, next) => {
    try {
      const feedback = await feedbackModel.getList();
      return res.json({ data: feedback });
    } catch (err) {
      return next(err);
    }
  });

  router.post('/', (req, res, next) => {
    try {
      const feedback = req.body.feedback;
      if (!feedback) {
        return res.send('You must provide feedback.');
      }
      return res.send(`Thanks for your posted feedback: ${feedback}`);
    } catch (err) {
      return next(err);
    }
  });

  // Register the unhandled route middleware
  function handleUnhandledRoutes(req, res, next) {
    // res.status(404).send('Page not found');
    return next(new Error('The Route does not Exist!'));
  }
  router.use(handleUnhandledRoutes);

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/views/404.ejs:

```ejs
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Error <%= status %> | An error occured!</title>
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
    />
    <style>
      body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        background-color: #f8f9fa;
      }

      .error-container {
        text-align: center;
      }

      .error-code {
        font-size: 6rem;
        font-weight: bold;
        color: #dc3545;
      }

      .error-message {
        font-size: 2rem;
        margin-top: 1rem;
      }
    </style>
  </head>

  <body>
    <div class="error-container">
      <h1 class="error-code"><%= status %> | <small>ERROR</small></h1>
      <p class="error-message"><%= message %></p>
    </div>
  </body>
</html>

```

![image](https://github.com/user-attachments/assets/906a9232-6721-4457-a42b-34873397136b)
![image](https://github.com/user-attachments/assets/ca528d67-c3b2-4c25-aded-1eec8e021ebf)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/49997815-ce1e-49ae-93c2-33c4f715c154">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/e0865123-6576-455a-b475-70e6a108021a">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/41f22d15-0d68-4d86-a097-0ab3499b2d08">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/2c7cf33d-0092-4efc-87a6-19c1141512d9">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/17c48b84-c9e9-4357-9986-129b76d5ae99">

# #END</details>

<details>
<summary>18. Express Forms - Create Feedback Form and Message Template </summary>

# Express Forms - Create Feedback Form and Message Template 

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');
const createError = require('http-errors');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    return next();
  } catch (err) {
    return next(err);
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

// createError middleware
app.use((req, res, next) => {
  // console.error(err.stack);
  // res.status(404).send('Page not Found!');
  return next(createError(404, 'Page not found'));
});

// Error-handling middleware
app.use((err, req, res, next) => {
  res.locals.message = err.message || 'The page you requested was not found.';
  const status = err.status || 500;
  res.locals.status = status;
  return res.status(status).render('404');
});

app.listen(PORT, () => {
  try {
    console.log(`Server running on port ${PORT}`);
    console.log('Ctrl + C to stop');
  } catch (err) {
    console.error(err.stack);
    throw new Error(`Something broke: ${err}`);
  }
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/feedbackRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = (db) => {
  const { feedbackModel } = db;

  router.get('/', async (req, res, next) => {
   try {
      const feedback = await feedbackModel.getList();
      const context = {
        pageTitle: 'Feedback',
        name: 'Roux Meetups',
        template: 'feedback',
        feedback
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  router.post('/', (req, res, next) => {
    try {
      const feedback = req.body.feedback;
      if (!feedback) {
        return res.send('You must provide feedback.');
      }
      return res.send(`Thanks for your posted feedback: ${feedback}`);
    } catch (err) {
      return next(err);
    }
  });

  // Register the unhandled route middleware
  function handleUnhandledRoutes(req, res, next) {
    // res.status(404).send('Page not found');
    return next(new Error('The Route does not Exist!'));
  }
  router.use(handleUnhandledRoutes);

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/views/layouts/base__partials/base__nav.ejs:

```ejs
<!--
    ==================================================
    block - Navbar
    ==================================================
    -->

<header data-bs-theme="dark">
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="/"><%= name %></a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarCollapse"
        aria-controls="navbarCollapse"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/">Home</a>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Speakers
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="/speakers">All Speakers</a></li>
              <li><hr class="dropdown-divider" /></li>

              <% speakersNames.forEach(speaker => { %>
                <li><a class="dropdown-item" href="/speakers/<%= speaker.shortname %>"><%= speaker.name %></a></li>
              <% }) %>

            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/feedback">Feedback</a>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
</header>
<!--
    ==================================================
    endblock - Navbar
    ==================================================
    -->

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/feedback.ejs:

```ejs
<div class="container">

<div class="row my-5">
  <div class="col-6">
    <h2>Enter a Feedback</h2>
    <form>
      <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" class="form-control" id="name" name="name" aria-describedby="textHelp">
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email address</label>
        <input type="email" class="form-control" id="email" name="email" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input type="text" class="form-control" id="title" name="title" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="message" class="form-label">Message</label>
        <textarea class="form-control" id="message" name="message" rows="3"></textarea>
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>

  <div class="col-6">
    <h2>Feedbacks</h2>
    <div class="accordion" id="accordionExample">
      <% feedback.forEach(function (items) { %>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#<%= items.name %>"
              aria-expanded="false"
              aria-controls="collapseThree"
            >
              <%= items.name %> | <%= items.email %>
            </button>
          </h2>
        </div>
        <div id="<%= items.name %>" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <h3><strong><%= items.title %></strong></h3>
            <p><%= items.message %></p>
          </div>
        </div>
      <% }) %>
    </div>
  </div>
</div>

```

### src-AI-Software/my_projects/01_building_a_website/data/feedback.json:

```json
[
    {
        "name": "Frank",
        "email": "frank-smith@gmail.com",
        "title": "Best Meetup Ever",
        "message": "I really love this meetup. Please don't let it end."
    },
    {
        "name": "Jane",
        "email": "jane-miller@gmail.com",
        "title": "Meeting Time",
        "message": "Would you consider moving the meeting time 30 minutes to about 6pm. It's tough to make it to the meetings on time right after work."
    },
    {
        "name": "Roy",
        "email": "roy-jones@gmail.com",
        "title": "Great Speaker",
        "message": "I really enjoyed the speaker this month. Would love to hear another presentation."
    }
]
```

![image](https://github.com/user-attachments/assets/b809b3e4-5883-41b7-82af-329d401809d1)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/f2556fa5-bedc-4312-8df5-69be20f7d818">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/578eec09-f212-4b88-bfea-4044e6270eef">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/07f14f95-1e0b-459a-9a26-af7d75988852">

# #END</details>

<details>
<summary>19. Express Forms - Handling POST requests </summary>

# Express Forms - Handling POST requests

## Install body-parser

```js
npm install body-parser
```

### src-AI-Software/my_projects/01_building_a_website/package.json:

```json
{
  "name": "01_building_a_website",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon --ignore feedback.json server.js"
  },
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "body-parser": "^1.20.2",
    "cookie-session": "^2.1.0",
    "ejs": "^3.1.10",
    "express": "^4.19.2",
    "http-errors": "^2.0.0",
    "nodemon": "^3.1.4"
  },
  "devDependencies": {
    "@eslint/js": "^9.7.0",
    "eslint": "^9.7.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-prettier": "^5.2.1",
    "globals": "^15.8.0",
    "prettier": "^3.3.3"
  }
}

```

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');
const createError = require('http-errors');
const bodyParser = require('body-parser');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

// app.use(express.json());
// app.use(express.urlencoded({ extended: true }));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    return next();
  } catch (err) {
    return next(err);
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

// createError middleware
app.use((req, res, next) => {
  // console.error(err.stack);
  // res.status(404).send('Page not Found!');
  return next(createError(404, 'Page not found'));
});

// Error-handling middleware
app.use((err, req, res, next) => {
  res.locals.message = err.message || 'The page you requested was not found.';
  const status = err.status || 500;
  res.locals.status = status;
  return res.status(status).render('404');
});

app.listen(PORT, () => {
  try {
    console.log(`Server running on port ${PORT}`);
    console.log('Ctrl + C to stop');
  } catch (err) {
    console.error(err.stack);
    throw new Error(`Something broke: ${err}`);
  }
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/feedbackRoutes.js:

```js
const express = require('express');

const router = express.Router();

module.exports = (db) => {
  const { feedbackModel } = db;

  router.get('/', async (req, res, next) => {
    try {
      const feedback = await feedbackModel.getList();
      const context = {
        pageTitle: 'Feedback',
        name: 'Roux Meetups',
        template: 'feedback',
        feedback,
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  router.post('/', (req, res, next) => {
    try {
      const message = req.body.message;
      if (!message) {
        return res.send('You must provide feedback.');
      }
      console.log(req.body);
      return res.send(`Thanks for your posted feedback:\n\n ${message}`);
    } catch (err) {
      return next(err);
    }
  });

  // Register the unhandled route middleware
  function handleUnhandledRoutes(req, res, next) {
    // res.status(404).send('Page not found');
    return next(new Error('The Route does not Exist!'));
  }
  router.use(handleUnhandledRoutes);

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/feedback.ejs:

```ejs
<div class="container">

<div class="row my-5">
  <div class="col-6">
    <h2>Enter a Feedback</h2>
    <form method="POST" action="/feedback">
      <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" class="form-control" id="name" name="name" aria-describedby="textHelp">
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email address</label>
        <input type="email" class="form-control" id="email" name="email" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input type="text" class="form-control" id="title" name="title" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="message" class="form-label">Message</label>
        <textarea class="form-control" id="message" name="message" rows="3"></textarea>
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>

  <div class="col-6">
    <h2>Feedbacks</h2>
    <div class="accordion" id="accordionExample">
      <% feedback.forEach(function (items) { %>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#<%= items.name %>"
              aria-expanded="false"
              aria-controls="collapseThree"
            >
              <%= items.name %> | <%= items.email %>
            </button>
          </h2>
        </div>
        <div id="<%= items.name %>" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <h3><strong><%= items.title %></strong></h3>
            <p><%= items.message %></p>
          </div>
        </div>
      <% }) %>
    </div>
  </div>
</div>

```

![image](https://github.com/user-attachments/assets/ebac367b-96c2-43be-8f01-6c7e93552cf9)
![image](https://github.com/user-attachments/assets/90c7a210-57f8-49e6-9ec5-949508d3d53d)
![image](https://github.com/user-attachments/assets/52302546-46e5-4728-9f38-786cb713a69e)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/869d87eb-918f-49ce-a693-b799652f8464">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/d3f3a0ee-36c0-4fa7-8d86-6abcfda5577d">

# #END</details>

<details>
<summary>20. Express Forms - Validating and Sanitizing User Input with Error Display </summary>

# Express Forms - Validating and Sanitizing User Input with Error Display 

## Install Express Validator

```js
npm install express-validator
```

### src-AI-Software/my_projects/01_building_a_website/package.json:

```json
{
  "name": "01_building_a_website",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon --ignore feedback.json server.js"
  },
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "body-parser": "^1.20.2",
    "cookie-session": "^2.1.0",
    "ejs": "^3.1.10",
    "express": "^4.19.2",
    "express-validator": "^7.1.0",
    "http-errors": "^2.0.0",
    "nodemon": "^3.1.4"
  },
  "devDependencies": {
    "@eslint/js": "^9.7.0",
    "eslint": "^9.7.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-prettier": "^5.2.1",
    "globals": "^15.8.0",
    "prettier": "^3.3.3"
  }
}

```

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');
const createError = require('http-errors');
const bodyParser = require('body-parser');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

// app.use(express.json());
// app.use(express.urlencoded({ extended: true }));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    return next();
  } catch (err) {
    return next(err);
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

// createError middleware
app.use((req, res, next) => {
  // console.error(err.stack);
  // res.status(404).send('Page not Found!');
  return next(createError(404, 'Page not found'));
});

// Error-handling middleware
app.use((err, req, res, next) => {
  res.locals.message = err.message || 'The page you requested was not found.';
  const status = err.status || 500;
  res.locals.status = status;
  return res.status(status).render('404');
});

app.listen(PORT, () => {
  try {
    console.log(`Server running on port ${PORT}`);
    console.log('Ctrl + C to stop');
  } catch (err) {
    console.error(err.stack);
    throw new Error(`Something broke: ${err}`);
  }
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/feedbackRoutes.js:

```js
const express = require('express');
const router = express.Router();
const { check, validationResult } = require('express-validator');

module.exports = (db) => {
  const { feedbackModel } = db;

  router.get('/', async (req, res, next) => {
    try {
      const feedback = await feedbackModel.getList();

      const errors = req.session.feedback ? req.session.feedback.errors : false;
      req.session.feedback = {};

      const context = {
        pageTitle: 'Feedback',
        name: 'Roux Meetups',
        template: 'feedback',
        feedback,
        errors,
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  const feedbackPOSTValidator = [
    check('name').trim().isLength({ min: 3 }).escape().withMessage('A name is required'),
    check('email')
      .trim()
      .isEmail()
      .normalizeEmail()
      .withMessage('A valid email address is required'),
    check('title').trim().isLength({ min: 3 }).escape().withMessage('A title is required'),
    check('message').trim().isLength({ min: 5 }).escape().withMessage('A message is required'),
  ];

  router.post('/', feedbackPOSTValidator, (req, res, next) => {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        req.session.feedback = {
          errors: errors.array(),
        };
        return res.redirect('/feedback');
      }
      return res.send(`Thanks for your posted feedback:\n\n ${JSON.stringify(req.body)}`);
    } catch (err) {
      return next(err);
    }
  });

  // Register the unhandled route middleware
  function handleUnhandledRoutes(req, res, next) {
    // res.status(404).send('Page not found');
    return next(new Error('The Route does not Exist!'));
  }
  router.use(handleUnhandledRoutes);

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/feedback.ejs:

```js
<div class="container">

<div class="row my-5">
  <div class="col-6">
    <h2>Enter a Feedback</h2>

    <% if(locals.errors) {%>
      <div class="alert alert-danger" role="alert">
        <% errors.forEach(function (error) {%>
          <li><%= error.msg %></li>
        <% }) %>
      </div>
    <% } %>

    <form method="POST" action="/feedback">
      <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" class="form-control" id="name" name="name" aria-describedby="textHelp">
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email address</label>
        <input type="email" class="form-control" id="email" name="email" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input type="text" class="form-control" id="title" name="title" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="message" class="form-label">Message</label>
        <textarea class="form-control" id="message" name="message" rows="3"></textarea>
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>

  <div class="col-6">
    <h2>Feedbacks</h2>
    <div class="accordion" id="accordionExample">
      <% feedback.forEach(function (items) { %>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#<%= items.name %>"
              aria-expanded="false"
              aria-controls="collapseThree"
            >
              <%= items.name %> | <%= items.email %>
            </button>
          </h2>
        </div>
        <div id="<%= items.name %>" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <h3><strong><%= items.title %></strong></h3>
            <p><%= items.message %></p>
          </div>
        </div>
      <% }) %>
    </div>
  </div>
</div>

```

![image](https://github.com/user-attachments/assets/e4e106ae-ecfd-4d40-b21d-6f636b49c9d0)
![image](https://github.com/user-attachments/assets/7227bd2c-7c9e-47fd-9008-6397da32a5e4)
![image](https://github.com/user-attachments/assets/4335a96a-c768-47a1-83e2-13950dfeb516)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/f56b6e60-5ad4-446a-b499-44c1ea87aac4">
<img width="1442" alt="image" src="https://github.com/user-attachments/assets/d399e057-b6f1-438e-bbdd-fbee7a84346f">

# #END</details>

<details>
<summary>21. Express Forms - Storing Data with Success Message </summary>

# Express Forms - Storing Data with Success Message 

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');
const createError = require('http-errors');
const bodyParser = require('body-parser');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

// app.use(express.json());
// app.use(express.urlencoded({ extended: true }));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    return next();
  } catch (err) {
    return next(err);
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

// createError middleware
app.use((req, res, next) => {
  // console.error(err.stack);
  // res.status(404).send('Page not Found!');
  return next(createError(404, 'Page not found'));
});

// Error-handling middleware
app.use((err, req, res, next) => {
  res.locals.message = err.message || 'The page you requested was not found.';
  const status = err.status || 500;
  res.locals.status = status;
  return res.status(status).render('404');
});

app.listen(PORT, () => {
  try {
    console.log(`Server running on port ${PORT}`);
    console.log('Ctrl + C to stop');
  } catch (err) {
    console.error(err.stack);
    throw new Error(`Something broke: ${err}`);
  }
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/feedbackRoutes.js:

```js
const express = require('express');
const router = express.Router();
const { check, validationResult } = require('express-validator');

module.exports = (db) => {
  const { feedbackModel } = db;

  router.get('/', async (req, res, next) => {
    try {
      const feedback = await feedbackModel.getList();

      const errors = req.session.feedback ? req.session.feedback.errors : false;
      const message = req.session.feedback ? req.session.feedback.message : false;
      req.session.feedback = {};

      const context = {
        pageTitle: 'Feedback',
        name: 'Roux Meetups',
        template: 'feedback',
        feedback,
        errors,
        message,
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  const feedbackPOSTValidator = [
    check('name').trim().isLength({ min: 3 }).escape().withMessage('A name is required'),
    check('email')
      .trim()
      .isEmail()
      .normalizeEmail()
      .withMessage('A valid email address is required'),
    check('title').trim().isLength({ min: 3 }).escape().withMessage('A title is required'),
    check('message').trim().isLength({ min: 5 }).escape().withMessage('A message is required'),
  ];

  router.post('/', feedbackPOSTValidator, async (req, res, next) => {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        req.session.feedback = {
          errors: errors.array(),
        };
        return res.redirect('/feedback');
      }

      const { name, email, title, message } = req.body;
      await feedbackModel.addEntry(name, email, title, message);
      req.session.feedback = {
        message: 'Thank you for your feedback!',
      };
      console.log(req.body);
      return res.redirect('/feedback');
      // return res.send(`Thanks for your posted feedback:\n\n ${JSON.stringify(req.body)}`);
    } catch (err) {
      return next(err);
    }
  });

  // Register the unhandled route middleware
  function handleUnhandledRoutes(req, res, next) {
    // res.status(404).send('Page not found');
    return next(new Error('The Route does not Exist!'));
  }
  router.use(handleUnhandledRoutes);

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/views/pages/feedback.ejs:

```ejs
<div class="container">

<div class="row my-5">
  <div class="col-6">
    <h2>Enter a Feedback</h2>

    <% if(locals.errors) {%>
      <div class="alert alert-danger" role="alert">
        <% errors.forEach(function (error) {%>
          <li><%= error.msg %></li>
        <% }) %>
      </div>
    <% } %>

    <% if(locals.message) {%>
      <div class="alert alert-success" role="alert">
        <li><%= message %></li>
      </div>
    <% } %>

    <form method="POST" action="/feedback">
      <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" class="form-control" id="name" name="name" aria-describedby="textHelp">
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email address</label>
        <input type="email" class="form-control" id="email" name="email" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input type="text" class="form-control" id="title" name="title" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="message" class="form-label">Message</label>
        <textarea class="form-control" id="message" name="message" rows="3"></textarea>
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>

  <div class="col-6">
    <h2>Feedbacks</h2>
    <div class="accordion" id="accordionExample">
      <% feedback.forEach(function (items) { %>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#<%= items.name %>"
              aria-expanded="false"
              aria-controls="collapseThree"
            >
              <%= items.name %> | <%= items.email %>
            </button>
          </h2>
        </div>
        <div id="<%= items.name %>" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <h3><strong><%= items.title %></strong></h3>
            <p><%= items.message %></p>
          </div>
        </div>
      <% }) %>
    </div>
  </div>
</div>

```

### src-AI-Software/my_projects/01_building_a_website/models/FeedbackModel.js:

```js
const fs = require('fs');
const util = require('util');

const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);

/**
 * Logic for reading and writing feedback data
 */
class FeedbackModel {
  /**
   * Constructor
   * @param {*} datafile Path to a JSOn file that contains the feedback data
   */
  constructor(datafile) {
    this.datafile = datafile;
  }

  /**
   * Get all feedback items
   */
  async getList() {
    const data = await this.getData();
    return data;
  }

  /**
   * Add a new feedback item
   * @param {*} name The name of the user
   * @param {*} title The title of the feedback message
   * @param {*} message The feedback message
   */
  async addEntry(name, email, title, message) {
    const data = (await this.getData()) || [];
    data.unshift({ name, email, title, message });
    return writeFile(this.datafile, JSON.stringify(data));
  }

  /**
   * Fetches feedback data from the JSON file provided to the constructor
   */
  async getData() {
    const data = await readFile(this.datafile, 'utf8');
    if (!data) return [];
    return JSON.parse(data);
  }
}

module.exports = FeedbackModel;

```

```x
[nodemon] starting `node server.js`
Server running on port 3000
Ctrl + C to stop
{
  name: 'Ifeanyi',
  email: 'ifeanyio@gmail.com',
  title: 'My Story',
  message: 'This is my Story!'
}
```

![image](https://github.com/user-attachments/assets/56edb912-4218-4963-a047-fd98e8b9bc05)
![image](https://github.com/user-attachments/assets/d32e4737-b08b-4bb0-907f-1c860736eb80)

<img width="1486" alt="image" src="https://github.com/user-attachments/assets/d0536000-c3c4-4ea4-bae5-a499024e67ca">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/21df6cb2-5772-4bc5-a001-b395c050f8e4">
<img width="1486" alt="image" src="https://github.com/user-attachments/assets/a8eed92f-35c1-4d43-b32c-de33af36587d">

# #END</details>

<details>
<summary>22. REST API - Creating and Testing API Endpoints </summary>

# REST API - Creating and Testing API Endpoints

### src-AI-Software/my_projects/01_building_a_website/server.js:

```js
const express = require('express');
const path = require('path');
const cookieSession = require('cookie-session');
const createError = require('http-errors');
const bodyParser = require('body-parser');

const FeedbackModel = require('./models/FeedbackModel');
const SpeakerModel = require('./models/SpeakerModel');

const feedbackModel = new FeedbackModel('./data/feedback.json');
const speakersModel = new SpeakerModel('./data/speakers.json');

const routes = require('./routes/homeRoutes');

const app = express();

const PORT = 3000;

app.set('trust proxy', 1);
app.use(
  cookieSession({
    name: 'session',
    keys: ['key14842784278', 'key232423423424'],
  })
);

app.locals.siteName = 'Global ROUX Meetups';

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(express.static(path.join(__dirname, './static')));

app.use(async (req, res, next) => {
  res.locals.newGreeting = 'Hello World';

  try {
    const names = await speakersModel.getNames();
    res.locals.speakersNames = names;
    return next();
  } catch (err) {
    return next(err);
  }
});

app.use('/', routes({ feedbackModel, speakersModel }));

// createError middleware
app.use((req, res, next) => {
  return next(createError(404, 'Page not found'));
});

// Error-handling middleware
app.use((err, req, res, next) => {
  res.locals.message = err.message || 'The page you requested was not found.';
  const status = err.status || 500;
  res.locals.status = status;
  return res.status(status).render('404');
});

app.listen(PORT, () => {
  try {
    console.log(`Server running on port ${PORT}`);
    console.log('Ctrl + C to stop');
  } catch (err) {
    console.error(err.stack);
    throw new Error(`Something broke: ${err}`);
  }
});

```

### src-AI-Software/my_projects/01_building_a_website/routes/feedbackRoutes.js:

```js
const express = require('express');
const router = express.Router();
const { check, validationResult } = require('express-validator');

const feedbackPOSTValidator = [
  check('name').trim().isLength({ min: 3 }).escape().withMessage('A name is required'),
  check('email').trim().isEmail().normalizeEmail().withMessage('A valid email address is required'),
  check('title').trim().isLength({ min: 3 }).escape().withMessage('A title is required'),
  check('message').trim().isLength({ min: 5 }).escape().withMessage('A message is required'),
];

module.exports = (db) => {
  const { feedbackModel } = db;

  router.get('/', async (req, res, next) => {
    try {
      const feedback = await feedbackModel.getList();

      const errors = req.session.feedback ? req.session.feedback.errors : false;
      const message = req.session.feedback ? req.session.feedback.message : false;
      req.session.feedback = {};

      const context = {
        pageTitle: 'Feedback',
        name: 'Roux Meetups',
        template: 'feedback',
        feedback,
        errors,
        message,
      };
      return res.render('layouts/base', context);
    } catch (err) {
      return next(err);
    }
  });

  router.post('/', feedbackPOSTValidator, async (req, res, next) => {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        req.session.feedback = {
          errors: errors.array(),
        };
        return res.redirect('/feedback');
      }

      const { name, email, title, message } = req.body;
      await feedbackModel.addEntry(name, email, title, message);
      req.session.feedback = {
        message: 'Thank you for your feedback!',
      };
      console.log(req.body);
      return res.redirect('/feedback');
    } catch (err) {
      return next(err);
    }
  });

  // API Endpoint for feedback
  router.post('/api', feedbackPOSTValidator, async (req, res, next) => {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.json({ errors: errors.array() });
      }
      const { name, email, title, message } = req.body;
      await feedbackModel.addEntry(name, email, title, message);
      const feedback = await feedbackModel.getList();
      return res.json({ feedback, successMessage: 'Thank you for your feedback!' });
    } catch (err) {
      return next(err);
    }
  });

  // Register the unhandled route middleware
  function handleUnhandledRoutes(req, res, next) {
    return next(new Error('The Route does not Exist!'));
  }
  router.use(handleUnhandledRoutes);

  return router;
};

```

### src-AI-Software/my_projects/01_building_a_website/models/FeedbackModel.js:

```js
const fs = require('fs');
const util = require('util');

const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);

/**
 * Logic for reading and writing feedback data
 */
class FeedbackModel {
  /**
   * Constructor
   * @param {*} datafile Path to a JSOn file that contains the feedback data
   */
  constructor(datafile) {
    this.datafile = datafile;
  }

  /**
   * Get all feedback items
   */
  async getList() {
    const data = await this.getData();
    return data;
  }

  /**
   * Add a new feedback item
   * @param {*} name The name of the user
   * @param {*} title The title of the feedback message
   * @param {*} message The feedback message
   */
  async addEntry(name, email, title, message) {
    const data = (await this.getData()) || [];
    data.unshift({ name, email, title, message });
    return writeFile(this.datafile, JSON.stringify(data));
  }

  /**
   * Fetches feedback data from the JSON file provided to the constructor
   */
  async getData() {
    const data = await readFile(this.datafile, 'utf8');
    if (!data) return [];
    return JSON.parse(data);
  }
}

module.exports = FeedbackModel;

```

### src-AI-Software/my_projects/01_building_a_website/data/feedback.json:

```json
[
    {
        "name": "Bob",
        "email": "bob@gmail.com",
        "title": "REST API Test",
        "message": "This is the REST API Test."
    },
    {
        "name": "Ifeanyi",
        "email": "ifeanyio@gmail.com",
        "title": "My Story",
        "message": "This is my Story!"
    },
    {
        "name": "Frank",
        "email": "frank-smith@gmail.com",
        "title": "Best Meetup Ever",
        "message": "I really love this meetup. Please don't let it end."
    },
    {
        "name": "Jane",
        "email": "jane-miller@gmail.com",
        "title": "Meeting Time",
        "message": "Would you consider moving the meeting time 30 minutes to about 6pm. It's tough to make it to the meetings on time right after work."
    },
    {
        "name": "Roy",
        "email": "roy-jones@gmail.com",
        "title": "Great Speaker",
        "message": "I really enjoyed the speaker this month. Would love to hear another presentation."
    }
]
```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/b0b23705-0ba8-44fa-a64a-6c5354a55f25">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/bbf214c6-5dbb-483e-b57d-0b78080aba30">

![image](https://github.com/user-attachments/assets/a1094be2-32ae-4ede-9a08-aa22db597f75)

<img width="1379" alt="image" src="https://github.com/user-attachments/assets/b74f9333-de98-415c-96af-7447d0bbf262">

# #END</details>

# #END
