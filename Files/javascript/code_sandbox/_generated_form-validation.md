<details>
  <summary>Form Validation</summary>

## Introduction

Forms can be checked with JavaScript (`return false`) or with HTML5 constraint validation (`required`, `min`, `pattern`, `:invalid`).

This section has **12** examples:

- [x] **Example 1:** JavaScript — reject an empty name [View](#form-validation-example-01)
- [x] **Example 2:** JavaScript — number between 1 and 10 [View](#form-validation-example-02)
- [x] **Example 3:** Automatic HTML validation — required [View](#form-validation-example-03)
- [x] **Example 4:** Data validation — client vs server [View](#form-validation-example-04)
- [x] **Example 5:** Constraint attribute — disabled [View](#form-validation-example-05)
- [x] **Example 6:** Constraint attributes — min and max [View](#form-validation-example-06)
- [x] **Example 7:** Constraint attribute — pattern [View](#form-validation-example-07)
- [x] **Example 8:** Constraint attribute — required [View](#form-validation-example-08)
- [x] **Example 9:** Constraint attribute — type [View](#form-validation-example-09)
- [x] **Example 10:** CSS pseudo — :disabled [View](#form-validation-example-10)
- [x] **Example 11:** CSS pseudo — :invalid and :valid [View](#form-validation-example-11)
- [x] **Example 12:** CSS pseudo — :required and :optional [View](#form-validation-example-12)

## Detailed Explanation

- [x] Client-side checks improve UX; **server-side** checks are required for safety.
- [x] HTML `required` / `min` / `max` / `pattern` / `type` work without JS in modern browsers.
- [x] CSS `:valid` / `:invalid` / `:required` / `:optional` / `:disabled` style those states.

<a id="form-validation-example-01"></a>

### **Example 1: JavaScript — reject an empty name**

- [x] `document.forms["myForm"]["fname"].value` reads the **Name** field.
- [x] If it is `""`, `alert` and **`return false`** cancel submit (with `onsubmit="return validateForm()"`).
- [x] Returning **true** (or nothing after checks pass) allows the submit.
- [x] The sandbox submits an empty form and records that validation **blocked** it (`preventDefault` equivalent via `return false`).

Sandbox: `code_sandbox/form-validation/js-empty-name.html`

```html
<form name="myForm" onsubmit="return validateForm()" action="#">
  Name: <input type="text" name="fname">
  <input type="submit" value="Submit">
</form>
<script>
function validateForm() {
  let x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }
}
</script>
```

<img alt="form-validation example 1 source" src="./code_sandbox/snaps/form-validation-01-code.png" />

<img alt="form-validation example 1 result" src="./code_sandbox/snaps/form-validation-01-result.png" />

- [x] **Outcome:** Empty name → validation returns **false** and the form does not navigate away.

<a id="form-validation-example-02"></a>

### **Example 2: JavaScript — number between 1 and 10**

- [x] Read the input, convert with `Number` or compare as numbers.
- [x] If the value is outside **1–10** (or not a number), show a message and stop.
- [x] The snapshot enters **15**, which fails the range check.

Sandbox: `code_sandbox/form-validation/js-numeric-range.html`

```html
<p>Please input a number between 1 and 10</p>
<input id="num" type="number">
<button type="button" id="go">Submit</button>
<script>
document.getElementById("go").onclick = function () {
  const v = Number(document.getElementById("num").value);
  if (Number.isNaN(v) || v < 1 || v > 10) {
    document.getElementById("demo").innerText = "Invalid: need 1–10";
  } else {
    document.getElementById("demo").innerText = "OK: " + v;
  }
};
</script>
```

<img alt="form-validation example 2 source" src="./code_sandbox/snaps/form-validation-02-code.png" />

<img alt="form-validation example 2 result" src="./code_sandbox/snaps/form-validation-02-result.png" />

- [x] **Outcome:** Value **15** is rejected: **Invalid: need 1–10**.

<a id="form-validation-example-03"></a>

### **Example 3: Automatic HTML validation — required**

- [x] The **`required`** attribute stops submit when the field is empty — **no JavaScript**.
- [x] The browser shows its own message. This did not work in **IE 9** and earlier (historical note).
- [x] `checkValidity()` returns false when empty. `reportValidity()` would show the native bubble.

Sandbox: `code_sandbox/form-validation/html-required.html`

```html
<form id="f" action="#">
  <input name="fname" required>
  <input type="submit">
</form>
```

<img alt="form-validation example 3 source" src="./code_sandbox/snaps/form-validation-03-code.png" />

<img alt="form-validation example 3 result" src="./code_sandbox/snaps/form-validation-03-result.png" />

- [x] **Outcome:** `checkValidity()` is **false** on an empty required field — the browser would block submit.

<a id="form-validation-example-04"></a>

### **Example 4: Data validation — client vs server**

- [x] **Data validation** means input is clean, correct, and useful (required filled, dates valid, numbers in numeric fields).
- [x] **Client-side** runs in the browser **before** send — fast UX, easy to skip (user can disable JS).
- [x] **Server-side** runs **after** the request arrives — the one you must trust for security.
- [x] Use both: client for instant help, server as the real gate.

Sandbox: `code_sandbox/form-validation/server-vs-client.html`

```html
<script>
const kinds = [
  "Client-side: browser, before request",
  "Server-side: server, after request"
];
</script>
```

<img alt="form-validation example 4 source" src="./code_sandbox/snaps/form-validation-04-code.png" />

<img alt="form-validation example 4 result" src="./code_sandbox/snaps/form-validation-04-result.png" />

- [x] **Outcome:** The snapshot lists **client-side** (before send) and **server-side** (after send).

<a id="form-validation-example-05"></a>

### **Example 5: Constraint attribute — disabled**

- [x] `disabled` means the control is not editable and is **not submitted**.
- [x] CSS `:disabled` matches it. JS `el.disabled = true` toggles the same state.

Sandbox: `code_sandbox/form-validation/attr-disabled.html`

```html
<input id="x" value="locked" disabled>
```

<img alt="form-validation example 5 source" src="./code_sandbox/snaps/form-validation-05-code.png" />

<img alt="form-validation example 5 result" src="./code_sandbox/snaps/form-validation-05-result.png" />

- [x] **Outcome:** The input is **disabled**; `disabled` is **true** and it matches `:disabled`.

<a id="form-validation-example-06"></a>

### **Example 6: Constraint attributes — min and max**

- [x] `min` / `max` bound numeric (and date) inputs.
- [x] `validity.rangeUnderflow` / `rangeOverflow` tell you which way it failed.
- [x] The snapshot sets **0** on a field with `min="1" max="10"`.

Sandbox: `code_sandbox/form-validation/attr-min-max.html`

```html
<input id="n" type="number" min="1" max="10" value="0">
```

<img alt="form-validation example 6 source" src="./code_sandbox/snaps/form-validation-06-code.png" />

<img alt="form-validation example 6 result" src="./code_sandbox/snaps/form-validation-06-result.png" />

- [x] **Outcome:** **0** is below min: `rangeUnderflow` is **true**, `checkValidity` is **false**.

<a id="form-validation-example-07"></a>

### **Example 7: Constraint attribute — pattern**

- [x] `pattern` is a **regex** for the whole value (HTML already anchors it).
- [x] Example: `[A-Za-z]{3}` means exactly three letters.
- [x] `validity.patternMismatch` is true when the value does not match.

Sandbox: `code_sandbox/form-validation/attr-pattern.html`

```html
<input id="p" pattern="[A-Za-z]{3}" value="12">
```

<img alt="form-validation example 7 source" src="./code_sandbox/snaps/form-validation-07-code.png" />

<img alt="form-validation example 7 result" src="./code_sandbox/snaps/form-validation-07-result.png" />

- [x] **Outcome:** **12** fails `[A-Za-z]{3}`: **patternMismatch** is true.

<a id="form-validation-example-08"></a>

### **Example 8: Constraint attribute — required**

- [x] `required` means the field must have a value before submit.
- [x] `validity.valueMissing` is the flag for “empty but required”.
- [x] This is the same idea as the automatic HTML example, as a table row of its own.

Sandbox: `code_sandbox/form-validation/attr-required.html`

```html
<input id="r" required value="">
```

<img alt="form-validation example 8 source" src="./code_sandbox/snaps/form-validation-08-code.png" />

<img alt="form-validation example 8 result" src="./code_sandbox/snaps/form-validation-08-result.png" />

- [x] **Outcome:** Empty required input: **valueMissing** true, `checkValidity` false.

<a id="form-validation-example-09"></a>

### **Example 9: Constraint attribute — type**

- [x] `type` selects the control and its built-in checks (`email`, `number`, `url`, …).
- [x] `type="email"` with `not-an-email` sets `validity.typeMismatch`.
- [x] Mobile browsers also pick a suitable keyboard from `type`.

Sandbox: `code_sandbox/form-validation/attr-type.html`

```html
<input id="e" type="email" value="not-an-email">
```

<img alt="form-validation example 9 source" src="./code_sandbox/snaps/form-validation-09-code.png" />

<img alt="form-validation example 9 result" src="./code_sandbox/snaps/form-validation-09-result.png" />

- [x] **Outcome:** **not-an-email** fails `type="email"`: **typeMismatch** is true.

<a id="form-validation-example-10"></a>

### **Example 10: CSS pseudo — :disabled**

- [x] `:disabled` selects inputs that have the disabled attribute / property.
- [x] Use it to grey out labels or hide helper text next to dead controls.

Sandbox: `code_sandbox/form-validation/pseudo-disabled.html`

```html
<input id="d" disabled>
<script>
document.querySelector("input:disabled");
</script>
```

<img alt="form-validation example 10 source" src="./code_sandbox/snaps/form-validation-10-code.png" />

<img alt="form-validation example 10 result" src="./code_sandbox/snaps/form-validation-10-result.png" />

- [x] **Outcome:** `querySelector("input:disabled")` finds the disabled control.

<a id="form-validation-example-11"></a>

### **Example 11: CSS pseudo — :invalid and :valid**

- [x] `:invalid` matches controls that fail constraint validation **right now**.
- [x] `:valid` is the opposite. Empty non-required fields are usually valid.
- [x] Great for red/green outlines without JavaScript.

Sandbox: `code_sandbox/form-validation/pseudo-invalid-valid.html`

```html
<input id="bad" type="email" value="x">
<input id="good" type="email" value="a@b.c">
```

<img alt="form-validation example 11 source" src="./code_sandbox/snaps/form-validation-11-code.png" />

<img alt="form-validation example 11 result" src="./code_sandbox/snaps/form-validation-11-result.png" />

- [x] **Outcome:** `#bad` matches **:invalid**; `#good` matches **:valid**.

<a id="form-validation-example-12"></a>

### **Example 12: CSS pseudo — :required and :optional**

- [x] `:required` selects fields with the required attribute.
- [x] `:optional` selects fields **without** required.
- [x] Use them to mark mandatory fields in CSS alone.

Sandbox: `code_sandbox/form-validation/pseudo-required-optional.html`

```html
<input id="req" required>
<input id="opt">
```

<img alt="form-validation example 12 source" src="./code_sandbox/snaps/form-validation-12-code.png" />

<img alt="form-validation example 12 result" src="./code_sandbox/snaps/form-validation-12-result.png" />

- [x] **Outcome:** `#req` matches **:required**; `#opt` matches **:optional**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/form-validation/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How does the empty-name script cancel submit?

<details>
<summary>Answer</summary>

- [x] It **`return false`** from the `onsubmit` handler after `alert`.

</details>

### Question 2: How do you read `fname` on `myForm`?

<details>
<summary>Answer</summary>

- [x] `document.forms["myForm"]["fname"].value`.

</details>

### Question 3: Is 15 valid for “number between 1 and 10”?

<details>
<summary>Answer</summary>

- [x] No — it is **outside** the range.

</details>

### Question 4: What HTML attribute blocks empty submit without JS?

<details>
<summary>Answer</summary>

- [x] **`required`**.

</details>

### Question 5: Why still validate on the server?

<details>
<summary>Answer</summary>

- [x] Client checks can be **skipped**. Security and correctness live on the **server**.

</details>

### Question 6: What flag is set when a required field is empty?

<details>
<summary>Answer</summary>

- [x] **`validity.valueMissing`**.

</details>

### Question 7: What flag is set for `type="email"` with `not-an-email`?

<details>
<summary>Answer</summary>

- [x] **`typeMismatch`**.

</details>

### Question 8: What does `pattern` use?

<details>
<summary>Answer</summary>

- [x] A **regular expression** for the whole value.

</details>

### Question 9: Which CSS selector matches a failing control?

<details>
<summary>Answer</summary>

- [x] **:invalid**.

</details>

### Question 10: Does `:optional` mean the value is wrong?

<details>
<summary>Answer</summary>

- [x] No — it means the field is **not required**.

</details>

### Question 11: What does `disabled` do to submit data?

<details>
<summary>Answer</summary>

- [x] Disabled controls are **not successful** — they are omitted from the submit payload.

</details>

### Question 12: IE 9 and `required`?

<details>
<summary>Answer</summary>

- [x] Automatic HTML5 validation **did not work** in IE 9 or earlier (historical).

</details>


</details>

## Summary

Use HTML constraints first, add JS for custom rules, and always validate again on the server.

## References

- [Form Validation](https://www.w3schools.com/js/js_validation.asp)
- [MDN Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)

</details>
