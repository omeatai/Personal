# HTML First Features

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Native HTML can replace small JavaScript widgets: disclosures, validation, specialized inputs, datalist, dialog, and lazy images.

This section has **10** examples:

- [x] **Example 1:** The details element [View](#html-first-features-example-01)
- [x] **Example 2:** HTML form validation attributes [View](#html-first-features-example-02)
- [x] **Example 3:** Input type — email [View](#html-first-features-example-03)
- [x] **Example 4:** Input type — number [View](#html-first-features-example-04)
- [x] **Example 5:** Input type — date (Birthday example) [View](#html-first-features-example-05)
- [x] **Example 6:** Input type — url [View](#html-first-features-example-06)
- [x] **Example 7:** Input type — search [View](#html-first-features-example-07)
- [x] **Example 8:** The datalist element [View](#html-first-features-example-08)
- [x] **Example 9:** The dialog element [View](#html-first-features-example-09)
- [x] **Example 10:** Lazy loading images [View](#html-first-features-example-10)

## Detailed Explanation

- [x] Ask: can the browser already do this?
- [x] `details`, constraint validation, input types, `datalist`, `dialog`, `loading=lazy`.
- [x] Add JS only when native HTML is not enough.

<a id="html-first-features-example-01"></a>

### **Example 1: The details element**

- [x] `<details>` is a disclosure widget. `<summary>` is the always-visible heading.
- [x] No JavaScript. The `open` attribute (or `.open` property) controls state.
- [x] W3Schools: “This works without any JavaScript.”

Sandbox: `code_sandbox/html-first-features/details.html`

```html
<details>
  <summary>More information</summary>
  This text is hidden until the user opens it.
</details>
```

<img alt="html-first-features example 1 source" src="../code_sandbox/snaps/html-first-features-01-code.png" />

<img alt="html-first-features example 1 result" src="../code_sandbox/snaps/html-first-features-01-result.png" />

- [x] **Outcome:** With `open` set for the snapshot, the extra text is visible; `open` is **true**.

<a id="html-first-features-example-02"></a>

### **Example 2: HTML form validation attributes**

- [x] `required`, `minlength`, `maxlength`, `pattern` run **in the browser** before submit.
- [x] The Register form checks username + email automatically.
- [x] JS is optional for extra messages; the constraint API still works without it.

Sandbox: `code_sandbox/html-first-features/form-validation-native.html`

```html
<form>
  <label>Username: <input name="user" required minlength="3"></label>
  <label>Email: <input name="email" type="email" required></label>
  <button>Register</button>
</form>
```

<img alt="html-first-features example 2 source" src="../code_sandbox/snaps/html-first-features-02-code.png" />

<img alt="html-first-features example 2 result" src="../code_sandbox/snaps/html-first-features-02-result.png" />

- [x] **Outcome:** Empty fields: `checkValidity()` is **false**. The browser would block Register.

<a id="html-first-features-example-03"></a>

### **Example 3: Input type — email**

- [x] `type="email"` adds format checking and a friendlier **mobile keyboard**.
- [x] Invalid strings set `typeMismatch`.
- [x] Listed on the page as a common native type.

Sandbox: `code_sandbox/html-first-features/type-email.html`

```html
<input id="e" type="email" value="not-an-email">
```

<img alt="html-first-features example 3 source" src="../code_sandbox/snaps/html-first-features-03-code.png" />

<img alt="html-first-features example 3 result" src="../code_sandbox/snaps/html-first-features-03-result.png" />

- [x] **Outcome:** **not-an-email** is invalid: `typeMismatch` is **true**.

<a id="html-first-features-example-04"></a>

### **Example 4: Input type — number**

- [x] `type="number"` is for numeric values; combine with `min`/`max`/`step`.
- [x] Some mobile browsers show a numeric keypad.
- [x] Non-numeric input is rejected by the control.

Sandbox: `code_sandbox/html-first-features/type-number.html`

```html
<input id="n" type="number" min="1" value="3">
```

<img alt="html-first-features example 4 source" src="../code_sandbox/snaps/html-first-features-04-code.png" />

<img alt="html-first-features example 4 result" src="../code_sandbox/snaps/html-first-features-04-result.png" />

- [x] **Outcome:** Value **3** with `min=1` is **valid**.

<a id="html-first-features-example-05"></a>

### **Example 5: Input type — date (Birthday example)**

- [x] `type="date"` shows a date picker in supporting browsers.
- [x] W3Schools Birthday field is this control.
- [x] The value is `yyyy-mm-dd` when set.

Sandbox: `code_sandbox/html-first-features/type-date.html`

```html
<label>Birthday: <input id="b" type="date" value="2000-01-31"></label>
```

<img alt="html-first-features example 5 source" src="../code_sandbox/snaps/html-first-features-05-code.png" />

<img alt="html-first-features example 5 result" src="../code_sandbox/snaps/html-first-features-05-result.png" />

- [x] **Outcome:** The date input holds **2000-01-31**.

<a id="html-first-features-example-06"></a>

### **Example 6: Input type — url**

- [x] `type="url"` expects a full URL (usually including a scheme).
- [x] `example.com` without `https://` is often **invalid**.
- [x] Mobile keyboards may offer `/` and `.com` shortcuts.

Sandbox: `code_sandbox/html-first-features/type-url.html`

```html
<input id="u" type="url" value="https://example.com">
```

<img alt="html-first-features example 6 source" src="../code_sandbox/snaps/html-first-features-06-code.png" />

<img alt="html-first-features example 6 result" src="../code_sandbox/snaps/html-first-features-06-result.png" />

- [x] **Outcome:** `https://example.com` is **valid** for `type=url`.

<a id="html-first-features-example-07"></a>

### **Example 7: Input type — search**

- [x] `type="search"` looks like text but may show a **clear ×** and a search keyboard.
- [x] Semantics help password managers and AT less than `email`, but it is the dedicated search control.
- [x] Listed among the page’s input types.

Sandbox: `code_sandbox/html-first-features/type-search.html`

```html
<input id="s" type="search" value="html first">
```

<img alt="html-first-features example 7 source" src="../code_sandbox/snaps/html-first-features-07-code.png" />

<img alt="html-first-features example 7 result" src="../code_sandbox/snaps/html-first-features-07-result.png" />

- [x] **Outcome:** `type` reports **search** and the value is kept.

<a id="html-first-features-example-08"></a>

### **Example 8: The datalist element**

- [x] `<datalist>` suggests values; the user may **pick or type something else**.
- [x] Hook it up with `input list="id"` matching `datalist id`.
- [x] This is autocomplete **without** a JS widget.

Sandbox: `code_sandbox/html-first-features/datalist.html`

```html
<label>Choose a browser:
  <input list="browsers" name="browser">
</label>
<datalist id="browsers">
  <option value="Edge">
  <option value="Firefox">
  <option value="Chrome">
  <option value="Opera">
  <option value="Safari">
</datalist>
```

<img alt="html-first-features example 8 source" src="../code_sandbox/snaps/html-first-features-08-code.png" />

<img alt="html-first-features example 8 result" src="../code_sandbox/snaps/html-first-features-08-result.png" />

- [x] **Outcome:** The datalist has **5** options; the input’s `list` id is **browsers**.

<a id="html-first-features-example-09"></a>

### **Example 9: The dialog element**

- [x] `<dialog>` is a native modal/non-modal dialog.
- [x] Opening usually needs a **small** script: `dialog.show()` / `showModal()`. Closing: `close()`.
- [x] Behavior (focus trap, backdrop for modal) is **built into the browser** — not a JS overlay library.

Sandbox: `code_sandbox/html-first-features/dialog.html`

```html
<dialog id="d" open>
  This is an open dialog window.
</dialog>
```

<img alt="html-first-features example 9 source" src="../code_sandbox/snaps/html-first-features-09-code.png" />

<img alt="html-first-features example 9 result" src="../code_sandbox/snaps/html-first-features-09-result.png" />

- [x] **Outcome:** The dialog is **open** in the snapshot (`open` attribute / `.open` true).

<a id="html-first-features-example-10"></a>

### **Example 10: Lazy loading images**

- [x] `loading="lazy"` defers off-screen images (and iframes) until near the viewport.
- [x] Native performance win — used to need IntersectionObserver JS.
- [x] W3Schools: use native HTML first; add JS only when native HTML cannot solve the problem.

Sandbox: `code_sandbox/html-first-features/lazy.html`

```html
<img alt="later" loading="lazy" width="16" height="16"
  src="data:image/gif;base64,R0lGODlhAQABAAAAACw=">
```

<img alt="html-first-features example 10 source" src="../code_sandbox/snaps/html-first-features-10-code.png" />

<img alt="html-first-features example 10 result" src="../code_sandbox/snaps/html-first-features-10-result.png" />

- [x] **Outcome:** `img.loading` is **lazy**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/html-first-features/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What tag pair makes an accordion without JS?

<details>
<summary>Answer</summary>

- [x] **`<details>`** and **`<summary>`**.

</details>

### Question 2: Which attributes validate a username of at least 3 characters?

<details>
<summary>Answer</summary>

- [x] **`required`** and **`minlength="3"`**.

</details>

### Question 3: Does the browser check `type="email"` without JS?

<details>
<summary>Answer</summary>

- [x] **Yes** — constraint validation is native.

</details>

### Question 4: What value format does `type="date"` use?

<details>
<summary>Answer</summary>

- [x] **`yyyy-mm-dd`**.

</details>

### Question 5: Can a user type a value that is not in a datalist?

<details>
<summary>Answer</summary>

- [x] **Yes** — suggestions are not a closed list.

</details>

### Question 6: How do you attach a datalist?

<details>
<summary>Answer</summary>

- [x] `input list="the-id"` matching **`<datalist id>`**.

</details>

### Question 7: Does `<dialog>` need JS?

<details>
<summary>Answer</summary>

- [x] A **little** to open/close (`showModal`/`close`); the widget itself is native.

</details>

### Question 8: What does `loading="lazy"` do?

<details>
<summary>Answer</summary>

- [x] Defers loading until the image is **near the viewport**.

</details>

### Question 9: Name two `type` values from the page list.

<details>
<summary>Answer</summary>

- [x] Any two of **email, number, date, url, search**.

</details>

### Question 10: When do you add JavaScript according to this page?

<details>
<summary>Answer</summary>

- [x] Only when **native HTML cannot** solve the problem.

</details>


</details>

## Summary

Reach for `details`, form attributes, input types, `datalist`, `dialog`, and `loading="lazy"` before writing a custom widget.

## References

- [HTML First Features](https://www.w3schools.com/js/js_htmlfirst_features.asp)
- [MDN Progressive enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement)
