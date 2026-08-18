<details>
  <summary>JS Data Types</summary>

## Introduction

A JavaScript variable can hold eight kinds of data: seven primitives (Number, BigInt, String, Boolean, Undefined, Null, Symbol) and Object. The Object kind includes many built-in types (Array, Map, Date, typed arrays, and more). Types are dynamic: the same binding can hold undefined, then a number, then a string. The + operator concatenates as soon as a string appears; 16 + 4 + "Volvo" is 20Volvo because addition runs left to right until the string. typeof reports the runtime type. typeof null is the legacy string "object". BigInt literals with n are exact; BigInt(aNumber) is not, because the Number is rounded first.

This section has **34** examples:

- [x] **Example 1:** Number [View](#js-data-types-example-01)
- [x] **Example 2:** BigInt — n suffix (exact) [View](#js-data-types-example-02)
- [x] **Example 3:** BigInt(number) loses precision [View](#js-data-types-example-03)
- [x] **Example 4:** String [View](#js-data-types-example-04)
- [x] **Example 5:** Boolean [View](#js-data-types-example-05)
- [x] **Example 6:** Undefined [View](#js-data-types-example-06)
- [x] **Example 7:** Null [View](#js-data-types-example-07)
- [x] **Example 8:** Symbol [View](#js-data-types-example-08)
- [x] **Example 9:** Object [View](#js-data-types-example-09)
- [x] **Example 10:** 16 + "Volvo" — number then string [View](#js-data-types-example-10)
- [x] **Example 11:** "Volvo" + 16 — string then number [View](#js-data-types-example-11)
- [x] **Example 12:** 16 + 4 + "Volvo" — left to right [View](#js-data-types-example-12)
- [x] **Example 13:** "Volvo" + 16 + 4 — string first [View](#js-data-types-example-13)
- [x] **Example 14:** Dynamic types — same variable, new type [View](#js-data-types-example-14)
- [x] **Example 15:** typeof strings — "", "John", "John Doe" [View](#js-data-types-example-15)
- [x] **Example 16:** typeof numbers — 0, 314, 3.14, (3), (3+4) [View](#js-data-types-example-16)
- [x] **Example 17:** Array [View](#js-data-types-example-17)
- [x] **Example 18:** Map [View](#js-data-types-example-18)
- [x] **Example 19:** Set [View](#js-data-types-example-19)
- [x] **Example 20:** WeakMap [View](#js-data-types-example-20)
- [x] **Example 21:** WeakSet [View](#js-data-types-example-21)
- [x] **Example 22:** Math [View](#js-data-types-example-22)
- [x] **Example 23:** Date [View](#js-data-types-example-23)
- [x] **Example 24:** RegExp [View](#js-data-types-example-24)
- [x] **Example 25:** Error [View](#js-data-types-example-25)
- [x] **Example 26:** JSON [View](#js-data-types-example-26)
- [x] **Example 27:** Promise [View](#js-data-types-example-27)
- [x] **Example 28:** Int8Array [View](#js-data-types-example-28)
- [x] **Example 29:** Int16Array [View](#js-data-types-example-29)
- [x] **Example 30:** Int32Array [View](#js-data-types-example-30)
- [x] **Example 31:** Float16Array [View](#js-data-types-example-31)
- [x] **Example 32:** Float32Array [View](#js-data-types-example-32)
- [x] **Example 33:** Float64Array [View](#js-data-types-example-33)
- [x] **Example 34:** BigInt64Array [View](#js-data-types-example-34)

## Detailed Explanation

- [x] **8 types:** Number, BigInt, String, Boolean, Undefined, Null, Symbol, Object.
- [x] **+ with a string concatenates.** `16 + 4 + "Volvo"` is **20Volvo**. `"Volvo" + 16 + 4` is **Volvo164**.
- [x] Types are **dynamic** — one variable can change from undefined → number → string.
- [x] `typeof null` is **"object"** (legacy). Null is still a primitive.
- [x] **`1234567890123456789012345n`** is exact. **`BigInt(1234567890123456789012345)`** is **1234567890123456824475648n**.
- [x] Every built-in object-table row is its own Example, including **Float16Array** (this Chrome has it) and **WeakMap** / **WeakSet**.

<a id="js-data-types-example-01"></a>

### **Example 1: Number**

- [x] **Number** is a numeric value. JavaScript numbers are **64-bit floats** (IEEE-754).
- [x] Integers and decimals use the **same** type.

Sandbox: `code_sandbox/js-data-types/type-number.html`

```javascript
let length = 16;
let weight = 7.5;
```

<img alt="js-data-types example 1 source" src="./code_sandbox/snaps/js-data-types-01-code.png" />

<img alt="js-data-types example 1 result" src="./code_sandbox/snaps/js-data-types-01-result.png" />

- [x] **Outcome:** length is **16**, weight is **7.5**. typeof length is **"number"**.

<a id="js-data-types-example-02"></a>

### **Example 2: BigInt — n suffix (exact)**

- [x] **BigInt** holds integers bigger than `Number.MAX_SAFE_INTEGER`.
- [x] A trailing **`n`** makes a BigInt **literal** — exact.

Sandbox: `code_sandbox/js-data-types/type-bigint-n.html`

```javascript
let x = 1234567890123456789012345n;
```

<img alt="js-data-types example 2 source" src="./code_sandbox/snaps/js-data-types-02-code.png" />

<img alt="js-data-types example 2 result" src="./code_sandbox/snaps/js-data-types-02-result.png" />

- [x] **Outcome:** x is **1234567890123456789012345n**. typeof is **"bigint"**.

<a id="js-data-types-example-03"></a>

### **Example 3: BigInt(number) loses precision**

- [x] `BigInt(1234567890123456789012345)` first creates a **Number**, then converts.
- [x] That Number is **not** exact past 2^53 − 1, so the BigInt is **wrong**.

Sandbox: `code_sandbox/js-data-types/type-bigint-number-arg.html`

```javascript
let y = BigInt(1234567890123456789012345);
let x = 1234567890123456789012345n;
```

<img alt="js-data-types example 3 source" src="./code_sandbox/snaps/js-data-types-03-code.png" />

<img alt="js-data-types example 3 result" src="./code_sandbox/snaps/js-data-types-03-result.png" />

- [x] **Outcome:** y is **1234567890123456824475648n**, not the digits in the source. `x === y` is **false**. Prefer **`n`** or **`BigInt("…")`**.

<a id="js-data-types-example-04"></a>

### **Example 4: String**

- [x] A **String** is text in **quotes** (single or double).

Sandbox: `code_sandbox/js-data-types/type-string.html`

```javascript
let color = "Yellow";
let lastName = "Johnson";
```

<img alt="js-data-types example 4 source" src="./code_sandbox/snaps/js-data-types-04-code.png" />

<img alt="js-data-types example 4 result" src="./code_sandbox/snaps/js-data-types-04-result.png" />

- [x] **Outcome:** color is **"Yellow"**, lastName is **"Johnson"**. typeof is **"string"**.

<a id="js-data-types-example-05"></a>

### **Example 5: Boolean**

- [x] A **Boolean** is only **`true`** or **`false`**.

Sandbox: `code_sandbox/js-data-types/type-boolean.html`

```javascript
let x = true;
let y = false;
```

<img alt="js-data-types example 5 source" src="./code_sandbox/snaps/js-data-types-05-code.png" />

<img alt="js-data-types example 5 result" src="./code_sandbox/snaps/js-data-types-05-result.png" />

- [x] **Outcome:** x is **true**, y is **false**. typeof is **"boolean"**.

<a id="js-data-types-example-06"></a>

### **Example 6: Undefined**

- [x] A declared variable with **no assignment** is **`undefined`**. The type is also **undefined**.

Sandbox: `code_sandbox/js-data-types/type-undefined.html`

```javascript
let x;
let y;
```

<img alt="js-data-types example 6 source" src="./code_sandbox/snaps/js-data-types-06-code.png" />

<img alt="js-data-types example 6 result" src="./code_sandbox/snaps/js-data-types-06-result.png" />

- [x] **Outcome:** x is **undefined**. typeof x is **"undefined"**.

<a id="js-data-types-example-07"></a>

### **Example 7: Null**

- [x] **`null`** is an assignment value meaning **intentional absence**.
- [x] `typeof null` is **"object"** — a **legacy bug**, not proof that null is an object.

Sandbox: `code_sandbox/js-data-types/type-null.html`

```javascript
let x = null;
let y = null;
```

<img alt="js-data-types example 7 source" src="./code_sandbox/snaps/js-data-types-07-code.png" />

<img alt="js-data-types example 7 result" src="./code_sandbox/snaps/js-data-types-07-result.png" />

- [x] **Outcome:** x is **null**. typeof x is **"object"** (legacy).

<a id="js-data-types-example-08"></a>

### **Example 8: Symbol**

- [x] A **Symbol** is a unique primitive identifier. Two `Symbol()` calls are **never** `===`.

Sandbox: `code_sandbox/js-data-types/type-symbol.html`

```javascript
const x = Symbol();
const y = Symbol();
```

<img alt="js-data-types example 8 source" src="./code_sandbox/snaps/js-data-types-08-code.png" />

<img alt="js-data-types example 8 result" src="./code_sandbox/snaps/js-data-types-08-result.png" />

- [x] **Outcome:** typeof x is **"symbol"**. `x === y` is **false**.

<a id="js-data-types-example-09"></a>

### **Example 9: Object**

- [x] An **Object** is a collection of **name:value** properties in `{ }`.

Sandbox: `code_sandbox/js-data-types/type-object.html`

```javascript
const person = {firstName:"John", lastName:"Doe"};
```

<img alt="js-data-types example 9 source" src="./code_sandbox/snaps/js-data-types-09-code.png" />

<img alt="js-data-types example 9 result" src="./code_sandbox/snaps/js-data-types-09-result.png" />

- [x] **Outcome:** firstName is **"John"**. typeof is **"object"**. String(person) is **[object Object]**.

<a id="js-data-types-example-10"></a>

### **Example 10: 16 + "Volvo" — number then string**

- [x] When you **add** a number and a string, JS treats the number as a **string**.

Sandbox: `code_sandbox/js-data-types/add-number-string.html`

```javascript
let x = 16 + "Volvo";
```

<img alt="js-data-types example 10 source" src="./code_sandbox/snaps/js-data-types-10-code.png" />

<img alt="js-data-types example 10 result" src="./code_sandbox/snaps/js-data-types-10-result.png" />

- [x] **Outcome:** x is **"16Volvo"**. typeof is **"string"**.

<a id="js-data-types-example-11"></a>

### **Example 11: "Volvo" + 16 — string then number**

- [x] Same rule from the other side: **`+`** with a string **concatenates**.

Sandbox: `code_sandbox/js-data-types/add-string-number.html`

```javascript
let x = "Volvo" + 16;
```

<img alt="js-data-types example 11 source" src="./code_sandbox/snaps/js-data-types-11-code.png" />

<img alt="js-data-types example 11 result" src="./code_sandbox/snaps/js-data-types-11-result.png" />

- [x] **Outcome:** x is **"Volvo16"**.

<a id="js-data-types-example-12"></a>

### **Example 12: 16 + 4 + "Volvo" — left to right**

- [x] JS evaluates **left to right**. `16 + 4` is numeric **20**, then `20 + "Volvo"` concatenates.

Sandbox: `code_sandbox/js-data-types/add-left-numbers-then-string.html`

```javascript
let x = 16 + 4 + "Volvo";
```

<img alt="js-data-types example 12 source" src="./code_sandbox/snaps/js-data-types-12-code.png" />

<img alt="js-data-types example 12 result" src="./code_sandbox/snaps/js-data-types-12-result.png" />

- [x] **Outcome:** x is **"20Volvo"**.

<a id="js-data-types-example-13"></a>

### **Example 13: "Volvo" + 16 + 4 — string first**

- [x] If the **first** operand is a string, later `+` operands become strings too.

Sandbox: `code_sandbox/js-data-types/add-string-then-numbers.html`

```javascript
let x = "Volvo" + 16 + 4;
```

<img alt="js-data-types example 13 source" src="./code_sandbox/snaps/js-data-types-13-code.png" />

<img alt="js-data-types example 13 result" src="./code_sandbox/snaps/js-data-types-13-result.png" />

- [x] **Outcome:** x is **"Volvo164"** (not Volvo20).

<a id="js-data-types-example-14"></a>

### **Example 14: Dynamic types — same variable, new type**

- [x] JavaScript types are **dynamic**: one variable may hold **undefined**, then a **number**, then a **string**.

Sandbox: `code_sandbox/js-data-types/dynamic-types.html`

```javascript
let x;          // undefined
x = 5;          // Number
x = "John";     // String
```

<img alt="js-data-types example 14 source" src="./code_sandbox/snaps/js-data-types-14-code.png" />

<img alt="js-data-types example 14 result" src="./code_sandbox/snaps/js-data-types-14-result.png" />

- [x] **Outcome:** After the last assignment, x is **"John"** and typeof is **"string"**.

<a id="js-data-types-example-15"></a>

### **Example 15: typeof strings — "", "John", "John Doe"**

- [x] `typeof` returns **"string"** for every string, including **empty**.

Sandbox: `code_sandbox/js-data-types/typeof-strings.html`

```javascript
typeof "";
typeof "John";
typeof "John Doe";
```

<img alt="js-data-types example 15 source" src="./code_sandbox/snaps/js-data-types-15-code.png" />

<img alt="js-data-types example 15 result" src="./code_sandbox/snaps/js-data-types-15-result.png" />

- [x] **Outcome:** All three are **"string"**.

<a id="js-data-types-example-16"></a>

### **Example 16: typeof numbers — 0, 314, 3.14, (3), (3+4)**

- [x] `typeof` a number (integer, decimal, or parenthesized expression) is **"number"**.

Sandbox: `code_sandbox/js-data-types/typeof-numbers.html`

```javascript
typeof 0;
typeof 314;
typeof 3.14;
typeof (3);
typeof (3 + 4);
```

<img alt="js-data-types example 16 source" src="./code_sandbox/snaps/js-data-types-16-code.png" />

<img alt="js-data-types example 16 result" src="./code_sandbox/snaps/js-data-types-16-result.png" />

- [x] **Outcome:** All five are **"number"**. `(3 + 4)` is **7**, still a number.

<a id="js-data-types-example-17"></a>

### **Example 17: Array**

- [x] An **Array** is a list of values at a **numeric index** (0-based).
- [x] `typeof` an array is **"object"**. Use **`Array.isArray`** to recognize it.

Sandbox: `code_sandbox/js-data-types/obj-array.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
```

<img alt="js-data-types example 17 source" src="./code_sandbox/snaps/js-data-types-17-code.png" />

<img alt="js-data-types example 17 result" src="./code_sandbox/snaps/js-data-types-17-result.png" />

- [x] **Outcome:** Print is **Saab,Volvo,BMW**. cars[0] is **"Saab"**. typeof is **"object"**. `Array.isArray` is **true**.

<a id="js-data-types-example-18"></a>

### **Example 18: Map**

- [x] A **Map** holds **key-value** pairs. Keys may be **any** type (not just strings).

Sandbox: `code_sandbox/js-data-types/obj-map.html`

```javascript
const m = new Map([["apples", 500], ["bananas", 300]]);
let n = m.get("apples");
```

<img alt="js-data-types example 18 source" src="./code_sandbox/snaps/js-data-types-18-code.png" />

<img alt="js-data-types example 18 result" src="./code_sandbox/snaps/js-data-types-18-result.png" />

- [x] **Outcome:** get("apples") is **500**. size is **2**. typeof is **"object"**.

<a id="js-data-types-example-19"></a>

### **Example 19: Set**

- [x] A **Set** stores **unique** values. Duplicates are kept once.

Sandbox: `code_sandbox/js-data-types/obj-set.html`

```javascript
const s = new Set(["A", "B", "A"]);
let n = s.size;
```

<img alt="js-data-types example 19 source" src="./code_sandbox/snaps/js-data-types-19-code.png" />

<img alt="js-data-types example 19 result" src="./code_sandbox/snaps/js-data-types-19-result.png" />

- [x] **Outcome:** size is **2** (the second **"A"** was ignored). `has("A")` is **true**. typeof is **"object"**.

<a id="js-data-types-example-20"></a>

### **Example 20: WeakMap**

- [x] A **WeakMap** is a Map whose keys are **objects** held **weakly** (not enumerable).
- [x] You cannot list keys. You **can** `get` / `set` / `has` while the key object lives.

Sandbox: `code_sandbox/js-data-types/obj-weakmap.html`

```javascript
const key = { id: 1 };
const wm = new WeakMap();
wm.set(key, "secret");
```

<img alt="js-data-types example 20 source" src="./code_sandbox/snaps/js-data-types-20-code.png" />

<img alt="js-data-types example 20 result" src="./code_sandbox/snaps/js-data-types-20-result.png" />

- [x] **Outcome:** get(key) is **"secret"**. has(key) is **true**. String(wm) is **[object WeakMap]**.

<a id="js-data-types-example-21"></a>

### **Example 21: WeakSet**

- [x] A **WeakSet** is a Set of **objects** with **weak** references. Not enumerable.

Sandbox: `code_sandbox/js-data-types/obj-weakset.html`

```javascript
const item = { id: 1 };
const ws = new WeakSet();
ws.add(item);
```

<img alt="js-data-types example 21 source" src="./code_sandbox/snaps/js-data-types-21-code.png" />

<img alt="js-data-types example 21 result" src="./code_sandbox/snaps/js-data-types-21-result.png" />

- [x] **Outcome:** has(item) is **true**. String(ws) is **[object WeakSet]**.

<a id="js-data-types-example-22"></a>

### **Example 22: Math**

- [x] **Math** is a built-in object of constants and functions (`PI`, `abs`, …).
- [x] It is **not** a constructor — do not call `new Math()`.

Sandbox: `code_sandbox/js-data-types/obj-math.html`

```javascript
let pi = Math.PI;
let abs = Math.abs(-3);
```

<img alt="js-data-types example 22 source" src="./code_sandbox/snaps/js-data-types-22-code.png" />

<img alt="js-data-types example 22 result" src="./code_sandbox/snaps/js-data-types-22-result.png" />

- [x] **Outcome:** Math.PI is **3.141592653589793**. abs(-3) is **3**. typeof Math is **"object"**.

<a id="js-data-types-example-23"></a>

### **Example 23: Date**

- [x] A **Date** object stores an instant in time.
- [x] Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**. In this Mountain zone, local `toString` / `toLocaleString` can fall on the **previous** calendar evening.

Sandbox: `code_sandbox/js-data-types/obj-date.html`

```javascript
const date = new Date("2022-03-25");
```

<img alt="js-data-types example 23 source" src="./code_sandbox/snaps/js-data-types-23-code.png" />

<img alt="js-data-types example 23 result" src="./code_sandbox/snaps/js-data-types-23-result.png" />

- [x] **Outcome:** ISO is **2022-03-25T00:00:00.000Z**. Local print is **Thu Mar 24 2022 18:00:00 GMT-0600**. typeof is **"object"**.

<a id="js-data-types-example-24"></a>

### **Example 24: RegExp**

- [x] A **RegExp** tests and matches text patterns.

Sandbox: `code_sandbox/js-data-types/obj-regexp.html`

```javascript
const pat = /w3/i;
let ok = pat.test("W3Schools");
```

<img alt="js-data-types example 24 source" src="./code_sandbox/snaps/js-data-types-24-code.png" />

<img alt="js-data-types example 24 result" src="./code_sandbox/snaps/js-data-types-24-result.png" />

- [x] **Outcome:** String(pat) is **/w3/i**. test("W3Schools") is **true**. typeof is **"object"**.

<a id="js-data-types-example-25"></a>

### **Example 25: Error**

- [x] An **Error** object represents a failure (`name` + `message`).

Sandbox: `code_sandbox/js-data-types/obj-error.html`

```javascript
const err = new Error("Oops");
```

<img alt="js-data-types example 25 source" src="./code_sandbox/snaps/js-data-types-25-code.png" />

<img alt="js-data-types example 25 result" src="./code_sandbox/snaps/js-data-types-25-result.png" />

- [x] **Outcome:** name is **"Error"**. message is **"Oops"**. String(err) is **"Error: Oops"**.

<a id="js-data-types-example-26"></a>

### **Example 26: JSON**

- [x] **JSON** is an object with **`stringify`** and **`parse`** — not a constructor.

Sandbox: `code_sandbox/js-data-types/obj-json.html`

```javascript
const obj = { name: "John" };
let text = JSON.stringify(obj);
let back = JSON.parse(text);
```

<img alt="js-data-types example 26 source" src="./code_sandbox/snaps/js-data-types-26-code.png" />

<img alt="js-data-types example 26 result" src="./code_sandbox/snaps/js-data-types-26-result.png" />

- [x] **Outcome:** stringify is **{"name":"John"}**. back.name is **"John"**. typeof JSON is **"object"**.

<a id="js-data-types-example-27"></a>

### **Example 27: Promise**

- [x] A **Promise** represents completion or failure of an async operation.
- [x] `typeof` a Promise is **"object"**. Check with **`instanceof Promise`**.

Sandbox: `code_sandbox/js-data-types/obj-promise.html`

```javascript
const p = Promise.resolve("ok");
```

<img alt="js-data-types example 27 source" src="./code_sandbox/snaps/js-data-types-27-code.png" />

<img alt="js-data-types example 27 result" src="./code_sandbox/snaps/js-data-types-27-result.png" />

- [x] **Outcome:** typeof is **"object"**. instanceof Promise is **true**. String(p) is **[object Promise]**.

<a id="js-data-types-example-28"></a>

### **Example 28: Int8Array**

- [x] **Int8Array** stores fixed-size **8-bit signed** integers (−128…127).

Sandbox: `code_sandbox/js-data-types/obj-int8array.html`

```javascript
const a = new Int8Array([1, 2, 3]);
```

<img alt="js-data-types example 28 source" src="./code_sandbox/snaps/js-data-types-28-code.png" />

<img alt="js-data-types example 28 result" src="./code_sandbox/snaps/js-data-types-28-result.png" />

- [x] **Outcome:** Print is **1,2,3**. length **3**. BYTES_PER_ELEMENT **1**.

<a id="js-data-types-example-29"></a>

### **Example 29: Int16Array**

- [x] **Int16Array** stores fixed-size **16-bit signed** integers.

Sandbox: `code_sandbox/js-data-types/obj-int16array.html`

```javascript
const a = new Int16Array([1, 2, 3]);
```

<img alt="js-data-types example 29 source" src="./code_sandbox/snaps/js-data-types-29-code.png" />

<img alt="js-data-types example 29 result" src="./code_sandbox/snaps/js-data-types-29-result.png" />

- [x] **Outcome:** Print is **1,2,3**. BYTES_PER_ELEMENT **2**.

<a id="js-data-types-example-30"></a>

### **Example 30: Int32Array**

- [x] **Int32Array** stores fixed-size **32-bit signed** integers.

Sandbox: `code_sandbox/js-data-types/obj-int32array.html`

```javascript
const a = new Int32Array([1, 2, 3]);
```

<img alt="js-data-types example 30 source" src="./code_sandbox/snaps/js-data-types-30-code.png" />

<img alt="js-data-types example 30 result" src="./code_sandbox/snaps/js-data-types-30-result.png" />

- [x] **Outcome:** Print is **1,2,3**. BYTES_PER_ELEMENT **4**.

<a id="js-data-types-example-31"></a>

### **Example 31: Float16Array**

- [x] **Float16Array** stores fixed-size **16-bit** floating-point values (newer engines).
- [x] This Chrome screenshot engine **does** define it.

Sandbox: `code_sandbox/js-data-types/obj-float16array.html`

```javascript
const a = new Float16Array([1.5, 2]);
```

<img alt="js-data-types example 31 source" src="./code_sandbox/snaps/js-data-types-31-code.png" />

<img alt="js-data-types example 31 result" src="./code_sandbox/snaps/js-data-types-31-result.png" />

- [x] **Outcome:** Print is **1.5,2**. constructor.name is **Float16Array**. typeof Float16Array is **"function"**.

<a id="js-data-types-example-32"></a>

### **Example 32: Float32Array**

- [x] **Float32Array** stores fixed-size **32-bit** floating-point values.

Sandbox: `code_sandbox/js-data-types/obj-float32array.html`

```javascript
const a = new Float32Array([1.5, 2]);
```

<img alt="js-data-types example 32 source" src="./code_sandbox/snaps/js-data-types-32-code.png" />

<img alt="js-data-types example 32 result" src="./code_sandbox/snaps/js-data-types-32-result.png" />

- [x] **Outcome:** Print is **1.5,2**. BYTES_PER_ELEMENT **4**.

<a id="js-data-types-example-33"></a>

### **Example 33: Float64Array**

- [x] **Float64Array** stores fixed-size **64-bit** floating-point values (same width as Number).

Sandbox: `code_sandbox/js-data-types/obj-float64array.html`

```javascript
const a = new Float64Array([1.5, 2]);
```

<img alt="js-data-types example 33 source" src="./code_sandbox/snaps/js-data-types-33-code.png" />

<img alt="js-data-types example 33 result" src="./code_sandbox/snaps/js-data-types-33-result.png" />

- [x] **Outcome:** Print is **1.5,2**. BYTES_PER_ELEMENT **8**.

<a id="js-data-types-example-34"></a>

### **Example 34: BigInt64Array**

- [x] **BigInt64Array** stores fixed-size **64-bit BigInt** values. Elements are **`n`** integers.

Sandbox: `code_sandbox/js-data-types/obj-bigint64array.html`

```javascript
const a = new BigInt64Array([10n, 20n]);
```

<img alt="js-data-types example 34 source" src="./code_sandbox/snaps/js-data-types-34-code.png" />

<img alt="js-data-types example 34 result" src="./code_sandbox/snaps/js-data-types-34-result.png" />

- [x] **Outcome:** Print is **10,20**. a[0] is **10n**. typeof a[0] is **"bigint"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-data-types/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How many data types can a variable hold?

<details>
<summary>Answer</summary>

- [x] **8** — **7 primitives** plus **Object**.

</details>

### Question 2: What is `16 + "Volvo"`?

<details>
<summary>Answer</summary>

- [x] **"16Volvo"** (string).

</details>

### Question 3: Why is `16 + 4 + "Volvo"` different from `"Volvo" + 16 + 4`?

<details>
<summary>Answer</summary>

- [x] Left to right: **20Volvo** vs **Volvo164**.
- [x] A leading string makes later `+` concatenate.

</details>

### Question 4: Can one variable hold a number then a string?

<details>
<summary>Answer</summary>

- [x] **Yes.** Types are dynamic: `let x; x = 5; x = "John"` ends as a **string**.

</details>

### Question 5: What is `typeof null`?

<details>
<summary>Answer</summary>

- [x] **"object"** — a legacy bug. Use `=== null` to test for null.

</details>

### Question 6: Are `Symbol()` and `Symbol()` equal?

<details>
<summary>Answer</summary>

- [x] **No.** `===` is **false**. Every Symbol() is unique.

</details>

### Question 7: What did `BigInt(1234567890123456789012345)` produce here?

<details>
<summary>Answer</summary>

- [x] **1234567890123456824475648n**, not the source digits.
- [x] The argument is a Number first. Prefer **`n`** or **`BigInt("…")`**.

</details>

### Question 8: What is `typeof` of an array?

<details>
<summary>Answer</summary>

- [x] **"object"**. Use **Array.isArray** to recognize arrays.

</details>

### Question 9: Is `new Math()` legal?

<details>
<summary>Answer</summary>

- [x] **No.** Math is an object of functions, not a constructor (see Object Types).

</details>

### Question 10: What is `new Date("2022-03-25")` locally here?

<details>
<summary>Answer</summary>

- [x] **Thu Mar 24 2022 18:00:00 GMT-0600** — date-only ISO is UTC midnight.

</details>

### Question 11: What did Float16Array print in this Chrome?

<details>
<summary>Answer</summary>

- [x] **1.5,2**. typeof Float16Array is **"function"**.

</details>

### Question 12: What is `typeof Promise.resolve("ok")`?

<details>
<summary>Answer</summary>

- [x] **"object"**. `instanceof Promise` is **true**.

</details>


</details>

## Summary

Remember the eight types, that + concatenates once a string appears, and that typeof null is the string object. Prefer BigInt literals or BigInt of a string. Built-in objects still typeof as object except functions.

## References

- [JS Data Types (W3Schools)](https://www.w3schools.com/js/js_datatypes.asp)
- [MDN: JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [MDN: BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)

</details>
