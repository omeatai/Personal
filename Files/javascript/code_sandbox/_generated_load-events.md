<details>
  <summary>Load Events</summary>

## Introduction

Load events tell you when HTML is ready (`DOMContentLoaded`) or when the whole page and its assets are ready (`load`). Images, scripts, and stylesheets fire `load` too.

This section has **6** examples:

- [x] **Example 1:** DOMContentLoaded [View](#load-events-example-01)
- [x] **Example 2:** window load [View](#load-events-example-02)
- [x] **Example 3:** Image load [View](#load-events-example-03)
- [x] **Example 4:** script load [View](#load-events-example-04)
- [x] **Example 5:** stylesheet link load [View](#load-events-example-05)
- [x] **Example 6:** media-specific loading events [View](#load-events-example-06)

## Detailed Explanation

- [x] DOMContentLoaded = DOM tree.
- [x] window load = everything.
- [x] img / script / link / media have their own load-related events.

<a id="load-events-example-01"></a>

### **Example 1: DOMContentLoaded**

- [x] Fires when HTML is parsed and the **DOM tree** is ready.
- [x] Images, stylesheets, and subframes may **still be loading**.
- [x] Best time to query elements, bind listeners, and build UI that only needs the DOM.
- [x] If the script runs after the event, `document.readyState` is already past `loading` — call the setup function directly.

Sandbox: `code_sandbox/load-events/domcontentloaded.html`

```html
<p id="out"></p>
<script>
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("out").innerHTML = "HTML is loaded!";
});
</script>
```

<img alt="load-events example 1 source" src="./code_sandbox/snaps/load-events-01-code.png" />

<img alt="load-events example 1 result" src="./code_sandbox/snaps/load-events-01-result.png" />

- [x] **Outcome:** The paragraph reads **HTML is loaded!** (handler ran on the event or immediately because the DOM is already ready).

<a id="load-events-example-02"></a>

### **Example 2: window load**

- [x] `window` `load` waits for the **whole page**: HTML, images, CSS, frames.
- [x] Use it for image dimensions, “fully loaded” banners, or anything that needs complete resources.
- [x] Slower than DOMContentLoaded — don’t put all UI setup here.

Sandbox: `code_sandbox/load-events/window-load.html`

```html
<p id="out"></p>
<script>
window.addEventListener("load", function () {
  document.getElementById("out").innerHTML = "Page is fully loaded!";
});
</script>
```

<img alt="load-events example 2 source" src="./code_sandbox/snaps/load-events-02-code.png" />

<img alt="load-events example 2 result" src="./code_sandbox/snaps/load-events-02-result.png" />

- [x] **Outcome:** When `readyState` is `complete` (or when `load` fires), the text is **Page is fully loaded!**.

<a id="load-events-example-03"></a>

### **Example 3: Image load**

- [x] `<img>` fires **`load`** when that image has finished downloading.
- [x] Also used on `<script>` (executed) and `<link rel=stylesheet>` (parsed).
- [x] Media elements have additional events (`canplay`, `loadeddata`, …).

Sandbox: `code_sandbox/load-events/img-load.html`

```html
<img id="myImg" alt="pic" width="32" height="32"
  src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32'%3E%3Crect width='32' height='32' fill='%2304AA6D'/%3E%3C/svg%3E">
<p id="out"></p>
<script>
const img = document.getElementById("myImg");
img.addEventListener("load", function () {
  document.getElementById("out").innerHTML = "Image loaded!";
});
</script>
```

<img alt="load-events example 3 source" src="./code_sandbox/snaps/load-events-03-code.png" />

<img alt="load-events example 3 result" src="./code_sandbox/snaps/load-events-03-result.png" />

- [x] **Outcome:** When the SVG data URL has loaded (or `complete` is already true), the text is **Image loaded!**.

<a id="load-events-example-04"></a>

### **Example 4: script load**

- [x] A `<script src>` fires `load` after the file is **fetched and executed**.
- [x] Inline scripts do not fetch, so this is about **external** files.
- [x] This sandbox appends a tiny extra file and waits for its `load`.

Sandbox: `code_sandbox/load-events/script-load.html`

```html
<script src="ping.js"></script>
```

<img alt="load-events example 4 source" src="./code_sandbox/snaps/load-events-04-code.png" />

<img alt="load-events example 4 result" src="./code_sandbox/snaps/load-events-04-result.png" />

- [x] **Outcome:** After `ping.js` loads, the log includes **script loaded**.

<a id="load-events-example-05"></a>

### **Example 5: stylesheet link load**

- [x] `<link rel="stylesheet">` fires `load` when the CSS is **loaded and parsed**.
- [x] Use it if you must measure layout that depends on those rules.
- [x] This sandbox injects a `<link>` to a local CSS file.

Sandbox: `code_sandbox/load-events/link-load.html`

```html
<link rel="stylesheet" href="extra.css">
```

<img alt="load-events example 5 source" src="./code_sandbox/snaps/load-events-05-code.png" />

<img alt="load-events example 5 result" src="./code_sandbox/snaps/load-events-05-result.png" />

- [x] **Outcome:** The stylesheet `load` handler prints **css loaded**.

<a id="load-events-example-06"></a>

### **Example 6: media-specific loading events**

- [x] `<audio>` / `<video>` fire `loadedmetadata`, `canplay`, `canplaythrough`, plus `error`.
- [x] Do not assume `load` is the only signal — media is streamed.
- [x] This example uses a tiny audio data URL and reports `readyState` after setting `src`.

Sandbox: `code_sandbox/load-events/media-load.html`

```html
<audio id="a"></audio>
```

<img alt="load-events example 6 source" src="./code_sandbox/snaps/load-events-06-code.png" />

<img alt="load-events example 6 result" src="./code_sandbox/snaps/load-events-06-result.png" />

- [x] **Outcome:** The audio element exists; `readyState` is logged (0 until data arrives).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/load-events/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: When is DOMContentLoaded the right event?

<details>
<summary>Answer</summary>

- [x] When you only need the **DOM** — bind listeners, fill text — not image sizes.

</details>

### Question 2: What does window `load` wait for?

<details>
<summary>Answer</summary>

- [x] HTML **plus** images, stylesheets, frames, and other resources.

</details>

### Question 3: What if your script is at the end of `<body>`?

<details>
<summary>Answer</summary>

- [x] The DOM is already there; you may not need DOMContentLoaded, but it is still safe if you check `readyState`.

</details>

### Question 4: Which element fires `load` when a picture finishes?

<details>
<summary>Answer</summary>

- [x] **`<img>`**.

</details>

### Question 5: When does an external `<script>` fire `load`?

<details>
<summary>Answer</summary>

- [x] After it is **downloaded and executed**.

</details>

### Question 6: Why extra media events besides `load`?

<details>
<summary>Answer</summary>

- [x] Audio/video are **streamed**; `canplay` / `loadeddata` describe buffer state.

</details>

### Question 7: What `readyState` means the document is fully loaded?

<details>
<summary>Answer</summary>

- [x] **`complete`**.

</details>

### Question 8: Should you put all setup in `window.load`?

<details>
<summary>Answer</summary>

- [x] No — it is **later**. Prefer DOMContentLoaded for UI wiring.

</details>

### Question 9: What if the image is already cached?

<details>
<summary>Answer</summary>

- [x] `img.complete` may already be true — call the handler **immediately** as well as on `load`.

</details>

### Question 10: Can `load` run on `<link rel=stylesheet>`?

<details>
<summary>Answer</summary>

- [x] Yes — when the stylesheet has been **loaded and parsed**.

</details>


</details>

## Summary

Wire UI on DOMContentLoaded. Wait for `window.load` or element `load` only when you need finished resources.

## References

- [Load Events](https://www.w3schools.com/js/js_events_load.asp)
- [MDN EventTarget.addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)

</details>
