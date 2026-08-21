# JS Error Object

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

JavaScript’s built-in Error object carries name and message (and, in modern engines, cause). new Error() creates one. Error.isError(x) is true only for real Error instances, not look-alike objects. The name property is one of EvalError (deprecated), RangeError, ReferenceError, SyntaxError, TypeError, or URIError. The page Tryits catch those (SyntaxError via eval so it is runtime-catchable). Skip non-standard properties such as description, stack-as-API, and evalError().

This section has **11** examples:

- [x] **Example 1:** new Error() — creates an Error object [View](#js-error-object-example-01)
- [x] **Example 2:** name — sets or returns the error name [View](#js-error-object-example-02)
- [x] **Example 3:** message — sets or returns the error message [View](#js-error-object-example-03)
- [x] **Example 4:** cause — sets or returns an error cause [View](#js-error-object-example-04)
- [x] **Example 5:** Error.isError(x) — true only for real Error objects [View](#js-error-object-example-05)
- [x] **Example 6:** EvalError — deprecated name; use SyntaxError [View](#js-error-object-example-06)
- [x] **Example 7:** RangeError — a number out of range [View](#js-error-object-example-07)
- [x] **Example 8:** ReferenceError — an illegal reference [View](#js-error-object-example-08)
- [x] **Example 9:** SyntaxError — eval of invalid source [View](#js-error-object-example-09)
- [x] **Example 10:** TypeError — wrong type for the operation [View](#js-error-object-example-10)
- [x] **Example 11:** URIError — decodeURI / encodeURI malformed [View](#js-error-object-example-11)

## Detailed Explanation

- [x] **`new Error()`** / **`new Error(message)`**. **`name`** defaults to **Error**. **`message`** defaults to **`""`**.
- [x] **`cause`** wraps an inner error: `new Error("outer", { cause: inner })`.
- [x] **`Error.isError`**: **true** for `new Error`, **false** for `{ name: "Error" }` and **null**.
- [x] **Six names:** EvalError (deprecated), RangeError, ReferenceError, SyntaxError, TypeError, URIError.
- [x] Do **not** use **`err.description`** (Microsoft only) or the other non-standard rows.

<a id="js-error-object-example-01"></a>

### **Example 1: new Error() — creates an Error object**

- [x] `new Error()` builds a built-in **Error** object.
- [x] With no message, **`message`** is **`""`**. **`name`** is **`"Error"`**.

Sandbox: `code_sandbox/js-error-object/new-error.html`

```javascript
const err = new Error();
const err2 = new Error("Something went wrong");
```

![js-error-object example 1 source](../code_sandbox/snaps/js-error-object-01-code.png)

![js-error-object example 1 result](../code_sandbox/snaps/js-error-object-01-result.png)

- [x] **Outcome:** `new Error()` → name **Error**, message **""**. `new Error("Something went wrong")` → message **Something went wrong**.

<a id="js-error-object-example-02"></a>

### **Example 2: name — sets or returns the error name**

- [x] **`name`** is the error **kind** (`Error`, `TypeError`, `RangeError`, …).
- [x] You can **read** it after `catch`, or **set** it on a custom Error.

Sandbox: `code_sandbox/js-error-object/error-name.html`

```javascript
const err = new Error("boom");
err.name;
err.name = "MyError";
```

![js-error-object example 2 source](../code_sandbox/snaps/js-error-object-02-code.png)

![js-error-object example 2 result](../code_sandbox/snaps/js-error-object-02-result.png)

- [x] **Outcome:** Default **`name`** is **"Error"**. After `err.name = "MyError"` it is **"MyError"** (message still **boom**).

<a id="js-error-object-example-03"></a>

### **Example 3: message — sets or returns the error message**

- [x] **`message`** is the human-readable description.
- [x] Pass it to **`new Error(message)`**, or assign **`err.message`** later.

Sandbox: `code_sandbox/js-error-object/error-message.html`

```javascript
const err = new Error("first");
err.message = "second";
```

![js-error-object example 3 source](../code_sandbox/snaps/js-error-object-03-code.png)

![js-error-object example 3 result](../code_sandbox/snaps/js-error-object-03-result.png)

- [x] **Outcome:** Constructor message is **"first"**. After assign, **`err.message`** is **"second"**.

<a id="js-error-object-example-04"></a>

### **Example 4: cause — sets or returns an error cause**

- [x] **`cause`** chains the **underlying** error: `new Error(msg, { cause })`.
- [x] Catch the inner error, wrap it, and still read **`err.cause`**.

Sandbox: `code_sandbox/js-error-object/error-cause.html`

```javascript
try {
  throw new TypeError("inner");
} catch (inner) {
  throw new Error("outer", { cause: inner });
}
```

![js-error-object example 4 source](../code_sandbox/snaps/js-error-object-04-code.png)

![js-error-object example 4 result](../code_sandbox/snaps/js-error-object-04-result.png)

- [x] **Outcome:** Outer **Error**: **outer**. `err.cause` is **TypeError**: **inner**.

<a id="js-error-object-example-05"></a>

### **Example 5: Error.isError(x) — true only for real Error objects**

- [x] **`Error.isError(x)`** is **true** if `x` is an Error (including TypeError, …).
- [x] A plain `{ name: "Error" }` object is **false** — it only looks like one.

Sandbox: `code_sandbox/js-error-object/error-is-error.html`

```javascript
Error.isError(new Error("x"));
Error.isError({ name: "Error", message: "x" });
```

![js-error-object example 5 source](../code_sandbox/snaps/js-error-object-05-code.png)

![js-error-object example 5 result](../code_sandbox/snaps/js-error-object-05-result.png)

- [x] **Outcome:** **Error.isError** is a **function**. `new Error("x")` → **true**. `{name:"Error", message:"x"}` → **false**.

<a id="js-error-object-example-06"></a>

### **Example 6: EvalError — deprecated name; use SyntaxError**

- [x] Six values for **`name`**: EvalError, RangeError, ReferenceError, SyntaxError, TypeError, URIError.
- [x] **EvalError is deprecated** — do not expect `eval()` to throw it.

Sandbox: `code_sandbox/js-error-object/evalerror-name.html`

```javascript
const e = new EvalError("legacy");
try {
  eval("alert('Hello)");
} catch (err) {
  // SyntaxError
}
```

![js-error-object example 6 source](../code_sandbox/snaps/js-error-object-06-code.png)

![js-error-object example 6 result](../code_sandbox/snaps/js-error-object-06-result.png)

- [x] **Outcome:** `new EvalError` has name **EvalError**. `eval("alert('Hello)")` throws **SyntaxError**: **Invalid or unexpected token**.

<a id="js-error-object-example-07"></a>

### **Example 7: RangeError — a number out of range**

- [x] **RangeError**: a number is **out of range**.
- [x] The page Tryit uses **`toPrecision(500)`**.

Sandbox: `code_sandbox/js-error-object/rangeerror-name.html`

```javascript
let num = 1;
try {
  num.toPrecision(500);
} catch (err) {
  let text = err.name + "\n" + err.message;
}
```

![js-error-object example 7 source](../code_sandbox/snaps/js-error-object-07-code.png)

![js-error-object example 7 result](../code_sandbox/snaps/js-error-object-07-result.png)

- [x] **Outcome:** **RangeError**: **toPrecision() argument must be between 1 and 100**.

<a id="js-error-object-example-08"></a>

### **Example 8: ReferenceError — an illegal reference**

- [x] **ReferenceError**: an **illegal reference** (the page Tryit link is the undeclared-variable demo).
- [x] `x = y + 1` when `y` was never declared.

Sandbox: `code_sandbox/js-error-object/referenceerror-name.html`

```javascript
let x = 5;
try {
  x = y + 1;
} catch (err) {
  let text = err.name + "\n" + err.message;
}
```

![js-error-object example 8 source](../code_sandbox/snaps/js-error-object-08-code.png)

![js-error-object example 8 result](../code_sandbox/snaps/js-error-object-08-result.png)

- [x] **Outcome:** **ReferenceError**: **y is not defined**.

<a id="js-error-object-example-09"></a>

### **Example 9: SyntaxError — eval of invalid source**

- [x] **SyntaxError**: the source is not valid JavaScript.
- [x] The page Tryit uses **`eval("alert('Hello)")`** so the error is **runtime-catchable** (eval parses later).
- [x] A raw unclosed string in a `<script>` would **not** be catchable — see JS Errors Intro.

Sandbox: `code_sandbox/js-error-object/syntaxerror-name.html`

```javascript
try {
  eval("alert('Hello)");
} catch (err) {
  let text = err.name + "\n" + err.message;
}
```

![js-error-object example 9 source](../code_sandbox/snaps/js-error-object-09-code.png)

![js-error-object example 9 result](../code_sandbox/snaps/js-error-object-09-result.png)

- [x] **Outcome:** **SyntaxError**: **Invalid or unexpected token** (caught from `eval`, not from a parse-time script).

<a id="js-error-object-example-10"></a>

### **Example 10: TypeError — wrong type for the operation**

- [x] **TypeError**: a value is the **wrong type**.
- [x] The page Tryit is **`num.toUpperCase()`** on the number **1**.

Sandbox: `code_sandbox/js-error-object/typeerror-name.html`

```javascript
let num = 1;
try {
  num.toUpperCase();
} catch (err) {
  let text = err.name + "\n" + err.message;
}
```

![js-error-object example 10 source](../code_sandbox/snaps/js-error-object-10-code.png)

![js-error-object example 10 result](../code_sandbox/snaps/js-error-object-10-result.png)

- [x] **Outcome:** **TypeError**: **num.toUpperCase is not a function**.

<a id="js-error-object-example-11"></a>

### **Example 11: URIError — decodeURI / encodeURI malformed**

- [x] **URIError**: illegal characters in a **URI** function (`decodeURI`, `encodeURI`, …).
- [x] The Tryit is **`decodeURI("%%%")`**. The table text also mentions **`encodeURI()`**.

Sandbox: `code_sandbox/js-error-object/urierror-name.html`

```javascript
try {
  decodeURI("%%%");
} catch (err) {
  let text = err.name + "\n" + err.message;
}
```

![js-error-object example 11 source](../code_sandbox/snaps/js-error-object-11-code.png)

![js-error-object example 11 result](../code_sandbox/snaps/js-error-object-11-result.png)

- [x] **Outcome:** **URIError**: **URI malformed** for `decodeURI("%%%")`. `encodeURI` of an unpaired surrogate is also **URIError**: **URI malformed**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-error-object/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `new Error()` with no argument?

<details>
<summary>Answer</summary>

- [x] **name** **Error**, **message** **`""`**.

</details>

### Question 2: What is `new Error("Something went wrong").message`?

<details>
<summary>Answer</summary>

- [x] **Something went wrong**.

</details>

### Question 3: Can you assign `err.name = "MyError"`?

<details>
<summary>Answer</summary>

- [x] **Yes.** name becomes **MyError**; message stays **boom** in the demo.

</details>

### Question 4: What is `cause` in `new Error("outer", { cause: new TypeError("inner") })`?

<details>
<summary>Answer</summary>

- [x] **err.cause.name** is **TypeError**. **err.cause.message** is **inner**.

</details>

### Question 5: Is `{ name: "Error", message: "x" }` an Error?

<details>
<summary>Answer</summary>

- [x] **No.** `Error.isError(plain)` is **false**. `Error.isError(new Error("x"))` is **true**.
- [x] `Error.isError(null)` is **false**.

</details>

### Question 6: Does `eval("alert('Hello)")` throw EvalError?

<details>
<summary>Answer</summary>

- [x] **No.** **SyntaxError**: **Invalid or unexpected token**.
- [x] `new EvalError("legacy").name` is still **EvalError**.

</details>

### Question 7: What is `num.toPrecision(500)`?

<details>
<summary>Answer</summary>

- [x] **RangeError**: **toPrecision() argument must be between 1 and 100**.

</details>

### Question 8: What is `x = y + 1` with no `y`?

<details>
<summary>Answer</summary>

- [x] **ReferenceError**: **y is not defined**.

</details>

### Question 9: Why can the SyntaxError Tryit use try/catch?

<details>
<summary>Answer</summary>

- [x] It uses **`eval(...)`**, which parses **at runtime**.
- [x] A raw `let x = Math.round(4.6;)` in a script is **not** catchable.

</details>

### Question 10: What is `(1).toUpperCase()`?

<details>
<summary>Answer</summary>

- [x] **TypeError**: **num.toUpperCase is not a function**.

</details>

### Question 11: What is `decodeURI("%%%")`?

<details>
<summary>Answer</summary>

- [x] **URIError**: **URI malformed**.
- [x] `encodeURI` of an unpaired surrogate is the same **URIError**: **URI malformed**.

</details>

### Question 12: Should you use `err.description`?

<details>
<summary>Answer</summary>

- [x] **No.** Microsoft-only / non-standard. Use **`err.message`**.

</details>


</details>

## Summary

Create errors with new Error, read name and message, and chain with cause. Error.isError distinguishes real errors from plain objects. The six name values match the intro types; EvalError is only a constructor now. Catch eval SyntaxErrors at runtime; parse-time SyntaxErrors still need new Function if you want a demo page.

## References

- [JS Error Object (W3Schools)](https://www.w3schools.com/js/js_error_object.asp)
- [MDN: Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
- [MDN: Error.isError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/isError)
- [MDN: Error.cause](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause)
