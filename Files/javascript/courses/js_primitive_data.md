# JS Primitive Data

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The seven primitives are Number, BigInt, String, Boolean, Undefined, Null, and Symbol. Strings use single or double quotes; inner quotes must differ from the outer pair. All ordinary numbers are 64-bit floats, so 34.00 equals 34, and 123e5 is 12300000. BigInt("…") keeps long integers exact; mixing BigInt with Number throws TypeError. A declared variable with no value is undefined. An empty string is a real string, not undefined. null is a primitive whose typeof is still "object". Prefer === when checking null — == also matches undefined.

This section has **15** examples:

- [x] **Example 1:** Strings — double or single quotes [View](#js-primitive-data-example-01)
- [x] **Example 2:** Quotes inside a string [View](#js-primitive-data-example-02)
- [x] **Example 3:** Numbers with or without decimals [View](#js-primitive-data-example-03)
- [x] **Example 4:** Exponential notation — 123e5 and 123e-5 [View](#js-primitive-data-example-04)
- [x] **Example 5:** BigInt("123456789012345678901234567890") [View](#js-primitive-data-example-05)
- [x] **Example 6:** BigInt + Number is TypeError [View](#js-primitive-data-example-06)
- [x] **Example 7:** Boolean from == comparison [View](#js-primitive-data-example-07)
- [x] **Example 8:** typeof strings — "", "John", "John Doe" [View](#js-primitive-data-example-08)
- [x] **Example 9:** typeof numbers — 0, 314, 3.14, (3), (3+4) [View](#js-primitive-data-example-09)
- [x] **Example 10:** let car — value and type undefined [View](#js-primitive-data-example-10)
- [x] **Example 11:** car = undefined — emptied [View](#js-primitive-data-example-11)
- [x] **Example 12:** Empty string "" is not undefined [View](#js-primitive-data-example-12)
- [x] **Example 13:** let carName = null [View](#js-primitive-data-example-13)
- [x] **Example 14:** typeof null is "object" (legacy) [View](#js-primitive-data-example-14)
- [x] **Example 15:** null === vs == undefined [View](#js-primitive-data-example-15)

## Detailed Explanation

- [x] Seven primitives: **string, number, boolean, bigint, symbol, null, undefined**.
- [x] `34.00 === 34` is **true**. `123e5` is **12300000**. `123e-5` is **0.00123**.
- [x] `BigInt("123…890")` is exact. **`1n + 1` is TypeError**.
- [x] `let car;` is **undefined**. `let car = ""` is a **string**. `let carName = null` is **null**.
- [x] `typeof null` is **"object"**. `null === undefined` is **false**; `null == undefined` is **true**.

<a id="js-primitive-data-example-01"></a>

### **Example 1: Strings — double or single quotes**

- [x] Strings use **double** or **single** quotes. Both are the same type.

Sandbox: `code_sandbox/js-primitive-data/string-quotes.html`

```javascript
let carName1 = "Volvo XC60";
let carName2 = 'Volvo XC60';
```

![js-primitive-data example 1 source](../code_sandbox/snaps/js-primitive-data-01-code.png)

![js-primitive-data example 1 result](../code_sandbox/snaps/js-primitive-data-01-result.png)

- [x] **Outcome:** Both are **"Volvo XC60"**. They **===** each other.

<a id="js-primitive-data-example-02"></a>

### **Example 2: Quotes inside a string**

- [x] You may put quotes **inside** a string if they **differ** from the outer quotes.

Sandbox: `code_sandbox/js-primitive-data/string-quotes-inside.html`

```javascript
let answer1 = "It's alright";
let answer2 = "He is called 'Johnny'";
let answer3 = 'He is called "Johnny"';
```

![js-primitive-data example 2 source](../code_sandbox/snaps/js-primitive-data-02-code.png)

![js-primitive-data example 2 result](../code_sandbox/snaps/js-primitive-data-02-result.png)

- [x] **Outcome:** answer1 is **"It's alright"**. answer2 is **"He is called 'Johnny'"**. answer3 is **"He is called \"Johnny\""**.

<a id="js-primitive-data-example-03"></a>

### **Example 3: Numbers with or without decimals**

- [x] All JS numbers are **64-bit floating point**. `34.00` and `34` are the same numeric value.

Sandbox: `code_sandbox/js-primitive-data/number-decimals.html`

```javascript
let x1 = 34.00;
let x2 = 34;
```

![js-primitive-data example 3 source](../code_sandbox/snaps/js-primitive-data-03-code.png)

![js-primitive-data example 3 result](../code_sandbox/snaps/js-primitive-data-03-result.png)

- [x] **Outcome:** Both are **34**. `x1 === x2` is **true**. typeof is **"number"**.

<a id="js-primitive-data-example-04"></a>

### **Example 4: Exponential notation — 123e5 and 123e-5**

- [x] **Scientific notation**: `e5` means × 10^5, `e-5` means × 10^−5.

Sandbox: `code_sandbox/js-primitive-data/number-exponential.html`

```javascript
let y = 123e5;
let z = 123e-5;
```

![js-primitive-data example 4 source](../code_sandbox/snaps/js-primitive-data-04-code.png)

![js-primitive-data example 4 result](../code_sandbox/snaps/js-primitive-data-04-result.png)

- [x] **Outcome:** y is **12300000**. z is **0.00123**.

<a id="js-primitive-data-example-05"></a>

### **Example 5: BigInt("123456789012345678901234567890")**

- [x] `BigInt("…")` parses a **string** of digits — exact, unlike `BigInt(number)`.

Sandbox: `code_sandbox/js-primitive-data/bigint-from-string.html`

```javascript
let x = BigInt("123456789012345678901234567890");
```

![js-primitive-data example 5 source](../code_sandbox/snaps/js-primitive-data-05-code.png)

![js-primitive-data example 5 result](../code_sandbox/snaps/js-primitive-data-05-result.png)

- [x] **Outcome:** x is **123456789012345678901234567890n**. typeof is **"bigint"**.

<a id="js-primitive-data-example-06"></a>

### **Example 6: BigInt + Number is TypeError**

- [x] You **cannot mix** BigInt and Number in arithmetic. The engine throws **TypeError**.

Sandbox: `code_sandbox/js-primitive-data/bigint-mix-typeerror.html`

```javascript
1n + 1;
```

![js-primitive-data example 6 source](../code_sandbox/snaps/js-primitive-data-06-code.png)

![js-primitive-data example 6 result](../code_sandbox/snaps/js-primitive-data-06-result.png)

- [x] **Outcome:** **TypeError: Cannot mix BigInt and other types, use explicit conversions**.

<a id="js-primitive-data-example-07"></a>

### **Example 7: Boolean from == comparison**

- [x] Booleans are only **true** / **false**. Comparisons produce booleans.

Sandbox: `code_sandbox/js-primitive-data/boolean-compare.html`

```javascript
let x = 5;
let y = 5;
let z = 6;
```

![js-primitive-data example 7 source](../code_sandbox/snaps/js-primitive-data-07-code.png)

![js-primitive-data example 7 result](../code_sandbox/snaps/js-primitive-data-07-result.png)

- [x] **Outcome:** `x == y` is **true**. `x == z` is **false**.

<a id="js-primitive-data-example-08"></a>

### **Example 8: typeof strings — "", "John", "John Doe"**

- [x] `typeof` on string values returns **"string"**.

Sandbox: `code_sandbox/js-primitive-data/typeof-strings.html`

```javascript
typeof "";
typeof "John";
typeof "John Doe";
```

![js-primitive-data example 8 source](../code_sandbox/snaps/js-primitive-data-08-code.png)

![js-primitive-data example 8 result](../code_sandbox/snaps/js-primitive-data-08-result.png)

- [x] **Outcome:** All three are **"string"**.

<a id="js-primitive-data-example-09"></a>

### **Example 9: typeof numbers — 0, 314, 3.14, (3), (3+4)**

- [x] `typeof` on number values returns **"number"**.

Sandbox: `code_sandbox/js-primitive-data/typeof-numbers.html`

```javascript
typeof 0;
typeof 314;
typeof 3.14;
typeof (3);
typeof (3 + 4);
```

![js-primitive-data example 9 source](../code_sandbox/snaps/js-primitive-data-09-code.png)

![js-primitive-data example 9 result](../code_sandbox/snaps/js-primitive-data-09-result.png)

- [x] **Outcome:** All five are **"number"**.

<a id="js-primitive-data-example-10"></a>

### **Example 10: let car — value and type undefined**

- [x] A variable declared with **no value** is **`undefined`**. `typeof` is also **"undefined"**.

Sandbox: `code_sandbox/js-primitive-data/undefined-declared.html`

```javascript
let car;
```

![js-primitive-data example 10 source](../code_sandbox/snaps/js-primitive-data-10-code.png)

![js-primitive-data example 10 result](../code_sandbox/snaps/js-primitive-data-10-result.png)

- [x] **Outcome:** car is **undefined**. typeof is **"undefined"**.

<a id="js-primitive-data-example-11"></a>

### **Example 11: car = undefined — emptied**

- [x] Any variable can be **emptied** by assigning **`undefined`**. Type stays **undefined**.

Sandbox: `code_sandbox/js-primitive-data/set-undefined.html`

```javascript
let car = "Volvo";
car = undefined;
```

![js-primitive-data example 11 source](../code_sandbox/snaps/js-primitive-data-11-code.png)

![js-primitive-data example 11 result](../code_sandbox/snaps/js-primitive-data-11-result.png)

- [x] **Outcome:** After the assignment, car is **undefined** and typeof is **"undefined"**.

<a id="js-primitive-data-example-12"></a>

### **Example 12: Empty string "" is not undefined**

- [x] An **empty string** is a real value with type **string**. It is **not** undefined.

Sandbox: `code_sandbox/js-primitive-data/empty-string.html`

```javascript
let car = "";
```

![js-primitive-data example 12 source](../code_sandbox/snaps/js-primitive-data-12-code.png)

![js-primitive-data example 12 result](../code_sandbox/snaps/js-primitive-data-12-result.png)

- [x] **Outcome:** value is **""**. typeof is **"string"** (JSON.stringify shows the quotes).

<a id="js-primitive-data-example-13"></a>

### **Example 13: let carName = null**

- [x] You may assign **`null`** to mean “no object”.

Sandbox: `code_sandbox/js-primitive-data/null-assign.html`

```javascript
let carName = null;
```

![js-primitive-data example 13 source](../code_sandbox/snaps/js-primitive-data-13-code.png)

![js-primitive-data example 13 result](../code_sandbox/snaps/js-primitive-data-13-result.png)

- [x] **Outcome:** carName is **null**. typeof is **"object"** (legacy quirk — **null is still a primitive**).

<a id="js-primitive-data-example-14"></a>

### **Example 14: typeof null is "object" (legacy)**

- [x] `typeof null` returns **"object"**. This is a **historical bug**, not a classification.
- [x] Null is still a **primitive**.

Sandbox: `code_sandbox/js-primitive-data/null-typeof-object.html`

```javascript
typeof null;
```

![js-primitive-data example 14 source](../code_sandbox/snaps/js-primitive-data-14-code.png)

![js-primitive-data example 14 result](../code_sandbox/snaps/js-primitive-data-14-result.png)

- [x] **Outcome:** typeof null is **"object"**.

<a id="js-primitive-data-example-15"></a>

### **Example 15: null === vs == undefined**

- [x] **`===`** needs the same type: `null === undefined` is **false**.
- [x] **`==`** coerces: `null == undefined` is **true**. Prefer **`===`** when checking null.

Sandbox: `code_sandbox/js-primitive-data/null-eq-undefined.html`

```javascript
null === null;
null === undefined;
null == undefined;
```

![js-primitive-data example 15 source](../code_sandbox/snaps/js-primitive-data-15-code.png)

![js-primitive-data example 15 result](../code_sandbox/snaps/js-primitive-data-15-result.png)

- [x] **Outcome:** `null === null` is **true**. `null === undefined` is **false**. `null == undefined` is **true**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-primitive-data/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Are `'Volvo XC60'` and `"Volvo XC60"` different types?

<details>
<summary>Answer</summary>

- [x] **No.** Both are strings and **===** each other.

</details>

### Question 2: Can you put a single quote inside double quotes?

<details>
<summary>Answer</summary>

- [x] **Yes.** `"It's alright"` and `"He is called 'Johnny'"` run.

</details>

### Question 3: Is `34.00` a different type from `34`?

<details>
<summary>Answer</summary>

- [x] **No.** Both are **number**. `34.00 === 34` is **true**.

</details>

### Question 4: What is `123e5`?

<details>
<summary>Answer</summary>

- [x] **12300000**.

</details>

### Question 5: What is `123e-5`?

<details>
<summary>Answer</summary>

- [x] **0.00123**.

</details>

### Question 6: What happens with `1n + 1`?

<details>
<summary>Answer</summary>

- [x] **TypeError: Cannot mix BigInt and other types, use explicit conversions**.

</details>

### Question 7: What is `(5 == 5)` vs `(5 == 6)`?

<details>
<summary>Answer</summary>

- [x] **true** and **false** — booleans from comparison.

</details>

### Question 8: Is `""` undefined?

<details>
<summary>Answer</summary>

- [x] **No.** Value `""`, typeof **"string"**.

</details>

### Question 9: How do you test for null?

<details>
<summary>Answer</summary>

- [x] Use **`=== null`**. Avoid `==`, which is also true for **undefined**.

</details>

### Question 10: What is `typeof null`?

<details>
<summary>Answer</summary>

- [x] **"object"** (legacy). Null is still a primitive.

</details>

### Question 11: What is `null === null`?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 12: Does emptying with `undefined` change the type?

<details>
<summary>Answer</summary>

- [x] **Yes** — both value and type become **undefined**.

</details>


</details>

## Summary

Primitives are not objects. Empty string is not undefined. null is not an object despite typeof. Keep BigInt math in BigInt-land or convert explicitly.

## References

- [JS Primitives (W3Schools)](https://www.w3schools.com/js/js_datatypes_primitives.asp)
- [MDN: Primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
- [MDN: null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
