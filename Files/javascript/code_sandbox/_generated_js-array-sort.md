<details>
  <summary>JS Array Sort</summary>

## Introduction

sort and reverse mutate. toSorted and toReversed (ES2023) return new arrays. Default sort is alphabetic, which orders numbers as strings (1, 10, 100, 25, 40, 5). A compare function return a-b for numeric ascending and b-a for descending. Random compare is a biased shuffle; Fisher–Yates is the fair one. Min and max can come from a sorted end, Math.min.apply, or a homemade loop. Object arrays sort by a property. After ES2019, sort is stable.

This section has **20** examples:

- [x] **Example 1:** fruits.sort() — alphabetic [View](#js-array-sort-example-01)
- [x] **Example 2:** fruits.reverse() [View](#js-array-sort-example-02)
- [x] **Example 3:** sort then reverse — descending alpha [View](#js-array-sort-example-03)
- [x] **Example 4:** months.toSorted() [View](#js-array-sort-example-04)
- [x] **Example 5:** months.toReversed() [View](#js-array-sort-example-05)
- [x] **Example 6:** sort(function(a, b){return a - b}) [View](#js-array-sort-example-06)
- [x] **Example 7:** sort(function(a, b){return b - a}) [View](#js-array-sort-example-07)
- [x] **Example 8:** Default sort vs numeric sort (the button demo) [View](#js-array-sort-example-08)
- [x] **Example 9:** sort(function(){return 0.5 - Math.random()}) [View](#js-array-sort-example-09)
- [x] **Example 10:** Fisher–Yates shuffle [View](#js-array-sort-example-10)
- [x] **Example 11:** Lowest / highest after ascending sort [View](#js-array-sort-example-11)
- [x] **Example 12:** Highest / lowest after descending sort [View](#js-array-sort-example-12)
- [x] **Example 13:** Math.min.apply(null, arr) [View](#js-array-sort-example-13)
- [x] **Example 14:** Math.max.apply(null, arr) [View](#js-array-sort-example-14)
- [x] **Example 15:** Home-made myArrayMin [View](#js-array-sort-example-15)
- [x] **Example 16:** Home-made myArrayMax [View](#js-array-sort-example-16)
- [x] **Example 17:** Array of car objects [View](#js-array-sort-example-17)
- [x] **Example 18:** Sort cars by year [View](#js-array-sort-example-18)
- [x] **Example 19:** Sort cars by type string [View](#js-array-sort-example-19)
- [x] **Example 20:** Stable sort by price (ES2019) [View](#js-array-sort-example-20)

## Detailed Explanation

- [x] Default `sort` is **string** order and **mutates**.
- [x] `toSorted` / `toReversed` keep the original (ES2023).
- [x] Numeric sort needs `function(a,b){return a-b}` (or `b-a`).
- [x] Random `0.5 - Math.random()` is **biased**; use **Fisher–Yates**.
- [x] Min/max: sorted ends, `Math.min.apply`, or a loop from `Infinity`.
- [x] Object sort compares a **property**. ES2019 `sort` is **stable**.

<a id="js-array-sort-example-01"></a>

### **Example 1: fruits.sort() — alphabetic**

- [x] Default `sort` compares **as strings** and **mutates** the array.

Sandbox: `code_sandbox/js-array-sort/sort-alpha.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.sort();
```

<img alt="js-array-sort example 1 source" src="./code_sandbox/snaps/js-array-sort-01-code.png" />

<img alt="js-array-sort example 1 result" src="./code_sandbox/snaps/js-array-sort-01-result.png" />

- [x] **Outcome:** **["Apple","Banana","Mango","Orange"]**.

<a id="js-array-sort-example-02"></a>

### **Example 2: fruits.reverse()**

- [x] `reverse` flips **in place** (no sort).

Sandbox: `code_sandbox/js-array-sort/reverse.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.reverse();
```

<img alt="js-array-sort example 2 source" src="./code_sandbox/snaps/js-array-sort-02-code.png" />

<img alt="js-array-sort example 2 result" src="./code_sandbox/snaps/js-array-sort-02-result.png" />

- [x] **Outcome:** **["Mango","Apple","Orange","Banana"]**.

<a id="js-array-sort-example-03"></a>

### **Example 3: sort then reverse — descending alpha**

- [x] Sort first, then reverse, for **Z→A** strings.

Sandbox: `code_sandbox/js-array-sort/sort-then-reverse.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.sort();
fruits.reverse();
```

<img alt="js-array-sort example 3 source" src="./code_sandbox/snaps/js-array-sort-03-code.png" />

<img alt="js-array-sort example 3 result" src="./code_sandbox/snaps/js-array-sort-03-result.png" />

- [x] **Outcome:** **["Orange","Mango","Banana","Apple"]**.

<a id="js-array-sort-example-04"></a>

### **Example 4: months.toSorted()**

- [x] ES2023 `toSorted` returns a **new** sorted array.

Sandbox: `code_sandbox/js-array-sort/tosorted.html`

```javascript
const months = ["Jan", "Feb", "Mar", "Apr"];
const sorted = months.toSorted();
```

<img alt="js-array-sort example 4 source" src="./code_sandbox/snaps/js-array-sort-04-code.png" />

<img alt="js-array-sort example 4 result" src="./code_sandbox/snaps/js-array-sort-04-result.png" />

- [x] **Outcome:** sorted **["Apr","Feb","Jan","Mar"]**. months unchanged.

<a id="js-array-sort-example-05"></a>

### **Example 5: months.toReversed()**

- [x] `toReversed` returns a **new** reversed array.

Sandbox: `code_sandbox/js-array-sort/toreversed.html`

```javascript
const months = ["Jan", "Feb", "Mar", "Apr"];
const reversed = months.toReversed();
```

<img alt="js-array-sort example 5 source" src="./code_sandbox/snaps/js-array-sort-05-code.png" />

<img alt="js-array-sort example 5 result" src="./code_sandbox/snaps/js-array-sort-05-result.png" />

- [x] **Outcome:** reversed **["Apr","Mar","Feb","Jan"]**. months unchanged.

<a id="js-array-sort-example-06"></a>

### **Example 6: sort(function(a, b){return a - b})**

- [x] Compare function: negative → `a` first. `a - b` is **ascending** numbers.

Sandbox: `code_sandbox/js-array-sort/numeric-asc.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});
```

<img alt="js-array-sort example 6 source" src="./code_sandbox/snaps/js-array-sort-06-code.png" />

<img alt="js-array-sort example 6 result" src="./code_sandbox/snaps/js-array-sort-06-result.png" />

- [x] **Outcome:** **[1,5,10,25,40,100]**.

<a id="js-array-sort-example-07"></a>

### **Example 7: sort(function(a, b){return b - a})**

- [x] `b - a` is **descending** numbers.

Sandbox: `code_sandbox/js-array-sort/numeric-desc.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return b - a});
```

<img alt="js-array-sort example 7 source" src="./code_sandbox/snaps/js-array-sort-07-code.png" />

<img alt="js-array-sort example 7 result" src="./code_sandbox/snaps/js-array-sort-07-result.png" />

- [x] **Outcome:** **[100,40,25,10,5,1]**.

<a id="js-array-sort-example-08"></a>

### **Example 8: Default sort vs numeric sort (the button demo)**

- [x] The page’s two buttons run **string sort** vs **`a - b`**.
- [x] String sort of numbers is wrong: `"25"` vs `"100"` compares `"2"` and `"1"`.

Sandbox: `code_sandbox/js-array-sort/alpha-vs-numeric-buttons.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
const alpha = points.slice().sort();
const numeric = points.slice().sort(function(a, b){return a - b});
```

<img alt="js-array-sort example 8 source" src="./code_sandbox/snaps/js-array-sort-08-code.png" />

<img alt="js-array-sort example 8 result" src="./code_sandbox/snaps/js-array-sort-08-result.png" />

- [x] **Outcome:** Alphabetic **[1,10,100,25,40,5]**. Numeric **[1,5,10,25,40,100]**.

<a id="js-array-sort-example-09"></a>

### **Example 9: sort(function(){return 0.5 - Math.random()})**

- [x] A random compare **shuffles**, but it is **biased**. Still run it.

Sandbox: `code_sandbox/js-array-sort/random-sort.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
points.sort(function(){return 0.5 - Math.random()});
```

<img alt="js-array-sort example 9 source" src="./code_sandbox/snaps/js-array-sort-09-code.png" />

<img alt="js-array-sort example 9 result" src="./code_sandbox/snaps/js-array-sort-09-result.png" />

- [x] **Outcome:** The printed order is **random** (one permutation of 40, 100, 1, 5, 25, 10). Do not treat this shuffle as fair.

<a id="js-array-sort-example-10"></a>

### **Example 10: Fisher–Yates shuffle**

- [x] The unbiased shuffle: swap `i` with a random index `≤ i`, walking **backward**.

Sandbox: `code_sandbox/js-array-sort/fisher-yates.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
for (let i = points.length - 1; i > 0; i--) {
  let j = Math.floor(Math.random() * (i + 1));
  let k = points[i];
  points[i] = points[j];
  points[j] = k;
}
```

<img alt="js-array-sort example 10 source" src="./code_sandbox/snaps/js-array-sort-10-code.png" />

<img alt="js-array-sort example 10 result" src="./code_sandbox/snaps/js-array-sort-10-result.png" />

- [x] **Outcome:** The printed order is **random** but a **fair** permutation of the six numbers.

<a id="js-array-sort-example-11"></a>

### **Example 11: Lowest / highest after ascending sort**

- [x] After `a - b`, `[0]` is min and `[length-1]` is max. Sorting all of it is **overkill** for one extremum.

Sandbox: `code_sandbox/js-array-sort/min-max-via-sort-asc.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});
let lowest = points[0];
let highest = points[points.length - 1];
```

<img alt="js-array-sort example 11 source" src="./code_sandbox/snaps/js-array-sort-11-code.png" />

<img alt="js-array-sort example 11 result" src="./code_sandbox/snaps/js-array-sort-11-result.png" />

- [x] **Outcome:** Sorted **[1,5,10,25,40,100]**. lowest **1**, highest **100**.

<a id="js-array-sort-example-12"></a>

### **Example 12: Highest / lowest after descending sort**

- [x] After `b - a`, `[0]` is max.

Sandbox: `code_sandbox/js-array-sort/min-max-via-sort-desc.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return b - a});
let highest = points[0];
let lowest = points[points.length - 1];
```

<img alt="js-array-sort example 12 source" src="./code_sandbox/snaps/js-array-sort-12-code.png" />

<img alt="js-array-sort example 12 result" src="./code_sandbox/snaps/js-array-sort-12-result.png" />

- [x] **Outcome:** Sorted **[100,40,25,10,5,1]**. highest **100**, lowest **1**.

<a id="js-array-sort-example-13"></a>

### **Example 13: Math.min.apply(null, arr)**

- [x] `Math.min.apply(null, [1,2,3])` is `Math.min(1,2,3)`.

Sandbox: `code_sandbox/js-array-sort/math-min-apply.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
function myArrayMin(arr) {
  return Math.min.apply(null, arr);
}
let min = myArrayMin(points);
```

<img alt="js-array-sort example 13 source" src="./code_sandbox/snaps/js-array-sort-13-code.png" />

<img alt="js-array-sort example 13 result" src="./code_sandbox/snaps/js-array-sort-13-result.png" />

- [x] **Outcome:** **1**.

<a id="js-array-sort-example-14"></a>

### **Example 14: Math.max.apply(null, arr)**

- [x] Same idea for the **highest** value.

Sandbox: `code_sandbox/js-array-sort/math-max-apply.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
function myArrayMax(arr) {
  return Math.max.apply(null, arr);
}
let max = myArrayMax(points);
```

<img alt="js-array-sort example 14 source" src="./code_sandbox/snaps/js-array-sort-14-code.png" />

<img alt="js-array-sort example 14 result" src="./code_sandbox/snaps/js-array-sort-14-result.png" />

- [x] **Outcome:** **100**.

<a id="js-array-sort-example-15"></a>

### **Example 15: Home-made myArrayMin**

- [x] Loop, compare to `Infinity`. Fastest simple min.

Sandbox: `code_sandbox/js-array-sort/homemade-min.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
function myArrayMin(arr) {
  let len = arr.length;
  let min = Infinity;
  while (len--) {
    if (arr[len] < min) {
      min = arr[len];
    }
  }
  return min;
}
let min = myArrayMin(points);
```

<img alt="js-array-sort example 15 source" src="./code_sandbox/snaps/js-array-sort-15-code.png" />

<img alt="js-array-sort example 15 result" src="./code_sandbox/snaps/js-array-sort-15-result.png" />

- [x] **Outcome:** **1**.

<a id="js-array-sort-example-16"></a>

### **Example 16: Home-made myArrayMax**

- [x] Loop, compare to `-Infinity`.

Sandbox: `code_sandbox/js-array-sort/homemade-max.html`

```javascript
const points = [40, 100, 1, 5, 25, 10];
function myArrayMax(arr) {
  let len = arr.length;
  let max = -Infinity;
  while (len--) {
    if (arr[len] > max) {
      max = arr[len];
    }
  }
  return max;
}
let max = myArrayMax(points);
```

<img alt="js-array-sort example 16 source" src="./code_sandbox/snaps/js-array-sort-16-code.png" />

<img alt="js-array-sort example 16 result" src="./code_sandbox/snaps/js-array-sort-16-result.png" />

- [x] **Outcome:** **100**.

<a id="js-array-sort-example-17"></a>

### **Example 17: Array of car objects**

- [x] No Tryit for the unsorted list — still a runnable demo of objects in an array.

Sandbox: `code_sandbox/js-array-sort/cars-objects.html`

```javascript
const cars = [
  {type:"Volvo", year:2016},
  {type:"Saab", year:2001},
  {type:"BMW", year:2010}
];
```

<img alt="js-array-sort example 17 source" src="./code_sandbox/snaps/js-array-sort-17-code.png" />

<img alt="js-array-sort example 17 result" src="./code_sandbox/snaps/js-array-sort-17-result.png" />

- [x] **Outcome:** Three cars: Volvo 2016, Saab 2001, BMW 2010.

<a id="js-array-sort-example-18"></a>

### **Example 18: Sort cars by year**

- [x] `a.year - b.year` sorts **numeric** properties.

Sandbox: `code_sandbox/js-array-sort/sort-cars-year.html`

```javascript
const cars = [
  {type:"Volvo", year:2016},
  {type:"Saab", year:2001},
  {type:"BMW", year:2010}
];
cars.sort(function(a, b){return a.year - b.year});
```

<img alt="js-array-sort example 18 source" src="./code_sandbox/snaps/js-array-sort-18-code.png" />

<img alt="js-array-sort example 18 result" src="./code_sandbox/snaps/js-array-sort-18-result.png" />

- [x] **Outcome:** Saab 2001, BMW 2010, Volvo 2016.

<a id="js-array-sort-example-19"></a>

### **Example 19: Sort cars by type string**

- [x] Compare lowercased strings with **-1 / 0 / 1**.

Sandbox: `code_sandbox/js-array-sort/sort-cars-type.html`

```javascript
const cars = [
  {type:"Volvo", year:2016},
  {type:"Saab", year:2001},
  {type:"BMW", year:2010}
];
cars.sort(function(a, b){
  let x = a.type.toLowerCase();
  let y = b.type.toLowerCase();
  if (x < y) {return -1;}
  if (x > y) {return 1;}
  return 0;
});
```

<img alt="js-array-sort example 19 source" src="./code_sandbox/snaps/js-array-sort-19-code.png" />

<img alt="js-array-sort example 19 result" src="./code_sandbox/snaps/js-array-sort-19-result.png" />

- [x] **Outcome:** BMW, Saab, Volvo.

<a id="js-array-sort-example-20"></a>

### **Example 20: Stable sort by price (ES2019)**

- [x] Equal keys must keep **relative order**. Sort these eight rows by `price`.

Sandbox: `code_sandbox/js-array-sort/stable-sort.html`

```javascript
const myArr = [
  {name:"X00",price:100}, {name:"X01",price:100},
  {name:"X02",price:100}, {name:"X03",price:100},
  {name:"X04",price:110}, {name:"X05",price:110},
  {name:"X06",price:110}, {name:"X07",price:110}
];
myArr.sort(function(a, b){return a.price - b.price});
const names = myArr.map(o => o.name + " " + o.price);
```

<img alt="js-array-sort example 20 source" src="./code_sandbox/snaps/js-array-sort-20-code.png" />

<img alt="js-array-sort example 20 result" src="./code_sandbox/snaps/js-array-sort-20-result.png" />

- [x] **Outcome:** **["X00 100","X01 100","X02 100","X03 100","X04 110","X05 110","X06 110","X07 110"]** — X00 stayed before X01, and so on.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-array-sort/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: fruits.sort() on Banana, Orange, Apple, Mango?

<details>
<summary>Answer</summary>

- [x] **Apple, Banana, Mango, Orange**.

</details>

### Question 2: reverse without sort?

<details>
<summary>Answer</summary>

- [x] **Mango, Apple, Orange, Banana**.

</details>

### Question 3: sort then reverse?

<details>
<summary>Answer</summary>

- [x] **Orange, Mango, Banana, Apple**.

</details>

### Question 4: toSorted on Jan Feb Mar Apr?

<details>
<summary>Answer</summary>

- [x] **Apr, Feb, Jan, Mar**. months unchanged.

</details>

### Question 5: Numeric a-b on [40,100,1,5,25,10]?

<details>
<summary>Answer</summary>

- [x] **[1,5,10,25,40,100]**.

</details>

### Question 6: Default sort of those numbers?

<details>
<summary>Answer</summary>

- [x] **[1,10,100,25,40,5]** — string order.

</details>

### Question 7: Is the random sort fair?

<details>
<summary>Answer</summary>

- [x] **No.** Fisher–Yates is the fair shuffle. Both still run; the printed order is **random**.

</details>

### Question 8: Math.min.apply on that list?

<details>
<summary>Answer</summary>

- [x] **1**. Math.max.apply is **100**.

</details>

### Question 9: Homemade min / max?

<details>
<summary>Answer</summary>

- [x] **1** and **100**, looping from Infinity / -Infinity.

</details>

### Question 10: Sort cars by year?

<details>
<summary>Answer</summary>

- [x] Saab 2001, BMW 2010, Volvo 2016.

</details>

### Question 11: Sort cars by type?

<details>
<summary>Answer</summary>

- [x] BMW, Saab, Volvo.

</details>

### Question 12: Is sort stable?

<details>
<summary>Answer</summary>

- [x] **Yes** since ES2019. X00–X03 stay in order among price 100.

</details>


</details>

## Summary

Default sort is alphabetic. Pass a-b for numbers. Prefer toSorted when you need a copy. Shuffle with Fisher–Yates, not a random compare. For a single min or max, a loop or Math.min beats sorting the whole array. Object sorts compare a field; equal keys keep their order.

## References

- [JS Array Sort (W3Schools)](https://www.w3schools.com/js/js_array_sort.asp)
- [MDN: Array.prototype.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
- [MDN: Array.prototype.toSorted](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted)

</details>
