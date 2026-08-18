<details>
  <summary>Debug Intro</summary>

## Introduction

Debugging is finding and fixing bugs. Code fails because of syntax errors or logic errors, and beginners often guess. The useful habit is Read the error → Reproduce → Reduce to a small example → Fix. If nothing visible happens, open the console (F12). This page’s Tryits: console.log Hello, log a total, string vs number +, ReferenceError, TypeError, = inside if vs ===, and a+b. The first known computer bug was a real insect in the electronics — the word stuck.

This section has **10** examples:

- [x] **Example 1:** console.log("Hello!") [View](#js-debugging-example-01)
- [x] **Example 2:** console.log price, quantity, and total [View](#js-debugging-example-02)
- [x] **Example 3:** 5 + "5" is "55"; 5 + Number("5") is 10 [View](#js-debugging-example-03)
- [x] **Example 4:** ReferenceError: myValue is not defined [View](#js-debugging-example-04)
- [x] **Example 5:** TypeError: Cannot read properties of undefined (reading 'length') [View](#js-debugging-example-05)
- [x] **Example 6:** Mistake: if (x = 5) assigns and always runs [View](#js-debugging-example-06)
- [x] **Example 7:** Fix: if (x === 5) compares without assigning [View](#js-debugging-example-07)
- [x] **Example 8:** console.log(c) after a + b [View](#js-debugging-example-08)
- [x] **Example 9:** Habit: Read → Reproduce → Reduce → Fix [View](#js-debugging-example-09)
- [x] **Example 10:** Open the browser console (F12) [View](#js-debugging-example-10)

## Detailed Explanation

- [x] Bugs are **normal**. The skill is **locating** them quickly.
- [x] **Read → Reproduce → Reduce → Fix.** Check **facts**, do not guess.
- [x] Open **F12 → Console**. **`console.log`** is the first tool.
- [x] **ReferenceError** = missing name. **TypeError** = impossible use of a value (often `undefined`).
- [x] `if (x = 5)` **assigns**. Use **`===`** to compare.

<a id="js-debugging-example-01"></a>

### **Example 1: console.log("Hello!")**

- [x] If the page **does nothing**, open the **console** (usually **F12** → **Console**).
- [x] **`console.log()`** prints a value. It does **not** change the HTML.
- [x] The Tryit is a full page: heading **My First Web Page**, then `console.log("Hello!")`.

Sandbox: `code_sandbox/js-debugging/console-hello.html`

```javascript
<!DOCTYPE html>
<html>
<body>
<h1>My First Web Page</h1>
<script>
console.log("Hello!");
</script>
</body>
</html>
```

<img alt="js-debugging example 1 source" src="./code_sandbox/snaps/js-debugging-01-code.png" />

<img alt="js-debugging example 1 result" src="./code_sandbox/snaps/js-debugging-01-result.png" />

- [x] **Outcome:** The mirrored console shows **log: Hello!**. The heading is unchanged — the message is **not** in the page body.

<a id="js-debugging-example-02"></a>

### **Example 2: console.log price, quantity, and total**

- [x] Log **variables** to see what the program is doing.
- [x] **Tip:** log **before and after** a suspect line to see where values go wrong.

Sandbox: `code_sandbox/js-debugging/console-variables.html`

```javascript
let price = 50;
let quantity = 3;
let total = price * quantity;
console.log("Total:", total);
```

<img alt="js-debugging example 2 source" src="./code_sandbox/snaps/js-debugging-02-code.png" />

<img alt="js-debugging example 2 result" src="./code_sandbox/snaps/js-debugging-02-result.png" />

- [x] **Outcome:** **log: Total: 150**. `price * quantity` is **150**.

<a id="js-debugging-example-03"></a>

### **Example 3: 5 + "5" is "55"; 5 + Number("5") is 10**

- [x] Many bugs are **wrong assumptions** about a value or its **type**.
- [x] `5 + "5"` concatenates (**`"55"`**). `5 + Number("5")` adds (**10**).
- [x] Check the value. Check the type. Do not guess.

Sandbox: `code_sandbox/js-debugging/string-vs-number.html`

```javascript
let x = 5;
let y = "5";
console.log(x + y);  // 55 (string!)
console.log(x + Number(y));  // 10 (number)
```

<img alt="js-debugging example 3 source" src="./code_sandbox/snaps/js-debugging-03-code.png" />

<img alt="js-debugging example 3 result" src="./code_sandbox/snaps/js-debugging-03-result.png" />

- [x] **Outcome:** First log is **"55"** (string). Second log is **10** (number).

<a id="js-debugging-example-04"></a>

### **Example 4: ReferenceError: myValue is not defined**

- [x] **ReferenceError** means **this name does not exist** (misspelling or never declared).
- [x] The console usually includes a **line number**. Click it to jump to the line.

Sandbox: `code_sandbox/js-debugging/referenceerror-myvalue.html`

```javascript
console.log(myValue);  // ReferenceError: myValue is not defined
```

<img alt="js-debugging example 4 source" src="./code_sandbox/snaps/js-debugging-04-code.png" />

<img alt="js-debugging example 4 result" src="./code_sandbox/snaps/js-debugging-04-result.png" />

- [x] **Outcome:** **ReferenceError: myValue is not defined**. Nothing is logged first — the throw happens immediately.

<a id="js-debugging-example-05"></a>

### **Example 5: TypeError: Cannot read properties of undefined (reading 'length')**

- [x] **TypeError** means you used a value in an **impossible** way.
- [x] `let x;` leaves `x` as **`undefined`**. `undefined` has no **`length`**.

Sandbox: `code_sandbox/js-debugging/typeerror-undefined-length.html`

```javascript
let x;
console.log(x.length);  // TypeError: Cannot read properties of undefined
```

<img alt="js-debugging example 5 source" src="./code_sandbox/snaps/js-debugging-05-code.png" />

<img alt="js-debugging example 5 result" src="./code_sandbox/snaps/js-debugging-05-result.png" />

- [x] **Outcome:** **TypeError: Cannot read properties of undefined (reading 'length')**.

<a id="js-debugging-example-06"></a>

### **Example 6: Mistake: if (x = 5) assigns and always runs**

- [x] `=` **assigns**. `==` / `===` **compare**.
- [x] `if (x = 5)` sets `x` to **5** (truthy) and the block **runs** even when `x` started as **10**.

Sandbox: `code_sandbox/js-debugging/assignment-in-if.html`

```javascript
let x = 10;
if (x = 5) {
  console.log("This runs");
}
```

<img alt="js-debugging example 6 source" src="./code_sandbox/snaps/js-debugging-06-code.png" />

<img alt="js-debugging example 6 result" src="./code_sandbox/snaps/js-debugging-06-result.png" />

- [x] **Outcome:** **log: This runs**. After the `if`, `x` is **5** (not 10).

<a id="js-debugging-example-07"></a>

### **Example 7: Fix: if (x === 5) compares without assigning**

- [x] Use **`===`** (or `==` if you really want coercion).
- [x] With `x = 10`, `if (x === 5)` is **false** — the log **does not run**.

Sandbox: `code_sandbox/js-debugging/strict-equals-in-if.html`

```javascript
let x = 10;
if (x === 5) {
  console.log("This runs only if x is 5");
}
```

<img alt="js-debugging example 7 source" src="./code_sandbox/snaps/js-debugging-07-code.png" />

<img alt="js-debugging example 7 result" src="./code_sandbox/snaps/js-debugging-07-result.png" />

- [x] **Outcome:** No **This runs only if x is 5** line. `x` stays **10**.

<a id="js-debugging-example-08"></a>

### **Example 8: console.log(c) after a + b**

- [x] A tiny script: `a = 5`, `b = 6`, `c = a + b`, then **`console.log(c)`**.
- [x] This is the page’s last Tryit (under browser debugging tools).

Sandbox: `code_sandbox/js-debugging/console-sum.html`

```javascript
let a = 5;
let b = 6;
let c = a + b;
console.log(c);
```

<img alt="js-debugging example 8 source" src="./code_sandbox/snaps/js-debugging-08-code.png" />

<img alt="js-debugging example 8 result" src="./code_sandbox/snaps/js-debugging-08-result.png" />

- [x] **Outcome:** **log: 11**.

<a id="js-debugging-example-09"></a>

### **Example 9: Habit: Read → Reproduce → Reduce → Fix**

- [x] Debugging is **not guessing**. The page’s habit: **Read** the error → **Reproduce** → **Reduce** to a small example → **Fix**.
- [x] Here a **reduced** snippet is `total = price + qty` with `qty` as a **string** — the bug is visible in one log.

Sandbox: `code_sandbox/js-debugging/read-reproduce-reduce-fix.html`

```javascript
let price = 50;
let qty = "3";
let total = price + qty;
console.log("total", total, typeof total);
let fixed = price + Number(qty);
console.log("fixed", fixed, typeof fixed);
```

<img alt="js-debugging example 9 source" src="./code_sandbox/snaps/js-debugging-09-code.png" />

<img alt="js-debugging example 9 result" src="./code_sandbox/snaps/js-debugging-09-result.png" />

- [x] **Outcome:** Broken **total** is **"503"** (string). **fixed** is **53** (number).

<a id="js-debugging-example-10"></a>

### **Example 10: Open the browser console (F12)**

- [x] All modern browsers have a built-in **JavaScript debugger**.
- [x] Usually **F12**, then the **Console** tab. You can also: right-click → **Inspect** → **Console**.
- [x] **Chrome:** More tools → Developer tools → Console. **Firefox:** Web Developer → Web Console. **Edge:** Developer Tools → Console. **Opera:** Developer → Developer tools → Console. **Safari:** Preferences → Advanced → Enable Develop menu, then Develop → Show Error Console.
- [x] If you do **one** thing when code fails: **look at the console**.

Sandbox: `code_sandbox/js-debugging/open-console-f12.html`

```javascript
console.log("F12 then Console");
```

<img alt="js-debugging example 10 source" src="./code_sandbox/snaps/js-debugging-10-code.png" />

<img alt="js-debugging example 10 result" src="./code_sandbox/snaps/js-debugging-10-result.png" />

- [x] **Outcome:** **log: F12 then Console**. The sandbox mirrors DevTools output onto the page so the snap is visible without opening F12.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-debugging/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `console.log("Hello!")` put on the page?

<details>
<summary>Answer</summary>

- [x] **Nothing** in the HTML body.
- [x] The **console** shows **Hello!**.

</details>

### Question 2: What is `50 * 3` in the Total log?

<details>
<summary>Answer</summary>

- [x] **150**.

</details>

### Question 3: What is `5 + "5"` vs `5 + Number("5")`?

<details>
<summary>Answer</summary>

- [x] **`"55"`** (string) vs **10** (number).

</details>

### Question 4: What is `console.log(myValue)`?

<details>
<summary>Answer</summary>

- [x] **ReferenceError: myValue is not defined**.

</details>

### Question 5: What is `(undefined).length`?

<details>
<summary>Answer</summary>

- [x] **TypeError: Cannot read properties of undefined (reading 'length')**.

</details>

### Question 6: Does `if (x = 5)` run when `x` started at 10?

<details>
<summary>Answer</summary>

- [x] **Yes.** It **assigns 5** and the block runs.
- [x] `x` is **5** afterward.

</details>

### Question 7: Does `if (x === 5)` run when `x` is 10?

<details>
<summary>Answer</summary>

- [x] **No.** `x` stays **10**.

</details>

### Question 8: What is `console.log(5 + 6)` in the last Tryit?

<details>
<summary>Answer</summary>

- [x] **11**.

</details>

### Question 9: What is the four-step habit?

<details>
<summary>Answer</summary>

- [x] **Read → Reproduce → Reduce → Fix**.

</details>

### Question 10: How do you open the console in Chrome?

<details>
<summary>Answer</summary>

- [x] **F12**, or More tools → Developer tools → **Console**.
- [x] Or right-click → Inspect → Console.

</details>


</details>

## Summary

Open the console first. Log values and types. ReferenceError is a missing name; TypeError is a bad operation (often undefined). Never use = when you meant ===. Reduce the bug to a tiny snippet, then fix one thing.

## References

- [JS Debugging (W3Schools)](https://www.w3schools.com/js/js_debugging.asp)
- [MDN: console.log()](https://developer.mozilla.org/en-US/docs/Web/API/console/log_static)
- [MDN: ReferenceError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
- [MDN: TypeError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

</details>
