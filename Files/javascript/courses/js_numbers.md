# JS Numbers

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

JavaScript has **one** number type: 64-bit IEEE 754 floating point. That explains integer rounding past 15 digits, `0.2 + 0.1`, `NaN`, `Infinity`, hex literals, and why `new Number()` is a bad idea. Each Tryit on the W3Schools page is its own Example.

This section has **32** examples:

- [x] **Example 1:** Decimals and integers [View](#js-numbers-example-01)
- [x] **Example 2:** Scientific (exponent) notation [View](#js-numbers-example-02)
- [x] **Example 3:** Integer precision (15 digits) [View](#js-numbers-example-03)
- [x] **Example 4:** Floating point: 0.2 + 0.1 [View](#js-numbers-example-04)
- [x] **Example 5:** Fix floating error with multiply and divide [View](#js-numbers-example-05)
- [x] **Example 6:** Add two numbers [View](#js-numbers-example-06)
- [x] **Example 7:** Add two strings [View](#js-numbers-example-07)
- [x] **Example 8:** Number + string concatenates [View](#js-numbers-example-08)
- [x] **Example 9:** String + number concatenates [View](#js-numbers-example-09)
- [x] **Example 10:** Common mistake: "The result is: " + x + y [View](#js-numbers-example-10)
- [x] **Example 11:** Left-to-right: numbers then a string [View](#js-numbers-example-11)
- [x] **Example 12:** Numeric strings vs numbers [View](#js-numbers-example-12)
- [x] **Example 13:** Numeric strings: division [View](#js-numbers-example-13)
- [x] **Example 14:** Numeric strings: multiplication [View](#js-numbers-example-14)
- [x] **Example 15:** Numeric strings: subtraction [View](#js-numbers-example-15)
- [x] **Example 16:** Numeric strings: + still concatenates [View](#js-numbers-example-16)
- [x] **Example 17:** NaN from 100 / "Apple" [View](#js-numbers-example-17)
- [x] **Example 18:** 100 / "10" is a number [View](#js-numbers-example-18)
- [x] **Example 19:** `isNaN()` checks Not-a-Number [View](#js-numbers-example-19)
- [x] **Example 20:** NaN infects math [View](#js-numbers-example-20)
- [x] **Example 21:** NaN + string concatenates [View](#js-numbers-example-21)
- [x] **Example 22:** `typeof NaN` is number [View](#js-numbers-example-22)
- [x] **Example 23:** Overflow to Infinity [View](#js-numbers-example-23)
- [x] **Example 24:** Division by zero [View](#js-numbers-example-24)
- [x] **Example 25:** `typeof Infinity` is number [View](#js-numbers-example-25)
- [x] **Example 26:** Hexadecimal 0xFF [View](#js-numbers-example-26)
- [x] **Example 27:** `toString()` bases 2–36 [View](#js-numbers-example-27)
- [x] **Example 28:** `new Number()` vs a literal [View](#js-numbers-example-28)
- [x] **Example 29:** Literal == Number object [View](#js-numbers-example-29)
- [x] **Example 30:** Literal === Number object [View](#js-numbers-example-30)
- [x] **Example 31:** Two Number objects with == [View](#js-numbers-example-31)
- [x] **Example 32:** Two Number objects with === [View](#js-numbers-example-32)

## Detailed Explanation

- [x] **One type** — no byte/short/int/long/float. Everything is a **double** (52-bit fraction, 11-bit exponent, 1 sign bit).
- [x] **`+` is overloaded** — numbers add; if either side is a string, it concatenates. `/` `*` `-` convert numeric strings.
- [x] **NaN and Infinity** are still `typeof "number"`.
- [x] **Do not use `new Number()`** — `==` can be true while `===` is false; two Number objects compare false.

<a id="js-numbers-example-01"></a>

### **Example 1: Decimals and integers**

- [x] JavaScript has **only one number type** — there is no separate `int` vs `float`.
- [x] You may write a number **with or without** a decimal point. Both are the same `typeof`: **number**.

Sandbox: `code_sandbox/js-numbers/decimals.html`

```javascript
let x = 3.14; // A number with decimals
let y = 3; // A number without decimals
```

![js-numbers example 1 source](../code_sandbox/snaps/js-numbers-01-code.png)

![js-numbers example 1 result](../code_sandbox/snaps/js-numbers-01-result.png)

- [x] **Outcome:** x is **3.14** and y is **3**. Both have `typeof` **number**.

<a id="js-numbers-example-02"></a>

### **Example 2: Scientific (exponent) notation**

- [x] **`e`** means “times ten to the power of”. `123e5` is 123 × 10⁵ = **12300000**.
- [x] A **negative** exponent moves the point left: `123e-5` is **0.00123**.

Sandbox: `code_sandbox/js-numbers/scientific.html`

```javascript
let x = 123e5; // 12300000
let y = 123e-5; // 0.00123
```

![js-numbers example 2 source](../code_sandbox/snaps/js-numbers-02-code.png)

![js-numbers example 2 result](../code_sandbox/snaps/js-numbers-02-result.png)

- [x] **Outcome:** x is **12300000**; y is **0.00123**.

<a id="js-numbers-example-03"></a>

### **Example 3: Integer precision (15 digits)**

- [x] Integers (no period, no exponent) are accurate up to **15 digits**.
- [x] A **16-digit** integer is rounded: `9999999999999999` becomes **10000000000000000**.
- [x] This is IEEE 754 — JavaScript cannot store every integer exactly past 2⁵³−1.

Sandbox: `code_sandbox/js-numbers/integer-precision.html`

```javascript
let x = 999999999999999; // x will be 999999999999999
let y = 9999999999999999; // y will be 10000000000000000
```

![js-numbers example 3 source](../code_sandbox/snaps/js-numbers-03-code.png)

![js-numbers example 3 result](../code_sandbox/snaps/js-numbers-03-result.png)

- [x] **Outcome:** x stays **999999999999999**. y rounds to **10000000000000000**.

<a id="js-numbers-example-04"></a>

### **Example 4: Floating point: 0.2 + 0.1**

- [x] Floating-point arithmetic is **not always 100% accurate**.
- [x] `0.2` and `0.1` cannot be represented exactly in binary, so their sum is slightly off **0.3**.

Sandbox: `code_sandbox/js-numbers/float-sum.html`

```javascript
let x = 0.2 + 0.1;
```

![js-numbers example 4 source](../code_sandbox/snaps/js-numbers-04-code.png)

![js-numbers example 4 result](../code_sandbox/snaps/js-numbers-04-result.png)

- [x] **Outcome:** x is **0.30000000000000004**, not exactly 0.3. `x === 0.3` is **false**.

<a id="js-numbers-example-05"></a>

### **Example 5: Fix floating error with multiply and divide**

- [x] A common fix is to work in **tenths** (or cents), then divide back.
- [x] `(0.2 * 10 + 0.1 * 10) / 10` adds **2 + 1** as integers, then divides.

Sandbox: `code_sandbox/js-numbers/float-fix.html`

```javascript
let x = (0.2 * 10 + 0.1 * 10) / 10;
```

![js-numbers example 5 source](../code_sandbox/snaps/js-numbers-05-code.png)

![js-numbers example 5 result](../code_sandbox/snaps/js-numbers-05-result.png)

- [x] **Outcome:** x is **0.3** and `x === 0.3` is **true**.

<a id="js-numbers-example-06"></a>

### **Example 6: Add two numbers**

- [x] JavaScript uses **`+`** for both **addition** and **concatenation**.
- [x] When **both** operands are numbers, `+` **adds**.

Sandbox: `code_sandbox/js-numbers/add-numbers.html`

```javascript
let x = 10;
let y = 20;
let z = x + y;
```

![js-numbers example 6 source](../code_sandbox/snaps/js-numbers-06-code.png)

![js-numbers example 6 result](../code_sandbox/snaps/js-numbers-06-result.png)

- [x] **Outcome:** z is **30** (a number).

<a id="js-numbers-example-07"></a>

### **Example 7: Add two strings**

- [x] When **both** operands are strings, `+` **concatenates**.
- [x] `"10" + "20"` is **`"1020"`**, not 30.

Sandbox: `code_sandbox/js-numbers/add-strings.html`

```javascript
let x = "10";
let y = "20";
let z = x + y;
```

![js-numbers example 7 source](../code_sandbox/snaps/js-numbers-07-code.png)

![js-numbers example 7 result](../code_sandbox/snaps/js-numbers-07-result.png)

- [x] **Outcome:** z is **"1020"** (a string).

<a id="js-numbers-example-08"></a>

### **Example 8: Number + string concatenates**

- [x] If **either** side of `+` is a string, JavaScript **concatenates**.
- [x] `10 + "20"` becomes **`"1020"`**.

Sandbox: `code_sandbox/js-numbers/number-plus-string.html`

```javascript
let x = 10;
let y = "20";
let z = x + y;
```

![js-numbers example 8 source](../code_sandbox/snaps/js-numbers-08-code.png)

![js-numbers example 8 result](../code_sandbox/snaps/js-numbers-08-result.png)

- [x] **Outcome:** z is **"1020"**.

<a id="js-numbers-example-09"></a>

### **Example 9: String + number concatenates**

- [x] Order does not save you: a string on the **left** still concatenates.
- [x] `"10" + 20` is **`"1020"`**.

Sandbox: `code_sandbox/js-numbers/string-plus-number.html`

```javascript
let x = "10";
let y = 20;
let z = x + y;
```

![js-numbers example 9 source](../code_sandbox/snaps/js-numbers-09-code.png)

![js-numbers example 9 result](../code_sandbox/snaps/js-numbers-09-result.png)

- [x] **Outcome:** z is **"1020"**.

<a id="js-numbers-example-10"></a>

### **Example 10: Common mistake: "The result is: " + x + y**

- [x] A common mistake is expecting **30** after a label string.
- [x] Evaluation is **left to right**: first `"The result is: " + 10` becomes a string, then that string `+ 20` concatenates again.

Sandbox: `code_sandbox/js-numbers/result-is-concat.html`

```javascript
let x = 10;
let y = 20;
let z = "The result is: " + x + y;
```

![js-numbers example 10 source](../code_sandbox/snaps/js-numbers-10-code.png)

![js-numbers example 10 result](../code_sandbox/snaps/js-numbers-10-result.png)

- [x] **Outcome:** z is **"The result is: 1020"**, not "The result is: 30".

<a id="js-numbers-example-11"></a>

### **Example 11: Left-to-right: numbers then a string**

- [x] A common mistake is expecting **102030**.
- [x] First `10 + 20` **adds** (both numbers) → **30**. Then `30 + "30"` **concatenates** → **`"3030"`**.

Sandbox: `code_sandbox/js-numbers/left-to-right.html`

```javascript
let x = 10;
let y = 20;
let z = "30";
let result = x + y + z;
```

![js-numbers example 11 source](../code_sandbox/snaps/js-numbers-11-code.png)

![js-numbers example 11 result](../code_sandbox/snaps/js-numbers-11-result.png)

- [x] **Outcome:** result is **"3030"** because the interpreter works **left to right**.

<a id="js-numbers-example-12"></a>

### **Example 12: Numeric strings vs numbers**

- [x] A string can **look** numeric: `"100"` is still a **string**.
- [x] `100` (no quotes) is a **number**. `typeof` tells them apart.

Sandbox: `code_sandbox/js-numbers/numeric-content.html`

```javascript
let x = 100; // x is a number
let y = "100"; // y is a string
```

![js-numbers example 12 source](../code_sandbox/snaps/js-numbers-12-code.png)

![js-numbers example 12 result](../code_sandbox/snaps/js-numbers-12-result.png)

- [x] **Outcome:** x is number **100**; y is string **"100"**.

<a id="js-numbers-example-13"></a>

### **Example 13: Numeric strings: division**

- [x] For **numeric operations other than `+`**, JavaScript **converts** numeric strings to numbers.
- [x] `"100" / "10"` is **10**.

Sandbox: `code_sandbox/js-numbers/numeric-divide.html`

```javascript
let x = "100";
let y = "10";
let z = x / y;
```

![js-numbers example 13 source](../code_sandbox/snaps/js-numbers-13-code.png)

![js-numbers example 13 result](../code_sandbox/snaps/js-numbers-13-result.png)

- [x] **Outcome:** z is **10** (a number).

<a id="js-numbers-example-14"></a>

### **Example 14: Numeric strings: multiplication**

- [x] `*` also converts numeric strings.
- [x] `"100" * "10"` is **1000**.

Sandbox: `code_sandbox/js-numbers/numeric-multiply.html`

```javascript
let x = "100";
let y = "10";
let z = x * y;
```

![js-numbers example 14 source](../code_sandbox/snaps/js-numbers-14-code.png)

![js-numbers example 14 result](../code_sandbox/snaps/js-numbers-14-result.png)

- [x] **Outcome:** z is **1000**.

<a id="js-numbers-example-15"></a>

### **Example 15: Numeric strings: subtraction**

- [x] `-` converts numeric strings too.
- [x] `"100" - "10"` is **90**.

Sandbox: `code_sandbox/js-numbers/numeric-subtract.html`

```javascript
let x = "100";
let y = "10";
let z = x - y;
```

![js-numbers example 15 source](../code_sandbox/snaps/js-numbers-15-code.png)

![js-numbers example 15 result](../code_sandbox/snaps/js-numbers-15-result.png)

- [x] **Outcome:** z is **90**.

<a id="js-numbers-example-16"></a>

### **Example 16: Numeric strings: + still concatenates**

- [x] **`+` is the exception.** It concatenates strings instead of converting them.
- [x] `"100" + "10"` is **`"10010"`**, not 110.

Sandbox: `code_sandbox/js-numbers/numeric-add-fails.html`

```javascript
let x = "100";
let y = "10";
let z = x + y;
```

![js-numbers example 16 source](../code_sandbox/snaps/js-numbers-16-code.png)

![js-numbers example 16 result](../code_sandbox/snaps/js-numbers-16-result.png)

- [x] **Outcome:** z is **"10010"**.

<a id="js-numbers-example-17"></a>

### **Example 17: NaN from 100 / "Apple"**

- [x] **`NaN`** means **Not a Number** — the result of illegal numeric math.
- [x] Dividing by a **non-numeric** string yields **NaN**.

Sandbox: `code_sandbox/js-numbers/nan-apple.html`

```javascript
let x = 100 / "Apple";
```

![js-numbers example 17 source](../code_sandbox/snaps/js-numbers-17-code.png)

![js-numbers example 17 result](../code_sandbox/snaps/js-numbers-17-result.png)

- [x] **Outcome:** x is **NaN**.

<a id="js-numbers-example-18"></a>

### **Example 18: 100 / "10" is a number**

- [x] If the string **is** numeric, arithmetic works.
- [x] `"10"` converts; the result is **10**.

Sandbox: `code_sandbox/js-numbers/divide-numeric-string.html`

```javascript
let x = 100 / "10";
```

![js-numbers example 18 source](../code_sandbox/snaps/js-numbers-18-code.png)

![js-numbers example 18 result](../code_sandbox/snaps/js-numbers-18-result.png)

- [x] **Outcome:** x is **10**.

<a id="js-numbers-example-19"></a>

### **Example 19: `isNaN()` checks Not-a-Number**

- [x] Use global **`isNaN()`** to test whether a value is NaN.
- [x] `isNaN` of a legal number is **false**; of `100 / "Apple"` is **true**.

Sandbox: `code_sandbox/js-numbers/isnan.html`

```javascript
let x = 100 / "Apple";
isNaN(x);
```

![js-numbers example 19 source](../code_sandbox/snaps/js-numbers-19-code.png)

![js-numbers example 19 result](../code_sandbox/snaps/js-numbers-19-result.png)

- [x] **Outcome:** `isNaN(x)` is **true**. `isNaN(100 / "10")` is **false**.

<a id="js-numbers-example-20"></a>

### **Example 20: NaN infects math**

- [x] If you use **NaN** in further math, the result is also **NaN**.
- [x] `NaN + 5` is **NaN**, not 5.

Sandbox: `code_sandbox/js-numbers/nan-plus-number.html`

```javascript
let x = NaN;
let y = 5;
let z = x + y;
```

![js-numbers example 20 source](../code_sandbox/snaps/js-numbers-20-code.png)

![js-numbers example 20 result](../code_sandbox/snaps/js-numbers-20-result.png)

- [x] **Outcome:** z is **NaN**.

<a id="js-numbers-example-21"></a>

### **Example 21: NaN + string concatenates**

- [x] `+` with a **string** concatenates even when one side is NaN.
- [x] `NaN + "5"` becomes **`"NaN5"`**.

Sandbox: `code_sandbox/js-numbers/nan-plus-string.html`

```javascript
let x = NaN;
let y = "5";
let z = x + y;
```

![js-numbers example 21 source](../code_sandbox/snaps/js-numbers-21-code.png)

![js-numbers example 21 result](../code_sandbox/snaps/js-numbers-21-result.png)

- [x] **Outcome:** z is **"NaN5"**.

<a id="js-numbers-example-22"></a>

### **Example 22: `typeof NaN` is number**

- [x] **Surprise:** `typeof NaN` returns **`"number"`**.
- [x] NaN is a **numeric value** that means “this number is invalid”, not a separate type.

Sandbox: `code_sandbox/js-numbers/typeof-nan.html`

```javascript
typeof NaN;
```

![js-numbers example 22 source](../code_sandbox/snaps/js-numbers-22-code.png)

![js-numbers example 22 result](../code_sandbox/snaps/js-numbers-22-result.png)

- [x] **Outcome:** `typeof NaN` is **"number"**.

<a id="js-numbers-example-23"></a>

### **Example 23: Overflow to Infinity**

- [x] **Infinity** is what you get when a calculation exceeds the largest finite number.
- [x] Repeatedly squaring 2 eventually overflows: 2 → 4 → 16 → … → **Infinity**.

Sandbox: `code_sandbox/js-numbers/loop-infinity.html`

```javascript
let myNumber = 2;
while (myNumber != Infinity) {
  myNumber = myNumber * myNumber;
}
```

![js-numbers example 23 source](../code_sandbox/snaps/js-numbers-23-code.png)

![js-numbers example 23 result](../code_sandbox/snaps/js-numbers-23-result.png)

- [x] **Outcome:** After the loop, myNumber is **Infinity**.

<a id="js-numbers-example-24"></a>

### **Example 24: Division by zero**

- [x] In JavaScript, dividing by **0** does **not** throw. It yields **Infinity** (or **−Infinity**).
- [x] `2 / 0` → **Infinity**; `-2 / 0` → **−Infinity**.

Sandbox: `code_sandbox/js-numbers/divide-by-zero.html`

```javascript
let x = 2 / 0;
let y = -2 / 0;
```

![js-numbers example 24 source](../code_sandbox/snaps/js-numbers-24-code.png)

![js-numbers example 24 result](../code_sandbox/snaps/js-numbers-24-result.png)

- [x] **Outcome:** x is **Infinity**; y is **-Infinity**.

<a id="js-numbers-example-25"></a>

### **Example 25: `typeof Infinity` is number**

- [x] Infinity is also a **number**.
- [x] `typeof Infinity` is **"number"**.

Sandbox: `code_sandbox/js-numbers/typeof-infinity.html`

```javascript
typeof Infinity;
```

![js-numbers example 25 source](../code_sandbox/snaps/js-numbers-25-code.png)

![js-numbers example 25 result](../code_sandbox/snaps/js-numbers-25-result.png)

- [x] **Outcome:** Both Infinity and -Infinity have `typeof` **"number"**.

<a id="js-numbers-example-26"></a>

### **Example 26: Hexadecimal 0xFF**

- [x] A literal starting with **`0x`** is **hexadecimal** (base 16).
- [x] `0xFF` is **255** in decimal.
- [x] **Do not** write a number with a leading **`0`** (like `07`). Old engines treated that as **octal**; modern strict mode makes it a **SyntaxError**.

Sandbox: `code_sandbox/js-numbers/hex.html`

```javascript
let x = 0xff;
```

![js-numbers example 26 source](../code_sandbox/snaps/js-numbers-26-code.png)

![js-numbers example 26 result](../code_sandbox/snaps/js-numbers-26-result.png)

- [x] **Outcome:** x is **255**.

<a id="js-numbers-example-27"></a>

### **Example 27: `toString()` bases 2–36**

- [x] By default, JavaScript **displays** numbers in **base 10**.
- [x] **`toString(radix)`** writes the same value in another base (2–36).
- [x] Base 16 is hex, 10 decimal, 8 octal, 2 binary. Base 32 and 12 are also legal.

Sandbox: `code_sandbox/js-numbers/tostring-radix.html`

```javascript
let myNumber = 32;
myNumber.toString(32);
myNumber.toString(16);
myNumber.toString(12);
myNumber.toString(10);
myNumber.toString(8);
myNumber.toString(2);
```

![js-numbers example 27 source](../code_sandbox/snaps/js-numbers-27-code.png)

![js-numbers example 27 result](../code_sandbox/snaps/js-numbers-27-result.png)

- [x] **Outcome:** 32 in those bases is **10**, **20**, **28**, **32**, **40**, **100000**.

<a id="js-numbers-example-28"></a>

### **Example 28: `new Number()` vs a literal**

- [x] A normal number is a **primitive**: `let x = 123`.
- [x] `new Number(123)` is a **Number object** (`typeof` **object**).
- [x] **Do not** create Number objects — they slow the code and cause `==` / `===` surprises.

Sandbox: `code_sandbox/js-numbers/number-object.html`

```javascript
let x = 123;
let y = new Number(123);
```

![js-numbers example 28 source](../code_sandbox/snaps/js-numbers-28-code.png)

![js-numbers example 28 result](../code_sandbox/snaps/js-numbers-28-result.png)

- [x] **Outcome:** `typeof x` is **"number"**; `typeof y` is **"object"**.

<a id="js-numbers-example-29"></a>

### **Example 29: Literal == Number object**

- [x] `==` **coerces**. A primitive **500** equals `new Number(500)` because the object is converted.

Sandbox: `code_sandbox/js-numbers/object-loose-eq.html`

```javascript
let x = 500;
let y = new Number(500);
```

![js-numbers example 29 source](../code_sandbox/snaps/js-numbers-29-code.png)

![js-numbers example 29 result](../code_sandbox/snaps/js-numbers-29-result.png)

- [x] **Outcome:** `x == y` is **true**.

<a id="js-numbers-example-30"></a>

### **Example 30: Literal === Number object**

- [x] `===` requires the **same type**. A primitive is not an object.
- [x] `500 === new Number(500)` is **false**.

Sandbox: `code_sandbox/js-numbers/object-strict-eq.html`

```javascript
let x = 500;
let y = new Number(500);
```

![js-numbers example 30 source](../code_sandbox/snaps/js-numbers-30-code.png)

![js-numbers example 30 result](../code_sandbox/snaps/js-numbers-30-result.png)

- [x] **Outcome:** `x === y` is **false**.

<a id="js-numbers-example-31"></a>

### **Example 31: Two Number objects with ==**

- [x] Comparing **two objects** with `==` still returns **false** — objects compare by **reference**, not value.
- [x] `new Number(500) == new Number(500)` is **false**.

Sandbox: `code_sandbox/js-numbers/two-objects-loose.html`

```javascript
let x = new Number(500);
let y = new Number(500);
```

![js-numbers example 31 source](../code_sandbox/snaps/js-numbers-31-code.png)

![js-numbers example 31 result](../code_sandbox/snaps/js-numbers-31-result.png)

- [x] **Outcome:** `x == y` is **false**.

<a id="js-numbers-example-32"></a>

### **Example 32: Two Number objects with ===**

- [x] `===` on two different objects is also **false**.
- [x] This is why the page says: **do not create Number objects**.

Sandbox: `code_sandbox/js-numbers/two-objects-strict.html`

```javascript
let x = new Number(500);
let y = new Number(500);
```

![js-numbers example 32 source](../code_sandbox/snaps/js-numbers-32-code.png)

![js-numbers example 32 result](../code_sandbox/snaps/js-numbers-32-result.png)

- [x] **Outcome:** `x === y` is **false**. Two objects are never equal to each other this way.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-numbers/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How many number types does JavaScript have?

<details>
<summary>Answer</summary>

- [x] **One.** All numbers are IEEE 754 **doubles**.

</details>

### Question 2: What is `9999999999999999` stored as?

<details>
<summary>Answer</summary>

- [x] **10000000000000000** — integers are exact only up to **15 digits** / `Number.MAX_SAFE_INTEGER`.

</details>

### Question 3: What is `0.2 + 0.1`?

<details>
<summary>Answer</summary>

- [x] **0.30000000000000004**, not 0.3.
- [x] Work in tenths: `(0.2 * 10 + 0.1 * 10) / 10`.

</details>

### Question 4: What is `10 + "20"`?

<details>
<summary>Answer</summary>

- [x] **`"1020"`** — `+` concatenates when a string is involved.

</details>

### Question 5: What is `"The result is: " + 10 + 20`?

<details>
<summary>Answer</summary>

- [x] **`"The result is: 1020"`** — left to right, after the first concatenation everything is a string.

</details>

### Question 6: What is `10 + 20 + "30"`?

<details>
<summary>Answer</summary>

- [x] **`"3030"`** — first add the numbers, then concatenate.

</details>

### Question 7: What is `"100" / "10"` vs `"100" + "10"`?

<details>
<summary>Answer</summary>

- [x] Division is **10** (converted).
- [x] Addition is **`"10010"`** (concatenated).

</details>

### Question 8: What is `100 / "Apple"`?

<details>
<summary>Answer</summary>

- [x] **NaN**.
- [x] `isNaN` of that value is **true**.
- [x] `typeof NaN` is still **"number"**.

</details>

### Question 9: What is `2 / 0`?

<details>
<summary>Answer</summary>

- [x] **Infinity**.
- [x] `typeof Infinity` is **"number"**.

</details>

### Question 10: What is `0xFF`?

<details>
<summary>Answer</summary>

- [x] **255** in decimal. `0x` means hexadecimal.

</details>

### Question 11: What does `(32).toString(2)` return?

<details>
<summary>Answer</summary>

- [x] **`"100000"`** — binary.

</details>

### Question 12: Is `500 == new Number(500)` true?

<details>
<summary>Answer</summary>

- [x] **Yes** with `==`.
- [x] **No** with `===`.
- [x] Two `new Number(500)` objects compare **false** even with `==`.

</details>

</details>

## Summary

JavaScript numbers are always 64-bit floats: 15-digit integers stay exact, `0.2 + 0.1` does not, `+` concatenates strings, other operators convert numeric strings, NaN and Infinity are still numbers, `0x` is hex, and `new Number()` should be avoided.

## References

- [JS Numbers (W3Schools)](https://www.w3schools.com/js/js_numbers.asp)
- [MDN: Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
- [MDN: NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)
