<details>
  <summary>Debug Reference</summary>

## Introduction

Full console method list (revised December 2026 on the page): assert, clear, dir, count, error, group, groupCollapsed, groupEnd, info, log, table, time, timeEnd, trace, warn. Each row below is a runnable demo. assert is silent when true. clear wipes the log. dir/table inspect structures. count tallies calls. group* indents. time/timeEnd measure. trace prints a stack.

This section has **15** examples:

- [x] **Example 1:** assert() — logs only when the assertion is false [View](#js-debugging-reference-example-01)
- [x] **Example 2:** clear() — clears the console [View](#js-debugging-reference-example-02)
- [x] **Example 3:** dir() — interactive listing of object properties [View](#js-debugging-reference-example-03)
- [x] **Example 4:** count() — how many times this call ran [View](#js-debugging-reference-example-04)
- [x] **Example 5:** error() — error-styled console message [View](#js-debugging-reference-example-05)
- [x] **Example 6:** group() — indent following messages until groupEnd() [View](#js-debugging-reference-example-06)
- [x] **Example 7:** groupCollapsed() — same group, starts collapsed [View](#js-debugging-reference-example-07)
- [x] **Example 8:** groupEnd() — exits the current inline group [View](#js-debugging-reference-example-08)
- [x] **Example 9:** info() — informational console message [View](#js-debugging-reference-example-09)
- [x] **Example 10:** log() — general message; accepts multiple arguments [View](#js-debugging-reference-example-10)
- [x] **Example 11:** table() — tabular data as a table [View](#js-debugging-reference-example-11)
- [x] **Example 12:** time() — starts a named timer [View](#js-debugging-reference-example-12)
- [x] **Example 13:** timeEnd() — stops a timer started by time() [View](#js-debugging-reference-example-13)
- [x] **Example 14:** trace() — stack trace to the console [View](#js-debugging-reference-example-14)
- [x] **Example 15:** warn() — warning-styled message (often yellow) [View](#js-debugging-reference-example-15)

## Detailed Explanation

- [x] One **Example per table row** — not a name list.
- [x] **assert** silent if true. **clear** empties. **count** increments a label.
- [x] **group / groupCollapsed / groupEnd** nest. **time / timeEnd** pair by **label**.
- [x] **error** / **warn** / **info** / **log** differ by **level**, not by throwing.

<a id="js-debugging-reference-example-01"></a>

### **Example 1: assert() — logs only when the assertion is false**

- [x] **`console.assert(condition, ...msg)`** writes **only if `condition` is falsy**.
- [x] A **true** assertion prints **nothing** (keeps logs clean).

Sandbox: `code_sandbox/js-debugging-reference/assert.html`

```javascript
console.assert(1 === 1, "this stays quiet");
console.assert(1 === 2, "math is broken");
```

<img alt="js-debugging-reference example 1 source" src="./code_sandbox/snaps/js-debugging-reference-01-code.png" />

<img alt="js-debugging-reference example 1 result" src="./code_sandbox/snaps/js-debugging-reference-01-result.png" />

- [x] **Outcome:** True assert: **no line**. False assert: **assert: Assertion failed: math is broken**.

<a id="js-debugging-reference-example-02"></a>

### **Example 2: clear() — clears the console**

- [x] **`console.clear()`** wipes previous console output.

Sandbox: `code_sandbox/js-debugging-reference/clear.html`

```javascript
console.log("before");
console.clear();
console.log("after");
```

<img alt="js-debugging-reference example 2 source" src="./code_sandbox/snaps/js-debugging-reference-02-code.png" />

<img alt="js-debugging-reference example 2 result" src="./code_sandbox/snaps/js-debugging-reference-02-result.png" />

- [x] **Outcome:** Capture shows **(console cleared)** then **log: after**. **before** is gone.

<a id="js-debugging-reference-example-03"></a>

### **Example 3: dir() — interactive listing of object properties**

- [x] **`console.dir(obj)`** is a **property tree**, often more detailed than `log` for DOM nodes / complex objects.

Sandbox: `code_sandbox/js-debugging-reference/dir.html`

```javascript
console.dir({ name: "John", age: 25 });
```

<img alt="js-debugging-reference example 3 source" src="./code_sandbox/snaps/js-debugging-reference-03-code.png" />

<img alt="js-debugging-reference example 3 result" src="./code_sandbox/snaps/js-debugging-reference-03-result.png" />

- [x] **Outcome:** **dir: {"name":"John","age":25}**.

<a id="js-debugging-reference-example-04"></a>

### **Example 4: count() — how many times this call ran**

- [x] **`console.count(label)`** increments a counter for that **label** (default label is **`default`**).

Sandbox: `code_sandbox/js-debugging-reference/count.html`

```javascript
console.count("click");
console.count("click");
console.count("click");
```

<img alt="js-debugging-reference example 4 source" src="./code_sandbox/snaps/js-debugging-reference-04-code.png" />

<img alt="js-debugging-reference example 4 result" src="./code_sandbox/snaps/js-debugging-reference-04-result.png" />

- [x] **Outcome:** **click: 1**, **click: 2**, **click: 3**.

<a id="js-debugging-reference-example-05"></a>

### **Example 5: error() — error-styled console message**

- [x] **`console.error()`** highlights **critical** issues (often red). It does **not** throw.

Sandbox: `code_sandbox/js-debugging-reference/error.html`

```javascript
console.error("Something went wrong!");
```

<img alt="js-debugging-reference example 5 source" src="./code_sandbox/snaps/js-debugging-reference-05-code.png" />

<img alt="js-debugging-reference example 5 result" src="./code_sandbox/snaps/js-debugging-reference-05-result.png" />

- [x] **Outcome:** **error: Something went wrong!**

<a id="js-debugging-reference-example-06"></a>

### **Example 6: group() — indent following messages until groupEnd()**

- [x] **`console.group(label)`** starts an **expanded** inline group.
- [x] Later messages are **indented** until **`console.groupEnd()`**.

Sandbox: `code_sandbox/js-debugging-reference/group.html`

```javascript
console.group("user");
console.log("John");
console.groupEnd();
```

<img alt="js-debugging-reference example 6 source" src="./code_sandbox/snaps/js-debugging-reference-06-code.png" />

<img alt="js-debugging-reference example 6 result" src="./code_sandbox/snaps/js-debugging-reference-06-result.png" />

- [x] **Outcome:** **group: user**, then indented **log: John**, then **groupEnd**.

<a id="js-debugging-reference-example-07"></a>

### **Example 7: groupCollapsed() — same group, starts collapsed**

- [x] **`console.groupCollapsed()`** creates a group that is **collapsed** until you expand it in DevTools.

Sandbox: `code_sandbox/js-debugging-reference/group-collapsed.html`

```javascript
console.groupCollapsed("details");
console.log("hidden until expanded");
console.groupEnd();
```

<img alt="js-debugging-reference example 7 source" src="./code_sandbox/snaps/js-debugging-reference-07-code.png" />

<img alt="js-debugging-reference example 7 result" src="./code_sandbox/snaps/js-debugging-reference-07-result.png" />

- [x] **Outcome:** **groupCollapsed: details**, indented **log: hidden until expanded**, **groupEnd**.

<a id="js-debugging-reference-example-08"></a>

### **Example 8: groupEnd() — exits the current inline group**

- [x] **`console.groupEnd()`** pops one group. Nested groups need **one `groupEnd` per `group`**.

Sandbox: `code_sandbox/js-debugging-reference/group-end.html`

```javascript
console.group("outer");
console.group("inner");
console.log("in");
console.groupEnd();
console.log("out");
console.groupEnd();
```

<img alt="js-debugging-reference example 8 source" src="./code_sandbox/snaps/js-debugging-reference-08-code.png" />

<img alt="js-debugging-reference example 8 result" src="./code_sandbox/snaps/js-debugging-reference-08-result.png" />

- [x] **Outcome:** **in** is indented twice. **out** is indented once (still in **outer**).

<a id="js-debugging-reference-example-09"></a>

### **Example 9: info() — informational console message**

- [x] **`console.info()`** is an **info** log (filterable in DevTools). Similar to `log` with a different **level**.

Sandbox: `code_sandbox/js-debugging-reference/info.html`

```javascript
console.info("loaded");
```

<img alt="js-debugging-reference example 9 source" src="./code_sandbox/snaps/js-debugging-reference-09-code.png" />

<img alt="js-debugging-reference example 9 result" src="./code_sandbox/snaps/js-debugging-reference-09-result.png" />

- [x] **Outcome:** **info: loaded**.

<a id="js-debugging-reference-example-10"></a>

### **Example 10: log() — general message; accepts multiple arguments**

- [x] **`console.log()`** is the default. It accepts **multiple arguments** (text + objects).

Sandbox: `code_sandbox/js-debugging-reference/log.html`

```javascript
console.log("x", 10, { ok: true });
```

<img alt="js-debugging-reference example 10 source" src="./code_sandbox/snaps/js-debugging-reference-10-code.png" />

<img alt="js-debugging-reference example 10 result" src="./code_sandbox/snaps/js-debugging-reference-10-result.png" />

- [x] **Outcome:** **log: x 10 {"ok":true}**.

<a id="js-debugging-reference-example-11"></a>

### **Example 11: table() — tabular data as a table**

- [x] **`console.table()`** is ideal for **arrays of objects**.

Sandbox: `code_sandbox/js-debugging-reference/table.html`

```javascript
console.table([{name:"John", age:25},{name:"Anna", age:30}]);
```

<img alt="js-debugging-reference example 11 source" src="./code_sandbox/snaps/js-debugging-reference-11-code.png" />

<img alt="js-debugging-reference example 11 result" src="./code_sandbox/snaps/js-debugging-reference-11-result.png" />

- [x] **Outcome:** **table:** two rows with **name** / **age**.

<a id="js-debugging-reference-example-12"></a>

### **Example 12: time() — starts a named timer**

- [x] **`console.time(label)`** starts a timer you later stop with **`timeEnd`**.

Sandbox: `code_sandbox/js-debugging-reference/time.html`

```javascript
console.time("work");
console.log("timer running");
```

<img alt="js-debugging-reference example 12 source" src="./code_sandbox/snaps/js-debugging-reference-12-code.png" />

<img alt="js-debugging-reference example 12 result" src="./code_sandbox/snaps/js-debugging-reference-12-result.png" />

- [x] **Outcome:** **time: started "work"** then **log: timer running**. Duration appears in **timeEnd**.

<a id="js-debugging-reference-example-13"></a>

### **Example 13: timeEnd() — stops a timer started by time()**

- [x] **`console.timeEnd(label)`** prints elapsed milliseconds for that label.
- [x] The exact ms **varies**. Expect a **small positive** number, not a fixed digit.

Sandbox: `code_sandbox/js-debugging-reference/time-end.html`

```javascript
console.time("work");
for (let i = 0; i < 10000; i++) {}
console.timeEnd("work");
```

<img alt="js-debugging-reference example 13 source" src="./code_sandbox/snaps/js-debugging-reference-13-code.png" />

<img alt="js-debugging-reference example 13 result" src="./code_sandbox/snaps/js-debugging-reference-13-result.png" />

- [x] **Outcome:** **timeEnd: "work":** a duration in **ms** (this engine; not a promised exact number).

<a id="js-debugging-reference-example-14"></a>

### **Example 14: trace() — stack trace to the console**

- [x] **`console.trace()`** prints a **stack** showing **how you got here**.

Sandbox: `code_sandbox/js-debugging-reference/trace.html`

```javascript
function inner() { console.trace("from inner"); }
function outer() { inner(); }
outer();
```

<img alt="js-debugging-reference example 14 source" src="./code_sandbox/snaps/js-debugging-reference-14-code.png" />

<img alt="js-debugging-reference example 14 result" src="./code_sandbox/snaps/js-debugging-reference-14-result.png" />

- [x] **Outcome:** **trace:** a stack that includes **inner** then **outer** (plus the page script).

<a id="js-debugging-reference-example-15"></a>

### **Example 15: warn() — warning-styled message (often yellow)**

- [x] **`console.warn()`** is like `log` with a **warning** level (filterable, often yellow).

Sandbox: `code_sandbox/js-debugging-reference/warn.html`

```javascript
console.warn("This is a warning!");
```

<img alt="js-debugging-reference example 15 source" src="./code_sandbox/snaps/js-debugging-reference-15-code.png" />

<img alt="js-debugging-reference example 15 result" src="./code_sandbox/snaps/js-debugging-reference-15-result.png" />

- [x] **Outcome:** **warn: This is a warning!**

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-debugging-reference/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: When does `console.assert` print?

<details>
<summary>Answer</summary>

- [x] Only when the condition is **falsy**.

</details>

### Question 2: What does `console.clear()` do to earlier logs?

<details>
<summary>Answer</summary>

- [x] They **disappear**. Next logs start fresh.

</details>

### Question 3: `console.count("click")` three times?

<details>
<summary>Answer</summary>

- [x] **click: 1**, **2**, **3**.

</details>

### Question 4: Does `console.error` throw?

<details>
<summary>Answer</summary>

- [x] **No.** It is a **styled log**.

</details>

### Question 5: What does `group` + log + `groupEnd` do?

<details>
<summary>Answer</summary>

- [x] The log is **indented** inside the group label.

</details>

### Question 6: `groupCollapsed` vs `group`?

<details>
<summary>Answer</summary>

- [x] Same grouping; collapsed **starts shut** in DevTools.

</details>

### Question 7: `console.log("x", 10, {ok:true})`?

<details>
<summary>Answer</summary>

- [x] **x 10 {"ok":true}** — multiple arguments.

</details>

### Question 8: What is `console.table` for?

<details>
<summary>Answer</summary>

- [x] **Arrays of objects** (rows/columns).

</details>

### Question 9: What does `time` / `timeEnd` print?

<details>
<summary>Answer</summary>

- [x] Elapsed **ms** for that **label** (exact value varies).

</details>

### Question 10: What is `console.trace()`?

<details>
<summary>Answer</summary>

- [x] A **stack trace** of the current call chain.

</details>


</details>

## Summary

Use log/info/warn/error for levels, table/dir for structure, count for tallies, group* for nesting, time* for duration, assert for quiet checks, trace for stacks, and clear to reset.

## References

- [JS Debugging Reference (W3Schools)](https://www.w3schools.com/js/js_debugging_reference.asp)
- [MDN: console](https://developer.mozilla.org/en-US/docs/Web/API/console)
- [MDN: console.assert()](https://developer.mozilla.org/en-US/docs/Web/API/console/assert_static)
- [MDN: console.time()](https://developer.mozilla.org/en-US/docs/Web/API/console/time_static)

</details>
