# JS Math Random

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Math.random() samples [0, 1). Scale with a multiplier and Math.floor to get integers. *10 then floor is [0, 9]; add 1 to shift to [1, 10]; use *11 to include 10 in a 0-based range. A helper with (max - min) excludes max; (max - min + 1) includes both ends. Snaps are samples — re-run for another value in the same range.

This section has **9** examples:

- [x] **Example 1:** Math.random() — [0, 1) [View](#js-math-random-example-01)
- [x] **Example 2:** Math.floor(Math.random() * 10) — [0, 9] [View](#js-math-random-example-02)
- [x] **Example 3:** Math.floor(Math.random() * 11) — [0, 10] [View](#js-math-random-example-03)
- [x] **Example 4:** Math.floor(Math.random() * 100) — [0, 99] [View](#js-math-random-example-04)
- [x] **Example 5:** Math.floor(Math.random() * 101) — [0, 100] [View](#js-math-random-example-05)
- [x] **Example 6:** Math.floor(Math.random() * 10) + 1 — [1, 10] [View](#js-math-random-example-06)
- [x] **Example 7:** Math.floor(Math.random() * 100) + 1 — [1, 100] [View](#js-math-random-example-07)
- [x] **Example 8:** getRndInteger(min, max) — max excluded [View](#js-math-random-example-08)
- [x] **Example 9:** getRndInteger(min, max) — both included [View](#js-math-random-example-09)

## Detailed Explanation

- [x] `Math.random()` ∈ **[0, 1)** — 0 included, **1 never**.
- [x] `Math.floor(Math.random() * N)` → integers **0 .. N−1**.
- [x] `+ 1` after floor shifts a 0-based range up (e.g. **[0,9] → [1,10]**).
- [x] **Proper helpers:** `(max - min)` excludes max; `(max - min + 1)` includes both.
- [x] Snaps show **one sample**. Outcomes name the **range**, not a promised digit.

<a id="js-math-random-example-01"></a>

### **Example 1: Math.random() — [0, 1)**

- [x] `Math.random()` is **≥ 0** and **< 1**. Always **lower than 1**.
- [x] The snap is one sample, not a fixed teaching constant.

Sandbox: `code_sandbox/js-math-random/random.html`

```javascript
Math.random();
```

![js-math-random example 1 source](../code_sandbox/snaps/js-math-random-01-code.png)

![js-math-random example 1 result](../code_sandbox/snaps/js-math-random-01-result.png)

- [x] **Outcome:** The snap shows a **sample in [0, 1)**. Never **1**. A second draw still satisfies the range check.

<a id="js-math-random-example-02"></a>

### **Example 2: Math.floor(Math.random() * 10) — [0, 9]**

- [x] `Math.random() * 10` is **[0, 10)**. `floor` then yields integers **0 through 9**.
- [x] There are no JavaScript integers as a type — this is a **number with no fraction**.

Sandbox: `code_sandbox/js-math-random/int-0-9.html`

```javascript
Math.floor(Math.random() * 10);
```

![js-math-random example 2 source](../code_sandbox/snaps/js-math-random-02-code.png)

![js-math-random example 2 result](../code_sandbox/snaps/js-math-random-02-result.png)

- [x] **Outcome:** The snap shows a **sample integer in [0, 9]**. Re-running can produce any integer in that range. The range check on a second draw is **true**.

<a id="js-math-random-example-03"></a>

### **Example 3: Math.floor(Math.random() * 11) — [0, 10]**

- [x] Multiply by **11** (not 10) to include **10**. Range is **[0, 10]**.

Sandbox: `code_sandbox/js-math-random/int-0-10.html`

```javascript
Math.floor(Math.random() * 11);
```

![js-math-random example 3 source](../code_sandbox/snaps/js-math-random-03-code.png)

![js-math-random example 3 result](../code_sandbox/snaps/js-math-random-03-result.png)

- [x] **Outcome:** The snap shows a **sample integer in [0, 10]**. Re-running can produce any integer in that range. The range check on a second draw is **true**.

<a id="js-math-random-example-04"></a>

### **Example 4: Math.floor(Math.random() * 100) — [0, 99]**

- [x] `* 100` then `floor` → integers **0 through 99**.

Sandbox: `code_sandbox/js-math-random/int-0-99.html`

```javascript
Math.floor(Math.random() * 100);
```

![js-math-random example 4 source](../code_sandbox/snaps/js-math-random-04-code.png)

![js-math-random example 4 result](../code_sandbox/snaps/js-math-random-04-result.png)

- [x] **Outcome:** The snap shows a **sample integer in [0, 99]**. Re-running can produce any integer in that range. The range check on a second draw is **true**.

<a id="js-math-random-example-05"></a>

### **Example 5: Math.floor(Math.random() * 101) — [0, 100]**

- [x] `* 101` then `floor` → **0 through 100** (100 included).

Sandbox: `code_sandbox/js-math-random/int-0-100.html`

```javascript
Math.floor(Math.random() * 101);
```

![js-math-random example 5 source](../code_sandbox/snaps/js-math-random-05-code.png)

![js-math-random example 5 result](../code_sandbox/snaps/js-math-random-05-result.png)

- [x] **Outcome:** The snap shows a **sample integer in [0, 100]**. Re-running can produce any integer in that range. The range check on a second draw is **true**.

<a id="js-math-random-example-06"></a>

### **Example 6: Math.floor(Math.random() * 10) + 1 — [1, 10]**

- [x] `* 10` then `floor` is **[0, 9]**; **`+ 1`** shifts to **[1, 10]**.

Sandbox: `code_sandbox/js-math-random/int-1-10.html`

```javascript
Math.floor(Math.random() * 10) + 1;
```

![js-math-random example 6 source](../code_sandbox/snaps/js-math-random-06-code.png)

![js-math-random example 6 result](../code_sandbox/snaps/js-math-random-06-result.png)

- [x] **Outcome:** The snap shows a **sample integer in [1, 10]**. Re-running can produce any integer in that range. The range check on a second draw is **true**.

<a id="js-math-random-example-07"></a>

### **Example 7: Math.floor(Math.random() * 100) + 1 — [1, 100]**

- [x] Same shift: **[0, 99] + 1 → [1, 100]**.

Sandbox: `code_sandbox/js-math-random/int-1-100.html`

```javascript
Math.floor(Math.random() * 100) + 1;
```

![js-math-random example 7 source](../code_sandbox/snaps/js-math-random-07-code.png)

![js-math-random example 7 result](../code_sandbox/snaps/js-math-random-07-result.png)

- [x] **Outcome:** The snap shows a **sample integer in [1, 100]**. Re-running can produce any integer in that range. The range check on a second draw is **true**.

<a id="js-math-random-example-08"></a>

### **Example 8: getRndInteger(min, max) — max excluded**

- [x] `Math.floor(Math.random() * (max - min)) + min` includes **min**, excludes **max**.
- [x] The Tryit button calls `getRndInteger(0, 10)` → integers **[0, 9]**.
- [x] This page auto-runs once so the screenshot is not blank; the button re-rolls.

Sandbox: `code_sandbox/js-math-random/rnd-min-max-excl.html`

```javascript
function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}
```

![js-math-random example 8 source](../code_sandbox/snaps/js-math-random-08-code.png)

![js-math-random example 8 result](../code_sandbox/snaps/js-math-random-08-result.png)

- [x] **Outcome:** The snap shows a **sample integer in [0, 9]** from `getRndInteger(0, 10)`. Max is **excluded**. Clicking yields another value in that range.

<a id="js-math-random-example-09"></a>

### **Example 9: getRndInteger(min, max) — both included**

- [x] `Math.floor(Math.random() * (max - min + 1)) + min` includes **both** ends.
- [x] The Tryit button calls `getRndInteger(1, 10)` → integers **[1, 10]**.
- [x] Auto-run once for the screenshot; the button re-rolls.

Sandbox: `code_sandbox/js-math-random/rnd-min-max-incl.html`

```javascript
function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}
```

![js-math-random example 9 source](../code_sandbox/snaps/js-math-random-09-code.png)

![js-math-random example 9 result](../code_sandbox/snaps/js-math-random-09-result.png)

- [x] **Outcome:** The snap shows a **sample integer in [1, 10]** from `getRndInteger(1, 10)`. Both ends **included**. Clicking yields another value in that range.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-math-random/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What range is `Math.random()`?

<details>
<summary>Answer</summary>

- [x] **0 inclusive, 1 exclusive.** The snap is a sample in **[0, 1)**.

</details>

### Question 2: What integers does `Math.floor(Math.random() * 10)` produce?

<details>
<summary>Answer</summary>

- [x] **0 through 9** (both included).

</details>

### Question 3: Why `* 11` for 0 through 10?

<details>
<summary>Answer</summary>

- [x] `* 10` only reaches **[0, 9]**. `* 11` then `floor` includes **10**.

</details>

### Question 4: `Math.floor(Math.random() * 100)` range?

<details>
<summary>Answer</summary>

- [x] **[0, 99]**.

</details>

### Question 5: `Math.floor(Math.random() * 101)` range?

<details>
<summary>Answer</summary>

- [x] **[0, 100]**.

</details>

### Question 6: How do you get **1 through 10**?

<details>
<summary>Answer</summary>

- [x] `Math.floor(Math.random() * 10) + 1`.

</details>

### Question 7: How do you get **1 through 100**?

<details>
<summary>Answer</summary>

- [x] `Math.floor(Math.random() * 100) + 1`.

</details>

### Question 8: What does the max-**excluded** helper do for `(0, 10)`?

<details>
<summary>Answer</summary>

- [x] Integers **[0, 9]**. Formula: `(max - min)` without `+ 1`.

</details>

### Question 9: What does the max-**included** helper do for `(1, 10)`?

<details>
<summary>Answer</summary>

- [x] Integers **[1, 10]**. Formula: `(max - min + 1)`.

</details>

### Question 10: Are these cryptographic random numbers?

<details>
<summary>Answer</summary>

- [x] **No.** `Math.random()` is a PRNG for demos/games, not security.

</details>

### Question 11: Will two screenshots of `Math.random()` match?

<details>
<summary>Answer</summary>

- [x] **Usually not.** Each load is a new sample in the same range.

</details>


</details>

## Summary

Scale Math.random() with floor for integer ranges. Count the span carefully (*10 is 0–9, *11 is 0–10). Prefer a named helper: exclude max with (max-min), include both with (max-min+1). Treat every snap as a sample in that range.

## References

- [JS Random (W3Schools)](https://www.w3schools.com/js/js_random.asp)
- [MDN: Math.random](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)
