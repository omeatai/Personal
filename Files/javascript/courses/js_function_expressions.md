# JS Function Expressions

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A function expression stores a function in a variable. The variable is how you call it. Expressions are usually anonymous (or optionally named) and end with a semicolon. They are not hoisted like declarations, which makes them useful as callbacks you pass around as values.

This section has **7** examples:

- [x] **Example 1:** const multiply = function(a, b) [View](#js-function-expressions-example-01)
- [x] **Example 2:** let z = multiply(4, 3) [View](#js-function-expressions-example-02)
- [x] **Example 3:** Semicolon after a function expression [View](#js-function-expressions-example-03)
- [x] **Example 4:** Callback: run(fn) [View](#js-function-expressions-example-04)
- [x] **Example 5:** sayHello expression called [View](#js-function-expressions-example-05)
- [x] **Example 6:** Function declaration is hoisted [View](#js-function-expressions-example-06)
- [x] **Example 7:** Function expression is not hoisted [View](#js-function-expressions-example-07)

## Detailed Explanation

- [x] A function expression is a **function stored in a variable**.
- [x] It is often **anonymous**; a **named** expression is allowed but you still call the variable.
- [x] Treat it as a **statement** — end with **`;`**.
- [x] **Declarations** are hoisted; **expressions** are not (TDZ / ReferenceError if called too early).

<a id="js-function-expressions-example-01"></a>

### **Example 1: const multiply = function(a, b)**

- [x] A **function expression** stores a function in a variable.
- [x] The function can be **anonymous** (no name after `function`) — the variable is the name you call.

Sandbox: `code_sandbox/js-function-expressions/const-multiply.html`

```javascript
const multiply = function (a, b) {
  return a * b;
};
```

![js-function-expressions example 1 source](../code_sandbox/snaps/js-function-expressions-01-code.png)

![js-function-expressions example 1 result](../code_sandbox/snaps/js-function-expressions-01-result.png)

- [x] **Outcome:** `typeof multiply` is **"function"**. `multiply(4, 3)` is **12**.

<a id="js-function-expressions-example-02"></a>

### **Example 2: let z = multiply(4, 3)**

- [x] After the expression is stored, the **variable** is used as the function.
- [x] Named form is also allowed: `const add = function add(a, b) { ... };` — still called via the variable.

Sandbox: `code_sandbox/js-function-expressions/let-z-multiply.html`

```javascript
const multiply = function (a, b) {
  return a * b;
};
let z = multiply(4, 3);
```

![js-function-expressions example 2 source](../code_sandbox/snaps/js-function-expressions-02-code.png)

![js-function-expressions example 2 result](../code_sandbox/snaps/js-function-expressions-02-result.png)

- [x] **Outcome:** z is **12**.

<a id="js-function-expressions-example-03"></a>

### **Example 3: Semicolon after a function expression**

- [x] A function **declaration** is not typically ended with `;`.
- [x] A function **expression** is a statement, so it **usually ends with a semicolon**.

Sandbox: `code_sandbox/js-function-expressions/semicolon-after.html`

```javascript
const add = function (a, b) {
  return a + b;
};
```

![js-function-expressions example 3 source](../code_sandbox/snaps/js-function-expressions-03-code.png)

![js-function-expressions example 3 result](../code_sandbox/snaps/js-function-expressions-03-result.png)

- [x] **Outcome:** add(2, 3) is **5**. Note the `;` after the closing `}`.

<a id="js-function-expressions-example-04"></a>

### **Example 4: Callback: run(fn)**

- [x] Because an expression is a **value**, you can pass it to another function.
- [x] `run(sayHello)` passes the function; `run` calls `fn()`.

Sandbox: `code_sandbox/js-function-expressions/callback-run.html`

```javascript
function run(fn) {
  return fn();
}
const sayHello = function () {
  return "Hello";
};
let result = run(sayHello);
```

![js-function-expressions example 4 source](../code_sandbox/snaps/js-function-expressions-04-code.png)

![js-function-expressions example 4 result](../code_sandbox/snaps/js-function-expressions-04-result.png)

- [x] **Outcome:** result is **"Hello"**.

<a id="js-function-expressions-example-05"></a>

### **Example 5: sayHello expression called**

- [x] Store the function in `sayHello`, then call **`sayHello()`**.
- [x] `sayHello` is the function; `sayHello()` is the result.

Sandbox: `code_sandbox/js-function-expressions/sayhello-expression.html`

```javascript
const sayHello = function () {
  return "Hello World";
};
sayHello();
```

![js-function-expressions example 5 source](../code_sandbox/snaps/js-function-expressions-05-code.png)

![js-function-expressions example 5 result](../code_sandbox/snaps/js-function-expressions-05-result.png)

- [x] **Outcome:** The call returns **"Hello World"**.

<a id="js-function-expressions-example-06"></a>

### **Example 6: Function declaration is hoisted**

- [x] A **function declaration** can be called **before** it appears in the code.
- [x] Declarations are **hoisted** to the top of their scope.

Sandbox: `code_sandbox/js-function-expressions/declaration-hoisted.html`

```javascript
let sum = add(2, 3);
function add(a, b) {
  return a + b;
}
```

![js-function-expressions example 6 source](../code_sandbox/snaps/js-function-expressions-06-code.png)

![js-function-expressions example 6 result](../code_sandbox/snaps/js-function-expressions-06-result.png)

- [x] **Outcome:** sum is **5**. The call before `function add` works.

<a id="js-function-expressions-example-07"></a>

### **Example 7: Function expression is not hoisted**

- [x] A `const` function expression lives in the **temporal dead zone** until that line runs.
- [x] Calling `add(2, 3)` **before** `const add = function...` throws **ReferenceError**.

Sandbox: `code_sandbox/js-function-expressions/expression-not-hoisted.html`

```javascript
let sum = add(2, 3); // error
const add = function (a, b) {
  return a + b;
};
```

![js-function-expressions example 7 source](../code_sandbox/snaps/js-function-expressions-07-code.png)

![js-function-expressions example 7 result](../code_sandbox/snaps/js-function-expressions-07-result.png)

- [x] **Outcome:** The early call throws **ReferenceError** (add is not initialized). After the `const` line, `add(2, 3)` would be **5**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-function-expressions/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `const multiply = function(a, b) { return a * b; }`?

<details>
<summary>Answer</summary>

- [x] A **function expression**.
- [x] `multiply(4, 3)` is **12**.

</details>

### Question 2: How do you call that function?

<details>
<summary>Answer</summary>

- [x] Use the **variable**: `multiply(4, 3)`.

</details>

### Question 3: Should the expression end with a semicolon?

<details>
<summary>Answer</summary>

- [x] **Yes.** It is a statement.

</details>

### Question 4: What is `run(sayHello)` if `run` does `return fn()`?

<details>
<summary>Answer</summary>

- [x] It **calls** the function you passed. Result **"Hello"**.

</details>

### Question 5: What is `sayHello()` for `const sayHello = function() { return "Hello World"; }`?

<details>
<summary>Answer</summary>

- [x] **"Hello World"**.

</details>

### Question 6: Can you call a declaration before its line?

<details>
<summary>Answer</summary>

- [x] **Yes.** `let sum = add(2, 3)` then `function add` yields **5**.

</details>

### Question 7: Can you call a `const` expression before its line?

<details>
<summary>Answer</summary>

- [x] **No.** **ReferenceError** (temporal dead zone).

</details>

### Question 8: What is an anonymous function?

<details>
<summary>Answer</summary>

- [x] A function **without a name** after `function`. The variable is the name you use.

</details>

### Question 9: When are expressions a good choice?

<details>
<summary>Answer</summary>

- [x] Callbacks, event handlers, and any time the function is a **value**.

</details>

### Question 10: What is `sayHello` vs `sayHello()`?

<details>
<summary>Answer</summary>

- [x] `sayHello` is the **function**. `sayHello()` is the **result**.

</details>

</details>

## Summary

Store a function in a variable, end the statement with a semicolon, and call the variable. Declarations hoist; expressions do not. Pass expressions as callbacks because they are values.

## References

- [JS Function Expressions (W3Schools)](https://www.w3schools.com/js/js_function_expressions.asp)
- [MDN: Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
- [MDN: Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
