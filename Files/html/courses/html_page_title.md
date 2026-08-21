# HTML Page Title

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

Every page should have a **`<title>`** that describes what the page means. The title appears in the **browser tab**, in **favorites**, and in **search results**. It matters for **SEO**.

This section has **1** example:

- [x] **Example 1:** The title element [View](#html-page-title-example-01)

## Detailed Explanation

- [x] **What is a good title?**
  - Describe the **content and meaning** of the page.
  - Search engines use it when **ranking** results.
  - `<title>` also: toolbar title, favorites name, search-result title.
  - Make it **accurate and meaningful**.

| Tag       | Description                       |
| --------- | --------------------------------- |
| `<title>` | Defines the title of the document |

<a id="html-page-title-example-01"></a>

### **Example 1: The title element**

- [x] **The title element**
  - Goes in `<head>`.
  - Example title: **HTML Tutorial**.
  - Body: `The content of the document......`

Sandbox: `code_sandbox/html-page-title/index.html`

```html
<!DOCTYPE html>
<html>
  <head>
    <title>HTML Tutorial</title>
  </head>
  <body>
    The content of the document......
  </body>
</html>
```

<img alt="html-page-title source" src="../code_sandbox/snaps/html-page-title-code.png" />

<img alt="html-page-title result" src="../code_sandbox/snaps/html-page-title-result.png" />

- [x] **Outcome:** the browser shows **HTML Tutorial The content of the document......**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-page-title/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Where does `<title>` go, and where is it shown?

<details>
<summary>Answer</summary>

- [x] In the **`<head>`**.
- [x] In the browser **title bar / tab**.

</details>

### Question 2: Why is the page title important for SEO?

<details>
<summary>Answer</summary>

- [x] Search engines use it when **ordering** results.
- [x] It also appears as the **search-result** title.

</details>

### Question 3: What else uses the title besides the tab?

<details>
<summary>Answer</summary>

- [x] The name when the page is added to **favorites**.
- [x] The title in **search engine** listings.

</details>

### Question 4: What makes a good title?

<details>
<summary>Answer</summary>

- [x] It describes the **content and meaning** of the page.
- [x] It is **accurate and meaningful**.

</details>

### Question 5: What title does the chapter example use?

<details>
<summary>Answer</summary>

- [x] **HTML Tutorial**.

</details>

</details>

## Summary

Put a meaningful `<title>` in `<head>`. It labels the tab, favorites, and search results, and it feeds SEO. The chapter example title is **HTML Tutorial**.

## References

- [HTML Page Title (W3Schools)](https://www.w3schools.com/html/html_page_title.asp)
- [MDN: `<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)
- [Google: Title links](https://developers.google.com/search/docs/appearance/title-link)
