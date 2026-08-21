# JS Arithmetic

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Arithmetic operators work on **numbers** (literals or variables). The numbers are **operands**; the symbol is the **operator**. This section covers `+ - * / % ++ -- **` and **precedence**.

This section has **4** examples:

- [x] **Example 1:** Basic arithmetic (`+ - * /`) [View](#js-arithmetic-example-01)
- [x] **Example 2:** Modulus (`%`) and exponentiation (`**`) [View](#js-arithmetic-example-02)
- [x] **Example 3:** Increment (`++`) and decrement (`--`) [View](#js-arithmetic-example-03)
- [x] **Example 4:** Operator precedence [View](#js-arithmetic-example-04)

## Detailed Explanation

- [x] **Arithmetic operators work on numbers** (literals or variables). In `100 + 50`, the numbers are the **operands** and `+` is the **operator**.
- [x] The set is `+ - * / % ** ++ --`, and expressions follow **operator precedence** rules.
- [x] Each demo below isolates one idea: basic math, remainder/power, increment/decrement, and precedence.

<a id="js-arithmetic-example-01"></a>

### **Example 1: Basic arithmetic (`+ - * /`)**

- [x] The four everyday operators add, subtract, multiply, and divide their operands.
- [x] Division returns the exact quotient here (`100 / 50` → `2`), but can produce decimals for uneven divisions.

Sandbox: `code_sandbox/js-arithmetic/basic.html`

```javascript
let a = 100,
  b = 50; // operands 100 and 50

a + b; // 150   +  add
a - b; // 50    -  subtract
a * b; // 5000  *  multiply
a / b; // 2     /  divide
```

![js-arithmetic example 1 source](../code_sandbox/snaps/js-arithmetic-01-code.png)

![js-arithmetic example 1 result](../code_sandbox/snaps/js-arithmetic-01-result.png)

- [x] **Outcome:** `150, 50, 5000, 2`.

<a id="js-arithmetic-example-02"></a>

### **Example 2: Modulus (`%`) and exponentiation (`**`)\*\*

- [x] **`%`** returns the **remainder** of a division (`5 % 2` → `1`); it is `0` when one number divides the other evenly.
- [x] **`**`** raises to a power (`5 ** 2`→`25`) and is **equivalent to `Math.pow(x, y)`\*\*.
- [x] `%` is handy for even/odd checks and cycling through ranges.

Sandbox: `code_sandbox/js-arithmetic/modulus.html`

```javascript
5 % 2; // 1    % remainder (modulus)
10 % 3; // 1
9 % 3; // 0    evenly divisible

5 ** 2; // 25   ** exponentiation (power)
2 ** 10; // 1024
Math.pow(5, 2); // 25  same as 5 ** 2
```

![js-arithmetic example 2 source](../code_sandbox/snaps/js-arithmetic-02-code.png)

![js-arithmetic example 2 result](../code_sandbox/snaps/js-arithmetic-02-result.png)

- [x] **Outcome:** the remainders are `1, 1, 0`, and the powers are `25, 1024`, with `Math.pow(5,2)` matching `5 ** 2`.

<a id="js-arithmetic-example-03"></a>

### **Example 3: Increment (`++`) and decrement (`--`)**

- [x] Both change a variable by **1**, but their **position** matters: **postfix** `x++` returns the **old** value then increments; **prefix** `++y` increments first and returns the **new** value.
- [x] `--` works the same way for subtracting 1.
- [x] This old/new distinction matters when you use the result in the same statement.

Sandbox: `code_sandbox/js-arithmetic/incdec.html`

```javascript
let x = 5;
let post = x++; // postfix: returns 5 (old), x becomes 6

let y = 5;
let pre = ++y; // prefix:  returns 6 (new), y becomes 6

let z = 8;
z--; // decrement: z becomes 7
```

![js-arithmetic example 3 source](../code_sandbox/snaps/js-arithmetic-03-code.png)

![js-arithmetic example 3 result](../code_sandbox/snaps/js-arithmetic-03-result.png)

- [x] **Outcome:** `x++` returned **5** (x is now 6), `++y` returned **6** (y is now 6), and `z--` left `z` at **7**.

<a id="js-arithmetic-example-04"></a>

### **Example 4: Operator precedence**

- [x] **`*` and `/` run before `+` and `-`**, so `100 + 50 * 3` is **250**, not `(100 + 50) * 3`.
- [x] **Parentheses** override the order: `(100 + 50) * 3` is **450**.
- [x] Operators of the **same** precedence run **left to right** (`100 + 50 - 3`), except **`**`** which is **right to left** (`2 ** 3 ** 2`is`2 \*\* 9` = 512).

Sandbox: `code_sandbox/js-arithmetic/precedence.html`

```javascript
100 + 50 * 3; // 250   * runs before +
(100 + 50) * 3; // 450   parentheses first
100 + 50 - 3; // 147   same level -> left to right
2 ** (3 ** 2); // 512   ** is right to left: 2 ** (3 ** 2)
```

![js-arithmetic example 4 source](../code_sandbox/snaps/js-arithmetic-04-code.png)

![js-arithmetic example 4 result](../code_sandbox/snaps/js-arithmetic-04-result.png)

- [x] **Outcome:** `250, 450, 147, 512` — precedence and associativity in action.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-arithmetic/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `%` return?

<details>
<summary>Answer</summary>

- [x] The **division remainder** (modulus).

</details>

### Question 2: What does `++` do?

<details>
<summary>Answer</summary>

- [x] It **increments** the number by 1.

</details>

### Question 3: Is `x ** y` the same as `Math.pow(x, y)`?

<details>
<summary>Answer</summary>

- [x] **Yes.**

</details>

### Question 4: In `100 + 50 * 3`, what runs first?

<details>
<summary>Answer</summary>

- [x] **Multiplication**, so it is not `(100 + 50) * 3`.
- [x] Use **parentheses** to add first.

</details>

### Question 5: What are operands and operators?

<details>
<summary>Answer</summary>

- [x] In `100 + 50`, the **operands** are `100` and `50`, and the **operator** is `+`.

</details>

### Question 6: What is the difference between `x++` and `++x`?

<details>
<summary>Answer</summary>

- [x] **`x++`** (postfix) returns the **old** value, then adds 1.
- [x] **`++x`** (prefix) adds 1 first, then returns the **new** value.

</details>

### Question 7: What is `9 % 3`?

<details>
<summary>Answer</summary>

- [x] **0** — 9 is evenly divisible by 3, so there is no remainder.

</details>

### Question 8: How do operators of the same precedence evaluate?

<details>
<summary>Answer</summary>

- [x] **Left to right** (e.g. `100 + 50 - 3`).
- [x] Exception: **`**`** evaluates **right to left\*\*.

</details>

</details>

## Summary

Arithmetic uses operands and operators: `+ - * / % ++ -- **`. `%` is the remainder and `**` matches `Math.pow`. Postfix `x++` returns the old value while prefix `++x` returns the new one. Multiplication/division precede addition/subtraction unless you use **parentheses**; same‑level operators run left to right (but `**` is right to left).

## References

- [JS Arithmetic (W3Schools)](https://www.w3schools.com/js/js_arithmetic.asp)
- [MDN: Arithmetic operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#arithmetic_operators)
- [JavaScript Operator Precedence Values](https://www.w3schools.com/js/js_precedence.asp)
