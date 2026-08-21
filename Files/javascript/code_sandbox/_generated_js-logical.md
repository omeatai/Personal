<details>
  <summary>JS Logical</summary>

## Introduction

Logical operators combine boolean tests: **`&&`** (AND), **`||`** (OR), **`!`** (NOT). **`??`** (nullish coalescing, ES2020) picks a fallback only for **`null`/`undefined`**, so **0** and **`""`** can stay.

This section has **9** examples:

- [x] **Example 1:** && AND — (x < 10 && y > 1) is true [View](#js-logical-example-01)
- [x] **Example 2:** || OR — (x === 5 || y === 5) is false [View](#js-logical-example-02)
- [x] **Example 3:** ! NOT — !(x === y) is true [View](#js-logical-example-03)
- [x] **Example 4:** Logical AND — both true with x=6 y=3 [View](#js-logical-example-04)
- [x] **Example 5:** Logical AND — false when y is not > 1 [View](#js-logical-example-05)
- [x] **Example 6:** Logical OR — x=6 y=-3 still true [View](#js-logical-example-06)
- [x] **Example 7:** Logical NOT — !(5 == 8) [View](#js-logical-example-07)
- [x] **Example 8:** ?? — null ?? "missing" is missing [View](#js-logical-example-08)
- [x] **Example 9:** ?? keeps 0; || treats 0 as missing [View](#js-logical-example-09)

## Detailed Explanation

- [x] Given **x = 6**, **y = 3**: **`x < 10 && y > 1`** is true; **`x === 5 || y === 5`** is false; **`!(x === y)`** is true.
- [x] **`&&`** needs both true. **`||`** needs at least one true. **`!`** negates.
- [x] **`??`** returns the right side only when the left is **nullish**. Prefer it over `||` when **0** or **""** are valid.

<a id="js-logical-example-01"></a>

### **Example 1: && AND — (x < 10 && y > 1) is true**

- [x] Given **x = 6**, **y = 3**: **`(x < 10 && y > 1)`** is **true** (both sides true).
- [x] **`&&`** is **true** only when **both** operands are true; otherwise **false**.
- [x] This is the first row of the operators table (and the AND Tryit).

Sandbox: `code_sandbox/js-logical/and-table.html`

```javascript
let x = 6;
let y = 3;
let z = (x < 10 && y > 1);
```

<img alt="js-logical example 1 source" src="./code_sandbox/snaps/js-logical-01-code.png" />

<img alt="js-logical example 1 result" src="./code_sandbox/snaps/js-logical-01-result.png" />

- [x] **Outcome:** Both sides are true, so **z** is **true**.

<a id="js-logical-example-02"></a>

### **Example 2: || OR — (x === 5 || y === 5) is false**

- [x] Given **x = 6**, **y = 3**: **`(x === 5 || y === 5)`** is **false** (neither equals 5).
- [x] **`||`** is **true** if **one or both** sides are true.

Sandbox: `code_sandbox/js-logical/or-table.html`

```javascript
let x = 6;
let y = 3;
let z = (x === 5 || y === 5);
```

<img alt="js-logical example 2 source" src="./code_sandbox/snaps/js-logical-02-code.png" />

<img alt="js-logical example 2 result" src="./code_sandbox/snaps/js-logical-02-result.png" />

- [x] **Outcome:** Both sides are false, so **z** is **false**.

<a id="js-logical-example-03"></a>

### **Example 3: ! NOT — !(x === y) is true**

- [x] Given **x = 6**, **y = 3**: **`x === y`** is false, so **`!(x === y)`** is **true**.
- [x] **`!`** flips true↔false.

Sandbox: `code_sandbox/js-logical/not-table.html`

```javascript
let x = 6;
let y = 3;
let z = !(x === y);
```

<img alt="js-logical example 3 source" src="./code_sandbox/snaps/js-logical-03-code.png" />

<img alt="js-logical example 3 result" src="./code_sandbox/snaps/js-logical-03-result.png" />

- [x] **Outcome:** **x === y** is **false**, so **! that** is **true**.

<a id="js-logical-example-04"></a>

### **Example 4: Logical AND — both true with x=6 y=3**

- [x] The AND section repeats `let z = (x < 10 && y > 1)` with **x = 6**, **y = 3**.
- [x] Same result as the table row: **true**.

Sandbox: `code_sandbox/js-logical/and-section.html`

```javascript
let x = 6;
let y = 3;
let z = (x < 10 && y > 1);
```

<img alt="js-logical example 4 source" src="./code_sandbox/snaps/js-logical-04-code.png" />

<img alt="js-logical example 4 result" src="./code_sandbox/snaps/js-logical-04-result.png" />

- [x] **Outcome:** **z** is **true**.

<a id="js-logical-example-05"></a>

### **Example 5: Logical AND — false when y is not > 1**

- [x] If **y = 0**, **`y > 1`** is false, so **`&&`** is **false** even though **x < 10** is true.
- [x] `&&` **short-circuits**: if the left side is false, the right side is not evaluated.

Sandbox: `code_sandbox/js-logical/and-false.html`

```javascript
let x = 6;
let y = 0;
let z = (x < 10 && y > 1);
```

<img alt="js-logical example 5 source" src="./code_sandbox/snaps/js-logical-05-code.png" />

<img alt="js-logical example 5 result" src="./code_sandbox/snaps/js-logical-05-result.png" />

- [x] **Outcome:** **y > 1** is **false**, so **z** is **false**.

<a id="js-logical-example-06"></a>

### **Example 6: Logical OR — x=6 y=-3 still true**

- [x] The OR section uses **x = 6**, **y = -3**, **`z = (x > 0 || y > 0)`**.
- [x] **x > 0** is true, so the whole `||` is **true** even though **y > 0** is false.

Sandbox: `code_sandbox/js-logical/or-section.html`

```javascript
let x = 6;
let y = -3;
let z = (x > 0 || y > 0);
```

<img alt="js-logical example 6 source" src="./code_sandbox/snaps/js-logical-06-code.png" />

<img alt="js-logical example 6 result" src="./code_sandbox/snaps/js-logical-06-result.png" />

- [x] **Outcome:** **x > 0** is **true**, so **z** is **true**.

<a id="js-logical-example-07"></a>

### **Example 7: Logical NOT — !(5 == 8)**

- [x] **`(5 == 8)`** is false. **`!(5 == 8)`** is **true**.
- [x] The page stores them as `let x = (5 == 8); let y = !(5 == 8)`.

Sandbox: `code_sandbox/js-logical/not-section.html`

```javascript
let x = (5 == 8);
let y = !(5 == 8);
```

<img alt="js-logical example 7 source" src="./code_sandbox/snaps/js-logical-07-code.png" />

<img alt="js-logical example 7 result" src="./code_sandbox/snaps/js-logical-07-result.png" />

- [x] **Outcome:** **x** is **false**; **y** is **true**.

<a id="js-logical-example-08"></a>

### **Example 8: ?? — null ?? "missing" is missing**

- [x] **`??`** (nullish coalescing) returns the **right** operand when the left is **`null` or `undefined`**; otherwise the **left**.
- [x] **`name = null`**, **`text = "missing"`**, **`result = name ?? text`** → **missing**.
- [x] `??` is **ES2020**. Use it when **0** or **""** should count as real values (unlike `||`).

Sandbox: `code_sandbox/js-logical/nullish-null.html`

```javascript
let name = null;
let text = "missing";
let result = name ?? text;
```

<img alt="js-logical example 8 source" src="./code_sandbox/snaps/js-logical-08-code.png" />

<img alt="js-logical example 8 result" src="./code_sandbox/snaps/js-logical-08-result.png" />

- [x] **Outcome:** **name** is **null**, so **result** is **missing**.

<a id="js-logical-example-09"></a>

### **Example 9: ?? keeps 0; || treats 0 as missing**

- [x] **`0 ?? 5`** is **0** (0 is not nullish). **`0 || 5`** is **5** (0 is falsy).
- [x] The page’s point: sometimes an empty string or `false` or `0` is a **valid** value — then use **`??`**, not **`||`**.

Sandbox: `code_sandbox/js-logical/nullish-vs-or.html`

```javascript
let viaNullish = 0 ?? 5;
let viaOr = 0 || 5;
let emptyKeep = "" ?? "fallback";
let emptyOr = "" || "fallback";
```

<img alt="js-logical example 9 source" src="./code_sandbox/snaps/js-logical-09-code.png" />

<img alt="js-logical example 9 result" src="./code_sandbox/snaps/js-logical-09-result.png" />

- [x] **Outcome:** **0 ?? 5** is **0**; **0 || 5** is **5**. **"" ?? …** stays **""**; **"" || …** becomes **fallback**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-logical/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: When is `&&` true?

<details>
<summary>Answer</summary>

- [x] When **both** operands are true.

</details>

### Question 2: With x=6 y=3, what is `(x < 10 && y > 1)`?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 3: With x=6 y=3, what is `(x === 5 || y === 5)`?

<details>
<summary>Answer</summary>

- [x] **false**.

</details>

### Question 4: With x=6 y=3, what is `!(x === y)`?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 5: With x=6 y=-3, what is `(x > 0 || y > 0)`?

<details>
<summary>Answer</summary>

- [x] **true** (x > 0).

</details>

### Question 6: What is `(5 == 8)` and `!(5 == 8)`?

<details>
<summary>Answer</summary>

- [x] **false** and **true**.

</details>

### Question 7: What does `null ?? "missing"` return?

<details>
<summary>Answer</summary>

- [x] **missing**.

</details>

### Question 8: What is `0 ?? 5` vs `0 || 5`?

<details>
<summary>Answer</summary>

- [x] **0** vs **5**. `??` keeps 0; `||` treats 0 as missing.

</details>

### Question 9: When was `??` added?

<details>
<summary>Answer</summary>

- [x] **ES2020** (widely supported since late 2020).

</details>

### Question 10: Does `&&` evaluate the right side if the left is false?

<details>
<summary>Answer</summary>

- [x] **No.** It **short-circuits**.

</details>


</details>

## Summary

**`&&`** / **`||`** / **`!`** combine tests (table: true / false / true with x=6 y=3). OR with y=-3 is still true via x>0. **`??`** replaces only **null/undefined** — **0 ?? 5** stays **0**.

## References

- [JS Logical (W3Schools)](https://www.w3schools.com/js/js_logical.asp)
- [MDN: Logical AND (&&)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND)
- [MDN: Nullish coalescing (??)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)

</details>
