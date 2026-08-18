<details>
  <summary>JS Performance</summary>

## Introduction

Speed tips from the page: cache array length outside the loop, cache DOM lookups, keep the DOM small, skip variables you never reuse, delay script loading (bottom of body, defer, or inject on load), and never use with (illegal in strict mode). Extra spaces do not matter to the CPU in small scripts; DOM and network usually dominate.

This section has **7** examples:

- [x] **Example 1:** Bad: arr.length read every iteration [View](#js-performance-example-01)
- [x] **Example 2:** Better: cache arr.length outside the comparison [View](#js-performance-example-02)
- [x] **Example 3:** Cache getElementById instead of searching the DOM twice [View](#js-performance-example-03)
- [x] **Example 4:** Keep the DOM small — search is cheaper [View](#js-performance-example-04)
- [x] **Example 5:** Don't create a variable you never reuse [View](#js-performance-example-05)
- [x] **Example 6:** Delay JS: put scripts at the bottom, or defer, or onload inject [View](#js-performance-example-06)
- [x] **Example 7:** Avoid with — slow, clutters scope, illegal in strict mode [View](#js-performance-example-07)

## Detailed Explanation

- [x] Hoist **`arr.length`**. Cache **`getElementById`**.
- [x] Fewer DOM nodes → faster search/render.
- [x] Load JS **late** (`defer` / bottom / onload inject).
- [x] **No `with`.** Strict mode **SyntaxError**.

<a id="js-performance-example-01"></a>

### **Example 1: Bad: arr.length read every iteration**

- [x] Every statement in a loop runs **each** iteration — including `i < arr.length`.
- [x] That **works**, but re-reads **`.length`** every time.

Sandbox: `code_sandbox/js-performance/loop-length-inside.html`

```javascript
for (let i = 0; i < arr.length; i++) {
  // ...
}
```

<img alt="js-performance example 1 source" src="./code_sandbox/snaps/js-performance-01-code.png" />

<img alt="js-performance example 1 result" src="./code_sandbox/snaps/js-performance-01-result.png" />

- [x] **Outcome:** With 4 items, the loop still visits **0..3**. Result **sum** is **10** (1+2+3+4).

<a id="js-performance-example-02"></a>

### **Example 2: Better: cache arr.length outside the comparison**

- [x] `let l = arr.length;` then `i < l` — **length** is read **once**.
- [x] Same results; fewer property lookups (the page’s performance tip).

Sandbox: `code_sandbox/js-performance/loop-length-cached.html`

```javascript
let l = arr.length;
for (let i = 0; i < l; i++) {
  // ...
}
```

<img alt="js-performance example 2 source" src="./code_sandbox/snaps/js-performance-02-code.png" />

<img alt="js-performance example 2 result" src="./code_sandbox/snaps/js-performance-02-result.png" />

- [x] **Outcome:** **sum** is still **10**. **l** is **4**.

<a id="js-performance-example-03"></a>

### **Example 3: Cache getElementById instead of searching the DOM twice**

- [x] **DOM access is slow** compared with plain JS.
- [x] If you need the node **several times**, store it: `const obj = document.getElementById("demo")`.

Sandbox: `code_sandbox/js-performance/reduce-dom-access.html`

```javascript
const obj = document.getElementById("demo");
obj.innerHTML = "Hello";
```

<img alt="js-performance example 3 source" src="./code_sandbox/snaps/js-performance-03-code.png" />

<img alt="js-performance example 3 result" src="./code_sandbox/snaps/js-performance-03-result.png" />

- [x] **Outcome:** The paragraph reads **Hello** after **one** lookup.

<a id="js-performance-example-04"></a>

### **Example 4: Keep the DOM small — search is cheaper**

- [x] Fewer elements → faster **load**, **render**, and **`getElementsByTagName` / query**.
- [x] This demo counts **p** nodes in a tiny vs larger subtree.

Sandbox: `code_sandbox/js-performance/reduce-dom-size.html`

```javascript
document.getElementsByTagName("p").length
```

<img alt="js-performance example 4 source" src="./code_sandbox/snaps/js-performance-04-code.png" />

<img alt="js-performance example 4 result" src="./code_sandbox/snaps/js-performance-04-result.png" />

- [x] **Outcome:** **small** subtree has **2** paragraphs. **large** has **20**. Searching the large tree visits more nodes.

<a id="js-performance-example-05"></a>

### **Example 5: Don't create a variable you never reuse**

- [x] If you only use `fullName` once, write the expression **in place**.

Sandbox: `code_sandbox/js-performance/avoid-extra-variable.html`

```javascript
let fullName = firstName + " " + lastName;
document.getElementById("demo").innerHTML = fullName;
// better:
document.getElementById("demo").innerHTML = firstName + " " + lastName;
```

<img alt="js-performance example 5 source" src="./code_sandbox/snaps/js-performance-05-code.png" />

<img alt="js-performance example 5 result" src="./code_sandbox/snaps/js-performance-05-result.png" />

- [x] **Outcome:** Both paths write **"Ada Lovelace"**. The second skips the extra binding.

<a id="js-performance-example-06"></a>

### **Example 6: Delay JS: put scripts at the bottom, or defer, or onload inject**

- [x] A script at the **bottom of `<body>`** lets HTML parse first.
- [x] **`defer`** (external scripts) runs after parse. The page writes `defer="true"`; HTML boolean **`defer`** is enough (`<script src="..." defer>`).
- [x] Or inject after load: `window.onload = function () { const el = document.createElement("script"); el.src = "myScript.js"; document.body.appendChild(el); };`
- [x] While a script downloads, the browser may **block** other work. HTTP/1.1 also limited parallel downloads (the page still mentions **two** parallel components — modern HTTP/2+ is more parallel).

Sandbox: `code_sandbox/js-performance/defer-script.html`

```javascript
window.onload = function() {
  const element = document.createElement("script");
  element.src = "myScript.js";
  document.body.appendChild(element);
};
```

<img alt="js-performance example 6 source" src="./code_sandbox/snaps/js-performance-06-code.png" />

<img alt="js-performance example 6 result" src="./code_sandbox/snaps/js-performance-06-result.png" />

- [x] **Outcome:** This page already loaded, so the demo **appends** a tiny inline script immediately and records **injected**. Same idea as onload injection.

<a id="js-performance-example-07"></a>

### **Example 7: Avoid with — slow, clutters scope, illegal in strict mode**

- [x] **`with`** is a performance and **scope** hazard.
- [x] In **strict mode** it is a **SyntaxError**.

Sandbox: `code_sandbox/js-performance/avoid-with.html`

```javascript
with (Math) {
  x = cos(0);
}
```

<img alt="js-performance example 7 source" src="./code_sandbox/snaps/js-performance-07-code.png" />

<img alt="js-performance example 7 result" src="./code_sandbox/snaps/js-performance-07-result.png" />

- [x] **Outcome:** Sloppy `with (Math) { cos(0) }` is **1**. Strict `with` is **SyntaxError: Strict mode code may not include a with statement**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-performance/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Why cache `arr.length`?

<details>
<summary>Answer</summary>

- [x] So each iteration does not **re-read** the property.

</details>

### Question 2: Does caching length change 1+2+3+4?

<details>
<summary>Answer</summary>

- [x] **No.** **sum** is still **10**.

</details>

### Question 3: How should you set innerHTML twice on #demo?

<details>
<summary>Answer</summary>

- [x] **One** `getElementById`, reuse the **node**.

</details>

### Question 4: Why a small DOM?

<details>
<summary>Answer</summary>

- [x] Faster **load**, **render**, and **tag searches**.

</details>

### Question 5: Need `fullName` if you print it once?

<details>
<summary>Answer</summary>

- [x] **No.** Inline `firstName + " " + lastName`.

</details>

### Question 6: What does `defer` do?

<details>
<summary>Answer</summary>

- [x] Runs the **external** script **after HTML parse**.

</details>

### Question 7: Is `with` allowed in strict mode?

<details>
<summary>Answer</summary>

- [x] **No.** **SyntaxError: Strict mode code may not include a with statement**.

</details>

### Question 8: Sloppy `with (Math) { cos(0) }`?

<details>
<summary>Answer</summary>

- [x] **1** — and you still should **not** write this.

</details>


</details>

## Summary

Cache lengths and DOM nodes, keep markup lean, load scripts late, and avoid with. Measure real bottlenecks (DOM, network) before micro-optimizing arithmetic.

## References

- [JS Performance (W3Schools)](https://www.w3schools.com/js/js_performance.asp)
- [MDN: <script> defer](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#defer)
- [MDN: with](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with)
- [MDN: Document.getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)

</details>
