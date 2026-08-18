<details>
  <summary>Changing CSS</summary>

## Introduction

JavaScript sets inline CSS through `element.style.property`. Clicks can restyle or hide nodes.

This section has **4** examples:

- [x] **Example 1:** Change a paragraph’s color [View](#changing-css-example-01)
- [x] **Example 2:** Change style when a button is clicked [View](#changing-css-example-02)
- [x] **Example 3:** Make an element invisible with display:none [View](#changing-css-example-03)
- [x] **Example 4:** HTML DOM Style object (inline only) [View](#changing-css-example-04)

## Detailed Explanation

- [x] Use camelCase CSS names on `element.style`.
- [x] Events (click) are a natural time to change styles.
- [x] `display:none` hides a node without deleting it.

<a id="changing-css-example-01"></a>

### **Example 1: Change a paragraph’s color**

- [x] Syntax: `document.getElementById(id).style.property = new style`.
- [x] `style.color = "blue"` sets the CSS **color** as an inline style.
- [x] Property names in JS drop the hyphen: `background-color` → `backgroundColor`.

Sandbox: `code_sandbox/changing-css/style-color.html`

```html
<p id="p2">Hello World!</p>
<script>
document.getElementById("p2").style.color = "blue";
</script>
```

<img alt="changing-css example 1 source" src="./code_sandbox/snaps/changing-css-01-code.png" />

<img alt="changing-css example 1 result" src="./code_sandbox/snaps/changing-css-01-result.png" />

- [x] **Outcome:** The paragraph is **blue**. `style.color` reports the inline value.

<a id="changing-css-example-02"></a>

### **Example 2: Change style when a button is clicked**

- [x] The DOM can run code when **events** happen: click, load, input change.
- [x] This example sets `#id1` to red **fontSize 40px** when the button is clicked.
- [x] The snapshot calls `.click()` so the result image shows the styled heading.

Sandbox: `code_sandbox/changing-css/style-on-click.html`

```html
<h1 id="id1">My Heading 1</h1>
<button type="button" onclick="document.getElementById('id1').style.color='red'; document.getElementById('id1').style.fontSize='40px';">
  Click Me!
</button>
```

<img alt="changing-css example 2 source" src="./code_sandbox/snaps/changing-css-02-code.png" />

<img alt="changing-css example 2 result" src="./code_sandbox/snaps/changing-css-02-result.png" />

- [x] **Outcome:** After the click, the heading is **red** and **40px**.

<a id="changing-css-example-03"></a>

### **Example 3: Make an element invisible with display:none**

- [x] `style.display = "none"` removes the element from layout (it does not delete the node).
- [x] `style.display = "block"` (or `""` to revert) shows it again.
- [x] `visibility: hidden` hides it but **keeps the gap**. `display:none` collapses the gap.

Sandbox: `code_sandbox/changing-css/hide-element.html`

```html
<p id="hide">I can vanish</p>
<button type="button" id="btn">Click Me!</button>
<script>
document.getElementById("btn").onclick = function () {
  document.getElementById("hide").style.display = "none";
};
</script>
```

<img alt="changing-css example 3 source" src="./code_sandbox/snaps/changing-css-03-code.png" />

<img alt="changing-css example 3 result" src="./code_sandbox/snaps/changing-css-03-result.png" />

- [x] **Outcome:** After click, `#hide` has **display:none** and is not visible in the result snap.

<a id="changing-css-example-04"></a>

### **Example 4: HTML DOM Style object (inline only)**

- [x] Every element has a **`style`** object. Assigning properties writes **inline** CSS.
- [x] It does not list rules from your stylesheet. Use `getComputedStyle(el)` for the used value.
- [x] Full property list: CSSStyleDeclaration / HTML DOM Style Object Reference on W3Schools.

Sandbox: `code_sandbox/changing-css/style-object-ref.html`

```html
<p id="box">box</p>
<script>
const el = document.getElementById("box");
el.style.backgroundColor = "gold";
const used = getComputedStyle(el).backgroundColor;
</script>
```

<img alt="changing-css example 4 source" src="./code_sandbox/snaps/changing-css-04-code.png" />

<img alt="changing-css example 4 result" src="./code_sandbox/snaps/changing-css-04-result.png" />

- [x] **Outcome:** Inline `backgroundColor` is **gold**; `getComputedStyle` returns the computed rgb color.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/changing-css/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the CSS-from-JS syntax?

<details>
<summary>Answer</summary>

- [x] `document.getElementById(id).style.property = new style`.

</details>

### Question 2: How is `background-color` written in JavaScript?

<details>
<summary>Answer</summary>

- [x] **`backgroundColor`** (camelCase).

</details>

### Question 3: Does `element.style` include stylesheet rules?

<details>
<summary>Answer</summary>

- [x] No — **inline** styles only. Use **`getComputedStyle`**.

</details>

### Question 4: What event did the heading example use?

<details>
<summary>Answer</summary>

- [x] A **click** on the button (`onclick`).

</details>

### Question 5: What does `display = "none"` do?

<details>
<summary>Answer</summary>

- [x] The element is not rendered and **does not take up space**.

</details>

### Question 6: How is that different from `visibility: hidden`?

<details>
<summary>Answer</summary>

- [x] Hidden still **occupies layout space**; `display:none` does not.

</details>

### Question 7: Can you change `fontSize` from JS?

<details>
<summary>Answer</summary>

- [x] Yes — `style.fontSize = "40px"` (include the unit).

</details>

### Question 8: Why include `'px'`?

<details>
<summary>Answer</summary>

- [x] Most CSS length properties need a unit. `fontSize = 40` is invalid / ignored.

</details>

### Question 9: Is the node deleted when display is none?

<details>
<summary>Answer</summary>

- [x] No — it stays in the DOM. You can show it again.

</details>

### Question 10: Where do you look up every style property name?

<details>
<summary>Answer</summary>

- [x] The **HTML DOM Style Object** reference (CSSStyleDeclaration).

</details>


</details>

## Summary

`style` writes inline CSS. Combine it with events to restyle or hide elements on demand.

## References

- [Changing CSS](https://www.w3schools.com/js/js_htmldom_css.asp)
- [MDN Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)

</details>
