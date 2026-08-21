# HTML Block & Inline

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

Every HTML element has a default **display** value. The two most common are **block** and **inline**. This chapter compares those display types, lists the tags in each group, and shows **`<div>`** (block container) and **`<span>`** (inline container) with CSS.

This section has **4** examples:

- [x] **Example 1:** Block `<p>` and `<div>` [View](#html-block-inline-example-01)
- [x] **Example 2:** Inline `<span>` [View](#html-block-inline-example-02)
- [x] **Example 3:** Styled `<div>` [View](#html-block-inline-example-03)
- [x] **Example 4:** Styled `<span>` [View](#html-block-inline-example-04)

## Detailed Explanation

- [x] **Default display**
  - The browser assigns a default `display` depending on the element type.
  - The two most common values: **block** and **inline**.
- [x] **Block-level tags listed on the page**
  - `<address>` `<article>` `<aside>` `<blockquote>` `<canvas>` `<dd>` `<div>` `<dl>` `<dt>` `<fieldset>` `<figcaption>` `<figure>` `<footer>` `<form>` `<h1>`–`<h6>` `<header>` `<hr>` `<li>` `<main>` `<nav>` `<noscript>` `<ol>` `<p>` `<pre>` `<section>` `<table>` `<tfoot>` `<ul>` `<video>`
- [x] **Inline tags listed on the page**
  - `<a>` `<abbr>` `<acronym>` `<b>` `<bdo>` `<big>` `<br>` `<button>` `<cite>` `<code>` `<dfn>` `<em>` `<i>` `<img>` `<input>` `<kbd>` `<label>` `<map>` `<object>` `<output>` `<q>` `<samp>` `<script>` `<select>` `<small>` `<span>` `<strong>` `<sub>` `<sup>` `<textarea>` `<time>` `<tt>` `<var>`
  - HTML5 treats **`<acronym>`**, **`<big>`**, and **`<tt>`** as obsolete (use `<abbr>`, CSS `font-size`, and `<code>` / `<kbd>` / `<samp>` instead). The other tags on the list remain valid.
- [x] **Chapter summary from the page**
  - Block: new line + full width.
  - Inline: same line + width as needed.
  - `<div>` is a block container; `<span>` is an inline container.

| Tag      | Description                                   |
| -------- | --------------------------------------------- |
| `<div>`  | Defines a section in a document (block-level) |
| `<span>` | Defines a section in a document (inline)      |

<a id="html-block-inline-example-01"></a>

### **Example 1: Block `<p>` and `<div>`**

- [x] **Block-level elements**
  - Always **start on a new line**.
  - Browsers add some **margin** before and after.
  - Take up the **full width** available (stretch left to right).
  - Two common examples: `<p>` (paragraph) and `<div>` (division / section).

Sandbox: `code_sandbox/html-block-inline/index.html`

```html
<p>Hello World</p>
<div>Hello World</div>
```

<img alt="html-block-inline p and div source" src="../code_sandbox/snaps/html-block-inline-code.png" />

<img alt="html-block-inline p and div result" src="../code_sandbox/snaps/html-block-inline-result.png" />

- [x] **Outcome:** the browser shows **Hello World**, **Hello World**.

<a id="html-block-inline-example-02"></a>

### **Example 2: Inline `<span>`**

- [x] **Inline elements**
  - Do **not** start on a new line.
  - Take up only as much **width as necessary**.
  - Example: a `<span>` by itself sits on one line.
  - **Note:** an inline element **cannot contain** a block-level element.
  - Sandbox: `span.html`.

Sandbox: `code_sandbox/html-block-inline/span.html`

```html
<span>Hello World</span>
```

<img alt="html-block-inline span source" src="../code_sandbox/snaps/html-block-inline-01-code.png" />

<img alt="html-block-inline span result" src="../code_sandbox/snaps/html-block-inline-01-result.png" />

- [x] **Outcome:** the browser shows **Hello World**.

<a id="html-block-inline-example-03"></a>

### **Example 3: Styled `<div>`**

- [x] **The `<div>` element**
  - A **block-level** container for other HTML elements.
  - No required attributes; **`style`**, **`class`**, and **`id`** are common.
  - With CSS it can style a **block of content** (example: black background, white text, padding, heading **London** plus a paragraph).
  - Sandbox: `div.html`. More on `<div>` in the next chapter.

Sandbox: `code_sandbox/html-block-inline/div.html`

```html
<div style="background-color:black;color:white;padding:20px;">
  <h2>London</h2>
  <p>
    London is the capital city of England. It is the most populous city in the
    United Kingdom, with a metropolitan area of over 13 million inhabitants.
  </p>
</div>
```

<img alt="html-block-inline styled div source" src="../code_sandbox/snaps/html-block-inline-02-code.png" />

<img alt="html-block-inline styled div result" src="../code_sandbox/snaps/html-block-inline-02-result.png" />

- [x] **Outcome:** the browser shows **London**, **London is the capital city of England. It is the most populous city in the United Kingdom, with a metropolitan area of over 13 million inhabitants.**.

<a id="html-block-inline-example-04"></a>

### **Example 4: Styled `<span>`**

- [x] **The `<span>` element**
  - An **inline** container for a part of text or a part of a document.
  - No required attributes; **`style`**, **`class`**, and **`id`** are common.
  - With CSS it can style **parts of the text** (example: **blue** and **dark green** eye colors).
  - Sandbox: `span-style.html`.

Sandbox: `code_sandbox/html-block-inline/span-style.html`

```html
<p>
  My mother has <span style="color:blue;font-weight:bold;">blue</span> eyes and
  my father has
  <span style="color:darkolivegreen;font-weight:bold;">dark green</span> eyes.
</p>
```

<img alt="html-block-inline styled span source" src="../code_sandbox/snaps/html-block-inline-03-code.png" />

<img alt="html-block-inline styled span result" src="../code_sandbox/snaps/html-block-inline-03-result.png" />

- [x] **Outcome:** the browser shows **My mother has blue eyes and my father has dark green eyes.**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-block-inline/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are the two most common default display values?

<details>
<summary>Answer</summary>

- [x] **Block**.
- [x] **Inline**.

</details>

### Question 2: How does a block-level element lay out?

<details>
<summary>Answer</summary>

- [x] It **starts on a new line**.
- [x] The browser adds **margin** before and after.
- [x] It takes the **full width** available.

</details>

### Question 3: Which two common tags are block-level in this chapter?

<details>
<summary>Answer</summary>

- [x] **`<p>`** (paragraph).
- [x] **`<div>`** (division / section).

</details>

### Question 4: How does an inline element lay out?

<details>
<summary>Answer</summary>

- [x] It does **not** start on a new line.
- [x] It takes only as much **width as necessary**.

</details>

### Question 5: Can an inline element contain a block-level element?

<details>
<summary>Answer</summary>

- [x] **No.**

</details>

### Question 6: What is `<div>` used for, and which attributes are common?

<details>
<summary>Answer</summary>

- [x] A **block-level container** for other HTML elements.
- [x] Common attributes: **`style`**, **`class`**, **`id`**.

</details>

### Question 7: What is `<span>` used for?

<details>
<summary>Answer</summary>

- [x] An **inline container** for a part of text or a part of a document.
- [x] With CSS it styles **parts of the text**.

</details>

### Question 8: Which listed inline tags are obsolete in HTML5?

<details>
<summary>Answer</summary>

- [x] **`<acronym>`** — use **`<abbr>`**.
- [x] **`<big>`** — use CSS **`font-size`**.
- [x] **`<tt>`** — use **`<code>`**, **`<kbd>`**, or **`<samp>`**.

</details>

</details>

## Summary

Block elements start on a new line and fill the available width (`<p>`, `<div>`, headings, lists, tables). Inline elements stay in the line and shrink to their content (`<span>`, `<a>`, `<img>`). `<div>` is the generic block container; `<span>` is the generic inline container. Do not nest a block inside an inline element.

## References

- [HTML Block and Inline Elements (W3Schools)](https://www.w3schools.com/html/html_blocks.asp)
- [Try it Yourself: tryhtml_block_div](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_block_div)
- [Try it Yourself: tryhtml_inline_span](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_inline_span)
- [Try it Yourself: tryhtml_div](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_div)
- [Try it Yourself: tryhtml_span](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_span)
- [HTML Tag Reference](https://www.w3schools.com/tags/default.asp)
- [MDN: Block-level elements](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)
- [MDN: Inline elements](https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content)
- [MDN: `<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
- [MDN: `<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span)
