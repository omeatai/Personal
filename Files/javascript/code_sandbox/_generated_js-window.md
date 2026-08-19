<details>
  <summary>JS Window</summary>

## Introduction

The Window object is the browser’s global. The BOM (Browser Object Model) is how JavaScript talks to the browser itself: size, tabs, and the objects hanging off `window`.

This section has **7** examples:

- [x] **Example 1:** window.document is the same object as document [View](#js-window-example-01)
- [x] **Example 2:** window.innerWidth — viewport width in pixels [View](#js-window-example-02)
- [x] **Example 3:** window.innerHeight — viewport height in pixels [View](#js-window-example-03)
- [x] **Example 4:** window.open() — open a new window [View](#js-window-example-04)
- [x] **Example 5:** window.close() — close the current window [View](#js-window-example-05)
- [x] **Example 6:** window.moveTo() — move the current window [View](#js-window-example-06)
- [x] **Example 7:** window.resizeTo() — resize the current window [View](#js-window-example-07)

## Detailed Explanation

- [x] `document` is `window.document`.
- [x] `innerWidth` / `innerHeight` are the viewport.
- [x] `open` / `close` / `moveTo` / `resizeTo` are legacy window controls and are often blocked.

<a id="js-window-example-01"></a>

### **Example 1: window.document is the same object as document**

- [x] The **BOM** (Browser Object Model) is everything the browser exposes besides the page tree.
- [x] The **Window** object is the global. All global variables and functions become properties/methods of `window`.
- [x] The HTML DOM `document` is a **property** of `window`. `window.document.getElementById` and `document.getElementById` are the same call.
- [x] You may omit `window.` for globals. `window` itself cannot be omitted if you need the Window object (size, open, …).

Sandbox: `code_sandbox/js-window/window-document.html`

```html
window.document.getElementById("header");
document.getElementById("header");
```

<img alt="js-window example 1 source" src="./code_sandbox/snaps/js-window-01-code.png" />

<img alt="js-window example 1 result" src="./code_sandbox/snaps/js-window-01-result.png" />

- [x] **Outcome:** `window.document === document` is **true**. Both lookups find the same **header** element.

<a id="js-window-example-02"></a>

### **Example 2: window.innerWidth — viewport width in pixels**

- [x] `window.innerWidth` is the **inner** width of the browser window (the viewport), in CSS pixels.
- [x] It does **not** include toolbars, window chrome, or (usually) the vertical scrollbar gutter the same way `outerWidth` does.
- [x] The W3Schools Tryit stores `let w = window.innerWidth` then writes it to the page.
- [x] This value changes when the user resizes the window or rotates a phone.

Sandbox: `code_sandbox/js-window/inner-width.html`

```html
let w = window.innerWidth;
```

<img alt="js-window example 2 source" src="./code_sandbox/snaps/js-window-02-code.png" />

<img alt="js-window example 2 result" src="./code_sandbox/snaps/js-window-02-result.png" />

- [x] **Outcome:** The snapshot window is **900px** wide, so `innerWidth` reports **900** (or very close).

<a id="js-window-example-03"></a>

### **Example 3: window.innerHeight — viewport height in pixels**

- [x] `window.innerHeight` is the **inner** height of the viewport, not including browser UI.
- [x] W3Schools pairs it with `innerWidth` in one Tryit: `let h = window.innerHeight`.
- [x] Use these — not `screen.height` — when you care about **how much page is visible**.
- [x] Headless screenshots use `--window-size=900,640`, so height is in that neighborhood.

Sandbox: `code_sandbox/js-window/inner-height.html`

```html
let h = window.innerHeight;
```

<img alt="js-window example 3 source" src="./code_sandbox/snaps/js-window-03-code.png" />

<img alt="js-window example 3 result" src="./code_sandbox/snaps/js-window-03-result.png" />

- [x] **Outcome:** `innerHeight` is a positive pixel count for the visible viewport (around **640** in this snap).

<a id="js-window-example-04"></a>

### **Example 4: window.open() — open a new window**

- [x] `window.open(url)` asks the browser to open **another** browsing context (tab or popup).
- [x] Popup blockers often return **`null`** if the call is not tied to a user gesture.
- [x] Always check the return value before calling methods on it.
- [x] The snapshot calls `open` without a click, so a blocker is likely — that is the realistic result.

Sandbox: `code_sandbox/js-window/open.html`

```html
window.open() - open a new window
```

<img alt="js-window example 4 source" src="./code_sandbox/snaps/js-window-04-code.png" />

<img alt="js-window example 4 result" src="./code_sandbox/snaps/js-window-04-result.png" />

- [x] **Outcome:** The call returns either a **Window** or **`null`** (blocked). The snapshot reports which happened.

<a id="js-window-example-05"></a>

### **Example 5: window.close() — close the current window**

- [x] `window.close()` closes **this** window, but browsers only allow it for windows **your script opened** with `open()`.
- [x] Calling it on a tab the user opened themselves is ignored (or prompts).
- [x] Do not put `close()` in onload — it will not do what tutorial snippets imply on a normal tab.
- [x] The snapshot does **not** close the page; it only proves the method exists.

Sandbox: `code_sandbox/js-window/close.html`

```html
window.close() - close the current window
```

<img alt="js-window example 5 source" src="./code_sandbox/snaps/js-window-05-code.png" />

<img alt="js-window example 5 result" src="./code_sandbox/snaps/js-window-05-result.png" />

- [x] **Outcome:** `typeof window.close` is **function**. The page stays open so the snapshot can be taken.

<a id="js-window-example-06"></a>

### **Example 6: window.moveTo() — move the current window**

- [x] `window.moveTo(x, y)` moves the **window** to screen coordinates.
- [x] Modern browsers **ignore** this for ordinary tabs (only some popup windows allow it).
- [x] Treat it as a legacy BOM method, not something you should rely on.
- [x] The snapshot calls it and then reports `screenX`/`screenY` (often unchanged).

Sandbox: `code_sandbox/js-window/move-to.html`

```html
window.moveTo() - move the current window
```

<img alt="js-window example 6 source" src="./code_sandbox/snaps/js-window-06-code.png" />

<img alt="js-window example 6 result" src="./code_sandbox/snaps/js-window-06-result.png" />

- [x] **Outcome:** After `moveTo(0, 0)`, `screenX`/`screenY` are reported. Tabs usually **do not move**.

<a id="js-window-example-07"></a>

### **Example 7: window.resizeTo() — resize the current window**

- [x] `window.resizeTo(width, height)` resizes the **outer** window.
- [x] Like `moveTo`, this is **blocked** for most tabs.
- [x] Prefer CSS layout and `innerWidth` over trying to resize the browser.
- [x] The snapshot calls `resizeTo(800, 600)` and reports inner size (typically unchanged).

Sandbox: `code_sandbox/js-window/resize-to.html`

```html
window.resizeTo() - resize the current window
```

<img alt="js-window example 7 source" src="./code_sandbox/snaps/js-window-07-code.png" />

<img alt="js-window example 7 result" src="./code_sandbox/snaps/js-window-07-result.png" />

- [x] **Outcome:** `resizeTo` is a function; the viewport size after the call is still the screenshot window.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-window/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the BOM?

<details>
<summary>Answer</summary>

- [x] The **Browser Object Model** — `window` and objects it owns (`document`, `location`, `history`, `navigator`, `screen`).

</details>

### Question 2: Are `document` and `window.document` different?

<details>
<summary>Answer</summary>

- [x] **No** — `document` is a property of `window`; they are the **same** object.

</details>

### Question 3: What does `innerWidth` measure?

<details>
<summary>Answer</summary>

- [x] The **viewport** width in pixels, not the monitor and not browser chrome.

</details>

### Question 4: Does `innerHeight` include toolbars?

<details>
<summary>Answer</summary>

- [x] **No** — it is the inner viewport height.

</details>

### Question 5: What does `window.open` return if a popup is blocked?

<details>
<summary>Answer</summary>

- [x] **`null`** (or a closed window). Always check before using it.

</details>

### Question 6: Can you `close()` any tab?

<details>
<summary>Answer</summary>

- [x] **No** — browsers only let scripts close windows they **opened**.

</details>

### Question 7: Do `moveTo` and `resizeTo` work on normal tabs?

<details>
<summary>Answer</summary>

- [x] Usually **no** — they are ignored except for some script-opened popups.

</details>

### Question 8: Can you omit the `window.` prefix?

<details>
<summary>Answer</summary>

- [x] **Yes** for globals (`document`, `alert`). Use `window` when you mean the Window object itself.

</details>

### Question 9: What becomes a property of `window`?

<details>
<summary>Answer</summary>

- [x] **Global variables** (and global functions become **methods**).

</details>

### Question 10: Which size should you use for “visible page”?

<details>
<summary>Answer</summary>

- [x] **`innerWidth` / `innerHeight`**, not `screen.width`.

</details>


</details>

## Summary

Treat `window` as the global. Read viewport size with innerWidth/innerHeight. Do not depend on open/move/resize in ordinary tabs.

## References

- [JS Window](https://www.w3schools.com/js/js_window.asp)
- [MDN Window](https://developer.mozilla.org/en-US/docs/Web/API/Window)

</details>
