# HTML Drag and Drop

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

The **HTML Drag and Drop API** lets you **grab** an element and drop it somewhere else. This chapter sets **`draggable="true"`**, sends an id with **`dataTransfer.setData`**, allows a drop with **`preventDefault` on dragover**, and **appends** the node on **drop**.

This section has **1** example:

- [x] **Example 1:** `index.html` [View](#html-drag-and-drop-example-01)

## Detailed Explanation

- [x] **Make it draggable:** `draggable="true"` on an image, paragraph, heading, or link.
- [x] **`ondragstart` / `setData`**
  - `ev.dataTransfer.setData("text", ev.target.id)` — type `"text"`, value the element **id** (`img1`).
- [x] **`ondragover`**
  - Drops are **blocked by default**. Call **`preventDefault()`** so the target can accept the drop.
- [x] **`ondrop`**
  - `preventDefault()` so the browser does not treat the drop as opening a link.
  - `getData("text")` returns the id; **`appendChild`** moves that element into the drop target.
  - Sandbox: `code_sandbox/html-drag-and-drop/index.html`.

<img alt="html-drag-and-drop result" src="../code_sandbox/snaps/html-drag-and-drop-result.png" />
- [x] **More examples on the page:** drag an `<h1>`, drag an `<a>`, drag an image **back and forth** between two divs.

<a id="html-drag-and-drop-example-01"></a>

### **Example 1: `index.html`**

- [x] This example runs the tested markup.

```javascript
function dragstartHandler(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}
function dragoverHandler(ev) {
  ev.preventDefault();
}
function dropHandler(ev) {
  ev.preventDefault();
  const data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}
```

<img alt="html-drag-and-drop source" src="../code_sandbox/snaps/html-drag-and-drop-code.png" />

<img alt="html-drag-and-drop result" src="../code_sandbox/snaps/html-drag-and-drop-result.png" />

- [x] **Outcome:** the browser shows **function dragstartHandler(ev) { ev.dataTransfer.setData("text", ev.target.id); } function dragoverHandler(ev) { ev.preventDefault(); } function dropHandler(ev) { ev.preventDefault(); const data = ev.dataTransfer.getData("text"); ev.target.appendChild(document.getElementById(data)); }**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-drag-and-drop/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you make an element draggable?

<details>
<summary>Answer</summary>

- [x] Set **`draggable="true"`**.

</details>

### Question 2: What does `setData` store in the example?

<details>
<summary>Answer</summary>

- [x] Type **`"text"`**.
- [x] Value = the dragged element’s **`id`**.

</details>

### Question 3: Why call `preventDefault` on dragover?

<details>
<summary>Answer</summary>

- [x] Browsers **forbid drops** by default.
- [x] `preventDefault` **allows** the drop.

</details>

### Question 4: What happens in `dropHandler`?

<details>
<summary>Answer</summary>

- [x] Prevent default (don’t open as a link).
- [x] `getData("text")` then **`appendChild`** into the target.

</details>

</details>

## Summary

Mark the source `draggable`, put its id in `dataTransfer` on dragstart, `preventDefault` on dragover, and append the node on drop.

## References

- [HTML Drag and Drop API (W3Schools)](https://www.w3schools.com/html/html5_draganddrop.asp)
- [MDN: HTML Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
