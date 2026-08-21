# JS BigInt

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

BigInt (ES2020) stores **integers of any size**, limited only by memory. Write `123n` or `BigInt("123")`. Do not mix with Number without converting. No decimals, no `>>>`, no `Math.*`, no `JSON.stringify`.

This section has **20** examples:

- [x] **Example 1:** Number accuracy: 15 digits [View](#js-bigint-example-01)
- [x] **Example 2:** `MAX_SAFE_INTEGER` / `MIN_SAFE_INTEGER` [View](#js-bigint-example-02)
- [x] **Example 3:** Lose precision above MAX_SAFE_INTEGER [View](#js-bigint-example-03)
- [x] **Example 4:** Lose precision below MIN_SAFE_INTEGER [View](#js-bigint-example-04)
- [x] **Example 5:** Create BigInt: `n` suffix and `BigInt()` [View](#js-bigint-example-05)
- [x] **Example 6:** 20-digit BigInt [View](#js-bigint-example-06)
- [x] **Example 7:** `BigInt()` from a Number (warning) [View](#js-bigint-example-07)
- [x] **Example 8:** `typeof` is bigint [View](#js-bigint-example-08)
- [x] **Example 9:** BigInt arithmetic [View](#js-bigint-example-09)
- [x] **Example 10:** Cannot mix BigInt and Number [View](#js-bigint-example-10)
- [x] **Example 11:** BigInt ↔ Number conversion [View](#js-bigint-example-11)
- [x] **Example 12:** No decimal BigInt; division [View](#js-bigint-example-12)
- [x] **Example 13:** Comparisons with Numbers [View](#js-bigint-example-13)
- [x] **Example 14:** BigInt bitwise AND/OR/XOR/NOT [View](#js-bigint-example-14)
- [x] **Example 15:** BigInt shifts `<<` `>>` [View](#js-bigint-example-15)
- [x] **Example 16:** Hex, octal, binary BigInt literals [View](#js-bigint-example-16)
- [x] **Example 17:** Huge hex / octal / binary BigInts [View](#js-bigint-example-17)
- [x] **Example 18:** MAX+1 === MAX+2 is true for Number [View](#js-bigint-example-18)
- [x] **Example 19:** The same values as BigInt are distinct [View](#js-bigint-example-19)
- [x] **Example 20:** JSON and Math do not accept BigInt [View](#js-bigint-example-20)

## Detailed Explanation

- [x] Numbers lose precision past **2⁵³−1**. BigInt does not.
- [x] **`typeof` is `"bigint"`** — the eighth JS type.
- [x] Prefer **`n` literals or strings** over `BigInt(someNumber)` so digits are not pre-rounded.

<a id="js-bigint-example-01"></a>

### **Example 1: Number accuracy: 15 digits**

- [x] Ordinary Numbers stay exact for **15 digits**.
- [x] The 16th digit **rounds**.

Sandbox: `code_sandbox/js-bigint/number-15-digits.html`

```javascript
let x = 999999999999999; // 15 digits
let y = 9999999999999999; // 16 digits
```

![js-bigint example 1 source](../code_sandbox/snaps/js-bigint-01-code.png)

![js-bigint example 1 result](../code_sandbox/snaps/js-bigint-01-result.png)

- [x] **Outcome:** x is exact; y becomes **10000000000000000**.

<a id="js-bigint-example-02"></a>

### **Example 2: `MAX_SAFE_INTEGER` / `MIN_SAFE_INTEGER`**

- [x] Safe integers are **±(2⁵³−1)** = **±9007199254740991**.

Sandbox: `code_sandbox/js-bigint/safe-range.html`

```javascript
let x = Number.MAX_SAFE_INTEGER;
let y = Number.MIN_SAFE_INTEGER;
```

![js-bigint example 2 source](../code_sandbox/snaps/js-bigint-02-code.png)

![js-bigint example 2 result](../code_sandbox/snaps/js-bigint-02-result.png)

- [x] **Outcome:** **9007199254740991** and **-9007199254740991**.

<a id="js-bigint-example-03"></a>

### **Example 3: Lose precision above MAX_SAFE_INTEGER**

- [x] `MAX + 10` cannot be stored exactly as a Number.

Sandbox: `code_sandbox/js-bigint/lose-high.html`

```javascript
let x = 9007199254740991;
let y = x + 10;
```

![js-bigint example 3 source](../code_sandbox/snaps/js-bigint-03-code.png)

![js-bigint example 3 result](../code_sandbox/snaps/js-bigint-03-result.png)

- [x] **Outcome:** y is **9007199254741000** (rounded), not 9007199254741001.

<a id="js-bigint-example-04"></a>

### **Example 4: Lose precision below MIN_SAFE_INTEGER**

- [x] The same rounding happens on the negative side.

Sandbox: `code_sandbox/js-bigint/lose-low.html`

```javascript
let x = -9007199254740991;
let y = x - 10;
```

![js-bigint example 4 source](../code_sandbox/snaps/js-bigint-04-code.png)

![js-bigint example 4 result](../code_sandbox/snaps/js-bigint-04-result.png)

- [x] **Outcome:** y is rounded, not exact min−10.

<a id="js-bigint-example-05"></a>

### **Example 5: Create BigInt: `n` suffix and `BigInt()`**

- [x] Two ways: an integer literal with **`n`**, or **`BigInt("...")`** with a **string**.
- [x] A string keeps every digit; a Number argument can already be rounded.

Sandbox: `code_sandbox/js-bigint/create-n-and-ctor.html`

```javascript
let x = 999999999999999n;
let y = BigInt("999999999999999");
```

![js-bigint example 5 source](../code_sandbox/snaps/js-bigint-05-code.png)

![js-bigint example 5 result](../code_sandbox/snaps/js-bigint-05-result.png)

- [x] **Outcome:** Both are **999999999999999n**. `typeof` is **bigint**.

<a id="js-bigint-example-06"></a>

### **Example 6: 20-digit BigInt**

- [x] BigInt can hold integers **larger than 15 digits** with no rounding.

Sandbox: `code_sandbox/js-bigint/create-20-digits.html`

```javascript
let x = 12345678901234567890n;
let y = BigInt("12345678901234567890");
```

![js-bigint example 6 source](../code_sandbox/snaps/js-bigint-06-code.png)

![js-bigint example 6 result](../code_sandbox/snaps/js-bigint-06-result.png)

- [x] **Outcome:** Both store **12345678901234567890n** exactly; they compare equal.

<a id="js-bigint-example-07"></a>

### **Example 7: `BigInt()` from a Number (warning)**

- [x] You **can** pass a Number, but Numbers are only accurate to **15 digits**.
- [x] `BigInt(9999999999999999)` converts the **already rounded** Number.

Sandbox: `code_sandbox/js-bigint/bigint-from-number.html`

```javascript
let x = BigInt(9999999999999999);
```

![js-bigint example 7 source](../code_sandbox/snaps/js-bigint-07-code.png)

![js-bigint example 7 result](../code_sandbox/snaps/js-bigint-07-result.png)

- [x] **Outcome:** x is **10000000000000000n** — the rounding already happened before BigInt saw it. Prefer a **string** or **`n` literal**.

<a id="js-bigint-example-08"></a>

### **Example 8: `typeof` is bigint**

- [x] `typeof` a BigInt is **`"bigint"`**.
- [x] That makes **8** primitive/object types in the language: string, number, bigint, boolean, undefined, null, symbol, object.

Sandbox: `code_sandbox/js-bigint/typeof-bigint.html`

```javascript
let x = BigInt(999999999999999);
let type = typeof x;
```

![js-bigint example 8 source](../code_sandbox/snaps/js-bigint-08-code.png)

![js-bigint example 8 result](../code_sandbox/snaps/js-bigint-08-result.png)

- [x] **Outcome:** type is **"bigint"**.

<a id="js-bigint-example-09"></a>

### **Example 9: BigInt arithmetic**

- [x] BigInt supports `+ - * / % **` and `++ --`.
- [x] **Division truncates** toward zero (no fractional BigInt).

Sandbox: `code_sandbox/js-bigint/multiply.html`

```javascript
let x = 9007199254740995n;
let y = 9007199254740995n;
let z = x * y;
```

![js-bigint example 9 source](../code_sandbox/snaps/js-bigint-09-code.png)

![js-bigint example 9 result](../code_sandbox/snaps/js-bigint-09-result.png)

- [x] **Outcome:** z is the exact product **8114963775263029770004520090025n**.

<a id="js-bigint-example-10"></a>

### **Example 10: Cannot mix BigInt and Number**

- [x] `10n + 5` throws **TypeError**. Convert **explicitly** first.
- [x] This demo catches the error, then shows the fix: `Number(x) + y`.

Sandbox: `code_sandbox/js-bigint/mix-error.html`

```javascript
let x = 10n;
let y = 5;
// let z = x + y;  // TypeError
let z = Number(x) + y;
```

![js-bigint example 10 source](../code_sandbox/snaps/js-bigint-10-code.png)

![js-bigint example 10 result](../code_sandbox/snaps/js-bigint-10-result.png)

- [x] **Outcome:** Mixing throws **TypeError**. `Number(10n) + 5` is **15**.

<a id="js-bigint-example-11"></a>

### **Example 11: BigInt ↔ Number conversion**

- [x] `Number(bigint)` and `BigInt(number)` convert.
- [x] A **huge** BigInt can become **Infinity** or a **rounded** Number.

Sandbox: `code_sandbox/js-bigint/convert.html`

```javascript
let largeNumber = BigInt("12345678901234567890");
let num = Number(largeNumber);
```

![js-bigint example 11 source](../code_sandbox/snaps/js-bigint-11-code.png)

![js-bigint example 11 result](../code_sandbox/snaps/js-bigint-11-result.png)

- [x] **Outcome:** The Number is **1.2345678901234568e+19** — precision is already lost.

<a id="js-bigint-example-12"></a>

### **Example 12: No decimal BigInt; division**

- [x] `1.5n` is a **SyntaxError**. BigInt is **integers only**.
- [x] `5n / 2` is a TypeError (mixed types). `5n / 2n` is **2n** (truncated). `Number(5n) / 2` is **2.5**.

Sandbox: `code_sandbox/js-bigint/no-decimals.html`

```javascript
let x = 5n;
let y = Number(x) / 2;
```

![js-bigint example 12 source](../code_sandbox/snaps/js-bigint-12-code.png)

![js-bigint example 12 result](../code_sandbox/snaps/js-bigint-12-result.png)

- [x] **Outcome:** `Number(5n) / 2` is **2.5**. `5n / 2n` is **2n**. `1.5n` does not parse.

<a id="js-bigint-example-13"></a>

### **Example 13: Comparisons with Numbers**

- [x] Relational operators **can** mix types: `10n > 5` is true.
- [x] `===` is **false** across types. `==` is **true** if the values match.

Sandbox: `code_sandbox/js-bigint/compare.html`

```javascript
let x = 10n > 5n;
let y = 10n === 10;
let z = 10n == 10;
```

![js-bigint example 13 source](../code_sandbox/snaps/js-bigint-13-code.png)

![js-bigint example 13 result](../code_sandbox/snaps/js-bigint-13-result.png)

- [x] **Outcome:** **true**, **false**, **true**.

<a id="js-bigint-example-14"></a>

### **Example 14: BigInt bitwise AND/OR/XOR/NOT**

- [x] Bitwise ops need **both** sides BigInt.
- [x] `5n` is `0101`; `3n` is `0011`.

Sandbox: `code_sandbox/js-bigint/bitwise.html`

```javascript
let a = 5n;
let b = 3n;
let x = a & b;
let y = a | b;
let z = a ^ b;
let n = ~a;
```

![js-bigint example 14 source](../code_sandbox/snaps/js-bigint-14-code.png)

![js-bigint example 14 result](../code_sandbox/snaps/js-bigint-14-result.png)

- [x] **Outcome:** **1n**, **7n**, **6n**, **-6n**.

<a id="js-bigint-example-15"></a>

### **Example 15: BigInt shifts `<<` `>>`**

- [x] Only **`<<`** and **`>>`**. Both operands must be BigInt; shift counts must be **non-negative**.
- [x] **`>>>` is not allowed** on BigInt (throws TypeError).

Sandbox: `code_sandbox/js-bigint/shift.html`

```javascript
let big = 10n;
let x = big << 2n;
let y = big >> 1n;
```

![js-bigint example 15 source](../code_sandbox/snaps/js-bigint-15-code.png)

![js-bigint example 15 result](../code_sandbox/snaps/js-bigint-15-result.png)

- [x] **Outcome:** `10n << 2n` is **40n**; `10n >> 1n` is **5n**. `>>>` throws **TypeError**.

<a id="js-bigint-example-16"></a>

### **Example 16: Hex, octal, binary BigInt literals**

- [x] `256n`, `0o400n`, `0x100n`, `0b100000000n` are the **same** value.

Sandbox: `code_sandbox/js-bigint/bases.html`

```javascript
let num = 256n;
let oct = 0o400n;
let hex = 0x100n;
let bin = 0b100000000n;
```

![js-bigint example 16 source](../code_sandbox/snaps/js-bigint-16-code.png)

![js-bigint example 16 result](../code_sandbox/snaps/js-bigint-16-result.png)

- [x] **Outcome:** All four are **256n**.

<a id="js-bigint-example-17"></a>

### **Example 17: Huge hex / octal / binary BigInts**

- [x] The same prefixes work for integers far beyond Number range.

Sandbox: `code_sandbox/js-bigint/bases-huge.html`

```javascript
let hex = 0x20000000000003n;
let oct = 0o400000000000000003n;
let bin = 0b100000000000000000000000000000000000000000000000000011n;
```

![js-bigint example 17 source](../code_sandbox/snaps/js-bigint-17-code.png)

![js-bigint example 17 result](../code_sandbox/snaps/js-bigint-17-result.png)

- [x] **Outcome:** Each prints as a large **…n** integer — no rounding.

<a id="js-bigint-example-18"></a>

### **Example 18: MAX+1 === MAX+2 is true for Number**

- [x] Rounding can make **different** integers compare equal as Numbers.
- [x] `9007199254740992 === 9007199254740993` is **true** — a security/logic hazard.

Sandbox: `code_sandbox/js-bigint/unsafe-eq-number.html`

```javascript
9007199254740992 === 9007199254740993;
```

![js-bigint example 18 source](../code_sandbox/snaps/js-bigint-18-code.png)

![js-bigint example 18 result](../code_sandbox/snaps/js-bigint-18-result.png)

- [x] **Outcome:** **true** — both round to the same Number.

<a id="js-bigint-example-19"></a>

### **Example 19: The same values as BigInt are distinct**

- [x] BigInt keeps every digit, so those two values are **not** equal.

Sandbox: `code_sandbox/js-bigint/unsafe-eq-bigint.html`

```javascript
9007199254740992n === 9007199254740993n;
```

![js-bigint example 19 source](../code_sandbox/snaps/js-bigint-19-code.png)

![js-bigint example 19 result](../code_sandbox/snaps/js-bigint-19-result.png)

- [x] **Outcome:** **false**.

<a id="js-bigint-example-20"></a>

### **Example 20: JSON and Math do not accept BigInt**

- [x] **`Math.sqrt`** (and other Math functions) do **not** take BigInt.
- [x] **`JSON.stringify(1n)`** throws **TypeError**.

Sandbox: `code_sandbox/js-bigint/json-math-limits.html`

```javascript
JSON.stringify(1n);
Math.sqrt(16n);
```

![js-bigint example 20 source](../code_sandbox/snaps/js-bigint-20-code.png)

![js-bigint example 20 result](../code_sandbox/snaps/js-bigint-20-result.png)

- [x] **Outcome:** Both throw **TypeError**. Convert with `Number(...)` only when the value fits.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-bigint/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you write a BigInt?

<details>
<summary>Answer</summary>

- [x] A literal with **`n`**, or **`BigInt("digits")`**.

</details>

### Question 2: What is `typeof 1n`?

<details>
<summary>Answer</summary>

- [x] **"bigint"**.

</details>

### Question 3: What happens if you write `10n + 5`?

<details>
<summary>Answer</summary>

- [x] **TypeError**. Convert with `Number(10n) + 5` or `10n + 5n`.

</details>

### Question 4: What is `5n / 2n`?

<details>
<summary>Answer</summary>

- [x] **2n** — integer division truncates. There is no `1.5n`.

</details>

### Question 5: Is `10n === 10`?

<details>
<summary>Answer</summary>

- [x] **false** (types differ). `10n == 10` is **true**.

</details>

### Question 6: Does BigInt support `>>>`?

<details>
<summary>Answer</summary>

- [x] **No.** Only `<<` and `>>`. `>>>` throws TypeError.

</details>

### Question 7: Why is `BigInt(9999999999999999)` wrong?

<details>
<summary>Answer</summary>

- [x] The Number is **already rounded** to 10000000000000000 before conversion.

</details>

### Question 8: Can `JSON.stringify` serialize a BigInt?

<details>
<summary>Answer</summary>

- [x] **No** — it throws TypeError.

</details>

### Question 9: Can `Math.sqrt` take a BigInt?

<details>
<summary>Answer</summary>

- [x] **No**.

</details>

### Question 10: Why is `9007199254740992 === 9007199254740993` true?

<details>
<summary>Answer</summary>

- [x] Both round to the same Number. As BigInts they are **not** equal.

</details>

### Question 11: Are hex/octal/binary BigInt literals allowed?

<details>
<summary>Answer</summary>

- [x] Yes: `0x100n`, `0o400n`, `0b100000000n`.

</details>

</details>

## Summary

Use BigInt for integers that must stay exact past 15 digits. Create with `n` or `BigInt("...")`, convert explicitly before mixing with Number, skip decimals/Math/JSON, and remember `===` is false against a Number even when `==` is true.

## References

- [JS BigInt (W3Schools)](https://www.w3schools.com/js/js_bigint.asp)
- [MDN: BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
- [MDN: Number.MAX_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)
