# JS Scope

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Scope is where a variable is visible. JavaScript has global scope, function scope, and (since ES6) block scope. Globals can be read from anywhere on the page. Locals exist only inside their function. Block lets and consts stay inside their braces. Undeclared assignment in sloppy mode becomes global; strict mode does not do that. In HTML, var globals hang off window and let globals do not.

This section has **8** examples:

- [x] **Example 1:** Three types of scope [View](#js-scope-example-01)
- [x] **Example 2:** Global let carName used inside a function [View](#js-scope-example-02)
- [x] **Example 3:** Function-local carName — outside is ReferenceError [View](#js-scope-example-03)
- [x] **Example 4:** Block let x = 2 — outside is ReferenceError [View](#js-scope-example-04)
- [x] **Example 5:** Block var x = 2 — still 2 outside (not recommended) [View](#js-scope-example-05)
- [x] **Example 6:** Undeclared assignment is automatically global [View](#js-scope-example-06)
- [x] **Example 7:** var carName belongs to window [View](#js-scope-example-07)
- [x] **Example 8:** let carName does not belong to window [View](#js-scope-example-08)

## Detailed Explanation

- [x] **Three scopes:** global, function, and block (`let` / `const` in `{ }`).
- [x] **Function locals** are created when the call starts and gone when it finishes. Same names can exist in different functions.
- [x] **`var` is not block-scoped** — it leaks out of `{ }`. Prefer `let` / `const`.
- [x] **Automatically global** only in sloppy mode. **Strict mode** undeclared assignment is an error (next chapter).
- [x] HTML global object is **`window`**. Global **`var`** is `window.name`; global **`let` is not**.
- [x] Do **not** create globals unless you mean to — they can clash with `window` properties.

<a id="js-scope-example-01"></a>

### **Example 1: Three types of scope**

- [x] JavaScript has **global**, **function**, and **block** scope.
- [x] Outside any function or `{ }`, `var` / `let` / `const` are all **global**.

Sandbox: `code_sandbox/js-scope/three-scope-types.html`

```javascript
var x = 1; // Global scope
let y = 2; // Global scope
const z = 3; // Global scope
function show() {
  return x + ", " + y + ", " + z;
}
```

![js-scope example 1 source](../code_sandbox/snaps/js-scope-01-code.png)

![js-scope example 1 result](../code_sandbox/snaps/js-scope-01-result.png)

- [x] **Outcome:** x, y, and z are **1**, **2**, **3**. `show()` can read all three: **1, 2, 3**.

<a id="js-scope-example-02"></a>

### **Example 2: Global let carName used inside a function**

- [x] A variable declared **outside** a function is **global**.
- [x] Functions on the same page can **read** that global.

Sandbox: `code_sandbox/js-scope/global-let-carname.html`

```javascript
let carName = "Volvo";
function myFunction() {
  return carName;
}
```

![js-scope example 2 source](../code_sandbox/snaps/js-scope-02-code.png)

![js-scope example 2 result](../code_sandbox/snaps/js-scope-02-result.png)

- [x] **Outcome:** Both the outer code and the function see **"Volvo"**.

<a id="js-scope-example-03"></a>

### **Example 3: Function-local carName — outside is ReferenceError**

- [x] A variable declared **inside** a function is **local** (function scope).
- [x] Reading it **outside** throws **ReferenceError**.

Sandbox: `code_sandbox/js-scope/function-local-carname.html`

```javascript
// code here can NOT use carName
function myFunction() {
  let carName = "Volvo";
  return carName; // code here CAN use carName
}
// code here can NOT use carName
```

![js-scope example 3 source](../code_sandbox/snaps/js-scope-03-code.png)

![js-scope example 3 result](../code_sandbox/snaps/js-scope-03-result.png)

- [x] **Outcome:** Inside the function, carName is **"Volvo"**. Outside, reading it throws **ReferenceError**.

<a id="js-scope-example-04"></a>

### **Example 4: Block let x = 2 — outside is ReferenceError**

- [x] `let` (and `const`) inside `{ }` have **block scope**.
- [x] Outside the braces, `x` is not declared — **ReferenceError**.

Sandbox: `code_sandbox/js-scope/block-let-x.html`

```javascript
{
  let x = 2;
}
// x can NOT be used here
```

![js-scope example 4 source](../code_sandbox/snaps/js-scope-04-code.png)

![js-scope example 4 result](../code_sandbox/snaps/js-scope-04-result.png)

- [x] **Outcome:** Inside the block, x is **2**. Outside, reading x throws **ReferenceError**.

<a id="js-scope-example-05"></a>

### **Example 5: Block var x = 2 — still 2 outside (not recommended)**

- [x] `var` does **not** have block scope.
- [x] `var` inside `{ }` **leaks** and can be used after the block. Avoid this.

Sandbox: `code_sandbox/js-scope/block-var-x.html`

```javascript
{
  var x = 2;
}
// x CAN be used here
```

![js-scope example 5 source](../code_sandbox/snaps/js-scope-05-code.png)

![js-scope example 5 result](../code_sandbox/snaps/js-scope-05-result.png)

- [x] **Outcome:** x is **2** outside the block. `var` in a block is **not recommended**.

<a id="js-scope-example-06"></a>

### **Example 6: Undeclared assignment is automatically global**

- [x] In **sloppy** mode, assigning to a name that was never declared creates a **global**.
- [x] In **strict mode**, undeclared assignment is **not** auto-global (see **JS Strict Mode**).

Sandbox: `code_sandbox/js-scope/automatically-global.html`

```javascript
myFunction();
// code here can use carName
function myFunction() {
  carName = "Volvo";
}
```

![js-scope example 6 source](../code_sandbox/snaps/js-scope-06-code.png)

![js-scope example 6 result](../code_sandbox/snaps/js-scope-06-result.png)

- [x] **Outcome:** After the call, outer code can use carName: **"Volvo"**. Do not rely on this.

<a id="js-scope-example-07"></a>

### **Example 7: var carName belongs to window**

- [x] In HTML, the global object is **`window`**.
- [x] A global **`var`** becomes **`window.carName`**. Not recommended.

Sandbox: `code_sandbox/js-scope/var-window-carname.html`

```javascript
var carName = "Volvo";
// code here can use window.carName
```

![js-scope example 7 source](../code_sandbox/snaps/js-scope-07-code.png)

![js-scope example 7 result](../code_sandbox/snaps/js-scope-07-result.png)

- [x] **Outcome:** `carName` and `window.carName` are both **"Volvo"**.

<a id="js-scope-example-08"></a>

### **Example 8: let carName does not belong to window**

- [x] A global **`let`** is **not** a property of `window`.
- [x] `window.carName` is **undefined** even though `carName` holds Volvo.

Sandbox: `code_sandbox/js-scope/let-window-carname.html`

```javascript
let carName = "Volvo";
// code here can NOT use window.carName
```

![js-scope example 8 source](../code_sandbox/snaps/js-scope-08-code.png)

![js-scope example 8 result](../code_sandbox/snaps/js-scope-08-result.png)

- [x] **Outcome:** `carName` is **"Volvo"**. `window.carName` is **undefined**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-scope/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are the three kinds of JavaScript scope?

<details>
<summary>Answer</summary>

- [x] **Global**, **function**, and **block**.

</details>

### Question 2: Can a global `let carName` be used inside a function?

<details>
<summary>Answer</summary>

- [x] **Yes.** Globals are visible everywhere on the page.

</details>

### Question 3: What happens if you read a function-local `carName` outside the function?

<details>
<summary>Answer</summary>

- [x] **ReferenceError**.

</details>

### Question 4: Does `let x = 2` inside `{ }` leak?

<details>
<summary>Answer</summary>

- [x] **No.** Outside is **ReferenceError**.

</details>

### Question 5: Does `var x = 2` inside `{ }` leak?

<details>
<summary>Answer</summary>

- [x] **Yes.** Outside, x is still **2**. Not recommended.

</details>

### Question 6: What is an automatically global variable?

<details>
<summary>Answer</summary>

- [x] An **assignment without a declaration** in sloppy mode.
- [x] It can be used **outside** the function that assigned it.

</details>

### Question 7: Does strict mode still auto-create globals?

<details>
<summary>Answer</summary>

- [x] **No.** Undeclared assignment is an error. Covered in JS Strict Mode.

</details>

### Question 8: Is `window.carName` set by `var carName`?

<details>
<summary>Answer</summary>

- [x] **Yes** (HTML). Not recommended.

</details>

### Question 9: Is `window.carName` set by `let carName`?

<details>
<summary>Answer</summary>

- [x] **No.** `window.carName` is **undefined**.

</details>

### Question 10: When are local variables deleted?

<details>
<summary>Answer</summary>

- [x] When the **function call finishes**.
- [x] Browser globals last until the **tab** closes.

</details>

### Question 11: Do `var`, `let`, and `const` all have function scope inside a function?

<details>
<summary>Answer</summary>

- [x] **Yes.** Inside a function they are all **local** to that function.

</details>

### Question 12: Should you create globals by default?

<details>
<summary>Answer</summary>

- [x] **No.** Only when you intend a page-wide value.

</details>

</details>

## Summary

Pick the smallest scope that works. Use let and const in blocks, keep function data local, and treat undeclared assignment and window-bound var as habits to drop — especially once strict mode is on.

## References

- [JS Scope (W3Schools)](https://www.w3schools.com/js/js_scope.asp)
- [MDN: Scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope)
- [MDN: let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
