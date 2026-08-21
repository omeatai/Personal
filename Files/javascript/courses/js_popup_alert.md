# JS Popup Alert

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The BOM popup trio is `alert`, `confirm`, and `prompt`. They are modal, blocking, and unstyled. Use `\n` for line breaks. Native dialogs cannot appear in these snapshots, so the sandbox mirrors the text on the page.

This section has **4** examples:

- [x] **Example 1:** alert() — alert box [View](#js-popup-alert-example-01)
- [x] **Example 2:** confirm() — OK / Cancel [View](#js-popup-alert-example-02)
- [x] **Example 3:** prompt() — ask for text [View](#js-popup-alert-example-03)
- [x] **Example 4:** Line breaks in popup text with \n [View](#js-popup-alert-example-04)

## Detailed Explanation

- [x] alert — message.
- [x] confirm — true/false.
- [x] prompt — string or null.
- [x] `\n` for a new line.

<a id="js-popup-alert-example-01"></a>

### **Example 1: alert() — alert box**

- [x] `window.alert(text)` (or `alert`) shows a modal message with **OK**.
- [x] It **blocks** script until dismissed — avoid it in real UIs.
- [x] You may omit the `window.` prefix.
- [x] Headless Chrome cannot show a native dialog in the PNG, so the sandbox **mirrors** the message on the page (same approach as JS Output).

Sandbox: `code_sandbox/js-popup-alert/alert.html`

```html
alert("I am an alert box!");
```

<img alt="js-popup-alert example 1 source" src="../code_sandbox/snaps/js-popup-alert-01-code.png" />

<img alt="js-popup-alert example 1 result" src="../code_sandbox/snaps/js-popup-alert-01-result.png" />

- [x] **Outcome:** The mirrored output is **alert: I am an alert box!**

<a id="js-popup-alert-example-02"></a>

### **Example 2: confirm() — OK / Cancel**

- [x] `confirm(text)` returns **`true`** for OK and **`false`** for Cancel.
- [x] Use the return value in an `if`.
- [x] Also modal and blocking — prefer a `<dialog>` for in-page UI.
- [x] The snapshot stubs `confirm` to return **true** (OK).

Sandbox: `code_sandbox/js-popup-alert/confirm.html`

```html
if (confirm("Press a button!")) {
  txt = "You pressed OK!";
} else {
  txt = "You pressed Cancel!";
}
```

<img alt="js-popup-alert example 2 source" src="../code_sandbox/snaps/js-popup-alert-02-code.png" />

<img alt="js-popup-alert example 2 result" src="../code_sandbox/snaps/js-popup-alert-02-result.png" />

- [x] **Outcome:** With OK stubbed, `txt` is **You pressed OK!**

<a id="js-popup-alert-example-03"></a>

### **Example 3: prompt() — ask for text**

- [x] `prompt(message, defaultText)` returns the string, or **`null`** if cancelled.
- [x] Empty OK yields `""`. Always check `null` and `""`.
- [x] The W3Schools default is **Harry Potter**.
- [x] The snapshot returns that default (as if the user clicked OK).

Sandbox: `code_sandbox/js-popup-alert/prompt.html`

```html
let person = prompt("Please enter your name", "Harry Potter");
let text;
if (person == null || person == "") {
  text = "User cancelled the prompt.";
} else {
  text = "Hello " + person + "! How are you today?";
}
```

<img alt="js-popup-alert example 3 source" src="../code_sandbox/snaps/js-popup-alert-03-code.png" />

<img alt="js-popup-alert example 3 result" src="../code_sandbox/snaps/js-popup-alert-03-result.png" />

- [x] **Outcome:** With default **Harry Potter** accepted, the greeting is **Hello Harry Potter! How are you today?**

<a id="js-popup-alert-example-04"></a>

### **Example 4: Line breaks in popup text with \n**

- [x] Popup text is **plain text**, not HTML.
- [x] Use **`\n`** for a new line (`alert("Hello\nHow are you?")`).
- [x] `<br>` would show as those characters, not a break.

Sandbox: `code_sandbox/js-popup-alert/line-breaks.html`

```html
alert("Hello\nHow are you?");
```

<img alt="js-popup-alert example 4 source" src="../code_sandbox/snaps/js-popup-alert-04-code.png" />

<img alt="js-popup-alert example 4 result" src="../code_sandbox/snaps/js-popup-alert-04-result.png" />

- [x] **Outcome:** The mirrored alert shows two lines: **Hello** then **How are you?**

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-popup-alert/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `alert` show?

<details>
<summary>Answer</summary>

- [x] A **modal** message with OK.

</details>

### Question 2: What does `confirm` return?

<details>
<summary>Answer</summary>

- [x] **`true`** (OK) or **`false`** (Cancel).

</details>

### Question 3: What does `prompt` return on Cancel?

<details>
<summary>Answer</summary>

- [x] **`null`**.

</details>

### Question 4: Can you omit `window.`?

<details>
<summary>Answer</summary>

- [x] **Yes** for `alert`, `confirm`, and `prompt`.

</details>

### Question 5: How do you put two lines in an alert?

<details>
<summary>Answer</summary>

- [x] A **`\n`** in the string.

</details>

### Question 6: Does `alert` accept HTML?

<details>
<summary>Answer</summary>

- [x] **No** — it is plain text.

</details>

### Question 7: Why avoid these in production UIs?

<details>
<summary>Answer</summary>

- [x] They **block** the thread and cannot be styled.

</details>

### Question 8: What is the W3Schools prompt default?

<details>
<summary>Answer</summary>

- [x] **Harry Potter**.

</details>

### Question 9: What text appears if confirm is cancelled?

<details>
<summary>Answer</summary>

- [x] **You pressed Cancel!** in their if/else.

</details>

### Question 10: What is a modern in-page alternative?

<details>
<summary>Answer</summary>

- [x] The HTML **`<dialog>`** element (or non-modal UI).

</details>


</details>

## Summary

alert/confirm/prompt still work but block the page. Prefer in-page UI. Remember confirm’s boolean and prompt’s null-on-cancel.

## References

- [JS Popup Alert](https://www.w3schools.com/js/js_popup.asp)
- [MDN Window.alert()](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert)
