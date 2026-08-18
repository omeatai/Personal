<details>
  <summary>JS Object Types</summary>

## Introduction

Besides primitives, JavaScript has objects: literal { } collections, arrays, maps, sets, dates, regexps, errors, JSON, promises, and typed arrays. typeof is "object" for almost all of them (functions are "function"). Math and JSON are singleton objects, not constructors — new Math() is TypeError. Arrays are 0-based. WeakMap and WeakSet hold objects weakly and cannot be listed. Date-only ISO strings are UTC midnight, so this Mountain zone prints the previous evening.

This section has **23** examples:

- [x] **Example 1:** Person object with 4 properties [View](#js-object-types-example-01)
- [x] **Example 2:** Array cars = ["Saab", "Volvo", "BMW"] [View](#js-object-types-example-02)
- [x] **Example 3:** typeof strings — "", "John", "John Doe" [View](#js-object-types-example-03)
- [x] **Example 4:** typeof numbers — 0, 314, 3.14, (3), (3+4) [View](#js-object-types-example-04)
- [x] **Example 5:** new Math() is TypeError [View](#js-object-types-example-05)
- [x] **Example 6:** Array [View](#js-object-types-example-06)
- [x] **Example 7:** Map [View](#js-object-types-example-07)
- [x] **Example 8:** Set [View](#js-object-types-example-08)
- [x] **Example 9:** WeakMap [View](#js-object-types-example-09)
- [x] **Example 10:** WeakSet [View](#js-object-types-example-10)
- [x] **Example 11:** Math [View](#js-object-types-example-11)
- [x] **Example 12:** Date [View](#js-object-types-example-12)
- [x] **Example 13:** RegExp [View](#js-object-types-example-13)
- [x] **Example 14:** Error [View](#js-object-types-example-14)
- [x] **Example 15:** JSON [View](#js-object-types-example-15)
- [x] **Example 16:** Promise [View](#js-object-types-example-16)
- [x] **Example 17:** Int8Array [View](#js-object-types-example-17)
- [x] **Example 18:** Int16Array [View](#js-object-types-example-18)
- [x] **Example 19:** Int32Array [View](#js-object-types-example-19)
- [x] **Example 20:** Float16Array [View](#js-object-types-example-20)
- [x] **Example 21:** Float32Array [View](#js-object-types-example-21)
- [x] **Example 22:** Float64Array [View](#js-object-types-example-22)
- [x] **Example 23:** BigInt64Array [View](#js-object-types-example-23)

## Detailed Explanation

- [x] Literal objects: **`{ firstName:"John", … }`**. Arrays: **`["Saab", "Volvo", "BMW"]`** with **`[0]`** first.
- [x] Table rows each have an Example: Array, Map, Set, WeakMap, WeakSet, Math, Date, RegExp, Error, JSON, Promise, and the typed arrays including **Float16Array**.
- [x] **`new Math()`** is **TypeError: Math is not a constructor**.
- [x] typeof array/map/set/date is **"object"**. Recognize arrays with **Array.isArray**.

<a id="js-object-types-example-01"></a>

### **Example 1: Person object with 4 properties**

- [x] Objects use **`{ }`**. Properties are **name:value** pairs separated by commas.

Sandbox: `code_sandbox/js-object-types/person-object.html`

```javascript
const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
```

<img alt="js-object-types example 1 source" src="./code_sandbox/snaps/js-object-types-01-code.png" />

<img alt="js-object-types example 1 result" src="./code_sandbox/snaps/js-object-types-01-result.png" />

- [x] **Outcome:** firstName is **"John"**, age is **50**. typeof is **"object"**.

<a id="js-object-types-example-02"></a>

### **Example 2: Array cars = ["Saab", "Volvo", "BMW"]**

- [x] Arrays use **`[ ]`**. Indexes are **0-based**: first item is `[0]`.

Sandbox: `code_sandbox/js-object-types/array-tryit.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
```

<img alt="js-object-types example 2 source" src="./code_sandbox/snaps/js-object-types-02-code.png" />

<img alt="js-object-types example 2 result" src="./code_sandbox/snaps/js-object-types-02-result.png" />

- [x] **Outcome:** [0] **"Saab"**, [1] **"Volvo"**, [2] **"BMW"**. length **3**.

<a id="js-object-types-example-03"></a>

### **Example 3: typeof strings — "", "John", "John Doe"**

- [x] This page repeats the string `typeof` Tryit. Strings are **not** objects.

Sandbox: `code_sandbox/js-object-types/typeof-strings.html`

```javascript
typeof "";
typeof "John";
typeof "John Doe";
```

<img alt="js-object-types example 3 source" src="./code_sandbox/snaps/js-object-types-03-code.png" />

<img alt="js-object-types example 3 result" src="./code_sandbox/snaps/js-object-types-03-result.png" />

- [x] **Outcome:** All three are **"string"**.

<a id="js-object-types-example-04"></a>

### **Example 4: typeof numbers — 0, 314, 3.14, (3), (3+4)**

- [x] This page repeats the number `typeof` Tryit. Numbers are **not** objects.

Sandbox: `code_sandbox/js-object-types/typeof-numbers.html`

```javascript
typeof 0;
typeof 314;
typeof 3.14;
typeof (3);
typeof (3 + 4);
```

<img alt="js-object-types example 4 source" src="./code_sandbox/snaps/js-object-types-04-code.png" />

<img alt="js-object-types example 4 result" src="./code_sandbox/snaps/js-object-types-04-result.png" />

- [x] **Outcome:** All five are **"number"**.

<a id="js-object-types-example-05"></a>

### **Example 5: new Math() is TypeError**

- [x] **Math** is listed as a built-in object, but it is **not constructable**.

Sandbox: `code_sandbox/js-object-types/math-not-constructor.html`

```javascript
new Math();
```

<img alt="js-object-types example 5 source" src="./code_sandbox/snaps/js-object-types-05-code.png" />

<img alt="js-object-types example 5 result" src="./code_sandbox/snaps/js-object-types-05-result.png" />

- [x] **Outcome:** **TypeError: Math is not a constructor**.

<a id="js-object-types-example-06"></a>

### **Example 6: Array**

- [x] An **Array** is a list of values at a **numeric index** (0-based).
- [x] `typeof` an array is **"object"**. Use **`Array.isArray`** to recognize it.

Sandbox: `code_sandbox/js-object-types/obj-array.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
```

<img alt="js-object-types example 6 source" src="./code_sandbox/snaps/js-object-types-06-code.png" />

<img alt="js-object-types example 6 result" src="./code_sandbox/snaps/js-object-types-06-result.png" />

- [x] **Outcome:** Print is **Saab,Volvo,BMW**. cars[0] is **"Saab"**. typeof is **"object"**. `Array.isArray` is **true**.

<a id="js-object-types-example-07"></a>

### **Example 7: Map**

- [x] A **Map** holds **key-value** pairs. Keys may be **any** type (not just strings).

Sandbox: `code_sandbox/js-object-types/obj-map.html`

```javascript
const m = new Map([["apples", 500], ["bananas", 300]]);
let n = m.get("apples");
```

<img alt="js-object-types example 7 source" src="./code_sandbox/snaps/js-object-types-07-code.png" />

<img alt="js-object-types example 7 result" src="./code_sandbox/snaps/js-object-types-07-result.png" />

- [x] **Outcome:** get("apples") is **500**. size is **2**. typeof is **"object"**.

<a id="js-object-types-example-08"></a>

### **Example 8: Set**

- [x] A **Set** stores **unique** values. Duplicates are kept once.

Sandbox: `code_sandbox/js-object-types/obj-set.html`

```javascript
const s = new Set(["A", "B", "A"]);
let n = s.size;
```

<img alt="js-object-types example 8 source" src="./code_sandbox/snaps/js-object-types-08-code.png" />

<img alt="js-object-types example 8 result" src="./code_sandbox/snaps/js-object-types-08-result.png" />

- [x] **Outcome:** size is **2** (the second **"A"** was ignored). `has("A")` is **true**. typeof is **"object"**.

<a id="js-object-types-example-09"></a>

### **Example 9: WeakMap**

- [x] A **WeakMap** is a Map whose keys are **objects** held **weakly** (not enumerable).
- [x] You cannot list keys. You **can** `get` / `set` / `has` while the key object lives.

Sandbox: `code_sandbox/js-object-types/obj-weakmap.html`

```javascript
const key = { id: 1 };
const wm = new WeakMap();
wm.set(key, "secret");
```

<img alt="js-object-types example 9 source" src="./code_sandbox/snaps/js-object-types-09-code.png" />

<img alt="js-object-types example 9 result" src="./code_sandbox/snaps/js-object-types-09-result.png" />

- [x] **Outcome:** get(key) is **"secret"**. has(key) is **true**. String(wm) is **[object WeakMap]**.

<a id="js-object-types-example-10"></a>

### **Example 10: WeakSet**

- [x] A **WeakSet** is a Set of **objects** with **weak** references. Not enumerable.

Sandbox: `code_sandbox/js-object-types/obj-weakset.html`

```javascript
const item = { id: 1 };
const ws = new WeakSet();
ws.add(item);
```

<img alt="js-object-types example 10 source" src="./code_sandbox/snaps/js-object-types-10-code.png" />

<img alt="js-object-types example 10 result" src="./code_sandbox/snaps/js-object-types-10-result.png" />

- [x] **Outcome:** has(item) is **true**. String(ws) is **[object WeakSet]**.

<a id="js-object-types-example-11"></a>

### **Example 11: Math**

- [x] **Math** is a built-in object of constants and functions (`PI`, `abs`, …).
- [x] It is **not** a constructor — do not call `new Math()`.

Sandbox: `code_sandbox/js-object-types/obj-math.html`

```javascript
let pi = Math.PI;
let abs = Math.abs(-3);
```

<img alt="js-object-types example 11 source" src="./code_sandbox/snaps/js-object-types-11-code.png" />

<img alt="js-object-types example 11 result" src="./code_sandbox/snaps/js-object-types-11-result.png" />

- [x] **Outcome:** Math.PI is **3.141592653589793**. abs(-3) is **3**. typeof Math is **"object"**.

<a id="js-object-types-example-12"></a>

### **Example 12: Date**

- [x] A **Date** object stores an instant in time.
- [x] Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**. In this Mountain zone, local `toString` / `toLocaleString` can fall on the **previous** calendar evening.

Sandbox: `code_sandbox/js-object-types/obj-date.html`

```javascript
const date = new Date("2022-03-25");
```

<img alt="js-object-types example 12 source" src="./code_sandbox/snaps/js-object-types-12-code.png" />

<img alt="js-object-types example 12 result" src="./code_sandbox/snaps/js-object-types-12-result.png" />

- [x] **Outcome:** ISO is **2022-03-25T00:00:00.000Z**. Local print is **Thu Mar 24 2022 18:00:00 GMT-0600**. typeof is **"object"**.

<a id="js-object-types-example-13"></a>

### **Example 13: RegExp**

- [x] A **RegExp** tests and matches text patterns.

Sandbox: `code_sandbox/js-object-types/obj-regexp.html`

```javascript
const pat = /w3/i;
let ok = pat.test("W3Schools");
```

<img alt="js-object-types example 13 source" src="./code_sandbox/snaps/js-object-types-13-code.png" />

<img alt="js-object-types example 13 result" src="./code_sandbox/snaps/js-object-types-13-result.png" />

- [x] **Outcome:** String(pat) is **/w3/i**. test("W3Schools") is **true**. typeof is **"object"**.

<a id="js-object-types-example-14"></a>

### **Example 14: Error**

- [x] An **Error** object represents a failure (`name` + `message`).

Sandbox: `code_sandbox/js-object-types/obj-error.html`

```javascript
const err = new Error("Oops");
```

<img alt="js-object-types example 14 source" src="./code_sandbox/snaps/js-object-types-14-code.png" />

<img alt="js-object-types example 14 result" src="./code_sandbox/snaps/js-object-types-14-result.png" />

- [x] **Outcome:** name is **"Error"**. message is **"Oops"**. String(err) is **"Error: Oops"**.

<a id="js-object-types-example-15"></a>

### **Example 15: JSON**

- [x] **JSON** is an object with **`stringify`** and **`parse`** — not a constructor.

Sandbox: `code_sandbox/js-object-types/obj-json.html`

```javascript
const obj = { name: "John" };
let text = JSON.stringify(obj);
let back = JSON.parse(text);
```

<img alt="js-object-types example 15 source" src="./code_sandbox/snaps/js-object-types-15-code.png" />

<img alt="js-object-types example 15 result" src="./code_sandbox/snaps/js-object-types-15-result.png" />

- [x] **Outcome:** stringify is **{"name":"John"}**. back.name is **"John"**. typeof JSON is **"object"**.

<a id="js-object-types-example-16"></a>

### **Example 16: Promise**

- [x] A **Promise** represents completion or failure of an async operation.
- [x] `typeof` a Promise is **"object"**. Check with **`instanceof Promise`**.

Sandbox: `code_sandbox/js-object-types/obj-promise.html`

```javascript
const p = Promise.resolve("ok");
```

<img alt="js-object-types example 16 source" src="./code_sandbox/snaps/js-object-types-16-code.png" />

<img alt="js-object-types example 16 result" src="./code_sandbox/snaps/js-object-types-16-result.png" />

- [x] **Outcome:** typeof is **"object"**. instanceof Promise is **true**. String(p) is **[object Promise]**.

<a id="js-object-types-example-17"></a>

### **Example 17: Int8Array**

- [x] **Int8Array** stores fixed-size **8-bit signed** integers (−128…127).

Sandbox: `code_sandbox/js-object-types/obj-int8array.html`

```javascript
const a = new Int8Array([1, 2, 3]);
```

<img alt="js-object-types example 17 source" src="./code_sandbox/snaps/js-object-types-17-code.png" />

<img alt="js-object-types example 17 result" src="./code_sandbox/snaps/js-object-types-17-result.png" />

- [x] **Outcome:** Print is **1,2,3**. length **3**. BYTES_PER_ELEMENT **1**.

<a id="js-object-types-example-18"></a>

### **Example 18: Int16Array**

- [x] **Int16Array** stores fixed-size **16-bit signed** integers.

Sandbox: `code_sandbox/js-object-types/obj-int16array.html`

```javascript
const a = new Int16Array([1, 2, 3]);
```

<img alt="js-object-types example 18 source" src="./code_sandbox/snaps/js-object-types-18-code.png" />

<img alt="js-object-types example 18 result" src="./code_sandbox/snaps/js-object-types-18-result.png" />

- [x] **Outcome:** Print is **1,2,3**. BYTES_PER_ELEMENT **2**.

<a id="js-object-types-example-19"></a>

### **Example 19: Int32Array**

- [x] **Int32Array** stores fixed-size **32-bit signed** integers.

Sandbox: `code_sandbox/js-object-types/obj-int32array.html`

```javascript
const a = new Int32Array([1, 2, 3]);
```

<img alt="js-object-types example 19 source" src="./code_sandbox/snaps/js-object-types-19-code.png" />

<img alt="js-object-types example 19 result" src="./code_sandbox/snaps/js-object-types-19-result.png" />

- [x] **Outcome:** Print is **1,2,3**. BYTES_PER_ELEMENT **4**.

<a id="js-object-types-example-20"></a>

### **Example 20: Float16Array**

- [x] **Float16Array** stores fixed-size **16-bit** floating-point values (newer engines).
- [x] This Chrome screenshot engine **does** define it.

Sandbox: `code_sandbox/js-object-types/obj-float16array.html`

```javascript
const a = new Float16Array([1.5, 2]);
```

<img alt="js-object-types example 20 source" src="./code_sandbox/snaps/js-object-types-20-code.png" />

<img alt="js-object-types example 20 result" src="./code_sandbox/snaps/js-object-types-20-result.png" />

- [x] **Outcome:** Print is **1.5,2**. constructor.name is **Float16Array**. typeof Float16Array is **"function"**.

<a id="js-object-types-example-21"></a>

### **Example 21: Float32Array**

- [x] **Float32Array** stores fixed-size **32-bit** floating-point values.

Sandbox: `code_sandbox/js-object-types/obj-float32array.html`

```javascript
const a = new Float32Array([1.5, 2]);
```

<img alt="js-object-types example 21 source" src="./code_sandbox/snaps/js-object-types-21-code.png" />

<img alt="js-object-types example 21 result" src="./code_sandbox/snaps/js-object-types-21-result.png" />

- [x] **Outcome:** Print is **1.5,2**. BYTES_PER_ELEMENT **4**.

<a id="js-object-types-example-22"></a>

### **Example 22: Float64Array**

- [x] **Float64Array** stores fixed-size **64-bit** floating-point values (same width as Number).

Sandbox: `code_sandbox/js-object-types/obj-float64array.html`

```javascript
const a = new Float64Array([1.5, 2]);
```

<img alt="js-object-types example 22 source" src="./code_sandbox/snaps/js-object-types-22-code.png" />

<img alt="js-object-types example 22 result" src="./code_sandbox/snaps/js-object-types-22-result.png" />

- [x] **Outcome:** Print is **1.5,2**. BYTES_PER_ELEMENT **8**.

<a id="js-object-types-example-23"></a>

### **Example 23: BigInt64Array**

- [x] **BigInt64Array** stores fixed-size **64-bit BigInt** values. Elements are **`n`** integers.

Sandbox: `code_sandbox/js-object-types/obj-bigint64array.html`

```javascript
const a = new BigInt64Array([10n, 20n]);
```

<img alt="js-object-types example 23 source" src="./code_sandbox/snaps/js-object-types-23-code.png" />

<img alt="js-object-types example 23 result" src="./code_sandbox/snaps/js-object-types-23-result.png" />

- [x] **Outcome:** Print is **10,20**. a[0] is **10n**. typeof a[0] is **"bigint"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-object-types/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are the four person properties in the Tryit?

<details>
<summary>Answer</summary>

- [x] **firstName, lastName, age, eyeColor**. firstName is **"John"**, age **50**.

</details>

### Question 2: What is `cars[0]`?

<details>
<summary>Answer</summary>

- [x] **"Saab"**. Indexes are 0-based.

</details>

### Question 3: What is `typeof` of a Map?

<details>
<summary>Answer</summary>

- [x] **"object"**. Use **instanceof Map**.

</details>

### Question 4: Does a Set keep duplicate `"A"`?

<details>
<summary>Answer</summary>

- [x] **No.** size is **2** for `["A","B","A"]`.

</details>

### Question 5: Can you iterate a WeakMap?

<details>
<summary>Answer</summary>

- [x] **No.** You can `get`/`set`/`has` while the key object lives. String is **[object WeakMap]**.

</details>

### Question 6: What is Math.PI?

<details>
<summary>Answer</summary>

- [x] **3.141592653589793**. typeof Math is **"object"**.

</details>

### Question 7: What happens with `new Math()`?

<details>
<summary>Answer</summary>

- [x] **TypeError: Math is not a constructor**.

</details>

### Question 8: What is `JSON.stringify({name:"John"})`?

<details>
<summary>Answer</summary>

- [x] **{"name":"John"}**. JSON is not a constructor.

</details>

### Question 9: What is `typeof` of a Promise?

<details>
<summary>Answer</summary>

- [x] **"object"**. instanceof Promise is **true**.

</details>

### Question 10: What did `new Date("2022-03-25")` print locally?

<details>
<summary>Answer</summary>

- [x] **Thu Mar 24 2022 18:00:00 GMT-0600**.

</details>

### Question 11: What is Int8Array BYTES_PER_ELEMENT?

<details>
<summary>Answer</summary>

- [x] **1**. Int16 → **2**, Int32 → **4**, Float32 → **4**, Float64 → **8**.

</details>

### Question 12: Does this Chrome have Float16Array?

<details>
<summary>Answer</summary>

- [x] **Yes.** `new Float16Array([1.5, 2])` prints **1.5,2**.

</details>


</details>

## Summary

Treat arrays, dates, maps, and typed arrays as objects with specialized APIs. Do not construct Math or JSON. Date-only ISO is UTC.

## References

- [JS Built-In Objects (W3Schools)](https://www.w3schools.com/js/js_datatypes_objects.asp)
- [MDN: Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
- [MDN: Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)

</details>
