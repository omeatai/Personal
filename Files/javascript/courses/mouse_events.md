# Mouse Events

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Mouse events fire for clicks, movement, wheel, right-click, and drag. The event object carries viewport coordinates.

This section has **10** examples:

- [x] **Example 1:** mouseover and mouseout on a box [View](#mouse-events-example-01)
- [x] **Example 2:** click [View](#mouse-events-example-02)
- [x] **Example 3:** dblclick [View](#mouse-events-example-03)
- [x] **Example 4:** mousedown / mouseup [View](#mouse-events-example-04)
- [x] **Example 5:** mousemove [View](#mouse-events-example-05)
- [x] **Example 6:** mouseenter / mouseleave [View](#mouse-events-example-06)
- [x] **Example 7:** contextmenu [View](#mouse-events-example-07)
- [x] **Example 8:** wheel [View](#mouse-events-example-08)
- [x] **Example 9:** drag events [View](#mouse-events-example-09)
- [x] **Example 10:** Mouse position — event.clientX and event.clientY [View](#mouse-events-example-10)

## Detailed Explanation

- [x] click / dblclick / down / up / move / over / out / enter / leave / contextmenu / wheel / drag.
- [x] `clientX` and `clientY` are viewport coordinates.
- [x] Pointer Events cover mouse + touch + pen.

<a id="mouse-events-example-01"></a>

### **Example 1: mouseover and mouseout on a box**

- [x] `mouseover` — pointer enters the element (bubbles; also fires on children).
- [x] `mouseout` — pointer leaves (same bubbling caveat).
- [x] The snapshot fires both in order so the final text is the **out** message.

Sandbox: `code_sandbox/mouse-events/over-out.html`

```html
<div id="box">Move mouse over this box</div>
<script>
const box = document.getElementById("box");
box.addEventListener("mouseover", function () { box.innerHTML = "Mouse is over me!"; });
box.addEventListener("mouseout", function () { box.innerHTML = "Mouse is out!"; });
</script>
```

<img alt="mouse-events example 1 source" src="../code_sandbox/snaps/mouse-events-01-code.png" />

<img alt="mouse-events example 1 result" src="../code_sandbox/snaps/mouse-events-01-result.png" />

- [x] **Outcome:** After simulated over then out, the box reads **Mouse is out!**.

<a id="mouse-events-example-02"></a>

### **Example 2: click**

- [x] Fires after **mousedown + mouseup** on the same element with the main button (usually left).
- [x] Keyboard activation of a button also synthesizes click.
- [x] This is the default event for buttons.

Sandbox: `code_sandbox/mouse-events/click.html`

```html
<button type="button" id="b">Click</button>
```

<img alt="mouse-events example 2 source" src="../code_sandbox/snaps/mouse-events-02-code.png" />

<img alt="mouse-events example 2 result" src="../code_sandbox/snaps/mouse-events-02-result.png" />

- [x] **Outcome:** `click` fires: **clicked**.

<a id="mouse-events-example-03"></a>

### **Example 3: dblclick**

- [x] Fires after **two rapid clicks** on the same element.
- [x] A dblclick is preceded by two `click` events — don’t double-count work.
- [x] The snapshot dispatches `dblclick` directly.

Sandbox: `code_sandbox/mouse-events/dblclick.html`

```html
<button type="button" id="b">Double-click</button>
```

<img alt="mouse-events example 3 source" src="../code_sandbox/snaps/mouse-events-03-code.png" />

<img alt="mouse-events example 3 result" src="../code_sandbox/snaps/mouse-events-03-result.png" />

- [x] **Outcome:** `dblclick` fires: **double**.

<a id="mouse-events-example-04"></a>

### **Example 4: mousedown / mouseup**

- [x] `mousedown` — button pressed. `mouseup` — button released.
- [x] Order for a full click: mousedown → mouseup → click.
- [x] Useful for “press and hold” (swap an image while the button is down).

Sandbox: `code_sandbox/mouse-events/mousedown-mouseup.html`

```html
<button type="button" id="b">Hold</button>
```

<img alt="mouse-events example 4 source" src="../code_sandbox/snaps/mouse-events-04-code.png" />

<img alt="mouse-events example 4 result" src="../code_sandbox/snaps/mouse-events-04-result.png" />

- [x] **Outcome:** The log shows **down** then **up**.

<a id="mouse-events-example-05"></a>

### **Example 5: mousemove**

- [x] Fires **continuously** as the pointer moves over the element.
- [x] The event object has coordinates (`clientX` / `clientY`).
- [x] Throttle or ignore extra moves if you do heavy work — this event is chatty.

Sandbox: `code_sandbox/mouse-events/mousemove.html`

```html
<div id="box">move</div>
```

<img alt="mouse-events example 5 source" src="../code_sandbox/snaps/mouse-events-05-code.png" />

<img alt="mouse-events example 5 result" src="../code_sandbox/snaps/mouse-events-05-result.png" />

- [x] **Outcome:** A dispatched `mousemove` at (40, 50) is recorded.

<a id="mouse-events-example-06"></a>

### **Example 6: mouseenter / mouseleave**

- [x] Like over/out but they **do not bubble** and **do not fire** when moving between a parent and its child.
- [x] Closer to CSS `:hover` on that one element.
- [x] Prefer these for “is the pointer inside this widget?”

Sandbox: `code_sandbox/mouse-events/mouseenter-leave.html`

```html
<div id="box"><span>child</span></div>
```

<img alt="mouse-events example 6 source" src="../code_sandbox/snaps/mouse-events-06-code.png" />

<img alt="mouse-events example 6 result" src="../code_sandbox/snaps/mouse-events-06-result.png" />

- [x] **Outcome:** Dispatched `mouseenter` then `mouseleave` update the log.

<a id="mouse-events-example-07"></a>

### **Example 7: contextmenu**

- [x] Fires when the user tries to open the **context menu** (usually right-click).
- [x] `preventDefault()` blocks the browser menu if you draw your own.
- [x] The snapshot dispatches `contextmenu` and prevents the default.

Sandbox: `code_sandbox/mouse-events/contextmenu.html`

```html
<div id="box">right-click</div>
```

<img alt="mouse-events example 7 source" src="../code_sandbox/snaps/mouse-events-07-code.png" />

<img alt="mouse-events example 7 result" src="../code_sandbox/snaps/mouse-events-07-result.png" />

- [x] **Outcome:** The handler runs and reports **contextmenu blocked**.

<a id="mouse-events-example-08"></a>

### **Example 8: wheel**

- [x] Fires when the **mouse wheel** (or trackpad scroll) rotates.
- [x] `event.deltaY` is the vertical scroll amount.
- [x] Used for custom zoom or scrolljacking — use sparingly for accessibility.

Sandbox: `code_sandbox/mouse-events/wheel.html`

```html
<div id="box">wheel me</div>
```

<img alt="mouse-events example 8 source" src="../code_sandbox/snaps/mouse-events-08-code.png" />

<img alt="mouse-events example 8 result" src="../code_sandbox/snaps/mouse-events-08-result.png" />

- [x] **Outcome:** `wheel` with `deltaY=100` is logged.

<a id="mouse-events-example-09"></a>

### **Example 9: drag events**

- [x] Drag-and-drop uses a set: `dragstart`, `drag`, `dragover`, `drop`, `dragend`, …
- [x] The source needs `draggable="true"`. `dragover` must `preventDefault` to allow drop.
- [x] This sandbox starts a drag on a draggable item and records **dragstart**.

Sandbox: `code_sandbox/mouse-events/drag.html`

```html
<div id="item" draggable="true">drag me</div>
```

<img alt="mouse-events example 9 source" src="../code_sandbox/snaps/mouse-events-09-code.png" />

<img alt="mouse-events example 9 result" src="../code_sandbox/snaps/mouse-events-09-result.png" />

- [x] **Outcome:** `dragstart` fires on the draggable item.

<a id="mouse-events-example-10"></a>

### **Example 10: Mouse position — event.clientX and event.clientY**

- [x] `MouseEvent.clientX` / `clientY` are coordinates **relative to the viewport** (not the element).
- [x] The W3Schools demo listens on `document` `mousemove` and writes `X: … Y: …`.
- [x] For touch/pen as well, look at the **Pointer Events** API.

Sandbox: `code_sandbox/mouse-events/clientxy.html`

```html
<p id="out">Move the mouse in this window!</p>
<script>
document.addEventListener("mousemove", function (event) {
  document.getElementById("out").innerHTML = "X: " + event.clientX + " Y: " + event.clientY;
});
</script>
```

<img alt="mouse-events example 10 source" src="../code_sandbox/snaps/mouse-events-10-code.png" />

<img alt="mouse-events example 10 result" src="../code_sandbox/snaps/mouse-events-10-result.png" />

- [x] **Outcome:** A synthetic mousemove at **(120, 80)** prints those coordinates.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/mouse-events/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Order of events in a normal click?

<details>
<summary>Answer</summary>

- [x] **mousedown** → **mouseup** → **click**.

</details>

### Question 2: Why might `mouseover` fire when moving between a parent and child?

<details>
<summary>Answer</summary>

- [x] It **bubbles** and also fires when entering descendants. Use **`mouseenter`** for :hover-like behavior.

</details>

### Question 3: What is `dblclick` preceded by?

<details>
<summary>Answer</summary>

- [x] Two **`click`** events.

</details>

### Question 4: What are `clientX` / `clientY` relative to?

<details>
<summary>Answer</summary>

- [x] The **viewport**, not the element.

</details>

### Question 5: How do you stop the browser context menu?

<details>
<summary>Answer</summary>

- [x] Listen for **`contextmenu`** and call **`preventDefault()`**.

</details>

### Question 6: Which event reports wheel rotation?

<details>
<summary>Answer</summary>

- [x] **`wheel`** (`deltaY`).

</details>

### Question 7: What attribute makes an element draggable?

<details>
<summary>Answer</summary>

- [x] **`draggable="true"`**.

</details>

### Question 8: Modern replacement covering mouse + touch + pen?

<details>
<summary>Answer</summary>

- [x] The **Pointer Events** API.

</details>

### Question 9: Is `mousemove` a good place for heavy work?

<details>
<summary>Answer</summary>

- [x] Usually no — it fires **very often**. Throttle or debounce.

</details>

### Question 10: Does `mouseleave` fire when entering a child?

<details>
<summary>Answer</summary>

- [x] **No** — that is the point vs `mouseout`.

</details>


</details>

## Summary

Pick the mouse event that matches the gesture. Use enter/leave for hover widgets and `preventDefault` on `contextmenu` only when you replace the menu.

## References

- [Mouse Events](https://www.w3schools.com/js/js_events_mouse.asp)
- [MDN EventTarget.addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
