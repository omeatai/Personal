# JS Loop for

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The **`for`** statement creates a loop with **three optional expressions**: initialize, condition, and update. Omit any of them when you set or increment the counter **outside** the header — but if you omit the **condition**, you must **`break`** or the loop never ends.

This section has **6** examples:

- [x] **Example 1:** `for` i < 5 numbers [View](#js-loop-for-example-01)
- [x] **Example 2:** `for` collect car names [View](#js-loop-for-example-02)
- [x] **Example 3:** Omit exp1 (`i = 2` before the loop) [View](#js-loop-for-example-03)
- [x] **Example 4:** Omit exp3 (`i++` inside the body) [View](#js-loop-for-example-04)
- [x] **Example 5:** `var i` in the loop leaks (i is 10 after) [View](#js-loop-for-example-05)
- [x] **Example 6:** `let i` in the loop does not leak (outer i stays 5) [View](#js-loop-for-example-06)

## Detailed Explanation

- [x] **`for (exp1; exp2; exp3)`** — init, test, update. All three are optional; keep the **semicolons**.
- [x] **Omit exp1** — set `i` first (`i = 2` starts at Saab). **Omit exp3** — increment in the body.
- [x] **Omit exp2** only with **`break`**, or the loop never ends (do **not** demo that).
- [x] **`var i` leaks**; **`let i` does not.** After the `var` loop, `i` is **10**; after the `let` loop, outer `i` stays **5**.

<a id="js-loop-for-example-01"></a>

### **Example 1: `for` i < 5 numbers**

- [x] `for (exp1; exp2; exp3)` — **exp1** once before (`let i = 0`), **exp2** condition (`i < 5`), **exp3** after each pass (`i++`).
- [x] If exp2 is **false**, the loop **ends**. **i = 5** is not printed.
- [x] All three expressions are **optional** (later Examples omit exp1 or exp3).

Sandbox: `code_sandbox/js-loop-for/for-numbers.html`

```javascript
let text = "";
for (let i = 0; i < 5; i++) {
  text += "The number is " + i + "\n";
}
```

![js-loop-for example 1 source](../code_sandbox/snaps/js-loop-for-01-code.png)

![js-loop-for example 1 result](../code_sandbox/snaps/js-loop-for-01-result.png)

- [x] **Outcome:** The text is **The number is 0 The number is 1 The number is 2 The number is 3 The number is 4**.

<a id="js-loop-for-example-02"></a>

### **Example 2: `for` collect car names**

- [x] `const cars = ["BMW", "Volvo", "Saab", "Ford"]` — **four** names (this page does not use Fiat/Audi).
- [x] `let len = cars.length` then `for (let i = 0; i < len; i++) { text += cars[i]; }`.
- [x] The page concatenates **with no spaces**, so the string is **BMWVolvoSaabFord**.

Sandbox: `code_sandbox/js-loop-for/for-cars.html`

```javascript
const cars = ["BMW", "Volvo", "Saab", "Ford"];
let len = cars.length;
let text = "";
for (let i = 0; i < len; i++) {
  text += cars[i];
}
```

![js-loop-for example 2 source](../code_sandbox/snaps/js-loop-for-02-code.png)

![js-loop-for example 2 result](../code_sandbox/snaps/js-loop-for-02-result.png)

- [x] **Outcome:** The collected string is **BMWVolvoSaabFord** (no spaces). **len** is **4**.

<a id="js-loop-for-example-03"></a>

### **Example 3: Omit exp1 (`i = 2` before the loop)**

- [x] **exp1 is optional.** Set the counter **before** the loop, then write `for (; i < len; i++)`.
- [x] Keep the **semicolons**. The first slot is empty.
- [x] Starting at **`i = 2`** skips BMW and Volvo and walks from **Saab** onward.

Sandbox: `code_sandbox/js-loop-for/omit-exp1.html`

```javascript
const cars = ["BMW", "Volvo", "Saab", "Ford"];
let len = cars.length;
let i = 2;
let text = "";
for (; i < len; i++) {
  text += cars[i] + " ";
}
```

![js-loop-for example 3 source](../code_sandbox/snaps/js-loop-for-03-code.png)

![js-loop-for example 3 result](../code_sandbox/snaps/js-loop-for-03-result.png)

- [x] **Outcome:** Starting at index **2** collects **Saab Ford**.

<a id="js-loop-for-example-04"></a>

### **Example 4: Omit exp3 (`i++` inside the body)**

- [x] **exp3 is optional.** You can increment **inside** the body: `for (; i < len; ) { ... i++; }`.
- [x] exp3 can also be `i--`, `i = i + 15`, or anything else — this demo uses `i++` in the body.
- [x] If you omit **exp2** (the condition) you **must `break`**, or the loop never ends. This Example keeps `i < len`.

Sandbox: `code_sandbox/js-loop-for/omit-exp3.html`

```javascript
const cars = ["BMW", "Volvo", "Saab", "Ford"];
let len = cars.length;
let i = 0;
let text = "";
for (; i < len; ) {
  text += cars[i] + " ";
  i++;
}
```

![js-loop-for example 4 source](../code_sandbox/snaps/js-loop-for-04-code.png)

![js-loop-for example 4 result](../code_sandbox/snaps/js-loop-for-04-result.png)

- [x] **Outcome:** Incrementing inside the body still collects **BMW Volvo Saab Ford**.

<a id="js-loop-for-example-05"></a>

### **Example 5: `var i` in the loop leaks (i is 10 after)**

- [x] `var` is **function-scoped** (or global), not block-scoped.
- [x] `var i = 5` then `for (var i = 0; i < 10; i++)` **redeclares the same** `i`.
- [x] After the loop, **`i` is 10** — the loop counter **leaked** out.

Sandbox: `code_sandbox/js-loop-for/var-leaks.html`

```javascript
var i = 5;
for (var i = 0; i < 10; i++) {
  // some code
}
// Here i is 10
```

![js-loop-for example 5 source](../code_sandbox/snaps/js-loop-for-05-code.png)

![js-loop-for example 5 result](../code_sandbox/snaps/js-loop-for-05-result.png)

- [x] **Outcome:** **var i** started at **5** and is **10** after the loop — the header `var i` leaked.

<a id="js-loop-for-example-06"></a>

### **Example 6: `let i` in the loop does not leak (outer i stays 5)**

- [x] `let i` in the header is **loop-scoped**. It does **not** redeclare an outer `let i`.
- [x] Outer `let i = 5` stays **5** after `for (let i = 0; i < 10; i++)`.
- [x] The loop `i` is visible **only inside** the loop. Prefer **`let`** (or `const` when the binding does not reassign) over `var`.

Sandbox: `code_sandbox/js-loop-for/let-no-leak.html`

```javascript
let i = 5;
for (let i = 0; i < 10; i++) {
  // some code
}
// Here i is 5
```

![js-loop-for example 6 source](../code_sandbox/snaps/js-loop-for-06-code.png)

![js-loop-for example 6 result](../code_sandbox/snaps/js-loop-for-06-result.png)

- [x] **Outcome:** Outer **let i** stays **5**. The loop `let i` did **not** leak.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-loop-for/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What numbers does `for (let i = 0; i < 5; i++)` append?

<details>
<summary>Answer</summary>

- [x] **The number is 0** through **The number is 4**.

</details>

### Question 2: What string does the cars collector build with `text += cars[i]` (no spaces)?

<details>
<summary>Answer</summary>

- [x] **BMWVolvoSaabFord**.
- [x] `len` is **4**.

</details>

### Question 3: If you omit exp1 and start at `i = 2`, which cars are collected?

<details>
<summary>Answer</summary>

- [x] **Saab Ford**.
- [x] Indexes 0 and 1 (BMW, Volvo) are skipped.

</details>

### Question 4: If you omit exp3 and write `i++` in the body, what text do you get?

<details>
<summary>Answer</summary>

- [x] **BMW Volvo Saab Ford**.
- [x] exp3 is optional as long as something still advances `i`.

</details>

### Question 5: After `var i = 5` and `for (var i = 0; i < 10; i++)`, what is `i`?

<details>
<summary>Answer</summary>

- [x] **10**.
- [x] `var` in the header **redeclares** the same function-scoped `i`.

</details>

### Question 6: After `let i = 5` and `for (let i = 0; i < 10; i++)`, what is the outer `i`?

<details>
<summary>Answer</summary>

- [x] **5**.
- [x] Loop `let i` is visible **only inside** the loop.

</details>

### Question 7: Are the three `for` expressions required?

<details>
<summary>Answer</summary>

- [x] **No.** All three are **optional**.
- [x] If you omit **exp2**, you must **`break`** or the loop never ends.

</details>

### Question 8: What is exp1 used for?

<details>
<summary>Answer</summary>

- [x] To **initialize** the loop variable(s), e.g. `let i = 0`.
- [x] You can set `i` **before** the loop and leave exp1 empty.

</details>

### Question 9: What can exp3 do besides `i++`?

<details>
<summary>Answer</summary>

- [x] Negative increment (`i--`).
- [x] Larger steps (`i = i + 15`).
- [x] Or increment **inside** the body and omit exp3.

</details>

### Question 10: Where is a `let i` declared in the `for` header visible?

<details>
<summary>Answer</summary>

- [x] **Only inside** the loop.

</details>

</details>

## Summary

`for` prints **0–4**, collects **BMWVolvoSaabFord**, starts at index **2** for **Saab Ford**, and still works when **`i++` is in the body**. **`var i` leaks to 10**; **`let i` keeps outer i at 5**. Omit the condition only if you **`break`**.

## References

- [JS Loop for (W3Schools)](https://www.w3schools.com/js/js_loop_for.asp)
- [MDN: for](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
- [MDN: let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
- [MDN: var](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
