# JS Operators

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Operators perform **math and logic**. This page introduces **assignment (`=`)**, **addition (`+`)**, **multiplication (`*`)**, **comparison (`>`)**, **string concatenation**, and **logical** operators (`&&`, `||`, `!`).

This section has **4** examples:

- [x] **Example 1:** Arithmetic operators [View](#js-operators-example-01)
- [x] **Example 2:** Assignment operators [View](#js-operators-example-02)
- [x] **Example 3:** Comparison & logical operators [View](#js-operators-example-03)
- [x] **Example 4:** String operators [View](#js-operators-example-04)

## Detailed Explanation

- [x] **Operators combine values and variables** into expressions that produce a result.
- [x] JavaScript groups them into families: **arithmetic** (`+ - * / % **`), **assignment** (`= += -= …`), **comparison** (`== === != > <`), **logical** (`&& || !`), and **string** (`+`, `+=`).
- [x] Each family below has its own runnable demo; the Arithmetic, Assignment, and Comparison chapters go deeper on each.

<a id="js-operators-example-01"></a>

### **Example 1: Arithmetic operators**

- [x] `+ - * /` do the usual math; **`%`** is the **remainder (modulus)** and **`**`** is **exponentiation (power)\*\*.
- [x] **`++`** and **`--`** increment/decrement a variable by 1.
- [x] Division can produce a **float** (`10 / 3` → `3.333…`).

Sandbox: `code_sandbox/js-operators/arithmetic.html`

```javascript
let a = 10,
  b = 3;

a + b; // 13   addition
a - b; // 7    subtraction
a * b; // 30   multiplication
a / b; // 3.33 division
a % b; // 1    remainder (modulus)
a ** b; // 1000 exponentiation (power)

let x = 5;
x++; // 6  increment
let y = 5;
y--; // 4  decrement
```

![js-operators example 1 source](../code_sandbox/snaps/js-operators-01-code.png)

![js-operators example 1 result](../code_sandbox/snaps/js-operators-01-result.png)

- [x] **Outcome:** `13, 7, 30, 3.333…, 1, 1000`, and the counters become **6** and **4**.

<a id="js-operators-example-02"></a>

### **Example 2: Assignment operators**

- [x] **`=`** assigns; the compound forms **`+= -= \*= /= %= **=`\*\* apply the operation to the current value and store the result.
- [x] `x += 5` is exactly shorthand for `x = x + 5`.
- [x] The demo threads one `x` through every operator so you can watch it change.

Sandbox: `code_sandbox/js-operators/assignment.html`

```javascript
let x = 10; // =    x is 10
x += 5; // +=   x is 15
x -= 3; // -=   x is 12
x *= 2; // *=   x is 24
x /= 4; // /=   x is 6
x %= 4; // %=   x is 2
x **= 3; // **=  x is 8
```

![js-operators example 2 source](../code_sandbox/snaps/js-operators-02-code.png)

![js-operators example 2 result](../code_sandbox/snaps/js-operators-02-result.png)

- [x] **Outcome:** `x` walks through **10 → 15 → 12 → 24 → 6 → 2 → 8**.

<a id="js-operators-example-03"></a>

### **Example 3: Comparison & logical operators**

- [x] Comparison operators always return a **boolean**: **`==`** compares value only (loose), **`===`** compares value **and** type (strict).
- [x] So `10 == "10"` is **true** but `10 === "10"` is **false**.
- [x] Logical operators combine booleans: **`&&`** (AND), **`||`** (OR), **`!`** (NOT).

Sandbox: `code_sandbox/js-operators/comparison.html`

```javascript
10 == "10"; // true   loose equality (value only)
10 === "10"; // false  strict equality (value + type)
10 != 8; // true   not equal
10 > 8; // true   greater than

10 > 5 && 10 < 20; // true   && AND
10 > 5 || 10 > 20; // true   || OR
!(10 > 5); // false  !  NOT
```

![js-operators example 3 source](../code_sandbox/snaps/js-operators-03-code.png)

![js-operators example 3 result](../code_sandbox/snaps/js-operators-03-result.png)

- [x] **Outcome:** loose `==` is **true** while strict `===` is **false**; the AND/OR expressions are **true** and the NOT flips to **false**.

<a id="js-operators-example-04"></a>

### **Example 4: String operators**

- [x] On strings, **`+`** is **concatenation** — it joins them (`"John" + " " + "Doe"` → `"John Doe"`).
- [x] **`+=`** appends to an existing string (`greet += " World"`).
- [x] Mixing a **number and a string** with `+` produces a **string** (`"5" + 5` → `"55"`, `"Hello" + 5` → `"Hello5"`), while `5 + 5` stays a number **10**.

Sandbox: `code_sandbox/js-operators/strings.html`

```javascript
let text1 = "John";
let text2 = "Doe";
text1 + " " + text2; // "John Doe"  concatenation

let greet = "Hello";
greet += " World"; // "Hello World"  append with +=

5 + 5; // 10       number + number
"5" + 5; // "55"     string + number -> string
"Hello" + 5; // "Hello5" string + number -> string
```

![js-operators example 4 source](../code_sandbox/snaps/js-operators-04-code.png)

![js-operators example 4 result](../code_sandbox/snaps/js-operators-04-result.png)

- [x] **Outcome:** the names join to **John Doe**, `greet` becomes **Hello World**, and mixing a string with a number concatenates (**55**, **Hello5**) while pure numbers add to **10**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-operators/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `=` do vs `+` vs `*` vs `>`?

<details>
<summary>Answer</summary>

- [x] `=` **assigns**.
- [x] `+` **adds** (or concatenates strings).
- [x] `*` **multiplies**.
- [x] `>` **compares**.

</details>

### Question 2: What is `5 + "5"`?

<details>
<summary>Answer</summary>

- [x] **`"55"`** (a string).
- [x] Adding a number and a string returns a **string**.

</details>

### Question 3: What is `+` called when used on strings?

<details>
<summary>Answer</summary>

- [x] The **concatenation** operator.

</details>

### Question 4: What does the `%` operator do?

<details>
<summary>Answer</summary>

- [x] Returns the **remainder** of a division (modulus): `10 % 3` is **1**.

</details>

### Question 5: What is the difference between `==` and `===`?

<details>
<summary>Answer</summary>

- [x] **`==`** compares **value only** (loose), with type conversion.
- [x] **`===`** compares **value and type** (strict).
- [x] `10 == "10"` is `true`, but `10 === "10"` is `false`.

</details>

### Question 6: What do `&&`, `||`, and `!` do?

<details>
<summary>Answer</summary>

- [x] **`&&`** logical AND, **`||`** logical OR, **`!`** logical NOT.

</details>

### Question 7: What is `x += 5` shorthand for?

<details>
<summary>Answer</summary>

- [x] `x = x + 5`.

</details>

### Question 8: What type does a comparison operator return?

<details>
<summary>Answer</summary>

- [x] Always a **boolean** (`true` or `false`).

</details>

### Question 9: What does the `**` operator do?

<details>
<summary>Answer</summary>

- [x] **Exponentiation** (power): `10 ** 3` is **1000**.

</details>

</details>

## Summary

Operators come in families: **arithmetic** (`+ - * / % **`, `++`/`--`), **assignment** (`=`, `+=`, …), **comparison** (`==` loose vs `===` strict, returning booleans), **logical** (`&& || !`), and **string** (`+`, `+=`). Mixing a number with a string via `+` concatenates into a string.

## References

- [JS Operators (W3Schools)](https://www.w3schools.com/js/js_operators.asp)
- [MDN: Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
