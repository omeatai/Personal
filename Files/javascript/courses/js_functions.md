# JS Functions

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

This study-path page is the map for JavaScript functions: what they are, how you call them, how parameters and return values work, then expressions, arrows, and a quiz. Each beginner step below is a small runnable demo of that idea. Advanced topics (callbacks, this, call/apply/bind, IIFE, closures) belong on later pages and are only named in the concepts list.

This section has **8** examples:

- [x] **Example 1:** What are Functions? [View](#js-functions-example-01)
- [x] **Example 2:** Calling Functions [View](#js-functions-example-02)
- [x] **Example 3:** Function Parameters [View](#js-functions-example-03)
- [x] **Example 4:** Function Return Values [View](#js-functions-example-04)
- [x] **Example 5:** Function Arguments [View](#js-functions-example-05)
- [x] **Example 6:** Function Expressions [View](#js-functions-example-06)
- [x] **Example 7:** Arrow Functions [View](#js-functions-example-07)
- [x] **Example 8:** Function Quiz teaser [View](#js-functions-example-08)

## Detailed Explanation

- [x] A function is a **reusable code block**. It runs when it is **called** with `()`.
- [x] **Parameters** are names in the definition; **arguments** are values in the call; **return** sends a value back.
- [x] A **function expression** stores a function in a variable; an **arrow** is a short expression syntax.
- [x] The **Advanced Functions** path (definitions, callbacks, `this`, `call`/`apply`/`bind`, IIFE, closures) is a later track — do not duplicate those chapters here.

<a id="js-functions-example-01"></a>

### **Example 1: What are Functions?**

- [x] A **function** is a reusable block of code for a particular task.
- [x] Nothing inside the function runs until you **call** (invoke) it.

Sandbox: `code_sandbox/js-functions/what-are-functions.html`

```javascript
function sayHello() {
  return "Hello World";
}
let text = sayHello();
```

![js-functions example 1 source](../code_sandbox/snaps/js-functions-01-code.png)

![js-functions example 1 result](../code_sandbox/snaps/js-functions-01-result.png)

- [x] **Outcome:** text is **"Hello World"** after the call.

<a id="js-functions-example-02"></a>

### **Example 2: Calling Functions**

- [x] Call a function by writing its name plus **parentheses**: `sayHello()`.
- [x] The `()` means **execute now**.

Sandbox: `code_sandbox/js-functions/calling-functions.html`

```javascript
function sayHello() {
  return "Hello World";
}
sayHello();
```

![js-functions example 2 source](../code_sandbox/snaps/js-functions-02-code.png)

![js-functions example 2 result](../code_sandbox/snaps/js-functions-02-result.png)

- [x] **Outcome:** The call returns **Hello World**.

<a id="js-functions-example-03"></a>

### **Example 3: Function Parameters**

- [x] **Parameters** are the names listed in the function definition.
- [x] `multiply(a, b)` receives two inputs and returns their product.

Sandbox: `code_sandbox/js-functions/function-parameters.html`

```javascript
function multiply(a, b) {
  return a * b;
}
let result = multiply(4, 5);
```

![js-functions example 3 source](../code_sandbox/snaps/js-functions-03-code.png)

![js-functions example 3 result](../code_sandbox/snaps/js-functions-03-result.png)

- [x] **Outcome:** result is **20**.

<a id="js-functions-example-04"></a>

### **Example 4: Function Return Values**

- [x] `return` sends a value **back** to the caller.
- [x] Store that value in a variable to use it later.

Sandbox: `code_sandbox/js-functions/function-return-values.html`

```javascript
function sayHello() {
  return "Hello World";
}
let message = sayHello();
```

![js-functions example 4 source](../code_sandbox/snaps/js-functions-04-code.png)

![js-functions example 4 result](../code_sandbox/snaps/js-functions-04-result.png)

- [x] **Outcome:** message is **"Hello World"**.

<a id="js-functions-example-05"></a>

### **Example 5: Function Arguments**

- [x] **Parameters** are names (`a`, `b`). **Arguments** are the values passed in (`4`, `5`).
- [x] Argument `4` is assigned to `a`; `5` is assigned to `b`.

Sandbox: `code_sandbox/js-functions/function-arguments.html`

```javascript
function multiply(a, b) {
  return a * b;
}
let result = multiply(4, 5);
```

![js-functions example 5 source](../code_sandbox/snaps/js-functions-05-code.png)

![js-functions example 5 result](../code_sandbox/snaps/js-functions-05-result.png)

- [x] **Outcome:** **a, b** are parameters; **4, 5** are arguments. result is **20**.

<a id="js-functions-example-06"></a>

### **Example 6: Function Expressions**

- [x] A **function expression** stores a function in a variable.
- [x] Call it with the **variable name** plus `()`.

Sandbox: `code_sandbox/js-functions/function-expressions.html`

```javascript
const multiply = function (a, b) {
  return a * b;
};
let z = multiply(4, 3);
```

![js-functions example 6 source](../code_sandbox/snaps/js-functions-06-code.png)

![js-functions example 6 result](../code_sandbox/snaps/js-functions-06-result.png)

- [x] **Outcome:** z is **12**. `multiply` is a **function**.

<a id="js-functions-example-07"></a>

### **Example 7: Arrow Functions**

- [x] Arrow functions are a **short syntax** for function expressions.
- [x] You can skip `function`, `return`, and `{}` when the body is one expression.

Sandbox: `code_sandbox/js-functions/arrow-functions.html`

```javascript
const multiply = (a, b) => a * b;
let z = multiply(4, 5);
```

![js-functions example 7 source](../code_sandbox/snaps/js-functions-07-code.png)

![js-functions example 7 result](../code_sandbox/snaps/js-functions-07-result.png)

- [x] **Outcome:** z is **20**.

<a id="js-functions-example-08"></a>

### **Example 8: Function Quiz teaser**

- [x] The quiz reuses the same `sayHello` example.
- [x] `let text = sayHello()` stores the **returned string**, not the function name.

Sandbox: `code_sandbox/js-functions/function-quiz-teaser.html`

```javascript
function sayHello() {
  return "Hello World";
}
let text = sayHello();
```

![js-functions example 8 source](../code_sandbox/snaps/js-functions-08-code.png)

![js-functions example 8 result](../code_sandbox/snaps/js-functions-08-result.png)

- [x] **Outcome:** text is **"Hello World"** (quiz question 1, answer **B**).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-functions/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a function?

<details>
<summary>Answer</summary>

- [x] A **reusable block** of code for a particular task.
- [x] It runs when it is **called** (invoked).

</details>

### Question 2: How do you call `sayHello`?

<details>
<summary>Answer</summary>

- [x] Write **`sayHello()`** — the parentheses mean execute now.

</details>

### Question 3: What does `function multiply(a, b)` use `a` and `b` for?

<details>
<summary>Answer</summary>

- [x] They are **parameters** — names that receive incoming values.

</details>

### Question 4: What does `return` do?

<details>
<summary>Answer</summary>

- [x] It sends a value **back** to the caller and **stops** the function.

</details>

### Question 5: What is the difference between parameters and arguments?

<details>
<summary>Answer</summary>

- [x] **Parameters** are names (`a`, `b`).
- [x] **Arguments** are values (`4`, `5`).

</details>

### Question 6: What is `const multiply = function(a, b) { return a * b; }`?

<details>
<summary>Answer</summary>

- [x] A **function expression** stored in `multiply`.
- [x] Call it with `multiply(4, 3)`.

</details>

### Question 7: What is `(a, b) => a * b`?

<details>
<summary>Answer</summary>

- [x] An **arrow function** — short syntax for a function expression.
- [x] `multiply(4, 5)` is **20**.

</details>

### Question 8: What is `let text = sayHello()` if `sayHello` returns `"Hello World"`?

<details>
<summary>Answer</summary>

- [x] **"Hello World"** — the quiz answer is **B**.

</details>

### Question 9: Does defining a function run its body?

<details>
<summary>Answer</summary>

- [x] **No.** Definition only creates the function. A call runs it.

</details>

### Question 10: Why is there an Advanced Functions path?

<details>
<summary>Answer</summary>

- [x] For later topics: callbacks, `this`, `call`/`apply`/`bind`, IIFE, closures.
- [x] This page only introduces the beginner/intermediate steps.

</details>

</details>

## Summary

Functions are reusable blocks you call with parentheses. Parameters receive arguments, return sends a value back, expressions store functions in variables, and arrows shorten that syntax. The quiz reuses these same examples. Advanced function features are a separate path.

## References

- [JS Functions (W3Schools)](https://www.w3schools.com/js/js_functions.asp)
- [MDN: Functions guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [MDN: Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
