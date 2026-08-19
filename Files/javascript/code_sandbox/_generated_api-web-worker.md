<details>
  <summary>API Web Worker</summary>

## Introduction

A Web Worker runs a script on another thread and talks to the page with `postMessage` / `onmessage`. It cannot use the DOM. terminate() stops it; set the variable to undefined before creating another. The sandbox worker uses `setTimeout(timedCount, 500)` instead of the page’s string timer.

This section has **8** examples:

- [x] **Example 1:** Check Web Worker support [View](#api-web-worker-example-01)
- [x] **Example 2:** Create a Web Worker file — postMessage a counter [View](#api-web-worker-example-02)
- [x] **Example 3:** new Worker("demo_workers.js") [View](#api-web-worker-example-03)
- [x] **Example 4:** w.onmessage — receive event.data [View](#api-web-worker-example-04)
- [x] **Example 5:** w.terminate() — stop the worker [View](#api-web-worker-example-05)
- [x] **Example 6:** Set w = undefined to reuse [View](#api-web-worker-example-06)
- [x] **Example 7:** Full example — Start / Stop buttons [View](#api-web-worker-example-07)
- [x] **Example 8:** Web Workers cannot touch the DOM [View](#api-web-worker-example-08)

## Detailed Explanation

- [x] typeof Worker for support.
- [x] postMessage / onmessage.
- [x] terminate + undefined to restart.
- [x] No DOM in the worker.

<a id="api-web-worker-example-01"></a>

### **Example 1: Check Web Worker support**

- [x] `typeof Worker !== "undefined"` means the constructor exists.
- [x] Workers need **http(s)** modules/scripts (not typically `file://`).

Sandbox: `code_sandbox/api-web-worker/support.html`

```html
if (typeof(Worker) !== "undefined") {
  // Yes! Web worker support!
} else {
  // Sorry! No Web Worker support..
}
```

<img alt="api-web-worker example 1 source" src="./code_sandbox/snaps/api-web-worker-01-code.png" />

<img alt="api-web-worker example 1 result" src="./code_sandbox/snaps/api-web-worker-01-result.png" />

- [x] **Outcome:** `typeof Worker` is **function** in this browser.

<a id="api-web-worker-example-02"></a>

### **Example 2: Create a Web Worker file — postMessage a counter**

- [x] A worker file runs in another thread. It cannot touch the DOM.
- [x] W3Schools `timedCount` increments `i` and **`postMessage(i)`** every 500ms.
- [x] They used `setTimeout("timedCount()",500)` (string). Current form: **`setTimeout(timedCount, 500)`** — same timing, no implied eval.

Sandbox: `code_sandbox/api-web-worker/worker-file.html`

```html
let i = 0;
function timedCount() {
  i++;
  postMessage(i);
  setTimeout("timedCount()",500);
}
timedCount();
```

<img alt="api-web-worker example 2 source" src="./code_sandbox/snaps/api-web-worker-02-code.png" />

<img alt="api-web-worker example 2 result" src="./code_sandbox/snaps/api-web-worker-02-result.png" />

- [x] **Outcome:** The worker script is saved as **demo_workers.js** and starts counting when constructed (next examples).

<a id="api-web-worker-example-03"></a>

### **Example 3: new Worker("demo_workers.js")**

- [x] Create the worker from the **page** script.
- [x] Guard with `if (typeof w == "undefined")` so you do not spawn two.
- [x] The snapshot starts one worker.

Sandbox: `code_sandbox/api-web-worker/create.html`

```html
if (typeof(w) == "undefined") {
  w = new Worker("demo_workers.js");
}
```

<img alt="api-web-worker example 3 source" src="./code_sandbox/snaps/api-web-worker-03-code.png" />

<img alt="api-web-worker example 3 result" src="./code_sandbox/snaps/api-web-worker-03-result.png" />

- [x] **Outcome:** `w` is a **Worker**. First messages are numbers **1, 2, …**

<a id="api-web-worker-example-04"></a>

### **Example 4: w.onmessage — receive event.data**

- [x] The page listens: `w.onmessage = function(event) { … event.data }`.
- [x] `data` is whatever the worker `postMessage`d (here, a number).
- [x] You can also `w.addEventListener("message", …)`.

Sandbox: `code_sandbox/api-web-worker/onmessage.html`

```html
w.onmessage = function(event){
  document.getElementById("result").innerHTML = event.data;
};
```

<img alt="api-web-worker example 4 source" src="./code_sandbox/snaps/api-web-worker-04-code.png" />

<img alt="api-web-worker example 4 result" src="./code_sandbox/snaps/api-web-worker-04-result.png" />

- [x] **Outcome:** `event.data` is a **number** (the counter).

<a id="api-web-worker-example-05"></a>

### **Example 5: w.terminate() — stop the worker**

- [x] `terminate()` kills the worker immediately from the page.
- [x] No more messages after that.

Sandbox: `code_sandbox/api-web-worker/terminate.html`

```html
w.terminate();
```

<img alt="api-web-worker example 5 source" src="./code_sandbox/snaps/api-web-worker-05-code.png" />

<img alt="api-web-worker example 5 result" src="./code_sandbox/snaps/api-web-worker-05-result.png" />

- [x] **Outcome:** After terminate, a flag shows the worker was **stopped** (no further increments applied).

<a id="api-web-worker-example-06"></a>

### **Example 6: Set w = undefined to reuse**

- [x] After terminate, the variable still points at a **dead** Worker.
- [x] `w = undefined` lets the `typeof w == "undefined"` guard create a **new** one.
- [x] That is “Reuse the Web Worker” on the page.

Sandbox: `code_sandbox/api-web-worker/reuse.html`

```html
w = undefined;
```

<img alt="api-web-worker example 6 source" src="./code_sandbox/snaps/api-web-worker-06-code.png" />

<img alt="api-web-worker example 6 result" src="./code_sandbox/snaps/api-web-worker-06-result.png" />

- [x] **Outcome:** `typeof w` after terminate+undefined is **undefined**, so the next start can `new Worker` again.

<a id="api-web-worker-example-07"></a>

### **Example 7: Full example — Start / Stop buttons**

- [x] Start: create worker if needed, set `onmessage` to write `#result`.
- [x] Stop: `terminate()` and `w = undefined`.
- [x] The snapshot starts, waits for a count, then stops — same functions as the page.

Sandbox: `code_sandbox/api-web-worker/full.html`

```html
<p>Count numbers: <output id="result"></output></p>
<button onclick="startWorker()">Start Worker</button>
<button onclick="stopWorker()">Stop Worker</button>
<script>
let w;
function startWorker() {
  if (typeof(w) == "undefined") {
    w = new Worker("demo_workers.js");
  }
  w.onmessage = function(event) {
    document.getElementById("result").innerHTML = event.data;
  };
}
function stopWorker() {
  w.terminate();
  w = undefined;
}
</script>
```

<img alt="api-web-worker example 7 source" src="./code_sandbox/snaps/api-web-worker-07-code.png" />

<img alt="api-web-worker example 7 result" src="./code_sandbox/snaps/api-web-worker-07-result.png" />

- [x] **Outcome:** After start, `#result` shows a **positive integer**. After stop, `w` is **undefined**.

<a id="api-web-worker-example-08"></a>

### **Example 8: Web Workers cannot touch the DOM**

- [x] Workers have **no `document`**. UI updates happen on the page when a **message** arrives.
- [x] That is the point: heavy work off the main thread, results posted back.
- [x] Trying `document.getElementById` inside the worker would throw.

Sandbox: `code_sandbox/api-web-worker/no-dom.html`

```html
// inside worker: no document / no DOM
```

<img alt="api-web-worker example 8 source" src="./code_sandbox/snaps/api-web-worker-08-code.png" />

<img alt="api-web-worker example 8 result" src="./code_sandbox/snaps/api-web-worker-08-result.png" />

- [x] **Outcome:** `document` in the **page** exists; the worker file never references it — it only `postMessage`s numbers.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/api-web-worker/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you detect workers?

<details>
<summary>Answer</summary>

- [x] **`typeof Worker !== "undefined"`**.

</details>

### Question 2: How does a worker send data to the page?

<details>
<summary>Answer</summary>

- [x] **`postMessage(value)`**.

</details>

### Question 3: How does the page read it?

<details>
<summary>Answer</summary>

- [x] **`w.onmessage`** and **`event.data`**.

</details>

### Question 4: How do you stop a worker?

<details>
<summary>Answer</summary>

- [x] **`w.terminate()`**.

</details>

### Question 5: Why set `w = undefined` after stop?

<details>
<summary>Answer</summary>

- [x] So the next Start can **`new Worker`** again.

</details>

### Question 6: Can a worker use `document.getElementById`?

<details>
<summary>Answer</summary>

- [x] **No** — workers have **no DOM**.

</details>

### Question 7: What did W3Schools use for the delay?

<details>
<summary>Answer</summary>

- [x] **`setTimeout("timedCount()",500)`** — a string. Prefer **`setTimeout(timedCount, 500)`**.

</details>

### Question 8: Why run this over http?

<details>
<summary>Answer</summary>

- [x] Worker scripts are subject to **origin** rules; `file://` often fails.

</details>

### Question 9: Are workers for tiny counters?

<details>
<summary>Answer</summary>

- [x] The page says **no** — they are for **CPU-heavy** work; the counter is a demo.

</details>

### Question 10: What type is `event.data` in the demo?

<details>
<summary>Answer</summary>

- [x] A **number** (the incrementing `i`).

</details>


</details>

## Summary

Start a Worker from an http page, handle onmessage, and terminate when done. Keep DOM updates on the main thread. Workers are for heavy work; the counter is only a demo.

## References

- [API Web Worker](https://www.w3schools.com/js/js_api_web_workers.asp)
- [MDN Worker](https://developer.mozilla.org/en-US/docs/Web/API/Worker)

</details>
