# JS Location

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

`window.location` reads the current URL (href, hostname, pathname, protocol, port) and can load another document with `assign`.

This section has **6** examples:

- [x] **Example 1:** window.location.href — full URL of this page [View](#js-location-example-01)
- [x] **Example 2:** window.location.hostname — host name [View](#js-location-example-02)
- [x] **Example 3:** window.location.pathname — path and file name [View](#js-location-example-03)
- [x] **Example 4:** window.location.protocol — http: or https: [View](#js-location-example-04)
- [x] **Example 5:** window.location.port — host port number [View](#js-location-example-05)
- [x] **Example 6:** window.location.assign() — load a new document [View](#js-location-example-06)

## Detailed Explanation

- [x] Omit the `window.` prefix if you want: `location.href`.
- [x] `assign` adds history; `replace` does not.
- [x] Default ports often make `port` an empty string.

<a id="js-location-example-01"></a>

### **Example 1: window.location.href — full URL of this page**

- [x] `location` (or `window.location`) is the current **address** and a way to **navigate**.
- [x] `href` is the entire URL: protocol, host, port, path, query, hash.
- [x] Assigning to `href` loads a new page (same as clicking a link).
- [x] The sandbox is served from `http://127.0.0.1:8771/...` so `href` includes that.

Sandbox: `code_sandbox/js-location/href.html`

```html
document.getElementById("demo").innerHTML = "Page location is " + window.location.href;
```

<img alt="js-location example 1 source" src="../code_sandbox/snaps/js-location-01-code.png" />

<img alt="js-location example 1 result" src="../code_sandbox/snaps/js-location-01-result.png" />

- [x] **Outcome:** **Page location is** the full sandbox URL (http, 127.0.0.1, port, path).

<a id="js-location-example-02"></a>

### **Example 2: window.location.hostname — host name**

- [x] `hostname` is the **domain** (or IP) without protocol or port.
- [x] On this sandbox it is **`127.0.0.1`**.
- [x] It does not include `:8771` — that is `port`.

Sandbox: `code_sandbox/js-location/hostname.html`

```html
document.getElementById("demo").innerHTML = "Page hostname is " + window.location.hostname;
```

<img alt="js-location example 2 source" src="../code_sandbox/snaps/js-location-02-code.png" />

<img alt="js-location example 2 result" src="../code_sandbox/snaps/js-location-02-result.png" />

- [x] **Outcome:** **Page hostname is 127.0.0.1** (or `localhost` if you used that host).

<a id="js-location-example-03"></a>

### **Example 3: window.location.pathname — path and file name**

- [x] `pathname` is the path after the host, starting with `/`.
- [x] It does **not** include the query string or hash.
- [x] Here it ends with the example file name under `/js-location/`.

Sandbox: `code_sandbox/js-location/pathname.html`

```html
document.getElementById("demo").innerHTML = "Page path is " + window.location.pathname;
```

<img alt="js-location example 3 source" src="../code_sandbox/snaps/js-location-03-code.png" />

<img alt="js-location example 3 result" src="../code_sandbox/snaps/js-location-03-result.png" />

- [x] **Outcome:** **Page path is** `/js-location/pathname.html` (this file).

<a id="js-location-example-04"></a>

### **Example 4: window.location.protocol — http: or https:**

- [x] `protocol` includes the colon: **`http:`** or **`https:`**.
- [x] The sandbox server is not TLS, so this page is **`http:`**.
- [x] Use this if you need to know whether the page is secure.

Sandbox: `code_sandbox/js-location/protocol.html`

```html
document.getElementById("demo").innerHTML = "Page protocol is " + window.location.protocol;
```

<img alt="js-location example 4 source" src="../code_sandbox/snaps/js-location-04-code.png" />

<img alt="js-location example 4 result" src="../code_sandbox/snaps/js-location-04-result.png" />

- [x] **Outcome:** **Page protocol is http:** on the local static server.

<a id="js-location-example-05"></a>

### **Example 5: window.location.port — host port number**

- [x] `port` is the port as a **string**. Default ports (80/443) are often **empty**.
- [x] This sandbox uses **8771**, so `port` is **`8771`**.
- [x] The W3Schools Tryit title says “Display the name of the host” but the code reads **`port`** — we follow the code.

Sandbox: `code_sandbox/js-location/port.html`

```html
document.getElementById("demo").innerHTML = "Port number is " + window.location.port;
```

<img alt="js-location example 5 source" src="../code_sandbox/snaps/js-location-05-code.png" />

<img alt="js-location example 5 result" src="../code_sandbox/snaps/js-location-05-result.png" />

- [x] **Outcome:** **Port number is 8771** for this HTTP screenshot server.

<a id="js-location-example-06"></a>

### **Example 6: window.location.assign() — load a new document**

- [x] `assign(url)` loads `url` and **pushes** a history entry (Back can return).
- [x] `location.href = url` does the same for most purposes.
- [x] `replace(url)` also navigates but **does not** keep the current page in history.
- [x] The snapshot does **not** leave this page (that would blank the result). It shows the handler that *would* assign.

Sandbox: `code_sandbox/js-location/assign.html`

```html
<input type="button" value="Load new document" onclick="newDoc()">
<script>
function newDoc() {
  window.location.assign("https://www.w3schools.com");
}
</script>
```

<img alt="js-location example 6 source" src="../code_sandbox/snaps/js-location-06-code.png" />

<img alt="js-location example 6 result" src="../code_sandbox/snaps/js-location-06-result.png" />

- [x] **Outcome:** The button is present; the snapshot prints that `newDoc` would **assign** `https://www.w3schools.com` rather than navigating away.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-location/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What object reads the current URL?

<details>
<summary>Answer</summary>

- [x] **`window.location`** (also just `location`).

</details>

### Question 2: Which property is the full URL?

<details>
<summary>Answer</summary>

- [x] **`href`**.

</details>

### Question 3: Does `hostname` include the port?

<details>
<summary>Answer</summary>

- [x] **No** — port is **`location.port`**.

</details>

### Question 4: What does `pathname` start with?

<details>
<summary>Answer</summary>

- [x] A **slash**, e.g. `/js-location/pathname.html`.

</details>

### Question 5: What is `protocol` for this sandbox?

<details>
<summary>Answer</summary>

- [x] **`http:`** (colon included).

</details>

### Question 6: When is `port` an empty string?

<details>
<summary>Answer</summary>

- [x] When the URL uses the **default** port (80 or 443).

</details>

### Question 7: What does `assign` do to history?

<details>
<summary>Answer</summary>

- [x] It **adds** an entry so Back can return.

</details>

### Question 8: How is `replace` different?

<details>
<summary>Answer</summary>

- [x] It **overwrites** the current history entry.

</details>

### Question 9: Name three location properties from the page.

<details>
<summary>Answer</summary>

- [x] Any three of **href, hostname, pathname, protocol, port**.

</details>

### Question 10: Does assigning `href` load a new page?

<details>
<summary>Answer</summary>

- [x] **Yes** — it navigates.

</details>


</details>

## Summary

Read location.href for the full URL and the other properties for the pieces. assign() navigates; do not call it if you still need the current page.

## References

- [JS Location](https://www.w3schools.com/js/js_window_location.asp)
- [MDN Location](https://developer.mozilla.org/en-US/docs/Web/API/Location)
