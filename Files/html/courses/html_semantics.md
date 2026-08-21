# HTML Semantics

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

**Semantic** elements have **meaning** for the browser and the developer (`<article>` vs a meaningless `<div>`). This chapter covers `<section>`, `<article>`, `<header>`, `<footer>`, `<nav>`, `<aside>`, and `<figure>`/`<figcaption>`, plus why the semantic web matters.

This section has **5** examples:

- [x] **Example 1:** Section [View](#html-semantics-example-01)
- [x] **Example 2:** Article [View](#html-semantics-example-02)
- [x] **Example 3:** Nav and footer [View](#html-semantics-example-03)
- [x] **Example 4:** Aside [View](#html-semantics-example-04)
- [x] **Example 5:** Figure [View](#html-semantics-example-05)

## Detailed Explanation

- [x] **What are semantic elements?**
  - They **clearly describe** their content.
  - Non-semantic: `<div>`, `<span>` (tell nothing about content).
  - Semantic: `<img>`, `<table>`, `<article>` (define the content).
  - Sites used to fake structure with `<div id="nav">`, `<div class="header">`, `<div id="footer">`. HTML now has real tags for those parts.
- [x] **`<header>`**
  - Introductory content or navigational links: headings, logo, authorship.
  - Several headers per document are OK.
  - **Cannot** nest inside `<footer>`, `<address>`, or another `<header>`.
- [x] **`<footer>`**
  - Authorship, copyright, contact, sitemap, back-to-top, related docs.
  - Several footers per document are OK.
- [x] **Why semantic elements?**
  - W3C: a semantic Web lets data be **shared and reused** across applications, enterprises, and communities.

| Tag            | Description                                   |
| -------------- | --------------------------------------------- |
| `<article>`    | Independent, self-contained content           |
| `<aside>`      | Content aside from the page content           |
| `<details>`    | Extra details the user can view or hide       |
| `<figcaption>` | Caption for a `<figure>`                      |
| `<figure>`     | Self-contained illustration / photo / listing |
| `<footer>`     | Footer for a document or section              |
| `<header>`     | Header for a document or section              |
| `<main>`       | Main content of a document                    |
| `<mark>`       | Marked / highlighted text                     |
| `<nav>`        | Navigation links                              |
| `<section>`    | A section in a document                       |
| `<summary>`    | Visible heading for `<details>`               |
| `<time>`       | A date/time                                   |

<a id="html-semantics-example-01"></a>

### **Example 1: Section**

- [x] **`<section>`**
  - A **thematic grouping**, typically with a heading (W3C).
  - Uses: chapters, introduction, news, contact.
  - Example: two WWF sections.

Sandbox: `code_sandbox/html-semantics/index.html`

```html
<section>
  <h1>WWF</h1>
  <p>...</p>
</section>
```

<img alt="html-semantics section source" src="../code_sandbox/snaps/html-semantics-code.png" />

<img alt="html-semantics section result" src="../code_sandbox/snaps/html-semantics-result.png" />

- [x] **Outcome:** the browser shows **WWF**, **...**.

<a id="html-semantics-example-02"></a>

### **Example 2: Article**

- [x] **`<article>`**
  - Independent, self-contained content you could **distribute alone**.
  - Uses: forum posts, blogs, comments, product cards, newspaper articles.
  - Nested styled browsers example (Chrome, Firefox, Edge).
  - Sandbox: `article.html`.
  - You **cannot** decide nesting from the definitions alone: pages nest `<section>` in `<article>` and the reverse.

Sandbox: `code_sandbox/html-semantics/article.html`

```html
<article class="all-browsers">
  <h1>Most Popular Browsers</h1>
  <article class="browser">...</article>
</article>
```

<img alt="html-semantics article source" src="../code_sandbox/snaps/html-semantics-01-code.png" />

<img alt="html-semantics article result" src="../code_sandbox/snaps/html-semantics-01-result.png" />

- [x] **Outcome:** the browser shows **Most Popular Browsers**, **...**.

<a id="html-semantics-example-03"></a>

### **Example 3: Nav and footer**

- [x] **`<nav>`**
  - **Major** navigation blocks only (not every link).
  - Helps screen readers skip or find nav.
  - Sandbox: `nav-footer.html`.

Sandbox: `code_sandbox/html-semantics/nav-footer.html`

```html
<nav><a href="/html/">HTML</a> | <a href="/css/">CSS</a></nav>
<footer>
  <p>Author: Hege Refsnes</p>
</footer>
```

<img alt="html-semantics nav footer source" src="../code_sandbox/snaps/html-semantics-02-code.png" />

<img alt="html-semantics nav footer result" src="../code_sandbox/snaps/html-semantics-02-result.png" />

- [x] **Outcome:** the browser shows **HTML**, **| CSS**, **Author: Hege Refsnes**.

<a id="html-semantics-example-04"></a>

### **Example 4: Aside**

- [x] **`<aside>`**
  - Sidebar-like content **indirectly related** to the surroundings.
  - Example: Epcot paragraph with a floated gray aside.
  - Sandbox: `aside.html`.

Sandbox: `code_sandbox/html-semantics/aside.html`

```html
<aside>
  <p>The Epcot center is a theme park...</p>
</aside>
```

<img alt="html-semantics aside source" src="../code_sandbox/snaps/html-semantics-03-code.png" />

<img alt="html-semantics aside result" src="../code_sandbox/snaps/html-semantics-03-result.png" />

- [x] **Outcome:** the browser shows **The Epcot center is a theme park...**.

<a id="html-semantics-example-05"></a>

### **Example 5: Figure**

- [x] **`<figure>` and `<figcaption>`**
  - Self-contained illustrations, diagrams, photos, code listings.
  - Caption is first or last child of `<figure>`.
  - Example: Trulli photo, **Fig1. - Trulli, Puglia, Italy.**
  - Sandbox: `figure.html`.

Sandbox: `code_sandbox/html-semantics/figure.html`

```html
<figure>
  <img src="pic_trulli.jpg" alt="Trulli" />
  <figcaption>Fig1. - Trulli, Puglia, Italy.</figcaption>
</figure>
```

<img alt="html-semantics figure source" src="../code_sandbox/snaps/html-semantics-04-code.png" />

<img alt="html-semantics figure result" src="../code_sandbox/snaps/html-semantics-04-result.png" />

- [x] **Outcome:** the browser shows **Fig1. - Trulli, Puglia, Italy.**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-semantics/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What makes an element semantic?

<details>
<summary>Answer</summary>

- [x] It **clearly describes** its meaning to the browser and the developer.
- [x] `<div>`/`<span>` are **non-semantic**.

</details>

### Question 2: How does `<section>` differ from `<article>`?

<details>
<summary>Answer</summary>

- [x] `<section>` — thematic grouping, typically with a **heading**.
- [x] `<article>` — **independent** content you could publish alone.
- [x] Either may nest inside the other.

</details>

### Question 3: What belongs in `<nav>` vs ordinary links?

<details>
<summary>Answer</summary>

- [x] **Major** navigation blocks only.
- [x] Not every link on the page.

</details>

### Question 4: Where can you **not** put `<header>`?

<details>
<summary>Answer</summary>

- [x] Not inside `<footer>`, `<address>`, or another `<header>`.

</details>

### Question 5: What are `<figure>` and `<figcaption>` for?

<details>
<summary>Answer</summary>

- [x] `<figure>` — self-contained illustration, photo, diagram, or listing.
- [x] `<figcaption>` — caption as the first or last child.

</details>

</details>

## Summary

Prefer semantic tags over anonymous divs. `<section>` groups themes; `<article>` is standalone; `<header>`/`<footer>`/`<nav>`/`<aside>` mark page regions; `<figure>` captions media. Semantics help people, tools, and reuse of data.

## References

- [HTML Semantic Elements (W3Schools)](https://www.w3schools.com/html/html5_semantic_elements.asp)
- [Try it Yourself: tryhtml5_section](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_section)
- [Try it Yourself: tryhtml5_article](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_article)
- [Try it Yourself: tryhtml5_article2](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_article2)
- [Try it Yourself: tryhtml5_header](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_header)
- [Try it Yourself: tryhtml5_footer](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_footer)
- [Try it Yourself: tryhtml5_nav](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_nav)
- [Try it Yourself: tryhtml5_aside](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_aside)
- [Try it Yourself: tryhtml5_aside2](https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_aside2)
- [Try it Yourself: tryhtml_figcaption](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_figcaption)
- [MDN: Semantics](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)
