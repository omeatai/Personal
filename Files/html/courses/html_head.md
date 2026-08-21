# HTML Head

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

The HTML **`<head>`** element holds **metadata** (data about data): `<title>`, `<style>`, `<meta>`, `<link>`, `<script>`, and `<base>`. Metadata sits between `<html>` and `<body>` and is **not shown** as page content.

This section has **6** examples:

- [x] **Example 1:** Title [View](#html-head-example-01)
- [x] **Example 2:** Style [View](#html-head-example-02)
- [x] **Example 3:** Link [View](#html-head-example-03)
- [x] **Example 4:** Meta [View](#html-head-example-04)
- [x] **Example 5:** Script [View](#html-head-example-05)
- [x] **Example 6:** Base [View](#html-head-example-06)

## Detailed Explanation

- [x] **The `<head>` element**
  - Container for metadata between `<html>` and `<body>`.
  - Typical metadata: document **title**, **character set**, **styles**, **scripts**, other meta information.
- [x] **Setting the viewport**
  - Viewport = the user’s **visible area** (smaller on a phone).
  - Include on **all** pages: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.
  - `width=device-width` follows the device screen width; `initial-scale=1.0` is the initial zoom.

<a id="html-head-example-01"></a>

### **Example 1: Title**

- [x] **The `<title>` element**
  - **Required.** Text-only title in the **tab / title bar**.
  - Important for **SEO** (search engines use it in rankings and result titles).
  - Also used in the toolbar and when the page is added to **favorites**.
  - Make the title **accurate and meaningful**.
  - Example: **A Meaningful Page Title**.

Sandbox: `code_sandbox/html-head/index.html`

```html
<title>A Meaningful Page Title</title>
```

<img alt="html-head title source" src="../code_sandbox/snaps/html-head-code.png" />

<img alt="html-head title result" src="../code_sandbox/snaps/html-head-result.png" />

- [x] **Outcome:** the browser shows **A Meaningful Page Title**.

<a id="html-head-example-02"></a>

### **Example 2: Style**

- [x] **The `<style>` element**
  - Style information for a **single** page.
  - Example: powderblue body, red `h1`, blue `p`.
  - Sandbox: `style.html`.

Sandbox: `code_sandbox/html-head/style.html`

```html
<style>
  body {
    background-color: powderblue;
  }
  h1 {
    color: red;
  }
  p {
    color: blue;
  }
</style>
```

<img alt="html-head style source" src="../code_sandbox/snaps/html-head-01-code.png" />

<img alt="html-head style result" src="../code_sandbox/snaps/html-head-01-result.png" />

- [x] **Outcome:** the browser shows **body { background-color: powderblue; } h1 { color: red; } p { color: blue; }**.

<a id="html-head-example-03"></a>

### **Example 3: Link**

- [x] **The `<link>` element**
  - Relationship to an **external resource**.
  - Most often: `<link rel="stylesheet" href="mystyle.css">`.
  - Sandbox: `link.html` + `mystyle.css`.

Sandbox: `code_sandbox/html-head/link.html`

```html
<link rel="stylesheet" href="mystyle.css" />
```

<img alt="html-head link source" src="../code_sandbox/snaps/html-head-02-code.png" />

<img alt="html-head link result" src="../code_sandbox/snaps/html-head-02-result.png" />

- [x] **Outcome:** the page demonstrates **Link** as shown in the result snap.

<a id="html-head-example-04"></a>

### **Example 4: Meta**

- [x] **The `<meta>` element**
  - Character set, description, keywords, author, viewport; not displayed.
  - Used by browsers, search engines, and other services.
  - Examples from the page: `charset="UTF-8"`; keywords; description **Free Web tutorials**; author **John Doe**; `http-equiv="refresh" content="30"` (reload every 30 seconds — omitted from the sandbox so it does not auto-refresh); viewport (below).
  - Sandbox: `meta.html`.

Sandbox: `code_sandbox/html-head/meta.html`

```html
<meta charset="UTF-8" />
<meta name="description" content="Free Web tutorials" />
<meta name="keywords" content="HTML, CSS, JavaScript" />
<meta name="author" content="John Doe" />
```

<img alt="html-head meta source" src="../code_sandbox/snaps/html-head-03-code.png" />

<img alt="html-head meta result" src="../code_sandbox/snaps/html-head-03-result.png" />

- [x] **Outcome:** the page demonstrates **Meta** as shown in the result snap.

<a id="html-head-example-05"></a>

### **Example 5: Script**

- [x] **The `<script>` element**
  - Client-side JavaScript.
  - Example: `myFunction()` writes **Hello JavaScript!** into `#demo`.
  - Sandbox: `script.html`.

Sandbox: `code_sandbox/html-head/script.html`

```html
<script>
  function myFunction() {
    document.getElementById("demo").innerHTML = "Hello JavaScript!";
  }
</script>
```

<img alt="html-head script source" src="../code_sandbox/snaps/html-head-04-code.png" />

<img alt="html-head script result" src="../code_sandbox/snaps/html-head-04-result.png" />

- [x] **Outcome:** the browser shows **function myFunction() { document.getElementById("demo").innerHTML = "Hello JavaScript!"; }**.

<a id="html-head-example-06"></a>

### **Example 6: Base**

- [x] **The `<base>` element**
  - Default **URL and/or target** for relative URLs.
  - Must have **`href` or `target` or both**.
  - **Only one** `<base>` per document.
  - Example: `href="https://www.w3schools.com/" target="_blank"` so `images/stickman.gif` and `tags/tag_base.asp` resolve on W3Schools and open in a new tab.
  - Sandbox: `base.html`.
    | Tag | Description |
    | ---------- | -------------------------------------------------------- |
    | `<head>` | Defines information about the document |
    | `<title>` | Defines the title of a document |
    | `<base>` | Default address or target for all links on a page |
    | `<link>` | Relationship between a document and an external resource |
    | `<meta>` | Metadata about an HTML document |
    | `<script>` | A client-side script |
    | `<style>` | Style information for a document |

Sandbox: `code_sandbox/html-head/base.html`

```html
<base href="https://www.w3schools.com/" target="_blank" />
```

<img alt="html-head base source" src="../code_sandbox/snaps/html-head-05-code.png" />

<img alt="html-head base result" src="../code_sandbox/snaps/html-head-05-result.png" />

- [x] **Outcome:** the page demonstrates **Base** as shown in the result snap.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-head/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `<head>` contain, and is that content shown on the page?

<details>
<summary>Answer</summary>

- [x] **Metadata** (title, charset, styles, scripts, and so on).
- [x] Metadata is **not displayed** as page content.

</details>

### Question 2: Why is `<title>` required, and why does it matter for SEO?

<details>
<summary>Answer</summary>

- [x] It is **required** and appears in the **tab / title bar**.
- [x] Search engines use it in **rankings** and **result titles**.

</details>

### Question 3: When do you use `<style>` vs `<link>`?

<details>
<summary>Answer</summary>

- [x] `<style>` — CSS for a **single** page.
- [x] `<link rel="stylesheet">` — an **external** style sheet.

</details>

### Question 4: What viewport meta should every page include?

<details>
<summary>Answer</summary>

- [x] `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.

</details>

### Question 5: What are the rules for `<base>`?

<details>
<summary>Answer</summary>

- [x] Sets the default **URL and/or target** for relative URLs.
- [x] Needs **`href` or `target` or both**.
- [x] **Only one** `<base>` per document.

</details>

</details>

## Summary

`<head>` holds metadata between `<html>` and `<body>`. `<title>` is required and matters for tabs and SEO. Use `<style>` or `<link>` for CSS, `<meta>` for charset/description/keywords/author/viewport, `<script>` for JS, and one `<base>` for default URLs.

## References

- [HTML The Head Element (W3Schools)](https://www.w3schools.com/html/html_head.asp)
- [Try it Yourself: tryhtml_head_title](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_head_title)
- [Try it Yourself: tryhtml_head_style](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_head_style)
- [Try it Yourself: tryhtml_head_link](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_head_link)
- [Try it Yourself: tryhtml_head_meta](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_head_meta)
- [Try it Yourself: tryhtml_head_script](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_head_script)
- [Try it Yourself: tryhtml_head_base](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_head_base)
- [CSS Tutorial](https://www.w3schools.com/css/default.asp)
- [JavaScript Tutorial](https://www.w3schools.com/js/default.asp)
- [MDN: `<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)
- [MDN: viewport meta](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag)
