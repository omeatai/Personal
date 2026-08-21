# JS Function Quiz

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Nine quiz questions from the functions track, each run as a live example. The sandbox prints the computed result and the correct letter so you can check yourself against the same snippets the tutorial used.

This section has **9** examples:

- [x] **Example 1:** Q1: What is returned in text? → B Hello World [View](#js-function-quiz-example-01)
- [x] **Example 2:** Q2: Which line calls the function? → C let y = test() [View](#js-function-quiz-example-02)
- [x] **Example 3:** Q3: What are a and b? → B Parameters [View](#js-function-quiz-example-03)
- [x] **Example 4:** Q4: What is x? → C 50 [View](#js-function-quiz-example-04)
- [x] **Example 5:** Q5: No return statement → C undefined [View](#js-function-quiz-example-05)
- [x] **Example 6:** Q6: Called before defined? → A Function declaration [View](#js-function-quiz-example-06)
- [x] **Example 7:** Q7: Which arrow is correct? → C const add = (a, b) => a + b [View](#js-function-quiz-example-07)
- [x] **Example 8:** Q8: What does this refer to in a method? → C The object that owns the method [View](#js-function-quiz-example-08)
- [x] **Example 9:** Q9: Why does the arrow method fail? → B Arrow functions do not have their own this [View](#js-function-quiz-example-09)

## Detailed Explanation

- [x] `()` **calls** a function; without `()` you have a **reference**.
- [x] **Parameters** are names; no `return` means **undefined**.
- [x] Only **declarations** hoist. Correct arrow: `(a, b) => a + b`.
- [x] In a method, `this` is the **owner object**. Arrows do **not** have their own `this`.

<a id="js-function-quiz-example-01"></a>

### **Example 1: Q1: What is returned in text? → B Hello World**

- [x] **Answer B.** `sayHello()` runs and returns the string.
- [x] A would be the function itself (`sayHello` without `()`). C would mean no return.

Sandbox: `code_sandbox/js-function-quiz/q1-hello-world.html`

```javascript
function sayHello() {
  return "Hello World";
}
let text = sayHello();
```

![js-function-quiz example 1 source](../code_sandbox/snaps/js-function-quiz-01-code.png)

![js-function-quiz example 1 result](../code_sandbox/snaps/js-function-quiz-01-result.png)

- [x] **Outcome:** text is **"Hello World"**. Correct choice: **B**.

<a id="js-function-quiz-example-02"></a>

### **Example 2: Q2: Which line calls the function? → C let y = test()**

- [x] **Answer C.** Parentheses **execute** the function.
- [x] `let x = test` only copies the function reference.

Sandbox: `code_sandbox/js-function-quiz/q2-which-line-calls.html`

```javascript
function test() {
  return 5;
}
let x = test;
let y = test();
```

![js-function-quiz example 2 source](../code_sandbox/snaps/js-function-quiz-02-code.png)

![js-function-quiz example 2 result](../code_sandbox/snaps/js-function-quiz-02-result.png)

- [x] **Outcome:** `x` is a **function**; `y` is **5**. Correct choice: **C**.

<a id="js-function-quiz-example-03"></a>

### **Example 3: Q3: What are a and b? → B Parameters**

- [x] **Answer B.** Parameters are the **names** in the definition.
- [x] Arguments would be the values in a call such as `multiply(4, 5)`.

Sandbox: `code_sandbox/js-function-quiz/q3-parameters.html`

```javascript
function multiply(a, b) {
  return a * b;
}
let result = multiply(4, 5);
```

![js-function-quiz example 3 source](../code_sandbox/snaps/js-function-quiz-03-code.png)

![js-function-quiz example 3 result](../code_sandbox/snaps/js-function-quiz-03-result.png)

- [x] **Outcome:** a and b are **parameters**. Correct choice: **B**.

<a id="js-function-quiz-example-04"></a>

### **Example 4: Q4: What is x? → C 50**

- [x] **Answer C.** `add(2, 3)` returns **5**, then `5 * 10` is **50**.

Sandbox: `code_sandbox/js-function-quiz/q4-fifty.html`

```javascript
function add(a, b) {
  return a + b;
}
let x = add(2, 3) * 10;
```

![js-function-quiz example 4 source](../code_sandbox/snaps/js-function-quiz-04-code.png)

![js-function-quiz example 4 result](../code_sandbox/snaps/js-function-quiz-04-result.png)

- [x] **Outcome:** x is **50**. Correct choice: **C**.

<a id="js-function-quiz-example-05"></a>

### **Example 5: Q5: No return statement → C undefined**

- [x] **Answer C.** A function without `return` yields **undefined**.
- [x] Not `null`, not `false`.

Sandbox: `code_sandbox/js-function-quiz/q5-undefined.html`

```javascript
function multiply(a, b) {
  let x = a * b;
}
let result = multiply(4, 3);
```

![js-function-quiz example 5 source](../code_sandbox/snaps/js-function-quiz-05-code.png)

![js-function-quiz example 5 result](../code_sandbox/snaps/js-function-quiz-05-result.png)

- [x] **Outcome:** result is **undefined**. Correct choice: **C**.

<a id="js-function-quiz-example-06"></a>

### **Example 6: Q6: Called before defined? → A Function declaration**

- [x] **Answer A.** Only **function declarations** are hoisted as callable functions.
- [x] Expressions and arrows cannot be called before their `const`/`let` line.

Sandbox: `code_sandbox/js-function-quiz/q6-declaration-hoisted.html`

```javascript
let fromDecl = add(2, 3);
function add(a, b) {
  return a + b;
}
```

![js-function-quiz example 6 source](../code_sandbox/snaps/js-function-quiz-06-code.png)

![js-function-quiz example 6 result](../code_sandbox/snaps/js-function-quiz-06-result.png)

- [x] **Outcome:** Declaration call works: **5**. Expression call before `const` is **ReferenceError**. Correct choice: **A**.

<a id="js-function-quiz-example-07"></a>

### **Example 7: Q7: Which arrow is correct? → C const add = (a, b) => a + b**

- [x] **Answer C.** A single expression after `=>` is the implicit return.
- [x] A is a SyntaxError (`return` in an expression body). B is missing parentheses around two params.

Sandbox: `code_sandbox/js-function-quiz/q7-arrow-correct.html`

```javascript
const add = (a, b) => a + b;
let x = add(2, 3);
```

![js-function-quiz example 7 source](../code_sandbox/snaps/js-function-quiz-07-code.png)

![js-function-quiz example 7 result](../code_sandbox/snaps/js-function-quiz-07-result.png)

- [x] **Outcome:** C runs: **5**. A is **SyntaxError**. B is **SyntaxError**. Correct choice: **C**.

<a id="js-function-quiz-example-08"></a>

### **Example 8: Q8: What does this refer to in a method? → C The object that owns the method**

- [x] **Answer C.** In `person.getName`, `this` is **person**.
- [x] Not the function itself, and not (for a method call) the global object.

Sandbox: `code_sandbox/js-function-quiz/q8-this-owner.html`

```javascript
const person = {
  name: "John",
  getName: function () {
    return this.name;
  },
};
let text = person.getName();
```

![js-function-quiz example 8 source](../code_sandbox/snaps/js-function-quiz-08-code.png)

![js-function-quiz example 8 result](../code_sandbox/snaps/js-function-quiz-08-result.png)

- [x] **Outcome:** text is **"John"**. Correct choice: **C**.

<a id="js-function-quiz-example-09"></a>

### **Example 9: Q9: Why does the arrow method fail? → B Arrow functions do not have their own this**

- [x] **Answer B.** Arrows inherit `this` from the surrounding scope.
- [x] They **can** return values, and the object syntax is fine.

Sandbox: `code_sandbox/js-function-quiz/q9-arrow-this.html`

```javascript
const person = {
  name: "John",
  greet: () => this.name,
};
let text = person.greet();
```

![js-function-quiz example 9 source](../code_sandbox/snaps/js-function-quiz-09-code.png)

![js-function-quiz example 9 result](../code_sandbox/snaps/js-function-quiz-09-result.png)

- [x] **Outcome:** `greet()` is **not** `"John"`. Correct choice: **B**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-function-quiz/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Q1: `let text = sayHello()` — what is text?

<details>
<summary>Answer</summary>

- [x] **B. Hello World**.
- [x] The function returns that string.

</details>

### Question 2: Q2: Which line calls `test`?

<details>
<summary>Answer</summary>

- [x] **C. `let y = test()`**.
- [x] `let x = test` only copies the function.

</details>

### Question 3: Q3: In `function multiply(a, b)`, what are a and b?

<details>
<summary>Answer</summary>

- [x] **B. Parameters**.

</details>

### Question 4: Q4: `x = add(2, 3) * 10` — what is x?

<details>
<summary>Answer</summary>

- [x] **C. 50**.
- [x] add returns 5, then 5 × 10.

</details>

### Question 5: Q5: No return statement — what is returned?

<details>
<summary>Answer</summary>

- [x] **C. undefined**.

</details>

### Question 6: Q6: Which kind can be called before it is defined?

<details>
<summary>Answer</summary>

- [x] **A. Function declaration**.
- [x] Expressions and arrows are not hoisted that way.

</details>

### Question 7: Q7: Which arrow is correct?

<details>
<summary>Answer</summary>

- [x] **C. `const add = (a, b) => a + b`**.
- [x] A is a SyntaxError; B is missing parentheses around two params.

</details>

### Question 8: Q8: What does `this` refer to in `person.getName`?

<details>
<summary>Answer</summary>

- [x] **C. The object that owns the method**.
- [x] `getName()` returns **John**.

</details>

### Question 9: Q9: Why does `greet: () => this.name` fail?

<details>
<summary>Answer</summary>

- [x] **B. Arrow functions do not have their own this**.
- [x] They inherit `this` from the surrounding scope.

</details>

### Question 10: What is `typeof` of `let x = test`?

<details>
<summary>Answer</summary>

- [x] **"function"**.

</details>

</details>

## Summary

The quiz answers are B, C, B, C, C, A, C, C, B. Calling needs parentheses, parameters are names, missing return is undefined, declarations hoist, the short arrow is `(a, b) => a + b`, and this in a method is the owner — arrows do not get their own this.

## References

- [JS Function Quiz (W3Schools)](https://www.w3schools.com/js/js_function_quiz.asp)
- [MDN: Functions guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [MDN: Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
