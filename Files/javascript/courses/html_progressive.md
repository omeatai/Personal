# HTML Progressive

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Progressive enhancement starts with a working basic page, then adds CSS and JS. Graceful degradation starts fancy and tries to cope with older browsers.

This section has **9** examples:

- [x] **Example 1:** Start with HTML — a working form [View](#html-progressive-example-01)
- [x] **Example 2:** Add CSS for better design [View](#html-progressive-example-02)
- [x] **Example 3:** Add JavaScript as an enhancement [View](#html-progressive-example-03)
- [x] **Example 4:** Why progressive enhancement matters [View](#html-progressive-example-04)
- [x] **Example 5:** Progressive Enhancement — starts simple [View](#html-progressive-example-05)
- [x] **Example 6:** Graceful Degradation — starts advanced [View](#html-progressive-example-06)
- [x] **Example 7:** PE adds features later vs GD removes unsupported ones [View](#html-progressive-example-07)
- [x] **Example 8:** PE focuses on accessibility; GD focuses on compatibility [View](#html-progressive-example-08)
- [x] **Example 9:** Modern HTML that used to need JavaScript [View](#html-progressive-example-09)

## Detailed Explanation

- [x] HTML → CSS → JS as layers.
- [x] PE starts simple and adds; GD starts advanced and strips.
- [x] Modern HTML (`required`, `details`, lazy images, CSS animation) makes PE easier.

<a id="html-progressive-example-01"></a>

### **Example 1: Start with HTML — a working form**

- [x] Step 1: meaningful HTML that works if CSS and JS **fail to load**.
- [x] The newsletter form still posts with a normal submit.
- [x] No script is required for the baseline.

Sandbox: `code_sandbox/html-progressive/start-html.html`

```html
<form action="#" method="post">
  <h2>Newsletter Signup</h2>
  <label>Email: <input type="email" name="email" required></label>
  <button type="submit">Join</button>
</form>
```

<img alt="html-progressive example 1 source" src="../code_sandbox/snaps/html-progressive-01-code.png" />

<img alt="html-progressive example 1 result" src="../code_sandbox/snaps/html-progressive-01-result.png" />

- [x] **Outcome:** The form is in the page and uses **required** + **email** with no JavaScript.

<a id="html-progressive-example-02"></a>

### **Example 2: Add CSS for better design**

- [x] Step 2: CSS improves **appearance** after the HTML already works.
- [x] W3Schools styles the button green with padding and no border.
- [x] If CSS fails, the form is still usable (unstyled).

Sandbox: `code_sandbox/html-progressive/add-css.html`

```css
button {
  background-color: #04AA6D;
  color: white;
  padding: 10px;
  border: none;
}
```

<img alt="html-progressive example 2 source" src="../code_sandbox/snaps/html-progressive-02-code.png" />

<img alt="html-progressive example 2 result" src="../code_sandbox/snaps/html-progressive-02-result.png" />

- [x] **Outcome:** Computed button background is the W3Schools **green** `#04AA6D`.

<a id="html-progressive-example-03"></a>

### **Example 3: Add JavaScript as an enhancement**

- [x] Step 3: JS can add instant feedback, but the form **must not depend** on it.
- [x] W3Schools `submit` listener `alert("Form submitted!")` — we print instead.
- [x] If this script does not load, native submit still works.

Sandbox: `code_sandbox/html-progressive/add-js-enhance.html`

```javascript
const form = document.querySelector("form");
form.addEventListener("submit", function () {
  alert("Form submitted!");
});
```

<img alt="html-progressive example 3 source" src="../code_sandbox/snaps/html-progressive-03-code.png" />

<img alt="html-progressive example 3 result" src="../code_sandbox/snaps/html-progressive-03-result.png" />

- [x] **Outcome:** Submit is enhanced: the log shows **Form submitted!** and `preventDefault` keeps the sandbox from navigating.

<a id="html-progressive-example-04"></a>

### **Example 4: Why progressive enhancement matters**

- [x] Users have different devices, browsers, speeds. Some **disable JS**.
- [x] Others use old browsers or assistive tech.
- [x] Tip from the page: test with **JavaScript disabled**.

Sandbox: `code_sandbox/html-progressive/why-matters.html`

```html
<p>Everybody should still access the content.</p>
```

<img alt="html-progressive example 4 source" src="../code_sandbox/snaps/html-progressive-04-code.png" />

<img alt="html-progressive example 4 result" src="../code_sandbox/snaps/html-progressive-04-result.png" />

- [x] **Outcome:** The snapshot records the testing tip: try the site with **JS off**.

<a id="html-progressive-example-05"></a>

### **Example 5: Progressive Enhancement — starts simple**

- [x] Table row: PE **starts simple** and adds features later.
- [x] Graceful degradation **starts advanced** and tries to keep old browsers working.
- [x] This example is the PE column: a plain form first.

Sandbox: `code_sandbox/html-progressive/pe-starts-simple.html`

```html
<form action="#"><button>Works with no extras</button></form>
```

<img alt="html-progressive example 5 source" src="../code_sandbox/snaps/html-progressive-05-code.png" />

<img alt="html-progressive example 5 result" src="../code_sandbox/snaps/html-progressive-05-result.png" />

- [x] **Outcome:** Baseline UI is a **plain HTML** form — PE starts simple.

<a id="html-progressive-example-06"></a>

### **Example 6: Graceful Degradation — starts advanced**

- [x] GD builds the **full** experience first, then tries to peel features off for weaker browsers.
- [x] That often leaves a worse baseline than PE.
- [x] Named contrast from the W3Schools table.

Sandbox: `code_sandbox/html-progressive/gd-starts-advanced.html`

```html
<div id="app">Imagine a JS-only SPA here</div>
```

<img alt="html-progressive example 6 source" src="../code_sandbox/snaps/html-progressive-06-code.png" />

<img alt="html-progressive example 6 result" src="../code_sandbox/snaps/html-progressive-06-result.png" />

- [x] **Outcome:** A JS-only shell is the **starts advanced** story — if JS fails, there may be nothing.

<a id="html-progressive-example-07"></a>

### **Example 7: PE adds features later vs GD removes unsupported ones**

- [x] PE: **add** features when the browser supports them (`@supports`, `required`, JS if present).
- [x] GD: **remove** or replace features that old browsers cannot handle.
- [x] Feature detection (`'open' in document.createElement('dialog')`) is a PE move.

Sandbox: `code_sandbox/html-progressive/pe-adds-later.html`

```html
<script>
const hasDialog = "showModal" in document.createElement("dialog");
</script>
```

<img alt="html-progressive example 7 source" src="../code_sandbox/snaps/html-progressive-07-code.png" />

<img alt="html-progressive example 7 result" src="../code_sandbox/snaps/html-progressive-07-result.png" />

- [x] **Outcome:** `showModal` in `HTMLDialogElement` is **true** in this browser — a feature we can add, not assume.

<a id="html-progressive-example-08"></a>

### **Example 8: PE focuses on accessibility; GD focuses on compatibility**

- [x] PE’s mindset is **everyone can use the content** (keyboard, AT, no-JS).
- [x] GD’s mindset is **make the fancy version limp along** on old engines.
- [x] Both mention compatibility, but the starting point differs.

Sandbox: `code_sandbox/html-progressive/pe-a11y-vs-gd-compat.html`

```html
<button type="button">Real button (accessible)</button>
<div role="button">Fake div button (harder)</div>
```

<img alt="html-progressive example 8 source" src="../code_sandbox/snaps/html-progressive-08-code.png" />

<img alt="html-progressive example 8 result" src="../code_sandbox/snaps/html-progressive-08-result.png" />

- [x] **Outcome:** A real **`<button>`** is the PE-friendly control; a clickable div is the “rebuild accessibility later” trap.

<a id="html-progressive-example-09"></a>

### **Example 9: Modern HTML that used to need JavaScript**

- [x] `required` validation, `<details>`, `loading="lazy"`, CSS animations — all used to be JS jobs.
- [x] That makes PE **easier** than a decade ago.
- [x] Reach for these before writing a widget library.

Sandbox: `code_sandbox/html-progressive/modern-html-helps.html`

```html
<details><summary>Native</summary>No JS accordion.</details>
<img alt="" loading="lazy" width="1" height="1" src="data:image/gif;base64,R0lGODlhAQABAAAAACw=">
```

<img alt="html-progressive example 9 source" src="../code_sandbox/snaps/html-progressive-09-code.png" />

<img alt="html-progressive example 9 result" src="../code_sandbox/snaps/html-progressive-09-result.png" />

- [x] **Outcome:** `details` and `loading="lazy"` are present as **native** features.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/html-progressive/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the first PE step?

<details>
<summary>Answer</summary>

- [x] **Meaningful HTML** that still works if CSS/JS fail.

</details>

### Question 2: What is the second step?

<details>
<summary>Answer</summary>

- [x] **CSS** for appearance.

</details>

### Question 3: What is the third step?

<details>
<summary>Answer</summary>

- [x] **JavaScript** as an enhancement, not a requirement.

</details>

### Question 4: Does the W3Schools submit alert replace the form?

<details>
<summary>Answer</summary>

- [x] No — if the script is missing the form **still works**.

</details>

### Question 5: How does PE start vs GD?

<details>
<summary>Answer</summary>

- [x] PE **starts simple**. GD **starts advanced**.

</details>

### Question 6: How do they treat features?

<details>
<summary>Answer</summary>

- [x] PE **adds** later. GD **removes** unsupported bits.

</details>

### Question 7: Where does PE put its focus?

<details>
<summary>Answer</summary>

- [x] **Accessibility** (everyone can use the content).

</details>

### Question 8: Where does GD put its focus?

<details>
<summary>Answer</summary>

- [x] **Compatibility** with older/weaker clients.

</details>

### Question 9: Name a modern HTML feature that replaced a JS widget.

<details>
<summary>Answer</summary>

- [x] **`required`**, **`<details>`**, **`loading="lazy"`**, or **CSS animation**.

</details>

### Question 10: What does W3Schools tell you to try?

<details>
<summary>Answer</summary>

- [x] Test the site with **JavaScript disabled**.

</details>


</details>

## Summary

Build the usable core in HTML, dress it with CSS, and treat JS as an optional layer. Prefer PE’s “start simple” over a JS-only shell.

## References

- [HTML Progressive](https://www.w3schools.com/js/js_htmlfirst_progressive.asp)
- [MDN Progressive enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement)
