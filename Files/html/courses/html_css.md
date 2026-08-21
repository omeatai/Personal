# HTML CSS

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

**CSS** (Cascading Style Sheets) formats the layout of a webpage: color, font, size, spacing, position, backgrounds, and different displays for different devices. You can add CSS in **three** ways: **inline**, **internal**, and **external**. Cascading means a style on a parent also applies to children unless you override it.

This section has **8** examples:

- [x] **Example 1:** Inline [View](#html-css-example-01)
- [x] **Example 2:** Internal [View](#html-css-example-02)
- [x] **Example 3:** External HTML [View](#html-css-example-03)
- [x] **Example 4:** `styles.css` [View](#html-css-example-04)
- [x] **Example 5:** Fonts [View](#html-css-example-05)
- [x] **Example 6:** Border [View](#html-css-example-06)
- [x] **Example 7:** Padding [View](#html-css-example-07)
- [x] **Example 8:** Margin [View](#html-css-example-08)

## Detailed Explanation

- [x] **What is CSS?**
  - Cascading Style Sheets.
  - Saves work: one sheet can control **many** pages.
  - Formats layout: color, font, text size, spacing, positioning, backgrounds, responsive displays.
- [x] **Three ways to add CSS**
  - **Inline** — `style` attribute on one element.
  - **Internal** — `<style>` in the page `<head>`.
  - **External** — `<link rel="stylesheet" href="…">` to a `.css` file.
  - External files are the usual way for a site. This chapter uses inline and internal a lot because they are easier to try.
- [x] **Linking to an external sheet (paths)**
  - Full URL: `href="https://www.w3schools.com/html/styles.css"`.
  - Site path: `href="/html/styles.css"`.
  - Same folder: `href="styles.css"`.
  - File paths are covered later in **HTML File Paths**.
- [x] **Cascade tip**
  - A style on a parent applies to children. If `body` text is blue, headings and paragraphs inherit it unless you set something else.
- [x] **HTML style tags**

| Tag       | Description                                        |
| --------- | -------------------------------------------------- |
| `<style>` | Style information for an HTML document             |
| `<link>`  | A link between a document and an external resource |

<a id="html-css-example-01"></a>

### **Example 1: Inline**

- [x] **Inline CSS**
  - Unique style on a **single** element.
  - Example: blue `<h1>`, red `<p>`.

Sandbox: `code_sandbox/html-css/index.html`

```html
<h1 style="color:blue;">A Blue Heading</h1>

<p style="color:red;">A red paragraph.</p>
```

<img alt="html-css inline source" src="../code_sandbox/snaps/html-css-code.png" />

<img alt="html-css inline result" src="../code_sandbox/snaps/html-css-result.png" />

- [x] **Outcome:** the browser shows **A Blue Heading**, **A red paragraph.**.

<a id="html-css-example-02"></a>

### **Example 2: Internal**

- [x] **Internal CSS**
  - Style for a **single page**, inside `<style>` in `<head>`.
  - Example: powderblue `body`, blue headings, red paragraphs (all `h1` / `p` on that page).

Sandbox: `code_sandbox/html-css/internal.html`

```html
<head>
  <style>
    body {
      background-color: powderblue;
    }
    h1 {
      color: blue;
    }
    p {
      color: red;
    }
  </style>
</head>
<body>
  <h1>This is a heading</h1>
  <p>This is a paragraph.</p>
</body>
```

<img alt="html-css internal source" src="../code_sandbox/snaps/html-css-01-code.png" />

<img alt="html-css internal result" src="../code_sandbox/snaps/html-css-01-result.png" />

- [x] **Outcome:** the browser shows **body { background-color: powderblue; } h1 { color: blue; } p { color: red; } This is a heading**, **This is a paragraph.**.

<a id="html-css-example-03"></a>

### **Example 3: External HTML**

- [x] **External CSS**
  - One sheet for **many** pages.
  - Link it from each page’s `<head>`: `<link rel="stylesheet" href="styles.css">`.
  - The `.css` file is plain CSS only (no HTML).
  - Changing that one file can restyle a whole site.

Sandbox: `code_sandbox/html-css/external.html`

```html
<head>
  <link rel="stylesheet" href="styles.css" />
</head>
```

<img alt="html-css external source" src="../code_sandbox/snaps/html-css-02-code.png" />

<img alt="html-css styles.css source" src="../code_sandbox/snaps/html-css-03-code.png" />

- [x] **Outcome:** the page demonstrates **External HTML** as shown in the result snap.

<a id="html-css-example-04"></a>

### **Example 4: `styles.css`**

- [x] This example runs the tested markup.

```css
body {
  background-color: powderblue;
}
h1 {
  color: blue;
}
p {
  color: red;
}
```

<img alt="html-css styles.css source" src="../code_sandbox/snaps/html-css-03-code.png" />

<img alt="html-css external result" src="../code_sandbox/snaps/html-css-02-result.png" />

- [x] **Outcome:** the browser shows **body { background-color: powderblue; } h1 { color: blue; } p { color: red; }**.

<a id="html-css-example-05"></a>

### **Example 5: Fonts**

- [x] **CSS colors, fonts, and sizes**
  - `color` — text color.
  - `font-family` — font (verdana heading, courier paragraph).
  - `font-size` — size (`300%` / `160%` in the example).

Sandbox: `code_sandbox/html-css/fonts.html`

```css
h1 {
  color: blue;
  font-family: verdana;
  font-size: 300%;
}
p {
  color: red;
  font-family: courier;
  font-size: 160%;
}
```

<img alt="html-css fonts source" src="../code_sandbox/snaps/html-css-04-code.png" />

<img alt="html-css fonts result" src="../code_sandbox/snaps/html-css-03-result.png" />

- [x] **Outcome:** the browser shows **h1 { color: blue; font-family: verdana; font-size: 300%; } p { color: red; font-family: courier; font-size: 160%; }**.

<a id="html-css-example-06"></a>

### **Example 6: Border**

- [x] **Border, padding, and margin**
  - `border` — a border around an element (almost any element).
  - `padding` — space **inside** the border (text to border).
  - `margin` — space **outside** the border.
  - Sandbox: `border.html`, `padding.html`, `margin.html`.

Sandbox: `code_sandbox/html-css/border.html`

```css
p {
  border: 2px solid powderblue;
}
```

<img alt="html-css border source" src="../code_sandbox/snaps/html-css-05-code.png" />

<img alt="html-css border result" src="../code_sandbox/snaps/html-css-04-result.png" />

- [x] **Outcome:** the browser shows **p { border: 2px solid powderblue; }**.

<a id="html-css-example-07"></a>

### **Example 7: Padding**

- [x] **Border, padding, and margin**
  - `border` — a border around an element (almost any element).
  - `padding` — space **inside** the border (text to border).
  - `margin` — space **outside** the border.
  - Sandbox: `border.html`, `padding.html`, `margin.html`.

Sandbox: `code_sandbox/html-css/padding.html`

```css
p {
  border: 2px solid powderblue;
  padding: 30px;
}
```

<img alt="html-css padding source" src="../code_sandbox/snaps/html-css-06-code.png" />

<img alt="html-css padding result" src="../code_sandbox/snaps/html-css-05-result.png" />

- [x] **Outcome:** the browser shows **p { border: 2px solid powderblue; padding: 30px; }**.

<a id="html-css-example-08"></a>

### **Example 8: Margin**

- [x] **Border, padding, and margin**
  - `border` — a border around an element (almost any element).
  - `padding` — space **inside** the border (text to border).
  - `margin` — space **outside** the border.
  - Sandbox: `border.html`, `padding.html`, `margin.html`.

Sandbox: `code_sandbox/html-css/margin.html`

```css
p {
  border: 2px solid powderblue;
  margin: 50px;
}
```

<img alt="html-css margin source" src="../code_sandbox/snaps/html-css-07-code.png" />

<img alt="html-css margin result" src="../code_sandbox/snaps/html-css-06-result.png" />

- [x] **Outcome:** the browser shows **p { border: 2px solid powderblue; margin: 50px; }**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-css/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does CSS stand for, and what is it for?

<details>
<summary>Answer</summary>

- [x] **Cascading Style Sheets**.
- [x] It formats the **layout** of a webpage (color, font, size, spacing, position, backgrounds, devices).

</details>

### Question 2: What are the three ways to add CSS to HTML?

<details>
<summary>Answer</summary>

- [x] **Inline** — `style` attribute.
- [x] **Internal** — `<style>` in `<head>`.
- [x] **External** — `<link>` to a `.css` file.

</details>

### Question 3: What does “cascading” mean here?

<details>
<summary>Answer</summary>

- [x] A style on a **parent** also applies to **children**.
- [x] You can still override it on a child.

</details>

### Question 4: When do you use inline CSS?

<details>
<summary>Answer</summary>

- [x] For a **unique** style on a **single** HTML element.
- [x] It uses the **`style`** attribute.

</details>

### Question 5: Where does internal CSS go?

<details>
<summary>Answer</summary>

- [x] In the **`<head>`**, inside a **`<style>`** element.
- [x] It styles **that page** (for example all `h1` and `p` elements).

</details>

### Question 6: How do you attach an external style sheet?

<details>
<summary>Answer</summary>

- [x] `<link rel="stylesheet" href="styles.css">` in `<head>`.
- [x] The file must be **CSS only** and end with **`.css`**.
- [x] One file can change the look of a **whole site**.

</details>

### Question 7: Which properties set text color, font, and size?

<details>
<summary>Answer</summary>

- [x] `color`
- [x] `font-family`
- [x] `font-size`

</details>

### Question 8: What is the difference between padding and margin?

<details>
<summary>Answer</summary>

- [x] **Padding** is space **inside** the border (text to border).
- [x] **Margin** is space **outside** the border.

</details>

### Question 9: Which tags belong in `<head>` for CSS?

<details>
<summary>Answer</summary>

- [x] `<style>` for internal CSS.
- [x] `<link>` for an external sheet.

</details>

### Question 10: How can you point `href` at an external sheet?

<details>
<summary>Answer</summary>

- [x] A **full URL**.
- [x] A **path** on the site (for example `/html/styles.css`).
- [x] A **same-folder** filename (`styles.css`).

</details>

</details>

## Summary

Add CSS inline (`style`), internally (`<style>` in `<head>`), or externally (`<link>` to a `.css` file). External sheets scale to a whole site. Use `color`, `font-family`, and `font-size` for text; `border`, `padding` (inside), and `margin` (outside) for boxes. Styles cascade from parent to child unless overridden.

## References

- [HTML Styles CSS (W3Schools)](https://www.w3schools.com/html/html_css.asp)
- [Try it Yourself: tryhtml_css_inline](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_css_inline)
- [Try it Yourself: tryhtml_css_internal](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_css_internal)
- [Try it Yourself: tryhtml_css_external](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_css_external)
- [Try it Yourself: tryhtml_css_fonts](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_css_fonts)
- [Try it Yourself: tryhtml_css_borders](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_css_borders)
- [Try it Yourself: tryhtml_css_padding](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_css_padding)
- [Try it Yourself: tryhtml_css_margin](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_css_margin)
- [Try it Yourself: tryhtml_css_external_url](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_css_external_url)
- [CSS Tutorial (W3Schools)](https://www.w3schools.com/css/default.asp)
- [MDN: Getting started with CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Getting_started)
- [MDN: `<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style)
- [MDN: `<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)
