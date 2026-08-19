<details>
  <summary>APIs Intro</summary>

## Introduction

A Web API is an interface for the web. Browser APIs (DOM, Fetch, Storage, History, Geolocation) are built in. Third-party APIs (YouTube, Twitter, Facebook) are loaded from the network.

This section has **7** examples:

- [x] **Example 1:** What is a Web API? [View](#apis-intro-example-01)
- [x] **Example 2:** Browser API example — Geolocation coordinates [View](#apis-intro-example-02)
- [x] **Example 3:** The DOM API [View](#apis-intro-example-03)
- [x] **Example 4:** The Fetch API [View](#apis-intro-example-04)
- [x] **Example 5:** The Web Storage API [View](#apis-intro-example-05)
- [x] **Example 6:** The History API [View](#apis-intro-example-06)
- [x] **Example 7:** Third-party APIs [View](#apis-intro-example-07)

## Detailed Explanation

- [x] API = Application Programming Interface.
- [x] Geolocation is the intro’s concrete browser example.
- [x] Third-party APIs are not built in.

<a id="apis-intro-example-01"></a>

### **Example 1: What is a Web API?**

- [x] **API** = Application Programming Interface.
- [x] A **Web API** is an API for the web: browser APIs extend the **browser**; server APIs extend a **server**.
- [x] You call methods the environment provides — you do not download them for built-in APIs.

Sandbox: `code_sandbox/apis-intro/what.html`

```html
API = Application Programming Interface
A Browser API extends the browser.
A Server API extends a server.
```

<img alt="apis-intro example 1 source" src="./code_sandbox/snaps/apis-intro-01-code.png" />

<img alt="apis-intro example 1 result" src="./code_sandbox/snaps/apis-intro-01-result.png" />

- [x] **Outcome:** The snapshot restates the three sentences from the page.

<a id="apis-intro-example-02"></a>

### **Example 2: Browser API example — Geolocation coordinates**

- [x] Browsers ship built-in APIs. Geolocation returns **coordinates**.
- [x] `navigator.geolocation.getCurrentPosition(success)` if supported.
- [x] Else show “not supported”.
- [x] Headless/permission-denied environments take the error path; we still prove the API object exists.

Sandbox: `code_sandbox/apis-intro/geo-example.html`

```html
const myElement = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    myElement.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showPosition(position) {
  myElement.innerHTML = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
}
```

<img alt="apis-intro example 2 source" src="./code_sandbox/snaps/apis-intro-02-code.png" />

<img alt="apis-intro example 2 result" src="./code_sandbox/snaps/apis-intro-02-result.png" />

- [x] **Outcome:** `navigator.geolocation` exists (**true** here). The snapshot then either prints lat/long or a permission/unavailable message — both are valid outcomes of this API.

<a id="apis-intro-example-03"></a>

### **Example 3: The DOM API**

- [x] Listed as a **most important** API.
- [x] Structured representation of the page so JS can change elements, attributes, and content.
- [x] This is the HTML DOM chapters you already studied.

Sandbox: `code_sandbox/apis-intro/dom-api.html`

```html
document.getElementById("demo")
```

<img alt="apis-intro example 3 source" src="./code_sandbox/snaps/apis-intro-03-code.png" />

<img alt="apis-intro example 3 result" src="./code_sandbox/snaps/apis-intro-03-result.png" />

- [x] **Outcome:** `document` is the DOM API entry; `nodeType` **9** is the Document.

<a id="apis-intro-example-04"></a>

### **Example 4: The Fetch API**

- [x] The modern **networking** API (vs XMLHttpRequest).
- [x] Also listed as fundamental.

Sandbox: `code_sandbox/apis-intro/fetch-api.html`

```html
fetch(url)
```

<img alt="apis-intro example 4 source" src="./code_sandbox/snaps/apis-intro-04-code.png" />

<img alt="apis-intro example 4 result" src="./code_sandbox/snaps/apis-intro-04-result.png" />

- [x] **Outcome:** `typeof fetch` is **function**.

<a id="apis-intro-example-05"></a>

### **Example 5: The Web Storage API**

- [x] **localStorage** and **sessionStorage** — key/value in the browser, more straightforward than cookies for non-secret data.
- [x] Persists across reloads (local) or for one tab session (session).

Sandbox: `code_sandbox/apis-intro/web-storage.html`

```html
localStorage / sessionStorage
```

<img alt="apis-intro example 5 source" src="./code_sandbox/snaps/apis-intro-05-code.png" />

<img alt="apis-intro example 5 result" src="./code_sandbox/snaps/apis-intro-05-result.png" />

- [x] **Outcome:** `typeof localStorage.setItem` is **function**.

<a id="apis-intro-example-06"></a>

### **Example 6: The History API**

- [x] Manipulate **session history** so SPAs can change the URL without a full reload.
- [x] Linked from this intro to the History chapter.

Sandbox: `code_sandbox/apis-intro/history-api.html`

```html
history.pushState(state, "", url)
```

<img alt="apis-intro example 6 source" src="./code_sandbox/snaps/apis-intro-06-code.png" />

<img alt="apis-intro example 6 result" src="./code_sandbox/snaps/apis-intro-06-result.png" />

- [x] **Outcome:** `typeof history.pushState` is **function**.

<a id="apis-intro-example-07"></a>

### **Example 7: Third-party APIs**

- [x] **Not** built into the browser. You load their script/SDK from the web.
- [x] Examples on the page: **YouTube**, **Twitter**, **Facebook** display widgets.
- [x] You also need API keys and their terms of use.

Sandbox: `code_sandbox/apis-intro/third-party.html`

```html
YouTube API — display videos
Twitter API — display Tweets
Facebook API — display Facebook info
```

<img alt="apis-intro example 7 source" src="./code_sandbox/snaps/apis-intro-07-code.png" />

<img alt="apis-intro example 7 result" src="./code_sandbox/snaps/apis-intro-07-result.png" />

- [x] **Outcome:** The snapshot lists the three third-party examples from the page.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/apis-intro/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does API stand for?

<details>
<summary>Answer</summary>

- [x] **Application Programming Interface**.

</details>

### Question 2: What is a Browser API?

<details>
<summary>Answer</summary>

- [x] A built-in interface that **extends the browser** (DOM, Fetch, Geolocation, …).

</details>

### Question 3: Name the three “most important” APIs on the page.

<details>
<summary>Answer</summary>

- [x] **DOM**, **Fetch**, **Web Storage**.

</details>

### Question 4: What fourth API is also introduced?

<details>
<summary>Answer</summary>

- [x] The **History** API.

</details>

### Question 5: Are third-party APIs built in?

<details>
<summary>Answer</summary>

- [x] **No** — you load their code (YouTube, Twitter, Facebook examples).

</details>

### Question 6: How do you start Geolocation?

<details>
<summary>Answer</summary>

- [x] **`navigator.geolocation.getCurrentPosition(success)`** if the object exists.

</details>

### Question 7: What is Fetch for?

<details>
<summary>Answer</summary>

- [x] **Networking** — requesting resources from a server.

</details>

### Question 8: What does Web Storage store?

<details>
<summary>Answer</summary>

- [x] **Key/value** pairs (`localStorage` / `sessionStorage`).

</details>

### Question 9: Why do SPAs use History?

<details>
<summary>Answer</summary>

- [x] To change the **URL** without a full page reload.

</details>

### Question 10: Is Geolocation a third-party API?

<details>
<summary>Answer</summary>

- [x] **No** — it is a **browser** API.

</details>


</details>

## Summary

Use built-in browser APIs first (DOM, Fetch, Storage, History). Load third-party SDKs only when you need their service. Geolocation is permission-gated.

## References

- [APIs Intro](https://www.w3schools.com/js/js_api_intro.asp)
- [MDN Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)

</details>
