# HTML Web APIs

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

A **Web API** is an **Application Programming Interface for the Web**: functions that let you use browser features or data with simpler syntax. This chapter lists the main **HTML5 APIs**, how to use them safely, and **third-party** APIs. There is **no Try it Yourself** demo on this page.

This section has **1** example:

- [x] **Example 1:** HTML5 APIs overview [View](#html-web-apis-example-01)

## Detailed Explanation

- [x] **Why APIs?** They can extend the browser, simplify complex work, and hide messy code behind easy syntax.
- [x] **API** = interface of functions/subroutines to reach features or data of an app, OS, or service.
- [x] **HTML5 APIs** (built into browsers)
  1. **Geolocation** — latitude and longitude (user’s current location).
  2. **Drag and Drop** — drag-and-drop in the browser.
  3. **Web Storage** — key/value storage (clearer than cookies).
  4. **Web Workers** — JavaScript in the **background** without freezing the page (user can still click and select).
  5. **Server-Sent Events** — the page **automatically** gets updates from a server.
  6. **Canvas** — draw graphics with JavaScript.
- [x] **When you implement an API**
  - **Check browser capability** — always test support; provide a fallback script or message.
  - **Robust error handling** — APIs can fail; keep the UX intact.
  - **Request user permission** — for sensitive data (Geolocation), **ask consent** first.
- [x] **Third-party APIs** are **not** built into the browser. Download their code from the web. Examples: **YouTube** (videos), **Twitter** (tweets), **Facebook** (profile info).

<a id="html-web-apis-example-01"></a>

### **Example 1: HTML5 APIs overview**

- [x] This chapter has **no Tryit page**. Later sections demo Geolocation, Drag and Drop, Web Storage, Web Workers, SSE, and Canvas.

```text
# No code snippets in this topic.
```

- [x] **Outcome:** there is nothing to render here — the APIs are listed in the bullets above.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

No server was started for this section (no sandbox page to open).

```bash
# none
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does API stand for?

<details>
<summary>Answer</summary>

- [x] **Application Programming Interface**.
- [x] A set of functions to access features or data.

</details>

### Question 2: Name the six HTML5 APIs listed here.

<details>
<summary>Answer</summary>

- [x] Geolocation, Drag and Drop, Web Storage, Web Workers, Server-Sent Events, Canvas.

</details>

### Question 3: What is a Web Worker for?

<details>
<summary>Answer</summary>

- [x] Run JavaScript in the **background**.
- [x] The page stays usable (click, select) while it runs.

</details>

### Question 4: What three practices should you always follow?

<details>
<summary>Answer</summary>

- [x] Check **browser support** (and fallback).
- [x] Add **error handling**.
- [x] **Ask permission** before sensitive data (Geolocation).

</details>

### Question 5: Are YouTube/Twitter/Facebook APIs built into the browser?

<details>
<summary>Answer</summary>

- [x] **No.** They are **third-party**; you download their code.

</details>

</details>

## Summary

Web APIs wrap browser features. HTML5 highlights Geolocation, Drag and Drop, Web Storage, Workers, SSE, and Canvas. Check support, handle errors, and ask permission. Third-party APIs are downloaded, not built-in.

## References

- [HTML - What is a Web API? (W3Schools)](https://www.w3schools.com/html/html5_api_whatis.asp)
- [MDN: Web APIs](https://developer.mozilla.org/en-US/docs/Web/API)
