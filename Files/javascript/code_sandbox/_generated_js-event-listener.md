<details>
  <summary>JS Event Listener</summary>

## Introduction

The same counter, but buttons have ids and JavaScript uses addEventListener('click', handler) instead of onclick attributes. That separates HTML from JS, allows multiple handlers on one node, and scales better. The improved version moves code into counter.js, wraps it in DOMContentLoaded, caches element variables, and shows Saved! / Loaded! for three seconds.

This section has **8** examples:

- [x] **Example 1:** Same counter, wired with addEventListener [View](#js-event-listener-example-01)
- [x] **Example 2:** HTML without onclick — ids only [View](#js-event-listener-example-02)
- [x] **Example 3:** addEventListener('click', handler) on each button [View](#js-event-listener-example-03)
- [x] **Example 4:** Two click listeners on the same button (why addEventListener) [View](#js-event-listener-example-04)
- [x] **Example 5:** Improvements: Saved! / Loaded! via showMessage [View](#js-event-listener-example-05)
- [x] **Example 6:** JavaScript in counter.js + script at the bottom [View](#js-event-listener-example-06)
- [x] **Example 7:** DOMContentLoaded — run after HTML is ready [View](#js-event-listener-example-07)
- [x] **Example 8:** Cache getElementById in const variables [View](#js-event-listener-example-08)

## Detailed Explanation

- [x] **No onclick in HTML.** **`addEventListener("click", fn)`** per button.
- [x] First Tryit **auto-loads** and **blocks decrease below 0**. The improved file’s `decreaseCount` is **unbounded** again.
- [x] **DOMContentLoaded** (or a script at the **end of body**) so nodes exist.
- [x] **showMessage** writes then clears after **3000 ms**.

<a id="js-event-listener-example-01"></a>

### **Example 1: Same counter, wired with addEventListener**

- [x] HTML buttons have **ids**, **no `onclick` attributes**.
- [x] `addEventListener("click", increaseCount)` keeps **HTML and JS separate**.
- [x] This Tryit also **`loadCount()`** on open and **blocks decrease below 0**.

Sandbox: `code_sandbox/js-event-listener/full-tryit.html`

```html
<h2>Counter</h2>
<p id="count" style="font-size:40px;">0</p>
<button type="button" id="btnPlus">+</button>
<button type="button" id="btnMinus">-</button>
<button type="button" id="btnReset">Reset</button>
<button type="button" id="btnSave">Save</button>
<button type="button" id="btnLoad">Load</button>


document.getElementById("btnPlus").addEventListener("click", increaseCount);
document.getElementById("btnMinus").addEventListener("click", decreaseCount);
document.getElementById("btnReset").addEventListener("click", resetCount);
document.getElementById("btnSave").addEventListener("click", saveCount);
document.getElementById("btnLoad").addEventListener("click", loadCount);
let count = 0;
loadCount();
function updateCount() {
  document.getElementById("count").innerHTML = count;
}
function increaseCount() {
  count++;
  updateCount();
}
function decreaseCount() {
  if (count > 0) {
    count--;
    updateCount();
  }
}
function resetCount() {
  count = 0;
  updateCount();
}
function saveCount() {
  localStorage.setItem("count", count);
}
function loadCount() {
  let saved = localStorage.getItem("count");
  if (saved !== null) {
    count = Number(saved);
  }
  updateCount();
}
```

<img alt="js-event-listener example 1 source" src="./code_sandbox/snaps/js-event-listener-01-code.png" />

<img alt="js-event-listener example 1 result" src="./code_sandbox/snaps/js-event-listener-01-result.png" />

- [x] **Outcome:** Auto ++ ++ makes **2**. Minus to **1**. Listeners fired without `onclick=` in HTML.

<a id="js-event-listener-example-02"></a>

### **Example 2: HTML without onclick — ids only**

- [x] `id="btnPlus"` etc. JavaScript **finds** the nodes and attaches listeners.
- [x] Put the **`<script>` at the bottom** (or use **DOMContentLoaded**) so the elements exist.

Sandbox: `code_sandbox/js-event-listener/html-no-onclick.html`

```html
<button type="button" id="btnPlus">+</button>
```

<img alt="js-event-listener example 2 source" src="./code_sandbox/snaps/js-event-listener-02-code.png" />

<img alt="js-event-listener example 2 result" src="./code_sandbox/snaps/js-event-listener-02-result.png" />

- [x] **Outcome:** Five id’d buttons, no inline handlers. Clicks do nothing until listeners are added.

<a id="js-event-listener-example-03"></a>

### **Example 3: addEventListener('click', handler) on each button**

- [x] Easier to add **multiple** events to one element, and to keep markup clean.

Sandbox: `code_sandbox/js-event-listener/add-listeners.html`

```javascript
document.getElementById("btnPlus").addEventListener("click", increaseCount);
document.getElementById("btnMinus").addEventListener("click", decreaseCount);
```

<img alt="js-event-listener example 3 source" src="./code_sandbox/snaps/js-event-listener-03-code.png" />

<img alt="js-event-listener example 3 result" src="./code_sandbox/snaps/js-event-listener-03-result.png" />

- [x] **Outcome:** `getElementById("btnPlus")` is an element. After `addEventListener`, a click runs **increaseCount**.

<a id="js-event-listener-example-04"></a>

### **Example 4: Two click listeners on the same button (why addEventListener)**

- [x] `onclick = fn` **replaces**. **`addEventListener`** can stack **several** handlers.
- [x] This extra demo logs **A** then **B** on one click.

Sandbox: `code_sandbox/js-event-listener/two-listeners.html`

```javascript
btn.addEventListener("click", handlerA);
btn.addEventListener("click", handlerB);
```

<img alt="js-event-listener example 4 source" src="./code_sandbox/snaps/js-event-listener-04-code.png" />

<img alt="js-event-listener example 4 result" src="./code_sandbox/snaps/js-event-listener-04-result.png" />

- [x] **Outcome:** One auto-click runs **both** handlers: **A** and **B**.

<a id="js-event-listener-example-05"></a>

### **Example 5: Improvements: Saved! / Loaded! via showMessage**

- [x] Cache elements in **`const`**. **`showMessage(text)`** writes `#message` then clears after **3 seconds**.
- [x] Save shows **Saved!**. Load shows **Loaded!** only if a value existed.
- [x] The improved `decreaseCount` on this page is **unbounded** (`count--` with no `if`).

Sandbox: `code_sandbox/js-event-listener/improvements-messages.html`

```javascript
function showMessage(text) {
  msgEl.innerHTML = text;
  setTimeout(function () {
    msgEl.innerHTML = "";
  }, 3000);
}
```

<img alt="js-event-listener example 5 source" src="./code_sandbox/snaps/js-event-listener-05-code.png" />

<img alt="js-event-listener example 5 result" src="./code_sandbox/snaps/js-event-listener-05-result.png" />

- [x] **Outcome:** After Save, `#message` reads **Saved!**. After Load, **Loaded!**.

<a id="js-event-listener-example-06"></a>

### **Example 6: JavaScript in counter.js + script at the bottom**

- [x] External files are **more organized**, separated from HTML, and closer to real projects.
- [x] The page puts **`<script src="counter.js">` before `</body>`**.

Sandbox: `code_sandbox/js-event-listener/external-file.html`

```html
<script src="counter.js"></script>
```

<img alt="js-event-listener example 6 source" src="./code_sandbox/snaps/js-event-listener-06-code.png" />

<img alt="js-event-listener example 6 result" src="./code_sandbox/snaps/js-event-listener-06-result.png" />

- [x] **Outcome:** `counter.js` loaded. Buttons work (auto ++ shows **1**). Script tag has **no type**.

<a id="js-event-listener-example-07"></a>

### **Example 7: DOMContentLoaded — run after HTML is ready**

- [x] An external script in **`<head>`** can run **before** `#btnPlus` exists → **`getElementById` is null** → crash.
- [x] `document.addEventListener("DOMContentLoaded", function () { ... })` waits until the HTML is parsed.
- [x] A script **at the bottom of body** is often ready without it; the page still wraps **counter.js** in DOMContentLoaded.

Sandbox: `code_sandbox/js-event-listener/domcontentloaded.html`

```javascript
document.addEventListener("DOMContentLoaded", function() {
  // JavaScript code
});
```

<img alt="js-event-listener example 7 source" src="./code_sandbox/snaps/js-event-listener-07-code.png" />

<img alt="js-event-listener example 7 result" src="./code_sandbox/snaps/js-event-listener-07-result.png" />

- [x] **Outcome:** Inside DOMContentLoaded, `#btnPlus` is an element (not null). That is why the wrap exists.

<a id="js-event-listener-example-08"></a>

### **Example 8: Cache getElementById in const variables**

- [x] `const countEl = document.getElementById("count")` — look up **once**, reuse.
- [x] Matches the performance tip from JS Performance, and the improved counter.js.

Sandbox: `code_sandbox/js-event-listener/element-variables.html`

```javascript
const countEl = document.getElementById("count");
const btnPlus = document.getElementById("btnPlus");
```

<img alt="js-event-listener example 8 source" src="./code_sandbox/snaps/js-event-listener-08-code.png" />

<img alt="js-event-listener example 8 result" src="./code_sandbox/snaps/js-event-listener-08-result.png" />

- [x] **Outcome:** **countEl.id** is **count**. **btnPlus.id** is **btnPlus**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-event-listener/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Where are the click handlers in the event-listener HTML?

<details>
<summary>Answer</summary>

- [x] **Not in HTML.** They are **`addEventListener`** calls.

</details>

### Question 2: Can one button have two click listeners?

<details>
<summary>Answer</summary>

- [x] **Yes.** This page’s extra demo runs **A** then **B**.

</details>

### Question 3: What does the first Tryit do on open?

<details>
<summary>Answer</summary>

- [x] **`loadCount()`** — restore if storage has a value.

</details>

### Question 4: Improved decreaseCount vs first Tryit?

<details>
<summary>Answer</summary>

- [x] Improved **`count--`** with no floor. First Tryit uses **`if (count > 0)`**.

</details>

### Question 5: What does Save show?

<details>
<summary>Answer</summary>

- [x] **Saved!** in `#message` for **3 seconds**.

</details>

### Question 6: Why DOMContentLoaded?

<details>
<summary>Answer</summary>

- [x] So **`getElementById`** does not run against **missing** nodes.

</details>

### Question 7: Where should `<script src="counter.js">` go?

<details>
<summary>Answer</summary>

- [x] At the **bottom of `<body>`** (the page’s pattern), or in head **with** DOMContentLoaded.

</details>

### Question 8: Why cache `const btnPlus = getElementById(...)`?

<details>
<summary>Answer</summary>

- [x] Look up **once**. Cleaner, and fewer DOM searches.

</details>


</details>

## Summary

Prefer addEventListener and an external file. Wait for DOMContentLoaded (or place the script last). Optional Saved!/Loaded! feedback makes storage visible.

## References

- [JS Event Listener (W3Schools)](https://www.w3schools.com/js/js_project_eventlistener.asp)
- [MDN: EventTarget.addEventListener()](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
- [MDN: DOMContentLoaded](https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event)

</details>
