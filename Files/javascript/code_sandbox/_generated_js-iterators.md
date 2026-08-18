<details>
  <summary>JS Iterators</summary>

## Introduction

An iterator follows the iterator protocol: next() returns {value, done}. Built-in iterables expose Symbol.iterator. ECMAScript 2025 adds Iterator helper methods (from, drop, take, map, filter, flatMap, forEach, find, every, some, reduce) so you can transform a stream without first copying it into an Array. Iterator.from wraps an iterable. Helpers that return iterators are lazy; every / some / find / reduce / forEach consume the iterator to a result.

This section has **12** examples:

- [x] **Example 1:** Array iterator: Symbol.iterator + next() [View](#js-iterators-example-01)
- [x] **Example 2:** Iterator.from([1, 2, 3]) [View](#js-iterators-example-02)
- [x] **Example 3:** drop(5) on [1, 2, 3, 4, 5, 6] [View](#js-iterators-example-03)
- [x] **Example 4:** every(x => x > 7) on "123456789" [View](#js-iterators-example-04)
- [x] **Example 5:** filter(x => x > 18) on [32, 33, 16, 40] [View](#js-iterators-example-05)
- [x] **Example 6:** find(x => x > 18) on [3, 10, 18, 30, 20] [View](#js-iterators-example-06)
- [x] **Example 7:** flatMap(x => [x, x * 10]) [View](#js-iterators-example-07)
- [x] **Example 8:** forEach on Iterator.from("123456789") [View](#js-iterators-example-08)
- [x] **Example 9:** map(x => x * 2) on "123456789" [View](#js-iterators-example-09)
- [x] **Example 10:** reduce sum of [175, 50, 25] [View](#js-iterators-example-10)
- [x] **Example 11:** some(x => x > 7) on "123456789" [View](#js-iterators-example-11)
- [x] **Example 12:** take(5) on [1, 2, 3, 4, 5, 6] [View](#js-iterators-example-12)

## Detailed Explanation

- [x] **`next()`** → `{value, done}`. **`done:true`** means no more elements.
- [x] Built-ins are iterable because **`Symbol.iterator`** lives on the prototype.
- [x] **`Iterator.from(x)`** makes an Iterator helper from an iterable or iterator.
- [x] **Lazy helpers:** `drop`, `take`, `map`, `filter`, `flatMap` return **iterators**.
- [x] **Eager helpers:** `every`, `some`, `find`, `reduce`, `forEach` walk the rest of the stream now.

<a id="js-iterators-example-01"></a>

### **Example 1: Array iterator: Symbol.iterator + next()**

- [x] Built-in iterables (arrays, strings, Maps, Sets) store **`Symbol.iterator`** on the prototype.
- [x] `arr[Symbol.iterator]()` returns an iterator. **`next()`** is `{value, done}`.
- [x] No Tryit for the protocol itself on this page — still run it.

Sandbox: `code_sandbox/js-iterators/array-iterator-next.html`

```javascript
const arr = ["a", "b"];
const it = arr[Symbol.iterator]();
const first = it.next();
const second = it.next();
const third = it.next();
```

<img alt="js-iterators example 1 source" src="./code_sandbox/snaps/js-iterators-01-code.png" />

<img alt="js-iterators example 1 result" src="./code_sandbox/snaps/js-iterators-01-result.png" />

- [x] **Outcome:** first **{"value":"a","done":false}**, second **{"value":"b","done":false}**, third **{"done":true}** (`value` is **undefined**).

<a id="js-iterators-example-02"></a>

### **Example 2: Iterator.from([1, 2, 3])**

- [x] `Iterator.from(iterable)` wraps an iterable as an **Iterator** helper object.
- [x] Then `for...of` (or helper methods) can consume it.

Sandbox: `code_sandbox/js-iterators/iterator-from.html`

```javascript
const myIterator = Iterator.from([1, 2, 3]);
let text = "";
for (const x of myIterator) {
  text += x + "\n";
}
```

<img alt="js-iterators example 2 source" src="./code_sandbox/snaps/js-iterators-02-code.png" />

<img alt="js-iterators example 2 result" src="./code_sandbox/snaps/js-iterators-02-result.png" />

- [x] **Outcome:** Lines **1**, **2**, **3**.

<a id="js-iterators-example-03"></a>

### **Example 3: drop(5) on [1, 2, 3, 4, 5, 6]**

- [x] `drop(n)` returns an iterator that **skips** the first **n** values.
- [x] The remaining values are still yielded one by one (not an Array until you collect them).

Sandbox: `code_sandbox/js-iterators/iterator-drop.html`

```javascript
const myIterator = Iterator.from([1, 2, 3, 4, 5, 6]);
const rest = myIterator.drop(5);
let text = "";
for (const x of rest) {
  text += x + "\n";
}
```

<img alt="js-iterators example 3 source" src="./code_sandbox/snaps/js-iterators-03-code.png" />

<img alt="js-iterators example 3 result" src="./code_sandbox/snaps/js-iterators-03-result.png" />

- [x] **Outcome:** Only **6** remains (the first five values were dropped).

<a id="js-iterators-example-04"></a>

### **Example 4: every(x => x > 7) on "123456789"**

- [x] `every(fn)` is **true** only if **every** element passes `fn`.
- [x] String digits coerce: `"1" > 7` is **false** (numeric compare), so the answer is false.

Sandbox: `code_sandbox/js-iterators/iterator-every.html`

```javascript
const myIterator = Iterator.from("123456789");
let result = myIterator.every(x => x > 7);
```

<img alt="js-iterators example 4 source" src="./code_sandbox/snaps/js-iterators-04-code.png" />

<img alt="js-iterators example 4 result" src="./code_sandbox/snaps/js-iterators-04-result.png" />

- [x] **Outcome:** **false** — `'1'` is not greater than 7. (`every` stops at the first failure.)

<a id="js-iterators-example-05"></a>

### **Example 5: filter(x => x > 18) on [32, 33, 16, 40]**

- [x] `filter(fn)` yields only elements for which `fn` is **truthy**.

Sandbox: `code_sandbox/js-iterators/iterator-filter.html`

```javascript
const myIterator = Iterator.from([32, 33, 16, 40]);
const filteredIterator = myIterator.filter(x => x > 18);
let text = "";
for (const x of filteredIterator) {
  text += x + "\n";
}
```

<img alt="js-iterators example 5 source" src="./code_sandbox/snaps/js-iterators-05-code.png" />

<img alt="js-iterators example 5 result" src="./code_sandbox/snaps/js-iterators-05-result.png" />

- [x] **Outcome:** Lines **32**, **33**, **40**. **16** is dropped.

<a id="js-iterators-example-06"></a>

### **Example 6: find(x => x > 18) on [3, 10, 18, 30, 20]**

- [x] `find(fn)` returns the **first** matching **value** (not an iterator).
- [x] **18** is not `> 18`. The first hit is **30**.

Sandbox: `code_sandbox/js-iterators/iterator-find.html`

```javascript
const myIterator = Iterator.from([3, 10, 18, 30, 20]);
let result = myIterator.find(x => x > 18);
```

<img alt="js-iterators example 6 source" src="./code_sandbox/snaps/js-iterators-06-code.png" />

<img alt="js-iterators example 6 result" src="./code_sandbox/snaps/js-iterators-06-result.png" />

- [x] **Outcome:** result is **30**.

<a id="js-iterators-example-07"></a>

### **Example 7: flatMap(x => [x, x * 10])**

- [x] `flatMap(fn)` maps each element to an **iterable** and **flattens one level**.
- [x] `[x, x * 10]` becomes two yielded numbers per input.

Sandbox: `code_sandbox/js-iterators/iterator-flatmap.html`

```javascript
const myIterator = Iterator.from([1, 2, 3, 4, 5, 6]);
const mappedIterator = myIterator.flatMap(x => [x, x * 10]);
let text = "";
for (const x of mappedIterator) {
  text += x + "\n";
}
```

<img alt="js-iterators example 7 source" src="./code_sandbox/snaps/js-iterators-07-code.png" />

<img alt="js-iterators example 7 result" src="./code_sandbox/snaps/js-iterators-07-result.png" />

- [x] **Outcome:** Lines **1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60**.

<a id="js-iterators-example-08"></a>

### **Example 8: forEach on Iterator.from("123456789")**

- [x] `forEach(fn)` runs `fn` once per remaining element (consumed; returns **undefined**).

Sandbox: `code_sandbox/js-iterators/iterator-foreach.html`

```javascript
const myIterator = Iterator.from("123456789");
let text = "";
myIterator.forEach(x => text += x);
```

<img alt="js-iterators example 8 source" src="./code_sandbox/snaps/js-iterators-08-code.png" />

<img alt="js-iterators example 8 result" src="./code_sandbox/snaps/js-iterators-08-result.png" />

- [x] **Outcome:** text is **"123456789"** (the nine digit characters concatenated).

<a id="js-iterators-example-09"></a>

### **Example 9: map(x => x * 2) on "123456789"**

- [x] `map(fn)` yields `fn(element)` for each element.
- [x] Digit characters coerce: `'1' * 2` is **2** (number).

Sandbox: `code_sandbox/js-iterators/iterator-map.html`

```javascript
const myIterator = Iterator.from("123456789");
const mappedIterator = myIterator.map(x => x * 2);
let text = "";
for (const x of mappedIterator) {
  text += x + "\n";
}
```

<img alt="js-iterators example 9 source" src="./code_sandbox/snaps/js-iterators-09-code.png" />

<img alt="js-iterators example 9 result" src="./code_sandbox/snaps/js-iterators-09-result.png" />

- [x] **Outcome:** Lines **2, 4, 6, 8, 10, 12, 14, 16, 18**.

<a id="js-iterators-example-10"></a>

### **Example 10: reduce sum of [175, 50, 25]**

- [x] `reduce(fn)` folds the iterator to **one value**.
- [x] With no initial value, the first element is the start accumulator.

Sandbox: `code_sandbox/js-iterators/iterator-reduce.html`

```javascript
function myFunc(total, num) {
  return total + num;
}
const myIterator = Iterator.from([175, 50, 25]);
let result = myIterator.reduce(myFunc);
```

<img alt="js-iterators example 10 source" src="./code_sandbox/snaps/js-iterators-10-code.png" />

<img alt="js-iterators example 10 result" src="./code_sandbox/snaps/js-iterators-10-result.png" />

- [x] **Outcome:** result is **250** (`175 + 50 + 25`).

<a id="js-iterators-example-11"></a>

### **Example 11: some(x => x > 7) on "123456789"**

- [x] `some(fn)` is **true** if **at least one** element passes `fn`.
- [x] `'8' > 7` and `'9' > 7` are true after numeric coercion.

Sandbox: `code_sandbox/js-iterators/iterator-some.html`

```javascript
const myIterator = Iterator.from("123456789");
let result = myIterator.some(x => x > 7);
```

<img alt="js-iterators example 11 source" src="./code_sandbox/snaps/js-iterators-11-code.png" />

<img alt="js-iterators example 11 result" src="./code_sandbox/snaps/js-iterators-11-result.png" />

- [x] **Outcome:** **true**.

<a id="js-iterators-example-12"></a>

### **Example 12: take(5) on [1, 2, 3, 4, 5, 6]**

- [x] `take(n)` yields **at most n** elements, then stops.

Sandbox: `code_sandbox/js-iterators/iterator-take.html`

```javascript
const myIterator = Iterator.from([1, 2, 3, 4, 5, 6]);
const firstFive = myIterator.take(5);
let text = "";
for (const x of firstFive) {
  text += x + "\n";
}
```

<img alt="js-iterators example 12 source" src="./code_sandbox/snaps/js-iterators-12-code.png" />

<img alt="js-iterators example 12 result" src="./code_sandbox/snaps/js-iterators-12-result.png" />

- [x] **Outcome:** Lines **1, 2, 3, 4, 5**. **6** is not taken.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-iterators/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `arr[Symbol.iterator]().next()` look like?

<details>
<summary>Answer</summary>

- [x] First of `["a","b"]` is **`{"value":"a","done":false}`**. After the end: **`done:true`**.

</details>

### Question 2: What does `Iterator.from([1,2,3])` print in `for...of`?

<details>
<summary>Answer</summary>

- [x] **1, 2, 3**.

</details>

### Question 3: What does `drop(5)` on `[1..6]` leave?

<details>
<summary>Answer</summary>

- [x] **6** only.

</details>

### Question 4: Why is `every(x => x > 7)` on `"123456789"` false?

<details>
<summary>Answer</summary>

- [x] `'1' > 7` is **false** (coerced to number). `every` fails immediately.

</details>

### Question 5: What does `filter(x => x > 18)` keep from `[32,33,16,40]`?

<details>
<summary>Answer</summary>

- [x] **32, 33, 40**.

</details>

### Question 6: What does `find(x => x > 18)` return from `[3,10,18,30,20]`?

<details>
<summary>Answer</summary>

- [x] **30** (18 is not greater than 18).

</details>

### Question 7: What does `flatMap(x => [x, x*10])` produce for 1..6?

<details>
<summary>Answer</summary>

- [x] **1, 10, 2, 20, … 6, 60**.

</details>

### Question 8: What does `map(x => x * 2)` do to the digit string?

<details>
<summary>Answer</summary>

- [x] **2, 4, 6, … 18** (characters coerce to numbers).

</details>

### Question 9: What is `reduce` of `[175, 50, 25]` with add?

<details>
<summary>Answer</summary>

- [x] **250**.

</details>

### Question 10: Is `some(x => x > 7)` on that digit string true?

<details>
<summary>Answer</summary>

- [x] **Yes** — `'8'` and `'9'` pass.

</details>

### Question 11: What does `take(5)` on `[1..6]` yield?

<details>
<summary>Answer</summary>

- [x] **1, 2, 3, 4, 5**.

</details>

### Question 12: Does `forEach` return a new iterator?

<details>
<summary>Answer</summary>

- [x] **No.** It runs the callback and returns **undefined**; this demo concatenates **123456789**.

</details>


</details>

## Summary

Call next() for {value, done}. Use Iterator.from plus the ES2025 helpers to skip, take, map, filter, or reduce a stream. String digits coerce in numeric callbacks. drop/take/map/filter/flatMap stay lazy; every/some/find/reduce/forEach consume.

## References

- [JS Iterators (W3Schools)](https://www.w3schools.com/js/js_iterators.asp)
- [MDN: Iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
- [MDN: Iterator.from](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)

</details>
