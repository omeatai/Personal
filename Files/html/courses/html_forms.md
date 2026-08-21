# HTML Forms

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

An HTML **form** collects **user input**, most often sent to a **server** for processing. This chapter introduces `<form>` and `<input>`, **text fields**, `<label>`, **radio buttons**, **checkboxes**, the **submit** button (`action`), and why every submitted field needs a **`name`**.

This section has **5** examples:

- [x] **Example 1:** Text fields [View](#html-forms-example-01)
- [x] **Example 2:** Radio [View](#html-forms-example-02)
- [x] **Example 3:** Checkboxes [View](#html-forms-example-03)
- [x] **Example 4:** Submit [View](#html-forms-example-04)
- [x] **Example 5:** Missing `name` [View](#html-forms-example-05)

## Detailed Explanation

- [x] **`<form>`**
  - Container for input elements: text fields, checkboxes, radio buttons, submit buttons, and more.
  - Form elements are covered in **HTML Form Elements**.
- [x] **`<input>`**
  - The most used form element. Appearance depends on **`type`**.

| Type              | Description                  |
| ----------------- | ---------------------------- |
| `type="text"`     | Single-line text field       |
| `type="radio"`    | One of many choices          |
| `type="checkbox"` | Zero or more of many choices |
| `type="submit"`   | Submit the form              |
| `type="button"`   | Clickable button             |

- All types: **HTML Input Types**.

- [x] **`<label>`**
  - Labels a form control. Screen readers read the label when the control is focused.
  - Clicking the label text also activates small controls (radio/checkbox).
  - Bind with **`for`** on `<label>` equal to **`id`** on `<input>`.

<a id="html-forms-example-01"></a>

### **Example 1: Text fields**

- [x] **Text fields**
  - `<input type="text">` is a **single-line** field. Default width is **20 characters**.
  - The form box itself is **not visible**.

Sandbox: `code_sandbox/html-forms/index.html`

```html
<form>
  <label for="fname">First name:</label><br />
  <input type="text" id="fname" name="fname" /><br />
  <label for="lname">Last name:</label><br />
  <input type="text" id="lname" name="lname" />
</form>
```

<img alt="html-forms text source" src="../code_sandbox/snaps/html-forms-code.png" />

<img alt="html-forms text fields result" src="../code_sandbox/snaps/html-forms-result.png" />

- [x] **Outcome:** the browser shows **First name: Last name:**.

<a id="html-forms-example-02"></a>

### **Example 2: Radio**

- [x] **Radio buttons**
  - `<input type="radio">` — select **ONE** of a limited set.
  - Same **`name`** (`fav_language`) groups the options.
  - Sandbox: `radio.html`.

Sandbox: `code_sandbox/html-forms/radio.html`

```html
<p>Choose your favorite Web language:</p>
<form>
  <input type="radio" id="html" name="fav_language" value="HTML" />
  <label for="html">HTML</label><br />
  <input type="radio" id="css" name="fav_language" value="CSS" />
  <label for="css">CSS</label><br />
  <input type="radio" id="javascript" name="fav_language" value="JavaScript" />
  <label for="javascript">JavaScript</label>
</form>
```

<img alt="html-forms radio source" src="../code_sandbox/snaps/html-forms-01-code.png" />

<img alt="html-forms radio result" src="../code_sandbox/snaps/html-forms-01-result.png" />

- [x] **Outcome:** the browser shows **Choose your favorite Web language:**, **HTML CSS JavaScript**.

<a id="html-forms-example-03"></a>

### **Example 3: Checkboxes**

- [x] **Checkboxes**
  - `<input type="checkbox">` — select **ZERO or MORE** options.
  - Sandbox: `checkbox.html`.

Sandbox: `code_sandbox/html-forms/checkbox.html`

```html
<form>
  <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike" />
  <label for="vehicle1"> I have a bike</label><br />
  <input type="checkbox" id="vehicle2" name="vehicle2" value="Car" />
  <label for="vehicle2"> I have a car</label><br />
  <input type="checkbox" id="vehicle3" name="vehicle3" value="Boat" />
  <label for="vehicle3"> I have a boat</label>
</form>
```

<img alt="html-forms checkbox source" src="../code_sandbox/snaps/html-forms-02-code.png" />

<img alt="html-forms checkbox result" src="../code_sandbox/snaps/html-forms-02-result.png" />

- [x] **Outcome:** the browser shows **I have a bike I have a car I have a boat**.

<a id="html-forms-example-04"></a>

### **Example 4: Submit**

- [x] **Submit button**
  - `<input type="submit">` sends data to the **form-handler** in **`action`** (here `/action_page.php`).
  - Example values: **John** / **Doe**.
  - Sandbox: `submit.html`.

Sandbox: `code_sandbox/html-forms/submit.html`

```html
<form action="/action_page.php">
  <label for="fname">First name:</label><br />
  <input type="text" id="fname" name="fname" value="John" /><br />
  <label for="lname">Last name:</label><br />
  <input type="text" id="lname" name="lname" value="Doe" /><br /><br />
  <input type="submit" value="Submit" />
</form>
```

<img alt="html-forms submit source" src="../code_sandbox/snaps/html-forms-03-code.png" />

<img alt="html-forms submit result" src="../code_sandbox/snaps/html-forms-03-result.png" />

- [x] **Outcome:** the browser shows **First name: Last name:**.

<a id="html-forms-example-05"></a>

### **Example 5: Missing `name`**

- [x] **`name` is required to submit**
  - If **`name` is omitted**, that field is **not sent**.
  - Sandbox: `no-name.html` — First name has `id` and `value="John"` but **no `name`**.

Sandbox: `code_sandbox/html-forms/no-name.html`

```html
<form action="/action_page.php">
  <label for="fname">First name:</label><br />
  <input type="text" id="fname" value="John" /><br /><br />
  <input type="submit" value="Submit" />
</form>
```

<img alt="html-forms missing name source" src="../code_sandbox/snaps/html-forms-04-code.png" />

<img alt="html-forms missing name result" src="../code_sandbox/snaps/html-forms-04-result.png" />

- [x] **Outcome:** the browser shows **First name:**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-forms/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is an HTML form for?

<details>
<summary>Answer</summary>

- [x] To **collect user input**.
- [x] The input is most often sent to a **server** for processing.

</details>

### Question 2: What does `<form>` contain?

<details>
<summary>Answer</summary>

- [x] Input elements: text fields, checkboxes, radio buttons, submit buttons, and so on.

</details>

### Question 3: Which attribute changes how `<input>` looks?

<details>
<summary>Answer</summary>

- [x] **`type`** — for example `text`, `radio`, `checkbox`, `submit`, `button`.

</details>

### Question 4: What is the default width of a text field?

<details>
<summary>Answer</summary>

- [x] **20 characters**.
- [x] The form container itself is **not visible**.

</details>

### Question 5: How do you bind a `<label>` to an input?

<details>
<summary>Answer</summary>

- [x] Set **`for`** on the label equal to the input’s **`id`**.

</details>

### Question 6: Why use `<label>` besides visible text?

<details>
<summary>Answer</summary>

- [x] Screen readers **read the label** when the control is focused.
- [x] Clicking the label toggles small controls (radio/checkbox).

</details>

### Question 7: Radio vs checkbox?

<details>
<summary>Answer</summary>

- [x] Radio: select **ONE** of a limited set (same `name` groups them).
- [x] Checkbox: select **ZERO or MORE** options.

</details>

### Question 8: How does submit know where to send data?

<details>
<summary>Answer</summary>

- [x] The form’s **`action`** attribute (the form-handler, often a server script).

</details>

### Question 9: What happens if an input has no `name`?

<details>
<summary>Answer</summary>

- [x] That field’s value is **not submitted** at all.

</details>

</details>

## Summary

`<form>` holds controls. `<input type="text|radio|checkbox|submit|button">` covers the common cases. Pair `<label for>` with `id`. Radios pick one; checkboxes pick any. Submit uses `action`. Every field you want sent needs a **`name`**.

## References

- [HTML Forms (W3Schools)](https://www.w3schools.com/html/html_forms.asp)
- [Try it Yourself: tryhtml_form_text](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_text)
- [Try it Yourself: tryhtml_form_radio](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_radio)
- [Try it Yourself: tryhtml_input_checkbox](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_checkbox)
- [Try it Yourself: tryhtml_form_submit](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit)
- [Try it Yourself: tryhtml_form_submit_id](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit_id)
- [HTML Form Elements](https://www.w3schools.com/html/html_form_elements.asp)
- [HTML Input Types](https://www.w3schools.com/html/html_form_input_types.asp)
- [MDN: `<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
- [MDN: `<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
