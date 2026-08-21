# JS Number Properties

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Number constants live on the **Number** object: `EPSILON`, `MAX_VALUE`, `MIN_VALUE`, safe-integer bounds, `±Infinity`, and `NaN`. Access them as **`Number.MAX_VALUE`**, never `x.MAX_VALUE`.

This section has **12** examples:

- [x] **Example 1:** `Number.EPSILON` [View](#js-number-properties-example-01)
- [x] **Example 2:** `Number.MAX_VALUE` [View](#js-number-properties-example-02)
- [x] **Example 3:** Properties are not on variables [View](#js-number-properties-example-03)
- [x] **Example 4:** `Number.MIN_VALUE` [View](#js-number-properties-example-04)
- [x] **Example 5:** `Number.MIN_SAFE_INTEGER` [View](#js-number-properties-example-05)
- [x] **Example 6:** `Number.MAX_SAFE_INTEGER` [View](#js-number-properties-example-06)
- [x] **Example 7:** `Number.POSITIVE_INFINITY` [View](#js-number-properties-example-07)
- [x] **Example 8:** POSITIVE_INFINITY on overflow [View](#js-number-properties-example-08)
- [x] **Example 9:** `Number.NEGATIVE_INFINITY` [View](#js-number-properties-example-09)
- [x] **Example 10:** NEGATIVE_INFINITY on overflow [View](#js-number-properties-example-10)
- [x] **Example 11:** `Number.NaN` [View](#js-number-properties-example-11)
- [x] **Example 12:** NaN from 100 / "Apple" [View](#js-number-properties-example-12)

## Detailed Explanation

- [x] **`MIN_VALUE`** is the smallest **positive** number, not the most negative.
- [x] **Safe integers** are `±(2⁵³−1)`.
- [x] **`x.MAX_VALUE`** is **undefined** — properties are not inherited as you might expect from a value.

<a id="js-number-properties-example-01"></a>

### **Example 1: `Number.EPSILON`**

- [x] **`Number.EPSILON`** is the difference between **1** and the next representable number above 1 (~ **2.22e-16**).
- [x] ES6. Use it as a **tolerance** when comparing floats.

Sandbox: `code_sandbox/js-number-properties/epsilon.html`

```javascript
let x = Number.EPSILON;
```

![js-number-properties example 1 source](../code_sandbox/snaps/js-number-properties-01-code.png)

![js-number-properties example 1 result](../code_sandbox/snaps/js-number-properties-01-result.png)

- [x] **Outcome:** x is **2.220446049250313e-16**.

<a id="js-number-properties-example-02"></a>

### **Example 2: `Number.MAX_VALUE`**

- [x] **`Number.MAX_VALUE`** is the **largest finite** number (~ **1.8e+308**).
- [x] Bigger results overflow to **Infinity**.

Sandbox: `code_sandbox/js-number-properties/max-value.html`

```javascript
let x = Number.MAX_VALUE;
```

![js-number-properties example 2 source](../code_sandbox/snaps/js-number-properties-02-code.png)

![js-number-properties example 2 result](../code_sandbox/snaps/js-number-properties-02-result.png)

- [x] **Outcome:** x is **1.7976931348623157e+308**.

<a id="js-number-properties-example-03"></a>

### **Example 3: Properties are not on variables**

- [x] Number properties live on **`Number`**, not on a value.
- [x] `x.MAX_VALUE` where x is **6** is **`undefined`** — it does not throw, it just is not there.

Sandbox: `code_sandbox/js-number-properties/prop-on-variable.html`

```javascript
let x = 6;
x.MAX_VALUE;
```

![js-number-properties example 3 source](../code_sandbox/snaps/js-number-properties-03-code.png)

![js-number-properties example 3 result](../code_sandbox/snaps/js-number-properties-03-result.png)

- [x] **Outcome:** **undefined** — write `Number.MAX_VALUE` instead.

<a id="js-number-properties-example-04"></a>

### **Example 4: `Number.MIN_VALUE`**

- [x] **`Number.MIN_VALUE`** is the **smallest positive** number (closest to 0), ~ **5e-324**.
- [x] It is **not** the most-negative number (that is `-Number.MAX_VALUE`).

Sandbox: `code_sandbox/js-number-properties/min-value.html`

```javascript
let x = Number.MIN_VALUE;
```

![js-number-properties example 4 source](../code_sandbox/snaps/js-number-properties-04-code.png)

![js-number-properties example 4 result](../code_sandbox/snaps/js-number-properties-04-result.png)

- [x] **Outcome:** x is **5e-324**.

<a id="js-number-properties-example-05"></a>

### **Example 5: `Number.MIN_SAFE_INTEGER`**

- [x] **`Number.MIN_SAFE_INTEGER`** is **−(2⁵³−1)** = **-9007199254740991**.
- [x] ES6 pair with `MAX_SAFE_INTEGER`.

Sandbox: `code_sandbox/js-number-properties/min-safe.html`

```javascript
let x = Number.MIN_SAFE_INTEGER;
```

![js-number-properties example 5 source](../code_sandbox/snaps/js-number-properties-05-code.png)

![js-number-properties example 5 result](../code_sandbox/snaps/js-number-properties-05-result.png)

- [x] **Outcome:** x is **-9007199254740991**.

<a id="js-number-properties-example-06"></a>

### **Example 6: `Number.MAX_SAFE_INTEGER`**

- [x] **`Number.MAX_SAFE_INTEGER`** is **2⁵³−1** = **9007199254740991**.

Sandbox: `code_sandbox/js-number-properties/max-safe.html`

```javascript
let x = Number.MAX_SAFE_INTEGER;
```

![js-number-properties example 6 source](../code_sandbox/snaps/js-number-properties-06-code.png)

![js-number-properties example 6 result](../code_sandbox/snaps/js-number-properties-06-result.png)

- [x] **Outcome:** x is **9007199254740991**.

<a id="js-number-properties-example-07"></a>

### **Example 7: `Number.POSITIVE_INFINITY`**

- [x] The constant for **Infinity**.

Sandbox: `code_sandbox/js-number-properties/pos-inf.html`

```javascript
let x = Number.POSITIVE_INFINITY;
```

![js-number-properties example 7 source](../code_sandbox/snaps/js-number-properties-07-code.png)

![js-number-properties example 7 result](../code_sandbox/snaps/js-number-properties-07-result.png)

- [x] **Outcome:** x is **Infinity**.

<a id="js-number-properties-example-08"></a>

### **Example 8: POSITIVE_INFINITY on overflow**

- [x] `1 / 0` returns **Infinity**, the same value as `Number.POSITIVE_INFINITY`.

Sandbox: `code_sandbox/js-number-properties/pos-inf-overflow.html`

```javascript
let x = 1 / 0;
```

![js-number-properties example 8 source](../code_sandbox/snaps/js-number-properties-08-code.png)

![js-number-properties example 8 result](../code_sandbox/snaps/js-number-properties-08-result.png)

- [x] **Outcome:** x is **Infinity**.

<a id="js-number-properties-example-09"></a>

### **Example 9: `Number.NEGATIVE_INFINITY`**

- [x] The constant for **−Infinity**.

Sandbox: `code_sandbox/js-number-properties/neg-inf.html`

```javascript
let x = Number.NEGATIVE_INFINITY;
```

![js-number-properties example 9 source](../code_sandbox/snaps/js-number-properties-09-code.png)

![js-number-properties example 9 result](../code_sandbox/snaps/js-number-properties-09-result.png)

- [x] **Outcome:** x is **-Infinity**.

<a id="js-number-properties-example-10"></a>

### **Example 10: NEGATIVE_INFINITY on overflow**

- [x] `-1 / 0` returns **−Infinity**.

Sandbox: `code_sandbox/js-number-properties/neg-inf-overflow.html`

```javascript
let x = -1 / 0;
```

![js-number-properties example 10 source](../code_sandbox/snaps/js-number-properties-10-code.png)

![js-number-properties example 10 result](../code_sandbox/snaps/js-number-properties-10-result.png)

- [x] **Outcome:** x is **-Infinity**.

<a id="js-number-properties-example-11"></a>

### **Example 11: `Number.NaN`**

- [x] **`Number.NaN`** is the same value as the global **`NaN`**.

Sandbox: `code_sandbox/js-number-properties/number-nan.html`

```javascript
let x = Number.NaN;
```

![js-number-properties example 11 source](../code_sandbox/snaps/js-number-properties-11-code.png)

![js-number-properties example 11 result](../code_sandbox/snaps/js-number-properties-11-result.png)

- [x] **Outcome:** x is **NaN**.

<a id="js-number-properties-example-12"></a>

### **Example 12: NaN from 100 / "Apple"**

- [x] Illegal arithmetic produces **NaN** — the same reserved value.

Sandbox: `code_sandbox/js-number-properties/nan-from-math.html`

```javascript
let x = 100 / "Apple";
```

![js-number-properties example 12 source](../code_sandbox/snaps/js-number-properties-12-code.png)

![js-number-properties example 12 result](../code_sandbox/snaps/js-number-properties-12-result.png)

- [x] **Outcome:** x is **NaN**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-number-properties/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `Number.EPSILON`?

<details>
<summary>Answer</summary>

- [x] About **2.22e-16** — the gap above 1. Use it as a float comparison tolerance.

</details>

### Question 2: What is `Number.MAX_VALUE`?

<details>
<summary>Answer</summary>

- [x] About **1.80e+308**, the largest finite number.

</details>

### Question 3: What does `(6).MAX_VALUE` return?

<details>
<summary>Answer</summary>

- [x] **undefined**. Write **`Number.MAX_VALUE`**.

</details>

### Question 4: Is `Number.MIN_VALUE` negative?

<details>
<summary>Answer</summary>

- [x] **No.** It is the smallest **positive** value (~ **5e-324**).

</details>

### Question 5: What is `Number.MAX_SAFE_INTEGER`?

<details>
<summary>Answer</summary>

- [x] **9007199254740991** (2⁵³−1).

</details>

### Question 6: What is `Number.MIN_SAFE_INTEGER`?

<details>
<summary>Answer</summary>

- [x] **-9007199254740991**.

</details>

### Question 7: What is `1 / 0`?

<details>
<summary>Answer</summary>

- [x] **Infinity**, the same as `Number.POSITIVE_INFINITY`.

</details>

### Question 8: What is `-1 / 0`?

<details>
<summary>Answer</summary>

- [x] **-Infinity** (`Number.NEGATIVE_INFINITY`).

</details>

### Question 9: What is `Number.NaN`?

<details>
<summary>Answer</summary>

- [x] The same **NaN** value as the global `NaN`.

</details>

### Question 10: When did EPSILON and safe integers arrive?

<details>
<summary>Answer</summary>

- [x] **ES6**.

</details>

</details>

## Summary

Read limits from `Number`: EPSILON for float gaps, MAX/MIN_VALUE for magnitude, MAX/MIN_SAFE_INTEGER for exact integers, and the Infinity/NaN constants. Never look those names up on a numeric variable.

## References

- [JS Number Properties (W3Schools)](https://www.w3schools.com/js/js_number_properties.asp)
- [MDN: Number.EPSILON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON)
- [MDN: Number.MAX_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)
