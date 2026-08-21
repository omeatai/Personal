# JS Code Blocks

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A code block is a group of statements inside curly braces. Function bodies, if/else branches, and loop bodies are blocks. let and const declared in a block stay in that block. You can also write a standalone pair of braces to give variables a short lifetime without wrapping them in a function.

This section has **6** examples:

- [x] **Example 1:** Function body is a code block [View](#js-code-blocks-example-01)
- [x] **Example 2:** if / else blocks [View](#js-code-blocks-example-02)
- [x] **Example 3:** for loop block [View](#js-code-blocks-example-03)
- [x] **Example 4:** while loop block [View](#js-code-blocks-example-04)
- [x] **Example 5:** { let x = 10 } — x not accessible outside [View](#js-code-blocks-example-05)
- [x] **Example 6:** Standalone block: areal inside, ReferenceError outside [View](#js-code-blocks-example-06)

## Detailed Explanation

- [x] A **block** `{ }` is one unit of statements — required for function bodies, `if`/`else`, `for`, and `while`.
- [x] `let` / `const` in a block are **block-scoped**. They do not leak.
- [x] A **standalone** block is valid: use it to encapsulate a calculation (`areal`) without polluting globals.
- [x] Inside the block you can read the bindings; **outside** they throw **ReferenceError**.

<a id="js-code-blocks-example-01"></a>

### **Example 1: Function body is a code block**

- [x] A **code block** is statements inside curly braces `{ }`.
- [x] A function **body** is always a block.

Sandbox: `code_sandbox/js-code-blocks/function-body-block.html`

```javascript
function myFunction() {
  // This is a code block
  let a = 1;
  let b = 2;
  return a + b;
}
let result = myFunction();
```

![js-code-blocks example 1 source](../code_sandbox/snaps/js-code-blocks-01-code.png)

![js-code-blocks example 1 result](../code_sandbox/snaps/js-code-blocks-01-result.png)

- [x] **Outcome:** The block runs when the function is called. result is **3**.

<a id="js-code-blocks-example-02"></a>

### **Example 2: if / else blocks**

- [x] `if` and `else` each take a **block** of statements.
- [x] This demo runs a **true** branch and a **false** branch so both outputs show.

Sandbox: `code_sandbox/js-code-blocks/if-else-blocks.html`

```javascript
function check(n) {
  if (n > 5) {
    return "if block: " + n + " is greater than 5";
  } else {
    return "else block: " + n + " is not greater than 5";
  }
}
```

![js-code-blocks example 2 source](../code_sandbox/snaps/js-code-blocks-02-code.png)

![js-code-blocks example 2 result](../code_sandbox/snaps/js-code-blocks-02-result.png)

- [x] **Outcome:** `check(10)` uses the **if** block; `check(3)` uses the **else** block.

<a id="js-code-blocks-example-03"></a>

### **Example 3: for loop block**

- [x] The body of a **`for`** loop is a code block.
- [x] `let i` in the loop head is **block-scoped** to that loop.

Sandbox: `code_sandbox/js-code-blocks/for-loop-block.html`

```javascript
let text = "";
for (let i = 0; i < 3; i++) {
  text += i + " ";
}
```

![js-code-blocks example 3 source](../code_sandbox/snaps/js-code-blocks-03-code.png)

![js-code-blocks example 3 result](../code_sandbox/snaps/js-code-blocks-03-result.png)

- [x] **Outcome:** text is **"0 1 2 "** after three iterations.

<a id="js-code-blocks-example-04"></a>

### **Example 4: while loop block**

- [x] The body of a **`while`** loop is a code block.
- [x] The loop repeats the block while the condition is true.

Sandbox: `code_sandbox/js-code-blocks/while-loop-block.html`

```javascript
let i = 0;
let text = "";
while (i < 3) {
  text += i + " ";
  i++;
}
```

![js-code-blocks example 4 source](../code_sandbox/snaps/js-code-blocks-04-code.png)

![js-code-blocks example 4 result](../code_sandbox/snaps/js-code-blocks-04-result.png)

- [x] **Outcome:** text is **"0 1 2 "**. i is **3** after the loop.

<a id="js-code-blocks-example-05"></a>

### **Example 5: { let x = 10 } — x not accessible outside**

- [x] `let` inside a block is visible **only in that block**.
- [x] Outside, `x` throws **ReferenceError**.

Sandbox: `code_sandbox/js-code-blocks/block-let-not-outside.html`

```javascript
{
  let x = 10;
  // x is accessible here
}
// x is not accessible here
```

![js-code-blocks example 5 source](../code_sandbox/snaps/js-code-blocks-05-code.png)

![js-code-blocks example 5 result](../code_sandbox/snaps/js-code-blocks-05-result.png)

- [x] **Outcome:** Inside, x is **10**. Outside, reading x throws **ReferenceError**.

<a id="js-code-blocks-example-06"></a>

### **Example 6: Standalone block: areal inside, ReferenceError outside**

- [x] A **standalone** `{ }` is a block not tied to `if`, `for`, or a function.
- [x] Use it to keep `let` / `const` **temporary** and off the global scope.

Sandbox: `code_sandbox/js-code-blocks/standalone-block-areal.html`

```javascript
{
  let x = 10;
  let y = 100;
  let areal = x * y;
}
```

![js-code-blocks example 6 source](../code_sandbox/snaps/js-code-blocks-06-code.png)

![js-code-blocks example 6 result](../code_sandbox/snaps/js-code-blocks-06-result.png)

- [x] **Outcome:** Inside, **areal** is **1000**. Outside, `x`, `y`, and `areal` each throw **ReferenceError**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-code-blocks/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a code block?

<details>
<summary>Answer</summary>

- [x] Statements grouped in **`{ }`**, treated as one unit.

</details>

### Question 2: Is a function body a block?

<details>
<summary>Answer</summary>

- [x] **Yes.** The body is always wrapped in braces.

</details>

### Question 3: Why do `if` / `else` use blocks?

<details>
<summary>Answer</summary>

- [x] So each branch can run **several statements** as one unit.

</details>

### Question 4: What did `check(10)` vs `check(3)` show?

<details>
<summary>Answer</summary>

- [x] **if block** vs **else block** — both ran in the demo.

</details>

### Question 5: What is the body of `for` / `while`?

<details>
<summary>Answer</summary>

- [x] A **code block** that repeats.

</details>

### Question 6: Can you read `let x = 10` after its `{ }`?

<details>
<summary>Answer</summary>

- [x] **No.** **ReferenceError**.

</details>

### Question 7: What is a standalone block for?

<details>
<summary>Answer</summary>

- [x] A **temporary scope** for `let` / `const` without a function.
- [x] Avoids polluting the global scope and name clashes.

</details>

### Question 8: What is `areal` inside `{ let x = 10; let y = 100; let areal = x * y }`?

<details>
<summary>Answer</summary>

- [x] **1000** inside. **ReferenceError** outside.

</details>

### Question 9: Does a standalone block run immediately?

<details>
<summary>Answer</summary>

- [x] **Yes.** It is not a function — the statements run when that part of the script runs.

</details>

### Question 10: Can you reuse the names `x` and `y` after the block?

<details>
<summary>Answer</summary>

- [x] **Yes.** They were never declared in the outer scope.

</details>

</details>

## Summary

Braces group statements for functions, branches, and loops, and they also define let/const scope. A standalone block is a lightweight way to keep short-lived names off the global object.

## References

- [JS Code Blocks (W3Schools)](https://www.w3schools.com/js/js_codeblocks.asp)
- [MDN: block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
