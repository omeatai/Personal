# HTML SSE

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

**Server-Sent Events (SSE)** let the **server push** updates to the page over HTTP. The page does not poll. This chapter uses **`EventSource`**, `onmessage`, and a server that sends `text/event-stream` lines starting with **`data:`**. Examples: feeds, stocks, scores.

This section has **2** examples:

- [x] **Example 1:** Page [View](#html-sse-example-01)
- [x] **Example 2:** PHP from the chapter [View](#html-sse-example-02)

## Detailed Explanation

- [x] **One-way messaging** — server → page. Facebook/Twitter-style updates, news, sports.
- [x] **Browser:** `new EventSource("demo_sse.php")` then `source.onmessage`.
  - Check: `typeof(EventSource) !== "undefined"`.
  - Each message appends `event.data` into `#result`.
- [x] **EventSource events:** `onopen` (connected), `onmessage` (data), `onerror` (error).

<a id="html-sse-example-01"></a>

### **Example 1: Page**

- [x] **Server**
  - Header **`Content-Type: text/event-stream`**, no cache.
  - Each event: `data: The server time is: …` then a **blank line**.
  - The page shows **PHP** and **ASP**. This sandbox has **no PHP**, so `sse_server.py` on **port 8767** sends the same `data:` stream and the page uses `EventSource("/sse")`.

Sandbox: `code_sandbox/html-sse/index.html`

```javascript
var source = new EventSource("demo_sse.php");
source.onmessage = function (event) {
  document.getElementById("result").innerHTML += event.data + "<br>";
};
```

<img alt="html-sse source" src="../code_sandbox/snaps/html-sse-code.png" />

<img alt="html-sse result" src="../code_sandbox/snaps/html-sse-result.png" />

- [x] **Outcome:** the page opens an EventSource and appends each `data:` line into `#result`. The sandbox stand-in `sse_server.py` streams `The server time is: …` every second.

<a id="html-sse-example-02"></a>

### **Example 2: PHP from the chapter**

- [x] This example runs the tested markup.

```php
<?php
header('Content-Type: text/event-stream');
header('Cache-Control: no-cache');
$time = date('r');
echo "data: The server time is: {$time}\n\n";
flush();
?>
```

- [x] **Outcome:** the page demonstrates **PHP from the chapter** as shown in the result snap.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox/html-sse
python sse_server.py
```

Then open `http://127.0.0.1:8767/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How is SSE different from a normal page request?

<details>
<summary>Answer</summary>

- [x] The page does **not** keep asking.
- [x] The **server pushes** updates over HTTP.

</details>

### Question 2: Which JS object receives events?

<details>
<summary>Answer</summary>

- [x] **`EventSource`**.
- [x] Handle **`onmessage`** and read **`event.data`**.

</details>

### Question 3: What Content-Type must the server send?

<details>
<summary>Answer</summary>

- [x] **`text/event-stream`**.
- [x] Each message starts with **`data:`** and ends with a blank line.

</details>

### Question 4: Which EventSource events are listed?

<details>
<summary>Answer</summary>

- [x] **`onopen`**, **`onmessage`**, **`onerror`**.

</details>

### Question 5: Why doesn’t `http.server 8766` run this demo?

<details>
<summary>Answer</summary>

- [x] It only serves **static files**.
- [x] SSE needs a process that keeps the connection and writes **event-stream** data (PHP on the page; `sse_server.py` here).

</details>

</details>

## Summary

SSE is one-way server push. Use `EventSource` and `onmessage`. The server sets `text/event-stream` and writes `data: …` lines. The tutorial uses PHP/ASP; this sandbox uses a small Python streamer on port 8767.

## References

- [HTML Server-Sent Events API (W3Schools)](https://www.w3schools.com/html/html5_serversentevents.asp)
- [MDN: Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)
- [MDN: `EventSource`](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)
- [WHATWG: Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html)
