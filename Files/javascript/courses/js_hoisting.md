# JS Hoisting

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Hoisting is the engine treating declarations as if they exist at the top of the current scope. var can be assigned before its line and still work. let and const are hoisted too but stay uninitialized in a temporal dead zone, so using them early is a ReferenceError. A const with no initializer is a SyntaxError at parse time, which is why a raw script tag would not run at all. Only declarations hoist, not the = value. Declare at the top of each scope.

This section has **7** examples:

- [x] **Example 1:** x = 5 then var x — displays 5 [View](#js-hoisting-example-01)
- [x] **Example 2:** var x then x = 5 — same result 5 [View](#js-hoisting-example-02)
- [x] **Example 3:** carName = Volvo then let carName — ReferenceError (TDZ) [View](#js-hoisting-example-03)
- [x] **Example 4:** carName = Volvo then const carName — SyntaxError [View](#js-hoisting-example-04)
- [x] **Example 5:** var x = 5; var y = 7 — show 5 7 [View](#js-hoisting-example-05)
- [x] **Example 6:** use y before var y = 7 — y is undefined [View](#js-hoisting-example-06)
- [x] **Example 7:** Equivalent: var y; display; y = 7 [View](#js-hoisting-example-07)

## Detailed Explanation

- [x] **Declarations** hoist; **initializations** do not.
- [x] `var` is hoisted and set to **undefined** until its assignment runs.
- [x] `let` / `const` hoist into the **TDZ**. Early use → **ReferenceError**.
- [x] `const name;` (no initializer) is a **SyntaxError**. That fails **parse** of a whole `<script>`. This section catches it with **`new Function`**.
- [x] A `const` **with** an initializer used early is **ReferenceError** (TDZ), same as `let` — that is the engine; the W3Schools const Tryit is the missing-initializer SyntaxError.
- [x] Declare variables at the **top** of every scope. Strict mode (next chapter) forbids undeclared names.

<a id="js-hoisting-example-01"></a>

### **Example 1: x = 5 then var x — displays 5**

- [x] **Hoisting** moves `var` **declarations** to the top of the scope.
- [x] `x = 5` then `var x` behaves like `var x; x = 5`.

Sandbox: `code_sandbox/js-hoisting/assign-then-var.html`

```javascript
x = 5;
var x;
```

![js-hoisting example 1 source](../code_sandbox/snaps/js-hoisting-01-code.png)

![js-hoisting example 1 result](../code_sandbox/snaps/js-hoisting-01-result.png)

- [x] **Outcome:** x is **5**. The declaration was hoisted; the assignment ran first in source order.

<a id="js-hoisting-example-02"></a>

### **Example 2: var x then x = 5 — same result 5**

- [x] Declaring first, then assigning, is the **readable** form of the same idea.
- [x] Example 1 and Example 2 print the **same** value.

Sandbox: `code_sandbox/js-hoisting/var-then-assign.html`

```javascript
var x;
x = 5;
```

![js-hoisting example 2 source](../code_sandbox/snaps/js-hoisting-02-code.png)

![js-hoisting example 2 result](../code_sandbox/snaps/js-hoisting-02-result.png)

- [x] **Outcome:** x is **5** — same result as assigning before `var x`.

<a id="js-hoisting-example-03"></a>

### **Example 3: carName = Volvo then let carName — ReferenceError (TDZ)**

- [x] `let` is hoisted but **not initialized**.
- [x] Using it before the `let` line is the **temporal dead zone** → **ReferenceError**.

Sandbox: `code_sandbox/js-hoisting/let-tdz.html`

```javascript
carName = "Volvo";
let carName;
```

![js-hoisting example 3 source](../code_sandbox/snaps/js-hoisting-03-code.png)

![js-hoisting example 3 result](../code_sandbox/snaps/js-hoisting-03-result.png)

- [x] **Outcome:** **ReferenceError** — cannot access `carName` before initialization (TDZ).

<a id="js-hoisting-example-04"></a>

### **Example 4: carName = Volvo then const carName — SyntaxError**

- [x] This snippet is a **parse-time SyntaxError**: `const` **must** have an initializer (`const carName;` is illegal).
- [x] W3Schools says the page “will not run.” A `<script>` with this source **fails to parse**, so nothing on that page runs.
- [x] If it were `const carName = "Volvo"` after an earlier use, the engine would throw **ReferenceError** (TDZ), like `let` — not SyntaxError.
- [x] This sandbox compiles the snippet with **`new Function(...)`** at **runtime** so the error can be caught and shown.

Sandbox: `code_sandbox/js-hoisting/const-syntax-error.html`

```javascript
carName = "Volvo";
const carName;
```

![js-hoisting example 4 source](../code_sandbox/snaps/js-hoisting-04-code.png)

![js-hoisting example 4 result](../code_sandbox/snaps/js-hoisting-04-result.png)

- [x] **Outcome:** **SyntaxError** (missing initializer in const declaration), caught via `new Function`. A raw script tag would not load.

<a id="js-hoisting-example-05"></a>

### **Example 5: var x = 5; var y = 7 — show 5 7**

- [x] **Initializations** are **not** hoisted — only declarations.
- [x] When both `var` lines run before you read them, you get both values.

Sandbox: `code_sandbox/js-hoisting/both-initialized.html`

```javascript
var x = 5;
var y = 7;
let text = x + " " + y;
```

![js-hoisting example 5 source](../code_sandbox/snaps/js-hoisting-05-code.png)

![js-hoisting example 5 result](../code_sandbox/snaps/js-hoisting-05-result.png)

- [x] **Outcome:** text is **"5 7"**.

<a id="js-hoisting-example-06"></a>

### **Example 6: use y before var y = 7 — y is undefined**

- [x] `var y` is hoisted, so `y` **exists** before that line.
- [x] The **`= 7`** is not hoisted, so `y` is **undefined** when first read.

Sandbox: `code_sandbox/js-hoisting/y-used-before-init.html`

```javascript
var x = 5;
let text = x + " " + y;
var y = 7;
```

![js-hoisting example 6 source](../code_sandbox/snaps/js-hoisting-06-code.png)

![js-hoisting example 6 result](../code_sandbox/snaps/js-hoisting-06-result.png)

- [x] **Outcome:** text is **"5 undefined"**. After the init line, y is **7**.

<a id="js-hoisting-example-07"></a>

### **Example 7: Equivalent: var y; display; y = 7**

- [x] The previous example is the same as declaring `y` first, reading it, then assigning.
- [x] Always **declare at the top** of the scope so hoisting cannot surprise you.

Sandbox: `code_sandbox/js-hoisting/equivalent-var-y.html`

```javascript
var x = 5;
var y;
let text = x + " " + y;
y = 7;
```

![js-hoisting example 7 source](../code_sandbox/snaps/js-hoisting-07-code.png)

![js-hoisting example 7 result](../code_sandbox/snaps/js-hoisting-07-result.png)

- [x] **Outcome:** text is **"5 undefined"**, then y becomes **7**. Same as Example 6.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-hoisting/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is hoisting?

<details>
<summary>Answer</summary>

- [x] Declarations are treated as existing at the **top** of the current scope (script or function).

</details>

### Question 2: Are initializations hoisted?

<details>
<summary>Answer</summary>

- [x] **No.** Only the declaration. `= 7` stays where you wrote it.

</details>

### Question 3: What is `x` after `x = 5; var x;`?

<details>
<summary>Answer</summary>

- [x] **5** — same as `var x; x = 5`.

</details>

### Question 4: What is `carName = "Volvo"; let carName`?

<details>
<summary>Answer</summary>

- [x] **ReferenceError** (temporal dead zone).

</details>

### Question 5: What is `carName = "Volvo"; const carName;`?

<details>
<summary>Answer</summary>

- [x] **SyntaxError** — `const` requires an initializer.
- [x] A `<script>` containing that source **does not parse**, so the page would show nothing.
- [x] This sandbox uses **`new Function`** to compile it at runtime and **catch** the error.

</details>

### Question 6: If the const line were `const carName = "Volvo"` after an early assignment, what error?

<details>
<summary>Answer</summary>

- [x] **ReferenceError** (TDZ), like `let` — not SyntaxError.

</details>

### Question 7: What is `x + " " + y` when `var x = 5` then display then `var y = 7`?

<details>
<summary>Answer</summary>

- [x] **`"5 undefined"`**.

</details>

### Question 8: Why is y undefined there?

<details>
<summary>Answer</summary>

- [x] `var y` was **declared** (hoisted) but **not yet assigned** 7.

</details>

### Question 9: What is the equivalent rewrite?

<details>
<summary>Answer</summary>

- [x] `var y;` then display, then `y = 7`.

</details>

### Question 10: Should you rely on hoisting in new code?

<details>
<summary>Answer</summary>

- [x] **No.** Declare at the **top** of the scope so the source matches the engine.

</details>

### Question 11: Does strict mode allow using a name that was never declared?

<details>
<summary>Answer</summary>

- [x] **No.** That is the next chapter.

</details>

</details>

## Summary

var declarations rise to the top as undefined; let and const rise into a dead zone; a const with no initializer never even parses. Write declarations first so you do not depend on hoisting.

## References

- [JS Hoisting (W3Schools)](https://www.w3schools.com/js/js_hoisting.asp)
- [MDN: Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
- [MDN: Temporal dead zone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)
