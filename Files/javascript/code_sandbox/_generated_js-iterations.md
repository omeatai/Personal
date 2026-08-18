<details>
  <summary>JS Iterations</summary>

## Introduction

JavaScript loops repeat a block. for uses init / condition / increment when the trip count is known. while and do...while follow a condition — do...while always runs once. for...in walks object keys; for...of walks iterable values. Array forEach is a method alternative. Always increment a while-condition variable or the loop never ends.

This section has **6** examples:

- [x] **Example 1:** for (let i = 0; i < 5; i++) [View](#js-iterations-example-01)
- [x] **Example 2:** while (i < 10) [View](#js-iterations-example-02)
- [x] **Example 3:** do...while (i < 10) [View](#js-iterations-example-03)
- [x] **Example 4:** for...in over a person object [View](#js-iterations-example-04)
- [x] **Example 5:** for...of over an array (table row; no Tryit) [View](#js-iterations-example-05)
- [x] **Example 6:** array.forEach() (table row; no Tryit) [View](#js-iterations-example-06)

## Detailed Explanation

- [x] **`for (exp1; exp2; exp3)`** — init once, test, body, increment.
- [x] **`while`** tests first. **`do...while`** runs the body first (at least once).
- [x] **`for...in`** → enumerable **keys**. **`for...of`** → iterable **values**.
- [x] **`forEach()`** is an Array method (also listed with map / filter / reduce).
- [x] Forgetting to increment a `while` / `do...while` variable is an **infinite loop**.

<a id="js-iterations-example-01"></a>

### **Example 1: for (let i = 0; i < 5; i++)**

- [x] `for` has **init**, **condition**, and **increment**: `for (exp1; exp2; exp3)`.
- [x] Use it when the number of trips is **known** (here: `i` from **0** to **4**).

Sandbox: `code_sandbox/js-iterations/for-loop.html`

```javascript
let text = "";
for (let i = 0; i < 5; i++) {
  text += "The number is " + i + "\n";
}
```

<img alt="js-iterations example 1 source" src="./code_sandbox/snaps/js-iterations-01-code.png" />

<img alt="js-iterations example 1 result" src="./code_sandbox/snaps/js-iterations-01-result.png" />

- [x] **Outcome:** text is five lines: **The number is 0** through **The number is 4**.

<a id="js-iterations-example-02"></a>

### **Example 2: while (i < 10)**

- [x] `while` repeats **as long as** the condition is true.
- [x] **Increment inside** the body. Forgetting that makes an **infinite loop**.

Sandbox: `code_sandbox/js-iterations/while-loop.html`

```javascript
let text = "";
let i = 0;
while (i < 10) {
  text += "The number is " + i + "\n";
  i++;
}
```

<img alt="js-iterations example 2 source" src="./code_sandbox/snaps/js-iterations-02-code.png" />

<img alt="js-iterations example 2 result" src="./code_sandbox/snaps/js-iterations-02-result.png" />

- [x] **Outcome:** Lines **The number is 0** through **The number is 9**. After the loop, `i` is **10**.

<a id="js-iterations-example-03"></a>

### **Example 3: do...while (i < 10)**

- [x] `do...while` runs the body **once before** testing the condition.
- [x] Even a false condition still produces **one** trip. Still increment, or it never ends.

Sandbox: `code_sandbox/js-iterations/do-while-loop.html`

```javascript
let text = "";
let i = 0;
do {
  text += "The number is " + i + "\n";
  i++;
} while (i < 10);
```

<img alt="js-iterations example 3 source" src="./code_sandbox/snaps/js-iterations-03-code.png" />

<img alt="js-iterations example 3 result" src="./code_sandbox/snaps/js-iterations-03-result.png" />

- [x] **Outcome:** Same ten lines **0** through **9**. `i` is **10**. The body ran **before** the first test.

<a id="js-iterations-example-04"></a>

### **Example 4: for...in over a person object**

- [x] `for...in` walks **enumerable keys** of an object (typically **plain objects**).
- [x] `x` is the **key**. `person[x]` is the **value**.

Sandbox: `code_sandbox/js-iterations/for-in-person.html`

```javascript
const person = {fname:"John", lname:"Doe", age:25};
let txt = "";
for (let x in person) {
  txt += person[x] + " ";
}
```

<img alt="js-iterations example 4 source" src="./code_sandbox/snaps/js-iterations-04-code.png" />

<img alt="js-iterations example 4 result" src="./code_sandbox/snaps/js-iterations-04-result.png" />

- [x] **Outcome:** txt is **"John Doe 25 "** (keys `fname`, `lname`, `age` in that order here).

<a id="js-iterations-example-05"></a>

### **Example 5: for...of over an array (table row; no Tryit)**

- [x] `for...of` walks **values** of an **iterable** (arrays, strings, Maps, Sets).
- [x] No Tryit on this page — the next chapter is **JS Iterables**. Still run one array loop.

Sandbox: `code_sandbox/js-iterations/for-of-array.html`

```javascript
const cars = ["BMW", "Volvo", "Saab", "Ford"];
let text = "";
for (const car of cars) {
  text += car + "\n";
}
```

<img alt="js-iterations example 5 source" src="./code_sandbox/snaps/js-iterations-05-code.png" />

<img alt="js-iterations example 5 result" src="./code_sandbox/snaps/js-iterations-05-result.png" />

- [x] **Outcome:** text is **BMW**, **Volvo**, **Saab**, **Ford** (one per line) — the **values**, not indexes.

<a id="js-iterations-example-06"></a>

### **Example 6: array.forEach() (table row; no Tryit)**

- [x] `forEach()` is an **Array** method: one callback per element.
- [x] Listed under **Other Methods** with `map` / `filter` / `reduce`. No Tryit on this page.

Sandbox: `code_sandbox/js-iterations/foreach-array.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let text = "";
numbers.forEach(function (value) {
  text += value + "\n";
});
```

<img alt="js-iterations example 6 source" src="./code_sandbox/snaps/js-iterations-06-code.png" />

<img alt="js-iterations example 6 result" src="./code_sandbox/snaps/js-iterations-06-result.png" />

- [x] **Outcome:** text is **45**, **4**, **9**, **16**, **25** (one per line).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-iterations/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: When do you use `for` vs `while`?

<details>
<summary>Answer</summary>

- [x] **`for`** when the count is known (init / test / increment).
- [x] **`while`** when you keep going while a condition stays true.

</details>

### Question 2: What are exp1, exp2, exp3 in `for`?

<details>
<summary>Answer</summary>

- [x] **exp1** runs once (init).
- [x] **exp2** is the continue condition.
- [x] **exp3** runs after each body (usually increment).

</details>

### Question 3: What does the page’s `for` Tryit print?

<details>
<summary>Answer</summary>

- [x] **The number is 0** through **The number is 4**.

</details>

### Question 4: What does the `while (i < 10)` Tryit print?

<details>
<summary>Answer</summary>

- [x] **0** through **9**. After the loop `i` is **10**.

</details>

### Question 5: How is `do...while` different from `while`?

<details>
<summary>Answer</summary>

- [x] The body runs **before** the test, so it always runs **at least once**.

</details>

### Question 6: What does `for...in` on `{fname, lname, age}` build?

<details>
<summary>Answer</summary>

- [x] **"John Doe 25 "** — values of those keys, space-separated.

</details>

### Question 7: What does `for...of` iterate?

<details>
<summary>Answer</summary>

- [x] **Values** of an **iterable** (arrays, strings, Maps, Sets) — not object keys.

</details>

### Question 8: What did the extra `forEach` print?

<details>
<summary>Answer</summary>

- [x] **45, 4, 9, 16, 25** (one per line).

</details>

### Question 9: What happens if you forget to increment in `while`?

<details>
<summary>Answer</summary>

- [x] The condition never becomes false — **infinite loop** (can freeze the page).

</details>

### Question 10: Is `forEach` a loop keyword?

<details>
<summary>Answer</summary>

- [x] **No.** It is **`Array.prototype.forEach`**, listed under other methods on this page.

</details>


</details>

## Summary

Pick for when the trip count is known, while/do...while for a condition (do runs once first), for...in for object keys, and for...of / forEach for values. Always advance the condition variable.

## References

- [JS Iterations (W3Schools)](https://www.w3schools.com/js/js_looping.asp)
- [MDN: Loops and iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)
- [MDN: for...of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)

</details>
