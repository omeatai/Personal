# JS Variables

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Variables are **containers** (labels) for data. You can declare them in **four** ways: automatically, **`var`**, **`let`**, and **`const`**. Modern code uses **`const`** by default and **`let`** when the value must change. Avoid **`var`** and undeclared variables.

This section has **4** examples:

- [x] **Example 1:** Declaring variables (`let` / `const` / `undefined`) [View](#js-variables-example-01)
- [x] **Example 2:** Identifiers (`_` and `$` count as letters) [View](#js-variables-example-02)
- [x] **Example 3:** Data types & multiple declarations [View](#js-variables-example-03)
- [x] **Example 4:** Assignment & arithmetic (`=` and `+`) [View](#js-variables-example-04)

## Detailed Explanation

- [x] **Variables are containers for data** — labels you attach to values so you can reuse them by name.
- [x] **Four ways to declare:** automatically (undeclared, not recommended), **`var`** (pre‑2015, avoid), **`let`**, and **`const`**.
- [x] **Modern rule of thumb:** use **`const`** by default; switch to **`let`** only when the value must change; avoid **`var`** and undeclared variables.
- [x] **Identifiers (names)** can be short (`x`) or descriptive (`carName`); they may contain letters, digits, `_`, and `$`, but **cannot start with a digit** (that is how JS tells identifiers from numbers). They are **case sensitive** and cannot be reserved words.

<a id="js-variables-example-01"></a>

### **Example 1: Declaring variables (`let` / `const` / `undefined`)**

- [x] `let` and `const` both **create** (declare) a variable; you can compute from other variables (`let z = x + y;`).
- [x] `const` can declare several names in **one statement** with commas (`const a = 5, b = 6, c = a + b;`).
- [x] Declaring **without** a value (`let carName;`) leaves it as **`undefined`** until you assign with **`=`** later (`carName = "Volvo";`).

Sandbox: `code_sandbox/js-variables/declare.html`

```javascript
let x = 5;
let y = 6;
let z = x + y; // declared with let
const a = 5,
  b = 6,
  c = a + b; // declared with const

let carName; // declared, no value yet -> undefined
const before = carName;
carName = "Volvo"; // assign later with =
```

![js-variables example 1 source](../code_sandbox/snaps/js-variables-01-code.png)

![js-variables example 1 result](../code_sandbox/snaps/js-variables-01-result.png)

- [x] **Outcome:** `x + y` is **11** and `a + b` is **11**; `carName` reads **undefined** before assignment and **Volvo** after — proof that a bare `let` starts life as `undefined`.

<a id="js-variables-example-02"></a>

### **Example 2: Identifiers (`_` and `$` count as letters)**

- [x] **`_`** is treated as a letter, so `_lastName`, `_x`, `_100` are valid names; a common convention is to start "private" names with an underscore.
- [x] **`$`** is also treated as a letter, so `$`, `$$$`, `$myMoney` are valid; libraries (e.g. jQuery) often use `$` as an alias for a main function.
- [x] Digits are allowed **after** the first character (`_100`), but a name may **never begin** with a digit.

Sandbox: `code_sandbox/js-variables/identifiers.html`

```javascript
let _lastName = "Johnson";
let _x = 2;
let _100 = 5;
let $ = "Hello World";
let $$$ = 2;
let $myMoney = 5;
```

![js-variables example 2 source](../code_sandbox/snaps/js-variables-02-code.png)

![js-variables example 2 result](../code_sandbox/snaps/js-variables-02-result.png)

- [x] **Outcome:** every name resolves normally — `_lastName = Johnson`, `$ = Hello World`, `$myMoney = 5` — showing `_` and `$` are ordinary letters to JavaScript.

<a id="js-variables-example-03"></a>

### **Example 3: Data types & multiple declarations**

- [x] **Numbers** are written **without quotes** (`const pi = 3.14;`); **strings** are wrapped in **quotes** (`let person = "John Doe";`).
- [x] You can declare **many variables in one statement**, separating them with commas — and the statement can **span several lines**.
- [x] Choosing `const` vs `let` is about whether the value should change, not about its type.

Sandbox: `code_sandbox/js-variables/datatypes.html`

```javascript
const pi = 3.14; // number: no quotes
let person = "John Doe"; // string: in quotes
let answer = "Yes I am!";

// one statement, many variables (commas, can span lines)
let p2 = "John Doe",
  carName = "Volvo",
  price = 200;
```

![js-variables example 3 source](../code_sandbox/snaps/js-variables-03-code.png)

![js-variables example 3 result](../code_sandbox/snaps/js-variables-03-result.png)

- [x] **Outcome:** `pi = 3.14`, `person = "John Doe"`, and the comma‑separated statement declares all three of `p2`, `carName`, `price` at once (`John Doe`, `Volvo`, `200`).

<a id="js-variables-example-04"></a>

### **Example 4: Assignment & arithmetic (`=` and `+`)**

- [x] The **`=`** operator **assigns**, it is not algebra: `x = x + 5` reads the old `x` (5), adds 5, and stores **10** back. The equal‑to comparison operator is **`==`**, not a single `=`.
- [x] With numbers, **`+`** adds (`5 + 2 + 3` → **10**); with strings, **`+`** concatenates (`"John" + " " + "Doe"` → **John Doe**).
- [x] Mixing types depends on **order**: `"5" + 2 + 3` starts with a string → **`523`**; but `2 + 3 + "5"` adds the numbers first, then concatenates → **`55`**.

Sandbox: `code_sandbox/js-variables/arithmetic.html`

```javascript
let x = 5;
x = x + 5; // = assigns; x becomes 10 (not algebra equality)

let sum = 5 + 2 + 3; // numbers add -> 10
let name = "John" + " " + "Doe"; // strings concatenate

let mix1 = "5" + 2 + 3; // string first -> "523"
let mix2 = 2 + 3 + "5"; // numbers add first, then concatenate -> "55"
```

![js-variables example 4 source](../code_sandbox/snaps/js-variables-04-code.png)

![js-variables example 4 result](../code_sandbox/snaps/js-variables-04-result.png)

- [x] **Outcome:** `x` becomes **10**, `sum` is **10**, `name` is **John Doe**, `"5" + 2 + 3` is **523**, and `2 + 3 + "5"` is **55** — the classic left‑to‑right `+` quirk.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-variables/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a JavaScript variable?

<details>
<summary>Answer</summary>

- [x] A **container** (label) for storing data.

</details>

### Question 2: How should you declare variables in modern JavaScript?

<details>
<summary>Answer</summary>

- [x] Use **`const`** if the value should not change.
- [x] Use **`let`** only if you cannot use `const`.
- [x] Avoid **`var`** and undeclared variables.

</details>

### Question 3: What is a variable’s value right after `let carName;`?

<details>
<summary>Answer</summary>

- [x] **`undefined`** until you assign with **`=`**.

</details>

### Question 4: Can identifiers start with a number?

<details>
<summary>Answer</summary>

- [x] **No.** That is how JavaScript distinguishes identifiers from numbers.

</details>

### Question 5: What does `"5" + 2 + 3` evaluate to?

<details>
<summary>Answer</summary>

- [x] **`523`** (string concatenation).
- [x] A number in quotes makes the rest treated as strings.

</details>

### Question 6: When were `let` and `const` added?

<details>
<summary>Answer</summary>

- [x] **2015** (ES6).
- [x] Before that, code used **`var`**.

</details>

### Question 7: What are the four ways to declare a variable?

<details>
<summary>Answer</summary>

- [x] **Automatically** (undeclared, not recommended), **`var`**, **`let`**, and **`const`**.

</details>

### Question 8: Can you declare several variables in one statement?

<details>
<summary>Answer</summary>

- [x] **Yes** — separate them with **commas**: `let p = "John Doe", carName = "Volvo", price = 200;`.
- [x] The statement can span **multiple lines**.

</details>

### Question 9: What is the difference between `=` and `==`?

<details>
<summary>Answer</summary>

- [x] **`=`** is the **assignment** operator (store a value).
- [x] **`==`** is the **equal‑to** comparison operator.

</details>

### Question 10: What does `2 + 3 + "5"` evaluate to, and why?

<details>
<summary>Answer</summary>

- [x] **`55`** (a string).
- [x] JavaScript works **left to right**: `2 + 3` adds to **5**, then `5 + "5"` concatenates to **`"55"`**.

</details>

### Question 11: How do numbers and strings look different in code?

<details>
<summary>Answer</summary>

- [x] **Numbers** are written **without quotes** (`3.14`).
- [x] **Strings** are written **inside quotes** (`"John Doe"`).

</details>

</details>

## Summary

Variables hold data. Prefer **`const`**, then **`let`**; avoid **`var`** and automatic declaration. Names cannot start with a digit; `_` and `$` count as letters. Assign with **`=`** (compare with **`==`**). With `+`, numbers add and strings concatenate, and order matters: `"5" + 2 + 3` → **523** but `2 + 3 + "5"` → **55**.

## References

- [JS Variables (W3Schools)](https://www.w3schools.com/js/js_variables.asp)
- [MDN: let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
- [MDN: const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
- [MDN: var](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
