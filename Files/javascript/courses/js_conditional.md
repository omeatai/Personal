# JS Conditional

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Conditional statements run **different code** for different **true/false** conditions. This overview names **`if`**, **`else`**, **`else if`**, **`switch`**, and the **ternary** `? :`. The W3Schools page is mostly syntax; each named construct still has its own runnable Example below, with hours and weekday numbers **pinned** so the snaps are stable.

This section has **5** examples:

- [x] **Example 1:** The `if` statement [View](#js-conditional-example-01)
- [x] **Example 2:** The `else` statement [View](#js-conditional-example-02)
- [x] **Example 3:** The `else if` statement [View](#js-conditional-example-03)
- [x] **Example 4:** The `switch` statement [View](#js-conditional-example-04)
- [x] **Example 5:** The ternary operator (`? :`) [View](#js-conditional-example-05)

## Detailed Explanation

- [x] **Core idea** — pick a branch from a Boolean test instead of running every line in order.
- [x] **`if` / `else` / `else if`** — one test, the opposite branch, then extra tests. Only the **first true** branch runs.
- [x] **`switch`** — many alternative blocks from **one** expression. Put **`break`** after each `case` (include **`default`**).
- [x] **Ternary `? :`** — shorthand `if` / `else` that **returns** a value: `condition ? a : b`.

<a id="js-conditional-example-01"></a>

### **Example 1: The `if` statement**

- [x] **`if (condition) { ... }`** runs the block only when the condition is **true**.
- [x] This page is mostly syntax. The sandbox pins **`hour = 10`** so the snap is stable (the live Tryit often uses `new Date().getHours()`).
- [x] Because **10 < 18**, the block runs and `greeting` becomes **Good day**.
- [x] If the condition is false, `if` does **nothing** — that is why **`else`** exists (next Example).

Sandbox: `code_sandbox/js-conditional/if.html`

```javascript
let hour = 10;
let greeting;
if (hour < 18) {
  greeting = "Good day";
}
```

![js-conditional example 1 source](../code_sandbox/snaps/js-conditional-01-code.png)

![js-conditional example 1 result](../code_sandbox/snaps/js-conditional-01-result.png)

- [x] **Outcome:** With **hour = 10**, `hour < 18` is **true**, so greeting is **Good day**.

<a id="js-conditional-example-02"></a>

### **Example 2: The `else` statement**

- [x] **`else`** runs when the matching **`if`** condition is **false**.
- [x] Pin **`hour = 20`**. **20 < 18** is false, so the `if` block is skipped and `else` assigns **Good evening**.
- [x] One `if` / `else` pair tests **one** condition. Use **`else if`** when you have a **new** test (next Example).

Sandbox: `code_sandbox/js-conditional/else.html`

```javascript
let hour = 20;
let greeting;
if (hour < 18) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}
```

![js-conditional example 2 source](../code_sandbox/snaps/js-conditional-02-code.png)

![js-conditional example 2 result](../code_sandbox/snaps/js-conditional-02-result.png)

- [x] **Outcome:** With **hour = 20**, `hour < 18` is **false**, so the `else` branch runs and greeting is **Good evening**.

<a id="js-conditional-example-03"></a>

### **Example 3: The `else if` statement**

- [x] **`else if`** tests a **new** condition only if every earlier test was **false**.
- [x] Chain: `hour < 10` → **Good morning**; else `hour < 18` → **Good day**; else → **Good evening**.
- [x] Pin **`hour = 8`**. **8 < 10** is true, so the first block runs and later branches are **skipped**.
- [x] Same chain with **hour = 12** would be **Good day**; **hour = 20** would be **Good evening**. Only the **first matching** branch runs.

Sandbox: `code_sandbox/js-conditional/else-if.html`

```javascript
let hour = 8;
let greeting;
if (hour < 10) {
  greeting = "Good morning";
} else if (hour < 18) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}
```

![js-conditional example 3 source](../code_sandbox/snaps/js-conditional-03-code.png)

![js-conditional example 3 result](../code_sandbox/snaps/js-conditional-03-result.png)

- [x] **Outcome:** With **hour = 8**, the first test `hour < 10` is **true**, so greeting is **Good morning**. The `else if` and `else` blocks do not run.

<a id="js-conditional-example-04"></a>

### **Example 4: The `switch` statement**

- [x] **`switch (expression)`** picks a **`case`** that **strictly matches** (`===`) the expression.
- [x] Use **`break`** after each case so execution does **not fall through** into the next case.
- [x] **`default`** runs when no case matches (for example an unexpected day number).
- [x] The live page uses `new Date().getDay()`. The sandbox pins **`dayNum = 3`** (Wednesday) so the snap always matches.

Sandbox: `code_sandbox/js-conditional/switch.html`

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
    break;
  default:
    day = "Unknown";
}
```

![js-conditional example 4 source](../code_sandbox/snaps/js-conditional-04-code.png)

![js-conditional example 4 result](../code_sandbox/snaps/js-conditional-04-result.png)

- [x] **Outcome:** With **dayNum = 3**, `case 3` matches, `break` exits the switch, and day is **Wednesday**.

<a id="js-conditional-example-05"></a>

### **Example 5: The ternary operator (`? :`)**

- [x] **`condition ? exprIfTrue : exprIfFalse`** is a one-line **`if` / `else`** that **returns a value**.
- [x] `(hour < 18) ? "Good day" : "Good evening"` assigns the greeting in one expression.
- [x] The sandbox prints **hour = 10** (true branch) and **hour = 20** (false branch) so you can see both sides.
- [x] Keep ternaries **short**. A long chain is usually clearer as `if` / `else if`.

Sandbox: `code_sandbox/js-conditional/ternary.html`

```javascript
let hour = 10;
let greeting = hour < 18 ? "Good day" : "Good evening";
```

![js-conditional example 5 source](../code_sandbox/snaps/js-conditional-05-code.png)

![js-conditional example 5 result](../code_sandbox/snaps/js-conditional-05-result.png)

- [x] **Outcome:** **hour 10** → **Good day** (condition true). **hour 20** → **Good evening** (condition false).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-conditional/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: With `hour = 10`, what does the `if (hour < 18)` example assign to `greeting`?

<details>
<summary>Answer</summary>

- [x] **Good day**.
- [x] `10 < 18` is **true**, so the `if` block runs.

</details>

### Question 2: With `hour = 20`, which branch of `if` / `else` runs?

<details>
<summary>Answer</summary>

- [x] The **`else`** branch.
- [x] `20 < 18` is **false**, so greeting is **Good evening**.

</details>

### Question 3: In the `else if` chain, what is `greeting` when `hour = 8`?

<details>
<summary>Answer</summary>

- [x] **Good morning**.
- [x] `hour < 10` is true first, so later branches are skipped.

</details>

### Question 4: In that same `else if` chain, what would `hour = 12` and `hour = 20` produce?

<details>
<summary>Answer</summary>

- [x] **12** → **Good day** (`hour < 10` is false, `hour < 18` is true).
- [x] **20** → **Good evening** (both tests false).

</details>

### Question 5: What does the `switch` print when `dayNum = 3`?

<details>
<summary>Answer</summary>

- [x] **Wednesday**.
- [x] `case 3` matches and **`break`** stops further cases.

</details>

### Question 6: Why does each `switch` case end with `break`?

<details>
<summary>Answer</summary>

- [x] Without `break`, execution **falls through** into the next case (and maybe `default`).
- [x] `break` **exits** the switch after the matching case.

</details>

### Question 7: What does `(hour < 18) ? "Good day" : "Good evening"` return for hour 10 and hour 20?

<details>
<summary>Answer</summary>

- [x] **10** → **Good day**.
- [x] **20** → **Good evening**.

</details>

### Question 8: When is `switch` a better fit than a long `if` / `else if` chain?

<details>
<summary>Answer</summary>

- [x] When you choose among **many alternative blocks** from **one** expression (like a weekday number).

</details>

### Question 9: Does `if` run any code when its condition is false and there is no `else`?

<details>
<summary>Answer</summary>

- [x] **No.** The `if` block is skipped.
- [x] That is why Example 1 with a false hour would leave `greeting` **undefined** unless you add `else`.

</details>

### Question 10: Does `else if` test its condition even when an earlier `if` was already true?

<details>
<summary>Answer</summary>

- [x] **No.** Only the **first matching** branch runs.
- [x] With `hour = 8`, `hour < 18` is never tested.

</details>

</details>

## Summary

Conditionals choose a branch: **`if`** (`hour = 10` → **Good day**), **`else`** (`hour = 20` → **Good evening**), **`else if`** (`hour = 8` → **Good morning**), **`switch`** (`dayNum = 3` → **Wednesday**, with `break` / `default`), and ternary **`? :`** (10 → **Good day**, 20 → **Good evening**). Later chapters go deeper on each form.

## References

- [JS Conditional (W3Schools)](https://www.w3schools.com/js/js_conditionals.asp)
- [MDN: if...else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
- [MDN: switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
- [MDN: Conditional (ternary) operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)
