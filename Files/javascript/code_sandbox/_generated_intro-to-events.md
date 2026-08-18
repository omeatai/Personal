<details>
  <summary>Intro to Events</summary>

## Introduction

HTML events are things that happen to elements. JavaScript can run when they are detected — via attributes, `onclick` assignment, or `addEventListener`.

This section has **12** examples:

- [x] **Example 1:** onclick attribute — write the date into another element [View](#intro-to-events-example-01)
- [x] **Example 2:** onclick — change this.innerHTML [View](#intro-to-events-example-02)
- [x] **Example 3:** Calling a JavaScript function from onclick [View](#intro-to-events-example-03)
- [x] **Example 4:** Common event — onchange [View](#intro-to-events-example-04)
- [x] **Example 5:** Common event — onclick [View](#intro-to-events-example-05)
- [x] **Example 6:** Common event — onmouseover [View](#intro-to-events-example-06)
- [x] **Example 7:** Common event — onmouseout [View](#intro-to-events-example-07)
- [x] **Example 8:** Common event — onkeydown [View](#intro-to-events-example-08)
- [x] **Example 9:** Common event — onload [View](#intro-to-events-example-09)
- [x] **Example 10:** What event handlers are for [View](#intro-to-events-example-10)
- [x] **Example 11:** Not recommended — onclick attribute [View](#intro-to-events-example-11)
- [x] **Example 12:** Highly recommended — addEventListener [View](#intro-to-events-example-12)

## Detailed Explanation

- [x] Event attributes vs functions vs listeners.
- [x] Common events: change, click, mouseover/out, keydown, load.
- [x] `addEventListener` is the recommended style.

<a id="intro-to-events-example-01"></a>

### **Example 1: onclick attribute — write the date into another element**

- [x] HTML event attributes run JavaScript when something happens to that element.
- [x] `onclick="document.getElementById('demo').innerHTML = Date()"` assigns a handler in markup.
- [x] Quotes: use single quotes inside a double-quoted attribute (or vice versa).
- [x] The snapshot clicks the button so the date string appears.

Sandbox: `code_sandbox/intro-to-events/onclick-date.html`

```html
<button type="button" onclick="document.getElementById('out').innerHTML = Date()">
  The time is?
</button>
<p id="out"></p>
```

<img alt="intro-to-events example 1 source" src="./code_sandbox/snaps/intro-to-events-01-code.png" />

<img alt="intro-to-events example 1 result" src="./code_sandbox/snaps/intro-to-events-01-result.png" />

- [x] **Outcome:** After click, the paragraph shows a **date/time string**.

<a id="intro-to-events-example-02"></a>

### **Example 2: onclick — change this.innerHTML**

- [x] `this` inside an HTML event attribute is the **element** that received the event.
- [x] `this.innerHTML = Date()` replaces the button’s own label with the time.
- [x] In an `addEventListener` callback, `this` is also the element (unless you use an arrow function).

Sandbox: `code_sandbox/intro-to-events/onclick-this.html`

```html
<button type="button" onclick="this.innerHTML = Date()">The time is?</button>
```

<img alt="intro-to-events example 2 source" src="./code_sandbox/snaps/intro-to-events-02-code.png" />

<img alt="intro-to-events example 2 result" src="./code_sandbox/snaps/intro-to-events-02-result.png" />

- [x] **Outcome:** The button caption becomes the **Date()** string.

<a id="intro-to-events-example-03"></a>

### **Example 3: Calling a JavaScript function from onclick**

- [x] Longer code belongs in a **named function**, then `onclick="displayDate()"`.
- [x] That keeps markup short and lets you reuse the same function on several controls.
- [x] Remember the `()` in the HTML attribute — that **calls** the function.

Sandbox: `code_sandbox/intro-to-events/onclick-function.html`

```html
<button type="button" onclick="displayDate()">The time is?</button>
<p id="out"></p>
<script>
function displayDate() {
  document.getElementById("out").innerHTML = Date();
}
</script>
```

<img alt="intro-to-events example 3 source" src="./code_sandbox/snaps/intro-to-events-03-code.png" />

<img alt="intro-to-events example 3 result" src="./code_sandbox/snaps/intro-to-events-03-result.png" />

- [x] **Outcome:** `displayDate()` runs on click and fills the paragraph with **Date()**.

<a id="intro-to-events-example-04"></a>

### **Example 4: Common event — onchange**

- [x] `onchange` fires when an input/select **commits** a new value (often on blur for text, immediately for select).
- [x] Typical use: validate or copy the field after the user finishes editing.
- [x] The snapshot sets a value and dispatches `change`.

Sandbox: `code_sandbox/intro-to-events/onchange.html`

```html
<input id="n" onchange="document.getElementById('out').textContent = this.value">
<p id="out"></p>
```

<img alt="intro-to-events example 4 source" src="./code_sandbox/snaps/intro-to-events-04-code.png" />

<img alt="intro-to-events example 4 result" src="./code_sandbox/snaps/intro-to-events-04-result.png" />

- [x] **Outcome:** After `change`, the output paragraph shows **Ada**.

<a id="intro-to-events-example-05"></a>

### **Example 5: Common event — onclick**

- [x] `onclick` / `click` — the user clicks an element (mousedown + mouseup on the same target).
- [x] Most buttons and fake-buttons use this event.
- [x] Prefer `addEventListener("click", …)` over the HTML attribute for non-trivial apps.

Sandbox: `code_sandbox/intro-to-events/onclick-named.html`

```html
<button type="button" id="b">Click</button>
```

<img alt="intro-to-events example 5 source" src="./code_sandbox/snaps/intro-to-events-05-code.png" />

<img alt="intro-to-events example 5 result" src="./code_sandbox/snaps/intro-to-events-05-result.png" />

- [x] **Outcome:** The click handler prints **clicked**.

<a id="intro-to-events-example-06"></a>

### **Example 6: Common event — onmouseover**

- [x] Fires when the pointer **enters** the element (and also when it enters a child — it bubbles).
- [x] Used for hover highlights. `mouseenter` is the non-bubbling cousin.
- [x] The snapshot dispatches `mouseover`.

Sandbox: `code_sandbox/intro-to-events/onmouseover.html`

```html
<div id="box">Mouse Over Me</div>
```

<img alt="intro-to-events example 6 source" src="./code_sandbox/snaps/intro-to-events-06-code.png" />

<img alt="intro-to-events example 6 result" src="./code_sandbox/snaps/intro-to-events-06-result.png" />

- [x] **Outcome:** After `mouseover`, the box text is **hovered**.

<a id="intro-to-events-example-07"></a>

### **Example 7: Common event — onmouseout**

- [x] Fires when the pointer **leaves** the element (also bubbles from children).
- [x] Pair with `mouseover` for hover in/out. `mouseleave` does not fire when moving to a child.
- [x] The snapshot dispatches `mouseout`.

Sandbox: `code_sandbox/intro-to-events/onmouseout.html`

```html
<div id="box">Mouse Over Me</div>
```

<img alt="intro-to-events example 7 source" src="./code_sandbox/snaps/intro-to-events-07-code.png" />

<img alt="intro-to-events example 7 result" src="./code_sandbox/snaps/intro-to-events-07-result.png" />

- [x] **Outcome:** After `mouseout`, the box text is **left**.

<a id="intro-to-events-example-08"></a>

### **Example 8: Common event — onkeydown**

- [x] Fires when a key is **pressed down** (repeats if held).
- [x] `event.key` is the character/name (`"a"`, `"Enter"`). `event.code` is the physical key (`"KeyA"`).
- [x] `keypress` is deprecated — use `keydown` / `keyup`.

Sandbox: `code_sandbox/intro-to-events/onkeydown.html`

```html
<input id="k">
```

<img alt="intro-to-events example 8 source" src="./code_sandbox/snaps/intro-to-events-08-code.png" />

<img alt="intro-to-events example 8 result" src="./code_sandbox/snaps/intro-to-events-08-result.png" />

- [x] **Outcome:** Dispatching keydown for **Z** prints **You pressed: Z**.

<a id="intro-to-events-example-09"></a>

### **Example 9: Common event — onload**

- [x] `window.onload` / `window` `load` fires when the **page and resources** (images, CSS) have loaded.
- [x] `DOMContentLoaded` is earlier — HTML is ready, images maybe not.
- [x] This script has already loaded, so we record that the `load` path ran (or we fire it).

Sandbox: `code_sandbox/intro-to-events/onload.html`

```html
<script>
window.onload = function () {
  document.getElementById("demo").innerText = "page loaded";
};
</script>
```

<img alt="intro-to-events example 9 source" src="./code_sandbox/snaps/intro-to-events-09-code.png" />

<img alt="intro-to-events example 9 result" src="./code_sandbox/snaps/intro-to-events-09-result.png" />

- [x] **Outcome:** The handler reports **page loaded** (the event already happened, or we invoke the same function).

<a id="intro-to-events-example-10"></a>

### **Example 10: What event handlers are for**

- [x] Handlers verify input, run actions on click, and set up the page on load.
- [x] You can: put JS in an HTML attribute; call a function from an attribute; assign `element.onclick = fn`; prevent default.
- [x] The next pages cover mouse, keyboard, load, and `addEventListener` in depth.

Sandbox: `code_sandbox/intro-to-events/handlers-uses.html`

```html
<script>
const uses = [
  "Things that should be done every time a page loads",
  "Action when a user clicks a button",
  "Content verified when a user inputs data"
];
</script>
```

<img alt="intro-to-events example 10 source" src="./code_sandbox/snaps/intro-to-events-10-code.png" />

<img alt="intro-to-events example 10 result" src="./code_sandbox/snaps/intro-to-events-10-result.png" />

- [x] **Outcome:** The snapshot lists typical handler jobs: **load**, **click**, **input check**.

<a id="intro-to-events-example-11"></a>

### **Example 11: Not recommended — onclick attribute**

- [x] HTML `onclick` is easy, but it **mixes** behavior into markup.
- [x] You can attach only **one** `onclick` property later without `addEventListener`.
- [x] W3Schools still shows it, then marks `addEventListener` as **highly recommended**.

Sandbox: `code_sandbox/intro-to-events/onclick-not-recommended.html`

```html
<button type="button" onclick="displayDate()">Time is?</button>
<script>
function displayDate() {
  document.getElementById("out").innerHTML = Date();
}
</script>
```

<img alt="intro-to-events example 11 source" src="./code_sandbox/snaps/intro-to-events-11-code.png" />

<img alt="intro-to-events example 11 result" src="./code_sandbox/snaps/intro-to-events-11-result.png" />

- [x] **Outcome:** The attribute still works — the date appears — but the next example is the preferred style.

<a id="intro-to-events-example-12"></a>

### **Example 12: Highly recommended — addEventListener**

- [x] `addEventListener("click", fn)` keeps HTML and JS **separate**.
- [x] You can add **many** listeners. The event name has **no** `on` prefix (`"click"` not `"onclick"`).
- [x] This is the style the rest of the Events group uses.

Sandbox: `code_sandbox/intro-to-events/addeventlistener-recommended.html`

```html
<button type="button" id="myBtn">Click me</button>
<p id="out"></p>
<script>
const btn = document.getElementById("myBtn");
btn.addEventListener("click", function () {
  document.getElementById("out").innerHTML = Date();
});
</script>
```

<img alt="intro-to-events example 12 source" src="./code_sandbox/snaps/intro-to-events-12-code.png" />

<img alt="intro-to-events example 12 result" src="./code_sandbox/snaps/intro-to-events-12-result.png" />

- [x] **Outcome:** The listener writes **Date()** into the paragraph after click.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/intro-to-events/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is an HTML event?

<details>
<summary>Answer</summary>

- [x] Something that happens to an element: click, load, key, mouse move, input change.

</details>

### Question 2: How do you put JS in an attribute with nested quotes?

<details>
<summary>Answer</summary>

- [x] Double-quoted attribute, **single quotes** inside (or the reverse).

</details>

### Question 3: What is `this` in `onclick="this.innerHTML = Date()"`?

<details>
<summary>Answer</summary>

- [x] The **element** that was clicked.

</details>

### Question 4: Why call a function from `onclick` instead of a long script?

<details>
<summary>Answer</summary>

- [x] Keeps markup short and the function **reusable**.

</details>

### Question 5: When does `onchange` usually fire on a text field?

<details>
<summary>Answer</summary>

- [x] When the value is **committed** (often on blur), not on every key.

</details>

### Question 6: What is the modern event name for a click listener?

<details>
<summary>Answer</summary>

- [x] **`"click"`** — no `on` prefix.

</details>

### Question 7: `keydown` vs deprecated `keypress`?

<details>
<summary>Answer</summary>

- [x] Use **`keydown` / `keyup`**. `keypress` skips many control keys and is deprecated.

</details>

### Question 8: `load` vs `DOMContentLoaded`?

<details>
<summary>Answer</summary>

- [x] `DOMContentLoaded` is HTML ready. **`load`** waits for images, CSS, frames too.

</details>

### Question 9: Why is `addEventListener` recommended?

<details>
<summary>Answer</summary>

- [x] Separates JS from HTML and lets you add **multiple** handlers.

</details>

### Question 10: Can you assign two functions to `element.onclick`?

<details>
<summary>Answer</summary>

- [x] The second assignment **replaces** the first. Use `addEventListener` to stack them.

</details>


</details>

## Summary

Detect events, then run a function. Prefer `addEventListener("click", fn)` over inline `onclick` for anything beyond a tiny demo.

## References

- [Intro to Events](https://www.w3schools.com/js/js_events.asp)
- [MDN EventTarget.addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)

</details>
