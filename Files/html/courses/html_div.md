# HTML Div

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

The **`<div>`** element is a **block-level container** for other HTML elements. This chapter shows a full-width `<div>`, grouping content, **centering** with `margin: auto`, **multiple** containers, and four ways to put divs **side by side**: **float**, **inline-block**, **flex**, and **grid**.

This section has **8** examples:

- [x] **Example 1:** Full-width break [View](#html-div-example-01)
- [x] **Example 2:** Container [View](#html-div-example-02)
- [x] **Example 3:** Center [View](#html-div-example-03)
- [x] **Example 4:** Multiple [View](#html-div-example-04)
- [x] **Example 5:** Float [View](#html-div-example-05)
- [x] **Example 6:** Inline-block [View](#html-div-example-06)
- [x] **Example 7:** Flex [View](#html-div-example-07)
- [x] **Example 8:** Grid [View](#html-div-example-08)

## Detailed Explanation

- [x] **Side by side — overview**
  - Pages often need two or more divs **in a row**.
  - Common CSS methods: **float**, **inline-block**, **flex**, **grid**.

<a id="html-div-example-01"></a>

### **Example 1: Full-width break**

- [x] **The `<div>` element**
  - Used as a **container** for other HTML elements.
  - Default: **block** — takes **all available width**, with **line breaks** before and after.
  - Example: `Lorem Ipsum <div>I am a div</div> dolor sit amet.` renders as three lines because the div breaks the sentence.
  - No required attributes; **`style`**, **`class`**, and **`id`** are common.

Sandbox: `code_sandbox/html-div/index.html`

```html
Lorem Ipsum
<div>I am a div</div>
dolor sit amet.
```

<img alt="html-div full-width source" src="../code_sandbox/snaps/html-div-code.png" />

<img alt="html-div full-width result" src="../code_sandbox/snaps/html-div-result.png" />

- [x] **Outcome:** Example: `Lorem Ipsum <div>I am a div</div> dolor sit amet.` renders as three lines because the div breaks the sentence.

<a id="html-div-example-02"></a>

### **Example 2: Container**

- [x] **`<div>` as a container**
  - Often used to **group sections** of a page.
  - Example: heading **London** plus two paragraphs inside one `<div>`.
  - Sandbox: `container.html`.

Sandbox: `code_sandbox/html-div/container.html`

```html
<div>
  <h2>London</h2>
  <p>London is the capital city of England.</p>
  <p>London has over 9 million inhabitants.</p>
</div>
```

<img alt="html-div container source" src="../code_sandbox/snaps/html-div-01-code.png" />

<img alt="html-div container result" src="../code_sandbox/snaps/html-div-01-result.png" />

- [x] **Outcome:** the browser shows **London**, **London is the capital city of England.**, **London has over 9 million inhabitants.**.

<a id="html-div-example-03"></a>

### **Example 3: Center**

- [x] **Center-align a `<div>`**
  - If the div is **not 100% wide**, set CSS **`margin: auto`** to center it.
  - Example: `div { width: 300px; margin: auto; }`.
  - Sandbox: `center.html`.

Sandbox: `code_sandbox/html-div/center.html`

```css
div {
  width: 300px;
  margin: auto;
}
```

<img alt="html-div center source" src="../code_sandbox/snaps/html-div-02-code.png" />

<img alt="html-div centered result" src="../code_sandbox/snaps/html-div-02-result.png" />

- [x] **Outcome:** the browser shows **div { width: 300px; margin: auto; }**.

<a id="html-div-example-04"></a>

### **Example 4: Multiple**

- [x] **Multiple `<div>` elements**
  - You can have **many** `<div>` containers on the same page.
  - Example: London, Oslo, and Rome stacked as three separate divs.
  - Sandbox: `multiple.html`.

Sandbox: `code_sandbox/html-div/multiple.html`

```html
<div><!-- London --></div>
<div><!-- Oslo --></div>
<div><!-- Rome --></div>
```

<img alt="html-div multiple source" src="../code_sandbox/snaps/html-div-03-code.png" />

<img alt="html-div multiple result" src="../code_sandbox/snaps/html-div-03-result.png" />

- [x] **Outcome:** the page demonstrates **Multiple** as shown in the result snap.

<a id="html-div-example-05"></a>

### **Example 5: Float**

- [x] **Float**
  - `float` was not originally for aligning divs, but has been used that way for years.
  - Positions content **horizontally** instead of only vertically.
  - Wrap columns in `.mycontainer` with `width: 100%; overflow: auto;` and `float: left; width: 33%;` on the inner divs.
  - Sandbox: `float.html`.

Sandbox: `code_sandbox/html-div/float.html`

```css
.mycontainer {
  width: 100%;
  overflow: auto;
}
.mycontainer div {
  width: 33%;
  float: left;
}
```

<img alt="html-div float source" src="../code_sandbox/snaps/html-div-04-code.png" />

<img alt="html-div float result" src="../code_sandbox/snaps/html-div-04-result.png" />

- [x] **Outcome:** the browser shows **.mycontainer { width: 100%; overflow: auto; } .mycontainer div { width: 33%; float: left; }**.

<a id="html-div-example-06"></a>

### **Example 6: Inline-block**

- [x] **Inline-block**
  - Change `display` from **block** to **`inline-block`**.
  - The div **no longer adds a line break** before and after, so siblings sit **side by side**.
  - Example: `div { width: 30%; display: inline-block; }`.
  - Sandbox: `inline-block.html`.

Sandbox: `code_sandbox/html-div/inline-block.html`

```css
div {
  width: 30%;
  display: inline-block;
}
```

<img alt="html-div inline-block source" src="../code_sandbox/snaps/html-div-05-code.png" />

<img alt="html-div inline-block result" src="../code_sandbox/snaps/html-div-05-result.png" />

- [x] **Outcome:** the browser shows **div { width: 30%; display: inline-block; }**.

<a id="html-div-example-07"></a>

### **Example 7: Flex**

- [x] **Flex**
  - **Flexbox** is for flexible responsive layout **without float or positioning**.
  - Surround the column divs with a container and set **`display: flex`**.
  - Example: `.mycontainer { display: flex; }` and `.mycontainer > div { width: 33%; }`.
  - Sandbox: `flex.html`.

Sandbox: `code_sandbox/html-div/flex.html`

```css
.mycontainer {
  display: flex;
}
.mycontainer > div {
  width: 33%;
}
```

<img alt="html-div flex source" src="../code_sandbox/snaps/html-div-06-code.png" />

<img alt="html-div flex result" src="../code_sandbox/snaps/html-div-06-result.png" />

- [x] **Outcome:** the browser shows **.mycontainer { display: flex; } .mycontainer > div { width: 33%; }**.

<a id="html-div-example-08"></a>

### **Example 8: Grid**

- [x] **Grid**
  - **CSS Grid** is rows and columns without floats/positioning.
  - Similar to flex, but you can define **more than one row** and position each row.
  - Surround columns with a grid container and set **column widths**.
  - Example: `.grid-container { display: grid; grid-template-columns: 33% 33% 33%; }`.
  - Sandbox: `grid.html`.
    | Tag | Description |
    | ------- | --------------------------------------------- |
    | `<div>` | Defines a section in a document (block-level) |

Sandbox: `code_sandbox/html-div/grid.html`

```css
.grid-container {
  display: grid;
  grid-template-columns: 33% 33% 33%;
}
```

<img alt="html-div grid source" src="../code_sandbox/snaps/html-div-07-code.png" />

<img alt="html-div grid result" src="../code_sandbox/snaps/html-div-07-result.png" />

- [x] **Outcome:** the browser shows **.grid-container { display: grid; grid-template-columns: 33% 33% 33%; }**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-div/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a `<div>` for, and what is its default display?

<details>
<summary>Answer</summary>

- [x] A **container** for other HTML elements.
- [x] Default **block**: full width, line breaks before and after.

</details>

### Question 2: Which attributes are common on `<div>`?

<details>
<summary>Answer</summary>

- [x] **`style`**, **`class`**, and **`id`**.
- [x] None are required.

</details>

### Question 3: How do you center a `<div>` that is not 100% wide?

<details>
<summary>Answer</summary>

- [x] Set CSS **`margin: auto`**.
- [x] Example: `width: 300px; margin: auto;`.

</details>

### Question 4: Why does `Lorem Ipsum <div>I am a div</div> dolor sit amet.` become three lines?

<details>
<summary>Answer</summary>

- [x] The `<div>` is **block-level**.
- [x] It inserts **line breaks** before and after.

</details>

### Question 5: Which four CSS methods does this chapter use to put divs side by side?

<details>
<summary>Answer</summary>

- [x] **Float**.
- [x] **Inline-block**.
- [x] **Flex**.
- [x] **Grid**.

</details>

### Question 6: How does `display: inline-block` change a div?

<details>
<summary>Answer</summary>

- [x] It **stops** adding a line break before and after.
- [x] Sibling divs can sit **side by side**.

</details>

### Question 7: What extra wrapper do flex and grid need?

<details>
<summary>Answer</summary>

- [x] An outer `<div>` that is the **flex** or **grid** container.
- [x] Flex: `display: flex`. Grid: `display: grid` plus **column widths**.

</details>

### Question 8: How does grid differ from flex in this chapter?

<details>
<summary>Answer</summary>

- [x] Grid can define **more than one row**.
- [x] You can **position each row** individually.

</details>

</details>

## Summary

`<div>` is a full-width block container for grouping page sections. Center a narrower div with `margin: auto`. Use many divs on one page. To place them in a row, use float, `inline-block`, flexbox (`display: flex` on a wrapper), or grid (`display: grid` and `grid-template-columns`).

## References

- [HTML Div Element (W3Schools)](https://www.w3schools.com/html/html_div.asp)
- [Try it Yourself: tryhtml_div1](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_div1)
- [Try it Yourself: tryhtml_div2](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_div2)
- [Try it Yourself: tryhtml_div3](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_div3)
- [Try it Yourself: tryhtml_div4](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_div4)
- [Try it Yourself: tryhtml_div_float](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_div_float)
- [Try it Yourself: tryhtml_div_inline-block](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_div_inline-block)
- [Try it Yourself: tryhtml_div_flex](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_div_flex)
- [Try it Yourself: tryhtml_div_grid](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_div_grid)
- [CSS Float](https://www.w3schools.com/css/css_float.asp)
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp)
- [CSS Grid](https://www.w3schools.com/css/css_grid.asp)
- [MDN: `<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
