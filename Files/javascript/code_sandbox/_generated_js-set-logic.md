<details>
  <summary>JS Set Logic</summary>

## Introduction

ECMAScript 2025 added seven Set logic methods. union, intersection, difference, and symmetricDifference return new Sets and leave the originals alone. isSubsetOf, isSupersetOf, and isDisjointFrom return booleans. The page Tryits all use A = {a,b,c} and B = {b,c,d}, so the three booleans are false. Extra Examples show true cases.

This section has **10** examples:

- [x] **Example 1:** union() [View](#js-set-logic-example-01)
- [x] **Example 2:** intersection() [View](#js-set-logic-example-02)
- [x] **Example 3:** difference() [View](#js-set-logic-example-03)
- [x] **Example 4:** symmetricDifference() [View](#js-set-logic-example-04)
- [x] **Example 5:** isSubsetOf() — page Tryit [View](#js-set-logic-example-05)
- [x] **Example 6:** isSupersetOf() — page Tryit [View](#js-set-logic-example-06)
- [x] **Example 7:** isDisjointFrom() — page Tryit [View](#js-set-logic-example-07)
- [x] **Example 8:** isSubsetOf() true case [View](#js-set-logic-example-08)
- [x] **Example 9:** isSupersetOf() true case [View](#js-set-logic-example-09)
- [x] **Example 10:** isDisjointFrom() true case [View](#js-set-logic-example-10)

## Detailed Explanation

- [x] A = **a,b,c**. B = **b,c,d**. Methods do **not** mutate A or B.
- [x] `union` → **a,b,c,d**. `intersection` → **b,c**. `difference` (A−B) → **a**. `symmetricDifference` → **a,d**.
- [x] On that pair: subset **false**, superset **false**, disjoint **false**.
- [x] `{b,c}.isSubsetOf(A)` is **true**. `A.isSupersetOf({b,c})` is **true**. `A.isDisjointFrom({z})` is **true**.
- [x] `B.difference(A)` is **["d"]** — argument order matters.

<a id="js-set-logic-example-01"></a>

### **Example 1: union()**

- [x] `A.union(B)` is a **new** Set of values in A, in B, or in both.
- [x] A and B are not mutated.

Sandbox: `code_sandbox/js-set-logic/union.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const C = A.union(B);
```

<img alt="js-set-logic example 1 source" src="./code_sandbox/snaps/js-set-logic-01-code.png" />

<img alt="js-set-logic example 1 result" src="./code_sandbox/snaps/js-set-logic-01-result.png" />

- [x] **Outcome:** C is **["a","b","c","d"]**. A stays **["a","b","c"]**. B stays **["b","c","d"]**.

<a id="js-set-logic-example-02"></a>

### **Example 2: intersection()**

- [x] `A.intersection(B)` is values that are in **both** A and B.

Sandbox: `code_sandbox/js-set-logic/intersection.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const C = A.intersection(B);
```

<img alt="js-set-logic example 2 source" src="./code_sandbox/snaps/js-set-logic-02-code.png" />

<img alt="js-set-logic example 2 result" src="./code_sandbox/snaps/js-set-logic-02-result.png" />

- [x] **Outcome:** C is **["b","c"]**.

<a id="js-set-logic-example-03"></a>

### **Example 3: difference()**

- [x] `A.difference(B)` is values in **A but not B** (order of the call matters).

Sandbox: `code_sandbox/js-set-logic/difference.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const C = A.difference(B);
```

<img alt="js-set-logic example 3 source" src="./code_sandbox/snaps/js-set-logic-03-code.png" />

<img alt="js-set-logic example 3 result" src="./code_sandbox/snaps/js-set-logic-03-result.png" />

- [x] **Outcome:** `A.difference(B)` is **["a"]**. `B.difference(A)` is **["d"]**.

<a id="js-set-logic-example-04"></a>

### **Example 4: symmetricDifference()**

- [x] `A.symmetricDifference(B)` is values in A or B **but not both**.

Sandbox: `code_sandbox/js-set-logic/symmetric-difference.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const C = A.symmetricDifference(B);
```

<img alt="js-set-logic example 4 source" src="./code_sandbox/snaps/js-set-logic-04-code.png" />

<img alt="js-set-logic example 4 result" src="./code_sandbox/snaps/js-set-logic-04-result.png" />

- [x] **Outcome:** C is **["a","d"]**.

<a id="js-set-logic-example-05"></a>

### **Example 5: isSubsetOf() — page Tryit**

- [x] `A.isSubsetOf(B)` is **true** only if **every** value in A is also in B.
- [x] The page uses A = a,b,c and B = b,c,d.

Sandbox: `code_sandbox/js-set-logic/is-subset-of.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const answer = A.isSubsetOf(B);
```

<img alt="js-set-logic example 5 source" src="./code_sandbox/snaps/js-set-logic-05-code.png" />

<img alt="js-set-logic example 5 result" src="./code_sandbox/snaps/js-set-logic-05-result.png" />

- [x] **Outcome:** `A.isSubsetOf(B)` is **false** because **"a"** is not in B.

<a id="js-set-logic-example-06"></a>

### **Example 6: isSupersetOf() — page Tryit**

- [x] `A.isSupersetOf(B)` is **true** only if **every** value in B is also in A.

Sandbox: `code_sandbox/js-set-logic/is-superset-of.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const answer = A.isSupersetOf(B);
```

<img alt="js-set-logic example 6 source" src="./code_sandbox/snaps/js-set-logic-06-code.png" />

<img alt="js-set-logic example 6 result" src="./code_sandbox/snaps/js-set-logic-06-result.png" />

- [x] **Outcome:** `A.isSupersetOf(B)` is **false** because **"d"** is not in A.

<a id="js-set-logic-example-07"></a>

### **Example 7: isDisjointFrom() — page Tryit**

- [x] `A.isDisjointFrom(B)` is **true** only if A and B share **no** values.

Sandbox: `code_sandbox/js-set-logic/is-disjoint-from.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const answer = A.isDisjointFrom(B);
```

<img alt="js-set-logic example 7 source" src="./code_sandbox/snaps/js-set-logic-07-code.png" />

<img alt="js-set-logic example 7 result" src="./code_sandbox/snaps/js-set-logic-07-result.png" />

- [x] **Outcome:** `A.isDisjointFrom(B)` is **false** because they share **"b"** and **"c"**.

<a id="js-set-logic-example-08"></a>

### **Example 8: isSubsetOf() true case**

- [x] The page Tryit is **false**. A smaller Set **is** a subset.

Sandbox: `code_sandbox/js-set-logic/is-subset-of-true.html`

```javascript
const A = new Set(["b","c"]);
const B = new Set(["a","b","c"]);
const answer = A.isSubsetOf(B);
```

<img alt="js-set-logic example 8 source" src="./code_sandbox/snaps/js-set-logic-08-code.png" />

<img alt="js-set-logic example 8 result" src="./code_sandbox/snaps/js-set-logic-08-result.png" />

- [x] **Outcome:** `A.isSubsetOf(B)` is **true**. `B.isSubsetOf(A)` is **false**.

<a id="js-set-logic-example-09"></a>

### **Example 9: isSupersetOf() true case**

- [x] A is a superset of C when C’s values are **all** in A.

Sandbox: `code_sandbox/js-set-logic/is-superset-of-true.html`

```javascript
const A = new Set(["a","b","c"]);
const C = new Set(["b","c"]);
const answer = A.isSupersetOf(C);
```

<img alt="js-set-logic example 9 source" src="./code_sandbox/snaps/js-set-logic-09-code.png" />

<img alt="js-set-logic example 9 result" src="./code_sandbox/snaps/js-set-logic-09-result.png" />

- [x] **Outcome:** `A.isSupersetOf(C)` is **true**. `C.isSupersetOf(A)` is **false**.

<a id="js-set-logic-example-10"></a>

### **Example 10: isDisjointFrom() true case**

- [x] No shared values means **disjoint**.

Sandbox: `code_sandbox/js-set-logic/is-disjoint-from-true.html`

```javascript
const A = new Set(["a","b","c"]);
const Z = new Set(["z"]);
const answer = A.isDisjointFrom(Z);
```

<img alt="js-set-logic example 10 source" src="./code_sandbox/snaps/js-set-logic-10-code.png" />

<img alt="js-set-logic example 10 result" src="./code_sandbox/snaps/js-set-logic-10-result.png" />

- [x] **Outcome:** `A.isDisjointFrom({z})` is **true**. Sharing **"a"** makes it **false**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-set-logic/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is A.union(B)?

<details>
<summary>Answer</summary>

- [x] **["a","b","c","d"]**. A and B unchanged.

</details>

### Question 2: What is A.intersection(B)?

<details>
<summary>Answer</summary>

- [x] **["b","c"]**.

</details>

### Question 3: What is A.difference(B)?

<details>
<summary>Answer</summary>

- [x] **["a"]**. `B.difference(A)` is **["d"]**.

</details>

### Question 4: What is A.symmetricDifference(B)?

<details>
<summary>Answer</summary>

- [x] **["a","d"]**.

</details>

### Question 5: Is A a subset of B on the page?

<details>
<summary>Answer</summary>

- [x] **false** — **"a"** is not in B.

</details>

### Question 6: Is A a superset of B on the page?

<details>
<summary>Answer</summary>

- [x] **false** — **"d"** is not in A.

</details>

### Question 7: Are A and B disjoint on the page?

<details>
<summary>Answer</summary>

- [x] **false** — they share **b** and **c**.

</details>

### Question 8: When is isSubsetOf true here?

<details>
<summary>Answer</summary>

- [x] `new Set(["b","c"]).isSubsetOf(A)` is **true**.

</details>

### Question 9: When is isSupersetOf true here?

<details>
<summary>Answer</summary>

- [x] `A.isSupersetOf({b,c})` is **true**.

</details>

### Question 10: When is isDisjointFrom true here?

<details>
<summary>Answer</summary>

- [x] `A.isDisjointFrom({z})` is **true**.

</details>


</details>

## Summary

Logic methods return a new Set or a boolean. The tutorial’s A/B pair overlaps, so the three predicates are false until you pick a contained or disjoint argument.

## References

- [JS Set Logic (W3Schools)](https://www.w3schools.com/js/js_set_logic.asp)
- [MDN: Set.prototype.union](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/union)
- [MDN: Set.prototype.intersection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/intersection)

</details>
