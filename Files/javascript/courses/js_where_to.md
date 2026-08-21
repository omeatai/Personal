# JS Where To

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

In HTML, JavaScript is inserted between **`<script>`** and **`</script>`**. This section shows scripts in the **`<head>`** or **`<body>`**, how **functions** run on events such as a button click, and how to load **external `.js` files** with the **`src`** attribute.

This section has **4** examples:

- [x] **Example 1:** The `<script>` tag [View](#js-where-to-example-01)
- [x] **Example 2:** JavaScript in `<head>` [View](#js-where-to-example-02)
- [x] **Example 3:** JavaScript in `<body>` [View](#js-where-to-example-03)
- [x] **Example 4:** External JavaScript [View](#js-where-to-example-04)

## Detailed Explanation

- [x] **The `<script>` tag holds JavaScript**
  - In HTML, code is inserted between **`<script>`** and **`</script>`**.
  - Old examples may use `<script type="text/javascript">`. The **`type` attribute is not required** — JavaScript is the **default** scripting language in HTML.
- [x] **Functions and events (previewed here)**
  - A **function** is a named block of JavaScript that runs only when it is **called**.
  - Events (like a **button click**) are one way to call a function. `onclick="myFunction()"` wires the click to the function.
- [x] **Scripts can go in `<head>`, `<body>`, or both**
  - You can place **any number** of scripts in a document.
  - Placement changes **when** the code runs relative to the HTML being parsed, which the examples below make concrete.

<a id="js-where-to-example-01"></a>

### **Example 1: The `<script>` tag**

- [x] A script placed directly in the page runs **as the browser reaches it** while parsing.
- [x] Here the script sets `#demo`'s `innerHTML` to **"My First JavaScript"**, so the paragraph is already changed by the time you see the page — no button needed.
- [x] This is the simplest form: inline code, no function, no event.

Sandbox: `code_sandbox/js-where-to/basic.html`

```html
<h2>My First Web Page</h2>
<p id="demo">A Paragraph.</p>
<script>
  document.getElementById("demo").innerHTML = "My First JavaScript";
</script>
```

![js-where-to example 1 source](../code_sandbox/snaps/js-where-to-01-code.png)

![js-where-to example 1 result](../code_sandbox/snaps/js-where-to-01-result.png)

- [x] **Outcome:** the paragraph loads already reading **My First JavaScript** (the inline script ran during page load), instead of the original **A Paragraph.**

<a id="js-where-to-example-02"></a>

### **Example 2: JavaScript in `<head>`**

- [x] The function `myFunction()` is **defined** in the `<head>`, but nothing runs until the button is clicked.
- [x] `onclick="myFunction()"` **invokes** the function, which sets `#demo` to **"Paragraph changed."**
- [x] Defining functions in `<head>` keeps them available before the body renders; they just wait to be called.

Sandbox: `code_sandbox/js-where-to/head.html`

```html
<head>
  <script>
    function myFunction() {
      document.getElementById("demo").innerHTML = "Paragraph changed.";
    }
  </script>
</head>
<body>
  <h2>Demo JavaScript in Head</h2>
  <p id="demo">A Paragraph</p>
  <button type="button" onclick="myFunction()">Try it</button>
</body>
```

![js-where-to example 2 source](../code_sandbox/snaps/js-where-to-02-code.png)

![js-where-to example 2 result](../code_sandbox/snaps/js-where-to-02-result.png)

- [x] **Outcome:** after clicking **Try it**, the paragraph changes from **A Paragraph** to **Paragraph changed.** (shown above).

<a id="js-where-to-example-03"></a>

### **Example 3: JavaScript in `<body>`**

- [x] The exact same function works when placed at the **bottom of `<body>`**.
- [x] **Placing scripts at the bottom of `<body>` improves display speed**, because parsing/running scripts can pause rendering — put them after the content they need.
- [x] Behaviour is identical to Example 2; only the script's position differs.

Sandbox: `code_sandbox/js-where-to/index.html`

```html
<body>
  <h2>Demo JavaScript in Body</h2>
  <p id="demo">A Paragraph</p>
  <button type="button" onclick="myFunction()">Try it</button>
  <script>
    function myFunction() {
      document.getElementById("demo").innerHTML = "Paragraph changed.";
    }
  </script>
</body>
```

![js-where-to example 3 source](../code_sandbox/snaps/js-where-to-03-code.png)

![js-where-to example 3 result](../code_sandbox/snaps/js-where-to-03-result.png)

- [x] **Outcome:** clicking **Try it** again produces **Paragraph changed.** under the **Demo JavaScript in Body** heading (shown above).

<a id="js-where-to-example-04"></a>

### **Example 4: External JavaScript**

- [x] Code can live in a separate **`.js`** file and be loaded with **`src`**: `<script src="myScript.js"></script>`.
- [x] The external file contains **only** JavaScript — **no `<script>` tags** inside it.
- [x] The script behaves as if it were written **exactly where the `<script src>` tag sits**; you can put that tag in `<head>` or `<body>`.
- [x] **Advantages:** separates HTML from code, easier to read/maintain, and **cached** `.js` files speed up later page loads. For several files, use several tags (`myScript1.js`, `myScript2.js`).
- [x] **Three ways to reference it:** a **full URL** (`https://.../myScript.js`), a **file path** (`/js/myScript.js`), or **no path** (same folder, `myScript.js`).

Sandbox: `code_sandbox/js-where-to/external.html` plus `code_sandbox/js-where-to/myScript.js`

```html
<!-- external.html -->
<h2>Demo External JavaScript</h2>
<p id="demo">A Paragraph</p>
<button type="button" onclick="myFunction()">Try it</button>
<script src="myScript.js"></script>
```

```javascript
// myScript.js
function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}
```

![js-where-to example 4 source](../code_sandbox/snaps/js-where-to-04-code.png)

![js-where-to example 4 result](../code_sandbox/snaps/js-where-to-04-result.png)

- [x] **Outcome:** the external `myScript.js` supplies the function; clicking **Try it** changes the paragraph to **Paragraph changed.** exactly like the inline versions (shown above).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-where-to/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Where do you put JavaScript in HTML?

<details>
<summary>Answer</summary>

- [x] Between **`<script>`** and **`</script>`** tags.

</details>

### Question 2: Is `type="text/javascript"` required on `<script>`?

<details>
<summary>Answer</summary>

- [x] **No.** The type attribute is **not required**.
- [x] JavaScript is the **default** scripting language in HTML.

</details>

### Question 3: What is a JavaScript function in this section?

<details>
<summary>Answer</summary>

- [x] A **block of JavaScript** that runs when it is **called**.
- [x] It can run when an **event** occurs, such as a **button click**.

</details>

### Question 4: Can you put scripts in both `<head>` and `<body>`?

<details>
<summary>Answer</summary>

- [x] **Yes.** You can place **any number** of scripts.
- [x] They can go in `<body>`, `<head>`, or **both**.

</details>

### Question 5: Why place scripts at the bottom of `<body>`?

<details>
<summary>Answer</summary>

- [x] It **improves display speed**.
- [x] Script interpretation **slows down** the display.

</details>

### Question 6: How do you load an external JavaScript file?

<details>
<summary>Answer</summary>

- [x] Use the **`src`** attribute: `<script src="myScript.js"></script>`.
- [x] JavaScript files use the **`.js`** extension.

</details>

### Question 7: Can an external script file contain `<script>` tags?

<details>
<summary>Answer</summary>

- [x] **No.** External scripts **cannot** contain `<script>` tags.

</details>

### Question 8: What are three advantages of external JavaScript files?

<details>
<summary>Answer</summary>

- [x] They **separate** HTML and code.
- [x] HTML and JavaScript are easier to **read and maintain**.
- [x] **Cached** files can **speed up** page loads.

</details>

### Question 9: What are three ways to reference an external script?

<details>
<summary>Answer</summary>

- [x] A **full URL**.
- [x] A **file path** (like `/js/`).
- [x] **Without any path**.

</details>

### Question 10: Where can you place an external `<script src="...">` tag?

<details>
<summary>Answer</summary>

- [x] In **`<head>`** or **`<body>`**, as you like.
- [x] The script behaves as if it were **exactly where the tag is**.

</details>

</details>

## Summary

Put JavaScript between **`<script>`** tags in **`<head>`**, **`<body>`**, or both. A **function** can run on a **click**. Scripts at the **bottom of `<body>`** display faster. External **`.js`** files use **`src`**, cannot contain `<script>` tags, and can be referenced by **URL**, **path**, or **no path**. Caching and separation of HTML and code are the main advantages.

## References

- [JS Where To (W3Schools)](https://www.w3schools.com/js/js_whereto.asp)
- [Try it Yourself: tryjs_whereto](https://www.w3schools.com/js/tryit.asp?filename=tryjs_whereto)
- [Try it Yourself: tryjs_whereto_head](https://www.w3schools.com/js/tryit.asp?filename=tryjs_whereto_head)
- [Try it Yourself: tryjs_whereto_body](https://www.w3schools.com/js/tryit.asp?filename=tryjs_whereto_body)
- [Try it Yourself: tryjs_whereto_external](https://www.w3schools.com/js/tryit.asp?filename=tryjs_whereto_external)
- [HTML File Paths](https://www.w3schools.com/html/html_filepaths.asp)
- [MDN: The script element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
