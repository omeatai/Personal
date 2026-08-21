# HTML Web Workers

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

A **web worker** is an **external JavaScript file** that runs in the **background** so a heavy script does not freeze the page. This chapter builds `demo_workers.js` (a counter via **`postMessage`**), starts it with **`new Worker`**, listens with **`onmessage`**, and stops it with **`terminate()`**.

This section has **2** examples:

- [x] **Example 1:** `index.html` [View](#html-web-workers-example-01)
- [x] **Example 2:** `demo_workers.js` [View](#html-web-workers-example-02)

## Detailed Explanation

- [x] Scripts on the main page block UI until they finish. A worker runs **independently** — you can still click and select.
- [x] Use workers for **CPU-heavy** work, not for a simple counter (the demo is simplified).
- [x] **Detect:** `typeof(Worker) !== "undefined"`.
- [x] **Worker file** `demo_workers.js`:
  - Increment `i`, `postMessage(i)`, `setTimeout` every 500 ms.
  - The page shows `setTimeout("timedCount()",500)` (string). The sandbox uses `setTimeout(timedCount, 500)` — same timing, current JS style.
- [x] **Main page**
  - Create once: `if (typeof(w) == "undefined") { w = new Worker("demo_workers.js"); }`
  - Both sides talk with **`postMessage`** / **`onmessage`**. Data is `event.data`.
  - **Stop:** `w.terminate()`. **Reuse:** `w = undefined` then start again.
  - Sandbox: `code_sandbox/html-web-workers/index.html`.

<img alt="html-web-workers result" src="../code_sandbox/snaps/html-web-workers-result.png" />
- [x] **Workers cannot use** `window`, `document`, or `parent`.

<a id="html-web-workers-example-01"></a>

### **Example 1: `index.html`**

- [x] This example runs the tested markup.

```javascript
w = new Worker("demo_workers.js");
w.onmessage = function (event) {
  document.getElementById("result").innerHTML = event.data;
};
```

<img alt="html-web-workers source" src="../code_sandbox/snaps/html-web-workers-code.png" />

<img alt="html-web-workers result" src="../code_sandbox/snaps/html-web-workers-result.png" />

- [x] **Outcome:** the browser shows **w = new Worker("demo_workers.js"); w.onmessage = function(event) { document.getElementById("result").innerHTML = event.data; };**.

<a id="html-web-workers-example-02"></a>

### **Example 2: `demo_workers.js`**

- [x] This example runs the tested markup.

```javascript
var i = 0;
function timedCount() {
  i = i + 1;
  postMessage(i);
  setTimeout(timedCount, 500);
}
timedCount();
```

- [x] **Outcome:** the browser shows **var i = 0; function timedCount() { i = i + 1; postMessage(i); setTimeout(timedCount, 500); } timedCount();**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-web-workers/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What problem do web workers solve?

<details>
<summary>Answer</summary>

- [x] Long scripts on the main thread make the page **unresponsive**.
- [x] A worker runs in the **background**.

</details>

### Question 2: How does the worker send data to the page?

<details>
<summary>Answer</summary>

- [x] **`postMessage(value)`**.
- [x] The page reads **`event.data`** in **`onmessage`**.

</details>

### Question 3: How do you stop and reuse a worker?

<details>
<summary>Answer</summary>

- [x] `terminate()` stops it.
- [x] Set the variable to **`undefined`** to create it again.

</details>

### Question 4: Can a worker touch the DOM?

<details>
<summary>Answer</summary>

- [x] **No.** No `window`, `document`, or `parent`.

</details>

</details>

## Summary

Put heavy work in an external `.js` worker. `new Worker`, `postMessage`/`onmessage`, `terminate`. Workers have no DOM. The demo counter is for learning, not a typical worker job.

## References

- [HTML Web Workers API (W3Schools)](https://www.w3schools.com/html/html5_webworkers.asp)
- [MDN: Using Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
- [MDN: `Worker`](https://developer.mozilla.org/en-US/docs/Web/API/Worker)
