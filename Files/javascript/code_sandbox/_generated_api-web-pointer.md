<details>
  <summary>API Web Pointer</summary>

## Introduction

Pointer events unify mouse, pen, and touch. Names mirror mouse events (`pointerdown`, …). Extra properties include pointerId, pointerType, isPrimary, and pressure. CSS `pointer-events` is a separate targeting switch.

This section has **16** examples:

- [x] **Example 1:** pointerdown event [View](#api-web-pointer-example-01)
- [x] **Example 2:** pointerup event [View](#api-web-pointer-example-02)
- [x] **Example 3:** pointermove event [View](#api-web-pointer-example-03)
- [x] **Example 4:** pointerover event [View](#api-web-pointer-example-04)
- [x] **Example 5:** pointerout event [View](#api-web-pointer-example-05)
- [x] **Example 6:** pointerenter event [View](#api-web-pointer-example-06)
- [x] **Example 7:** pointerleave event [View](#api-web-pointer-example-07)
- [x] **Example 8:** pointercancel event [View](#api-web-pointer-example-08)
- [x] **Example 9:** pointerId property [View](#api-web-pointer-example-09)
- [x] **Example 10:** pointerType property [View](#api-web-pointer-example-10)
- [x] **Example 11:** isPrimary property [View](#api-web-pointer-example-11)
- [x] **Example 12:** pressure property [View](#api-web-pointer-example-12)
- [x] **Example 13:** setPointerCapture — keep receiving events while dragging [View](#api-web-pointer-example-13)
- [x] **Example 14:** CSS pointer-events: none [View](#api-web-pointer-example-14)
- [x] **Example 15:** CSS pointer-events: auto [View](#api-web-pointer-example-15)
- [x] **Example 16:** Unified model — one listener for mouse, pen, and touch [View](#api-web-pointer-example-16)

## Detailed Explanation

- [x] Replace mouse with pointer in the event name.
- [x] enter/leave do not bubble.
- [x] setPointerCapture for dragging.
- [x] pointer-events:none is CSS, not the JS API.

<a id="api-web-pointer-example-01"></a>

### **Example 1: pointerdown event**

- [x] **`pointerdown`** — pointer becomes active (button pressed / contact).
- [x] Pointer names match mouse events: replace **mouse** with **pointer**.
- [x] The sandbox dispatches a synthetic `PointerEvent` so the listener runs without a real mouse/touch.

Sandbox: `code_sandbox/api-web-pointer/pointerdown.html`

```html
el.addEventListener("pointerdown", handler);
```

<img alt="api-web-pointer example 1 source" src="./code_sandbox/snaps/api-web-pointer-01-code.png" />

<img alt="api-web-pointer example 1 result" src="./code_sandbox/snaps/api-web-pointer-01-result.png" />

- [x] **Outcome:** Dispatching `pointerdown` sets the log to **pointerdown**.

<a id="api-web-pointer-example-02"></a>

### **Example 2: pointerup event**

- [x] **`pointerup`** — pointer is no longer active (release / contact ended).
- [x] Pointer names match mouse events: replace **mouse** with **pointer**.
- [x] The sandbox dispatches a synthetic `PointerEvent` so the listener runs without a real mouse/touch.

Sandbox: `code_sandbox/api-web-pointer/pointerup.html`

```html
el.addEventListener("pointerup", handler);
```

<img alt="api-web-pointer example 2 source" src="./code_sandbox/snaps/api-web-pointer-02-code.png" />

<img alt="api-web-pointer example 2 result" src="./code_sandbox/snaps/api-web-pointer-02-result.png" />

- [x] **Outcome:** Dispatching `pointerup` sets the log to **pointerup**.

<a id="api-web-pointer-example-03"></a>

### **Example 3: pointermove event**

- [x] **`pointermove`** — pointer changes coordinates.
- [x] Pointer names match mouse events: replace **mouse** with **pointer**.
- [x] The sandbox dispatches a synthetic `PointerEvent` so the listener runs without a real mouse/touch.

Sandbox: `code_sandbox/api-web-pointer/pointermove.html`

```html
el.addEventListener("pointermove", handler);
```

<img alt="api-web-pointer example 3 source" src="./code_sandbox/snaps/api-web-pointer-03-code.png" />

<img alt="api-web-pointer example 3 result" src="./code_sandbox/snaps/api-web-pointer-03-result.png" />

- [x] **Outcome:** Dispatching `pointermove` sets the log to **pointermove**.

<a id="api-web-pointer-example-04"></a>

### **Example 4: pointerover event**

- [x] **`pointerover`** — pointer moves **into** an element (bubbles).
- [x] Pointer names match mouse events: replace **mouse** with **pointer**.
- [x] The sandbox dispatches a synthetic `PointerEvent` so the listener runs without a real mouse/touch.
- [x] Unlike mouseenter, **over** bubbles.

Sandbox: `code_sandbox/api-web-pointer/pointerover.html`

```html
el.addEventListener("pointerover", handler);
```

<img alt="api-web-pointer example 4 source" src="./code_sandbox/snaps/api-web-pointer-04-code.png" />

<img alt="api-web-pointer example 4 result" src="./code_sandbox/snaps/api-web-pointer-04-result.png" />

- [x] **Outcome:** Dispatching `pointerover` sets the log to **pointerover**.

<a id="api-web-pointer-example-05"></a>

### **Example 5: pointerout event**

- [x] **`pointerout`** — pointer moves **out** of an element (bubbles).
- [x] Pointer names match mouse events: replace **mouse** with **pointer**.
- [x] The sandbox dispatches a synthetic `PointerEvent` so the listener runs without a real mouse/touch.

Sandbox: `code_sandbox/api-web-pointer/pointerout.html`

```html
el.addEventListener("pointerout", handler);
```

<img alt="api-web-pointer example 5 source" src="./code_sandbox/snaps/api-web-pointer-05-code.png" />

<img alt="api-web-pointer example 5 result" src="./code_sandbox/snaps/api-web-pointer-05-result.png" />

- [x] **Outcome:** Dispatching `pointerout` sets the log to **pointerout**.

<a id="api-web-pointer-example-06"></a>

### **Example 6: pointerenter event**

- [x] **`pointerenter`** — like pointerover but **does not bubble**.
- [x] Pointer names match mouse events: replace **mouse** with **pointer**.
- [x] The sandbox dispatches a synthetic `PointerEvent` so the listener runs without a real mouse/touch.

Sandbox: `code_sandbox/api-web-pointer/pointerenter.html`

```html
el.addEventListener("pointerenter", handler);
```

<img alt="api-web-pointer example 6 source" src="./code_sandbox/snaps/api-web-pointer-06-code.png" />

<img alt="api-web-pointer example 6 result" src="./code_sandbox/snaps/api-web-pointer-06-result.png" />

- [x] **Outcome:** Dispatching `pointerenter` sets the log to **pointerenter**.

<a id="api-web-pointer-example-07"></a>

### **Example 7: pointerleave event**

- [x] **`pointerleave`** — like pointerout but **does not bubble**.
- [x] Pointer names match mouse events: replace **mouse** with **pointer**.
- [x] The sandbox dispatches a synthetic `PointerEvent` so the listener runs without a real mouse/touch.

Sandbox: `code_sandbox/api-web-pointer/pointerleave.html`

```html
el.addEventListener("pointerleave", handler);
```

<img alt="api-web-pointer example 7 source" src="./code_sandbox/snaps/api-web-pointer-07-code.png" />

<img alt="api-web-pointer example 7 result" src="./code_sandbox/snaps/api-web-pointer-07-result.png" />

- [x] **Outcome:** Dispatching `pointerleave` sets the log to **pointerleave**.

<a id="api-web-pointer-example-08"></a>

### **Example 8: pointercancel event**

- [x] **`pointercancel`** — the system **cancels** the interaction (OS UI, etc.).
- [x] Pointer names match mouse events: replace **mouse** with **pointer**.
- [x] The sandbox dispatches a synthetic `PointerEvent` so the listener runs without a real mouse/touch.

Sandbox: `code_sandbox/api-web-pointer/pointercancel.html`

```html
el.addEventListener("pointercancel", handler);
```

<img alt="api-web-pointer example 8 source" src="./code_sandbox/snaps/api-web-pointer-08-code.png" />

<img alt="api-web-pointer example 8 result" src="./code_sandbox/snaps/api-web-pointer-08-result.png" />

- [x] **Outcome:** Dispatching `pointercancel` sets the log to **pointercancel**.

<a id="api-web-pointer-example-09"></a>

### **Example 9: pointerId property**

- [x] **Unique id** per pointer — required for multi-touch.
- [x] Mouse is usually id **1**.

Sandbox: `code_sandbox/api-web-pointer/pointer-id.html`

```html
event.pointerId
```

<img alt="api-web-pointer example 9 source" src="./code_sandbox/snaps/api-web-pointer-09-code.png" />

<img alt="api-web-pointer example 9 result" src="./code_sandbox/snaps/api-web-pointer-09-result.png" />

- [x] **Outcome:** The synthetic event’s **pointerId** is **1**.

<a id="api-web-pointer-example-10"></a>

### **Example 10: pointerType property**

- [x] String: **`mouse`**, **`pen`**, or **`touch`**.
- [x] One listener can branch on hardware.

Sandbox: `code_sandbox/api-web-pointer/pointer-type.html`

```html
event.pointerType
```

<img alt="api-web-pointer example 10 source" src="./code_sandbox/snaps/api-web-pointer-10-code.png" />

<img alt="api-web-pointer example 10 result" src="./code_sandbox/snaps/api-web-pointer-10-result.png" />

- [x] **Outcome:** **pointerType=mouse** on the synthetic event.

<a id="api-web-pointer-example-11"></a>

### **Example 11: isPrimary property**

- [x] **true** for the primary pointer (first finger; the mouse).
- [x] Extra fingers are not primary.

Sandbox: `code_sandbox/api-web-pointer/is-primary.html`

```html
event.isPrimary
```

<img alt="api-web-pointer example 11 source" src="./code_sandbox/snaps/api-web-pointer-11-code.png" />

<img alt="api-web-pointer example 11 result" src="./code_sandbox/snaps/api-web-pointer-11-result.png" />

- [x] **Outcome:** **isPrimary=true** for this mouse-like event.

<a id="api-web-pointer-example-12"></a>

### **Example 12: pressure property**

- [x] Normalized **0–1**. Mouse often reports **0.5** when the button is down.
- [x] Pens can vary.

Sandbox: `code_sandbox/api-web-pointer/pressure.html`

```html
event.pressure
```

<img alt="api-web-pointer example 12 source" src="./code_sandbox/snaps/api-web-pointer-12-code.png" />

<img alt="api-web-pointer example 12 result" src="./code_sandbox/snaps/api-web-pointer-12-result.png" />

- [x] **Outcome:** **pressure=0.5** on the synthetic down event.

<a id="api-web-pointer-example-13"></a>

### **Example 13: setPointerCapture — keep receiving events while dragging**

- [x] `element.setPointerCapture(pointerId)` sends later events to **that element** even if the pointer leaves.
- [x] Useful for sliders.
- [x] `hasPointerCapture` confirms it.

Sandbox: `code_sandbox/api-web-pointer/capture.html`

```html
el.setPointerCapture(event.pointerId)
```

<img alt="api-web-pointer example 13 source" src="./code_sandbox/snaps/api-web-pointer-13-code.png" />

<img alt="api-web-pointer example 13 result" src="./code_sandbox/snaps/api-web-pointer-13-result.png" />

- [x] **Outcome:** After capture, `hasPointerCapture(1)` is **true**.

<a id="api-web-pointer-example-14"></a>

### **Example 14: CSS pointer-events: none**

- [x] **Separate** from the Pointer Events API: a CSS property.
- [x] `pointer-events: none` makes the element (and descendants) **not** a target.
- [x] Clicks “fall through” to whatever is underneath.

Sandbox: `code_sandbox/api-web-pointer/css-none.html`

```html
style="pointer-events: none;" 
```

<img alt="api-web-pointer example 14 source" src="./code_sandbox/snaps/api-web-pointer-14-code.png" />

<img alt="api-web-pointer example 14 result" src="./code_sandbox/snaps/api-web-pointer-14-result.png" />

- [x] **Outcome:** Computed `pointer-events` is **none**; `elementFromPoint` over the box is **not** the box itself.

<a id="api-web-pointer-example-15"></a>

### **Example 15: CSS pointer-events: auto**

- [x] `pointer-events: auto` restores **default** targeting.
- [x] Use it to re-enable a layer you had turned off.

Sandbox: `code_sandbox/api-web-pointer/css-auto.html`

```html
style="pointer-events: auto;" 
```

<img alt="api-web-pointer example 15 source" src="./code_sandbox/snaps/api-web-pointer-15-code.png" />

<img alt="api-web-pointer example 15 result" src="./code_sandbox/snaps/api-web-pointer-15-result.png" />

- [x] **Outcome:** Computed value is **auto**.

<a id="api-web-pointer-example-16"></a>

### **Example 16: Unified model — one listener for mouse, pen, and touch**

- [x] The page’s benefit: **one set of listeners** instead of mouse + touch + pen separately.
- [x] Also extra properties: tiltX, tiltY, width, height for pen/touch.
- [x] Recommended approach for modern interactive UI.

Sandbox: `code_sandbox/api-web-pointer/unified.html`

```html
el.addEventListener("pointerdown", onDown); // mouse, pen, and touch
```

<img alt="api-web-pointer example 16 source" src="./code_sandbox/snaps/api-web-pointer-16-code.png" />

<img alt="api-web-pointer example 16 result" src="./code_sandbox/snaps/api-web-pointer-16-result.png" />

- [x] **Outcome:** `PointerEvent` exists and inherits mouse coordinates (`clientX` is a number on the synthetic event).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/api-web-pointer/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do pointer event names relate to mouse events?

<details>
<summary>Answer</summary>

- [x] Replace **mouse** with **pointer** (`mousedown` → `pointerdown`).

</details>

### Question 2: Which pair does **not** bubble?

<details>
<summary>Answer</summary>

- [x] **pointerenter** and **pointerleave**.

</details>

### Question 3: What is `pointerType`?

<details>
<summary>Answer</summary>

- [x] **`mouse`**, **`pen`**, or **`touch`**.

</details>

### Question 4: What is `pointerId` for?

<details>
<summary>Answer</summary>

- [x] Identifying each pointer in **multi-touch**.

</details>

### Question 5: What is `isPrimary`?

<details>
<summary>Answer</summary>

- [x] **true** for the main pointer (mouse / first finger).

</details>

### Question 6: Pressure range?

<details>
<summary>Answer</summary>

- [x] **0 to 1**.

</details>

### Question 7: What does `setPointerCapture` do?

<details>
<summary>Answer</summary>

- [x] The element **keeps** getting events if the pointer leaves it (dragging).

</details>

### Question 8: Is CSS `pointer-events` the same API?

<details>
<summary>Answer</summary>

- [x] **No** — it only controls whether the element can be a **target**.

</details>

### Question 9: What does `pointer-events: none` do?

<details>
<summary>Answer</summary>

- [x] The element is **not** a pointer target (clicks pass through).

</details>

### Question 10: Why prefer pointer events?

<details>
<summary>Answer</summary>

- [x] **One** listener model for mouse, pen, and touch.

</details>


</details>

## Summary

Listen for pointer* events instead of maintaining mouse + touch handlers. Use pointerId for multi-touch and setPointerCapture for drags. CSS pointer-events only changes hit-testing.

## References

- [API Web Pointer](https://www.w3schools.com/js/js_api_pointer_events.asp)
- [MDN Pointer events](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events)

</details>
