<details>
  <summary>JS NaN</summary>

## Introduction

NaN means Not a Number, but typeof NaN is number. You get NaN from invalid math such as 100 / "Apple" or 0 / 0. Numeric strings still work: 100 / "10" is 10. NaN is the only value that is not == or === to itself. Do not write x === NaN. Use Number.isNaN (no coercion). Global isNaN("Apple") is true because it coerces; Number.isNaN("Apple") is false. Math with NaN stays NaN. Object.is(NaN, NaN) is true.

This section has **12** examples:

- [x] **Example 1:** 100 / "Apple" is NaN [View](#js-nan-example-01)
- [x] **Example 2:** typeof NaN is number [View](#js-nan-example-02)
- [x] **Example 3:** 100 / "10" is 10 [View](#js-nan-example-03)
- [x] **Example 4:** isNaN(100 / "Apple") [View](#js-nan-example-04)
- [x] **Example 5:** NaN == NaN is false [View](#js-nan-example-05)
- [x] **Example 6:** NaN !== NaN is true [View](#js-nan-example-06)
- [x] **Example 7:** Number.isNaN(NaN) is the right test [View](#js-nan-example-07)
- [x] **Example 8:** isNaN("Apple") vs Number.isNaN("Apple") [View](#js-nan-example-08)
- [x] **Example 9:** NaN + 5 is NaN [View](#js-nan-example-09)
- [x] **Example 10:** 0 / 0 is NaN [View](#js-nan-example-10)
- [x] **Example 11:** Object.is(NaN, NaN) is true [View](#js-nan-example-11)
- [x] **Example 12:** parseInt("abc") is NaN [View](#js-nan-example-12)

## Detailed Explanation

- [x] `100 / "Apple"` is **NaN**. `100 / "10"` is **10**.
- [x] **typeof NaN** is **"number"**.
- [x] **NaN !== NaN**. `NaN == NaN` is **false**. Use **Number.isNaN**.
- [x] `isNaN("Apple")` is **true** (coerces). `Number.isNaN("Apple")` is **false**.
- [x] **NaN + 5** is **NaN**. **0 / 0** is **NaN**. **1 / 0** is **Infinity**.

<a id="js-nan-example-01"></a>

### **Example 1: 100 / "Apple" is NaN**

- [x] You get **NaN** when JS **cannot** calculate a number.

Sandbox: `code_sandbox/js-nan/div-apple.html`

```javascript
let x = 100 / "Apple";
```

<img alt="js-nan example 1 source" src="./code_sandbox/snaps/js-nan-01-code.png" />

<img alt="js-nan example 1 result" src="./code_sandbox/snaps/js-nan-01-result.png" />

- [x] **Outcome:** x is **NaN**. typeof is **"number"**.

<a id="js-nan-example-02"></a>

### **Example 2: typeof NaN is number**

- [x] **NaN** belongs to the **number** type. The name means Not-a-Number; the type is still number.

Sandbox: `code_sandbox/js-nan/typeof-nan.html`

```javascript
let x = NaN;
```

<img alt="js-nan example 2 source" src="./code_sandbox/snaps/js-nan-02-code.png" />

<img alt="js-nan example 2 result" src="./code_sandbox/snaps/js-nan-02-result.png" />

- [x] **Outcome:** typeof NaN is **"number"**.

<a id="js-nan-example-03"></a>

### **Example 3: 100 / "10" is 10**

- [x] A **numeric string** is coerced to a number in **arithmetic** (`/`, `-`, `*`).

Sandbox: `code_sandbox/js-nan/div-numeric-string.html`

```javascript
let x = 100 / "10";
```

<img alt="js-nan example 3 source" src="./code_sandbox/snaps/js-nan-03-code.png" />

<img alt="js-nan example 3 result" src="./code_sandbox/snaps/js-nan-03-result.png" />

- [x] **Outcome:** x is **10**. typeof is **"number"**.

<a id="js-nan-example-04"></a>

### **Example 4: isNaN(100 / "Apple")**

- [x] The global **`isNaN()`** is **true** if the value (after number coercion) is NaN.

Sandbox: `code_sandbox/js-nan/isnan-apple.html`

```javascript
let x = 100 / "Apple";
isNaN(x);
```

<img alt="js-nan example 4 source" src="./code_sandbox/snaps/js-nan-04-code.png" />

<img alt="js-nan example 4 result" src="./code_sandbox/snaps/js-nan-04-result.png" />

- [x] **Outcome:** isNaN(x) is **true**.

<a id="js-nan-example-05"></a>

### **Example 5: NaN == NaN is false**

- [x] **NaN is not equal to itself** with `==` or `===`.

Sandbox: `code_sandbox/js-nan/nan-ne-nan-eq.html`

```javascript
let x = NaN;
x == x;
```

<img alt="js-nan example 5 source" src="./code_sandbox/snaps/js-nan-05-code.png" />

<img alt="js-nan example 5 result" src="./code_sandbox/snaps/js-nan-05-result.png" />

- [x] **Outcome:** `x == x` is **false**. `x === x` is also **false**.

<a id="js-nan-example-06"></a>

### **Example 6: NaN !== NaN is true**

- [x] `NaN !== NaN` is **true**. Never test with `x === NaN`.

Sandbox: `code_sandbox/js-nan/nan-strict-ne.html`

```javascript
NaN !== NaN;
```

<img alt="js-nan example 6 source" src="./code_sandbox/snaps/js-nan-06-code.png" />

<img alt="js-nan example 6 result" src="./code_sandbox/snaps/js-nan-06-result.png" />

- [x] **Outcome:** `NaN !== NaN` is **true**. `NaN === NaN` is **false**.

<a id="js-nan-example-07"></a>

### **Example 7: Number.isNaN(NaN) is the right test**

- [x] **`Number.isNaN`** is true **only** for the real NaN value. It does **not** coerce.

Sandbox: `code_sandbox/js-nan/number-isnan.html`

```javascript
Number.isNaN(NaN);
Number.isNaN(100 / "Apple");
```

<img alt="js-nan example 7 source" src="./code_sandbox/snaps/js-nan-07-code.png" />

<img alt="js-nan example 7 result" src="./code_sandbox/snaps/js-nan-07-result.png" />

- [x] **Outcome:** Both are **true** (the division already produced NaN).

<a id="js-nan-example-08"></a>

### **Example 8: isNaN("Apple") vs Number.isNaN("Apple")**

- [x] Global **`isNaN("Apple")`** coerces the string → NaN → **true**.
- [x] **`Number.isNaN("Apple")`** does **not** coerce → **false** (it is not the NaN value).

Sandbox: `code_sandbox/js-nan/isnan-coerces-string.html`

```javascript
isNaN("Apple");
Number.isNaN("Apple");
```

<img alt="js-nan example 8 source" src="./code_sandbox/snaps/js-nan-08-code.png" />

<img alt="js-nan example 8 result" src="./code_sandbox/snaps/js-nan-08-result.png" />

- [x] **Outcome:** isNaN("Apple") is **true**. Number.isNaN("Apple") is **false**. Prefer **Number.isNaN**.

<a id="js-nan-example-09"></a>

### **Example 9: NaN + 5 is NaN**

- [x] Any math with **NaN** stays **NaN**.

Sandbox: `code_sandbox/js-nan/nan-plus-5.html`

```javascript
let x = NaN;
let y = 5;
```

<img alt="js-nan example 9 source" src="./code_sandbox/snaps/js-nan-09-code.png" />

<img alt="js-nan example 9 result" src="./code_sandbox/snaps/js-nan-09-result.png" />

- [x] **Outcome:** NaN + 5 is **NaN**.

<a id="js-nan-example-10"></a>

### **Example 10: 0 / 0 is NaN**

- [x] **`0 / 0`** is NaN. (`1 / 0` is **Infinity**, not NaN.)

Sandbox: `code_sandbox/js-nan/zero-div-zero.html`

```javascript
let x = 0 / 0;
let inf = 1 / 0;
```

<img alt="js-nan example 10 source" src="./code_sandbox/snaps/js-nan-10-code.png" />

<img alt="js-nan example 10 result" src="./code_sandbox/snaps/js-nan-10-result.png" />

- [x] **Outcome:** 0 / 0 is **NaN**. 1 / 0 is **Infinity**.

<a id="js-nan-example-11"></a>

### **Example 11: Object.is(NaN, NaN) is true**

- [x] **`Object.is(NaN, NaN)`** is **true** — another correct NaN test besides **Number.isNaN**.

Sandbox: `code_sandbox/js-nan/object-is-nan.html`

```javascript
Object.is(NaN, NaN);
```

<img alt="js-nan example 11 source" src="./code_sandbox/snaps/js-nan-11-code.png" />

<img alt="js-nan example 11 result" src="./code_sandbox/snaps/js-nan-11-result.png" />

- [x] **Outcome:** Object.is(NaN, NaN) is **true**.

<a id="js-nan-example-12"></a>

### **Example 12: parseInt("abc") is NaN**

- [x] Parsing a **non-numeric** string with `parseInt` / `parseFloat` yields **NaN**.

Sandbox: `code_sandbox/js-nan/parseint-abc.html`

```javascript
parseInt("abc");
parseFloat("abc");
```

<img alt="js-nan example 12 source" src="./code_sandbox/snaps/js-nan-12-code.png" />

<img alt="js-nan example 12 result" src="./code_sandbox/snaps/js-nan-12-result.png" />

- [x] **Outcome:** Both are **NaN**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-nan/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `100 / "Apple"`?

<details>
<summary>Answer</summary>

- [x] **NaN**.

</details>

### Question 2: What is `typeof NaN`?

<details>
<summary>Answer</summary>

- [x] **"number"**.

</details>

### Question 3: What is `100 / "10"`?

<details>
<summary>Answer</summary>

- [x] **10** — numeric strings coerce in arithmetic.

</details>

### Question 4: Is `NaN === NaN`?

<details>
<summary>Answer</summary>

- [x] **false**. `NaN !== NaN` is **true**.

</details>

### Question 5: How should you test for NaN?

<details>
<summary>Answer</summary>

- [x] **Number.isNaN(x)**. Not `x === NaN`.

</details>

### Question 6: Why is `isNaN("Apple")` true?

<details>
<summary>Answer</summary>

- [x] Global isNaN **coerces** the string to NaN. **Number.isNaN("Apple")** is **false**.

</details>

### Question 7: What is `NaN + 5`?

<details>
<summary>Answer</summary>

- [x] **NaN**.

</details>

### Question 8: What is `0 / 0` vs `1 / 0`?

<details>
<summary>Answer</summary>

- [x] **NaN** vs **Infinity**.

</details>

### Question 9: What is `Object.is(NaN, NaN)`?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 10: What is `parseInt("abc")`?

<details>
<summary>Answer</summary>

- [x] **NaN**.

</details>

### Question 11: Is NaN a legal number value?

<details>
<summary>Answer</summary>

- [x] It is a **number** that is **not a legal numeric result** — Not a Number.

</details>


</details>

## Summary

Treat NaN as a number that failed. Compare with Number.isNaN or Object.is, never ===. Arithmetic that cannot produce a number, including 0/0, yields NaN.

## References

- [JS NaN (W3Schools)](https://www.w3schools.com/js/js_nan.asp)
- [MDN: NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
- [MDN: Number.isNaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)

</details>
