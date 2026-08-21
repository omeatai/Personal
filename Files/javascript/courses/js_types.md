# JS Types

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A JavaScript variable can hold **8 types** of data. Use **`typeof`** to find the type of a value. This section covers **strings**, **numbers**, **booleans**, **undefined**, and **empty strings**.

This section has **4** examples:

- [x] **Example 1:** The `typeof` operator [View](#js-types-example-01)
- [x] **Example 2:** Strings [View](#js-types-example-02)
- [x] **Example 3:** Numbers [View](#js-types-example-03)
- [x] **Example 4:** Booleans, `undefined` & empty string [View](#js-types-example-04)

## Detailed Explanation

- [x] **A JavaScript value can be one of 8 types:** **String**, **Number**, **BigInt**, **Boolean**, **Object** (including arrays and dates), **Undefined**, **Null**, and **Symbol**.
- [x] **`typeof`** reports the type of a value or expression as a string (`typeof 3.14` → `"number"`).
- [x] JavaScript is **dynamically typed:** the same variable can hold different types over time; `typeof` tells you what it currently holds.

<a id="js-types-example-01"></a>

### **Example 1: The `typeof` operator**

- [x] `typeof` returns a **string** naming the type: `"string"`, `"number"`, `"boolean"`, `"bigint"`, `"object"`, `"undefined"`.
- [x] Two famous quirks: **arrays report `"object"`** (they are a kind of object) and **`typeof null` is `"object"`** (a long‑standing bug kept for compatibility).
- [x] `BigInt` literals end in **`n`** (`42n`) and report **`"bigint"`**.

Sandbox: `code_sandbox/js-types/typeof.html`

```javascript
typeof "John"; // "string"
typeof 3.14; // "number"
typeof true; // "boolean"
typeof 42n; // "bigint"
typeof { name: "x" }; // "object"
typeof [1, 2, 3]; // "object"  (arrays are objects)
typeof null; // "object"  (historic quirk)
typeof undefined; // "undefined"
```

![js-types example 1 source](../code_sandbox/snaps/js-types-01-code.png)

![js-types example 1 result](../code_sandbox/snaps/js-types-01-result.png)

- [x] **Outcome:** each value prints its type; note `[1,2,3]` and `null` both come back as **object**, while `undefined` is its own type.

<a id="js-types-example-02"></a>

### **Example 2: Strings**

- [x] A **string** is a series of characters wrapped in **single or double quotes** — both are equivalent.
- [x] You can put quotes **inside** a string as long as they **do not match** the surrounding quotes (`"It's alright"`, `'He is called "Johnny"'`).
- [x] Matching quotes inside would end the string early, so pick the outer quote that differs from the inner ones.

Sandbox: `code_sandbox/js-types/strings.html`

```javascript
let carName1 = "Volvo XC60"; // double quotes
let carName2 = "Volvo XC60"; // single quotes

// quotes inside are OK if they don't match the outer quotes
let answer1 = "It's alright";
let answer2 = "He is called 'Johnny'";
let answer3 = 'He is called "Johnny"';
```

![js-types example 2 source](../code_sandbox/snaps/js-types-02-code.png)

![js-types example 2 result](../code_sandbox/snaps/js-types-02-result.png)

- [x] **Outcome:** all five strings print intact, including the ones with an inner apostrophe or inner quotes.

<a id="js-types-example-03"></a>

### **Example 3: Numbers**

- [x] All JavaScript numbers are **floating point** — with or without decimals (`34.00` and `34` both print as `34`).
- [x] **Scientific notation** uses `e`: `123e5` is **12300000** and `123e-5` is **0.00123**.
- [x] Numbers have a **precision limit** (safe integers up to ~2^53): `9999999999999999` rounds to `10000000000000000`.

Sandbox: `code_sandbox/js-types/numbers.html`

```javascript
let x1 = 34.0; // with decimals    -> 34
let x2 = 34; // without decimals -> 34

let y = 123e5; // scientific -> 12300000
let z = 123e-5; // scientific -> 0.00123

let big = 9999999999999999; // beyond safe integer -> rounds
```

![js-types example 3 source](../code_sandbox/snaps/js-types-03-code.png)

![js-types example 3 result](../code_sandbox/snaps/js-types-03-result.png)

- [x] **Outcome:** `34.00` and `34` both show **34**, the `e` forms expand to **12300000** and **0.00123**, and the huge integer rounds to **10000000000000000**.

<a id="js-types-example-04"></a>

### **Example 4: Booleans, `undefined` & empty string**

- [x] A **boolean** is only **`true`** or **`false`**; comparison operators (`>`, `<`, `==`, `!=`) return booleans.
- [x] A variable declared with **no value** is **`undefined`** in both **value and type**.
- [x] An **empty string** `""` is a perfectly legal **string** — it is _not_ `undefined`. (And remember `typeof null` is `"object"`.)

Sandbox: `code_sandbox/js-types/booleans.html`

```javascript
let b = 10 > 9; // true
let c = 10 > 11; // false

let car; // declared, no value -> undefined
let carEmpty = ""; // an empty string is a legal string

typeof car; // "undefined"
typeof carEmpty; // "string"
typeof null; // "object" (known quirk)
```

![js-types example 4 source](../code_sandbox/snaps/js-types-04-code.png)

![js-types example 4 result](../code_sandbox/snaps/js-types-04-result.png)

- [x] **Outcome:** `10 > 9` is **true**, `10 > 11` is **false**, an unassigned variable is **undefined**, and `""` still reports type **string** — distinct from `undefined`.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-types/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you find a value’s type?

<details>
<summary>Answer</summary>

- [x] The **`typeof`** operator.

</details>

### Question 2: What type is `let x = 7.5`?

<details>
<summary>Answer</summary>

- [x] **Number** (all JS numbers are floating point).

</details>

### Question 3: What is the type of a declared-but-unassigned variable?

<details>
<summary>Answer</summary>

- [x] **`undefined`**.

</details>

### Question 4: Is an empty string the same as `undefined`?

<details>
<summary>Answer</summary>

- [x] **No.** `""` has a legal value and type **`string`**.

</details>

### Question 5: How many data types does JavaScript have?

<details>
<summary>Answer</summary>

- [x] **Eight:** String, Number, BigInt, Boolean, Object, Undefined, Null, Symbol.

</details>

### Question 6: What is `typeof [1,2,3]`?

<details>
<summary>Answer</summary>

- [x] **`"object"`** — arrays are a kind of object.

</details>

### Question 7: What is `typeof null`, and why is that surprising?

<details>
<summary>Answer</summary>

- [x] **`"object"`**.
- [x] It is a long‑standing **quirk/bug** kept for backward compatibility.

</details>

### Question 8: How do you write a string that contains an apostrophe?

<details>
<summary>Answer</summary>

- [x] Wrap it in **double quotes**: `"It's alright"`.
- [x] The inner quote must **not match** the outer quotes.

</details>

### Question 9: What does `123e5` equal?

<details>
<summary>Answer</summary>

- [x] **12300000** (scientific notation, `123 × 10^5`).

</details>

### Question 10: What type is a `BigInt` literal like `42n`?

<details>
<summary>Answer</summary>

- [x] **`"bigint"`** — used for integers beyond the safe Number range.

</details>

</details>

## Summary

JavaScript has **eight** datatypes and is **dynamically typed**. **`typeof`** reports the type (with quirks: arrays and `null` both report `"object"`). Strings use single or double quotes; numbers are floats with optional scientific notation and a precision limit; booleans are `true`/`false`. Unassigned variables are **`undefined`**, while `""` is still a **string**.

## References

- [JS Types (W3Schools)](https://www.w3schools.com/js/js_types.asp)
- [MDN: typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
- [MDN: JavaScript data types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
