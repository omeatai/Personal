# JS Statements

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A computer program is a list of **instructions** to **execute**. Those instructions are **statements**. JavaScript statements run **one by one** in the order they are written. In HTML, the **browser** executes the program. This section covers **semicolons**, **white space**, **line breaks**, **code blocks**, and **keywords**.

This section has **3** examples:

- [x] **Example 1:** Statements and execution order [View](#js-statements-example-01)
- [x] **Example 2:** Semicolons separate statements [View](#js-statements-example-02)
- [x] **Example 3:** Code blocks [View](#js-statements-example-03)

## Detailed Explanation

- [x] **A program is a list of statements**
  - Each **statement** is one instruction; a program is many statements executed **top to bottom, in order**.
  - In a web page, the **browser** executes them.
  - Statements are built from **values, operators, expressions, keywords, and comments**.

<a id="js-statements-example-01"></a>

### **Example 1: Statements and execution order**

- [x] The four numbered lines run **in sequence**: declare `x, y, z`; assign `x = 5`; assign `y = 6`; then compute `z = x + y`.
- [x] Order matters — `z` can only be `11` because `x` and `y` were assigned **before** the `z = x + y` line.
- [x] The last statement writes **"Hello Dolly."** into `#demo` with `innerHTML`.

Sandbox: `code_sandbox/js-statements/statements.html`

```javascript
let x, y, z; // Statement 1
x = 5; // Statement 2
y = 6; // Statement 3
z = x + y; // Statement 4
document.getElementById("demo").innerHTML = "Hello Dolly.";
```

![js-statements example 1 source](../code_sandbox/snaps/js-statements-01-code.png)

![js-statements example 1 result](../code_sandbox/snaps/js-statements-01-result.png)

- [x] **Outcome:** the page prints **x = 5, y = 6, z = x + y = 11** and the message **Hello Dolly.**

<a id="js-statements-example-02"></a>

### **Example 2: Semicolons separate statements**

- [x] A **semicolon** ends an executable statement. Ending statements with `;` is **not strictly required** but **highly recommended**.
- [x] Because semicolons separate statements, you can even put **several on one line**: `a = 5; b = 6; c = a + b;`.
- [x] **White space** is ignored: `let person = "Hege";` and `let person="Hege";` are equivalent — put spaces around operators for readability.

Sandbox: `code_sandbox/js-statements/semicolons.html`

```javascript
let a, b, c; // Declare 3 variables
a = 5; // Assign 5 to a
b = 6; // Assign 6 to b
c = a + b; // Assign the sum to c

// multiple statements on one line are allowed:
a = 5;
b = 6;
c = a + b;
```

![js-statements example 2 source](../code_sandbox/snaps/js-statements-02-code.png)

![js-statements example 2 result](../code_sandbox/snaps/js-statements-02-result.png)

- [x] **Outcome:** the page reports **a = 5, b = 6, c = a + b = 11** — the three statements executed and produced the sum.

<a id="js-statements-example-03"></a>

### **Example 3: Code blocks**

- [x] Statements grouped inside **curly brackets `{ ... }`** form a **code block** that runs together.
- [x] Functions are the most common place you meet blocks; this tutorial uses **2 spaces** of indentation.
- [x] Calling `myFunction()` runs **both** inner statements, filling `#demo1` and `#demo2`.

Sandbox: `code_sandbox/js-statements/blocks.html`

```javascript
function myFunction() {
  document.getElementById("demo1").innerHTML = "Hello Dolly!";
  document.getElementById("demo2").innerHTML = "How are you?";
}
myFunction();
```

![js-statements example 3 source](../code_sandbox/snaps/js-statements-03-code.png)

![js-statements example 3 result](../code_sandbox/snaps/js-statements-03-result.png)

- [x] **Outcome:** both paragraphs appear — **Hello Dolly!** and **How are you?** — because the block's two statements ran together.

### **Line breaks and keywords (reference)**

- [x] **Line length:** for readability, keep lines under ~**80 characters**; if a statement is too long, break it **after an operator** (e.g. after `=`).
- [x] **Keywords** often start a statement and name the action to perform. They are **reserved words** and cannot be used as variable names:

| Keyword    | Description                                |
| ---------- | ------------------------------------------ |
| `var`      | Declares a variable                        |
| `let`      | Declares a block variable                  |
| `const`    | Declares a block constant                  |
| `if`       | Marks statements to run on a condition     |
| `switch`   | Marks statements to run in different cases |
| `for`      | Marks statements to run in a loop          |
| `function` | Declares a function                        |
| `return`   | Exits a function                           |
| `try`      | Implements error handling for a block      |

- [x] **Page exercise —** _How many statements in `let a = 5; let b = 6; c = a + b;`?_ → **3** (each `;`-separated instruction is one statement).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-statements/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a JavaScript statement?

<details>
<summary>Answer</summary>

- [x] A programming **instruction** to be **executed**.
- [x] Statements run **one by one**, in the order they are written.

</details>

### Question 2: Who executes JavaScript in HTML?

<details>
<summary>Answer</summary>

- [x] The **web browser**.

</details>

### Question 3: What are statements composed of?

<details>
<summary>Answer</summary>

- [x] Values, operators, expressions, keywords, and comments.

</details>

### Question 4: Are semicolons required?

<details>
<summary>Answer</summary>

- [x] They **separate** statements.
- [x] They are **not required**, but **highly recommended**.

</details>

### Question 5: Where should you break a long statement?

<details>
<summary>Answer</summary>

- [x] After an **operator**.
- [x] Prefer lines no longer than **80 characters**.

</details>

### Question 6: What is a code block?

<details>
<summary>Answer</summary>

- [x] Statements grouped in **curly brackets** `{...}` to run **together**.
- [x] Functions are a common place for blocks.

</details>

### Question 7: Can you use a keyword as a variable name?

<details>
<summary>Answer</summary>

- [x] **No.** Keywords are **reserved words**.

</details>

### Question 8: How many statements are in `let a = 5; let b = 6; c = a + b;`?

<details>
<summary>Answer</summary>

- [x] **Three** statements, separated by semicolons.

</details>

</details>

## Summary

Statements are instructions the browser runs **in order**. End them with **semicolons** (recommended). White space is flexible; break long lines **after an operator**. Group work in **`{...}`** blocks (as in functions). **Keywords** start many statements and cannot be variable names.

## References

- [JS Statements (W3Schools)](https://www.w3schools.com/js/js_statements.asp)
- [MDN: JavaScript statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
- [MDN: Lexical grammar — Automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
