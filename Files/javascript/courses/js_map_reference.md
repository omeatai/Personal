# JS Map Reference

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The July 2025 Map reference lists constructor, mutators, accessors, iterators, size, and Map.groupBy. Each table row is its own Example on the apples/bananas/oranges map except groupBy, which uses the quantity fruit array.

This section has **12** examples:

- [x] **Example 1:** new Map() — creates a new Map object [View](#js-map-reference-example-01)
- [x] **Example 2:** clear() — removes all elements [View](#js-map-reference-example-02)
- [x] **Example 3:** delete() — removes a Map element by key [View](#js-map-reference-example-03)
- [x] **Example 4:** entries() — [key, value] iterator [View](#js-map-reference-example-04)
- [x] **Example 5:** forEach() — callback per pair [View](#js-map-reference-example-05)
- [x] **Example 6:** get() — value for a key [View](#js-map-reference-example-06)
- [x] **Example 7:** groupBy() — Map.groupBy [View](#js-map-reference-example-07)
- [x] **Example 8:** has() — whether a key exists [View](#js-map-reference-example-08)
- [x] **Example 9:** keys() — key iterator [View](#js-map-reference-example-09)
- [x] **Example 10:** set() — set the value for a key [View](#js-map-reference-example-10)
- [x] **Example 11:** size — number of Map elements [View](#js-map-reference-example-11)
- [x] **Example 12:** values() — value iterator [View](#js-map-reference-example-12)

## Detailed Explanation

- [x] **Every table row is an Example.**
- [x] `set` returns the same Map. `delete` returns a boolean. `clear` empties.
- [x] `forEach` is `(value, key)`.
- [x] groupBy keys **ok** / **low** with two fruits each.
- [x] `size` is a property listed on the method table.

<a id="js-map-reference-example-01"></a>

### **Example 1: new Map() — creates a new Map object**

- [x] Construct from an array of pairs.

Sandbox: `code_sandbox/js-map-reference/new-map.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
```

![js-map-reference example 1 source](../code_sandbox/snaps/js-map-reference-01-code.png)

![js-map-reference example 1 result](../code_sandbox/snaps/js-map-reference-01-result.png)

- [x] **Outcome:** **[["apples",500],["bananas",300],["oranges",200]]**, size **3**.

<a id="js-map-reference-example-02"></a>

### **Example 2: clear() — removes all elements**

- [x] Empties the Map.

Sandbox: `code_sandbox/js-map-reference/clear.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.clear();
```

![js-map-reference example 2 source](../code_sandbox/snaps/js-map-reference-02-code.png)

![js-map-reference example 2 result](../code_sandbox/snaps/js-map-reference-02-result.png)

- [x] **Outcome:** size **0**, **[]**.

<a id="js-map-reference-example-03"></a>

### **Example 3: delete() — removes a Map element by key**

- [x] Returns whether the key existed.

Sandbox: `code_sandbox/js-map-reference/delete.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
const ok = fruits.delete("apples");
```

![js-map-reference example 3 source](../code_sandbox/snaps/js-map-reference-03-code.png)

![js-map-reference example 3 result](../code_sandbox/snaps/js-map-reference-03-result.png)

- [x] **Outcome:** `delete("apples")` is **true**. Remaining **[["bananas",300],["oranges",200]]**.

<a id="js-map-reference-example-04"></a>

### **Example 4: entries() — [key, value] iterator**

- [x] Yields each pair as a two-element array.

Sandbox: `code_sandbox/js-map-reference/entries.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
const pairs = Array.from(fruits.entries());
```

![js-map-reference example 4 source](../code_sandbox/snaps/js-map-reference-04-code.png)

![js-map-reference example 4 result](../code_sandbox/snaps/js-map-reference-04-result.png)

- [x] **Outcome:** **[["apples",500],["bananas",300],["oranges",200]]**.

<a id="js-map-reference-example-05"></a>

### **Example 5: forEach() — callback per pair**

- [x] Callback arguments are `(value, key)`.

Sandbox: `code_sandbox/js-map-reference/for-each.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
let text = "";
fruits.forEach(function (value, key) {
  text += key + "=" + value + ";";
});
```

![js-map-reference example 5 source](../code_sandbox/snaps/js-map-reference-05-code.png)

![js-map-reference example 5 result](../code_sandbox/snaps/js-map-reference-05-result.png)

- [x] **Outcome:** text is **"apples=500;bananas=300;oranges=200;"**.

<a id="js-map-reference-example-06"></a>

### **Example 6: get() — value for a key**

- [x] Missing keys return **undefined**.

Sandbox: `code_sandbox/js-map-reference/get.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.get("bananas");
```

![js-map-reference example 6 source](../code_sandbox/snaps/js-map-reference-06-code.png)

![js-map-reference example 6 result](../code_sandbox/snaps/js-map-reference-06-result.png)

- [x] **Outcome:** `get("bananas")` is **300**. `get("kiwi")` is **undefined**.

<a id="js-map-reference-example-07"></a>

### **Example 7: groupBy() — Map.groupBy**

- [x] Static `Map.groupBy` groups an iterable by callback results.

Sandbox: `code_sandbox/js-map-reference/group-by.html`

```javascript
const fruits = [
  {name:"apples", quantity:300},
  {name:"bananas", quantity:500},
  {name:"oranges", quantity:200},
  {name:"kiwi", quantity:150}
];
function myCallback({ quantity }) {
  return quantity > 200 ? "ok" : "low";
}
const result = Map.groupBy(fruits, myCallback);
```

![js-map-reference example 7 source](../code_sandbox/snaps/js-map-reference-07-code.png)

![js-map-reference example 7 result](../code_sandbox/snaps/js-map-reference-07-result.png)

- [x] **Outcome:** keys are **["ok","low"]**. **"ok"** has **2** fruits (apples, bananas). **"low"** has **2** (oranges, kiwi).

<a id="js-map-reference-example-08"></a>

### **Example 8: has() — whether a key exists**

- [x] Boolean membership on the **key**.

Sandbox: `code_sandbox/js-map-reference/has.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.has("oranges");
```

![js-map-reference example 8 source](../code_sandbox/snaps/js-map-reference-08-code.png)

![js-map-reference example 8 result](../code_sandbox/snaps/js-map-reference-08-result.png)

- [x] **Outcome:** `has("oranges")` is **true**. `has("kiwi")` is **false**.

<a id="js-map-reference-example-09"></a>

### **Example 9: keys() — key iterator**

- [x] Insertion-order keys.

Sandbox: `code_sandbox/js-map-reference/keys.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
const list = Array.from(fruits.keys());
```

![js-map-reference example 9 source](../code_sandbox/snaps/js-map-reference-09-code.png)

![js-map-reference example 9 result](../code_sandbox/snaps/js-map-reference-09-result.png)

- [x] **Outcome:** **["apples","bananas","oranges"]**.

<a id="js-map-reference-example-10"></a>

### **Example 10: set() — set the value for a key**

- [x] Adds or overwrites. Returns the **same** Map.

Sandbox: `code_sandbox/js-map-reference/set.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
const ret = fruits.set("apples", 200);
```

![js-map-reference example 10 source](../code_sandbox/snaps/js-map-reference-10-code.png)

![js-map-reference example 10 result](../code_sandbox/snaps/js-map-reference-10-result.png)

- [x] **Outcome:** `get("apples")` is **200**. `set` returned the same Map (**true**).

<a id="js-map-reference-example-11"></a>

### **Example 11: size — number of Map elements**

- [x] Listed on the method table; it is a **property**.

Sandbox: `code_sandbox/js-map-reference/size.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.size;
```

![js-map-reference example 11 source](../code_sandbox/snaps/js-map-reference-11-code.png)

![js-map-reference example 11 result](../code_sandbox/snaps/js-map-reference-11-result.png)

- [x] **Outcome:** `size` is **3**.

<a id="js-map-reference-example-12"></a>

### **Example 12: values() — value iterator**

- [x] Insertion-order values.

Sandbox: `code_sandbox/js-map-reference/values.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
const list = Array.from(fruits.values());
```

![js-map-reference example 12 source](../code_sandbox/snaps/js-map-reference-12-code.png)

![js-map-reference example 12 result](../code_sandbox/snaps/js-map-reference-12-result.png)

- [x] **Outcome:** **[500,300,200]**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-map-reference/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does new Map(pairs) create?

<details>
<summary>Answer</summary>

- [x] A Map of three fruit pairs, size **3**.

</details>

### Question 2: What does clear() do?

<details>
<summary>Answer</summary>

- [x] size **0**, **[]**.

</details>

### Question 3: delete("apples")?

<details>
<summary>Answer</summary>

- [x] **true**, leftover bananas and oranges.

</details>

### Question 4: What does entries() yield?

<details>
<summary>Answer</summary>

- [x] **[["apples",500],["bananas",300],["oranges",200]]**.

</details>

### Question 5: get("bananas") vs get("kiwi")?

<details>
<summary>Answer</summary>

- [x] **300** vs **undefined**.

</details>

### Question 6: groupBy keys and lengths?

<details>
<summary>Answer</summary>

- [x] **["ok","low"]**, two fruits each.

</details>

### Question 7: has("oranges") vs has("kiwi")?

<details>
<summary>Answer</summary>

- [x] **true** / **false**.

</details>

### Question 8: What are keys() and values()?

<details>
<summary>Answer</summary>

- [x] keys **["apples","bananas","oranges"]**. values **[500,300,200]**.

</details>

### Question 9: set("apples", 200) return value?

<details>
<summary>Answer</summary>

- [x] The **same** Map. get becomes **200**.

</details>

### Question 10: Is size a method?

<details>
<summary>Answer</summary>

- [x] **No.** It is a **property** (still one table row / Example).

</details>


</details>

## Summary

The Map catalog is construct, clear/delete/set, get/has/size, iterate keys/values/entries/forEach, and groupBy for grouping an iterable into a Map.

## References

- [JS Map Reference (W3Schools)](https://www.w3schools.com/js/js_map_reference.asp)
- [MDN: Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [MDN: Map.groupBy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy)
