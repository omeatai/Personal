# JS Screen

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

`window.screen` describes the visitor’s monitor: width, height, available area, and color depth — not the browser viewport.

This section has **6** examples:

- [x] **Example 1:** screen.width — visitor screen width [View](#js-screen-example-01)
- [x] **Example 2:** screen.height — visitor screen height [View](#js-screen-example-02)
- [x] **Example 3:** screen.availWidth — width minus OS chrome [View](#js-screen-example-03)
- [x] **Example 4:** screen.availHeight — height minus OS chrome [View](#js-screen-example-04)
- [x] **Example 5:** screen.colorDepth — bits per color [View](#js-screen-example-05)
- [x] **Example 6:** screen.pixelDepth — bits per pixel [View](#js-screen-example-06)

## Detailed Explanation

- [x] `screen` can be written without `window.`.
- [x] avail* subtracts OS chrome such as a taskbar.
- [x] colorDepth / pixelDepth are usually 24 or 32 today.

<a id="js-screen-example-01"></a>

### **Example 1: screen.width — visitor screen width**

- [x] `window.screen` (or just `screen`) describes the **monitor**, not the browser viewport.
- [x] `screen.width` is the full screen width in pixels.
- [x] This is **not** the same as `window.innerWidth` (the tab).
- [x] W3Schools writes: `Screen Width: ` + `screen.width`.

Sandbox: `code_sandbox/js-screen/width.html`

```html
document.getElementById("demo").innerHTML = "Screen Width: " + screen.width;
```

<img alt="js-screen example 1 source" src="../code_sandbox/snaps/js-screen-01-code.png" />

<img alt="js-screen example 1 result" src="../code_sandbox/snaps/js-screen-01-result.png" />

- [x] **Outcome:** The page prints **Screen Width:** followed by this machine’s pixel width.

<a id="js-screen-example-02"></a>

### **Example 2: screen.height — visitor screen height**

- [x] `screen.height` is the full screen height in pixels.
- [x] It includes areas covered by the taskbar in the **total** height (unlike `availHeight`).
- [x] Use it for “how big is the display?”, not “how big is my page?”.

Sandbox: `code_sandbox/js-screen/height.html`

```html
document.getElementById("demo").innerHTML = "Screen Height: " + screen.height;
```

<img alt="js-screen example 2 source" src="../code_sandbox/snaps/js-screen-02-code.png" />

<img alt="js-screen example 2 result" src="../code_sandbox/snaps/js-screen-02-result.png" />

- [x] **Outcome:** The page prints **Screen Height:** and the monitor height in pixels.

<a id="js-screen-example-03"></a>

### **Example 3: screen.availWidth — width minus OS chrome**

- [x] `availWidth` subtracts **interface features** such as a Windows taskbar if it reduces usable width.
- [x] On many desktops it equals `screen.width` because the taskbar is on the bottom.
- [x] On a vertical taskbar it can be smaller than `width`.

Sandbox: `code_sandbox/js-screen/avail-width.html`

```html
document.getElementById("demo").innerHTML = "Available Screen Width: " + screen.availWidth;
```

<img alt="js-screen example 3 source" src="../code_sandbox/snaps/js-screen-03-code.png" />

<img alt="js-screen example 3 result" src="../code_sandbox/snaps/js-screen-03-result.png" />

- [x] **Outcome:** **Available Screen Width:** is `availWidth` (≤ `screen.width`).

<a id="js-screen-example-04"></a>

### **Example 4: screen.availHeight — height minus OS chrome**

- [x] `availHeight` is height minus the taskbar (and similar OS UI).
- [x] Typically `availHeight < height` when a bottom taskbar is present.
- [x] This is still **not** the browser viewport — that is `innerHeight`.

Sandbox: `code_sandbox/js-screen/avail-height.html`

```html
document.getElementById("demo").innerHTML = "Available Screen Height: " + screen.availHeight;
```

<img alt="js-screen example 4 source" src="../code_sandbox/snaps/js-screen-04-code.png" />

<img alt="js-screen example 4 result" src="../code_sandbox/snaps/js-screen-04-result.png" />

- [x] **Outcome:** **Available Screen Height:** is `availHeight` (often less than `screen.height`).

<a id="js-screen-example-05"></a>

### **Example 5: screen.colorDepth — bits per color**

- [x] `colorDepth` is how many bits are used to display one color.
- [x] Modern displays: **24** (“True Color”, 16,777,216 colors) or **32** (“Deep Color”).
- [x] Older: **16** High Color; very old: **8** VGA (256 colors).
- [x] 32-bit often still means 24-bit color plus 8-bit alpha at the hardware level — the property still reports 24 or 32.

Sandbox: `code_sandbox/js-screen/color-depth.html`

```html
document.getElementById("demo").innerHTML = "Screen Color Depth: " + screen.colorDepth;
```

<img alt="js-screen example 5 source" src="../code_sandbox/snaps/js-screen-05-code.png" />

<img alt="js-screen example 5 result" src="../code_sandbox/snaps/js-screen-05-result.png" />

- [x] **Outcome:** **Screen Color Depth:** is typically **24** or **32** on a current machine.

<a id="js-screen-example-06"></a>

### **Example 6: screen.pixelDepth — bits per pixel**

- [x] `pixelDepth` is the bit depth of the screen.
- [x] On modern browsers it is usually **the same number as `colorDepth`**.
- [x] Do not use either property to detect “the user’s device type” — they are about color, not phone vs desktop.

Sandbox: `code_sandbox/js-screen/pixel-depth.html`

```html
document.getElementById("demo").innerHTML = "Screen Pixel Depth: " + screen.pixelDepth;
```

<img alt="js-screen example 6 source" src="../code_sandbox/snaps/js-screen-06-code.png" />

<img alt="js-screen example 6 result" src="../code_sandbox/snaps/js-screen-06-result.png" />

- [x] **Outcome:** **Screen Pixel Depth:** matches this display’s reported bit depth (often equal to `colorDepth`).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-screen/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Is `screen.width` the browser width?

<details>
<summary>Answer</summary>

- [x] **No** — it is the **monitor**. Use `innerWidth` for the viewport.

</details>

### Question 2: What does `availHeight` leave out?

<details>
<summary>Answer</summary>

- [x] OS UI such as the **taskbar**.

</details>

### Question 3: Typical modern `colorDepth`?

<details>
<summary>Answer</summary>

- [x] **24** or **32** bits.

</details>

### Question 4: How many colors is 24-bit?

<details>
<summary>Answer</summary>

- [x] **16,777,216** (“True Color”).

</details>

### Question 5: Can you skip the `window.` prefix?

<details>
<summary>Answer</summary>

- [x] **Yes** — `screen.width` is the same as `window.screen.width`.

</details>

### Question 6: Is `pixelDepth` usually different from `colorDepth`?

<details>
<summary>Answer</summary>

- [x] Usually **the same** on current browsers.

</details>

### Question 7: 16-bit color is called what on the page?

<details>
<summary>Answer</summary>

- [x] **High Color** (65,536 colors).

</details>

### Question 8: 8-bit color is called what?

<details>
<summary>Answer</summary>

- [x] **VGA colors** (256).

</details>

### Question 9: When would `availWidth` be smaller than `width`?

<details>
<summary>Answer</summary>

- [x] When a **vertical taskbar** (or similar) reduces usable width.

</details>

### Question 10: Which object is this page about?

<details>
<summary>Answer</summary>

- [x] **`window.screen`**.

</details>


</details>

## Summary

Use screen.* for the monitor and innerWidth/innerHeight for the tab. availHeight is often smaller than height because of the taskbar.

## References

- [JS Screen](https://www.w3schools.com/js/js_window_screen.asp)
- [MDN Screen](https://developer.mozilla.org/en-US/docs/Web/API/Screen)
