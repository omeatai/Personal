# JS Navigator

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

`navigator` reports cookies, language, and online state. Most of the old “what browser is this?” properties (`appName`, `userAgent`, `javaEnabled`, …) are compatibility lies — the page warns you on each one.

This section has **10** examples:

- [x] **Example 1:** navigator.cookieEnabled [View](#js-navigator-example-01)
- [x] **Example 2:** navigator.language — browser language [View](#js-navigator-example-02)
- [x] **Example 3:** navigator.onLine — is the browser online? [View](#js-navigator-example-03)
- [x] **Example 4:** navigator.appName — application name (do not trust) [View](#js-navigator-example-04)
- [x] **Example 5:** navigator.appCodeName — code name (do not trust) [View](#js-navigator-example-05)
- [x] **Example 6:** navigator.product — engine product (do not trust) [View](#js-navigator-example-06)
- [x] **Example 7:** navigator.appVersion — version string (do not trust) [View](#js-navigator-example-07)
- [x] **Example 8:** navigator.userAgent — UA header (do not trust) [View](#js-navigator-example-08)
- [x] **Example 9:** navigator.platform — OS/platform (do not trust) [View](#js-navigator-example-09)
- [x] **Example 10:** navigator.javaEnabled() always false [View](#js-navigator-example-10)

## Detailed Explanation

- [x] Useful-ish: cookieEnabled, language, onLine.
- [x] Do not sniff appName / appCodeName / product / appVersion / userAgent / platform.
- [x] javaEnabled() is always false.

<a id="js-navigator-example-01"></a>

### **Example 1: navigator.cookieEnabled**

- [x] `navigator` describes the **browser / user agent**.
- [x] `cookieEnabled` is **true** if cookies are enabled.
- [x] It does not tell you whether *your* cookie was stored — only the preference.
- [x] Can be written `window.navigator` or `navigator`.

Sandbox: `code_sandbox/js-navigator/cookie-enabled.html`

```html
document.getElementById("demo").innerHTML =
  "cookiesEnabled is " + navigator.cookieEnabled;
```

<img alt="js-navigator example 1 source" src="../code_sandbox/snaps/js-navigator-01-code.png" />

<img alt="js-navigator example 1 result" src="../code_sandbox/snaps/js-navigator-01-result.png" />

- [x] **Outcome:** **cookiesEnabled is true** (or false if cookies are off in this browser).

<a id="js-navigator-example-02"></a>

### **Example 2: navigator.language — browser language**

- [x] `language` is a BCP 47 tag such as `en-US` or `en`.
- [x] It is the UI/preferred language, not the page’s `<html lang>`.

Sandbox: `code_sandbox/js-navigator/language.html`

```html
document.getElementById("demo").innerHTML = navigator.language;
```

<img alt="js-navigator example 2 source" src="../code_sandbox/snaps/js-navigator-02-code.png" />

<img alt="js-navigator example 2 result" src="../code_sandbox/snaps/js-navigator-02-result.png" />

- [x] **Outcome:** The page prints the browser language tag (for example **en-US**).

<a id="js-navigator-example-03"></a>

### **Example 3: navigator.onLine — is the browser online?**

- [x] `onLine` is **true** if the browser thinks it has a network.
- [x] It can be **wrong** (captive portal, “online” but no internet).
- [x] Listen to `window` events `online` / `offline` for changes.

Sandbox: `code_sandbox/js-navigator/online.html`

```html
document.getElementById("demo").innerHTML = navigator.onLine;
```

<img alt="js-navigator example 3 source" src="../code_sandbox/snaps/js-navigator-03-code.png" />

<img alt="js-navigator example 3 result" src="../code_sandbox/snaps/js-navigator-03-result.png" />

- [x] **Outcome:** `navigator.onLine` is **true** or **false** as a boolean (printed as such).

<a id="js-navigator-example-04"></a>

### **Example 4: navigator.appName — application name (do not trust)**

- [x] `appName` historically returned the browser product name.
- [x] **Warning (W3Schools + MDN):** it is unreliable. Chrome/Firefox often report **`Netscape`** for compatibility.
- [x] Do not use it for feature detection.

Sandbox: `code_sandbox/js-navigator/app-name.html`

```html
document.getElementById("demo").innerHTML =
  "navigator.appName is " + navigator.appName;
```

<img alt="js-navigator example 4 source" src="../code_sandbox/snaps/js-navigator-04-code.png" />

<img alt="js-navigator example 4 result" src="../code_sandbox/snaps/js-navigator-04-result.png" />

- [x] **Outcome:** **navigator.appName is** typically **Netscape** even in Chrome — which is why the page warns you.

<a id="js-navigator-example-05"></a>

### **Example 5: navigator.appCodeName — code name (do not trust)**

- [x] `appCodeName` is another frozen compatibility string, usually **`Mozilla`**.
- [x] The page warns: do not use it to identify the browser.

Sandbox: `code_sandbox/js-navigator/app-code-name.html`

```html
document.getElementById("demo").innerHTML =
  "navigator.appCodeName is " + navigator.appCodeName;
```

<img alt="js-navigator example 5 source" src="../code_sandbox/snaps/js-navigator-05-code.png" />

<img alt="js-navigator example 5 result" src="../code_sandbox/snaps/js-navigator-05-result.png" />

- [x] **Outcome:** **navigator.appCodeName is Mozilla** on almost every modern engine.

<a id="js-navigator-example-06"></a>

### **Example 6: navigator.product — engine product (do not trust)**

- [x] `product` is supposed to be the engine name; it is usually **`Gecko`** even in Chromium.
- [x] Same warning: **not** a real browser sniff.

Sandbox: `code_sandbox/js-navigator/product.html`

```html
document.getElementById("demo").innerHTML =
  "navigator.product is " + navigator.product;
```

<img alt="js-navigator example 6 source" src="../code_sandbox/snaps/js-navigator-06-code.png" />

<img alt="js-navigator example 6 result" src="../code_sandbox/snaps/js-navigator-06-result.png" />

- [x] **Outcome:** **navigator.product is Gecko** on this engine (compatibility value).

<a id="js-navigator-example-07"></a>

### **Example 7: navigator.appVersion — version string (do not trust)**

- [x] `appVersion` is a long compatibility string, not a clean version number.
- [x] The page warns it does **not** return the correct browser version.
- [x] Use feature detection, not this string.

Sandbox: `code_sandbox/js-navigator/app-version.html`

```html
document.getElementById("demo").innerHTML = navigator.appVersion;
```

<img alt="js-navigator example 7 source" src="../code_sandbox/snaps/js-navigator-07-code.png" />

<img alt="js-navigator example 7 result" src="../code_sandbox/snaps/js-navigator-07-result.png" />

- [x] **Outcome:** `appVersion` prints a long UA-like string; do not parse it as “the version”.

<a id="js-navigator-example-08"></a>

### **Example 8: navigator.userAgent — UA header (do not trust)**

- [x] `userAgent` is what the browser sends as **User-Agent**.
- [x] It is spoofable, frozen in places, and a poor way to detect features.
- [x] The page still shows it because many tutorials mention it — then warns you.

Sandbox: `code_sandbox/js-navigator/user-agent.html`

```html
document.getElementById("demo").innerHTML = navigator.userAgent;
```

<img alt="js-navigator example 8 source" src="../code_sandbox/snaps/js-navigator-08-code.png" />

<img alt="js-navigator example 8 result" src="../code_sandbox/snaps/js-navigator-08-result.png" />

- [x] **Outcome:** The full user-agent string is printed. Treat it as **unreliable** for branching.

<a id="js-navigator-example-09"></a>

### **Example 9: navigator.platform — OS/platform (do not trust)**

- [x] `platform` was meant to be the OS (e.g. `Win32`).
- [x] The page warns it is **not** correct in all browsers (and some lie for privacy).
- [x] `userAgentData.platform` (where supported) is the newer hint — still not for capability checks.

Sandbox: `code_sandbox/js-navigator/platform.html`

```html
document.getElementById("demo").innerHTML = navigator.platform;
```

<img alt="js-navigator example 9 source" src="../code_sandbox/snaps/js-navigator-09-code.png" />

<img alt="js-navigator example 9 result" src="../code_sandbox/snaps/js-navigator-09-result.png" />

- [x] **Outcome:** `platform` prints a string such as **Win32**. Do not use it as a hard OS check.

<a id="js-navigator-example-10"></a>

### **Example 10: navigator.javaEnabled() always false**

- [x] `javaEnabled()` used to report whether **Java** (the plugin) was on.
- [x] W3Schools warning: it **always returns false** now — the plugin is gone.
- [x] Calling it is harmless; do not build logic on it.

Sandbox: `code_sandbox/js-navigator/java-enabled.html`

```html
document.getElementById("demo").innerHTML = navigator.javaEnabled();
```

<img alt="js-navigator example 10 source" src="../code_sandbox/snaps/js-navigator-10-code.png" />

<img alt="js-navigator example 10 result" src="../code_sandbox/snaps/js-navigator-10-result.png" />

- [x] **Outcome:** `javaEnabled()` returns **false**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-navigator/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you know if cookies are enabled?

<details>
<summary>Answer</summary>

- [x] **`navigator.cookieEnabled`** (boolean).

</details>

### Question 2: What does `language` return?

<details>
<summary>Answer</summary>

- [x] A **language tag** such as `en-US`.

</details>

### Question 3: Is `onLine` a perfect network test?

<details>
<summary>Answer</summary>

- [x] **No** — it is the browser’s guess.

</details>

### Question 4: Why is `appName` useless?

<details>
<summary>Answer</summary>

- [x] Engines lie and often report **Netscape**.

</details>

### Question 5: What is a typical `appCodeName`?

<details>
<summary>Answer</summary>

- [x] **Mozilla**.

</details>

### Question 6: What is a typical `product`?

<details>
<summary>Answer</summary>

- [x] **Gecko** (even in Chrome).

</details>

### Question 7: Should you parse `userAgent` to detect Chrome?

<details>
<summary>Answer</summary>

- [x] **No** — use **feature detection**.

</details>

### Question 8: What does `javaEnabled()` return today?

<details>
<summary>Answer</summary>

- [x] Always **false**.

</details>

### Question 9: Can you omit `window.`?

<details>
<summary>Answer</summary>

- [x] **Yes** — `navigator` is a `window` property.

</details>

### Question 10: Name two navigator properties that are still somewhat useful.

<details>
<summary>Answer</summary>

- [x] **`cookieEnabled`**, **`language`**, **`onLine`** (with caveats).

</details>


</details>

## Summary

Trust cookieEnabled, language, and onLine (with caution). Ignore the legacy sniff properties and javaEnabled(). Detect features, not browsers.

## References

- [JS Navigator](https://www.w3schools.com/js/js_window_navigator.asp)
- [MDN Navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator)
