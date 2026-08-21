# JS Type Conversion

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Conversion is explicit: Number(), String(), Boolean(), unary +, parseInt, parseFloat, and toString / toFixed / toExponential / toPrecision. Number("3.14") is 3.14; Number("") and Number(" ") are 0; Number("John") and Number("99 88") are NaN. parseInt/parseFloat can parse a prefix where Number cannot. Date-part getters return numbers you can toString; getMonth is 0–11 so add 1 for 1–12. The conversion table is one Example per original value. Surprises: Boolean("0") is true, Number([]) is 0, Number(null) is 0, Number(undefined) is NaN, empty arrays are truthy.

This section has **70** examples:

- [x] **Example 1:** Number("3.14") [View](#js-type-conversion-example-01)
- [x] **Example 2:** Number(Math.PI) [View](#js-type-conversion-example-02)
- [x] **Example 3:** Number(" ") [View](#js-type-conversion-example-03)
- [x] **Example 4:** Number("") [View](#js-type-conversion-example-04)
- [x] **Example 5:** Number("99 88") — does not convert [View](#js-type-conversion-example-05)
- [x] **Example 6:** Number("John") — does not convert [View](#js-type-conversion-example-06)
- [x] **Example 7:** parseFloat("10.33") [View](#js-type-conversion-example-07)
- [x] **Example 8:** parseInt("10.33") [View](#js-type-conversion-example-08)
- [x] **Example 9:** unary + on "5" [View](#js-type-conversion-example-09)
- [x] **Example 10:** unary + on "John" is NaN [View](#js-type-conversion-example-10)
- [x] **Example 11:** String(x) from a number variable [View](#js-type-conversion-example-11)
- [x] **Example 12:** String(123) [View](#js-type-conversion-example-12)
- [x] **Example 13:** String(100 + 23) [View](#js-type-conversion-example-13)
- [x] **Example 14:** x.toString() [View](#js-type-conversion-example-14)
- [x] **Example 15:** (123).toString() [View](#js-type-conversion-example-15)
- [x] **Example 16:** (100 + 23).toString() [View](#js-type-conversion-example-16)
- [x] **Example 17:** toExponential() [View](#js-type-conversion-example-17)
- [x] **Example 18:** toFixed(2) [View](#js-type-conversion-example-18)
- [x] **Example 19:** toPrecision(4) [View](#js-type-conversion-example-19)
- [x] **Example 20:** Number(date) — ms since epoch [View](#js-type-conversion-example-20)
- [x] **Example 21:** String(Date()) — Date() as a function [View](#js-type-conversion-example-21)
- [x] **Example 22:** Date().toString() — already a string [View](#js-type-conversion-example-22)
- [x] **Example 23:** getFullYear().toString() [View](#js-type-conversion-example-23)
- [x] **Example 24:** getMonth().toString() — 0-based [View](#js-type-conversion-example-24)
- [x] **Example 25:** getDate().toString() [View](#js-type-conversion-example-25)
- [x] **Example 26:** getDay().toString() — weekday 0–6 [View](#js-type-conversion-example-26)
- [x] **Example 27:** getHours().toString() [View](#js-type-conversion-example-27)
- [x] **Example 28:** getMinutes().toString() — 0–59 (not 0–23) [View](#js-type-conversion-example-28)
- [x] **Example 29:** getSeconds().toString() [View](#js-type-conversion-example-29)
- [x] **Example 30:** getMilliseconds().toString() [View](#js-type-conversion-example-30)
- [x] **Example 31:** (getMonth()+1).toString() — 1–12 [View](#js-type-conversion-example-31)
- [x] **Example 32:** toLocaleString month:'long' [View](#js-type-conversion-example-32)
- [x] **Example 33:** Number(false) is 0 [View](#js-type-conversion-example-33)
- [x] **Example 34:** Number(true) is 1 [View](#js-type-conversion-example-34)
- [x] **Example 35:** String(false) is "false" [View](#js-type-conversion-example-35)
- [x] **Example 36:** String(true) is "true" [View](#js-type-conversion-example-36)
- [x] **Example 37:** false.toString() is "false" [View](#js-type-conversion-example-37)
- [x] **Example 38:** true.toString() is "true" [View](#js-type-conversion-example-38)
- [x] **Example 39:** 5 + null — null becomes 0 [View](#js-type-conversion-example-39)
- [x] **Example 40:** "5" + null — null becomes "null" [View](#js-type-conversion-example-40)
- [x] **Example 41:** "5" + 2 — 2 becomes "2" [View](#js-type-conversion-example-41)
- [x] **Example 42:** "5" - 2 — "5" becomes 5 [View](#js-type-conversion-example-42)
- [x] **Example 43:** "5" * "2" — both become numbers [View](#js-type-conversion-example-43)
- [x] **Example 44:** Automatic toString — object → "[object Object]" [View](#js-type-conversion-example-44)
- [x] **Example 45:** Automatic toString — array → "1,2,3,4" [View](#js-type-conversion-example-45)
- [x] **Example 46:** Automatic toString — Date [View](#js-type-conversion-example-46)
- [x] **Example 47:** Automatic toString — 123 → "123" [View](#js-type-conversion-example-47)
- [x] **Example 48:** Automatic toString — true → "true" [View](#js-type-conversion-example-48)
- [x] **Example 49:** Convert false [View](#js-type-conversion-example-49)
- [x] **Example 50:** Convert true [View](#js-type-conversion-example-50)
- [x] **Example 51:** Convert 0 [View](#js-type-conversion-example-51)
- [x] **Example 52:** Convert 1 [View](#js-type-conversion-example-52)
- [x] **Example 53:** Convert "0" [View](#js-type-conversion-example-53)
- [x] **Example 54:** Convert "000" [View](#js-type-conversion-example-54)
- [x] **Example 55:** Convert "1" [View](#js-type-conversion-example-55)
- [x] **Example 56:** Convert NaN [View](#js-type-conversion-example-56)
- [x] **Example 57:** Convert Infinity [View](#js-type-conversion-example-57)
- [x] **Example 58:** Convert -Infinity [View](#js-type-conversion-example-58)
- [x] **Example 59:** Convert "" [View](#js-type-conversion-example-59)
- [x] **Example 60:** Convert "20" [View](#js-type-conversion-example-60)
- [x] **Example 61:** Convert "twenty" [View](#js-type-conversion-example-61)
- [x] **Example 62:** Convert [ ] [View](#js-type-conversion-example-62)
- [x] **Example 63:** Convert [20] [View](#js-type-conversion-example-63)
- [x] **Example 64:** Convert [10,20] [View](#js-type-conversion-example-64)
- [x] **Example 65:** Convert ["twenty"] [View](#js-type-conversion-example-65)
- [x] **Example 66:** Convert ["ten","twenty"] [View](#js-type-conversion-example-66)
- [x] **Example 67:** Convert function(){} [View](#js-type-conversion-example-67)
- [x] **Example 68:** Convert { } [View](#js-type-conversion-example-68)
- [x] **Example 69:** Convert null [View](#js-type-conversion-example-69)
- [x] **Example 70:** Convert undefined [View](#js-type-conversion-example-70)

## Detailed Explanation

- [x] **Number()** / **String()** / **Boolean()** are explicit. Unary **`+`** is a number cast.
- [x] `Number("")` and `Number(" ")` are **0**. `Number("99 88")` is **NaN**. `parseFloat("99 88")` is **99**.
- [x] Date **Number(d)** equals **getTime()**. Date() without new is already a **string of now**.
- [x] Table rows (not collapsed): false, true, 0, 1, "0", "000", "1", NaN, ±Infinity, "", "20", "twenty", [], [20], [10,20], function, {}, null, undefined.
- [x] Red surprises: **Boolean("0") true**, **Number([]) 0**, **Boolean([]) true**, **Number(null) 0**.

<a id="js-type-conversion-example-01"></a>

### **Example 1: Number("3.14")**

- [x] A numeric string converts to that number.

Sandbox: `code_sandbox/js-type-conversion/number-3-14.html`

```javascript
Number("3.14");
```

![js-type-conversion example 1 source](../code_sandbox/snaps/js-type-conversion-01-code.png)

![js-type-conversion example 1 result](../code_sandbox/snaps/js-type-conversion-01-result.png)

- [x] **Outcome:** Number("3.14") is **3.14**.

<a id="js-type-conversion-example-02"></a>

### **Example 2: Number(Math.PI)**

- [x] Number() on an already-numeric value returns that number.

Sandbox: `code_sandbox/js-type-conversion/number-math-pi.html`

```javascript
Number(Math.PI);
```

![js-type-conversion example 2 source](../code_sandbox/snaps/js-type-conversion-02-code.png)

![js-type-conversion example 2 result](../code_sandbox/snaps/js-type-conversion-02-result.png)

- [x] **Outcome:** Number(Math.PI) is **3.141592653589793**.

<a id="js-type-conversion-example-03"></a>

### **Example 3: Number(" ")**

- [x] A string of **whitespace** converts to **0**.

Sandbox: `code_sandbox/js-type-conversion/number-space.html`

```javascript
Number(" ");
```

![js-type-conversion example 3 source](../code_sandbox/snaps/js-type-conversion-03-code.png)

![js-type-conversion example 3 result](../code_sandbox/snaps/js-type-conversion-03-result.png)

- [x] **Outcome:** Number(" ") is **0**.

<a id="js-type-conversion-example-04"></a>

### **Example 4: Number("")**

- [x] An **empty string** converts to **0**.

Sandbox: `code_sandbox/js-type-conversion/number-empty.html`

```javascript
Number("");
```

![js-type-conversion example 4 source](../code_sandbox/snaps/js-type-conversion-04-code.png)

![js-type-conversion example 4 result](../code_sandbox/snaps/js-type-conversion-04-result.png)

- [x] **Outcome:** Number("") is **0**.

<a id="js-type-conversion-example-05"></a>

### **Example 5: Number("99 88") — does not convert**

- [x] A string with an **internal space** is not a numeric string → **NaN**.

Sandbox: `code_sandbox/js-type-conversion/number-99-88.html`

```javascript
Number("99 88");
```

![js-type-conversion example 5 source](../code_sandbox/snaps/js-type-conversion-05-code.png)

![js-type-conversion example 5 result](../code_sandbox/snaps/js-type-conversion-05-result.png)

- [x] **Outcome:** Number("99 88") is **NaN**.

<a id="js-type-conversion-example-06"></a>

### **Example 6: Number("John") — does not convert**

- [x] A **non-numeric** string → **NaN**.

Sandbox: `code_sandbox/js-type-conversion/number-john.html`

```javascript
Number("John");
```

![js-type-conversion example 6 source](../code_sandbox/snaps/js-type-conversion-06-code.png)

![js-type-conversion example 6 result](../code_sandbox/snaps/js-type-conversion-06-result.png)

- [x] **Outcome:** Number("John") is **NaN**.

<a id="js-type-conversion-example-07"></a>

### **Example 7: parseFloat("10.33")**

- [x] **parseFloat** parses a leading float. Trailing junk may be ignored (unlike Number()).

Sandbox: `code_sandbox/js-type-conversion/parsefloat.html`

```javascript
parseFloat("10.33");
parseFloat("99 88");
```

![js-type-conversion example 7 source](../code_sandbox/snaps/js-type-conversion-07-code.png)

![js-type-conversion example 7 result](../code_sandbox/snaps/js-type-conversion-07-result.png)

- [x] **Outcome:** parseFloat("10.33") is **10.33**. parseFloat("99 88") is **99** (Number("99 88") was NaN).

<a id="js-type-conversion-example-08"></a>

### **Example 8: parseInt("10.33")**

- [x] **parseInt** parses a leading **integer** (stops at the decimal point).

Sandbox: `code_sandbox/js-type-conversion/parseint.html`

```javascript
parseInt("10.33");
parseInt("99 88");
```

![js-type-conversion example 8 source](../code_sandbox/snaps/js-type-conversion-08-code.png)

![js-type-conversion example 8 result](../code_sandbox/snaps/js-type-conversion-08-result.png)

- [x] **Outcome:** parseInt("10.33") is **10**. parseInt("99 88") is **99**.

<a id="js-type-conversion-example-09"></a>

### **Example 9: unary + on "5"**

- [x] Unary **`+`** converts a numeric string to a number.

Sandbox: `code_sandbox/js-type-conversion/unary-plus-5.html`

```javascript
let y = "5";
let x = + y;
```

![js-type-conversion example 9 source](../code_sandbox/snaps/js-type-conversion-09-code.png)

![js-type-conversion example 9 result](../code_sandbox/snaps/js-type-conversion-09-result.png)

- [x] **Outcome:** y is **"5"** (string). x is **5** (number).

<a id="js-type-conversion-example-10"></a>

### **Example 10: unary + on "John" is NaN**

- [x] If unary `+` cannot convert, the result is still a **number**, but the value is **NaN**.

Sandbox: `code_sandbox/js-type-conversion/unary-plus-john.html`

```javascript
let y = "John";
let x = + y;
```

![js-type-conversion example 10 source](../code_sandbox/snaps/js-type-conversion-10-code.png)

![js-type-conversion example 10 result](../code_sandbox/snaps/js-type-conversion-10-result.png)

- [x] **Outcome:** x is **NaN**. typeof is **"number"**.

<a id="js-type-conversion-example-11"></a>

### **Example 11: String(x) from a number variable**

- [x] Global **`String()`** converts any value to a string.

Sandbox: `code_sandbox/js-type-conversion/string-variable.html`

```javascript
let x = 123;
String(x);
```

![js-type-conversion example 11 source](../code_sandbox/snaps/js-type-conversion-11-code.png)

![js-type-conversion example 11 result](../code_sandbox/snaps/js-type-conversion-11-result.png)

- [x] **Outcome:** String(x) is **"123"**. typeof is **"string"**.

<a id="js-type-conversion-example-12"></a>

### **Example 12: String(123)**

- [x] String() on a number **literal**.

Sandbox: `code_sandbox/js-type-conversion/string-literal.html`

```javascript
String(123);
```

![js-type-conversion example 12 source](../code_sandbox/snaps/js-type-conversion-12-code.png)

![js-type-conversion example 12 result](../code_sandbox/snaps/js-type-conversion-12-result.png)

- [x] **Outcome:** String(123) is **"123"**.

<a id="js-type-conversion-example-13"></a>

### **Example 13: String(100 + 23)**

- [x] String() on an **expression** (adds first, then stringifies).

Sandbox: `code_sandbox/js-type-conversion/string-expression.html`

```javascript
String(100 + 23);
```

![js-type-conversion example 13 source](../code_sandbox/snaps/js-type-conversion-13-code.png)

![js-type-conversion example 13 result](../code_sandbox/snaps/js-type-conversion-13-result.png)

- [x] **Outcome:** String(100 + 23) is **"123"**.

<a id="js-type-conversion-example-14"></a>

### **Example 14: x.toString()**

- [x] Number **`toString()`** does the same as String(x) for a number.

Sandbox: `code_sandbox/js-type-conversion/tostring-variable.html`

```javascript
let x = 123;
x.toString();
```

![js-type-conversion example 14 source](../code_sandbox/snaps/js-type-conversion-14-code.png)

![js-type-conversion example 14 result](../code_sandbox/snaps/js-type-conversion-14-result.png)

- [x] **Outcome:** x.toString() is **"123"**.

<a id="js-type-conversion-example-15"></a>

### **Example 15: (123).toString()**

- [x] Parentheses are required on a **literal**: `(123).toString()`.

Sandbox: `code_sandbox/js-type-conversion/tostring-literal.html`

```javascript
(123).toString();
```

![js-type-conversion example 15 source](../code_sandbox/snaps/js-type-conversion-15-code.png)

![js-type-conversion example 15 result](../code_sandbox/snaps/js-type-conversion-15-result.png)

- [x] **Outcome:** (123).toString() is **"123"**.

<a id="js-type-conversion-example-16"></a>

### **Example 16: (100 + 23).toString()**

- [x] toString on an expression.

Sandbox: `code_sandbox/js-type-conversion/tostring-expression.html`

```javascript
(100 + 23).toString();
```

![js-type-conversion example 16 source](../code_sandbox/snaps/js-type-conversion-16-code.png)

![js-type-conversion example 16 result](../code_sandbox/snaps/js-type-conversion-16-result.png)

- [x] **Outcome:** (100 + 23).toString() is **"123"**.

<a id="js-type-conversion-example-17"></a>

### **Example 17: toExponential()**

- [x] **toExponential()** returns a string in **exponential** notation.

Sandbox: `code_sandbox/js-type-conversion/toexponential.html`

```javascript
let x = 123;
x.toExponential();
```

![js-type-conversion example 17 source](../code_sandbox/snaps/js-type-conversion-17-code.png)

![js-type-conversion example 17 result](../code_sandbox/snaps/js-type-conversion-17-result.png)

- [x] **Outcome:** this engine printed **"1.23e+2"** for 123.

<a id="js-type-conversion-example-18"></a>

### **Example 18: toFixed(2)**

- [x] **toFixed(n)** is a string with **n** digits after the decimal (rounded).

Sandbox: `code_sandbox/js-type-conversion/tofixed.html`

```javascript
let x = 123.456;
x.toFixed(2);
```

![js-type-conversion example 18 source](../code_sandbox/snaps/js-type-conversion-18-code.png)

![js-type-conversion example 18 result](../code_sandbox/snaps/js-type-conversion-18-result.png)

- [x] **Outcome:** toFixed(2) is **"123.46"**.

<a id="js-type-conversion-example-19"></a>

### **Example 19: toPrecision(4)**

- [x] **toPrecision(n)** is a string with **n** significant digits.

Sandbox: `code_sandbox/js-type-conversion/toprecision.html`

```javascript
let x = 123.456;
x.toPrecision(4);
```

![js-type-conversion example 19 source](../code_sandbox/snaps/js-type-conversion-19-code.png)

![js-type-conversion example 19 result](../code_sandbox/snaps/js-type-conversion-19-result.png)

- [x] **Outcome:** toPrecision(4) is **"123.5"**.

<a id="js-type-conversion-example-20"></a>

### **Example 20: Number(date) — ms since epoch**

- [x] **Number(date)** is the same millisecond count as **`getTime()`**.
- [x] Fixed instant so the snap is stable.

Sandbox: `code_sandbox/js-type-conversion/date-to-number.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
Number(d);
d.getTime();
```

![js-type-conversion example 20 source](../code_sandbox/snaps/js-type-conversion-20-code.png)

![js-type-conversion example 20 result](../code_sandbox/snaps/js-type-conversion-20-result.png)

- [x] **Outcome:** Both are **1616686245123**.

<a id="js-type-conversion-example-21"></a>

### **Example 21: String(Date()) — Date() as a function**

- [x] **`Date()`** (no `new`) already returns a **string** of **now**.
- [x] String(Date()) stringifies that string (no change). Snap is the **current local** clock.

Sandbox: `code_sandbox/js-type-conversion/string-date-now.html`

```javascript
String(Date());
```

![js-type-conversion example 21 source](../code_sandbox/snaps/js-type-conversion-21-code.png)

![js-type-conversion example 21 result](../code_sandbox/snaps/js-type-conversion-21-result.png)

- [x] **Outcome:** The snap shows this engine's **current local** date/time string.

<a id="js-type-conversion-example-22"></a>

### **Example 22: Date().toString() — already a string**

- [x] `Date()` returns a string, and strings have **toString()** (identity).

Sandbox: `code_sandbox/js-type-conversion/date-fn-tostring.html`

```javascript
Date().toString();
```

![js-type-conversion example 22 source](../code_sandbox/snaps/js-type-conversion-22-code.png)

![js-type-conversion example 22 result](../code_sandbox/snaps/js-type-conversion-22-result.png)

- [x] **Outcome:** The snap shows this engine's **current local** date/time string (same family as String(Date())).

<a id="js-type-conversion-example-23"></a>

### **Example 23: getFullYear().toString()**

- [x] Date-part getters return **numbers**. **toString()** makes a string.
- [x] W3Schools Tryit uses now; this sandbox uses the **fixed** instant.

Sandbox: `code_sandbox/js-type-conversion/getfullyear-tostring.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
d.getFullYear().toString();
```

![js-type-conversion example 23 source](../code_sandbox/snaps/js-type-conversion-23-code.png)

![js-type-conversion example 23 result](../code_sandbox/snaps/js-type-conversion-23-result.png)

- [x] **Outcome:** getFullYear is **2021**. toString is **"2021"**.

<a id="js-type-conversion-example-24"></a>

### **Example 24: getMonth().toString() — 0-based**

- [x] `getMonth()` is **0–11**. March is **2**.

Sandbox: `code_sandbox/js-type-conversion/getmonth-tostring.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
d.getMonth().toString();
```

![js-type-conversion example 24 source](../code_sandbox/snaps/js-type-conversion-24-code.png)

![js-type-conversion example 24 result](../code_sandbox/snaps/js-type-conversion-24-result.png)

- [x] **Outcome:** getMonth is **2**. toString is **"2"**.

<a id="js-type-conversion-example-25"></a>

### **Example 25: getDate().toString()**

- [x] `getDate()` is the local **day of month** (1–31).

Sandbox: `code_sandbox/js-type-conversion/getdate-tostring.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
d.getDate().toString();
```

![js-type-conversion example 25 source](../code_sandbox/snaps/js-type-conversion-25-code.png)

![js-type-conversion example 25 result](../code_sandbox/snaps/js-type-conversion-25-result.png)

- [x] **Outcome:** getDate is **25**. toString is **"25"**.

<a id="js-type-conversion-example-26"></a>

### **Example 26: getDay().toString() — weekday 0–6**

- [x] `getDay()` is the local **weekday**. **0 is Sunday**. This instant is Thursday.

Sandbox: `code_sandbox/js-type-conversion/getday-tostring.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
d.getDay().toString();
```

![js-type-conversion example 26 source](../code_sandbox/snaps/js-type-conversion-26-code.png)

![js-type-conversion example 26 result](../code_sandbox/snaps/js-type-conversion-26-result.png)

- [x] **Outcome:** getDay is **4**. toString is **"4"**.

<a id="js-type-conversion-example-27"></a>

### **Example 27: getHours().toString()**

- [x] `getHours()` is local **0–23**. This UTC 15:30 is **09** Mountain (UTC−6).

Sandbox: `code_sandbox/js-type-conversion/gethours-tostring.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
d.getHours().toString();
```

![js-type-conversion example 27 source](../code_sandbox/snaps/js-type-conversion-27-code.png)

![js-type-conversion example 27 result](../code_sandbox/snaps/js-type-conversion-27-result.png)

- [x] **Outcome:** getHours is **9**. toString is **"9"**.

<a id="js-type-conversion-example-28"></a>

### **Example 28: getMinutes().toString() — 0–59 (not 0–23)**

- [x] The W3Schools table says getMinutes 0–23; the real range is **0–59**.

Sandbox: `code_sandbox/js-type-conversion/getminutes-tostring.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
d.getMinutes().toString();
```

![js-type-conversion example 28 source](../code_sandbox/snaps/js-type-conversion-28-code.png)

![js-type-conversion example 28 result](../code_sandbox/snaps/js-type-conversion-28-result.png)

- [x] **Outcome:** getMinutes is **30**. toString is **"30"**.

<a id="js-type-conversion-example-29"></a>

### **Example 29: getSeconds().toString()**

- [x] `getSeconds()` is **0–59**.

Sandbox: `code_sandbox/js-type-conversion/getseconds-tostring.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
d.getSeconds().toString();
```

![js-type-conversion example 29 source](../code_sandbox/snaps/js-type-conversion-29-code.png)

![js-type-conversion example 29 result](../code_sandbox/snaps/js-type-conversion-29-result.png)

- [x] **Outcome:** getSeconds is **45**. toString is **"45"**.

<a id="js-type-conversion-example-30"></a>

### **Example 30: getMilliseconds().toString()**

- [x] `getMilliseconds()` is **0–999**.

Sandbox: `code_sandbox/js-type-conversion/getmilliseconds-tostring.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
d.getMilliseconds().toString();
```

![js-type-conversion example 30 source](../code_sandbox/snaps/js-type-conversion-30-code.png)

![js-type-conversion example 30 result](../code_sandbox/snaps/js-type-conversion-30-result.png)

- [x] **Outcome:** getMilliseconds is **123**. toString is **"123"**.

<a id="js-type-conversion-example-31"></a>

### **Example 31: (getMonth()+1).toString() — 1–12**

- [x] Add **1** to getMonth for a **1–12** month number.

Sandbox: `code_sandbox/js-type-conversion/month-plus-one.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
(d.getMonth() + 1).toString();
```

![js-type-conversion example 31 source](../code_sandbox/snaps/js-type-conversion-31-code.png)

![js-type-conversion example 31 result](../code_sandbox/snaps/js-type-conversion-31-result.png)

- [x] **Outcome:** getMonth()+1 is **3**. toString is **"3"**.

<a id="js-type-conversion-example-32"></a>

### **Example 32: toLocaleString month:'long'**

- [x] `toLocaleString` with `{ month: 'long' }` is the **month name**.

Sandbox: `code_sandbox/js-type-conversion/month-long-name.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
d.toLocaleString('default', { month: 'long' });
```

![js-type-conversion example 32 source](../code_sandbox/snaps/js-type-conversion-32-code.png)

![js-type-conversion example 32 result](../code_sandbox/snaps/js-type-conversion-32-result.png)

- [x] **Outcome:** This engine printed **"March"**.

<a id="js-type-conversion-example-33"></a>

### **Example 33: Number(false) is 0**

- [x] **Number(false)** is **0**.

Sandbox: `code_sandbox/js-type-conversion/number-false.html`

```javascript
Number(false);
```

![js-type-conversion example 33 source](../code_sandbox/snaps/js-type-conversion-33-code.png)

![js-type-conversion example 33 result](../code_sandbox/snaps/js-type-conversion-33-result.png)

- [x] **Outcome:** Number(false) is **0**.

<a id="js-type-conversion-example-34"></a>

### **Example 34: Number(true) is 1**

- [x] **Number(true)** is **1**.

Sandbox: `code_sandbox/js-type-conversion/number-true.html`

```javascript
Number(true);
```

![js-type-conversion example 34 source](../code_sandbox/snaps/js-type-conversion-34-code.png)

![js-type-conversion example 34 result](../code_sandbox/snaps/js-type-conversion-34-result.png)

- [x] **Outcome:** Number(true) is **1**.

<a id="js-type-conversion-example-35"></a>

### **Example 35: String(false) is "false"**

- [x] **String(false)** is the string **"false"**.

Sandbox: `code_sandbox/js-type-conversion/string-false.html`

```javascript
String(false);
```

![js-type-conversion example 35 source](../code_sandbox/snaps/js-type-conversion-35-code.png)

![js-type-conversion example 35 result](../code_sandbox/snaps/js-type-conversion-35-result.png)

- [x] **Outcome:** String(false) is **"false"**.

<a id="js-type-conversion-example-36"></a>

### **Example 36: String(true) is "true"**

- [x] **String(true)** is the string **"true"**.

Sandbox: `code_sandbox/js-type-conversion/string-true.html`

```javascript
String(true);
```

![js-type-conversion example 36 source](../code_sandbox/snaps/js-type-conversion-36-code.png)

![js-type-conversion example 36 result](../code_sandbox/snaps/js-type-conversion-36-result.png)

- [x] **Outcome:** String(true) is **"true"**.

<a id="js-type-conversion-example-37"></a>

### **Example 37: false.toString() is "false"**

- [x] Boolean **toString** matches String().

Sandbox: `code_sandbox/js-type-conversion/false-tostring.html`

```javascript
false.toString();
```

![js-type-conversion example 37 source](../code_sandbox/snaps/js-type-conversion-37-code.png)

![js-type-conversion example 37 result](../code_sandbox/snaps/js-type-conversion-37-result.png)

- [x] **Outcome:** false.toString() is **"false"**.

<a id="js-type-conversion-example-38"></a>

### **Example 38: true.toString() is "true"**

- [x] Boolean **toString** matches String().

Sandbox: `code_sandbox/js-type-conversion/true-tostring.html`

```javascript
true.toString();
```

![js-type-conversion example 38 source](../code_sandbox/snaps/js-type-conversion-38-code.png)

![js-type-conversion example 38 result](../code_sandbox/snaps/js-type-conversion-38-result.png)

- [x] **Outcome:** true.toString() is **"true"**.

<a id="js-type-conversion-example-39"></a>

### **Example 39: 5 + null — null becomes 0**

- [x] Automatic conversion: **null** becomes **0** in numeric `+`.

Sandbox: `code_sandbox/js-type-conversion/auto-5-plus-null.html`

```javascript
5 + null;
```

![js-type-conversion example 39 source](../code_sandbox/snaps/js-type-conversion-39-code.png)

![js-type-conversion example 39 result](../code_sandbox/snaps/js-type-conversion-39-result.png)

- [x] **Outcome:** 5 + null is **5**.

<a id="js-type-conversion-example-40"></a>

### **Example 40: "5" + null — null becomes "null"**

- [x] With string `+`, **null** becomes the string **"null"**.

Sandbox: `code_sandbox/js-type-conversion/auto-str5-plus-null.html`

```javascript
"5" + null;
```

![js-type-conversion example 40 source](../code_sandbox/snaps/js-type-conversion-40-code.png)

![js-type-conversion example 40 result](../code_sandbox/snaps/js-type-conversion-40-result.png)

- [x] **Outcome:** "5" + null is **"5null"**.

<a id="js-type-conversion-example-41"></a>

### **Example 41: "5" + 2 — 2 becomes "2"**

- [x] String `+` concatenates.

Sandbox: `code_sandbox/js-type-conversion/auto-str5-plus-2.html`

```javascript
"5" + 2;
```

![js-type-conversion example 41 source](../code_sandbox/snaps/js-type-conversion-41-code.png)

![js-type-conversion example 41 result](../code_sandbox/snaps/js-type-conversion-41-result.png)

- [x] **Outcome:** "5" + 2 is **"52"**.

<a id="js-type-conversion-example-42"></a>

### **Example 42: "5" - 2 — "5" becomes 5**

- [x] `-` forces numbers.

Sandbox: `code_sandbox/js-type-conversion/auto-str5-minus-2.html`

```javascript
"5" - 2;
```

![js-type-conversion example 42 source](../code_sandbox/snaps/js-type-conversion-42-code.png)

![js-type-conversion example 42 result](../code_sandbox/snaps/js-type-conversion-42-result.png)

- [x] **Outcome:** "5" - 2 is **3**.

<a id="js-type-conversion-example-43"></a>

### **Example 43: "5" * "2" — both become numbers**

- [x] `*` forces numbers on both strings.

Sandbox: `code_sandbox/js-type-conversion/auto-str5-times-str2.html`

```javascript
"5" * "2";
```

![js-type-conversion example 43 source](../code_sandbox/snaps/js-type-conversion-43-code.png)

![js-type-conversion example 43 result](../code_sandbox/snaps/js-type-conversion-43-result.png)

- [x] **Outcome:** "5" * "2" is **10**.

<a id="js-type-conversion-example-44"></a>

### **Example 44: Automatic toString — object → "[object Object]"**

- [x] Output / string context calls **toString** on the value.

Sandbox: `code_sandbox/js-type-conversion/auto-string-object.html`

```javascript
let myVar = {name: "Fjohn"};
String(myVar);
```

![js-type-conversion example 44 source](../code_sandbox/snaps/js-type-conversion-44-code.png)

![js-type-conversion example 44 result](../code_sandbox/snaps/js-type-conversion-44-result.png)

- [x] **Outcome:** String({name:"Fjohn"}) is **"[object Object]"**.

<a id="js-type-conversion-example-45"></a>

### **Example 45: Automatic toString — array → "1,2,3,4"**

- [x] Arrays stringify as a comma list.

Sandbox: `code_sandbox/js-type-conversion/auto-string-array.html`

```javascript
let myVar = [1, 2, 3, 4];
String(myVar);
```

![js-type-conversion example 45 source](../code_sandbox/snaps/js-type-conversion-45-code.png)

![js-type-conversion example 45 result](../code_sandbox/snaps/js-type-conversion-45-result.png)

- [x] **Outcome:** String([1,2,3,4]) is **"1,2,3,4"**.

<a id="js-type-conversion-example-46"></a>

### **Example 46: Automatic toString — Date**

- [x] Dates stringify like `toString()` (local).

Sandbox: `code_sandbox/js-type-conversion/auto-string-date.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
String(d);
```

![js-type-conversion example 46 source](../code_sandbox/snaps/js-type-conversion-46-code.png)

![js-type-conversion example 46 result](../code_sandbox/snaps/js-type-conversion-46-result.png)

- [x] **Outcome:** String(d) is **"Thu Mar 25 2021 09:30:45 GMT-0600 (Mountain Daylight Time)"**.

<a id="js-type-conversion-example-47"></a>

### **Example 47: Automatic toString — 123 → "123"**

- [x] Numbers stringify in decimal.

Sandbox: `code_sandbox/js-type-conversion/auto-string-number.html`

```javascript
String(123);
```

![js-type-conversion example 47 source](../code_sandbox/snaps/js-type-conversion-47-code.png)

![js-type-conversion example 47 result](../code_sandbox/snaps/js-type-conversion-47-result.png)

- [x] **Outcome:** String(123) is **"123"**.

<a id="js-type-conversion-example-48"></a>

### **Example 48: Automatic toString — true → "true"**

- [x] Booleans stringify as **"true"** / **"false"**.

Sandbox: `code_sandbox/js-type-conversion/auto-string-true.html`

```javascript
String(true);
String(false);
```

![js-type-conversion example 48 source](../code_sandbox/snaps/js-type-conversion-48-code.png)

![js-type-conversion example 48 result](../code_sandbox/snaps/js-type-conversion-48-result.png)

- [x] **Outcome:** true → **"true"**. false → **"false"**.

<a id="js-type-conversion-example-49"></a>

### **Example 49: Convert false**

- [x] Conversion-table row: original **false**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-false.html`

```javascript
let v = false;
```

![js-type-conversion example 49 source](../code_sandbox/snaps/js-type-conversion-49-code.png)

![js-type-conversion example 49 result](../code_sandbox/snaps/js-type-conversion-49-result.png)

- [x] **Outcome:** Number → **0**. String → **"false"**. Boolean → **false**.

<a id="js-type-conversion-example-50"></a>

### **Example 50: Convert true**

- [x] Conversion-table row: original **true**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-true.html`

```javascript
let v = true;
```

![js-type-conversion example 50 source](../code_sandbox/snaps/js-type-conversion-50-code.png)

![js-type-conversion example 50 result](../code_sandbox/snaps/js-type-conversion-50-result.png)

- [x] **Outcome:** Number → **1**. String → **"true"**. Boolean → **true**.

<a id="js-type-conversion-example-51"></a>

### **Example 51: Convert 0**

- [x] Conversion-table row: original **0**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-0.html`

```javascript
let v = 0;
```

![js-type-conversion example 51 source](../code_sandbox/snaps/js-type-conversion-51-code.png)

![js-type-conversion example 51 result](../code_sandbox/snaps/js-type-conversion-51-result.png)

- [x] **Outcome:** Number → **0**. String → **"0"**. Boolean → **false**.

<a id="js-type-conversion-example-52"></a>

### **Example 52: Convert 1**

- [x] Conversion-table row: original **1**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-1.html`

```javascript
let v = 1;
```

![js-type-conversion example 52 source](../code_sandbox/snaps/js-type-conversion-52-code.png)

![js-type-conversion example 52 result](../code_sandbox/snaps/js-type-conversion-52-result.png)

- [x] **Outcome:** Number → **1**. String → **"1"**. Boolean → **true**.

<a id="js-type-conversion-example-53"></a>

### **Example 53: Convert "0"**

- [x] Conversion-table row: original **"0"**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-str-0.html`

```javascript
let v = "0";
```

![js-type-conversion example 53 source](../code_sandbox/snaps/js-type-conversion-53-code.png)

![js-type-conversion example 53 result](../code_sandbox/snaps/js-type-conversion-53-result.png)

- [x] **Outcome:** Number → **0**. String → **"0"**. Boolean → **true**.

<a id="js-type-conversion-example-54"></a>

### **Example 54: Convert "000"**

- [x] Conversion-table row: original **"000"**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-str-000.html`

```javascript
let v = "000";
```

![js-type-conversion example 54 source](../code_sandbox/snaps/js-type-conversion-54-code.png)

![js-type-conversion example 54 result](../code_sandbox/snaps/js-type-conversion-54-result.png)

- [x] **Outcome:** Number → **0**. String → **"000"**. Boolean → **true**.

<a id="js-type-conversion-example-55"></a>

### **Example 55: Convert "1"**

- [x] Conversion-table row: original **"1"**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-str-1.html`

```javascript
let v = "1";
```

![js-type-conversion example 55 source](../code_sandbox/snaps/js-type-conversion-55-code.png)

![js-type-conversion example 55 result](../code_sandbox/snaps/js-type-conversion-55-result.png)

- [x] **Outcome:** Number → **1**. String → **"1"**. Boolean → **true**.

<a id="js-type-conversion-example-56"></a>

### **Example 56: Convert NaN**

- [x] Conversion-table row: original **NaN**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-nan.html`

```javascript
let v = NaN;
```

![js-type-conversion example 56 source](../code_sandbox/snaps/js-type-conversion-56-code.png)

![js-type-conversion example 56 result](../code_sandbox/snaps/js-type-conversion-56-result.png)

- [x] **Outcome:** Number → **NaN**. String → **"NaN"**. Boolean → **false**.

<a id="js-type-conversion-example-57"></a>

### **Example 57: Convert Infinity**

- [x] Conversion-table row: original **Infinity**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-infinity.html`

```javascript
let v = Infinity;
```

![js-type-conversion example 57 source](../code_sandbox/snaps/js-type-conversion-57-code.png)

![js-type-conversion example 57 result](../code_sandbox/snaps/js-type-conversion-57-result.png)

- [x] **Outcome:** Number → **Infinity**. String → **"Infinity"**. Boolean → **true**.

<a id="js-type-conversion-example-58"></a>

### **Example 58: Convert -Infinity**

- [x] Conversion-table row: original **-Infinity**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-neginfinity.html`

```javascript
let v = -Infinity;
```

![js-type-conversion example 58 source](../code_sandbox/snaps/js-type-conversion-58-code.png)

![js-type-conversion example 58 result](../code_sandbox/snaps/js-type-conversion-58-result.png)

- [x] **Outcome:** Number → **-Infinity**. String → **"-Infinity"**. Boolean → **true**.

<a id="js-type-conversion-example-59"></a>

### **Example 59: Convert ""**

- [x] Conversion-table row: original **""**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-empty-str.html`

```javascript
let v = "";
```

![js-type-conversion example 59 source](../code_sandbox/snaps/js-type-conversion-59-code.png)

![js-type-conversion example 59 result](../code_sandbox/snaps/js-type-conversion-59-result.png)

- [x] **Outcome:** Number → **0**. String → **""**. Boolean → **false**.

<a id="js-type-conversion-example-60"></a>

### **Example 60: Convert "20"**

- [x] Conversion-table row: original **"20"**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-str-20.html`

```javascript
let v = "20";
```

![js-type-conversion example 60 source](../code_sandbox/snaps/js-type-conversion-60-code.png)

![js-type-conversion example 60 result](../code_sandbox/snaps/js-type-conversion-60-result.png)

- [x] **Outcome:** Number → **20**. String → **"20"**. Boolean → **true**.

<a id="js-type-conversion-example-61"></a>

### **Example 61: Convert "twenty"**

- [x] Conversion-table row: original **"twenty"**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-str-twenty.html`

```javascript
let v = "twenty";
```

![js-type-conversion example 61 source](../code_sandbox/snaps/js-type-conversion-61-code.png)

![js-type-conversion example 61 result](../code_sandbox/snaps/js-type-conversion-61-result.png)

- [x] **Outcome:** Number → **NaN**. String → **"twenty"**. Boolean → **true**.

<a id="js-type-conversion-example-62"></a>

### **Example 62: Convert [ ]**

- [x] Conversion-table row: original **[ ]**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-empty-arr.html`

```javascript
let v = [];
```

![js-type-conversion example 62 source](../code_sandbox/snaps/js-type-conversion-62-code.png)

![js-type-conversion example 62 result](../code_sandbox/snaps/js-type-conversion-62-result.png)

- [x] **Outcome:** Number → **0**. String → **""**. Boolean → **true**.

<a id="js-type-conversion-example-63"></a>

### **Example 63: Convert [20]**

- [x] Conversion-table row: original **[20]**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-arr-20.html`

```javascript
let v = [20];
```

![js-type-conversion example 63 source](../code_sandbox/snaps/js-type-conversion-63-code.png)

![js-type-conversion example 63 result](../code_sandbox/snaps/js-type-conversion-63-result.png)

- [x] **Outcome:** Number → **20**. String → **"20"**. Boolean → **true**.

<a id="js-type-conversion-example-64"></a>

### **Example 64: Convert [10,20]**

- [x] Conversion-table row: original **[10,20]**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-arr-10-20.html`

```javascript
let v = [10, 20];
```

![js-type-conversion example 64 source](../code_sandbox/snaps/js-type-conversion-64-code.png)

![js-type-conversion example 64 result](../code_sandbox/snaps/js-type-conversion-64-result.png)

- [x] **Outcome:** Number → **NaN**. String → **"10,20"**. Boolean → **true**.

<a id="js-type-conversion-example-65"></a>

### **Example 65: Convert ["twenty"]**

- [x] Conversion-table row: original **["twenty"]**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-arr-twenty.html`

```javascript
let v = ["twenty"];
```

![js-type-conversion example 65 source](../code_sandbox/snaps/js-type-conversion-65-code.png)

![js-type-conversion example 65 result](../code_sandbox/snaps/js-type-conversion-65-result.png)

- [x] **Outcome:** Number → **NaN**. String → **"twenty"**. Boolean → **true**.

<a id="js-type-conversion-example-66"></a>

### **Example 66: Convert ["ten","twenty"]**

- [x] Conversion-table row: original **["ten","twenty"]**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-arr-ten-twenty.html`

```javascript
let v = ["ten", "twenty"];
```

![js-type-conversion example 66 source](../code_sandbox/snaps/js-type-conversion-66-code.png)

![js-type-conversion example 66 result](../code_sandbox/snaps/js-type-conversion-66-result.png)

- [x] **Outcome:** Number → **NaN**. String → **"ten,twenty"**. Boolean → **true**.

<a id="js-type-conversion-example-67"></a>

### **Example 67: Convert function(){}**

- [x] Conversion-table row: original **function(){}**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-function.html`

```javascript
let v = function(){};
```

![js-type-conversion example 67 source](../code_sandbox/snaps/js-type-conversion-67-code.png)

![js-type-conversion example 67 result](../code_sandbox/snaps/js-type-conversion-67-result.png)

- [x] **Outcome:** Number → **NaN**. String → **"function(){}"**. Boolean → **true**.

<a id="js-type-conversion-example-68"></a>

### **Example 68: Convert { }**

- [x] Conversion-table row: original **{ }**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-object.html`

```javascript
let v = {};
```

![js-type-conversion example 68 source](../code_sandbox/snaps/js-type-conversion-68-code.png)

![js-type-conversion example 68 result](../code_sandbox/snaps/js-type-conversion-68-result.png)

- [x] **Outcome:** Number → **NaN**. String → **"[object Object]"**. Boolean → **true**.

<a id="js-type-conversion-example-69"></a>

### **Example 69: Convert null**

- [x] Conversion-table row: original **null**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-null.html`

```javascript
let v = null;
```

![js-type-conversion example 69 source](../code_sandbox/snaps/js-type-conversion-69-code.png)

![js-type-conversion example 69 result](../code_sandbox/snaps/js-type-conversion-69-result.png)

- [x] **Outcome:** Number → **0**. String → **"null"**. Boolean → **false**.

<a id="js-type-conversion-example-70"></a>

### **Example 70: Convert undefined**

- [x] Conversion-table row: original **undefined**.
- [x] **Number()**, **String()**, and **Boolean()** are separate conversions on the same value.

Sandbox: `code_sandbox/js-type-conversion/conv-undefined.html`

```javascript
let v = undefined;
```

![js-type-conversion example 70 source](../code_sandbox/snaps/js-type-conversion-70-code.png)

![js-type-conversion example 70 result](../code_sandbox/snaps/js-type-conversion-70-result.png)

- [x] **Outcome:** Number → **NaN**. String → **"undefined"**. Boolean → **false**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-type-conversion/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `Number("3.14")`?

<details>
<summary>Answer</summary>

- [x] **3.14**.

</details>

### Question 2: What is `Number("")` and `Number(" ")`?

<details>
<summary>Answer</summary>

- [x] Both **0**.

</details>

### Question 3: What is `Number("99 88")` vs `parseInt("99 88")`?

<details>
<summary>Answer</summary>

- [x] **NaN** vs **99**.

</details>

### Question 4: What is `+"John"`?

<details>
<summary>Answer</summary>

- [x] **NaN**, typeof **"number"**.

</details>

### Question 5: What is `String(100 + 23)`?

<details>
<summary>Answer</summary>

- [x] **"123"**.

</details>

### Question 6: What is `(123.456).toFixed(2)`?

<details>
<summary>Answer</summary>

- [x] **"123.46"**.

</details>

### Question 7: What is `(123.456).toPrecision(4)`?

<details>
<summary>Answer</summary>

- [x] **"123.5"**.

</details>

### Question 8: What is Number(false) / Number(true)?

<details>
<summary>Answer</summary>

- [x] **0** and **1**.

</details>

### Question 9: What is `5 + null` vs `"5" + null`?

<details>
<summary>Answer</summary>

- [x] **5** vs **"5null"**.

</details>

### Question 10: What is `Boolean("0")`?

<details>
<summary>Answer</summary>

- [x] **true** — non-empty strings are truthy, even **"0"** and **"000"**.

</details>

### Question 11: What is `Number([])` and `Boolean([])`?

<details>
<summary>Answer</summary>

- [x] **0** and **true**.

</details>

### Question 12: What is `Number(null)` vs `Number(undefined)`?

<details>
<summary>Answer</summary>

- [x] **0** vs **NaN**. Both are falsy as Boolean.

</details>

### Question 13: What is `Number([10,20])`?

<details>
<summary>Answer</summary>

- [x] **NaN**. String is **"10,20"**. Boolean **true**.

</details>

### Question 14: What is getMonth()+1 on the fixed March date?

<details>
<summary>Answer</summary>

- [x] **3**, string **"3"**. getMonth itself is **2**.

</details>

### Question 15: Is getMinutes 0–23 as the page table says?

<details>
<summary>Answer</summary>

- [x] **No.** Real range is **0–59**. This instant is **30**.

</details>


</details>

## Summary

Prefer explicit Number/String/Boolean. Remember empty strings become 0, whitespace strings become 0, and Boolean of a non-empty string is true even if that string looks like 0. The table rows are the checklist for surprises.

## References

- [JS Type Conversion (W3Schools)](https://www.w3schools.com/js/js_type_conversion.asp)
- [MDN: Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
- [MDN: parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
- [MDN: Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
