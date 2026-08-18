<details>
  <summary>JS Maps</summary>

## Introduction

A Map stores key/value pairs. Keys may be any type, insertion order is kept, size is a property, and Maps are iterable. Create with set() on an empty Map or pass an array of pairs. set() also overwrites. get() reads a value. typeof is object; instanceof Map is true. Compared with objects: objects are not directly iterable, have no size, coerce keys to strings, reorder integer keys, and inherit default keys such as toString.

This section has **12** examples:

- [x] **Example 1:** new Map() then set() [View](#js-maps-example-01)
- [x] **Example 2:** new Map(array of pairs) [View](#js-maps-example-02)
- [x] **Example 3:** set("mangos", 100) [View](#js-maps-example-03)
- [x] **Example 4:** set("apples", 200) — change a value [View](#js-maps-example-04)
- [x] **Example 5:** get("apples") [View](#js-maps-example-05)
- [x] **Example 6:** typeof a Map is object [View](#js-maps-example-06)
- [x] **Example 7:** instanceof Map is true [View](#js-maps-example-07)
- [x] **Example 8:** Object vs Map — not directly iterable [View](#js-maps-example-08)
- [x] **Example 9:** Object vs Map — size property [View](#js-maps-example-09)
- [x] **Example 10:** Object vs Map — key types [View](#js-maps-example-10)
- [x] **Example 11:** Object vs Map — key order [View](#js-maps-example-11)
- [x] **Example 12:** Object vs Map — default keys [View](#js-maps-example-12)

## Detailed Explanation

- [x] Maps remember **insertion order** and expose **size**.
- [x] `set("apples", 200)` overwrites in place → get **200**.
- [x] `get("kiwi")` is **undefined**.
- [x] Objects: not iterable, no size, string keys, integer keys sort first, prototype keys exist.
- [x] Map keys keep types: **1** stays a number; object keys stay objects.

<a id="js-maps-example-01"></a>

### **Example 1: new Map() then set()**

- [x] Create an **empty** Map and `set(key, value)` each pair.
- [x] Map keys can be **any** type. Insertion order is remembered.

Sandbox: `code_sandbox/js-maps/empty-then-set.html`

```javascript
const fruits = new Map();
fruits.set("apples", 500);
fruits.set("bananas", 300);
fruits.set("oranges", 200);
```

<img alt="js-maps example 1 source" src="./code_sandbox/snaps/js-maps-01-code.png" />

<img alt="js-maps example 1 result" src="./code_sandbox/snaps/js-maps-01-result.png" />

- [x] **Outcome:** fruits is **[["apples",500],["bananas",300],["oranges",200]]**. size **3**.

<a id="js-maps-example-02"></a>

### **Example 2: new Map(array of pairs)**

- [x] Pass an array of **[key, value]** pairs to `new Map()`.

Sandbox: `code_sandbox/js-maps/new-map-array.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
```

<img alt="js-maps example 2 source" src="./code_sandbox/snaps/js-maps-02-code.png" />

<img alt="js-maps example 2 result" src="./code_sandbox/snaps/js-maps-02-result.png" />

- [x] **Outcome:** Same three pairs. size **3**.

<a id="js-maps-example-03"></a>

### **Example 3: set("mangos", 100)**

- [x] `set()` **adds** a new key at the end if it did not exist.

Sandbox: `code_sandbox/js-maps/set-mangos.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.set("mangos", 100);
```

<img alt="js-maps example 3 source" src="./code_sandbox/snaps/js-maps-03-code.png" />

<img alt="js-maps example 3 result" src="./code_sandbox/snaps/js-maps-03-result.png" />

- [x] **Outcome:** Now **[["apples",500],["bananas",300],["oranges",200],["mangos",100]]**. size **4**.

<a id="js-maps-example-04"></a>

### **Example 4: set("apples", 200) — change a value**

- [x] `set()` on an **existing** key **overwrites** the value. The key’s position stays.

Sandbox: `code_sandbox/js-maps/change-apples.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.set("apples", 200);
```

<img alt="js-maps example 4 source" src="./code_sandbox/snaps/js-maps-04-code.png" />

<img alt="js-maps example 4 result" src="./code_sandbox/snaps/js-maps-04-result.png" />

- [x] **Outcome:** `get("apples")` is **200**. The pairs are **[["apples",200],["bananas",300],["oranges",200]]**.

<a id="js-maps-example-05"></a>

### **Example 5: get("apples")**

- [x] `get(key)` returns the value, or **undefined** if the key is missing.

Sandbox: `code_sandbox/js-maps/get-apples.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits.get("apples");
```

<img alt="js-maps example 5 source" src="./code_sandbox/snaps/js-maps-05-code.png" />

<img alt="js-maps example 5 result" src="./code_sandbox/snaps/js-maps-05-result.png" />

- [x] **Outcome:** `get("apples")` is **500**. `get("kiwi")` is **undefined**.

<a id="js-maps-example-06"></a>

### **Example 6: typeof a Map is object**

- [x] `typeof` a Map is **object**, same as other objects.

Sandbox: `code_sandbox/js-maps/typeof-object.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
typeof fruits;
```

<img alt="js-maps example 6 source" src="./code_sandbox/snaps/js-maps-06-code.png" />

<img alt="js-maps example 6 result" src="./code_sandbox/snaps/js-maps-06-result.png" />

- [x] **Outcome:** `typeof fruits` is **object**.

<a id="js-maps-example-07"></a>

### **Example 7: instanceof Map is true**

- [x] `fruits instanceof Map` distinguishes Maps from plain objects.

Sandbox: `code_sandbox/js-maps/instanceof-map.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
fruits instanceof Map;
```

<img alt="js-maps example 7 source" src="./code_sandbox/snaps/js-maps-07-code.png" />

<img alt="js-maps example 7 result" src="./code_sandbox/snaps/js-maps-07-result.png" />

- [x] **Outcome:** `instanceof Map` is **true**.

<a id="js-maps-example-08"></a>

### **Example 8: Object vs Map — not directly iterable**

- [x] A plain object is **not** iterable with `for...of`. A Map **is**.

Sandbox: `code_sandbox/js-maps/object-not-iterable.html`

```javascript
const obj = {apples: 500};
const fruits = new Map([['apples', 500]]);
```

<img alt="js-maps example 8 source" src="./code_sandbox/snaps/js-maps-08-code.png" />

<img alt="js-maps example 8 result" src="./code_sandbox/snaps/js-maps-08-result.png" />

- [x] **Outcome:** `for...of obj` throws **TypeError: obj is not iterable**. `Array.from(fruits)` is **[["apples",500]]**.

<a id="js-maps-example-09"></a>

### **Example 9: Object vs Map — size property**

- [x] Maps have **`size`**. Objects do **not** (use `Object.keys(obj).length`).

Sandbox: `code_sandbox/js-maps/size-vs-object.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
const obj = {apples: 500, bananas: 300, oranges: 200};
```

<img alt="js-maps example 9 source" src="./code_sandbox/snaps/js-maps-09-code.png" />

<img alt="js-maps example 9 result" src="./code_sandbox/snaps/js-maps-09-result.png" />

- [x] **Outcome:** `fruits.size` is **3**. `obj.size` is **undefined**. `Object.keys(obj).length` is **3**.

<a id="js-maps-example-10"></a>

### **Example 10: Object vs Map — key types**

- [x] Object keys become **strings** (or symbols). Map keys stay **any** type.

Sandbox: `code_sandbox/js-maps/keys-any-type.html`

```javascript
const obj = {};
obj[1] = 'num';
obj[{x: 1}] = 'obj';
const fruits = new Map();
const key = {x: 1};
fruits.set(1, 'num');
fruits.set(key, 'obj');
```

<img alt="js-maps example 10 source" src="./code_sandbox/snaps/js-maps-10-code.png" />

<img alt="js-maps example 10 result" src="./code_sandbox/snaps/js-maps-10-result.png" />

- [x] **Outcome:** Object.keys is **["1","[object Object]"]** — both coerced to strings. Map keys stay **1** and **{x:1}**. `get(key)` is **obj**. `get(1)` is **num**.

<a id="js-maps-example-11"></a>

### **Example 11: Object vs Map — key order**

- [x] Map iteration follows **insertion** order.
- [x] Object integer keys are sorted **before** string keys.

Sandbox: `code_sandbox/js-maps/insertion-order.html`

```javascript
const obj = {};
obj.z = 1;
obj.a = 2;
obj[1] = 3;
const fruits = new Map();
fruits.set('z', 1);
fruits.set('a', 2);
fruits.set(1, 3);
```

<img alt="js-maps example 11 source" src="./code_sandbox/snaps/js-maps-11-code.png" />

<img alt="js-maps example 11 result" src="./code_sandbox/snaps/js-maps-11-result.png" />

- [x] **Outcome:** Object.keys is **["1","z","a"]** (integer key first). Map keys are **["z","a",1]** (insertion order).

<a id="js-maps-example-12"></a>

### **Example 12: Object vs Map — default keys**

- [x] Objects inherit **`toString`** on the prototype. Maps do **not** have default keys.

Sandbox: `code_sandbox/js-maps/no-default-keys.html`

```javascript
const obj = {};
const fruits = new Map();
```

<img alt="js-maps example 12 source" src="./code_sandbox/snaps/js-maps-12-code.png" />

<img alt="js-maps example 12 result" src="./code_sandbox/snaps/js-maps-12-result.png" />

- [x] **Outcome:** `'toString' in obj` is **true** (prototype). `hasOwnProperty` is **false**. `fruits.has('toString')` is **false**. size **0**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-maps/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you fill an empty Map?

<details>
<summary>Answer</summary>

- [x] `set(key, value)` for each pair.

</details>

### Question 2: What does new Map(pairs) contain?

<details>
<summary>Answer</summary>

- [x] **[["apples",500],["bananas",300],["oranges",200]]**.

</details>

### Question 3: What does set("mangos", 100) do?

<details>
<summary>Answer</summary>

- [x] Appends mangos. size **4**.

</details>

### Question 4: What does set("apples", 200) do?

<details>
<summary>Answer</summary>

- [x] Overwrites apples to **200**. Order unchanged.

</details>

### Question 5: What is get("apples") on the original map?

<details>
<summary>Answer</summary>

- [x] **500**. Missing keys are **undefined**.

</details>

### Question 6: typeof and instanceof?

<details>
<summary>Answer</summary>

- [x] **object** and **true**.

</details>

### Question 7: Can you for...of a plain object?

<details>
<summary>Answer</summary>

- [x] **No.** **TypeError: obj is not iterable**.

</details>

### Question 8: Does an object have size?

<details>
<summary>Answer</summary>

- [x] **undefined**. Use `Object.keys(obj).length` (**3** here).

</details>

### Question 9: What happens to object key `{x:1}`?

<details>
<summary>Answer</summary>

- [x] Becomes **"[object Object]"**. Map keeps the object.

</details>

### Question 10: Object keys after z, a, then 1?

<details>
<summary>Answer</summary>

- [x] **["1","z","a"]**. Map: **["z","a",1]**.

</details>

### Question 11: Does an empty object have toString?

<details>
<summary>Answer</summary>

- [x] `'toString' in obj` is **true** (prototype). `map.has('toString')` is **false**.

</details>


</details>

## Summary

Pick a Map when keys are not only strings, when you need size, or when insertion order must hold. Objects still work for simple string dictionaries but coerce keys and inherit prototype names.

## References

- [JS Maps (W3Schools)](https://www.w3schools.com/js/js_maps.asp)
- [MDN: Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)

</details>
