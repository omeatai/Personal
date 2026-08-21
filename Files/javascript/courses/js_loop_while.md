# JS Loop while

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

**While loops** run a block **as long as a condition is true**. JavaScript has **`while`** (test first) and **`do while`** (run first). A `while` is like a `for` with statement 1 and 3 omitted. Forgetting **`i++`** infinite-loops — the warning is in the bullets; the sandbox never omits the increment.

This section has **4** examples:

- [x] **Example 1:** `while` i < 10 [View](#js-loop-while-example-01)
- [x] **Example 2:** `do while` i < 10 [View](#js-loop-while-example-02)
- [x] **Example 3:** `for (; cars[i]; )` collect cars [View](#js-loop-while-example-03)
- [x] **Example 4:** `while (cars[i])` collect cars [View](#js-loop-while-example-04)

## Detailed Explanation

- [x] **`while`** — test, then maybe run. **`do while`** — run once, then test (**at least once**).
- [x] **Always increment** the condition variable. Do **not** run a loop that forgets `i++`.
- [x] **`for (; cars[i]; )`** and **`while (cars[i])`** are the same idea: stop when the next slot is falsy.

<a id="js-loop-while-example-01"></a>

### **Example 1: `while` i < 10**

- [x] JavaScript has two while-style loops: **`while`** and **`do while`**.
- [x] `while (condition)` tests **first**. With `i = 0` and `i++` in the body you get **0–9**.
- [x] **Warning:** forgetting **`i++`** means the loop **never ends** and can **crash the browser**. Mentioned only — this script increments.

Sandbox: `code_sandbox/js-loop-while/while.html`

```javascript
let i = 0;
let text = "";
while (i < 10) {
  text += "The number is " + i + "\n";
  i++;
}
```

![js-loop-while example 1 source](../code_sandbox/snaps/js-loop-while-01-code.png)

![js-loop-while example 1 result](../code_sandbox/snaps/js-loop-while-01-result.png)

- [x] **Outcome:** **The number is 0** through **The number is 9**. After the loop, **i is 10**.

<a id="js-loop-while-example-02"></a>

### **Example 2: `do while` i < 10**

- [x] `do { ... } while (condition);` runs the block **before** the test, so it runs **at least once**.
- [x] Start **0** still prints 0–9. Start **10** (condition already false) still prints **The number is 10** once.
- [x] Do not forget `i++` here either — infinite loops are described, not executed.

Sandbox: `code_sandbox/js-loop-while/do-while.html`

```javascript
let i = 0;
let text = "";
do {
  text += "The number is " + i + "\n";
  i++;
} while (i < 10);
```

![js-loop-while example 2 source](../code_sandbox/snaps/js-loop-while-02-code.png)

![js-loop-while example 2 result](../code_sandbox/snaps/js-loop-while-02-result.png)

- [x] **Outcome:** Start **0** → **The number is 0** … **The number is 9**. Start **10** still runs once → **The number is 10**.

<a id="js-loop-while-example-03"></a>

### **Example 3: `for (; cars[i]; )` collect cars**

- [x] A `while` is like a `for` with **statement 1 and 3 omitted**.
- [x] `for (; cars[i]; )` uses the **array value** as the condition: truthy names keep going; **`undefined`** past the end is falsy and **stops**.
- [x] `i++` lives in the body. Cars: BMW, Volvo, Saab, Ford (concatenated with **no spaces** on this page).

Sandbox: `code_sandbox/js-loop-while/for-cars-cond.html`

```javascript
const cars = ["BMW", "Volvo", "Saab", "Ford"];
let i = 0;
let text = "";
for (; cars[i]; ) {
  text += cars[i];
  i++;
}
```

![js-loop-while example 3 source](../code_sandbox/snaps/js-loop-while-03-code.png)

![js-loop-while example 3 result](../code_sandbox/snaps/js-loop-while-03-result.png)

- [x] **Outcome:** The `for (; cars[i]; )` collector builds **BMWVolvoSaabFord** and stops when `cars[i]` is **undefined** (`i` is **4**).

<a id="js-loop-while-example-04"></a>

### **Example 4: `while (cars[i])` collect cars**

- [x] Same walk as the previous Example, written as **`while (cars[i])`**.
- [x] No `cars.length` check is required in this pattern: it stops on the first **falsy** slot (`undefined` after the last name).
- [x] Result matches the `for (; cars[i]; )` version: **BMWVolvoSaabFord**.

Sandbox: `code_sandbox/js-loop-while/while-cars.html`

```javascript
const cars = ["BMW", "Volvo", "Saab", "Ford"];
let i = 0;
let text = "";
while (cars[i]) {
  text += cars[i];
  i++;
}
```

![js-loop-while example 4 source](../code_sandbox/snaps/js-loop-while-04-code.png)

![js-loop-while example 4 result](../code_sandbox/snaps/js-loop-while-04-result.png)

- [x] **Outcome:** `while (cars[i])` also builds **BMWVolvoSaabFord** and stops at **i = 4**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-loop-while/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are the two while-style loops?

<details>
<summary>Answer</summary>

- [x] **`while`**
- [x] **`do while`**

</details>

### Question 2: What does `while (i < 10)` print when `i` starts at 0?

<details>
<summary>Answer</summary>

- [x] **The number is 0** through **The number is 9**.
- [x] Afterward `i` is **10**.

</details>

### Question 3: When does `do while` run if the condition is already false?

<details>
<summary>Answer</summary>

- [x] It still runs the block **once**.
- [x] Start **10** prints **The number is 10** once.

</details>

### Question 4: How is `while` like `for`?

<details>
<summary>Answer</summary>

- [x] Like a `for` with **statement 1 and 3 omitted**.
- [x] `for (; cars[i]; )` vs `while (cars[i])`.

</details>

### Question 5: What string does `for (; cars[i]; )` build from BMW, Volvo, Saab, Ford?

<details>
<summary>Answer</summary>

- [x] **BMWVolvoSaabFord**.
- [x] It stops when `cars[i]` is **undefined** (`i === 4`).

</details>

### Question 6: What string does `while (cars[i])` build from the same array?

<details>
<summary>Answer</summary>

- [x] **BMWVolvoSaabFord** — the same result.
- [x] No `length` check is required in this pattern.

</details>

### Question 7: What happens if you never increment `i` in a `while`?

<details>
<summary>Answer</summary>

- [x] The loop **never ends**.
- [x] That can **crash the browser**. The examples always `i++`.

</details>

### Question 8: Does `while (cars[i])` need `cars.length`?

<details>
<summary>Answer</summary>

- [x] **No** in this pattern: it stops when `cars[i]` is **falsy** (`undefined` past the end).

</details>

### Question 9: Why does `cars[4]` stop the collector?

<details>
<summary>Answer</summary>

- [x] There is no index 4, so `cars[4]` is **`undefined`**, which is falsy.

</details>

### Question 10: Does `do while` need a semicolon after `while (condition)`?

<details>
<summary>Answer</summary>

- [x] **Yes.** The syntax is `do { ... } while (condition);`.

</details>

</details>

## Summary

**`while`** tests then runs (0–9). **`do while`** runs then tests (at least once — start 10 still prints once). **`for (; cars[i]; )`** and **`while (cars[i])`** both collect **BMWVolvoSaabFord**. Always change the counter; never demo an infinite loop.

## References

- [JS Loop while (W3Schools)](https://www.w3schools.com/js/js_loop_while.asp)
- [MDN: while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
- [MDN: do...while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
