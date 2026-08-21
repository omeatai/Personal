# HTML Charsets

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

A browser must know the **character set** to display a page correctly. This chapter sets `charset` in `<meta>`, compares **ASCII**, **ANSI (Windows-1252)**, **ISO-8859-1**, and **UTF-8**, and shows why UTF-8 is the HTML recommendation.

This section has **2** examples:

- [x] **Example 1:** Declare UTF-8, then put Unicode in the file [View](#html-charsets-example-01)
- [x] **Example 2:** Sandbox body [View](#html-charsets-example-02)

## Detailed Explanation

- [x] **Specify the set** in a meta tag: `<meta charset="UTF-8">`.
- [x] The HTML spec encourages **UTF-8** — it covers almost all characters and symbols in the world.
- [x] **ASCII** — first web encoding; **128** Latin characters: a–z A–Z, 0–9, and some punctuation (`! $ + - ( ) @ < > . # ?`).
- [x] **ANSI (Windows-1252)** — first Windows set: ASCII for 0–127, extra characters 128–159, same as UTF-8 from 160–255. `<meta charset="Windows-1252">`.
- [x] **ISO-8859-1** — default for **HTML 4**; 256 characters. ASCII for 0–127, unused 128–159, same as ANSI/UTF-8 from 160–255.
  - HTML 4: `<meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1">`
  - HTML 5: `<meta charset="ISO-8859-1">`
- [x] **UTF-8**
  - Same as ASCII for 0–127; unused 128–159; same as ANSI and 8859-1 for 160–255; then continues from 256 to **10 000+** characters.
  - `<meta charset="UTF-8">`

<a id="html-charsets-example-01"></a>

### **Example 1: Declare UTF-8, then put Unicode in the file**

- [x] This example runs the tested markup in `code_sandbox/html-charsets/index.html`.

Sandbox: `code_sandbox/html-charsets/index.html`

```html
<meta charset="UTF-8" />
```

<img alt="html-charsets source" src="../code_sandbox/snaps/html-charsets-code.png" />

- [x] **Outcome:** the page demonstrates **Declare UTF-8, then put Unicode in the file** as shown in the result snap.

<a id="html-charsets-example-02"></a>

### **Example 2: Sandbox body**

- [x] This example runs the tested markup in `code_sandbox/html-charsets/html-charsets/index.html`.

Sandbox: `code_sandbox/html-charsets/html-charsets/index.html`

```html
<p>Basic Latin: ABCD abcd 0123 ?#$%</p>
<p>Latin Extended: Ā Ć Ē</p>
<p>Punctuation: ‰ ‼ ⁇</p>
<p>Diacritics: à á â ã</p>
```

<img alt="html-charsets result" src="../code_sandbox/snaps/html-charsets-result.png" />

- [x] **Outcome:** the browser shows **Basic Latin: ABCD abcd 0123 ?#$%**, **Latin Extended: Ā Ć Ē**, **Punctuation: ‰ ‼ ⁇**, **Diacritics: à á â ã**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-charsets/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you tell the browser the character set?

<details>
<summary>Answer</summary>

- [x] `<meta charset="UTF-8">` (or another set name).

</details>

### Question 2: Which character set does the HTML spec encourage?

<details>
<summary>Answer</summary>

- [x] **UTF-8**.

</details>

### Question 3: How many characters did ASCII define?

<details>
<summary>Answer</summary>

- [x] **128** Latin characters.

</details>

### Question 4: What was the default character set for HTML 4?

<details>
<summary>Answer</summary>

- [x] **ISO-8859-1**.

</details>

### Question 5: How did HTML 4 vs HTML 5 declare ISO-8859-1?

<details>
<summary>Answer</summary>

- [x] HTML 4: `<meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1">`.
- [x] HTML 5: `<meta charset="ISO-8859-1">`.

</details>

### Question 6: How does UTF-8 relate to ASCII?

<details>
<summary>Answer</summary>

- [x] Identical to ASCII for values **0–127**.
- [x] Then it continues from 256 to thousands more characters.

</details>

</details>

## Summary

Put `<meta charset="UTF-8">` in the head. ASCII, ANSI, and ISO-8859-1 cover a small Latin range; UTF-8 includes those values and almost every other character.

## References

- [HTML Encoding / Charsets (W3Schools)](https://www.w3schools.com/html/html_charset.asp)
- [Full UTF-8 Reference](https://www.w3schools.com/charsets/ref_html_utf8.asp)
- [HTML Character Sets](https://www.w3schools.com/charsets/default.asp)
- [MDN: `<meta>` charset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#charset)
- [WHATWG: Encoding](https://html.spec.whatwg.org/multipage/semantics.html#character-encoding-declaration)
