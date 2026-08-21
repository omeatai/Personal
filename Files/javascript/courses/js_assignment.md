# JS Assignment

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Assignment operators **put values into variables**. The simple operator is **`=`**. Compound forms (`+=`, `-=`, `*=`, `**=`, `/=`, `%=`) update a variable in place (`x += 5` means `x = x + 5`). On strings, `+=` **concatenates**. ES2020 adds logical assignment (`&&=`, `||=`, `??=`). This page also shows the **spread** `...` operator, which splits an iterable into individual elements.

This section has **8** examples:

- [x] **Example 1:** Simple assignment (`=`) [View](#js-assignment-example-01)
- [x] **Example 2:** Addition assignment (`+=`) [View](#js-assignment-example-02)
- [x] **Example 3:** Other arithmetic assignments (`-= *= **= /= %=`) [View](#js-assignment-example-03)
- [x] **Example 4:** String assignment (`=` and `+=`) [View](#js-assignment-example-04)
- [x] **Example 5:** Logical AND assignment (`&&=`) [View](#js-assignment-example-05)
- [x] **Example 6:** Logical OR assignment (`||=`) [View](#js-assignment-example-06)
- [x] **Example 7:** Nullish coalescing assignment (`??=`) [View](#js-assignment-example-07)
- [x] **Example 8:** Spread (`...`) [View](#js-assignment-example-08)

## Detailed Explanation

- [x] **Assignment operators assign values to JavaScript variables.** Given `x = 10` and `y = 5`:
  - `=` copies the right-hand value (`x = y` → `x` is `5`).
  - `+=` `-=` `*=` `**=` `/=` `%=` mean `x = x + y`, `x = x - y`, and so on.
  - The page table also lists object-property shorthand `x: 45` (same idea as `size.x = 45`) — that is **object syntax**, not a standalone assignment operator you write as `x: 45` by itself.
- [x] **Logical assignment (ES2020)** uses truthiness / nullishness, not arithmetic:
  - `&&=` assigns the right-hand value only if the left is **truthy**.
  - `||=` assigns the right-hand value only if the left is **falsy**.
  - `??=` assigns the right-hand value only if the left is **`null` or `undefined`** (nullish). `0` and `""` are falsy but **not** nullish.
- [x] **The eight falsy values** are `false`, `0`, `-0`, `0n`, `""` / `''` / `` ` ` `` (empty strings), `null`, `undefined`, and `NaN`. Common traps that are actually **truthy**: `"0"`, `"false"`, `[]`, `{}`.

<a id="js-assignment-example-01"></a>

### **Example 1: Simple assignment (`=`)**

- [x] **`=`** evaluates the right-hand side, then stores that value in the variable on the left.
- [x] The right-hand side can be a **literal** (`10`) or an **expression** (`10 + y`). The expression runs first, then the result is assigned.
- [x] After `let y = 5`, `let z = 10 + y` stores **15** in `z`. `y` itself is unchanged.

Sandbox: `code_sandbox/js-assignment/simple.html`

```javascript
let x = 10;
let y = 5;
let z = 10 + y;
```

![js-assignment example 1 source](../code_sandbox/snaps/js-assignment-01-code.png)

![js-assignment example 1 result](../code_sandbox/snaps/js-assignment-01-result.png)

- [x] **Outcome:** `x` is **10**, `y` is **5**, and `z` is **15**.

<a id="js-assignment-example-02"></a>

### **Example 2: Addition assignment (`+=`)**

- [x] **`x += 5`** is exactly **`x = x + 5`**. It reads the current value, adds 5, and writes the sum back.
- [x] Starting at `10`, `x += 5` leaves `x` at **15**.
- [x] Do not confuse `+=` with `=+` (a unary plus after `=`). Always write the operator as **`+=`**.

Sandbox: `code_sandbox/js-assignment/add.html`

```javascript
let x = 10;
x += 5;
```

![js-assignment example 2 source](../code_sandbox/snaps/js-assignment-02-code.png)

![js-assignment example 2 result](../code_sandbox/snaps/js-assignment-02-result.png)

- [x] **Outcome:** after `x += 5`, `x` is **15**.

<a id="js-assignment-example-03"></a>

### **Example 3: Other arithmetic assignments (`-= \*= **= /= %=`)\*\*

- [x] Each compound operator is shorthand for using the same variable on both sides:
  - `x -= 5` → `x = x - 5` → **5**
  - `a *= 5` → `a = a * 5` → **50**
  - `b **= 5` → `b = b ** 5` → **100000** (`10` to the power of `5`)
  - `c /= 5` → `c = c / 5` → **2**
  - `d %= 5` → `d = d % 5` → **0** (10 divides evenly by 5)
- [x] The page table uses the same numbers with `x = 10` and `y = 5` (`x += y` → 15, `x **= y` → 100000, and so on).
- [x] Reset the variable to `10` before each line if you want to compare operators; otherwise each compound mutates the previous result.

Sandbox: `code_sandbox/js-assignment/others.html`

```javascript
let x = 10;
x -= 5; // 5
let a = 10;
a *= 5; // 50
let b = 10;
b **= 5; // 100000
let c = 10;
c /= 5; // 2
let d = 10;
d %= 5; // 0
```

![js-assignment example 3 source](../code_sandbox/snaps/js-assignment-03-code.png)

![js-assignment example 3 result](../code_sandbox/snaps/js-assignment-03-result.png)

- [x] **Outcome:** the five results are **5, 50, 100000, 2, 0**.

<a id="js-assignment-example-04"></a>

### **Example 4: String assignment (`=` and `+=`)**

- [x] **`=`** stores a string just like a number: `let text = "Hello"` makes `text` the string **Hello**.
- [x] On strings, **`+=` concatenates** (it does not add numbers). `"Hello" + " World"` becomes **Hello World** — note the leading space in `" World"` or the words glue together.
- [x] Only `=` and `+=` are used for string assignment on this page. `-=` / `*=` and the rest are for numbers.

Sandbox: `code_sandbox/js-assignment/strings.html`

```javascript
let text = "Hello";
text += " World";
```

![js-assignment example 4 source](../code_sandbox/snaps/js-assignment-04-code.png)

![js-assignment example 4 result](../code_sandbox/snaps/js-assignment-04-result.png)

- [x] **Outcome:** `text` starts as **Hello** and becomes **Hello World** after `+=`.

<a id="js-assignment-example-05"></a>

### **Example 5: Logical AND assignment (`&&=`)**

- [x] **`x &&= 10`** assigns `10` to `x` **only if `x` is truthy**. If `x` is falsy, `x` is left alone (short-circuit).
- [x] `let y = x &&= 10` stores the **result of that assignment expression** in `y` (the new `x` if assignment happened, otherwise the original falsy `x`).
- [x] Truthy starters `true` and `1` become **10**. Falsy starters `false`, `0`, `undefined`, and `null` stay as they were.
- [x] This operator is an **ES2020** feature.

Sandbox: `code_sandbox/js-assignment/and.html`

```javascript
let x = true;
let y = (x &&= 10);
let x = false;
let y = (x &&= 10);
let x = 1;
let y = (x &&= 10);
let x = 0;
let y = (x &&= 10);
let x = undefined;
let y = (x &&= 10);
let x = null;
let y = (x &&= 10);
```

![js-assignment example 5 source](../code_sandbox/snaps/js-assignment-05-code.png)

![js-assignment example 5 result](../code_sandbox/snaps/js-assignment-05-result.png)

- [x] **Outcome:** truthy `x` becomes **10**; falsy `x` stays `false`, `0`, `undefined`, or `null`. `y` matches `x` in every row.

<a id="js-assignment-example-06"></a>

### **Example 6: Logical OR assignment (`||=`)**

- [x] **`x ||= 10`** assigns `10` **only if `x` is falsy**. If `x` is already truthy, it is left alone.
- [x] Falsy starters `false`, `null`, and `undefined` all become **10**. Truthy `true` stays **true**.
- [x] This is a common pattern for default values (`name ||= "Guest"`), but it will also overwrite `0` and `""` because those are falsy — use `??=` when you only want to fill in `null` / `undefined`.
- [x] **ES2020** feature.

Sandbox: `code_sandbox/js-assignment/or.html`

```javascript
let x = false;
let y = (x ||= 10);
let x = true;
let y = (x ||= 10);
let x = null;
let y = (x ||= 10);
let x = undefined;
let y = (x ||= 10);
```

![js-assignment example 6 source](../code_sandbox/snaps/js-assignment-06-code.png)

![js-assignment example 6 result](../code_sandbox/snaps/js-assignment-06-result.png)

- [x] **Outcome:** `false` / `null` / `undefined` become **10**; `true` stays **true**.

<a id="js-assignment-example-07"></a>

### **Example 7: Nullish coalescing assignment (`??=`)**

- [x] **`x ??= 10`** assigns `10` **only if `x` is `null` or `undefined`**. Other falsy values (`0`, `""`, `false`) are kept.
- [x] An uninitialized `let a;` is `undefined`, so `a ??= 10` becomes **10**. `b = 0` stays **0**. `null` and `undefined` become **10**. An already-set `x = 10` stays **10**.
- [x] Prefer `??=` over `||=` when `0` or an empty string is a valid stored value.
- [x] **ES2020** feature.

Sandbox: `code_sandbox/js-assignment/nullish.html`

```javascript
let a;
a ??= 10;
let b = 0;
b ??= 10;
let c = null;
c ??= 10;
let d = undefined;
d ??= 10;
let x = 10;
let y = 5;
x ??= 10;
```

![js-assignment example 7 source](../code_sandbox/snaps/js-assignment-07-code.png)

![js-assignment example 7 result](../code_sandbox/snaps/js-assignment-07-result.png)

- [x] **Outcome:** `a`, `c`, and `d` become **10**; `b` stays **0**; `x` stays **10**.

<a id="js-assignment-example-08"></a>

### **Example 8: Spread (`...`)**

- [x] **`...`** splits an iterable into individual elements. A string is iterable **character by character**.
- [x] `Math.min(...text)` with `text = "12345"` is `Math.min("1","2","3","4","5")`, which coerces to numbers and returns **1**. `Math.max` returns **5**.
- [x] Spread is not an assignment operator; the page includes it here because it is used when passing many values (including into assignments and function calls).

Sandbox: `code_sandbox/js-assignment/spread.html`

```javascript
let text = "12345";
let min = Math.min(...text);
let max = Math.max(...text);
```

![js-assignment example 8 source](../code_sandbox/snaps/js-assignment-08-code.png)

![js-assignment example 8 result](../code_sandbox/snaps/js-assignment-08-result.png)

- [x] **Outcome:** `Math.min(...text)` is **1** and `Math.max(...text)` is **5**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-assignment/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `x += 5` if `x` started at 10?

<details>
<summary>Answer</summary>

- [x] **15.** Same as `x = x + 5`.

</details>

### Question 2: What is `10 **= 5` (starting `b = 10; b **= 5`)?

<details>
<summary>Answer</summary>

- [x] **100000** — ten to the power of five.
- [x] Same as `b = b ** 5`.

</details>

### Question 3: What is `10 %= 5`?

<details>
<summary>Answer</summary>

- [x] **0** — 10 divides evenly by 5, so the remainder is 0.

</details>

### Question 4: Can `+=` be used on strings?

<details>
<summary>Answer</summary>

- [x] **Yes.** It **concatenates**.
- [x] `"Hello"` then `+= " World"` becomes **Hello World**.

</details>

### Question 5: What does `x &&= 10` do when `x` is `true` vs `false`?

<details>
<summary>Answer</summary>

- [x] If `x` is **truthy** (`true`, `1`), it becomes **10**.
- [x] If `x` is **falsy** (`false`, `0`, `null`, `undefined`), it is left unchanged.

</details>

### Question 6: What does `x ||= 10` do when `x` is `true` vs `false`?

<details>
<summary>Answer</summary>

- [x] If `x` is **falsy**, it becomes **10**.
- [x] If `x` is **truthy** (`true`), it stays **true**.

</details>

### Question 7: What does `??=` do with `0` vs `null`?

<details>
<summary>Answer</summary>

- [x] `0 ??= 10` stays **0** — zero is not nullish.
- [x] `null ??= 10` becomes **10**.
- [x] Only **`null`** and **`undefined`** trigger the assignment.

</details>

### Question 8: Name the eight falsy values.

<details>
<summary>Answer</summary>

- [x] `false`, `0`, `-0`, `0n`, empty strings (`""`, `''`, empty template), `null`, `undefined`, `NaN`.
- [x] `"0"`, `"false"`, `[]`, and `{}` are **truthy**.

</details>

### Question 9: What do `Math.min(... "12345")` and `Math.max(... "12345")` return?

<details>
<summary>Answer</summary>

- [x] **1** and **5**.
- [x] Spread turns the string into the characters `"1"` … `"5"`, which coerce to numbers.

</details>

### Question 10: When should you use `??=` instead of `||=` for a default?

<details>
<summary>Answer</summary>

- [x] Use **`??=`** when **`0`** or an **empty string** is a valid value you must keep.
- [x] **`||=`** would overwrite those because they are falsy.

</details>

### Question 11: Is `&&=` / `||=` / `??=` old JavaScript?

<details>
<summary>Answer</summary>

- [x] **No.** They are **ES2020** features.

</details>

</details>

## Summary

**`=`** assigns a value (literal or expression). Compound arithmetic operators (`+= -= *= **= /= %=`) mean `x = x ⊕ value`. On strings, **`+=` concatenates**. Logical assignment is ES2020: **`&&=`** writes when the left is truthy, **`||=`** when it is falsy, **`??=`** only when it is `null` or `undefined` (`0` is kept). Spread **`...`** unpacks iterables — `"12345"` into `Math.min` / `Math.max` yields **1** and **5**.

## References

- [JS Assignment (W3Schools)](https://www.w3schools.com/js/js_assignment.asp)
- [MDN: Assignment operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
- [MDN: Logical AND assignment (&&=)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND_assignment)
- [MDN: Nullish coalescing assignment (??=)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment)
- [MDN: Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
