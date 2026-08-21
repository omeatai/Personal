# JS Function Arguments

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Arguments are the real values passed into a call. They map to parameters by position. Extra values are available on the arguments object or with rest parameters. Missing values are undefined unless you default them. Primitives are copied; object properties can change outside the function.

This section has **12** examples:

- [x] **Example 1:** multiply: parameters vs arguments [View](#js-function-arguments-example-01)
- [x] **Example 2:** findMax using the arguments object [View](#js-function-arguments-example-02)
- [x] **Example 3:** sumAll using arguments [View](#js-function-arguments-example-03)
- [x] **Example 4:** subtract: order matters [View](#js-function-arguments-example-04)
- [x] **Example 5:** multiply(x, y) — variables as arguments [View](#js-function-arguments-example-05)
- [x] **Example 6:** toCelsius("John") → NaN [View](#js-function-arguments-example-06)
- [x] **Example 7:** multiply(4) missing argument → NaN [View](#js-function-arguments-example-07)
- [x] **Example 8:** Old-style default if y is undefined [View](#js-function-arguments-example-08)
- [x] **Example 9:** Default parameter y = 10 [View](#js-function-arguments-example-09)
- [x] **Example 10:** Rest parameter ...args sum [View](#js-function-arguments-example-10)
- [x] **Example 11:** Pass-by-value (number not changed outside) [View](#js-function-arguments-example-11)
- [x] **Example 12:** Object passed by reference (property changes outside) [View](#js-function-arguments-example-12)

## Detailed Explanation

- [x] **Parameters** = names. **Arguments** = values, assigned **in order**.
- [x] The **`arguments`** object is array-like (not in arrows). **Rest** `...args` is a real array.
- [x] No type or count checking. Missing args are **undefined** (often **NaN**).
- [x] Primitives are **pass-by-value**. Object **properties** change in place.

<a id="js-function-arguments-example-01"></a>

### **Example 1: multiply: parameters vs arguments**

- [x] **Parameters** are the names (`a`, `b`) in the definition.
- [x] **Arguments** are the values (`4`, `5`) in the call.

Sandbox: `code_sandbox/js-function-arguments/params-vs-args.html`

```javascript
function multiply(a, b) {
  return a * b;
}
let result = multiply(4, 5);
```

![js-function-arguments example 1 source](../code_sandbox/snaps/js-function-arguments-01-code.png)

![js-function-arguments example 1 result](../code_sandbox/snaps/js-function-arguments-01-result.png)

- [x] **Outcome:** 4 maps to `a`, 5 maps to `b`. result is **20**.

<a id="js-function-arguments-example-02"></a>

### **Example 2: findMax using the arguments object**

- [x] Every non-arrow function has a built-in **`arguments`** object.
- [x] It is array-like: `arguments.length` and `arguments[i]`.

Sandbox: `code_sandbox/js-function-arguments/findmax-arguments.html`

```javascript
function findMax() {
  let max = -Infinity;
  for (let i = 0; i < arguments.length; i++) {
    if (arguments[i] > max) {
      max = arguments[i];
    }
  }
  return max;
}
let x = findMax(1, 123, 500, 115, 44, 88);
```

![js-function-arguments example 2 source](../code_sandbox/snaps/js-function-arguments-02-code.png)

![js-function-arguments example 2 result](../code_sandbox/snaps/js-function-arguments-02-result.png)

- [x] **Outcome:** x is **500**.

<a id="js-function-arguments-example-03"></a>

### **Example 3: sumAll using arguments**

- [x] Too many arguments are still reachable via **`arguments`**.

Sandbox: `code_sandbox/js-function-arguments/sumall-arguments.html`

```javascript
function sumAll() {
  let sum = 0;
  for (let i = 0; i < arguments.length; i++) {
    sum += arguments[i];
  }
  return sum;
}
let x = sumAll(1, 123, 500, 115, 44, 88);
```

![js-function-arguments example 3 source](../code_sandbox/snaps/js-function-arguments-03-code.png)

![js-function-arguments example 3 result](../code_sandbox/snaps/js-function-arguments-03-result.png)

- [x] **Outcome:** x is **871**.

<a id="js-function-arguments-example-04"></a>

### **Example 4: subtract: order matters**

- [x] Arguments are assigned to parameters **in order**.
- [x] `subtract(10, 5)` is not `subtract(5, 10)`.

Sandbox: `code_sandbox/js-function-arguments/subtract-order.html`

```javascript
function subtract(a, b) {
  return a - b;
}
let x1 = subtract(10, 5);
let x2 = subtract(5, 10);
```

![js-function-arguments example 4 source](../code_sandbox/snaps/js-function-arguments-04-code.png)

![js-function-arguments example 4 result](../code_sandbox/snaps/js-function-arguments-04-result.png)

- [x] **Outcome:** x1 is **5**; x2 is **-5**.

<a id="js-function-arguments-example-05"></a>

### **Example 5: multiply(x, y) — variables as arguments**

- [x] Arguments do not have to be literals. They can be **variables**.
- [x] The **values** of `x` and `y` are passed, not the names.

Sandbox: `code_sandbox/js-function-arguments/variables-as-args.html`

```javascript
let x = 5;
let y = 6;
function multiply(a, b) {
  return a * b;
}
let result = multiply(x, y);
```

![js-function-arguments example 5 source](../code_sandbox/snaps/js-function-arguments-05-code.png)

![js-function-arguments example 5 result](../code_sandbox/snaps/js-function-arguments-05-result.png)

- [x] **Outcome:** result is **30**.

<a id="js-function-arguments-example-06"></a>

### **Example 6: toCelsius("John") → NaN**

- [x] JavaScript does **not** type-check arguments.
- [x] `"John" - 32` is **NaN**, so the whole formula is NaN.

Sandbox: `code_sandbox/js-function-arguments/wrong-type-nan.html`

```javascript
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}
let value = toCelsius("John");
```

![js-function-arguments example 6 source](../code_sandbox/snaps/js-function-arguments-06-code.png)

![js-function-arguments example 6 result](../code_sandbox/snaps/js-function-arguments-06-result.png)

- [x] **Outcome:** value is **NaN**.

<a id="js-function-arguments-example-07"></a>

### **Example 7: multiply(4) missing argument → NaN**

- [x] Fewer arguments than parameters: the rest are **undefined**.
- [x] `4 * undefined` is **NaN**.

Sandbox: `code_sandbox/js-function-arguments/missing-arg.html`

```javascript
function multiply(a, b) {
  return a * b;
}
let result = multiply(4);
```

![js-function-arguments example 7 source](../code_sandbox/snaps/js-function-arguments-07-code.png)

![js-function-arguments example 7 result](../code_sandbox/snaps/js-function-arguments-07-result.png)

- [x] **Outcome:** result is **NaN**.

<a id="js-function-arguments-example-08"></a>

### **Example 8: Old-style default if y is undefined**

- [x] Before default parameters, people assigned a fallback **inside** the function.
- [x] If `y === undefined`, set `y = 2`.

Sandbox: `code_sandbox/js-function-arguments/old-default.html`

```javascript
function myFunction(x, y) {
  if (y === undefined) {
    y = 2;
  }
  return x + y;
}
let a = myFunction(5);
let b = myFunction(5, 3);
```

![js-function-arguments example 8 source](../code_sandbox/snaps/js-function-arguments-08-code.png)

![js-function-arguments example 8 result](../code_sandbox/snaps/js-function-arguments-08-result.png)

- [x] **Outcome:** `myFunction(5)` is **7**. `myFunction(5, 3)` is **8**.

<a id="js-function-arguments-example-09"></a>

### **Example 9: Default parameter y = 10**

- [x] ES2015: `y = 10` in the parameter list.
- [x] Used when the argument is omitted or **undefined**.

Sandbox: `code_sandbox/js-function-arguments/default-param-y10.html`

```javascript
function myFunction(x, y = 10) {
  return x + y;
}
let a = myFunction(5);
let b = myFunction(5, undefined);
let c = myFunction(5, 1);
```

![js-function-arguments example 9 source](../code_sandbox/snaps/js-function-arguments-09-code.png)

![js-function-arguments example 9 result](../code_sandbox/snaps/js-function-arguments-09-result.png)

- [x] **Outcome:** **15**, **15**, and **6**.

<a id="js-function-arguments-example-10"></a>

### **Example 10: Rest parameter ...args sum**

- [x] `...args` gathers remaining arguments into a **real array**.
- [x] Prefer rest over `arguments` in new code (and rest works in arrows).

Sandbox: `code_sandbox/js-function-arguments/rest-sum.html`

```javascript
function sum(...args) {
  let total = 0;
  for (let arg of args) total += arg;
  return total;
}
let x = sum(4, 9, 16, 25, 29, 100, 66, 77);
```

![js-function-arguments example 10 source](../code_sandbox/snaps/js-function-arguments-10-code.png)

![js-function-arguments example 10 result](../code_sandbox/snaps/js-function-arguments-10-result.png)

- [x] **Outcome:** x is **326**.

<a id="js-function-arguments-example-11"></a>

### **Example 11: Pass-by-value (number not changed outside)**

- [x] Primitives are passed **by value**. The function gets a copy.
- [x] Changing the parameter does **not** change the original variable.

Sandbox: `code_sandbox/js-function-arguments/pass-by-value.html`

```javascript
function addOne(n) {
  n = n + 1;
  return n;
}
let x = 10;
let y = addOne(x);
```

![js-function-arguments example 11 source](../code_sandbox/snaps/js-function-arguments-11-code.png)

![js-function-arguments example 11 result](../code_sandbox/snaps/js-function-arguments-11-result.png)

- [x] **Outcome:** x is still **10**. y is **11**.

<a id="js-function-arguments-example-12"></a>

### **Example 12: Object passed by reference (property changes outside)**

- [x] Object **references** are values, so objects behave as pass-by-reference.
- [x] Changing a **property** inside the function changes the original object.

Sandbox: `code_sandbox/js-function-arguments/pass-by-reference.html`

```javascript
function changeName(obj) {
  obj.name = "Jane";
}
let person = { name: "John" };
changeName(person);
```

![js-function-arguments example 12 source](../code_sandbox/snaps/js-function-arguments-12-code.png)

![js-function-arguments example 12 result](../code_sandbox/snaps/js-function-arguments-12-result.png)

- [x] **Outcome:** person.name is **"Jane"** outside the function too.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-function-arguments/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: In `multiply(4, 5)`, what are parameters vs arguments?

<details>
<summary>Answer</summary>

- [x] Parameters: **a, b**.
- [x] Arguments: **4, 5**.

</details>

### Question 2: What is `findMax(1, 123, 500, 115, 44, 88)`?

<details>
<summary>Answer</summary>

- [x] **500** — uses the `arguments` object.

</details>

### Question 3: What is `sumAll(1, 123, 500, 115, 44, 88)`?

<details>
<summary>Answer</summary>

- [x] **871**.

</details>

### Question 4: What is `subtract(10, 5)` vs `subtract(5, 10)`?

<details>
<summary>Answer</summary>

- [x] **5** vs **-5**. Order matters.

</details>

### Question 5: Can arguments be variables?

<details>
<summary>Answer</summary>

- [x] **Yes.** `multiply(x, y)` passes the **values** of x and y.

</details>

### Question 6: What is `toCelsius("John")`?

<details>
<summary>Answer</summary>

- [x] **NaN** — no type check.

</details>

### Question 7: What is `multiply(4)` with two parameters?

<details>
<summary>Answer</summary>

- [x] **NaN** — `b` is undefined.

</details>

### Question 8: How did people default `y` before ES2015?

<details>
<summary>Answer</summary>

- [x] `if (y === undefined) { y = 2; }` inside the function.

</details>

### Question 9: What is `myFunction(5)` with `y = 10`?

<details>
<summary>Answer</summary>

- [x] **15**.

</details>

### Question 10: What is `sum(4, 9, 16, 25, 29, 100, 66, 77)` with rest?

<details>
<summary>Answer</summary>

- [x] **326**.

</details>

### Question 11: If `addOne` does `n = n + 1` on a number `x = 10`, is `x` changed?

<details>
<summary>Answer</summary>

- [x] **No.** `x` stays **10**. The function got a copy.

</details>

### Question 12: If a function sets `obj.name = "Jane"`, does the original object change?

<details>
<summary>Answer</summary>

- [x] **Yes.** Object properties are visible outside.

</details>

</details>

## Summary

Arguments fill parameters by position. Use arguments or rest for a variable number of values, defaults for missing ones, and remember that numbers are copied while object properties are not.

## References

- [JS Function Arguments (W3Schools)](https://www.w3schools.com/js/js_function_arguments.asp)
- [MDN: arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
- [MDN: Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [MDN: Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
