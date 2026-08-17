<details>
  <summary>HTML Geolocation</summary>

## Introduction

The **Geolocation API** reads the user’s **current location**. Because that is private, the browser **asks permission**. This chapter covers `navigator.geolocation`, **`getCurrentPosition()`**, **error codes**, returned **coords**, and **`watchPosition()` / `clearWatch()`**. It works on **secure contexts** (HTTPS or localhost).

## Detailed Explanation

- [x] **Privacy** — location is unavailable until the user **approves**.
- [x] **Secure context** — HTTPS (localhost/`127.0.0.1` also counts). Most accurate on **GPS** devices.
- [x] **`navigator.geolocation.getCurrentPosition(success, error)`**
  - If unsupported: “Geolocation is not supported by this browser.”
  - Success: **Latitude** and **Longitude** from `position.coords`.
  - Sandbox: `code_sandbox/html-geolocation/index.html` (button **Try It**). Headless snaps will not grant permission.

<img alt="html-geolocation result" src="./code_sandbox/snaps/html-geolocation-result.png" />

- [x] **Error `code`:** `PERMISSION_DENIED`, `POSITION_UNAVAILABLE`, `TIMEOUT`, `UNKNOWN_ERROR`.
- [x] **Uses:** local info, nearby points of interest, turn-by-turn GPS.
- [x] **Always returned:** `coords.latitude`, `coords.longitude`, `coords.accuracy`. Optional: altitude, altitudeAccuracy, heading, speed, timestamp.
- [x] **`watchPosition()`** — keeps updating as the user moves (needs a GPS device). **`clearWatch()`** stops it.

<details>
  <summary>Lab</summary>

## Lab

Open the Try It page on HTTPS or `127.0.0.1` and allow location.

### **Overview**

- [ ] Serve `code_sandbox` and open `html-geolocation/`.
- [ ] Click **Try It** and allow (or deny) location.
- [ ] Success: lat/long, or a clear error such as permission denied.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-geolocation/`

<img alt="html-geolocation result" src="./code_sandbox/snaps/html-geolocation-result.png" />

The geolocation UI matches the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-geolocation/`.

</details>

<details>
  <summary>Code</summary>

## Code

`index.html`:

<img alt="html-geolocation source" src="./code_sandbox/snaps/html-geolocation-code.png" />

```javascript
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(success, error);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
```

<img alt="html-geolocation result" src="./code_sandbox/snaps/html-geolocation-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Why does the browser ask before sharing location?

<details>
<summary>Answer</summary>

- [x] Location can **compromise privacy**.
- [x] Data is available only if the user **approves**.

</details>

### Question 2: Does Geolocation work on plain `http://` sites?

<details>
<summary>Answer</summary>

- [x] **No** on the public web — it needs a **secure context** (HTTPS).
- [x] **localhost** / `127.0.0.1` is treated as secure.

</details>

### Question 3: Which method returns the current position once?

<details>
<summary>Answer</summary>

- [x] **`getCurrentPosition(success, error)`**.

</details>

### Question 4: Which coords are always returned?

<details>
<summary>Answer</summary>

- [x] **latitude**, **longitude**, and **accuracy**.

</details>

### Question 5: `watchPosition` vs `getCurrentPosition`?

<details>
<summary>Answer</summary>

- [x] `watchPosition` **keeps updating** as the user moves.
- [x] Stop it with **`clearWatch()`**.

</details>

</details>

## Summary

Ask permission, then `getCurrentPosition` (or `watchPosition`) on a secure context. Always get lat/long/accuracy. Handle denied, unavailable, timeout, and unknown errors.

## References

- [HTML Geolocation API (W3Schools)](https://www.w3schools.com/html/html5_geolocation.asp)
- [MDN: Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)
- [MDN: `getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition)

</details>

<details>
  <summary>HTML Drag and Drop</summary>

## Introduction

The **HTML Drag and Drop API** lets you **grab** an element and drop it somewhere else. This chapter sets **`draggable="true"`**, sends an id with **`dataTransfer.setData`**, allows a drop with **`preventDefault` on dragover**, and **appends** the node on **drop**.

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

<img alt="html-drag-and-drop result" src="./code_sandbox/snaps/html-drag-and-drop-result.png" />

- [x] **More examples on the page:** drag an `<h1>`, drag an `<a>`, drag an image **back and forth** between two divs.

<details>
  <summary>Lab</summary>

## Lab

Drag the logo into the empty rectangle.

### **Overview**

- [ ] Serve `code_sandbox` and open `html-drag-and-drop/`.
- [ ] Success: the image sits **inside** the bordered box after drop.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-drag-and-drop/`

<img alt="html-drag-and-drop result" src="./code_sandbox/snaps/html-drag-and-drop-result.png" />

The drag-and-drop example matches the chapter.

</details>

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
  <summary>Code</summary>

## Code

`index.html`:

<img alt="html-drag-and-drop source" src="./code_sandbox/snaps/html-drag-and-drop-code.png" />

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

<img alt="html-drag-and-drop result" src="./code_sandbox/snaps/html-drag-and-drop-result.png" />

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

</details>
