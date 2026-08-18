<details>
  <summary>JS Map WeakMap</summary>

## Introduction

A WeakMap is key/value storage whose keys are objects (or unregistered symbols) held weakly. get/set/has/delete are the API. String keys throw Invalid value used as weak map key. Symbol.for (registered) throws; Symbol('x') works. WeakMaps are not iterable and have no size or clear. The visitor demo stores counts. The class demo stores {secret}; user1 is the key, so myMap.get(user1) works if myMap is in scope — the real privacy is that you cannot enumerate keys.

This section has **10** examples:

- [x] **Example 1:** new WeakMap() [View](#js-map-weakmap-example-01)
- [x] **Example 2:** set() then get() [View](#js-map-weakmap-example-02)
- [x] **Example 3:** has(key) [View](#js-map-weakmap-example-03)
- [x] **Example 4:** delete(key) [View](#js-map-weakmap-example-04)
- [x] **Example 5:** Keys: objects / unregistered symbols; primitives throw [View](#js-map-weakmap-example-05)
- [x] **Example 6:** WeakMap is not iterable [View](#js-map-weakmap-example-06)
- [x] **Example 7:** No size and no clear() [View](#js-map-weakmap-example-07)
- [x] **Example 8:** Track visit counts with WeakMap [View](#js-map-weakmap-example-08)
- [x] **Example 9:** WeakMap secret data on a class [View](#js-map-weakmap-example-09)
- [x] **Example 10:** Dropping the only key reference (GC) [View](#js-map-weakmap-example-10)

## Detailed Explanation

- [x] Keys: **objects** or **unregistered symbols**. Primitives and `Symbol.for` throw **Invalid value used as weak map key**.
- [x] `get` / `set` / `has` / `delete` only. **Not iterable.** `size` is **undefined**.
- [x] Visitor counts: Paul **3**, Ringo **1**, John **1**, George **undefined**.
- [x] `getSecret()` is **hidden data**. `myMap.get(user1)` is the same pair. `[...myMap]` throws. `Array.from(myMap)` is **[]**.
- [x] Nulling the only key binding drops your lookup. `get(null)` throws.

<a id="js-map-weakmap-example-01"></a>

### **Example 1: new WeakMap()**

- [x] `new WeakMap()` creates an empty WeakMap.
- [x] Keys **must be objects** (or unregistered symbols). Keys are held **weakly**.

Sandbox: `code_sandbox/js-map-weakmap/new-weakmap.html`

```javascript
const myMap = new WeakMap();
```

<img alt="js-map-weakmap example 1 source" src="./code_sandbox/snaps/js-map-weakmap-01-code.png" />

<img alt="js-map-weakmap example 1 result" src="./code_sandbox/snaps/js-map-weakmap-01-result.png" />

- [x] **Outcome:** `typeof` is **object**. `instanceof WeakMap` is **true**.

<a id="js-map-weakmap-example-02"></a>

### **Example 2: set() then get()**

- [x] `set(obj, value)` stores a pair. `get(obj)` reads it back.

Sandbox: `code_sandbox/js-map-weakmap/set-get.html`

```javascript
const myMap = new WeakMap();
let myObj = {fname:"John", lname:"Doe"};
myMap.set(myObj, "player");
const type = myMap.get(myObj);
```

<img alt="js-map-weakmap example 2 source" src="./code_sandbox/snaps/js-map-weakmap-02-code.png" />

<img alt="js-map-weakmap example 2 result" src="./code_sandbox/snaps/js-map-weakmap-02-result.png" />

- [x] **Outcome:** `get(myObj)` is **"player"**.

<a id="js-map-weakmap-example-03"></a>

### **Example 3: has(key)**

- [x] `has(obj)` is **true** while that object is a key.

Sandbox: `code_sandbox/js-map-weakmap/has.html`

```javascript
const myMap = new WeakMap();
let myObj = {fname:"John", lname:"Doe"};
myMap.set(myObj, "player");
```

<img alt="js-map-weakmap example 3 source" src="./code_sandbox/snaps/js-map-weakmap-03-code.png" />

<img alt="js-map-weakmap example 3 result" src="./code_sandbox/snaps/js-map-weakmap-03-result.png" />

- [x] **Outcome:** `has(myObj)` is **true**. `has` of a **new** look-alike object is **false**.

<a id="js-map-weakmap-example-04"></a>

### **Example 4: delete(key)**

- [x] `delete(obj)` removes that pair.

Sandbox: `code_sandbox/js-map-weakmap/delete.html`

```javascript
const myMap = new WeakMap();
let myObj = {fname:"John", lname:"Doe"};
myMap.set(myObj, "player");
const ok = myMap.delete(myObj);
```

<img alt="js-map-weakmap example 4 source" src="./code_sandbox/snaps/js-map-weakmap-04-code.png" />

<img alt="js-map-weakmap example 4 result" src="./code_sandbox/snaps/js-map-weakmap-04-result.png" />

- [x] **Outcome:** `delete` returns **true**. Then `has` is **false** and `get` is **undefined**.

<a id="js-map-weakmap-example-05"></a>

### **Example 5: Keys: objects / unregistered symbols; primitives throw**

- [x] The page: keys must be **objects or non-registered symbols**.
- [x] Strings throw. `Symbol.for` (registered) throws. `Symbol('x')` **works**.

Sandbox: `code_sandbox/js-map-weakmap/primitive-and-symbols.html`

```javascript
const myMap = new WeakMap();
const obj = {x: 1};
const unique = Symbol('x');
myMap.set(obj, 'obj');
myMap.set(unique, 'sym');
myMap.set("nope", 1);
```

<img alt="js-map-weakmap example 5 source" src="./code_sandbox/snaps/js-map-weakmap-05-code.png" />

<img alt="js-map-weakmap example 5 result" src="./code_sandbox/snaps/js-map-weakmap-05-result.png" />

- [x] **Outcome:** `get(obj)` is **"obj"**. `get(unique)` is **"sym"**. `set("nope", 1)` and `set(Symbol.for("x"), 1)` throw **TypeError: Invalid value used as weak map key**.

<a id="js-map-weakmap-example-06"></a>

### **Example 6: WeakMap is not iterable**

- [x] No `for...of`, `forEach`, or `keys()` on a WeakMap.

Sandbox: `code_sandbox/js-map-weakmap/not-iterable.html`

```javascript
const myMap = new WeakMap();
const obj = {x: 1};
myMap.set(obj, "v");
for (const x of myMap) {}
```

<img alt="js-map-weakmap example 6 source" src="./code_sandbox/snaps/js-map-weakmap-06-code.png" />

<img alt="js-map-weakmap example 6 result" src="./code_sandbox/snaps/js-map-weakmap-06-result.png" />

- [x] **Outcome:** `[...myMap]` / `for...of` throw **TypeError: myMap is not iterable**. `forEach` and `keys()` throw **TypeError: myMap.forEach is not a function** (same pattern for `keys`).

<a id="js-map-weakmap-example-07"></a>

### **Example 7: No size and no clear()**

- [x] You cannot read `size` or `clear()` a WeakMap.

Sandbox: `code_sandbox/js-map-weakmap/no-size-clear.html`

```javascript
const myMap = new WeakMap();
myMap.size;
myMap.clear();
```

<img alt="js-map-weakmap example 7 source" src="./code_sandbox/snaps/js-map-weakmap-07-code.png" />

<img alt="js-map-weakmap example 7 result" src="./code_sandbox/snaps/js-map-weakmap-07-result.png" />

- [x] **Outcome:** `myMap.size` is **undefined**. `clear()` throws **TypeError: myMap.clear is not a function**.

<a id="js-map-weakmap-example-08"></a>

### **Example 8: Track visit counts with WeakMap**

- [x] Store **counts** on object keys without pinning those objects forever.

Sandbox: `code_sandbox/js-map-weakmap/track-visitors.html`

```javascript
let text = "";
const visitsCount = new WeakMap();
const John = {name:"John", age:40};
const Paul = {name:"Paul", age:41};
const Ringo = {name:"Ringo", age:42};
const George = {name:"George", age:43};
function track(visitor) {
  let count = visitsCount.get(visitor) || 0;
  count++;
  visitsCount.set(visitor, count);
  text += visitor.name + ", age " + visitor.age + ", has visited " + count + " time(s). ";
}
track(Paul);
track(Ringo);
track(Paul);
track(Paul);
track(John);
```

<img alt="js-map-weakmap example 8 source" src="./code_sandbox/snaps/js-map-weakmap-08-code.png" />

<img alt="js-map-weakmap example 8 result" src="./code_sandbox/snaps/js-map-weakmap-08-result.png" />

- [x] **Outcome:** text is **"Paul, age 41, has visited 1 time(s). Ringo, age 42, has visited 1 time(s). Paul, age 41, has visited 2 time(s). Paul, age 41, has visited 3 time(s). John, age 40, has visited 1 time(s). "**. `get(Paul)` is **3**. `get(George)` is **undefined**.

<a id="js-map-weakmap-example-09"></a>

### **Example 9: WeakMap secret data on a class**

- [x] The page simulates private fields: `myMap.set(this, {secret})`.
- [x] `user1` **is** the constructor’s `this`, so `myMap.get(user1)` also works when `myMap` is in scope.
- [x] Privacy is **no enumeration**: you cannot list keys you do not already hold.

Sandbox: `code_sandbox/js-map-weakmap/secret-data.html`

```javascript
const myMap = new WeakMap();
class User {
  constructor(name) {
    myMap.set(this, {secret:"hidden data"});
    this.name = name;
  }
  getSecret() {
    return myMap.get(this).secret;
  }
}
const user1 = new User("John");
const secret = user1.getSecret();
```

<img alt="js-map-weakmap example 9 source" src="./code_sandbox/snaps/js-map-weakmap-09-code.png" />

<img alt="js-map-weakmap example 9 result" src="./code_sandbox/snaps/js-map-weakmap-09-result.png" />

- [x] **Outcome:** `getSecret()` is **"hidden data"**. `myMap.get(user1).secret` is also **"hidden data"** (same object key). `[...myMap]` throws **TypeError: myMap is not iterable**. `Array.from(myMap)` is **[]** (non-iterable objects become an empty array — not a leak).

<a id="js-map-weakmap-example-10"></a>

### **Example 10: Dropping the only key reference (GC)**

- [x] After `myObj = null`, you no longer have the key. The pair **may** be collected.
- [x] `get(null)` / `has(null)` are invalid keys.

Sandbox: `code_sandbox/js-map-weakmap/gc-null.html`

```javascript
const myMap = new WeakMap();
let myObj = {fname:"John", lname:"Doe"};
myMap.set(myObj, "secret");
const held = myMap.get(myObj);
myObj = null;
```

<img alt="js-map-weakmap example 10 source" src="./code_sandbox/snaps/js-map-weakmap-10-code.png" />

<img alt="js-map-weakmap example 10 result" src="./code_sandbox/snaps/js-map-weakmap-10-result.png" />

- [x] **Outcome:** Before nulling, `get` was **"secret"**. After, `myObj` is **null**. `get(null)` throws **TypeError: Invalid value used as weak map key**. You cannot iterate to see leftover pairs. GC is not immediate.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-map-weakmap/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does set(myObj, "player") then get return?

<details>
<summary>Answer</summary>

- [x] **"player"**.

</details>

### Question 2: has(look-alike object)?

<details>
<summary>Answer</summary>

- [x] **false** — different reference.

</details>

### Question 3: delete then get?

<details>
<summary>Answer</summary>

- [x] delete **true**, has **false**, get **undefined**.

</details>

### Question 4: Can you set a string key?

<details>
<summary>Answer</summary>

- [x] **No.** **TypeError: Invalid value used as weak map key**.

</details>

### Question 5: Does Symbol('x') work as a key?

<details>
<summary>Answer</summary>

- [x] **Yes** (unregistered). `Symbol.for('x')` throws.

</details>

### Question 6: Can you iterate a WeakMap?

<details>
<summary>Answer</summary>

- [x] **No.** **myMap is not iterable**.

</details>

### Question 7: What is myMap.size?

<details>
<summary>Answer</summary>

- [x] **undefined**.

</details>

### Question 8: How many times did Paul visit?

<details>
<summary>Answer</summary>

- [x] **3**. George was never tracked → **undefined**.

</details>

### Question 9: Is the secret unreachable via myMap.get(user1)?

<details>
<summary>Answer</summary>

- [x] **No** — `user1` is the key, so get works if `myMap` is in scope. You still cannot **list** keys.

</details>

### Question 10: What is Array.from(myMap)?

<details>
<summary>Answer</summary>

- [x] **[]** — not iterable, treated as a non-array-like object.

</details>


</details>

## Summary

Use WeakMap for per-object metadata you do not want to keep alive. Keys are objects or unique symbols. Do not iterate. Privacy is lack of enumeration, not a magic wall around a key you already hold.

## References

- [JS WeakMap (W3Schools)](https://www.w3schools.com/js/js_maps_weak.asp)
- [MDN: WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

</details>
