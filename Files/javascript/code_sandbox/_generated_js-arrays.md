<details>
  <summary>JS Arrays</summary>

## Introduction

An array is an ordered, zero-indexed list of elements under one name. Literals use square brackets; you can also start empty and assign by index, or use new Array. Elements are heterogeneous: numbers, strings, objects, functions, and nested arrays can share one list. Arrays are objects (typeof is object), so Array.isArray or instanceof Array is how you recognize them. JavaScript has no associative array — named indexes do not create a list, they just add object properties and leave length at 0.

This section has **27** examples:

- [x] **Example 1:** const cars = ["Saab", "Volvo", "BMW"] [View](#js-arrays-example-01)
- [x] **Example 2:** Array literal spanning lines [View](#js-arrays-example-02)
- [x] **Example 3:** Empty array, then assign by index [View](#js-arrays-example-03)
- [x] **Example 4:** new Array("Saab", "Volvo", "BMW") [View](#js-arrays-example-04)
- [x] **Example 5:** Access cars[0] [View](#js-arrays-example-05)
- [x] **Example 6:** cars[0] = "Opel" [View](#js-arrays-example-06)
- [x] **Example 7:** fruits.toString() [View](#js-arrays-example-07)
- [x] **Example 8:** Display the array by name [View](#js-arrays-example-08)
- [x] **Example 9:** JSON.stringify(cars) [View](#js-arrays-example-09)
- [x] **Example 10:** Array: person[0] is John [View](#js-arrays-example-10)
- [x] **Example 11:** Object: person.firstName is John [View](#js-arrays-example-11)
- [x] **Example 12:** Array elements can be objects, functions, arrays [View](#js-arrays-example-12)
- [x] **Example 13:** fruits.length [View](#js-arrays-example-13)
- [x] **Example 14:** First element fruits[0] [View](#js-arrays-example-14)
- [x] **Example 15:** Last element fruits[fruits.length - 1] [View](#js-arrays-example-15)
- [x] **Example 16:** for loop over fruits [View](#js-arrays-example-16)
- [x] **Example 17:** fruits.forEach(myFunction) [View](#js-arrays-example-17)
- [x] **Example 18:** fruits.push("Lemon") [View](#js-arrays-example-18)
- [x] **Example 19:** fruits[fruits.length] = Lemon [View](#js-arrays-example-19)
- [x] **Example 20:** WARNING fruits[6] = Lemon creates holes [View](#js-arrays-example-20)
- [x] **Example 21:** Numbered indexes (not associative) [View](#js-arrays-example-21)
- [x] **Example 22:** WARNING named indexes become an object [View](#js-arrays-example-22)
- [x] **Example 23:** new Array(40, 100, 1, 5, 25, 10) vs literal [View](#js-arrays-example-23)
- [x] **Example 24:** typeof fruits is object [View](#js-arrays-example-24)
- [x] **Example 25:** Array.isArray(fruits) [View](#js-arrays-example-25)
- [x] **Example 26:** fruits instanceof Array [View](#js-arrays-example-26)
- [x] **Example 27:** Nested arrays and objects [View](#js-arrays-example-27)

## Detailed Explanation

- [x] Prefer an array **literal** `[]`. `const` is the usual declaration.
- [x] Indexes start at **0**. `length` is one more than the highest index.
- [x] `typeof` an array is **`object`**. Use **`Array.isArray`** (or `instanceof Array`).
- [x] Writing a **high index** or using **`delete`** leaves empty holes.
- [x] Named indexes do **not** make associative arrays — use an **object** for string keys.
- [x] One array may hold **objects, functions, and nested arrays**.

<a id="js-arrays-example-01"></a>

### **Example 1: const cars = ["Saab", "Volvo", "BMW"]**

- [x] An **array literal** is a comma-separated list inside **`[]`**.
- [x] Declare arrays with **`const`**. Indexes start at **0**.

Sandbox: `code_sandbox/js-arrays/literal-cars.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
```

<img alt="js-arrays example 1 source" src="./code_sandbox/snaps/js-arrays-01-code.png" />

<img alt="js-arrays example 1 result" src="./code_sandbox/snaps/js-arrays-01-result.png" />

- [x] **Outcome:** cars is **["Saab","Volvo","BMW"]**. The hero Tryit and the “Creating an Array” Tryit are the same snippet — shown once.

<a id="js-arrays-example-02"></a>

### **Example 2: Array literal spanning lines**

- [x] Spaces and line breaks do not matter. A declaration may span **multiple lines**.

Sandbox: `code_sandbox/js-arrays/literal-multiline.html`

```javascript
const cars = [
  "Saab",
  "Volvo",
  "BMW"
];
```

<img alt="js-arrays example 2 source" src="./code_sandbox/snaps/js-arrays-02-code.png" />

<img alt="js-arrays example 2 result" src="./code_sandbox/snaps/js-arrays-02-result.png" />

- [x] **Outcome:** Same value: **["Saab","Volvo","BMW"]**.

<a id="js-arrays-example-03"></a>

### **Example 3: Empty array, then assign by index**

- [x] Create **`[]`**, then set `cars[0]`, `cars[1]`, `cars[2]`.

Sandbox: `code_sandbox/js-arrays/empty-then-assign.html`

```javascript
const cars = [];
cars[0] = "Saab";
cars[1] = "Volvo";
cars[2] = "BMW";
```

<img alt="js-arrays example 3 source" src="./code_sandbox/snaps/js-arrays-03-code.png" />

<img alt="js-arrays example 3 result" src="./code_sandbox/snaps/js-arrays-03-result.png" />

- [x] **Outcome:** **["Saab","Volvo","BMW"]**.

<a id="js-arrays-example-04"></a>

### **Example 4: new Array("Saab", "Volvo", "BMW")**

- [x] `new Array(...)` with **several arguments** builds the same list as a literal.
- [x] Prefer **`[]`** for simplicity, readability, and speed.

Sandbox: `code_sandbox/js-arrays/new-array-cars.html`

```javascript
const cars = new Array("Saab", "Volvo", "BMW");
```

<img alt="js-arrays example 4 source" src="./code_sandbox/snaps/js-arrays-04-code.png" />

<img alt="js-arrays example 4 result" src="./code_sandbox/snaps/js-arrays-04-result.png" />

- [x] **Outcome:** **["Saab","Volvo","BMW"]** — same as the literal.

<a id="js-arrays-example-05"></a>

### **Example 5: Access cars[0]**

- [x] Read an element by **index**. **`[0]`** is the first element.

Sandbox: `code_sandbox/js-arrays/access-index-0.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
let car = cars[0];
```

<img alt="js-arrays example 5 source" src="./code_sandbox/snaps/js-arrays-05-code.png" />

<img alt="js-arrays example 5 result" src="./code_sandbox/snaps/js-arrays-05-result.png" />

- [x] **Outcome:** car is **"Saab"**.

<a id="js-arrays-example-06"></a>

### **Example 6: cars[0] = "Opel"**

- [x] Assignment to an index **replaces** that element. `const` still allows this.

Sandbox: `code_sandbox/js-arrays/change-element.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
cars[0] = "Opel";
```

<img alt="js-arrays example 6 source" src="./code_sandbox/snaps/js-arrays-06-code.png" />

<img alt="js-arrays example 6 result" src="./code_sandbox/snaps/js-arrays-06-result.png" />

- [x] **Outcome:** **["Opel","Volvo","BMW"]**.

<a id="js-arrays-example-07"></a>

### **Example 7: fruits.toString()**

- [x] `toString()` joins elements with **commas** (no spaces).

Sandbox: `code_sandbox/js-arrays/tostring.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let text = fruits.toString();
```

<img alt="js-arrays example 7 source" src="./code_sandbox/snaps/js-arrays-07-code.png" />

<img alt="js-arrays example 7 result" src="./code_sandbox/snaps/js-arrays-07-result.png" />

- [x] **Outcome:** **Banana,Orange,Apple,Mango**.

<a id="js-arrays-example-08"></a>

### **Example 8: Display the array by name**

- [x] Referring to the array name stringifies it the same way as `toString()`.

Sandbox: `code_sandbox/js-arrays/display-array-name.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
let text = String(cars);
```

<img alt="js-arrays example 8 source" src="./code_sandbox/snaps/js-arrays-08-code.png" />

<img alt="js-arrays example 8 result" src="./code_sandbox/snaps/js-arrays-08-result.png" />

- [x] **Outcome:** **Saab,Volvo,BMW**.

<a id="js-arrays-example-09"></a>

### **Example 9: JSON.stringify(cars)**

- [x] `JSON.stringify` shows **quotes** and **brackets** — useful for nested data.

Sandbox: `code_sandbox/js-arrays/json-stringify.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
let text = JSON.stringify(cars);
```

<img alt="js-arrays example 9 source" src="./code_sandbox/snaps/js-arrays-09-code.png" />

<img alt="js-arrays example 9 result" src="./code_sandbox/snaps/js-arrays-09-result.png" />

- [x] **Outcome:** **["Saab","Volvo","BMW"]**.

<a id="js-arrays-example-10"></a>

### **Example 10: Array: person[0] is John**

- [x] Arrays are objects, but you access **elements by number**.

Sandbox: `code_sandbox/js-arrays/array-numbered-person.html`

```javascript
const person = ["John", "Doe", 46];
```

<img alt="js-arrays example 10 source" src="./code_sandbox/snaps/js-arrays-10-code.png" />

<img alt="js-arrays example 10 result" src="./code_sandbox/snaps/js-arrays-10-result.png" />

- [x] **Outcome:** **["John","Doe",46]**. `person[0]` is **"John"**.

<a id="js-arrays-example-11"></a>

### **Example 11: Object: person.firstName is John**

- [x] Objects use **names** for members, not numbered indexes.

Sandbox: `code_sandbox/js-arrays/object-named-person.html`

```javascript
const person = {firstName:"John", lastName:"Doe", age:46};
```

<img alt="js-arrays example 11 source" src="./code_sandbox/snaps/js-arrays-11-code.png" />

<img alt="js-arrays example 11 result" src="./code_sandbox/snaps/js-arrays-11-result.png" />

- [x] **Outcome:** `firstName` is **"John"**.

<a id="js-arrays-example-12"></a>

### **Example 12: Array elements can be objects, functions, arrays**

- [x] No Tryit on the page — arrays are heterogeneous.
- [x] This demo stores a **function reference**, a **function**, and a **nested array**.

Sandbox: `code_sandbox/js-arrays/mixed-objects-functions.html`

```javascript
function myFunction() {
  return "hello";
}
const myCars = ["Saab", "Volvo"];
const myArray = [];
myArray[0] = Date.now;
myArray[1] = myFunction;
myArray[2] = myCars;
```

<img alt="js-arrays example 12 source" src="./code_sandbox/snaps/js-arrays-12-code.png" />

<img alt="js-arrays example 12 result" src="./code_sandbox/snaps/js-arrays-12-result.png" />

- [x] **Outcome:** `Date.now` is a **function**. `myArray[1]()` is **"hello"**. Nested cars are **["Saab","Volvo"]**.

<a id="js-arrays-example-13"></a>

### **Example 13: fruits.length**

- [x] `length` is the number of elements. It is **one more** than the highest index.

Sandbox: `code_sandbox/js-arrays/length.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let length = fruits.length;
```

<img alt="js-arrays example 13 source" src="./code_sandbox/snaps/js-arrays-13-code.png" />

<img alt="js-arrays example 13 result" src="./code_sandbox/snaps/js-arrays-13-result.png" />

- [x] **Outcome:** **4**.

<a id="js-arrays-example-14"></a>

### **Example 14: First element fruits[0]**

- [x] The first element is always index **0**.

Sandbox: `code_sandbox/js-arrays/first-element.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits[0];
```

<img alt="js-arrays example 14 source" src="./code_sandbox/snaps/js-arrays-14-code.png" />

<img alt="js-arrays example 14 result" src="./code_sandbox/snaps/js-arrays-14-result.png" />

- [x] **Outcome:** **Banana**.

<a id="js-arrays-example-15"></a>

### **Example 15: Last element fruits[fruits.length - 1]**

- [x] `length - 1` is the last valid index.

Sandbox: `code_sandbox/js-arrays/last-element.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits[fruits.length - 1];
```

<img alt="js-arrays example 15 source" src="./code_sandbox/snaps/js-arrays-15-code.png" />

<img alt="js-arrays example 15 result" src="./code_sandbox/snaps/js-arrays-15-result.png" />

- [x] **Outcome:** **Mango**.

<a id="js-arrays-example-16"></a>

### **Example 16: for loop over fruits**

- [x] A classic **`for`** from `0` to `length - 1` visits every index.

Sandbox: `code_sandbox/js-arrays/for-loop.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fLen = fruits.length;
let text = "";
for (let i = 0; i < fLen; i++) {
  text += fruits[i] + (i < fLen - 1 ? ", " : "");
}
```

<img alt="js-arrays example 16 source" src="./code_sandbox/snaps/js-arrays-16-code.png" />

<img alt="js-arrays example 16 result" src="./code_sandbox/snaps/js-arrays-16-result.png" />

- [x] **Outcome:** **Banana, Orange, Apple, Mango**.

<a id="js-arrays-example-17"></a>

### **Example 17: fruits.forEach(myFunction)**

- [x] `forEach` calls a function once per element.

Sandbox: `code_sandbox/js-arrays/foreach.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let text = "";
fruits.forEach(myFunction);
function myFunction(value) {
  text += value + " ";
}
```

<img alt="js-arrays example 17 source" src="./code_sandbox/snaps/js-arrays-17-code.png" />

<img alt="js-arrays example 17 result" src="./code_sandbox/snaps/js-arrays-17-result.png" />

- [x] **Outcome:** **Banana Orange Apple Mango** (trailing space from the callback).

<a id="js-arrays-example-18"></a>

### **Example 18: fruits.push("Lemon")**

- [x] `push` appends at the **end**.

Sandbox: `code_sandbox/js-arrays/push.html`

```javascript
const fruits = ["Banana", "Orange", "Apple"];
fruits.push("Lemon");
```

<img alt="js-arrays example 18 source" src="./code_sandbox/snaps/js-arrays-18-code.png" />

<img alt="js-arrays example 18 result" src="./code_sandbox/snaps/js-arrays-18-result.png" />

- [x] **Outcome:** **["Banana","Orange","Apple","Lemon"]**.

<a id="js-arrays-example-19"></a>

### **Example 19: fruits[fruits.length] = Lemon**

- [x] Writing at `fruits.length` also **appends**.

Sandbox: `code_sandbox/js-arrays/add-via-length.html`

```javascript
const fruits = ["Banana", "Orange", "Apple"];
fruits[fruits.length] = "Lemon";
```

<img alt="js-arrays example 19 source" src="./code_sandbox/snaps/js-arrays-19-code.png" />

<img alt="js-arrays example 19 result" src="./code_sandbox/snaps/js-arrays-19-result.png" />

- [x] **Outcome:** **["Banana","Orange","Apple","Lemon"]**.

<a id="js-arrays-example-20"></a>

### **Example 20: WARNING fruits[6] = Lemon creates holes**

- [x] A **high index** grows `length` and leaves **empty slots** in between.
- [x] `JSON.stringify` prints holes as **`null`**. `3 in fruits` is still **false**.

Sandbox: `code_sandbox/js-arrays/holes-warning.html`

```javascript
const fruits = ["Banana", "Orange", "Apple"];
fruits[6] = "Lemon";
```

<img alt="js-arrays example 20 source" src="./code_sandbox/snaps/js-arrays-20-code.png" />

<img alt="js-arrays example 20 result" src="./code_sandbox/snaps/js-arrays-20-result.png" />

- [x] **Outcome:** JSON **["Banana","Orange","Apple",null,null,null,"Lemon"]**. length **7**. `fruits[3]` is **undefined**. `3 in fruits` is **false**.

<a id="js-arrays-example-21"></a>

### **Example 21: Numbered indexes (not associative)**

- [x] JavaScript arrays always use **numbered** indexes.

Sandbox: `code_sandbox/js-arrays/numbered-indexes.html`

```javascript
const person = [];
person[0] = "John";
person[1] = "Doe";
person[2] = 46;
```

<img alt="js-arrays example 21 source" src="./code_sandbox/snaps/js-arrays-21-code.png" />

<img alt="js-arrays example 21 result" src="./code_sandbox/snaps/js-arrays-21-result.png" />

- [x] **Outcome:** length **3**. `person[0]` is **"John"**.

<a id="js-arrays-example-22"></a>

### **Example 22: WARNING named indexes become an object**

- [x] Named keys do **not** make an associative array. `length` stays **0**.
- [x] Some array methods then give **wrong** results.

Sandbox: `code_sandbox/js-arrays/named-indexes-warning.html`

```javascript
const person = [];
person["firstName"] = "John";
person["lastName"] = "Doe";
person["age"] = 46;
```

<img alt="js-arrays example 22 source" src="./code_sandbox/snaps/js-arrays-22-code.png" />

<img alt="js-arrays example 22 result" src="./code_sandbox/snaps/js-arrays-22-result.png" />

- [x] **Outcome:** length **0**. `person[0]` is **undefined**. `firstName` is **"John"**. It is still an Array object, but **not** a list of elements.

<a id="js-arrays-example-23"></a>

### **Example 23: new Array(40, 100, 1, 5, 25, 10) vs literal**

- [x] Several numeric arguments create an array **of those numbers** — same as `[...]`.

Sandbox: `code_sandbox/js-arrays/new-array-six-vs-literal.html`

```javascript
const a = new Array(40, 100, 1, 5, 25, 10);
const b = [40, 100, 1, 5, 25, 10];
```

<img alt="js-arrays example 23 source" src="./code_sandbox/snaps/js-arrays-23-code.png" />

<img alt="js-arrays example 23 result" src="./code_sandbox/snaps/js-arrays-23-result.png" />

- [x] **Outcome:** Both are **[40,100,1,5,25,10]**.

<a id="js-arrays-example-24"></a>

### **Example 24: typeof fruits is object**

- [x] `typeof` on an array is **`object`** because arrays are objects.

Sandbox: `code_sandbox/js-arrays/typeof-object.html`

```javascript
const fruits = ["Banana", "Orange", "Apple"];
let type = typeof fruits;
```

<img alt="js-arrays example 24 source" src="./code_sandbox/snaps/js-arrays-24-code.png" />

<img alt="js-arrays example 24 result" src="./code_sandbox/snaps/js-arrays-24-result.png" />

- [x] **Outcome:** **object**.

<a id="js-arrays-example-25"></a>

### **Example 25: Array.isArray(fruits)**

- [x] `Array.isArray` is the ES5 way to recognize an array.

Sandbox: `code_sandbox/js-arrays/isarray.html`

```javascript
const fruits = ["Banana", "Orange", "Apple"];
Array.isArray(fruits);
```

<img alt="js-arrays example 25 source" src="./code_sandbox/snaps/js-arrays-25-code.png" />

<img alt="js-arrays example 25 result" src="./code_sandbox/snaps/js-arrays-25-result.png" />

- [x] **Outcome:** **true**.

<a id="js-arrays-example-26"></a>

### **Example 26: fruits instanceof Array**

- [x] `instanceof Array` is **true** when the value was created as an array.

Sandbox: `code_sandbox/js-arrays/instanceof.html`

```javascript
const fruits = ["Banana", "Orange", "Apple"];
fruits instanceof Array;
```

<img alt="js-arrays example 26 source" src="./code_sandbox/snaps/js-arrays-26-code.png" />

<img alt="js-arrays example 26 result" src="./code_sandbox/snaps/js-arrays-26-result.png" />

- [x] **Outcome:** **true**.

<a id="js-arrays-example-27"></a>

### **Example 27: Nested arrays and objects**

- [x] Object values may be arrays; array values may be objects.
- [x] The page’s loop Tryit walks `cars` then each `models` list.

Sandbox: `code_sandbox/js-arrays/nested-arrays-objects.html`

```javascript
const myObj = {
  name: "John",
  age: 30,
  cars: [
    {name:"Ford", models:["Fiesta", "Focus", "Mustang"]},
    {name:"BMW", models:["320", "X3", "X5"]},
    {name:"Fiat", models:["500", "Panda"]}
  ]
};
let x = "";
for (let i in myObj.cars) {
  x += myObj.cars[i].name + ": ";
  for (let j in myObj.cars[i].models) {
    x += myObj.cars[i].models[j] + " ";
  }
}
```

<img alt="js-arrays example 27 source" src="./code_sandbox/snaps/js-arrays-27-code.png" />

<img alt="js-arrays example 27 result" src="./code_sandbox/snaps/js-arrays-27-result.png" />

- [x] **Outcome:** **Ford: Fiesta Focus Mustang BMW: 320 X3 X5 Fiat: 500 Panda** (trailing spaces).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-arrays/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you create an array?

<details>
<summary>Answer</summary>

- [x] An array literal: `const cars = ["Saab", "Volvo", "BMW"]`.
- [x] `new Array(...)` works but `[]` is preferred.

</details>

### Question 2: What is cars[0] for that list?

<details>
<summary>Answer</summary>

- [x] **"Saab"**. Indexes start at **0**.

</details>

### Question 3: Does const stop you changing cars[0]?

<details>
<summary>Answer</summary>

- [x] **No.** `cars[0] = "Opel"` becomes **["Opel","Volvo","BMW"]**.

</details>

### Question 4: What does fruits.toString() print?

<details>
<summary>Answer</summary>

- [x] **Banana,Orange,Apple,Mango** (commas, no spaces).

</details>

### Question 5: What is typeof fruits?

<details>
<summary>Answer</summary>

- [x] **object**. Arrays are objects.

</details>

### Question 6: How do you test for an array?

<details>
<summary>Answer</summary>

- [x] **Array.isArray(fruits)** is **true**.
- [x] `fruits instanceof Array` is also **true**.

</details>

### Question 7: What happens if you set fruits[6] = "Lemon" on a 3-item list?

<details>
<summary>Answer</summary>

- [x] length becomes **7**. Indexes 3–5 are **holes**.
- [x] JSON.stringify shows **null** in the holes; `3 in fruits` is **false**.

</details>

### Question 8: What if you use person["firstName"] on []?

<details>
<summary>Answer</summary>

- [x] length stays **0**. `person[0]` is **undefined**.
- [x] JavaScript does **not** have associative arrays.

</details>

### Question 9: Can an array hold a function?

<details>
<summary>Answer</summary>

- [x] **Yes.** This demo stores `Date.now`, a function, and a nested cars array.

</details>

### Question 10: How do you loop?

<details>
<summary>Answer</summary>

- [x] A `for` from 0 to length-1, or `forEach`.

</details>

### Question 11: How do you append?

<details>
<summary>Answer</summary>

- [x] `push("Lemon")` or `fruits[fruits.length] = "Lemon"`.

</details>

### Question 12: How do you recognize nested car models?

<details>
<summary>Answer</summary>

- [x] Objects inside `cars`, each with a `models` array. Loop both levels.

</details>


</details>

## Summary

Use [] and numbered indexes. length, push, and loops cover everyday list work. Trust Array.isArray, not typeof. Keep string keys on objects, not on arrays. Holes from high indexes or delete are real empty slots even when JSON prints null.

## References

- [JS Arrays (W3Schools)](https://www.w3schools.com/js/js_arrays.asp)
- [MDN: Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [MDN: Array.isArray](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray)

</details>
