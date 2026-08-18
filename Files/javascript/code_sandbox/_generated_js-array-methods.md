<details>
  <summary>JS Array Methods</summary>

## Introduction

Basic array methods cover length, string conversion, indexed reads, join, stack operations at both ends, concat, copyWithin, flattening, and splice versus slice. pop, push, shift, unshift, splice, and copyWithin mutate; concat, slice, flat, flatMap, and toSpliced return new arrays. delete leaves a hole. slice arguments are different Tryits: slice(1), slice(3), slice(1,3), and slice(2) are four examples. at() matches bracket indexing for positive indexes and also supports negatives, which fruits[-1] does not.

This section has **36** examples:

- [x] **Example 1:** fruits.length [View](#js-array-methods-example-01)
- [x] **Example 2:** fruits.length = 2 [View](#js-array-methods-example-02)
- [x] **Example 3:** fruits.toString() [View](#js-array-methods-example-03)
- [x] **Example 4:** fruits.at(2) [View](#js-array-methods-example-04)
- [x] **Example 5:** fruits[2] [View](#js-array-methods-example-05)
- [x] **Example 6:** WARNING fruits[-1] vs fruits.at(-1) [View](#js-array-methods-example-06)
- [x] **Example 7:** fruits.join(" * ") [View](#js-array-methods-example-07)
- [x] **Example 8:** fruits.pop() [View](#js-array-methods-example-08)
- [x] **Example 9:** let fruit = fruits.pop() [View](#js-array-methods-example-09)
- [x] **Example 10:** fruits.push("Kiwi") [View](#js-array-methods-example-10)
- [x] **Example 11:** let length = fruits.push("Kiwi") [View](#js-array-methods-example-11)
- [x] **Example 12:** fruits.shift() [View](#js-array-methods-example-12)
- [x] **Example 13:** let fruit = fruits.shift() [View](#js-array-methods-example-13)
- [x] **Example 14:** fruits.unshift("Lemon") [View](#js-array-methods-example-14)
- [x] **Example 15:** let length = fruits.unshift("Lemon") [View](#js-array-methods-example-15)
- [x] **Example 16:** fruits[0] = "Kiwi" [View](#js-array-methods-example-16)
- [x] **Example 17:** fruits[fruits.length] = Kiwi [View](#js-array-methods-example-17)
- [x] **Example 18:** Array.isArray(fruits) [View](#js-array-methods-example-18)
- [x] **Example 19:** WARNING delete fruits[0] [View](#js-array-methods-example-19)
- [x] **Example 20:** concat two arrays [View](#js-array-methods-example-20)
- [x] **Example 21:** concat three arrays [View](#js-array-methods-example-21)
- [x] **Example 22:** concat an array with "Peter" [View](#js-array-methods-example-22)
- [x] **Example 23:** copyWithin(2, 0) [View](#js-array-methods-example-23)
- [x] **Example 24:** copyWithin(2, 0, 2) [View](#js-array-methods-example-24)
- [x] **Example 25:** [[1,2],[3,4],[5,6]].flat() [View](#js-array-methods-example-25)
- [x] **Example 26:** flatMap(x => [x, x * 10]) [View](#js-array-methods-example-26)
- [x] **Example 27:** splice(2, 0, "Lemon", "Kiwi") [View](#js-array-methods-example-27)
- [x] **Example 28:** splice(2, 2, "Lemon", "Kiwi") [View](#js-array-methods-example-28)
- [x] **Example 29:** splice(0, 1) — remove without holes [View](#js-array-methods-example-29)
- [x] **Example 30:** months.toSpliced(0, 1) [View](#js-array-methods-example-30)
- [x] **Example 31:** slice(1) [View](#js-array-methods-example-31)
- [x] **Example 32:** slice(3) [View](#js-array-methods-example-32)
- [x] **Example 33:** slice(1, 3) [View](#js-array-methods-example-33)
- [x] **Example 34:** slice(2) [View](#js-array-methods-example-34)
- [x] **Example 35:** fruits.toString() for display [View](#js-array-methods-example-35)
- [x] **Example 36:** String(fruits) without calling toString [View](#js-array-methods-example-36)

## Detailed Explanation

- [x] `length` can be **read or set**. Setting it truncates.
- [x] `at(i)` matches `arr[i]` for **≥ 0**. `at(-1)` is the last item; `arr[-1]` is not.
- [x] `pop`/`push` work on the **end**. `shift`/`unshift` work on the **front**. They return the item or the new length.
- [x] `concat`, `slice`, `flat`, `flatMap`, `toSpliced` are **non-mutating**.
- [x] `splice` and `copyWithin` **mutate**. `delete` leaves a hole — prefer splice.
- [x] `slice(start, end)` excludes **end**. Omitting end copies the rest.

<a id="js-array-methods-example-01"></a>

### **Example 1: fruits.length**

- [x] `length` is the **size** of the array.

Sandbox: `code_sandbox/js-array-methods/length-read.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let size = fruits.length;
```

<img alt="js-array-methods example 1 source" src="./code_sandbox/snaps/js-array-methods-01-code.png" />

<img alt="js-array-methods example 1 result" src="./code_sandbox/snaps/js-array-methods-01-result.png" />

- [x] **Outcome:** **4**.

<a id="js-array-methods-example-02"></a>

### **Example 2: fruits.length = 2**

- [x] Setting `length` **truncates** (or extends with holes).

Sandbox: `code_sandbox/js-array-methods/length-set.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.length = 2;
```

<img alt="js-array-methods example 2 source" src="./code_sandbox/snaps/js-array-methods-02-code.png" />

<img alt="js-array-methods example 2 result" src="./code_sandbox/snaps/js-array-methods-02-result.png" />

- [x] **Outcome:** **["Banana","Orange"]**.

<a id="js-array-methods-example-03"></a>

### **Example 3: fruits.toString()**

- [x] `toString()` is a comma-separated string. Every object has `toString`.

Sandbox: `code_sandbox/js-array-methods/tostring.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let myList = fruits.toString();
```

<img alt="js-array-methods example 3 source" src="./code_sandbox/snaps/js-array-methods-03-code.png" />

<img alt="js-array-methods example 3 result" src="./code_sandbox/snaps/js-array-methods-03-result.png" />

- [x] **Outcome:** **Banana,Orange,Apple,Mango**.

<a id="js-array-methods-example-04"></a>

### **Example 4: fruits.at(2)**

- [x] ES2022 `at()` returns the element at that **index**.

Sandbox: `code_sandbox/js-array-methods/at-2.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits.at(2);
```

<img alt="js-array-methods example 4 source" src="./code_sandbox/snaps/js-array-methods-04-code.png" />

<img alt="js-array-methods example 4 result" src="./code_sandbox/snaps/js-array-methods-04-result.png" />

- [x] **Outcome:** **Apple**.

<a id="js-array-methods-example-05"></a>

### **Example 5: fruits[2]**

- [x] `fruits[2]` is the same **positive** index as `at(2)`.

Sandbox: `code_sandbox/js-array-methods/bracket-2.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits[2];
```

<img alt="js-array-methods example 5 source" src="./code_sandbox/snaps/js-array-methods-05-code.png" />

<img alt="js-array-methods example 5 result" src="./code_sandbox/snaps/js-array-methods-05-result.png" />

- [x] **Outcome:** **Apple**.

<a id="js-array-methods-example-06"></a>

### **Example 6: WARNING fruits[-1] vs fruits.at(-1)**

- [x] JS **`[-1]`** is the property named `"-1"`, not the last element.
- [x] `at(-1)` was added to read from the **end**.

Sandbox: `code_sandbox/js-array-methods/at-negative-vs-bracket.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let bracket = fruits[-1];
let fromEnd = fruits.at(-1);
```

<img alt="js-array-methods example 6 source" src="./code_sandbox/snaps/js-array-methods-06-code.png" />

<img alt="js-array-methods example 6 result" src="./code_sandbox/snaps/js-array-methods-06-result.png" />

- [x] **Outcome:** `fruits[-1]` is **undefined**. `fruits.at(-1)` is **Mango**.

<a id="js-array-methods-example-07"></a>

### **Example 7: fruits.join(" * ")**

- [x] `join` is like `toString` but you pick the **separator**.

Sandbox: `code_sandbox/js-array-methods/join-star.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let text = fruits.join(" * ");
```

<img alt="js-array-methods example 7 source" src="./code_sandbox/snaps/js-array-methods-07-code.png" />

<img alt="js-array-methods example 7 result" src="./code_sandbox/snaps/js-array-methods-07-result.png" />

- [x] **Outcome:** **Banana * Orange * Apple * Mango**.

<a id="js-array-methods-example-08"></a>

### **Example 8: fruits.pop()**

- [x] `pop` **removes the last** element.

Sandbox: `code_sandbox/js-array-methods/pop.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.pop();
```

<img alt="js-array-methods example 8 source" src="./code_sandbox/snaps/js-array-methods-08-code.png" />

<img alt="js-array-methods example 8 result" src="./code_sandbox/snaps/js-array-methods-08-result.png" />

- [x] **Outcome:** **["Banana","Orange","Apple"]**.

<a id="js-array-methods-example-09"></a>

### **Example 9: let fruit = fruits.pop()**

- [x] `pop` **returns** the removed value.

Sandbox: `code_sandbox/js-array-methods/pop-return.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits.pop();
```

<img alt="js-array-methods example 9 source" src="./code_sandbox/snaps/js-array-methods-09-code.png" />

<img alt="js-array-methods example 9 result" src="./code_sandbox/snaps/js-array-methods-09-result.png" />

- [x] **Outcome:** fruit is **"Mango"**. fruits is **["Banana","Orange","Apple"]**.

<a id="js-array-methods-example-10"></a>

### **Example 10: fruits.push("Kiwi")**

- [x] `push` **appends** at the end.

Sandbox: `code_sandbox/js-array-methods/push-kiwi.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.push("Kiwi");
```

<img alt="js-array-methods example 10 source" src="./code_sandbox/snaps/js-array-methods-10-code.png" />

<img alt="js-array-methods example 10 result" src="./code_sandbox/snaps/js-array-methods-10-result.png" />

- [x] **Outcome:** **["Banana","Orange","Apple","Mango","Kiwi"]**.

<a id="js-array-methods-example-11"></a>

### **Example 11: let length = fruits.push("Kiwi")**

- [x] `push` **returns the new length**.

Sandbox: `code_sandbox/js-array-methods/push-return-length.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let length = fruits.push("Kiwi");
```

<img alt="js-array-methods example 11 source" src="./code_sandbox/snaps/js-array-methods-11-code.png" />

<img alt="js-array-methods example 11 result" src="./code_sandbox/snaps/js-array-methods-11-result.png" />

- [x] **Outcome:** length **5**. fruits **["Banana","Orange","Apple","Mango","Kiwi"]**.

<a id="js-array-methods-example-12"></a>

### **Example 12: fruits.shift()**

- [x] `shift` removes the **first** element and moves the rest down.

Sandbox: `code_sandbox/js-array-methods/shift.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.shift();
```

<img alt="js-array-methods example 12 source" src="./code_sandbox/snaps/js-array-methods-12-code.png" />

<img alt="js-array-methods example 12 result" src="./code_sandbox/snaps/js-array-methods-12-result.png" />

- [x] **Outcome:** **["Orange","Apple","Mango"]**.

<a id="js-array-methods-example-13"></a>

### **Example 13: let fruit = fruits.shift()**

- [x] `shift` **returns** the removed first value.

Sandbox: `code_sandbox/js-array-methods/shift-return.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits.shift();
```

<img alt="js-array-methods example 13 source" src="./code_sandbox/snaps/js-array-methods-13-code.png" />

<img alt="js-array-methods example 13 result" src="./code_sandbox/snaps/js-array-methods-13-result.png" />

- [x] **Outcome:** fruit is **"Banana"**. fruits is **["Orange","Apple","Mango"]**.

<a id="js-array-methods-example-14"></a>

### **Example 14: fruits.unshift("Lemon")**

- [x] `unshift` inserts at the **beginning**.

Sandbox: `code_sandbox/js-array-methods/unshift-lemon.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.unshift("Lemon");
```

<img alt="js-array-methods example 14 source" src="./code_sandbox/snaps/js-array-methods-14-code.png" />

<img alt="js-array-methods example 14 result" src="./code_sandbox/snaps/js-array-methods-14-result.png" />

- [x] **Outcome:** **["Lemon","Banana","Orange","Apple","Mango"]**.

<a id="js-array-methods-example-15"></a>

### **Example 15: let length = fruits.unshift("Lemon")**

- [x] `unshift` **returns the new length** (the page’s second unshift Tryit).

Sandbox: `code_sandbox/js-array-methods/unshift-return-length.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let length = fruits.unshift("Lemon");
```

<img alt="js-array-methods example 15 source" src="./code_sandbox/snaps/js-array-methods-15-code.png" />

<img alt="js-array-methods example 15 result" src="./code_sandbox/snaps/js-array-methods-15-result.png" />

- [x] **Outcome:** length **5**. fruits **["Lemon","Banana","Orange","Apple","Mango"]**.

<a id="js-array-methods-example-16"></a>

### **Example 16: fruits[0] = "Kiwi"**

- [x] Indexes start at **0**. Assignment replaces that slot.

Sandbox: `code_sandbox/js-array-methods/change-index-0.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits[0] = "Kiwi";
```

<img alt="js-array-methods example 16 source" src="./code_sandbox/snaps/js-array-methods-16-code.png" />

<img alt="js-array-methods example 16 result" src="./code_sandbox/snaps/js-array-methods-16-result.png" />

- [x] **Outcome:** **["Kiwi","Orange","Apple","Mango"]**.

<a id="js-array-methods-example-17"></a>

### **Example 17: fruits[fruits.length] = Kiwi**

- [x] Writing at `length` **appends**.

Sandbox: `code_sandbox/js-array-methods/append-via-length.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits[fruits.length] = "Kiwi";
```

<img alt="js-array-methods example 17 source" src="./code_sandbox/snaps/js-array-methods-17-code.png" />

<img alt="js-array-methods example 17 result" src="./code_sandbox/snaps/js-array-methods-17-result.png" />

- [x] **Outcome:** **["Banana","Orange","Apple","Mango","Kiwi"]**.

<a id="js-array-methods-example-18"></a>

### **Example 18: Array.isArray(fruits)**

- [x] ES5 `Array.isArray` identifies arrays.

Sandbox: `code_sandbox/js-array-methods/isarray.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
Array.isArray(fruits);
```

<img alt="js-array-methods example 18 source" src="./code_sandbox/snaps/js-array-methods-18-code.png" />

<img alt="js-array-methods example 18 result" src="./code_sandbox/snaps/js-array-methods-18-result.png" />

- [x] **Outcome:** **true**.

<a id="js-array-methods-example-19"></a>

### **Example 19: WARNING delete fruits[0]**

- [x] `delete` leaves an **undefined hole**. Prefer `pop` / `shift` / `splice`.

Sandbox: `code_sandbox/js-array-methods/delete-holes.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
delete fruits[0];
```

<img alt="js-array-methods example 19 source" src="./code_sandbox/snaps/js-array-methods-19-code.png" />

<img alt="js-array-methods example 19 result" src="./code_sandbox/snaps/js-array-methods-19-result.png" />

- [x] **Outcome:** JSON **[null,"Orange","Apple","Mango"]**. `fruits[0]` is **undefined**. `0 in fruits` is **false**. length still **4**.

<a id="js-array-methods-example-20"></a>

### **Example 20: concat two arrays**

- [x] `concat` **merges** arrays and returns a **new** array. Originals stay.

Sandbox: `code_sandbox/js-array-methods/concat-two.html`

```javascript
const myGirls = ["Cecilie", "Lone"];
const myBoys = ["Emil", "Tobias", "Linus"];
const myChildren = myGirls.concat(myBoys);
```

<img alt="js-array-methods example 20 source" src="./code_sandbox/snaps/js-array-methods-20-code.png" />

<img alt="js-array-methods example 20 result" src="./code_sandbox/snaps/js-array-methods-20-result.png" />

- [x] **Outcome:** **["Cecilie","Lone","Emil","Tobias","Linus"]**. myGirls is unchanged.

<a id="js-array-methods-example-21"></a>

### **Example 21: concat three arrays**

- [x] `concat` takes **any number** of array arguments.

Sandbox: `code_sandbox/js-array-methods/concat-three.html`

```javascript
const arr1 = ["Cecilie", "Lone"];
const arr2 = ["Emil", "Tobias", "Linus"];
const arr3 = ["Robin", "Morgan"];
const myChildren = arr1.concat(arr2, arr3);
```

<img alt="js-array-methods example 21 source" src="./code_sandbox/snaps/js-array-methods-21-code.png" />

<img alt="js-array-methods example 21 result" src="./code_sandbox/snaps/js-array-methods-21-result.png" />

- [x] **Outcome:** **["Cecilie","Lone","Emil","Tobias","Linus","Robin","Morgan"]**.

<a id="js-array-methods-example-22"></a>

### **Example 22: concat an array with "Peter"**

- [x] Arguments may be **values**, not only arrays.

Sandbox: `code_sandbox/js-array-methods/concat-string.html`

```javascript
const arr1 = ["Emil", "Tobias", "Linus"];
const myChildren = arr1.concat("Peter");
```

<img alt="js-array-methods example 22 source" src="./code_sandbox/snaps/js-array-methods-22-code.png" />

<img alt="js-array-methods example 22 result" src="./code_sandbox/snaps/js-array-methods-22-result.png" />

- [x] **Outcome:** **["Emil","Tobias","Linus","Peter"]**.

<a id="js-array-methods-example-23"></a>

### **Example 23: copyWithin(2, 0)**

- [x] Copy to index **2** from index **0** through the end. **Overwrites**. Length unchanged.

Sandbox: `code_sandbox/js-array-methods/copywithin-2-0.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.copyWithin(2, 0);
```

<img alt="js-array-methods example 23 source" src="./code_sandbox/snaps/js-array-methods-23-code.png" />

<img alt="js-array-methods example 23 result" src="./code_sandbox/snaps/js-array-methods-23-result.png" />

- [x] **Outcome:** **["Banana","Orange","Banana","Orange"]**.

<a id="js-array-methods-example-24"></a>

### **Example 24: copyWithin(2, 0, 2)**

- [x] Copy to index **2** the slice **[0, 2)** (end not included).

Sandbox: `code_sandbox/js-array-methods/copywithin-2-0-2.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango", "Kiwi"];
fruits.copyWithin(2, 0, 2);
```

<img alt="js-array-methods example 24 source" src="./code_sandbox/snaps/js-array-methods-24-code.png" />

<img alt="js-array-methods example 24 result" src="./code_sandbox/snaps/js-array-methods-24-result.png" />

- [x] **Outcome:** **["Banana","Orange","Banana","Orange","Kiwi"]**.

<a id="js-array-methods-example-25"></a>

### **Example 25: [[1,2],[3,4],[5,6]].flat()**

- [x] ES2019 `flat()` concatenates **one level** of sub-arrays by default.

Sandbox: `code_sandbox/js-array-methods/flat.html`

```javascript
const myArr = [[1,2],[3,4],[5,6]];
const newArr = myArr.flat();
```

<img alt="js-array-methods example 25 source" src="./code_sandbox/snaps/js-array-methods-25-code.png" />

<img alt="js-array-methods example 25 result" src="./code_sandbox/snaps/js-array-methods-25-result.png" />

- [x] **Outcome:** **[1,2,3,4,5,6]**.

<a id="js-array-methods-example-26"></a>

### **Example 26: flatMap(x => [x, x * 10])**

- [x] `flatMap` maps, then flattens **one** level.

Sandbox: `code_sandbox/js-array-methods/flatmap.html`

```javascript
const myArr = [1, 2, 3, 4, 5, 6];
const newArr = myArr.flatMap(x => [x, x * 10]);
```

<img alt="js-array-methods example 26 source" src="./code_sandbox/snaps/js-array-methods-26-code.png" />

<img alt="js-array-methods example 26 result" src="./code_sandbox/snaps/js-array-methods-26-result.png" />

- [x] **Outcome:** **[1,10,2,20,3,30,4,40,5,50,6,60]**.

<a id="js-array-methods-example-27"></a>

### **Example 27: splice(2, 0, "Lemon", "Kiwi")**

- [x] Start at **2**, delete **0**, insert Lemon and Kiwi. **Mutates**.

Sandbox: `code_sandbox/js-array-methods/splice-add.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(2, 0, "Lemon", "Kiwi");
```

<img alt="js-array-methods example 27 source" src="./code_sandbox/snaps/js-array-methods-27-code.png" />

<img alt="js-array-methods example 27 result" src="./code_sandbox/snaps/js-array-methods-27-result.png" />

- [x] **Outcome:** **["Banana","Orange","Lemon","Kiwi","Apple","Mango"]**.

<a id="js-array-methods-example-28"></a>

### **Example 28: splice(2, 2, "Lemon", "Kiwi")**

- [x] Delete **2** items at index 2, insert two new ones. Returns the **deleted** items.

Sandbox: `code_sandbox/js-array-methods/splice-replace.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let removed = fruits.splice(2, 2, "Lemon", "Kiwi");
```

<img alt="js-array-methods example 28 source" src="./code_sandbox/snaps/js-array-methods-28-code.png" />

<img alt="js-array-methods example 28 result" src="./code_sandbox/snaps/js-array-methods-28-result.png" />

- [x] **Outcome:** fruits **["Banana","Orange","Lemon","Kiwi"]**. removed **["Apple","Mango"]**.

<a id="js-array-methods-example-29"></a>

### **Example 29: splice(0, 1) — remove without holes**

- [x] Delete 1 at index 0. No insert. Cleaner than `delete`.

Sandbox: `code_sandbox/js-array-methods/splice-remove.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(0, 1);
```

<img alt="js-array-methods example 29 source" src="./code_sandbox/snaps/js-array-methods-29-code.png" />

<img alt="js-array-methods example 29 result" src="./code_sandbox/snaps/js-array-methods-29-result.png" />

- [x] **Outcome:** **["Orange","Apple","Mango"]**.

<a id="js-array-methods-example-30"></a>

### **Example 30: months.toSpliced(0, 1)**

- [x] ES2023 `toSpliced` returns a **new** array. Original stays.

Sandbox: `code_sandbox/js-array-methods/tospliced.html`

```javascript
const months = ["Jan", "Feb", "Mar", "Apr"];
const spliced = months.toSpliced(0, 1);
```

<img alt="js-array-methods example 30 source" src="./code_sandbox/snaps/js-array-methods-30-code.png" />

<img alt="js-array-methods example 30 result" src="./code_sandbox/snaps/js-array-methods-30-result.png" />

- [x] **Outcome:** spliced **["Feb","Mar","Apr"]**. months still **["Jan","Feb","Mar","Apr"]**.

<a id="js-array-methods-example-31"></a>

### **Example 31: slice(1)**

- [x] `slice(1)` copies from index **1** to the end. Source is unchanged.

Sandbox: `code_sandbox/js-array-methods/slice-1.html`

```javascript
const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruits.slice(1);
```

<img alt="js-array-methods example 31 source" src="./code_sandbox/snaps/js-array-methods-31-code.png" />

<img alt="js-array-methods example 31 result" src="./code_sandbox/snaps/js-array-methods-31-result.png" />

- [x] **Outcome:** **["Orange","Lemon","Apple","Mango"]**. fruits unchanged.

<a id="js-array-methods-example-32"></a>

### **Example 32: slice(3)**

- [x] `slice(3)` starts at **Apple**.

Sandbox: `code_sandbox/js-array-methods/slice-3.html`

```javascript
const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruits.slice(3);
```

<img alt="js-array-methods example 32 source" src="./code_sandbox/snaps/js-array-methods-32-code.png" />

<img alt="js-array-methods example 32 result" src="./code_sandbox/snaps/js-array-methods-32-result.png" />

- [x] **Outcome:** **["Apple","Mango"]**.

<a id="js-array-methods-example-33"></a>

### **Example 33: slice(1, 3)**

- [x] `slice(start, end)` copies **up to but not including** end.

Sandbox: `code_sandbox/js-array-methods/slice-1-3.html`

```javascript
const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruits.slice(1, 3);
```

<img alt="js-array-methods example 33 source" src="./code_sandbox/snaps/js-array-methods-33-code.png" />

<img alt="js-array-methods example 33 result" src="./code_sandbox/snaps/js-array-methods-33-result.png" />

- [x] **Outcome:** **["Orange","Lemon"]**.

<a id="js-array-methods-example-34"></a>

### **Example 34: slice(2)**

- [x] Omitting end still means **the rest** of the array.

Sandbox: `code_sandbox/js-array-methods/slice-2.html`

```javascript
const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruits.slice(2);
```

<img alt="js-array-methods example 34 source" src="./code_sandbox/snaps/js-array-methods-34-code.png" />

<img alt="js-array-methods example 34 result" src="./code_sandbox/snaps/js-array-methods-34-result.png" />

- [x] **Outcome:** **["Lemon","Apple","Mango"]**.

<a id="js-array-methods-example-35"></a>

### **Example 35: fruits.toString() for display**

- [x] When a primitive is needed, JS calls `toString` on the array.

Sandbox: `code_sandbox/js-array-methods/auto-tostring.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let text = fruits.toString();
```

<img alt="js-array-methods example 35 source" src="./code_sandbox/snaps/js-array-methods-35-code.png" />

<img alt="js-array-methods example 35 result" src="./code_sandbox/snaps/js-array-methods-35-result.png" />

- [x] **Outcome:** **Banana,Orange,Apple,Mango**.

<a id="js-array-methods-example-36"></a>

### **Example 36: String(fruits) without calling toString**

- [x] The matching Tryit assigns the array into HTML; coercion is the same.

Sandbox: `code_sandbox/js-array-methods/auto-string-coercion.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let text = String(fruits);
```

<img alt="js-array-methods example 36 source" src="./code_sandbox/snaps/js-array-methods-36-code.png" />

<img alt="js-array-methods example 36 result" src="./code_sandbox/snaps/js-array-methods-36-result.png" />

- [x] **Outcome:** **Banana,Orange,Apple,Mango** — same as `toString()`.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-array-methods/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is fruits.length on four fruits?

<details>
<summary>Answer</summary>

- [x] **4**. Setting `length = 2` leaves **Banana, Orange**.

</details>

### Question 2: at(2) vs fruits[2]?

<details>
<summary>Answer</summary>

- [x] Both **Apple** for this list.

</details>

### Question 3: What is fruits[-1] vs fruits.at(-1)?

<details>
<summary>Answer</summary>

- [x] `[-1]` is **undefined** (property "-1").
- [x] `at(-1)` is **Mango**.

</details>

### Question 4: What does join(" * ") print?

<details>
<summary>Answer</summary>

- [x] **Banana * Orange * Apple * Mango**.

</details>

### Question 5: What does pop return?

<details>
<summary>Answer</summary>

- [x] **Mango**, leaving three fruits.

</details>

### Question 6: What does push("Kiwi") return?

<details>
<summary>Answer</summary>

- [x] The new length **5**.

</details>

### Question 7: What does shift return?

<details>
<summary>Answer</summary>

- [x] **Banana**.

</details>

### Question 8: What does unshift("Lemon") return?

<details>
<summary>Answer</summary>

- [x] The new length **5**.

</details>

### Question 9: What does delete fruits[0] do?

<details>
<summary>Answer</summary>

- [x] A hole: JSON **null** at [0], length still **4**.

</details>

### Question 10: Does concat change the originals?

<details>
<summary>Answer</summary>

- [x] **No.** It returns a new array.

</details>

### Question 11: copyWithin(2, 0) on four fruits?

<details>
<summary>Answer</summary>

- [x] **["Banana","Orange","Banana","Orange"]**.

</details>

### Question 12: slice(1, 3) on Banana, Orange, Lemon, Apple, Mango?

<details>
<summary>Answer</summary>

- [x] **["Orange","Lemon"]**.

</details>

### Question 13: toSpliced(0, 1) on months?

<details>
<summary>Answer</summary>

- [x] **["Feb","Mar","Apr"]**. Original months stay.

</details>

### Question 14: flatMap(x => [x, x*10]) on 1..6?

<details>
<summary>Answer</summary>

- [x] **[1,10,2,20,3,30,4,40,5,50,6,60]**.

</details>


</details>

## Summary

Mutating methods change the same array; slicing, concatenating, flattening, and toSpliced give you a new one. delete is not a real remove. Remember the four slice argument sets and that at() is how you index from the end.

## References

- [JS Array Methods (W3Schools)](https://www.w3schools.com/js/js_array_methods.asp)
- [MDN: Array.prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [MDN: Array.prototype.at](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at)
- [MDN: Array.prototype.splice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)

</details>
