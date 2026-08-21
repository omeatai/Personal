# JS Array Iterations

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Iteration methods walk every item. for...of yields values (recommended). for...in yields indexes and is meant for objects. forEach, map, filter, every, and some take a callback with value, index, and array — extra parameters can be dropped. map/filter return new arrays; reduce/reduceRight fold to one value (optional initial). Array.from builds from an iterable or from a mapped list. keys and entries are iterators. with() updates one index on a copy. Spread expands; rest collects.

This section has **29** examples:

- [x] **Example 1:** for...of over car values [View](#js-array-iterations-example-01)
- [x] **Example 2:** for...in over indexes (not recommended) [View](#js-array-iterations-example-02)
- [x] **Example 3:** for...in with cars[x] [View](#js-array-iterations-example-03)
- [x] **Example 4:** forEach with value, index, array [View](#js-array-iterations-example-04)
- [x] **Example 5:** forEach with value only [View](#js-array-iterations-example-05)
- [x] **Example 6:** map value * 2 (three-arg callback) [View](#js-array-iterations-example-06)
- [x] **Example 7:** map value * 2 (value only) [View](#js-array-iterations-example-07)
- [x] **Example 8:** flatMap(x => [x, x * 10]) [View](#js-array-iterations-example-08)
- [x] **Example 9:** filter values > 18 (three-arg callback) [View](#js-array-iterations-example-09)
- [x] **Example 10:** filter values > 18 (value only) [View](#js-array-iterations-example-10)
- [x] **Example 11:** reduce sum (four-arg callback) [View](#js-array-iterations-example-11)
- [x] **Example 12:** reduce sum (total, value) [View](#js-array-iterations-example-12)
- [x] **Example 13:** reduce sum with initial 100 [View](#js-array-iterations-example-13)
- [x] **Example 14:** reduceRight sum (four-arg callback) [View](#js-array-iterations-example-14)
- [x] **Example 15:** reduceRight sum (total, value) [View](#js-array-iterations-example-15)
- [x] **Example 16:** every value > 18 (three-arg callback) [View](#js-array-iterations-example-16)
- [x] **Example 17:** every value > 18 (value only) [View](#js-array-iterations-example-17)
- [x] **Example 18:** some value > 18 [View](#js-array-iterations-example-18)
- [x] **Example 19:** Array.from("ABCDEFG") [View](#js-array-iterations-example-19)
- [x] **Example 20:** Array.from(array, x => x * 2) [View](#js-array-iterations-example-20)
- [x] **Example 21:** fruits.keys() iterator [View](#js-array-iterations-example-21)
- [x] **Example 22:** fruits.entries() key/value pairs [View](#js-array-iterations-example-22)
- [x] **Example 23:** months.with(2, "March") [View](#js-array-iterations-example-23)
- [x] **Example 24:** Spread join two arrays [View](#js-array-iterations-example-24)
- [x] **Example 25:** Spread four quarter arrays [View](#js-array-iterations-example-25)
- [x] **Example 26:** Spread copy an array [View](#js-array-iterations-example-26)
- [x] **Example 27:** Math.min / Math.max with spread [View](#js-array-iterations-example-27)
- [x] **Example 28:** [a, ...rest] = arr1 [View](#js-array-iterations-example-28)
- [x] **Example 29:** [a, b, ...rest] = arr1 [View](#js-array-iterations-example-29)

## Detailed Explanation

- [x] `for...of` is for **values**. `for...in` is for **keys** — skip it on arrays.
- [x] `map` / `filter` / `flatMap` return **new** arrays. `forEach` returns **undefined**.
- [x] `reduce` is left-to-right; `reduceRight` is right-to-left. An initial value is optional.
- [x] `every` needs **all** matches; `some` needs **any**.
- [x] `Array.from` copies iterables; optional map runs per element.
- [x] `...` spread expands; `...` rest in destructuring **collects** leftovers.
- [x] ES2023 `with(i, value)` updates one index on a **copy**.

<a id="js-array-iterations-example-01"></a>

### **Example 1: for...of over car values**

- [x] `for...of` yields **values**. Recommended for arrays.

Sandbox: `code_sandbox/js-array-iterations/for-of.html`

```javascript
const cars = ["BMW", "Volvo", "Mini"];
let text = "";
for (let x of cars) {
  text += x + ",";
}
```

![js-array-iterations example 1 source](../code_sandbox/snaps/js-array-iterations-01-code.png)

![js-array-iterations example 1 result](../code_sandbox/snaps/js-array-iterations-01-result.png)

- [x] **Outcome:** **BMW,Volvo,Mini,**

<a id="js-array-iterations-example-02"></a>

### **Example 2: for...in over indexes (not recommended)**

- [x] `for...in` yields **keys** (indexes as strings). Built for **objects**, not arrays.

Sandbox: `code_sandbox/js-array-iterations/for-in-indexes.html`

```javascript
const cars = ["BMW", "Volvo", "Mini"];
let text = "";
for (let x in cars) {
  text += x + ",";
}
```

![js-array-iterations example 2 source](../code_sandbox/snaps/js-array-iterations-02-code.png)

![js-array-iterations example 2 result](../code_sandbox/snaps/js-array-iterations-02-result.png)

- [x] **Outcome:** **0,1,2,**

<a id="js-array-iterations-example-03"></a>

### **Example 3: for...in with cars[x]**

- [x] You can read `cars[x]`, but `for...in` is still a **bad idea** for arrays.

Sandbox: `code_sandbox/js-array-iterations/for-in-values.html`

```javascript
const cars = ["BMW", "Volvo", "Mini"];
let text = "";
for (let x in cars) {
  text += cars[x] + "";
}
```

![js-array-iterations example 3 source](../code_sandbox/snaps/js-array-iterations-03-code.png)

![js-array-iterations example 3 result](../code_sandbox/snaps/js-array-iterations-03-result.png)

- [x] **Outcome:** **BMWVolvoMini** (the Tryit concatenates with an empty separator).

<a id="js-array-iterations-example-04"></a>

### **Example 4: forEach with value, index, array**

- [x] Callback receives **value, index, array**. This demo uses value only in the body.

Sandbox: `code_sandbox/js-array-iterations/foreach-three-args.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let txt = "";
numbers.forEach(myFunction);
function myFunction(value, index, array) {
  txt += value + " ";
}
```

![js-array-iterations example 4 source](../code_sandbox/snaps/js-array-iterations-04-code.png)

![js-array-iterations example 4 result](../code_sandbox/snaps/js-array-iterations-04-result.png)

- [x] **Outcome:** **45 4 9 16 25** (trailing space).

<a id="js-array-iterations-example-05"></a>

### **Example 5: forEach with value only**

- [x] Unused index/array parameters may be **omitted**.

Sandbox: `code_sandbox/js-array-iterations/foreach-value-only.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let txt = "";
numbers.forEach(myFunction);
function myFunction(value) {
  txt += value + " ";
}
```

![js-array-iterations example 5 source](../code_sandbox/snaps/js-array-iterations-05-code.png)

![js-array-iterations example 5 result](../code_sandbox/snaps/js-array-iterations-05-result.png)

- [x] **Outcome:** **45 4 9 16 25** (trailing space).

<a id="js-array-iterations-example-06"></a>

### **Example 6: map value * 2 (three-arg callback)**

- [x] `map` returns a **new** array. Original stays.

Sandbox: `code_sandbox/js-array-iterations/map-three-args.html`

```javascript
const numbers1 = [45, 4, 9, 16, 25];
const numbers2 = numbers1.map(myFunction);
function myFunction(value, index, array) {
  return value * 2;
}
```

![js-array-iterations example 6 source](../code_sandbox/snaps/js-array-iterations-06-code.png)

![js-array-iterations example 6 result](../code_sandbox/snaps/js-array-iterations-06-result.png)

- [x] **Outcome:** New **[90,8,18,32,50]**. Original unchanged.

<a id="js-array-iterations-example-07"></a>

### **Example 7: map value * 2 (value only)**

- [x] Same result with a **one-parameter** callback.

Sandbox: `code_sandbox/js-array-iterations/map-value-only.html`

```javascript
const numbers1 = [45, 4, 9, 16, 25];
const numbers2 = numbers1.map(myFunction);
function myFunction(value) {
  return value * 2;
}
```

![js-array-iterations example 7 source](../code_sandbox/snaps/js-array-iterations-07-code.png)

![js-array-iterations example 7 result](../code_sandbox/snaps/js-array-iterations-07-result.png)

- [x] **Outcome:** **[90,8,18,32,50]**.

<a id="js-array-iterations-example-08"></a>

### **Example 8: flatMap(x => [x, x * 10])**

- [x] Map then flatten one level — same Tryit idea as the methods page.

Sandbox: `code_sandbox/js-array-iterations/flatmap.html`

```javascript
const myArr = [1, 2, 3, 4, 5, 6];
const newArr = myArr.flatMap(x => [x, x * 10]);
```

![js-array-iterations example 8 source](../code_sandbox/snaps/js-array-iterations-08-code.png)

![js-array-iterations example 8 result](../code_sandbox/snaps/js-array-iterations-08-result.png)

- [x] **Outcome:** **[1,10,2,20,3,30,4,40,5,50,6,60]**.

<a id="js-array-iterations-example-09"></a>

### **Example 9: filter values > 18 (three-arg callback)**

- [x] `filter` keeps elements that pass the test. **New** array.

Sandbox: `code_sandbox/js-array-iterations/filter-three-args.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
const over18 = numbers.filter(myFunction);
function myFunction(value, index, array) {
  return value > 18;
}
```

![js-array-iterations example 9 source](../code_sandbox/snaps/js-array-iterations-09-code.png)

![js-array-iterations example 9 result](../code_sandbox/snaps/js-array-iterations-09-result.png)

- [x] **Outcome:** **[45,25]**.

<a id="js-array-iterations-example-10"></a>

### **Example 10: filter values > 18 (value only)**

- [x] Same filter with unused parameters dropped.

Sandbox: `code_sandbox/js-array-iterations/filter-value-only.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
const over18 = numbers.filter(myFunction);
function myFunction(value) {
  return value > 18;
}
```

![js-array-iterations example 10 source](../code_sandbox/snaps/js-array-iterations-10-code.png)

![js-array-iterations example 10 result](../code_sandbox/snaps/js-array-iterations-10-result.png)

- [x] **Outcome:** **[45,25]**.

<a id="js-array-iterations-example-11"></a>

### **Example 11: reduce sum (four-arg callback)**

- [x] `reduce` folds left-to-right into **one value**. Does not change the array.
- [x] Args: total, value, index, array.

Sandbox: `code_sandbox/js-array-iterations/reduce-four-args.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let sum = numbers.reduce(myFunction);
function myFunction(total, value, index, array) {
  return total + value;
}
```

![js-array-iterations example 11 source](../code_sandbox/snaps/js-array-iterations-11-code.png)

![js-array-iterations example 11 result](../code_sandbox/snaps/js-array-iterations-11-result.png)

- [x] **Outcome:** **99** (45+4+9+16+25).

<a id="js-array-iterations-example-12"></a>

### **Example 12: reduce sum (total, value)**

- [x] Same sum without unused parameters.

Sandbox: `code_sandbox/js-array-iterations/reduce-two-args.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let sum = numbers.reduce(myFunction);
function myFunction(total, value) {
  return total + value;
}
```

![js-array-iterations example 12 source](../code_sandbox/snaps/js-array-iterations-12-code.png)

![js-array-iterations example 12 result](../code_sandbox/snaps/js-array-iterations-12-result.png)

- [x] **Outcome:** **99**.

<a id="js-array-iterations-example-13"></a>

### **Example 13: reduce sum with initial 100**

- [x] The second argument to `reduce` is the **starting total**.

Sandbox: `code_sandbox/js-array-iterations/reduce-initial-100.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let sum = numbers.reduce(myFunction, 100);
function myFunction(total, value) {
  return total + value;
}
```

![js-array-iterations example 13 source](../code_sandbox/snaps/js-array-iterations-13-code.png)

![js-array-iterations example 13 result](../code_sandbox/snaps/js-array-iterations-13-result.png)

- [x] **Outcome:** **199**.

<a id="js-array-iterations-example-14"></a>

### **Example 14: reduceRight sum (four-arg callback)**

- [x] `reduceRight` folds **right-to-left**. Same sum for addition.

Sandbox: `code_sandbox/js-array-iterations/reduceright-four-args.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let sum = numbers.reduceRight(myFunction);
function myFunction(total, value, index, array) {
  return total + value;
}
```

![js-array-iterations example 14 source](../code_sandbox/snaps/js-array-iterations-14-code.png)

![js-array-iterations example 14 result](../code_sandbox/snaps/js-array-iterations-14-result.png)

- [x] **Outcome:** **99**.

<a id="js-array-iterations-example-15"></a>

### **Example 15: reduceRight sum (total, value)**

- [x] Same right-fold with a shorter callback.

Sandbox: `code_sandbox/js-array-iterations/reduceright-two-args.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let sum = numbers.reduceRight(myFunction);
function myFunction(total, value) {
  return total + value;
}
```

![js-array-iterations example 15 source](../code_sandbox/snaps/js-array-iterations-15-code.png)

![js-array-iterations example 15 result](../code_sandbox/snaps/js-array-iterations-15-result.png)

- [x] **Outcome:** **99**.

<a id="js-array-iterations-example-16"></a>

### **Example 16: every value > 18 (three-arg callback)**

- [x] `every` is **true** only if **all** elements pass.

Sandbox: `code_sandbox/js-array-iterations/every-three-args.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let allOver18 = numbers.every(myFunction);
function myFunction(value, index, array) {
  return value > 18;
}
```

![js-array-iterations example 16 source](../code_sandbox/snaps/js-array-iterations-16-code.png)

![js-array-iterations example 16 result](../code_sandbox/snaps/js-array-iterations-16-result.png)

- [x] **Outcome:** **false** (4, 9, and 16 fail).

<a id="js-array-iterations-example-17"></a>

### **Example 17: every value > 18 (value only)**

- [x] Same test with a one-parameter callback.

Sandbox: `code_sandbox/js-array-iterations/every-value-only.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let allOver18 = numbers.every(myFunction);
function myFunction(value) {
  return value > 18;
}
```

![js-array-iterations example 17 source](../code_sandbox/snaps/js-array-iterations-17-code.png)

![js-array-iterations example 17 result](../code_sandbox/snaps/js-array-iterations-17-result.png)

- [x] **Outcome:** **false**.

<a id="js-array-iterations-example-18"></a>

### **Example 18: some value > 18**

- [x] `some` is **true** if **any** element passes.

Sandbox: `code_sandbox/js-array-iterations/some-three-args.html`

```javascript
const numbers = [45, 4, 9, 16, 25];
let someOver18 = numbers.some(myFunction);
function myFunction(value, index, array) {
  return value > 18;
}
```

![js-array-iterations example 18 source](../code_sandbox/snaps/js-array-iterations-18-code.png)

![js-array-iterations example 18 result](../code_sandbox/snaps/js-array-iterations-18-result.png)

- [x] **Outcome:** **true** (45 and 25 pass).

<a id="js-array-iterations-example-19"></a>

### **Example 19: Array.from("ABCDEFG")**

- [x] `Array.from` builds an array from an **iterable** (here a string).

Sandbox: `code_sandbox/js-array-iterations/from-string.html`

```javascript
let text = "ABCDEFG";
const letters = Array.from(text);
```

![js-array-iterations example 19 source](../code_sandbox/snaps/js-array-iterations-19-code.png)

![js-array-iterations example 19 result](../code_sandbox/snaps/js-array-iterations-19-result.png)

- [x] **Outcome:** **["A","B","C","D","E","F","G"]**.

<a id="js-array-iterations-example-20"></a>

### **Example 20: Array.from(array, x => x * 2)**

- [x] Optional map function runs on each new element.

Sandbox: `code_sandbox/js-array-iterations/from-map.html`

```javascript
const myNumbers = [1,2,3,4];
const myArr = Array.from(myNumbers, (x) => x * 2);
```

![js-array-iterations example 20 source](../code_sandbox/snaps/js-array-iterations-20-code.png)

![js-array-iterations example 20 result](../code_sandbox/snaps/js-array-iterations-20-result.png)

- [x] **Outcome:** **[2,4,6,8]**.

<a id="js-array-iterations-example-21"></a>

### **Example 21: fruits.keys() iterator**

- [x] `keys()` is an **iterator** of indexes.

Sandbox: `code_sandbox/js-array-iterations/keys.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
const keys = fruits.keys();
let text = "";
for (let x of keys) {
  text += x + " ";
}
```

![js-array-iterations example 21 source](../code_sandbox/snaps/js-array-iterations-21-code.png)

![js-array-iterations example 21 result](../code_sandbox/snaps/js-array-iterations-21-result.png)

- [x] **Outcome:** **0 1 2 3** (trailing space).

<a id="js-array-iterations-example-22"></a>

### **Example 22: fruits.entries() key/value pairs**

- [x] `entries()` yields **[index, value]** pairs.

Sandbox: `code_sandbox/js-array-iterations/entries.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
const f = fruits.entries();
let text = "";
for (let x of f) {
  text += String(x);
}
```

![js-array-iterations example 22 source](../code_sandbox/snaps/js-array-iterations-22-code.png)

![js-array-iterations example 22 result](../code_sandbox/snaps/js-array-iterations-22-result.png)

- [x] **Outcome:** **0,Banana1,Orange2,Apple3,Mango** (each pair stringifies as `index,value`).

<a id="js-array-iterations-example-23"></a>

### **Example 23: months.with(2, "March")**

- [x] ES2023 `with` returns a **new** array with one index updated.

Sandbox: `code_sandbox/js-array-iterations/with-method.html`

```javascript
const months = ["Januar", "Februar", "Mar", "April"];
const myMonths = months.with(2, "March");
```

![js-array-iterations example 23 source](../code_sandbox/snaps/js-array-iterations-23-code.png)

![js-array-iterations example 23 result](../code_sandbox/snaps/js-array-iterations-23-result.png)

- [x] **Outcome:** myMonths **["Januar","Februar","March","April"]**. Original still has **"Mar"**.

<a id="js-array-iterations-example-24"></a>

### **Example 24: Spread join two arrays**

- [x] `...` expands an array into **elements**.

Sandbox: `code_sandbox/js-array-iterations/spread-join-two.html`

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const arr3 = [...arr1, ...arr2];
```

![js-array-iterations example 24 source](../code_sandbox/snaps/js-array-iterations-24-code.png)

![js-array-iterations example 24 result](../code_sandbox/snaps/js-array-iterations-24-result.png)

- [x] **Outcome:** **[1,2,3,4,5,6]**.

<a id="js-array-iterations-example-25"></a>

### **Example 25: Spread four quarter arrays**

- [x] The page uses **Des** (not Dec) in q4.

Sandbox: `code_sandbox/js-array-iterations/spread-year.html`

```javascript
const q1 = ["Jan", "Feb", "Mar"];
const q2 = ["Apr", "May", "Jun"];
const q3 = ["Jul", "Aug", "Sep"];
const q4 = ["Oct", "Nov", "Des"];
const year = [...q1, ...q2, ...q3, ...q4];
```

![js-array-iterations example 25 source](../code_sandbox/snaps/js-array-iterations-25-code.png)

![js-array-iterations example 25 result](../code_sandbox/snaps/js-array-iterations-25-result.png)

- [x] **Outcome:** **["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Des"]**.

<a id="js-array-iterations-example-26"></a>

### **Example 26: Spread copy an array**

- [x] `[...arr1]` is a **shallow copy**.

Sandbox: `code_sandbox/js-array-iterations/spread-copy.html`

```javascript
const arr1 = [1, 2, 3];
const arr2 = [...arr1];
```

![js-array-iterations example 26 source](../code_sandbox/snaps/js-array-iterations-26-code.png)

![js-array-iterations example 26 result](../code_sandbox/snaps/js-array-iterations-26-result.png)

- [x] **Outcome:** **[1,2,3]**. `arr1 === arr2` is **false** (different array).

<a id="js-array-iterations-example-27"></a>

### **Example 27: Math.min / Math.max with spread**

- [x] Spread turns an array into **argument list**.

Sandbox: `code_sandbox/js-array-iterations/spread-math-min-max.html`

```javascript
const numbers = [23, 55, 21, 87, 56];
let minValue = Math.min(...numbers);
let maxValue = Math.max(...numbers);
```

![js-array-iterations example 27 source](../code_sandbox/snaps/js-array-iterations-27-code.png)

![js-array-iterations example 27 result](../code_sandbox/snaps/js-array-iterations-27-result.png)

- [x] **Outcome:** min **21**, max **87**.

<a id="js-array-iterations-example-28"></a>

### **Example 28: [a, ...rest] = arr1**

- [x] Rest **collects leftover** elements after destructuring.

Sandbox: `code_sandbox/js-array-iterations/rest-a.html`

```javascript
let a, rest;
const arr1 = [1,2,3,4,5,6,7,8];
[a, ...rest] = arr1;
```

![js-array-iterations example 28 source](../code_sandbox/snaps/js-array-iterations-28-code.png)

![js-array-iterations example 28 result](../code_sandbox/snaps/js-array-iterations-28-result.png)

- [x] **Outcome:** a **1**. rest **[2,3,4,5,6,7,8]**.

<a id="js-array-iterations-example-29"></a>

### **Example 29: [a, b, ...rest] = arr1**

- [x] Two named bindings, then the rest.

Sandbox: `code_sandbox/js-array-iterations/rest-a-b.html`

```javascript
let a, b, rest;
const arr1 = [1,2,3,4,5,6,7,8];
[a, b, ...rest] = arr1;
```

![js-array-iterations example 29 source](../code_sandbox/snaps/js-array-iterations-29-code.png)

![js-array-iterations example 29 result](../code_sandbox/snaps/js-array-iterations-29-result.png)

- [x] **Outcome:** a **1**, b **2**, rest **[3,4,5,6,7,8]**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-array-iterations/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: for...of on BMW, Volvo, Mini?

<details>
<summary>Answer</summary>

- [x] **BMW,Volvo,Mini,**

</details>

### Question 2: for...in on the same array?

<details>
<summary>Answer</summary>

- [x] Indexes **0,1,2,** — not the names.

</details>

### Question 3: map * 2 on [45,4,9,16,25]?

<details>
<summary>Answer</summary>

- [x] **[90,8,18,32,50]**.

</details>

### Question 4: filter > 18?

<details>
<summary>Answer</summary>

- [x] **[45,25]**.

</details>

### Question 5: reduce sum? With initial 100?

<details>
<summary>Answer</summary>

- [x] **99**. With 100: **199**.

</details>

### Question 6: every > 18? some > 18?

<details>
<summary>Answer</summary>

- [x] every **false**. some **true**.

</details>

### Question 7: Array.from("ABCDEFG")?

<details>
<summary>Answer</summary>

- [x] **["A","B","C","D","E","F","G"]**.

</details>

### Question 8: Array.from([1,2,3,4], x => x*2)?

<details>
<summary>Answer</summary>

- [x] **[2,4,6,8]**.

</details>

### Question 9: keys() loop?

<details>
<summary>Answer</summary>

- [x] **0 1 2 3**.

</details>

### Question 10: entries() stringified in a loop?

<details>
<summary>Answer</summary>

- [x] **0,Banana1,Orange2,Apple3,Mango**.

</details>

### Question 11: with(2, "March") on Januar, Februar, Mar, April?

<details>
<summary>Answer</summary>

- [x] Mar becomes **March** on the copy.

</details>

### Question 12: Spread [1,2,3] and [4,5,6]?

<details>
<summary>Answer</summary>

- [x] **[1,2,3,4,5,6]**.

</details>

### Question 13: Math.min(...[23,55,21,87,56])?

<details>
<summary>Answer</summary>

- [x] **21**. max is **87**.

</details>

### Question 14: [a, ...rest] on 1..8?

<details>
<summary>Answer</summary>

- [x] a **1**, rest **[2,3,4,5,6,7,8]**.

</details>

### Question 15: [a, b, ...rest]?

<details>
<summary>Answer</summary>

- [x] a **1**, b **2**, rest **[3,4,5,6,7,8]**.

</details>


</details>

## Summary

Prefer for...of and the dedicated methods. map and filter copy; reduce folds; every/some test. from, keys, entries, with, spread, and rest round out iteration without a C-style index if you do not need one.

## References

- [JS Array Iterations (W3Schools)](https://www.w3schools.com/js/js_array_iteration.asp)
- [MDN: Array iteration methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods)
- [MDN: Array.prototype.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
- [MDN: Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
