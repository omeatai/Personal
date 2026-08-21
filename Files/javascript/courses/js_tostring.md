# JS toString()

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

toString() turns a value into a string. Arrays become comma-separated lists with no spaces. Dates become a local date/time/zone string. Numbers become decimal text, or another radix such as toString(2) for binary. Functions return their source. Plain objects return [object Object] unless you override toString. null and undefined have no toString method — calling it is TypeError; use String(null) instead.

This section has **10** examples:

- [x] **Example 1:** Array.prototype.toString — comma list [View](#js-tostring-example-01)
- [x] **Example 2:** Date.prototype.toString — local date/time [View](#js-tostring-example-02)
- [x] **Example 3:** Date toString on a fixed instant [View](#js-tostring-example-03)
- [x] **Example 4:** Number.prototype.toString — decimal [View](#js-tostring-example-04)
- [x] **Example 5:** Number toString(2) — binary [View](#js-tostring-example-05)
- [x] **Example 6:** Function.prototype.toString — source [View](#js-tostring-example-06)
- [x] **Example 7:** Object toString default — "[object Object]" [View](#js-tostring-example-07)
- [x] **Example 8:** Object toString override [View](#js-tostring-example-08)
- [x] **Example 9:** Boolean.prototype.toString [View](#js-tostring-example-09)
- [x] **Example 10:** null.toString() is TypeError [View](#js-tostring-example-10)

## Detailed Explanation

- [x] `["Banana","Orange","Apple","Mango"].toString()` is **"Banana,Orange,Apple,Mango"**.
- [x] `(123).toString()` is **"123"**. `(123).toString(2)` is **"1111011"**.
- [x] Default object toString is **"[object Object]"**. Override it to print real fields.
- [x] `null.toString()` / `undefined.toString()` are **TypeError**. Use **String(null)**.
- [x] Date toString is **local**. Fixed instant: **Thu Mar 25 2021 09:30:45 GMT-0600 (Mountain Daylight Time)**.

<a id="js-tostring-example-01"></a>

### **Example 1: Array.prototype.toString — comma list**

- [x] Array **`toString()`** joins elements with **commas** (no spaces).

Sandbox: `code_sandbox/js-tostring/array-tostring.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let myList = fruits.toString();
```

![js-tostring example 1 source](../code_sandbox/snaps/js-tostring-01-code.png)

![js-tostring example 1 result](../code_sandbox/snaps/js-tostring-01-result.png)

- [x] **Outcome:** myList is **"Banana,Orange,Apple,Mango"**.

<a id="js-tostring-example-02"></a>

### **Example 2: Date.prototype.toString — local date/time**

- [x] Date **`toString()`** is a human-readable **local** date, time, and zone.
- [x] This Tryit uses **`new Date()`** (now). The snap is the **browser's current local** clock.

Sandbox: `code_sandbox/js-tostring/date-tostring.html`

```javascript
const d = new Date();
let text = d.toString();
```

![js-tostring example 2 source](../code_sandbox/snaps/js-tostring-02-code.png)

![js-tostring example 2 result](../code_sandbox/snaps/js-tostring-02-result.png)

- [x] **Outcome:** The snap shows this engine's **current local** `toString()` (Mountain, GMT-0600 / GMT-0700).

<a id="js-tostring-example-03"></a>

### **Example 3: Date toString on a fixed instant**

- [x] Same method on a **fixed** UTC instant so the outcome is stable.

Sandbox: `code_sandbox/js-tostring/date-tostring-fixed.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
let text = d.toString();
```

![js-tostring example 3 source](../code_sandbox/snaps/js-tostring-03-code.png)

![js-tostring example 3 result](../code_sandbox/snaps/js-tostring-03-result.png)

- [x] **Outcome:** text is **"Thu Mar 25 2021 09:30:45 GMT-0600 (Mountain Daylight Time)"**.

<a id="js-tostring-example-04"></a>

### **Example 4: Number.prototype.toString — decimal**

- [x] Number **`toString()`** (no argument) is the decimal string.

Sandbox: `code_sandbox/js-tostring/number-tostring.html`

```javascript
let x = 123;
let text = x.toString();
```

![js-tostring example 4 source](../code_sandbox/snaps/js-tostring-04-code.png)

![js-tostring example 4 result](../code_sandbox/snaps/js-tostring-04-result.png)

- [x] **Outcome:** text is **"123"**. typeof is **"string"**.

<a id="js-tostring-example-05"></a>

### **Example 5: Number toString(2) — binary**

- [x] `toString(radix)` with **2** is **binary**.

Sandbox: `code_sandbox/js-tostring/number-tostring-binary.html`

```javascript
let x = 123;
let text = x.toString(2);
```

![js-tostring example 5 source](../code_sandbox/snaps/js-tostring-05-code.png)

![js-tostring example 5 result](../code_sandbox/snaps/js-tostring-05-result.png)

- [x] **Outcome:** text is **"1111011"** (123 in base 2).

<a id="js-tostring-example-06"></a>

### **Example 6: Function.prototype.toString — source**

- [x] Function **`toString()`** returns the **source text** of the function.
- [x] Named on the page; no Tryit — still run it.

Sandbox: `code_sandbox/js-tostring/function-tostring.html`

```javascript
function add(a, b) { return a + b; }
let text = add.toString();
```

![js-tostring example 6 source](../code_sandbox/snaps/js-tostring-06-code.png)

![js-tostring example 6 result](../code_sandbox/snaps/js-tostring-06-result.png)

- [x] **Outcome:** text is **"function add(a, b) { return a + b; }"**.

<a id="js-tostring-example-07"></a>

### **Example 7: Object toString default — "[object Object]"**

- [x] Default object **`toString()`** is **[object Object]** — not the keys.

Sandbox: `code_sandbox/js-tostring/object-tostring-default.html`

```javascript
let person = {
  firstname: "John",
  lastname: "Doe"
};
let text = person.toString();
```

![js-tostring example 7 source](../code_sandbox/snaps/js-tostring-07-code.png)

![js-tostring example 7 result](../code_sandbox/snaps/js-tostring-07-result.png)

- [x] **Outcome:** text is **"[object Object]"**.

<a id="js-tostring-example-08"></a>

### **Example 8: Object toString override**

- [x] Override **`toString`** on the object (or prototype) for a useful string.

Sandbox: `code_sandbox/js-tostring/object-tostring-override.html`

```javascript
let person = {
  firstname: "John",
  lastname: "Doe",
  toString: function () {
    return this.firstname + " " + this.lastname;
  }
};
let text = person.toString();
```

![js-tostring example 8 source](../code_sandbox/snaps/js-tostring-08-code.png)

![js-tostring example 8 result](../code_sandbox/snaps/js-tostring-08-result.png)

- [x] **Outcome:** text is **"John Doe"**. String(person) also uses the override: **"John Doe"**.

<a id="js-tostring-example-09"></a>

### **Example 9: Boolean.prototype.toString**

- [x] `true.toString()` / `false.toString()` are the strings **"true"** / **"false"**.

Sandbox: `code_sandbox/js-tostring/boolean-tostring.html`

```javascript
true.toString();
false.toString();
```

![js-tostring example 9 source](../code_sandbox/snaps/js-tostring-09-code.png)

![js-tostring example 9 result](../code_sandbox/snaps/js-tostring-09-result.png)

- [x] **Outcome:** true → **"true"**. false → **"false"**.

<a id="js-tostring-example-10"></a>

### **Example 10: null.toString() is TypeError**

- [x] **`null`** and **`undefined`** have no `toString` method. Calling it throws **TypeError**.
- [x] Use **`String(null)`** instead (**"null"**).

Sandbox: `code_sandbox/js-tostring/null-tostring-typeerror.html`

```javascript
null.toString();
```

![js-tostring example 10 source](../code_sandbox/snaps/js-tostring-10-code.png)

![js-tostring example 10 result](../code_sandbox/snaps/js-tostring-10-result.png)

- [x] **Outcome:** null.toString() is **TypeError: Cannot read properties of null (reading 'toString')**. undefined.toString() is the same kind of TypeError. String(null) is **"null"**. String(undefined) is **"undefined"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-tostring/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is fruits.toString() for Banana/Orange/Apple/Mango?

<details>
<summary>Answer</summary>

- [x] **"Banana,Orange,Apple,Mango"** (no spaces).

</details>

### Question 2: What is `(123).toString()`?

<details>
<summary>Answer</summary>

- [x] **"123"**.

</details>

### Question 3: What is `(123).toString(2)`?

<details>
<summary>Answer</summary>

- [x] **"1111011"**.

</details>

### Question 4: What is a function’s toString?

<details>
<summary>Answer</summary>

- [x] Its **source text**, e.g. **function add(a, b) { return a + b; }**.

</details>

### Question 5: What is `{firstname, lastname}.toString()` by default?

<details>
<summary>Answer</summary>

- [x] **"[object Object]"**.

</details>

### Question 6: How do you make an object print usefully?

<details>
<summary>Answer</summary>

- [x] Override **toString**. The demo returns **"John Doe"**.

</details>

### Question 7: What is `true.toString()`?

<details>
<summary>Answer</summary>

- [x] **"true"**. false → **"false"**.

</details>

### Question 8: Can you call `null.toString()`?

<details>
<summary>Answer</summary>

- [x] **No. TypeError.** Use **String(null)** → **"null"**.

</details>

### Question 9: Is Date toString UTC?

<details>
<summary>Answer</summary>

- [x] **No.** It is **local** plus a zone name. ISO is `toISOString()`.

</details>

### Question 10: Does array toString add spaces after commas?

<details>
<summary>Answer</summary>

- [x] **No.**

</details>


</details>

## Summary

Use toString for a readable string, but know the defaults: arrays join with commas, objects say [object Object], and null/undefined throw. Override object toString when you need a real dump.

## References

- [JS toString() (W3Schools)](https://www.w3schools.com/js/js_tostring.asp)
- [MDN: Object.prototype.toString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
- [MDN: Number.prototype.toString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString)
