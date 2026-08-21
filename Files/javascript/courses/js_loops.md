# JS Loops

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

**Loops** run a block **many times**, usually with a **different value** each pass. They replace copy-paste when you walk an **array**. This overview covers **`for`**, **loop scope** with `let`, **`while`**, and **`do while`**.

This section has **6** examples:

- [x] **Example 1:** `for` over a cars array [View](#js-loops-example-01)
- [x] **Example 2:** `for` i < 5 — "The number is i" [View](#js-loops-example-02)
- [x] **Example 3:** Loop scope: outer `let i = 5`, loop reuses `i` (i is 10 after) [View](#js-loops-example-03)
- [x] **Example 4:** Loop scope: inner `let i` (outer i stays 5) [View](#js-loops-example-04)
- [x] **Example 5:** `while` i < 10 [View](#js-loops-example-05)
- [x] **Example 6:** `do while` i < 10 (runs at least once) [View](#js-loops-example-06)

## Detailed Explanation

- [x] **Why loops** — same code, over and over; typical with **arrays** instead of `cars[0]` … `cars[5]`.
- [x] **`for (expr1; expr2; expr3)`** — init once, test, then update after each pass.
- [x] **Loop scope** — a header `let i` is **only** visible in the loop; reusing an outer `i` **does** change that outer `i`.
- [x] **`while`** tests then runs. **`do while`** runs then tests (**at least once**). Always **`i++`** (or equivalent) or the loop never ends — do **not** demo an infinite loop.

<a id="js-loops-example-01"></a>

### **Example 1: `for` over a cars array**

- [x] Loops run the **same block many times**, usually with a **different value** each pass.
- [x] Instead of `text += cars[0]` … `cars[5]`, use `for (let i = 0; i < cars.length; i++)`.
- [x] This array has **six** names (indexes **0–5**), matching the page’s `cars[0]` … `cars[5]` copy-paste.
- [x] `cars.length` is **6**, so `i < cars.length` visits every element once.

Sandbox: `code_sandbox/js-loops/for-cars.html`

```javascript
const cars = ["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi"];
let text = "";
for (let i = 0; i < cars.length; i++) {
  text += cars[i] + " ";
}
```

![js-loops example 1 source](../code_sandbox/snaps/js-loops-01-code.png)

![js-loops example 1 result](../code_sandbox/snaps/js-loops-01-result.png)

- [x] **Outcome:** The loop concatenates all six names: **BMW Volvo Saab Ford Fiat Audi**.

<a id="js-loops-example-02"></a>

### **Example 2: `for` i < 5 — "The number is i"**

- [x] `for (expr1; expr2; expr3)` — **expr1** once before, **expr2** the condition, **expr3** after each pass.
- [x] `let i = 0` starts the counter. `i < 5` keeps going while i is 0, 1, 2, 3, 4. `i++` steps by one.
- [x] **i = 5** is **not** printed: when `i < 5` becomes false, the loop **ends**.

Sandbox: `code_sandbox/js-loops/for-numbers.html`

```javascript
let text = "";
for (let i = 0; i < 5; i++) {
  text += "The number is " + i + "\n";
}
```

![js-loops example 2 source](../code_sandbox/snaps/js-loops-02-code.png)

![js-loops example 2 result](../code_sandbox/snaps/js-loops-02-result.png)

- [x] **Outcome:** The joined text is **The number is 0 The number is 1 The number is 2 The number is 3 The number is 4**.

<a id="js-loops-example-03"></a>

### **Example 3: Loop scope: outer `let i = 5`, loop reuses `i` (i is 10 after)**

- [x] `let i = 5` is declared **outside**. The header `for (i = 0; i < 10; i++)` **reuses** that same `i` (no second `let`).
- [x] The loop assigns `i = 0`, then increments until the condition fails.
- [x] When `i` becomes **10**, `i < 10` is false. After the loop, the **outer** `i` is **10**.

Sandbox: `code_sandbox/js-loops/scope-reuse.html`

```javascript
let i = 5;
for (i = 0; i < 10; i++) {
  // some code
}
// Here i is 10
```

![js-loops example 3 source](../code_sandbox/snaps/js-loops-03-code.png)

![js-loops example 3 result](../code_sandbox/snaps/js-loops-03-result.png)

- [x] **Outcome:** Outer **i** started at **5**. After `for (i = 0; i < 10; i++)`, **i is 10**.

<a id="js-loops-example-04"></a>

### **Example 4: Loop scope: inner `let i` (outer i stays 5)**

- [x] `for (let i = 0; i < 10; i++)` declares a **new** `i` that exists **only inside** the loop.
- [x] The outer `let i = 5` is a **different** binding. The loop does **not** change it.
- [x] `let` / `const` declared **inside** a loop (including the header) are **loop-scoped**.

Sandbox: `code_sandbox/js-loops/scope-inner-let.html`

```javascript
let i = 5;
for (let i = 0; i < 10; i++) {
  // some code
}
// Here i is 5
```

![js-loops example 4 source](../code_sandbox/snaps/js-loops-04-code.png)

![js-loops example 4 result](../code_sandbox/snaps/js-loops-04-result.png)

- [x] **Outcome:** After the loop, the **outer** `i` is still **5**. The header `let i` was loop-scoped.

<a id="js-loops-example-05"></a>

### **Example 5: `while` i < 10**

- [x] **`while (condition) { ... }`** tests **first**, then maybe runs the block.
- [x] Initialize **`i = 0`**, append text, then **`i++`**. The page warns: if you **forget `i++`**, the loop **never ends** and can **crash the browser**. This demo **does** increment.
- [x] Numbers printed: **0 through 9** (not 10).

Sandbox: `code_sandbox/js-loops/while.html`

```javascript
let i = 0;
let text = "";
while (i < 10) {
  text += "The number is " + i + "\n";
  i++;
}
```

![js-loops example 5 source](../code_sandbox/snaps/js-loops-05-code.png)

![js-loops example 5 result](../code_sandbox/snaps/js-loops-05-result.png)

- [x] **Outcome:** The loop prints **The number is 0** … **The number is 9**. After it ends, **i is 10**. Forgetting `i++` would infinite-loop — do **not** run that.

<a id="js-loops-example-06"></a>

### **Example 6: `do while` i < 10 (runs at least once)**

- [x] **`do { ... } while (condition);`** runs the block **once first**, then tests.
- [x] It therefore runs **at least once**, even if the condition starts **false**.
- [x] With `i = 0` you still get 0–9. The sandbox also starts at **10** to prove the extra first pass: it prints **The number is 10** once.
- [x] Still increment the counter. Forgetting `i++` never ends — mentioned only, not executed.

Sandbox: `code_sandbox/js-loops/do-while.html`

```javascript
let i = 0;
let text = "";
do {
  text += "The number is " + i + "\n";
  i++;
} while (i < 10);
```

![js-loops example 6 source](../code_sandbox/snaps/js-loops-06-code.png)

![js-loops example 6 result](../code_sandbox/snaps/js-loops-06-result.png)

- [x] **Outcome:** Start **0** prints **The number is 0** … **The number is 9**. Start **10** still runs **once** → **The number is 10**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-loops/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Why use a `for` loop over `cars` instead of writing `cars[0]` through `cars[5]`?

<details>
<summary>Answer</summary>

- [x] To run the **same** code for **each** element.
- [x] The sandbox result is **BMW Volvo Saab Ford Fiat Audi**.

</details>

### Question 2: What numbers does `for (let i = 0; i < 5; i++)` print in "The number is i"?

<details>
<summary>Answer</summary>

- [x] **0 1 2 3 4**.
- [x] **5** is not printed because `i < 5` is then false.

</details>

### Question 3: After `let i = 5` and `for (i = 0; i < 10; i++)`, what is `i`?

<details>
<summary>Answer</summary>

- [x] **10**.
- [x] The loop reused the **outer** `i` until `i < 10` failed.

</details>

### Question 4: After `let i = 5` and `for (let i = 0; i < 10; i++)`, what is the outer `i`?

<details>
<summary>Answer</summary>

- [x] **5**.
- [x] The inner `let i` is **loop-scoped** and does not change the outer binding.

</details>

### Question 5: What values does `while (i < 10)` print when `i` starts at 0?

<details>
<summary>Answer</summary>

- [x] **The number is 0** through **The number is 9**.
- [x] After the loop, `i` is **10**.

</details>

### Question 6: What happens if you forget `i++` in a `while`?

<details>
<summary>Answer</summary>

- [x] The condition stays true and the loop **never ends**.
- [x] That can **crash the browser**. The sandbox always increments.

</details>

### Question 7: How does `do while` differ from `while` when the condition starts false?

<details>
<summary>Answer</summary>

- [x] **`do while`** still runs the block **once**, then tests.
- [x] Start **10** still prints **The number is 10** once.

</details>

### Question 8: What do expr1, expr2, and expr3 mean in a `for` header?

<details>
<summary>Answer</summary>

- [x] **expr1** runs **once** before the loop (initialize).
- [x] **expr2** is the **condition** to keep looping.
- [x] **expr3** runs **after each** iteration (usually increment).

</details>

### Question 9: Are `let` / `const` declared inside a loop visible after the loop?

<details>
<summary>Answer</summary>

- [x] **No.** They are visible **only in the loop**.

</details>

### Question 10: Does `i < 5` include `i === 5`?

<details>
<summary>Answer</summary>

- [x] **No.** The loop stops when the condition is **false**.
- [x] Printed numbers are **0–4**.

</details>

</details>

## Summary

Loops repeat a block: **`for`** walks **BMW … Audi** and prints **The number is 0–4**. Reusing outer `i` leaves **i = 10**; inner `let i` leaves outer **i = 5**. **`while`** prints 0–9; **`do while`** does too and still runs once if `i` starts at 10. Always update the counter or the loop never ends.

## References

- [JS Loops (W3Schools)](https://www.w3schools.com/js/js_loops.asp)
- [MDN: for](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
- [MDN: while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
- [MDN: do...while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
