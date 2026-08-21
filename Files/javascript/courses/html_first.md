# HTML First

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

HTML-First builds pages so HTML (and CSS) already work. JavaScript is added later, only when the browser cannot do the job natively.

This section has **8** examples:

- [x] **Example 1:** A page that works without JavaScript [View](#html-first-example-01)
- [x] **Example 2:** Avoid unnecessary JavaScript [View](#html-first-example-02)
- [x] **Example 3:** Progressive enhancement — form without JavaScript [View](#html-first-example-03)
- [x] **Example 4:** Why HTML-First is not “no JavaScript” [View](#html-first-example-04)
- [x] **Example 5:** Browsers already understand details/summary [View](#html-first-example-05)
- [x] **Example 6:** HTML is visible before JavaScript loads [View](#html-first-example-06)
- [x] **Example 7:** Semantic HTML improves accessibility [View](#html-first-example-07)
- [x] **Example 8:** When JavaScript is still useful [View](#html-first-example-08)

## Detailed Explanation

- [x] Related to progressive enhancement.
- [x] Less JS can mean faster, more accessible, more reliable pages.
- [x] Semantic HTML and native widgets (`details`, forms) come first.

<a id="html-first-example-01"></a>

### **Example 1: A page that works without JavaScript**

- [x] HTML-First means **HTML is the foundation**. The page should be readable and usable with basic HTML and CSS.
- [x] This is the same idea as **progressive enhancement**: start with a working document, then add JS.
- [x] The example is a heading + paragraph — no script required for the content to appear.

Sandbox: `code_sandbox/html-first/works-without-js.html`

```html
<!doctype html>
<html>
<body>
  <h1>HTML First</h1>
  <p>Welcome This page works without JavaScript.</p>
</body>
</html>
```

<img alt="html-first example 1 source" src="../code_sandbox/snaps/html-first-01-code.png" />

<img alt="html-first example 1 result" src="../code_sandbox/snaps/html-first-01-result.png" />

- [x] **Outcome:** The heading **HTML First** and the welcome paragraph render with **zero** script.

<a id="html-first-example-02"></a>

### **Example 2: Avoid unnecessary JavaScript**

- [x] JS is powerful, but extra JS makes sites **slower** and harder to maintain.
- [x] HTML-first can improve page speed, accessibility, SEO, maintainability, and reliability.
- [x] Ask: can native HTML/CSS do this? If yes, skip the library.

Sandbox: `code_sandbox/html-first/avoid-unnecessary-js.html`

```html
<p>Benefits: speed, accessibility, search, maintainability, reliability.</p>
```

<img alt="html-first example 2 source" src="../code_sandbox/snaps/html-first-02-code.png" />

<img alt="html-first example 2 result" src="../code_sandbox/snaps/html-first-02-result.png" />

- [x] **Outcome:** The snapshot lists the five benefits from the W3Schools page.

<a id="html-first-example-03"></a>

### **Example 3: Progressive enhancement — form without JavaScript**

- [x] An HTML form should **still submit** if JS fails.
- [x] `type="email"` + `required` give built-in checks with **no script**.
- [x] The W3Schools Subscribe form uses native validation only.

Sandbox: `code_sandbox/html-first/form-html-validation.html`

```html
<form action="#" method="post">
  <label>Email: <input type="email" name="email" required></label>
  <button type="submit">Subscribe</button>
</form>
```

<img alt="html-first example 3 source" src="../code_sandbox/snaps/html-first-03-code.png" />

<img alt="html-first example 3 result" src="../code_sandbox/snaps/html-first-03-result.png" />

- [x] **Outcome:** Empty email: `checkValidity()` is **false**. Filling a valid email would allow submit even with JS disabled.

<a id="html-first-example-04"></a>

### **Example 4: Why HTML-First is not “no JavaScript”**

- [x] HTML-first is **not** rejecting JS. It is using **browser features first**.
- [x] Many UI pieces used to need JS and now exist as HTML/CSS.
- [x] Add JS when the browser cannot do the job natively.

Sandbox: `code_sandbox/html-first/not-rejecting-js.html`

```html
<p>HTML-first does not mean JavaScript never. It means HTML before JavaScript.</p>
```

<img alt="html-first example 4 source" src="../code_sandbox/snaps/html-first-04-code.png" />

<img alt="html-first example 4 result" src="../code_sandbox/snaps/html-first-04-result.png" />

- [x] **Outcome:** The note prints the W3Schools line: HTML **before** JavaScript.

<a id="html-first-example-05"></a>

### **Example 5: Browsers already understand details/summary**

- [x] `<details>` / `<summary>` open and close **without JS**.
- [x] Also native: `<dialog>`, `<form>` validation, `<search>` (where supported).
- [x] This is “browsers are already powerful.”

Sandbox: `code_sandbox/html-first/details-native.html`

```html
<details>
  <summary>Click to read more</summary>
  This text can be opened and closed without JavaScript.
</details>
```

<img alt="html-first example 5 source" src="../code_sandbox/snaps/html-first-05-code.png" />

<img alt="html-first example 5 result" src="../code_sandbox/snaps/html-first-05-result.png" />

- [x] **Outcome:** `details` is in the document; opening it is a **user/browser** behavior, not a script.

<a id="html-first-example-06"></a>

### **Example 6: HTML is visible before JavaScript loads**

- [x] The browser can **paint HTML** as it arrives.
- [x] Users may start reading before scripts finish. That matters on slow phones.
- [x] Tutorials, articles, product pages, docs, and forms often need nothing more for first paint.

Sandbox: `code_sandbox/html-first/html-before-scripts-load.html`

```html
<article>
  <h1>Article title</h1>
  <p>Readable immediately.</p>
</article>
<script src="app.js" defer></script>
```

<img alt="html-first example 6 source" src="../code_sandbox/snaps/html-first-06-code.png" />

<img alt="html-first example 6 result" src="../code_sandbox/snaps/html-first-06-result.png" />

- [x] **Outcome:** The article text is in the DOM even if `app.js` is slow or missing.

<a id="html-first-example-07"></a>

### **Example 7: Semantic HTML improves accessibility**

- [x] Use elements for their **meaning**: `<header>`, `<main>`, `<article>`, `<nav>`, `<button>` — not empty `<div>` soup.
- [x] Screen readers, search engines, and keyboard users get a real outline.
- [x] W3Schools: “Use meaningful HTML first.”

Sandbox: `code_sandbox/html-first/semantic-html.html`

```html
<main>
  <article>
    <h1>Use meaningful HTML first.</h1>
  </article>
</main>
```

<img alt="html-first example 7 source" src="../code_sandbox/snaps/html-first-07-code.png" />

<img alt="html-first example 7 result" src="../code_sandbox/snaps/html-first-07-result.png" />

- [x] **Outcome:** `querySelector("article h1")` finds the heading because the markup is **semantic**, not a generic div.

<a id="html-first-example-08"></a>

### **Example 8: When JavaScript is still useful**

- [x] JS is still the right tool for **logic**, live data, storage, and talking to servers.
- [x] The rule is: add it **when it is needed**, not before.
- [x] HTML-first = HTML **before** JS, not HTML **instead of** JS forever.

Sandbox: `code_sandbox/html-first/when-js-useful.html`

```html
<button type="button" id="b">Load extra (needs JS)</button>
<p id="out">Base content always here.</p>
```

<img alt="html-first example 8 source" src="../code_sandbox/snaps/html-first-08-code.png" />

<img alt="html-first example 8 result" src="../code_sandbox/snaps/html-first-08-result.png" />

- [x] **Outcome:** Base content is visible without the click. JS only fills the extra line when the button is used.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/html-first/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is HTML-First?

<details>
<summary>Answer</summary>

- [x] Build so the page works with **HTML (and CSS)** as the foundation; JS is extra.

</details>

### Question 2: Is it the same as progressive enhancement?

<details>
<summary>Answer</summary>

- [x] **Closely related** — start with a working basic page, then enhance.

</details>

### Question 3: Name two benefits of less JS.

<details>
<summary>Answer</summary>

- [x] Any two of: **speed**, **accessibility**, **SEO**, **maintainability**, **reliability**.

</details>

### Question 4: Should a form work if JS fails?

<details>
<summary>Answer</summary>

- [x] **Yes** — native `action` + `required` / `type=email` still function.

</details>

### Question 5: Does HTML-first mean never write JavaScript?

<details>
<summary>Answer</summary>

- [x] **No** — it means HTML **before** JavaScript.

</details>

### Question 6: Which element toggles extra text with no script?

<details>
<summary>Answer</summary>

- [x] **`<details>`** + **`<summary>`**.

</details>

### Question 7: Why can users read before scripts finish?

<details>
<summary>Answer</summary>

- [x] HTML is **parsed and painted** as it arrives; JS must download and run.

</details>

### Question 8: What is semantic HTML?

<details>
<summary>Answer</summary>

- [x] Using tags for **meaning** (`article`, `nav`, `button`) instead of anonymous divs.

</details>

### Question 9: When is JS still the right tool?

<details>
<summary>Answer</summary>

- [x] **Logic**, data, storage, server communication, widgets HTML cannot provide.

</details>

### Question 10: What question should you ask first?

<details>
<summary>Answer</summary>

- [x] **Can the browser already do this?**

</details>


</details>

## Summary

Ship a usable HTML document first. Enhance with CSS, then JS. Do not start with a framework when a form or article only needs markup.

## References

- [HTML First](https://www.w3schools.com/js/js_htmlfirst.asp)
- [MDN Progressive enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement)
