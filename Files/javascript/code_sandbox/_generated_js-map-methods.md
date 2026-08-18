<details>
  <summary>JS Map Methods</summary>

## Introduction

Map methods cover construct, get, set, size, delete, clear, has, and the iterators. forEach is (value, key). Object keys work; get('apples') is undefined when the key is an object named apples. Map.groupBy (ES2024) groups an iterable into a Map. Object.groupBy does the same into a plain object. Summing values() of 500+300+200 is 1000.

This section has **18** examples:

- [x] **Example 1:** new Map() from pairs [View](#js-map-methods-example-01)
- [x] **Example 2:** get() [View](#js-map-methods-example-02)
- [x] **Example 3:** set() — create and fill [View](#js-map-methods-example-03)
- [x] **Example 4:** set("apples", 500) — overwrite [View](#js-map-methods-example-04)
- [x] **Example 5:** size [View](#js-map-methods-example-05)
- [x] **Example 6:** delete() [View](#js-map-methods-example-06)
- [x] **Example 7:** clear() [View](#js-map-methods-example-07)
- [x] **Example 8:** has() [View](#js-map-methods-example-08)
- [x] **Example 9:** delete() then has() [View](#js-map-methods-example-09)
- [x] **Example 10:** forEach() [View](#js-map-methods-example-10)
- [x] **Example 11:** entries() [View](#js-map-methods-example-11)
- [x] **Example 12:** keys() [View](#js-map-methods-example-12)
- [x] **Example 13:** values() [View](#js-map-methods-example-13)
- [x] **Example 14:** sum values() [View](#js-map-methods-example-14)
- [x] **Example 15:** Objects as keys [View](#js-map-methods-example-15)
- [x] **Example 16:** get("apples") when the key is an object [View](#js-map-methods-example-16)
- [x] **Example 17:** Map.groupBy() [View](#js-map-methods-example-17)
- [x] **Example 18:** Object.groupBy() vs Map.groupBy() [View](#js-map-methods-example-18)

## Detailed Explanation

- [x] `delete` returns a boolean. `clear` empties. `has` follows delete.
- [x] `forEach` text is **"apples = 500bananas = 300oranges = 200"** (no gap between pairs).
- [x] `entries` concat is **"apples,500bananas,300oranges,200"**.
- [x] Object key: `get(apples)` **500**, `get("apples")` **undefined**.
- [x] groupBy quantity>200: **ok** = apples+bananas, **low** = oranges+kiwi. Original array unchanged.
- [x] Object.groupBy → plain object JSON; Map.groupBy → `instanceof Map` **true**.

<a id="js-map-methods-example-01"></a>

### **Example 1: new Map() from pairs**

- [x] Pass `[key, value]` pairs to the constructor.

Sandbox: `code_sandbox/js-map-methods/new-map-array.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
```

<img alt="js-map-methods example 1 source" src="./code_sandbox/snaps/js-map-methods-01-code.png" />

<img alt="js-map-methods example 1 result" src="./code_sandbox/snaps/js-map-methods-01-result.png" />

- [x] **Outcome:** **[["apples",500],["bananas",300],["oranges",200]]**.

<a id="js-map-methods-example-02"></a>

### **Example 2: get()**

- [x] `get(key)` reads the value for that key.

Sandbox: `code_sandbox/js-map-methods/get.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.get("apples");
```

<img alt="js-map-methods example 2 source" src="./code_sandbox/snaps/js-map-methods-02-code.png" />

<img alt="js-map-methods example 2 result" src="./code_sandbox/snaps/js-map-methods-02-result.png" />

- [x] **Outcome:** `get("apples")` is **500**.

<a id="js-map-methods-example-03"></a>

### **Example 3: set() — create and fill**

- [x] `set(key, value)` adds pairs to an empty Map.

Sandbox: `code_sandbox/js-map-methods/set-create.html`

```javascript
const fruits = new Map();
fruits.set("apples", 500);
fruits.set("bananas", 300);
fruits.set("oranges", 200);
```

<img alt="js-map-methods example 3 source" src="./code_sandbox/snaps/js-map-methods-03-code.png" />

<img alt="js-map-methods example 3 result" src="./code_sandbox/snaps/js-map-methods-03-result.png" />

- [x] **Outcome:** Three pairs, size **3**.

<a id="js-map-methods-example-04"></a>

### **Example 4: set("apples", 500) — overwrite**

- [x] The page uses `set` to **change** an existing key.
- [x] Here apples was already **500**, so the stored value stays **500**.

Sandbox: `code_sandbox/js-map-methods/set-change.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.set("apples", 500);
```

<img alt="js-map-methods example 4 source" src="./code_sandbox/snaps/js-map-methods-04-code.png" />

<img alt="js-map-methods example 4 result" src="./code_sandbox/snaps/js-map-methods-04-result.png" />

- [x] **Outcome:** `get("apples")` is still **500**. The key was overwritten with the same number.

<a id="js-map-methods-example-05"></a>

### **Example 5: size**

- [x] `size` is the number of key/value pairs.

Sandbox: `code_sandbox/js-map-methods/size.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.size;
```

<img alt="js-map-methods example 5 source" src="./code_sandbox/snaps/js-map-methods-05-code.png" />

<img alt="js-map-methods example 5 result" src="./code_sandbox/snaps/js-map-methods-05-result.png" />

- [x] **Outcome:** `size` is **3**.

<a id="js-map-methods-example-06"></a>

### **Example 6: delete()**

- [x] `delete(key)` removes that pair and returns **true** if it existed.

Sandbox: `code_sandbox/js-map-methods/delete.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
const ok = fruits.delete("apples");
```

<img alt="js-map-methods example 6 source" src="./code_sandbox/snaps/js-map-methods-06-code.png" />

<img alt="js-map-methods example 6 result" src="./code_sandbox/snaps/js-map-methods-06-result.png" />

- [x] **Outcome:** `delete("apples")` is **true**. size **2**. Remaining **[["bananas",300],["oranges",200]]**.

<a id="js-map-methods-example-07"></a>

### **Example 7: clear()**

- [x] `clear()` removes **every** pair.

Sandbox: `code_sandbox/js-map-methods/clear.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.clear();
```

<img alt="js-map-methods example 7 source" src="./code_sandbox/snaps/js-map-methods-07-code.png" />

<img alt="js-map-methods example 7 result" src="./code_sandbox/snaps/js-map-methods-07-result.png" />

- [x] **Outcome:** size **0**, **[]**.

<a id="js-map-methods-example-08"></a>

### **Example 8: has()**

- [x] `has(key)` is **true** if the key exists.

Sandbox: `code_sandbox/js-map-methods/has.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.has("apples");
```

<img alt="js-map-methods example 8 source" src="./code_sandbox/snaps/js-map-methods-08-code.png" />

<img alt="js-map-methods example 8 result" src="./code_sandbox/snaps/js-map-methods-08-result.png" />

- [x] **Outcome:** `has("apples")` is **true**. `has("kiwi")` is **false**.

<a id="js-map-methods-example-09"></a>

### **Example 9: delete() then has()**

- [x] After deleting a key, `has` becomes **false**.

Sandbox: `code_sandbox/js-map-methods/delete-then-has.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.delete("apples");
fruits.has("apples");
```

<img alt="js-map-methods example 9 source" src="./code_sandbox/snaps/js-map-methods-09-code.png" />

<img alt="js-map-methods example 9 result" src="./code_sandbox/snaps/js-map-methods-09-result.png" />

- [x] **Outcome:** After `delete("apples")`, `has("apples")` is **false**. size **2**.

<a id="js-map-methods-example-10"></a>

### **Example 10: forEach()**

- [x] `forEach(callback)` runs per pair.
- [x] The callback is **`(value, key)`** — value first, like Array, unlike `Map`’s mental [key,value] order.

Sandbox: `code_sandbox/js-map-methods/for-each.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
let text = "";
fruits.forEach(function (value, key) {
  text += key + " = " + value;
});
```

<img alt="js-map-methods example 10 source" src="./code_sandbox/snaps/js-map-methods-10-code.png" />

<img alt="js-map-methods example 10 result" src="./code_sandbox/snaps/js-map-methods-10-result.png" />

- [x] **Outcome:** text is **"apples = 500bananas = 300oranges = 200"** (no separator between pairs).

<a id="js-map-methods-example-11"></a>

### **Example 11: entries()**

- [x] `entries()` yields **[key, value]** pairs. `text += pair` stringifies with a comma.

Sandbox: `code_sandbox/js-map-methods/entries.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
let text = "";
for (const x of fruits.entries()) {
  text += x;
}
```

<img alt="js-map-methods example 11 source" src="./code_sandbox/snaps/js-map-methods-11-code.png" />

<img alt="js-map-methods example 11 result" src="./code_sandbox/snaps/js-map-methods-11-result.png" />

- [x] **Outcome:** text is **"apples,500bananas,300oranges,200"**. Pairs are **[["apples",500],["bananas",300],["oranges",200]]**.

<a id="js-map-methods-example-12"></a>

### **Example 12: keys()**

- [x] `keys()` iterates the keys in insertion order.

Sandbox: `code_sandbox/js-map-methods/keys.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
let text = "";
for (const x of fruits.keys()) {
  text += x;
}
```

<img alt="js-map-methods example 12 source" src="./code_sandbox/snaps/js-map-methods-12-code.png" />

<img alt="js-map-methods example 12 result" src="./code_sandbox/snaps/js-map-methods-12-result.png" />

- [x] **Outcome:** text is **"applesbananasoranges"**. keys are **["apples","bananas","oranges"]**.

<a id="js-map-methods-example-13"></a>

### **Example 13: values()**

- [x] `values()` iterates the values.

Sandbox: `code_sandbox/js-map-methods/values.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
let text = "";
for (const x of fruits.values()) {
  text += x;
}
```

<img alt="js-map-methods example 13 source" src="./code_sandbox/snaps/js-map-methods-13-code.png" />

<img alt="js-map-methods example 13 result" src="./code_sandbox/snaps/js-map-methods-13-result.png" />

- [x] **Outcome:** text is **"500300200"** (string concat from `""`). values are **[500,300,200]**.

<a id="js-map-methods-example-14"></a>

### **Example 14: sum values()**

- [x] Loop `values()` with `+=` on a **number** to total them.

Sandbox: `code_sandbox/js-map-methods/values-sum.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
let total = 0;
for (const x of fruits.values()) {
  total += x;
}
```

<img alt="js-map-methods example 14 source" src="./code_sandbox/snaps/js-map-methods-14-code.png" />

<img alt="js-map-methods example 14 result" src="./code_sandbox/snaps/js-map-methods-14-result.png" />

- [x] **Outcome:** total is **1000** (500 + 300 + 200).

<a id="js-map-methods-example-15"></a>

### **Example 15: Objects as keys**

- [x] Using **objects** as keys is a Map feature objects cannot match.
- [x] The key is the object **reference**, not `name`.

Sandbox: `code_sandbox/js-map-methods/objects-as-keys.html`

```javascript
const apples = {name: "Apples"};
const bananas = {name: "Bananas"};
const oranges = {name: "Oranges"};
const fruits = new Map();
fruits.set(apples, 500);
fruits.set(bananas, 300);
fruits.set(oranges, 200);
```

<img alt="js-map-methods example 15 source" src="./code_sandbox/snaps/js-map-methods-15-code.png" />

<img alt="js-map-methods example 15 result" src="./code_sandbox/snaps/js-map-methods-15-result.png" />

- [x] **Outcome:** JSON is **[[{"name":"Apples"},500],[{"name":"Bananas"},300],[{"name":"Oranges"},200]]**. `get(apples)` is **500**.

<a id="js-map-methods-example-16"></a>

### **Example 16: get("apples") when the key is an object**

- [x] The key is the **object** `apples`, not the string **"apples"**.

Sandbox: `code_sandbox/js-map-methods/get-string-undefined.html`

```javascript
const apples = {name: "Apples"};
const fruits = new Map();
fruits.set(apples, 500);
fruits.get("apples");
```

<img alt="js-map-methods example 16 source" src="./code_sandbox/snaps/js-map-methods-16-code.png" />

<img alt="js-map-methods example 16 result" src="./code_sandbox/snaps/js-map-methods-16-result.png" />

- [x] **Outcome:** `get("apples")` is **undefined**. `get(apples)` is **500**.

<a id="js-map-methods-example-17"></a>

### **Example 17: Map.groupBy()**

- [x] `Map.groupBy(iterable, callback)` groups elements by the callback’s return value.
- [x] The original array is **not** changed. Result is a **Map** of key → array.
- [x] `quantity > 200` → **"ok"**, else **"low"**.

Sandbox: `code_sandbox/js-map-methods/group-by.html`

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

<img alt="js-map-methods example 17 source" src="./code_sandbox/snaps/js-map-methods-17-code.png" />

<img alt="js-map-methods example 17 result" src="./code_sandbox/snaps/js-map-methods-17-result.png" />

- [x] **Outcome:** result is **[["ok",[{"name":"apples","quantity":300},{"name":"bananas","quantity":500}]],["low",[{"name":"oranges","quantity":200},{"name":"kiwi","quantity":150}]]]**. `instanceof Map` is **true**. The input array is unchanged.

<a id="js-map-methods-example-18"></a>

### **Example 18: Object.groupBy() vs Map.groupBy()**

- [x] The page names **`Object.groupBy()`**: same grouping, result is a **plain object**.
- [x] No Tryit — still run it on the same fruit list.

Sandbox: `code_sandbox/js-map-methods/object-group-by.html`

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
const obj = Object.groupBy(fruits, myCallback);
const map = Map.groupBy(fruits, myCallback);
```

<img alt="js-map-methods example 18 source" src="./code_sandbox/snaps/js-map-methods-18-code.png" />

<img alt="js-map-methods example 18 result" src="./code_sandbox/snaps/js-map-methods-18-result.png" />

- [x] **Outcome:** Object.groupBy JSON is **{"ok":[{"name":"apples","quantity":300},{"name":"bananas","quantity":500}],"low":[{"name":"oranges","quantity":200},{"name":"kiwi","quantity":150}]}**. `obj instanceof Map` is **false**. `map instanceof Map` is **true**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-map-methods/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is get("apples")?

<details>
<summary>Answer</summary>

- [x] **500**.

</details>

### Question 2: What is size of the three-fruit map?

<details>
<summary>Answer</summary>

- [x] **3**.

</details>

### Question 3: What does delete("apples") return?

<details>
<summary>Answer</summary>

- [x] **true**, size **2**, leftover bananas and oranges.

</details>

### Question 4: What does clear() leave?

<details>
<summary>Answer</summary>

- [x] size **0**, **[]**.

</details>

### Question 5: has("apples") then delete then has?

<details>
<summary>Answer</summary>

- [x] **true**, then **false**.

</details>

### Question 6: forEach callback argument order?

<details>
<summary>Answer</summary>

- [x] **(value, key)** — value first.

</details>

### Question 7: What is the values() string concat vs the sum?

<details>
<summary>Answer</summary>

- [x] Concat **"500300200"**. Sum **1000**.

</details>

### Question 8: Why is get("apples") undefined with object keys?

<details>
<summary>Answer</summary>

- [x] The key is the **object**, not the string.

</details>

### Question 9: What does Map.groupBy return?

<details>
<summary>Answer</summary>

- [x] A **Map**. ok has 2, low has 2. Input array unchanged.

</details>

### Question 10: Object.groupBy vs Map.groupBy?

<details>
<summary>Answer</summary>

- [x] Object → plain object (`instanceof Map` **false**). Map → Map.

</details>

### Question 11: Does set() on an existing key move it?

<details>
<summary>Answer</summary>

- [x] **No.** It overwrites the value in place.

</details>


</details>

## Summary

get/set/has/delete/clear plus size are the mutators. Iterators give keys, values, or pairs. Object keys are references. groupBy builds a Map of groups; Object.groupBy builds a plain object instead.

## References

- [JS Map Methods (W3Schools)](https://www.w3schools.com/js/js_map_methods.asp)
- [MDN: Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [MDN: Map.groupBy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy)

</details>
