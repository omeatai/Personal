# Event Listener

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

`addEventListener` attaches handlers without overwriting others, works on any EventTarget, supports capture vs bubble, and pairs with `removeEventListener`.

This section has **11** examples:

- [x] **Example 1:** addEventListener that fires on button click [View](#event-listener-example-01)
- [x] **Example 2:** Syntax — event, function, useCapture [View](#event-listener-example-02)
- [x] **Example 3:** Anonymous function handler [View](#event-listener-example-03)
- [x] **Example 4:** Named function handler [View](#event-listener-example-04)
- [x] **Example 5:** Many handlers of the same type [View](#event-listener-example-05)
- [x] **Example 6:** Different event types on the same element [View](#event-listener-example-06)
- [x] **Example 7:** Listener on window — resize [View](#event-listener-example-07)
- [x] **Example 8:** Passing parameters with an anonymous wrapper [View](#event-listener-example-08)
- [x] **Example 9:** Event bubbling vs capturing [View](#event-listener-example-09)
- [x] **Example 10:** Bubbling (useCapture false) for comparison [View](#event-listener-example-10)
- [x] **Example 11:** removeEventListener [View](#event-listener-example-11)

## Detailed Explanation

- [x] No `on` prefix.
- [x] Many listeners per element.
- [x] Capture = outer first; bubble = inner first.

<a id="event-listener-example-01"></a>

### **Example 1: addEventListener that fires on button click**

- [x] `document.getElementById("myBtn").addEventListener("click", displayDate);`
- [x] The method attaches a handler **without overwriting** other listeners.
- [x] Event name: `"click"`, not `"onclick"`.

Sandbox: `code_sandbox/event-listener/add-displaydate.html`

```html
<button type="button" id="myBtn">Try it</button>
<script>
document.getElementById("myBtn").addEventListener("click", displayDate);
function displayDate() {
  document.getElementById("out").innerHTML = Date();
}
</script>
```

<img alt="event-listener example 1 source" src="../code_sandbox/snaps/event-listener-01-code.png" />

<img alt="event-listener example 1 result" src="../code_sandbox/snaps/event-listener-01-result.png" />

- [x] **Outcome:** Click runs `displayDate` and shows the date.

<a id="event-listener-example-02"></a>

### **Example 2: Syntax — event, function, useCapture**

- [x] `element.addEventListener(event, function, useCapture);`
- [x] 1) event type  2) callback  3) optional boolean — `true` = **capture**, default `false` = **bubble**.
- [x] Do not write the `on` prefix.

Sandbox: `code_sandbox/event-listener/syntax.html`

```javascript
element.addEventListener("click", function () { /* ... */ }, false);
```

<img alt="event-listener example 2 source" src="../code_sandbox/snaps/event-listener-02-code.png" />

<img alt="event-listener example 2 result" src="../code_sandbox/snaps/event-listener-02-result.png" />

- [x] **Outcome:** The sandbox attaches with the default bubble phase (`false`) and the click succeeds.

<a id="event-listener-example-03"></a>

### **Example 3: Anonymous function handler**

- [x] `element.addEventListener("click", function(){ … });`
- [x] Fine when you will **never remove** the listener.
- [x] Alerts are replaced with DOM text in this sandbox.

Sandbox: `code_sandbox/event-listener/anonymous.html`

```javascript
element.addEventListener("click", function(){ alert("Hello World!"); });
```

<img alt="event-listener example 3 source" src="../code_sandbox/snaps/event-listener-03-code.png" />

<img alt="event-listener example 3 result" src="../code_sandbox/snaps/event-listener-03-result.png" />

- [x] **Outcome:** Click prints **Hello World!** (alert stand-in).

<a id="event-listener-example-04"></a>

### **Example 4: Named function handler**

- [x] `addEventListener("click", myFunction);` then `function myFunction(){…}`.
- [x] Named functions are reusable and **removable**.
- [x] Pass the function **reference**, no `()`.

Sandbox: `code_sandbox/event-listener/named.html`

```javascript
element.addEventListener("click", myFunction);
function myFunction() { alert("Hello World!"); }
```

<img alt="event-listener example 4 source" src="../code_sandbox/snaps/event-listener-04-code.png" />

<img alt="event-listener example 4 result" src="../code_sandbox/snaps/event-listener-04-result.png" />

- [x] **Outcome:** The named function runs: **Hello World!**.

<a id="event-listener-example-05"></a>

### **Example 5: Many handlers of the same type**

- [x] Two `click` listeners on the **same** element both run — neither overwrites the other.
- [x] That is the big difference vs `onclick = …`.
- [x] Order is registration order (for the same phase).

Sandbox: `code_sandbox/event-listener/many-same-type.html`

```javascript
element.addEventListener("click", myFunction);
element.addEventListener("click", mySecondFunction);
```

<img alt="event-listener example 5 source" src="../code_sandbox/snaps/event-listener-05-code.png" />

<img alt="event-listener example 5 result" src="../code_sandbox/snaps/event-listener-05-result.png" />

- [x] **Outcome:** The log is **first second** — both click handlers ran.

<a id="event-listener-example-06"></a>

### **Example 6: Different event types on the same element**

- [x] You can mix `mouseover`, `click`, and `mouseout` on one node.
- [x] Each type has its own listener list.
- [x] The snapshot fires all three in order.

Sandbox: `code_sandbox/event-listener/many-types.html`

```javascript
element.addEventListener("mouseover", myFunction);
element.addEventListener("click", mySecondFunction);
element.addEventListener("mouseout", myThirdFunction);
```

<img alt="event-listener example 6 source" src="../code_sandbox/snaps/event-listener-06-code.png" />

<img alt="event-listener example 6 result" src="../code_sandbox/snaps/event-listener-06-result.png" />

- [x] **Outcome:** The log is **over click out**.

<a id="event-listener-example-07"></a>

### **Example 7: Listener on window — resize**

- [x] `addEventListener` works on **any** EventTarget: elements, `document`, `window`, XHR, …
- [x] W3Schools listens for `resize` and writes text into `#demo`.
- [x] The snapshot dispatches `resize` (real window chrome may not change in headless).

Sandbox: `code_sandbox/event-listener/window-resize.html`

```html
<p id="out"></p>
<script>
window.addEventListener("resize", function(){
  document.getElementById("out").innerHTML = "resized " + window.innerWidth;
});
</script>
```

<img alt="event-listener example 7 source" src="../code_sandbox/snaps/event-listener-07-code.png" />

<img alt="event-listener example 7 result" src="../code_sandbox/snaps/event-listener-07-result.png" />

- [x] **Outcome:** The resize handler runs and prints the inner width.

<a id="event-listener-example-08"></a>

### **Example 8: Passing parameters with an anonymous wrapper**

- [x] You cannot write `addEventListener("click", myFunction(p1, p2))` — that **calls** it now.
- [x] Wrap: `addEventListener("click", function(){ myFunction(p1, p2); });`.
- [x] The wrapper closes over `p1`/`p2`.

Sandbox: `code_sandbox/event-listener/parameters.html`

```javascript
element.addEventListener("click", function(){ myFunction(p1, p2); });
```

<img alt="event-listener example 8 source" src="../code_sandbox/snaps/event-listener-08-code.png" />

<img alt="event-listener example 8 result" src="../code_sandbox/snaps/event-listener-08-result.png" />

- [x] **Outcome:** Click calls `myFunction("A", "B")` and prints **A B**.

<a id="event-listener-example-09"></a>

### **Example 9: Event bubbling vs capturing**

- [x] **Bubbling** (default): inner handler first, then outer.
- [x] **Capturing**: outer first, then inner. Pass `true` as the third argument.
- [x] W3Schools attaches both `myP` and `myDiv` with `true` so they use capture.

Sandbox: `code_sandbox/event-listener/bubble-capture.html`

```html
<div id="myDiv"><p id="myP">click inner</p></div>
<script>
document.getElementById("myP").addEventListener("click", function () { log("P"); }, true);
document.getElementById("myDiv").addEventListener("click", function () { log("DIV"); }, true);
</script>
```

<img alt="event-listener example 9 source" src="../code_sandbox/snaps/event-listener-09-code.png" />

<img alt="event-listener example 9 result" src="../code_sandbox/snaps/event-listener-09-result.png" />

- [x] **Outcome:** With `useCapture true`, clicking P logs **DIV** then **P** (outer first).

<a id="event-listener-example-10"></a>

### **Example 10: Bubbling (useCapture false) for comparison**

- [x] The same markup with default bubbling logs **P then DIV** (inner first).
- [x] This extra example makes the capture vs bubble difference visible.
- [x] Most code uses bubbling.

Sandbox: `code_sandbox/event-listener/bubble-default.html`

```javascript
document.getElementById("myP").addEventListener("click", fn, false);
document.getElementById("myDiv").addEventListener("click", fn, false);
```

<img alt="event-listener example 10 source" src="../code_sandbox/snaps/event-listener-10-code.png" />

<img alt="event-listener example 10 result" src="../code_sandbox/snaps/event-listener-10-result.png" />

- [x] **Outcome:** Clicking P with bubble phase logs **P then DIV**.

<a id="event-listener-example-11"></a>

### **Example 11: removeEventListener**

- [x] `element.removeEventListener("mousemove", myFunction);`
- [x] Must match **type**, **function**, and **capture flag** from `addEventListener`.
- [x] After removal, mousemove no longer updates the text.

Sandbox: `code_sandbox/event-listener/remove.html`

```javascript
element.removeEventListener("mousemove", myFunction);
```

<img alt="event-listener example 11 source" src="../code_sandbox/snaps/event-listener-11-code.png" />

<img alt="event-listener example 11 result" src="../code_sandbox/snaps/event-listener-11-result.png" />

- [x] **Outcome:** A move after removal does **not** change the message **removed**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/event-listener/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Do you write `onclick` or `click` in addEventListener?

<details>
<summary>Answer</summary>

- [x] **`"click"`** — no `on` prefix.

</details>

### Question 2: What is the third argument?

<details>
<summary>Answer</summary>

- [x] **`useCapture`**: `true` capture, `false`/omit bubble.

</details>

### Question 3: Can two click listeners coexist?

<details>
<summary>Answer</summary>

- [x] Yes — `addEventListener` does **not** overwrite.

</details>

### Question 4: How do you pass extra parameters?

<details>
<summary>Answer</summary>

- [x] Wrap in an **anonymous function** that calls `myFunction(p1, p2)`.

</details>

### Question 5: Capture order for inner P inside DIV?

<details>
<summary>Answer</summary>

- [x] **DIV then P** (outer first).

</details>

### Question 6: Bubble order for the same click?

<details>
<summary>Answer</summary>

- [x] **P then DIV** (inner first).

</details>

### Question 7: What can you listen on besides elements?

<details>
<summary>Answer</summary>

- [x] **`window`**, **`document`**, and other EventTargets (for example XHR).

</details>

### Question 8: Why named functions for remove?

<details>
<summary>Answer</summary>

- [x] `removeEventListener` needs the **same function reference**.

</details>

### Question 9: What happens if the capture flag differs on remove?

<details>
<summary>Answer</summary>

- [x] The listener is **not** removed — type, fn, and capture must match.

</details>

### Question 10: Why not `addEventListener("click", myFunction())`?

<details>
<summary>Answer</summary>

- [x] The `()` **calls** it immediately and registers `undefined`.

</details>

### Question 11: Does addEventListener work if you do not control the HTML?

<details>
<summary>Answer</summary>

- [x] Yes — that is a listed advantage: JS stays **off** the markup.

</details>


</details>

## Summary

Use `addEventListener(type, fn, useCapture)` everywhere you can. Wrap parameterised calls, and remove with the same function and capture flag.

## References

- [Event Listener](https://www.w3schools.com/js/js_htmldom_eventlistener.asp)
- [MDN EventTarget.addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
