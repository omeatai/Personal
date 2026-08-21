# JS Style Guide

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Coding conventions are agreed style: names, whitespace, indentation, comments, and practices. They improve readability and maintenance. W3Schools uses camelCase, spaces around operators, 2-space indent (not tabs), semicolons on simple statements, K&R braces for functions/loops/ifs, object rules (colon-space, no trailing comma in their guide, `};`), lines under 80 characters, script src without type, matching HTML ids, .html/.css/.js extensions, and lower-case file names. Computers ignore extra spaces — minify only for production.

This section has **17** examples:

- [x] **Example 1:** camelCase identifier names (firstName, lastName) [View](#js-style-guide-example-01)
- [x] **Example 2:** Spaces around operators and after commas [View](#js-style-guide-example-02)
- [x] **Example 3:** Indent code blocks with 2 spaces (not tabs) [View](#js-style-guide-example-03)
- [x] **Example 4:** End simple statements with a semicolon [View](#js-style-guide-example-04)
- [x] **Example 5:** Functions: `{` at end of first line; no semicolon after `}` [View](#js-style-guide-example-05)
- [x] **Example 6:** for loop: `{` on the `for` line [View](#js-style-guide-example-06)
- [x] **Example 7:** if / else: `{` on the same line as if/else [View](#js-style-guide-example-07)
- [x] **Example 8:** Object rules: `{` same line, colon-space, no trailing comma, `};` [View](#js-style-guide-example-08)
- [x] **Example 9:** Short objects may be one compressed line [View](#js-style-guide-example-09)
- [x] **Example 10:** Break long lines after an operator or comma (line length < 80) [View](#js-style-guide-example-10)
- [x] **Example 11:** Hyphens are not allowed in JavaScript names [View](#js-style-guide-example-11)
- [x] **Example 12:** camelCase vs under_score vs PascalCase vs $ [View](#js-style-guide-example-12)
- [x] **Example 13:** Load scripts with <script src="myscript.js"> (no type) [View](#js-style-guide-example-13)
- [x] **Example 14:** getElementById("Demo") vs getElementById("demo") [View](#js-style-guide-example-14)
- [x] **Example 15:** File extensions: .html .css .js [View](#js-style-guide-example-15)
- [x] **Example 16:** Use lower-case file names [View](#js-style-guide-example-16)
- [x] **Example 17:** Readability in development; minify production [View](#js-style-guide-example-17)

## Detailed Explanation

- [x] **camelCase** names. **Spaces** around `= + - * /` and after commas.
- [x] **2 spaces**, not tabs. Simple statements end with **`;`. Compound `}` has **no** semicolon.
- [x] Objects: `{` same line, **colon space**, optional short one-liner, **`;`** after `}`.
- [x] Break long lines **after** an operator/comma. **No hyphens** in JS names. Avoid leading **`$`**.
- [x] `getElementById` is **case-sensitive**. Prefer **lower-case** file names.

<a id="js-style-guide-example-01"></a>

### **Example 1: camelCase identifier names (firstName, lastName)**

- [x] W3Schools uses **camelCase** for variables and functions. Names **start with a letter**.
- [x] `firstName`, `lastName`, `fullPrice` — not `first_name` in their examples.

Sandbox: `code_sandbox/js-style-guide/camelcase-names.html`

```javascript
firstName = "John";
lastName = "Doe";
price = 19.90;
tax = 0.20;
fullPrice = price + (price * tax);
```

<img alt="js-style-guide example 1 source" src="../code_sandbox/snaps/js-style-guide-01-code.png" />

<img alt="js-style-guide example 1 result" src="../code_sandbox/snaps/js-style-guide-01-result.png" />

- [x] **Outcome:** **fullPrice** is **23.88**. These assignments without `let`/`const` create **globals** in sloppy mode — the next chapter says to avoid that. The **names** are the lesson here.

<a id="js-style-guide-example-02"></a>

### **Example 2: Spaces around operators and after commas**

- [x] Always put **spaces around operators** `= + - * /` and **after commas**.
- [x] `let x = y + z;` not `let x=y+z;`.

Sandbox: `code_sandbox/js-style-guide/spaces-around-operators.html`

```javascript
let x = y + z;
const myArray = ["Volvo", "Saab", "Fiat"];
```

<img alt="js-style-guide example 2 source" src="../code_sandbox/snaps/js-style-guide-02-code.png" />

<img alt="js-style-guide example 2 result" src="../code_sandbox/snaps/js-style-guide-02-result.png" />

- [x] **Outcome:** `x` is **5** (`2 + 3`). `myArray` is **Volvo, Saab, Fiat**.

<a id="js-style-guide-example-03"></a>

### **Example 3: Indent code blocks with 2 spaces (not tabs)**

- [x] Always use **2 spaces** for indentation.
- [x] **Do not use tabs** — editors disagree on tab width.

Sandbox: `code_sandbox/js-style-guide/indent-two-spaces.html`

```javascript
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}
```

<img alt="js-style-guide example 3 source" src="../code_sandbox/snaps/js-style-guide-03-code.png" />

<img alt="js-style-guide example 3 result" src="../code_sandbox/snaps/js-style-guide-03-result.png" />

- [x] **Outcome:** **toCelsius(32)** is **0**. **toCelsius(212)** is **100**.

<a id="js-style-guide-example-04"></a>

### **Example 4: End simple statements with a semicolon**

- [x] Simple statements **end with `;`**.
- [x] Arrays and objects used as **values** are simple statements when assigned.

Sandbox: `code_sandbox/js-style-guide/semicolon-simple-statements.html`

```javascript
const cars = ["Volvo", "Saab", "Fiat"];
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};
```

<img alt="js-style-guide example 4 source" src="../code_sandbox/snaps/js-style-guide-04-code.png" />

<img alt="js-style-guide example 4 result" src="../code_sandbox/snaps/js-style-guide-04-result.png" />

- [x] **Outcome:** **cars.length** is **3**. **person.firstName** is **John**.

<a id="js-style-guide-example-05"></a>

### **Example 5: Functions: `{` at end of first line; no semicolon after `}`**

- [x] Compound statements: opening **`{` at the end of the first line**, one space before `{`.
- [x] Closing **`}` on its own line**, **no leading spaces**, **no semicolon** after the block.

Sandbox: `code_sandbox/js-style-guide/function-brackets.html`

```javascript
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}
```

<img alt="js-style-guide example 5 source" src="../code_sandbox/snaps/js-style-guide-05-code.png" />

<img alt="js-style-guide example 5 result" src="../code_sandbox/snaps/js-style-guide-05-result.png" />

- [x] **Outcome:** Same function as the indent example. The **style** is: `{` on the signature line, `}` alone, no `;` after `}`.

<a id="js-style-guide-example-06"></a>

### **Example 6: for loop: `{` on the `for` line**

- [x] Same bracket rule as functions: `for (...) {` then the body, then `}`.

Sandbox: `code_sandbox/js-style-guide/loop-brackets.html`

```javascript
for (let i = 0; i < 5; i++) {
  x += i;
}
```

<img alt="js-style-guide example 6 source" src="../code_sandbox/snaps/js-style-guide-06-code.png" />

<img alt="js-style-guide example 6 result" src="../code_sandbox/snaps/js-style-guide-06-result.png" />

- [x] **Outcome:** Starting `x = 0`, after `i = 0..4`, **x** is **10** (0+1+2+3+4).

<a id="js-style-guide-example-07"></a>

### **Example 7: if / else: `{` on the same line as if/else**

- [x] `if (time < 20) {` ... `} else {` ... `}`.
- [x] Do **not** put `{` on the next line in this style guide.

Sandbox: `code_sandbox/js-style-guide/if-else-brackets.html`

```javascript
if (time < 20) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}
```

<img alt="js-style-guide example 7 source" src="../code_sandbox/snaps/js-style-guide-07-code.png" />

<img alt="js-style-guide example 7 result" src="../code_sandbox/snaps/js-style-guide-07-result.png" />

- [x] **Outcome:** With **time = 15**, greeting is **"Good day"**. With **time = 21**, **"Good evening"**.

<a id="js-style-guide-example-08"></a>

### **Example 8: Object rules: `{` same line, colon-space, no trailing comma, `};`**

- [x] Opening `{` on the **same line** as the assignment.
- [x] **Colon + space** between property and value. **Quotes** around **strings**, not around numbers.
- [x] **No comma** after the last property (W3Schools rule; trailing commas are legal in modern JS — they still warn for old IE / JSON).
- [x] Closing `}` on a new line. **Always** end the definition with **`;`**.

Sandbox: `code_sandbox/js-style-guide/object-rules.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};
```

<img alt="js-style-guide example 8 source" src="../code_sandbox/snaps/js-style-guide-08-code.png" />

<img alt="js-style-guide example 8 result" src="../code_sandbox/snaps/js-style-guide-08-result.png" />

- [x] **Outcome:** **person.age** is **50** (number, unquoted). **eyeColor** is **blue**.

<a id="js-style-guide-example-09"></a>

### **Example 9: Short objects may be one compressed line**

- [x] Short objects can sit on **one line**, spaces **between properties**.

Sandbox: `code_sandbox/js-style-guide/short-object.html`

```javascript
const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
```

<img alt="js-style-guide example 9 source" src="../code_sandbox/snaps/js-style-guide-09-code.png" />

<img alt="js-style-guide example 9 result" src="../code_sandbox/snaps/js-style-guide-09-result.png" />

- [x] **Outcome:** Same data as the multi-line object. **firstName** is **John**.

<a id="js-style-guide-example-10"></a>

### **Example 10: Break long lines after an operator or comma (line length < 80)**

- [x] Avoid lines **longer than 80 characters**.
- [x] If a statement does not fit, break **after an operator or a comma**.
- [x] This is the page’s Tryit: assign **Hello Dolly.** across two lines after `=`.

Sandbox: `code_sandbox/js-style-guide/line-length-80.html`

```javascript
document.getElementById("demo").innerHTML =
"Hello Dolly.";
```

<img alt="js-style-guide example 10 source" src="../code_sandbox/snaps/js-style-guide-10-code.png" />

<img alt="js-style-guide example 10 result" src="../code_sandbox/snaps/js-style-guide-10-result.png" />

- [x] **Outcome:** The paragraph reads **Hello Dolly.**

<a id="js-style-guide-example-11"></a>

### **Example 11: Hyphens are not allowed in JavaScript names**

- [x] HTML/CSS use hyphens (`data-price`, `font-size`). **JavaScript names cannot**.
- [x] `first-name` is parsed as **subtraction** (`first - name`), or is a SyntaxError as a binding.

Sandbox: `code_sandbox/js-style-guide/naming-hyphens-illegal.html`

```javascript
// first-name = "John";  // illegal as a variable name
const firstName = "John";
```

<img alt="js-style-guide example 11 source" src="../code_sandbox/snaps/js-style-guide-11-code.png" />

<img alt="js-style-guide example 11 result" src="../code_sandbox/snaps/js-style-guide-11-result.png" />

- [x] **Outcome:** **firstName** works. `let first-name` is a **SyntaxError**.

<a id="js-style-guide-example-12"></a>

### **Example 12: camelCase vs under_score vs PascalCase vs $**

- [x] **camelCase** — JavaScript itself, jQuery, most JS libraries.
- [x] **under_score** — common in SQL / PHP docs (`date_of_birth`).
- [x] **PascalCase** — often constructors / classes (C-style too).
- [x] **UPPERCASE** — common for globals/constants like **PI** (W3Schools say they don’t, but it is common).
- [x] Do **not** start names with **`$`** — that collides with many library names.

Sandbox: `code_sandbox/js-style-guide/naming-styles.html`

```javascript
const firstName = "camel";
const date_of_birth = "underscore";
const Person = { kind: "PascalCase constructor style" };
const PI = 3.14;
```

<img alt="js-style-guide example 12 source" src="../code_sandbox/snaps/js-style-guide-12-code.png" />

<img alt="js-style-guide example 12 result" src="../code_sandbox/snaps/js-style-guide-12-result.png" />

- [x] **Outcome:** All four bind. `$foo` as a name is **legal JS** but the style guide says **avoid it**.

<a id="js-style-guide-example-13"></a>

### **Example 13: Load scripts with <script src="myscript.js"> (no type)**

- [x] Use simple syntax for external scripts. The **`type` attribute is not necessary** (`text/javascript` is the default).

Sandbox: `code_sandbox/js-style-guide/script-src-no-type.html`

```javascript
<script src="myscript.js"></script>
```

<img alt="js-style-guide example 13 source" src="../code_sandbox/snaps/js-style-guide-13-code.png" />

<img alt="js-style-guide example 13 result" src="../code_sandbox/snaps/js-style-guide-13-result.png" />

- [x] **Outcome:** The sandbox `myscript.js` sets **loaded = yes**. No `type=` needed.

<a id="js-style-guide-example-14"></a>

### **Example 14: getElementById("Demo") vs getElementById("demo")**

- [x] HTML **id** matching in `getElementById` is **case-sensitive**.
- [x] `id="demo"` is **not** found as `"Demo"`. Untidy HTML + JS naming causes **null** and then TypeErrors.
- [x] Use the **same** convention in HTML as in JS (camelCase / lowercase).

Sandbox: `code_sandbox/js-style-guide/html-id-case.html`

```javascript
const obj = document.getElementById("Demo");
const obj2 = document.getElementById("demo");
```

<img alt="js-style-guide example 14 source" src="../code_sandbox/snaps/js-style-guide-14-code.png" />

<img alt="js-style-guide example 14 result" src="../code_sandbox/snaps/js-style-guide-14-result.png" />

- [x] **Outcome:** **Demo** is **null**. **demo** is the paragraph element. Always match case.

<a id="js-style-guide-example-15"></a>

### **Example 15: File extensions: .html .css .js**

- [x] HTML: **`.html`** (`.htm` allowed). CSS: **`.css`**. JavaScript: **`.js`**.

Sandbox: `code_sandbox/js-style-guide/file-extensions.html`

```javascript
const files = ["index.html", "style.css", "app.js"];
```

<img alt="js-style-guide example 15 source" src="../code_sandbox/snaps/js-style-guide-15-code.png" />

<img alt="js-style-guide example 15 result" src="../code_sandbox/snaps/js-style-guide-15-result.png" />

- [x] **Outcome:** Three conventional extensions. Servers and editors rely on them.

<a id="js-style-guide-example-16"></a>

### **Example 16: Use lower-case file names**

- [x] **Apache / Unix** file names are **case-sensitive**: `london.jpg` ≠ `London.jpg`.
- [x] **IIS / Windows** often are **not**. Mixing case **breaks** when you deploy to Linux.
- [x] Prefer **all lower-case** names.

Sandbox: `code_sandbox/js-style-guide/lowercase-filenames.html`

```javascript
const unix = "london.jpg" === "London.jpg";
```

<img alt="js-style-guide example 16 source" src="../code_sandbox/snaps/js-style-guide-16-code.png" />

<img alt="js-style-guide example 16 result" src="../code_sandbox/snaps/js-style-guide-16-result.png" />

- [x] **Outcome:** In JavaScript string compare, **london.jpg === London.jpg** is **false** — same trap as a case-sensitive server.

<a id="js-style-guide-example-17"></a>

### **Example 17: Readability in development; minify production**

- [x] Computers **ignore** extra spaces. Conventions are for **humans**.
- [x] Prefer **readability** while developing. **Minify** large production scripts.

Sandbox: `code_sandbox/js-style-guide/readability-vs-minify.html`

```javascript
let x = 1 + 2;
let y=1+2;
```

<img alt="js-style-guide example 17 source" src="../code_sandbox/snaps/js-style-guide-17-code.png" />

<img alt="js-style-guide example 17 result" src="../code_sandbox/snaps/js-style-guide-17-result.png" />

- [x] **Outcome:** Both **x** and **y** are **3**. Spaces did not change the result — only the **read** of the source.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-style-guide/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What naming style does W3Schools use?

<details>
<summary>Answer</summary>

- [x] **camelCase**, starting with a **letter**.

</details>

### Question 2: Spaces around `+`?

<details>
<summary>Answer</summary>

- [x] **Yes.** `let x = y + z;` not `x=y+z;`.

</details>

### Question 3: Tabs for indent?

<details>
<summary>Answer</summary>

- [x] **No.** Use **2 spaces**.

</details>

### Question 4: Semicolon after a function `}`?

<details>
<summary>Answer</summary>

- [x] **No.** Compound blocks do **not** take a trailing `;`.

</details>

### Question 5: Where do you break a long line?

<details>
<summary>Answer</summary>

- [x] After an **operator** or **comma**. Keep under **~80** chars.

</details>

### Question 6: Is `first-name` a legal JS variable?

<details>
<summary>Answer</summary>

- [x] **No.** Hyphens are **subtraction** / **SyntaxError**.

</details>

### Question 7: Does `getElementById("Demo")` find `id="demo"`?

<details>
<summary>Answer</summary>

- [x] **No.** It returns **null**. IDs are **case-sensitive**.

</details>

### Question 8: `london.jpg` vs `London.jpg` on Unix?

<details>
<summary>Answer</summary>

- [x] **Different files.** Use **lower-case** names.

</details>

### Question 9: Do extra spaces change `1+2`?

<details>
<summary>Answer</summary>

- [x] **No.** `1 + 2` is still **3**. Minify for **production size**, not correctness.

</details>

### Question 10: Need `type="text/javascript"` on `<script src>`?

<details>
<summary>Answer</summary>

- [x] **No.** The default is already JavaScript.

</details>


</details>

## Summary

Pick one style and keep it: camelCase, 2 spaces, operator spacing, K&R braces, semicolons on simple statements, short lines, matching HTML ids, lower-case filenames. Style is for readers; minify only when shipping large scripts.

## References

- [JS Style Guide (W3Schools)](https://www.w3schools.com/js/js_conventions.asp)
- [MDN: JavaScript guidelines](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide/Code_style_guide/JavaScript)
- [HTML Style Guide (W3Schools)](https://www.w3schools.com/html/html5_syntax.asp)
