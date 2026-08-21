# JS Let

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

**`let`** was added in **ES6 (2015)**. Variables declared with `let` have **block scope**, must be **declared before use**, and **cannot be redeclared** in the same scope. Prefer `let`/`const` over **`var`**.

This section has **4** examples:

- [x] **Example 1:** Block scope with `let` [View](#js-let-example-01)
- [x] **Example 2:** `var` is not block scoped [View](#js-let-example-02)
- [x] **Example 3:** Redeclaring variables [View](#js-let-example-03)
- [x] **Example 4:** Hoisting (`var` vs `let`) [View](#js-let-example-04)

## Detailed Explanation

- [x] **`let` was added in ES6 (2015)** alongside `const`, giving JavaScript **block scope** for the first time (before that there were only **global** and **function** scope).
- [x] **Three key traits of `let`:** it is **block scoped**, it **cannot be redeclared** in the same scope, and it **must be declared before use** (no reading it earlier in the block).
- [x] Inside a **function**, `var`, `let`, and `const` all share **function scope**; the differences below are about **blocks** (`{ }`) and **hoisting**.

<a id="js-let-example-01"></a>

### **Example 1: Block scope with `let`**

- [x] A variable declared with `let` inside `{ }` exists **only inside that block**; the outer variable of the same name is untouched.
- [x] Here the inner `let x = 2;` is a **separate** variable from the outer `let x = 10;`.
- [x] After the block ends, the name `x` refers to the **outer** variable again.

Sandbox: `code_sandbox/js-let/block.html`

```javascript
let x = 10;
// Here x is 10
{
  let x = 2; // a different x, only visible inside { }
  // Here x is 2
}
// Here x is 10 again
```

![js-let example 1 source](../code_sandbox/snaps/js-let-01-code.png)

![js-let example 1 result](../code_sandbox/snaps/js-let-01-result.png)

- [x] **Outcome:** prints `x = 10` before the block, `x = 2` inside, and `x = 10` again after — the inner `let` never leaked out.

<a id="js-let-example-02"></a>

### **Example 2: `var` is not block scoped**

- [x] `var` **ignores blocks**: a `var` declared inside `{ }` is the **same** variable as one outside, so it can be read (and changed) after the block.
- [x] Redeclaring `var x` inside the block just **reassigns** the one outer `x`.
- [x] This "leaking" is the classic `var` bug that `let` was designed to fix.

Sandbox: `code_sandbox/js-let/varleak.html`

```javascript
var x = 10;
// Here x is 10
{
  var x = 2; // SAME x -> changes the outer variable
  // Here x is 2
}
// Here x is 2  (var leaked out of the block!)
```

![js-let example 2 source](../code_sandbox/snaps/js-let-02-code.png)

![js-let example 2 result](../code_sandbox/snaps/js-let-02-result.png)

- [x] **Outcome:** after the block, `x = 2` — the `var` assignment inside the block **overwrote** the outer value, unlike `let` in Example 1.

<a id="js-let-example-03"></a>

### **Example 3: Redeclaring variables**

- [x] **`var` can be redeclared** in the same scope (`var x = 2; var x = 3;` is legal and just reassigns).
- [x] **`let` cannot be redeclared** in the **same** scope — `let y = 2; let y = 3;` is a **`SyntaxError`**.
- [x] But re-using the name `let y` **inside a new block** is fine, because a block is a **new scope**.

Sandbox: `code_sandbox/js-let/redeclare.html`

```javascript
var x = 2;
var x = 3; // var: redeclaration in the same scope is allowed

let y = 2;
// let y = 3;   // SAME scope -> SyntaxError (not allowed)
{
  let y = 3; // OK: a new block is a new scope
}
```

![js-let example 3 source](../code_sandbox/snaps/js-let-03-code.png)

![js-let example 3 result](../code_sandbox/snaps/js-let-03-result.png)

- [x] **Outcome:** `var x` becomes **3**, the outer `let y` stays **2**, and the block's own `let y` is **3** — same‑scope `let` redeclaration is rejected as a `SyntaxError`.

<a id="js-let-example-04"></a>

### **Example 4: Hoisting (`var` vs `let`)**

- [x] **`var` is hoisted and initialized to `undefined`**, so using it _before_ its line does not error — you just read `undefined`.
- [x] **`let` is hoisted but NOT initialized**; the span before its declaration is the **temporal dead zone**, and reading it there throws a **`ReferenceError`**.
- [x] The demo uses `try/catch` so the `ReferenceError` can be caught and shown instead of stopping the script.

Sandbox: `code_sandbox/js-let/hoisting.html`

```javascript
// var is hoisted and auto-initialized to undefined
typeof x; // "undefined" (used before its line, no error)
var x = 5;

// let is hoisted but NOT initialized (temporal dead zone)
try {
  y; // ReferenceError: used before its line
} catch (e) {
  // e.name === "ReferenceError"
}
let y = 5;
```

![js-let example 4 source](../code_sandbox/snaps/js-let-04-code.png)

![js-let example 4 result](../code_sandbox/snaps/js-let-04-result.png)

- [x] **Outcome:** `typeof x` before its line is **undefined** (no error), while touching `y` before its line raises a **ReferenceError** — proof of the temporal dead zone.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-let/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: When was `let` introduced?

<details>
<summary>Answer</summary>

- [x] **ES6 (2015)**.

</details>

### Question 2: What scope does `let` have?

<details>
<summary>Answer</summary>

- [x] **Block scope**.
- [x] A `let` inside `{ }` cannot be used outside.

</details>

### Question 3: Can you redeclare a `let` variable in the same scope?

<details>
<summary>Answer</summary>

- [x] **No.**

</details>

### Question 4: Does `var` have block scope?

<details>
<summary>Answer</summary>

- [x] **No.** `var` inside a block can still be used **outside**.

</details>

### Question 5: What happens if you use `let` before it is declared?

<details>
<summary>Answer</summary>

- [x] A **`ReferenceError`**.
- [x] `let` is hoisted but **not initialized** (temporal dead zone).

</details>

### Question 6: What happens if you use a `var` before it is declared?

<details>
<summary>Answer</summary>

- [x] No error — you read **`undefined`**.
- [x] `var` is hoisted **and** auto‑initialized to `undefined`.

</details>

### Question 7: Can you redeclare a `var` in the same scope?

<details>
<summary>Answer</summary>

- [x] **Yes.** `var x = 2; var x = 3;` is allowed and just reassigns.

</details>

### Question 8: Is it OK to reuse a `let` name inside a nested block?

<details>
<summary>Answer</summary>

- [x] **Yes.** A block is a **new scope**, so a new `let` of the same name is fine there.
- [x] It does **not** affect the outer variable.

</details>

### Question 9: What is the "temporal dead zone"?

<details>
<summary>Answer</summary>

- [x] The region from the **start of the block** to the **`let`/`const` declaration** where the variable exists but is **not initialized**.
- [x] Accessing it there throws a **`ReferenceError`**.

</details>

### Question 10: Why prefer `let`/`const` over `var`?

<details>
<summary>Answer</summary>

- [x] **Block scope** prevents variables leaking out of `{ }`.
- [x] **No accidental redeclaration** in the same scope.
- [x] The **temporal dead zone** catches "used before declared" bugs early.

</details>

</details>

## Summary

**`let`** (ES6) is **block-scoped**, cannot be **redeclared** in the same scope, and cannot be used before its declaration (`ReferenceError`, the temporal dead zone). **`var`** leaks out of blocks, can be redeclared, and reads as `undefined` before its line. Modern code prefers `let`/`const` and avoids `var`.

## References

- [JS Let (W3Schools)](https://www.w3schools.com/js/js_let.asp)
- [MDN: let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
- [MDN: JavaScript Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
