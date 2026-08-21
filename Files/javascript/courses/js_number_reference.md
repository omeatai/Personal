# JS Number Reference

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Complete **Number** catalog (revised July 2025): every property and method from **`constructor`** through **`valueOf()`**. Number methods return a **new** value; they do **not** change the original number. Each table row is its own Example.

This section has **22** examples:

- [x] **Example 1:** `constructor` [View](#js-number-reference-example-01)
- [x] **Example 2:** `EPSILON` [View](#js-number-reference-example-02)
- [x] **Example 3:** `isFinite()` [View](#js-number-reference-example-03)
- [x] **Example 4:** `isInteger()` [View](#js-number-reference-example-04)
- [x] **Example 5:** `isNaN()` [View](#js-number-reference-example-05)
- [x] **Example 6:** `isSafeInteger()` [View](#js-number-reference-example-06)
- [x] **Example 7:** `MAX_SAFE_INTEGER` [View](#js-number-reference-example-07)
- [x] **Example 8:** `MIN_SAFE_INTEGER` [View](#js-number-reference-example-08)
- [x] **Example 9:** `MAX_VALUE` [View](#js-number-reference-example-09)
- [x] **Example 10:** `MIN_VALUE` [View](#js-number-reference-example-10)
- [x] **Example 11:** `NaN` [View](#js-number-reference-example-11)
- [x] **Example 12:** `NEGATIVE_INFINITY` [View](#js-number-reference-example-12)
- [x] **Example 13:** `POSITIVE_INFINITY` [View](#js-number-reference-example-13)
- [x] **Example 14:** `parseFloat()` [View](#js-number-reference-example-14)
- [x] **Example 15:** `parseInt()` [View](#js-number-reference-example-15)
- [x] **Example 16:** `prototype` [View](#js-number-reference-example-16)
- [x] **Example 17:** `toExponential(x)` [View](#js-number-reference-example-17)
- [x] **Example 18:** `toFixed(x)` [View](#js-number-reference-example-18)
- [x] **Example 19:** `toLocaleString()` [View](#js-number-reference-example-19)
- [x] **Example 20:** `toPrecision(x)` [View](#js-number-reference-example-20)
- [x] **Example 21:** `toString()` [View](#js-number-reference-example-21)
- [x] **Example 22:** `valueOf()` [View](#js-number-reference-example-22)

## Detailed Explanation

- [x] **Grain** — one Example per reference-table row.
- [x] **Static vs instance** — `Number.isInteger(x)` vs `x.toFixed(2)`.
- [x] **`toLocaleString()`** is the extra instance method that the Methods chapter did not spotlight.

<a id="js-number-reference-example-01"></a>

### **Example 1: `constructor`**

- [x] **`constructor`** is the function that created the prototype — for a number that is **`Number`**.
- [x] Rarely useful in day-to-day code.

Sandbox: `code_sandbox/js-number-reference/constructor.html`

```javascript
let x = 123;
x.constructor;
```

![js-number-reference example 1 source](../code_sandbox/snaps/js-number-reference-01-code.png)

![js-number-reference example 1 result](../code_sandbox/snaps/js-number-reference-01-result.png)

- [x] **Outcome:** `x.constructor` is the **Number** function.

<a id="js-number-reference-example-02"></a>

### **Example 2: `EPSILON`**

- [x] Difference between 1 and the next number above 1.

Sandbox: `code_sandbox/js-number-reference/epsilon.html`

```javascript
Number.EPSILON;
```

![js-number-reference example 2 source](../code_sandbox/snaps/js-number-reference-02-code.png)

![js-number-reference example 2 result](../code_sandbox/snaps/js-number-reference-02-result.png)

- [x] **Outcome:** **2.220446049250313e-16**.

<a id="js-number-reference-example-03"></a>

### **Example 3: `isFinite()`**

- [x] Static: **`Number.isFinite(value)`** — true for finite numbers only.

Sandbox: `code_sandbox/js-number-reference/isfinite.html`

```javascript
Number.isFinite(123);
Number.isFinite(Infinity);
```

![js-number-reference example 3 source](../code_sandbox/snaps/js-number-reference-03-code.png)

![js-number-reference example 3 result](../code_sandbox/snaps/js-number-reference-03-result.png)

- [x] **Outcome:** **true**, **false**.

<a id="js-number-reference-example-04"></a>

### **Example 4: `isInteger()`**

- [x] Static: **`Number.isInteger(value)`**.

Sandbox: `code_sandbox/js-number-reference/isinteger.html`

```javascript
Number.isInteger(10);
Number.isInteger(10.5);
```

![js-number-reference example 4 source](../code_sandbox/snaps/js-number-reference-04-code.png)

![js-number-reference example 4 result](../code_sandbox/snaps/js-number-reference-04-result.png)

- [x] **Outcome:** **true**, **false**.

<a id="js-number-reference-example-05"></a>

### **Example 5: `isNaN()`**

- [x] Static: **`Number.isNaN(value)`** — true only for NaN.

Sandbox: `code_sandbox/js-number-reference/isnan.html`

```javascript
Number.isNaN(123);
Number.isNaN(NaN);
```

![js-number-reference example 5 source](../code_sandbox/snaps/js-number-reference-05-code.png)

![js-number-reference example 5 result](../code_sandbox/snaps/js-number-reference-05-result.png)

- [x] **Outcome:** **false**, **true**.

<a id="js-number-reference-example-06"></a>

### **Example 6: `isSafeInteger()`**

- [x] Static: integer in **[−(2⁵³−1), 2⁵³−1]**.

Sandbox: `code_sandbox/js-number-reference/issafeinteger.html`

```javascript
Number.isSafeInteger(10);
Number.isSafeInteger(9007199254740992);
```

![js-number-reference example 6 source](../code_sandbox/snaps/js-number-reference-06-code.png)

![js-number-reference example 6 result](../code_sandbox/snaps/js-number-reference-06-result.png)

- [x] **Outcome:** **true**, **false**.

<a id="js-number-reference-example-07"></a>

### **Example 7: `MAX_SAFE_INTEGER`**

- [x] Maximum safe integer: **2⁵³−1**.

Sandbox: `code_sandbox/js-number-reference/max-safe.html`

```javascript
Number.MAX_SAFE_INTEGER;
```

![js-number-reference example 7 source](../code_sandbox/snaps/js-number-reference-07-code.png)

![js-number-reference example 7 result](../code_sandbox/snaps/js-number-reference-07-result.png)

- [x] **Outcome:** **9007199254740991**.

<a id="js-number-reference-example-08"></a>

### **Example 8: `MIN_SAFE_INTEGER`**

- [x] Minimum safe integer: **−(2⁵³−1)**.

Sandbox: `code_sandbox/js-number-reference/min-safe.html`

```javascript
Number.MIN_SAFE_INTEGER;
```

![js-number-reference example 8 source](../code_sandbox/snaps/js-number-reference-08-code.png)

![js-number-reference example 8 result](../code_sandbox/snaps/js-number-reference-08-result.png)

- [x] **Outcome:** **-9007199254740991**.

<a id="js-number-reference-example-09"></a>

### **Example 9: `MAX_VALUE`**

- [x] Largest finite number.

Sandbox: `code_sandbox/js-number-reference/max-value.html`

```javascript
Number.MAX_VALUE;
```

![js-number-reference example 9 source](../code_sandbox/snaps/js-number-reference-09-code.png)

![js-number-reference example 9 result](../code_sandbox/snaps/js-number-reference-09-result.png)

- [x] **Outcome:** **1.7976931348623157e+308**.

<a id="js-number-reference-example-10"></a>

### **Example 10: `MIN_VALUE`**

- [x] Smallest **positive** number (closest to zero).

Sandbox: `code_sandbox/js-number-reference/min-value.html`

```javascript
Number.MIN_VALUE;
```

![js-number-reference example 10 source](../code_sandbox/snaps/js-number-reference-10-code.png)

![js-number-reference example 10 result](../code_sandbox/snaps/js-number-reference-10-result.png)

- [x] **Outcome:** **5e-324**.

<a id="js-number-reference-example-11"></a>

### **Example 11: `NaN`**

- [x] Represents **"Not-a-Number"**.

Sandbox: `code_sandbox/js-number-reference/nan.html`

```javascript
Number.NaN;
```

![js-number-reference example 11 source](../code_sandbox/snaps/js-number-reference-11-code.png)

![js-number-reference example 11 result](../code_sandbox/snaps/js-number-reference-11-result.png)

- [x] **Outcome:** **NaN**.

<a id="js-number-reference-example-12"></a>

### **Example 12: `NEGATIVE_INFINITY`**

- [x] Negative infinity (overflow).

Sandbox: `code_sandbox/js-number-reference/neg-inf.html`

```javascript
Number.NEGATIVE_INFINITY;
```

![js-number-reference example 12 source](../code_sandbox/snaps/js-number-reference-12-code.png)

![js-number-reference example 12 result](../code_sandbox/snaps/js-number-reference-12-result.png)

- [x] **Outcome:** **-Infinity**.

<a id="js-number-reference-example-13"></a>

### **Example 13: `POSITIVE_INFINITY`**

- [x] Infinity (overflow).

Sandbox: `code_sandbox/js-number-reference/pos-inf.html`

```javascript
Number.POSITIVE_INFINITY;
```

![js-number-reference example 13 source](../code_sandbox/snaps/js-number-reference-13-code.png)

![js-number-reference example 13 result](../code_sandbox/snaps/js-number-reference-13-result.png)

- [x] **Outcome:** **Infinity**.

<a id="js-number-reference-example-14"></a>

### **Example 14: `parseFloat()`**

- [x] Parses a string and returns a number. Same as global `parseFloat`.

Sandbox: `code_sandbox/js-number-reference/parsefloat.html`

```javascript
Number.parseFloat("10.33 years");
```

![js-number-reference example 14 source](../code_sandbox/snaps/js-number-reference-14-code.png)

![js-number-reference example 14 result](../code_sandbox/snaps/js-number-reference-14-result.png)

- [x] **Outcome:** **10.33**.

<a id="js-number-reference-example-15"></a>

### **Example 15: `parseInt()`**

- [x] Parses a string and returns a whole number. Same as global `parseInt`.

Sandbox: `code_sandbox/js-number-reference/parseint.html`

```javascript
Number.parseInt("10.33 years");
```

![js-number-reference example 15 source](../code_sandbox/snaps/js-number-reference-15-code.png)

![js-number-reference example 15 result](../code_sandbox/snaps/js-number-reference-15-result.png)

- [x] **Outcome:** **10**.

<a id="js-number-reference-example-16"></a>

### **Example 16: `prototype`**

- [x] **`Number.prototype`** is where instance methods live (`toFixed`, `toString`, …).
- [x] You **can** add methods, but **do not** extend built-in prototypes in library code — it surprises everyone else.

Sandbox: `code_sandbox/js-number-reference/prototype.html`

```javascript
Number.prototype.twice = function () {
  return this * 2;
};
(21).twice();
```

![js-number-reference example 16 source](../code_sandbox/snaps/js-number-reference-16-code.png)

![js-number-reference example 16 result](../code_sandbox/snaps/js-number-reference-16-result.png)

- [x] **Outcome:** **42** — a demo only; prefer a plain function instead of changing `Number.prototype`.

<a id="js-number-reference-example-17"></a>

### **Example 17: `toExponential(x)`**

- [x] Exponential notation with x digits after the decimal.

Sandbox: `code_sandbox/js-number-reference/toexponential.html`

```javascript
(9.656).toExponential(2);
```

![js-number-reference example 17 source](../code_sandbox/snaps/js-number-reference-17-code.png)

![js-number-reference example 17 result](../code_sandbox/snaps/js-number-reference-17-result.png)

- [x] **Outcome:** **"9.66e+0"**.

<a id="js-number-reference-example-18"></a>

### **Example 18: `toFixed(x)`**

- [x] x digits after the decimal. Good for money.

Sandbox: `code_sandbox/js-number-reference/tofixed.html`

```javascript
(9.656).toFixed(2);
```

![js-number-reference example 18 source](../code_sandbox/snaps/js-number-reference-18-code.png)

![js-number-reference example 18 result](../code_sandbox/snaps/js-number-reference-18-result.png)

- [x] **Outcome:** **"9.66"**.

<a id="js-number-reference-example-19"></a>

### **Example 19: `toLocaleString()`**

- [x] Converts a number to a string using **locale** grouping/decimals.
- [x] Optional locale like `"de-DE"` uses a **comma** as the decimal mark.

Sandbox: `code_sandbox/js-number-reference/tolocalestring.html`

```javascript
let n = 123456.789;
n.toLocaleString();
n.toLocaleString("de-DE");
```

![js-number-reference example 19 source](../code_sandbox/snaps/js-number-reference-19-code.png)

![js-number-reference example 19 result](../code_sandbox/snaps/js-number-reference-19-result.png)

- [x] **Outcome:** Default (en) looks like **123,456.789**; German looks like **123.456,789**.

<a id="js-number-reference-example-20"></a>

### **Example 20: `toPrecision(x)`**

- [x] Format to x **significant** digits.

Sandbox: `code_sandbox/js-number-reference/toprecision.html`

```javascript
(9.656).toPrecision(2);
```

![js-number-reference example 20 source](../code_sandbox/snaps/js-number-reference-20-code.png)

![js-number-reference example 20 result](../code_sandbox/snaps/js-number-reference-20-result.png)

- [x] **Outcome:** **"9.7"**.

<a id="js-number-reference-example-21"></a>

### **Example 21: `toString()`**

- [x] Convert to a string; optional radix 2–36.

Sandbox: `code_sandbox/js-number-reference/tostring.html`

```javascript
(255).toString();
(255).toString(16);
```

![js-number-reference example 21 source](../code_sandbox/snaps/js-number-reference-21-code.png)

![js-number-reference example 21 result](../code_sandbox/snaps/js-number-reference-21-result.png)

- [x] **Outcome:** **"255"** and **"ff"**.

<a id="js-number-reference-example-22"></a>

### **Example 22: `valueOf()`**

- [x] Primitive value of a Number object. Used internally.

Sandbox: `code_sandbox/js-number-reference/valueof.html`

```javascript
let x = new Number(123);
x.valueOf();
```

![js-number-reference example 22 source](../code_sandbox/snaps/js-number-reference-22-code.png)

![js-number-reference example 22 result](../code_sandbox/snaps/js-number-reference-22-result.png)

- [x] **Outcome:** Primitive **123** (`typeof` **number**).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-number-reference/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Do number methods mutate the original?

<details>
<summary>Answer</summary>

- [x] **No.** They return a new value.

</details>

### Question 2: How do you call `isInteger`?

<details>
<summary>Answer</summary>

- [x] **`Number.isInteger(x)`**, not `x.isInteger()`.

</details>

### Question 3: What is `Number.MAX_SAFE_INTEGER`?

<details>
<summary>Answer</summary>

- [x] **9007199254740991**.

</details>

### Question 4: What is `MIN_VALUE`?

<details>
<summary>Answer</summary>

- [x] Smallest **positive** number, **5e-324**.

</details>

### Question 5: What does `parseInt` vs `parseFloat` do on `"10.33"`?

<details>
<summary>Answer</summary>

- [x] **10** vs **10.33**.

</details>

### Question 6: Should you add methods to `Number.prototype`?

<details>
<summary>Answer</summary>

- [x] Only as a demo. Prefer a **plain function** so you do not break other code.

</details>

### Question 7: What is `(9.656).toFixed(2)`?

<details>
<summary>Answer</summary>

- [x] **"9.66"**.

</details>

### Question 8: What is `(255).toString(16)`?

<details>
<summary>Answer</summary>

- [x] **"ff"**.

</details>

### Question 9: What does `toLocaleString('de-DE')` change?

<details>
<summary>Answer</summary>

- [x] Uses locale grouping and a **comma** decimal for German.

</details>

### Question 10: What does `valueOf()` return on `new Number(123)`?

<details>
<summary>Answer</summary>

- [x] The primitive **123**.

</details>

</details>

## Summary

Every Number property and method has its own Example. Format with `toFixed` / `toPrecision` / `toExponential` / `toString` / `toLocaleString`. Test with the static `is*` helpers. Read limits from the `Number.*` constants. Methods do not mutate.

## References

- [JS Number Reference (W3Schools)](https://www.w3schools.com/js/js_number_reference.asp)
- [MDN: Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
- [MDN: Number.prototype.toLocaleString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toLocaleString)
