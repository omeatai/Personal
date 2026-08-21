# JS Number Methods

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Instance methods (`toString`, `toFixed`, …) work on **any number**. Static methods (`Number.isInteger`, …) are called on **`Number`**, not on a variable. Global `Number()` / `parseInt` / `parseFloat` convert values. The page repeats `isInteger` and `isSafeInteger` at the bottom; those duplicates are covered once here, plus a TypeError demo for calling a static method on a value.

This section has **19** examples:

- [x] **Example 1:** `toString()` [View](#js-number-methods-example-01)
- [x] **Example 2:** `toString(2)` radix [View](#js-number-methods-example-02)
- [x] **Example 3:** `toExponential()` [View](#js-number-methods-example-03)
- [x] **Example 4:** `toFixed()` [View](#js-number-methods-example-04)
- [x] **Example 5:** `toPrecision()` [View](#js-number-methods-example-05)
- [x] **Example 6:** `valueOf()` [View](#js-number-methods-example-06)
- [x] **Example 7:** `Number()` conversions [View](#js-number-methods-example-07)
- [x] **Example 8:** `Number(new Date("1970-01-01"))` [View](#js-number-methods-example-08)
- [x] **Example 9:** `Number(new Date("1970-01-02"))` [View](#js-number-methods-example-09)
- [x] **Example 10:** `Number(new Date("2017-09-30"))` [View](#js-number-methods-example-10)
- [x] **Example 11:** `parseInt()` [View](#js-number-methods-example-11)
- [x] **Example 12:** `parseFloat()` [View](#js-number-methods-example-12)
- [x] **Example 13:** `Number.isInteger()` [View](#js-number-methods-example-13)
- [x] **Example 14:** `Number.isFinite()` [View](#js-number-methods-example-14)
- [x] **Example 15:** `Number.isNaN()` [View](#js-number-methods-example-15)
- [x] **Example 16:** `Number.isSafeInteger()` [View](#js-number-methods-example-16)
- [x] **Example 17:** `Number.parseFloat()` [View](#js-number-methods-example-17)
- [x] **Example 18:** `Number.parseInt()` [View](#js-number-methods-example-18)
- [x] **Example 19:** Static methods are not on variables [View](#js-number-methods-example-19)

## Detailed Explanation

- [x] **Instance vs static** — `x.toFixed(2)` vs `Number.isInteger(x)`.
- [x] **`toFixed(2)`** for money; **`toPrecision`** for significant digits; **`toExponential`** for scientific notation.
- [x] **`Number.isNaN`** is the right NaN test (`NaN === NaN` is false).

<a id="js-number-methods-example-01"></a>

### **Example 1: `toString()`**

- [x] **`toString()`** returns a number as a **string**.
- [x] It works on **literals**, **variables**, and **expressions**. A literal needs parentheses: `(123).toString()`.

Sandbox: `code_sandbox/js-number-methods/tostring.html`

```javascript
let x = 123;
x.toString();
(123).toString();
(100 + 23).toString();
```

![js-number-methods example 1 source](../code_sandbox/snaps/js-number-methods-01-code.png)

![js-number-methods example 1 result](../code_sandbox/snaps/js-number-methods-01-result.png)

- [x] **Outcome:** All three return **"123"** (a string).

<a id="js-number-methods-example-02"></a>

### **Example 2: `toString(2)` radix**

- [x] An optional **radix** converts the number to that base.
- [x] `123.toString(2)` is the **binary** representation of 123.

Sandbox: `code_sandbox/js-number-methods/tostring-radix.html`

```javascript
let x = 123;
let text = x.toString(2);
```

![js-number-methods example 2 source](../code_sandbox/snaps/js-number-methods-02-code.png)

![js-number-methods example 2 result](../code_sandbox/snaps/js-number-methods-02-result.png)

- [x] **Outcome:** text is **"1111011"** (123 in binary).

<a id="js-number-methods-example-03"></a>

### **Example 3: `toExponential()`**

- [x] **`toExponential(n)`** returns a string in **exponential notation**, rounded to **n** digits after the decimal.
- [x] The parameter is **optional**. Omit it and JavaScript does **not** round the same way.

Sandbox: `code_sandbox/js-number-methods/toexponential.html`

```javascript
let x = 9.656;
x.toExponential(2);
x.toExponential(4);
x.toExponential(6);
```

![js-number-methods example 3 source](../code_sandbox/snaps/js-number-methods-03-code.png)

![js-number-methods example 3 result](../code_sandbox/snaps/js-number-methods-03-result.png)

- [x] **Outcome:** With 2, 4, and 6 digits you get **9.66e+0**, **9.6560e+0**, **9.656000e+0**.

<a id="js-number-methods-example-04"></a>

### **Example 4: `toFixed()`**

- [x] **`toFixed(n)`** returns a string with **n** digits after the decimal (rounded).
- [x] **`toFixed(2)`** is the usual choice for **money**.

Sandbox: `code_sandbox/js-number-methods/tofixed.html`

```javascript
let x = 9.656;
x.toFixed(0);
x.toFixed(2);
x.toFixed(4);
x.toFixed(6);
```

![js-number-methods example 4 source](../code_sandbox/snaps/js-number-methods-04-code.png)

![js-number-methods example 4 result](../code_sandbox/snaps/js-number-methods-04-result.png)

- [x] **Outcome:** Results: **10**, **9.66**, **9.6560**, **9.656000** (all strings).

<a id="js-number-methods-example-05"></a>

### **Example 5: `toPrecision()`**

- [x] **`toPrecision(n)`** returns a string with **n significant digits** (total length), not “digits after the point”.
- [x] With no argument it returns the same as a normal string conversion.

Sandbox: `code_sandbox/js-number-methods/toprecision.html`

```javascript
let x = 9.656;
x.toPrecision();
x.toPrecision(2);
x.toPrecision(4);
x.toPrecision(6);
```

![js-number-methods example 5 source](../code_sandbox/snaps/js-number-methods-05-code.png)

![js-number-methods example 5 result](../code_sandbox/snaps/js-number-methods-05-result.png)

- [x] **Outcome:** Results: **9.656**, **9.7**, **9.656**, **9.65600**.

<a id="js-number-methods-example-06"></a>

### **Example 6: `valueOf()`**

- [x] **`valueOf()`** returns a number as a **number** (the primitive).
- [x] JavaScript calls it **internally** to unwrap Number objects. There is **no reason** to call it in your code.
- [x] Every data type has `valueOf()` and `toString()`.

Sandbox: `code_sandbox/js-number-methods/valueof.html`

```javascript
let x = 123;
x.valueOf();
(123).valueOf();
(100 + 23).valueOf();
```

![js-number-methods example 6 source](../code_sandbox/snaps/js-number-methods-06-code.png)

![js-number-methods example 6 result](../code_sandbox/snaps/js-number-methods-06-result.png)

- [x] **Outcome:** All three expressions are the primitive **123**.

<a id="js-number-methods-example-07"></a>

### **Example 7: `Number()` conversions**

- [x] **`Number()`**, **`parseFloat()`**, and **`parseInt()`** are **global** methods (not `x.Number()`).
- [x] `Number` converts the **whole** value. Spaces around a number are OK. Commas, extra text, or two numbers → **NaN**.
- [x] `true` → **1**, `false` → **0**.

Sandbox: `code_sandbox/js-number-methods/number-convert.html`

```javascript
Number(true);
Number(false);
Number("10");
Number("  10");
Number("10  ");
Number(" 10  ");
Number("10.33");
Number("10,33");
Number("10 33");
Number("John");
```

![js-number-methods example 7 source](../code_sandbox/snaps/js-number-methods-07-code.png)

![js-number-methods example 7 result](../code_sandbox/snaps/js-number-methods-07-result.png)

- [x] **Outcome:** **1**, **0**, **10**, **10**, **10**, **10**, **10.33**, then **NaN** for comma, space-inside, and John.

<a id="js-number-methods-example-08"></a>

### **Example 8: `Number(new Date("1970-01-01"))`**

- [x] `Number(date)` is milliseconds since **1 Jan 1970 UTC** (Unix epoch).
- [x] The date-only ISO string is treated as **UTC midnight**, so this is **0**.

Sandbox: `code_sandbox/js-number-methods/number-date-epoch.html`

```javascript
Number(new Date("1970-01-01"));
```

![js-number-methods example 8 source](../code_sandbox/snaps/js-number-methods-08-code.png)

![js-number-methods example 8 result](../code_sandbox/snaps/js-number-methods-08-result.png)

- [x] **Outcome:** **0** — the epoch itself.

<a id="js-number-methods-example-09"></a>

### **Example 9: `Number(new Date("1970-01-02"))`**

- [x] One day is **86400000** milliseconds (24 × 60 × 60 × 1000).

Sandbox: `code_sandbox/js-number-methods/number-date-next-day.html`

```javascript
Number(new Date("1970-01-02"));
```

![js-number-methods example 9 source](../code_sandbox/snaps/js-number-methods-09-code.png)

![js-number-methods example 9 result](../code_sandbox/snaps/js-number-methods-09-result.png)

- [x] **Outcome:** **86400000**.

<a id="js-number-methods-example-10"></a>

### **Example 10: `Number(new Date("2017-09-30"))`**

- [x] Any date converts to its epoch milliseconds.
- [x] This is useful for **comparing** or **sorting** dates as numbers.

Sandbox: `code_sandbox/js-number-methods/number-date-2017.html`

```javascript
Number(new Date("2017-09-30"));
```

![js-number-methods example 10 source](../code_sandbox/snaps/js-number-methods-10-code.png)

![js-number-methods example 10 result](../code_sandbox/snaps/js-number-methods-10-result.png)

- [x] **Outcome:** **1506729600000** (UTC midnight on that day).

<a id="js-number-methods-example-11"></a>

### **Example 11: `parseInt()`**

- [x] **`parseInt()`** reads a string and returns a **whole number**.
- [x] Spaces are allowed. Only the **first number** is used. A trailing decimal is **truncated**, not rounded.
- [x] `"years 10"` starts with letters → **NaN**.

Sandbox: `code_sandbox/js-number-methods/parseint.html`

```javascript
parseInt("-10");
parseInt("-10.33");
parseInt("10");
parseInt("10.33");
parseInt("10 20 30");
parseInt("10 years");
parseInt("years 10");
```

![js-number-methods example 11 source](../code_sandbox/snaps/js-number-methods-11-code.png)

![js-number-methods example 11 result](../code_sandbox/snaps/js-number-methods-11-result.png)

- [x] **Outcome:** **-10**, **-10**, **10**, **10**, **10**, **10**, **NaN**.

<a id="js-number-methods-example-12"></a>

### **Example 12: `parseFloat()`**

- [x] **`parseFloat()`** keeps the **decimal** part.
- [x] Same “first number / leading junk → NaN” rules as `parseInt`.

Sandbox: `code_sandbox/js-number-methods/parsefloat.html`

```javascript
parseFloat("10");
parseFloat("10.33");
parseFloat("10 20 30");
parseFloat("10 years");
parseFloat("years 10");
```

![js-number-methods example 12 source](../code_sandbox/snaps/js-number-methods-12-code.png)

![js-number-methods example 12 result](../code_sandbox/snaps/js-number-methods-12-result.png)

- [x] **Outcome:** **10**, **10.33**, **10**, **10**, **NaN**.

<a id="js-number-methods-example-13"></a>

### **Example 13: `Number.isInteger()`**

- [x] Static methods live on **`Number`**, not on a value. Call **`Number.isInteger(x)`**, never `x.isInteger()`.
- [x] Returns **true** only for an integer (no fractional part).

Sandbox: `code_sandbox/js-number-methods/isinteger.html`

```javascript
Number.isInteger(10);
Number.isInteger(10.5);
```

![js-number-methods example 13 source](../code_sandbox/snaps/js-number-methods-13-code.png)

![js-number-methods example 13 result](../code_sandbox/snaps/js-number-methods-13-result.png)

- [x] **Outcome:** **true** for 10; **false** for 10.5.

<a id="js-number-methods-example-14"></a>

### **Example 14: `Number.isFinite()`**

- [x] **`Number.isFinite(x)`** is **true** when x is a finite number — not **Infinity**, **−Infinity**, or **NaN**.
- [x] Unlike global `isFinite`, it does **not** coerce strings: `Number.isFinite("123")` is **false**.

Sandbox: `code_sandbox/js-number-methods/isfinite.html`

```javascript
Number.isFinite(123);
```

![js-number-methods example 14 source](../code_sandbox/snaps/js-number-methods-14-code.png)

![js-number-methods example 14 result](../code_sandbox/snaps/js-number-methods-14-result.png)

- [x] **Outcome:** **true** for 123; **false** for Infinity and NaN.

<a id="js-number-methods-example-15"></a>

### **Example 15: `Number.isNaN()`**

- [x] **`Number.isNaN(x)`** is **true** only if x is **NaN**.
- [x] You **cannot** test NaN with `==` or `===` (`NaN === NaN` is false). Prefer `Number.isNaN`.
- [x] Unlike global `isNaN`, it does **not** coerce: `Number.isNaN("NaN")` is **false**.

Sandbox: `code_sandbox/js-number-methods/isnan.html`

```javascript
Number.isNaN(123);
```

![js-number-methods example 15 source](../code_sandbox/snaps/js-number-methods-15-code.png)

![js-number-methods example 15 result](../code_sandbox/snaps/js-number-methods-15-result.png)

- [x] **Outcome:** **false** for 123; **true** for NaN. `NaN === NaN` is **false**.

<a id="js-number-methods-example-16"></a>

### **Example 16: `Number.isSafeInteger()`**

- [x] A **safe integer** is exactly representable as a double: from **−(2⁵³−1)** to **+(2⁵³−1)**.
- [x] **9007199254740991** is safe. **9007199254740992** is not.
- [x] A huge literal like `12345678901234567890` is **not** a safe integer (it already rounded as a Number).

Sandbox: `code_sandbox/js-number-methods/issafeinteger.html`

```javascript
Number.isSafeInteger(10);
Number.isSafeInteger(12345678901234567890);
```

![js-number-methods example 16 source](../code_sandbox/snaps/js-number-methods-16-code.png)

![js-number-methods example 16 result](../code_sandbox/snaps/js-number-methods-16-result.png)

- [x] **Outcome:** **true** for 10 and 2⁵³−1; **false** for the 20-digit literal and 2⁵³.

<a id="js-number-methods-example-17"></a>

### **Example 17: `Number.parseFloat()`**

- [x] **`Number.parseFloat`** is the same function as global **`parseFloat`**.
- [x] It exists so code can avoid globals (modules / non-browser JS).

Sandbox: `code_sandbox/js-number-methods/number-parsefloat.html`

```javascript
Number.parseFloat("10");
Number.parseFloat("10.33");
Number.parseFloat("10 20 30");
Number.parseFloat("10 years");
Number.parseFloat("years 10");
```

![js-number-methods example 17 source](../code_sandbox/snaps/js-number-methods-17-code.png)

![js-number-methods example 17 result](../code_sandbox/snaps/js-number-methods-17-result.png)

- [x] **Outcome:** **10**, **10.33**, **10**, **10**, **NaN** — same as `parseFloat`.

<a id="js-number-methods-example-18"></a>

### **Example 18: `Number.parseInt()`**

- [x] **`Number.parseInt`** is the same function as global **`parseInt`**.

Sandbox: `code_sandbox/js-number-methods/number-parseint.html`

```javascript
Number.parseInt("-10");
Number.parseInt("-10.33");
Number.parseInt("10");
Number.parseInt("10.33");
Number.parseInt("10 20 30");
Number.parseInt("10 years");
Number.parseInt("years 10");
```

![js-number-methods example 18 source](../code_sandbox/snaps/js-number-methods-18-code.png)

![js-number-methods example 18 result](../code_sandbox/snaps/js-number-methods-18-result.png)

- [x] **Outcome:** Same results as `parseInt`: **-10**, **-10**, **10**, **10**, **10**, **10**, **NaN**.

<a id="js-number-methods-example-19"></a>

### **Example 19: Static methods are not on variables**

- [x] `Number.isInteger` belongs to the **Number object**.
- [x] Calling **`x.isInteger()`** on a number variable throws **TypeError: x.isInteger is not a function**.
- [x] The page repeats `isInteger` / `isSafeInteger` at the bottom; those Tryits are the same as Examples 13 and 16.

Sandbox: `code_sandbox/js-number-methods/static-not-on-value.html`

```javascript
let x = 10;
x.isInteger(); // TypeError
```

![js-number-methods example 19 source](../code_sandbox/snaps/js-number-methods-19-code.png)

![js-number-methods example 19 result](../code_sandbox/snaps/js-number-methods-19-result.png)

- [x] **Outcome:** The sandbox catches the error: **TypeError** — use `Number.isInteger(x)` instead.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-number-methods/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `(123).toString()` return?

<details>
<summary>Answer</summary>

- [x] The string **"123"**. Parentheses are required on a literal.

</details>

### Question 2: What is `(9.656).toFixed(2)`?

<details>
<summary>Answer</summary>

- [x] **"9.66"** — a string, rounded, two decimal places. Use it for money.

</details>

### Question 3: How does `toPrecision(2)` differ from `toFixed(2)`?

<details>
<summary>Answer</summary>

- [x] `toPrecision` counts **significant digits** (9.656 → **9.7**).
- [x] `toFixed` counts **digits after the decimal**.

</details>

### Question 4: What is `Number(true)` and `Number("10,33")`?

<details>
<summary>Answer</summary>

- [x] **1** and **NaN**. Commas are not part of a JS number.

</details>

### Question 5: What is `Number(new Date("1970-01-01"))`?

<details>
<summary>Answer</summary>

- [x] **0** — milliseconds at the Unix epoch (UTC).

</details>

### Question 6: What is `parseInt("10.33")` vs `parseFloat("10.33")`?

<details>
<summary>Answer</summary>

- [x] **10** (truncated) vs **10.33**.

</details>

### Question 7: What is `parseInt("years 10")`?

<details>
<summary>Answer</summary>

- [x] **NaN** — the string must **start** with a number (optional sign/spaces).

</details>

### Question 8: Why not write `x.isInteger()`?

<details>
<summary>Answer</summary>

- [x] **TypeError** — call **`Number.isInteger(x)`**.

</details>

### Question 9: What is a safe integer?

<details>
<summary>Answer</summary>

- [x] An integer from **−(2⁵³−1)** to **2⁵³−1**.
- [x] `Number.isSafeInteger(9007199254740992)` is **false**.

</details>

### Question 10: Are `Number.parseInt` and `parseInt` different?

<details>
<summary>Answer</summary>

- [x] **No.** Same function; the Number form avoids globals.

</details>

### Question 11: Should you call `valueOf()` yourself?

<details>
<summary>Answer</summary>

- [x] **No.** JavaScript uses it internally to unwrap Number objects.

</details>

### Question 12: What is `Number.isNaN(NaN)` vs `NaN === NaN`?

<details>
<summary>Answer</summary>

- [x] **true** vs **false**. Prefer `Number.isNaN`.

</details>

</details>

## Summary

Use instance methods to format numbers as strings (`toFixed`, `toPrecision`, `toString`). Use `Number()`, `parseInt`, and `parseFloat` to convert. Use `Number.isInteger` / `isFinite` / `isNaN` / `isSafeInteger` as **static** checks. Do not call those on a variable.

## References

- [JS Number Methods (W3Schools)](https://www.w3schools.com/js/js_number_methods.asp)
- [MDN: Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
- [MDN: Number.prototype.toFixed()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)
- [MDN: Number.isNaN()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)
