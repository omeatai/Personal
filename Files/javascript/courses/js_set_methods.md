# JS Set Methods

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Set methods cover create, add, size, has, iteration, and the Map-compatible keys/values/entries trio. values() and keys() yield the same values. entries() yields [value, value] pairs so a Set can be treated like a Map. delete() and clear() are listed on the page without Tryits and still each get an Example. has('d') on {a,b,c} is false.

This section has **15** examples:

- [x] **Example 1:** new Set() from an array [View](#js-set-methods-example-01)
- [x] **Example 2:** add("d") and add("e") [View](#js-set-methods-example-02)
- [x] **Example 3:** add() ignores duplicates [View](#js-set-methods-example-03)
- [x] **Example 4:** size property [View](#js-set-methods-example-04)
- [x] **Example 5:** for...of lists elements [View](#js-set-methods-example-05)
- [x] **Example 6:** has("d") [View](#js-set-methods-example-06)
- [x] **Example 7:** forEach() for each value [View](#js-set-methods-example-07)
- [x] **Example 8:** values() iterator variable [View](#js-set-methods-example-08)
- [x] **Example 9:** for...of letters.values() [View](#js-set-methods-example-09)
- [x] **Example 10:** keys() iterator variable [View](#js-set-methods-example-10)
- [x] **Example 11:** for...of letters.keys() [View](#js-set-methods-example-11)
- [x] **Example 12:** entries() iterator variable [View](#js-set-methods-example-12)
- [x] **Example 13:** for...of letters.entries() [View](#js-set-methods-example-13)
- [x] **Example 14:** delete("b") — listed, no Tryit [View](#js-set-methods-example-14)
- [x] **Example 15:** clear() — listed, no Tryit [View](#js-set-methods-example-15)

## Detailed Explanation

- [x] `size` is an element count, not `length`.
- [x] `has('d')` on `{a,b,c}` is **false**; `has('a')` is **true**.
- [x] `forEach` and `for...of` both walk values → **abc**.
- [x] `keys()` === `values()`. `entries()` → **[value, value]**.
- [x] `text += entry` on entries stringifies to **"a,ab,bc,c"**.
- [x] `delete("b")` → **true**, leftover **["a","c"]**. `clear()` → size **0**.

<a id="js-set-methods-example-01"></a>

### **Example 1: new Set() from an array**

- [x] `new Set(iterable)` copies unique values from the array.

Sandbox: `code_sandbox/js-set-methods/new-set.html`

```javascript
const letters = new Set(["a","b","c"]);
```

![js-set-methods example 1 source](../code_sandbox/snaps/js-set-methods-01-code.png)

![js-set-methods example 1 result](../code_sandbox/snaps/js-set-methods-01-result.png)

- [x] **Outcome:** letters is **["a","b","c"]**. size is **3**.

<a id="js-set-methods-example-02"></a>

### **Example 2: add("d") and add("e")**

- [x] `add()` appends a value that is not already present.

Sandbox: `code_sandbox/js-set-methods/add-d-e.html`

```javascript
const letters = new Set(["a","b","c"]);
letters.add("d");
letters.add("e");
```

![js-set-methods example 2 source](../code_sandbox/snaps/js-set-methods-02-code.png)

![js-set-methods example 2 result](../code_sandbox/snaps/js-set-methods-02-result.png)

- [x] **Outcome:** After the two adds: **["a","b","c","d","e"]**, size **5**.

<a id="js-set-methods-example-03"></a>

### **Example 3: add() ignores duplicates**

- [x] Adding an existing value **leaves the Set unchanged**.

Sandbox: `code_sandbox/js-set-methods/add-duplicates.html`

```javascript
const letters = new Set();
letters.add("a");
letters.add("b");
letters.add("c");
letters.add("c");
letters.add("c");
letters.add("c");
letters.add("c");
letters.add("c");
```

![js-set-methods example 3 source](../code_sandbox/snaps/js-set-methods-03-code.png)

![js-set-methods example 3 result](../code_sandbox/snaps/js-set-methods-03-result.png)

- [x] **Outcome:** Result is **["a","b","c"]**. size **3**.

<a id="js-set-methods-example-04"></a>

### **Example 4: size property**

- [x] `size` is the number of **unique** elements (not `length`).

Sandbox: `code_sandbox/js-set-methods/size.html`

```javascript
const mySet = new Set(["a","b","c"]);
mySet.size;
```

![js-set-methods example 4 source](../code_sandbox/snaps/js-set-methods-04-code.png)

![js-set-methods example 4 result](../code_sandbox/snaps/js-set-methods-04-result.png)

- [x] **Outcome:** `mySet.size` is **3**.

<a id="js-set-methods-example-05"></a>

### **Example 5: for...of lists elements**

- [x] `for...of` walks the Set in insertion order.

Sandbox: `code_sandbox/js-set-methods/for-of-list.html`

```javascript
const letters = new Set(["a","b","c"]);
let text = "";
for (const x of letters) {
  text += x;
}
```

![js-set-methods example 5 source](../code_sandbox/snaps/js-set-methods-05-code.png)

![js-set-methods example 5 result](../code_sandbox/snaps/js-set-methods-05-result.png)

- [x] **Outcome:** text is **"abc"**.

<a id="js-set-methods-example-06"></a>

### **Example 6: has("d")**

- [x] `has(value)` is **true** only if that value is in the Set.
- [x] This Tryit asks about **"d"** in `["a","b","c"]`.

Sandbox: `code_sandbox/js-set-methods/has-d.html`

```javascript
const letters = new Set(["a","b","c"]);
const answer = letters.has("d");
```

![js-set-methods example 6 source](../code_sandbox/snaps/js-set-methods-06-code.png)

![js-set-methods example 6 result](../code_sandbox/snaps/js-set-methods-06-result.png)

- [x] **Outcome:** `has("d")` is **false**. `has("a")` is **true**.

<a id="js-set-methods-example-07"></a>

### **Example 7: forEach() for each value**

- [x] `forEach(callback)` runs once per value.
- [x] The callback’s first argument is the **value** (Sets have no separate key).

Sandbox: `code_sandbox/js-set-methods/for-each.html`

```javascript
const letters = new Set(["a","b","c"]);
let text = "";
letters.forEach(function (value) {
  text += value;
});
```

![js-set-methods example 7 source](../code_sandbox/snaps/js-set-methods-07-code.png)

![js-set-methods example 7 result](../code_sandbox/snaps/js-set-methods-07-result.png)

- [x] **Outcome:** text is **"abc"**.

<a id="js-set-methods-example-08"></a>

### **Example 8: values() iterator variable**

- [x] `values()` returns an **iterator** of the Set’s values.
- [x] Store it, then `for...of` the iterator.

Sandbox: `code_sandbox/js-set-methods/values-iterator.html`

```javascript
const letters = new Set(["a","b","c"]);
const myIterator = letters.values();
let text = "";
for (const entry of myIterator) {
  text += entry;
}
```

![js-set-methods example 8 source](../code_sandbox/snaps/js-set-methods-08-code.png)

![js-set-methods example 8 result](../code_sandbox/snaps/js-set-methods-08-result.png)

- [x] **Outcome:** text is **"abc"**. `Array.from(letters.values())` is **["a","b","c"]**.

<a id="js-set-methods-example-09"></a>

### **Example 9: for...of letters.values()**

- [x] You can loop `letters.values()` **directly** without a named iterator.

Sandbox: `code_sandbox/js-set-methods/values-direct.html`

```javascript
const letters = new Set(["a","b","c"]);
let text = "";
for (const entry of letters.values()) {
  text += entry;
}
```

![js-set-methods example 9 source](../code_sandbox/snaps/js-set-methods-09-code.png)

![js-set-methods example 9 result](../code_sandbox/snaps/js-set-methods-09-result.png)

- [x] **Outcome:** Same concatenation: **"abc"**.

<a id="js-set-methods-example-10"></a>

### **Example 10: keys() iterator variable**

- [x] A Set has **no keys**, so `keys()` is the **same as** `values()`.
- [x] That pairing exists so Sets line up with Maps.

Sandbox: `code_sandbox/js-set-methods/keys-iterator.html`

```javascript
const letters = new Set(["a","b","c"]);
const myIterator = letters.keys();
let text = "";
for (const x of myIterator) {
  text += x;
}
```

![js-set-methods example 10 source](../code_sandbox/snaps/js-set-methods-10-code.png)

![js-set-methods example 10 result](../code_sandbox/snaps/js-set-methods-10-result.png)

- [x] **Outcome:** text is **"abc"**. keys are **["a","b","c"]** — the values, reused as keys.

<a id="js-set-methods-example-11"></a>

### **Example 11: for...of letters.keys()**

- [x] Loop `letters.keys()` directly; it still yields the values.

Sandbox: `code_sandbox/js-set-methods/keys-direct.html`

```javascript
const letters = new Set(["a","b","c"]);
let text = "";
for (const x of letters.keys()) {
  text += x;
}
```

![js-set-methods example 11 source](../code_sandbox/snaps/js-set-methods-11-code.png)

![js-set-methods example 11 result](../code_sandbox/snaps/js-set-methods-11-result.png)

- [x] **Outcome:** text is **"abc"**.

<a id="js-set-methods-example-12"></a>

### **Example 12: entries() iterator variable**

- [x] `entries()` is supposed to yield **[key, value]** pairs.
- [x] A Set has no keys, so each pair is **[value, value]**.

Sandbox: `code_sandbox/js-set-methods/entries-iterator.html`

```javascript
const letters = new Set(["a","b","c"]);
const myIterator = letters.entries();
let text = "";
for (const entry of myIterator) {
  text += entry;
}
```

![js-set-methods example 12 source](../code_sandbox/snaps/js-set-methods-12-code.png)

![js-set-methods example 12 result](../code_sandbox/snaps/js-set-methods-12-result.png)

- [x] **Outcome:** `text += entry` stringifies each pair: **"a,ab,bc,c"**. The pairs themselves are **[["a","a"],["b","b"],["c","c"]]**.

<a id="js-set-methods-example-13"></a>

### **Example 13: for...of letters.entries()**

- [x] Loop `letters.entries()` directly. Same **[value, value]** pairs.

Sandbox: `code_sandbox/js-set-methods/entries-direct.html`

```javascript
const letters = new Set(["a","b","c"]);
let text = "";
for (const entry of letters.entries()) {
  text += entry;
}
```

![js-set-methods example 13 source](../code_sandbox/snaps/js-set-methods-13-code.png)

![js-set-methods example 13 result](../code_sandbox/snaps/js-set-methods-13-result.png)

- [x] **Outcome:** text is again **"a,ab,bc,c"** (`Array.prototype.toString` joins with a comma, then the next pair is glued on).

<a id="js-set-methods-example-14"></a>

### **Example 14: delete("b") — listed, no Tryit**

- [x] `delete(value)` removes that value and returns **true** if it was present.
- [x] The methods list includes `delete()` with no Tryit — still run it.

Sandbox: `code_sandbox/js-set-methods/delete-b.html`

```javascript
const letters = new Set(["a","b","c"]);
const removed = letters.delete("b");
const missing = letters.delete("z");
```

![js-set-methods example 14 source](../code_sandbox/snaps/js-set-methods-14-code.png)

![js-set-methods example 14 result](../code_sandbox/snaps/js-set-methods-14-result.png)

- [x] **Outcome:** `delete("b")` is **true**. `delete("z")` is **false**. letters is **["a","c"]**, size **2**.

<a id="js-set-methods-example-15"></a>

### **Example 15: clear() — listed, no Tryit**

- [x] `clear()` removes **all** elements. size becomes **0**.

Sandbox: `code_sandbox/js-set-methods/clear.html`

```javascript
const letters = new Set(["a","b","c"]);
letters.clear();
```

![js-set-methods example 15 source](../code_sandbox/snaps/js-set-methods-15-code.png)

![js-set-methods example 15 result](../code_sandbox/snaps/js-set-methods-15-result.png)

- [x] **Outcome:** After `clear()`, size is **0** and `Array.from` is **[]**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-set-methods/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `size` report for a,b,c?

<details>
<summary>Answer</summary>

- [x] **3**.

</details>

### Question 2: What is `has("d")` on that Set?

<details>
<summary>Answer</summary>

- [x] **false**. `has("a")` is **true**.

</details>

### Question 3: What does forEach concatenate?

<details>
<summary>Answer</summary>

- [x] **"abc"**.

</details>

### Question 4: Do keys() and values() differ on a Set?

<details>
<summary>Answer</summary>

- [x] **No.** Both yield **a, b, c** so Sets match Maps.

</details>

### Question 5: What does entries() yield?

<details>
<summary>Answer</summary>

- [x] **[value, value]** pairs: **[["a","a"],["b","b"],["c","c"]]**.

</details>

### Question 6: Why is entries concatenation **"a,ab,bc,c"**?

<details>
<summary>Answer</summary>

- [x] Each pair’s `toString()` is `a,a` (comma). The next pair is glued on with no separator.

</details>

### Question 7: What does `delete("b")` return?

<details>
<summary>Answer</summary>

- [x] **true**, leftover **["a","c"]**. Deleting a missing **"z"** returns **false**.

</details>

### Question 8: What does clear() leave?

<details>
<summary>Answer</summary>

- [x] size **0**, **[]**.

</details>

### Question 9: Does add() keep duplicates?

<details>
<summary>Answer</summary>

- [x] **No.** size stays **3** after many `add("c")`.

</details>

### Question 10: Why do Sets have keys()?

<details>
<summary>Answer</summary>

- [x] Map compatibility — a Set has no real keys, so keys are the values.

</details>


</details>

## Summary

has/add/delete/clear plus size cover membership. forEach, values, keys, and entries cover walking. Remember entries are [value, value], and adding a pair array to a string uses comma joins.

## References

- [JS Set Methods (W3Schools)](https://www.w3schools.com/js/js_set_methods.asp)
- [MDN: Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [MDN: Set.prototype.entries](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/entries)
