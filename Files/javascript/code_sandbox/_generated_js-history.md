<details>
  <summary>JS History</summary>

## Introduction

The History API is Back/Forward (`back`, `forward`, `go`) plus SPA tools: `pushState`, `replaceState`, `state`, `popstate`, and `scrollRestoration`.

This section has **15** examples:

- [x] **Example 1:** history.back() — previous session entry [View](#js-history-example-01)
- [x] **Example 2:** history.forward() — next session entry [View](#js-history-example-02)
- [x] **Example 3:** history.go(-2) — two steps back [View](#js-history-example-03)
- [x] **Example 4:** history.go(1) — one step forward [View](#js-history-example-04)
- [x] **Example 5:** history.go(0) reloads the current page [View](#js-history-example-05)
- [x] **Example 6:** history.length — number of session entries [View](#js-history-example-06)
- [x] **Example 7:** history.state is null until pushState/replaceState [View](#js-history-example-07)
- [x] **Example 8:** history.pushState(state, "", url) [View](#js-history-example-08)
- [x] **Example 9:** pushState does not load a new page [View](#js-history-example-09)
- [x] **Example 10:** history.replaceState(state, "", url) [View](#js-history-example-10)
- [x] **Example 11:** replaceState does not load a new page [View](#js-history-example-11)
- [x] **Example 12:** popstate fires on Back/Forward [View](#js-history-example-12)
- [x] **Example 13:** popstate event.state [View](#js-history-example-13)
- [x] **Example 14:** Simple History API example (Home / About) [View](#js-history-example-14)
- [x] **Example 15:** history.scrollRestoration [View](#js-history-example-15)

## Detailed Explanation

- [x] `pushState` / `replaceState` do not load a document.
- [x] `popstate` fires on Back/Forward, not on pushState itself.
- [x] `state` is null until you store an object.

<a id="js-history-example-01"></a>

### **Example 1: history.back() — previous session entry**

- [x] `history.back()` is the same as the browser **Back** button.
- [x] It loads the previous **session history** entry (may be another site).
- [x] There is no previous page in this snapshot, so we do not call it (it would leave or no-op).
- [x] The button in the Tryit is `onclick="history.back()"`.

Sandbox: `code_sandbox/js-history/back.html`

```html
<button onclick="history.back()">Go Back</button>
```

<img alt="js-history example 1 source" src="./code_sandbox/snaps/js-history-01-code.png" />

<img alt="js-history example 1 result" src="./code_sandbox/snaps/js-history-01-result.png" />

- [x] **Outcome:** The **Go Back** button is in the page. `typeof history.back` is **function**; it is not invoked here.

<a id="js-history-example-02"></a>

### **Example 2: history.forward() — next session entry**

- [x] `history.forward()` is the **Forward** button.
- [x] It only works if the user already went Back (there is a “next” entry).
- [x] Equivalent to `history.go(1)`.

Sandbox: `code_sandbox/js-history/forward.html`

```html
<button onclick="history.forward()">Go Forward</button>
```

<img alt="js-history example 2 source" src="./code_sandbox/snaps/js-history-02-code.png" />

<img alt="js-history example 2 result" src="./code_sandbox/snaps/js-history-02-result.png" />

- [x] **Outcome:** **Go Forward** is wired to `history.forward`. The snapshot does not navigate away.

<a id="js-history-example-03"></a>

### **Example 3: history.go(-2) — two steps back**

- [x] `go(delta)` moves **relative** to the current entry.
- [x] `go(-2)` is “back two pages”.
- [x] If there are not enough entries, the call does nothing useful.

Sandbox: `code_sandbox/js-history/go-back-two.html`

```html
<button onclick="history.go(-2)">Go Back</button>
```

<img alt="js-history example 3 source" src="./code_sandbox/snaps/js-history-03-code.png" />

<img alt="js-history example 3 result" src="./code_sandbox/snaps/js-history-03-result.png" />

- [x] **Outcome:** The button would call **`history.go(-2)`**. Not clicked in the snapshot.

<a id="js-history-example-04"></a>

### **Example 4: history.go(1) — one step forward**

- [x] `go(1)` is the same as **`forward()`**.
- [x] Positive numbers go forward; negative go back.

Sandbox: `code_sandbox/js-history/go-forward-one.html`

```html
<button onclick="history.go(1)">Go Forward</button>
```

<img alt="js-history example 4 source" src="./code_sandbox/snaps/js-history-04-code.png" />

<img alt="js-history example 4 result" src="./code_sandbox/snaps/js-history-04-result.png" />

- [x] **Outcome:** The control is labeled **Go Forward** and would call `go(1)`.

<a id="js-history-example-05"></a>

### **Example 5: history.go(0) reloads the current page**

- [x] `go(0)` **reloads** the current entry.
- [x] `back()` ≡ `go(-1)`. `forward()` ≡ `go(1)`.
- [x] Do not call `go(0)` in a screenshot — the reload races the capture.
- [x] Prefer `location.reload()` when you mean reload.

Sandbox: `code_sandbox/js-history/go-zero.html`

```html
history.go(0) reloads the current page.
history.back() is equivalent to history.go(-1).
history.forward() is equivalent to history.go(1).
```

<img alt="js-history example 5 source" src="./code_sandbox/snaps/js-history-05-code.png" />

<img alt="js-history example 5 result" src="./code_sandbox/snaps/js-history-05-result.png" />

- [x] **Outcome:** The note is printed; **no reload** is performed.

<a id="js-history-example-06"></a>

### **Example 6: history.length — number of session entries**

- [x] `length` is how many entries are in **this tab’s** session history.
- [x] It is at least **1** (the current page).
- [x] You cannot read other tabs’ history (privacy).

Sandbox: `code_sandbox/js-history/length.html`

```html
let length = history.length;
```

<img alt="js-history example 6 source" src="./code_sandbox/snaps/js-history-06-code.png" />

<img alt="js-history example 6 result" src="./code_sandbox/snaps/js-history-06-result.png" />

- [x] **Outcome:** `history.length` is an integer **≥ 1** for this tab.

<a id="js-history-example-07"></a>

### **Example 7: history.state is null until pushState/replaceState**

- [x] `state` is the **data object** stored with the current history entry.
- [x] On a normal first load it is **`null`**.
- [x] It becomes an object after `pushState` or `replaceState`.

Sandbox: `code_sandbox/js-history/state-null.html`

```html
let state = history.state;
```

<img alt="js-history example 7 source" src="./code_sandbox/snaps/js-history-07-code.png" />

<img alt="js-history example 7 result" src="./code_sandbox/snaps/js-history-07-result.png" />

- [x] **Outcome:** On this fresh example page, `history.state` is **null**.

<a id="js-history-example-08"></a>

### **Example 8: history.pushState(state, "", url)**

- [x] `pushState(state, unused, url)` **adds** an entry without loading a document.
- [x] The second argument is unused (was `title`; pass `""`).
- [x] `url` must be **same-origin**. Here we use `?page=2`.
- [x] The page content does **not** change unless you update the DOM yourself.

Sandbox: `code_sandbox/js-history/push-state.html`

```html
let state = {name:"example", page: 2};
let url = "page2.html";
history.pushState(state, "", url);
```

<img alt="js-history example 8 source" src="./code_sandbox/snaps/js-history-08-code.png" />

<img alt="js-history example 8 result" src="./code_sandbox/snaps/js-history-08-result.png" />

- [x] **Outcome:** After `pushState`, `history.state.page` is **2** and the query/path reflects the new URL. The heading text is still this page — no load.

<a id="js-history-example-09"></a>

### **Example 9: pushState does not load a new page**

- [x] If you need new HTML from the server, set `location.href` (or `assign`).
- [x] `pushState` only updates **history + URL**. SPAs then render in JS.
- [x] W3Schools notes a separate `location.href = "page2.html"` if content should change.

Sandbox: `code_sandbox/js-history/push-no-load.html`

```html
history.pushState() method does not load a new page.
```

<img alt="js-history example 9 source" src="./code_sandbox/snaps/js-history-09-code.png" />

<img alt="js-history example 9 result" src="./code_sandbox/snaps/js-history-09-result.png" />

- [x] **Outcome:** `document.title` is unchanged after `pushState` — proof the document was not replaced.

<a id="js-history-example-10"></a>

### **Example 10: history.replaceState(state, "", url)**

- [x] `replaceState` **overwrites** the current entry — history length does not grow.
- [x] Useful to fix a URL without creating a Back step.
- [x] Same-origin rules still apply.

Sandbox: `code_sandbox/js-history/replace-state.html`

```html
let state = {name:"example", page: 2};
let url = "page2.html";
history.replaceState(state, "", url);
```

<img alt="js-history example 10 source" src="./code_sandbox/snaps/js-history-10-code.png" />

<img alt="js-history example 10 result" src="./code_sandbox/snaps/js-history-10-result.png" />

- [x] **Outcome:** `replaceState` sets `state.page` to **2**. Length does not increase because of this call.

<a id="js-history-example-11"></a>

### **Example 11: replaceState does not load a new page**

- [x] Like `pushState`, it only changes the **current** history slot.
- [x] You must still update the DOM if the UI should match the new URL.

Sandbox: `code_sandbox/js-history/replace-no-load.html`

```html
history.replaceState() method does not load a new page.
```

<img alt="js-history example 11 source" src="./code_sandbox/snaps/js-history-11-code.png" />

<img alt="js-history example 11 result" src="./code_sandbox/snaps/js-history-11-result.png" />

- [x] **Outcome:** The document is the same; only `history.state` / URL change.

<a id="js-history-example-12"></a>

### **Example 12: popstate fires on Back/Forward**

- [x] `popstate` runs when the **active** history entry changes via Back/Forward/`go`.
- [x] It does **not** fire for the `pushState`/`replaceState` call itself.
- [x] Listen on `window`.

Sandbox: `code_sandbox/js-history/popstate.html`

```html
window.addEventListener("popstate", function(event) {
  myDisplayer("Page changed");
});
```

<img alt="js-history example 12 source" src="./code_sandbox/snaps/js-history-12-code.png" />

<img alt="js-history example 12 result" src="./code_sandbox/snaps/js-history-12-result.png" />

- [x] **Outcome:** After `pushState` then `history.back()`, the listener runs and prints **Page changed**.

<a id="js-history-example-13"></a>

### **Example 13: popstate event.state**

- [x] The event’s **`state`** is the object you stored with `pushState`.
- [x] It can be `null` for entries that were never given state.
- [x] Use it to restore the SPA view.

Sandbox: `code_sandbox/js-history/popstate-state.html`

```html
window.addEventListener("popstate", function(event) {
  if (event.state) {
    myDisplayer(event.state.page);
  }
});
```

<img alt="js-history example 13 source" src="./code_sandbox/snaps/js-history-13-code.png" />

<img alt="js-history example 13 result" src="./code_sandbox/snaps/js-history-13-result.png" />

- [x] **Outcome:** Going back to the `about` state prints **about** from `event.state.page`.

<a id="js-history-example-14"></a>

### **Example 14: Simple History API example (Home / About)**

- [x] Buttons call `showPage`, which updates the paragraph **and** `pushState`.
- [x] `popstate` restores the paragraph when the user hits Back.
- [x] This is the SPA pattern in miniature.

Sandbox: `code_sandbox/js-history/spa-example.html`

```html
<button onclick="showPage('home')">Home</button>
<button onclick="showPage('about')">About</button>
<p id="out">Home</p>
<script>
function showPage(page) {
  myDisplayer(page);
  history.pushState({page: page}, "", "?page=" + page);
}
window.addEventListener("popstate", function(event) {
  if (event.state) { myDisplayer(event.state.page); }
});
</script>
```

<img alt="js-history example 14 source" src="./code_sandbox/snaps/js-history-14-code.png" />

<img alt="js-history example 14 result" src="./code_sandbox/snaps/js-history-14-result.png" />

- [x] **Outcome:** After clicking **About**, the paragraph is **about** and the URL has `?page=about`.

<a id="js-history-example-15"></a>

### **Example 15: history.scrollRestoration**

- [x] `scrollRestoration` is **`"auto"`** (browser restores scroll) or **`"manual"`** (you restore it).
- [x] SPAs often set **`manual`** so Back does not jump to a leftover scroll position.
- [x] W3Schools: `history.scrollRestoration = "manual"`.

Sandbox: `code_sandbox/js-history/scroll-restoration.html`

```html
history.scrollRestoration = "manual";
```

<img alt="js-history example 15 source" src="./code_sandbox/snaps/js-history-15-code.png" />

<img alt="js-history example 15 result" src="./code_sandbox/snaps/js-history-15-result.png" />

- [x] **Outcome:** After assignment, `scrollRestoration` is **manual**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-history/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `history.back()` equal to?

<details>
<summary>Answer</summary>

- [x] The browser **Back** button, and `history.go(-1)`.

</details>

### Question 2: What does `go(0)` do?

<details>
<summary>Answer</summary>

- [x] **Reloads** the current page.

</details>

### Question 3: Does `pushState` fetch new HTML?

<details>
<summary>Answer</summary>

- [x] **No** — it only adds a history entry and may change the URL.

</details>

### Question 4: How is `replaceState` different?

<details>
<summary>Answer</summary>

- [x] It **changes the current** entry and does not add one.

</details>

### Question 5: When is `history.state` null?

<details>
<summary>Answer</summary>

- [x] Until you call **`pushState` or `replaceState`** (and for entries without state).

</details>

### Question 6: When does `popstate` fire?

<details>
<summary>Answer</summary>

- [x] On **Back / Forward / go**, not on the `pushState` call itself.

</details>

### Question 7: What is `event.state`?

<details>
<summary>Answer</summary>

- [x] The **object** you stored with that history entry.

</details>

### Question 8: What does `length` count?

<details>
<summary>Answer</summary>

- [x] Entries in **this tab’s** session history.

</details>

### Question 9: Why set `scrollRestoration = "manual"`?

<details>
<summary>Answer</summary>

- [x] So **you** control scroll when the user navigates history (common in SPAs).

</details>

### Question 10: Must `pushState` URLs be same-origin?

<details>
<summary>Answer</summary>

- [x] **Yes**.

</details>

### Question 11: In the Home/About demo, who updates the paragraph on Back?

<details>
<summary>Answer</summary>

- [x] The **`popstate`** listener reading `event.state.page`.

</details>


</details>

## Summary

Use back/forward/go for real navigation. Use pushState + popstate when the URL should change without a reload, and update the DOM yourself.

## References

- [JS History](https://www.w3schools.com/js/js_window_history.asp)
- [MDN History](https://developer.mozilla.org/en-US/docs/Web/API/History)

</details>
