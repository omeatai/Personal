<details>
  <summary>JS Array Reference</summary>

## Introduction

The complete Array reference table (revised July 2025) lists every constructor form and instance method on this page. Each row is its own Example. Literals and new Array() both create arrays. at, concat, copyWithin, fill, and the find/filter/map/reduce family do what their tutorial chapters already showed, collected here as one catalog. of(7) is [7], unlike new Array(7). prototype is demonstrated with a tiny last() helper on this sandbox page only. valueOf returns the array itself. toReversed, toSorted, toSpliced, and with are the non-mutating ES2023 copies.

This section has **45** examples:

- [x] **Example 1:** [] — creates a new Array [View](#js-array-reference-example-01)
- [x] **Example 2:** new Array() — creates a new Array [View](#js-array-reference-example-02)
- [x] **Example 3:** at() — indexed element [View](#js-array-reference-example-03)
- [x] **Example 4:** concat() — join arrays [View](#js-array-reference-example-04)
- [x] **Example 5:** constructor — function that created Array.prototype [View](#js-array-reference-example-05)
- [x] **Example 6:** copyWithin() — copy within the array [View](#js-array-reference-example-06)
- [x] **Example 7:** entries() — [index, value] iterator [View](#js-array-reference-example-07)
- [x] **Example 8:** every() — all pass a test? [View](#js-array-reference-example-08)
- [x] **Example 9:** fill() — fill with a static value [View](#js-array-reference-example-09)
- [x] **Example 10:** filter() — keep elements that pass [View](#js-array-reference-example-10)
- [x] **Example 11:** find() — first matching value [View](#js-array-reference-example-11)
- [x] **Example 12:** findIndex() — first matching index [View](#js-array-reference-example-12)
- [x] **Example 13:** findLast() — last matching value [View](#js-array-reference-example-13)
- [x] **Example 14:** findLastIndex() — last matching index [View](#js-array-reference-example-14)
- [x] **Example 15:** flat() — concatenate sub-arrays [View](#js-array-reference-example-15)
- [x] **Example 16:** flatMap() — map then flatten [View](#js-array-reference-example-16)
- [x] **Example 17:** forEach() — call a function per element [View](#js-array-reference-example-17)
- [x] **Example 18:** from() — array from an object [View](#js-array-reference-example-18)
- [x] **Example 19:** includes() — contains the element? [View](#js-array-reference-example-19)
- [x] **Example 20:** indexOf() — first position [View](#js-array-reference-example-20)
- [x] **Example 21:** isArray() — is this an array? [View](#js-array-reference-example-21)
- [x] **Example 22:** join() — elements to a string [View](#js-array-reference-example-22)
- [x] **Example 23:** keys() — iterator of indexes [View](#js-array-reference-example-23)
- [x] **Example 24:** lastIndexOf() — last position [View](#js-array-reference-example-24)
- [x] **Example 25:** length — number of elements [View](#js-array-reference-example-25)
- [x] **Example 26:** map() — new array from a function [View](#js-array-reference-example-26)
- [x] **Example 27:** of() — array from arguments [View](#js-array-reference-example-27)
- [x] **Example 28:** pop() — remove last, return it [View](#js-array-reference-example-28)
- [x] **Example 29:** prototype — add a method (this page only) [View](#js-array-reference-example-29)
- [x] **Example 30:** push() — add at the end, return length [View](#js-array-reference-example-30)
- [x] **Example 31:** reduce() — fold left to right [View](#js-array-reference-example-31)
- [x] **Example 32:** reduceRight() — fold right to left [View](#js-array-reference-example-32)
- [x] **Example 33:** reverse() — reverse in place [View](#js-array-reference-example-33)
- [x] **Example 34:** shift() — remove first, return it [View](#js-array-reference-example-34)
- [x] **Example 35:** slice() — copy a part [View](#js-array-reference-example-35)
- [x] **Example 36:** some() — any pass a test? [View](#js-array-reference-example-36)
- [x] **Example 37:** sort() — sort the elements [View](#js-array-reference-example-37)
- [x] **Example 38:** splice() — add or remove in place [View](#js-array-reference-example-38)
- [x] **Example 39:** toReversed() — reverse to a new array [View](#js-array-reference-example-39)
- [x] **Example 40:** toSorted() — sort to a new array [View](#js-array-reference-example-40)
- [x] **Example 41:** toSpliced() — splice to a new array [View](#js-array-reference-example-41)
- [x] **Example 42:** toString() — array as a string [View](#js-array-reference-example-42)
- [x] **Example 43:** unshift() — add at the start, return length [View](#js-array-reference-example-43)
- [x] **Example 44:** valueOf() — primitive value of the array [View](#js-array-reference-example-44)
- [x] **Example 45:** with() — new array with an updated index [View](#js-array-reference-example-45)

## Detailed Explanation

- [x] **Every table row is an Example** — 45 rows including `[]` and `new Array()`.
- [x] `Array.of(7)` is **[7]**; `new Array(7)` is seven holes.
- [x] Mutating: copyWithin, fill, pop, push, reverse, shift, sort, splice, unshift.
- [x] Copying: concat, slice, toReversed, toSorted, toSpliced, with, map, filter, flat*.
- [x] `valueOf()` is the array itself. `constructor` is **Array**.
- [x] `Array.prototype` add-ons belong in a demo file only.

<a id="js-array-reference-example-01"></a>

### **Example 1: [] — creates a new Array**

- [x] An array **literal** creates a new array.

Sandbox: `code_sandbox/js-array-reference/literal.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
```

<img alt="js-array-reference example 1 source" src="./code_sandbox/snaps/js-array-reference-01-code.png" />

<img alt="js-array-reference example 1 result" src="./code_sandbox/snaps/js-array-reference-01-result.png" />

- [x] **Outcome:** **["Saab","Volvo","BMW"]**.

<a id="js-array-reference-example-02"></a>

### **Example 2: new Array() — creates a new Array**

- [x] `new Array()` with no args is an **empty** array.

Sandbox: `code_sandbox/js-array-reference/new-array.html`

```javascript
const a = new Array();
```

<img alt="js-array-reference example 2 source" src="./code_sandbox/snaps/js-array-reference-02-code.png" />

<img alt="js-array-reference example 2 result" src="./code_sandbox/snaps/js-array-reference-02-result.png" />

- [x] **Outcome:** **[]**.

<a id="js-array-reference-example-03"></a>

### **Example 3: at() — indexed element**

- [x] `at(2)` is **Apple**. `at` also accepts negatives.

Sandbox: `code_sandbox/js-array-reference/at.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits.at(2);
```

<img alt="js-array-reference example 3 source" src="./code_sandbox/snaps/js-array-reference-03-code.png" />

<img alt="js-array-reference example 3 result" src="./code_sandbox/snaps/js-array-reference-03-result.png" />

- [x] **Outcome:** **Apple**.

<a id="js-array-reference-example-04"></a>

### **Example 4: concat() — join arrays**

- [x] `concat` returns a **new** joined array.

Sandbox: `code_sandbox/js-array-reference/concat.html`

```javascript
const a = ["Cecilie", "Lone"];
const b = a.concat(["Emil"]);
```

<img alt="js-array-reference example 4 source" src="./code_sandbox/snaps/js-array-reference-04-code.png" />

<img alt="js-array-reference example 4 result" src="./code_sandbox/snaps/js-array-reference-04-result.png" />

- [x] **Outcome:** **["Cecilie","Lone","Emil"]**.

<a id="js-array-reference-example-05"></a>

### **Example 5: constructor — function that created Array.prototype**

- [x] Instance `constructor` is **Array**.

Sandbox: `code_sandbox/js-array-reference/constructor.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.constructor;
fruits.constructor === Array;
```

<img alt="js-array-reference example 5 source" src="./code_sandbox/snaps/js-array-reference-05-code.png" />

<img alt="js-array-reference example 5 result" src="./code_sandbox/snaps/js-array-reference-05-result.png" />

- [x] **Outcome:** `function Array() { [native code] }`. `=== Array` is **true**.

<a id="js-array-reference-example-06"></a>

### **Example 6: copyWithin() — copy within the array**

- [x] `copyWithin(2, 0)` overwrites from index 2 using items from 0.

Sandbox: `code_sandbox/js-array-reference/copywithin.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.copyWithin(2, 0);
```

<img alt="js-array-reference example 6 source" src="./code_sandbox/snaps/js-array-reference-06-code.png" />

<img alt="js-array-reference example 6 result" src="./code_sandbox/snaps/js-array-reference-06-result.png" />

- [x] **Outcome:** **["Banana","Orange","Banana","Orange"]**.

<a id="js-array-reference-example-07"></a>

### **Example 7: entries() — [index, value] iterator**

- [x] `Array.from(fruits.entries())` materializes the pairs.

Sandbox: `code_sandbox/js-array-reference/entries.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
const pairs = Array.from(fruits.entries());
```

<img alt="js-array-reference example 7 source" src="./code_sandbox/snaps/js-array-reference-07-code.png" />

<img alt="js-array-reference example 7 result" src="./code_sandbox/snaps/js-array-reference-07-result.png" />

- [x] **Outcome:** **[[0,"Banana"],[1,"Orange"],[2,"Apple"],[3,"Mango"]]**.

<a id="js-array-reference-example-08"></a>

### **Example 8: every() — all pass a test?**

- [x] `every(v => v > 18)` on [4, 9, 16, 25, 29].

Sandbox: `code_sandbox/js-array-reference/every.html`

```javascript
const numbers = [4, 9, 16, 25, 29];
let ok = numbers.every(v => v > 18);
```

<img alt="js-array-reference example 8 source" src="./code_sandbox/snaps/js-array-reference-08-code.png" />

<img alt="js-array-reference example 8 result" src="./code_sandbox/snaps/js-array-reference-08-result.png" />

- [x] **Outcome:** **false**.

<a id="js-array-reference-example-09"></a>

### **Example 9: fill() — fill with a static value**

- [x] `fill("Kiwi")` replaces every element.

Sandbox: `code_sandbox/js-array-reference/fill.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.fill("Kiwi");
```

<img alt="js-array-reference example 9 source" src="./code_sandbox/snaps/js-array-reference-09-code.png" />

<img alt="js-array-reference example 9 result" src="./code_sandbox/snaps/js-array-reference-09-result.png" />

- [x] **Outcome:** **["Kiwi","Kiwi","Kiwi","Kiwi"]**.

<a id="js-array-reference-example-10"></a>

### **Example 10: filter() — keep elements that pass**

- [x] Keep values **> 18**.

Sandbox: `code_sandbox/js-array-reference/filter.html`

```javascript
const numbers = [4, 9, 16, 25, 29];
const over = numbers.filter(v => v > 18);
```

<img alt="js-array-reference example 10 source" src="./code_sandbox/snaps/js-array-reference-10-code.png" />

<img alt="js-array-reference example 10 result" src="./code_sandbox/snaps/js-array-reference-10-result.png" />

- [x] **Outcome:** **[25,29]**.

<a id="js-array-reference-example-11"></a>

### **Example 11: find() — first matching value**

- [x] First value **> 18**.

Sandbox: `code_sandbox/js-array-reference/find.html`

```javascript
const numbers = [4, 9, 16, 25, 29];
let first = numbers.find(v => v > 18);
```

<img alt="js-array-reference example 11 source" src="./code_sandbox/snaps/js-array-reference-11-code.png" />

<img alt="js-array-reference example 11 result" src="./code_sandbox/snaps/js-array-reference-11-result.png" />

- [x] **Outcome:** **25**.

<a id="js-array-reference-example-12"></a>

### **Example 12: findIndex() — first matching index**

- [x] Index of first value **> 18**.

Sandbox: `code_sandbox/js-array-reference/findindex.html`

```javascript
const numbers = [4, 9, 16, 25, 29];
let i = numbers.findIndex(v => v > 18);
```

<img alt="js-array-reference example 12 source" src="./code_sandbox/snaps/js-array-reference-12-code.png" />

<img alt="js-array-reference example 12 result" src="./code_sandbox/snaps/js-array-reference-12-result.png" />

- [x] **Outcome:** **3**.

<a id="js-array-reference-example-13"></a>

### **Example 13: findLast() — last matching value**

- [x] From the end, first value **> 40**.

Sandbox: `code_sandbox/js-array-reference/findlast.html`

```javascript
const temp = [27, 28, 30, 40, 42, 35, 30];
let high = temp.findLast(x => x > 40);
```

<img alt="js-array-reference example 13 source" src="./code_sandbox/snaps/js-array-reference-13-code.png" />

<img alt="js-array-reference example 13 result" src="./code_sandbox/snaps/js-array-reference-13-result.png" />

- [x] **Outcome:** **42**.

<a id="js-array-reference-example-14"></a>

### **Example 14: findLastIndex() — last matching index**

- [x] Index of that last match.

Sandbox: `code_sandbox/js-array-reference/findlastindex.html`

```javascript
const temp = [27, 28, 30, 40, 42, 35, 30];
let pos = temp.findLastIndex(x => x > 40);
```

<img alt="js-array-reference example 14 source" src="./code_sandbox/snaps/js-array-reference-14-code.png" />

<img alt="js-array-reference example 14 result" src="./code_sandbox/snaps/js-array-reference-14-result.png" />

- [x] **Outcome:** **4**.

<a id="js-array-reference-example-15"></a>

### **Example 15: flat() — concatenate sub-arrays**

- [x] Flatten one level.

Sandbox: `code_sandbox/js-array-reference/flat.html`

```javascript
const newArr = [[1,2],[3,4]].flat();
```

<img alt="js-array-reference example 15 source" src="./code_sandbox/snaps/js-array-reference-15-code.png" />

<img alt="js-array-reference example 15 result" src="./code_sandbox/snaps/js-array-reference-15-result.png" />

- [x] **Outcome:** **[1,2,3,4]**.

<a id="js-array-reference-example-16"></a>

### **Example 16: flatMap() — map then flatten**

- [x] Each `x` becomes `[x, x*10]`.

Sandbox: `code_sandbox/js-array-reference/flatmap.html`

```javascript
const newArr = [1, 2].flatMap(x => [x, x * 10]);
```

<img alt="js-array-reference example 16 source" src="./code_sandbox/snaps/js-array-reference-16-code.png" />

<img alt="js-array-reference example 16 result" src="./code_sandbox/snaps/js-array-reference-16-result.png" />

- [x] **Outcome:** **[1,10,2,20]**.

<a id="js-array-reference-example-17"></a>

### **Example 17: forEach() — call a function per element**

- [x] Join values with spaces.

Sandbox: `code_sandbox/js-array-reference/foreach.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let text = "";
fruits.forEach(function(value){ text += value + " "; });
```

<img alt="js-array-reference example 17 source" src="./code_sandbox/snaps/js-array-reference-17-code.png" />

<img alt="js-array-reference example 17 result" src="./code_sandbox/snaps/js-array-reference-17-result.png" />

- [x] **Outcome:** **Banana Orange Apple Mango** (trailing space).

<a id="js-array-reference-example-18"></a>

### **Example 18: from() — array from an object**

- [x] `Array.from` on a string.

Sandbox: `code_sandbox/js-array-reference/from.html`

```javascript
const letters = Array.from("ABC");
```

<img alt="js-array-reference example 18 source" src="./code_sandbox/snaps/js-array-reference-18-code.png" />

<img alt="js-array-reference example 18 result" src="./code_sandbox/snaps/js-array-reference-18-result.png" />

- [x] **Outcome:** **["A","B","C"]**.

<a id="js-array-reference-example-19"></a>

### **Example 19: includes() — contains the element?**

- [x] Does fruits include **"Mango"**?

Sandbox: `code_sandbox/js-array-reference/includes.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.includes("Mango");
```

<img alt="js-array-reference example 19 source" src="./code_sandbox/snaps/js-array-reference-19-code.png" />

<img alt="js-array-reference example 19 result" src="./code_sandbox/snaps/js-array-reference-19-result.png" />

- [x] **Outcome:** **true**.

<a id="js-array-reference-example-20"></a>

### **Example 20: indexOf() — first position**

- [x] First index of **"Apple"** in a list that has two Apples.

Sandbox: `code_sandbox/js-array-reference/indexof.html`

```javascript
const fruits = ["Apple", "Orange", "Apple", "Mango"];
let i = fruits.indexOf("Apple");
```

<img alt="js-array-reference example 20 source" src="./code_sandbox/snaps/js-array-reference-20-code.png" />

<img alt="js-array-reference example 20 result" src="./code_sandbox/snaps/js-array-reference-20-result.png" />

- [x] **Outcome:** **0**.

<a id="js-array-reference-example-21"></a>

### **Example 21: isArray() — is this an array?**

- [x] `Array.isArray(fruits)`.

Sandbox: `code_sandbox/js-array-reference/isarray.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
Array.isArray(fruits);
```

<img alt="js-array-reference example 21 source" src="./code_sandbox/snaps/js-array-reference-21-code.png" />

<img alt="js-array-reference example 21 result" src="./code_sandbox/snaps/js-array-reference-21-result.png" />

- [x] **Outcome:** **true**.

<a id="js-array-reference-example-22"></a>

### **Example 22: join() — elements to a string**

- [x] Join with **" * "**.

Sandbox: `code_sandbox/js-array-reference/join.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let text = fruits.join(" * ");
```

<img alt="js-array-reference example 22 source" src="./code_sandbox/snaps/js-array-reference-22-code.png" />

<img alt="js-array-reference example 22 result" src="./code_sandbox/snaps/js-array-reference-22-result.png" />

- [x] **Outcome:** **Banana * Orange * Apple * Mango**.

<a id="js-array-reference-example-23"></a>

### **Example 23: keys() — iterator of indexes**

- [x] `Array.from(fruits.keys())`.

Sandbox: `code_sandbox/js-array-reference/keys.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
const keys = Array.from(fruits.keys());
```

<img alt="js-array-reference example 23 source" src="./code_sandbox/snaps/js-array-reference-23-code.png" />

<img alt="js-array-reference example 23 result" src="./code_sandbox/snaps/js-array-reference-23-result.png" />

- [x] **Outcome:** **[0,1,2,3]**.

<a id="js-array-reference-example-24"></a>

### **Example 24: lastIndexOf() — last position**

- [x] Last index of **"Apple"**.

Sandbox: `code_sandbox/js-array-reference/lastindexof.html`

```javascript
const fruits = ["Apple", "Orange", "Apple", "Mango"];
let i = fruits.lastIndexOf("Apple");
```

<img alt="js-array-reference example 24 source" src="./code_sandbox/snaps/js-array-reference-24-code.png" />

<img alt="js-array-reference example 24 result" src="./code_sandbox/snaps/js-array-reference-24-result.png" />

- [x] **Outcome:** **2**.

<a id="js-array-reference-example-25"></a>

### **Example 25: length — number of elements**

- [x] Read `fruits.length`.

Sandbox: `code_sandbox/js-array-reference/length.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let n = fruits.length;
```

<img alt="js-array-reference example 25 source" src="./code_sandbox/snaps/js-array-reference-25-code.png" />

<img alt="js-array-reference example 25 result" src="./code_sandbox/snaps/js-array-reference-25-result.png" />

- [x] **Outcome:** **4**.

<a id="js-array-reference-example-26"></a>

### **Example 26: map() — new array from a function**

- [x] Double each number.

Sandbox: `code_sandbox/js-array-reference/map.html`

```javascript
const doubled = [4, 9, 16].map(v => v * 2);
```

<img alt="js-array-reference example 26 source" src="./code_sandbox/snaps/js-array-reference-26-code.png" />

<img alt="js-array-reference example 26 result" src="./code_sandbox/snaps/js-array-reference-26-result.png" />

- [x] **Outcome:** **[8,18,32]**.

<a id="js-array-reference-example-27"></a>

### **Example 27: of() — array from arguments**

- [x] `Array.of(7)` is **`[7]`**, not 7 empty slots.

Sandbox: `code_sandbox/js-array-reference/of.html`

```javascript
const a = Array.of(7);
const b = Array.of(1, 2, 3);
```

<img alt="js-array-reference example 27 source" src="./code_sandbox/snaps/js-array-reference-27-code.png" />

<img alt="js-array-reference example 27 result" src="./code_sandbox/snaps/js-array-reference-27-result.png" />

- [x] **Outcome:** **[7]** and **[1,2,3]**.

<a id="js-array-reference-example-28"></a>

### **Example 28: pop() — remove last, return it**

- [x] Pop mango off fruits.

Sandbox: `code_sandbox/js-array-reference/pop.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits.pop();
```

<img alt="js-array-reference example 28 source" src="./code_sandbox/snaps/js-array-reference-28-code.png" />

<img alt="js-array-reference example 28 result" src="./code_sandbox/snaps/js-array-reference-28-result.png" />

- [x] **Outcome:** **Mango**. fruits **["Banana","Orange","Apple"]**.

<a id="js-array-reference-example-29"></a>

### **Example 29: prototype — add a method (this page only)**

- [x] `Array.prototype` can add methods. Prefer **not** to ship prototype pollution.
- [x] A tiny `last()` helper **in this sandbox file only**.

Sandbox: `code_sandbox/js-array-reference/prototype.html`

```javascript
Array.prototype.last = function () {
  return this[this.length - 1];
};
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits.last();
```

<img alt="js-array-reference example 29 source" src="./code_sandbox/snaps/js-array-reference-29-code.png" />

<img alt="js-array-reference example 29 result" src="./code_sandbox/snaps/js-array-reference-29-result.png" />

- [x] **Outcome:** **Mango**. Isolated to this file — do not add this to shared pages.

<a id="js-array-reference-example-30"></a>

### **Example 30: push() — add at the end, return length**

- [x] Push **"Kiwi"** and capture the new length.

Sandbox: `code_sandbox/js-array-reference/push.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let n = fruits.push("Kiwi");
```

<img alt="js-array-reference example 30 source" src="./code_sandbox/snaps/js-array-reference-30-code.png" />

<img alt="js-array-reference example 30 result" src="./code_sandbox/snaps/js-array-reference-30-result.png" />

- [x] **Outcome:** length **5**. **["Banana","Orange","Apple","Mango","Kiwi"]**.

<a id="js-array-reference-example-31"></a>

### **Example 31: reduce() — fold left to right**

- [x] Sum [45, 4, 9, 16, 25].

Sandbox: `code_sandbox/js-array-reference/reduce.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let sum = numbers.reduce((t, v) => t + v);
```

<img alt="js-array-reference example 31 source" src="./code_sandbox/snaps/js-array-reference-31-code.png" />

<img alt="js-array-reference example 31 result" src="./code_sandbox/snaps/js-array-reference-31-result.png" />

- [x] **Outcome:** **99**.

<a id="js-array-reference-example-32"></a>

### **Example 32: reduceRight() — fold right to left**

- [x] Same sum from the other end.

Sandbox: `code_sandbox/js-array-reference/reduceright.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let sum = numbers.reduceRight((t, v) => t + v);
```

<img alt="js-array-reference example 32 source" src="./code_sandbox/snaps/js-array-reference-32-code.png" />

<img alt="js-array-reference example 32 result" src="./code_sandbox/snaps/js-array-reference-32-result.png" />

- [x] **Outcome:** **99**.

<a id="js-array-reference-example-33"></a>

### **Example 33: reverse() — reverse in place**

- [x] Reverse fruits.

Sandbox: `code_sandbox/js-array-reference/reverse.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.reverse();
```

<img alt="js-array-reference example 33 source" src="./code_sandbox/snaps/js-array-reference-33-code.png" />

<img alt="js-array-reference example 33 result" src="./code_sandbox/snaps/js-array-reference-33-result.png" />

- [x] **Outcome:** **["Mango","Apple","Orange","Banana"]**.

<a id="js-array-reference-example-34"></a>

### **Example 34: shift() — remove first, return it**

- [x] Shift banana off fruits.

Sandbox: `code_sandbox/js-array-reference/shift.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits.shift();
```

<img alt="js-array-reference example 34 source" src="./code_sandbox/snaps/js-array-reference-34-code.png" />

<img alt="js-array-reference example 34 result" src="./code_sandbox/snaps/js-array-reference-34-result.png" />

- [x] **Outcome:** **Banana**. fruits **["Orange","Apple","Mango"]**.

<a id="js-array-reference-example-35"></a>

### **Example 35: slice() — copy a part**

- [x] `slice(1, 3)` is up to but not including 3.

Sandbox: `code_sandbox/js-array-reference/slice.html`

```javascript
const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruits.slice(1, 3);
```

<img alt="js-array-reference example 35 source" src="./code_sandbox/snaps/js-array-reference-35-code.png" />

<img alt="js-array-reference example 35 result" src="./code_sandbox/snaps/js-array-reference-35-result.png" />

- [x] **Outcome:** **["Orange","Lemon"]**.

<a id="js-array-reference-example-36"></a>

### **Example 36: some() — any pass a test?**

- [x] `some(v => v > 18)` on [4, 9, 16, 25, 29].

Sandbox: `code_sandbox/js-array-reference/some.html`

```javascript
const numbers = [4, 9, 16, 25, 29];
let ok = numbers.some(v => v > 18);
```

<img alt="js-array-reference example 36 source" src="./code_sandbox/snaps/js-array-reference-36-code.png" />

<img alt="js-array-reference example 36 result" src="./code_sandbox/snaps/js-array-reference-36-result.png" />

- [x] **Outcome:** **true**.

<a id="js-array-reference-example-37"></a>

### **Example 37: sort() — sort the elements**

- [x] Default alphabetic sort.

Sandbox: `code_sandbox/js-array-reference/sort.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.sort();
```

<img alt="js-array-reference example 37 source" src="./code_sandbox/snaps/js-array-reference-37-code.png" />

<img alt="js-array-reference example 37 result" src="./code_sandbox/snaps/js-array-reference-37-result.png" />

- [x] **Outcome:** **["Apple","Banana","Mango","Orange"]**.

<a id="js-array-reference-example-38"></a>

### **Example 38: splice() — add or remove in place**

- [x] Insert Lemon and Kiwi at 2, delete 0.

Sandbox: `code_sandbox/js-array-reference/splice.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(2, 0, "Lemon", "Kiwi");
```

<img alt="js-array-reference example 38 source" src="./code_sandbox/snaps/js-array-reference-38-code.png" />

<img alt="js-array-reference example 38 result" src="./code_sandbox/snaps/js-array-reference-38-result.png" />

- [x] **Outcome:** **["Banana","Orange","Lemon","Kiwi","Apple","Mango"]**.

<a id="js-array-reference-example-39"></a>

### **Example 39: toReversed() — reverse to a new array**

- [x] Non-mutating reverse.

Sandbox: `code_sandbox/js-array-reference/toreversed.html`

```javascript
const months = ["Jan", "Feb", "Mar", "Apr"];
const reversed = months.toReversed();
```

<img alt="js-array-reference example 39 source" src="./code_sandbox/snaps/js-array-reference-39-code.png" />

<img alt="js-array-reference example 39 result" src="./code_sandbox/snaps/js-array-reference-39-result.png" />

- [x] **Outcome:** **["Apr","Mar","Feb","Jan"]**. Original unchanged.

<a id="js-array-reference-example-40"></a>

### **Example 40: toSorted() — sort to a new array**

- [x] Non-mutating sort.

Sandbox: `code_sandbox/js-array-reference/tosorted.html`

```javascript
const months = ["Jan", "Feb", "Mar", "Apr"];
const sorted = months.toSorted();
```

<img alt="js-array-reference example 40 source" src="./code_sandbox/snaps/js-array-reference-40-code.png" />

<img alt="js-array-reference example 40 result" src="./code_sandbox/snaps/js-array-reference-40-result.png" />

- [x] **Outcome:** **["Apr","Feb","Jan","Mar"]**. Original unchanged.

<a id="js-array-reference-example-41"></a>

### **Example 41: toSpliced() — splice to a new array**

- [x] Non-mutating splice: drop index 0.

Sandbox: `code_sandbox/js-array-reference/tospliced.html`

```javascript
const months = ["Jan", "Feb", "Mar", "Apr"];
const spliced = months.toSpliced(0, 1);
```

<img alt="js-array-reference example 41 source" src="./code_sandbox/snaps/js-array-reference-41-code.png" />

<img alt="js-array-reference example 41 result" src="./code_sandbox/snaps/js-array-reference-41-result.png" />

- [x] **Outcome:** **["Feb","Mar","Apr"]**. Original unchanged.

<a id="js-array-reference-example-42"></a>

### **Example 42: toString() — array as a string**

- [x] Comma-separated values.

Sandbox: `code_sandbox/js-array-reference/tostring.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let text = fruits.toString();
```

<img alt="js-array-reference example 42 source" src="./code_sandbox/snaps/js-array-reference-42-code.png" />

<img alt="js-array-reference example 42 result" src="./code_sandbox/snaps/js-array-reference-42-result.png" />

- [x] **Outcome:** **Banana,Orange,Apple,Mango**.

<a id="js-array-reference-example-43"></a>

### **Example 43: unshift() — add at the start, return length**

- [x] Unshift **"Lemon"**.

Sandbox: `code_sandbox/js-array-reference/unshift.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let n = fruits.unshift("Lemon");
```

<img alt="js-array-reference example 43 source" src="./code_sandbox/snaps/js-array-reference-43-code.png" />

<img alt="js-array-reference example 43 result" src="./code_sandbox/snaps/js-array-reference-43-result.png" />

- [x] **Outcome:** length **5**. **["Lemon","Banana","Orange","Apple","Mango"]**.

<a id="js-array-reference-example-44"></a>

### **Example 44: valueOf() — primitive value of the array**

- [x] `valueOf()` returns **the array itself**. Stringifying it matches `toString`.

Sandbox: `code_sandbox/js-array-reference/valueof.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.valueOf() === fruits;
String(fruits.valueOf());
```

<img alt="js-array-reference example 44 source" src="./code_sandbox/snaps/js-array-reference-44-code.png" />

<img alt="js-array-reference example 44 result" src="./code_sandbox/snaps/js-array-reference-44-result.png" />

- [x] **Outcome:** `=== fruits` is **true**. String is **Banana,Orange,Apple,Mango**.

<a id="js-array-reference-example-45"></a>

### **Example 45: with() — new array with an updated index**

- [x] Replace index 2 with **"March"** without mutating.

Sandbox: `code_sandbox/js-array-reference/with.html`

```javascript
const months = ["Januar", "Februar", "Mar", "April"];
const next = months.with(2, "March");
```

<img alt="js-array-reference example 45 source" src="./code_sandbox/snaps/js-array-reference-45-code.png" />

<img alt="js-array-reference example 45 result" src="./code_sandbox/snaps/js-array-reference-45-result.png" />

- [x] **Outcome:** **["Januar","Februar","March","April"]**. Original still **"Mar"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-array-reference/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How many table rows?

<details>
<summary>Answer</summary>

- [x] **45**, each with its own Example.

</details>

### Question 2: [] vs new Array()?

<details>
<summary>Answer</summary>

- [x] Both create arrays. `[]` is the empty literal; `new Array()` is the empty constructor.

</details>

### Question 3: What does constructor print?

<details>
<summary>Answer</summary>

- [x] `function Array() { [native code] }`. `=== Array` is **true**.

</details>

### Question 4: Array.of(7)?

<details>
<summary>Answer</summary>

- [x] **[7]**, not seven empty slots.

</details>

### Question 5: fill("Kiwi") on four fruits?

<details>
<summary>Answer</summary>

- [x] **["Kiwi","Kiwi","Kiwi","Kiwi"]**.

</details>

### Question 6: filter > 18 on [4,9,16,25,29]?

<details>
<summary>Answer</summary>

- [x] **[25,29]**.

</details>

### Question 7: What does the prototype demo add?

<details>
<summary>Answer</summary>

- [x] `last()` → **Mango** on that page only.

</details>

### Question 8: valueOf() === fruits?

<details>
<summary>Answer</summary>

- [x] **true**. String(valueOf()) is the comma list.

</details>

### Question 9: toSorted vs sort?

<details>
<summary>Answer</summary>

- [x] toSorted returns a **new** array. sort mutates.

</details>

### Question 10: with(2, "March")?

<details>
<summary>Answer</summary>

- [x] A copy with index 2 replaced. Original unchanged.

</details>

### Question 11: entries() as JSON?

<details>
<summary>Answer</summary>

- [x] **[[0,"Banana"],[1,"Orange"],[2,"Apple"],[3,"Mango"]]**.

</details>

### Question 12: reduce sum of [45,4,9,16,25]?

<details>
<summary>Answer</summary>

- [x] **99**.

</details>


</details>

## Summary

Treat this page as the catalog: construct with [] or Array.of, mutate with splice/push/sort, copy with slice/toSpliced/with, and fold with reduce. Keep prototype experiments in the demo file.

## References

- [JS Array Reference (W3Schools)](https://www.w3schools.com/js/js_array_reference.asp)
- [MDN: Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [MDN: Array.of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of)

</details>
