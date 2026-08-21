# HTML Styles

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

The HTML **`style`** attribute adds CSS to an element: **color**, **font**, **size**, alignment, and more. The syntax is `<tagname style="property:value;">`. You will learn more CSS later; this chapter is the inline `style` attribute.

This section has **7** examples:

- [x] **Example 1:** Intro colors and size [View](#html-styles-example-01)
- [x] **Example 2:** Page background [View](#html-styles-example-02)
- [x] **Example 3:** Element backgrounds [View](#html-styles-example-03)
- [x] **Example 4:** Text color [View](#html-styles-example-04)
- [x] **Example 5:** Fonts [View](#html-styles-example-05)
- [x] **Example 6:** Text size [View](#html-styles-example-06)
- [x] **Example 7:** Text alignment [View](#html-styles-example-07)

## Detailed Explanation

<a id="html-styles-example-01"></a>

### **Example 1: Intro colors and size**

- [x] **The `style` attribute**
  - Setting the style of an HTML element can be done with **`style`**.
  - Syntax: `<tagname style="property:value;">`.
  - The **property** is a CSS property; the **value** is a CSS value.
  - Intro demo: normal, red, blue, and 50px text.

Sandbox: `code_sandbox/html-styles/index.html`

```html
<p>I am normal</p>
<p style="color:red;">I am red</p>
<p style="color:blue;">I am blue</p>
<p style="font-size:50px;">I am big</p>
```

<img alt="html-styles source" src="../code_sandbox/snaps/html-styles-code.png" />

<img alt="html-styles result" src="../code_sandbox/snaps/html-styles-result.png" />

- [x] **Outcome:** the browser shows **I am normal**, **I am red**, **I am blue**, **I am big**.

<a id="html-styles-example-02"></a>

### **Example 2: Page background**

- [x] **Background color (`background-color`)**
  - Defines the **background color** for an HTML element.
  - Page background: `<body style="background-color:powderblue;">`.

Sandbox: `code_sandbox/html-styles/background.html`

```html
<body style="background-color:powderblue;">
  <h1>This is a heading</h1>
  <p>This is a paragraph.</p>
</body>
```

<img alt="html-styles body background source" src="../code_sandbox/snaps/html-styles-01-code.png" />

<img alt="html-styles body background result" src="../code_sandbox/snaps/html-styles-01-result.png" />

- [x] **Outcome:** the browser shows **This is a heading**, **This is a paragraph.**.

<a id="html-styles-example-03"></a>

### **Example 3: Element backgrounds**

- [x] **Background color on individual elements**
  - The same property can style **different** elements (`h1` powderblue, `p` tomato).

Sandbox: `code_sandbox/html-styles/background2.html`

```html
<h1 style="background-color:powderblue;">This is a heading</h1>
<p style="background-color:tomato;">This is a paragraph.</p>
```

<img alt="html-styles element backgrounds source" src="../code_sandbox/snaps/html-styles-02-code.png" />

<img alt="html-styles element backgrounds result" src="../code_sandbox/snaps/html-styles-02-result.png" />

- [x] **Outcome:** the browser shows **This is a heading**, **This is a paragraph.**.

<a id="html-styles-example-04"></a>

### **Example 4: Text color**

- [x] **Text color (`color`)**
  - Defines the **text color** for an HTML element.

Sandbox: `code_sandbox/html-styles/color.html`

```html
<h1 style="color:blue;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>
```

<img alt="html-styles text color source" src="../code_sandbox/snaps/html-styles-03-code.png" />

<img alt="html-styles text color result" src="../code_sandbox/snaps/html-styles-03-result.png" />

- [x] **Outcome:** the browser shows **This is a heading**, **This is a paragraph.**.

<a id="html-styles-example-05"></a>

### **Example 5: Fonts**

- [x] **Fonts (`font-family`)**
  - Defines the **font** for an HTML element (Verdana heading, Courier paragraph).

Sandbox: `code_sandbox/html-styles/font.html`

```html
<h1 style="font-family:verdana;">This is a heading</h1>
<p style="font-family:courier;">This is a paragraph.</p>
```

<img alt="html-styles font-family source" src="../code_sandbox/snaps/html-styles-04-code.png" />

<img alt="html-styles font-family result" src="../code_sandbox/snaps/html-styles-04-result.png" />

- [x] **Outcome:** the browser shows **This is a heading**, **This is a paragraph.**.

<a id="html-styles-example-06"></a>

### **Example 6: Text size**

- [x] **Text size (`font-size`)**
  - Defines the **text size**. Percentages are relative to the parent (here `300%` / `160%`).

Sandbox: `code_sandbox/html-styles/size.html`

```html
<h1 style="font-size:300%;">This is a heading</h1>
<p style="font-size:160%;">This is a paragraph.</p>
```

<img alt="html-styles font-size source" src="../code_sandbox/snaps/html-styles-05-code.png" />

<img alt="html-styles font-size result" src="../code_sandbox/snaps/html-styles-05-result.png" />

- [x] **Outcome:** the browser shows **This is a heading**, **This is a paragraph.**.

<a id="html-styles-example-07"></a>

### **Example 7: Text alignment**

- [x] **Text alignment (`text-align`)**
  - Defines **horizontal** text alignment (`center` in the example).

Sandbox: `code_sandbox/html-styles/align.html`

```html
<h1 style="text-align:center;">Centered Heading</h1>
<p style="text-align:center;">Centered paragraph.</p>
```

<img alt="html-styles text-align source" src="../code_sandbox/snaps/html-styles-06-code.png" />

<img alt="html-styles text-align result" src="../code_sandbox/snaps/html-styles-06-result.png" />

- [x] **Outcome:** the browser shows **Centered Heading**, **Centered paragraph.**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-styles/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the syntax of the HTML `style` attribute?

<details>
<summary>Answer</summary>

- [x] `<tagname style="property:value;">`.
- [x] The **property** is a CSS property; the **value** is a CSS value.

</details>

### Question 2: Which CSS property sets a page or element background color?

<details>
<summary>Answer</summary>

- [x] **`background-color`**.
- [x] Example: `<body style="background-color:powderblue;">`.

</details>

### Question 3: Which property sets text color?

<details>
<summary>Answer</summary>

- [x] **`color`**.
- [x] Example: `<h1 style="color:blue;">`.

</details>

### Question 4: Which property chooses the font?

<details>
<summary>Answer</summary>

- [x] **`font-family`**.
- [x] Example: `font-family:verdana` or `font-family:courier`.

</details>

### Question 5: How do you change text size with the style attribute?

<details>
<summary>Answer</summary>

- [x] Use **`font-size`**.
- [x] The chapter uses percentages such as `300%` and `160%`.

</details>

### Question 6: How do you center text?

<details>
<summary>Answer</summary>

- [x] Use **`text-align:center`**.
- [x] It sets **horizontal** alignment.

</details>

### Question 7: Is inline `style` the only way to style HTML?

<details>
<summary>Answer</summary>

- [x] **No.** This chapter uses the **`style` attribute**.
- [x] You will learn more about **CSS** later in the tutorial.

</details>

</details>

## Summary

Use the **`style`** attribute for styling HTML elements. Use **`background-color`** for backgrounds, **`color`** for text colors, **`font-family`** for fonts, **`font-size`** for sizes, and **`text-align`** for alignment.

## References

- [HTML Styles (W3Schools)](https://www.w3schools.com/html/html_styles.asp)
- [Try it Yourself: tryhtml_styles_intro](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_intro)
- [Try it Yourself: tryhtml_styles_background-color](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_background-color)
- [Try it Yourself: tryhtml_styles_background-color2](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_background-color2)
- [Try it Yourself: tryhtml_styles_color](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_color)
- [Try it Yourself: tryhtml_styles_font-family](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_font-family)
- [Try it Yourself: tryhtml_styles_font-size](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_font-size)
- [Try it Yourself: tryhtml_styles_text-align](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_text-align)
- [MDN: style](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/style)
- [MDN: CSS background-color](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color)
- [MDN: CSS color](https://developer.mozilla.org/en-US/docs/Web/CSS/color)
- [MDN: CSS font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)
- [MDN: CSS font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
- [MDN: CSS text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align)
