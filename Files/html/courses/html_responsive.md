# HTML Responsive

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

**Responsive web design** makes pages look good on **all devices**. HTML and CSS **resize, hide, shrink, or enlarge** content for desktops, tablets, and phones. This chapter covers the **viewport** meta tag, **responsive images**, **vw** text, **media queries**, and CSS **frameworks** (W3.CSS, Bootstrap).

This section has **4** examples:

- [x] **Example 1:** Viewport [View](#html-responsive-example-01)
- [x] **Example 2:** `width: 100%` [View](#html-responsive-example-02)
- [x] **Example 3:** `max-width: 100%` [View](#html-responsive-example-03)
- [x] **Example 4:** Media query [View](#html-responsive-example-04)

## Detailed Explanation

- [x] **`<picture>` (from the page)**
  - Different images for different window sizes (`srcset` + `media`).
  - Example sources: small flower at max 600px, flowers at max 1500px, then a default.
- [x] **Responsive text size**
  - Unit **`vw`** = viewport width. `1vw` = 1% of the viewport width.
  - Example: `<h1 style="font-size:10vw">Hello World</h1>`.
- [x] **Frameworks**
  - Popular CSS frameworks include responsive design (free, easy).
  - **W3.CSS** — desktop/tablet/mobile by default; smaller/faster; no jQuery required.
  - **Bootstrap** — example uses Bootstrap 5 CDN and a three-column row.

<a id="html-responsive-example-01"></a>

### **Example 1: Viewport**

- [x] **Viewport**
  - Add to **all** pages: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.
  - Tells the browser how to control **dimensions and scaling**.

Sandbox: `code_sandbox/html-responsive/index.html`

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

<img alt="html-responsive viewport source" src="../code_sandbox/snaps/html-responsive-code.png" />

<img alt="html-responsive viewport vw result" src="../code_sandbox/snaps/html-responsive-result.png" />

- [x] **Outcome:** the page demonstrates **Viewport** as shown in the result snap.

<a id="html-responsive-example-02"></a>

### **Example 2: `width: 100%`**

- [x] **Responsive images — `width: 100%`**
  - The image scales up and down with the browser.
  - It can grow **larger than the original**.
  - Sandbox: `width.html`.

Sandbox: `code_sandbox/html-responsive/width.html`

```html
<img src="img_girl.jpg" style="width:100%;" />
```

<img alt="html-responsive width source" src="../code_sandbox/snaps/html-responsive-01-code.png" />

<img alt="html-responsive width 100 result" src="../code_sandbox/snaps/html-responsive-01-result.png" />

- [x] **Outcome:** the page demonstrates **`width: 100%`** as shown in the result snap.

<a id="html-responsive-example-03"></a>

### **Example 3: `max-width: 100%`**

- [x] **Responsive images — `max-width: 100%`**
  - Scales **down** if needed, but **never larger** than the original.
  - Often the **better** choice. Use with `height: auto`.
  - Sandbox: `maxwidth.html`.

Sandbox: `code_sandbox/html-responsive/maxwidth.html`

```html
<img src="img_girl.jpg" style="max-width:100%;height:auto;" />
```

<img alt="html-responsive max-width source" src="../code_sandbox/snaps/html-responsive-02-code.png" />

<img alt="html-responsive max-width result" src="../code_sandbox/snaps/html-responsive-02-result.png" />

- [x] **Outcome:** the page demonstrates **`max-width: 100%`** as shown in the result snap.

<a id="html-responsive-example-04"></a>

### **Example 4: Media query**

- [x] **Media queries**
  - Completely different styles for different sizes.
  - Example: `.left`/`.right` 20%, `.main` 60% floated; at **max-width 800px** all become **100%** (stack).
  - Sandbox: `media.html`.

Sandbox: `code_sandbox/html-responsive/media.html`

```css
@media screen and (max-width: 800px) {
  .left,
  .main,
  .right {
    width: 100%;
  }
}
```

<img alt="html-responsive media query source" src="../code_sandbox/snaps/html-responsive-03-code.png" />

<img alt="html-responsive media query result" src="../code_sandbox/snaps/html-responsive-03-result.png" />

- [x] **Outcome:** the browser shows **@media screen and (max-width: 800px) { .left, .main, .right { width: 100%; } }**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-responsive/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is responsive web design?

<details>
<summary>Answer</summary>

- [x] Pages that **look good on all devices**.
- [x] HTML/CSS **resize, hide, shrink, or enlarge** the layout.

</details>

### Question 2: Which meta tag should every responsive page include?

<details>
<summary>Answer</summary>

- [x] `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.

</details>

### Question 3: Why prefer `max-width: 100%` over `width: 100%` on images?

<details>
<summary>Answer</summary>

- [x] `width: 100%` can scale **larger than the original**.
- [x] `max-width: 100%` scales **down only**.

</details>

### Question 4: What does `10vw` mean?

<details>
<summary>Answer</summary>

- [x] **10% of the viewport width**.
- [x] `1vw` = 1% of the browser window width.

</details>

### Question 5: What do media queries do in this chapter?

<details>
<summary>Answer</summary>

- [x] Apply **different styles** at different browser sizes.
- [x] Example: stack columns at **800px** or smaller.

</details>

</details>

## Summary

Add the viewport meta tag. Make images fluid with `max-width: 100%` (or `width: 100%`). Size text with `vw` if you want it to follow the window. Use media queries (and optionally W3.CSS or Bootstrap) for different layouts at different widths.

## References

- [HTML Responsive Web Design (W3Schools)](https://www.w3schools.com/html/html_responsive.asp)
- [Try it Yourself: tryhtml_responsive_viewport](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_responsive_viewport)
- [Try it Yourself: tryhtml_responsive_image](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_responsive_image)
- [Try it Yourself: tryhtml_responsive_image_maxwidth](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_responsive_image_maxwidth)
- [Try it Yourself: tryhtml_responsive_picture](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_responsive_picture)
- [Try it Yourself: tryhtml_responsive_text](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_responsive_text)
- [Try it Yourself: tryhtml_responsive_media_query](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_responsive_media_query)
- [RWD Tutorial](https://www.w3schools.com/css/css_rwd_intro.asp)
- [W3.CSS Tutorial](https://www.w3schools.com/w3css/default.asp)
- [Bootstrap Tutorial](https://www.w3schools.com/bootstrap/bootstrap_ver.asp)
- [MDN: Responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design)
