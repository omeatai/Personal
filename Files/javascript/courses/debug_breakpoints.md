# Debug Breakpoints

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Breakpoints pause JavaScript on a line so you can inspect real values. Set them in Sources by clicking line numbers, then reload. The debugger keyword is the same idea in source. When paused, Step Over / Into / Out control the next line. Scope shows locals vs globals. Watch tracks a name as it changes. Reload after adding a breakpoint; a breakpoint in a loop fires every iteration.

This section has **6** examples:

- [x] **Example 1:** add(a, b) — pause on a line, then inspect result [View](#js-debugging-breakpoints-example-01)
- [x] **Example 2:** debugger; pauses like a breakpoint [View](#js-debugging-breakpoints-example-02)
- [x] **Example 3:** Step Over, Step Into, Step Out [View](#js-debugging-breakpoints-example-03)
- [x] **Example 4:** Scope: local y vs global x [View](#js-debugging-breakpoints-example-04)
- [x] **Example 5:** Watch a variable instead of many console.log calls [View](#js-debugging-breakpoints-example-05)
- [x] **Example 6:** Reload after setting a breakpoint; loops fire often [View](#js-debugging-breakpoints-example-06)

## Detailed Explanation

- [x] Click a **line number** in **Sources**, **reload**, use **play** to continue.
- [x] **`debugger;`** pauses if DevTools is attached; otherwise it is a no-op.
- [x] **Step Over / Into / Out**. **Scope** = locals vs globals. **Watch** = live expressions.
- [x] Reload after setting. Loops pause **repeatedly**.

<a id="js-debugging-breakpoints-example-01"></a>

### **Example 1: add(a, b) — pause on a line, then inspect result**

- [x] A **breakpoint** pauses on a **specific line**. You then inspect variables and **step**.
- [x] Set them in DevTools **Sources**: click a **line number**, **reload**, use **play** to continue.
- [x] This Tryit calls `add` four times (5, 50, 500, 5000). Without a breakpoint the last write wins: **5010**.
- [x] Headless snaps cannot pause DevTools. The sandbox still **runs** the function so you see the final DOM value.

Sandbox: `code_sandbox/js-debugging-breakpoints/add-function-breakpoints.html`

```javascript
function add(a, b) {
  let result = a + b;
  return result;
}
document.getElementById("demo").innerHTML = add(10, 5);
document.getElementById("demo").innerHTML = add(10, 50);
document.getElementById("demo").innerHTML = add(10, 500);
document.getElementById("demo").innerHTML = add(10, 5000);
```

<img alt="js-debugging-breakpoints example 1 source" src="../code_sandbox/snaps/js-debugging-breakpoints-01-code.png" />

<img alt="js-debugging-breakpoints example 1 result" src="../code_sandbox/snaps/js-debugging-breakpoints-01-result.png" />

- [x] **Outcome:** The paragraph ends as **5010** (`10 + 5000`). Earlier results **15**, **60**, **510** were overwritten.

<a id="js-debugging-breakpoints-example-02"></a>

### **Example 2: debugger; pauses like a breakpoint**

- [x] The **`debugger`** keyword stops execution and opens the debugger **if DevTools is open**.
- [x] If no debugger is attached, **`debugger` has no effect**.
- [x] The page’s Tryit: `let x = 15 * 5; debugger; document.getElementById("demo").innerHTML = x;`
- [x] This sandbox **omits** `debugger` so the screenshot can finish. With DevTools open, the original line would pause **before** writing **75**.

Sandbox: `code_sandbox/js-debugging-breakpoints/debugger-keyword.html`

```javascript
let x = 15 * 5;
// debugger;  // omitted in the live demo so the page can finish
document.getElementById("demo").innerHTML = x;
```

<img alt="js-debugging-breakpoints example 2 source" src="../code_sandbox/snaps/js-debugging-breakpoints-02-code.png" />

<img alt="js-debugging-breakpoints example 2 result" src="../code_sandbox/snaps/js-debugging-breakpoints-02-result.png" />

- [x] **Outcome:** **x** is **75**. A live `debugger;` would pause **before** that assignment when DevTools is open.

<a id="js-debugging-breakpoints-example-03"></a>

### **Example 3: Step Over, Step Into, Step Out**

- [x] When paused: **Step Over** runs the **next line** (does not enter a call). **Step Into** **enters** a function. **Step Out** **finishes** the current function.
- [x] Watch values change as you step. This demo shows the same calls without pausing.

Sandbox: `code_sandbox/js-debugging-breakpoints/step-over-into-out.html`

```javascript
function double(n) {
  return n * 2;
}
function total(a, b) {
  return double(a) + double(b);
}
console.log(total(3, 4));
```

<img alt="js-debugging-breakpoints example 3 source" src="../code_sandbox/snaps/js-debugging-breakpoints-03-code.png" />

<img alt="js-debugging-breakpoints example 3 result" src="../code_sandbox/snaps/js-debugging-breakpoints-03-result.png" />

- [x] **Outcome:** **log: 14** (`double(3)+double(4)` → 6+8). Step Into from `total` would enter **`double`**.

<a id="js-debugging-breakpoints-example-04"></a>

### **Example 4: Scope: local y vs global x**

- [x] The **Scope** panel lists variables **at the current line**.
- [x] **Local** variables exist **inside** the function. **Global** variables exist **everywhere**.
- [x] At a breakpoint inside `test()`, **`y` exists only there**. **`x`** is still visible (global).

Sandbox: `code_sandbox/js-debugging-breakpoints/scope-panel.html`

```javascript
let x = 10;
function test() {
  let y = 5;
  console.log(x + y);
}
test();
```

<img alt="js-debugging-breakpoints example 4 source" src="../code_sandbox/snaps/js-debugging-breakpoints-04-code.png" />

<img alt="js-debugging-breakpoints example 4 result" src="../code_sandbox/snaps/js-debugging-breakpoints-04-result.png" />

- [x] **Outcome:** **log: 15**. Inside `test`, local **y** is **5** and global **x** is **10**. Outside `test`, **`y` is not defined**.

<a id="js-debugging-breakpoints-example-05"></a>

### **Example 5: Watch a variable instead of many console.log calls**

- [x] The **Watch** panel tracks an expression **live** as you step.
- [x] Add a name (or `result`, `i`, `user.age`). The value **updates** as the code runs.
- [x] Prefer Watch for values that change **many times** (loops).

Sandbox: `code_sandbox/js-debugging-breakpoints/watch-panel.html`

```javascript
let sum = 0;
for (let i = 1; i <= 3; i++) {
  sum += i;
  console.log("i", i, "sum", sum);
}
```

<img alt="js-debugging-breakpoints example 5 source" src="../code_sandbox/snaps/js-debugging-breakpoints-05-code.png" />

<img alt="js-debugging-breakpoints example 5 result" src="../code_sandbox/snaps/js-debugging-breakpoints-05-result.png" />

- [x] **Outcome:** Watch **`sum`** would show **1**, then **3**, then **6**. Logs: **i 1 sum 1**, **i 2 sum 3**, **i 3 sum 6**.

<a id="js-debugging-breakpoints-example-06"></a>

### **Example 6: Reload after setting a breakpoint; loops fire often**

- [x] A common miss: you set a breakpoint **then forget to reload** — old code already ran.
- [x] A breakpoint **inside a loop** pauses **every iteration**. Disable it if that gets noisy.
- [x] Use breakpoints when values change **unexpectedly**, results are **wrong**, or logic is **complex**.

Sandbox: `code_sandbox/js-debugging-breakpoints/breakpoint-gotchas.html`

```javascript
for (let i = 0; i < 3; i++) {
  console.log("loop", i);
}
```

<img alt="js-debugging-breakpoints example 6 source" src="../code_sandbox/snaps/js-debugging-breakpoints-06-code.png" />

<img alt="js-debugging-breakpoints example 6 result" src="../code_sandbox/snaps/js-debugging-breakpoints-06-result.png" />

- [x] **Outcome:** **loop 0**, **loop 1**, **loop 2** — a breakpoint on that log would pause **three** times.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-debugging-breakpoints/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the last `innerHTML` after four `add` calls?

<details>
<summary>Answer</summary>

- [x] **5010** (`add(10, 5000)`). Earlier results were overwritten.

</details>

### Question 2: What is `add(10, 5)`?

<details>
<summary>Answer</summary>

- [x] **15**.

</details>

### Question 3: What does `debugger` do with DevTools closed?

<details>
<summary>Answer</summary>

- [x] **Nothing.** No debugger is available.

</details>

### Question 4: What is `15 * 5` in the debugger Tryit?

<details>
<summary>Answer</summary>

- [x] **75** — written to `#demo` after the pause point.

</details>

### Question 5: Step Into vs Step Over at `total(3, 4)`?

<details>
<summary>Answer</summary>

- [x] **Into** enters **`double`**. **Over** runs the call as one line.

</details>

### Question 6: Where does `y` exist in `function test() { let y = 5; }`?

<details>
<summary>Answer</summary>

- [x] **Only inside `test`.** Outside, `y` is **not defined**.

</details>

### Question 7: What values would Watch `sum` show for `for (i=1; i<=3; i++) sum += i`?

<details>
<summary>Answer</summary>

- [x] **1**, then **3**, then **6**.

</details>

### Question 8: Why did my new breakpoint never hit?

<details>
<summary>Answer</summary>

- [x] You probably **did not reload**. The previous run already finished.

</details>


</details>

## Summary

Pause with a breakpoint or debugger, step through, read Scope and Watch, then resume. Reload after setting breakpoints. Use them when logging is not enough.

## References

- [JS Debugging Breakpoints (W3Schools)](https://www.w3schools.com/js/js_debugging_breakpoints.asp)
- [MDN: debugger](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger)
- [MDN: Chrome DevTools breakpoints](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#debugging)
