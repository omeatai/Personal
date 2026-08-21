# JS Comparisons

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Comparison operators compare two values and **always return `true` or `false`**. Use them in **conditional statements** (`if (age < 18) …`). The traps on this page are **`==` vs `===`**, **alphabetical string order**, and **mixed-type** compares that coerce a string to a number (or to `NaN`).

This section has **5** examples:

- [x] **Example 1:** Equal to (`==`) vs strict equal (`===`) [View](#js-comparisons-example-01)
- [x] **Example 2:** Not equal and relational operators [View](#js-comparisons-example-02)
- [x] **Example 3:** String comparison (alphabetical) [View](#js-comparisons-example-03)
- [x] **Example 4:** Comparing different types [View](#js-comparisons-example-04)
- [x] **Example 5:** Convert before you compare [View](#js-comparisons-example-05)

## Detailed Explanation

- [x] **Given `x = 5`**, the operators are `==` `===` `!=` `!==` `>` `<` `>=` `<=`.
- [x] **`==` is loose** (type conversion allowed). **`===` is strict** (value **and** type). Prefer `===` / `!==` when you care about type.
- [x] Strings use the **same operators** but compare **alphabetically** (Unicode order), not as numbers.
- [x] Mixed string/number: JavaScript **converts the string to a number**. `""` becomes `0`. A non-numeric string becomes **`NaN`**, and any `>` / `<` / `==` with `NaN` is **false**.
- [x] Convert with **`Number()`** and guard with **`isNaN()`** before you compare user input.

<a id="js-comparisons-example-01"></a>

### **Example 1: Equal to (`==`) vs strict equal (`===`)**

- [x] With `x = 5`: `x == 8` is **false**, `x == 5` is **true**.
- [x] **`x == "5"` is true** — loose equality converts the string `"5"` to the number `5`.
- [x] **`x === 5` is true**, but **`x === "5"` is false** — the number `5` and the string `"5"` are different types.
- [x] Use `===` unless you **want** type coercion.

Sandbox: `code_sandbox/js-comparisons/equal.html`

```javascript
let x = 5;
x == 8; // false
x == 5; // true
x == "5"; // true   (loose)
x === 5; // true
x === "5"; // false  (strict)
```

![js-comparisons example 1 source](../code_sandbox/snaps/js-comparisons-01-code.png)

![js-comparisons example 1 result](../code_sandbox/snaps/js-comparisons-01-result.png)

- [x] **Outcome:** loose `== "5"` is **true**; strict `=== "5"` is **false**.

<a id="js-comparisons-example-02"></a>

### **Example 2: Not equal and relational operators**

- [x] **`!=`** is the loose “not equal”; **`!==`** is strict (not equal **value or type**).
- [x] With `x = 5`: `x != 8` is **true**. `x !== 5` is **false** (same value and type). `x !== "5"` is **true** (number vs string). `x !== 8` is **true**.
- [x] Relational: `x > 8` **false**, `x < 8` **true**, `x >= 8` **false**, `x <= 8` **true**.
- [x] These same operators appear later in `if` conditions, e.g. `if (age < 18) text = "Too young to buy alcohol";`.

Sandbox: `code_sandbox/js-comparisons/relational.html`

```javascript
let x = 5;
x != 8; // true
x !== 5; // false
x !== "5"; // true
x !== 8; // true
x > 8; // false
x < 8; // true
x >= 8; // false
x <= 8; // true
```

![js-comparisons example 2 source](../code_sandbox/snaps/js-comparisons-02-code.png)

![js-comparisons example 2 result](../code_sandbox/snaps/js-comparisons-02-result.png)

- [x] **Outcome:** `!= 8` is **true**; `!== 5` is **false**; `!== "5"` is **true**; `x < 8` and `x <= 8` are **true**; `x > 8` and `x >= 8` are **false**.

<a id="js-comparisons-example-03"></a>

### **Example 3: String comparison (alphabetical)**

- [x] `"A" < "B"` is **true** — `"A"` comes first in the alphabet.
- [x] **`"20" < "5"` is also true**, because strings compare **character by character**. The first characters are `"2"` and `"5"`, and `"2"` comes before `"5"`. Numerically 20 is larger than 5 — that is the trap.
- [x] Alphabetically, **1 is less than 2**, so `"12"` starts with `"1"` and sorts before anything starting with `"2"`.

Sandbox: `code_sandbox/js-comparisons/strings.html`

```javascript
let text1 = "A";
let text2 = "B";
let result = text1 < text2; // true

let n1 = "20";
let n2 = "5";
n1 < n2; // true  ("2" before "5")
```

![js-comparisons example 3 source](../code_sandbox/snaps/js-comparisons-03-code.png)

![js-comparisons example 3 result](../code_sandbox/snaps/js-comparisons-03-result.png)

- [x] **Outcome:** `"A" < "B"` is **true**, and `"20" < "5"` is **true** (text order, not numeric order).

<a id="js-comparisons-example-04"></a>

### **Example 4: Comparing different types**

- [x] Number vs number: `2 < 12` is **true**.
- [x] Number vs numeric string: `2 < "12"` is **true** — `"12"` converts to `12`.
- [x] Number vs non-numeric string: `2 < "John"`, `2 > "John"`, and `2 == "John"` are all **false** — `"John"` becomes **`NaN`**, and `NaN` comparisons are false.
- [x] String vs string: `"2" < "12"` is **false** and `"2" > "12"` is **true** — first characters `"2"` vs `"1"`. `"2" == "12"` is **false**.
- [x] Empty string converts to **0** when compared with a number (not shown in the table, but stated on the page).

Sandbox: `code_sandbox/js-comparisons/types.html`

```javascript
2 < 12; // true
2 < "12"; // true
2 < "John"; // false
2 > "John"; // false
2 == "John"; // false
"2" < "12"; // false
"2" > "12"; // true
"2" == "12"; // false
```

![js-comparisons example 4 source](../code_sandbox/snaps/js-comparisons-04-code.png)

![js-comparisons example 4 result](../code_sandbox/snaps/js-comparisons-04-result.png)

- [x] **Outcome:** mixed number/numeric-string works (`2 < "12"` **true**); `"John"` yields **false**; two strings sort alphabetically (`"2" > "12"` **true**).

<a id="js-comparisons-example-05"></a>

### **Example 5: Convert before you compare**

- [x] To get a **proper numeric result**, convert first: `age = Number(age)`.
- [x] If conversion fails, **`isNaN(age)`** is true — treat that as “not a number”, do not compare it.
- [x] Otherwise use a comparison (here a **ternary**): `(age < 18) ? "Too young" : "Old enough"`.
- [x] Tested with `16` → **Too young**, `"21"` → **Old enough**, `"John"` → **Input is not a number**.

Sandbox: `code_sandbox/js-comparisons/convert.html`

```javascript
age = Number(age);
if (isNaN(age)) {
  voteable = "Input is not a number";
} else {
  voteable = age < 18 ? "Too young" : "Old enough";
}
```

![js-comparisons example 5 source](../code_sandbox/snaps/js-comparisons-05-code.png)

![js-comparisons example 5 result](../code_sandbox/snaps/js-comparisons-05-result.png)

- [x] **Outcome:** `16` → **Too young**; `"21"` → **Old enough**; `"John"` → **Input is not a number**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-comparisons/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What do comparison operators always return?

<details>
<summary>Answer</summary>

- [x] **`true` or `false`**.

</details>

### Question 2: What is `5 == "5"` vs `5 === "5"`?

<details>
<summary>Answer</summary>

- [x] **`==` is true** (loose; the string converts to a number).
- [x] **`===` is false** (strict; number vs string).

</details>

### Question 3: What is `x !== "5"` when `x` is the number `5`?

<details>
<summary>Answer</summary>

- [x] **true** — same value after coercion, but **different types**, so strict not-equal is true.

</details>

### Question 4: How are strings compared?

<details>
<summary>Answer</summary>

- [x] **Alphabetically** (character / Unicode order), not as numbers.
- [x] `"A" < "B"` is true.

</details>

### Question 5: Why is `"20" < "5"` true?

<details>
<summary>Answer</summary>

- [x] The first characters are `"2"` and `"5"`.
- [x] `"2"` comes **before** `"5"` in text order, so the whole string `"20"` is “less than” `"5"`.

</details>

### Question 6: Why is `"2" > "12"` true?

<details>
<summary>Answer</summary>

- [x] Both sides are **strings**, so they sort as text.
- [x] `"2"` vs `"1"` — `"2"` is greater, so `"2" > "12"`.

</details>

### Question 7: What is `2 < "John"`?

<details>
<summary>Answer</summary>

- [x] **false**.
- [x] `"John"` converts to **`NaN`**, and comparisons with `NaN` are false.

</details>

### Question 8: What does an empty string become in a number comparison?

<details>
<summary>Answer</summary>

- [x] **0**.

</details>

### Question 9: How do you compare user input as a number safely?

<details>
<summary>Answer</summary>

- [x] Convert with **`Number(age)`**.
- [x] If **`isNaN(age)`**, reject it; otherwise compare (e.g. `age < 18`).

</details>

### Question 10: What does `if (age < 18)` illustrate?

<details>
<summary>Answer</summary>

- [x] Comparison operators drive **conditional statements**.
- [x] The `if` chapter covers that in more depth.

</details>

</details>

## Summary

Comparisons always return booleans. **`==` / `!=` coerce types**; **`===` / `!==` do not**. Relational operators (`>` `<` `>=` `<=`) work on numbers and on strings, but strings sort **alphabetically** (`"20" < "5"` is true; `"2" > "12"` is true). Mixing a number with a non-numeric string yields **`NaN`** and **false**. Convert with **`Number()`** and check **`isNaN()`** before comparing input.

## References

- [JS Comparisons (W3Schools)](https://www.w3schools.com/js/js_comparisons.asp)
- [MDN: Equality comparisons and sameness](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness)
- [MDN: Comparison operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#relational_operators)
