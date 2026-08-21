# HTML JavaScript

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

**JavaScript** makes HTML pages more **dynamic and interactive**. This chapter covers the **`<script>`** tag, `getElementById()`, changing **content**, **styles**, and **attributes**, and **`<noscript>`** for browsers without scripts.

This section has **5** examples:

- [x] **Example 1:** Date button [View](#html-javascript-example-01)
- [x] **Example 2:** Change content [View](#html-javascript-example-02)
- [x] **Example 3:** Change styles [View](#html-javascript-example-03)
- [x] **Example 4:** Change attributes [View](#html-javascript-example-04)
- [x] **Example 5:** Noscript [View](#html-javascript-example-05)

## Detailed Explanation

<a id="html-javascript-example-01"></a>

### **Example 1: Date button**

- [x] **My First JavaScript**
  - A button writes the current **date and time** into a paragraph.

Sandbox: `code_sandbox/html-javascript/index.html`

```html
<button
  type="button"
  onclick="document.getElementById('demo').innerHTML = Date()"
>
  Click me to display Date and Time
</button>
<p id="demo"></p>
```

<img alt="html-javascript date source" src="../code_sandbox/snaps/html-javascript-code.png" />

<img alt="html-javascript date button result" src="../code_sandbox/snaps/html-javascript-result.png" />

- [x] **Outcome:** the browser shows **Click me to display Date and Time**.

<a id="html-javascript-example-02"></a>

### **Example 2: Change content**

- [x] **The `<script>` tag**
  - Defines a **client-side script** (JavaScript).
  - Either contains statements, or points to an external file with **`src`**.
  - Common uses: image manipulation, form validation, dynamic content.
  - Selecting an element: **`document.getElementById()`**.
  - Example: write **Hello JavaScript!** into `id="demo"`.
  - Sandbox: `content.html`.

Sandbox: `code_sandbox/html-javascript/content.html`

```html
<script>
  document.getElementById("demo").innerHTML = "Hello JavaScript!";
</script>
```

<img alt="html-javascript content source" src="../code_sandbox/snaps/html-javascript-01-code.png" />

<img alt="html-javascript content result" src="../code_sandbox/snaps/html-javascript-01-result.png" />

- [x] **Outcome:** the browser shows **document.getElementById("demo").innerHTML = "Hello JavaScript!";**.

<a id="html-javascript-example-03"></a>

### **Example 3: Change styles**

- [x] **A taste of JavaScript**
  - **Change content:** `innerHTML = "Hello JavaScript!"`.
  - **Change styles:** `fontSize`, `color`, `backgroundColor`.
  - **Change attributes:** `src` on an image (`picture.gif` in the sandbox).
  - Sandbox: `styles.html` and `attribute.html`.

Sandbox: `code_sandbox/html-javascript/styles.html`

```js
document.getElementById("demo").style.fontSize = "25px";
document.getElementById("demo").style.color = "red";
document.getElementById("demo").style.backgroundColor = "yellow";
```

<img alt="html-javascript styles source" src="../code_sandbox/snaps/html-javascript-02-code.png" />

<img alt="html-javascript styles result" src="../code_sandbox/snaps/html-javascript-02-result.png" />

- [x] **Outcome:** the browser shows **document.getElementById("demo").style.fontSize = "25px"; document.getElementById("demo").style.color = "red"; document.getElementById("demo").style.backgroundColor = "yellow";**.

<a id="html-javascript-example-04"></a>

### **Example 4: Change attributes**

- [x] **A taste of JavaScript**
  - **Change content:** `innerHTML = "Hello JavaScript!"`.
  - **Change styles:** `fontSize`, `color`, `backgroundColor`.
  - **Change attributes:** `src` on an image (`picture.gif` in the sandbox).
  - Sandbox: `styles.html` and `attribute.html`.

Sandbox: `code_sandbox/html-javascript/attribute.html`

```js
document.getElementById("image").src = "picture.gif";
```

<img alt="html-javascript attribute source" src="../code_sandbox/snaps/html-javascript-03-code.png" />

<img alt="html-javascript attribute result" src="../code_sandbox/snaps/html-javascript-03-result.png" />

- [x] **Outcome:** the browser shows **document.getElementById("image").src = "picture.gif";**.

<a id="html-javascript-example-05"></a>

### **Example 5: Noscript**

- [x] **The `<noscript>` tag**
  - Alternate content if scripts are **disabled** or unsupported.
  - Example: `Sorry, your browser does not support JavaScript!`
  - With JS on, the script runs and noscript is hidden.
  - Sandbox: `noscript.html`.
    | Tag | Description |
    | ------------ | ------------------------------------------------------------------- |
    | `<script>` | Defines a client-side script |
    | `<noscript>` | Alternate content for users that do not support client-side scripts |

Sandbox: `code_sandbox/html-javascript/noscript.html`

```html
<noscript>Sorry, your browser does not support JavaScript!</noscript>
```

<img alt="html-javascript noscript source" src="../code_sandbox/snaps/html-javascript-04-code.png" />

<img alt="html-javascript noscript result" src="../code_sandbox/snaps/html-javascript-04-result.png" />

- [x] **Outcome:** the browser shows **Sorry, your browser does not support JavaScript!**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-javascript/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does JavaScript add to HTML pages?

<details>
<summary>Answer</summary>

- [x] It makes pages more **dynamic and interactive**.

</details>

### Question 2: What does the `<script>` tag do?

<details>
<summary>Answer</summary>

- [x] Defines a **client-side script** (JavaScript).
- [x] It can contain statements, or load a file with **`src`**.

</details>

### Question 3: How does this chapter select an HTML element?

<details>
<summary>Answer</summary>

- [x] **`document.getElementById()`**.

</details>

### Question 4: How can JavaScript change content, style, and an attribute?

<details>
<summary>Answer</summary>

- [x] Content: **`innerHTML`**.
- [x] Style: properties like **`fontSize`**, **`color`**, **`backgroundColor`**.
- [x] Attribute: example **`src`** on an image.

</details>

### Question 5: What is `<noscript>` for?

<details>
<summary>Answer</summary>

- [x] Alternate content if scripts are **disabled** or **unsupported**.

</details>

</details>

## Summary

`<script>` holds or loads JavaScript. Use `getElementById()` to change `innerHTML`, CSS styles, or attributes. `<noscript>` is fallback text when JS is off.

## References

- [HTML JavaScript (W3Schools)](https://www.w3schools.com/html/html_scripts.asp)
- [Try it Yourself: tryhtml_scripts_intro](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_scripts_intro)
- [Try it Yourself: tryhtml_script](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_script)
- [Try it Yourself: tryhtml_script_html](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_script_html)
- [Try it Yourself: tryhtml_script_styles](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_script_styles)
- [Try it Yourself: tryhtml_script_attribute](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_script_attribute)
- [Try it Yourself: tryhtml_noscript](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_noscript)
- [JavaScript Tutorial](https://www.w3schools.com/js/default.asp)
- [MDN: `<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
- [MDN: `<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)
