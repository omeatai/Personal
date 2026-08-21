# HTML Links

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

HTML links are **hyperlinks**. Click one to jump to another document. The mouse pointer becomes a **hand** over a link. A link can be **text**, an **image**, or another element. The `<a>` tag defines a hyperlink; **`href`** is the destination.

This section has **8** examples:

- [x] **Example 1:** Syntax [View](#html-links-example-01)
- [x] **Example 2:** Basic link [View](#html-links-example-02)
- [x] **Example 3:** Target [View](#html-links-example-03)
- [x] **Example 4:** Absolute vs relative [View](#html-links-example-04)
- [x] **Example 5:** Image as a link [View](#html-links-example-05)
- [x] **Example 6:** Email [View](#html-links-example-06)
- [x] **Example 7:** Button [View](#html-links-example-07)
- [x] **Example 8:** Title [View](#html-links-example-08)

## Detailed Explanation

- [x] **Default look**
  - Unvisited: underlined **blue**.
  - Visited: underlined **purple**.
  - Active: underlined **red**.
  - You can restyle links with CSS.
- [x] **More path forms**
  - Full URL, site path (`/html/default.asp`), or same-folder file (`default.asp`).
  - File paths are covered in **HTML File Paths**. Link **colors** and **bookmarks** are the next sidebar pages.

| Tag   | Description         |
| ----- | ------------------- |
| `<a>` | Defines a hyperlink |

<a id="html-links-example-01"></a>

### **Example 1: Syntax**

- [x] **Syntax**
  - `<a href="url">link text</a>`
  - The **link text** is what the reader sees; clicking it goes to the URL.
- [x] **A basic link**
  - Example: Visit W3Schools.com.

Sandbox: `code_sandbox/html-links/index.html`

```html
<a href="url">link text</a>
```

<img alt="html-links syntax source" src="../code_sandbox/snaps/html-links-code.png" />

<img alt="html-links basic source" src="../code_sandbox/snaps/html-links-01-code.png" />

- [x] **Outcome:** the browser shows **link text**.

<a id="html-links-example-02"></a>

### **Example 2: Basic link**

- [x] **A basic link**
  - Example: Visit W3Schools.com.

Sandbox: `code_sandbox/html-links/index.html`

```html
<a href="https://www.w3schools.com/">Visit W3Schools.com!</a>
```

<img alt="html-links basic source" src="../code_sandbox/snaps/html-links-01-code.png" />

<img alt="html-links basic result" src="../code_sandbox/snaps/html-links-result.png" />

- [x] **Outcome:** the browser shows **Visit W3Schools.com!**.

<a id="html-links-example-03"></a>

### **Example 3: Target**

- [x] **The `target` attribute**
  - Where to open the document.
  - `_self` — same window/tab (default).
  - `_blank` — new window or tab.
  - `_parent` — parent frame.
  - `_top` — full window.

Sandbox: `code_sandbox/html-links/target.html`

```html
<a href="https://www.w3schools.com/" target="_blank">Visit W3Schools!</a>
```

<img alt="html-links target source" src="../code_sandbox/snaps/html-links-02-code.png" />

<img alt="html-links target result" src="../code_sandbox/snaps/html-links-01-result.png" />

- [x] **Outcome:** the browser shows **Visit W3Schools!**.

<a id="html-links-example-04"></a>

### **Example 4: Absolute vs relative**

- [x] **Absolute vs relative URLs**
  - **Absolute** — full address (`https://www.w3.org/`, Google).
  - **Relative** — a page on the same site (no `https://www` part).
  - The chapter uses `html_images.asp` and `/css/default.asp`. The sandbox uses local `images.html` and `css.html` so the relative links run offline.

Sandbox: `code_sandbox/html-links/urls.html`

```html
<h2>Absolute URLs</h2>
<p><a href="https://www.w3.org/">W3C</a></p>
<p><a href="https://www.google.com/">Google</a></p>

<h2>Relative URLs</h2>
<p><a href="images.html">HTML Images</a></p>
<p><a href="css.html">CSS Tutorial</a></p>
```

<img alt="html-links urls source" src="../code_sandbox/snaps/html-links-03-code.png" />

<img alt="html-links urls result" src="../code_sandbox/snaps/html-links-02-result.png" />

- [x] **Outcome:** the browser shows **Absolute URLs**, **W3C**, **Google**, **Relative URLs**, **HTML Images**.

<a id="html-links-example-05"></a>

### **Example 5: Image as a link**

- [x] **Image as a link**
  - Put `<img>` inside `<a>`.
  - The page uses `smiley.gif` and `href="default.asp"`. The sandbox uses `smiley.png` and `href="index.html"` (the gif URL was blocked; the image is a local 42×42 smiley).

Sandbox: `code_sandbox/html-links/image.html`

```html
<a href="index.html">
  <img src="smiley.png" alt="HTML tutorial" style="width:42px;height:42px;" />
</a>
```

<img alt="html-links image source" src="../code_sandbox/snaps/html-links-04-code.png" />

<img alt="html-links image result" src="../code_sandbox/snaps/html-links-03-result.png" />

- [x] **Outcome:** the browser shows **HTML tutorial**.

<a id="html-links-example-06"></a>

### **Example 6: Email**

- [x] **Email link**
  - `href="mailto:someone@example.com"` opens the user’s mail program.

Sandbox: `code_sandbox/html-links/email.html`

```html
<a href="mailto:someone@example.com">Send email</a>
```

<img alt="html-links email source" src="../code_sandbox/snaps/html-links-05-code.png" />

<img alt="html-links email result" src="../code_sandbox/snaps/html-links-04-result.png" />

- [x] **Outcome:** the browser shows **Send email**.

<a id="html-links-example-07"></a>

### **Example 7: Button**

- [x] **Button as a link**
  - A `<button>` needs **JavaScript** for the click (`onclick` + `document.location`).
  - The page uses `default.asp`; the sandbox uses `index.html`.

Sandbox: `code_sandbox/html-links/button.html`

```html
<button onclick="document.location='index.html'">HTML Tutorial</button>
```

<img alt="html-links button source" src="../code_sandbox/snaps/html-links-06-code.png" />

<img alt="html-links button result" src="../code_sandbox/snaps/html-links-05-result.png" />

- [x] **Outcome:** the browser shows **HTML Tutorial**.

<a id="html-links-example-08"></a>

### **Example 8: Title**

- [x] **Link titles**
  - The `title` attribute is extra info, usually a **tooltip** on hover.

Sandbox: `code_sandbox/html-links/title.html`

```html
<a href="https://www.w3schools.com/html/" title="Go to W3Schools HTML section"
  >Visit our HTML Tutorial</a
>
```

<img alt="html-links title source" src="../code_sandbox/snaps/html-links-07-code.png" />

<img alt="html-links title result" src="../code_sandbox/snaps/html-links-06-result.png" />

- [x] **Outcome:** the browser shows **Visit our HTML Tutorial**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-links/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Which tag defines a hyperlink, and which attribute is the destination?

<details>
<summary>Answer</summary>

- [x] The **`<a>`** tag.
- [x] The **`href`** attribute.

</details>

### Question 2: How do unvisited, visited, and active links look by default?

<details>
<summary>Answer</summary>

- [x] Unvisited: underlined **blue**.
- [x] Visited: underlined **purple**.
- [x] Active: underlined **red**.

</details>

### Question 3: What does `target="_blank"` do?

<details>
<summary>Answer</summary>

- [x] Opens the document in a **new** window or tab.
- [x] `_self` is the default (same window/tab).

</details>

### Question 4: What is the difference between an absolute URL and a relative URL?

<details>
<summary>Answer</summary>

- [x] **Absolute** is a full web address (`https://…`).
- [x] **Relative** is a page on the **same site** (no `https://www` part).

</details>

### Question 5: How do you make an image a link?

<details>
<summary>Answer</summary>

- [x] Put the **`<img>`** tag **inside** the **`<a>`** tag.

</details>

### Question 6: How do you create an email link?

<details>
<summary>Answer</summary>

- [x] Use **`mailto:`** in `href` (for example `mailto:someone@example.com`).

</details>

### Question 7: How do you make a button act as a link?

<details>
<summary>Answer</summary>

- [x] Add **JavaScript** on the click (`onclick` and `document.location`).
- [x] A button is **not** a link by itself.

</details>

### Question 8: What does the `title` attribute show on a link?

<details>
<summary>Answer</summary>

- [x] Extra information, usually as a **tooltip** when the mouse is over the element.

</details>

</details>

## Summary

Use `<a href="…">` for hyperlinks. `target` chooses the window (`_blank` for a new tab). Absolute URLs are full addresses; relative URLs stay on the site. Wrap `<img>` in `<a>` for an image link, use `mailto:` for email, JavaScript for a button, and `title` for a tooltip.

## References

- [HTML Links Hyperlinks (W3Schools)](https://www.w3schools.com/html/html_links.asp)
- [Try it Yourself: tryhtml_links_w3schools](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_links_w3schools)
- [Try it Yourself: tryhtml_links_target](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_links_target)
- [Try it Yourself: tryhtml_links](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_links)
- [Try it Yourself: tryhtml_links_image](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_links_image)
- [Try it Yourself: tryhtml_links_email](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_links_email)
- [Try it Yourself: tryhtml_links_button_element](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_links_button_element)
- [Try it Yourself: tryhtml_links_title](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_links_title)
- [HTML Link Colors](https://www.w3schools.com/html/html_links_colors.asp)
- [HTML Link Bookmarks](https://www.w3schools.com/html/html_links_bookmarks.asp)
- [MDN: `<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
