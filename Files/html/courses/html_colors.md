# HTML Colors

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

HTML colors are specified with **predefined color names**, or with **RGB**, **HEX**, **HSL**, **RGBA**, or **HSLA** values. This chapter shows named colors on backgrounds, then the same idea for **text** and **borders**, and finally the numeric color-value forms (including 50% transparency).

This section has **5** examples:

- [x] **Example 1:** Color names [View](#html-colors-example-01)
- [x] **Example 2:** Background color [View](#html-colors-example-02)
- [x] **Example 3:** Text color [View](#html-colors-example-03)
- [x] **Example 4:** Border color [View](#html-colors-example-04)
- [x] **Example 5:** Color values [View](#html-colors-example-05)

## Detailed Explanation

<a id="html-colors-example-01"></a>

### **Example 1: Color names**

- [x] **Color names**
  - A color can be a **name** such as Tomato, Orange, DodgerBlue, MediumSeaGreen, Gray, SlateBlue, Violet, LightGray.
  - HTML supports **140 standard color names**.

Sandbox: `code_sandbox/html-colors/index.html`

```html
<h1 style="background-color:Tomato;">Tomato</h1>
<h1 style="background-color:Orange;">Orange</h1>
<h1 style="background-color:DodgerBlue;">DodgerBlue</h1>
<h1 style="background-color:MediumSeaGreen;">MediumSeaGreen</h1>
<h1 style="background-color:Gray;">Gray</h1>
<h1 style="background-color:SlateBlue;">SlateBlue</h1>
<h1 style="background-color:Violet;">Violet</h1>
<h1 style="background-color:LightGray;">LightGray</h1>
```

<img alt="html-colors names source" src="../code_sandbox/snaps/html-colors-code.png" />

<img alt="html-colors names result" src="../code_sandbox/snaps/html-colors-result.png" />

- [x] **Outcome:** the browser shows **Tomato**, **Orange**, **DodgerBlue**, **MediumSeaGreen**, **Gray**.

<a id="html-colors-example-02"></a>

### **Example 2: Background color**

- [x] **Background color**
  - Set an element’s background with `style="background-color:…"` (DodgerBlue heading, Tomato paragraph).

Sandbox: `code_sandbox/html-colors/background.html`

```html
<h1 style="background-color:DodgerBlue;">Hello World</h1>

<p style="background-color:Tomato;">
  Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy
  nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi
  enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis
  nisl ut aliquip ex ea commodo consequat.
</p>
```

<img alt="html-colors background source" src="../code_sandbox/snaps/html-colors-01-code.png" />

<img alt="html-colors background result" src="../code_sandbox/snaps/html-colors-01-result.png" />

- [x] **Outcome:** the browser shows **Hello World**, **Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.**.

<a id="html-colors-example-03"></a>

### **Example 3: Text color**

- [x] **Text color**
  - Set text with `style="color:…"` (Tomato heading, DodgerBlue and MediumSeaGreen paragraphs).

Sandbox: `code_sandbox/html-colors/text.html`

```html
<h3 style="color:Tomato;">Hello World</h3>

<p style="color:DodgerBlue;">
  Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy
  nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
</p>

<p style="color:MediumSeaGreen;">
  Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit
  lobortis nisl ut aliquip ex ea commodo consequat.
</p>
```

<img alt="html-colors text source" src="../code_sandbox/snaps/html-colors-02-code.png" />

<img alt="html-colors text result" src="../code_sandbox/snaps/html-colors-02-result.png" />

- [x] **Outcome:** the browser shows **Hello World**, **Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.**, **Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.**.

<a id="html-colors-example-04"></a>

### **Example 4: Border color**

- [x] **Border color**
  - Set a border with `style="border:2px solid …"` (Tomato, DodgerBlue, Violet).

Sandbox: `code_sandbox/html-colors/border.html`

```html
<h1 style="border: 2px solid Tomato;">Hello World</h1>

<h1 style="border: 2px solid DodgerBlue;">Hello World</h1>

<h1 style="border: 2px solid Violet;">Hello World</h1>
```

<img alt="html-colors border source" src="../code_sandbox/snaps/html-colors-03-code.png" />

<img alt="html-colors border result" src="../code_sandbox/snaps/html-colors-03-result.png" />

- [x] **Outcome:** the browser shows **Hello World**, **Hello World**, **Hello World**.

<a id="html-colors-example-05"></a>

### **Example 5: Color values**

- [x] **Color values**
  - Besides names, use **RGB**, **HEX**, **HSL**, **RGBA**, and **HSLA**.
  - `rgb(255, 99, 71)`, `#ff6347`, and `hsl(9, 100%, 64%)` are the same as **Tomato**.
  - RGBA / HSLA add an **alpha** channel; `0.5` is **50% transparent**.
  - RGB, HEX, and HSL are covered in more depth on the following color pages.

Sandbox: `code_sandbox/html-colors/values.html`

```html
<p>Same as color name "Tomato":</p>

<h1 style="background-color:rgb(255, 99, 71);">rgb(255, 99, 71)</h1>
<h1 style="background-color:#ff6347;">#ff6347</h1>
<h1 style="background-color:hsl(9, 100%, 64%);">hsl(9, 100%, 64%)</h1>

<p>Same as color name "Tomato", but 50% transparent:</p>
<h1 style="background-color:rgba(255, 99, 71, 0.5);">rgba(255, 99, 71, 0.5)</h1>
<h1 style="background-color:hsla(9, 100%, 64%, 0.5);">
  hsla(9, 100%, 64%, 0.5)
</h1>
```

<img alt="html-colors values source" src="../code_sandbox/snaps/html-colors-04-code.png" />

<img alt="html-colors values result" src="../code_sandbox/snaps/html-colors-04-result.png" />

- [x] **Outcome:** the browser shows **Same as color name "Tomato":**, **rgb(255, 99, 71)**, **#ff6347**, **hsl(9, 100%, 64%)**, **Same as color name "Tomato", but 50% transparent:**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-colors/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How can you specify a color in HTML?

<details>
<summary>Answer</summary>

- [x] With a **predefined color name**.
- [x] Or with **RGB**, **HEX**, **HSL**, **RGBA**, or **HSLA** values.

</details>

### Question 2: How many standard color names does HTML support?

<details>
<summary>Answer</summary>

- [x] **140** standard color names.

</details>

### Question 3: Which CSS property sets an element’s background color?

<details>
<summary>Answer</summary>

- [x] `background-color` (for example `style="background-color:DodgerBlue;"`).

</details>

### Question 4: Which CSS property sets text color?

<details>
<summary>Answer</summary>

- [x] `color` (for example `style="color:Tomato;"`).

</details>

### Question 5: How does the chapter set a colored border?

<details>
<summary>Answer</summary>

- [x] `style="border:2px solid Tomato;"` (or DodgerBlue / Violet).

</details>

### Question 6: Name three value forms that match the color Tomato.

<details>
<summary>Answer</summary>

- [x] `rgb(255, 99, 71)`
- [x] `#ff6347`
- [x] `hsl(9, 100%, 64%)`

</details>

### Question 7: What do RGBA and HSLA add compared with RGB and HSL?

<details>
<summary>Answer</summary>

- [x] An **alpha** channel (transparency).
- [x] In the example, `0.5` is **50% transparent**.

</details>

### Question 8: Where does this chapter send you for more on RGB, HEX, and HSL?

<details>
<summary>Answer</summary>

- [x] The **next chapters** (RGB, HEX, HSL pages).

</details>

</details>

## Summary

Specify colors with **names** (140 standard names) or with **RGB / HEX / HSL / RGBA / HSLA**. Use `background-color` for backgrounds, `color` for text, and `border` for borders. `rgb(255, 99, 71)`, `#ff6347`, and `hsl(9, 100%, 64%)` equal Tomato; RGBA and HSLA add transparency.

## References

- [HTML Colors (W3Schools)](https://www.w3schools.com/html/html_colors.asp)
- [HTML Color Names](https://www.w3schools.com/colors/colors_names.asp)
- [Try it Yourself: tryhtml_color_names](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_color_names)
- [Try it Yourself: tryhtml_color_background](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_color_background)
- [Try it Yourself: tryhtml_color_text](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_color_text)
- [Try it Yourself: tryhtml_color_border](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_color_border)
- [Try it Yourself: tryhtml_color_values](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_color_values)
- [HTML RGB](https://www.w3schools.com/html/html_colors_rgb.asp)
- [HTML HEX](https://www.w3schools.com/html/html_colors_hex.asp)
- [HTML HSL](https://www.w3schools.com/html/html_colors_hsl.asp)
- [MDN: color](https://developer.mozilla.org/en-US/docs/Web/CSS/color)
- [MDN: background-color](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color)
