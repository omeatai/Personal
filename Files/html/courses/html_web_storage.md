# HTML Web Storage

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

**Web Storage** keeps key/value data in the browser. It is **more secure** than cookies, **at least 5MB**, and is **never sent to the server**. This chapter covers **`localStorage`** (no expiry) and **`sessionStorage`** (one tab session).

This section has **3** examples:

- [x] **Example 1:** Click counter [View](#html-web-storage-example-01)
- [x] **Example 2:** setItem [View](#html-web-storage-example-02)
- [x] **Example 3:** sessionStorage [View](#html-web-storage-example-03)

## Detailed Explanation

- [x] **Per origin** (domain + protocol). All pages of that origin share the same store.
- [x] **`window.localStorage`** — data **survives** closing the tab.
- [x] **`window.sessionStorage`** — data is **deleted** when that tab closes.
- [x] **Feature detect:** `typeof(Storage) !== "undefined"`.

<a id="html-web-storage-example-01"></a>

### **Example 1: Click counter**

- [x] **Click counter (`localStorage.clickcount`)**
  - Convert with `Number(...)` then add 1.
  - Sandbox: `index.html`.

Sandbox: `code_sandbox/html-web-storage/index.html`

```javascript
if (localStorage.clickcount) {
  localStorage.clickcount = Number(localStorage.clickcount) + 1;
} else {
  localStorage.clickcount = 1;
}
```

<img alt="html-web-storage counter source" src="../code_sandbox/snaps/html-web-storage-code.png" />

<img alt="html-web-storage localStorage counter result" src="../code_sandbox/snaps/html-web-storage-result.png" />

- [x] **Outcome:** the browser shows **if (localStorage.clickcount) { localStorage.clickcount = Number(localStorage.clickcount) + 1; } else { localStorage.clickcount = 1; }**.

<a id="html-web-storage-example-02"></a>

### **Example 2: setItem**

- [x] **setItem / getItem**
  - `localStorage.setItem("lastname", "Smith")` and `bgcolor` yellow.
  - Values are always **strings** — convert when you need a number.
  - Remove: `localStorage.removeItem("lastname")`.

Sandbox: `code_sandbox/html-web-storage/names.html`

```javascript
localStorage.setItem("lastname", "Smith");
localStorage.setItem("bgcolor", "yellow");
x.innerHTML = localStorage.getItem("lastname");
```

<img alt="html-web-storage setItem source" src="../code_sandbox/snaps/html-web-storage-01-code.png" />

<img alt="html-web-storage names result" src="../code_sandbox/snaps/html-web-storage-01-result.png" />

- [x] **Outcome:** the browser shows **localStorage.setItem("lastname", "Smith"); localStorage.setItem("bgcolor", "yellow"); x.innerHTML = localStorage.getItem("lastname");**.

<a id="html-web-storage-example-03"></a>

### **Example 3: sessionStorage**

- [x] **sessionStorage counter** — same idea; count is “in this session”.
  - Sandbox: `session.html`.

Sandbox: `code_sandbox/html-web-storage/session.html`

```javascript
sessionStorage.clickcount = Number(sessionStorage.clickcount) + 1;
```

<img alt="html-web-storage session source" src="../code_sandbox/snaps/html-web-storage-02-code.png" />

<img alt="html-web-storage sessionStorage counter result" src="../code_sandbox/snaps/html-web-storage-02-result.png" />

- [x] **Outcome:** the browser shows **sessionStorage.clickcount = Number(sessionStorage.clickcount)+1;**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-web-storage/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How is web storage better than cookies here?

<details>
<summary>Answer</summary>

- [x] **Larger** (at least **5MB**).
- [x] **Never transferred** to the server with every request.

</details>

### Question 2: localStorage vs sessionStorage?

<details>
<summary>Answer</summary>

- [x] localStorage: **no expiry** (survives tab close).
- [x] sessionStorage: **one tab session**.

</details>

### Question 3: How do you store and read a pair?

<details>
<summary>Answer</summary>

- [x] `setItem(name, value)` and `getItem(name)`.
- [x] Values are **strings**.

</details>

### Question 4: How do you delete one item?

<details>
<summary>Answer</summary>

- [x] `localStorage.removeItem("lastname")`.

</details>

</details>

## Summary

Web storage is per-origin key/value data. localStorage lasts; sessionStorage dies with the tab. Detect `Storage`, use setItem/getItem, and convert strings to numbers when counting.

## References

- [HTML Web Storage API (W3Schools)](https://www.w3schools.com/html/html5_webstorage.asp)
- [MDN: Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)
- [MDN: `Window.localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
