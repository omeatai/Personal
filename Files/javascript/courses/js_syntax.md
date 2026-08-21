# JS Syntax

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

JavaScript **syntax** is the set of rules for writing the language. Values are **literals** (fixed) or **variables**. This section covers **numbers**, **strings**, **keywords** (`let`, `const`), **identifiers**, **operators**, **expressions**, **case sensitivity**, and **camel case**.

This section has **4** examples:

- [x] **Example 1:** Literals (fixed values) [View](#js-syntax-example-01)
- [x] **Example 2:** Keywords, variables, and identifiers [View](#js-syntax-example-02)
- [x] **Example 3:** Operators and expressions [View](#js-syntax-example-03)
- [x] **Example 4:** Case sensitivity and camelCase [View](#js-syntax-example-04)

## Detailed Explanation

- [x] **Syntax = the rules for how programs are constructed**
  - Declaring variables (`let x = 5;`), computing values (`let z = x + y;`), and comments (`// ...`) are all governed by syntax rules.
- [x] **Two kinds of values**
  - **Literals** are fixed values written directly in code.
  - **Variables** are named containers whose value can change.
- [x] Each example below is a small page that computes real values with `<script>` and prints them, so you can see what the rules produce.

<a id="js-syntax-example-01"></a>

### **Example 1: Literals (fixed values)**

- [x] **Number literals** are written with or without decimals: `10.50` (shows as `10.5`) and `1001`.
- [x] **String literals** are text wrapped in **double or single quotes**: `"John Doe"` and `'John Doe'` are equally valid.
- [x] A literal is just the value itself — no name attached.

Sandbox: `code_sandbox/js-syntax/literals.html`

```javascript
// Numbers, with or without decimals
10.5;
1001;

// Strings, in double or single quotes
("John Doe");
("John Doe");
```

![js-syntax example 1 source](../code_sandbox/snaps/js-syntax-01-code.png)

![js-syntax example 1 result](../code_sandbox/snaps/js-syntax-01-result.png)

- [x] **Outcome:** the page prints the numbers **10.5, 1001** and the strings **"John Doe", 'John Doe'**, confirming both number forms and both quote styles are valid.

<a id="js-syntax-example-02"></a>

### **Example 2: Keywords, variables, and identifiers**

- [x] **Keywords** define actions. **`let`** and **`const`** both create variables (`let x = 5;`, `const fname = "John";`).
- [x] Keywords are **case-sensitive**: `LET` or `Let` is **not** the keyword `let`.
- [x] A variable can be **defined first and assigned later** (`let y;` then `y = 6;`).
- [x] **Identifier rules:** must start with a **letter, `_`, or `$`**; may contain digits after the first character; cannot be a **reserved keyword**; and are **case-sensitive**.

Sandbox: `code_sandbox/js-syntax/variables.html`

```javascript
let x = 5;
const fname = "John";

let y;
y = 6;
```

![js-syntax example 2 source](../code_sandbox/snaps/js-syntax-02-code.png)

![js-syntax example 2 result](../code_sandbox/snaps/js-syntax-02-result.png)

- [x] **Outcome:** the page reports **let x = 5**, **const fname = "John"**, and **y = 6** — the define-then-assign step worked.

<a id="js-syntax-example-03"></a>

### **Example 3: Operators and expressions**

- [x] The **assignment** operator `=` stores a value; **arithmetic** operators `+ - * /` compute values.
- [x] An **expression** combines values, variables, and operators and **evaluates to a single value**: `(5 + 6) * 10` → **110** (parentheses first).
- [x] With strings, `+` means **concatenation**: `"John" + " " + "Doe"` → **"John Doe"**.

Sandbox: `code_sandbox/js-syntax/expressions.html`

```javascript
let x = 5,
  y = 6;
let sum = x + y; // 11
5 * 10; // 50
(5 + 6) * 10; // 110
"John" + " " + "Doe"; // "John Doe"
```

![js-syntax example 3 source](../code_sandbox/snaps/js-syntax-03-code.png)

![js-syntax example 3 result](../code_sandbox/snaps/js-syntax-03-result.png)

- [x] **Outcome:** the page prints **x + y = 11**, **5 \* 10 = 50**, **(5 + 6) \* 10 = 110**, and **"John" + " " + "Doe" = John Doe**.

<a id="js-syntax-example-04"></a>

### **Example 4: Case sensitivity and camelCase**

- [x] Identifiers are **case-sensitive**: `lastName` and `lastname` are **two different variables** holding different values.
- [x] Naming conventions: **hyphens are not allowed** (`first-name` is reserved for subtraction); underscore (`first_name`), **UpperCamelCase/Pascal** (`FirstName`), and **lowerCamelCase** (`firstName`) are all possible.
- [x] JavaScript programmers **conventionally use lowerCamelCase** for variables.

Sandbox: `code_sandbox/js-syntax/case.html`

```javascript
let lastName = "Doe";
let lastname = "Peterson"; // different variable!
```

![js-syntax example 4 source](../code_sandbox/snaps/js-syntax-04-code.png)

![js-syntax example 4 result](../code_sandbox/snaps/js-syntax-04-result.png)

- [x] **Outcome:** the page shows **lastName = Doe** and **lastname = Peterson** side by side — proof the two names are distinct.
- [x] **Page exercise —** _Correct syntax to assign a value?_ → **`x = 5`** (not `x : 5`, `x == 5`, or `x -> 5`).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-syntax/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What two types of values does JavaScript syntax define?

<details>
<summary>Answer</summary>

- [x] **Literals** (fixed values).
- [x] **Variables** (variable values).

</details>

### Question 2: How are number and string literals written?

<details>
<summary>Answer</summary>

- [x] Numbers: with or without decimals (`10.50`, `1001`).
- [x] Strings: in **double or single quotes**.

</details>

### Question 3: Are JavaScript keywords case-sensitive?

<details>
<summary>Answer</summary>

- [x] **Yes.** `LET` or `Let` is **not** the keyword `let`.

</details>

### Question 4: What are the identifier rules?

<details>
<summary>Answer</summary>

- [x] Start with a letter, `_`, or `$`.
- [x] Digits are allowed after the first character.
- [x] Cannot be a reserved keyword.
- [x] Are case-sensitive.

</details>

### Question 5: What does `(5 + 6) * 10` evaluate to?

<details>
<summary>Answer</summary>

- [x] **110**.

</details>

### Question 6: Are `lastName` and `lastname` the same variable?

<details>
<summary>Answer</summary>

- [x] **No.** Identifiers are **case sensitive**.

</details>

### Question 7: Why are hyphens not allowed in variable names?

<details>
<summary>Answer</summary>

- [x] Hyphens are reserved for **subtractions**.

</details>

### Question 8: Which naming style do JavaScript programmers tend to use?

<details>
<summary>Answer</summary>

- [x] **Lower camel case** (`firstName`, `lastName`).

</details>

</details>

## Summary

Syntax covers **literals** (numbers and quoted strings) and **variables** created with **`let`** / **`const`**. Identifiers must start with a letter, `_`, or `$`, cannot be keywords, and are **case-sensitive**. Use **`=`** to assign and **`+ - * /`** to compute. Expressions such as `(5 + 6) * 10` yield **110**. Prefer **lower camel case**; **hyphens are not allowed**.

## References

- [JS Syntax (W3Schools)](https://www.w3schools.com/js/js_syntax.asp)
- [MDN: Grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types)
- [MDN: Lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
