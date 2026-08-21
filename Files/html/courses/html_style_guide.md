# HTML Style Guide

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

**Consistent, clean, tidy** HTML is easier for others to read. This chapter is W3Schools’ **coding conventions**: doctype, lowercase names, quoted attributes, titles, `lang`, charset, viewport, comments, CSS/JS loading, and **lowercase file names**.

This section has **1** example:

- [x] **Example 1:** Good document [View](#html-style-guide-example-01)

## Detailed Explanation

- [x] **Always declare document type** first: `<!DOCTYPE html>`.
- [x] **Lowercase element names** (mixing case looks bad; lowercase is cleaner and easier to type).
- [x] **Close all elements** even when optional (`<p>...</p>`).
- [x] **Lowercase attribute names**; **always quote** values (required if the value has spaces). `class=table striped` is invalid.
- [x] **Images:** always `alt`, plus **width and height** (or CSS size) so the browser can reserve space and reduce flicker.
- [x] **No spaces around `=`** (`rel="stylesheet"` not `rel = "stylesheet"`).
- [x] **Avoid long lines**; indent with **two spaces**, not Tab; blank lines only to separate logical blocks.
- [x] **Never skip `<title>`** (required; SEO; tab; favorites). Example title: **HTML Style Guide and Coding Conventions**.
- [x] Pages can **validate without** `<html>`/`<body>`/`<head>`, but **always include them**. Omitting `<body>` can break older browsers; omitting html/body can crash DOM/XML tools.
- [x] Empty elements: `<meta charset="utf-8">` or with a trailing slash. Keep `/` if XML/XHTML software will read the page.
- [x] Always **`lang`** on `<html>` (search engines and browsers). Example: `lang="en-us"`.
- [x] Put **`lang` and `charset` as early as possible**. Include the **viewport** meta on every page.
- [x] Comments: one line `<!-- ... -->`; long comments indented two spaces inside a block comment.
- [x] Style sheets: `<link rel="stylesheet" href="styles.css">` (`type` not needed). Short CSS can be one line; long rules: `{` on the same line as the selector, two-space indent, semicolon including the last property, quotes only if the value has spaces.
- [x] Scripts: `<script src="myscript.js">` (`type` not needed). Untidy HTML can cause JS errors: `Demo` vs `demo` are **different** ids.
- [x] **Lowercase file names** (Apache/Unix are case-sensitive; IIS is not). Extensions: `.html`/`.htm`, `.css`, `.js`. `.htm` and `.html` are the same to browsers. Default filenames: `index.html`, `index.htm`, `default.html`, `default.htm` depending on the server.

<a id="html-style-guide-example-01"></a>

### **Example 1: Good document**

- [x] This example runs the tested markup in `code_sandbox/html-style-guide/index.html`.

Sandbox: `code_sandbox/html-style-guide/index.html`

```html
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="UTF-8" />
    <title>HTML Style Guide and Coding Conventions</title>
  </head>
  <body>
    <h1>Famous Cities</h1>
    ...
  </body>
</html>
```

<img alt="html-style-guide source" src="../code_sandbox/snaps/html-style-guide-code.png" />

<img alt="html-style-guide result" src="../code_sandbox/snaps/html-style-guide-result.png" />

- [x] **Outcome:** the browser shows **HTML Style Guide and Coding Conventions Famous Cities**, **...**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-style-guide/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What should be the first line of an HTML file?

<details>
<summary>Answer</summary>

- [x] `<!DOCTYPE html>`.

</details>

### Question 2: Should you close optional tags like `<p>`?

<details>
<summary>Answer</summary>

- [x] **Yes.** Strongly recommended to close **all** elements.

</details>

### Question 3: When must attribute values be quoted?

<details>
<summary>Answer</summary>

- [x] Always, by this guide.
- [x] **Required** if the value contains **spaces**.

</details>

### Question 4: Why set `alt`, width, and height on images?

<details>
<summary>Answer</summary>

- [x] `alt` if the image **cannot be displayed**.
- [x] Size lets the browser **reserve space** and reduce flicker.

</details>

### Question 5: Why keep `<html>`, `<head>`, and `<body>` even if validators allow omitting them?

<details>
<summary>Answer</summary>

- [x] Omitting `<body>` can break **older browsers**.
- [x] Omitting html/body can crash **DOM and XML** software.

</details>

### Question 6: Why use lowercase file names?

<details>
<summary>Answer</summary>

- [x] Unix/Apache servers are **case sensitive**.
- [x] Mixing case can **break the site** after a move to a case-sensitive host.

</details>

</details>

## Summary

Start with `<!DOCTYPE html>`, use lowercase quoted markup, close tags, keep `title`/`lang`/charset/viewport, size images, indent two spaces, load CSS/JS without `type`, and name files in lowercase `.html`.

## References

- [HTML Style Guide (W3Schools)](https://www.w3schools.com/html/html5_syntax.asp)
- [Try it Yourself: tryhtml_syntax_nobody](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_syntax_nobody)
- [Try it Yourself: tryhtml_syntax_nohead](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_syntax_nohead)
- [Try it Yourself: tryhtml_syntax_body](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_syntax_body)
- [Try it Yourself: tryhtml_syntax_javascript](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_syntax_javascript)
- [JavaScript Style Guide](https://www.w3schools.com/js/js_conventions.asp)
- [MDN: HTML: A good basis for accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML)
