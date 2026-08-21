# Debug Async

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Async code runs later, so bugs feel invisible. fetch does not return JSON immediately — chain .then or await. Log the Response before .json(). Use the Network tab for status and path. Handle errors with try/catch on async functions. A missing return drops the promise so callers see undefined. Debugging async is a checklist: console, Network, log responses, try/catch, breakpoints on await.

This section has **7** examples:

- [x] **Example 1:** fetch("data.json").then(...).then(data => console.log(data)) [View](#js-debugging-async-example-01)
- [x] **Example 2:** Log the Response before calling .json() [View](#js-debugging-async-example-02)
- [x] **Example 3:** Network tab: failed request / wrong path [View](#js-debugging-async-example-03)
- [x] **Example 4:** async function loadData() { await fetch(...) } [View](#js-debugging-async-example-04)
- [x] **Example 5:** try/catch around await — errors must be handled [View](#js-debugging-async-example-05)
- [x] **Example 6:** Forgotten return — the promise result is dropped [View](#js-debugging-async-example-06)
- [x] **Example 7:** Async debugging checklist [View](#js-debugging-async-example-07)

## Detailed Explanation

- [x] `fetch` / `await` run **when the work finishes**, not on the next source line.
- [x] Log **`response`** (`ok`, `status`) before **`.json()`**.
- [x] Failed paths (`wrong.json`) need **`.catch`** or **`try/catch`**.
- [x] **Return** the promise if the caller needs the data.

<a id="js-debugging-async-example-01"></a>

### **Example 1: fetch("data.json").then(...).then(data => console.log(data))**

- [x] **`fetch()` is asynchronous.** It does **not** return the JSON immediately.
- [x] The page writes `fetch("data.json")`. This sandbox uses a **Blob URL** so `fetch` works from `file://` (same `.then` shape).
- [x] If **nothing appears**, check the console first.

Sandbox: `code_sandbox/js-debugging-async/fetch-then.html`

```javascript
fetch("data.json")
  .then(response => response.json())
  .then(data => console.log(data));
```

<img alt="js-debugging-async example 1 source" src="../code_sandbox/snaps/js-debugging-async-01-code.png" />

<img alt="js-debugging-async example 1 result" src="../code_sandbox/snaps/js-debugging-async-01-result.png" />

- [x] **Outcome:** After the promise resolves: **log: {"name":"Ada","ok":true}**. The `fetch("data.json")` form is what the page shows; the snap uses a Blob URL with the same chain.

<a id="js-debugging-async-example-02"></a>

### **Example 2: Log the Response before calling .json()**

- [x] Always **log the response** before using the data.
- [x] `response.ok` / `response.status` tell you if the HTTP call **worked**.

Sandbox: `code_sandbox/js-debugging-async/fetch-log-response.html`

```javascript
fetch("data.json")
  .then(response => {
    console.log(response);
    return response.json();
  })
  .then(data => console.log(data));
```

<img alt="js-debugging-async example 2 source" src="../code_sandbox/snaps/js-debugging-async-02-code.png" />

<img alt="js-debugging-async example 2 result" src="../code_sandbox/snaps/js-debugging-async-02-result.png" />

- [x] **Outcome:** First a **Response** snapshot (`ok`, `status` **200**), then the JSON **Ada** object.

<a id="js-debugging-async-example-03"></a>

### **Example 3: Network tab: failed request / wrong path**

- [x] Async bugs are often **network** problems. The **Network** tab shows status and path.
- [x] Check **status**, **file path**, and whether the server returned an **error**.
- [x] `fetch("wrong.json")` fails here (no such file) — **TypeError: Failed to fetch** or a 404 depending on how the page is served.

Sandbox: `code_sandbox/js-debugging-async/network-tab-404.html`

```javascript
fetch("wrong.json")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

<img alt="js-debugging-async example 3 source" src="../code_sandbox/snaps/js-debugging-async-03-code.png" />

<img alt="js-debugging-async example 3 result" src="../code_sandbox/snaps/js-debugging-async-03-result.png" />

- [x] **Outcome:** **error:** a failed fetch (TypeError **Failed to fetch**, or HTTP **404** when served over http). The catch ran; no JSON was logged.

<a id="js-debugging-async-example-04"></a>

### **Example 4: async function loadData() { await fetch(...) }**

- [x] **`async` / `await`** still run **later**. They only **look** synchronous.
- [x] You can set breakpoints on **`await`** lines and step the same way as normal code.

Sandbox: `code_sandbox/js-debugging-async/async-await.html`

```javascript
async function loadData() {
  let response = await fetch("data.json");
  let data = await response.json();
  console.log(data);
}
loadData();
```

<img alt="js-debugging-async example 4 source" src="../code_sandbox/snaps/js-debugging-async-04-code.png" />

<img alt="js-debugging-async example 4 result" src="../code_sandbox/snaps/js-debugging-async-04-result.png" />

- [x] **Outcome:** **log: {"name":"Ada","ok":true}** after both awaits finish.

<a id="js-debugging-async-example-05"></a>

### **Example 5: try/catch around await — errors must be handled**

- [x] Async errors **fail silently** unless you handle them.
- [x] Wrap `await` in **`try...catch`** (or `.catch` on the promise).
- [x] The page fetches **`wrong.json`** on purpose.

Sandbox: `code_sandbox/js-debugging-async/async-try-catch.html`

```javascript
async function loadData() {
  try {
    let response = await fetch("wrong.json");
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
```

<img alt="js-debugging-async example 5 source" src="../code_sandbox/snaps/js-debugging-async-05-code.png" />

<img alt="js-debugging-async example 5 result" src="../code_sandbox/snaps/js-debugging-async-05-result.png" />

- [x] **Outcome:** **error:** fetch failed (or JSON parse on a 404 HTML page). **catch** ran; `console.log(data)` did not.

<a id="js-debugging-async-example-06"></a>

### **Example 6: Forgotten return — the promise result is dropped**

- [x] A promise that **never seems to finish** is often a **missing `return`**.
- [x] `getData()` calls `fetch` but **does not return** the chain. The caller gets **`undefined`**, not JSON.
- [x] **Always return** promises when chaining.

Sandbox: `code_sandbox/js-debugging-async/missing-return.html`

```javascript
function getData() {
  fetch("data.json")
    .then(response => response.json());
}
```

<img alt="js-debugging-async example 6 source" src="../code_sandbox/snaps/js-debugging-async-06-code.png" />

<img alt="js-debugging-async example 6 result" src="../code_sandbox/snaps/js-debugging-async-06-result.png" />

- [x] **Outcome:** `getData()` returns **undefined**. The inner fetch still logs the JSON if you add a log inside, but **callers cannot `await` the data**.

<a id="js-debugging-async-example-07"></a>

### **Example 7: Async debugging checklist**

- [x] Check the **console** for errors.
- [x] Check the **Network** tab.
- [x] **Log responses** before using them.
- [x] Use **`try...catch`** with async functions.
- [x] Set breakpoints on **`await`** lines.

Sandbox: `code_sandbox/js-debugging-async/async-checklist.html`

```javascript
console.log("checklist: console, Network, log response, try/catch, await breakpoints");
```

<img alt="js-debugging-async example 7 source" src="../code_sandbox/snaps/js-debugging-async-07-code.png" />

<img alt="js-debugging-async example 7 result" src="../code_sandbox/snaps/js-debugging-async-07-result.png" />

- [x] **Outcome:** Five checks. Debugging is a **habit**, not a talent — the page’s closing line.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-debugging-async/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does `fetch` return the JSON immediately?

<details>
<summary>Answer</summary>

- [x] **No.** You **`then`** or **`await`** the body.

</details>

### Question 2: What JSON does the sandbox Blob fetch resolve to?

<details>
<summary>Answer</summary>

- [x] **{"name":"Ada","ok":true}** (stand-in for the page’s `data.json`).

</details>

### Question 3: Why log `response` before `.json()`?

<details>
<summary>Answer</summary>

- [x] To see **ok** / **status** if the HTTP call failed.

</details>

### Question 4: What happens on `fetch("wrong.json")`?

<details>
<summary>Answer</summary>

- [x] **catch** / **console.error** — failed fetch or 404. No data log.

</details>

### Question 5: Is `async/await` synchronous?

<details>
<summary>Answer</summary>

- [x] **No.** It still waits. It only **reads** top-to-bottom.

</details>

### Question 6: What if you omit `try/catch` in an async function?

<details>
<summary>Answer</summary>

- [x] Rejections can look **silent** (unhandled promise).

</details>

### Question 7: What does `function getData() { fetch(...).then(...) }` return?

<details>
<summary>Answer</summary>

- [x] **`undefined`**. The promise is **not returned**.

</details>

### Question 8: Name three async checklist items.

<details>
<summary>Answer</summary>

- [x] **Console**, **Network tab**, **log the response** (also try/catch and await breakpoints).

</details>


</details>

## Summary

Async runs later. Log responses, watch Network, catch errors, return promises, and breakpoint on await. The skill is habit, not talent.

## References

- [JS Debugging Async (W3Schools)](https://www.w3schools.com/js/js_debugging_async.asp)
- [MDN: fetch()](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [MDN: async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [MDN: Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
