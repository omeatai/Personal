# JS Break

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

**`break`** **jumps out** of a **loop** or **`switch`**. In a loop it **stops immediately**. In a `switch` it prevents **fall-through**. With a **label**, `break` can leave a **nested loop** or even a **plain `{ }` block**.

This section has **5** examples:

- [x] **Example 1:** `break` when i === 3 in a for loop [View](#js-break-example-01)
- [x] **Example 2:** `break` in a switch (dayNum = 3) [View](#js-break-example-02)
- [x] **Example 3:** Labeled `break loop1` (leave the outer loop) [View](#js-break-example-03)
- [x] **Example 4:** Labeled `break loop2` (leave the inner loop only) [View](#js-break-example-04)
- [x] **Example 5:** Labeled `break` out of a block after the second car [View](#js-break-example-05)

## Detailed Explanation

- [x] **Loop `break`** — remaining iterations never run. `i === 3` leaves **0 1 2**.
- [x] **`switch` `break`** — exit after the matching case (`dayNum = 3` → **Wednesday**).
- [x] **Labels** — `name:` before a statement or block. `break loop1` leaves the **outer** loop; `break loop2` leaves only the **inner**.
- [x] **Labeled block** — `break list` after two cars leaves **BMW Volvo**.

<a id="js-break-example-01"></a>

### **Example 1: `break` when i === 3 in a for loop**

- [x] In a loop, **`break` terminates immediately**. No later iterations run. Control continues **after** the loop.
- [x] `for (let i = 0; i < 10; i++)` would normally print 0–9. `if (i === 3) { break; }` stops **before** appending 3.
- [x] The text is **The number is 0 The number is 1 The number is 2**. **3–9 never run.**

Sandbox: `code_sandbox/js-break/break-for.html`

```javascript
let text = "";
for (let i = 0; i < 10; i++) {
  if (i === 3) {
    break;
  }
  text += "The number is " + i + "\n";
}
```

![js-break example 1 source](../code_sandbox/snaps/js-break-01-code.png)

![js-break example 1 result](../code_sandbox/snaps/js-break-01-result.png)

- [x] **Outcome:** **break** at **i === 3** leaves **The number is 0 The number is 1 The number is 2**. **3** is not appended.

<a id="js-break-example-02"></a>

### **Example 2: `break` in a switch (dayNum = 3)**

- [x] In a **`switch`**, `break` **exits** after the matching case so later cases do not **fall through**.
- [x] The live page uses `new Date().getDay()`. The sandbox pins **`dayNum = 3`** → **Wednesday**.
- [x] Without `break`, case 3 would keep running into Thursday, Friday, …

Sandbox: `code_sandbox/js-break/break-switch.html`

```javascript
let dayNum = 3;
let day;
switch (dayNum) {
  case 0:
    day = "Sunday";
    break;
  case 1:
    day = "Monday";
    break;
  case 2:
    day = "Tuesday";
    break;
  case 3:
    day = "Wednesday";
    break;
  case 4:
    day = "Thursday";
    break;
  case 5:
    day = "Friday";
    break;
  case 6:
    day = "Saturday";
}
```

![js-break example 2 source](../code_sandbox/snaps/js-break-02-code.png)

![js-break example 2 result](../code_sandbox/snaps/js-break-02-result.png)

- [x] **Outcome:** **dayNum = 3** matches **case 3**, `break` exits, and day is **Wednesday**.

<a id="js-break-example-03"></a>

### **Example 3: Labeled `break loop1` (leave the outer loop)**

- [x] A **label** is an identifier plus a **colon**: `loop1: for (...)`.
- [x] `break loop1` leaves the **outer** labeled loop, not just the inner one.
- [x] Inner `i` goes 1, 2, then `i === 3` breaks **all** remaining nested work. Result text is **12**.

Sandbox: `code_sandbox/js-break/break-loop1.html`

```javascript
let text = "";
loop1: for (let j = 1; j < 5; j++) {
  loop2: for (let i = 1; i < 5; i++) {
    if (i === 3) {
      break loop1;
    }
    text += i;
  }
}
```

![js-break example 3 source](../code_sandbox/snaps/js-break-03-code.png)

![js-break example 3 result](../code_sandbox/snaps/js-break-03-result.png)

- [x] **Outcome:** `break loop1` at **i === 3** stops **both** loops. text is **12**.

<a id="js-break-example-04"></a>

### **Example 4: Labeled `break loop2` (leave the inner loop only)**

- [x] `break loop2` leaves **only the inner** loop. The **outer** loop continues with the next `j`.
- [x] Each outer pass appends **12** (i = 1, 2, then break inner; i = 4 never runs).
- [x] `j` is 1..4, so the text is **12121212**.

Sandbox: `code_sandbox/js-break/break-loop2.html`

```javascript
let text = "";
loop1: for (let j = 1; j < 5; j++) {
  loop2: for (let i = 1; i < 5; i++) {
    if (i === 3) {
      break loop2;
    }
    text += i;
  }
}
```

![js-break example 4 source](../code_sandbox/snaps/js-break-04-code.png)

![js-break example 4 result](../code_sandbox/snaps/js-break-04-result.png)

- [x] **Outcome:** `break loop2` stops only the **inner** loop. Four outer passes produce **12121212**.

<a id="js-break-example-05"></a>

### **Example 5: Labeled `break` out of a block after the second car**

- [x] Without a label, `break` only leaves a **loop** or **`switch`**.
- [x] With a label, `break` can leave **any `{ }` block**.
- [x] `list: { text += cars[0]; text += cars[1]; break list; text += cars[2]; ... }` never reaches Saab or Ford.
- [x] `break` and `continue` are the only statements that can **jump out of** a `{ }` block.

Sandbox: `code_sandbox/js-break/break-block.html`

```javascript
const cars = ["BMW", "Volvo", "Saab", "Ford"];
let text = "";
list: {
  text += cars[0] + " ";
  text += cars[1] + " ";
  break list;
  text += cars[2] + " ";
  text += cars[3] + " ";
}
```

![js-break example 5 source](../code_sandbox/snaps/js-break-05-code.png)

![js-break example 5 result](../code_sandbox/snaps/js-break-05-result.png)

- [x] **Outcome:** `break list` after the second name leaves **BMW Volvo**. Saab and Ford are skipped.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-break/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `break` do in `for (let i = 0; i < 10; i++)` when `i === 3`?

<details>
<summary>Answer</summary>

- [x] It **ends** the loop immediately.
- [x] The text is **The number is 0 The number is 1 The number is 2**.
- [x] **3** is not appended.

</details>

### Question 2: Does the `i === 3` iteration still append text before breaking in that Example?

<details>
<summary>Answer</summary>

- [x] **No.** `break` runs **before** `text += ...` in the sandbox order.
- [x] So **3** never appears.

</details>

### Question 3: What does the switch print for `dayNum = 3`?

<details>
<summary>Answer</summary>

- [x] **Wednesday**.
- [x] `break` after `case 3` prevents fall-through.

</details>

### Question 4: Why is `break` needed in `switch`?

<details>
<summary>Answer</summary>

- [x] Without it, execution **falls through** later cases.
- [x] `break` **exits** the switch after a matching case.

</details>

### Question 5: What text does `break loop1` produce in the nested 1..4 loops?

<details>
<summary>Answer</summary>

- [x] **12**.
- [x] It leaves the **outer** loop on the first `i === 3`.

</details>

### Question 6: What text does `break loop2` produce in the same nest?

<details>
<summary>Answer</summary>

- [x] **12121212**.
- [x] Only the **inner** loop stops; the outer `j` still runs 1..4.

</details>

### Question 7: What is a label?

<details>
<summary>Answer</summary>

- [x] An identifier followed by a **colon**.
- [x] It names a statement or `{ }` block for `break` / `continue`.

</details>

### Question 8: Can unlabeled `break` leave a plain `{ }` block?

<details>
<summary>Answer</summary>

- [x] **No.** Without a label, `break` only works in a **loop** or **switch**.
- [x] With `break list`, the block Example leaves **BMW Volvo**.

</details>

### Question 9: Which statements can jump out of a `{ }` block?

<details>
<summary>Answer</summary>

- [x] **`break`**
- [x] **`continue`**

</details>

### Question 10: After `break list` on the cars block, are Saab and Ford included?

<details>
<summary>Answer</summary>

- [x] **No.** Those lines never run.
- [x] The text is **BMW Volvo**.

</details>

</details>

## Summary

`break` exits a loop (`i === 3` → **0 1 2**) or a switch (`dayNum = 3` → **Wednesday**). **`break loop1`** yields **12**; **`break loop2`** yields **12121212**. A labeled block can stop after **BMW Volvo**. Only `break` and `continue` jump out of a `{ }` block.

## References

- [JS Break (W3Schools)](https://www.w3schools.com/js/js_break.asp)
- [MDN: break](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
- [MDN: labeled statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
- [MDN: switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
