# HTML Images

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

Images improve how a page looks. The empty `<img>` tag **links** an image into the page (it is a holding space, not “inserted” bytes). Required attributes: **`src`** (path) and **`alt`** (alternate text). Nested sidebar pages cover **image maps**, **background images**, and **`<picture>`**.

This section has **5** examples:

- [x] **Example 1:** Syntax [View](#html-images-example-01)
- [x] **Example 2:** Trulli [View](#html-images-example-02)
- [x] **Example 3:** Broken `src` / alt [View](#html-images-example-03)
- [x] **Example 4:** Size [View](#html-images-example-04)
- [x] **Example 5:** Float [View](#html-images-example-05)

## Detailed Explanation

- [x] **Other folders and other servers**
  - Sub-folder: include the folder in `src` (`images/html5.gif` in the sandbox; the page shows `/images/html5.gif`).
  - Another server: **absolute URL**. External images may be copyrighted, and you cannot control if they disappear.
  - Sandbox: `folder.html`, `external.html`.
- [x] **Animated GIFs**
  - HTML allows animated GIFs (`programming.gif`).
  - Sandbox: `animated.html`.
- [x] **Image as a link**
  - Put `<img>` inside `<a>` (same idea as the Links chapter).
  - Sandbox: `link.html`.
- [x] **Common formats** (all major browsers): APNG, GIF, ICO, JPEG, PNG, SVG.
- [x] **Caution:** large images slow the page. Use them carefully.

| Tag         | Description                            |
| ----------- | -------------------------------------- |
| `<img>`     | Defines an image                       |
| `<map>`     | Defines an image map                   |
| `<area>`    | Clickable area inside an image map     |
| `<picture>` | Container for multiple image resources |

<a id="html-images-example-01"></a>

### **Example 1: Syntax**

- [x] **Syntax**
  - No end tag. Only attributes.
- [x] **`src`**
  - Path (URL) to the image.
  - The **browser** fetches it when the page loads, so the file must stay where `src` points.
  - If it cannot find the image: broken-link icon + **alt** text.
  - Examples on the page: `pic_trulli.jpg`, `img_girl.jpg`, `img_chania.jpg`.

Sandbox: `code_sandbox/html-images/index.html`

```html
<img src="url" alt="alternatetext" />
```

<img alt="html-images syntax source" src="../code_sandbox/snaps/html-images-01-code.png" />

<img alt="html-images trulli source" src="../code_sandbox/snaps/html-images-code.png" />

- [x] **Outcome:** the browser shows **alternatetext**.

<a id="html-images-example-02"></a>

### **Example 2: Trulli**

- [x] **`src`**
  - Path (URL) to the image.
  - The **browser** fetches it when the page loads, so the file must stay where `src` points.
  - If it cannot find the image: broken-link icon + **alt** text.
  - Examples on the page: `pic_trulli.jpg`, `img_girl.jpg`, `img_chania.jpg`.

Sandbox: `code_sandbox/html-images/index.html`

```html
<img src="pic_trulli.jpg" alt="Italian Trulli" />
```

<img alt="html-images trulli source" src="../code_sandbox/snaps/html-images-code.png" />

<img alt="html-images trulli result" src="../code_sandbox/snaps/html-images-result.png" />

- [x] **Outcome:** the browser shows **Italian Trulli**.

<a id="html-images-example-03"></a>

### **Example 3: Broken `src` / alt**

- [x] **`alt`**
  - Required. Shown if the image cannot be viewed (slow connection, bad `src`, or a **screen reader**).
  - The value should **describe** the image.
  - Wrong filename example: `wrongname.gif` with `alt="Flowers in Chania"`.

Sandbox: `code_sandbox/html-images/wrong.html`

```html
<img src="wrongname.gif" alt="Flowers in Chania" />
```

<img alt="html-images wrong source" src="../code_sandbox/snaps/html-images-02-code.png" />

<img alt="html-images alt result" src="../code_sandbox/snaps/html-images-01-result.png" />

- [x] **Outcome:** the browser shows **Flowers in Chania**.

<a id="html-images-example-04"></a>

### **Example 4: Size**

- [x] **Width and height**
  - Prefer `style="width:…;height:…"` (pixels).
  - Or `width` and `height` attributes (always pixels).
  - Always set size so the page does not **flicker** while the image loads.
  - Prefer **style** so a stylesheet cannot override the size (`width: 100%` in a sheet would stretch the `width`/`height` attributes, not the style).
  - Sandbox: `size.html` (style 500×600), `attributes.html` (width/height attributes), `style.html` (html5.gif).

Sandbox: `code_sandbox/html-images/size.html`

```html
<img
  src="img_girl.jpg"
  alt="Girl in a jacket"
  style="width:500px;height:600px;"
/>
```

<img alt="html-images size result" src="../code_sandbox/snaps/html-images-03-result.png" />

- [x] **Outcome:** the browser shows **Girl in a jacket**.

<a id="html-images-example-05"></a>

### **Example 5: Float**

- [x] **Image floating**
  - CSS `float:right` / `float:left` beside text.
  - Sandbox: `float.html`.

Sandbox: `code_sandbox/html-images/float.html`

```html
<p>
  <img
    src="smiley.gif"
    alt="Smiley face"
    style="float:right;width:42px;height:42px;"
  />
  The image will float to the right of the text.
</p>

<p>
  <img
    src="smiley.gif"
    alt="Smiley face"
    style="float:left;width:42px;height:42px;"
  />
  The image will float to the left of the text.
</p>
```

<img alt="html-images float source" src="../code_sandbox/snaps/html-images-03-code.png" />

<img alt="html-images float result" src="../code_sandbox/snaps/html-images-02-result.png" />

- [x] **Outcome:** the browser shows **The image will float to the right of the text.**, **The image will float to the left of the text.**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-images/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Is `<img>` empty, and which two attributes are required?

<details>
<summary>Answer</summary>

- [x] **Yes.** It has **no** end tag.
- [x] **`src`** (path) and **`alt`** (alternate text).

</details>

### Question 2: What happens if the browser cannot find the image?

<details>
<summary>Answer</summary>

- [x] It shows a **broken-link** icon and the **alt** text.

</details>

### Question 3: Why set width and height, and why prefer `style`?

<details>
<summary>Answer</summary>

- [x] So the page does not **flicker** while the image loads.
- [x] **`style`** keeps a stylesheet from changing the size.

</details>

### Question 4: How do you load an image from a sub-folder or another server?

<details>
<summary>Answer</summary>

- [x] Sub-folder: include the **folder name** in `src`.
- [x] Other server: an **absolute URL**. Watch copyright and that the file can vanish.

</details>

### Question 5: How do you make an image a link, or float it beside text?

<details>
<summary>Answer</summary>

- [x] Put `<img>` **inside** `<a>`.
- [x] Use CSS **`float:left`** or **`float:right`**.

</details>

### Question 6: Name common image formats all major browsers support.

<details>
<summary>Answer</summary>

- [x] APNG, GIF, ICO, JPEG, PNG, SVG.

</details>

</details>

## Summary

`<img src="…" alt="…">` embeds an image (empty tag). Always set **alt** and a size (`style` preferred). Sub-folders and absolute URLs work for `src`. GIFs can animate. Wrap `<img>` in `<a>` for a link; use `float` to sit beside text. Large images slow the page.

## References

- [HTML Images (W3Schools)](https://www.w3schools.com/html/html_images.asp)
- [Try it Yourself: tryhtml_images_trulli](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_images_trulli)
- [Try it Yourself: tryhtml_images_wrongname](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_images_wrongname)
- [Try it Yourself: tryhtml_images_size](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_images_size)
- [Try it Yourself: tryhtml_images_float](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_images_float)
- [HTML Image Map](https://www.w3schools.com/html/html_images_imagemap.asp)
- [HTML Background Images](https://www.w3schools.com/html/html_images_background.asp)
- [The Picture Element](https://www.w3schools.com/html/html_images_picture.asp)
- [MDN: `<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
