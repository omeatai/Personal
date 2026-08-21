# HTML URL Encode

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

A **URL** is a web address. This chapter explains URL **syntax**, common **schemes**, and **URL encoding**: non-ASCII characters become `%` plus hex, and spaces become `+` or `%20`.

This section has **1** example:

- [x] **Example 1:** Main document [View](#html-url-encode-example-01)

## Detailed Explanation

- [x] **URL = web address** — words (`w3schools.com`) or an IP (`192.68.20.50`). Names are easier to remember.
- [x] Browsers request pages with a URL. Example: `https://www.w3schools.com/html/default.asp`.
- [x] **Syntax:** `scheme://prefix.domain:port/path/filename`
  - **scheme** — service type (`http` or `https`)
  - **prefix** — domain prefix (default `www` for http)
  - **domain** — name like `w3schools.com`
  - **port** — host port (default **80** for http)
  - **path** — path on the server (omit = site root)
  - **filename** — document or resource name
- [x] **Common schemes**

| Scheme  | Short for                          | Used for                        |
| ------- | ---------------------------------- | ------------------------------- |
| `http`  | HyperText Transfer Protocol        | Common web pages. Not encrypted |
| `https` | Secure HyperText Transfer Protocol | Secure web pages. Encrypted     |
| `ftp`   | File Transfer Protocol             | Downloading or uploading files  |
| `file`  |                                    | A file on your computer         |

- [x] **URL encoding**
  - URLs can only be sent using the **ASCII** character set. Non-ASCII must be converted.
  - Encoding replaces non-ASCII with **`%` + hexadecimal digits**.
  - URLs cannot contain spaces: a space becomes **`+`** or **`%20`**.
- [x] **Try It Yourself:** a form `GET`s the input; the browser encodes it before the request. After Submit, the query string shows `+` / `%20` (and UTF-8 sequences such as `%E2%82%AC` for €).
- [x] **ASCII encoding examples** (page charset is UTF-8 by default in HTML5)

| Character | From Windows-1252 | From UTF-8  |
| --------- | ----------------- | ----------- |
| €         | `%80`             | `%E2%82%AC` |
| £         | `%A3`             | `%C2%A3`    |
| ©         | `%A9`             | `%C2%A9`    |
| ®         | `%AE`             | `%C2%AE`    |
| À         | `%C0`             | `%C3%80`    |
| Á         | `%C1`             | `%C3%81`    |
| Â         | `%C2`             | `%C3%82`    |
| Ã         | `%C3`             | `%C3%83`    |
| Ä         | `%C4`             | `%C3%84`    |
| Å         | `%C5`             | `%C3%85`    |

<a id="html-url-encode-example-01"></a>

### **Example 1: Main document**

- [x] This example runs the tested markup in `code_sandbox/html-url-encode/index.html`.

Sandbox: `code_sandbox/html-url-encode/index.html`

```html
<p>Example URL: https://www.w3schools.com/html/default.asp</p>
<p>Syntax: scheme://prefix.domain:port/path/filename</p>
<p>Spaces become + or %20. Euro in UTF-8 is %E2%82%AC.</p>
<form action="" method="get">
  <label>Try It Yourself: <input name="text" value="Hello World" /></label>
  <button type="submit">Submit</button>
</form>
```

<img alt="html-url-encode source" src="../code_sandbox/snaps/html-url-encode-code.png" />

<img alt="html-url-encode result" src="../code_sandbox/snaps/html-url-encode-result.png" />

- [x] **Outcome:** the browser shows **Example URL: https://www.w3schools.com/html/default.asp**, **Syntax: scheme://prefix.domain:port/path/filename**, **Spaces become + or %20. Euro in UTF-8 is %E2%82%AC.**, **Try It Yourself: Submit**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-url-encode/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a URL?

<details>
<summary>Answer</summary>

- [x] Another word for a **web address**.
- [x] Browsers use it to request a page from a server.

</details>

### Question 2: What is the URL syntax pattern?

<details>
<summary>Answer</summary>

- [x] `scheme://prefix.domain:port/path/filename`.

</details>

### Question 3: What is the difference between `http` and `https`?

<details>
<summary>Answer</summary>

- [x] `http` — common web pages, **not encrypted**.
- [x] `https` — secure web pages, **encrypted**.

</details>

### Question 4: Why encode URLs?

<details>
<summary>Answer</summary>

- [x] URLs may only use the **ASCII** character set.
- [x] Non-ASCII characters are replaced with `%` plus hex digits.

</details>

### Question 5: How is a space encoded in a URL?

<details>
<summary>Answer</summary>

- [x] As a plus (`+`) or as `%20`.

</details>

### Question 6: How is € encoded in UTF-8 vs Windows-1252?

<details>
<summary>Answer</summary>

- [x] UTF-8: `%E2%82%AC`.
- [x] Windows-1252: `%80`.

</details>

</details>

## Summary

A URL is `scheme://prefix.domain:port/path/filename`. Use `https` for encrypted pages. Encode non-ASCII as `%HH` and spaces as `+` or `%20`; the encoding depends on the page charset (HTML5 default: UTF-8).

## References

- [HTML URL Encoding (W3Schools)](https://www.w3schools.com/html/html_urlencode.asp)
- [URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp)
- [MDN: URLs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)
- [MDN: `encodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
