# HTML Attributes

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

HTML **attributes** add extra information about an element. They go in the **start tag**, usually as `name="value"`. This chapter covers **`href`**, **`src`**, **`width`/`height`**, **`alt`**, **`style`**, **`lang`**, and **`title`**, plus quoting and lowercase conventions.

This section has **6** examples:

- [x] **Example 1:** `href` [View](#html-attributes-example-01)
- [x] **Example 2:** Image size [View](#html-attributes-example-02)
- [x] **Example 3:** Broken image + `alt` [View](#html-attributes-example-03)
- [x] **Example 4:** `style` [View](#html-attributes-example-04)
- [x] **Example 5:** `title` [View](#html-attributes-example-05)
- [x] **Example 6:** The lang attribute [View](#html-attributes-example-06)

## Detailed Explanation

- [x] **Attribute rules**
  - All HTML elements can have attributes.
  - Attributes provide **additional information** about elements.
  - Always specified in the **start tag**.
  - Usually **name/value** pairs: `name="value"`.
- [x] **The `src` attribute**
  - `<img>` embeds an image. **`src`** is the path.
  - **Absolute URL:** full address, e.g. `https://www.w3schools.com/images/img_girl.jpg`. External images can be copyrighted or disappear.
  - **Relative URL:** no domain. `img_girl.jpg` is relative to the **current page**; `/images/img_girl.jpg` is relative to the **domain**.
  - Prefer **relative** URLs so they do not break if the domain changes.
- [x] **The `lang` attribute**
  - Put **`lang`** on `<html>` to declare the page language (helps search engines and browsers).
  - English: `<html lang="en">`. Country: `<html lang="en-US">` (language + country).
- [x] **Lowercase and quotes**
  - The HTML standard does not require lowercase names or quotes, but **W3C recommends** both; **XHTML requires** them.
  - W3Schools always uses **lowercase names** and **quoted values**.
  - Quotes are **required** when the value has a **space** (`title=Description of W3Schools` fails).
  - Double quotes are most common; use single quotes if the value itself contains double quotes (or the reverse).

<a id="html-attributes-example-01"></a>

### **Example 1: `href`**

- [x] **The `href` attribute**
  - `<a>` is a hyperlink. **`href`** is the URL it goes to.

Sandbox: `code_sandbox/html-attributes/href.html`

```html
<a href="https://www.w3schools.com">Visit W3Schools</a>
```

<img alt="html-attributes href source" src="../code_sandbox/snaps/html-attributes-code.png" />

<img alt="html-attributes href result" src="../code_sandbox/snaps/html-attributes-result.png" />

- [x] **Outcome:** the browser shows **Visit W3Schools**.

<a id="html-attributes-example-02"></a>

### **Example 2: Image size**

- [x] **`width` and `height`**
  - Size the image in **pixels**.
  - Example: `width="500"` `height="600"` with `src="img_girl.jpg"`.

Sandbox: `code_sandbox/html-attributes/img.html`

```html
<img src="img_girl.jpg" alt="Girl with a jacket" width="500" height="600" />
```

<img alt="html-attributes img source" src="../code_sandbox/snaps/html-attributes-01-code.png" />

<img alt="html-attributes img size result" src="../code_sandbox/snaps/html-attributes-01-result.png" />

- [x] **Outcome:** the browser shows **Girl with a jacket**.

<a id="html-attributes-example-03"></a>

### **Example 3: Broken image + `alt`**

- [x] **The `alt` attribute**
  - **Required** on `<img>`. Alternate text if the image cannot be shown (slow connection, bad `src`, or a screen reader).
  - Broken `src` (`img_typo.jpg`) still shows **Girl with a jacket**.

Sandbox: `code_sandbox/html-attributes/alt-error.html`

```html
<img src="img_typo.jpg" alt="Girl with a jacket" />
```

<img alt="html-attributes alt-error source" src="../code_sandbox/snaps/html-attributes-02-code.png" />

<img alt="html-attributes alt fallback result" src="../code_sandbox/snaps/html-attributes-02-result.png" />

- [x] **Outcome:** the browser shows **Girl with a jacket**.

<a id="html-attributes-example-04"></a>

### **Example 4: `style`**

- [x] **The `style` attribute**
  - Adds styles (color, font, size, and more).
  - Example: red paragraph.

Sandbox: `code_sandbox/html-attributes/style.html`

```html
<p style="color:red;">This is a red paragraph.</p>
```

<img alt="html-attributes style source" src="../code_sandbox/snaps/html-attributes-03-code.png" />

<img alt="html-attributes style result" src="../code_sandbox/snaps/html-attributes-03-result.png" />

- [x] **Outcome:** the browser shows **This is a red paragraph.**.

<a id="html-attributes-example-05"></a>

### **Example 5: `title`**

- [x] **The `title` attribute**
  - Extra information about an element.
  - Shown as a **tooltip** on mouse over.

Sandbox: `code_sandbox/html-attributes/title.html`

```html
<p title="I'm a tooltip">This is a paragraph.</p>
```

<img alt="html-attributes title source" src="../code_sandbox/snaps/html-attributes-04-code.png" />

<img alt="html-attributes title result" src="../code_sandbox/snaps/html-attributes-04-result.png" />

- [x] **Outcome:** the browser shows **This is a paragraph.**.

<a id="html-attributes-example-06"></a>

### **Example 6: The lang attribute**

- [x] **The `lang` attribute**
  - Put **`lang`** on `<html>` to declare the page language (helps search engines and browsers).
  - English: `<html lang="en">`. Country: `<html lang="en-US">` (language + country).
  - The sandbox files in this chapter use `lang="en"` on the document.

```html
<!DOCTYPE html>
<html lang="en">
  <body>
    ...
  </body>
</html>
```

- [x] **Outcome:** the document root is `<html lang="en">`, which tells the browser the page is in English.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-attributes/href.html`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Where do you put attributes, and in what form?

<details>
<summary>Answer</summary>

- [x] In the **start tag**.
- [x] Usually **name/value** pairs: `name="value"`.

</details>

### Question 2: What does `href` on `<a>` do?

<details>
<summary>Answer</summary>

- [x] It specifies the **URL** of the page the link goes to.

</details>

### Question 3: Absolute vs relative `src` — which is safer for your own images?

<details>
<summary>Answer</summary>

- [x] **Relative** URLs (no domain).
- [x] They do not break if you **change domain**.
- [x] Absolute URLs point at another site and can vanish or be copyrighted.

</details>

### Question 4: Why set `width` and `height` on `<img>`?

<details>
<summary>Answer</summary>

- [x] They specify the image size in **pixels**.

</details>

### Question 5: Why is `alt` required?

<details>
<summary>Answer</summary>

- [x] It is the **alternate text** if the image cannot be displayed.
- [x] Used for slow connections, bad `src`, and **screen readers**.

</details>

### Question 6: What does `lang` on `<html>` do?

<details>
<summary>Answer</summary>

- [x] Declares the **language** of the page.
- [x] Helps **search engines** and **browsers**.
- [x] Example: `lang="en"` or `lang="en-US"`.

</details>

### Question 7: What does `title` show?

<details>
<summary>Answer</summary>

- [x] Extra information as a **tooltip** when you mouse over the element.

</details>

### Question 8: Must attribute names be lowercase and values quoted?

<details>
<summary>Answer</summary>

- [x] HTML does **not require** either.
- [x] **W3C recommends** lowercase and quotes; **XHTML requires** them.
- [x] Quotes are needed when the value contains a **space**.

</details>

### Question 9: When do you use single quotes around an attribute value?

<details>
<summary>Answer</summary>

- [x] When the value itself contains **double quotes**.
- [x] Or use double quotes if the value contains **single quotes**.

</details>

</details>

## Summary

Attributes live in the **start tag** as `name="value"`. **`href`** is the link URL, **`src`** the image path (prefer **relative**), **`width`/`height`** size in pixels, **`alt`** fallback text, **`style`** inline CSS, **`lang`** the page language, **`title`** a tooltip. Use **lowercase names** and **quoted values**.

## References

- [HTML Attributes (W3Schools)](https://www.w3schools.com/html/html_attributes.asp)
- [Try it Yourself: tryhtml_attributes_link](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_attributes_link)
- [Try it Yourself: tryhtml_attributes_img](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_attributes_img)
- [Try it Yourself: tryhtml_attributes_alt_error](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_attributes_alt_error)
- [Try it Yourself: tryhtml_attributes_style](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_attributes_style)
- [Try it Yourself: tryhtml_attributes_title](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_attributes_title)
- [HTML Attribute Reference](https://www.w3schools.com/tags/ref_attributes.asp)
- [HTML Language Code Reference](https://www.w3schools.com/tags/ref_language_codes.asp)
- [MDN: HTML attribute reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes)
