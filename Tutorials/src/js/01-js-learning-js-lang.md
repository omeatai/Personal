## 01-Learning Javascript Language

## [COURSE](https://www.linkedin.com/learning/learning-the-javascript-language-22309208/become-conversant-in-javascript?resume=false)

<details>
<summary>1-Declaring and Assigning Variables</summary>

## Declaring and Assigning Variables

```js
var x = 32;
x;

var whereAmI = "Santa Barbara, CA";
whereAmI;

x = 45;
x;

whereAmI = 75;
whereAmI;

var monster1 = "Grover",
  monster2 = "Cookie Monster",
  monster3 = "Animal";

monster1;
monster2;
monster3;

```

<img width="1506" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/463e4f30-365d-4de0-94cb-b34e8d2c19d8">

# #END</details>

<details>
<summary>2-Strings</summary>

## Strings

```js
"This is a string";
"12";
// 12;

"This is also a string";
// 'This is a string"; // mismatched quotes - this will not execute

'<a href="">';
'<a href="http://www.example.com">';

"This is Joe's favorite string";
'This is Joe\'s "favorite" string';
"This is Joe's \"favorite\" string";

"This is \
Joe's Favorite \
String EVER";

```

<img width="1514" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/c1f9baff-b3c3-4ae6-a201-bf1173799327">


# #END</details>

<details>
<summary>3-String Properties and Methods</summary>

## String Properties and Methods

```js
var myString = "This is my string. Leave it alone";

myString;

var str1Len = myString.length;
str1Len;

var str1Upper = myString.toUpperCase();
str1Upper;

var str2Len = "This is my string".length;
str2Len;

let declaration = `This I say to you: "good morning". Huzzah!`;
declaration;

declaration = `This I say to you: "${myString}". Huzzah!`;
declaration;

```

<img width="1514" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/b05854dd-35c2-4e7c-a1e3-4e5c3d1b7a66">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/013fcf11-ccef-4026-953d-3f0df9725c0e)

# #END</details>

<details>
<summary>4-Numbers</summary>

## Numbers

```js
12;
12.0;
12.82358972893527582
-12;
Infinity
-Infinity;
NaN;

var myNumber = 33;

var num1 = Math.round(12.4984012840918);
console.log(num1);

var num2 = Math.round(12.92309820948209384);
console.log(num2);

var num3 = Math.random();
console.log(num3);

var num4 = Math.random();
console.log(num4);

var num5 = Math.random();
console.log(num5);

var num6 = Math.random();
console.log(num6);

// More info:
// https://developer.mozilla.org/en-US/docs/Glossary/Number
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Infinity
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math

```

<img width="1511" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/f12529a8-8819-4450-ae48-933cd9922b8d">

# #END</details>

<details>
<summary>5-Booleans</summary>

## Booleans

```js
// true;
// false;

var myLocation = "Santa Barbara",
  myOtherLocation = "Los Angeles",
  buttonHasBeenClicked = false;

console.log(buttonHasBeenClicked);
console.log(myLocation);
console.log(myOtherLocation);

console.log(myLocation === myOtherLocation);

myOtherLocation = "Santa Barbara";

console.log(myLocation === myOtherLocation);

// More info:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#literals
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean

```

<img width="1511" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/cbd382d3-d73f-4adf-b538-516703590561">

# #END</details>

<details>
<summary>6-Variable immutability with const and let</summary>

## Variable immutability with const and let

```js
const dozen = 12,
  halfDozen = 6,
  bakersDozen = 13;

// dozen = 13; WRONG! Assignment to constant variable.
console.log(dozen);

let cookieCount = 5;
// var cookieCount = 10; Identifier 'cookieCount' has already been declared

// More info:
// http://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let
// http://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const

```

<img width="1511" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9f769cee-5485-4745-8bd1-80337f0f964a">

# #END</details>

<details>
<summary>7-Objects</summary>

## Objects

```js
var emptyObject = {};
emptyObject;

var notEmptyObject = {
  label: "value",
  label2: "value2",
};

notEmptyObject;

let bird = {
  genus: "corvus",
  species: "corvax",
  commonName: "raven",
  callType: "squawky",
  quote: "Nevermore",
  maxOffspring: 5,
  noisy: true,
  deadly: false,
};

let bear = {
  genus: "ursus",
  species: "arctos",
  commonName: "brown bear",
  callType: "roar",
  quote: "",
  maxOffspring: 3,
  noisy: true,
  deadly: true,
};

const bookOfKnowledge = {
  "lunch time": "12:30 PM",
  "the ultimate answer": 42,
  bestSong: "Lonnie's Lament",
  earth: "Mostly harmless.",
};

console.log(bird);
console.log(bear);
console.log(bookOfKnowledge);

// More info:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer

```

<img width="1511" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/351e55ac-97ea-4e30-8814-284ae01282a6">

# #END</details>

<details>
<summary>8-Accessing and Manipulating Objects</summary>

## Accessing and Manipulating Objects

```js
var bird = {
  genus: "corvus",
  species: "corvax",
  commonName: "raven",
  callType: "squawky",
  quote: "Nevermore",
  maxOffspring: 5,
  noisy: true,
  deadly: false,
};

//Accessing Values in Object
// bird."quote"; // this does not work
console.log(bird.quote);
console.log(bird["quote"]);

//Manipulating Objects
bird.color = "black";
bird;

bird["where it lives"] = "in London";
bird.whereItLives = "in a small tree";

console.log(bird["where it lives"]);
console.log(bird.whereItLives);

delete bird.color;

bird;

// More info:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object

```

<img width="1511" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/33535a67-6a41-43d4-99d2-1b8d8a03ceff">

# #END</details>

<details>
<summary>9-Object References-Copying an Object safely </summary>

## Object References-Copying an Object safely

```js
var animal = {
  genus: "corvus",
  species: "corvax",
  commonName: "raven",
  callType: "squawky",
  quote: "Nevermore",
  maxOffspring: 5,
  noisy: true,
  deadly: false,
};

animal;

//Both animal2 and animal have same memory location
var animal2 = animal;

animal2;

animal2.deadly = true;
animal2;
animal;

// Make a copy of an object safely
animal2 = Object.assign({}, animal);
var animal3 = { ...animal };
var animal4 = JSON.parse(JSON.stringify(animal));

animal2.deadly = false;
animal3.quote = "I am animal 3";
animal4.quote = "I am animal 4";

animal;
animal2;
animal3;
animal4;

// More info:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object

```

<img width="1511" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/fbcb4774-fc4e-4189-b480-533470785cff">

# #END</details>

<details>
<summary>10-Arrays</summary>

## Arrays

```js
var myArray = [];
myArray;

var daysOfTheWeek = ["Sunday", "Monday", "Tuesday", "Wednesday"];
daysOfTheWeek;

var myList = [0, 1, 2, "string1", "string2", "string3", true, false];
myList;

var counties = ["Belknap", "Strafford", "Carroll", "Rockingham"];
counties;

var listOfStuff = [{ name: "value" }, [1, 2, 3], true, "nifty"];
listOfStuff;
console.log(listOfStuff.length);

// More info:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#array_literals
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

```

<img width="1378" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/a661e280-0407-4153-9819-e578bfeac800">


# #END</details>

<details>
<summary>11-Manipulating Arrays</summary>

## Manipulating Arrays

```js
var counties = ["Belknap", "Strafford", "Carroll", "Rockingham"];

// Get items from an array
console.log(counties[0]);
console.log(counties[2]);

// Add items at a specific index
counties[2] = "Cheshire";
counties;

counties[4] = "Carroll";
counties;

// Add items to the end of the array
counties[counties.length] = "Merrimack";
counties;

counties.push("Coos");
counties;

// Remove items from the end of the array
var removedValue = counties.pop();
removedValue;
counties;

// Delete an item from the array
delete counties[2];
counties;

// Remove specific items from the array
counties.splice(2, 1);
counties;
console.log(counties.length);

// More info:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

```

<img width="1378" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/bd6a0fd3-a1b2-4fd6-aa6b-190ca40f83f3">

# #END</details>

<details>
<summary>12-Whitespace</summary>

## Whitespace

```js
var year=2012,month='October',day=31,holiday='Halloween';

var year   = 2012,       month    =    'October', day =          31,          holiday='Halloween';

var year = 2012,
	month = 'October',
	day = 31,
	holiday = 'Halloween';
	
var year  = 2012,
	month   = 'October',
	day     = 31,
	holiday = 'Halloween';

var tinyAlmanac={'year':2012,'month':'October','day':31,'holiday':'Halloween'};

var tinyAlmanac = {
	'year' : 2012,
	'month' : 'October',
	'day' : 31,
	'holiday' : 'Halloween'
};

var longString = "Four score \
and seven years ago \
our fathers brought forth \
on this continent \
a new nation";

// More info:
// These are not specifications on whitespace, but the Mozilla code style guide discusses formatting.
// https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide/Code_style_guide/JavaScript#choosing_a_format

```

<img width="1378" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d037f37a-ad7d-4f40-8df3-6323448ae23e">

# #END</details>

<details>
<summary>13-Comments</summary>

## Comments

```js
// another after the slashes does not execute
var year = 2012,
  month = "October", // this is the month
  day = 31,
  holiday = "Halloween";

/*
You can write comments
across multiple lines
finally ending with:
*/

var tinyAlmanac = {
  year: 2012,
  month: "October",
  day: 31,
  holiday: "Halloween",
};

// watch out for block comments here
var myRegExp = /[0-9].*/;

// More info:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#comments

```

<img width="1378" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d8065503-e1a5-47c8-8d58-74b93dcf42f1">


# #END</details>

<details>
<summary>14-Regular Expressions </summary>

## Regular Expressions

```js
var string1 = "This is the longest string ever.";
var string2 = "This is the shortest string ever.";
var string3 = "Is this the thing called Mount Everest?";
var string4 = "This is the Sherman on the Mount.";

var regex = /this/; // "this" is found in string

console.log(regex.test(string1));
console.log(regex.test(string2));
console.log(regex.test(string3));
console.log(regex.test(string4));

regex = /this/i; // "this" (case-insensitive) is found in string

console.log(regex.test(string1));
console.log(regex.test(string2));
console.log(regex.test(string3));
console.log(regex.test(string4));

regex = /^this/i; // "this" (case-insensitive) is found at the beginning of string

console.log(regex.test(string1));
console.log(regex.test(string2));
console.log(regex.test(string3));
console.log(regex.test(string4));

regex = /this$/i; // "this" (case-insensitive) is found at the end of string

console.log(regex.test(string1));
console.log(regex.test(string2));
console.log(regex.test(string3));
console.log(regex.test(string4));

regex = /ever.$/i; // "ever" (case-insensitive) is found at the end of string

console.log(regex.test(string1));
console.log(regex.test(string2));
console.log(regex.test(string3));
console.log(regex.test(string4));

regex = /ever\.$/i; // "ever." (case-insensitive) is found at the end of string

console.log(regex.test(string1));
console.log(regex.test(string2));
console.log(regex.test(string3));
console.log(regex.test(string4));

// More info:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
// http://regex.info/book.html

```

<img width="1378" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/8c6c76c7-094e-4b2c-b8d6-b9e0401d16bf">


# #END</details>

<details>
<summary>15-Comparisons </summary>

## Comparisons

```js
var one = 1,
  two = 2;

one === one; // true
one !== one; // false
one !== two; // true
one === two; // false

one == one; // true
one == "1"; // true (?!)
one != "1"; // false (?!)
one === "1"; // false

one < two; // true

one > two; // false

one <= two; // true

one <= one; // true

one >= two; // false

10 >= two; // true

// More info:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#equality_operators
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#relational_operators

```

<img width="1378" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/bb386faf-24a2-4628-a8a4-2cc957bfe1ec">

# #END</details>

<details>
<summary>16-Arithmetic Operators </summary>

## Arithmetic Operators

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
