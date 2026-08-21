# JS Best Practices

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Avoid global variables, avoid new wrappers, avoid ==, avoid eval(). Declare locals with let/const (strict mode forbids undeclared assigns). Declare at the top and initialize. var redeclare keeps the value; let/const redeclare is a SyntaxError. const stops rebinding objects/arrays (not mutation). Prefer literals over new String/Number/Boolean/Object/Array/RegExp/Function. Watch + concatenation vs - coercion. Use ===. Default parameters. End switch with default. Never treat primitives as objects. eval is a security footgun.

This section has **22** examples:

- [x] **Example 1:** Avoid global variables — they can be overwritten [View](#js-best-practices-example-01)
- [x] **Example 2:** Always declare local variables (var / let / const) [View](#js-best-practices-example-02)
- [x] **Example 3:** Put all declarations at the top of the script or function [View](#js-best-practices-example-03)
- [x] **Example 4:** Initialize variables when you declare them [View](#js-best-practices-example-04)
- [x] **Example 5:** var carName = "Volvo"; var carName; keeps the value (not recommended) [View](#js-best-practices-example-05)
- [x] **Example 6:** let carName twice — SyntaxError [View](#js-best-practices-example-06)
- [x] **Example 7:** const carName twice — SyntaxError [View](#js-best-practices-example-07)
- [x] **Example 8:** let car = {...}; car = "Fiat" changes the type [View](#js-best-practices-example-08)
- [x] **Example 9:** const car = {...}; car = "Fiat" is not possible [View](#js-best-practices-example-09)
- [x] **Example 10:** let cars = [...]; cars = 3 changes array to number [View](#js-best-practices-example-10)
- [x] **Example 11:** const cars = [...]; cars = 3 is not possible [View](#js-best-practices-example-11)
- [x] **Example 12:** Don't use new Object() — use literals [View](#js-best-practices-example-12)
- [x] **Example 13:** let x = "Hello"; x = 5 changes typeof to number [View](#js-best-practices-example-13)
- [x] **Example 14:** 5 + 7 is 12; 5 + "7" is "57"; 5 - "7" is -2 [View](#js-best-practices-example-14)
- [x] **Example 15:** "Hello" - "Dolly" returns NaN [View](#js-best-practices-example-15)
- [x] **Example 16:** Use === — 0 == "" is true; 0 === "" is false [View](#js-best-practices-example-16)
- [x] **Example 17:** Default a missing argument: if (y === undefined) y = 0 [View](#js-best-practices-example-17)
- [x] **Example 18:** ES2015 default parameters: function (a = 1, b = 1) [View](#js-best-practices-example-18)
- [x] **Example 19:** Always end switch with default [View](#js-best-practices-example-19)
- [x] **Example 20:** "John" === new String("John") is false [View](#js-best-practices-example-20)
- [x] **Example 21:** new String("John") == new String("John") is false [View](#js-best-practices-example-21)
- [x] **Example 22:** Avoid eval() — it runs text as code [View](#js-best-practices-example-22)

## Detailed Explanation

- [x] **No implied globals.** Strict mode throws **ReferenceError** on undeclared assigns.
- [x] **`const`** for objects/arrays you must not **replace**. **`let`** still allows type changes.
- [x] Literals, not **`new String()`** etc. **`===`**, not **`==`**. **No `eval`**.
- [x] Default parameters (or `y === undefined`). **`default:`** on every **switch**.

<a id="js-best-practices-example-01"></a>

### **Example 1: Avoid global variables — they can be overwritten**

- [x] Minimize **globals** (all types, objects, functions). Another script can **overwrite** them.
- [x] Prefer **local** variables and **closures**.

Sandbox: `code_sandbox/js-best-practices/avoid-globals.html`

```javascript
var leaked = "global";
function hide() {
  let local = "local";
  return local;
}
```

<img alt="js-best-practices example 1 source" src="../code_sandbox/snaps/js-best-practices-01-code.png" />

<img alt="js-best-practices example 1 result" src="../code_sandbox/snaps/js-best-practices-01-result.png" />

- [x] **Outcome:** **leaked** is visible as a global. **local** is **not** visible outside `hide` (**ReferenceError**).

<a id="js-best-practices-example-02"></a>

### **Example 2: Always declare local variables (var / let / const)**

- [x] Undeclared assignments become **globals** (sloppy mode).
- [x] **Strict mode** does **not** allow undeclared variables (**ReferenceError**).

Sandbox: `code_sandbox/js-best-practices/declare-locals.html`

```javascript
function sloppy() {
  implicit = 1;
}
function strictish() {
  "use strict";
  implicit2 = 1;
}
```

<img alt="js-best-practices example 2 source" src="../code_sandbox/snaps/js-best-practices-02-code.png" />

<img alt="js-best-practices example 2 result" src="../code_sandbox/snaps/js-best-practices-02-result.png" />

- [x] **Outcome:** Sloppy `implicit = 1` creates a **global**. Strict assignment to `implicit2` is **ReferenceError: implicit2 is not defined**.

<a id="js-best-practices-example-03"></a>

### **Example 3: Put all declarations at the top of the script or function**

- [x] Cleaner code, one place to look, fewer implied globals, fewer accidental re-declarations.
- [x] Also declare **loop** variables in the `for` head: `for (let i = 0; ...)`.

Sandbox: `code_sandbox/js-best-practices/declarations-on-top.html`

```javascript
let firstName, lastName, price, discount, fullPrice;
firstName = "John";
lastName = "Doe";
price = 19.90;
discount = 0.10;
fullPrice = price - discount;
```

<img alt="js-best-practices example 3 source" src="../code_sandbox/snaps/js-best-practices-03-code.png" />

<img alt="js-best-practices example 3 result" src="../code_sandbox/snaps/js-best-practices-03-result.png" />

- [x] **Outcome:** **fullPrice** is **19.8**. Names were declared **first**, assigned **later**.

<a id="js-best-practices-example-04"></a>

### **Example 4: Initialize variables when you declare them**

- [x] Avoid **undefined** placeholders. Initialization documents the **intended type**: `""`, `0`, `[]`, `{}`.

Sandbox: `code_sandbox/js-best-practices/initialize-variables.html`

```javascript
let firstName = "";
let lastName = "";
let price = 0;
let discount = 0;
let fullPrice = 0;
const myArray = [];
const myObject = {};
```

<img alt="js-best-practices example 4 source" src="../code_sandbox/snaps/js-best-practices-04-code.png" />

<img alt="js-best-practices example 4 result" src="../code_sandbox/snaps/js-best-practices-04-result.png" />

- [x] **Outcome:** **firstName** is **`""`**. **price** is **0**. **myArray** is **[]**. **myObject** is **{}**. None are **undefined**.

<a id="js-best-practices-example-05"></a>

### **Example 5: var carName = "Volvo"; var carName; keeps the value (not recommended)**

- [x] Re-declaring **`var`** does **not** reset the value.
- [x] Still **not recommended**. Prefer **`let` / `const`** (you **cannot** re-declare those).

Sandbox: `code_sandbox/js-best-practices/var-redeclare.html`

```javascript
var carName = "Volvo";
var carName;
```

<img alt="js-best-practices example 5 source" src="../code_sandbox/snaps/js-best-practices-05-code.png" />

<img alt="js-best-practices example 5 result" src="../code_sandbox/snaps/js-best-practices-05-result.png" />

- [x] **Outcome:** **carName** is still **Volvo** after the second `var carName;`.

<a id="js-best-practices-example-06"></a>

### **Example 6: let carName twice — SyntaxError**

- [x] You **cannot** re-declare **`let`** in the same scope.

Sandbox: `code_sandbox/js-best-practices/let-redeclare.html`

```javascript
let carName = "Volvo";
let carName;
```

<img alt="js-best-practices example 6 source" src="../code_sandbox/snaps/js-best-practices-06-code.png" />

<img alt="js-best-practices example 6 result" src="../code_sandbox/snaps/js-best-practices-06-result.png" />

- [x] **Outcome:** **SyntaxError: Identifier 'carName' has already been declared** (via `new Function`; a raw script would not parse).

<a id="js-best-practices-example-07"></a>

### **Example 7: const carName twice — SyntaxError**

- [x] You **cannot** re-declare **`const`** in the same scope either.

Sandbox: `code_sandbox/js-best-practices/const-redeclare.html`

```javascript
const carName = "Volvo";
const carName;
```

<img alt="js-best-practices example 7 source" src="../code_sandbox/snaps/js-best-practices-07-code.png" />

<img alt="js-best-practices example 7 result" src="../code_sandbox/snaps/js-best-practices-07-result.png" />

- [x] **Outcome:** **SyntaxError: Identifier 'carName' has already been declared**.

<a id="js-best-practices-example-08"></a>

### **Example 8: let car = {...}; car = "Fiat" changes the type**

- [x] `let` **allows** replacing an object with a string. That is a **type change** bug.

Sandbox: `code_sandbox/js-best-practices/let-object-reassign.html`

```javascript
let car = {type:"Fiat", model:"500", color:"white"};
car = "Fiat";  // Changes object to string
```

<img alt="js-best-practices example 8 source" src="../code_sandbox/snaps/js-best-practices-08-code.png" />

<img alt="js-best-practices example 8 result" src="../code_sandbox/snaps/js-best-practices-08-result.png" />

- [x] **Outcome:** After assign, **car** is **"Fiat"** (`typeof` **string**), not an object.

<a id="js-best-practices-example-09"></a>

### **Example 9: const car = {...}; car = "Fiat" is not possible**

- [x] **`const`** prevents **rebinding**. You may still **mutate** properties (`car.color = ...`).
- [x] `car = "Fiat"` is **TypeError: Assignment to constant variable**.

Sandbox: `code_sandbox/js-best-practices/const-object-reassign.html`

```javascript
const car = {type:"Fiat", model:"500", color:"white"};
car = "Fiat";  // Not possible
```

<img alt="js-best-practices example 9 source" src="../code_sandbox/snaps/js-best-practices-09-code.png" />

<img alt="js-best-practices example 9 result" src="../code_sandbox/snaps/js-best-practices-09-result.png" />

- [x] **Outcome:** **TypeError: Assignment to constant variable**. The object is unchanged.

<a id="js-best-practices-example-10"></a>

### **Example 10: let cars = [...]; cars = 3 changes array to number**

- [x] Same type-change hole as objects: `let` arrays can be replaced with a number.

Sandbox: `code_sandbox/js-best-practices/let-array-reassign.html`

```javascript
let cars = ["Saab", "Volvo", "BMW"];
cars = 3;
```

<img alt="js-best-practices example 10 source" src="../code_sandbox/snaps/js-best-practices-10-code.png" />

<img alt="js-best-practices example 10 result" src="../code_sandbox/snaps/js-best-practices-10-result.png" />

- [x] **Outcome:** **cars** is **3**. **Array.isArray** is **false**.

<a id="js-best-practices-example-11"></a>

### **Example 11: const cars = [...]; cars = 3 is not possible**

- [x] **`const`** blocks replacing the array. **`.push` still works** (mutating contents).

Sandbox: `code_sandbox/js-best-practices/const-array-reassign.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
cars = 3;  // Not possible
```

<img alt="js-best-practices example 11 source" src="../code_sandbox/snaps/js-best-practices-11-code.png" />

<img alt="js-best-practices example 11 result" src="../code_sandbox/snaps/js-best-practices-11-result.png" />

- [x] **Outcome:** **TypeError: Assignment to constant variable**. `cars[0]` is still **Saab**.

<a id="js-best-practices-example-12"></a>

### **Example 12: Don't use new Object() — use literals**

- [x] Use **`""`** not `new String()`, **`0`** not `new Number()`, **`false`** not `new Boolean()`.
- [x] Use **`{}`** not `new Object()`, **`[]`** not `new Array()`, **`/()/`** not `new RegExp()`, **`function (){}`** not `new Function()`.

Sandbox: `code_sandbox/js-best-practices/no-new-object.html`

```javascript
let x1 = "";
let x2 = 0;
let x3 = false;
const x4 = {};
const x5 = [];
const x6 = /()/;
const x7 = function(){};
```

<img alt="js-best-practices example 12 source" src="../code_sandbox/snaps/js-best-practices-12-code.png" />

<img alt="js-best-practices example 12 result" src="../code_sandbox/snaps/js-best-practices-12-result.png" />

- [x] **Outcome:** typeof: **string**, **number**, **boolean**, **object**, **object** (array), **object** (regexp), **function**.

<a id="js-best-practices-example-13"></a>

### **Example 13: let x = "Hello"; x = 5 changes typeof to number**

- [x] JavaScript is **loosely typed**. A variable can **change** data type.

Sandbox: `code_sandbox/js-best-practices/type-change.html`

```javascript
let x = "Hello";
x = 5;
```

<img alt="js-best-practices example 13 source" src="../code_sandbox/snaps/js-best-practices-13-code.png" />

<img alt="js-best-practices example 13 result" src="../code_sandbox/snaps/js-best-practices-13-result.png" />

- [x] **Outcome:** First **typeof** is **string**. After `x = 5`, **typeof** is **number**.

<a id="js-best-practices-example-14"></a>

### **Example 14: 5 + 7 is 12; 5 + "7" is "57"; 5 - "7" is -2**

- [x] `+` with a string **concatenates**. `-` **coerces to number**.
- [x] `5 - "x"` is **NaN** (`typeof` still **number**).

Sandbox: `code_sandbox/js-best-practices/plus-vs-minus-coercion.html`

```javascript
let a = 5 + 7;
let b = 5 + "7";
let c = "5" + 7;
let d = 5 - 7;
let e = 5 - "7";
let f = "5" - 7;
let g = 5 - "x";
```

<img alt="js-best-practices example 14 source" src="../code_sandbox/snaps/js-best-practices-14-code.png" />

<img alt="js-best-practices example 14 result" src="../code_sandbox/snaps/js-best-practices-14-result.png" />

- [x] **Outcome:** **12** number, **"57"** string, **"57"** string, **-2** number, **-2**, **-2**, **NaN**.

<a id="js-best-practices-example-15"></a>

### **Example 15: "Hello" - "Dolly" returns NaN**

- [x] Subtracting two strings does **not throw**. It returns **NaN**.

Sandbox: `code_sandbox/js-best-practices/hello-minus-dolly.html`

```javascript
"Hello" - "Dolly"
```

<img alt="js-best-practices example 15 source" src="../code_sandbox/snaps/js-best-practices-15-code.png" />

<img alt="js-best-practices example 15 result" src="../code_sandbox/snaps/js-best-practices-15-result.png" />

- [x] **Outcome:** **NaN**. `Number.isNaN` is **true**.

<a id="js-best-practices-example-16"></a>

### **Example 16: Use === — 0 == "" is true; 0 === "" is false**

- [x] **`==`** converts types first. **`===`** compares **value and type**.
- [x] `0 == ""` **true**, `1 == "1"` **true**, `1 == true` **true**. All **false** with **`===`**.

Sandbox: `code_sandbox/js-best-practices/triple-equals.html`

```javascript
0 == "";
1 == "1";
1 == true;
0 === "";
1 === "1";
1 === true;
```

<img alt="js-best-practices example 16 source" src="../code_sandbox/snaps/js-best-practices-16-code.png" />

<img alt="js-best-practices example 16 result" src="../code_sandbox/snaps/js-best-practices-16-result.png" />

- [x] **Outcome:** Loose: **true, true, true**. Strict: **false, false, false**.

<a id="js-best-practices-example-17"></a>

### **Example 17: Default a missing argument: if (y === undefined) y = 0**

- [x] Missing arguments are **`undefined`** and can break math.
- [x] Old pattern: `if (y === undefined) { y = 0; }`.

Sandbox: `code_sandbox/js-best-practices/parameter-defaults-if.html`

```javascript
function myFunction(x, y) {
  if (y === undefined) {
    y = 0;
  }
  return x + y;
}
```

<img alt="js-best-practices example 17 source" src="../code_sandbox/snaps/js-best-practices-17-code.png" />

<img alt="js-best-practices example 17 result" src="../code_sandbox/snaps/js-best-practices-17-result.png" />

- [x] **Outcome:** **myFunction(5)** is **5** (`y` defaulted to **0**). **myFunction(5, 2)** is **7**.

<a id="js-best-practices-example-18"></a>

### **Example 18: ES2015 default parameters: function (a = 1, b = 1)**

- [x] ES2015: defaults in the **signature**. Cleaner than the `undefined` check.

Sandbox: `code_sandbox/js-best-practices/default-parameters.html`

```javascript
function add(a = 1, b = 1) {
  return a + b;
}
```

<img alt="js-best-practices example 18 source" src="../code_sandbox/snaps/js-best-practices-18-code.png" />

<img alt="js-best-practices example 18 result" src="../code_sandbox/snaps/js-best-practices-18-result.png" />

- [x] **Outcome:** **add()** is **2**. **add(5)** is **6**. **add(5, 3)** is **8**.

<a id="js-best-practices-example-19"></a>

### **Example 19: Always end switch with default**

- [x] Even if you think every case is covered, add **`default`**.
- [x] The Tryit maps `getDay()` 0–6, then **Unknown**.

Sandbox: `code_sandbox/js-best-practices/switch-default.html`

```javascript
switch (new Date().getDay()) {
  case 0: day = "Sunday"; break;
  case 1: day = "Monday"; break;
  case 2: day = "Tuesday"; break;
  case 3: day = "Wednesday"; break;
  case 4: day = "Thursday"; break;
  case 5: day = "Friday"; break;
  case 6: day = "Saturday"; break;
  default: day = "Unknown";
}
```

<img alt="js-best-practices example 19 source" src="../code_sandbox/snaps/js-best-practices-19-code.png" />

<img alt="js-best-practices example 19 result" src="../code_sandbox/snaps/js-best-practices-19-result.png" />

- [x] **Outcome:** A real weekday name for 0–6. Force **`switch (99)`** and **default** is **Unknown**.

<a id="js-best-practices-example-20"></a>

### **Example 20: "John" === new String("John") is false**

- [x] Treat numbers, strings, booleans as **primitives**, not objects.
- [x] `new String` is an **object**. Primitive **`===`** object is **false**. Also **slower**.

Sandbox: `code_sandbox/js-best-practices/string-vs-new-string.html`

```javascript
let x = "John";
let y = new String("John");
(x === y)
```

<img alt="js-best-practices example 20 source" src="../code_sandbox/snaps/js-best-practices-20-code.png" />

<img alt="js-best-practices example 20 result" src="../code_sandbox/snaps/js-best-practices-20-result.png" />

- [x] **Outcome:** **x === y** is **false**. **typeof x** is **string**. **typeof y** is **object**.

<a id="js-best-practices-example-21"></a>

### **Example 21: new String("John") == new String("John") is false**

- [x] Even **worse**: two String **objects** are never `==` equal (different references).

Sandbox: `code_sandbox/js-best-practices/new-string-equals-new-string.html`

```javascript
let x = new String("John");
let y = new String("John");
(x == y)
```

<img alt="js-best-practices example 21 source" src="../code_sandbox/snaps/js-best-practices-21-code.png" />

<img alt="js-best-practices example 21 result" src="../code_sandbox/snaps/js-best-practices-21-result.png" />

- [x] **Outcome:** **x == y** is **false**. **x.valueOf() == y.valueOf()** is **true**.

<a id="js-best-practices-example-22"></a>

### **Example 22: Avoid eval() — it runs text as code**

- [x] **`eval()`** runs a string as code. Almost never needed.
- [x] It is a **security** problem (arbitrary code) and is slower.

Sandbox: `code_sandbox/js-best-practices/avoid-eval.html`

```javascript
let x = eval("2 + 2");
```

<img alt="js-best-practices example 22 source" src="../code_sandbox/snaps/js-best-practices-22-code.png" />

<img alt="js-best-practices example 22 result" src="../code_sandbox/snaps/js-best-practices-22-result.png" />

- [x] **Outcome:** **eval("2 + 2")** is **4** — it **works**, and you still **should not** use it. `2 + 2` in source is the same result without eval.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-best-practices/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is an undeclared `implicit = 1` in sloppy mode?

<details>
<summary>Answer</summary>

- [x] A **global**.

</details>

### Question 2: Same assign in strict mode?

<details>
<summary>Answer</summary>

- [x] **ReferenceError: implicit2 is not defined**.

</details>

### Question 3: `var carName = "Volvo"; var carName;`?

<details>
<summary>Answer</summary>

- [x] Still **Volvo**. Do not rely on this.

</details>

### Question 4: `let carName` twice?

<details>
<summary>Answer</summary>

- [x] **SyntaxError: Identifier 'carName' has already been declared**.

</details>

### Question 5: `const car = {}; car = "Fiat"`?

<details>
<summary>Answer</summary>

- [x] **TypeError: Assignment to constant variable**.

</details>

### Question 6: `5 + "7"` vs `5 - "7"`?

<details>
<summary>Answer</summary>

- [x] **`"57"`** (string) vs **-2** (number).

</details>

### Question 7: `0 == ""` vs `0 === ""`?

<details>
<summary>Answer</summary>

- [x] **true** vs **false**.

</details>

### Question 8: `add()` with `function add(a=1,b=1)`?

<details>
<summary>Answer</summary>

- [x] **2**.

</details>

### Question 9: `"John" === new String("John")`?

<details>
<summary>Answer</summary>

- [x] **false** (primitive vs object).

</details>

### Question 10: `new String("John") == new String("John")`?

<details>
<summary>Answer</summary>

- [x] **false** (two objects).

</details>

### Question 11: Should you use `eval("2+2")`?

<details>
<summary>Answer</summary>

- [x] **No.** It works (**4**) but is **unsafe** and unnecessary.

</details>

### Question 12: `switch(99)` with a default?

<details>
<summary>Answer</summary>

- [x] **Unknown** in this demo.

</details>


</details>

## Summary

Declare locals, initialize, prefer const, literals, ===, default parameters, and switch default. Do not leak globals, wrap primitives with new, or call eval.

## References

- [JS Best Practices (W3Schools)](https://www.w3schools.com/js/js_best_practices.asp)
- [MDN: Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
- [MDN: Equality comparisons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness)
- [MDN: eval()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
