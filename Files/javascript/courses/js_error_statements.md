# JS Error Statements

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

try tests a block, catch handles a throw, and finally always runs afterward. JavaScript normally stops and creates an Error with name and message; throw lets you raise a string, number, boolean, or object instead. The input-validation Tryit throws custom phrases (empty, not a number, too low, too high). HTML min/max on an input can reject values without any JavaScript throw. The finally Tryit clears the field even when the number was valid.

This section has **8** examples:

- [x] **Example 1:** try block — code that might throw [View](#js-error-statements-example-01)
- [x] **Example 2:** catch block — handles the thrown value [View](#js-error-statements-example-02)
- [x] **Example 3:** finally — always runs, error or not [View](#js-error-statements-example-03)
- [x] **Example 4:** throw "Too big" — throw a text [View](#js-error-statements-example-04)
- [x] **Example 5:** throw 500 — throw a number [View](#js-error-statements-example-05)
- [x] **Example 6:** Input validation — throw empty / not a number / too low / too high [View](#js-error-statements-example-06)
- [x] **Example 7:** HTML validation — input type=number min=5 max=10 [View](#js-error-statements-example-07)
- [x] **Example 8:** finally example — always clears the input [View](#js-error-statements-example-08)

## Detailed Explanation

- [x] **`try`** — code that might throw. **`catch`** — only if it did. **`finally`** — **always** (cleanup).
- [x] **`throw`** a String / Number / Boolean / Object. Thrown primitives are **not** Error objects (`name` is missing).
- [x] Built-in throws **do** create `{ name, message }`.
- [x] Validation Tryit messages: **Input is empty**, **not a number**, **too low**, **too high**. Valid **7** leaves the message **blank**.
- [x] Finally Tryit: **Input is empty / is not a number / is too high / is too low**, then the **field is cleared**.
- [x] HTML `type="number" min="5" max="10"` uses **`checkValidity()`**, not `throw`.

<a id="js-error-statements-example-01"></a>

### **Example 1: try block — code that might throw**

- [x] The **`try`** block contains code that **might** throw.
- [x] If nothing throws, **`catch` is skipped**.

Sandbox: `code_sandbox/js-error-statements/try-syntax.html`

```javascript
try {
  // Code that may cause an error
  let x = 1 + 1;
} catch (error) {
  // Code to handle the error
}
```

![js-error-statements example 1 source](../code_sandbox/snaps/js-error-statements-01-code.png)

![js-error-statements example 1 result](../code_sandbox/snaps/js-error-statements-01-result.png)

- [x] **Outcome:** `1 + 1` is **2**. Catch did **not** run.

<a id="js-error-statements-example-02"></a>

### **Example 2: catch block — handles the thrown value**

- [x] **`catch`** runs **only** if `try` throws.
- [x] For built-in errors the parameter is an **Error** object (`name`, `message`).

Sandbox: `code_sandbox/js-error-statements/catch-syntax.html`

```javascript
try {
  // Code that may cause an error
  missing();
} catch (error) {
  // Code to handle the error
}
```

![js-error-statements example 2 source](../code_sandbox/snaps/js-error-statements-02-code.png)

![js-error-statements example 2 result](../code_sandbox/snaps/js-error-statements-02-result.png)

- [x] **Outcome:** **ReferenceError**: **missing is not defined**. Catch ran.

<a id="js-error-statements-example-03"></a>

### **Example 3: finally — always runs, error or not**

- [x] **`finally`** runs after `try` / `catch` **whether or not** an error occurred.
- [x] Use it for **cleanup** (clear a field, hide a loader).

Sandbox: `code_sandbox/js-error-statements/finally-syntax.html`

```javascript
try {
  // Code that may cause an error
} catch (error) {
  // Code to handle the error
} finally {
  // Code that always runs, no matter what
}
```

![js-error-statements example 3 source](../code_sandbox/snaps/js-error-statements-03-code.png)

![js-error-statements example 3 result](../code_sandbox/snaps/js-error-statements-03-result.png)

- [x] **Outcome:** Success path: finally **yes**, catch **no**. Error path: catch **yes**, finally **yes**.

<a id="js-error-statements-example-04"></a>

### **Example 4: throw "Too big" — throw a text**

- [x] **`throw`** creates a **custom** exception. It can be a **String**, **Number**, **Boolean**, or **Object**.
- [x] A thrown string is **not** an Error object — `err.name` is **undefined**; `String(err)` is the text.

Sandbox: `code_sandbox/js-error-statements/throw-string.html`

```javascript
throw "Too big";  // throw a text
```

![js-error-statements example 4 source](../code_sandbox/snaps/js-error-statements-04-code.png)

![js-error-statements example 4 result](../code_sandbox/snaps/js-error-statements-04-result.png)

- [x] **Outcome:** Catch receives the string **"Too big"**. `err.name` is not an Error name (`(not an Error object)`).

<a id="js-error-statements-example-05"></a>

### **Example 5: throw 500 — throw a number**

- [x] You can **`throw` a number**. Same rule: it is **not** `{name, message}`.
- [x] `String(err)` is **`"500"`**.

Sandbox: `code_sandbox/js-error-statements/throw-number.html`

```javascript
throw 500;  // throw a number
```

![js-error-statements example 5 source](../code_sandbox/snaps/js-error-statements-05-code.png)

![js-error-statements example 5 result](../code_sandbox/snaps/js-error-statements-05-result.png)

- [x] **Outcome:** Catch receives **500**. `String(err)` is **500** — not `Error: 500`.

<a id="js-error-statements-example-06"></a>

### **Example 6: Input validation — throw empty / not a number / too low / too high**

- [x] Together, **`throw` + `try` + `catch`** control flow and show a **custom** message.
- [x] This sandbox runs the Tryit function against several values (no clicking required).

Sandbox: `code_sandbox/js-error-statements/input-validation-throw.html`

```javascript
function myFunction(x) {
  const message = { innerHTML: "" };
  try {
    if (x.trim() == "") throw "empty";
    if (isNaN(x)) throw "not a number";
    x = Number(x);
    if (x < 5) throw "too low";
    if (x > 10) throw "too high";
  } catch (err) {
    message.innerHTML = "Input is " + err;
  }
  return message.innerHTML;
}
```

![js-error-statements example 6 source](../code_sandbox/snaps/js-error-statements-06-code.png)

![js-error-statements example 6 result](../code_sandbox/snaps/js-error-statements-06-result.png)

- [x] **Outcome:** `""` → **Input is empty**. `"hello"` → **Input is not a number**. `"3"` → **Input is too low**. `"12"` → **Input is too high**. `"7"` → blank (valid; catch skipped).

<a id="js-error-statements-example-07"></a>

### **Example 7: HTML validation — input type=number min=5 max=10**

- [x] Modern browsers can validate with **HTML attributes** (`type`, `min`, `max`, `step`) instead of `throw`.
- [x] `checkValidity()` is **true/false** — it does **not** throw a JavaScript Error.

Sandbox: `code_sandbox/js-error-statements/html-validation.html`

```javascript
<input id="demo" type="number" min="5" max="10" step="1">
```

![js-error-statements example 7 source](../code_sandbox/snaps/js-error-statements-07-code.png)

![js-error-statements example 7 result](../code_sandbox/snaps/js-error-statements-07-result.png)

- [x] **Outcome:** `3` is **invalid** (`rangeUnderflow`). `7` is **valid**. `11` is **invalid** (`rangeOverflow`). No JS **throw**.

<a id="js-error-statements-example-08"></a>

### **Example 8: finally example — always clears the input**

- [x] After `try` / `catch`, **`finally`** still runs.
- [x] The Tryit **clears** the input field in `finally`, including on a **valid** value.

Sandbox: `code_sandbox/js-error-statements/finally-clears-input.html`

```javascript
function myFunction() {
  const message = document.getElementById("p01");
  message.innerHTML = "";
  let x = document.getElementById("demo").value;
  try {
    if (x.trim() == "") throw "is empty";
    if (isNaN(x)) throw "is not a number";
    x = Number(x);
    if (x > 10) throw "is too high";
    if (x < 5) throw "is too low";
  } catch (err) {
    message.innerHTML = "Input " + err;
  } finally {
    document.getElementById("demo").value = "";
  }
}
```

![js-error-statements example 8 source](../code_sandbox/snaps/js-error-statements-08-code.png)

![js-error-statements example 8 result](../code_sandbox/snaps/js-error-statements-08-result.png)

- [x] **Outcome:** `"3"` → **Input is too low** and field **cleared**. `"7"` → no error message, field **still cleared**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-error-statements/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does catch run after `try { 1 + 1 }`?

<details>
<summary>Answer</summary>

- [x] **No.** x is **2**. catch ran → **false**.

</details>

### Question 2: What is `missing()`?

<details>
<summary>Answer</summary>

- [x] **ReferenceError**: **missing is not defined**.

</details>

### Question 3: Does `finally` run when try succeeds?

<details>
<summary>Answer</summary>

- [x] **Yes.** Order: **try | finally**.

</details>

### Question 4: Does `finally` run when try throws?

<details>
<summary>Answer</summary>

- [x] **Yes.** Order: **try, catch:ReferenceError | finally**.

</details>

### Question 5: What is `throw "Too big"` in catch?

<details>
<summary>Answer</summary>

- [x] The string **Too big**. It is **not** an Error object.

</details>

### Question 6: What is `throw 500` in catch?

<details>
<summary>Answer</summary>

- [x] The number **500**. `String(err)` is **500**.

</details>

### Question 7: What does the validation Tryit print for `""`, `"hello"`, `"3"`, `"12"`, `"7"`?

<details>
<summary>Answer</summary>

- [x] **Input is empty**.
- [x] **Input is not a number**.
- [x] **Input is too low**.
- [x] **Input is too high**.
- [x] **blank** (valid).

</details>

### Question 8: Does HTML `min`/`max` throw a JS Error?

<details>
<summary>Answer</summary>

- [x] **No.** `checkValidity()` is **false** for **3** (`rangeUnderflow`) and **11** (`rangeOverflow`), **true** for **7**.

</details>

### Question 9: Does `finally` clear the input on a valid `7`?

<details>
<summary>Answer</summary>

- [x] **Yes.** Message stays **blank**; **fieldAfter** is **`""`**.

</details>

### Question 10: What is the finally message for `"3"`?

<details>
<summary>Answer</summary>

- [x] **Input is too low** (Tryit text is `"Input " + err`).

</details>

### Question 11: Can you `throw` a Boolean?

<details>
<summary>Answer</summary>

- [x] **Yes.** The page lists String, Number, Boolean, or Object. This section demos **string** and **number** as in the syntax lines.

</details>


</details>

## Summary

Use try to protect code, catch to handle a throw, and finally to clean up. throw can be any value; only Error objects have name and message. The validation Tryits map empty / NaN / range into custom strings. HTML constraint validation is a separate, non-throwing path.

## References

- [JS Error Statements (W3Schools)](https://www.w3schools.com/js/js_errors.asp)
- [MDN: try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
- [MDN: throw](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
- [MDN: Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation)
