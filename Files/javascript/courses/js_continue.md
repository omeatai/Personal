# JS Continue

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

**`continue`** **skips the rest of the current iteration** and starts the **next** one. With a **label**, it can skip to the next pass of an **outer** loop, not only the inner one. Unlike `break`, the loop **keeps going**.

This section has **3** examples:

- [x] **Example 1:** `continue` skips i === 3 in a for loop [View](#js-continue-example-01)
- [x] **Example 2:** `continue loop1` [View](#js-continue-example-02)
- [x] **Example 3:** `continue loop2` [View](#js-continue-example-03)

## Detailed Explanation

- [x] **Skip one pass** — `i === 3` is omitted; **1 2 4 5 6 7 8 9** still print.
- [x] **`continue loop1`** — next **outer** iteration (**12121212**, no inner 4 on that pass).
- [x] **`continue loop2`** — next **inner** iteration (**124124124124**).
- [x] **`break` and `continue`** are the only statements that can jump out of a `{ }` block.

<a id="js-continue-example-01"></a>

### **Example 1: `continue` skips i === 3 in a for loop**

- [x] **`continue`** skips the **rest of this iteration** and starts the **next** one. The loop does **not** stop.
- [x] `for (let i = 1; i < 10; i++)` with `if (i === 3) { continue; }` before appending means **3** is missing.
- [x] Printed: **1 2 4 5 6 7 8 9** (no 3). Contrast `break`, which would stop at 1 2.

Sandbox: `code_sandbox/js-continue/continue-for.html`

```javascript
let text = "";
for (let i = 1; i < 10; i++) {
  if (i === 3) {
    continue;
  }
  text += "The number is " + i + "\n";
}
```

![js-continue example 1 source](../code_sandbox/snaps/js-continue-01-code.png)

![js-continue example 1 result](../code_sandbox/snaps/js-continue-01-result.png)

- [x] **Outcome:** `continue` at **i === 3** skips that pass only. The text is **The number is 1 The number is 2 The number is 4 The number is 5 The number is 6 The number is 7 The number is 8 The number is 9**.

<a id="js-continue-example-02"></a>

### **Example 2: `continue loop1`**

- [x] `continue loop1` jumps to the **next iteration of the outer** labeled loop.
- [x] When `i === 3`, the inner loop does **not** finish that outer pass (**i = 4** is skipped) and `j` advances.
- [x] Each of `j = 1..4` appends **12**, so text is **12121212**.
- [x] Same digits as `break loop2` on the Break page, but the meaning is different: here you **continue the outer** loop, not merely exit the inner one.

Sandbox: `code_sandbox/js-continue/continue-loop1.html`

```javascript
let text = "";
loop1: for (let j = 1; j < 5; j++) {
  loop2: for (let i = 1; i < 5; i++) {
    if (i === 3) {
      continue loop1;
    }
    text += i;
  }
}
```

![js-continue example 2 source](../code_sandbox/snaps/js-continue-02-code.png)

![js-continue example 2 result](../code_sandbox/snaps/js-continue-02-result.png)

- [x] **Outcome:** `continue loop1` at **i === 3** skips the rest of that **outer** pass. text is **12121212**.

<a id="js-continue-example-03"></a>

### **Example 3: `continue loop2`**

- [x] `continue loop2` skips only the **current inner** iteration. **`i = 4` still runs**.
- [x] Each outer pass appends **124** (1, 2, skip 3, then 4).
- [x] `j` is 1..4, so the text is **124124124124**.

Sandbox: `code_sandbox/js-continue/continue-loop2.html`

```javascript
let text = "";
loop1: for (let j = 1; j < 5; j++) {
  loop2: for (let i = 1; i < 5; i++) {
    if (i === 3) {
      continue loop2;
    }
    text += i;
  }
}
```

![js-continue example 3 source](../code_sandbox/snaps/js-continue-03-code.png)

![js-continue example 3 result](../code_sandbox/snaps/js-continue-03-result.png)

- [x] **Outcome:** `continue loop2` skips only inner **3**. Each outer pass adds **124**, so text is **124124124124**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-continue/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What numbers remain when `continue` skips `i === 3` in `for (let i = 1; i < 10; i++)`?

<details>
<summary>Answer</summary>

- [x] **1 2 4 5 6 7 8 9**.
- [x] **3** is skipped; the loop does **not** stop.

</details>

### Question 2: How is `continue` different from `break`?

<details>
<summary>Answer</summary>

- [x] **`break`** **ends** the loop.
- [x] **`continue`** **skips one** iteration and continues.

</details>

### Question 3: What text does `continue loop1` produce?

<details>
<summary>Answer</summary>

- [x] **12121212**.
- [x] At `i === 3` it jumps to the next **outer** `j`, so inner **4** is skipped.

</details>

### Question 4: What text does `continue loop2` produce?

<details>
<summary>Answer</summary>

- [x] **124124124124**.
- [x] Only the inner pass **3** is skipped; **4** still runs.

</details>

### Question 5: Why is there no `4` in each outer pass of `continue loop1`?

<details>
<summary>Answer</summary>

- [x] `continue loop1` abandons the rest of that outer iteration, including remaining inner `i` values.

</details>

### Question 6: Do `continue loop1` and `break loop2` print the same digits in this nest?

<details>
<summary>Answer</summary>

- [x] **Yes, both are 12121212** in this specific example.
- [x] The meaning still differs: **continue outer** vs **break inner**.

</details>

### Question 7: Which statements can jump out of a `{ }` block?

<details>
<summary>Answer</summary>

- [x] **`break`**
- [x] **`continue`**

</details>

### Question 8: What is a label?

<details>
<summary>Answer</summary>

- [x] An identifier followed by a **colon** (`loop1:`).
- [x] `continue labelname;` targets that loop.

</details>

### Question 9: After `continue` in a `for` loop, does exp3 (`i++`) still run?

<details>
<summary>Answer</summary>

- [x] **Yes.** `continue` in `for` still runs the **update** expression, then re-tests the condition.

</details>

### Question 10: Does `continue` at `i === 3` prevent later values like 8 and 9?

<details>
<summary>Answer</summary>

- [x] **No.** Only that one pass is skipped. **8** and **9** still print.

</details>

</details>

## Summary

`continue` skips **this** iteration: the 1..9 loop omits **3**. **`continue loop1`** → **12121212**; **`continue loop2`** → **124124124124**. The loop does **not** stop. Only `break` and `continue` jump out of a code block.

## References

- [JS Continue (W3Schools)](https://www.w3schools.com/js/js_continue.asp)
- [MDN: continue](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
- [MDN: labeled statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
