<details>
  <summary>JS Modal Popup</summary>

## Introduction

A modal is a popup on top of the page: a full-screen overlay plus a box. Hidden with display:none; shown by adding class show. Close three ways: ×, click the overlay (event.target === modal), or Escape. Use openBtn (the prose typo openBth is wrong). Do not close when the click is inside the box.

This section has **8** examples:

- [x] **Example 1:** HTML: Open button, overlay, box, close × [View](#js-modal-popup-example-01)
- [x] **Example 2:** CSS: overlay display none by default [View](#js-modal-popup-example-02)
- [x] **Example 3:** CSS: .modal-overlay.show { display: block } [View](#js-modal-popup-example-03)
- [x] **Example 4:** openModal / closeModal — classList add/remove show [View](#js-modal-popup-example-04)
- [x] **Example 5:** Full Tryit: three ways to close [View](#js-modal-popup-example-05)
- [x] **Example 6:** Click overlay (event.target === modal) closes [View](#js-modal-popup-example-06)
- [x] **Example 7:** Escape key closes the modal [View](#js-modal-popup-example-07)
- [x] **Example 8:** Close button (×) calls closeModal [View](#js-modal-popup-example-08)

## Detailed Explanation

- [x] **Overlay** + **box**. Default **display: none**. **`.show` → display: block**.
- [x] **classList.add/remove("show")** — not inline style.
- [x] Overlay click: **`event.target === modal`**. **Escape** on document **keydown**.

<a id="js-modal-popup-example-01"></a>

### **Example 1: HTML: Open button, overlay, box, close ×**

- [x] Two layers: **`.modal-overlay`** (dim background) and **`.modal-box`** (the card).
- [x] The page’s id typo **`openBth`** in the prose is **`openBtn`** in the working code — use **`openBtn`**.

Sandbox: `code_sandbox/js-modal-popup/html-structure.html`

```html
<h2>Modal Popup</h2>
<button type="button" id="openBtn">Open Modal</button>
<div id="modal" class="modal-overlay">
  <div class="modal-box">
    <button type="button" id="closeBtn" class="modal-close">&times;</button>
    <h3>Hello!</h3>
    <p>This is a modal popup.</p>
  </div>
</div>
```

<img alt="js-modal-popup example 1 source" src="./code_sandbox/snaps/js-modal-popup-01-code.png" />

<img alt="js-modal-popup example 1 result" src="./code_sandbox/snaps/js-modal-popup-01-result.png" />

- [x] **Outcome:** Open button is visible. Overlay exists in the DOM but is **hidden** (`display: none`) until `.show`.

<a id="js-modal-popup-example-02"></a>

### **Example 2: CSS: overlay display none by default**

- [x] `.modal-overlay { display: none; }` **hides** the modal until JS adds **`.show`**.

Sandbox: `code_sandbox/js-modal-popup/css-hidden.html`

```css
.modal-overlay {
  display: none;
}
```

<img alt="js-modal-popup example 2 source" src="./code_sandbox/snaps/js-modal-popup-02-code.png" />

<img alt="js-modal-popup example 2 result" src="./code_sandbox/snaps/js-modal-popup-02-result.png" />

- [x] **Outcome:** Computed **display** is **none**. The Hello box is not shown.

<a id="js-modal-popup-example-03"></a>

### **Example 3: CSS: .modal-overlay.show { display: block }**

- [x] JavaScript **adds/removes** the **`show`** class. No `style.display` juggling required.

Sandbox: `code_sandbox/js-modal-popup/css-show.html`

```css
.modal-overlay.show {
  display: block;
}
```

<img alt="js-modal-popup example 3 source" src="./code_sandbox/snaps/js-modal-popup-03-code.png" />

<img alt="js-modal-popup example 3 result" src="./code_sandbox/snaps/js-modal-popup-03-result.png" />

- [x] **Outcome:** After `classList.add("show")`, display is **block** (modal visible).

<a id="js-modal-popup-example-04"></a>

### **Example 4: openModal / closeModal — classList add/remove show**

- [x] `openModal()` → **`classList.add("show")`**. `closeModal()` → **`remove("show")`**.

Sandbox: `code_sandbox/js-modal-popup/open-close.html`

```javascript
function openModal() {
  modal.classList.add("show");
}
function closeModal() {
  modal.classList.remove("show");
}
```

<img alt="js-modal-popup example 4 source" src="./code_sandbox/snaps/js-modal-popup-04-code.png" />

<img alt="js-modal-popup example 4 result" src="./code_sandbox/snaps/js-modal-popup-04-result.png" />

- [x] **Outcome:** Open → has **show**. Close → does **not**.

<a id="js-modal-popup-example-05"></a>

### **Example 5: Full Tryit: three ways to close**

- [x] Close with **×**, **click overlay**, or **Escape**.
- [x] This snap **opens** the modal so the screenshot shows the popup on top of the page.

Sandbox: `code_sandbox/js-modal-popup/full-js.html`

```javascript
const modal = document.getElementById("modal");
const openBtn = document.getElementById("openBtn");
const closeBtn = document.getElementById("closeBtn");
function openModal() {
  modal.classList.add("show");
}
function closeModal() {
  modal.classList.remove("show");
}
openBtn.addEventListener("click", openModal);
closeBtn.addEventListener("click", closeModal);
modal.addEventListener("click", function (event) {
  if (event.target === modal) {
    closeModal();
  }
});
document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    closeModal();
  }
});
```

<img alt="js-modal-popup example 5 source" src="./code_sandbox/snaps/js-modal-popup-05-code.png" />

<img alt="js-modal-popup example 5 result" src="./code_sandbox/snaps/js-modal-popup-05-result.png" />

- [x] **Outcome:** After `openModal()`, overlay has **show** and the **Hello!** box is visible in the snap.

<a id="js-modal-popup-example-06"></a>

### **Example 6: Click overlay (event.target === modal) closes**

- [x] `event.target === modal` means the click hit the **overlay**, not the inner box.
- [x] Clicks **inside `.modal-box`** do **not** close.

Sandbox: `code_sandbox/js-modal-popup/click-overlay.html`

```javascript
modal.addEventListener("click", function (event) {
  if (event.target === modal) {
    closeModal();
  }
});
```

<img alt="js-modal-popup example 6 source" src="./code_sandbox/snaps/js-modal-popup-06-code.png" />

<img alt="js-modal-popup example 6 result" src="./code_sandbox/snaps/js-modal-popup-06-result.png" />

- [x] **Outcome:** Click on overlay → closed. Click on the box → still open.

<a id="js-modal-popup-example-07"></a>

### **Example 7: Escape key closes the modal**

- [x] `keydown` on **document**. If **`event.key === "Escape"`**, call **`closeModal()`**.
- [x] The page notes Escape may fire even when hidden — optional extra check: only close if open.

Sandbox: `code_sandbox/js-modal-popup/escape-key.html`

```javascript
document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    closeModal();
  }
});
```

<img alt="js-modal-popup example 7 source" src="./code_sandbox/snaps/js-modal-popup-07-code.png" />

<img alt="js-modal-popup example 7 result" src="./code_sandbox/snaps/js-modal-popup-07-result.png" />

- [x] **Outcome:** Open, then dispatch **Escape** → **show** is **false**.

<a id="js-modal-popup-example-08"></a>

### **Example 8: Close button (×) calls closeModal**

- [x] `closeBtn.addEventListener("click", closeModal)` — the **×** in the corner.

Sandbox: `code_sandbox/js-modal-popup/close-button.html`

```javascript
openBtn.addEventListener("click", openModal);
closeBtn.addEventListener("click", closeModal);
```

<img alt="js-modal-popup example 8 source" src="./code_sandbox/snaps/js-modal-popup-08-code.png" />

<img alt="js-modal-popup example 8 result" src="./code_sandbox/snaps/js-modal-popup-08-result.png" />

- [x] **Outcome:** Open, click × → overlay no longer has **show**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-modal-popup/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How is the modal hidden at first?

<details>
<summary>Answer</summary>

- [x] **.modal-overlay { display: none; }**.

</details>

### Question 2: How does JS show it?

<details>
<summary>Answer</summary>

- [x] **`modal.classList.add("show")`**.

</details>

### Question 3: Three close methods?

<details>
<summary>Answer</summary>

- [x] **× button**, **click overlay**, **Escape**.

</details>

### Question 4: Why `event.target === modal`?

<details>
<summary>Answer</summary>

- [x] The click hit the **overlay**, not the inner box.

</details>

### Question 5: Does a click inside the box close it?

<details>
<summary>Answer</summary>

- [x] **No** — target is the box (or a child), not the overlay.

</details>

### Question 6: What key closes it?

<details>
<summary>Answer</summary>

- [x] **Escape** (`event.key === "Escape"`).

</details>

### Question 7: Prose id `openBth`?

<details>
<summary>Answer</summary>

- [x] Typo. Working code uses **`openBtn`**.

</details>

### Question 8: open then close classList?

<details>
<summary>Answer</summary>

- [x] **show** present, then **removed**.

</details>


</details>

## Summary

Toggle a show class on the overlay. Close from the ×, overlay clicks (target === overlay), and Escape. Keep the box clicks from bubbling into a close.

## References

- [JS Modal Popup (W3Schools)](https://www.w3schools.com/js/js_project_modal_popup.asp)
- [MDN: Element.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList)
- [MDN: KeyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)

</details>
