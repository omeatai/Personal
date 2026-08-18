<details>
  <summary>HTML First CSS</summary>

## Introduction

After HTML, CSS handles hover, transitions, simple menus, responsive layout, and animations so you often do not need JavaScript for visual behavior.

This section has **6** examples:

- [x] **Example 1:** Hover effects with :hover [View](#html-first-css-example-01)
- [x] **Example 2:** CSS transitions [View](#html-first-css-example-02)
- [x] **Example 3:** Show and hide content with CSS (menu) [View](#html-first-css-example-03)
- [x] **Example 4:** Responsive layouts with media queries [View](#html-first-css-example-04)
- [x] **Example 5:** CSS animations — spinner [View](#html-first-css-example-05)
- [x] **Example 6:** When CSS is enough vs when you need JavaScript [View](#html-first-css-example-06)

## Detailed Explanation

- [x] :hover, transition, display toggling, grid + media queries, @keyframes.
- [x] Visual problems → CSS first.
- [x] Logic/data/network → JavaScript.

<a id="html-first-css-example-01"></a>

### **Example 1: Hover effects with :hover**

- [x] `:hover` changes an element when the pointer is over it — **no JS**.
- [x] W3Schools button goes from `#04AA6D` to `#059862`.
- [x] The snapshot adds class `forced` so the result image shows the hover colors (headless has no pointer).

Sandbox: `code_sandbox/html-first-css/hover.html`

```css
button:hover { background-color:#059862; }
<button>Hover Over Me</button>
```

<img alt="html-first-css example 1 source" src="./code_sandbox/snaps/html-first-css-01-code.png" />

<img alt="html-first-css example 1 result" src="./code_sandbox/snaps/html-first-css-01-result.png" />

- [x] **Outcome:** Forced hover style: background is the darker **#059862** green.

<a id="html-first-css-example-02"></a>

### **Example 2: CSS transitions**

- [x] `transition:width 0.5s` animates width changes smoothly.
- [x] Hover (or a class) sets `width:200px`; the browser tweens from 100px.
- [x] No `setInterval` — this is the CSS alternative to the DOM Animations chapter.

Sandbox: `code_sandbox/html-first-css/transition.html`

```css
 .box { width:100px; height:100px; background-color:#04AA6D; transition:width 0.5s; }
 .box:hover { width:200px; }
```

<img alt="html-first-css example 2 source" src="./code_sandbox/snaps/html-first-css-02-code.png" />

<img alt="html-first-css example 2 result" src="./code_sandbox/snaps/html-first-css-02-result.png" />

- [x] **Outcome:** With `.forced`, computed width is **200px** (end of the hover transition).

<a id="html-first-css-example-03"></a>

### **Example 3: Show and hide content with CSS (menu)**

- [x] `.menu-content { display:none }` then `.menu:hover .menu-content { display:block }`.
- [x] Simple menus/dropdowns without JS. Keyboard users may still need a focus-based variant (`:focus-within`).
- [x] The snapshot forces the open state so **Link 1 / Link 2** are visible.

Sandbox: `code_sandbox/html-first-css/show-hide.html`

```css
 .menu-content { display:none; }
 .menu:hover .menu-content { display:block; }
<div class="menu">Menu
  <div class="menu-content">Link 1<br>Link 2</div>
</div>
```

<img alt="html-first-css example 3 source" src="./code_sandbox/snaps/html-first-css-03-code.png" />

<img alt="html-first-css example 3 result" src="./code_sandbox/snaps/html-first-css-03-result.png" />

- [x] **Outcome:** Forced open menu: the content `display` is **block** and the links are in the tree.

<a id="html-first-css-example-04"></a>

### **Example 4: Responsive layouts with media queries**

- [x] CSS Grid `1fr 1fr 1fr` becomes **one column** at `max-width:600px`.
- [x] No JS breakpoint listeners (`matchMedia` is optional, not required).
- [x] The snapshot reports the computed `grid-template-columns` at this window size (900px wide chrome → three columns).

Sandbox: `code_sandbox/html-first-css/responsive-grid.html`

```css
 .container { display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; }
 @media (max-width:600px) {
   .container { grid-template-columns:1fr; }
 }
```

<img alt="html-first-css example 4 source" src="./code_sandbox/snaps/html-first-css-04-code.png" />

<img alt="html-first-css example 4 result" src="./code_sandbox/snaps/html-first-css-04-result.png" />

- [x] **Outcome:** At 900px screenshot width the grid stays **three columns**. Shrink below 600px and it becomes one (the media query).

<a id="html-first-css-example-05"></a>

### **Example 5: CSS animations — spinner**

- [x] `@keyframes spin` + `animation: spin 1s linear infinite` rotates forever **without JS**.
- [x] This is the CSS answer to a loading indicator.
- [x] The snapshot waits so you can see the spinner mid-rotation.

Sandbox: `code_sandbox/html-first-css/css-animation.html`

```css
 .spinner {
   width:40px; height:40px;
   border:6px solid #ddd;
   border-top:6px solid #04AA6D;
   border-radius:50%;
   animation:spin 1s linear infinite;
 }
 @keyframes spin { to { transform:rotate(360deg); } }
```

<img alt="html-first-css example 5 source" src="./code_sandbox/snaps/html-first-css-05-code.png" />

<img alt="html-first-css example 5 result" src="./code_sandbox/snaps/html-first-css-05-result.png" />

- [x] **Outcome:** Computed `animation-name` is **spin** and the box is a 40px circle.

<a id="html-first-css-example-06"></a>

### **Example 6: When CSS is enough vs when you need JavaScript**

- [x] CSS is enough for **visual** change: color, size, spacing, layout, motion, simple show/hide.
- [x] JavaScript is for **logic**, data, storage, and server communication.
- [x] W3Schools: “If the problem is visual, try CSS first.”

Sandbox: `code_sandbox/html-first-css/when-css-enough.html`

```html
<p>Visual → CSS. Logic/data/network → JS.</p>
```

<img alt="html-first-css example 6 source" src="./code_sandbox/snaps/html-first-css-06-code.png" />

<img alt="html-first-css example 6 result" src="./code_sandbox/snaps/html-first-css-06-result.png" />

- [x] **Outcome:** The snapshot prints the split: **visual → CSS**, **logic → JS**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/html-first-css/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you restyle a button on hover without JS?

<details>
<summary>Answer</summary>

- [x] A **`:hover`** rule.

</details>

### Question 2: What property animates the box width?

<details>
<summary>Answer</summary>

- [x] **`transition: width 0.5s`** (plus a hover width).

</details>

### Question 3: How does the CSS menu show links?

<details>
<summary>Answer</summary>

- [x] `.menu:hover .menu-content { display:block }` after hiding with **`display:none`**.

</details>

### Question 4: How do you change columns for small screens?

<details>
<summary>Answer</summary>

- [x] A **`@media (max-width:600px)`** rule that sets **one** grid column.

</details>

### Question 5: Does the spinner use `setInterval`?

<details>
<summary>Answer</summary>

- [x] **No** — **`@keyframes`** + the **`animation`** property.

</details>

### Question 6: When is CSS the right tool?

<details>
<summary>Answer</summary>

- [x] When the change is **visual** (color, layout, motion, simple hide).

</details>

### Question 7: When is JS required?

<details>
<summary>Answer</summary>

- [x] **Logic**, data, **storage**, or **server** communication.

</details>

### Question 8: What is the page’s closing advice?

<details>
<summary>Answer</summary>

- [x] If the problem is visual, **try CSS first**.

</details>

### Question 9: Why force a `.forced` class in the sandbox?

<details>
<summary>Answer</summary>

- [x] Headless screenshots have **no pointer**, so `:hover` would not apply; the class duplicates the hover rule.

</details>

### Question 10: Can CSS replace `myMove()` from DOM Animations?

<details>
<summary>Answer</summary>

- [x] For many motions **yes** — transitions/animations. JS timers are for logic-driven motion.

</details>


</details>

## Summary

If the change is visual, write CSS. Save JavaScript for behavior that CSS cannot express.

## References

- [HTML First CSS](https://www.w3schools.com/js/js_htmlfirst_css.asp)
- [MDN Progressive enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement)

</details>
