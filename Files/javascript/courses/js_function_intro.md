# JS Function Intro

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Functions are reusable code blocks. This page shows the shape of a function, why you call it, how to pass parameters, how local variables stay inside the function, and how a call can be used as a value in a larger expression.

This section has **6** examples:

- [x] **Example 1:** Function defined but not called [View](#js-function-intro-example-01)
- [x] **Example 2:** Call sayHello() and store the message [View](#js-function-intro-example-02)
- [x] **Example 3:** multiply(a, b) [View](#js-function-intro-example-03)
- [x] **Example 4:** add called twice (sum1, sum2) [View](#js-function-intro-example-04)
- [x] **Example 5:** Local variable carName [View](#js-function-intro-example-05)
- [x] **Example 6:** toCelsius used inline as a variable value [View](#js-function-intro-example-06)

## Detailed Explanation

- [x] Write `function name(params) { ... }` — name, parentheses, then a **block**.
- [x] Nothing runs until you **call** `name()`. Returned values can be stored or used inline.
- [x] **Local** variables exist only inside the function; they throw **ReferenceError** outside.
- [x] Call the same function **many times** with different inputs for different results.

<a id="js-function-intro-example-01"></a>

### **Example 1: Function defined but not called**

- [x] A function definition is **not** an executable statement by itself.
- [x] The function **exists**, but its body does not run until you call it.

Sandbox: `code_sandbox/js-function-intro/defined-not-called.html`

```javascript
function sayHello() {
  return "Hello World";
}
```

![js-function-intro example 1 source](../code_sandbox/snaps/js-function-intro-01-code.png)

![js-function-intro example 1 result](../code_sandbox/snaps/js-function-intro-01-result.png)

- [x] **Outcome:** `typeof sayHello` is **"function"**. Nothing printed Hello World because it was never called.

<a id="js-function-intro-example-02"></a>

### **Example 2: Call sayHello() and store the message**

- [x] `sayHello()` runs the body and **returns** a string.
- [x] `()` means execute now. Store the result in a variable to use it.

Sandbox: `code_sandbox/js-function-intro/call-and-store.html`

```javascript
function sayHello() {
  return "Hello World";
}
let message = sayHello();
```

![js-function-intro example 2 source](../code_sandbox/snaps/js-function-intro-02-code.png)

![js-function-intro example 2 result](../code_sandbox/snaps/js-function-intro-02-result.png)

- [x] **Outcome:** message is **"Hello World"**.

<a id="js-function-intro-example-03"></a>

### **Example 3: multiply(a, b)**

- [x] Parameters `a` and `b` sit in the parentheses of the **definition**.
- [x] Function declarations usually **do not** end with a semicolon.

Sandbox: `code_sandbox/js-function-intro/multiply.html`

```javascript
function multiply(a, b) {
  return a * b;
}
let result = multiply(4, 5);
```

![js-function-intro example 3 source](../code_sandbox/snaps/js-function-intro-03-code.png)

![js-function-intro example 3 result](../code_sandbox/snaps/js-function-intro-03-result.png)

- [x] **Outcome:** result is **20**.

<a id="js-function-intro-example-04"></a>

### **Example 4: add called twice (sum1, sum2)**

- [x] The same function can run **many times** with different inputs.
- [x] Returned values can be stored in different variables.

Sandbox: `code_sandbox/js-function-intro/add-twice.html`

```javascript
function add(a, b) {
  return a + b;
}
let sum1 = add(5, 5);
let sum2 = add(50, 50);
```

![js-function-intro example 4 source](../code_sandbox/snaps/js-function-intro-04-code.png)

![js-function-intro example 4 result](../code_sandbox/snaps/js-function-intro-04-result.png)

- [x] **Outcome:** sum1 is **10**; sum2 is **100**.

<a id="js-function-intro-example-05"></a>

### **Example 5: Local variable carName**

- [x] Variables declared **inside** a function are **local** to that function.
- [x] Outside the function, `carName` throws **ReferenceError**.

Sandbox: `code_sandbox/js-function-intro/local-carname.html`

```javascript
// code here can NOT use carName
function myFunction() {
  let carName = "Volvo";
  return carName; // code here CAN use carName
}
// code here can NOT use carName
```

![js-function-intro example 5 source](../code_sandbox/snaps/js-function-intro-05-code.png)

![js-function-intro example 5 result](../code_sandbox/snaps/js-function-intro-05-result.png)

- [x] **Outcome:** Inside the function, carName is **Volvo**. Outside, reading it throws **ReferenceError**.

<a id="js-function-intro-example-06"></a>

### **Example 6: toCelsius used inline as a variable value**

- [x] You can store `toCelsius(77)` in `x`, then build a string.
- [x] Or use the **call itself** as a value in the expression.

Sandbox: `code_sandbox/js-function-intro/tocelsius-inline.html`

```javascript
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}
let x = toCelsius(77);
let text1 = "The temperature is " + x + " Celsius";
let text2 = "The temperature is " + toCelsius(77) + " Celsius";
```

![js-function-intro example 6 source](../code_sandbox/snaps/js-function-intro-06-code.png)

![js-function-intro example 6 result](../code_sandbox/snaps/js-function-intro-06-result.png)

- [x] **Outcome:** Both strings are **"The temperature is 25 Celsius"**. 77°F is **25**°C.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-function-intro/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does `function sayHello() { return "Hello World"; }` print anything by itself?

<details>
<summary>Answer</summary>

- [x] **No.** `typeof sayHello` is **function**, but the body has not run.

</details>

### Question 2: What is `let message = sayHello()`?

<details>
<summary>Answer</summary>

- [x] **"Hello World"** stored in `message`.
- [x] `()` means execute now.

</details>

### Question 3: What is `multiply(4, 5)` if the function returns `a * b`?

<details>
<summary>Answer</summary>

- [x] **20**.

</details>

### Question 4: What are `sum1` and `sum2` after `add(5, 5)` and `add(50, 50)`?

<details>
<summary>Answer</summary>

- [x] **10** and **100**.
- [x] The same function ran twice.

</details>

### Question 5: Can code outside `myFunction` read `let carName` declared inside it?

<details>
<summary>Answer</summary>

- [x] **No.** That is a **ReferenceError**.
- [x] Local variables are created when the function starts and deleted when it finishes.

</details>

### Question 6: What is `toCelsius(77)`?

<details>
<summary>Answer</summary>

- [x] **25**.
- [x] You can store it in `x` or drop the call into a string.

</details>

### Question 7: Should a function declaration end with a semicolon?

<details>
<summary>Answer</summary>

- [x] Usually **no**. Semicolons separate executable statements, not declarations.

</details>

### Question 8: Why use functions?

<details>
<summary>Answer</summary>

- [x] **Reuse** code, **organize** it, and make it easier to **read** and maintain.

</details>

### Question 9: What is the usual input/output pattern?

<details>
<summary>Answer</summary>

- [x] Parameters in, work in the body, **return** a value out.

</details>

### Question 10: What string does inline `toCelsius(77)` build?

<details>
<summary>Answer</summary>

- [x] **"The temperature is 25 Celsius"**.

</details>

</details>

## Summary

Define a function, then call it. Parameters take input, return gives output, local variables stay inside, and you can reuse the same function with different arguments — even inline inside a string.

## References

- [JS Functions intro (W3Schools)](https://www.w3schools.com/js/js_function_intro.asp)
- [MDN: Functions guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [MDN: return](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
