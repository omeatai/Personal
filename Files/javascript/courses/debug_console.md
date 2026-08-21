# Debug Console

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The browser console is the main debugging tool for beginners. Keep it open while testing. This page’s Tryits cover console.log (message and variables), console.warn, console.error, logging several values, logging an object, and console.table for arrays of objects. Professionals log the value instead of guessing.

This section has **8** examples:

- [x] **Example 1:** console.log("Hello from JavaScript!") [View](#js-debugging-console-example-01)
- [x] **Example 2:** console.log(name) and console.log(age) [View](#js-debugging-console-example-02)
- [x] **Example 3:** console.warn("This is a warning!") [View](#js-debugging-console-example-03)
- [x] **Example 4:** console.error("Something went wrong!") [View](#js-debugging-console-example-04)
- [x] **Example 5:** console.log("x =", x, "y =", y) [View](#js-debugging-console-example-05)
- [x] **Example 6:** console.log(user) inspects an object [View](#js-debugging-console-example-06)
- [x] **Example 7:** console.table(users) for arrays of objects [View](#js-debugging-console-example-07)
- [x] **Example 8:** Stop guessing — log the value [View](#js-debugging-console-example-08)

## Detailed Explanation

- [x] Right-click → **Inspect** → **Console** (Chrome / Edge), or **F12**.
- [x] **`log`** general, **`warn`** suspicious, **`error`** failed (styled, **not** a throw).
- [x] Pass **multiple arguments**. Log **objects**. Use **`table`** for arrays of objects.
- [x] Do **not guess** — log the value.

<a id="js-debugging-console-example-01"></a>

### **Example 1: console.log("Hello from JavaScript!")**

- [x] **`console.log()`** is the most common console method.
- [x] Use it to print values and see what the program is doing.

Sandbox: `code_sandbox/js-debugging-console/log-hello.html`

```javascript
console.log("Hello from JavaScript!");
```

<img alt="js-debugging-console example 1 source" src="../code_sandbox/snaps/js-debugging-console-01-code.png" />

<img alt="js-debugging-console example 1 result" src="../code_sandbox/snaps/js-debugging-console-01-result.png" />

- [x] **Outcome:** **log: Hello from JavaScript!**

<a id="js-debugging-console-example-02"></a>

### **Example 2: console.log(name) and console.log(age)**

- [x] You can log **each** variable on its own line.
- [x] That is clearer than guessing which value is wrong.

Sandbox: `code_sandbox/js-debugging-console/log-variables.html`

```javascript
let name = "John";
let age = 25;
console.log(name);
console.log(age);
```

<img alt="js-debugging-console example 2 source" src="../code_sandbox/snaps/js-debugging-console-02-code.png" />

<img alt="js-debugging-console example 2 result" src="../code_sandbox/snaps/js-debugging-console-02-result.png" />

- [x] **Outcome:** **log: John** then **log: 25**.

<a id="js-debugging-console-example-03"></a>

### **Example 3: console.warn("This is a warning!")**

- [x] **`console.warn()`** is a **warning** (often yellow). The program **still runs**.
- [x] Use it for something **suspicious**, not a hard failure.

Sandbox: `code_sandbox/js-debugging-console/console-warn.html`

```javascript
console.warn("This is a warning!");
```

<img alt="js-debugging-console example 3 source" src="../code_sandbox/snaps/js-debugging-console-03-code.png" />

<img alt="js-debugging-console example 3 result" src="../code_sandbox/snaps/js-debugging-console-03-result.png" />

- [x] **Outcome:** **warn: This is a warning!**

<a id="js-debugging-console-example-04"></a>

### **Example 4: console.error("Something went wrong!")**

- [x] **`console.error()`** prints an **error-styled** message (often red).
- [x] It does **not** throw. Execution **continues**. Use `throw` if you need to stop.

Sandbox: `code_sandbox/js-debugging-console/console-error.html`

```javascript
console.error("Something went wrong!");
```

<img alt="js-debugging-console example 4 source" src="../code_sandbox/snaps/js-debugging-console-04-code.png" />

<img alt="js-debugging-console example 4 result" src="../code_sandbox/snaps/js-debugging-console-04-result.png" />

- [x] **Outcome:** **error: Something went wrong!** — and the next line can still run.

<a id="js-debugging-console-example-05"></a>

### **Example 5: console.log("x =", x, "y =", y)**

- [x] `console.log` accepts **multiple arguments**. They print separated by spaces.
- [x] Useful for labeling values: `"x =", x, "y =", y`.

Sandbox: `code_sandbox/js-debugging-console/log-multiple.html`

```javascript
let x = 10;
let y = 5;
console.log("x =", x, "y =", y);
```

<img alt="js-debugging-console example 5 source" src="../code_sandbox/snaps/js-debugging-console-05-code.png" />

<img alt="js-debugging-console example 5 result" src="../code_sandbox/snaps/js-debugging-console-05-result.png" />

- [x] **Outcome:** **log: x = 10 y = 5**.

<a id="js-debugging-console-example-06"></a>

### **Example 6: console.log(user) inspects an object**

- [x] Logging an **object** shows its properties.
- [x] In DevTools you can **click to expand**. Here JSON shows **name** and **age**.

Sandbox: `code_sandbox/js-debugging-console/log-object.html`

```javascript
let user = {name: "John", age: 25};
console.log(user);
```

<img alt="js-debugging-console example 6 source" src="../code_sandbox/snaps/js-debugging-console-06-code.png" />

<img alt="js-debugging-console example 6 result" src="../code_sandbox/snaps/js-debugging-console-06-result.png" />

- [x] **Outcome:** **log: {"name":"John","age":25}**.

<a id="js-debugging-console-example-07"></a>

### **Example 7: console.table(users) for arrays of objects**

- [x] **`console.table()`** renders rows as a **table** (index, name, age).
- [x] Much easier to scan than a nested object dump.

Sandbox: `code_sandbox/js-debugging-console/console-table.html`

```javascript
let users = [
  {name: "John", age: 25},
  {name: "Anna", age: 30}
];
console.table(users);
```

<img alt="js-debugging-console example 7 source" src="../code_sandbox/snaps/js-debugging-console-07-code.png" />

<img alt="js-debugging-console example 7 result" src="../code_sandbox/snaps/js-debugging-console-07-result.png" />

- [x] **Outcome:** **table:** `[{"name":"John","age":25},{"name":"Anna","age":30}]`. In DevTools this is a grid with columns **name** and **age**.

<a id="js-debugging-console-example-08"></a>

### **Example 8: Stop guessing — log the value**

- [x] Beginners **guess**. Professionals **log and confirm**.
- [x] If code misbehaves, do not invent a theory first — **`console.log` the actual value**.

Sandbox: `code_sandbox/js-debugging-console/stop-guessing.html`

```javascript
let cart = { items: 2, total: 0 };
console.log("cart before", cart);
cart.total = 19.9 * cart.items;
console.log("cart after", cart);
```

<img alt="js-debugging-console example 8 source" src="../code_sandbox/snaps/js-debugging-console-08-code.png" />

<img alt="js-debugging-console example 8 result" src="../code_sandbox/snaps/js-debugging-console-08-result.png" />

- [x] **Outcome:** Before: **total 0**. After: **total 39.8**. The log **confirms** the write.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-debugging-console/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `console.log("Hello from JavaScript!")` print?

<details>
<summary>Answer</summary>

- [x] **Hello from JavaScript!**

</details>

### Question 2: What do `console.log(name)` and `console.log(age)` print for John / 25?

<details>
<summary>Answer</summary>

- [x] **John** then **25**.

</details>

### Question 3: Does `console.warn` stop the script?

<details>
<summary>Answer</summary>

- [x] **No.** It is a **warning**. Execution continues.

</details>

### Question 4: Does `console.error("Something went wrong!")` throw?

<details>
<summary>Answer</summary>

- [x] **No.** It only **styles** a message. The next statement can still run.

</details>

### Question 5: What is `console.log("x =", 10, "y =", 5)`?

<details>
<summary>Answer</summary>

- [x] **x = 10 y = 5**.

</details>

### Question 6: What does logging `{name:"John", age:25}` show?

<details>
<summary>Answer</summary>

- [x] **{"name":"John","age":25}** (expandable in DevTools).

</details>

### Question 7: Why `console.table(users)`?

<details>
<summary>Answer</summary>

- [x] It shows **rows** (John 25, Anna 30) instead of a nested dump.

</details>

### Question 8: What should you do instead of guessing a value?

<details>
<summary>Answer</summary>

- [x] **`console.log` it** and confirm.

</details>


</details>

## Summary

Keep the console open. Use log, warn, error, multi-arg log, object log, and table. Confirm values; do not guess. Breakpoints come next when you need to pause.

## References

- [JS Debugging Console (W3Schools)](https://www.w3schools.com/js/js_debugging_console.asp)
- [MDN: console](https://developer.mozilla.org/en-US/docs/Web/API/console)
- [MDN: console.table()](https://developer.mozilla.org/en-US/docs/Web/API/console/table_static)
