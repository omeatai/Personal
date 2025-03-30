## 03-Javascript Essential Training

## [COURSE](https://www.linkedin.com/learning/javascript-essential-training/javascript-the-soil-from-which-the-modern-web-grows?resume=false)

<details>
<summary>1-JS Comments</summary>

# JS Comments

```js
// Single line comment

/* Multi-line comment
See! this line is also commented out! */

/**
 * function updateBackpack
 * returns HTML
 * @param {string} update
 */
const updateBackpack = (update) => {
  let main = document.querySelector("main"); // main is an element
  main.innerHTML = markup(backpack);
  console.info(update);
};
```

# #END</details>

<details>
<summary>2-Loading JS in external files - async/defer</summary>

# Loading JS in external files - async/defer

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/02_03/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Module demo</title>
    <script src="script.js" defer></script>
  </head>
  <body></body>
</html>
```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/02_03/script.js:

```js
/**
 * Create a Backpack object, populate some HTML to display its properties.
 */
const updateBackpack = (update) => {
  let main = document.querySelector("main");
  main.innerHTML = markup(backpack);
  console.info(update);
};

const backpack = {
  name: "Everyday Backpack",
  volume: 30,
  color: "grey",
  pocketNum: 15,
  strapLength: {
    left: 26,
    right: 26,
  },
  lidOpen: false,
  toggleLid: function (lidStatus) {
    this.lidOpen = lidStatus;
    updateBackpack(`Lid status changed.`);
  },
  newStrapLength: function (lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
    updateBackpack(`Strap lengths updated.`);
  },
};

const markup = (backpack) => {
  return `
  <div>
    <h3>${backpack.name}</h3>
    <ul>
      <li>Volume: ${backpack.volume}</li>
      <li>Color: ${backpack.color}</li>
      <li>Number of pockets: ${backpack.pocketNum}</li>
      <li>Strap lengths: L: ${backpack.strapLength.left}, R: ${
    backpack.strapLength.right
  } </li>
      <li>Top lid: ${backpack.lidOpen ? "Open" : "Closed"}</li>
    </ul>
  </div>
`;
};

const main = document.createElement("main");
main.innerHTML = markup(backpack);
document.body.appendChild(main);

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/7a2527a8-053d-42d7-8977-29590ac3c285)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/655ed317-c00b-41f1-b92a-ff22b6c8e4e3)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/1e866625-1f55-4eca-a72a-e4cb4694679f)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/ddb21a9a-886c-4e4d-ad69-3c52e3f86d9c)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d9843fb1-98be-4b06-afbc-220cec2b08ef)

<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/2bebf9cd-6349-4dc9-a93a-d7899a8e4dce">
<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/2d7d8f8b-937f-48cd-a3f4-b70f6399cd03">

# #END</details>

<details>
<summary>3-Using Javascript Modules</summary>

# Using Javascript Modules

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/02_04/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Module demo</title>
    <script type="module" src="backpack.js"></script>
    <script type="module" src="script.js"></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/02_04/backpack.js:

```js
const updateBackpack = (update) => {
  let main = document.querySelector("main");
  main.innerHTML = markup(backpack);
  console.info(update);
};

const backpack = {
  name: "Everyday Backpack",
  volume: 30,
  color: "grey",
  pocketNum: 15,
  strapLength: {
    left: 26,
    right: 26,
  },
  lidOpen: false,
  toggleLid: function (lidStatus) {
    this.lidOpen = lidStatus;
    updateBackpack(`Lid status changed.`);
  },
  newStrapLength: function (lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
    updateBackpack(`Strap lengths updated.`);
  },
};

export default backpack;
```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/02_04/script.js:

```js
/**
 * Create a Backpack object, populate some HTML to display its properties.
 */
import backpack from "./backpack.js";

const markup = (backpack) => {
  return `
  <div>
    <h3>${backpack.name}</h3>
    <ul>
      <li>Volume: ${backpack.volume}</li>
      <li>Color: ${backpack.color}</li>
      <li>Number of pockets: ${backpack.pocketNum}</li>
      <li>Strap lengths: L: ${backpack.strapLength.left}, R: ${
    backpack.strapLength.right
  } </li>
      <li>Top lid: ${backpack.lidOpen ? "Open" : "Closed"}</li>
    </ul>
  </div>
`;
};

const main = document.createElement("main");
main.innerHTML = markup(backpack);
document.body.appendChild(main);

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/e8ce63d9-72da-4714-b72a-e464c8990440)

<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/a3c7f6bf-b688-4330-98fa-49ea38cbb029">
<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/09d0ecee-1361-42a3-85ad-4bc9128b9e1d">
<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/3123111d-0662-4741-8cef-9832b3554e4b">

# #END</details>

<details>
<summary>4-JS Objects with Properties and Methods </summary>

## JS Objects with Properties and Methods

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_02/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Building a JavaScript object from scratch</title>
    <script src="script.js" defer></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_02/script.js:

```js
/**
 * Create a Backpack object.
 */

const backpack = {
  name: "Everyday Backpack", // This is a Property
  volume: 30,
  color: "grey",
  pocketNum: 15, // This is a Property
  strapLength: {
    // This is a Property
    left: 26,
    right: 26,
  },
  lidOpen: false, // This is a Property

  toggleLid: function (lidStatus) {
    // This is a Method
    this.lidOpen = lidStatus;
  },
  newStrapLength: function (lengthLeft, lengthRight) {
    // This is a Method
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  },
};

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/afb49d58-ca67-4516-bb29-c8c074b1f47e)

<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/45ef5068-dc20-48cb-a955-e48e320c64d8">

# #END</details>

<details>
<summary>5-JS Objects - Accessing Object Properties </summary>

# JS Objects - Accessing Object Properties

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_08/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Object methods</title>
    <script src="script.js" defer></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_08/script.js:

```js
/**
 * Create a Backpack object.
 */

const backpack = {
  name: "Everyday Backpack",
  volume: 30,
  color: "grey",
  pocketNum: 15,
  strapLength: {
    left: 26,
    right: 26,
  },
  lidOpen: false,

  toggleLid: function (lidStatus) {
    this.lidOpen = lidStatus;
  },
  newStrapLength: function (lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  },
};

console.log("The backpack object:", backpack);
console.log("The pocketNum value:", backpack.pocketNum);
console.log("Left before:", backpack.strapLength.left);

console.log("The pocketNum value:", backpack["pocketNum"]);

let query = "pocketNum";
console.log("The pocketNum value:", backpack[query]);
```

## Output

```x
The backpack object: {name: 'Everyday Backpack', volume: 30, color: 'grey', pocketNum: 15, strapLength: {…}, …}
The pocketNum value: 15
Left before: 26
The pocketNum value: 15
The pocketNum value: 15
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/ae17e8fd-7c08-4ab5-9153-fe24d75f9a05)

<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/17d02b3c-7bf2-4841-904b-5626e8bb1263">

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/Practice/03_07/script.js:

```js
/**
 * Practice: Building objects
 *
 * - Create JavaScript objects based on objects in your current environment.
 * - Give each object an identifiable name.
 * - Create properties to describe the objects and set their values.
 * - Find an object that has another object inside of it to create a nested object.
 * - Test your objects in the browser console by accessing the entire object and its specific properties.
 */

// Create an object for a car
const car = {
  make: "Toyota",
  model: "Corolla",
  year: 2020,
  color: "black",
  price: 20000,
  lightBulbON: true,
  "travel bag": {
    brand: "chanel",
    color: "black",
    straps: 2,
    compartments: 3,
    contents: {
      clothes: 5,
      shoes: 2,
      toiletries: 1,
      electronics: 1,
    },
  },

  start: function () {
    console.log("Car started");
  },

  stop: function () {
    console.log("Car stopped");
  },

  drive: function () {
    console.log("Car is moving");
  },

  toggleLights: function (lightBulbON) {
    this.lightBulbON = !this.lightBulbON;
    console.log(
      this.lightBulbON ? "Light is turned ON" : "Light is turned OFF"
    );
  },

  lightStatus: function () {
    console.log(this.lightBulbON ? "Light is ON" : "Light is OFF");
    return this.lightBulbON;
  },
};

console.log("Car", car);
console.log("Car Model", car.model);
console.log("Car Year", car.year);
console.log("Car Bulb Status", car.lightStatus());
console.log("Car Luggage contents", car["travel bag"].contents);

```

## Output

```x
Car 
{make: 'Toyota', model: 'Corolla', year: 2020, color: 'black', price: 20000, …}
Car Model Corolla
Car Year 2020
Light is ON
Car Bulb Status true
Car Luggage contents 
{clothes: 5, shoes: 2, toiletries: 1, electronics: 1}
clothes: 5
electronics: 1
shoes: 2
toiletries: 1

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/ec2ab3d9-bbbf-453f-9b2b-4811661d14b1)


# #END</details>

<details>
<summary>6-JS Objects - Access Methods </summary>

# JS Objects - Access Methods

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_08e/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Object methods</title>
    <script src="script.js" defer></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_08e/script.js:

```js
/**
 * Create a Backpack object.
 */

const backpack = {
  name: "Everyday Backpack",
  volume: 30,
  color: "grey",
  pocketNum: 15,
  strapLength: {
    left: 26,
    right: 26,
  },
  lidOpen: false,
  toggleLid: function (lidStatus) {
    this.lidOpen = lidStatus;
  },
  newStrapLength: function (lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  },
};

console.log("The backpack object:", backpack);
console.log("The pocketNum value:", backpack.pocketNum);
console.log("Left before:", backpack.strapLength.left);

backpack.newStrapLength(10, 15);

console.log("Left after:", backpack.strapLength.left);

```

## Output

```x
The backpack object: {name: 'Everyday Backpack', volume: 30, color: 'grey', pocketNum: 15, strapLength: {…}, …}color: "grey"lidOpen: falsename: "Everyday Backpack"newStrapLength: ƒ (lengthLeft, lengthRight)pocketNum: 15strapLength: {left: 10, right: 15}toggleLid: ƒ (lidStatus)volume: 30[[Prototype]]: Object
The pocketNum value: 15
Left before: 26
Left after: 10
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/ad7cec28-0894-4a41-9ad7-3800aecaa13e)

<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/776614f9-2f88-41b7-b2e9-b5fad9d297e6">

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/Practice/03_09/script.js:

```js
/**
 * Practice: Making methods
 *
 * - Create a method for each object property.
 * - The method receives a value to match the property to be changed.
 * - Create a simple function to replace the current property value with the received value.
 * - Test the method by sending new values and checking the properties in the console.
 */

const backpack = {
  name: "Everyday Backpack",
  volume: 30,
  color: "grey",
  pocketNum: 15,
  strapLength: {
    left: 26,
    right: 26,
  },
  toggleLid: function (lidStatus) {
    this.lidOpen = lidStatus;
  },
  newStrapLength: function (lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  },

  setName: function (newName) {
    this.name = newName;
    console.log("The new name is: ", this.name);
  },

  setVolume: function (newVolume) {
    this.volume = newVolume;
    console.log("The new volume is: ", this.volume);
  },

  setColor: function (newColor) {
    this.color = newColor;
    console.log("The new color is: ", this.color);
  },

  setStrapLength: function (leftStrapLength, rightStrapLength) {
    this.strapLength.left = leftStrapLength;
    this.strapLength.right = rightStrapLength;
    console.log("The new strap length is: ", this.strapLength);
  },
};

```

## Output

```x
backpack.name
'Everyday Backpack'

backpack.setName("Ruby Backpack")
script.js:29 The new name is:  Ruby Backpack
undefined

backpack.name
'Ruby Backpack'

backpack.setStrapLength(10, 15)
script.js:45 The new strap length is:  {left: 10, right: 15}
undefined

backpack.strapLength
{left: 10, right: 15}
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/941ca51e-5a3a-40f2-8bf9-3a87b0875084)

<img width="1448" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d3cd6967-7127-4fd9-88c1-0a27042aba6e">

# #END</details>

<details>
<summary>7-JS Objects - Classes as Blueprints </summary>

# JS Objects - Classes as Blueprints

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_10/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Classes</title>
    <script type="module" src="Backpack.js"></script>
    <script type="module" src="script.js"></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_10/Backpack.js:

```js
/**
 * Creating classes:
 *
 * Class declaration: class Name {}
 * Class expression:  const Name = class {}
 */

class Backpack {
  constructor(
    // Defines parameters:
    name,
    volume,
    color,
    pocketNum,
    strapLengthL,
    strapLengthR,
    lidOpen
  ) {
    // Define properties:
    this.name = name;
    this.volume = volume;
    this.color = color;
    this.pocketNum = pocketNum;
    this.strapLength = {
      left: strapLengthL,
      right: strapLengthR,
    };
    this.lidOpen = lidOpen;
  }

  // Add methods like normal functions:
  toggleLid(lidStatus) {
    this.lidOpen = lidStatus;
  }
  newStrapLength(lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  }
}

export default Backpack;

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_10/script.js:

```js
/**
 * Create a class for the Backpack object type.
 * @link https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes
 */
import Backpack from "./Backpack.js";

const everydayPack = new Backpack(
  "Everyday Backpack",
  30,
  "grey",
  15,
  26,
  26,
  false
);

console.log("The everydayPack object:", everydayPack);
console.log("The pocketNum value:", everydayPack.pocketNum);

```

## Output

```x
The everydayPack object: Backpack {name: 'Everyday Backpack', volume: 30, color: 'grey', pocketNum: 15, strapLength: {…}, …}
The pocketNum value: 15
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9ba1b5a0-e4b3-4b20-82a6-2f147e214b1f)

<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/3b359261-5164-472b-aaa0-6e28bb1d527a">

<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d4550153-068d-48db-b8d7-ab06394f56d9">

# #END</details>

<details>
<summary>8-JS Objects - Functional Object Constructors as Blueprints </summary>

# JS Objects - Functional Object Constructors as Blueprints

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_11/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Classes</title>
    <script src="script.js" defer></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_11/script.js:

```js
/**
 * Create an object constructor function for the Backpack object type.
 * @link https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new
 */

function Backpack(
  name,
  volume,
  color,
  pocketNum,
  strapLengthL,
  strapLengthR,
  lidOpen
) {
  this.name = name;
  this.volume = volume;
  this.color = color;
  this.pocketNum = pocketNum;
  this.strapLength = {
    left: strapLengthL,
    right: strapLengthR,
  };
  this.lidOpen = lidOpen;

  // Methods are within the Constructor
  this.toggleLid = function (lidStatus) {
    this.lidOpen = lidStatus;
  };
  this.newStrapLength = function (lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  };
}

const everydayPack = new Backpack(
  "Everyday Backpack",
  30,
  "grey",
  15,
  26,
  26,
  false
);

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/34bcd280-72f6-494f-8071-94e599e0a678)

<img width="1448" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/f742e4f2-6adb-4cec-8acf-729fc1655e05">

# Another Sample

```js
const bookTitle = "Alice's Adventures in Wonderland"
const bookAuthor = "Lewis Carroll"
const bookPubYear = 1865
const bookISBN = 9798369203415

// Your code goes here
function Book(bookTitle, bookAuthor, bookISBN, bookPubYear){
        this.title = bookTitle
        this.author = bookAuthor
        this.ISBN = bookISBN
        this.publicationYear = bookPubYear
}

```

# #END</details>

<details>
<summary>9-JS Objects - Extending Classes </summary>

# JS Objects - Extending Classes

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_11/index.html:

```js
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Extending Classes</title>
    <script src="script.js" defer></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_11/script.js:

```js
/**
 * Create an object constructor function for the Backpack object type.
 * @link https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new
 */

class Backpack {
  constructor(
    // Defines parameters:
    name,
    volume,
    color,
    pocketNum,
    strapLengthL,
    strapLengthR,
    lidOpen
  ) {
    // Define properties:
    this.name = name;
    this.volume = volume;
    this.color = color;
    this.pocketNum = pocketNum;
    this.strapLength = {
      left: strapLengthL,
      right: strapLengthR,
    };
    this.lidOpen = lidOpen;
  }

  // Add methods like normal functions:
  toggleLid(lidStatus) {
    this.lidOpen = lidStatus;
  }
  newStrapLength(lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  }
}

class HikingBackpack extends Backpack {
  constructor(
    name,
    volume,
    color,
    pocketNum,
    strapLengthL,
    strapLengthR,
    lidOpen,
    hydrationCapacity
  ) {
    // Initialize the parent class properties
    super(name, volume, color, pocketNum, strapLengthL, strapLengthR, lidOpen);
    // New property specific to HikingBackpack
    this.hydrationCapacity = hydrationCapacity; // Capacity in liters
  }

  // Method to check the hydration level and alert if it needs refilling
  checkHydration() {
    if (this.hydrationCapacity > 0) {
      console.log(`You have ${this.hydrationCapacity} liters of water left.`);
    } else {
      console.log("Time to refill your water!");
    }
  }

  // Extend or override methods from the parent class if necessary
  // For example, adding extra functionality when the lid is toggled
  toggleLid(lidStatus) {
    super.toggleLid(lidStatus); // Call the parent method
    if (lidStatus) {
      console.log(
        "Your hiking backpack lid is open. Remember to check to make sure the hydration pack is inserted."
      );
    } else {
      console.log(
        "Your hiking backpack lid is closed. Remember to check to make sure the hydration pack is inserted."
      );
    }
  }
}

const everydayPack = new HikingBackpack(
  "Everyday Backpack",
  30,
  "grey",
  15,
  26,
  26,
  false,
  30
);

console.log("The everydayPack object:", everydayPack);
console.log("The hydration level:", everydayPack.hydrationCapacity);
console.log("Check the hydration pack", everydayPack.checkHydration());
console.log("Open the lid", everydayPack.toggleLid(true));

```

## Output

```x
The everydayPack object: HikingBackpack {name: 'Everyday Backpack', volume: 30, color: 'grey', pocketNum: 15, strapLength: {…}, …}
The hydration level: 30
You have 30 liters of water left.
Check the hydration pack undefined
Your hiking backpack lid is open. Remember to check to make sure the hydration pack is inserted.
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/feb208e1-8c4b-4bdb-9fb0-9e998fcb934b)

<img width="1448" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/b49ff9ef-27fd-4d26-92e8-ceceee4c45d6">

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/Practice/03_12b/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Practice: Making classes and objects</title>
    <script type="module" src="script.js" defer></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/Practice/03_12b/script.js:

```js
/**
 * Practice: Making classes and objects
 *
 * - Find a type of object you have more than one of in your house (eg. clothing, writing tools, etc).
 * - Create a class describing this object type - its properties and methods.
 * - Create several objects using the class.
 * - Test the objects by calling their properties and using their methods in the console.
 */

import { Jug, ArmyJug } from "./Jug.js";

const mySmallJug = new Jug("My Small Jug", 5, "green", "plastic", false);
const myArmyJug = new ArmyJug("My Army Jug", 10, "brown", "metal", true, true);

console.log(mySmallJug);
console.log(mySmallJug.volume);
console.log(mySmallJug.setVolume(10));
console.log(mySmallJug.volume);

console.log(myArmyJug);
console.log(myArmyJug.color);
console.log(myArmyJug.hasStraw);
console.log(myArmyJug.toggleStraw());
console.log(myArmyJug.hasStraw);

/**
 * Creates a new WaterJug object.
 * @param {string} name - The name of the WaterJug.
 * @param {number} volume - The volume of the water in the jug in liters.
 * @param {string} color- The color of the water jug.
 * @param {string} material - The type of material used to make the jug.
 * @param {boolean} lidOpen - The status of the lid on the jug.
 */

const waterJug = {
  name: "Water Jug",
  volume: 15,
  color: "blue",
  material: "plastic",
  lidOpen: false,

  toggleLid: function (lidStatus) {
    this.lidOpen = lidStatus;
  },
  setVolume: function (newVolume) {
    this.volume = newVolume;
    console.log("The new volume is: ", this.volume);
  },
  setName: function (newName) {
    this.name = newName;
    console.log("The new name is: ", this.name);
  },
};

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/Practice/03_12b/Jug.js:

```js
/**
 * Represents a water jug with various properties.
 * @class Jug
 * @constructor
 * @param {string} name - The name of the water jug.
 * @param {number} volume - The volume of water in the jug, in liters.
 * @param {string} color - The color of the jug.
 * @param {string} material - The material used to make the jug.
 * @param {boolean} lidOpen - Indicates whether the jug's lid is open or closed.
 */
class Jug {
  constructor(name, volume, color, material, lidOpen) {
    this.name = name;
    this.volume = volume;
    this.color = color;
    this.material = material;
    this.lidOpen = lidOpen;
  }

  /**
   * Toggles the status of the Jug's lid from open to close or vice versa.
   * @returns {void}
   */
  toggleLid(lidStatus) {
    this.lidOpen = lidStatus;
  }

  /**
   * Sets the volume of the Jug.
   * Logs the new volume to the console.
   * @param {number} newVolume - The new volume to set.
   * @returns {void}
   */
  setVolume(newVolume) {
    this.volume = newVolume;
    console.log(`The new volume is: ${this.volume}`);
  }

  /**
   * Sets the name of the Jug.
   * Logs the new name to the console.
   * @param {string} newName - The new name to set.
   * @returns {void}
   */
  setName(newName) {
    this.name = newName;
    console.log("The new name is: ", this.name);
  }
}

/**
 * Represents an Army Jug with properties and methods
 *
 * @class ArmyJug
 * @extends {Jug}
 * @constructor
 * @param {string} name - The name of the water jug.
 * @param {number} volume - The volume of water in the jug, in liters.
 * @param {string} color - The color of the jug.
 * @param {string} material - The material used to make the jug.
 * @param {boolean} lidOpen - Indicates whether the jug's lid is open or closed.
 * @param {boolean} hasStraw - Indicates whether a straw is in the Jug as true or false.
 */
class ArmyJug extends Jug {
  constructor(name, volume, color, material, lidOpen, hasStraw) {
    super(name, volume, color, material, lidOpen);
    this.hasStraw = true;
  }

  /**
   * Toggle the status of the hasStraw property in the Army Jug.
   * Logs the hasStraw property status
   * @returns {void}
   */
  toggleStraw() {
    this.hasStraw = !this.hasStraw;
    console.log("The straw is: ", this.hasStraw ? "inside" : "outside");
  }

  /**
   * Sets the volume of the Army Jug.
   * overwrites the setVolume method in the Jug class.
   * @param {number} newVolume
   * @returns {void}
   */
  setVolume(newVolume) {
    this.volume = newVolume;
    console.log("The new Army Jug volume is: ", this.volume + 30);
  }

  /**
   * Sets the name of the Army Jug.
   * Extends the setName method in the Jug class.
   * @param {string} newName
   * @returns {void}
   */
  setName(newName) {
    super.setName(newName);
    console.log("It is an Army Jug.");
  }
}

export { Jug, ArmyJug };

```

Output:

```x
Jug {name: 'My Small Jug', volume: 5, color: 'green', material: 'plastic', lidOpen: false}
5
The new volume is: 10
undefined
10

ArmyJug {name: 'My Army Jug', volume: 10, color: 'brown', material: 'metal', lidOpen: true, …}
brown
true
The straw is:  outside
undefined
false
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/47c10e6b-99d5-47c0-a8de-29738095641e)

<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/29e83d69-f50c-4be6-9067-85c2882a04f8">
<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/e47dcdf0-54e9-4688-a274-2f710a41cfea">

# #END</details>

<details>
<summary>10-JS Objects - Global Date Object </summary>

# JS Objects - Global Date Object

## MDN Date Object = [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_13e/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Classes</title>
    <script type="module" src="Backpack.js"></script>
    <script type="module" src="script.js"></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_13e/Backpack.js:

```js
class Backpack {
  constructor(
    name,
    volume,
    color,
    pocketNum,
    strapLengthL,
    strapLengthR,
    lidOpen,
    dateAcquired
  ) {
    this.name = name;
    this.volume = volume;
    this.color = color;
    this.pocketNum = pocketNum;
    this.strapLength = {
      left: strapLengthL,
      right: strapLengthR,
    };
    this.lidOpen = lidOpen;
    this.dateAcquired = dateAcquired;
  }
  toggleLid(lidStatus) {
    this.lidOpen = lidStatus;
  }
  newStrapLength(lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  }
  backpackAge() {
    let now = new Date();
    let acquired = new Date(this.dateAcquired);
    let elapsed = now - acquired; // elapsed time in milliseconds
    let daysSinceAcquired = Math.floor(elapsed / (1000 * 3600 * 24));
    return daysSinceAcquired;
  }
}

export default Backpack;

```

## src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/03_13e/script.js:

```js
/**
 * Use the global Date() object to transform dates.
 * @link https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date
 */

import Backpack from "./Backpack.js";

const everydayPack = new Backpack(
  "Everyday Backpack",
  30,
  "grey",
  15,
  26,
  26,
  false,
  "December 5, 2018 15:00:00 PST"
);

console.log("The everydayPack object:", everydayPack);
console.log("The pocketNum value:", everydayPack.pocketNum);
console.log("Days since aquired:", everydayPack.backpackAge());

```

## Output:

```x
The everydayPack object: Backpackcolor: "grey"dateAcquired: "December 5, 2018 15:00:00 PST"lidOpen: falsename: "Everyday Backpack"pocketNum: 15strapLength: {left: 26, right: 26}volume: 30[[Prototype]]: Object
The pocketNum value: 15
Days since aquired: 2037
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9a2a61b7-ca8d-4554-b86a-d1624499a55b)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d3a59e24-4111-4d70-bb3a-48d87fab09e1)

<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/db55a596-3671-42f4-a807-4fe8ca68f5e0">
<img width="1492" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/e20dafea-3b85-4fa6-90e4-6b15cb58e403">

# #END</details>

<details>
<summary>11-JS Strings - Using Template Literals (for HTML in JS) </summary>

# JS Strings - Using Template Literals (for HTML in JS)

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/04_01e/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>String output</title>
    <script type="module" src="Backpack.js"></script>
    <script type="module" src="script.js"></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/04_01e/Backpack.js:

```js
class Backpack {
  constructor(
    name,
    volume,
    color,
    pocketNum,
    strapLengthL,
    strapLengthR,
    lidOpen,
    dateAcquired
  ) {
    this.name = name;
    this.volume = volume;
    this.color = color;
    this.pocketNum = pocketNum;
    this.strapLength = {
      left: strapLengthL,
      right: strapLengthR,
    };
    this.lidOpen = lidOpen;
    this.dateAcquired = dateAcquired;
  }
  toggleLid(lidStatus) {
    this.lidOpen = lidStatus;
  }
  newStrapLength(lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  }
  backpackAge() {
    let now = new Date();
    let acquired = new Date(this.dateAcquired);
    let elapsed = now - acquired; // elapsed time in milliseconds
    let daysSinceAcquired = Math.floor(elapsed / (1000 * 3600 * 24));
    return daysSinceAcquired;
  }
}

export default Backpack;

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/04_01e/script.js:

```js
/**
 * Use template literals to output HTML
 * @link https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
 *
 */
import Backpack from "./Backpack.js";

const everydayPack = new Backpack(
  "Everyday Pack",
  30,
  "grey",
  15,
  26,
  26,
  false,
  "December 5, 2018 15:00:00 PST"
);

const content = `
  <main>
    <article>
      <h1>${everydayPack.name}</h1>
      <ul>
        <li>Volume: ${everydayPack.volume}</li>
        <li>Color: ${everydayPack.color}</li>
        <li>Age: ${everydayPack.backpackAge()}</li>
        <li>Number of pockets: ${everydayPack.pocketNum}</li>
        <li>Left strap length: ${everydayPack.strapLength.left}</li>
        <li>Right strap length: ${everydayPack.strapLength.right}</li>
        <li>Lid status: ${everydayPack.lidOpen}</li>
      </ul>
    </article>
  </main>
`;

document.body.innerHTML = content;

console.log("The everydayPack object:", everydayPack);
console.log("The pocketNum value:", everydayPack.pocketNum);
console.log("Days since aquired:", everydayPack.backpackAge());

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/fb480a4f-e1f2-4605-807f-fb3f70dc36be)

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/434dad16-3e99-491f-982a-137dba71e989">

## Another Example:

```js
function Camera(brand, model, year, format, lens, filmType) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.format = format;
    this.lens = lens;
    this.filmType = filmType;
}

const getCurrentYear = () => new Date().getFullYear();

const cameraAge = (year) => getCurrentYear() - year;

// Goal output:
// My camera is a [brand] [model] made in [year] making it [age] years old. It's a [format] camera with a [lens] lens using [filmtype] film.`
const cameraHTML = (myCamera) => {
    // Your code goes between the backticks in `cameraStory` below.
    const cameraStory = `My camera is a ${myCamera.brand} ${myCamera.model} made in ${myCamera.year} making it ${cameraAge(myCamera.year)} years old. It's a ${myCamera.format} camera with a ${myCamera.lens} lens using ${myCamera.filmType} film.`;
    return cameraStory;
}    

const myCamera = new Camera("Hasselblad", "500C/M", 1963, "medium format", "Carl Zeiss 80mm f/2.8 Planar T", "120")
const result = cameraHTML(myCamera);

```

```x
Your code returned:
My camera is a Hasselblad 500C/M made in 1963 making it 61 years old.
It's a medium format camera with a Carl Zeiss 80mm f/2.8 Planar T lens using 120 film.
```

# #END</details>

<details>
<summary>12-JS Strings - Using Traditional String Concatenation (for HTML in JS) </summary>

# JS Strings - Using Traditional String Concatenation (for HTML in JS)

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/04_02e/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>String output</title>
    <script type="module" src="Backpack.js"></script>
    <script type="module" src="script.js"></script>
  </head>
  <body></body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/04_02e/Backpack.js:

```js
class Backpack {
  constructor(
    name,
    volume,
    color,
    pocketNum,
    strapLengthL,
    strapLengthR,
    lidOpen,
    dateAcquired
  ) {
    this.name = name;
    this.volume = volume;
    this.color = color;
    this.pocketNum = pocketNum;
    this.strapLength = {
      left: strapLengthL,
      right: strapLengthR,
    };
    this.lidOpen = lidOpen;
    this.dateAcquired = dateAcquired;
  }
  toggleLid(lidStatus) {
    this.lidOpen = lidStatus;
  }
  newStrapLength(lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  }
  backpackAge() {
    let now = new Date();
    let acquired = new Date(this.dateAcquired);
    let elapsed = now - acquired; // elapsed time in milliseconds
    let daysSinceAcquired = Math.floor(elapsed / (1000 * 3600 * 24));
    return daysSinceAcquired;
  }
}

export default Backpack;

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/04_02e/script.js:

```js
/**
 * Use template literals to output HTML
 * @link https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
 *
 */
import Backpack from "./Backpack.js";

const everydayPack = new Backpack(
  "Everyday Pack",
  30,
  "grey",
  15,
  26,
  26,
  false,
  "December 5, 2018 15:00:00 PST"
);

const content = "<h1>" + everydayPack.name + "</h1>";

document.body.innerHTML = content;

console.log("The everydayPack object:", everydayPack);
console.log("The pocketNum value:", everydayPack.pocketNum);
console.log("Days since aquired:", everydayPack.backpackAge());

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/97714b71-c017-4c32-9561-07c68819c9e7)

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/8748fd99-1438-4d96-918f-d17fe415c635">

# #END</details>

<details>
<summary>13-JS DOM - Access DOM Elements and Target CSS Queries with querySelectors </summary>

# JS DOM - Access DOM Elements and Target CSS Queries with querySelectors

## Select an element

```js
// Select the main element
document.querySelector("main")

// Select the article element in the main element
document.querySelector("main article")

// Select the main->article->figure->img element
document.querySelector("main article figure img")
document.querySelector("main img")

// Style the article element with a red border
document.querySelector("article").style.border="10px solid orange"
```

## Select all elements

```js
// Select all the list items
document.querySelectorAll("main li")

//Select the first item in the list
document.querySelectorAll("main li")[0]
document.querySelectorAll("main li:first-child")
document.querySelectorAll("main li:first-of-type")
document.querySelectorAll("main li:first-child").forEach(item => item.style.backgroundColor="blue")

//Select the last item in the list
document.querySelectorAll("main li")[(document.querySelectorAll("main li").length) - 1]
document.querySelectorAll("main li:last-child")
document.querySelectorAll("main li:last-of-type")
document.querySelectorAll("main li:last-child").forEach(item => item.style.backgroundColor="red")

//Select the third item in the list
document.querySelectorAll("main li:nth-child(3)")
document.querySelectorAll("main li:nth-child(3)").forEach(item => item.style.backgroundColor="purple")

//Select the first to third items from the top of the list
document.querySelectorAll("main li:nth-child(-n + 3)")
document.querySelectorAll("main li:nth-child(-n + 3)").forEach(item => item.style.border="5px solid red")

//Select the first to third items from the bottom of the list
document.querySelectorAll("main li:nth-last-child(-n + 3)")
document.querySelectorAll("main li:nth-last-child(-n + 3)").forEach(item => item.style.border="5px solid blue")

//Select the even indexed items in the list
document.querySelectorAll("main li:nth-child(even)")
document.querySelectorAll("main li:nth-child(even)").forEach(item => item.style.backgroundColor="#f0f8ff")

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/a9914140-a3a5-4e57-a727-74ec8cb901fd)

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/05_02/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>BackpackPacker</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&family=Work+Sans:wght@100..900&display=swap"
      rel="stylesheet"
    />
    <link
      rel="stylesheet"
      href="../assets/style.css"
      type="text/css"
      media="all"
    />
    <script type="module" src="Backpack.js"></script>
    <script type="module" src="script.js"></script>
  </head>
  <body>
    <header class="siteheader">
      <div class="site-title">BackpackPacker</div>
      <div class="site-description">All backpack packing, all the time.</div>
    </header>
    <main class="maincontent"></main>
    <footer class="sitefooter">
      <p>
        Demo project for JavaScript Essential Training, a LinkedIn Learning
        course.
      </p>
    </footer>
  </body>
</html>

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/05_02/Backpack.js:

```js
class Backpack {
  constructor(
    name,
    volume,
    color,
    pocketNum,
    strapLengthL,
    strapLengthR,
    lidOpen,
    dateAcquired,
    image
  ) {
    this.name = name;
    this.volume = volume;
    this.color = color;
    this.pocketNum = pocketNum;
    this.strapLength = {
      left: strapLengthL,
      right: strapLengthR,
    };
    this.lidOpen = lidOpen;
    this.dateAcquired = dateAcquired;
    this.image = image;
  }
  toggleLid(lidStatus) {
    this.lidOpen = lidStatus;
  }
  newStrapLength(lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  }
  backpackAge() {
    let now = new Date();
    let acquired = new Date(this.dateAcquired);
    let elapsed = now - acquired; // elapsed time in milliseconds
    let daysSinceAcquired = Math.floor(elapsed / (1000 * 3600 * 24));
    return daysSinceAcquired;
  }
}

export default Backpack;

```

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/05_02/script.js:

```js
/**
 * Traverse the DOM tree using querySelector() and querySelectorAll()
 * @link https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector
 * @link https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll
 */

import Backpack from "./Backpack.js";

const everydayPack = new Backpack(
  "Everyday Backpack",
  30,
  "grey",
  15,
  26,
  26,
  false,
  "December 5, 2018 15:00:00 PST",
  "../assets/images/everyday.svg"
);

const main = document.querySelector(".maincontent");

const content = `
  <article class="backpack" id="everyday">
    <figure class="backpack__image">
      <img src=${everydayPack.image} alt="" />
    </figure>
    <h1 class="backpack__name">${everydayPack.name}</h1>
    <ul class="backpack__features">
      <li class="backpack__volume">Volume:<span> ${
        everydayPack.volume
      }l</span></li>
      <li class="backpack__color">Color:<span> ${everydayPack.color}</span></li>
      <li class="backpack__age">Age:<span> ${everydayPack.backpackAge()} days old</span></li>
      <li class="backpack__pockets">Number of pockets:<span> ${
        everydayPack.pocketNum
      }</span></li>
      <li class="backpack__strap">Left strap length:<span> ${
        everydayPack.strapLength.left
      } inches</span></li>
      <li class="backpack__strap">Right strap length:<span> ${
        everydayPack.strapLength.right
      } inches</span></li>
      <li class="backpack__lid">Lid status:<span> ${
        everydayPack.lidOpen
      }</span></li>
    </ul>
  </article>
`;

main.innerHTML = content;

```

<img width="1490" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/7d753a3f-726e-4de8-9d3d-fc6e730d2fd2">

# #END</details>

<details>
<summary>14-JS DOM - Modifying DOM Element Classes </summary>

# JS DOM - Modifying DOM Element Classes

## Get the ClassName of an element

```js
document.querySelector("main li").className
// 'backpack__volume'

document.querySelector("main li").classList
// DOMTokenList ['backpack__volume', value: 'backpack__volume']
```

## Get the ClassName of an element in a List

```js
document.querySelectorAll("main li:first-child")[0].classList
// DOMTokenList ['backpack__volume', value: 'backpack__volume']
```

## Add a new class to an element in a List

```js
document.querySelectorAll("main li:first-child")[0].classList.add("backpack__volume2")

document.querySelectorAll("main li:first-child")[0].classList
// DOMTokenList(2) ['backpack__volume', 'backpack__volume2', value: 'backpack__volume backpack__volume2']
```

## Remove a class from an element in a List

```js
document.querySelectorAll("main li:first-child")[0].classList.remove("backpack__volume2")

document.querySelectorAll("main li:first-child")[0].classList
// DOMTokenList ['backpack__volume', value: 'backpack__volume']
```

## Toggle: Add a class (if not exist) or Remove it (if exists) from an element in a List

```js
document.querySelectorAll("main li:first-child")[0].classList.toggle("backpack__volume3")

document.querySelectorAll("main li:first-child")[0].classList
// DOMTokenList(2) ['backpack__volume', 'backpack__volume3', value: 'backpack__volume backpack__volume3']
```

## Replace a class in an element in a List

```js
document.querySelectorAll("main li:first-child")[0].classList.replace("backpack__volume3", "backback__dim")

document.querySelectorAll("main li:first-child")[0].classList
// DOMTokenList(2) ['backpack__volume', 'backback__dim', value: 'backpack__volume backback__dim']
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/05835043-e5fe-4244-a3fa-ae90c5dc2be4)

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/05_02/script.js:

```js
/**
 * Traverse the DOM tree using querySelector() and querySelectorAll()
 * @link https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector
 * @link https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll
 */

import Backpack from "./Backpack.js";

const everydayPack = new Backpack(
  "Everyday Backpack",
  30,
  "grey",
  15,
  26,
  26,
  false,
  "December 5, 2018 15:00:00 PST",
  "../assets/images/everyday.svg"
);

const main = document.querySelector(".maincontent");

const content = `
  <article class="backpack" id="everyday">
    <figure class="backpack__image">
      <img src=${everydayPack.image} alt="" />
    </figure>
    <h1 class="backpack__name">${everydayPack.name}</h1>
    <ul class="backpack__features">
      <li class="backpack__volume">Volume:<span> ${
        everydayPack.volume
      }l</span></li>
      <li class="backpack__color">Color:<span> ${everydayPack.color}</span></li>
      <li class="backpack__age">Age:<span> ${everydayPack.backpackAge()} days old</span></li>
      <li class="backpack__pockets">Number of pockets:<span> ${
        everydayPack.pocketNum
      }</span></li>
      <li class="backpack__strap">Left strap length:<span> ${
        everydayPack.strapLength.left
      } inches</span></li>
      <li class="backpack__strap">Right strap length:<span> ${
        everydayPack.strapLength.right
      } inches</span></li>
      <li class="backpack__lid">Lid status:<span> ${
        everydayPack.lidOpen
      }</span></li>
    </ul>
  </article>
`;

main.innerHTML = content;

```

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/90c3ed29-7cf5-4485-91f4-04b8a1bdcc34">

# #END</details>

<details>
<summary>15-JS DOM - Accessing DOM Attributes with Methods </summary>

# JS DOM - Accessing DOM Attributes with Methods

## Check if element has attribute

```js
document.querySelector("main img")
// <img src="../assets/images/everyday.svg" alt="">

document.querySelector("main img").hasAttribute("id")
// false

document.querySelector("main img").hasAttribute("src")
// true
```

## Get the value assigned to attribute

```js
document.querySelector("main img")
// <img src="../assets/images/everyday.svg" alt="">

document.querySelector("main img").getAttribute("src")
// '../assets/images/everyday.svg'
```

## Set a value to attribute

```js
document.querySelector("main img")
// <img src="../assets/images/everyday.svg" alt="">

document.querySelector("main img").setAttribute("alt", "A drawing of a backpack")

document.querySelector("main img")
// <img src="../assets/images/everyday.svg" alt="A drawing of a backpack">

document.querySelector("main img").setAttribute("title", "This image shouldn't be here.")

document.querySelector("main img")
// <img src="../assets/images/everyday.svg" alt="A drawing of a backpack" title="This image shouldn't be here.">
```

## Remove value from attribute

```js
document.querySelector("main img").removeAttribute("title")

document.querySelector("main img")
// <img src="../assets/images/everyday.svg" alt="A drawing of a backpack">
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d48ef5bc-0297-4baa-9db8-3c312d53f76d)

### src-AI-Software/my_projects/06_js_ess_proj/Exercises/DEMO/05_05/script.js:

```js
/**
 * Traverse the DOM tree using querySelector() and querySelectorAll()
 * @link https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector
 * @link https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll
 */

import Backpack from "./Backpack.js";

const everydayPack = new Backpack(
  "Everyday Backpack",
  30,
  "grey",
  15,
  26,
  26,
  false,
  "December 5, 2018 15:00:00 PST",
  "../assets/images/everyday.svg"
);

const main = document.querySelector(".maincontent");

const content = `
  <article class="backpack" id="everyday">
    <figure class="backpack__image">
      <img src=${everydayPack.image} alt="" />
    </figure>
    <h1 class="backpack__name">${everydayPack.name}</h1>
    <ul class="backpack__features">
      <li class="packprop backpack__volume">Volume:<span> ${
        everydayPack.volume
      }l</span></li>
      <li class="packprop backpack__color">Color:<span> ${
        everydayPack.color
      }</span></li>
      <li class="backpack__age">Age:<span> ${everydayPack.backpackAge()} days old</span></li>
      <li class="packprop backpack__pockets">Number of pockets:<span> ${
        everydayPack.pocketNum
      }</span></li>
      <li class="packprop backpack__strap">Left strap length:<span> ${
        everydayPack.strapLength.left
      } inches</span></li>
      <li class="packprop backpack__strap">Right strap length:<span> ${
        everydayPack.strapLength.right
      } inches</span></li>
      <li class="packprop backpack__lid">Lid status:<span> ${
        everydayPack.lidOpen
      }</span></li>
    </ul>
  </article>
`;

main.innerHTML = content;

```

<img width="1534" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/05fb6fe3-9b96-45f8-9373-9502aec8efa0">

# #END</details>

<details>
<summary>16-JS DOM - Inline Styling of DOM Elements </summary>

# JS DOM - Inline Styling of DOM Elements

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

```js

```

```js

```


# #END</details>
