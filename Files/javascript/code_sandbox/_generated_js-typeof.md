<details>
  <summary>JS typeof</summary>

## Introduction

typeof returns a type string: string, number, boolean, bigint, symbol, undefined, object, or function. It does not distinguish arrays, dates, maps, or sets — those are all object. typeof null is object (legacy). typeof of an undeclared name is undefined and does not throw. Array.isArray and instanceof (and constructor) tell object kinds apart. undefined and null compare equal with == and unequal with ===. void 0 is a reliable undefined. NaN’s typeof is number.

This section has **43** examples:

- [x] **Example 1:** typeof "John" [View](#js-typeof-example-01)
- [x] **Example 2:** typeof ("John" + "Doe") [View](#js-typeof-example-02)
- [x] **Example 3:** typeof 3.14 [View](#js-typeof-example-03)
- [x] **Example 4:** typeof 33 [View](#js-typeof-example-04)
- [x] **Example 5:** typeof (33 + 66) [View](#js-typeof-example-05)
- [x] **Example 6:** typeof true [View](#js-typeof-example-06)
- [x] **Example 7:** typeof false [View](#js-typeof-example-07)
- [x] **Example 8:** typeof 1234n [View](#js-typeof-example-08)
- [x] **Example 9:** typeof Symbol() [View](#js-typeof-example-09)
- [x] **Example 10:** typeof x [View](#js-typeof-example-10)
- [x] **Example 11:** typeof null — returns object (legacy) [View](#js-typeof-example-11)
- [x] **Example 12:** typeof NaN [View](#js-typeof-example-12)
- [x] **Example 13:** typeof {name:'John'} — object [View](#js-typeof-example-13)
- [x] **Example 14:** typeof [1, 2, 3, 4] [View](#js-typeof-example-14)
- [x] **Example 15:** typeof {} [View](#js-typeof-example-15)
- [x] **Example 16:** typeof [] [View](#js-typeof-example-16)
- [x] **Example 17:** typeof new Object() [View](#js-typeof-example-17)
- [x] **Example 18:** typeof new Array() [View](#js-typeof-example-18)
- [x] **Example 19:** typeof new Date() [View](#js-typeof-example-19)
- [x] **Example 20:** typeof new Set() [View](#js-typeof-example-20)
- [x] **Example 21:** typeof new Map() [View](#js-typeof-example-21)
- [x] **Example 22:** typeof function () {} [View](#js-typeof-example-22)
- [x] **Example 23:** Array.isArray(fruits) [View](#js-typeof-example-23)
- [x] **Example 24:** time instanceof Date [View](#js-typeof-example-24)
- [x] **Example 25:** fruits instanceof Array [View](#js-typeof-example-25)
- [x] **Example 26:** fruits instanceof Map [View](#js-typeof-example-26)
- [x] **Example 27:** fruits instanceof Set [View](#js-typeof-example-27)
- [x] **Example 28:** typeof car — undeclared variable [View](#js-typeof-example-28)
- [x] **Example 29:** let car; typeof car [View](#js-typeof-example-29)
- [x] **Example 30:** car = undefined after "Volvo" [View](#js-typeof-example-30)
- [x] **Example 31:** let car = ""; typeof car [View](#js-typeof-example-31)
- [x] **Example 32:** person = null — value null, typeof object [View](#js-typeof-example-32)
- [x] **Example 33:** person = undefined — value and type undefined [View](#js-typeof-example-33)
- [x] **Example 34:** undefined vs null — type and == / === [View](#js-typeof-example-34)
- [x] **Example 35:** {name:'John',age:34}.constructor [View](#js-typeof-example-35)
- [x] **Example 36:** [1,2,3,4].constructor [View](#js-typeof-example-36)
- [x] **Example 37:** new Date().constructor [View](#js-typeof-example-37)
- [x] **Example 38:** new Set().constructor [View](#js-typeof-example-38)
- [x] **Example 39:** new Map().constructor [View](#js-typeof-example-39)
- [x] **Example 40:** function () {}.constructor [View](#js-typeof-example-40)
- [x] **Example 41:** myArray.constructor === Array [View](#js-typeof-example-41)
- [x] **Example 42:** myDate.constructor === Date [View](#js-typeof-example-42)
- [x] **Example 43:** void 0 returns undefined [View](#js-typeof-example-43)

## Detailed Explanation

- [x] Primitives: **string / number / boolean / bigint / symbol / undefined**. **null → "object"** (bug).
- [x] Complex: **object** for `{}`, `[]`, Date, Map, Set. **function** for functions.
- [x] **Array.isArray** and **instanceof** (Date, Array, Map, Set) split object kinds. **constructor** also works.
- [x] `typeof` of an **undeclared** name is **"undefined"**. Reading the name is **ReferenceError**.
- [x] `null == undefined` **true**; `null === undefined` **false**. **`void 0`** is **undefined**.
- [x] **typeof NaN** is **"number"**.

<a id="js-typeof-example-01"></a>

### **Example 1: typeof "John"**

- [x] `typeof "John"` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-john.html`

```javascript
typeof "John";
```

<img alt="js-typeof example 1 source" src="./code_sandbox/snaps/js-typeof-01-code.png" />

<img alt="js-typeof example 1 result" src="./code_sandbox/snaps/js-typeof-01-result.png" />

- [x] **Outcome:** `typeof "John"` is **"string"**.

<a id="js-typeof-example-02"></a>

### **Example 2: typeof ("John" + "Doe")**

- [x] `typeof ("John" + "Doe")` is a **typeof** table row.
- [x] `"John"+"Doe"` is **"JohnDoe"**, still a string.

Sandbox: `code_sandbox/js-typeof/typeof-john-doe-concat.html`

```javascript
typeof ("John" + "Doe");
```

<img alt="js-typeof example 2 source" src="./code_sandbox/snaps/js-typeof-02-code.png" />

<img alt="js-typeof example 2 result" src="./code_sandbox/snaps/js-typeof-02-result.png" />

- [x] **Outcome:** `typeof ("John" + "Doe")` is **"string"**.

<a id="js-typeof-example-03"></a>

### **Example 3: typeof 3.14**

- [x] `typeof 3.14` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-3-14.html`

```javascript
typeof 3.14;
```

<img alt="js-typeof example 3 source" src="./code_sandbox/snaps/js-typeof-03-code.png" />

<img alt="js-typeof example 3 result" src="./code_sandbox/snaps/js-typeof-03-result.png" />

- [x] **Outcome:** `typeof 3.14` is **"number"**.

<a id="js-typeof-example-04"></a>

### **Example 4: typeof 33**

- [x] `typeof 33` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-33.html`

```javascript
typeof 33;
```

<img alt="js-typeof example 4 source" src="./code_sandbox/snaps/js-typeof-04-code.png" />

<img alt="js-typeof example 4 result" src="./code_sandbox/snaps/js-typeof-04-result.png" />

- [x] **Outcome:** `typeof 33` is **"number"**.

<a id="js-typeof-example-05"></a>

### **Example 5: typeof (33 + 66)**

- [x] `typeof (33 + 66)` is a **typeof** table row.
- [x] `33 + 66` is **99**, still a number.

Sandbox: `code_sandbox/js-typeof/typeof-33-plus-66.html`

```javascript
typeof (33 + 66);
```

<img alt="js-typeof example 5 source" src="./code_sandbox/snaps/js-typeof-05-code.png" />

<img alt="js-typeof example 5 result" src="./code_sandbox/snaps/js-typeof-05-result.png" />

- [x] **Outcome:** `typeof (33 + 66)` is **"number"**.

<a id="js-typeof-example-06"></a>

### **Example 6: typeof true**

- [x] `typeof true` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-true.html`

```javascript
typeof true;
```

<img alt="js-typeof example 6 source" src="./code_sandbox/snaps/js-typeof-06-code.png" />

<img alt="js-typeof example 6 result" src="./code_sandbox/snaps/js-typeof-06-result.png" />

- [x] **Outcome:** `typeof true` is **"boolean"**.

<a id="js-typeof-example-07"></a>

### **Example 7: typeof false**

- [x] `typeof false` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-false.html`

```javascript
typeof false;
```

<img alt="js-typeof example 7 source" src="./code_sandbox/snaps/js-typeof-07-code.png" />

<img alt="js-typeof example 7 result" src="./code_sandbox/snaps/js-typeof-07-result.png" />

- [x] **Outcome:** `typeof false` is **"boolean"**.

<a id="js-typeof-example-08"></a>

### **Example 8: typeof 1234n**

- [x] `typeof 1234n` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-bigint.html`

```javascript
typeof 1234n;
```

<img alt="js-typeof example 8 source" src="./code_sandbox/snaps/js-typeof-08-code.png" />

<img alt="js-typeof example 8 result" src="./code_sandbox/snaps/js-typeof-08-result.png" />

- [x] **Outcome:** `typeof 1234n` is **"bigint"**.

<a id="js-typeof-example-09"></a>

### **Example 9: typeof Symbol()**

- [x] `typeof Symbol()` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-symbol.html`

```javascript
typeof Symbol();
```

<img alt="js-typeof example 9 source" src="./code_sandbox/snaps/js-typeof-09-code.png" />

<img alt="js-typeof example 9 result" src="./code_sandbox/snaps/js-typeof-09-result.png" />

- [x] **Outcome:** `typeof Symbol()` is **"symbol"**.

<a id="js-typeof-example-10"></a>

### **Example 10: typeof x**

- [x] `typeof x` is a **typeof** table row.
- [x] `typeof` on an **undeclared** name is **"undefined"** — it does **not** throw.

Sandbox: `code_sandbox/js-typeof/typeof-undeclared-x.html`

```javascript
typeof x;
```

<img alt="js-typeof example 10 source" src="./code_sandbox/snaps/js-typeof-10-code.png" />

<img alt="js-typeof example 10 result" src="./code_sandbox/snaps/js-typeof-10-result.png" />

- [x] **Outcome:** `typeof x` is **"undefined"**.

<a id="js-typeof-example-11"></a>

### **Example 11: typeof null — returns object (legacy)**

- [x] `null` is a **primitive**, but `typeof null` is **"object"**.
- [x] This is a well-known **legacy bug**. Do not use typeof to test for null; use **`=== null`**.

Sandbox: `code_sandbox/js-typeof/typeof-null.html`

```javascript
typeof null;
```

<img alt="js-typeof example 11 source" src="./code_sandbox/snaps/js-typeof-11-code.png" />

<img alt="js-typeof example 11 result" src="./code_sandbox/snaps/js-typeof-11-result.png" />

- [x] **Outcome:** typeof null is **"object"**.

<a id="js-typeof-example-12"></a>

### **Example 12: typeof NaN**

- [x] `typeof NaN` is a **typeof** table row.
- [x] **NaN** is a number. The type of Not-a-Number is still **"number"**.

Sandbox: `code_sandbox/js-typeof/typeof-nan.html`

```javascript
typeof NaN;
```

<img alt="js-typeof example 12 source" src="./code_sandbox/snaps/js-typeof-12-code.png" />

<img alt="js-typeof example 12 result" src="./code_sandbox/snaps/js-typeof-12-result.png" />

- [x] **Outcome:** `typeof NaN` is **"number"**.

<a id="js-typeof-example-13"></a>

### **Example 13: typeof {name:'John'} — object**

- [x] A plain object’s typeof is **"object"**.

Sandbox: `code_sandbox/js-typeof/typeof-object-literal.html`

```javascript
typeof {name: 'John'};
```

<img alt="js-typeof example 13 source" src="./code_sandbox/snaps/js-typeof-13-code.png" />

<img alt="js-typeof example 13 result" src="./code_sandbox/snaps/js-typeof-13-result.png" />

- [x] **Outcome:** typeof {name:'John'} is **"object"**.

<a id="js-typeof-example-14"></a>

### **Example 14: typeof [1, 2, 3, 4]**

- [x] `typeof [1, 2, 3, 4]` is a **typeof** table row.
- [x] Arrays are objects. Use **Array.isArray** to tell them apart.

Sandbox: `code_sandbox/js-typeof/typeof-array-lit.html`

```javascript
typeof [1, 2, 3, 4];
```

<img alt="js-typeof example 14 source" src="./code_sandbox/snaps/js-typeof-14-code.png" />

<img alt="js-typeof example 14 result" src="./code_sandbox/snaps/js-typeof-14-result.png" />

- [x] **Outcome:** `typeof [1, 2, 3, 4]` is **"object"**.

<a id="js-typeof-example-15"></a>

### **Example 15: typeof {}**

- [x] `typeof {}` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-empty-object.html`

```javascript
typeof {};
```

<img alt="js-typeof example 15 source" src="./code_sandbox/snaps/js-typeof-15-code.png" />

<img alt="js-typeof example 15 result" src="./code_sandbox/snaps/js-typeof-15-result.png" />

- [x] **Outcome:** `typeof {}` is **"object"**.

<a id="js-typeof-example-16"></a>

### **Example 16: typeof []**

- [x] `typeof []` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-empty-array.html`

```javascript
typeof [];
```

<img alt="js-typeof example 16 source" src="./code_sandbox/snaps/js-typeof-16-code.png" />

<img alt="js-typeof example 16 result" src="./code_sandbox/snaps/js-typeof-16-result.png" />

- [x] **Outcome:** `typeof []` is **"object"**.

<a id="js-typeof-example-17"></a>

### **Example 17: typeof new Object()**

- [x] `typeof new Object()` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-new-object.html`

```javascript
typeof new Object();
```

<img alt="js-typeof example 17 source" src="./code_sandbox/snaps/js-typeof-17-code.png" />

<img alt="js-typeof example 17 result" src="./code_sandbox/snaps/js-typeof-17-result.png" />

- [x] **Outcome:** `typeof new Object()` is **"object"**.

<a id="js-typeof-example-18"></a>

### **Example 18: typeof new Array()**

- [x] `typeof new Array()` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-new-array.html`

```javascript
typeof new Array();
```

<img alt="js-typeof example 18 source" src="./code_sandbox/snaps/js-typeof-18-code.png" />

<img alt="js-typeof example 18 result" src="./code_sandbox/snaps/js-typeof-18-result.png" />

- [x] **Outcome:** `typeof new Array()` is **"object"**.

<a id="js-typeof-example-19"></a>

### **Example 19: typeof new Date()**

- [x] `typeof new Date()` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-new-date.html`

```javascript
typeof new Date();
```

<img alt="js-typeof example 19 source" src="./code_sandbox/snaps/js-typeof-19-code.png" />

<img alt="js-typeof example 19 result" src="./code_sandbox/snaps/js-typeof-19-result.png" />

- [x] **Outcome:** `typeof new Date()` is **"object"**.

<a id="js-typeof-example-20"></a>

### **Example 20: typeof new Set()**

- [x] `typeof new Set()` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-new-set.html`

```javascript
typeof new Set();
```

<img alt="js-typeof example 20 source" src="./code_sandbox/snaps/js-typeof-20-code.png" />

<img alt="js-typeof example 20 result" src="./code_sandbox/snaps/js-typeof-20-result.png" />

- [x] **Outcome:** `typeof new Set()` is **"object"**.

<a id="js-typeof-example-21"></a>

### **Example 21: typeof new Map()**

- [x] `typeof new Map()` is a **typeof** table row.

Sandbox: `code_sandbox/js-typeof/typeof-new-map.html`

```javascript
typeof new Map();
```

<img alt="js-typeof example 21 source" src="./code_sandbox/snaps/js-typeof-21-code.png" />

<img alt="js-typeof example 21 result" src="./code_sandbox/snaps/js-typeof-21-result.png" />

- [x] **Outcome:** `typeof new Map()` is **"object"**.

<a id="js-typeof-example-22"></a>

### **Example 22: typeof function () {}**

- [x] `typeof function () {}` is a **typeof** table row.
- [x] Functions are the **other** typeof result besides object for callables.

Sandbox: `code_sandbox/js-typeof/typeof-function.html`

```javascript
typeof function () {};
```

<img alt="js-typeof example 22 source" src="./code_sandbox/snaps/js-typeof-22-code.png" />

<img alt="js-typeof example 22 result" src="./code_sandbox/snaps/js-typeof-22-result.png" />

- [x] **Outcome:** `typeof function () {}` is **"function"**.

<a id="js-typeof-example-23"></a>

### **Example 23: Array.isArray(fruits)**

- [x] `typeof` cannot tell an array from a date. **`Array.isArray`** can.

Sandbox: `code_sandbox/js-typeof/array-isarray.html`

```javascript
const fruits = ["apples", "bananas", "oranges"];
Array.isArray(fruits);
```

<img alt="js-typeof example 23 source" src="./code_sandbox/snaps/js-typeof-23-code.png" />

<img alt="js-typeof example 23 result" src="./code_sandbox/snaps/js-typeof-23-result.png" />

- [x] **Outcome:** Array.isArray(fruits) is **true**. Array.isArray({a:1}) is **false**.

<a id="js-typeof-example-24"></a>

### **Example 24: time instanceof Date**

- [x] **`instanceof`** is **true** if the object was created from that constructor (prototype chain).

Sandbox: `code_sandbox/js-typeof/instanceof-date.html`

```javascript
const time = new Date();
(time instanceof Date);
```

<img alt="js-typeof example 24 source" src="./code_sandbox/snaps/js-typeof-24-code.png" />

<img alt="js-typeof example 24 result" src="./code_sandbox/snaps/js-typeof-24-result.png" />

- [x] **Outcome:** `time instanceof Date` is **true**. `time instanceof Array` is **false**.

<a id="js-typeof-example-25"></a>

### **Example 25: fruits instanceof Array**

- [x] Array instances are `instanceof Array`.

Sandbox: `code_sandbox/js-typeof/instanceof-array.html`

```javascript
const fruits = ["apples", "bananas", "oranges"];
(fruits instanceof Array);
```

<img alt="js-typeof example 25 source" src="./code_sandbox/snaps/js-typeof-25-code.png" />

<img alt="js-typeof example 25 result" src="./code_sandbox/snaps/js-typeof-25-result.png" />

- [x] **Outcome:** `fruits instanceof Array` is **true**.

<a id="js-typeof-example-26"></a>

### **Example 26: fruits instanceof Map**

- [x] `new Map(...)` instances are `instanceof Map`.

Sandbox: `code_sandbox/js-typeof/instanceof-map.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
(fruits instanceof Map);
```

<img alt="js-typeof example 26 source" src="./code_sandbox/snaps/js-typeof-26-code.png" />

<img alt="js-typeof example 26 result" src="./code_sandbox/snaps/js-typeof-26-result.png" />

- [x] **Outcome:** `instanceof Map` is **true**. `instanceof Array` is **false**.

<a id="js-typeof-example-27"></a>

### **Example 27: fruits instanceof Set**

- [x] `new Set(...)` instances are `instanceof Set`.

Sandbox: `code_sandbox/js-typeof/instanceof-set.html`

```javascript
const fruits = new Set(["apples", "bananas", "oranges"]);
(fruits instanceof Set);
```

<img alt="js-typeof example 27 source" src="./code_sandbox/snaps/js-typeof-27-code.png" />

<img alt="js-typeof example 27 result" src="./code_sandbox/snaps/js-typeof-27-result.png" />

- [x] **Outcome:** `fruits instanceof Set` is **true**.

<a id="js-typeof-example-28"></a>

### **Example 28: typeof car — undeclared variable**

- [x] `typeof car` when **car was never declared** is **"undefined"**, not a ReferenceError.

Sandbox: `code_sandbox/js-typeof/typeof-undeclared-car.html`

```javascript
typeof car;
```

<img alt="js-typeof example 28 source" src="./code_sandbox/snaps/js-typeof-28-code.png" />

<img alt="js-typeof example 28 result" src="./code_sandbox/snaps/js-typeof-28-result.png" />

- [x] **Outcome:** typeof car is **"undefined"**.

<a id="js-typeof-example-29"></a>

### **Example 29: let car; typeof car**

- [x] A declared variable with no value: value **undefined**, typeof **"undefined"**.

Sandbox: `code_sandbox/js-typeof/typeof-declared-no-value.html`

```javascript
let car;
typeof car;
```

<img alt="js-typeof example 29 source" src="./code_sandbox/snaps/js-typeof-29-code.png" />

<img alt="js-typeof example 29 result" src="./code_sandbox/snaps/js-typeof-29-result.png" />

- [x] **Outcome:** car is **undefined**. typeof is **"undefined"**.

<a id="js-typeof-example-30"></a>

### **Example 30: car = undefined after "Volvo"**

- [x] Assigning **`undefined`** empties the variable. Type becomes **undefined**.

Sandbox: `code_sandbox/js-typeof/emptied-undefined.html`

```javascript
let car = "Volvo";
car = undefined;
```

<img alt="js-typeof example 30 source" src="./code_sandbox/snaps/js-typeof-30-code.png" />

<img alt="js-typeof example 30 result" src="./code_sandbox/snaps/js-typeof-30-result.png" />

- [x] **Outcome:** car is **undefined**. typeof is **"undefined"**.

<a id="js-typeof-example-31"></a>

### **Example 31: let car = ""; typeof car**

- [x] An empty string is **not** undefined. typeof is **"string"**.

Sandbox: `code_sandbox/js-typeof/empty-string-typeof.html`

```javascript
let car = "";
typeof car;
```

<img alt="js-typeof example 31 source" src="./code_sandbox/snaps/js-typeof-31-code.png" />

<img alt="js-typeof example 31 result" src="./code_sandbox/snaps/js-typeof-31-result.png" />

- [x] **Outcome:** value is **""**. typeof is **"string"**.

<a id="js-typeof-example-32"></a>

### **Example 32: person = null — value null, typeof object**

- [x] Setting an object variable to **`null`** empties it. `typeof` stays **"object"** (legacy).

Sandbox: `code_sandbox/js-typeof/object-set-null.html`

```javascript
let person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
person = null;
```

<img alt="js-typeof example 32 source" src="./code_sandbox/snaps/js-typeof-32-code.png" />

<img alt="js-typeof example 32 result" src="./code_sandbox/snaps/js-typeof-32-result.png" />

- [x] **Outcome:** person is **null**. typeof is **"object"**.

<a id="js-typeof-example-33"></a>

### **Example 33: person = undefined — value and type undefined**

- [x] Setting the same variable to **`undefined`** makes **both** value and type undefined.

Sandbox: `code_sandbox/js-typeof/object-set-undefined.html`

```javascript
let person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
person = undefined;
```

<img alt="js-typeof example 33 source" src="./code_sandbox/snaps/js-typeof-33-code.png" />

<img alt="js-typeof example 33 result" src="./code_sandbox/snaps/js-typeof-33-result.png" />

- [x] **Outcome:** person is **undefined**. typeof is **"undefined"**.

<a id="js-typeof-example-34"></a>

### **Example 34: undefined vs null — type and == / ===**

- [x] `undefined` and `null` are **equal in value** under **`==`**, **different types** under **`===`**.

Sandbox: `code_sandbox/js-typeof/null-vs-undefined.html`

```javascript
typeof undefined;
typeof null;
null === undefined;
null == undefined;
```

<img alt="js-typeof example 34 source" src="./code_sandbox/snaps/js-typeof-34-code.png" />

<img alt="js-typeof example 34 result" src="./code_sandbox/snaps/js-typeof-34-result.png" />

- [x] **Outcome:** typeof undefined is **"undefined"**. typeof null is **"object"**. `===` is **false**. `==` is **true**.

<a id="js-typeof-example-35"></a>

### **Example 35: {name:'John',age:34}.constructor**

- [x] **`constructor`** is the function that created the value’s prototype.

Sandbox: `code_sandbox/js-typeof/constructor-object.html`

```javascript
let c = {name: 'John', age: 34}.constructor;
```

<img alt="js-typeof example 35 source" src="./code_sandbox/snaps/js-typeof-35-code.png" />

<img alt="js-typeof example 35 result" src="./code_sandbox/snaps/js-typeof-35-result.png" />

- [x] **Outcome:** String(c) is **"function Object() { [native code] }"**. `c === Object` is **true**.

<a id="js-typeof-example-36"></a>

### **Example 36: [1,2,3,4].constructor**

- [x] Array instances have **`Array`** as their constructor function.

Sandbox: `code_sandbox/js-typeof/constructor-array.html`

```javascript
let c = [1, 2, 3, 4].constructor;
```

<img alt="js-typeof example 36 source" src="./code_sandbox/snaps/js-typeof-36-code.png" />

<img alt="js-typeof example 36 result" src="./code_sandbox/snaps/js-typeof-36-result.png" />

- [x] **Outcome:** String(c) is **"function Array() { [native code] }"**. `c === Array` is **true**.

<a id="js-typeof-example-37"></a>

### **Example 37: new Date().constructor**

- [x] Date instances have **`Date`** as constructor.

Sandbox: `code_sandbox/js-typeof/constructor-date.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
let c = d.constructor;
```

<img alt="js-typeof example 37 source" src="./code_sandbox/snaps/js-typeof-37-code.png" />

<img alt="js-typeof example 37 result" src="./code_sandbox/snaps/js-typeof-37-result.png" />

- [x] **Outcome:** String(c) is **"function Date() { [native code] }"**. `c === Date` is **true**.

<a id="js-typeof-example-38"></a>

### **Example 38: new Set().constructor**

- [x] Set instances have **`Set`** as constructor.

Sandbox: `code_sandbox/js-typeof/constructor-set.html`

```javascript
let c = new Set().constructor;
```

<img alt="js-typeof example 38 source" src="./code_sandbox/snaps/js-typeof-38-code.png" />

<img alt="js-typeof example 38 result" src="./code_sandbox/snaps/js-typeof-38-result.png" />

- [x] **Outcome:** String(c) is **"function Set() { [native code] }"**. `c === Set` is **true**.

<a id="js-typeof-example-39"></a>

### **Example 39: new Map().constructor**

- [x] Map instances have **`Map`** as constructor.

Sandbox: `code_sandbox/js-typeof/constructor-map.html`

```javascript
let c = new Map().constructor;
```

<img alt="js-typeof example 39 source" src="./code_sandbox/snaps/js-typeof-39-code.png" />

<img alt="js-typeof example 39 result" src="./code_sandbox/snaps/js-typeof-39-result.png" />

- [x] **Outcome:** String(c) is **"function Map() { [native code] }"**. `c === Map` is **true**.

<a id="js-typeof-example-40"></a>

### **Example 40: function () {}.constructor**

- [x] Functions have **`Function`** as constructor.

Sandbox: `code_sandbox/js-typeof/constructor-function.html`

```javascript
let c = function () {}.constructor;
```

<img alt="js-typeof example 40 source" src="./code_sandbox/snaps/js-typeof-40-code.png" />

<img alt="js-typeof example 40 result" src="./code_sandbox/snaps/js-typeof-40-result.png" />

- [x] **Outcome:** String(c) is **"function Function() { [native code] }"**. `c === Function` is **true**.

<a id="js-typeof-example-41"></a>

### **Example 41: myArray.constructor === Array**

- [x] You can recognize an array with **`constructor === Array`** (or prefer **Array.isArray**).

Sandbox: `code_sandbox/js-typeof/constructor-eq-array.html`

```javascript
const myArray = [1, 2, 3, 4];
(myArray.constructor === Array);
```

<img alt="js-typeof example 41 source" src="./code_sandbox/snaps/js-typeof-41-code.png" />

<img alt="js-typeof example 41 result" src="./code_sandbox/snaps/js-typeof-41-result.png" />

- [x] **Outcome:** `myArray.constructor === Array` is **true**.

<a id="js-typeof-example-42"></a>

### **Example 42: myDate.constructor === Date**

- [x] You can recognize a Date with **`constructor === Date`**.

Sandbox: `code_sandbox/js-typeof/constructor-eq-date.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
const myDate = d;
(myDate.constructor === Date);
```

<img alt="js-typeof example 42 source" src="./code_sandbox/snaps/js-typeof-42-code.png" />

<img alt="js-typeof example 42 result" src="./code_sandbox/snaps/js-typeof-42-result.png" />

- [x] **Outcome:** `myDate.constructor === Date` is **true**.

<a id="js-typeof-example-43"></a>

### **Example 43: void 0 returns undefined**

- [x] **`void`** evaluates an expression and returns **`undefined`**.
- [x] Often written **`void(0)`** / **`void 0`**. The page also uses `javascript:void(0)` on a link.

Sandbox: `code_sandbox/js-typeof/void-operator.html`

```javascript
void 0;
void (0);
```

<img alt="js-typeof example 43 source" src="./code_sandbox/snaps/js-typeof-43-code.png" />

<img alt="js-typeof example 43 result" src="./code_sandbox/snaps/js-typeof-43-result.png" />

- [x] **Outcome:** `void 0` is **undefined**. typeof is **"undefined"**. `void (0)` is the same.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-typeof/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `typeof "John"`?

<details>
<summary>Answer</summary>

- [x] **"string"**.

</details>

### Question 2: What is `typeof 3.14`?

<details>
<summary>Answer</summary>

- [x] **"number"**.

</details>

### Question 3: What is `typeof 1234n`?

<details>
<summary>Answer</summary>

- [x] **"bigint"**.

</details>

### Question 4: What is `typeof Symbol()`?

<details>
<summary>Answer</summary>

- [x] **"symbol"**.

</details>

### Question 5: What is `typeof null`?

<details>
<summary>Answer</summary>

- [x] **"object"** — legacy. Test with `=== null`.

</details>

### Question 6: What is `typeof NaN`?

<details>
<summary>Answer</summary>

- [x] **"number"**.

</details>

### Question 7: What is `typeof function () {}`?

<details>
<summary>Answer</summary>

- [x] **"function"**.

</details>

### Question 8: What is `typeof [1,2,3,4]`?

<details>
<summary>Answer</summary>

- [x] **"object"**. Use **Array.isArray** — **true** for that array.

</details>

### Question 9: Does `typeof car` throw if car was never declared?

<details>
<summary>Answer</summary>

- [x] **No.** It is **"undefined"**.

</details>

### Question 10: person = null vs person = undefined — types?

<details>
<summary>Answer</summary>

- [x] null → typeof **"object"**. undefined → typeof **"undefined"**.

</details>

### Question 11: `null === undefined` and `null == undefined`?

<details>
<summary>Answer</summary>

- [x] **false** and **true**.

</details>

### Question 12: What is `{name:'John',age:34}.constructor === Object`?

<details>
<summary>Answer</summary>

- [x] **true**. String(constructor) is **function Object() { [native code] }**.

</details>

### Question 13: What is `void 0`?

<details>
<summary>Answer</summary>

- [x] **undefined**. typeof is **"undefined"**.

</details>

### Question 14: Can typeof tell a Date from an Array?

<details>
<summary>Answer</summary>

- [x] **No.** Both **"object"**. Use **instanceof** / **constructor** / **Array.isArray**.

</details>


</details>

## Summary

Trust typeof for primitives and functions. For objects, follow up with Array.isArray, instanceof, or constructor. Remember the null bug and that NaN is a number. void 0 is undefined.

## References

- [JS typeof (W3Schools)](https://www.w3schools.com/js/js_typeof.asp)
- [MDN: typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
- [MDN: instanceof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
- [MDN: void operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void)

</details>
