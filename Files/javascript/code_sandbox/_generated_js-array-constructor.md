<details>
  <summary>JS Array Constructor</summary>

## Introduction

The Array constructor creates an Array object. new Array() and Array() are the same: if you forget new, the function puts it back. A single numeric argument is a length (empty slots), not an element — that is the dangerous case. A single non-number, or any list of two or more arguments, becomes elements. An array literal avoids the trap: [40] is one number, new Array(40) is forty holes.

This section has **14** examples:

- [x] **Example 1:** new Array() — empty [View](#js-array-constructor-example-01)
- [x] **Example 2:** new Array(3) — three empty spots [View](#js-array-constructor-example-02)
- [x] **Example 3:** new Array("3") — one string element [View](#js-array-constructor-example-03)
- [x] **Example 4:** new Array("Saab", "Volvo", "BMW") [View](#js-array-constructor-example-04)
- [x] **Example 5:** Array() without new — empty [View](#js-array-constructor-example-05)
- [x] **Example 6:** Array(3) without new — three empty spots [View](#js-array-constructor-example-06)
- [x] **Example 7:** Array("3") without new [View](#js-array-constructor-example-07)
- [x] **Example 8:** Array("Saab", "Volvo", "BMW") without new [View](#js-array-constructor-example-08)
- [x] **Example 9:** Six numbers: new Array vs [] [View](#js-array-constructor-example-09)
- [x] **Example 10:** new Array(40, 100, 1) — three elements [View](#js-array-constructor-example-10)
- [x] **Example 11:** new Array(40, 100) — two elements [View](#js-array-constructor-example-11)
- [x] **Example 12:** WARNING new Array(40) — 40 empty slots [View](#js-array-constructor-example-12)
- [x] **Example 13:** [40] — one element [View](#js-array-constructor-example-13)
- [x] **Example 14:** Array literal (preferred) [View](#js-array-constructor-example-14)

## Detailed Explanation

- [x] `new Array()` and `Array()` are **functionally the same**.
- [x] `new Array(n)` for a number `n` makes **n empty slots**, not `[n]`.
- [x] `new Array("3")` is **["3"]** — a string is not a length.
- [x] Two or more arguments are **elements**: `new Array(40, 100, 1)` is `[40,100,1]`.
- [x] Prefer **`[]`**. It is clearer and skips the single-number trap.
- [x] `JSON.stringify` shows holes as **null**, but `0 in a` is **false**.

<a id="js-array-constructor-example-01"></a>

### **Example 1: new Array() — empty**

- [x] `new Array()` with **no arguments** creates an empty array.

Sandbox: `code_sandbox/js-array-constructor/new-array-empty.html`

```javascript
const a = new Array();
```

<img alt="js-array-constructor example 1 source" src="./code_sandbox/snaps/js-array-constructor-01-code.png" />

<img alt="js-array-constructor example 1 result" src="./code_sandbox/snaps/js-array-constructor-01-result.png" />

- [x] **Outcome:** **[]**. length **0**.

<a id="js-array-constructor-example-02"></a>

### **Example 2: new Array(3) — three empty spots**

- [x] A **single number** is a length, not an element. Dangerous special case.
- [x] `JSON.stringify` shows holes as **null**, but `0 in a` is **false**.

Sandbox: `code_sandbox/js-array-constructor/new-array-3.html`

```javascript
const a = new Array(3);
```

<img alt="js-array-constructor example 2 source" src="./code_sandbox/snaps/js-array-constructor-02-code.png" />

<img alt="js-array-constructor example 2 result" src="./code_sandbox/snaps/js-array-constructor-02-result.png" />

- [x] **Outcome:** JSON **[null,null,null]**. length **3**. `0 in a` is **false** (empty slots, not nulls).

<a id="js-array-constructor-example-03"></a>

### **Example 3: new Array("3") — one string element**

- [x] A **non-number** single argument is **one element**, not a length.

Sandbox: `code_sandbox/js-array-constructor/new-array-string-3.html`

```javascript
const a = new Array("3");
```

<img alt="js-array-constructor example 3 source" src="./code_sandbox/snaps/js-array-constructor-03-code.png" />

<img alt="js-array-constructor example 3 result" src="./code_sandbox/snaps/js-array-constructor-03-result.png" />

- [x] **Outcome:** **["3"]**. length **1**.

<a id="js-array-constructor-example-04"></a>

### **Example 4: new Array("Saab", "Volvo", "BMW")**

- [x] Multiple arguments become **elements**.

Sandbox: `code_sandbox/js-array-constructor/new-array-three-cars.html`

```javascript
const a = new Array("Saab", "Volvo", "BMW");
```

<img alt="js-array-constructor example 4 source" src="./code_sandbox/snaps/js-array-constructor-04-code.png" />

<img alt="js-array-constructor example 4 result" src="./code_sandbox/snaps/js-array-constructor-04-result.png" />

- [x] **Outcome:** **["Saab","Volvo","BMW"]**.

<a id="js-array-constructor-example-05"></a>

### **Example 5: Array() without new — empty**

- [x] `Array()` and `new Array()` do the **same** thing.
- [x] If you omit `new`, the function adds it behind the scenes.

Sandbox: `code_sandbox/js-array-constructor/array-fn-empty.html`

```javascript
const a = Array();
```

<img alt="js-array-constructor example 5 source" src="./code_sandbox/snaps/js-array-constructor-05-code.png" />

<img alt="js-array-constructor example 5 result" src="./code_sandbox/snaps/js-array-constructor-05-result.png" />

- [x] **Outcome:** **[]**. length **0**.

<a id="js-array-constructor-example-06"></a>

### **Example 6: Array(3) without new — three empty spots**

- [x] Same length trap **without** `new`.

Sandbox: `code_sandbox/js-array-constructor/array-fn-3.html`

```javascript
const a = Array(3);
```

<img alt="js-array-constructor example 6 source" src="./code_sandbox/snaps/js-array-constructor-06-code.png" />

<img alt="js-array-constructor example 6 result" src="./code_sandbox/snaps/js-array-constructor-06-result.png" />

- [x] **Outcome:** JSON **[null,null,null]**. length **3**. `0 in a` is **false**.

<a id="js-array-constructor-example-07"></a>

### **Example 7: Array("3") without new**

- [x] One string argument is still **one element**.

Sandbox: `code_sandbox/js-array-constructor/array-fn-string-3.html`

```javascript
const a = Array("3");
```

<img alt="js-array-constructor example 7 source" src="./code_sandbox/snaps/js-array-constructor-07-code.png" />

<img alt="js-array-constructor example 7 result" src="./code_sandbox/snaps/js-array-constructor-07-result.png" />

- [x] **Outcome:** **["3"]**.

<a id="js-array-constructor-example-08"></a>

### **Example 8: Array("Saab", "Volvo", "BMW") without new**

- [x] Multiple arguments without `new` still build that list.

Sandbox: `code_sandbox/js-array-constructor/array-fn-three-cars.html`

```javascript
const a = Array("Saab", "Volvo", "BMW");
```

<img alt="js-array-constructor example 8 source" src="./code_sandbox/snaps/js-array-constructor-08-code.png" />

<img alt="js-array-constructor example 8 result" src="./code_sandbox/snaps/js-array-constructor-08-result.png" />

- [x] **Outcome:** **["Saab","Volvo","BMW"]**.

<a id="js-array-constructor-example-09"></a>

### **Example 9: Six numbers: new Array vs []**

- [x] Several numbers are **elements**, matching the literal.

Sandbox: `code_sandbox/js-array-constructor/six-numbers-new-vs-literal.html`

```javascript
const a = new Array(40, 100, 1, 5, 25, 10);
const b = [40, 100, 1, 5, 25, 10];
```

<img alt="js-array-constructor example 9 source" src="./code_sandbox/snaps/js-array-constructor-09-code.png" />

<img alt="js-array-constructor example 9 result" src="./code_sandbox/snaps/js-array-constructor-09-result.png" />

- [x] **Outcome:** Both **[40,100,1,5,25,10]**.

<a id="js-array-constructor-example-10"></a>

### **Example 10: new Array(40, 100, 1) — three elements**

- [x] Three numeric arguments → **three elements**.

Sandbox: `code_sandbox/js-array-constructor/new-array-three-nums.html`

```javascript
const points = new Array(40, 100, 1);
```

<img alt="js-array-constructor example 10 source" src="./code_sandbox/snaps/js-array-constructor-10-code.png" />

<img alt="js-array-constructor example 10 result" src="./code_sandbox/snaps/js-array-constructor-10-result.png" />

- [x] **Outcome:** **[40,100,1]**. length **3**.

<a id="js-array-constructor-example-11"></a>

### **Example 11: new Array(40, 100) — two elements**

- [x] Two numeric arguments → **two elements**.

Sandbox: `code_sandbox/js-array-constructor/new-array-two-nums.html`

```javascript
const points = new Array(40, 100);
```

<img alt="js-array-constructor example 11 source" src="./code_sandbox/snaps/js-array-constructor-11-code.png" />

<img alt="js-array-constructor example 11 result" src="./code_sandbox/snaps/js-array-constructor-11-result.png" />

- [x] **Outcome:** **[40,100]**. length **2**.

<a id="js-array-constructor-example-12"></a>

### **Example 12: WARNING new Array(40) — 40 empty slots**

- [x] **Single-number trap:** this is **not** `[40]`.
- [x] The page shows this Tryit twice (the “???” line and the warning). Included once.

Sandbox: `code_sandbox/js-array-constructor/new-array-40-trap.html`

```javascript
const points = new Array(40);
```

<img alt="js-array-constructor example 12 source" src="./code_sandbox/snaps/js-array-constructor-12-code.png" />

<img alt="js-array-constructor example 12 result" src="./code_sandbox/snaps/js-array-constructor-12-result.png" />

- [x] **Outcome:** length **40**. `0 in points` is **false**. `points[0]` is **undefined**.

<a id="js-array-constructor-example-13"></a>

### **Example 13: [40] — one element**

- [x] A literal **`[40]`** is one number, not forty holes.

Sandbox: `code_sandbox/js-array-constructor/literal-40.html`

```javascript
const points = [40];
```

<img alt="js-array-constructor example 13 source" src="./code_sandbox/snaps/js-array-constructor-13-code.png" />

<img alt="js-array-constructor example 13 result" src="./code_sandbox/snaps/js-array-constructor-13-result.png" />

- [x] **Outcome:** **[40]**. length **1**.

<a id="js-array-constructor-example-14"></a>

### **Example 14: Array literal (preferred)**

- [x] Use **`[]`**. It is faster to type, easier to read, and avoids the number trap.

Sandbox: `code_sandbox/js-array-constructor/literal-preferred.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
```

<img alt="js-array-constructor example 14 source" src="./code_sandbox/snaps/js-array-constructor-14-code.png" />

<img alt="js-array-constructor example 14 result" src="./code_sandbox/snaps/js-array-constructor-14-result.png" />

- [x] **Outcome:** **["Saab","Volvo","BMW"]**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-array-constructor/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Is Array() different from new Array()?

<details>
<summary>Answer</summary>

- [x] **No.** Omitting `new` is corrected internally.

</details>

### Question 2: What is new Array()?

<details>
<summary>Answer</summary>

- [x] An **empty** array `[]`, length **0**.

</details>

### Question 3: What is new Array(3)?

<details>
<summary>Answer</summary>

- [x] length **3** with **empty slots**.
- [x] JSON looks like [null,null,null]; `0 in a` is **false**.

</details>

### Question 4: What is new Array("3")?

<details>
<summary>Answer</summary>

- [x] **["3"]**, length **1**.

</details>

### Question 5: What is new Array(40, 100, 1)?

<details>
<summary>Answer</summary>

- [x] **[40,100,1]**, three elements.

</details>

### Question 6: What is new Array(40, 100)?

<details>
<summary>Answer</summary>

- [x] **[40,100]**, two elements.

</details>

### Question 7: What is new Array(40)?

<details>
<summary>Answer</summary>

- [x] **40 empty slots**, not `[40]`.

</details>

### Question 8: What is [40]?

<details>
<summary>Answer</summary>

- [x] **One** element, the number 40.

</details>

### Question 9: Why prefer []?

<details>
<summary>Answer</summary>

- [x] Faster to type, easier to read, no single-number trap.

</details>

### Question 10: Does new Array(40, 100, 1, 5, 25, 10) match the literal?

<details>
<summary>Answer</summary>

- [x] **Yes.** Both **[40,100,1,5,25,10]**.

</details>


</details>

## Summary

Use []. Reach for new Array only when you understand the single-number length rule. Array() without new is not a different constructor — it is the same function filling in new for you.

## References

- [JS Array Constructor (W3Schools)](https://www.w3schools.com/js/js_array_constructor.asp)
- [MDN: Array() constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Array)

</details>
