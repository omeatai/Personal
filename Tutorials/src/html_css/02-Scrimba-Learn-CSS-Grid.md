## +Scrimba-Learn-CSS-Grid

## [COURSE](https://v2.scrimba.com/learn-css-grid-c02k)

<details>
<summary>1-create-react-app </summary>

# 1-create-react-app

```x
npm create-react-app my_app
```

```x
cd my_app
npm start
```

<img width="1281" alt="image" src="https://github.com/user-attachments/assets/c718243d-894f-414d-b5eb-af5d89cfca48">
<img width="1382" alt="image" src="https://github.com/user-attachments/assets/7cab9921-3406-438d-a6ac-c441e888a018">
<img width="1382" alt="image" src="https://github.com/user-attachments/assets/59b0798c-3c88-4e32-ab74-006a0b013d84">
<img width="1382" alt="image" src="https://github.com/user-attachments/assets/eb9cd127-2cea-49ae-ae76-84190ddde29c">
<img width="1382" alt="image" src="https://github.com/user-attachments/assets/f8ca50dc-a2d9-4b85-a446-a4933af419cd">

</details>

<details>
<summary>2-Create-Horizontal-rows-with-div </summary>

# 2-Create-Horizontal-rows-with-div

### github_projects/project-css-grid-flex/my_app/src/App.js:

```js
import "./App.css";
import Grid from "./components/Grid/Grid";

function App() {
  return (
    <div className="App">
      <Grid />
    </div>
  );
}

export default App;

```

### github_projects/project-css-grid-flex/my_app/src/components/Grid/Grid.jsx:

```jsx
import React from "react";
import "./GridStyles.css";

const Grid = () => {
  return (
    <section className="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
    </section>
  );
};

export default Grid;

```

### github_projects/project-css-grid-flex/my_app/src/App.css:

```css
html,
body {
  margin: 5px;
  background-color: #ffeead;
  overflow: hidden;
}
```

### github_projects/project-css-grid-flex/my_app/src/components/Grid/GridStyles.css:

```css
.container>div {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    color: #ffeead;
    background-color: #ffeead;
}

.container>div:nth-child(1n) {
    background-color: #96ceb4;
}

.container>div:nth-child(3n) {
    background-color: #88d8b0;
}

.container>div:nth-child(2n) {
    background-color: #ff6f69;
}

.container>div:nth-child(4n) {
    background-color: #ffcc5c;
}
```

<img width="1332" alt="image" src="https://github.com/user-attachments/assets/a1d5c17d-567c-4eae-95bf-262fa5158186">
<img width="1382" alt="image" src="https://github.com/user-attachments/assets/5ec965ef-d23d-4679-8348-9924c0ff9bbb">
<img width="1382" alt="image" src="https://github.com/user-attachments/assets/87c3e0a9-d974-4cbb-adcf-0cfff44d6c32">
<img width="1382" alt="image" src="https://github.com/user-attachments/assets/09d4ba04-cb82-4e39-8d70-eb44ae2bbeea">
<img width="1382" alt="image" src="https://github.com/user-attachments/assets/5c4c648f-25c9-48be-877e-9e9f599f8030">

</details>

<details>
<summary>3-grid-template-columns and grid-template-rows </summary>

# 3-grid-template-columns and grid-template-rows

### github_projects/project-css-grid-flex/my_app/src/components/Grid/GridStyles.css:

```css
.container>div {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    color: #ffeead;
    background-color: #ffeead;
}

.container {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: 100px auto 100px;
    grid-template-rows: 40px 40px;
}

.container>div:nth-child(1n) {
    background-color: #96ceb4;
}

.container>div:nth-child(3n) {
    background-color: #88d8b0;
}

.container>div:nth-child(2n) {
    background-color: #ff6f69;
}

.container>div:nth-child(4n) {
    background-color: #ffcc5c;
}
```

<img width="1332" alt="image" src="https://github.com/user-attachments/assets/6335bdc3-fd6b-4f22-b464-e70e26e6168f">

### github_projects/project-css-grid-flex/my_app/src/components/Grid/GridStyles.css:

```css
.container {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr;
}

```

```css
.container {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 1fr);
}

```

```css
.container {
    display: grid;
    grid-gap: 5px;
    grid-template: repeat(2, 1fr) / repeat(4, 1fr);
}
```

<img width="1332" alt="image" src="https://github.com/user-attachments/assets/769e0c82-7a0f-46af-a136-126f109a8b93">

</details>

<details>
<summary>4-positioning-items-in-grid-with grid-column-start and grid-column-end </summary>

# 4-positioning-items-in-grid-with grid-column-start and grid-column-end

### github_projects/project-css-grid-flex/my_app/src/components/Grid/Grid.jsx:

```css
import React from "react";
import "./GridStyles.css";

const Grid = () => {
  return (
    <section className="container">
      <div className="header">HEADER</div>
      <div className="menu">MENU</div>
      <div className="content">CONTENT</div>
      <div className="footer">FOOTER</div>
    </section>
  );
};

export default Grid;
```

### github_projects/project-css-grid-flex/my_app/src/components/Grid/GridStyles.css:

```css
.container>div {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    color: #ffeead;
    background-color: #ffeead;
}

.container {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 40px 200px 40px;
}

.header {}

.menu {}

.content {}

.footer {}

.container>div:nth-child(1n) {
    background-color: #96ceb4;
}

.container>div:nth-child(3n) {
    background-color: #88d8b0;
}

.container>div:nth-child(2n) {
    background-color: #ff6f69;
}

.container>div:nth-child(4n) {
    background-color: #ffcc5c;
}
```

<img width="1332" alt="image" src="https://github.com/user-attachments/assets/68c2918b-fbda-4681-8eea-8235b1f98c64">

### github_projects/project-css-grid-flex/my_app/src/components/Grid/GridStyles.css:

```css
.container>div {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    color: #ffeead;
    background-color: #ffeead;
}

.container {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: 40px 200px 40px;
}

.header {
    grid-column-start: 1;
    grid-column-end: 13;
}

.menu {
    grid-column-start: 1;
    grid-column-end: 2;
}

.content {
    grid-column-start: 2;
    grid-column-end: 13;
}

.footer {
    grid-column-start: 1;
    grid-column-end: 13;
}

.container>div:nth-child(1n) {
    background-color: #96ceb4;
}

.container>div:nth-child(3n) {
    background-color: #88d8b0;
}

.container>div:nth-child(2n) {
    background-color: #ff6f69;
}

.container>div:nth-child(4n) {
    background-color: #ffcc5c;
}
```

```css
.header {
    grid-column: 1 / 13;
}

.menu {
    grid-column: 1 / 2;
}

.content {
    grid-column: 2 / 13;
}

.footer {
    grid-column: 1 / 13;
}
```

```css
.header {
    grid-column: 1 / -1;
}

.menu {
    grid-column: 1 / 2;
}

.content {
    grid-column: 2 / -1;
}

.footer {
    grid-column: 1 / -1;
}

```

```css
.header {
    grid-column: 1 / span 12;
}

.menu {
    grid-column: 1 / span 1;
}

.content {
    grid-column: 2 / span 11;
}

.footer {
    grid-column: 1 / span 12;
}
```

<img width="1332" alt="image" src="https://github.com/user-attachments/assets/4356538c-947f-4da8-8028-23373ea3f1cc">

### github_projects/project-css-grid-flex/my_app/src/components/Grid/GridStyles.css:

```css
.container {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: 40px 200px 40px;
}

.header {
    grid-column: 2 / -1;
}

.menu {
    grid-column: 1 / span 1;
    grid-row: 1 / span 2;
}

.content {
    grid-column: 2 / -1;
}

.footer {
    grid-column: 1 / -1;
}
```

<img width="1377" alt="image" src="https://github.com/user-attachments/assets/0577dbe5-71b1-430c-a258-2d4de33a122f">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/ab4c4d9e-83d4-4353-8d3c-3f893ebd258f">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/f33a89fc-832d-4ef5-b0e4-e1159d9c117a">

</details>

<details>
<summary>5-positioning-items-in-grid-with grid-template-areas </summary>

# 5-positioning-items-in-grid-with grid-template-areas

### github_projects/project-css-grid-flex/my_app/src/components/Grid/Grid.jsx:

```jsx
import React from "react";
import "./GridStyles.css";

const Grid = () => {
  return (
    <section className="container">
      <div className="header">HEADER</div>
      <div className="menu">MENU</div>
      <div className="content">CONTENT</div>
      <div className="footer">FOOTER</div>
    </section>
  );
};

export default Grid;

```

### github_projects/project-css-grid-flex/my_app/src/App.css:

```css
html,
body {
  overflow: hidden;
  box-sizing: border-box;
  height: 100vh;
  padding: 10px;
  background-color: #ffeead;
}
```

### github_projects/project-css-grid-flex/my_app/src/components/Grid/GridStyles.css:

```css
.container>div {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    color: #ffeead;
    background-color: #ffeead;
}

.container {
    overflow: hidden;
    min-height: 95vh;
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: 40px auto 40px;
    grid-template-areas:
        ". h h h h h h h h h h h"
        "m c c c c c c c c c c c"
        "m f f f f f f f f f f f";
}

.header {
    grid-area: h;
}

.menu {
    grid-area: m;
}

.content {
    grid-area: c;
}

.footer {
    grid-area: f;
}

.container>div:nth-child(1n) {
    background-color: #96ceb4;
}

.container>div:nth-child(3n) {
    background-color: #88d8b0;
}

.container>div:nth-child(2n) {
    background-color: #ff6f69;
}

.container>div:nth-child(4n) {
    background-color: #ffcc5c;
}
```

<img width="1149" alt="image" src="https://github.com/user-attachments/assets/dc2121e8-4433-49b3-89e6-d83093cf5142">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/0ccccd00-7641-4200-bc87-a38b357653ad">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/cae960ce-52df-4672-9799-3160f9584fb1">

</details>

<details>
<summary>6-auto-fit and minmax </summary>

# 6-auto-fit and minmax 

### github_projects/project-css-grid-flex/my_app/src/components/Grid/Grid.jsx:

```jsx
import React from "react";
import "./GridStyles.css";

const Grid = () => {
  return (
    <section className="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
      <div>7</div>
      <div>8</div>
      <div>9</div>
      <div>10</div>
      <div>11</div>
      <div>12</div>
    </section>
  );
};

export default Grid;

```

### github_projects/project-css-grid-flex/my_app/src/App.css:

```css
html,
body {
  overflow: hidden;
  box-sizing: border-box;
  background-color: #ffeead;
  margin: 10px;
}
```

### github_projects/project-css-grid-flex/my_app/src/components/Grid/GridStyles.css:

```css
.container>div {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    color: #ffeead;
}

.container {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    grid-template-rows: repeat(12, 200px);
}

.container>div:nth-child(1n) {
    background-color: #96ceb4;
}

.container>div:nth-child(3n) {
    background-color: #88d8b0;
}

.container>div:nth-child(2n) {
    background-color: #ff6f69;
}

.container>div:nth-child(4n) {
    background-color: #ffcc5c;
}
```

![image](https://github.com/user-attachments/assets/280f31eb-c11c-4bc1-80fc-62a3396b221e)

<img width="1341" alt="image" src="https://github.com/user-attachments/assets/465f8811-7ede-4ef2-9315-7dd720ffe84e">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/1c5e0f57-da29-47cf-abb2-768718464f10">
<img width="1341" alt="image" src="https://github.com/user-attachments/assets/61859dee-baee-42fe-896f-2d44248aea9b">

</details>

<details>
<summary>7-implicit-rows with grid-auto-row </summary>

# 7-implicit-rows with grid-auto-row 

### github_projects/project-css-grid-flex/my_app/src/components/Grid/Grid.jsx:

```jsx
import React from "react";
import "./GridStyles.css";

const Grid = () => {
  return (
    <section className="container">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
      <div>7</div>
      <div>8</div>
      <div>9</div>
      <div>10</div>
      <div>11</div>
      <div>12</div>
    </section>
  );
};

export default Grid;

```

### github_projects/project-css-grid-flex/my_app/src/App.css:

```css
html,
body {
  overflow: hidden;
  box-sizing: border-box;
  background-color: #ffeead;
  margin: 10px;
}
```

### github_projects/project-css-grid-flex/my_app/src/components/Grid/GridStyles.css:

```css
.container>div {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    color: #ffeead;
}

.container {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    /* grid-template-rows: repeat(12, 200px); */
    grid-auto-rows: 300px;
}

.container>div:nth-child(1n) {
    background-color: #96ceb4;
}

.container>div:nth-child(3n) {
    background-color: #88d8b0;
}

.container>div:nth-child(2n) {
    background-color: #ff6f69;
}

.container>div:nth-child(4n) {
    background-color: #ffcc5c;
}
```

![image](https://github.com/user-attachments/assets/8beda3e9-624f-420f-b81f-548f68c40d1a)

<img width="1385" alt="image" src="https://github.com/user-attachments/assets/6b4d84d6-974c-4340-b5a3-a48c46775aa3">

</details>

<details>
<summary>8-complex-rows with grid-auto-flow </summary>

# 8-complex-rows with grid-auto-flow

### github_projects/project-css-grid-flex/my_app/src/components/Grid/Grid.jsx:

```jsx
import React from "react";
import "./GridStyles.css";

import normal1 from "./img/normal1.jpg";
import normal2 from "./img/normal2.jpg";
import normal3 from "./img/normal3.jpg";
import normal4 from "./img/normal4.jpg";
import normal5 from "./img/normal5.jpg";
import normal6 from "./img/normal6.jpg";
import normal7 from "./img/normal7.jpg";
import normal8 from "./img/normal8.jpg";
import normal9 from "./img/normal9.jpg";
import big1 from "./img/big1.jpg";
import big2 from "./img/big2.jpg";
import big3 from "./img/big3.jpg";
import vertical1 from "./img/vertical1.jpg";
import vertical2 from "./img/vertical2.jpg";
import vertical3 from "./img/vertical3.jpg";
import horizontal1 from "./img/horizontal1.jpg";
import horizontal2 from "./img/horizontal2.jpg";
import horizontal3 from "./img/horizontal3.jpg";

const Grid = () => {
  return (
    <section className="container">
      <div>
        <img src={normal1} alt="" />
      </div>
      <div class="vertical">
        <img src={vertical1} alt="" />
      </div>
      <div class="horizontal">
        <img src={horizontal1} alt="" />
      </div>
      <div>
        <img src={normal2} alt="" />
      </div>
      <div>
        <img src={normal3} alt="" />
      </div>
      <div class="big">
        <img src={big1} alt="" />
      </div>
      <div>
        <img src={normal4} alt="" />
      </div>
      <div class="vertical">
        <img src={vertical2} alt="" />
      </div>
      <div>
        <img src={normal5} alt="" />
      </div>
      <div class="horizontal">
        <img src={horizontal2} alt="" />
      </div>
      <div>
        <img src={normal6} alt="" />
      </div>
      <div class="big">
        <img src={big2} alt="" />
      </div>
      <div>
        <img src={normal7} alt="" />
      </div>
      <div class="horizontal">
        <img src={horizontal3} alt="" />
      </div>
      <div>
        <img src={normal8} alt="" />
      </div>
      <div class="big">
        <img src={big3} alt="" />
      </div>
      <div>
        <img src={normal9} alt="" />
      </div>
      <div class="vertical">
        <img src={vertical3} alt="" />
      </div>
    </section>
  );
};

export default Grid;

```

### github_projects/project-css-grid-flex/my_app/src/App.css:

```css
html,
body {
  box-sizing: border-box;
  background-color: #ffeead;
  margin: 10px;
}
```

### github_projects/project-css-grid-flex/my_app/src/components/Grid/GridStyles.css:

```css
.container>div {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    color: #ffeead;
}

.container {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    grid-auto-rows: 150px;
    grid-auto-flow: dense;
}

.container>div>img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.horizontal {
    grid-column: auto / span 2;
}

.vertical {
    grid-row: auto / span 2;
}

.big {
    grid-column: auto / span 2;
    grid-row: auto / span 2;
}
```

![image](https://github.com/user-attachments/assets/b928d0e5-df11-45a9-88cd-db767ef4ffc6)
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/01691d4b-de54-45ae-9880-a0faeff6b1a8">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/92a0e7be-b3c4-4008-be39-a545506767ce">

</details>

<details>
<summary>9-named-lines </summary>

# 9-named-lines

```css

```

</details>

