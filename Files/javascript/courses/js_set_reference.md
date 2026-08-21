# JS Set Reference

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The July 2025 Set reference lists every method plus the size property. Each table row is its own Example. Logic methods reuse A = {a,b,c} and B = {b,c,d}. Boolean methods also show a true case so the description is visible, not only the overlapping false pair.

This section has **17** examples:

- [x] **Example 1:** new Set() — creates a new set [View](#js-set-reference-example-01)
- [x] **Example 2:** add() — adds a new element [View](#js-set-reference-example-02)
- [x] **Example 3:** clear() — removes all elements [View](#js-set-reference-example-03)
- [x] **Example 4:** delete() — removes an element [View](#js-set-reference-example-04)
- [x] **Example 5:** difference() [View](#js-set-reference-example-05)
- [x] **Example 6:** entries() — [value, value] pairs [View](#js-set-reference-example-06)
- [x] **Example 7:** forEach() — callback per element [View](#js-set-reference-example-07)
- [x] **Example 8:** has() — true if a value exists [View](#js-set-reference-example-08)
- [x] **Example 9:** intersection() [View](#js-set-reference-example-09)
- [x] **Example 10:** isDisjointFrom() — no elements in common [View](#js-set-reference-example-10)
- [x] **Example 11:** isSubsetOf() — all elements are in the other Set [View](#js-set-reference-example-11)
- [x] **Example 12:** isSupersetOf() — contains the other Set [View](#js-set-reference-example-12)
- [x] **Example 13:** keys() — same as values() [View](#js-set-reference-example-13)
- [x] **Example 14:** symmetricDifference() [View](#js-set-reference-example-14)
- [x] **Example 15:** union() [View](#js-set-reference-example-15)
- [x] **Example 16:** values() — iterator of values [View](#js-set-reference-example-16)
- [x] **Example 17:** size — number of elements [View](#js-set-reference-example-17)

## Detailed Explanation

- [x] **Every table row is an Example**, including `size`.
- [x] `add` returns the same Set. `delete` returns a boolean. `clear` empties.
- [x] A∪B **a,b,c,d**. A∩B **b,c**. A−B **a**. symmetric **a,d**.
- [x] A vs B: disjoint **false**, subset **false**, superset **false**. `{b,c} ⊂ A` **true**.
- [x] `keys()` matches `values()`. `entries()` is **[value,value]**.

<a id="js-set-reference-example-01"></a>

### **Example 1: new Set() — creates a new set**

- [x] `new Set()` with an array copies unique values.

Sandbox: `code_sandbox/js-set-reference/new-set.html`

```javascript
const letters = new Set(["a","b","c"]);
```

![js-set-reference example 1 source](../code_sandbox/snaps/js-set-reference-01-code.png)

![js-set-reference example 1 result](../code_sandbox/snaps/js-set-reference-01-result.png)

- [x] **Outcome:** **["a","b","c"]**, size **3**.

<a id="js-set-reference-example-02"></a>

### **Example 2: add() — adds a new element**

- [x] `add()` inserts a value and returns the **same** Set (chainable).

Sandbox: `code_sandbox/js-set-reference/add.html`

```javascript
const letters = new Set(["a","b","c"]);
const ret = letters.add("d");
```

![js-set-reference example 2 source](../code_sandbox/snaps/js-set-reference-02-code.png)

![js-set-reference example 2 result](../code_sandbox/snaps/js-set-reference-02-result.png)

- [x] **Outcome:** letters is **["a","b","c","d"]**. `add` returned the **same** Set (**true**).

<a id="js-set-reference-example-03"></a>

### **Example 3: clear() — removes all elements**

- [x] `clear()` empties the Set.

Sandbox: `code_sandbox/js-set-reference/clear.html`

```javascript
const letters = new Set(["a","b","c"]);
letters.clear();
```

![js-set-reference example 3 source](../code_sandbox/snaps/js-set-reference-03-code.png)

![js-set-reference example 3 result](../code_sandbox/snaps/js-set-reference-03-result.png)

- [x] **Outcome:** size **0**, **[]**.

<a id="js-set-reference-example-04"></a>

### **Example 4: delete() — removes an element**

- [x] `delete(value)` returns whether the value **was** present.

Sandbox: `code_sandbox/js-set-reference/delete.html`

```javascript
const letters = new Set(["a","b","c"]);
const ok = letters.delete("b");
```

![js-set-reference example 4 source](../code_sandbox/snaps/js-set-reference-04-code.png)

![js-set-reference example 4 result](../code_sandbox/snaps/js-set-reference-04-result.png)

- [x] **Outcome:** First `delete("b")` is **true**, letters **["a","c"]**. Second delete is **false**.

<a id="js-set-reference-example-05"></a>

### **Example 5: difference()**

- [x] `difference()` returns values in this Set but not the argument Set.
- [x] Fixed A = a,b,c and B = b,c,d (same as the logic page).

Sandbox: `code_sandbox/js-set-reference/difference.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const C = A.difference(B);
```

![js-set-reference example 5 source](../code_sandbox/snaps/js-set-reference-05-code.png)

![js-set-reference example 5 result](../code_sandbox/snaps/js-set-reference-05-result.png)

- [x] **Outcome:** C is **["a"]**.

<a id="js-set-reference-example-06"></a>

### **Example 6: entries() — [value, value] pairs**

- [x] `entries()` yields **[value, value]** so Sets match Maps.

Sandbox: `code_sandbox/js-set-reference/entries.html`

```javascript
const letters = new Set(["a","b","c"]);
const pairs = Array.from(letters.entries());
```

![js-set-reference example 6 source](../code_sandbox/snaps/js-set-reference-06-code.png)

![js-set-reference example 6 result](../code_sandbox/snaps/js-set-reference-06-result.png)

- [x] **Outcome:** pairs is **[["a","a"],["b","b"],["c","c"]]**.

<a id="js-set-reference-example-07"></a>

### **Example 7: forEach() — callback per element**

- [x] `forEach` invokes a callback once per value.

Sandbox: `code_sandbox/js-set-reference/for-each.html`

```javascript
const letters = new Set(["a","b","c"]);
let text = "";
letters.forEach(function (value) {
  text += value;
});
```

![js-set-reference example 7 source](../code_sandbox/snaps/js-set-reference-07-code.png)

![js-set-reference example 7 result](../code_sandbox/snaps/js-set-reference-07-result.png)

- [x] **Outcome:** text is **"abc"**.

<a id="js-set-reference-example-08"></a>

### **Example 8: has() — true if a value exists**

- [x] `has(value)` is a boolean membership test.

Sandbox: `code_sandbox/js-set-reference/has.html`

```javascript
const letters = new Set(["a","b","c"]);
letters.has("b");
letters.has("z");
```

![js-set-reference example 8 source](../code_sandbox/snaps/js-set-reference-08-code.png)

![js-set-reference example 8 result](../code_sandbox/snaps/js-set-reference-08-result.png)

- [x] **Outcome:** `has("b")` is **true**. `has("z")` is **false**.

<a id="js-set-reference-example-09"></a>

### **Example 9: intersection()**

- [x] `intersection()` returns values in both Sets.
- [x] Fixed A = a,b,c and B = b,c,d (same as the logic page).

Sandbox: `code_sandbox/js-set-reference/intersection.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const C = A.intersection(B);
```

![js-set-reference example 9 source](../code_sandbox/snaps/js-set-reference-09-code.png)

![js-set-reference example 9 result](../code_sandbox/snaps/js-set-reference-09-result.png)

- [x] **Outcome:** C is **["b","c"]**.

<a id="js-set-reference-example-10"></a>

### **Example 10: isDisjointFrom() — no elements in common**

- [x] Returns **true** if the two Sets share nothing.

Sandbox: `code_sandbox/js-set-reference/is-disjoint-from.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const overlap = A.isDisjointFrom(B);
const split = A.isDisjointFrom(new Set(['z']));
```

![js-set-reference example 10 source](../code_sandbox/snaps/js-set-reference-10-code.png)

![js-set-reference example 10 result](../code_sandbox/snaps/js-set-reference-10-result.png)

- [x] **Outcome:** Overlap with B is **false**. Disjoint from `{z}` is **true**.

<a id="js-set-reference-example-11"></a>

### **Example 11: isSubsetOf() — all elements are in the other Set**

- [x] Returns **true** if this Set’s values are all in the argument.

Sandbox: `code_sandbox/js-set-reference/is-subset-of.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const small = new Set(['b','c']);
```

![js-set-reference example 11 source](../code_sandbox/snaps/js-set-reference-11-code.png)

![js-set-reference example 11 result](../code_sandbox/snaps/js-set-reference-11-result.png)

- [x] **Outcome:** A ⊂ B is **false**. `{b,c} ⊂ A` is **true**.

<a id="js-set-reference-example-12"></a>

### **Example 12: isSupersetOf() — contains the other Set**

- [x] Returns **true** if every argument value is also in this Set.

Sandbox: `code_sandbox/js-set-reference/is-superset-of.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const small = new Set(['b','c']);
```

![js-set-reference example 12 source](../code_sandbox/snaps/js-set-reference-12-code.png)

![js-set-reference example 12 result](../code_sandbox/snaps/js-set-reference-12-result.png)

- [x] **Outcome:** A ⊃ B is **false**. A ⊃ `{b,c}` is **true**.

<a id="js-set-reference-example-13"></a>

### **Example 13: keys() — same as values()**

- [x] `keys()` equals `values()` so Sets are Map-compatible.

Sandbox: `code_sandbox/js-set-reference/keys.html`

```javascript
const letters = new Set(["a","b","c"]);
const same = Array.from(letters.keys()).join() === Array.from(letters.values()).join();
```

![js-set-reference example 13 source](../code_sandbox/snaps/js-set-reference-13-code.png)

![js-set-reference example 13 result](../code_sandbox/snaps/js-set-reference-13-result.png)

- [x] **Outcome:** keys are **["a","b","c"]**. Joined keys and values match (**true**).

<a id="js-set-reference-example-14"></a>

### **Example 14: symmetricDifference()**

- [x] `symmetricDifference()` returns values in either Set but not both.
- [x] Fixed A = a,b,c and B = b,c,d (same as the logic page).

Sandbox: `code_sandbox/js-set-reference/symmetric-difference.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const C = A.symmetricDifference(B);
```

![js-set-reference example 14 source](../code_sandbox/snaps/js-set-reference-14-code.png)

![js-set-reference example 14 result](../code_sandbox/snaps/js-set-reference-14-result.png)

- [x] **Outcome:** C is **["a","d"]**.

<a id="js-set-reference-example-15"></a>

### **Example 15: union()**

- [x] `union()` returns values in this Set, the argument, or both.
- [x] Fixed A = a,b,c and B = b,c,d (same as the logic page).

Sandbox: `code_sandbox/js-set-reference/union.html`

```javascript
const A = new Set(["a","b","c"]);
const B = new Set(["b","c","d"]);
const C = A.union(B);
```

![js-set-reference example 15 source](../code_sandbox/snaps/js-set-reference-15-code.png)

![js-set-reference example 15 result](../code_sandbox/snaps/js-set-reference-15-result.png)

- [x] **Outcome:** C is **["a","b","c","d"]**.

<a id="js-set-reference-example-16"></a>

### **Example 16: values() — iterator of values**

- [x] `values()` iterates the Set’s values in insertion order.

Sandbox: `code_sandbox/js-set-reference/values.html`

```javascript
const letters = new Set(["a","b","c"]);
const list = Array.from(letters.values());
```

![js-set-reference example 16 source](../code_sandbox/snaps/js-set-reference-16-code.png)

![js-set-reference example 16 result](../code_sandbox/snaps/js-set-reference-16-result.png)

- [x] **Outcome:** list is **["a","b","c"]**.

<a id="js-set-reference-example-17"></a>

### **Example 17: size — number of elements**

- [x] `size` is the only Set **property** on the table (not a method).

Sandbox: `code_sandbox/js-set-reference/size.html`

```javascript
const mySet = new Set(["a","b","c"]);
mySet.size;
```

![js-set-reference example 17 source](../code_sandbox/snaps/js-set-reference-17-code.png)

![js-set-reference example 17 result](../code_sandbox/snaps/js-set-reference-17-result.png)

- [x] **Outcome:** `size` is **3**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-set-reference/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How many Set properties are on the table?

<details>
<summary>Answer</summary>

- [x] **One:** `size`.

</details>

### Question 2: Does add() return a new Set?

<details>
<summary>Answer</summary>

- [x] **No.** It returns **the same** Set (**true** for `ret === letters`).

</details>

### Question 3: What is delete("b") the first vs second time?

<details>
<summary>Answer</summary>

- [x] **true** then leftover **["a","c"]**. Second call **false**.

</details>

### Question 4: What is union of A and B?

<details>
<summary>Answer</summary>

- [x] **["a","b","c","d"]**. A unchanged.

</details>

### Question 5: What is intersection?

<details>
<summary>Answer</summary>

- [x] **["b","c"]**.

</details>

### Question 6: What is difference A−B?

<details>
<summary>Answer</summary>

- [x] **["a"]**.

</details>

### Question 7: What is symmetricDifference?

<details>
<summary>Answer</summary>

- [x] **["a","d"]**.

</details>

### Question 8: isSubsetOf A of B?

<details>
<summary>Answer</summary>

- [x] **false**. `{b,c} ⊂ A` is **true**.

</details>

### Question 9: isSupersetOf A of B?

<details>
<summary>Answer</summary>

- [x] **false**. A ⊃ `{b,c}` is **true**.

</details>

### Question 10: isDisjointFrom A and B?

<details>
<summary>Answer</summary>

- [x] **false**. A vs `{z}` is **true**.

</details>

### Question 11: What does entries() look like?

<details>
<summary>Answer</summary>

- [x] **[["a","a"],["b","b"],["c","c"]]**.

</details>


</details>

## Summary

Treat the reference as a catalog: construct, mutate (add/delete/clear), test (has and the three predicates), combine (union and friends), and iterate (keys/values/entries/forEach). size is the only property.

## References

- [JS Set Reference (W3Schools)](https://www.w3schools.com/js/js_set_reference.asp)
- [MDN: Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
