# HTML Id

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

The HTML **`id`** attribute gives an element a **unique** name in the document. CSS targets it with a **hash** (`#myHeader`). The same value also makes **bookmarks** (`href="#C4"`) and lets JavaScript use **`getElementById()`**. A **class** may be reused; an **id** may not.

This section has **4** examples:

- [x] **Example 1:** Unique id [View](#html-id-example-01)
- [x] **Example 2:** Class vs id [View](#html-id-example-02)
- [x] **Example 3:** Bookmark [View](#html-id-example-03)
- [x] **Example 4:** JavaScript [View](#html-id-example-04)

## Detailed Explanation

- [x] **Id name rules (from the page)**
  - The id name is **case sensitive**.
  - Must contain **at least one character**.
  - **Cannot start with a number**.
  - Must **not contain whitespaces** (spaces, tabs, and so on).
- [x] **Chapter summary from the page**
  - Unique id per document; CSS and JS select it; **case sensitive**; also used for **bookmarks**; JS uses **`getElementById()`**.

<a id="html-id-example-01"></a>

### **Example 1: Unique id**

- [x] **The `id` attribute**
  - Specifies a **unique id** for an HTML element.
  - You **cannot** have more than one element with the same `id` in a document.
  - Used to point to a **specific style** in a style sheet, and by JavaScript to access that element.
  - CSS syntax: **hash (`#`)** + id name + properties in `{}`.
  - Example: `<h1 id="myHeader">` styled by `#myHeader` (light blue, padding, centered).

Sandbox: `code_sandbox/html-id/index.html`

```html
<style>
  #myHeader {
    background-color: lightblue;
    color: black;
    padding: 40px;
    text-align: center;
  }
</style>
<h1 id="myHeader">My Header</h1>
```

<img alt="html-id header source" src="../code_sandbox/snaps/html-id-code.png" />

<img alt="html-id header result" src="../code_sandbox/snaps/html-id-result.png" />

- [x] **Outcome:** the browser shows **#myHeader { background-color: lightblue; color: black; padding: 40px; text-align: center; } My Header**.

<a id="html-id-example-02"></a>

### **Example 2: Class vs id**

- [x] **Difference between class and id**
  - A **class** name can be used by **multiple** elements.
  - An **id** name must be used by **only one** element on the page.
  - Example: unique `#myHeader` (“My Cities”) plus shared `.city` on London, Paris, Tokyo.
  - Sandbox: `class.html`.

Sandbox: `code_sandbox/html-id/class.html`

```css
#myHeader {
  /* one unique id */
}
.city {
  /* many elements */
}
```

<img alt="html-id class vs id source" src="../code_sandbox/snaps/html-id-01-code.png" />

<img alt="html-id class vs id result" src="../code_sandbox/snaps/html-id-01-result.png" />

- [x] **Outcome:** the browser shows **#myHeader { /_ one unique id _/ } .city { /_ many elements _/ }**.

<a id="html-id-example-03"></a>

### **Example 3: Bookmark**

- [x] **HTML bookmarks with id and links**
  - Bookmarks let readers **jump** to a part of a (often long) page.
  - Create the bookmark: `<h2 id="C4">Chapter 4</h2>`.
  - Same-page link: `<a href="#C4">Jump to Chapter 4</a>`.
  - Other-page link: `<a href="html_demo.html#C4">Jump to Chapter 4</a>`.
  - Sandbox: `bookmark.html`.

Sandbox: `code_sandbox/html-id/bookmark.html`

```html
<h2 id="C4">Chapter 4</h2>
<a href="#C4">Jump to Chapter 4</a>
```

<img alt="html-id bookmark source" src="../code_sandbox/snaps/html-id-02-code.png" />

<img alt="html-id bookmark result" src="../code_sandbox/snaps/html-id-02-result.png" />

- [x] **Outcome:** the browser shows **Chapter 4**, **Jump to Chapter 4**.

<a id="html-id-example-04"></a>

### **Example 4: JavaScript**

- [x] **JavaScript and id**
  - `document.getElementById("myHeader")` accesses that one element.
  - Example: set `innerHTML` to **Have a nice day!**.
  - Sandbox: `js.html`.

Sandbox: `code_sandbox/html-id/js.html`

```html
<script>
  function displayResult() {
    document.getElementById("myHeader").innerHTML = "Have a nice day!";
  }
</script>
```

<img alt="html-id javascript source" src="../code_sandbox/snaps/html-id-03-code.png" />

<img alt="html-id javascript result" src="../code_sandbox/snaps/html-id-03-result.png" />

- [x] **Outcome:** the browser shows **function displayResult() { document.getElementById("myHeader").innerHTML = "Have a nice day!"; }**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-id/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does the `id` attribute specify, and how many elements may share it?

<details>
<summary>Answer</summary>

- [x] A **unique id** for an HTML element.
- [x] **Only one** element per document may use that value.

</details>

### Question 2: How do you write a CSS id selector?

<details>
<summary>Answer</summary>

- [x] A **hash (`#`)** then the id name.
- [x] Then properties inside **curly braces**.

</details>

### Question 3: What rules apply to an id name?

<details>
<summary>Answer</summary>

- [x] **Case sensitive**.
- [x] At least **one character**.
- [x] **Cannot start with a number**.
- [x] **No whitespaces**.

</details>

### Question 4: How does `class` differ from `id`?

<details>
<summary>Answer</summary>

- [x] A **class** can be used by **multiple** elements.
- [x] An **id** must be used by **only one** element on the page.

</details>

### Question 5: How do you create a same-page bookmark?

<details>
<summary>Answer</summary>

- [x] Put `id` on the target: `<h2 id="C4">Chapter 4</h2>`.
- [x] Link with `<a href="#C4">Jump to Chapter 4</a>`.

</details>

### Question 6: How do you link to a bookmark on another page?

<details>
<summary>Answer</summary>

- [x] Use the filename plus the hash: `html_demo.html#C4`.

</details>

### Question 7: How does JavaScript select one element by id?

<details>
<summary>Answer</summary>

- [x] **`document.getElementById("myHeader")`**.

</details>

</details>

## Summary

`id` is unique, case sensitive, and cannot start with a number or contain spaces. CSS uses `#id`. Class can be reused; id cannot. Use `id` plus `href="#id"` for bookmarks, and `getElementById()` in JavaScript.

## References

- [HTML id Attribute (W3Schools)](https://www.w3schools.com/html/html_id.asp)
- [Try it Yourself: tryhtml_id_css](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_id_css)
- [Try it Yourself: tryhtml_id_class](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_id_class)
- [Try it Yourself: tryhtml_id_bookmark](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_id_bookmark)
- [Try it Yourself: tryhtml_id_js](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_id_js)
- [CSS Tutorial](https://www.w3schools.com/css/default.asp)
- [HTML JavaScript](https://www.w3schools.com/html/html_scripts.asp)
- [MDN: id](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)
- [MDN: `getElementById()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)
