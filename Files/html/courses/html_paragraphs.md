# HTML Paragraphs

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

A **paragraph** (`<p>`) is a block of text that **starts on a new line**. Browsers add **margin** around it. Extra spaces and line breaks in the source **collapse**. Use `<hr>` for a thematic break, `<br>` for a line break inside a paragraph, and `<pre>` when you must keep the source layout (poems, code).

This section has **6** examples:

- [x] **Example 1:** Two paragraphs [View](#html-paragraphs-example-01)
- [x] **Example 2:** Collapsed whitespace [View](#html-paragraphs-example-02)
- [x] **Example 3:** Horizontal rules [View](#html-paragraphs-example-03)
- [x] **Example 4:** Line breaks [View](#html-paragraphs-example-04)
- [x] **Example 5:** Poem in `<p>` [View](#html-paragraphs-example-05)
- [x] **Example 6:** Poem in `<pre>` [View](#html-paragraphs-example-06)

## Detailed Explanation

<a id="html-paragraphs-example-01"></a>

### **Example 1: Two paragraphs**

- [x] **HTML paragraphs**
  - `<p>` defines a paragraph.
  - A paragraph always starts on a **new line**.
  - Browsers add **white space (margin)** before and after it.

Sandbox: `code_sandbox/html-paragraphs/index.html`

```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```

<img alt="html-paragraphs source" src="../code_sandbox/snaps/html-paragraphs-code.png" />

<img alt="html-paragraphs result" src="../code_sandbox/snaps/html-paragraphs-result.png" />

- [x] **Outcome:** the browser shows **This is a paragraph.**, **This is another paragraph.**.

<a id="html-paragraphs-example-02"></a>

### **Example 2: Collapsed whitespace**

- [x] **HTML display (whitespace)**
  - You cannot be sure how HTML will look: screen size and window size change the wrap.
  - Extra **spaces** or **lines** in the source do **not** change the display.
  - The browser **removes extra spaces and lines**; many spaces or newlines count as **one space**.

Sandbox: `code_sandbox/html-paragraphs/display.html`

```html
<p>
  This paragraph contains a lot of lines in the source code, but the browser
  ignores it.
</p>
```

<img alt="html-paragraphs whitespace source" src="../code_sandbox/snaps/html-paragraphs-01-code.png" />

<img alt="html-paragraphs whitespace result" src="../code_sandbox/snaps/html-paragraphs-01-result.png" />

- [x] **Outcome:** the browser shows **This paragraph contains a lot of lines in the source code, but the browser ignores it.**.

<a id="html-paragraphs-example-03"></a>

### **Example 3: Horizontal rules**

- [x] **HTML horizontal rules**
  - `<hr>` is a **thematic break**, usually shown as a horizontal line.
  - Use it to **separate** content or mark a change.
  - `<hr>` is **empty** (no end tag).

Sandbox: `code_sandbox/html-paragraphs/hr.html`

```html
<h1>This is heading 1</h1>
<p>This is some text.</p>
<hr />
<h2>This is heading 2</h2>
<p>This is some other text.</p>
<hr />
```

<img alt="html-paragraphs hr source" src="../code_sandbox/snaps/html-paragraphs-02-code.png" />

<img alt="html-paragraphs hr result" src="../code_sandbox/snaps/html-paragraphs-02-result.png" />

- [x] **Outcome:** the browser shows **This is heading 1**, **This is some text.**, **This is heading 2**, **This is some other text.**.

<a id="html-paragraphs-example-04"></a>

### **Example 4: Line breaks**

- [x] **HTML line breaks**
  - `<br>` starts a **new line** without a new paragraph.
  - `<br>` is **empty** (no end tag).

Sandbox: `code_sandbox/html-paragraphs/br.html`

```html
<p>This is<br />a paragraph<br />with line breaks.</p>
```

<img alt="html-paragraphs br source" src="../code_sandbox/snaps/html-paragraphs-03-code.png" />

<img alt="html-paragraphs br result" src="../code_sandbox/snaps/html-paragraphs-03-result.png" />

- [x] **Outcome:** the browser shows **This is a paragraph with line breaks.**.

<a id="html-paragraphs-example-05"></a>

### **Example 5: Poem in `<p>`**

- [x] **The poem problem**
  - A poem in `<p>` with blank lines in the source still **renders on one flow** (one paragraph).

Sandbox: `code_sandbox/html-paragraphs/poem.html`

```html
<p>
  My Bonnie lies over the ocean. My Bonnie lies over the sea. My Bonnie lies
  over the ocean. Oh, bring back my Bonnie to me.
</p>
```

<img alt="html-paragraphs poem source" src="../code_sandbox/snaps/html-paragraphs-04-code.png" />

<img alt="html-paragraphs poem-in-p result" src="../code_sandbox/snaps/html-paragraphs-04-result.png" />

- [x] **Outcome:** the browser shows **My Bonnie lies over the ocean. My Bonnie lies over the sea. My Bonnie lies over the ocean. Oh, bring back my Bonnie to me.**.

<a id="html-paragraphs-example-06"></a>

### **Example 6: Poem in `<pre>`**

- [x] **Solution: `<pre>`**
  - `<pre>` is **preformatted** text: spaces and line breaks in the source are **kept**.
  - Browsers typically show it in a **monospace** font.

Sandbox: `code_sandbox/html-paragraphs/pre.html`

```html
<pre>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.

  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</pre>
```

<img alt="html-paragraphs pre source" src="../code_sandbox/snaps/html-paragraphs-05-code.png" />

<img alt="html-paragraphs pre result" src="../code_sandbox/snaps/html-paragraphs-05-result.png" />

- [x] **Outcome:** the browser shows **My Bonnie lies over the ocean. My Bonnie lies over the sea. My Bonnie lies over the ocean. Oh, bring back my Bonnie to me.**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-paragraphs/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `<p>` define, and where does it start?

<details>
<summary>Answer</summary>

- [x] A **paragraph**.
- [x] It always starts on a **new line**.
- [x] Browsers add **margin** before and after it.

</details>

### Question 2: Do extra spaces and blank lines in the HTML source show on the page?

<details>
<summary>Answer</summary>

- [x] **No.** The browser **collapses** extra spaces and lines.
- [x] Many spaces or newlines count as **one space**.

</details>

### Question 3: What is `<hr>` for?

<details>
<summary>Answer</summary>

- [x] A **thematic break**, usually a **horizontal rule**.
- [x] It **separates** content (or marks a change).
- [x] It is an **empty** tag (no end tag).

</details>

### Question 4: When do you use `<br>` instead of a new `<p>`?

<details>
<summary>Answer</summary>

- [x] When you want a **new line** without starting a **new paragraph**.
- [x] `<br>` is **empty** (no end tag).

</details>

### Question 5: Why does a poem in `<p>` appear as one block?

<details>
<summary>Answer</summary>

- [x] `<p>` **ignores** extra line breaks in the source.
- [x] The lines collapse into **one paragraph**.

</details>

### Question 6: How do you keep a poem’s line breaks?

<details>
<summary>Answer</summary>

- [x] Use the `<pre>` element (**preformatted** text).
- [x] Spaces and line breaks in the source are **preserved**.

</details>

### Question 7: Can you control wrapping by adding spaces in the HTML file?

<details>
<summary>Answer</summary>

- [x] **No.** Screen size and window size change the wrap.
- [x] Extra spaces in the source do **not** control the layout.

</details>

</details>

## Summary

`<p>` starts a new paragraph with automatic **margin**. Extra source **spaces/newlines collapse**. `<hr>` is an empty **thematic break**; `<br>` is an empty **line break**. A poem in `<p>` becomes one flow; `<pre>` keeps the layout.

## References

- [HTML Paragraphs (W3Schools)](https://www.w3schools.com/html/html_paragraphs.asp)
- [Try it Yourself: tryhtml_paragraphs1](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_paragraphs1)
- [Try it Yourself: tryhtml_paragraphs2](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_paragraphs2)
- [Try it Yourself: tryhtml_headings_hr](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_headings_hr)
- [Try it Yourself: tryhtml_paragraphs](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_paragraphs)
- [Try it Yourself: tryhtml_poem](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_poem)
- [Try it Yourself: tryhtml_pre](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_pre)
- [MDN: `<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)
- [MDN: `<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
- [MDN: `<hr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
- [MDN: `<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)
