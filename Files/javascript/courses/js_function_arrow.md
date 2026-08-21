# JS Function Arrow

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Arrow functions are a short syntax for function expressions. You can omit function, return, and braces for a single expression, and omit parentheses around a single parameter. They are not hoisted, they do not have their own this, and braces without return yield undefined. Duplicate Tryits on the W3Schools page are shown once.

This section has **12** examples:

- [x] **Example 1:** const multiply = (a, b) => a \* b [View](#js-function-arrow-example-01)
- [x] **Example 2:** Before arrow: function expression multiply [View](#js-function-arrow-example-02)
- [x] **Example 3:** hello arrow with no parameters [View](#js-function-arrow-example-03)
- [x] **Example 4:** hello as a function expression [View](#js-function-arrow-example-04)
- [x] **Example 5:** square (x) => with parentheses [View](#js-function-arrow-example-05)
- [x] **Example 6:** square x => without parentheses [View](#js-function-arrow-example-06)
- [x] **Example 7:** hello (val) => one parameter [View](#js-function-arrow-example-07)
- [x] **Example 8:** hello val => one parameter, no parens [View](#js-function-arrow-example-08)
- [x] **Example 9:** Braces without return → undefined [View](#js-function-arrow-example-09)
- [x] **Example 10:** Calling an arrow before it is defined [View](#js-function-arrow-example-10)
- [x] **Example 11:** Method this with function() → "John" [View](#js-function-arrow-example-11)
- [x] **Example 12:** Method this with arrow → not John [View](#js-function-arrow-example-12)

## Detailed Explanation

- [x] `(a, b) => a * b` skips `function`, `return`, and `{}` for one expression.
- [x] Parentheses: required for **zero or 2+** parameters; optional for **one**.
- [x] A `{ }` body needs an explicit **`return`**. `=> return` is a **SyntaxError**.
- [x] Arrows are **not hoisted** and do **not** bind their own **`this`** — skip them as object methods.

<a id="js-function-arrow-example-01"></a>

### **Example 1: const multiply = (a, b) => a \* b**

- [x] Skip `function`, `return`, and `{}` when the body is one expression.
- [x] The W3Schools page repeats this same Tryit under **Shorter Syntax / With Arrow** — included once.

Sandbox: `code_sandbox/js-function-arrow/multiply-arrow.html`

```javascript
const multiply = (a, b) => a * b;
let z = multiply(4, 5);
```

![js-function-arrow example 1 source](../code_sandbox/snaps/js-function-arrow-01-code.png)

![js-function-arrow example 1 result](../code_sandbox/snaps/js-function-arrow-01-result.png)

- [x] **Outcome:** z is **20**.

<a id="js-function-arrow-example-02"></a>

### **Example 2: Before arrow: function expression multiply**

- [x] This is the longer **function expression** that the arrow replaces.

Sandbox: `code_sandbox/js-function-arrow/before-arrow.html`

```javascript
const multiply = function (a, b) {
  return a * b;
};
let z = multiply(4, 5);
```

![js-function-arrow example 2 source](../code_sandbox/snaps/js-function-arrow-02-code.png)

![js-function-arrow example 2 result](../code_sandbox/snaps/js-function-arrow-02-result.png)

- [x] **Outcome:** z is also **20**.

<a id="js-function-arrow-example-03"></a>

### **Example 3: hello arrow with no parameters**

- [x] Zero parameters still need **empty parentheses**: `() =>`.
- [x] The page repeats this Tryit (return-by-default and no-params sections). Included once.

Sandbox: `code_sandbox/js-function-arrow/hello-no-params.html`

```javascript
const hello = () => "Hello World!";
let text = hello();
```

![js-function-arrow example 3 source](../code_sandbox/snaps/js-function-arrow-03-code.png)

![js-function-arrow example 3 result](../code_sandbox/snaps/js-function-arrow-03-result.png)

- [x] **Outcome:** text is **"Hello World!"**.

<a id="js-function-arrow-example-04"></a>

### **Example 4: hello as a function expression**

- [x] Same result without arrow syntax.

Sandbox: `code_sandbox/js-function-arrow/hello-expression.html`

```javascript
const hello = function () {
  return "Hello World!";
};
let text = hello();
```

![js-function-arrow example 4 source](../code_sandbox/snaps/js-function-arrow-04-code.png)

![js-function-arrow example 4 result](../code_sandbox/snaps/js-function-arrow-04-result.png)

- [x] **Outcome:** text is **"Hello World!"**.

<a id="js-function-arrow-example-05"></a>

### **Example 5: square (x) => with parentheses**

- [x] One parameter **may** keep the parentheses.

Sandbox: `code_sandbox/js-function-arrow/square-parens.html`

```javascript
const square = (x) => x * x;
let z = square(5);
```

![js-function-arrow example 5 source](../code_sandbox/snaps/js-function-arrow-05-code.png)

![js-function-arrow example 5 result](../code_sandbox/snaps/js-function-arrow-05-result.png)

- [x] **Outcome:** z is **25**.

<a id="js-function-arrow-example-06"></a>

### **Example 6: square x => without parentheses**

- [x] With **exactly one** parameter, parentheses are optional.

Sandbox: `code_sandbox/js-function-arrow/square-no-parens.html`

```javascript
const square = (x) => x * x;
let z = square(5);
```

![js-function-arrow example 6 source](../code_sandbox/snaps/js-function-arrow-06-code.png)

![js-function-arrow example 6 result](../code_sandbox/snaps/js-function-arrow-06-result.png)

- [x] **Outcome:** z is **25**.

<a id="js-function-arrow-example-07"></a>

### **Example 7: hello (val) => one parameter**

- [x] `(val)` is one parameter with parentheses.
- [x] The page repeats this Tryit later; included once.

Sandbox: `code_sandbox/js-function-arrow/hello-val-parens.html`

```javascript
const hello = (val) => "Hello " + val;
let text = hello("World");
```

![js-function-arrow example 7 source](../code_sandbox/snaps/js-function-arrow-07-code.png)

![js-function-arrow example 7 result](../code_sandbox/snaps/js-function-arrow-07-result.png)

- [x] **Outcome:** text is **"Hello World"**.

<a id="js-function-arrow-example-08"></a>

### **Example 8: hello val => one parameter, no parens**

- [x] One parameter: you can skip `()`.
- [x] The page has a stray **this** Tryit with the same code — included once.

Sandbox: `code_sandbox/js-function-arrow/hello-val-no-parens.html`

```javascript
const hello = (val) => "Hello " + val;
let text = hello("World");
```

![js-function-arrow example 8 source](../code_sandbox/snaps/js-function-arrow-08-code.png)

![js-function-arrow example 8 result](../code_sandbox/snaps/js-function-arrow-08-result.png)

- [x] **Outcome:** text is **"Hello World"**.

<a id="js-function-arrow-example-09"></a>

### **Example 9: Braces without return → undefined**

- [x] `{ x * y }` is a **block**, not an implicit return — result is **undefined**.
- [x] `=> return x * y` is a **SyntaxError** (`return` is a statement, not an expression).
- [x] `{ return x * y }` works. Keep `return` when you use `{ }`.

Sandbox: `code_sandbox/js-function-arrow/braces-return-variants.html`

```javascript
const a = (x, y) => {
  x * y;
};
// const b = (x, y) => return x * y;  // SyntaxError
const c = (x, y) => {
  return x * y;
};
```

![js-function-arrow example 9 source](../code_sandbox/snaps/js-function-arrow-09-code.png)

![js-function-arrow example 9 result](../code_sandbox/snaps/js-function-arrow-09-result.png)

- [x] **Outcome:** `{ x * y }` → **undefined**. `=> return` → **SyntaxError**. `{ return x * y }` → **20**.

<a id="js-function-arrow-example-10"></a>

### **Example 10: Calling an arrow before it is defined**

- [x] Arrows are **expressions**, not declarations. They are **not hoisted**.
- [x] `hello()` before `const hello = () => ...` throws **ReferenceError**.

Sandbox: `code_sandbox/js-function-arrow/call-before-define.html`

```javascript
hello(); // Error
const hello = () => "Hello";
```

![js-function-arrow example 10 source](../code_sandbox/snaps/js-function-arrow-10-code.png)

![js-function-arrow example 10 result](../code_sandbox/snaps/js-function-arrow-10-result.png)

- [x] **Outcome:** **ReferenceError** — cannot access `hello` before initialization. After the `const`, `hello()` is **Hello**.

<a id="js-function-arrow-example-11"></a>

### **Example 11: Method this with function() → "John"**

- [x] A regular method has its own **`this`**: the object that owns the call.
- [x] `person.greet()` sets `this` to `person`.

Sandbox: `code_sandbox/js-function-arrow/method-this-function.html`

```javascript
const person = {
  name: "John",
  greet: function () {
    return this.name;
  },
};
let text = person.greet();
```

![js-function-arrow example 11 source](../code_sandbox/snaps/js-function-arrow-11-code.png)

![js-function-arrow example 11 result](../code_sandbox/snaps/js-function-arrow-11-result.png)

- [x] **Outcome:** text is **"John"**.

<a id="js-function-arrow-example-12"></a>

### **Example 12: Method this with arrow → not John**

- [x] Arrow functions do **not** have their own `this`.
- [x] They inherit `this` from the surrounding scope (here, the window/global), so `this.name` is **not** `"John"`.

Sandbox: `code_sandbox/js-function-arrow/method-this-arrow.html`

```javascript
const person = {
  name: "John",
  greet: () => {
    return this.name;
  },
};
let text = person.greet();
```

![js-function-arrow example 12 source](../code_sandbox/snaps/js-function-arrow-12-code.png)

![js-function-arrow example 12 result](../code_sandbox/snaps/js-function-arrow-12-result.png)

- [x] **Outcome:** `person.greet()` is **not** `"John"` (empty string or undefined on the global `this`). Do not use arrows as methods.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-function-arrow/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `(a, b) => a * b` for 4 and 5?

<details>
<summary>Answer</summary>

- [x] **20**.

</details>

### Question 2: What is the longer equivalent?

<details>
<summary>Answer</summary>

- [x] `const multiply = function(a, b) { return a * b; }`.

</details>

### Question 3: What is `const hello = () => "Hello World!"`?

<details>
<summary>Answer</summary>

- [x] **"Hello World!"** when called.
- [x] Empty `()` is required with no parameters.

</details>

### Question 4: Are `(x) => x * x` and `x => x * x` the same?

<details>
<summary>Answer</summary>

- [x] **Yes** for one parameter. `square(5)` is **25**.

</details>

### Question 5: What is `(val) => "Hello " + val` with `"World"`?

<details>
<summary>Answer</summary>

- [x] **"Hello World"**.

</details>

### Question 6: What does `{ x * y }` return?

<details>
<summary>Answer</summary>

- [x] **undefined** — a block with no `return`.

</details>

### Question 7: What does `=> return x * y` do?

<details>
<summary>Answer</summary>

- [x] **SyntaxError** — `return` is not an expression.

</details>

### Question 8: What does `{ return x * y }` return for 4 and 5?

<details>
<summary>Answer</summary>

- [x] **20**.

</details>

### Question 9: Can you call an arrow before its `const` line?

<details>
<summary>Answer</summary>

- [x] **No.** **ReferenceError**.

</details>

### Question 10: What is `this.name` in `greet: function() { return this.name; }` on `{name: "John"}`?

<details>
<summary>Answer</summary>

- [x] **"John"**.

</details>

### Question 11: What is `this.name` if `greet` is an arrow on that object?

<details>
<summary>Answer</summary>

- [x] **Not** `"John"`. The arrow uses surrounding `this` (often the global object).

</details>

### Question 12: When should you not use arrows?

<details>
<summary>Answer</summary>

- [x] As **object methods**, when you need your own `this`, or when you want a hoisted declaration.

</details>

</details>

## Summary

Arrows shorten function expressions. Keep parentheses for 0 or 2+ parameters, use return inside braces, define them before you call them, and do not use them as methods that need this.

## References

- [JS Arrow Function (W3Schools)](https://www.w3schools.com/js/js_arrow_function.asp)
- [MDN: Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [MDN: this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
