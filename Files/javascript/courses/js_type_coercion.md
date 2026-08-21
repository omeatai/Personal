# JS Type Coercion

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Coercion is implicit conversion when operators mix types. + concatenates if either side is a string ("5"+2 is "52"). -, *, /, %, and unary + force numbers ("5"-2 is 3). Boolean contexts treat 0, "", null, undefined, NaN, and false as falsy; everything else is truthy, including {} and []. == coerces (5=="5" is true; 0==false is true). === does not (both false). A failed numeric coerce is NaN ("abc"-1).

This section has **20** examples:

- [x] **Example 1:** ('5' + '2') vs ('5' - '2') [View](#js-type-coercion-example-01)
- [x] **Example 2:** "5" + 2 — string coercion of + [View](#js-type-coercion-example-02)
- [x] **Example 3:** "5" - 2 — numeric coercion of - [View](#js-type-coercion-example-03)
- [x] **Example 4:** "5" * 2 — numeric * [View](#js-type-coercion-example-04)
- [x] **Example 5:** "5" / 2 — numeric / [View](#js-type-coercion-example-05)
- [x] **Example 6:** "5" % 2 — numeric % [View](#js-type-coercion-example-06)
- [x] **Example 7:** +"5" — unary plus to number [View](#js-type-coercion-example-07)
- [x] **Example 8:** 5 == "5" — loose equality [View](#js-type-coercion-example-08)
- [x] **Example 9:** 5 === "5" — strict equality [View](#js-type-coercion-example-09)
- [x] **Example 10:** "abc" - 1 is NaN [View](#js-type-coercion-example-10)
- [x] **Example 11:** Boolean coercion — !!0 [View](#js-type-coercion-example-11)
- [x] **Example 12:** Boolean coercion — !!"" [View](#js-type-coercion-example-12)
- [x] **Example 13:** Boolean coercion — !!null [View](#js-type-coercion-example-13)
- [x] **Example 14:** Boolean coercion — !!undefined [View](#js-type-coercion-example-14)
- [x] **Example 15:** Boolean coercion — !!NaN [View](#js-type-coercion-example-15)
- [x] **Example 16:** Boolean coercion — !!false [View](#js-type-coercion-example-16)
- [x] **Example 17:** Boolean coercion — !!{} [View](#js-type-coercion-example-17)
- [x] **Example 18:** Boolean coercion — !![] [View](#js-type-coercion-example-18)
- [x] **Example 19:** 0 == false is true; 0 === false is false [View](#js-type-coercion-example-19)
- [x] **Example 20:** "" == 0 is true [View](#js-type-coercion-example-20)

## Detailed Explanation

- [x] **Implicit** vs **explicit** (Number/String/Boolean). JS is weakly typed — mixed types rarely throw.
- [x] `+` with a string → **concat**. Other arithmetic → **numbers**.
- [x] Falsy: **0, "", null, undefined, NaN, false**. Truthy: **{}**, **[]**, and the rest.
- [x] `==` coerces. `===` does not. Prefer **===**.
- [x] `"abc" - 1` is **NaN**.

<a id="js-type-coercion-example-01"></a>

### **Example 1: ('5' + '2') vs ('5' - '2')**

- [x] **Coercion is implicit.** `+` with strings **concatenates**. `-` forces **numbers**.

Sandbox: `code_sandbox/js-type-coercion/plus-vs-minus-strings.html`

```javascript
let result1 = ('5' + '2');
let result2 = ('5' - '2');
```

![js-type-coercion example 1 source](../code_sandbox/snaps/js-type-coercion-01-code.png)

![js-type-coercion example 1 result](../code_sandbox/snaps/js-type-coercion-01-result.png)

- [x] **Outcome:** result1 is **"52"** (string). result2 is **3** (number).

<a id="js-type-coercion-example-02"></a>

### **Example 2: "5" + 2 — string coercion of +**

- [x] If **any** operand of **`+`** is a string, the other becomes a string and they **concatenate**.

Sandbox: `code_sandbox/js-type-coercion/string-plus.html`

```javascript
let x = "5" + 2;
```

![js-type-coercion example 2 source](../code_sandbox/snaps/js-type-coercion-02-code.png)

![js-type-coercion example 2 result](../code_sandbox/snaps/js-type-coercion-02-result.png)

- [x] **Outcome:** x is **"52"**. typeof is **"string"**.

<a id="js-type-coercion-example-03"></a>

### **Example 3: "5" - 2 — numeric coercion of -**

- [x] **`-`** always does numeric subtraction (after coercion).

Sandbox: `code_sandbox/js-type-coercion/numeric-minus.html`

```javascript
let x = "5" - 2;
```

![js-type-coercion example 3 source](../code_sandbox/snaps/js-type-coercion-03-code.png)

![js-type-coercion example 3 result](../code_sandbox/snaps/js-type-coercion-03-result.png)

- [x] **Outcome:** x is **3**. typeof is **"number"**.

<a id="js-type-coercion-example-04"></a>

### **Example 4: "5" * 2 — numeric ***

- [x] **`*`** coerces both sides to numbers.

Sandbox: `code_sandbox/js-type-coercion/numeric-times.html`

```javascript
let x = "5" * 2;
```

![js-type-coercion example 4 source](../code_sandbox/snaps/js-type-coercion-04-code.png)

![js-type-coercion example 4 result](../code_sandbox/snaps/js-type-coercion-04-result.png)

- [x] **Outcome:** x is **10**.

<a id="js-type-coercion-example-05"></a>

### **Example 5: "5" / 2 — numeric /**

- [x] **`/`** coerces both sides to numbers.

Sandbox: `code_sandbox/js-type-coercion/numeric-div.html`

```javascript
let x = "5" / 2;
```

![js-type-coercion example 5 source](../code_sandbox/snaps/js-type-coercion-05-code.png)

![js-type-coercion example 5 result](../code_sandbox/snaps/js-type-coercion-05-result.png)

- [x] **Outcome:** x is **2.5**.

<a id="js-type-coercion-example-06"></a>

### **Example 6: "5" % 2 — numeric %**

- [x] **`%`** (remainder) coerces both sides to numbers.

Sandbox: `code_sandbox/js-type-coercion/numeric-mod.html`

```javascript
let x = "5" % 2;
```

![js-type-coercion example 6 source](../code_sandbox/snaps/js-type-coercion-06-code.png)

![js-type-coercion example 6 result](../code_sandbox/snaps/js-type-coercion-06-result.png)

- [x] **Outcome:** x is **1**.

<a id="js-type-coercion-example-07"></a>

### **Example 7: +"5" — unary plus to number**

- [x] **Unary `+`** forces a number (same idea as `Number()`).

Sandbox: `code_sandbox/js-type-coercion/unary-plus.html`

```javascript
let x = +"5";
```

![js-type-coercion example 7 source](../code_sandbox/snaps/js-type-coercion-07-code.png)

![js-type-coercion example 7 result](../code_sandbox/snaps/js-type-coercion-07-result.png)

- [x] **Outcome:** x is **5**. typeof is **"number"**.

<a id="js-type-coercion-example-08"></a>

### **Example 8: 5 == "5" — loose equality**

- [x] **`==`** coerces to a common type before comparing. `5 == "5"` is **true**.

Sandbox: `code_sandbox/js-type-coercion/loose-eq-number-string.html`

```javascript
let x = (5 == "5");
```

![js-type-coercion example 8 source](../code_sandbox/snaps/js-type-coercion-08-code.png)

![js-type-coercion example 8 result](../code_sandbox/snaps/js-type-coercion-08-result.png)

- [x] **Outcome:** x is **true**.

<a id="js-type-coercion-example-09"></a>

### **Example 9: 5 === "5" — strict equality**

- [x] **`===`** does **not** coerce. Different types → **false**.

Sandbox: `code_sandbox/js-type-coercion/strict-eq-number-string.html`

```javascript
let x = (5 === "5");
```

![js-type-coercion example 9 source](../code_sandbox/snaps/js-type-coercion-09-code.png)

![js-type-coercion example 9 result](../code_sandbox/snaps/js-type-coercion-09-result.png)

- [x] **Outcome:** x is **false**.

<a id="js-type-coercion-example-10"></a>

### **Example 10: "abc" - 1 is NaN**

- [x] If a string **cannot** become a valid number, numeric coercion yields **NaN**.

Sandbox: `code_sandbox/js-type-coercion/abc-minus-1.html`

```javascript
let x = "abc" - 1;
```

![js-type-coercion example 10 source](../code_sandbox/snaps/js-type-coercion-10-code.png)

![js-type-coercion example 10 result](../code_sandbox/snaps/js-type-coercion-10-result.png)

- [x] **Outcome:** x is **NaN**.

<a id="js-type-coercion-example-11"></a>

### **Example 11: Boolean coercion — !!0**

- [x] **Falsy:** `0`, `""`, `null`, `undefined`, `NaN`, `false`.
- [x] `!!` is the usual explicit boolean coercion demo.

Sandbox: `code_sandbox/js-type-coercion/falsy-0.html`

```javascript
!!0;
```

![js-type-coercion example 11 source](../code_sandbox/snaps/js-type-coercion-11-code.png)

![js-type-coercion example 11 result](../code_sandbox/snaps/js-type-coercion-11-result.png)

- [x] **Outcome:** `!!0` is **false**.

<a id="js-type-coercion-example-12"></a>

### **Example 12: Boolean coercion — !!""**

- [x] The empty string is **falsy**.

Sandbox: `code_sandbox/js-type-coercion/falsy-empty-string.html`

```javascript
!!"";
```

![js-type-coercion example 12 source](../code_sandbox/snaps/js-type-coercion-12-code.png)

![js-type-coercion example 12 result](../code_sandbox/snaps/js-type-coercion-12-result.png)

- [x] **Outcome:** `!!""` is **false**.

<a id="js-type-coercion-example-13"></a>

### **Example 13: Boolean coercion — !!null**

- [x] **null** is falsy.

Sandbox: `code_sandbox/js-type-coercion/falsy-null.html`

```javascript
!!null;
```

![js-type-coercion example 13 source](../code_sandbox/snaps/js-type-coercion-13-code.png)

![js-type-coercion example 13 result](../code_sandbox/snaps/js-type-coercion-13-result.png)

- [x] **Outcome:** `!!null` is **false**.

<a id="js-type-coercion-example-14"></a>

### **Example 14: Boolean coercion — !!undefined**

- [x] **undefined** is falsy.

Sandbox: `code_sandbox/js-type-coercion/falsy-undefined.html`

```javascript
!!undefined;
```

![js-type-coercion example 14 source](../code_sandbox/snaps/js-type-coercion-14-code.png)

![js-type-coercion example 14 result](../code_sandbox/snaps/js-type-coercion-14-result.png)

- [x] **Outcome:** `!!undefined` is **false**.

<a id="js-type-coercion-example-15"></a>

### **Example 15: Boolean coercion — !!NaN**

- [x] **NaN** is falsy.

Sandbox: `code_sandbox/js-type-coercion/falsy-nan.html`

```javascript
!!NaN;
```

![js-type-coercion example 15 source](../code_sandbox/snaps/js-type-coercion-15-code.png)

![js-type-coercion example 15 result](../code_sandbox/snaps/js-type-coercion-15-result.png)

- [x] **Outcome:** `!!NaN` is **false**.

<a id="js-type-coercion-example-16"></a>

### **Example 16: Boolean coercion — !!false**

- [x] **false** is falsy.

Sandbox: `code_sandbox/js-type-coercion/falsy-false.html`

```javascript
!!false;
```

![js-type-coercion example 16 source](../code_sandbox/snaps/js-type-coercion-16-code.png)

![js-type-coercion example 16 result](../code_sandbox/snaps/js-type-coercion-16-result.png)

- [x] **Outcome:** `!!false` is **false**.

<a id="js-type-coercion-example-17"></a>

### **Example 17: Boolean coercion — !!{}**

- [x] Empty objects **`{}`** are **truthy**.

Sandbox: `code_sandbox/js-type-coercion/truthy-object.html`

```javascript
!!{};
```

![js-type-coercion example 17 source](../code_sandbox/snaps/js-type-coercion-17-code.png)

![js-type-coercion example 17 result](../code_sandbox/snaps/js-type-coercion-17-result.png)

- [x] **Outcome:** `!!{}` is **true**.

<a id="js-type-coercion-example-18"></a>

### **Example 18: Boolean coercion — !![]**

- [x] Empty arrays **`[]`** are **truthy** (unlike `""`).

Sandbox: `code_sandbox/js-type-coercion/truthy-array.html`

```javascript
!![];
```

![js-type-coercion example 18 source](../code_sandbox/snaps/js-type-coercion-18-code.png)

![js-type-coercion example 18 result](../code_sandbox/snaps/js-type-coercion-18-result.png)

- [x] **Outcome:** `!![]` is **true**.

<a id="js-type-coercion-example-19"></a>

### **Example 19: 0 == false is true; 0 === false is false**

- [x] `==` coerces **false** to **0**. `===` sees number vs boolean.

Sandbox: `code_sandbox/js-type-coercion/loose-eq-zero-false.html`

```javascript
0 == false;
0 === false;
```

![js-type-coercion example 19 source](../code_sandbox/snaps/js-type-coercion-19-code.png)

![js-type-coercion example 19 result](../code_sandbox/snaps/js-type-coercion-19-result.png)

- [x] **Outcome:** `==` is **true**. `===` is **false**.

<a id="js-type-coercion-example-20"></a>

### **Example 20: "" == 0 is true**

- [x] Empty string **`==`** 0 after numeric coercion.

Sandbox: `code_sandbox/js-type-coercion/loose-eq-empty-zero.html`

```javascript
"" == 0;
```

![js-type-coercion example 20 source](../code_sandbox/snaps/js-type-coercion-20-code.png)

![js-type-coercion example 20 result](../code_sandbox/snaps/js-type-coercion-20-result.png)

- [x] **Outcome:** `"" == 0` is **true**. `"" === 0` is **false**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-type-coercion/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `'5' + '2'` vs `'5' - '2'`?

<details>
<summary>Answer</summary>

- [x] **"52"** (string) vs **3** (number).

</details>

### Question 2: What is `"5" + 2`?

<details>
<summary>Answer</summary>

- [x] **"52"**.

</details>

### Question 3: What is `"5" - 2`?

<details>
<summary>Answer</summary>

- [x] **3**.

</details>

### Question 4: What is `"5" * 2`?

<details>
<summary>Answer</summary>

- [x] **10**.

</details>

### Question 5: What is `"5" / 2`?

<details>
<summary>Answer</summary>

- [x] **2.5**.

</details>

### Question 6: What is `"5" % 2`?

<details>
<summary>Answer</summary>

- [x] **1**.

</details>

### Question 7: What is `+"5"`?

<details>
<summary>Answer</summary>

- [x] **5** (number).

</details>

### Question 8: What is `5 == "5"` vs `5 === "5"`?

<details>
<summary>Answer</summary>

- [x] **true** vs **false**.

</details>

### Question 9: Name the falsy values.

<details>
<summary>Answer</summary>

- [x] **0, "", null, undefined, NaN, false**.

</details>

### Question 10: Are `{}` and `[]` falsy?

<details>
<summary>Answer</summary>

- [x] **No.** `!!{}` and `!![]` are **true**.

</details>

### Question 11: What is `0 == false`?

<details>
<summary>Answer</summary>

- [x] **true**. `0 === false` is **false**.

</details>

### Question 12: What is `"" == 0`?

<details>
<summary>Answer</summary>

- [x] **true**. `===` is **false**.

</details>

### Question 13: What is `"abc" - 1`?

<details>
<summary>Answer</summary>

- [x] **NaN**.

</details>


</details>

## Summary

Do not rely on + to add when a string might be present. Use === unless you truly want coercion. List the six falsy values; empty objects and arrays are not among them.

## References

- [JS Type Coercion (W3Schools)](https://www.w3schools.com/js/js_type_coercion.asp)
- [MDN: Type coercion](https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion)
- [MDN: Equality comparisons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)
