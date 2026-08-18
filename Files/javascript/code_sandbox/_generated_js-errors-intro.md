<details>
  <summary>JS Errors Intro</summary>

## Introduction

When JavaScript runs, errors happen: programmer mistakes, bad input, and surprises. This page names the built-in kinds — ReferenceError, TypeError, RangeError, URIError, SyntaxError, and the deprecated EvalError — and introduces try/catch. Runtime errors can be caught. Syntax errors are thrown while the engine is still parsing, so a raw script never starts and try/catch on the same page cannot help. This sandbox uses new Function only so those parse errors can be shown without blanking the page.

This section has **12** examples:

- [x] **Example 1:** try — catch is skipped when nothing throws [View](#js-errors-intro-example-01)
- [x] **Example 2:** catch — runs when the try block throws [View](#js-errors-intro-example-02)
- [x] **Example 3:** ReferenceError — y is not defined [View](#js-errors-intro-example-03)
- [x] **Example 4:** ReferenceError — Cannot access y before initialization [View](#js-errors-intro-example-04)
- [x] **Example 5:** TypeError — anna is not a function [View](#js-errors-intro-example-05)
- [x] **Example 6:** TypeError — num.toUpperCase is not a function [View](#js-errors-intro-example-06)
- [x] **Example 7:** RangeError — Invalid array length [View](#js-errors-intro-example-07)
- [x] **Example 8:** RangeError — toPrecision() argument must be between 1 and 100 [View](#js-errors-intro-example-08)
- [x] **Example 9:** URIError — decodeURI('%%%') URI malformed [View](#js-errors-intro-example-09)
- [x] **Example 10:** SyntaxError — unclosed string (not catchable in a raw script) [View](#js-errors-intro-example-10)
- [x] **Example 11:** SyntaxError — try/catch cannot catch Math.round(4.6;) [View](#js-errors-intro-example-11)
- [x] **Example 12:** EvalError — deprecated; eval throws SyntaxError instead [View](#js-errors-intro-example-12)

## Detailed Explanation

- [x] **`try` / `catch`** come in pairs. `try` tests a block; `catch` runs only if that block throws.
- [x] **ReferenceError** — missing name, or **TDZ** (`Cannot access 'y' before initialization`).
- [x] **TypeError** — wrong type (`anna is not a function`, `num.toUpperCase is not a function`).
- [x] **RangeError** — out of range (`Invalid array length`, `toPrecision() argument must be between 1 and 100`).
- [x] **URIError** — `decodeURI("%%%")` → **URI malformed**.
- [x] **SyntaxError** is **not catchable** in the same `<script>`. Use **`new Function`** here to display it. `eval` of bad source **is** catchable (Error Object page).
- [x] **EvalError** is **deprecated**. `eval("var = 1")` throws **SyntaxError**, not EvalError.

<a id="js-errors-intro-example-01"></a>

### **Example 1: try — catch is skipped when nothing throws**

- [x] The **`try`** block is the code you want to test for errors.
- [x] If the block finishes **without** throwing, **`catch` is skipped**.

Sandbox: `code_sandbox/js-errors-intro/try-block-no-error.html`

```javascript
let status = "start";
try {
  status = "try ran";
} catch (err) {
  status = "catch ran: " + err;
}
```

<img alt="js-errors-intro example 1 source" src="./code_sandbox/snaps/js-errors-intro-01-code.png" />

<img alt="js-errors-intro example 1 result" src="./code_sandbox/snaps/js-errors-intro-01-result.png" />

- [x] **Outcome:** status is **"try ran"**. The catch block did **not** run.

<a id="js-errors-intro-example-02"></a>

### **Example 2: catch — runs when the try block throws**

- [x] **`catch`** runs only if **`try`** throws.
- [x] The parameter (`err`) is the thrown value. Built-in errors have **`name`** and **`message`**.

Sandbox: `code_sandbox/js-errors-intro/catch-block-runs.html`

```javascript
try {
  null.foo;
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 2 source" src="./code_sandbox/snaps/js-errors-intro-02-code.png" />

<img alt="js-errors-intro example 2 result" src="./code_sandbox/snaps/js-errors-intro-02-result.png" />

- [x] **Outcome:** **TypeError**: Cannot read properties of **null** (reading **'foo'**). Catch ran.

<a id="js-errors-intro-example-03"></a>

### **Example 3: ReferenceError — y is not defined**

- [x] A **`ReferenceError`** occurs if you use a variable that **does not exist**.
- [x] The W3Schools table also lists `fname = foo` → **foo is not defined**. Same error name.

Sandbox: `code_sandbox/js-errors-intro/referenceerror-undeclared.html`

```javascript
let x = 5;
try {
  x = y + 1;
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 3 source" src="./code_sandbox/snaps/js-errors-intro-03-code.png" />

<img alt="js-errors-intro example 3 result" src="./code_sandbox/snaps/js-errors-intro-03-result.png" />

- [x] **Outcome:** **ReferenceError**: **y is not defined**.

<a id="js-errors-intro-example-04"></a>

### **Example 4: ReferenceError — Cannot access y before initialization**

- [x] `let x = y` then `let y = 5` is **not** “y does not exist.”
- [x] `let y` is in the **temporal dead zone** — **ReferenceError** before initialization.

Sandbox: `code_sandbox/js-errors-intro/referenceerror-tdz.html`

```javascript
try {
  let x = y;
  let y = 5;
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 4 source" src="./code_sandbox/snaps/js-errors-intro-04-code.png" />

<img alt="js-errors-intro example 4 result" src="./code_sandbox/snaps/js-errors-intro-04-result.png" />

- [x] **Outcome:** **ReferenceError**: **Cannot access 'y' before initialization**.

<a id="js-errors-intro-example-05"></a>

### **Example 5: TypeError — anna is not a function**

- [x] A **`TypeError`** occurs when a value is the **wrong type** for the operation.
- [x] `anna` is the number **5**, so `anna(5)` is not a call.

Sandbox: `code_sandbox/js-errors-intro/typeerror-not-a-function.html`

```javascript
let anna = 5;
try {
  anna(5);
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 5 source" src="./code_sandbox/snaps/js-errors-intro-05-code.png" />

<img alt="js-errors-intro example 5 result" src="./code_sandbox/snaps/js-errors-intro-05-result.png" />

- [x] **Outcome:** **TypeError**: **anna is not a function**.

<a id="js-errors-intro-example-06"></a>

### **Example 6: TypeError — num.toUpperCase is not a function**

- [x] Numbers do not have **`toUpperCase`** (that is a **string** method).
- [x] Calling it is a **TypeError**, not a silent no-op.

Sandbox: `code_sandbox/js-errors-intro/typeerror-touppercase.html`

```javascript
let num = 1;
try {
  num.toUpperCase();
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 6 source" src="./code_sandbox/snaps/js-errors-intro-06-code.png" />

<img alt="js-errors-intro example 6 result" src="./code_sandbox/snaps/js-errors-intro-06-result.png" />

- [x] **Outcome:** **TypeError**: **num.toUpperCase is not a function**.

<a id="js-errors-intro-example-07"></a>

### **Example 7: RangeError — Invalid array length**

- [x] A **`RangeError`** occurs when a value is **out of its valid range**.
- [x] `new Array(-1)` is not a legal length.

Sandbox: `code_sandbox/js-errors-intro/rangeerror-array-length.html`

```javascript
try {
  new Array(-1);
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 7 source" src="./code_sandbox/snaps/js-errors-intro-07-code.png" />

<img alt="js-errors-intro example 7 result" src="./code_sandbox/snaps/js-errors-intro-07-result.png" />

- [x] **Outcome:** **RangeError**: **Invalid array length**.

<a id="js-errors-intro-example-08"></a>

### **Example 8: RangeError — toPrecision() argument must be between 1 and 100**

- [x] `Number.prototype.toPrecision(precision)` only allows **1–100** significant digits.
- [x] **500** is out of range.

Sandbox: `code_sandbox/js-errors-intro/rangeerror-toprecision.html`

```javascript
let num = 1;
try {
  num.toPrecision(500);  // A number cannot have 500 significant digits
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 8 source" src="./code_sandbox/snaps/js-errors-intro-08-code.png" />

<img alt="js-errors-intro example 8 result" src="./code_sandbox/snaps/js-errors-intro-08-result.png" />

- [x] **Outcome:** **RangeError**: **toPrecision() argument must be between 1 and 100**.

<a id="js-errors-intro-example-09"></a>

### **Example 9: URIError — decodeURI('%%%') URI malformed**

- [x] A **`URIError`** occurs if you pass **illegal characters** to a URI function.
- [x] `decodeURI("%%%")` is not a valid percent-encoding.

Sandbox: `code_sandbox/js-errors-intro/urierror-decodeuri.html`

```javascript
try {
  decodeURI("%%%");  // You cannot URI decode percent signs
} catch (err) {
  document.getElementById("demo").innerHTML = err.name;
}
```

<img alt="js-errors-intro example 9 source" src="./code_sandbox/snaps/js-errors-intro-09-code.png" />

<img alt="js-errors-intro example 9 result" src="./code_sandbox/snaps/js-errors-intro-09-result.png" />

- [x] **Outcome:** **URIError**: **URI malformed**.

<a id="js-errors-intro-example-10"></a>

### **Example 10: SyntaxError — unclosed string (not catchable in a raw script)**

- [x] A **`SyntaxError`** means the source **violates JavaScript grammar**.
- [x] The engine throws it **before runtime**. A raw `<script>` **does not load**.
- [x] This sandbox compiles the snippet with **`new Function`** so the page can still render.

Sandbox: `code_sandbox/js-errors-intro/syntaxerror-unclosed-string.html`

```javascript
// This line cannot be parsed by JavaScript
let text = "John Doe);
// This line will not be executed
```

<img alt="js-errors-intro example 10 source" src="./code_sandbox/snaps/js-errors-intro-10-code.png" />

<img alt="js-errors-intro example 10 result" src="./code_sandbox/snaps/js-errors-intro-10-result.png" />

- [x] **Outcome:** **SyntaxError**: **Invalid or unexpected token** (via `new Function`). A raw script would stop the page.

<a id="js-errors-intro-example-11"></a>

### **Example 11: SyntaxError — try/catch cannot catch Math.round(4.6;)**

- [x] `Math.round(4.6;)` has an extra **`;`** inside the parentheses — **missing ) after argument list**.
- [x] **`try...catch` does not help**: the **whole script** fails to parse, so `try` never starts.
- [x] `err.description` on the W3Schools page is **IE-only**. This engine uses **`err.message`**.

Sandbox: `code_sandbox/js-errors-intro/syntaxerror-not-catchable.html`

```javascript
try {
  let x = Math.round(4.6;)
} catch (err) {
  let text = err.name + " " + err.description;
}
```

<img alt="js-errors-intro example 11 source" src="./code_sandbox/snaps/js-errors-intro-11-code.png" />

<img alt="js-errors-intro example 11 result" src="./code_sandbox/snaps/js-errors-intro-11-result.png" />

- [x] **Outcome:** **SyntaxError**: **missing ) after argument list**. Inner `catch` never ran — the snippet did not parse.

<a id="js-errors-intro-example-12"></a>

### **Example 12: EvalError — deprecated; eval throws SyntaxError instead**

- [x] The page lists **EvalError** (deprecated). Newer engines **do not throw EvalError** from `eval()`.
- [x] `new EvalError(...)` still constructs an object whose **`name`** is **EvalError**.
- [x] Bad `eval` source is a **SyntaxError** (use that).

Sandbox: `code_sandbox/js-errors-intro/evalerror-deprecated.html`

```javascript
const made = new EvalError("still constructable");
try {
  eval("var = 1");
} catch (err) {
  // SyntaxError, not EvalError
}
```

<img alt="js-errors-intro example 12 source" src="./code_sandbox/snaps/js-errors-intro-12-code.png" />

<img alt="js-errors-intro example 12 result" src="./code_sandbox/snaps/js-errors-intro-12-result.png" />

- [x] **Outcome:** `new EvalError` has name **EvalError**. `eval("var = 1")` throws **SyntaxError**: **Unexpected token '='** — not EvalError.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-errors-intro/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `try` do if nothing throws?

<details>
<summary>Answer</summary>

- [x] The **try** block finishes. **`catch` is skipped**.
- [x] The demo status is **try ran**.

</details>

### Question 2: What is `null.foo`?

<details>
<summary>Answer</summary>

- [x] **TypeError**: **Cannot read properties of null (reading 'foo')**.
- [x] That is the dedicated **catch** demo (not the later TypeError Tryits).

</details>

### Question 3: What is `x = y + 1` when `y` was never declared?

<details>
<summary>Answer</summary>

- [x] **ReferenceError**: **y is not defined**.

</details>

### Question 4: What is `let x = y; let y = 5`?

<details>
<summary>Answer</summary>

- [x] **ReferenceError**: **Cannot access 'y' before initialization** (TDZ).
- [x] It is **not** “y is not defined.”

</details>

### Question 5: What is `anna(5)` if `anna` is `5`?

<details>
<summary>Answer</summary>

- [x] **TypeError**: **anna is not a function**.

</details>

### Question 6: What is `(1).toUpperCase()`?

<details>
<summary>Answer</summary>

- [x] **TypeError**: **num.toUpperCase is not a function**.

</details>

### Question 7: What is `new Array(-1)`?

<details>
<summary>Answer</summary>

- [x] **RangeError**: **Invalid array length**.

</details>

### Question 8: What is `(1).toPrecision(500)`?

<details>
<summary>Answer</summary>

- [x] **RangeError**: **toPrecision() argument must be between 1 and 100**.

</details>

### Question 9: What is `decodeURI("%%%")`?

<details>
<summary>Answer</summary>

- [x] **URIError**: **URI malformed**.

</details>

### Question 10: What is `let text = "John Doe);`?

<details>
<summary>Answer</summary>

- [x] **SyntaxError**: **Invalid or unexpected token**.
- [x] A raw script **does not parse**. This sandbox uses **`new Function`**.

</details>

### Question 11: Can `try { Math.round(4.6;) }` catch the extra semicolon?

<details>
<summary>Answer</summary>

- [x] **No.** The **whole script** is a SyntaxError: **missing ) after argument list**.
- [x] `try` never starts. `err.description` is **IE-only**; this engine has **`err.message`**.

</details>

### Question 12: Does `eval("var = 1")` throw EvalError?

<details>
<summary>Answer</summary>

- [x] **No.** **SyntaxError**: **Unexpected token '='**.
- [x] `new EvalError` still exists; **`eval()` does not throw it** in this engine.

</details>


</details>

## Summary

Catch runtime errors with try/catch. Read err.name and err.message. Syntax errors happen before the script runs — wrap demos in new Function if you need to display them. EvalError is a leftover name; bad eval source is SyntaxError.

## References

- [JS Errors Intro (W3Schools)](https://www.w3schools.com/js/js_errors_intro.asp)
- [MDN: Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
- [MDN: try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
- [MDN: SyntaxError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

</details>
