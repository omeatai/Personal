# JS Function Returns

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

return sends a value out of a function and stops the function immediately. You can return any type, use the call inside a larger expression, leave early on a condition, or update HTML with the result. A function with no return yields undefined. console.log is not the same as return.

This section has **9** examples:

- [x] **Example 1:** sayHello return stored [View](#js-function-return-example-01)
- [x] **Example 2:** multiply(4, 5) = 20 [View](#js-function-return-example-02)
- [x] **Example 3:** multiply(2, 3) \* 10 = 60 [View](#js-function-return-example-03)
- [x] **Example 4:** fullName returns a string [View](#js-function-return-example-04)
- [x] **Example 5:** Early return "Done" skips a \* b [View](#js-function-return-example-05)
- [x] **Example 6:** No return → undefined [View](#js-function-return-example-06)
- [x] **Example 7:** checkAge early return [View](#js-function-return-example-07)
- [x] **Example 8:** toCelsius innerHTML 77 [View](#js-function-return-example-08)
- [x] **Example 9:** console.log vs return [View](#js-function-return-example-09)

## Detailed Explanation

- [x] `return value;` sends **value** to the caller and **exits** the function.
- [x] Code **after** `return` never runs.
- [x] No `return` means the result is **undefined**.
- [x] `console.log` displays; it does **not** return a value to assign.

<a id="js-function-return-example-01"></a>

### **Example 1: sayHello return stored**

- [x] `return` sends a value out of the function.
- [x] After the call, `message` holds that value.

Sandbox: `code_sandbox/js-function-return/sayhello-stored.html`

```javascript
function sayHello() {
  return "Hello World";
}
let message = sayHello();
```

![js-function-return example 1 source](../code_sandbox/snaps/js-function-return-01-code.png)

![js-function-return example 1 result](../code_sandbox/snaps/js-function-return-01-result.png)

- [x] **Outcome:** message is **"Hello World"**.

<a id="js-function-return-example-02"></a>

### **Example 2: multiply(4, 5) = 20**

- [x] Most functions return a **calculated** value.

Sandbox: `code_sandbox/js-function-return/multiply-20.html`

```javascript
function multiply(a, b) {
  return a * b;
}
let result = multiply(4, 5);
```

![js-function-return example 2 source](../code_sandbox/snaps/js-function-return-02-code.png)

![js-function-return example 2 result](../code_sandbox/snaps/js-function-return-02-result.png)

- [x] **Outcome:** result is **20**.

<a id="js-function-return-example-03"></a>

### **Example 3: multiply(2, 3) \* 10 = 60**

- [x] A function call can sit **inside another expression**.
- [x] `multiply(2, 3)` returns 6, then `6 * 10` is 60.

Sandbox: `code_sandbox/js-function-return/multiply-in-expression.html`

```javascript
function multiply(a, b) {
  return a * b;
}
let total = multiply(2, 3) * 10;
```

![js-function-return example 3 source](../code_sandbox/snaps/js-function-return-03-code.png)

![js-function-return example 3 result](../code_sandbox/snaps/js-function-return-03-result.png)

- [x] **Outcome:** total is **60**.

<a id="js-function-return-example-04"></a>

### **Example 4: fullName returns a string**

- [x] A function can return **any** type, not only numbers.

Sandbox: `code_sandbox/js-function-return/fullname-return.html`

```javascript
function fullName(firstName, lastName) {
  return firstName + " " + lastName;
}
let name = fullName("John", "Doe");
```

![js-function-return example 4 source](../code_sandbox/snaps/js-function-return-04-code.png)

![js-function-return example 4 result](../code_sandbox/snaps/js-function-return-04-result.png)

- [x] **Outcome:** name is **"John Doe"**.

<a id="js-function-return-example-05"></a>

### **Example 5: Early return "Done" skips a \* b**

- [x] When JavaScript hits `return`, the function **stops**.
- [x] Code after `return` never runs.

Sandbox: `code_sandbox/js-function-return/early-return-done.html`

```javascript
function multiply(a, b) {
  return "Done";
  return a * b;
}
let result = multiply(4, 3);
```

![js-function-return example 5 source](../code_sandbox/snaps/js-function-return-05-code.png)

![js-function-return example 5 result](../code_sandbox/snaps/js-function-return-05-result.png)

- [x] **Outcome:** result is **"Done"**, not 12.

<a id="js-function-return-example-06"></a>

### **Example 6: No return → undefined**

- [x] If a function has no `return`, the result is **undefined**.
- [x] Computing `a * b` inside is not enough — you must return it.

Sandbox: `code_sandbox/js-function-return/no-return-undefined.html`

```javascript
function multiply(a, b) {
  let x = a * b;
}
let result = multiply(4, 3);
```

![js-function-return example 6 source](../code_sandbox/snaps/js-function-return-06-code.png)

![js-function-return example 6 result](../code_sandbox/snaps/js-function-return-06-result.png)

- [x] **Outcome:** result is **undefined**.

<a id="js-function-return-example-07"></a>

### **Example 7: checkAge early return**

- [x] Use `return` to **leave early** on a condition.
- [x] Younger than 18 gets **Too young**; otherwise **Access granted**.

Sandbox: `code_sandbox/js-function-return/checkage-early.html`

```javascript
function checkAge(age) {
  if (age < 18) {
    return "Too young";
  }
  return "Access granted";
}
let a = checkAge(15);
let b = checkAge(21);
```

![js-function-return example 7 source](../code_sandbox/snaps/js-function-return-07-code.png)

![js-function-return example 7 result](../code_sandbox/snaps/js-function-return-07-result.png)

- [x] **Outcome:** 15 → **"Too young"**. 21 → **"Access granted"**.

<a id="js-function-return-example-08"></a>

### **Example 8: toCelsius innerHTML 77**

- [x] Returned values are often used to **update HTML**.

Sandbox: `code_sandbox/js-function-return/tocelsius-innerhtml.html`

```javascript
function toCelsius(farenheit) {
  return (5 / 9) * (farenheit - 32);
}
document.getElementById("demo").innerHTML = toCelsius(77);
```

![js-function-return example 8 source](../code_sandbox/snaps/js-function-return-08-code.png)

![js-function-return example 8 result](../code_sandbox/snaps/js-function-return-08-result.png)

- [x] **Outcome:** #demo shows **25**.

<a id="js-function-return-example-09"></a>

### **Example 9: console.log vs return**

- [x] `console.log()` **shows** a value; it does **not** return it to the caller.
- [x] A function that only logs returns **undefined** if you store the call.

Sandbox: `code_sandbox/js-function-return/console-vs-return.html`

```javascript
function onlyLog() {
  console.log("Hello");
}
function withReturn() {
  return "Hello";
}
let x = onlyLog();
let y = withReturn();
```

![js-function-return example 9 source](../code_sandbox/snaps/js-function-return-09-code.png)

![js-function-return example 9 result](../code_sandbox/snaps/js-function-return-09-result.png)

- [x] **Outcome:** `onlyLog()` returns **undefined**. `withReturn()` returns **"Hello"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-function-return/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `let message = sayHello()`?

<details>
<summary>Answer</summary>

- [x] **"Hello World"**.

</details>

### Question 2: What is `multiply(4, 5)`?

<details>
<summary>Answer</summary>

- [x] **20**.

</details>

### Question 3: What is `multiply(2, 3) * 10`?

<details>
<summary>Answer</summary>

- [x] **60** — 6 times 10.

</details>

### Question 4: What is `fullName("John", "Doe")`?

<details>
<summary>Answer</summary>

- [x] **"John Doe"**.

</details>

### Question 5: What if the first line is `return "Done"` before `return a * b`?

<details>
<summary>Answer</summary>

- [x] The result is **"Done"**. The multiply never runs.

</details>

### Question 6: What is the result if you compute `a * b` but never return it?

<details>
<summary>Answer</summary>

- [x] **undefined**.

</details>

### Question 7: What does `checkAge(15)` vs `checkAge(21)` return?

<details>
<summary>Answer</summary>

- [x] **"Too young"** vs **"Access granted"**.

</details>

### Question 8: What does `innerHTML = toCelsius(77)` show?

<details>
<summary>Answer</summary>

- [x] **25**.

</details>

### Question 9: Is `console.log("Hello")` a return value?

<details>
<summary>Answer</summary>

- [x] **No.** Logging is a side effect.
- [x] A function that only logs returns **undefined**.

</details>

### Question 10: Can a function return a string, not just a number?

<details>
<summary>Answer</summary>

- [x] **Yes.** `return` works with any type.

</details>

### Question 11: Does `return` stop the rest of the function?

<details>
<summary>Answer</summary>

- [x] **Yes.** That is why early returns work.

</details>

</details>

## Summary

Use return to send a value back and to stop the function. Expressions can use that value immediately. Skip return and you get undefined. Logging to the console is not returning.

## References

- [JS Function Return (W3Schools)](https://www.w3schools.com/js/js_function_return.asp)
- [MDN: return](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
- [MDN: Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
