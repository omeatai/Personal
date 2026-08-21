# JS Control Flow

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

**Control flow** is the **order** statements run. By default JavaScript goes **top to bottom, left to right**. Conditions, loops, jumps, and function calls **change** that order. JavaScript is **single-threaded** (one thing at a time) unless you use **async** APIs — that idea is a bullet here, not a separate Example.

This section has **5** examples:

- [x] **Example 1:** Default sequential flow [View](#js-control-flow-example-01)
- [x] **Example 2:** Conditional `if` / `else` (age 20 Adult) [View](#js-control-flow-example-02)
- [x] **Example 3:** `for` loop i < 5 [View](#js-control-flow-example-03)
- [x] **Example 4:** `break` when i === 3 [View](#js-control-flow-example-04)
- [x] **Example 5:** Function `myFunction(p1, p2)` returns p1 \* p2 [View](#js-control-flow-example-05)

## Detailed Explanation

- [x] **Default** — sequential: `x = 5`, `y = 6`, `z = x + y` → **11**.
- [x] **Conditional** — `if` / `else` / `switch` / ternary. **age 20** → **Adult**; **age 16** → **Minor**.
- [x] **Loops** — `for` / `while` / `do...while`. **`for i < 5`** prints 0–4.
- [x] **Jumps** — `break`, `continue`, `return`, `throw`. **`break` at 3** leaves 0 1 2. **`return`** is shown via `myFunction(3, 4)` → **12**.
- [x] **Single-threaded** — JavaScript does **one thing at a time**. A slow file or network call can **freeze** the page unless you use **asynchronous** APIs (later Advanced chapter). No extra Example; the point is the model, not a demo.

<a id="js-control-flow-example-01"></a>

### **Example 1: Default sequential flow**

- [x] **Control flow** is the **order** statements run. By default JavaScript goes **top to bottom, left to right**.
- [x] `let x = 5; let y = 6; let z = x + y;` runs in that order: x, then y, then the sum.
- [x] **z** is **11**. Nothing branches or repeats yet.

Sandbox: `code_sandbox/js-control-flow/sequential.html`

```javascript
let x = 5;
let y = 6;
let z = x + y;
```

![js-control-flow example 1 source](../code_sandbox/snaps/js-control-flow-01-code.png)

![js-control-flow example 1 result](../code_sandbox/snaps/js-control-flow-01-result.png)

- [x] **Outcome:** Sequential assignment yields **x = 5**, **y = 6**, **z = 11**.

<a id="js-control-flow-example-02"></a>

### **Example 2: Conditional `if` / `else` (age 20 Adult)**

- [x] Conditions **branch** the flow: **`if`**, **`if...else`**, **`switch`**, ternary **`? :`**.
- [x] `if (age >= 18) { text = "Adult"; } else { text = "Minor"; }`.
- [x] Pin **`age = 20`** → **Adult**. The other branch: **age 16** would be **Minor** (called out in the labeled result).

Sandbox: `code_sandbox/js-control-flow/conditional.html`

```javascript
let age = 20;
let text = "Unknown";
if (age >= 18) {
  text = "Adult";
} else {
  text = "Minor";
}
```

![js-control-flow example 2 source](../code_sandbox/snaps/js-control-flow-02-code.png)

![js-control-flow example 2 result](../code_sandbox/snaps/js-control-flow-02-result.png)

- [x] **Outcome:** **age 20** → **Adult**. The other branch **age 16** → **Minor**.

<a id="js-control-flow-example-03"></a>

### **Example 3: `for` loop i < 5**

- [x] Loops **repeat** flow: **`for`**, **`while`**, **`do...while`**.
- [x] `for (let i = 0; i < 5; i++)` keeps going until `i < 5` is false.
- [x] Printed numbers: **0 1 2 3 4**.

Sandbox: `code_sandbox/js-control-flow/for-loop.html`

```javascript
let text = "";
for (let i = 0; i < 5; i++) {
  text += "The number is " + i + "\n";
}
```

![js-control-flow example 3 source](../code_sandbox/snaps/js-control-flow-03-code.png)

![js-control-flow example 3 result](../code_sandbox/snaps/js-control-flow-03-result.png)

- [x] **Outcome:** The loop text is **The number is 0 The number is 1 The number is 2 The number is 3 The number is 4**.

<a id="js-control-flow-example-04"></a>

### **Example 4: `break` when i === 3**

- [x] **Jump** statements change flow abruptly: **`break`**, **`continue`**, **`return`**, **`throw`**.
- [x] `break` **exits** a loop or switch. Here it stops when **i === 3** (before appending 3).
- [x] Result: **The number is 0 The number is 1 The number is 2**.

Sandbox: `code_sandbox/js-control-flow/break.html`

```javascript
let text = "";
for (let i = 0; i < 10; i++) {
  if (i === 3) {
    break;
  }
  text += "The number is " + i + "\n";
}
```

![js-control-flow example 4 source](../code_sandbox/snaps/js-control-flow-04-code.png)

![js-control-flow example 4 result](../code_sandbox/snaps/js-control-flow-04-result.png)

- [x] **Outcome:** `break` at **i === 3** leaves **The number is 0 The number is 1 The number is 2**.

<a id="js-control-flow-example-05"></a>

### **Example 5: Function `myFunction(p1, p2)` returns p1 \* p2**

- [x] Functions are **callable, reusable** blocks. They run **when called**, not when defined.
- [x] `function myFunction(p1, p2) { return p1 * p2; }` — **`return`** is a jump that **exits the function** with a value.
- [x] Call **`myFunction(3, 4)`** → **12**.

Sandbox: `code_sandbox/js-control-flow/function.html`

```javascript
function myFunction(p1, p2) {
  return p1 * p2;
}
myFunction(3, 4);
```

![js-control-flow example 5 source](../code_sandbox/snaps/js-control-flow-05-code.png)

![js-control-flow example 5 result](../code_sandbox/snaps/js-control-flow-05-result.png)

- [x] **Outcome:** **myFunction(3, 4)** returns **12**. The function body runs only when it is **called**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-control-flow/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is control flow?

<details>
<summary>Answer</summary>

- [x] The **order** in which statements execute.
- [x] Default is **top to bottom**, **left to right**.

</details>

### Question 2: What is `z` after `let x = 5; let y = 6; let z = x + y`?

<details>
<summary>Answer</summary>

- [x] **11**.

</details>

### Question 3: With `age = 20`, what does the `if` / `else` assign?

<details>
<summary>Answer</summary>

- [x] **Adult**.
- [x] `age >= 18` is true.

</details>

### Question 4: What would the other branch print for `age = 16`?

<details>
<summary>Answer</summary>

- [x] **Minor**.
- [x] That is the `else` path shown in the labeled result.

</details>

### Question 5: What numbers does `for (let i = 0; i < 5; i++)` print?

<details>
<summary>Answer</summary>

- [x] **The number is 0** through **The number is 4**.

</details>

### Question 6: What does `break` at `i === 3` leave in the 0..9 loop?

<details>
<summary>Answer</summary>

- [x] **The number is 0 The number is 1 The number is 2**.

</details>

### Question 7: What does `myFunction(3, 4)` return when the body is `return p1 * p2`?

<details>
<summary>Answer</summary>

- [x] **12**.
- [x] The function runs **when it is called**, not when it is defined.

</details>

### Question 8: Name the four jump statements on this page.

<details>
<summary>Answer</summary>

- [x] **`break`** — exit a loop or switch.
- [x] **`continue`** — skip this iteration.
- [x] **`return`** — exit a function.
- [x] **`throw`** — jump to error handling.

</details>

### Question 9: What does “JavaScript is single-threaded” mean?

<details>
<summary>Answer</summary>

- [x] It can do **one thing at a time**.
- [x] Slow work can **freeze** the page unless you use **async** APIs.

</details>

### Question 10: When does a function change control flow?

<details>
<summary>Answer</summary>

- [x] When it is **called**: execution jumps into the function, then **`return`** jumps back with a value (or `undefined`).

</details>

### Question 11: Which statements change flow with conditions?

<details>
<summary>Answer</summary>

- [x] **`if`** / **`if...else`**
- [x] **`switch`**
- [x] Ternary **`? :`**

</details>

</details>

## Summary

Default flow is sequential (**z = 11**). **Conditions** branch (**age 20** → **Adult**). **Loops** repeat (**0–4**). **`break`** cuts the 0..9 loop to **0 1 2**. **`myFunction(3, 4)`** returns **12**. JavaScript is **single-threaded**; async work is covered later.

## References

- [JS Control Flow (W3Schools)](https://www.w3schools.com/js/js_control_flow.asp)
- [MDN: Control flow and error handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [MDN: return](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
- [MDN: throw](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
