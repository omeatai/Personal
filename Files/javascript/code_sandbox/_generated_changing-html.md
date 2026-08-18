<details>
  <summary>Changing HTML</summary>

## Introduction

The DOM lets JavaScript replace element HTML, change attributes such as `src`, and write the date into the page.

This section has **6** examples:

- [x] **Example 1:** Change the content of a p element [View](#changing-html-example-01)
- [x] **Example 2:** Change the content of an h1 element [View](#changing-html-example-02)
- [x] **Example 3:** Change an img src attribute [View](#changing-html-example-03)
- [x] **Example 4:** Dynamic HTML content with Date() [View](#changing-html-example-04)
- [x] **Example 5:** document.write() during parse [View](#changing-html-example-05)
- [x] **Example 6:** Warning — never document.write() after the document is loaded [View](#changing-html-example-06)

## Detailed Explanation

- [x] `innerHTML` replaces an element’s HTML content.
- [x] Assign `element.attribute` (for example `img.src`) to change attributes.
- [x] **Never** `document.write` after the document has loaded — it overwrites the page.

<a id="changing-html-example-01"></a>

### **Example 1: Change the content of a p element**

- [x] Syntax: `document.getElementById(id).innerHTML = new HTML`.
- [x] The page has `<p id="p1">Hello World!</p>`. JS replaces the text with **New text!**.
- [x] Do not run this before the element exists (put the script **after** the HTML, or wait for DOMContentLoaded).
- [x] Always quote the id: `"p1"`, not `p1` as a bare identifier.

Sandbox: `code_sandbox/changing-html/innerhtml-p.html`

```html
<p id="p1">Hello World!</p>
<script>
document.getElementById("p1").innerHTML = "New text!";
</script>
```

<img alt="changing-html example 1 source" src="./code_sandbox/snaps/changing-html-01-code.png" />

<img alt="changing-html example 1 result" src="./code_sandbox/snaps/changing-html-01-result.png" />

- [x] **Outcome:** The paragraph that said **Hello World!** now says **New text!**.

<a id="changing-html-example-02"></a>

### **Example 2: Change the content of an h1 element**

- [x] `innerHTML` works on **any** element, including headings.
- [x] Here `#id01` starts as **Old Heading** and becomes **New Heading**.
- [x] Same three steps: find by id → take the element → assign `innerHTML`.

Sandbox: `code_sandbox/changing-html/innerhtml-heading.html`

```html
<h1 id="id01">Old Heading</h1>
<script>
const element = document.getElementById("id01");
element.innerHTML = "New Heading";
</script>
```

<img alt="changing-html example 2 source" src="./code_sandbox/snaps/changing-html-02-code.png" />

<img alt="changing-html example 2 result" src="./code_sandbox/snaps/changing-html-02-result.png" />

- [x] **Outcome:** The heading reads **New Heading**.

<a id="changing-html-example-03"></a>

### **Example 3: Change an img src attribute**

- [x] Syntax: `document.getElementById(id).attribute = new value`.
- [x] Here `src` starts as a smiley SVG and is switched to a landscape SVG (stand-ins for the site’s `smiley.gif` / `landscape.jpg`).
- [x] `img.src` after assignment is the **absolute** URL the browser resolved.
- [x] Changing `src` starts a new image load.

Sandbox: `code_sandbox/changing-html/change-src.html`

```html
<img id="myImage" alt="demo" src="smiley.svg" width="48" height="48">
<script>
document.getElementById("myImage").src = "landscape.svg";
</script>
```

<img alt="changing-html example 3 source" src="./code_sandbox/snaps/changing-html-03-code.png" />

<img alt="changing-html example 3 result" src="./code_sandbox/snaps/changing-html-03-result.png" />

- [x] **Outcome:** The image `src` is changed from the smiley file to **landscape.svg**.

<a id="changing-html-example-04"></a>

### **Example 4: Dynamic HTML content with Date()**

- [x] JavaScript can write **live** values into the page, such as the current date.
- [x] `Date()` with no `new` returns a date **string** (implementation dependent, usually locale-like).
- [x] Re-run the assignment to refresh the clock (or use `setInterval` later).

Sandbox: `code_sandbox/changing-html/dynamic-date.html`

```html
<p id="when"></p>
<script>
document.getElementById("when").innerHTML = "Date : " + Date();
</script>
```

<img alt="changing-html example 4 source" src="./code_sandbox/snaps/changing-html-04-code.png" />

<img alt="changing-html example 4 result" src="./code_sandbox/snaps/changing-html-04-result.png" />

- [x] **Outcome:** The paragraph shows **Date :** followed by the current date/time string.

<a id="changing-html-example-05"></a>

### **Example 5: document.write() during parse**

- [x] `document.write()` writes into the HTML **output stream** while the document is still loading.
- [x] The W3Schools example places it between two “Bla bla bla” paragraphs so the date appears in the middle.
- [x] This sandbox uses an **iframe** so we can `open` / `write` / `close` without wiping the tutorial page.
- [x] During initial parse, `write` inserts at the current position; after load it **replaces the whole document**.

Sandbox: `code_sandbox/changing-html/document-write-stream.html`

```html
<p>Bla bla bla</p>
<script>
document.write(Date());
</script>
<p>Bla bla bla</p>
```

<img alt="changing-html example 5 source" src="./code_sandbox/snaps/changing-html-05-code.png" />

<img alt="changing-html example 5 result" src="./code_sandbox/snaps/changing-html-05-result.png" />

- [x] **Outcome:** The iframe document contains Bla, then the **date string**, then Bla — `write` ran as part of the stream.

<a id="changing-html-example-06"></a>

### **Example 6: Warning — never document.write() after the document is loaded**

- [x] **Never** call `document.write()` after load. It calls `open()` implicitly and **overwrites** the page.
- [x] That is why modern code uses `innerHTML`, `textContent`, or `appendChild` instead.
- [x] This demo writes into an iframe **after** it has loaded so you can see the previous content vanish.

Sandbox: `code_sandbox/changing-html/document-write-warning.html`

```html
<script>
window.addEventListener("load", function () {
  // This would wipe the real page. Do not do this on a live document.
  // document.write("oops");
});
</script>
```

<img alt="changing-html example 6 source" src="./code_sandbox/snaps/changing-html-06-code.png" />

<img alt="changing-html example 6 result" src="./code_sandbox/snaps/changing-html-06-result.png" />

- [x] **Outcome:** The iframe first shows **keep me**, then after `write` it only shows **overwritten** — the original document is gone.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/changing-html/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the `innerHTML` assignment syntax?

<details>
<summary>Answer</summary>

- [x] `document.getElementById(id).innerHTML = new HTML`.

</details>

### Question 2: Why might `getElementById` be null if the markup looks correct?

<details>
<summary>Answer</summary>

- [x] The script ran **before** the element existed. Move the script below the HTML or wait for **DOMContentLoaded**.

</details>

### Question 3: Does `innerHTML` work on headings?

<details>
<summary>Answer</summary>

- [x] Yes — any element, including **`<h1>`**.

</details>

### Question 4: How do you change an image file from JS?

<details>
<summary>Answer</summary>

- [x] Set **`img.src`** (or `setAttribute("src", …)`) to the new URL.

</details>

### Question 5: What does `Date()` return when called as a function?

<details>
<summary>Answer</summary>

- [x] A **date string**, not a Date object (`new Date()` is the object).

</details>

### Question 6: When is `document.write` acceptable?

<details>
<summary>Answer</summary>

- [x] Only while the document is still **parsing** (or into a document you `open()` yourself).

</details>

### Question 7: What happens if you `document.write` after load?

<details>
<summary>Answer</summary>

- [x] It **overwrites** the entire document. The previous DOM is destroyed.

</details>

### Question 8: How can you quote the id wrong?

<details>
<summary>Answer</summary>

- [x] Forgetting quotes (`p1` as a variable) or putting a script in `<head>` too early.

</details>

### Question 9: Why does this sandbox use an iframe for `write`?

<details>
<summary>Answer</summary>

- [x] So the example can demonstrate overwriting **without** destroying the tutorial page around it.

</details>

### Question 10: What should you use instead of `write` for updates?

<details>
<summary>Answer</summary>

- [x] **`innerHTML`**, **`textContent`**, or DOM methods like **`appendChild`**.

</details>


</details>

## Summary

Prefer `innerHTML` / `textContent` / `src` assignments. Keep `document.write` off live pages.

## References

- [Changing HTML](https://www.w3schools.com/js/js_htmldom_html.asp)
- [MDN Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)

</details>
