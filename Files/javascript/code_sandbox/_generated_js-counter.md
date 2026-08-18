<details>
  <summary>JS Counter</summary>

## Introduction

Build a localStorage counter with five onclick buttons: increase, decrease, reset, save, and load. count is a number in memory; updateCount writes it to #count. Save stores a string; Load converts with Number. The first Tryit can go negative. Exercises start at 10, block decrease below 0, and call loadCount when the page opens.

This section has **11** examples:

- [x] **Example 1:** Full Tryit: + − Reset Save Load [View](#js-counter-example-01)
- [x] **Example 2:** HTML: #count and five onclick buttons [View](#js-counter-example-02)
- [x] **Example 3:** let count = 0 and updateCount() [View](#js-counter-example-03)
- [x] **Example 4:** increaseCount() — count++ then updateCount() [View](#js-counter-example-04)
- [x] **Example 5:** decreaseCount() — count-- then updateCount() [View](#js-counter-example-05)
- [x] **Example 6:** resetCount() — count = 0 [View](#js-counter-example-06)
- [x] **Example 7:** saveCount() — localStorage.setItem("count", count) [View](#js-counter-example-07)
- [x] **Example 8:** loadCount() — getItem + Number(saved) [View](#js-counter-example-08)
- [x] **Example 9:** Exercise 1: start at 10 instead of 0 [View](#js-counter-example-09)
- [x] **Example 10:** Exercise 2: do not go below 0 [View](#js-counter-example-10)
- [x] **Example 11:** Exercise 3 + solutions: loadCount() when the page opens [View](#js-counter-example-11)

## Detailed Explanation

- [x] **onclick** attributes call **increaseCount / decreaseCount / resetCount / saveCount / loadCount**.
- [x] **localStorage** stores **text**. Use **`Number(saved)`** on load. Skip if **`getItem` is null**.
- [x] Exercises: start **10**, **no negatives**, **auto-load** (function declarations are hoisted).

<a id="js-counter-example-01"></a>

### **Example 1: Full Tryit: + − Reset Save Load**

- [x] The Tryit is a **counter** with five **`onclick`** buttons: **+**, **−**, **Reset**, **Save**, **Load**.
- [x] **`count`** is a number. **`updateCount()`** writes it to **`#count`**.
- [x] **Save** uses **`localStorage.setItem("count", count)`**. Values are stored as **text**.
- [x] **Load** reads the key, skips if **`null`**, then **`Number(saved)`**.
- [x] This snap auto-runs **++ ++ − Save Reset Load** so you see the cycle without clicking.

Sandbox: `code_sandbox/js-counter/full-project.html`

```html
<h2>Counter</h2>
<p id="count" style="font-size:40px;">0</p>
<button type="button" onclick="increaseCount()">+</button>
<button type="button" onclick="decreaseCount()">-</button>
<button type="button" onclick="resetCount()">Reset</button>
<button type="button" onclick="saveCount()">Save</button>
<button type="button" onclick="loadCount()">Load</button>

let count = 0;
function updateCount() {
  document.getElementById("count").innerHTML = count;
}
function increaseCount() {
  count++;
  updateCount();
}
function decreaseCount() {
  count--;
  updateCount();
}
function resetCount() {
  count = 0;
  updateCount();
}
function saveCount() {
  localStorage.setItem("count", count);
}
function loadCount() {
  let saved = localStorage.getItem("count");
  if (saved !== null) {
    count = Number(saved);
  }
  updateCount();
}
```

<img alt="js-counter example 1 source" src="./code_sandbox/snaps/js-counter-01-code.png" />

<img alt="js-counter example 1 result" src="./code_sandbox/snaps/js-counter-01-result.png" />

- [x] **Outcome:** After ++ ++ the display is **2**. After − it is **1**. Save stores **"1"**. Reset shows **0**. Load restores **1**.

<a id="js-counter-example-02"></a>

### **Example 2: HTML: #count and five onclick buttons**

- [x] Header **Counter**, paragraph **`id="count"`** (start **0**, large font), five **`<button onclick>`**.
- [x] Without the script, clicks do **nothing** — the functions are not defined yet.

Sandbox: `code_sandbox/js-counter/html-buttons.html`

```html
<h2>Counter</h2>
<p id="count" style="font-size:40px;">0</p>
<button onclick="increaseCount()">+</button>
<button onclick="decreaseCount()">-</button>
<button onclick="resetCount()">Reset</button>
<button onclick="saveCount()">Save</button>
<button onclick="loadCount()">Load</button>
```

<img alt="js-counter example 2 source" src="./code_sandbox/snaps/js-counter-02-code.png" />

<img alt="js-counter example 2 result" src="./code_sandbox/snaps/js-counter-02-result.png" />

- [x] **Outcome:** The page shows **0** and five buttons. Clicks are not wired in this HTML-only demo.

<a id="js-counter-example-03"></a>

### **Example 3: let count = 0 and updateCount()**

- [x] `let count = 0` is the **variable**.
- [x] `updateCount()` sets **`#count` innerHTML** to the current number.

Sandbox: `code_sandbox/js-counter/update-count.html`

```javascript
let count = 0;
function updateCount() {
  document.getElementById("count").innerHTML = count;
}
```

<img alt="js-counter example 3 source" src="./code_sandbox/snaps/js-counter-03-code.png" />

<img alt="js-counter example 3 result" src="./code_sandbox/snaps/js-counter-03-result.png" />

- [x] **Outcome:** Calling `updateCount()` with `count = 7` shows **7** in the paragraph.

<a id="js-counter-example-04"></a>

### **Example 4: increaseCount() — count++ then updateCount()**

- [x] `count++` adds **1**. Then **`updateCount()`** refreshes the page.

Sandbox: `code_sandbox/js-counter/increase-count.html`

```javascript
function increaseCount() {
  count++;
  updateCount();
}
```

<img alt="js-counter example 4 source" src="./code_sandbox/snaps/js-counter-04-code.png" />

<img alt="js-counter example 4 result" src="./code_sandbox/snaps/js-counter-04-result.png" />

- [x] **Outcome:** From **0**, two clicks (auto) show **2**.

<a id="js-counter-example-05"></a>

### **Example 5: decreaseCount() — count-- then updateCount()**

- [x] `count--` subtracts **1**. The first Tryit **does not** stop at 0 (it can go negative).

Sandbox: `code_sandbox/js-counter/decrease-count.html`

```javascript
function decreaseCount() {
  count--;
  updateCount();
}
```

<img alt="js-counter example 5 source" src="./code_sandbox/snaps/js-counter-05-code.png" />

<img alt="js-counter example 5 result" src="./code_sandbox/snaps/js-counter-05-result.png" />

- [x] **Outcome:** From **0**, one − shows **−1**. Exercise 2 later blocks that.

<a id="js-counter-example-06"></a>

### **Example 6: resetCount() — count = 0**

- [x] Reset **assigns 0** (it does not load from storage).

Sandbox: `code_sandbox/js-counter/reset-count.html`

```javascript
function resetCount() {
  count = 0;
  updateCount();
}
```

<img alt="js-counter example 6 source" src="./code_sandbox/snaps/js-counter-06-code.png" />

<img alt="js-counter example 6 result" src="./code_sandbox/snaps/js-counter-06-result.png" />

- [x] **Outcome:** After ++ to **3**, Reset shows **0**.

<a id="js-counter-example-07"></a>

### **Example 7: saveCount() — localStorage.setItem("count", count)**

- [x] **`localStorage.setItem(key, value)`** writes a **string**.
- [x] The number **5** is stored as **`"5"`**.

Sandbox: `code_sandbox/js-counter/save-count.html`

```javascript
function saveCount() {
  localStorage.setItem("count", count);
}
```

<img alt="js-counter example 7 source" src="./code_sandbox/snaps/js-counter-07-code.png" />

<img alt="js-counter example 7 result" src="./code_sandbox/snaps/js-counter-07-result.png" />

- [x] **Outcome:** After setting count to **5** and Save, `localStorage.getItem("count")` is **"5"** (string).

<a id="js-counter-example-08"></a>

### **Example 8: loadCount() — getItem + Number(saved)**

- [x] `getItem` returns **`null`** if the key was never saved — **do not** `Number(null)` into count blindly; the `if` skips that.
- [x] `Number("4")` is **4**. `localStorage` cannot store a real number type.

Sandbox: `code_sandbox/js-counter/load-count.html`

```javascript
function loadCount() {
  let saved = localStorage.getItem("count");
  if (saved !== null) {
    count = Number(saved);
  }
  updateCount();
}
```

<img alt="js-counter example 8 source" src="./code_sandbox/snaps/js-counter-08-code.png" />

<img alt="js-counter example 8 result" src="./code_sandbox/snaps/js-counter-08-result.png" />

- [x] **Outcome:** Save **4**, reset to **0**, Load → **4**. Missing key leaves the current count unchanged.

<a id="js-counter-example-09"></a>

### **Example 9: Exercise 1: start at 10 instead of 0**

- [x] Change the declaration: **`let count = 10`**.
- [x] The solutions Tryit also resets **back to 10** (not 0).

Sandbox: `code_sandbox/js-counter/ex-start-10.html`

```javascript
let count = 10;
```

<img alt="js-counter example 9 source" src="./code_sandbox/snaps/js-counter-09-code.png" />

<img alt="js-counter example 9 result" src="./code_sandbox/snaps/js-counter-09-result.png" />

- [x] **Outcome:** Initial display is **10**. Reset in the solutions file also returns to **10**.

<a id="js-counter-example-10"></a>

### **Example 10: Exercise 2: do not go below 0**

- [x] Wrap `count--` in **`if (count > 0)`**.
- [x] At **0**, − does **nothing**.

Sandbox: `code_sandbox/js-counter/ex-no-negative.html`

```javascript
function decreaseCount() {
  if (count > 0) {
    count--;
    updateCount();
  }
}
```

<img alt="js-counter example 10 source" src="./code_sandbox/snaps/js-counter-10-code.png" />

<img alt="js-counter example 10 result" src="./code_sandbox/snaps/js-counter-10-result.png" />

- [x] **Outcome:** From **0**, − leaves **0**. From **2**, − twice lands on **0**, not **−1**.

<a id="js-counter-example-11"></a>

### **Example 11: Exercise 3 + solutions: loadCount() when the page opens**

- [x] Call **`loadCount()`** at the top (function declarations are **hoisted**).
- [x] Save, reload — the saved number appears **without clicking Load**.
- [x] This sandbox seeds storage with **10**, then runs `loadCount()` like a fresh page.

Sandbox: `code_sandbox/js-counter/ex-autoload.html`

```javascript
let count = 10;
loadCount();
```

<img alt="js-counter example 11 source" src="./code_sandbox/snaps/js-counter-11-code.png" />

<img alt="js-counter example 11 result" src="./code_sandbox/snaps/js-counter-11-result.png" />

- [x] **Outcome:** With `localStorage.count = "10"`, the page opens at **10**. Auto-load ran.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-counter/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does + twice do from 0?

<details>
<summary>Answer</summary>

- [x] **count** becomes **2**.

</details>

### Question 2: Does the first Tryit’s − stop at 0?

<details>
<summary>Answer</summary>

- [x] **No.** From 0 it goes to **−1**.

</details>

### Question 3: What type is `localStorage.getItem("count")` after save 5?

<details>
<summary>Answer</summary>

- [x] A **string**: **"5"**.

</details>

### Question 4: Why `Number(saved)`?

<details>
<summary>Answer</summary>

- [x] Storage is **text**. You need a **number** for `++` / `--`.

</details>

### Question 5: What if the key was never saved?

<details>
<summary>Answer</summary>

- [x] **getItem** is **null**. Leave **count** as-is.

</details>

### Question 6: Exercise 1 starting value?

<details>
<summary>Answer</summary>

- [x] **10** (and reset returns to **10** in the solutions file).

</details>

### Question 7: Exercise 2 at count 0, press −?

<details>
<summary>Answer</summary>

- [x] **Nothing.** `if (count > 0)` fails.

</details>

### Question 8: How does auto-load work on open?

<details>
<summary>Answer</summary>

- [x] Call **`loadCount()`** at startup. Function declarations are **hoisted**.

</details>


</details>

## Summary

Five onclick handlers around one count variable. Persist with localStorage strings plus Number on the way back. Guard decrease and auto-load if you want a friendlier app.

## References

- [JS Counter (W3Schools)](https://www.w3schools.com/js/js_project_counter.asp)
- [MDN: Window.localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- [MDN: Number()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)

</details>
