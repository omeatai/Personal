# JS Fetch API

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Fetch is the modern way to load a URL. You get a Response, then read it with text/json/blob/bytes/arrayBuffer. Always check `ok` — Fetch does not throw on 404. Work is asynchronous, so later lines run first unless you await.

This section has **17** examples:

- [x] **Example 1:** fetch().then — read a text file [View](#js-fetch-api-example-01)
- [x] **Example 2:** fetch with arrow functions [View](#js-fetch-api-example-02)
- [x] **Example 3:** async function loadText — await fetch [View](#js-fetch-api-example-03)
- [x] **Example 4:** The Response object [View](#js-fetch-api-example-04)
- [x] **Example 5:** response.ok [View](#js-fetch-api-example-05)
- [x] **Example 6:** response.status [View](#js-fetch-api-example-06)
- [x] **Example 7:** response.statusText [View](#js-fetch-api-example-07)
- [x] **Example 8:** response.url [View](#js-fetch-api-example-08)
- [x] **Example 9:** JavaScript continues while fetch is in flight [View](#js-fetch-api-example-09)
- [x] **Example 10:** Checking HTTP errors — if (!response.ok) [View](#js-fetch-api-example-10)
- [x] **Example 11:** response.json() — parse JSON body [View](#js-fetch-api-example-11)
- [x] **Example 12:** response.blob() — binary Blob [View](#js-fetch-api-example-12)
- [x] **Example 13:** response.bytes() — Uint8Array [View](#js-fetch-api-example-13)
- [x] **Example 14:** response.arrayBuffer() — ArrayBuffer [View](#js-fetch-api-example-14)
- [x] **Example 15:** Fetch vs XHR — Promise-based vs callback-based [View](#js-fetch-api-example-15)
- [x] **Example 16:** Fetch vs XHR — error handling [View](#js-fetch-api-example-16)
- [x] **Example 17:** Fetch vs XHR — streams [View](#js-fetch-api-example-17)

## Detailed Explanation

- [x] then / arrows / async await are the same two steps.
- [x] ok, status, statusText, url describe the Response.
- [x] HTTP errors need an explicit check.
- [x] Fetch is Promise-based and stream-capable vs XHR.

<a id="js-fetch-api-example-01"></a>

### **Example 1: fetch().then — read a text file**

- [x] `fetch(url)` returns a **Promise** of a **Response**.
- [x] The first `.then` receives the Response; **`response.text()`** is another Promise of the body string.
- [x] The second `.then` receives that string (W3Schools `myDisplayer(data)`).
- [x] Fetch needs **http(s)** — not `file://`.

Sandbox: `code_sandbox/js-fetch-api/then-text.html`

```javascript
fetch(file)
  .then(function(response) {
    return response.text();
  })
  .then(function(data) {
    myDisplayer(data);
  });
```

<img alt="js-fetch-api example 1 source" src="../code_sandbox/snaps/js-fetch-api-01-code.png" />

<img alt="js-fetch-api example 1 result" src="../code_sandbox/snaps/js-fetch-api-01-result.png" />

- [x] **Outcome:** The body of **fetch.txt** is displayed: **Hello Fetch API** on the first line.

<a id="js-fetch-api-example-02"></a>

### **Example 2: fetch with arrow functions**

- [x] Same flow, shorter: `response => response.text()` then `data => myDisplayer(data)`.
- [x] Arrows here are just functions — still two async steps.
- [x] Errors still need `.catch` or `try/catch` in `async`.

Sandbox: `code_sandbox/js-fetch-api/then-arrows.html`

```javascript
fetch(file)
  .then(response => response.text())
  .then(data => myDisplayer(data));
```

<img alt="js-fetch-api example 2 source" src="../code_sandbox/snaps/js-fetch-api-02-code.png" />

<img alt="js-fetch-api example 2 result" src="../code_sandbox/snaps/js-fetch-api-02-result.png" />

- [x] **Outcome:** Arrow-style fetch also prints the **fetch.txt** contents.

<a id="js-fetch-api-example-03"></a>

### **Example 3: async function loadText — await fetch**

- [x] `async function` lets you **`await fetch(file)`** then **`await response.text()`**.
- [x] This is the same two Promises, written as if they were sequential.
- [x] W3Schools `loadText` then calls `myDisplayer`.

Sandbox: `code_sandbox/js-fetch-api/async-fn.html`

```javascript
async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(await response.text());
}
```

<img alt="js-fetch-api example 3 source" src="../code_sandbox/snaps/js-fetch-api-03-code.png" />

<img alt="js-fetch-api example 3 result" src="../code_sandbox/snaps/js-fetch-api-03-result.png" />

- [x] **Outcome:** `loadText("fetch.txt")` displays the file text.

<a id="js-fetch-api-example-04"></a>

### **Example 4: The Response object**

- [x] If you `myDisplayer(response)` without `.text()`, you get a **Response**, not the file contents.
- [x] Useful properties: `ok`, `status`, `statusText`, `url`.
- [x] `String(response)` is not the body — you must call a reader method.

Sandbox: `code_sandbox/js-fetch-api/response-object.html`

```javascript
async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(response);
}
```

<img alt="js-fetch-api example 4 source" src="../code_sandbox/snaps/js-fetch-api-04-code.png" />

<img alt="js-fetch-api example 4 result" src="../code_sandbox/snaps/js-fetch-api-04-result.png" />

- [x] **Outcome:** `response` is an object; `ok` is **true** for fetch.txt. The default string is not the file body.

<a id="js-fetch-api-example-05"></a>

### **Example 5: response.ok**

- [x] `ok` is **true** for status **200–299**.
- [x] It is **false** for 404/500. Fetch **does not throw** on HTTP errors — check `ok`.
- [x] Network failure (offline, CORS) **does** reject the Promise.

Sandbox: `code_sandbox/js-fetch-api/ok.html`

```javascript
async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(response.ok);
}
```

<img alt="js-fetch-api example 5 source" src="../code_sandbox/snaps/js-fetch-api-05-code.png" />

<img alt="js-fetch-api example 5 result" src="../code_sandbox/snaps/js-fetch-api-05-result.png" />

- [x] **Outcome:** `response.ok` is **true** for the existing file.

<a id="js-fetch-api-example-06"></a>

### **Example 6: response.status**

- [x] `status` is the **HTTP code**: 200, 404, 500, …
- [x] Pair it with `ok` when you log errors.

Sandbox: `code_sandbox/js-fetch-api/status.html`

```javascript
async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(response.status);
}
```

<img alt="js-fetch-api example 6 source" src="../code_sandbox/snaps/js-fetch-api-06-code.png" />

<img alt="js-fetch-api example 6 result" src="../code_sandbox/snaps/js-fetch-api-06-result.png" />

- [x] **Outcome:** `status` is **200** for fetch.txt.

<a id="js-fetch-api-example-07"></a>

### **Example 7: response.statusText**

- [x] `statusText` is the reason phrase, e.g. **OK** or **Not Found**.
- [x] It can be empty in HTTP/2. Prefer `status` + `ok` for logic.

Sandbox: `code_sandbox/js-fetch-api/status-text.html`

```javascript
response.statusText
```

<img alt="js-fetch-api example 7 source" src="../code_sandbox/snaps/js-fetch-api-07-code.png" />

<img alt="js-fetch-api example 7 result" src="../code_sandbox/snaps/js-fetch-api-07-result.png" />

- [x] **Outcome:** For 200, `statusText` is typically **OK**.

<a id="js-fetch-api-example-08"></a>

### **Example 8: response.url**

- [x] `url` is the **final** URL after redirects.
- [x] Useful to see where the browser actually landed.

Sandbox: `code_sandbox/js-fetch-api/url.html`

```javascript
async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(response.url);
}
```

<img alt="js-fetch-api example 8 source" src="../code_sandbox/snaps/js-fetch-api-08-code.png" />

<img alt="js-fetch-api example 8 result" src="../code_sandbox/snaps/js-fetch-api-08-result.png" />

- [x] **Outcome:** `response.url` ends with **`/js-fetch-api/fetch.txt`**.

<a id="js-fetch-api-example-09"></a>

### **Example 9: JavaScript continues while fetch is in flight**

- [x] `loadText("fetch.txt")` starts work and **returns immediately**.
- [x] The next line `myDisplayer("JavaScript continues.")` runs **before** the file arrives.
- [x] That is why the page shows “continues” first, then the file — unless you `await loadText` at the top level.

Sandbox: `code_sandbox/js-fetch-api/async-continues.html`

```javascript
async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(response.url);
}
loadText("fetch.txt");
myDisplayer("JavaScript continues.");
```

<img alt="js-fetch-api example 9 source" src="../code_sandbox/snaps/js-fetch-api-09-code.png" />

<img alt="js-fetch-api example 9 result" src="../code_sandbox/snaps/js-fetch-api-09-result.png" />

- [x] **Outcome:** The log order is **JavaScript continues.** first, then the response URL — proving fetch is asynchronous.

<a id="js-fetch-api-example-10"></a>

### **Example 10: Checking HTTP errors — if (!response.ok)**

- [x] Fetch **fulfills** on 404. You must **`if (!response.ok)`** and show `status + statusText`.
- [x] Then `return` so you do not parse an error page as success.
- [x] The sandbox fetches a missing file to force **404**.

Sandbox: `code_sandbox/js-fetch-api/http-error.html`

```javascript
async function loadText(file) {
  const response = await fetch(file);
  if (!response.ok) {
    myDisplayer(response.status + " " + response.statusText);
    return;
  }
  myDisplayer(await response.text());
}
```

<img alt="js-fetch-api example 10 source" src="../code_sandbox/snaps/js-fetch-api-10-code.png" />

<img alt="js-fetch-api example 10 result" src="../code_sandbox/snaps/js-fetch-api-10-result.png" />

- [x] **Outcome:** Fetching a missing path prints **404** and a status text (often **Not Found**).

<a id="js-fetch-api-example-11"></a>

### **Example 11: response.json() — parse JSON body**

- [x] `json()` reads the body and **`JSON.parse`s** it.
- [x] Do **not** call `JSON.parse` again on the result.
- [x] Wrong Content-Type still often parses if the bytes are JSON.

Sandbox: `code_sandbox/js-fetch-api/json-method.html`

```javascript
const data = await response.json();
```

<img alt="js-fetch-api example 11 source" src="../code_sandbox/snaps/js-fetch-api-11-code.png" />

<img alt="js-fetch-api example 11 result" src="../code_sandbox/snaps/js-fetch-api-11-result.png" />

- [x] **Outcome:** `customer.json` parses to an object whose **name** is **John Doe**.

<a id="js-fetch-api-example-12"></a>

### **Example 12: response.blob() — binary Blob**

- [x] `blob()` is for files you might download or put in an `<img>` via `URL.createObjectURL`.
- [x] The Blob has `size` and `type`.

Sandbox: `code_sandbox/js-fetch-api/blob-method.html`

```javascript
const data = await response.blob();
```

<img alt="js-fetch-api example 12 source" src="../code_sandbox/snaps/js-fetch-api-12-code.png" />

<img alt="js-fetch-api example 12 result" src="../code_sandbox/snaps/js-fetch-api-12-result.png" />

- [x] **Outcome:** `fetch.txt` as a Blob has a **size** > 0 and a MIME `type` (often `text/plain`).

<a id="js-fetch-api-example-13"></a>

### **Example 13: response.bytes() — Uint8Array**

- [x] `bytes()` is a newer method that returns a **Uint8Array**.
- [x] If missing, fall back to `new Uint8Array(await response.arrayBuffer())`.
- [x] W3Schools lists it on the Response methods table.

Sandbox: `code_sandbox/js-fetch-api/bytes-method.html`

```javascript
const data = await response.bytes();
```

<img alt="js-fetch-api example 13 source" src="../code_sandbox/snaps/js-fetch-api-13-code.png" />

<img alt="js-fetch-api example 13 result" src="../code_sandbox/snaps/js-fetch-api-13-result.png" />

- [x] **Outcome:** `bytes()` (or the ArrayBuffer fallback) yields a **Uint8Array** whose first bytes decode as **Hello**.

<a id="js-fetch-api-example-14"></a>

### **Example 14: response.arrayBuffer() — ArrayBuffer**

- [x] `arrayBuffer()` is the raw binary buffer (WebGL, WASM, manual parsing).
- [x] `byteLength` is the size in bytes.

Sandbox: `code_sandbox/js-fetch-api/array-buffer.html`

```javascript
const data = await response.arrayBuffer();
```

<img alt="js-fetch-api example 14 source" src="../code_sandbox/snaps/js-fetch-api-14-code.png" />

<img alt="js-fetch-api example 14 result" src="../code_sandbox/snaps/js-fetch-api-14-result.png" />

- [x] **Outcome:** `byteLength` is the file size in bytes (same as the Blob size).

<a id="js-fetch-api-example-15"></a>

### **Example 15: Fetch vs XHR — Promise-based vs callback-based**

- [x] Fetch is **Promise-based** (`then` / `await`).
- [x] XHR is **callback-based** (`onload`, `onerror`).
- [x] That is the first row of the comparison table.

Sandbox: `code_sandbox/js-fetch-api/xhr-syntax.html`

```html
fetch(url).then(r => r.text());
// vs
xhr.onload = function () { /* this.responseText */ };
```

<img alt="js-fetch-api example 15 source" src="../code_sandbox/snaps/js-fetch-api-15-code.png" />

<img alt="js-fetch-api example 15 result" src="../code_sandbox/snaps/js-fetch-api-15-result.png" />

- [x] **Outcome:** The snapshot labels the two styles: **Promise-based** vs **callback-based**.

<a id="js-fetch-api-example-16"></a>

### **Example 16: Fetch vs XHR — error handling**

- [x] Fetch **rejects on network failure**, not on 404.
- [x] XHR needs **manual** `status` checks in `onload` plus `onerror`.
- [x] Always check `response.ok` with Fetch.

Sandbox: `code_sandbox/js-fetch-api/xhr-errors.html`

```html
if (!response.ok) { /* HTTP error */ }
// XHR: if (xhr.status >= 200 && xhr.status < 300)
```

<img alt="js-fetch-api example 16 source" src="../code_sandbox/snaps/js-fetch-api-16-code.png" />

<img alt="js-fetch-api example 16 result" src="../code_sandbox/snaps/js-fetch-api-16-result.png" />

- [x] **Outcome:** The note prints: Fetch rejects on **network** failure; HTTP errors need **`ok`**.

<a id="js-fetch-api-example-17"></a>

### **Example 17: Fetch vs XHR — streams**

- [x] Fetch **supports streams** (`response.body` is a ReadableStream).
- [x] XHR **does not** give you that streaming body API.
- [x] Large downloads can be consumed chunk by chunk with Fetch.

Sandbox: `code_sandbox/js-fetch-api/xhr-streams.html`

```html
response.body // ReadableStream in Fetch
```

<img alt="js-fetch-api example 17 source" src="../code_sandbox/snaps/js-fetch-api-17-code.png" />

<img alt="js-fetch-api example 17 result" src="../code_sandbox/snaps/js-fetch-api-17-result.png" />

- [x] **Outcome:** `response.body` exists as a **ReadableStream** on this Response.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-fetch-api/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `fetch` return?

<details>
<summary>Answer</summary>

- [x] A **Promise** that resolves to a **Response**.

</details>

### Question 2: How do you read a text body?

<details>
<summary>Answer</summary>

- [x] **`response.text()`** (another Promise).

</details>

### Question 3: Does Fetch throw on 404?

<details>
<summary>Answer</summary>

- [x] **No** — check **`response.ok`** or `status`.

</details>

### Question 4: What does `ok` mean?

<details>
<summary>Answer</summary>

- [x] Status is in **200–299**.

</details>

### Question 5: Why does “JavaScript continues” print first?

<details>
<summary>Answer</summary>

- [x] `fetch` is **asynchronous**; the next line runs before the response.

</details>

### Question 6: What is `response.url`?

<details>
<summary>Answer</summary>

- [x] The **final** URL after redirects.

</details>

### Question 7: How do you parse JSON?

<details>
<summary>Answer</summary>

- [x] **`await response.json()`** — do not `JSON.parse` that result again.

</details>

### Question 8: When does Fetch **reject**?

<details>
<summary>Answer</summary>

- [x] **Network** failure (and some CORS/abort cases), not HTTP 404.

</details>

### Question 9: Fetch vs XHR syntax?

<details>
<summary>Answer</summary>

- [x] Fetch is **Promise-based**; XHR is **callback-based**.

</details>

### Question 10: Does XHR support body streams like Fetch?

<details>
<summary>Answer</summary>

- [x] **No**.

</details>

### Question 11: Why serve these examples over http?

<details>
<summary>Answer</summary>

- [x] Browsers **block** `fetch` of local files from `file://`.

</details>


</details>

## Summary

Call fetch, await the Response, check ok, then read the body with the matching method. Remember that JavaScript continues while the request is in flight.

## References

- [JS Fetch API](https://www.w3schools.com/js/js_api_fetch.asp)
- [MDN fetch()](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch)
