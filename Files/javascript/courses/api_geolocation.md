# API Geolocation

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The Geolocation API returns the user’s position (`getCurrentPosition`) or a stream of updates (`watchPosition`). Always handle permission, timeout, and unavailable errors. Success always includes latitude, longitude, and accuracy.

This section has **16** examples:

- [x] **Example 1:** getCurrentPosition — latitude and longitude [View](#api-geolocation-example-01)
- [x] **Example 2:** Error PERMISSION_DENIED [View](#api-geolocation-example-02)
- [x] **Example 3:** Error POSITION_UNAVAILABLE [View](#api-geolocation-example-03)
- [x] **Example 4:** Error TIMEOUT [View](#api-geolocation-example-04)
- [x] **Example 5:** Error UNKNOWN_ERROR [View](#api-geolocation-example-05)
- [x] **Example 6:** Displaying the result in a map URL [View](#api-geolocation-example-06)
- [x] **Example 7:** coords.latitude (always returned) [View](#api-geolocation-example-07)
- [x] **Example 8:** coords.longitude (always returned) [View](#api-geolocation-example-08)
- [x] **Example 9:** coords.accuracy (always returned) [View](#api-geolocation-example-09)
- [x] **Example 10:** coords.altitude (if available) [View](#api-geolocation-example-10)
- [x] **Example 11:** coords.altitudeAccuracy (if available) [View](#api-geolocation-example-11)
- [x] **Example 12:** coords.heading (if available) [View](#api-geolocation-example-12)
- [x] **Example 13:** coords.speed (if available) [View](#api-geolocation-example-13)
- [x] **Example 14:** position.timestamp [View](#api-geolocation-example-14)
- [x] **Example 15:** watchPosition() — keep updating [View](#api-geolocation-example-15)
- [x] **Example 16:** clearWatch(id) — stop watching [View](#api-geolocation-example-16)

## Detailed Explanation

- [x] Secure context + permission.
- [x] Error codes 1 / 2 / 3.
- [x] clearWatch stops a watch.
- [x] Map images need a real API key.

<a id="api-geolocation-example-01"></a>

### **Example 1: getCurrentPosition — latitude and longitude**

- [x] `navigator.geolocation.getCurrentPosition(success, error?, options?)`.
- [x] Success receives a **GeolocationPosition** with `coords.latitude` / `longitude`.
- [x] Must be **secure context** (https or localhost) and the user must **allow** permission.
- [x] The snapshot uses a 1.5s timeout so headless Chrome fails fast, then still prints whether the API exists.

Sandbox: `code_sandbox/api-geolocation/get-current.html`

```html
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
}
```

<img alt="api-geolocation example 1 source" src="../code_sandbox/snaps/api-geolocation-01-code.png" />

<img alt="api-geolocation example 1 result" src="../code_sandbox/snaps/api-geolocation-01-result.png" />

- [x] **Outcome:** Either **Latitude/Longitude** numbers appear (permission granted) or an error code is printed. `navigator.geolocation` is present in this browser.

<a id="api-geolocation-example-02"></a>

### **Example 2: Error PERMISSION_DENIED**

- [x] `error.code` **1** — the user (or browser policy) denied permission.
- [x] Show a clear message; do not retry in a loop.

Sandbox: `code_sandbox/api-geolocation/error-denied.html`

```html
case error.PERMISSION_DENIED:
  x.innerHTML = "User denied the request for Geolocation.";
```

<img alt="api-geolocation example 2 source" src="../code_sandbox/snaps/api-geolocation-02-code.png" />

<img alt="api-geolocation example 2 result" src="../code_sandbox/snaps/api-geolocation-02-result.png" />

- [x] **Outcome:** `GeolocationPositionError.PERMISSION_DENIED` is **1**. The switch maps that to the W3Schools sentence.

<a id="api-geolocation-example-03"></a>

### **Example 3: Error POSITION_UNAVAILABLE**

- [x] Code **2** — location hardware/provider failed.

Sandbox: `code_sandbox/api-geolocation/error-unavailable.html`

```html
case error.POSITION_UNAVAILABLE:
  x.innerHTML = "Location information is unavailable.";
```

<img alt="api-geolocation example 3 source" src="../code_sandbox/snaps/api-geolocation-03-code.png" />

<img alt="api-geolocation example 3 result" src="../code_sandbox/snaps/api-geolocation-03-result.png" />

- [x] **Outcome:** **POSITION_UNAVAILABLE** is **2** with the page’s message.

<a id="api-geolocation-example-04"></a>

### **Example 4: Error TIMEOUT**

- [x] Code **3** — `options.timeout` elapsed.
- [x] The snapshot’s getCurrentPosition uses a short timeout to make this likely in headless.

Sandbox: `code_sandbox/api-geolocation/error-timeout.html`

```html
case error.TIMEOUT:
  x.innerHTML = "The request to get user location timed out.";
```

<img alt="api-geolocation example 4 source" src="../code_sandbox/snaps/api-geolocation-04-code.png" />

<img alt="api-geolocation example 4 result" src="../code_sandbox/snaps/api-geolocation-04-result.png" />

- [x] **Outcome:** **TIMEOUT** is **3**.

<a id="api-geolocation-example-05"></a>

### **Example 5: Error UNKNOWN_ERROR**

- [x] Code **0** in the spec is unused; some docs still mention UNKNOWN_ERROR.
- [x] W3Schools `default` / `UNKNOWN_ERROR` branch: “An unknown error occurred.”

Sandbox: `code_sandbox/api-geolocation/error-unknown.html`

```html
case error.UNKNOWN_ERROR:
  x.innerHTML = "An unknown error occurred.";
```

<img alt="api-geolocation example 5 source" src="../code_sandbox/snaps/api-geolocation-05-code.png" />

<img alt="api-geolocation example 5 result" src="../code_sandbox/snaps/api-geolocation-05-result.png" />

- [x] **Outcome:** The unknown-error message is printed for completeness.

<a id="api-geolocation-example-06"></a>

### **Example 6: Displaying the result in a map URL**

- [x] Build a lat,lon string and plug it into a **static map** image URL.
- [x] The page uses Google Static Maps with **`YOUR_KEY`** — you must supply a real key; we do **not** call Google here.
- [x] The snapshot shows the URL shape with sample coordinates.

Sandbox: `code_sandbox/api-geolocation/map-url.html`

```html
let latlon = position.coords.latitude + "," + position.coords.longitude;
let img_url = "https://maps.googleapis.com/maps/api/staticmap?center="
  + latlon + "&zoom=14&size=400x300&sensor=false&key=YOUR_KEY";
```

<img alt="api-geolocation example 6 source" src="../code_sandbox/snaps/api-geolocation-06-code.png" />

<img alt="api-geolocation example 6 result" src="../code_sandbox/snaps/api-geolocation-06-result.png" />

- [x] **Outcome:** The constructed URL contains **center=59.9,10.7** and **YOUR_KEY** as on the page (not fetched).

<a id="api-geolocation-example-07"></a>

### **Example 7: coords.latitude (always returned)**

- [x] Always present on a success Position.
- [x] Decimal degrees.

Sandbox: `code_sandbox/api-geolocation/coords-latitude.html`

```html
position.coords.latitude
```

<img alt="api-geolocation example 7 source" src="../code_sandbox/snaps/api-geolocation-07-code.png" />

<img alt="api-geolocation example 7 result" src="../code_sandbox/snaps/api-geolocation-07-result.png" />

- [x] **Outcome:** A mock Position-like object prints latitude **59.9** so you see the property shape without needing GPS.

<a id="api-geolocation-example-08"></a>

### **Example 8: coords.longitude (always returned)**

- [x] Decimal degrees, always on success.

Sandbox: `code_sandbox/api-geolocation/coords-longitude.html`

```html
position.coords.longitude
```

<img alt="api-geolocation example 8 source" src="../code_sandbox/snaps/api-geolocation-08-code.png" />

<img alt="api-geolocation example 8 result" src="../code_sandbox/snaps/api-geolocation-08-result.png" />

- [x] **Outcome:** **longitude=10.7** on the mock coords.

<a id="api-geolocation-example-09"></a>

### **Example 9: coords.accuracy (always returned)**

- [x] Accuracy of the position in **meters** (radius).

Sandbox: `code_sandbox/api-geolocation/coords-accuracy.html`

```html
position.coords.accuracy
```

<img alt="api-geolocation example 9 source" src="../code_sandbox/snaps/api-geolocation-09-code.png" />

<img alt="api-geolocation example 9 result" src="../code_sandbox/snaps/api-geolocation-09-result.png" />

- [x] **Outcome:** **accuracy=20** (meters) on the mock.

<a id="api-geolocation-example-10"></a>

### **Example 10: coords.altitude (if available)**

- [x] Meters above mean sea level. May be **null**.

Sandbox: `code_sandbox/api-geolocation/coords-altitude.html`

```html
position.coords.altitude
```

<img alt="api-geolocation example 10 source" src="../code_sandbox/snaps/api-geolocation-10-code.png" />

<img alt="api-geolocation example 10 result" src="../code_sandbox/snaps/api-geolocation-10-result.png" />

- [x] **Outcome:** Mock **altitude=null** (typical for a laptop without a barometer).

<a id="api-geolocation-example-11"></a>

### **Example 11: coords.altitudeAccuracy (if available)**

- [x] Accuracy of altitude; often **null**.

Sandbox: `code_sandbox/api-geolocation/coords-altitude-accuracy.html`

```html
position.coords.altitudeAccuracy
```

<img alt="api-geolocation example 11 source" src="../code_sandbox/snaps/api-geolocation-11-code.png" />

<img alt="api-geolocation example 11 result" src="../code_sandbox/snaps/api-geolocation-11-result.png" />

- [x] **Outcome:** **altitudeAccuracy=null** on the mock.

<a id="api-geolocation-example-12"></a>

### **Example 12: coords.heading (if available)**

- [x] Degrees clockwise from **north**. Null if stationary/unknown.

Sandbox: `code_sandbox/api-geolocation/coords-heading.html`

```html
position.coords.heading
```

<img alt="api-geolocation example 12 source" src="../code_sandbox/snaps/api-geolocation-12-code.png" />

<img alt="api-geolocation example 12 result" src="../code_sandbox/snaps/api-geolocation-12-result.png" />

- [x] **Outcome:** **heading=null** when not moving.

<a id="api-geolocation-example-13"></a>

### **Example 13: coords.speed (if available)**

- [x] Meters per second. Null if unknown.

Sandbox: `code_sandbox/api-geolocation/coords-speed.html`

```html
position.coords.speed
```

<img alt="api-geolocation example 13 source" src="../code_sandbox/snaps/api-geolocation-13-code.png" />

<img alt="api-geolocation example 13 result" src="../code_sandbox/snaps/api-geolocation-13-result.png" />

- [x] **Outcome:** **speed=null** on the mock.

<a id="api-geolocation-example-14"></a>

### **Example 14: position.timestamp**

- [x] Time of the response. Listed as “returned if available”; in the spec it is on the Position object.

Sandbox: `code_sandbox/api-geolocation/timestamp.html`

```html
position.timestamp
```

<img alt="api-geolocation example 14 source" src="../code_sandbox/snaps/api-geolocation-14-code.png" />

<img alt="api-geolocation example 14 result" src="../code_sandbox/snaps/api-geolocation-14-result.png" />

- [x] **Outcome:** A `Date.now()`-style timestamp is a **number** of milliseconds.

<a id="api-geolocation-example-15"></a>

### **Example 15: watchPosition() — keep updating**

- [x] `watchPosition(success, error?, options?)` returns a **watch id** (number).
- [x] Like GPS in a car: it keeps calling success as the device moves.
- [x] Do not start a watch you never clear.

Sandbox: `code_sandbox/api-geolocation/watch.html`

```html
navigator.geolocation.watchPosition(showPosition)
```

<img alt="api-geolocation example 15 source" src="../code_sandbox/snaps/api-geolocation-15-code.png" />

<img alt="api-geolocation example 15 result" src="../code_sandbox/snaps/api-geolocation-15-result.png" />

- [x] **Outcome:** `typeof watchPosition` is **function**. We do not leave a watch running in the snapshot.

<a id="api-geolocation-example-16"></a>

### **Example 16: clearWatch(id) — stop watching**

- [x] `clearWatch(id)` stops that watch.
- [x] Pass the number `watchPosition` returned.

Sandbox: `code_sandbox/api-geolocation/clear-watch.html`

```html
navigator.geolocation.clearWatch(id)
```

<img alt="api-geolocation example 16 source" src="../code_sandbox/snaps/api-geolocation-16-code.png" />

<img alt="api-geolocation example 16 result" src="../code_sandbox/snaps/api-geolocation-16-result.png" />

- [x] **Outcome:** `typeof clearWatch` is **function**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/api-geolocation/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Which method gets a one-shot position?

<details>
<summary>Answer</summary>

- [x] **`getCurrentPosition`**.

</details>

### Question 2: Which properties are always on success?

<details>
<summary>Answer</summary>

- [x] **latitude, longitude, accuracy** (and typically **timestamp**).

</details>

### Question 3: What is PERMISSION_DENIED’s code?

<details>
<summary>Answer</summary>

- [x] **1**.

</details>

### Question 4: What is TIMEOUT’s code?

<details>
<summary>Answer</summary>

- [x] **3**.

</details>

### Question 5: What does `watchPosition` return?

<details>
<summary>Answer</summary>

- [x] A numeric **watch id**.

</details>

### Question 6: How do you stop a watch?

<details>
<summary>Answer</summary>

- [x] **`clearWatch(id)`**.

</details>

### Question 7: Does the map example work without an API key?

<details>
<summary>Answer</summary>

- [x] **No** — `YOUR_KEY` must be a real Google key (we did not call the service).

</details>

### Question 8: What units is `speed` in?

<details>
<summary>Answer</summary>

- [x] **Meters per second**.

</details>

### Question 9: What units is `heading` in?

<details>
<summary>Answer</summary>

- [x] **Degrees** clockwise from north.

</details>

### Question 10: Why might this fail in the snapshot?

<details>
<summary>Answer</summary>

- [x] **Permission**, **insecure origin**, or **timeout** — all are real API outcomes.

</details>


</details>

## Summary

Call getCurrentPosition with success and error callbacks. Read coords.latitude/longitude/accuracy. Use watchPosition only if you will clearWatch. Do not ship YOUR_KEY placeholders to Google.

## References

- [API Geolocation](https://www.w3schools.com/js/js_api_geolocation.asp)
- [MDN Geolocation.getCurrentPosition()](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition)
