# Input Form Attributes

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

W3Schools page title: **HTML Input form\* Attributes**. These `form*` attributes on **`<input>`** override the parent `<form>`, or associate a control **outside** the form. Covered: **`form`**, **`formaction`**, **`formenctype`**, **`formmethod`**, **`formtarget`**, **`formnovalidate`**, plus form-level **`novalidate`**.

This section has **3** examples:

- [x] **Example 1:** `form` [View](#input-form-attributes-example-01)
- [x] **Example 2:** Overrides [View](#input-form-attributes-example-02)
- [x] **Example 3:** Novalidate [View](#input-form-attributes-example-03)

## Detailed Explanation

- [x] **`form`**
  - Which `<form>` this input belongs to.
  - Value must equal that form’s **`id`**.
  - Last name can sit **outside** the form and still submit with `form="form1"`.
  - Sandbox: `code_sandbox/html-input-form-attributes/index.html`.

<img alt="html-input-form-attributes form= result" src="../code_sandbox/snaps/html-input-form-attributes-result.png" />

<a id="input-form-attributes-example-01"></a>

### **Example 1: `form`**

- [x] This example runs the tested markup in `code_sandbox/input-form-attributes/index.html`.

Sandbox: `code_sandbox/input-form-attributes/index.html`

```html
<form action="/action_page.php" id="form1">
  <input type="text" id="fname" name="fname" />
</form>
<input type="text" id="lname" name="lname" form="form1" />
```

<img alt="html-input-form-attributes source" src="../code_sandbox/snaps/html-input-form-attributes-code.png" />

<img alt="html-input-form-attributes form= result" src="../code_sandbox/snaps/html-input-form-attributes-result.png" />

- [x] **Outcome:** the page demonstrates **`form`** as shown in the result snap.

<a id="input-form-attributes-example-02"></a>

### **Example 2: Overrides**

- [x] **Overrides on `type="submit"` and `type="image"`** (except `formnovalidate`: submit only)
  - **`formaction`** — overrides `action` (example: **Submit as Admin** → `/action_page2.php`).
  - **`formenctype`** — overrides `enctype` (POST only). Second button: `multipart/form-data`.
  - **`formmethod`** — overrides `method` (`get` vs `post`). GET is bookmarkable but visible in the URL and size-limited; POST is more robust.
  - **`formtarget`** — overrides `target` (example: `_blank`).
  - Sandbox: `override.html`.

Sandbox: `code_sandbox/input-form-attributes/override.html`

```html
<input type="submit" formaction="/action_page2.php" value="Submit as Admin" />
<input type="submit" formmethod="post" value="Submit using POST" />
<input type="submit" formtarget="_blank" value="Submit to a new window/tab" />
<input
  type="submit"
  formenctype="multipart/form-data"
  value="Submit as Multipart"
/>
```

<img alt="html-input-form-attributes overrides source" src="../code_sandbox/snaps/html-input-form-attributes-01-code.png" />

<img alt="html-input-form-attributes override buttons result" src="../code_sandbox/snaps/html-input-form-attributes-01-result.png" />

- [x] **Outcome:** the page demonstrates **Overrides** as shown in the result snap.

<a id="input-form-attributes-example-03"></a>

### **Example 3: Novalidate**

- [x] **`formnovalidate` vs `novalidate`**
  - `formnovalidate` on a **submit** button skips validation for that click.
  - `novalidate` on **`<form>`** skips validation for the whole form.
  - Sandbox: `novalidate.html`.

Sandbox: `code_sandbox/input-form-attributes/novalidate.html`

```html
<input
  type="submit"
  formnovalidate="formnovalidate"
  value="Submit without validation"
/>
<form action="/action_page.php" novalidate></form>
```

<img alt="html-input-form-attributes novalidate source" src="../code_sandbox/snaps/html-input-form-attributes-02-code.png" />

<img alt="html-input-form-attributes novalidate result" src="../code_sandbox/snaps/html-input-form-attributes-02-result.png" />

- [x] **Outcome:** the page demonstrates **Novalidate** as shown in the result snap.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-input-form-attributes/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How can an input outside `<form>` still submit?

<details>
<summary>Answer</summary>

- [x] Set **`form="theFormId"`** equal to the form’s **`id`**.

</details>

### Question 2: What does `formaction` override?

<details>
<summary>Answer</summary>

- [x] The form’s **`action`**.
- [x] Works on **`submit`** and **`image`**.

</details>

### Question 3: When does `formenctype` apply?

<details>
<summary>Answer</summary>

- [x] Only with **`method="post"`**.
- [x] It overrides the form’s **`enctype`**.

</details>

### Question 4: GET vs POST on a submit button?

<details>
<summary>Answer</summary>

- [x] `formmethod="get"` — data in the **URL** (bookmarkable, visible, size-limited).
- [x] `formmethod="post"` — request **body** (not bookmarkable, more robust).

</details>

### Question 5: What does `formtarget="_blank"` do?

<details>
<summary>Answer</summary>

- [x] Shows the response in a **new window or tab**.
- [x] Overrides the form’s **`target`**.

</details>

### Question 6: `formnovalidate` vs `novalidate`?

<details>
<summary>Answer</summary>

- [x] `formnovalidate` — skip validation for **that submit button**.
- [x] `novalidate` — skip validation for the **whole form**.

</details>

</details>

## Summary

`form` ties an outside input to a form `id`. On submit/image buttons, `formaction`, `formenctype`, `formmethod`, and `formtarget` override the parent form. `formnovalidate` skips checks for one button; `novalidate` skips them for the form.

## References

- [HTML Input form\* Attributes (W3Schools)](https://www.w3schools.com/html/html_form_attributes_form.asp)
- [HTML Form Attributes](https://www.w3schools.com/html/html_forms_attributes.asp)
- [MDN: `<input>` form attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#form)
- [MDN: `formaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#formaction)
