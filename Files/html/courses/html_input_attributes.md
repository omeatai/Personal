# HTML Input Attributes

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

This chapter covers attributes of **`<input>`**: **`value`**, **`readonly`**, **`disabled`**, **`size`**, **`maxlength`**, **`min`/`max`**, **`multiple`**, **`pattern`**, **`placeholder`**, **`required`**, **`step`**, **`autofocus`**, **`height`/`width`**, **`list`**, and **`autocomplete`**. Browser checks are **not** enough — the **server** must validate too.

This section has **3** examples:

- [x] **Example 1:** Readonly / disabled [View](#html-input-attributes-example-01)
- [x] **Example 2:** Limits [View](#html-input-attributes-example-02)
- [x] **Example 3:** List / autocomplete / image [View](#html-input-attributes-example-03)

## Detailed Explanation

- [x] **`value`** — initial/default text (John / Doe).
- [x] **`readonly`** — cannot edit; **can** tab, highlight, copy; **is submitted**.
- [x] **`size`** — visible width in **characters** (default **20**). Works with text, search, tel, url, email, password.
- [x] **`maxlength`** — max characters; the field **stops accepting** more, but gives **no message** (use JS to alert).
- [x] **`min` / `max`** — number, range, date, datetime-local, month, time, week.
- [x] **`multiple`** — more than one value (`email`, `file`).
- [x] **`pattern`** — regex checked on submit (text, date, search, url, tel, email, password). Use **`title`** to explain (three-letter country code).
- [x] **`placeholder`** — hint before typing (`123-45-678`).
- [x] **`required`** — must be filled (text, search, url, tel, email, password, date pickers, number, checkbox, radio, file).
- [x] **`autofocus`** — focus on load (omitted from the sandbox so snapping does not steal focus).
- [x] **`height` / `width`** — size of `type="image"`. Set both so layout does not jump while the image loads.
- [x] **`list`** — points at a `<datalist>` `id`.
- [x] **Note:** Restrictions are **not foolproof**. Check again on the **server**.

<a id="html-input-attributes-example-01"></a>

### **Example 1: Readonly / disabled**

- [x] **`disabled`** — unusable / un-clickable; **not submitted**.

Sandbox: `code_sandbox/html-input-attributes/index.html`

```html
<input type="text" name="fname" value="John" readonly />
<input type="text" name="lname" value="Doe" disabled />
```

<img alt="html-input-attributes source" src="../code_sandbox/snaps/html-input-attributes-code.png" />

<img alt="html-input-attributes value readonly disabled result" src="../code_sandbox/snaps/html-input-attributes-result.png" />

- [x] **Outcome:** the page demonstrates **Readonly / disabled** as shown in the result snap.

<a id="html-input-attributes-example-02"></a>

### **Example 2: Limits**

- [x] **`step`** — legal intervals (`step="3"` → -3, 0, 3, 6…).
  - Sandbox: `limits.html`.

Sandbox: `code_sandbox/html-input-attributes/limits.html`

```html
<input type="text" size="50" />
<input type="text" maxlength="4" size="4" />
<input type="number" min="1" max="5" />
<input type="file" multiple />
<input type="text" pattern="[A-Za-z]{3}" title="Three letter country code" />
<input type="tel" placeholder="123-45-678" />
<input type="text" required />
<input type="number" step="3" />
```

<img alt="html-input-attributes limits source" src="../code_sandbox/snaps/html-input-attributes-01-code.png" />

<img alt="html-input-attributes limits result" src="../code_sandbox/snaps/html-input-attributes-01-result.png" />

- [x] **Outcome:** the page demonstrates **Limits** as shown in the result snap.

<a id="html-input-attributes-example-03"></a>

### **Example 3: List / autocomplete / image**

- [x] **`autocomplete`** — on/off for a form or field (text, search, url, tel, email, password, date pickers, range, color). Some browsers need autocomplete enabled in Preferences.
  - Sandbox: `extra.html`.

Sandbox: `code_sandbox/html-input-attributes/extra.html`

```html
<input list="browsers" />
<input type="email" autocomplete="off" />
<input type="image" src="img_submit.gif" width="48" height="48" />
```

<img alt="html-input-attributes extra source" src="../code_sandbox/snaps/html-input-attributes-02-code.png" />

<img alt="html-input-attributes list autocomplete image result" src="../code_sandbox/snaps/html-input-attributes-02-result.png" />

- [x] **Outcome:** the page demonstrates **List / autocomplete / image** as shown in the result snap.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-input-attributes/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Is a readonly field submitted? A disabled field?

<details>
<summary>Answer</summary>

- [x] **Readonly: yes** (and you can copy the text).
- [x] **Disabled: no.**

</details>

### Question 2: What is the default `size`?

<details>
<summary>Answer</summary>

- [x] **20** characters.
- [x] `size` applies to text, search, tel, url, email, password.

</details>

### Question 3: Does `maxlength` show an error message?

<details>
<summary>Answer</summary>

- [x] **No.** Extra characters are blocked silently.
- [x] Use **JavaScript** if you want an alert.

</details>

### Question 4: Which types support `multiple`?

<details>
<summary>Answer</summary>

- [x] **`email`** and **`file`**.

</details>

### Question 5: How do you explain a `pattern` to the user?

<details>
<summary>Answer</summary>

- [x] Set the global **`title`** attribute (for example “Three letter country code”).

</details>

### Question 6: What does `step="3"` allow?

<details>
<summary>Answer</summary>

- [x] Legal numbers such as **-3, 0, 3, 6**, …

</details>

### Question 7: Why set both `height` and `width` on `type="image"`?

<details>
<summary>Answer</summary>

- [x] The browser **reserves space** so the layout does not jump while the image loads.

</details>

### Question 8: Are these attributes enough to secure a form?

<details>
<summary>Answer</summary>

- [x] **No.** Check the values again on the **server**.

</details>

</details>

## Summary

`value` sets defaults. Readonly submits; disabled does not. `size`/`maxlength` shape text; `min`/`max`/`step` shape numbers and dates. Use `pattern`+`title`, `placeholder`, `required`, `multiple`, `list`, and `autocomplete`. Always validate on the server.

## References

- [HTML Input Attributes (W3Schools)](https://www.w3schools.com/html/html_form_attributes.asp)
- [HTML Input Types](https://www.w3schools.com/html/html_form_input_types.asp)
- [MDN: `<input>` attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#attributes)
