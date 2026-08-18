<details>
  <summary>Debug Errors</summary>

## Introduction

Error messages look scary; they are clues. Read the type, the short text, and the line number. ReferenceError is a missing name, TypeError is an illegal operation (often undefined/null), SyntaxError is broken source, and NaN is invalid math that usually does not throw. Fix the first error; it often causes the rest.

This section has **8** examples:

- [x] **Example 1:** An error message has type, text, and a line number [View](#js-debugging-errors-example-01)
- [x] **Example 2:** ReferenceError — a name does not exist [View](#js-debugging-errors-example-02)
- [x] **Example 3:** TypeError — invalid use of a value [View](#js-debugging-errors-example-03)
- [x] **Example 4:** SyntaxError — missing ) in if (x == 5 { [View](#js-debugging-errors-example-04)
- [x] **Example 5:** NaN — "abc" * 5 is not a number [View](#js-debugging-errors-example-05)
- [x] **Example 6:** Cannot read property of undefined — user.name [View](#js-debugging-errors-example-06)
- [x] **Example 7:** Cheat sheet: ReferenceError, TypeError, SyntaxError, NaN [View](#js-debugging-errors-example-07)
- [x] **Example 8:** Fix the first error before moving on [View](#js-debugging-errors-example-08)

## Detailed Explanation

- [x] Parts: **type**, **message**, **line**.
- [x] **ReferenceError** — name missing. **TypeError** — bad use (`.length` on `undefined`, `.name` on missing object).
- [x] **SyntaxError** — will not parse (`if (x == 5 {`). **NaN** — `"abc" * 5`.
- [x] Fix the **first** console error, then re-run.

<a id="js-debugging-errors-example-01"></a>

### **Example 1: An error message has type, text, and a line number**

- [x] Read **three** parts: the **error type**, a **short explanation**, and a **line number**.
- [x] Click the line number in the console to jump to the code.

Sandbox: `code_sandbox/js-debugging-errors/read-error-parts.html`

```javascript
let x = 1;
try {
  x = missing + 1;
} catch (e) {
  console.log(e.name);
  console.log(e.message);
}
```

<img alt="js-debugging-errors example 1 source" src="./code_sandbox/snaps/js-debugging-errors-01-code.png" />

<img alt="js-debugging-errors example 1 result" src="./code_sandbox/snaps/js-debugging-errors-01-result.png" />

- [x] **Outcome:** **name:** ReferenceError. **message:** **missing is not defined**. Those two lines are the type + explanation.

<a id="js-debugging-errors-example-02"></a>

### **Example 2: ReferenceError — a name does not exist**

- [x] Often a **typo** or a missing **`let` / `const`**.
- [x] JavaScript cannot find **`myValue`**.

Sandbox: `code_sandbox/js-debugging-errors/referenceerror.html`

```javascript
console.log(myValue);
```

<img alt="js-debugging-errors example 2 source" src="./code_sandbox/snaps/js-debugging-errors-02-code.png" />

<img alt="js-debugging-errors example 2 result" src="./code_sandbox/snaps/js-debugging-errors-02-result.png" />

- [x] **Outcome:** **ReferenceError: myValue is not defined**.

<a id="js-debugging-errors-example-03"></a>

### **Example 3: TypeError — invalid use of a value**

- [x] Usually **`undefined`** or **`null`**.
- [x] `let x;` exists, but has **no value**. You cannot read **`.length`** from `undefined`.
- [x] **Log the value before using it.**

Sandbox: `code_sandbox/js-debugging-errors/typeerror.html`

```javascript
let x;
console.log(x.length);
```

<img alt="js-debugging-errors example 3 source" src="./code_sandbox/snaps/js-debugging-errors-03-code.png" />

<img alt="js-debugging-errors example 3 result" src="./code_sandbox/snaps/js-debugging-errors-03-result.png" />

- [x] **Outcome:** **TypeError: Cannot read properties of undefined (reading 'length')**.

<a id="js-debugging-errors-example-04"></a>

### **Example 4: SyntaxError — missing ) in if (x == 5 {**

- [x] JavaScript **cannot parse** the file. Missing **brackets or parentheses** are typical.
- [x] `if (x == 5 {` is missing **`)`**. The **whole script** fails — `try/catch` in the same file cannot help.
- [x] This sandbox compiles with **`new Function`** so the page can still render.

Sandbox: `code_sandbox/js-debugging-errors/syntaxerror.html`

```javascript
if (x == 5 {
  console.log("Hello");
}
```

<img alt="js-debugging-errors example 4 source" src="./code_sandbox/snaps/js-debugging-errors-04-code.png" />

<img alt="js-debugging-errors example 4 result" src="./code_sandbox/snaps/js-debugging-errors-04-result.png" />

- [x] **Outcome:** **SyntaxError** (missing `)` after argument list / unexpected `{`). A raw `<script>` would not load.

<a id="js-debugging-errors-example-05"></a>

### **Example 5: NaN — "abc" * 5 is not a number**

- [x] **NaN** means **Not a Number**. Invalid math often **does not throw**.
- [x] `"abc" * 5` is **NaN**. Check both sides are numbers **before** multiplying.

Sandbox: `code_sandbox/js-debugging-errors/nan-errors.html`

```javascript
let result = "abc" * 5;
console.log(result);
```

<img alt="js-debugging-errors example 5 source" src="./code_sandbox/snaps/js-debugging-errors-05-code.png" />

<img alt="js-debugging-errors example 5 result" src="./code_sandbox/snaps/js-debugging-errors-05-result.png" />

- [x] **Outcome:** **log: NaN**. `Number.isNaN(result)` is **true**. No exception.

<a id="js-debugging-errors-example-06"></a>

### **Example 6: Cannot read property of undefined — user.name**

- [x] One of the most common beginner errors: using **something that is not there**.
- [x] `let user;` — the variable exists, the **object does not**. `user.name` is a TypeError.

Sandbox: `code_sandbox/js-debugging-errors/cannot-read-property.html`

```javascript
let user;
console.log(user.name);
```

<img alt="js-debugging-errors example 6 source" src="./code_sandbox/snaps/js-debugging-errors-06-code.png" />

<img alt="js-debugging-errors example 6 result" src="./code_sandbox/snaps/js-debugging-errors-06-result.png" />

- [x] **Outcome:** **TypeError: Cannot read properties of undefined (reading 'name')**.

<a id="js-debugging-errors-example-07"></a>

### **Example 7: Cheat sheet: ReferenceError, TypeError, SyntaxError, NaN**

- [x] **ReferenceError** — a **name** is not defined.
- [x] **TypeError** — a **value** is used incorrectly.
- [x] **SyntaxError** — **broken structure** (the script does not parse).
- [x] **NaN** — **invalid math** (often silent).

Sandbox: `code_sandbox/js-debugging-errors/error-meanings.html`

```javascript
console.log("see outcomes");
```

<img alt="js-debugging-errors example 7 source" src="./code_sandbox/snaps/js-debugging-errors-07-code.png" />

<img alt="js-debugging-errors example 7 result" src="./code_sandbox/snaps/js-debugging-errors-07-result.png" />

- [x] **Outcome:** Four labels, four different failures — do not treat them as the same bug.

<a id="js-debugging-errors-example-08"></a>

### **Example 8: Fix the first error before moving on**

- [x] Do **not** ignore errors. **One** error often causes **many** later ones.
- [x] Fix the **first** message in the console, reload, then look again.

Sandbox: `code_sandbox/js-debugging-errors/fix-first-error.html`

```javascript
function first() { missingFn(); }
function second() { console.log("never"); }
try { first(); second(); } catch (e) { console.log("stopped at", e.message); }
```

<img alt="js-debugging-errors example 8 source" src="./code_sandbox/snaps/js-debugging-errors-08-code.png" />

<img alt="js-debugging-errors example 8 result" src="./code_sandbox/snaps/js-debugging-errors-08-result.png" />

- [x] **Outcome:** **stopped at missingFn is not defined**. **never** is **not** logged — `second()` did not run.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-debugging-errors/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What three parts does an error message have?

<details>
<summary>Answer</summary>

- [x] **Type**, **explanation**, **line number**.

</details>

### Question 2: What is `console.log(myValue)`?

<details>
<summary>Answer</summary>

- [x] **ReferenceError: myValue is not defined**.

</details>

### Question 3: What is `let x; x.length`?

<details>
<summary>Answer</summary>

- [x] **TypeError: Cannot read properties of undefined (reading 'length')**.

</details>

### Question 4: What is `if (x == 5 {`?

<details>
<summary>Answer</summary>

- [x] **SyntaxError**. The script does not parse.

</details>

### Question 5: What is `"abc" * 5`?

<details>
<summary>Answer</summary>

- [x] **NaN**. It does **not** throw.

</details>

### Question 6: What is `let user; user.name`?

<details>
<summary>Answer</summary>

- [x] **TypeError: Cannot read properties of undefined (reading 'name')**.

</details>

### Question 7: Does SyntaxError get caught by try/catch in the same file?

<details>
<summary>Answer</summary>

- [x] **No.** Parsing fails **before** runtime.

</details>

### Question 8: Why fix the first error first?

<details>
<summary>Answer</summary>

- [x] One failure **stops later lines** (or causes a cascade).

</details>


</details>

## Summary

Read type + message + line. ReferenceError vs TypeError vs SyntaxError vs silent NaN. Click the line number. Fix the first error, then look again.

## References

- [JS Debugging Errors (W3Schools)](https://www.w3schools.com/js/js_debugging_errors.asp)
- [MDN: SyntaxError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
- [MDN: NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)

</details>
