# HTML Geolocation

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

The **Geolocation API** reads the user’s **current location**. Because that is private, the browser **asks permission**. This chapter covers `navigator.geolocation`, **`getCurrentPosition()`**, **error codes**, returned **coords**, and **`watchPosition()` / `clearWatch()`**. It works on **secure contexts** (HTTPS or localhost).

This section has **1** example:

- [x] **Example 1:** `index.html` [View](#html-geolocation-example-01)

## Detailed Explanation

- [x] **Privacy** — location is unavailable until the user **approves**.
- [x] **Secure context** — HTTPS (localhost/`127.0.0.1` also counts). Most accurate on **GPS** devices.
- [x] **`navigator.geolocation.getCurrentPosition(success, error)`**
  - If unsupported: “Geolocation is not supported by this browser.”
  - Success: **Latitude** and **Longitude** from `position.coords`.
  - Sandbox: `code_sandbox/html-geolocation/index.html` (button **Try It**). Headless snaps will not grant permission.

<img alt="html-geolocation result" src="../code_sandbox/snaps/html-geolocation-result.png" />
- [x] **Error `code`:** `PERMISSION_DENIED`, `POSITION_UNAVAILABLE`, `TIMEOUT`, `UNKNOWN_ERROR`.
- [x] **Uses:** local info, nearby points of interest, turn-by-turn GPS.
- [x] **Always returned:** `coords.latitude`, `coords.longitude`, `coords.accuracy`. Optional: altitude, altitudeAccuracy, heading, speed, timestamp.
- [x] **`watchPosition()`** — keeps updating as the user moves (needs a GPS device). **`clearWatch()`** stops it.

<a id="html-geolocation-example-01"></a>

### **Example 1: `index.html`**

- [x] This example runs the tested markup.

```javascript
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(success, error);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
```

<img alt="html-geolocation source" src="../code_sandbox/snaps/html-geolocation-code.png" />

<img alt="html-geolocation result" src="../code_sandbox/snaps/html-geolocation-result.png" />

- [x] **Outcome:** the browser shows **function getLocation() { if (navigator.geolocation) { navigator.geolocation.getCurrentPosition(success, error); } else { x.innerHTML = "Geolocation is not supported by this browser."; } }**.

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
