# JS Strict Mode

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Strict mode turns sloppy mistakes into errors. Place use strict at the very beginning of a script (this sandbox file) or a function. Undeclared assignments, duplicate parameters, with, octal literals, binding the names eval or arguments, and delete on a variable name are all rejected. Some of those are SyntaxErrors at parse time, so this section compiles them with new Function in order to catch and print the error. A function called without an owner has this equal to undefined. The W3Schools undeclared-variable Tryit appears twice; it is shown once.

This section has **19** examples:

- [x] **Example 1:** "use strict"; x = 3.14 — undeclared variable [View](#js-strict-mode-example-01)
- [x] **Example 2:** Global strict: undeclared y inside a function [View](#js-strict-mode-example-02)
- [x] **Example 3:** Local strict in a function; outer assignment OK [View](#js-strict-mode-example-03)
- [x] **Example 4:** Undeclared object x = {p1, p2} [View](#js-strict-mode-example-04)
- [x] **Example 5:** delete x (let x) — not allowed [View](#js-strict-mode-example-05)
- [x] **Example 6:** delete function — not allowed [View](#js-strict-mode-example-06)
- [x] **Example 7:** Duplicate parameter names — SyntaxError [View](#js-strict-mode-example-07)
- [x] **Example 8:** Octal literal 010 — SyntaxError [View](#js-strict-mode-example-08)
- [x] **Example 9:** Octal escape "\010" [View](#js-strict-mode-example-09)
- [x] **Example 10:** Write a read-only defineProperty (writable: false) [View](#js-strict-mode-example-10)
- [x] **Example 11:** Write a getter-only property [View](#js-strict-mode-example-11)
- [x] **Example 12:** delete Object.prototype [View](#js-strict-mode-example-12)
- [x] **Example 13:** let eval = 3.14 [View](#js-strict-mode-example-13)
- [x] **Example 14:** let arguments = 3.14 [View](#js-strict-mode-example-14)
- [x] **Example 15:** with (Math) — SyntaxError [View](#js-strict-mode-example-15)
- [x] **Example 16:** eval("x=2") then x — error [View](#js-strict-mode-example-16)
- [x] **Example 17:** eval("var x=2") then x — error in strict [View](#js-strict-mode-example-17)
- [x] **Example 18:** eval("let x=2") then x — error [View](#js-strict-mode-example-18)
- [x] **Example 19:** Strict function this is undefined [View](#js-strict-mode-example-19)

## Detailed Explanation

- [x] `"use strict";` is a **directive**. It must be **first** in a script or function or it is ignored.
- [x] This sandbox script **is** the script — global examples put use strict at the top of that script.
- [x] **ReferenceError / TypeError** can be try/caught in the same script. **SyntaxError** would blank the page, so those snippets run inside **`new Function`**.
- [x] Strict `eval` does not leak `var`/`let` into the caller. Bare-call **`this`** is **undefined**.

<a id="js-strict-mode-example-01"></a>

### **Example 1: "use strict"; x = 3.14 — undeclared variable**

- [x] `"use strict";` at the **start of the script** enables strict mode for this whole file.
- [x] Assigning to an **undeclared** name throws **ReferenceError** (no auto-global).
- [x] The later “Not Allowed” Tryit is the **same** snippet — included once.

Sandbox: `code_sandbox/js-strict-mode/undeclared-x.html`

```javascript
"use strict";
x = 3.14;
```

![js-strict-mode example 1 source](../code_sandbox/snaps/js-strict-mode-01-code.png)

![js-strict-mode example 1 result](../code_sandbox/snaps/js-strict-mode-01-result.png)

- [x] **Outcome:** **ReferenceError** (x is not defined). Strict mode does not create a global `x`.

<a id="js-strict-mode-example-02"></a>

### **Example 2: Global strict: undeclared y inside a function**

- [x] Global strict mode applies **inside functions** in the same script too.
- [x] `y = 3.14` in `myFunction` still throws **ReferenceError**.

Sandbox: `code_sandbox/js-strict-mode/global-strict-in-function.html`

```javascript
"use strict";
myFunction();
function myFunction() {
  y = 3.14;
}
```

![js-strict-mode example 2 source](../code_sandbox/snaps/js-strict-mode-02-code.png)

![js-strict-mode example 2 result](../code_sandbox/snaps/js-strict-mode-02-result.png)

- [x] **Outcome:** Calling `myFunction()` throws **ReferenceError** because `y` is not declared.

<a id="js-strict-mode-example-03"></a>

### **Example 3: Local strict in a function; outer assignment OK**

- [x] `"use strict";` **inside a function** is local — only that function is strict.
- [x] This sandbox script is **not** globally strict, so outer `x = 3.14` is allowed.

Sandbox: `code_sandbox/js-strict-mode/local-strict-only.html`

```javascript
x = 3.14;
myFunction();
function myFunction() {
  "use strict";
  y = 3.14;
}
```

![js-strict-mode example 3 source](../code_sandbox/snaps/js-strict-mode-03-code.png)

![js-strict-mode example 3 result](../code_sandbox/snaps/js-strict-mode-03-result.png)

- [x] **Outcome:** Outer `x` is **3.14**. Inner `y = 3.14` throws **ReferenceError**.

<a id="js-strict-mode-example-04"></a>

### **Example 4: Undeclared object x = {p1, p2}**

- [x] Objects are values assigned to variables — they still need a **declaration**.
- [x] In strict mode, `x = { ... }` without `let`/`var`/`const` throws **ReferenceError**.

Sandbox: `code_sandbox/js-strict-mode/undeclared-object.html`

```javascript
"use strict";
x = { p1: 10, p2: 20 };
```

![js-strict-mode example 4 source](../code_sandbox/snaps/js-strict-mode-04-code.png)

![js-strict-mode example 4 result](../code_sandbox/snaps/js-strict-mode-04-result.png)

- [x] **Outcome:** **ReferenceError** — undeclared `x` (same rule as a number).

<a id="js-strict-mode-example-05"></a>

### **Example 5: delete x (let x) — not allowed**

- [x] `delete` on a **variable** (unqualified identifier) is a **SyntaxError** in strict mode.
- [x] Caught with `new Function` so this page can still render.

Sandbox: `code_sandbox/js-strict-mode/delete-variable.html`

```javascript
"use strict";
let x = 3.14;
delete x;
```

![js-strict-mode example 5 source](../code_sandbox/snaps/js-strict-mode-05-code.png)

![js-strict-mode example 5 result](../code_sandbox/snaps/js-strict-mode-05-result.png)

- [x] **Outcome:** **SyntaxError** — applying `delete` to an unqualified identifier.

<a id="js-strict-mode-example-06"></a>

### **Example 6: delete function — not allowed**

- [x] Deleting a **function declaration** is also a strict **SyntaxError**.

Sandbox: `code_sandbox/js-strict-mode/delete-function.html`

```javascript
"use strict";
function x(p1, p2) {}
delete x;
```

![js-strict-mode example 6 source](../code_sandbox/snaps/js-strict-mode-06-code.png)

![js-strict-mode example 6 result](../code_sandbox/snaps/js-strict-mode-06-result.png)

- [x] **Outcome:** **SyntaxError** — cannot `delete` the function name `x`.

<a id="js-strict-mode-example-07"></a>

### **Example 7: Duplicate parameter names — SyntaxError**

- [x] Strict mode forbids **two parameters with the same name**.
- [x] Parse-time **SyntaxError** via `new Function`.

Sandbox: `code_sandbox/js-strict-mode/duplicate-params.html`

```javascript
"use strict";
function x(p1, p1) {}
```

![js-strict-mode example 7 source](../code_sandbox/snaps/js-strict-mode-07-code.png)

![js-strict-mode example 7 result](../code_sandbox/snaps/js-strict-mode-07-result.png)

- [x] **Outcome:** **SyntaxError** — duplicate parameter name `p1`.

<a id="js-strict-mode-example-08"></a>

### **Example 8: Octal literal 010 — SyntaxError**

- [x] Legacy octal `010` (leading zero) is **forbidden** in strict mode.
- [x] **SyntaxError** at parse time (`new Function`).

Sandbox: `code_sandbox/js-strict-mode/octal-literal.html`

```javascript
"use strict";
let x = 010;
```

![js-strict-mode example 8 source](../code_sandbox/snaps/js-strict-mode-08-code.png)

![js-strict-mode example 8 result](../code_sandbox/snaps/js-strict-mode-08-result.png)

- [x] **Outcome:** **SyntaxError** — octal literals are not allowed in strict mode.

<a id="js-strict-mode-example-09"></a>

### **Example 9: Octal escape "\010"**

- [x] Octal escape sequences like `\010` are not allowed in strict mode.
- [x] **SyntaxError** at parse time.

Sandbox: `code_sandbox/js-strict-mode/octal-escape.html`

```javascript
"use strict";
let x = "\010";
```

![js-strict-mode example 9 source](../code_sandbox/snaps/js-strict-mode-09-code.png)

![js-strict-mode example 9 result](../code_sandbox/snaps/js-strict-mode-09-result.png)

- [x] **Outcome:** **SyntaxError** — octal escape `\010` in a string.

<a id="js-strict-mode-example-10"></a>

### **Example 10: Write a read-only defineProperty (writable: false)**

- [x] In sloppy mode, writing a non-writable property **fails silently**.
- [x] In strict mode it throws **TypeError**.

Sandbox: `code_sandbox/js-strict-mode/write-readonly.html`

```javascript
"use strict";
const obj = {};
Object.defineProperty(obj, "x", { value: 0, writable: false });
obj.x = 3.14;
```

![js-strict-mode example 10 source](../code_sandbox/snaps/js-strict-mode-10-code.png)

![js-strict-mode example 10 result](../code_sandbox/snaps/js-strict-mode-10-result.png)

- [x] **Outcome:** **TypeError** — cannot assign to read-only property `x`.

<a id="js-strict-mode-example-11"></a>

### **Example 11: Write a getter-only property**

- [x] An object with only a **getter** for `x` has no setter.
- [x] Assigning `obj.x = 3.14` throws **TypeError** in strict mode.

Sandbox: `code_sandbox/js-strict-mode/write-getter-only.html`

```javascript
"use strict";
const obj = {
  get x() {
    return 0;
  },
};
obj.x = 3.14;
```

![js-strict-mode example 11 source](../code_sandbox/snaps/js-strict-mode-11-code.png)

![js-strict-mode example 11 result](../code_sandbox/snaps/js-strict-mode-11-result.png)

- [x] **Outcome:** **TypeError** — property `x` has only a getter.

<a id="js-strict-mode-example-12"></a>

### **Example 12: delete Object.prototype**

- [x] `Object.prototype` is **non-configurable**.
- [x] `delete Object.prototype` throws **TypeError** in strict mode.

Sandbox: `code_sandbox/js-strict-mode/delete-object-prototype.html`

```javascript
"use strict";
delete Object.prototype;
```

![js-strict-mode example 12 source](../code_sandbox/snaps/js-strict-mode-12-code.png)

![js-strict-mode example 12 result](../code_sandbox/snaps/js-strict-mode-12-result.png)

- [x] **Outcome:** **TypeError** — cannot delete undeletable `Object.prototype`.

<a id="js-strict-mode-example-13"></a>

### **Example 13: let eval = 3.14**

- [x] `eval` is a **reserved name** in strict mode — you cannot bind it.
- [x] **SyntaxError** via `new Function`.

Sandbox: `code_sandbox/js-strict-mode/let-eval.html`

```javascript
"use strict";
let eval = 3.14;
```

![js-strict-mode example 13 source](../code_sandbox/snaps/js-strict-mode-13-code.png)

![js-strict-mode example 13 result](../code_sandbox/snaps/js-strict-mode-13-result.png)

- [x] **Outcome:** **SyntaxError** — unexpected `eval` in strict mode.

<a id="js-strict-mode-example-14"></a>

### **Example 14: let arguments = 3.14**

- [x] `arguments` is also reserved as a binding name in strict mode.
- [x] **SyntaxError** via `new Function`.

Sandbox: `code_sandbox/js-strict-mode/let-arguments.html`

```javascript
"use strict";
let arguments = 3.14;
```

![js-strict-mode example 14 source](../code_sandbox/snaps/js-strict-mode-14-code.png)

![js-strict-mode example 14 result](../code_sandbox/snaps/js-strict-mode-14-result.png)

- [x] **Outcome:** **SyntaxError** — unexpected `arguments` in strict mode.

<a id="js-strict-mode-example-15"></a>

### **Example 15: with (Math) — SyntaxError**

- [x] The **`with`** statement is forbidden in strict mode.
- [x] **SyntaxError** via `new Function`.

Sandbox: `code_sandbox/js-strict-mode/with-statement.html`

```javascript
"use strict";
with (Math) {
  x = cos(2);
}
```

![js-strict-mode example 15 source](../code_sandbox/snaps/js-strict-mode-15-code.png)

![js-strict-mode example 15 result](../code_sandbox/snaps/js-strict-mode-15-result.png)

- [x] **Outcome:** **SyntaxError** — strict mode code may not include a `with` statement.

<a id="js-strict-mode-example-16"></a>

### **Example 16: eval("x=2") then x — error**

- [x] In strict mode, `eval` does **not** create a variable in the caller’s scope.
- [x] `eval("x = 2")` is an undeclared assignment inside eval → **ReferenceError**.

Sandbox: `code_sandbox/js-strict-mode/eval-assign-x.html`

```javascript
"use strict";
eval("x = 2");
// x is not available here
```

![js-strict-mode example 16 source](../code_sandbox/snaps/js-strict-mode-16-code.png)

![js-strict-mode example 16 result](../code_sandbox/snaps/js-strict-mode-16-result.png)

- [x] **Outcome:** **ReferenceError** — `x` is not created in this scope (and the eval assignment itself fails).

<a id="js-strict-mode-example-17"></a>

### **Example 17: eval("var x=2") then x — error in strict**

- [x] Strict `eval` **does not leak** `var` into the surrounding scope.
- [x] Reading `x` afterward is **ReferenceError**.

Sandbox: `code_sandbox/js-strict-mode/eval-var-x.html`

```javascript
"use strict";
eval("var x = 2");
// x is not available here
```

![js-strict-mode example 17 source](../code_sandbox/snaps/js-strict-mode-17-code.png)

![js-strict-mode example 17 result](../code_sandbox/snaps/js-strict-mode-17-result.png)

- [x] **Outcome:** **ReferenceError** when reading `x` after `eval("var x = 2")` in strict mode.

<a id="js-strict-mode-example-18"></a>

### **Example 18: eval("let x=2") then x — error**

- [x] `let` inside `eval` is scoped to the eval itself (the page Tryit does not even need use strict).
- [x] Outer `x` is still **ReferenceError**.

Sandbox: `code_sandbox/js-strict-mode/eval-let-x.html`

```javascript
eval("let x = 2");
// x is not available here
```

![js-strict-mode example 18 source](../code_sandbox/snaps/js-strict-mode-18-code.png)

![js-strict-mode example 18 result](../code_sandbox/snaps/js-strict-mode-18-result.png)

- [x] **Outcome:** **ReferenceError** — `let` in eval does not create an outer `x`.

<a id="js-strict-mode-example-19"></a>

### **Example 19: Strict function this is undefined**

- [x] A **bare** function call in strict mode sets `this` to **undefined** (not `window`).
- [x] In sloppy mode the same call would use the global object.

Sandbox: `code_sandbox/js-strict-mode/strict-this-undefined.html`

```javascript
"use strict";
function myFunction() {
  return this;
}
myFunction();
```

![js-strict-mode example 19 source](../code_sandbox/snaps/js-strict-mode-19-code.png)

![js-strict-mode example 19 result](../code_sandbox/snaps/js-strict-mode-19-result.png)

- [x] **Outcome:** `myFunction()` returns **undefined**. `this === undefined` is **true**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-strict-mode/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Where must `"use strict";` go?

<details>
<summary>Answer</summary>

- [x] The **first** statement of a **script** or a **function**.

</details>

### Question 2: What does `x = 3.14` do in strict mode?

<details>
<summary>Answer</summary>

- [x] **ReferenceError** — x was never declared.

</details>

### Question 3: If only the function has `"use strict"`, is outer `x = 3.14` OK?

<details>
<summary>Answer</summary>

- [x] **Yes** (sloppy outer script). Inner undeclared `y` still errors.

</details>

### Question 4: Why skip a second undeclared-`x` Tryit?

<details>
<summary>Answer</summary>

- [x] It is an **exact duplicate** of the first “Not Allowed” example.

</details>

### Question 5: What error is `delete x` on a `let` in strict mode?

<details>
<summary>Answer</summary>

- [x] **SyntaxError** (unqualified identifier). Caught with `new Function`.

</details>

### Question 6: Duplicate parameter names?

<details>
<summary>Answer</summary>

- [x] **SyntaxError** in strict mode.

</details>

### Question 7: What about `let x = 010` or `"\010"`?

<details>
<summary>Answer</summary>

- [x] **SyntaxError** — octal literals and octal escapes are banned.

</details>

### Question 8: Writing a `writable: false` property?

<details>
<summary>Answer</summary>

- [x] **TypeError** in strict mode (silent fail in sloppy mode).

</details>

### Question 9: `delete Object.prototype`?

<details>
<summary>Answer</summary>

- [x] **TypeError** — the property is undeletable.

</details>

### Question 10: `let eval` or `let arguments`?

<details>
<summary>Answer</summary>

- [x] **SyntaxError** — those names are reserved in strict mode.

</details>

### Question 11: Is `with` allowed?

<details>
<summary>Answer</summary>

- [x] **No.** **SyntaxError**.

</details>

### Question 12: Does `eval("var x = 2")` create an outer `x` in strict mode?

<details>
<summary>Answer</summary>

- [x] **No.** Reading `x` is **ReferenceError**.

</details>

### Question 13: What is `this` in a strict function called as `myFunction()`?

<details>
<summary>Answer</summary>

- [x] **undefined** (not `window`).

</details>

</details>

## Summary

Put use strict first. Undeclared names, with, octals, duplicate parameters, and delete-on-variable become errors. Parse-time SyntaxErrors are demonstrated with new Function so the sandbox page can still load. Strict this on a bare call is undefined.

## References

- [JS Strict Mode (W3Schools)](https://www.w3schools.com/js/js_strict.asp)
- [MDN: Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
