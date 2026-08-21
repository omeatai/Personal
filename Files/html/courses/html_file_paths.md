# HTML File Paths

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

A **file path** is the location of a file in a site’s folder structure. Paths are used for pages, images, style sheets, and scripts. This chapter compares **absolute** (full URL) and **relative** paths, and recommends relative paths when possible.

This section has **4** examples:

- [x] **Example 1:** Absolute [View](#html-file-paths-example-01)
- [x] **Example 2:** Root-relative [View](#html-file-paths-example-02)
- [x] **Example 3:** Current folder [View](#html-file-paths-example-03)
- [x] **Example 4:** Parent folder [View](#html-file-paths-example-04)

## Detailed Explanation

- [x] **Used when linking to**
  - Web pages, images, style sheets, JavaScripts.
- [x] **Absolute file paths**
  - The **full URL** to a file.
  - Example: `https://www.w3schools.com/images/picture.jpg` (alt **Mountain**).
  - Sandbox: `code_sandbox/html-filepaths/absolute.html`.

<img alt="html-filepaths absolute result" src="../code_sandbox/snaps/html-filepaths-result.png" />
- [x] **Best practice**
  - Prefer **relative** file paths when possible.
  - Then pages are **not bound** to the current base URL.
  - Links work on **localhost**, the current public domain, and **future** domains.

<a id="html-file-paths-example-01"></a>

### **Example 1: Absolute**

- [x] This example runs the tested markup in `code_sandbox/html-file-paths/absolute.html`.

Sandbox: `code_sandbox/html-file-paths/absolute.html`

```html
<img src="https://www.w3schools.com/images/picture.jpg" alt="Mountain" />
```

<img alt="html-filepaths absolute source" src="../code_sandbox/snaps/html-filepaths-code.png" />

<img alt="html-filepaths absolute result" src="../code_sandbox/snaps/html-filepaths-result.png" />

- [x] **Outcome:** the browser shows **Mountain**.

<a id="html-file-paths-example-02"></a>

### **Example 2: Root-relative**

- [x] **File path examples (from the page)**
      | Path | Description |
      | --------------------------------- | -------------------------------------------------- |
- [x] **Relative file paths**
  - Point to a file **relative to the current page**.
  - Root of the site: `/images/picture.jpg` (sandbox serves this from `code_sandbox/images/`).
  - Current folder: `images/picture.jpg`.
  - One level up (example on the page): `../images/picture.jpg` (sandbox: `nested/up.html`).
  - Sandbox: `root.html`, `folder.html`, `nested/up.html`. Same-folder also: `index.html` (`picture.jpg`).

Sandbox: `code_sandbox/html-file-paths/root.html`

```html
<img src="/images/picture.jpg" alt="Mountain" />
```

<img alt="html-filepaths root source" src="../code_sandbox/snaps/html-filepaths-01-code.png" />

<img alt="html-filepaths root-relative result" src="../code_sandbox/snaps/html-filepaths-01-result.png" />

- [x] **Outcome:** the browser shows **Mountain**.

<a id="html-file-paths-example-03"></a>

### **Example 3: Current folder**

- [x] **File path examples (from the page)**
      | Path | Description |
      | --------------------------------- | -------------------------------------------------- |
- [x] **Relative file paths**
  - Point to a file **relative to the current page**.
  - Root of the site: `/images/picture.jpg` (sandbox serves this from `code_sandbox/images/`).
  - Current folder: `images/picture.jpg`.
  - One level up (example on the page): `../images/picture.jpg` (sandbox: `nested/up.html`).
  - Sandbox: `root.html`, `folder.html`, `nested/up.html`. Same-folder also: `index.html` (`picture.jpg`).

Sandbox: `code_sandbox/html-file-paths/folder.html`

```html
<img src="images/picture.jpg" alt="Mountain" />
```

<img alt="html-filepaths folder source" src="../code_sandbox/snaps/html-filepaths-02-code.png" />

<img alt="html-filepaths current-folder result" src="../code_sandbox/snaps/html-filepaths-02-result.png" />

- [x] **Outcome:** the browser shows **Mountain**.

<a id="html-file-paths-example-04"></a>

### **Example 4: Parent folder**

- [x] This example runs the tested markup in `code_sandbox/html-file-paths/nested/up.html`.

Sandbox: `code_sandbox/html-file-paths/nested/up.html`

```html
<img src="../images/picture.jpg" alt="Mountain" />
```

<img alt="html-filepaths parent source" src="../code_sandbox/snaps/html-filepaths-03-code.png" />

<img alt="html-filepaths parent-folder result" src="../code_sandbox/snaps/html-filepaths-03-result.png" />

- [x] **Outcome:** the browser shows **Mountain**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-filepaths/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a file path?

<details>
<summary>Answer</summary>

- [x] The **location** of a file in a website’s folder structure.

</details>

### Question 2: What does `src="picture.jpg"` mean?

<details>
<summary>Answer</summary>

- [x] The file is in the **same folder** as the current page.

</details>

### Question 3: What is the difference between `images/` and `/images/`?

<details>
<summary>Answer</summary>

- [x] `images/` is inside the **current folder**.
- [x] `/images/` is at the **root** of the current web.

</details>

### Question 4: What does `../` mean in a path?

<details>
<summary>Answer</summary>

- [x] The folder **one level up**.

</details>

### Question 5: What is an absolute file path?

<details>
<summary>Answer</summary>

- [x] The **full URL** to a file.

</details>

### Question 6: Why prefer relative paths?

<details>
<summary>Answer</summary>

- [x] Pages are **not bound** to the current base URL.
- [x] Links work on **localhost**, the current domain, and **future** domains.

</details>

</details>

## Summary

Use file paths to locate pages, images, CSS, and JS. Absolute paths are full URLs. Relative paths are same folder, `images/`, `/images/` (site root), or `../` (parent). Prefer relative paths so the site is portable.

## References

- [HTML File Paths (W3Schools)](https://www.w3schools.com/html/html_filepaths.asp)
- [Try it Yourself: tryhtml_files_absoulute](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_files_absoulute)
- [Try it Yourself: tryhtml_files_relative](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_files_relative)
- [Try it Yourself: tryhtml_files_relative_1](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_files_relative_1)
- [Try it Yourself: tryhtml_files_relative_2](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_files_relative_2)
- [HTML Images](https://www.w3schools.com/html/html_images.asp)
- [MDN: URLs and paths](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)
