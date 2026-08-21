# HTML Favicon

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

A **favicon** is a small image next to the page title in the **browser tab**. Add it with `<link rel="icon">` in `<head>` after `<title>`. Keep the image **simple** and **high contrast**. A common filename is `favicon.ico`.

This section has **1** example:

- [x] **Example 1:** How to add it [View](#html-favicon-example-01)

## Detailed Explanation

- [x] **Where it shows**
  - Left of the page title in the tab.
- [x] **Format support**
  - Edge, Chrome, Firefox, Opera, and Safari all support **ICO, PNG, GIF, JPEG, and SVG**.
- [x] **Chapter summary**
  - Use the HTML `<link>` element to insert a favicon.

| Tag      | Description                                              |
| -------- | -------------------------------------------------------- |
| `<link>` | Relationship between a document and an external resource |

<a id="html-favicon-example-01"></a>

### **Example 1: How to add it**

- [x] **How to add it**
  - Save the image in the site root, or in an `images` folder.
  - In `index.html`, after `<title>`: `<link rel="icon" type="image/x-icon" href="/images/favicon.ico">`.
  - Reload; the tab should show the icon.
  - You can make a favicon on sites like favicon.cc.
  - The sandbox uses a local `favicon.ico` and `href="favicon.ico"`.

Sandbox: `code_sandbox/html-favicon/index.html`

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page Title</title>
    <link rel="icon" type="image/x-icon" href="favicon.ico" />
  </head>
  <body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

<img alt="html-favicon source" src="../code_sandbox/snaps/html-favicon-code.png" />

<img alt="html-favicon result" src="../code_sandbox/snaps/html-favicon-result.png" />

- [x] **Outcome:** the browser shows **My Page Title This is a Heading**, **This is a paragraph.**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-favicon/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a favicon?

<details>
<summary>Answer</summary>

- [x] A **small image** next to the page title in the **browser tab**.

</details>

### Question 2: Which tag adds a favicon?

<details>
<summary>Answer</summary>

- [x] `<link rel="icon" type="image/x-icon" href="…">` in **`<head>`**, after **`<title>`**.

</details>

### Question 3: What kind of image works well?

<details>
<summary>Answer</summary>

- [x] A **simple** image with **high contrast**.
- [x] A common name is **`favicon.ico`**.

</details>

### Question 4: Which formats do major browsers support?

<details>
<summary>Answer</summary>

- [x] **ICO, PNG, GIF, JPEG, SVG** (Edge, Chrome, Firefox, Opera, Safari).

</details>

### Question 5: Where do you save the favicon file?

<details>
<summary>Answer</summary>

- [x] In the **site root**, or in an **`images`** folder.
- [x] Then point `href` at that file.

</details>

</details>

## Summary

Add a favicon with `<link rel="icon">` in `<head>` after `<title>`. Store `favicon.ico` in the root or an images folder. Use a simple high-contrast image. ICO, PNG, GIF, JPEG, and SVG work in current major browsers.

## References

- [HTML Favicon (W3Schools)](https://www.w3schools.com/html/html_favicon.asp)
- [favicon.cc](https://www.favicon.cc)
- [MDN: Adding a favicon](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Webpage_metadata#adding_custom_icons_to_your_site)
- [MDN: `<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)
