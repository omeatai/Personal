<details>
  <summary>Event Examples</summary>

## Introduction

A tour of HTML event attributes and DOM `onclick` assignment: click text, load/unload, input/change, mouse, and extra Tryits (image press, focus, hover color).

This section has **13** examples:

- [x] **Example 1:** Change text when the paragraph is clicked [View](#event-examples-example-01)
- [x] **Example 2:** Call a function and pass this [View](#event-examples-example-02)
- [x] **Example 3:** HTML event attribute on a button [View](#event-examples-example-03)
- [x] **Example 4:** Assign onclick with the HTML DOM [View](#event-examples-example-04)
- [x] **Example 5:** onload and onunload [View](#event-examples-example-05)
- [x] **Example 6:** The oninput event [View](#event-examples-example-06)
- [x] **Example 7:** The onchange event — upperCase [View](#event-examples-example-07)
- [x] **Example 8:** onmouseover and onmouseout [View](#event-examples-example-08)
- [x] **Example 9:** onmousedown, onmouseup, and onclick [View](#event-examples-example-09)
- [x] **Example 10:** More examples — change an image while the mouse is down [View](#event-examples-example-10)
- [x] **Example 11:** More examples — onload (alert stand-in) [View](#event-examples-example-11)
- [x] **Example 12:** More examples — onfocus background [View](#event-examples-example-12)
- [x] **Example 13:** More examples — mouse events change color [View](#event-examples-example-13)

## Detailed Explanation

- [x] Attributes vs `element.onclick = fn`.
- [x] `oninput` (live) vs `onchange` (committed).
- [x] mousedown → mouseup → click.

<a id="event-examples-example-01"></a>

### **Example 1: Change text when the paragraph is clicked**

- [x] `onclick` on a `<h1>` (or any element) can rewrite its own `innerHTML`.
- [x] The W3Schools first Tryit turns “Click on this text!” into a new message.
- [x] This is reacting to events with an **HTML attribute**.

Sandbox: `code_sandbox/event-examples/click-text.html`

```html
<h1 onclick="this.innerHTML = 'Ooops!'">Click on this text!</h1>
```

<img alt="event-examples example 1 source" src="./code_sandbox/snaps/event-examples-01-code.png" />

<img alt="event-examples example 1 result" src="./code_sandbox/snaps/event-examples-01-result.png" />

- [x] **Outcome:** After click, the heading is **Ooops!**.

<a id="event-examples-example-02"></a>

### **Example 2: Call a function and pass this**

- [x] `onclick="changeText(this)"` passes the element into the function as `id` (their parameter name).
- [x] The function assigns `id.innerHTML = "Ooops!"`.
- [x] Passing `this` is how attribute handlers share the element without `getElementById`.

Sandbox: `code_sandbox/event-examples/click-function-id.html`

```html
<h1 onclick="changeText(this)">Click on this text!</h1>
<script>
function changeText(id) {
  id.innerHTML = "Ooops!";
}
</script>
```

<img alt="event-examples example 2 source" src="./code_sandbox/snaps/event-examples-02-code.png" />

<img alt="event-examples example 2 result" src="./code_sandbox/snaps/event-examples-02-result.png" />

- [x] **Outcome:** The heading becomes **Ooops!** via `changeText(this)`.

<a id="event-examples-example-03"></a>

### **Example 3: HTML event attribute on a button**

- [x] `onclick="displayDate()"` on a button is the classic HTML event attribute.
- [x] The function name in the attribute is called with `()`.
- [x] Works, but mixes concerns — later examples assign from JS.

Sandbox: `code_sandbox/event-examples/assign-onclick-attr.html`

```html
<button type="button" onclick="displayDate()">Try it</button>
```

<img alt="event-examples example 3 source" src="./code_sandbox/snaps/event-examples-03-code.png" />

<img alt="event-examples example 3 result" src="./code_sandbox/snaps/event-examples-03-result.png" />

- [x] **Outcome:** `displayDate` runs and writes the date.

<a id="event-examples-example-04"></a>

### **Example 4: Assign onclick with the HTML DOM**

- [x] `document.getElementById("myBtn").onclick = displayDate;` — no `()` on the right-hand side.
- [x] You pass the **function object**. Writing `displayDate()` would run it immediately and assign its return value (`undefined`).
- [x] This is the DOM assignment style from the W3Schools page.

Sandbox: `code_sandbox/event-examples/assign-onclick-dom.html`

```html
<button type="button" id="myBtn">Try it</button>
<script>
document.getElementById("myBtn").onclick = displayDate;
function displayDate() {
  document.getElementById("out").innerHTML = Date();
}
</script>
```

<img alt="event-examples example 4 source" src="./code_sandbox/snaps/event-examples-04-code.png" />

<img alt="event-examples example 4 result" src="./code_sandbox/snaps/event-examples-04-result.png" />

- [x] **Outcome:** Clicking the button fills **Date()** via the assigned `onclick` property.

<a id="event-examples-example-05"></a>

### **Example 5: onload and onunload**

- [x] `onload` / `onunload` fire when the user **enters** or **leaves** the page.
- [x] Historically used to sniff the browser or handle cookies. `onunload` is unreliable on mobile.
- [x] Prefer `addEventListener("load" / "pagehide")` today. This demo records that load ran.

Sandbox: `code_sandbox/event-examples/onload-unonload.html`

```html
<body onload="checkCookies()">
```

<img alt="event-examples example 5 source" src="./code_sandbox/snaps/event-examples-05-code.png" />

<img alt="event-examples example 5 result" src="./code_sandbox/snaps/event-examples-05-result.png" />

- [x] **Outcome:** The load-style function runs and prints **onload fired** (cookies API may be empty on file://).

<a id="event-examples-example-06"></a>

### **Example 6: The oninput event**

- [x] `oninput` fires on **every** change while the user types (unlike `onchange`).
- [x] W3Schools uses it to copy the field into another element live.
- [x] The snapshot sets a value and dispatches `input`.

Sandbox: `code_sandbox/event-examples/oninput.html`

```html
<input id="fname" oninput="document.getElementById('out').innerHTML = this.value">
<p id="out"></p>
```

<img alt="event-examples example 6 source" src="./code_sandbox/snaps/event-examples-06-code.png" />

<img alt="event-examples example 6 result" src="./code_sandbox/snaps/event-examples-06-result.png" />

- [x] **Outcome:** Output shows **Hi** after the input event.

<a id="event-examples-example-07"></a>

### **Example 7: The onchange event — upperCase**

- [x] `onchange` is often paired with **validation** or formatting after the user leaves the field.
- [x] W3Schools `upperCase()` runs when the content **changes** (committed).
- [x] The snapshot sets `hello` and fires `change` so the field becomes **HELLO**.

Sandbox: `code_sandbox/event-examples/onchange-upper.html`

```html
<input id="fname" onchange="this.value = this.value.toUpperCase()">
```

<img alt="event-examples example 7 source" src="./code_sandbox/snaps/event-examples-07-code.png" />

<img alt="event-examples example 7 result" src="./code_sandbox/snaps/event-examples-07-result.png" />

- [x] **Outcome:** The input value is **HELLO** after `change`.

<a id="event-examples-example-08"></a>

### **Example 8: onmouseover and onmouseout**

- [x] Hover in/out can trigger functions that restyle or rewrite text.
- [x] W3Schools “Mouse Over Me” box uses these two events.
- [x] The snapshot ends on **mouseout** so the leave style is visible.

Sandbox: `code_sandbox/event-examples/mouseover-out-color.html`

```html
<div onmouseover="this.style.color='red'" onmouseout="this.style.color='black'">Mouse Over Me</div>
```

<img alt="event-examples example 8 source" src="./code_sandbox/snaps/event-examples-08-code.png" />

<img alt="event-examples example 8 result" src="./code_sandbox/snaps/event-examples-08-result.png" />

- [x] **Outcome:** After over then out, `style.color` is **black** again; the log notes both handlers ran.

<a id="event-examples-example-09"></a>

### **Example 9: onmousedown, onmouseup, and onclick**

- [x] A full click is three events: **mousedown**, **mouseup**, **onclick** in that order.
- [x] W3Schools “Click Me” demonstrates the sequence.
- [x] The snapshot dispatches all three and logs the order.

Sandbox: `code_sandbox/event-examples/down-up-click.html`

```html
<div id="box">Click Me</div>
```

<img alt="event-examples example 9 source" src="./code_sandbox/snaps/event-examples-09-code.png" />

<img alt="event-examples example 9 result" src="./code_sandbox/snaps/event-examples-09-result.png" />

- [x] **Outcome:** The log is **down -> up -> click**.

<a id="event-examples-example-10"></a>

### **Example 10: More examples — change an image while the mouse is down**

- [x] `onmousedown` / `onmouseup` can swap `img.src` for a “pressed” look.
- [x] This sandbox uses two local SVG files as the two states.
- [x] The snapshot holds **mousedown** so you see the down image.

Sandbox: `code_sandbox/event-examples/mousedown-image.html`

```html
<img id="light" alt="bulb" width="48" height="48"
  onmousedown="this.src='down.svg'" onmouseup="this.src='up.svg'" src="up.svg">
```

<img alt="event-examples example 10 source" src="./code_sandbox/snaps/event-examples-10-code.png" />

<img alt="event-examples example 10 result" src="./code_sandbox/snaps/event-examples-10-result.png" />

- [x] **Outcome:** `src` after mousedown is **down.svg**.

<a id="event-examples-example-11"></a>

### **Example 11: More examples — onload (alert stand-in)**

- [x] The site’s extra example **alerts** when the page has finished loading.
- [x] Alerts are blocked/hidden in screenshots, so we write to `#demo` instead — same event.
- [x] Do not use `alert` for real UX; this is a teaching stand-in.

Sandbox: `code_sandbox/event-examples/onload-alert.html`

```html
<body onload="alert('Page loaded')">
```

<img alt="event-examples example 11 source" src="./code_sandbox/snaps/event-examples-11-code.png" />

<img alt="event-examples example 11 result" src="./code_sandbox/snaps/event-examples-11-result.png" />

- [x] **Outcome:** The load handler runs and prints **Page loaded** (alert replaced with DOM text).

<a id="event-examples-example-12"></a>

### **Example 12: More examples — onfocus background**

- [x] `onfocus` fires when the control becomes the **active** field (click or Tab).
- [x] W3Schools changes `backgroundColor` on focus so the user sees the caret field.
- [x] The snapshot focuses the input.

Sandbox: `code_sandbox/event-examples/onfocus-bg.html`

```html
<input id="n" onfocus="this.style.background='yellow'">
```

<img alt="event-examples example 12 source" src="./code_sandbox/snaps/event-examples-12-code.png" />

<img alt="event-examples example 12 result" src="./code_sandbox/snaps/event-examples-12-result.png" />

- [x] **Outcome:** After `focus()`, `style.background` is **yellow**.

<a id="event-examples-example-13"></a>

### **Example 13: More examples — mouse events change color**

- [x] A compact hover: change `style.color` when the cursor moves over the element.
- [x] This is the “Mouse Events Change the color…” extra example.
- [x] The snapshot stops on **mouseover** so the color is **red** in the result.

Sandbox: `code_sandbox/event-examples/mouse-events-color.html`

```html
<h2 onmouseover="this.style.color='red'">Mouse over me</h2>
```

<img alt="event-examples example 13 source" src="./code_sandbox/snaps/event-examples-13-code.png" />

<img alt="event-examples example 13 result" src="./code_sandbox/snaps/event-examples-13-result.png" />

- [x] **Outcome:** The heading `style.color` is **red** after mouseover.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/event-examples/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `onclick="changeText(this)"` pass?

<details>
<summary>Answer</summary>

- [x] The **element** that was clicked (`this`).

</details>

### Question 2: Why assign `onclick = displayDate` without `()`?

<details>
<summary>Answer</summary>

- [x] So you store the **function**, not the result of calling it now.

</details>

### Question 3: `oninput` vs `onchange` on a text field?

<details>
<summary>Answer</summary>

- [x] `oninput` fires **as you type**. `onchange` fires when the value is **committed**.

</details>

### Question 4: What is the mousedown → click order?

<details>
<summary>Answer</summary>

- [x] **mousedown**, **mouseup**, **onclick**.

</details>

### Question 5: What are `onload` / `onunload` for?

<details>
<summary>Answer</summary>

- [x] Entering / leaving the page. Prefer `addEventListener` today; `onunload` is flaky on mobile.

</details>

### Question 6: How can you highlight a field on focus?

<details>
<summary>Answer</summary>

- [x] `onfocus` → set **`style.background`**.

</details>

### Question 7: Why replace `alert` in the sandbox?

<details>
<summary>Answer</summary>

- [x] Alerts are a poor snapshot target; the **event** is the same.

</details>

### Question 8: Can any element have `onclick`?

<details>
<summary>Answer</summary>

- [x] Yes — headings, divs, images — not only buttons. Prefer real `<button>` for accessibility.

</details>

### Question 9: What does the upperCase onchange example do?

<details>
<summary>Answer</summary>

- [x] It rewrites the field to **uppercase** when `change` fires.

</details>

### Question 10: How do you swap an image on press?

<details>
<summary>Answer</summary>

- [x] Set **`src`** in `onmousedown` and restore it in `onmouseup`.

</details>


</details>

## Summary

You can attach events in HTML or from JavaScript. Know the event you need (`input` vs `change`, `focus`, mouse sequence) and prefer listeners as apps grow.

## References

- [Event Examples](https://www.w3schools.com/js/js_htmldom_events.asp)
- [MDN EventTarget.addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)

</details>
