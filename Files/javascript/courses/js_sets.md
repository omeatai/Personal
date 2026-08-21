# JS Sets

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A JavaScript Set is a collection of unique values. Each value occurs at most once. Create a Set by passing an array to new Set(), or start empty and add(). Values may be primitives or objects. Objects are compared by reference, so two {x:1} literals are two entries. Sets are iterable with for...of. typeof a Set is object; instanceof Set is true.

This section has **10** examples:

- [x] **Example 1:** new Set(["a","b","c"]) [View](#js-sets-example-01)
- [x] **Example 2:** new Set() then add() values [View](#js-sets-example-02)
- [x] **Example 3:** add() variables [View](#js-sets-example-03)
- [x] **Example 4:** add("d") and add("e") [View](#js-sets-example-04)
- [x] **Example 5:** add() equal elements — only the first is kept [View](#js-sets-example-05)
- [x] **Example 6:** for...of lists Set values [View](#js-sets-example-06)
- [x] **Example 7:** typeof a Set is object [View](#js-sets-example-07)
- [x] **Example 8:** instanceof Set is true [View](#js-sets-example-08)
- [x] **Example 9:** Values may be any type [View](#js-sets-example-09)
- [x] **Example 10:** Two similar objects are two values [View](#js-sets-example-10)

## Detailed Explanation

- [x] A Set holds **unique** values in **insertion** order.
- [x] `new Set(array)` or `new Set()` plus `add()`.
- [x] Duplicates from `add()` are ignored — size does not grow.
- [x] `for...of` concatenating `a`,`b`,`c` with no separator is **abc**.
- [x] `typeof` → **object**. `instanceof Set` → **true**.
- [x] `1` and `"1"` are different. The same object added twice is one entry; two similar objects are two.

<a id="js-sets-example-01"></a>

### **Example 1: new Set(["a","b","c"])**

- [x] Pass an **array** to `new Set()` to fill the Set in one step.
- [x] A Set stores **unique** values of any type (primitives or objects).

Sandbox: `code_sandbox/js-sets/new-set-array.html`

```javascript
const letters = new Set(["a","b","c"]);
```

![js-sets example 1 source](../code_sandbox/snaps/js-sets-01-code.png)

![js-sets example 1 result](../code_sandbox/snaps/js-sets-01-result.png)

- [x] **Outcome:** letters is **["a","b","c"]**. size is **3**.

<a id="js-sets-example-02"></a>

### **Example 2: new Set() then add() values**

- [x] You can start **empty** and `add()` values one at a time.

Sandbox: `code_sandbox/js-sets/new-set-add-values.html`

```javascript
const letters = new Set();
letters.add("a");
letters.add("b");
letters.add("c");
```

![js-sets example 2 source](../code_sandbox/snaps/js-sets-02-code.png)

![js-sets example 2 result](../code_sandbox/snaps/js-sets-02-result.png)

- [x] **Outcome:** Same result: **["a","b","c"]**, size **3**.

<a id="js-sets-example-03"></a>

### **Example 3: add() variables**

- [x] `add()` accepts a **variable**. The Set stores the **value**, not the name.

Sandbox: `code_sandbox/js-sets/new-set-add-variables.html`

```javascript
const letters = new Set();
const a = "a";
const b = "b";
const c = "c";
letters.add(a);
letters.add(b);
letters.add(c);
```

![js-sets example 3 source](../code_sandbox/snaps/js-sets-03-code.png)

![js-sets example 3 result](../code_sandbox/snaps/js-sets-03-result.png)

- [x] **Outcome:** Still **["a","b","c"]**. The variables were just another way to pass **"a"**, **"b"**, **"c"**.

<a id="js-sets-example-04"></a>

### **Example 4: add("d") and add("e")**

- [x] `add()` inserts a value if it is **not already** in the Set.
- [x] Insertion order is kept: new values go at the **end**.

Sandbox: `code_sandbox/js-sets/add-d-e.html`

```javascript
const letters = new Set(["a","b","c"]);
letters.add("d");
letters.add("e");
```

![js-sets example 4 source](../code_sandbox/snaps/js-sets-04-code.png)

![js-sets example 4 result](../code_sandbox/snaps/js-sets-04-result.png)

- [x] **Outcome:** letters is **["a","b","c","d","e"]**. size is **5**.

<a id="js-sets-example-05"></a>

### **Example 5: add() equal elements — only the first is kept**

- [x] If you add a value that **already exists**, `add()` does **nothing**.
- [x] That uniqueness is the main Set feature.

Sandbox: `code_sandbox/js-sets/add-duplicates.html`

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

![js-sets example 5 source](../code_sandbox/snaps/js-sets-05-code.png)

![js-sets example 5 result](../code_sandbox/snaps/js-sets-05-result.png)

- [x] **Outcome:** Six `add("c")` calls still leave **["a","b","c"]**. size stays **3**.

<a id="js-sets-example-06"></a>

### **Example 6: for...of lists Set values**

- [x] Sets are **iterable**. `for...of` yields each value in insertion order.

Sandbox: `code_sandbox/js-sets/for-of-list.html`

```javascript
const letters = new Set(["a","b","c"]);
let text = "";
for (const x of letters) {
  text += x;
}
```

![js-sets example 6 source](../code_sandbox/snaps/js-sets-06-code.png)

![js-sets example 6 result](../code_sandbox/snaps/js-sets-06-result.png)

- [x] **Outcome:** text is **"abc"**. The loop concatenated **"a"**, **"b"**, **"c"** with no separator.

<a id="js-sets-example-07"></a>

### **Example 7: typeof a Set is object**

- [x] `typeof` on a Set is **"object"** (same as Array, Date, Map).
- [x] Use `instanceof Set` if you need to tell Sets from other objects.

Sandbox: `code_sandbox/js-sets/typeof-object.html`

```javascript
const letters = new Set(["a","b","c"]);
typeof letters;
```

![js-sets example 7 source](../code_sandbox/snaps/js-sets-07-code.png)

![js-sets example 7 result](../code_sandbox/snaps/js-sets-07-result.png)

- [x] **Outcome:** `typeof letters` is **object**.

<a id="js-sets-example-08"></a>

### **Example 8: instanceof Set is true**

- [x] `letters instanceof Set` is **true** for a real Set.

Sandbox: `code_sandbox/js-sets/instanceof-set.html`

```javascript
const letters = new Set(["a","b","c"]);
letters instanceof Set;
```

![js-sets example 8 source](../code_sandbox/snaps/js-sets-08-code.png)

![js-sets example 8 result](../code_sandbox/snaps/js-sets-08-result.png)

- [x] **Outcome:** `instanceof Set` is **true**.

<a id="js-sets-example-09"></a>

### **Example 9: Values may be any type**

- [x] The page says values can be **primitives or objects**.
- [x] `1` and `"1"` are **different**. The same object added twice is **one** entry.

Sandbox: `code_sandbox/js-sets/mixed-types.html`

```javascript
const obj = {n: 1};
const letters = new Set([1, "1", obj, obj]);
```

![js-sets example 9 source](../code_sandbox/snaps/js-sets-09-code.png)

![js-sets example 9 result](../code_sandbox/snaps/js-sets-09-result.png)

- [x] **Outcome:** The Set is **[1,"1",{"n":1}]**. size is **3** — `obj` was stored once.

<a id="js-sets-example-10"></a>

### **Example 10: Two similar objects are two values**

- [x] Objects compare by **reference**, not by matching fields.
- [x] `{x:1}` and another `{x:1}` are **two** Set entries.

Sandbox: `code_sandbox/js-sets/two-objects-distinct.html`

```javascript
const a = {x: 1};
const b = {x: 1};
const letters = new Set([a, b]);
```

![js-sets example 10 source](../code_sandbox/snaps/js-sets-10-code.png)

![js-sets example 10 result](../code_sandbox/snaps/js-sets-10-result.png)

- [x] **Outcome:** size is **2**. JSON is **[{"x":1},{"x":1}]** — same shape, two objects.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-sets/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is in `new Set(["a","b","c"])`?

<details>
<summary>Answer</summary>

- [x] **["a","b","c"]**. size **3**.

</details>

### Question 2: Does starting empty and add() match the array constructor?

<details>
<summary>Answer</summary>

- [x] **Yes** — still **a, b, c**.

</details>

### Question 3: What happens if you add variables a, b, c holding those strings?

<details>
<summary>Answer</summary>

- [x] The Set still stores **"a"**, **"b"**, **"c"**.

</details>

### Question 4: What is `letters` after add("d") and add("e")?

<details>
<summary>Answer</summary>

- [x] **["a","b","c","d","e"]**, size **5**.

</details>

### Question 5: What if you `add("c")` six times?

<details>
<summary>Answer</summary>

- [x] Still **3** values. Extra adds are ignored.

</details>

### Question 6: What does `for...of` concatenation produce?

<details>
<summary>Answer</summary>

- [x] **"abc"** — no commas or spaces.

</details>

### Question 7: What is `typeof letters`?

<details>
<summary>Answer</summary>

- [x] **object**.

</details>

### Question 8: What is `letters instanceof Set`?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 9: Are `1` and `"1"` the same Set value?

<details>
<summary>Answer</summary>

- [x] **No.** Mixed example size is **3**: number, string, one object.

</details>

### Question 10: Are two `{x:1}` objects one Set value?

<details>
<summary>Answer</summary>

- [x] **No.** size **2** — reference equality.

</details>


</details>

## Summary

Use a Set when membership and uniqueness matter. Build from an array or add() into an empty Set. Duplicates do not land. Iterate with for...of. Check the type with instanceof Set, not typeof.

## References

- [JS Sets (W3Schools)](https://www.w3schools.com/js/js_sets.asp)
- [MDN: Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
