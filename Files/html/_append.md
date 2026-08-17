<details>
  <summary>HTML Plug-ins</summary>

## Introduction

**Plug-ins** extend the browser (Java applets, ActiveX, Flash, maps, virus scanners, bank IDs). **Most browsers no longer support** applets, plug-ins, ActiveX, or Shockwave Flash. This chapter still shows **`<object>`** and **`<embed>`** for including HTML or images.

## Detailed Explanation

- [x] **Warning**
  - Java Applets and plug-ins: **mostly gone**.
  - **ActiveX**: no longer supported in any browsers.
  - **Shockwave Flash**: turned off in modern browsers.
- [x] **`<object>`**
  - Supported by all browsers. Defines an **embedded object**.
  - Designed for plug-ins (applets, PDF, Flash) but can include **HTML in HTML** or an **image**.
  - Examples: `data="snippet.html"` (page used height **500px**; sandbox uses **200px** so the snap fits) and `data="audi.jpeg"`.
  - Sandbox: `code_sandbox/html-plug-ins/index.html`.

<img alt="html-plug-ins object result" src="./code_sandbox/snaps/html-plug-ins-result.png" />

- [x] **`<embed>`**
  - Supported in all major browsers. Was used for years but only became part of the spec in **HTML5**.
  - **No closing tag**; **cannot** contain alternative text.
  - Examples: `src="audi.jpeg"` and `src="snippet.html"`.
  - Sandbox: `embed.html`.

<img alt="html-plug-ins embed result" src="./code_sandbox/snaps/html-plug-ins-01-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Open the object page (nested HTML + image) and the embed page.

### **Overview**

- [ ] Serve `code_sandbox` and open both `html-plug-ins` files.
- [ ] Success: nested **Snippet** heading; photo via `object` and via `embed`.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-plug-ins/`
- [ ] `http://127.0.0.1:8766/html-plug-ins/embed.html`

<img alt="html-plug-ins result" src="./code_sandbox/snaps/html-plug-ins-result.png" />

The object/embed examples match the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-plug-ins/`.

</details>

<details>
  <summary>Code</summary>

## Code

Object (`index.html`):

<img alt="html-plug-ins object source" src="./code_sandbox/snaps/html-plug-ins-code.png" />

```html
<object width="100%" height="500px" data="snippet.html"></object>
<object data="audi.jpeg"></object>
```

<img alt="html-plug-ins object result" src="./code_sandbox/snaps/html-plug-ins-result.png" />

Embed (`embed.html`):

<img alt="html-plug-ins embed source" src="./code_sandbox/snaps/html-plug-ins-01-code.png" />

```html
<embed src="audi.jpeg">
<embed width="100%" height="500px" src="snippet.html">
```

<img alt="html-plug-ins embed result" src="./code_sandbox/snaps/html-plug-ins-01-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What were plug-ins for?

<details>
<summary>Answer</summary>

- [x] Extra programs: Java applets, ActiveX, Flash, maps, virus scans, bank IDs.

</details>

### Question 2: Do modern browsers still run Flash and ActiveX?

<details>
<summary>Answer</summary>

- [x] **No.** ActiveX is gone; Flash is turned off; applets/plug-ins are largely unsupported.

</details>

### Question 3: What can `<object>` embed today in this chapter?

<details>
<summary>Answer</summary>

- [x] HTML in HTML (`data="snippet.html"`).
- [x] An image (`data="audi.jpeg"`).

</details>

### Question 4: How does `<embed>` differ from `<object>`?

<details>
<summary>Answer</summary>

- [x] `<embed>` has **no closing tag**.
- [x] It **cannot** hold alternative text.
- [x] It joined the HTML spec in **HTML5**.

</details>

</details>

## Summary

Plug-ins (Java, ActiveX, Flash) are obsolete. Use `<object>` or `<embed>` to include HTML or images. `<embed>` is empty (no end tag, no fallback text).

## References

- [HTML Plug-ins (W3Schools)](https://www.w3schools.com/html/html_object.asp)
- [MDN: `<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)
- [MDN: `<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed)

</details>
