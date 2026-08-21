# JS Function Parameters

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Parameters are the names in a function definition. They receive the arguments you pass when you call the function. JavaScript does not type-check, does not require a matching argument count, and since ES2015 you can give a parameter a default.

This section has **6** examples:

- [x] **Example 1:** multiply(4, 5) [View](#js-function-parameters-example-01)
- [x] **Example 2:** sayHello("John") — one parameter [View](#js-function-parameters-example-02)
- [x] **Example 3:** toCelsius(77) — one parameter [View](#js-function-parameters-example-03)
- [x] **Example 4:** fullName("John", "Doe") — multiple parameters [View](#js-function-parameters-example-04)
- [x] **Example 5:** toCelsius() missing argument → NaN [View](#js-function-parameters-example-05)
- [x] **Example 6:** Default parameter y = 10 [View](#js-function-parameters-example-06)

## Detailed Explanation

- [x] Parameters are listed in `function name(p1, p2)` — **comma-separated**.
- [x] JS does **not** specify types, type-check, or count arguments.
- [x] A missing argument is **undefined** (often producing **NaN** in math).
- [x] **Default parameters** (`y = 10`) fill in omitted or undefined arguments.

<a id="js-function-parameters-example-01"></a>

### **Example 1: multiply(4, 5)**

- [x] Parameters `a` and `b` receive the arguments **4** and **5**.

Sandbox: `code_sandbox/js-function-parameters/multiply-4-5.html`

```javascript
function multiply(a, b) {
  return a * b;
}
let result = multiply(4, 5);
```

![js-function-parameters example 1 source](../code_sandbox/snaps/js-function-parameters-01-code.png)

![js-function-parameters example 1 result](../code_sandbox/snaps/js-function-parameters-01-result.png)

- [x] **Outcome:** result is **20**.

<a id="js-function-parameters-example-02"></a>

### **Example 2: sayHello("John") — one parameter**

- [x] A function can have **one** parameter.
- [x] The argument `"John"` is assigned to `name`.

Sandbox: `code_sandbox/js-function-parameters/sayhello-john.html`

```javascript
function sayHello(name) {
  return "Hello " + name;
}
let greeting = sayHello("John");
```

![js-function-parameters example 2 source](../code_sandbox/snaps/js-function-parameters-02-code.png)

![js-function-parameters example 2 result](../code_sandbox/snaps/js-function-parameters-02-result.png)

- [x] **Outcome:** greeting is **"Hello John"**.

<a id="js-function-parameters-example-03"></a>

### **Example 3: toCelsius(77) — one parameter**

- [x] `fahrenheit` is the parameter; **77** is the argument.

Sandbox: `code_sandbox/js-function-parameters/tocelsius-77.html`

```javascript
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}
let value = toCelsius(77);
```

![js-function-parameters example 3 source](../code_sandbox/snaps/js-function-parameters-03-code.png)

![js-function-parameters example 3 result](../code_sandbox/snaps/js-function-parameters-03-result.png)

- [x] **Outcome:** value is **25**.

<a id="js-function-parameters-example-04"></a>

### **Example 4: fullName("John", "Doe") — multiple parameters**

- [x] List multiple parameters **separated by commas**.

Sandbox: `code_sandbox/js-function-parameters/fullname.html`

```javascript
function fullName(firstName, lastName) {
  return firstName + " " + lastName;
}
let name = fullName("John", "Doe");
```

![js-function-parameters example 4 source](../code_sandbox/snaps/js-function-parameters-04-code.png)

![js-function-parameters example 4 result](../code_sandbox/snaps/js-function-parameters-04-result.png)

- [x] **Outcome:** name is **"John Doe"**.

<a id="js-function-parameters-example-05"></a>

### **Example 5: toCelsius() missing argument → NaN**

- [x] JavaScript does **not** check the number of arguments.
- [x] A missing parameter is **undefined**. `(5/9) * (undefined - 32)` is **NaN**.

Sandbox: `code_sandbox/js-function-parameters/missing-arg-nan.html`

```javascript
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}
let value = toCelsius();
```

![js-function-parameters example 5 source](../code_sandbox/snaps/js-function-parameters-05-code.png)

![js-function-parameters example 5 result](../code_sandbox/snaps/js-function-parameters-05-result.png)

- [x] **Outcome:** value is **NaN**.

<a id="js-function-parameters-example-06"></a>

### **Example 6: Default parameter y = 10**

- [x] ES2015 default parameters: if `y` is omitted or `undefined`, use **10**.
- [x] `myFunction(5)` is `5 + 10`.

Sandbox: `code_sandbox/js-function-parameters/default-param.html`

```javascript
function myFunction(x, y = 10) {
  return x + y;
}
let a = myFunction(5);
let b = myFunction(5, 3);
```

![js-function-parameters example 6 source](../code_sandbox/snaps/js-function-parameters-06-code.png)

![js-function-parameters example 6 result](../code_sandbox/snaps/js-function-parameters-06-result.png)

- [x] **Outcome:** `myFunction(5)` is **15**. `myFunction(5, 3)` is **8**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-function-parameters/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `multiply(4, 5)`?

<details>
<summary>Answer</summary>

- [x] **20**. Parameters `a` and `b` received 4 and 5.

</details>

### Question 2: What is `sayHello("John")`?

<details>
<summary>Answer</summary>

- [x] **"Hello John"**.

</details>

### Question 3: What is `toCelsius(77)`?

<details>
<summary>Answer</summary>

- [x] **25**.

</details>

### Question 4: What is `fullName("John", "Doe")`?

<details>
<summary>Answer</summary>

- [x] **"John Doe"**.

</details>

### Question 5: What is `toCelsius()` with no argument?

<details>
<summary>Answer</summary>

- [x] **NaN** — `fahrenheit` is undefined.

</details>

### Question 6: What is `myFunction(5)` if `y = 10`?

<details>
<summary>Answer</summary>

- [x] **15**.
- [x] `myFunction(5, 3)` is **8**.

</details>

### Question 7: Does JavaScript check argument types?

<details>
<summary>Answer</summary>

- [x] **No.**

</details>

### Question 8: Does JavaScript check how many arguments you passed?

<details>
<summary>Answer</summary>

- [x] **No.** Extra args are ignored unless you read `arguments` or rest. Missing ones are **undefined**.

</details>

### Question 9: When is a default parameter used?

<details>
<summary>Answer</summary>

- [x] When the argument is **omitted** or **undefined**.

</details>

### Question 10: What is the difference between a parameter and an argument?

<details>
<summary>Answer</summary>

- [x] Parameter = **name** in the definition.
- [x] Argument = **value** in the call.

</details>

</details>

## Summary

List parameters in the definition and pass arguments in the call. JavaScript will not type-check or count them for you. Missing values are undefined (NaN in math) unless you set a default.

## References

- [JS Function Parameters (W3Schools)](https://www.w3schools.com/js/js_function_parameters.asp)
- [MDN: Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [MDN: Functions guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
