# JS Function Invocation

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A function runs when something invokes it: a call in your code, an event such as a button click, or a self-invoked function. Parentheses invoke. Without them you get the function object itself, not the result. You must store, log, or display a return value if you want to see it.

This section has **13** examples:

- [x] **Example 1:** Function defined, not run [View](#js-function-invocation-example-01)
- [x] **Example 2:** sayHello() called unused [View](#js-function-invocation-example-02)
- [x] **Example 3:** Store the greeting [View](#js-function-invocation-example-03)
- [x] **Example 4:** console.log(sayHello()) [View](#js-function-invocation-example-04)
- [x] **Example 5:** innerHTML = sayHello() [View](#js-function-invocation-example-05)
- [x] **Example 6:** Call many times: a, b, c [View](#js-function-invocation-example-06)
- [x] **Example 7:** toCelsius(77) invokes the function [View](#js-function-invocation-example-07)
- [x] **Example 8:** Access without () — the function object [View](#js-function-invocation-example-08)
- [x] **Example 9:** let text = sayHello (reference) [View](#js-function-invocation-example-09)
- [x] **Example 10:** showHello() wrapping sayHello [View](#js-function-invocation-example-10)
- [x] **Example 11:** Button click invoking showHello [View](#js-function-invocation-example-11)
- [x] **Example 12:** Common mistake: no return [View](#js-function-invocation-example-12)
- [x] **Example 13:** Common mistake: no display [View](#js-function-invocation-example-13)

## Detailed Explanation

- [x] **Invoke** means run the function — by a call, an event, or automatically.
- [x] `name()` is the **result**. `name` (no `()`) is the **function object**.
- [x] A return value is unused unless you **store** or **display** it.
- [x] Functions can call other functions, and buttons can call functions.

<a id="js-function-invocation-example-01"></a>

### **Example 1: Function defined, not run**

- [x] The code inside a function does **not** run when it is defined.
- [x] It runs when something **invokes** it (a call, an event, or an IIFE).

Sandbox: `code_sandbox/js-function-invocation/defined-not-run.html`

```javascript
function sayHello() {
  return "Hello World";
}
```

![js-function-invocation example 1 source](../code_sandbox/snaps/js-function-invocation-01-code.png)

![js-function-invocation example 1 result](../code_sandbox/snaps/js-function-invocation-01-result.png)

- [x] **Outcome:** The function object exists, but **Hello World** has not been produced yet.

<a id="js-function-invocation-example-02"></a>

### **Example 2: sayHello() called unused**

- [x] This call **does** run the function.
- [x] The return value is **thrown away** unless you store or display it.

Sandbox: `code_sandbox/js-function-invocation/called-unused.html`

```javascript
function sayHello() {
  return "Hello World";
}
sayHello();
```

![js-function-invocation example 2 source](../code_sandbox/snaps/js-function-invocation-02-code.png)

![js-function-invocation example 2 result](../code_sandbox/snaps/js-function-invocation-02-result.png)

- [x] **Outcome:** The function ran, but the first return value was unused. Calling again still returns **Hello World**.

<a id="js-function-invocation-example-03"></a>

### **Example 3: Store the greeting**

- [x] To **use** a returned value, assign it to a variable.

Sandbox: `code_sandbox/js-function-invocation/store-greeting.html`

```javascript
function sayHello() {
  return "Hello World";
}
let greeting = sayHello();
```

![js-function-invocation example 3 source](../code_sandbox/snaps/js-function-invocation-03-code.png)

![js-function-invocation example 3 result](../code_sandbox/snaps/js-function-invocation-03-result.png)

- [x] **Outcome:** greeting is **"Hello World"**.

<a id="js-function-invocation-example-04"></a>

### **Example 4: console.log(sayHello())**

- [x] `console.log` prints the return value to the **console**.
- [x] This sandbox also writes it to **#demo** so the screenshot can show it.

Sandbox: `code_sandbox/js-function-invocation/console-log.html`

```javascript
function sayHello() {
  return "Hello World";
}
console.log(sayHello());
```

![js-function-invocation example 4 source](../code_sandbox/snaps/js-function-invocation-04-code.png)

![js-function-invocation example 4 result](../code_sandbox/snaps/js-function-invocation-04-result.png)

- [x] **Outcome:** console.log prints **"Hello World"**; #demo shows the same string.

<a id="js-function-invocation-example-05"></a>

### **Example 5: innerHTML = sayHello()**

- [x] You can put the return value into an HTML element.
- [x] `innerHTML` (or `innerText`) displays it on the page.

Sandbox: `code_sandbox/js-function-invocation/innerhtml.html`

```javascript
function sayHello() {
  return "Hello World";
}
document.getElementById("demo").innerHTML = sayHello();
```

![js-function-invocation example 5 source](../code_sandbox/snaps/js-function-invocation-05-code.png)

![js-function-invocation example 5 result](../code_sandbox/snaps/js-function-invocation-05-result.png)

- [x] **Outcome:** #demo shows **Hello World**.

<a id="js-function-invocation-example-06"></a>

### **Example 6: Call many times: a, b, c**

- [x] You can invoke the same function **whenever** you need it.
- [x] Each call returns a fresh value.

Sandbox: `code_sandbox/js-function-invocation/call-many-times.html`

```javascript
function sayHello() {
  return "Hello World";
}
let a = sayHello();
let b = sayHello();
let c = sayHello();
```

![js-function-invocation example 6 source](../code_sandbox/snaps/js-function-invocation-06-code.png)

![js-function-invocation example 6 result](../code_sandbox/snaps/js-function-invocation-06-result.png)

- [x] **Outcome:** a, b, and c are each **Hello World**.

<a id="js-function-invocation-example-07"></a>

### **Example 7: toCelsius(77) invokes the function**

- [x] The `()` operator **invokes** the function.
- [x] `toCelsius(77)` is the **result**; `toCelsius` without `()` is the function itself.

Sandbox: `code_sandbox/js-function-invocation/tocelsius-77.html`

```javascript
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}
let value = toCelsius(77);
```

![js-function-invocation example 7 source](../code_sandbox/snaps/js-function-invocation-07-code.png)

![js-function-invocation example 7 result](../code_sandbox/snaps/js-function-invocation-07-result.png)

- [x] **Outcome:** value is **25**.

<a id="js-function-invocation-example-08"></a>

### **Example 8: Access without () — the function object**

- [x] `toCelsius` (no parentheses) returns the **function itself**, not 25.
- [x] `typeof` is **function**. `String(value)` is the source text.

Sandbox: `code_sandbox/js-function-invocation/access-without-parens.html`

```javascript
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}
let value = toCelsius;
```

![js-function-invocation example 8 source](../code_sandbox/snaps/js-function-invocation-08-code.png)

![js-function-invocation example 8 result](../code_sandbox/snaps/js-function-invocation-08-result.png)

- [x] **Outcome:** `typeof value` is **"function"**. The string starts with `function toCelsius`.

<a id="js-function-invocation-example-09"></a>

### **Example 9: let text = sayHello (reference)**

- [x] `sayHello` refers to the **function**. `sayHello()` refers to the **result**.
- [x] `let text = sayHello` copies the function reference, not "Hello World".

Sandbox: `code_sandbox/js-function-invocation/text-is-reference.html`

```javascript
function sayHello() {
  return "Hello World";
}
let text = sayHello;
```

![js-function-invocation example 9 source](../code_sandbox/snaps/js-function-invocation-09-code.png)

![js-function-invocation example 9 result](../code_sandbox/snaps/js-function-invocation-09-result.png)

- [x] **Outcome:** `text` is the function. `text()` returns **"Hello World"**.

<a id="js-function-invocation-example-10"></a>

### **Example 10: showHello() wrapping sayHello**

- [x] You can call functions from **other functions**.
- [x] `showHello` writes `sayHello()` into #demo.

Sandbox: `code_sandbox/js-function-invocation/showhello-wraps.html`

```javascript
function sayHello() {
  return "Hello World";
}
function showHello() {
  document.getElementById("demo").innerHTML = sayHello();
}
showHello();
```

![js-function-invocation example 10 source](../code_sandbox/snaps/js-function-invocation-10-code.png)

![js-function-invocation example 10 result](../code_sandbox/snaps/js-function-invocation-10-result.png)

- [x] **Outcome:** #demo shows **Hello World** after `showHello()` runs.

<a id="js-function-invocation-example-11"></a>

### **Example 11: Button click invoking showHello**

- [x] A function can run when an **event** occurs (a button click).
- [x] This page auto-calls `showHello()` on load so the screenshot shows the result after a “click”.

Sandbox: `code_sandbox/js-function-invocation/button-click.html`

```javascript
function sayHello() {
  return "Hello World";
}
function showHello() {
  document.getElementById("demo").innerHTML = sayHello();
}
```

![js-function-invocation example 11 source](../code_sandbox/snaps/js-function-invocation-11-code.png)

![js-function-invocation example 11 result](../code_sandbox/snaps/js-function-invocation-11-result.png)

- [x] **Outcome:** The button is present, and #demo shows **Hello World**.

<a id="js-function-invocation-example-12"></a>

### **Example 12: Common mistake: no return**

- [x] Some functions do **not** return a value.
- [x] Storing the call then yields **undefined**.

Sandbox: `code_sandbox/js-function-invocation/mistake-no-return.html`

```javascript
function sayHello() {
  let msg = "Hello World";
}
let text = sayHello();
```

![js-function-invocation example 12 source](../code_sandbox/snaps/js-function-invocation-12-code.png)

![js-function-invocation example 12 result](../code_sandbox/snaps/js-function-invocation-12-result.png)

- [x] **Outcome:** text is **undefined** because there is no `return`.

<a id="js-function-invocation-example-13"></a>

### **Example 13: Common mistake: no display**

- [x] Even with a return value, the page stays blank unless you **display** it.
- [x] Store it, `console.log` it, or write it into an element.

Sandbox: `code_sandbox/js-function-invocation/mistake-no-display.html`

```javascript
function sayHello() {
  return "Hello World";
}
let hidden = sayHello();
// nothing writes hidden to the page in the original mistake
```

![js-function-invocation example 13 source](../code_sandbox/snaps/js-function-invocation-13-code.png)

![js-function-invocation example 13 result](../code_sandbox/snaps/js-function-invocation-13-result.png)

- [x] **Outcome:** The value **Hello World** exists in `hidden`, but a page that never displays it looks empty.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-function-invocation/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does defining `sayHello` run it?

<details>
<summary>Answer</summary>

- [x] **No.** The body waits for an invocation.

</details>

### Question 2: What happens if you write `sayHello();` and ignore the result?

<details>
<summary>Answer</summary>

- [x] The function **runs**, but the return value is **discarded**.

</details>

### Question 3: How do you keep the greeting?

<details>
<summary>Answer</summary>

- [x] `let greeting = sayHello();` — greeting is **"Hello World"**.

</details>

### Question 4: What does `console.log(sayHello())` print?

<details>
<summary>Answer</summary>

- [x] **Hello World** (in the console).
- [x] This sandbox also shows it in #demo.

</details>

### Question 5: What does `innerHTML = sayHello()` show?

<details>
<summary>Answer</summary>

- [x] **Hello World** in the element.

</details>

### Question 6: What are `a`, `b`, and `c` after three `sayHello()` calls?

<details>
<summary>Answer</summary>

- [x] Each is **"Hello World"**.

</details>

### Question 7: What is `toCelsius(77)`?

<details>
<summary>Answer</summary>

- [x] **25** — the function **result**.

</details>

### Question 8: What is `let value = toCelsius` (no parentheses)?

<details>
<summary>Answer</summary>

- [x] `typeof value` is **"function"** — the function object, not 25.

</details>

### Question 9: What is `let text = sayHello`?

<details>
<summary>Answer</summary>

- [x] `text` is a **reference** to the function.
- [x] `text()` then returns **Hello World**.

</details>

### Question 10: How can `showHello` display a greeting?

<details>
<summary>Answer</summary>

- [x] It calls `sayHello()` and writes the string into **#demo**.

</details>

### Question 11: What is a common event that invokes a function?

<details>
<summary>Answer</summary>

- [x] A **button click** (`onclick`).

</details>

### Question 12: What if the function has no `return`?

<details>
<summary>Answer</summary>

- [x] The call evaluates to **undefined**.

</details>

### Question 13: Why might the page look empty after a call?

<details>
<summary>Answer</summary>

- [x] You returned a value but **never displayed** it.

</details>

</details>

## Summary

Parentheses invoke a function. Skip them and you get the function itself. Store or display the return value, call from other functions or events, and remember that no return means undefined.

## References

- [JS Function Invocation (W3Schools)](https://www.w3schools.com/js/js_function_invocation.asp)
- [MDN: Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
- [MDN: Function.prototype.call](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
