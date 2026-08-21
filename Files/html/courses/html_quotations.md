# HTML Quotations

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

This chapter covers **quotation and citation** elements: `<blockquote>`, `<q>`, `<abbr>`, `<address>`, `<cite>`, and `<bdo>`. They mark quotes, abbreviations, contact info, work titles, and text direction.

This section has **6** examples:

- [x] **Example 1:** Intro / blockquote [View](#html-quotations-example-01)
- [x] **Example 2:** Short quotation [View](#html-quotations-example-02)
- [x] **Example 3:** Abbreviation [View](#html-quotations-example-03)
- [x] **Example 4:** Address [View](#html-quotations-example-04)
- [x] **Example 5:** Cite [View](#html-quotations-example-05)
- [x] **Example 6:** Bi-directional override [View](#html-quotations-example-06)

## Detailed Explanation

<a id="html-quotations-example-01"></a>

### **Example 1: Intro / blockquote**

- [x] **`<blockquote>` for quotations**
  - Defines a section **quoted from another source**.
  - Browsers usually **indent** it.
  - Optional `cite` URL (here WWF).

Sandbox: `code_sandbox/html-quotations/index.html`

```html
<p>Here is a quote from WWF's website:</p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">
  For 60 years, WWF has worked to help people and nature thrive. As the world's
  leading conservation organization, WWF works in nearly 100 countries. At every
  level, we collaborate with people around the world to develop and deliver
  innovative solutions that protect communities, wildlife, and the places in
  which they live.
</blockquote>
```

<img alt="html-quotations intro" src="../code_sandbox/snaps/html-quotations-code.png" />

<img alt="html-quotations blockquote source" src="../code_sandbox/snaps/html-quotations-01-code.png" />

<img alt="html-quotations blockquote result" src="../code_sandbox/snaps/html-quotations-result.png" />

- [x] **Outcome:** the browser shows **Here is a quote from WWF's website:**, **For 60 years, WWF has worked to help people and nature thrive. As the world's leading conservation organization, WWF works in nearly 100 countries. At every level, we collaborate with people around the world to develop and deliver innovative solutions that protect communities, wildlife, and the places in which they live.**.

<a id="html-quotations-example-02"></a>

### **Example 2: Short quotation**

- [x] **`<q>` for short quotations**
  - Defines a **short** quotation.
  - Browsers normally insert **quotation marks**.

Sandbox: `code_sandbox/html-quotations/q.html`

```html
<p>
  <q>Build a future where people live in harmony with nature.</q>
</p>
```

<img alt="html-quotations q source" src="../code_sandbox/snaps/html-quotations-02-code.png" />

<img alt="html-quotations q result" src="../code_sandbox/snaps/html-quotations-02-result.png" />

- [x] **Outcome:** the browser shows **WWF's goal is to: Build a future where people live in harmony with nature.**.

<a id="html-quotations-example-03"></a>

### **Example 3: Abbreviation**

- [x] **`<abbr>` for abbreviations**
  - Defines an **abbreviation or acronym** (HTML, CSS, Mr., Dr., ASAP, ATM).
  - Helps browsers, translation systems, and search engines.
  - Use the global **`title`** attribute so the description shows on **mouse over**.

Sandbox: `code_sandbox/html-quotations/abbr.html`

```html
<p>
  The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.
</p>
```

<img alt="html-quotations abbr source" src="../code_sandbox/snaps/html-quotations-03-code.png" />

<img alt="html-quotations abbr result" src="../code_sandbox/snaps/html-quotations-03-result.png" />

- [x] **Outcome:** the browser shows **The WHO was founded in 1948.**.

<a id="html-quotations-example-04"></a>

### **Example 4: Address**

- [x] **`<address>` for contact information**
  - Contact info for the **author/owner** of a document or article (email, URL, physical address, phone, social handle).
  - Usually **italic**. Browsers add a **line break** before and after.

Sandbox: `code_sandbox/html-quotations/address.html`

```html
<address>
  Written by John Doe.<br />
  Visit us at:<br />
  Example.com<br />
  Box 564, Disneyland<br />
  USA
</address>
```

<img alt="html-quotations address source" src="../code_sandbox/snaps/html-quotations-04-code.png" />

<img alt="html-quotations address result" src="../code_sandbox/snaps/html-quotations-04-result.png" />

- [x] **Outcome:** the browser shows **Written by John Doe. Visit us at: Example.com Box 564, Disneyland USA**.

<a id="html-quotations-example-05"></a>

### **Example 5: Cite**

- [x] **`<cite>` for work title**
  - Title of a **creative work** (book, poem, song, movie, painting, sculpture).
  - A person’s name is **not** the title of a work.
  - Usually **italic**.

Sandbox: `code_sandbox/html-quotations/cite.html`

```html
<p><cite>The Scream</cite> by Edvard Munch. Painted in 1893.</p>
```

<img alt="html-quotations cite source" src="../code_sandbox/snaps/html-quotations-05-code.png" />

<img alt="html-quotations cite result" src="../code_sandbox/snaps/html-quotations-05-result.png" />

- [x] **Outcome:** the browser shows **The Scream by Edvard Munch. Painted in 1893.**.

<a id="html-quotations-example-06"></a>

### **Example 6: Bi-directional override**

- [x] **`<bdo>` for bi-directional override**
  - BDO = **Bi-Directional Override**.
  - Overrides the current **text direction** (`dir="rtl"` in the example).

Sandbox: `code_sandbox/html-quotations/bdo.html`

```html
<bdo dir="rtl">This text will be written from right to left</bdo>
```

<img alt="html-quotations bdo source" src="../code_sandbox/snaps/html-quotations-06-code.png" />

<img alt="html-quotations bdo result" src="../code_sandbox/snaps/html-quotations-06-result.png" />

- [x] **Outcome:** the browser shows **This text will be written from right to left**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-quotations/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `<blockquote>` do, and how do browsers show it?

<details>
<summary>Answer</summary>

- [x] It marks a section **quoted from another source**.
- [x] Browsers usually **indent** it.
- [x] You can add a **`cite`** URL for the source.

</details>

### Question 2: How is `<q>` different from `<blockquote>`?

<details>
<summary>Answer</summary>

- [x] `<q>` is a **short** (inline) quotation.
- [x] Browsers normally add **quotation marks**.

</details>

### Question 3: Why use `<abbr>` with `title`?

<details>
<summary>Answer</summary>

- [x] It marks an **abbreviation or acronym**.
- [x] **`title`** shows the full description on **mouse over**.
- [x] It can help browsers, translation systems, and search engines.

</details>

### Question 4: What belongs in `<address>`?

<details>
<summary>Answer</summary>

- [x] **Contact information** for the author/owner of a document or article.
- [x] Email, URL, physical address, phone, social handle, etc.
- [x] Usually **italic**, with a line break before and after.

</details>

### Question 5: What should `<cite>` wrap?

<details>
<summary>Answer</summary>

- [x] The **title of a creative work**.
- [x] A person’s name is **not** the title of a work.
- [x] Usually rendered in **italic**.

</details>

### Question 6: What does `<bdo dir="rtl">` do?

<details>
<summary>Answer</summary>

- [x] **BDO** means Bi-Directional Override.
- [x] It **overrides** the current text direction (here **right-to-left**).

</details>

### Question 7: Name the six quotation/citation elements from this chapter.

<details>
<summary>Answer</summary>

- [x] `<blockquote>`, `<q>`, `<abbr>`, `<address>`, `<cite>`, `<bdo>`.

</details>

</details>

## Summary

Use `<blockquote>` for a sourced block quote (usually indented), `<q>` for a short quote with marks, `<abbr title="...">` for acronyms, `<address>` for contact info, `<cite>` for a work’s title, and `<bdo>` to override text direction.

## References

- [HTML Quotation Elements (W3Schools)](https://www.w3schools.com/html/html_quotation_elements.asp)
- [Try it Yourself: tryhtml_formatting_intro2](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_intro2)
- [Try it Yourself: tryhtml_formatting_blockquote](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_blockquote)
- [Try it Yourself: tryhtml_formatting_q](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_q)
- [Try it Yourself: tryhtml_formatting_abbr](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_abbr)
- [Try it Yourself: tryhtml_formatting_address](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_address)
- [Try it Yourself: tryhtml_formatting_cite](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_cite)
- [Try it Yourself: tryhtml_formatting_bdo](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_bdo)
- [MDN: `<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
- [MDN: `<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
- [MDN: `<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
- [MDN: `<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
- [MDN: `<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
- [MDN: `<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
