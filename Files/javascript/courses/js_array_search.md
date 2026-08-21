# JS Array Search

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Search methods find a position, a boolean, or the element that passes a test. indexOf and lastIndexOf return indexes (the page adds 1 to show a 1-based position). includes is a boolean and is the way to detect NaN. find / findIndex walk from the start; findLast / findLastIndex walk from the end (ES2023).

This section has **8** examples:

- [x] **Example 1:** indexOf("Apple") + 1 [View](#js-array-search-example-01)
- [x] **Example 2:** lastIndexOf("Apple") + 1 [View](#js-array-search-example-02)
- [x] **Example 3:** includes("Mango") [View](#js-array-search-example-03)
- [x] **Example 4:** includes(NaN) vs indexOf(NaN) [View](#js-array-search-example-04)
- [x] **Example 5:** find first value > 18 [View](#js-array-search-example-05)
- [x] **Example 6:** findIndex of first value > 18 [View](#js-array-search-example-06)
- [x] **Example 7:** findLast(x => x > 40) [View](#js-array-search-example-07)
- [x] **Example 8:** findLastIndex(x => x > 40) [View](#js-array-search-example-08)

## Detailed Explanation

- [x] `indexOf` / `lastIndexOf` return an **index** or **-1**.
- [x] The W3Schools Tryits add **`+ 1`** so the first Apple is position **1**.
- [x] `includes` is **true/false** and can see **NaN** (indexOf cannot).
- [x] `find` returns a **value**; `findIndex` returns an **index**.
- [x] `findLast` / `findLastIndex` start at the **end** (ES2023).
- [x] find callbacks receive **value, index, array**.

<a id="js-array-search-example-01"></a>

### **Example 1: indexOf("Apple") + 1**

- [x] `indexOf` returns the **first** index, or **-1**. The page adds **1** for a 1-based position.

Sandbox: `code_sandbox/js-array-search/indexof-apple.html`

```javascript
const fruits = ["Apple", "Orange", "Apple", "Mango"];
let position = fruits.indexOf("Apple") + 1;
```

![js-array-search example 1 source](../code_sandbox/snaps/js-array-search-01-code.png)

![js-array-search example 1 result](../code_sandbox/snaps/js-array-search-01-result.png)

- [x] **Outcome:** First index is **0**, so position is **1**.

<a id="js-array-search-example-02"></a>

### **Example 2: lastIndexOf("Apple") + 1**

- [x] `lastIndexOf` is the **last** occurrence, still +1 on the page.

Sandbox: `code_sandbox/js-array-search/lastindexof-apple.html`

```javascript
const fruits = ["Apple", "Orange", "Apple", "Mango"];
let position = fruits.lastIndexOf("Apple") + 1;
```

![js-array-search example 2 source](../code_sandbox/snaps/js-array-search-02-code.png)

![js-array-search example 2 result](../code_sandbox/snaps/js-array-search-02-result.png)

- [x] **Outcome:** Last index is **2**, so position is **3**.

<a id="js-array-search-example-03"></a>

### **Example 3: includes("Mango")**

- [x] ES2016 `includes` is a **boolean** membership test.

Sandbox: `code_sandbox/js-array-search/includes-mango.html`

```javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.includes("Mango");
```

![js-array-search example 3 source](../code_sandbox/snaps/js-array-search-03-code.png)

![js-array-search example 3 result](../code_sandbox/snaps/js-array-search-03-result.png)

- [x] **Outcome:** **true**.

<a id="js-array-search-example-04"></a>

### **Example 4: includes(NaN) vs indexOf(NaN)**

- [x] No Tryit — the page notes `includes` finds **NaN**; `indexOf` does not.

Sandbox: `code_sandbox/js-array-search/includes-nan-vs-indexof.html`

```javascript
const a = [NaN];
```

![js-array-search example 4 source](../code_sandbox/snaps/js-array-search-04-code.png)

![js-array-search example 4 result](../code_sandbox/snaps/js-array-search-04-result.png)

- [x] **Outcome:** `indexOf` is **-1**. `includes` is **true**.

<a id="js-array-search-example-05"></a>

### **Example 5: find first value > 18**

- [x] `find` returns the **value** of the first match, or `undefined`.
- [x] Callback args: value, index, array.

Sandbox: `code_sandbox/js-array-search/find-gt-18.html`

```javascript
const numbers = [4, 9, 16, 25, 29];
let first = numbers.find(myFunction);
function myFunction(value, index, array) {
  return value > 18;
}
```

![js-array-search example 5 source](../code_sandbox/snaps/js-array-search-05-code.png)

![js-array-search example 5 result](../code_sandbox/snaps/js-array-search-05-result.png)

- [x] **Outcome:** **25**.

<a id="js-array-search-example-06"></a>

### **Example 6: findIndex of first value > 18**

- [x] `findIndex` returns the **index** of that first match, or **-1**.

Sandbox: `code_sandbox/js-array-search/findindex-gt-18.html`

```javascript
const numbers = [4, 9, 16, 25, 29];
let first = numbers.findIndex(myFunction);
function myFunction(value, index, array) {
  return value > 18;
}
```

![js-array-search example 6 source](../code_sandbox/snaps/js-array-search-06-code.png)

![js-array-search example 6 result](../code_sandbox/snaps/js-array-search-06-result.png)

- [x] **Outcome:** **3**.

<a id="js-array-search-example-07"></a>

### **Example 7: findLast(x => x > 40)**

- [x] ES2023 `findLast` searches **from the end** and returns the value.

Sandbox: `code_sandbox/js-array-search/findlast-gt-40.html`

```javascript
const temp = [27, 28, 30, 40, 42, 35, 30];
let high = temp.findLast(x => x > 40);
```

![js-array-search example 7 source](../code_sandbox/snaps/js-array-search-07-code.png)

![js-array-search example 7 result](../code_sandbox/snaps/js-array-search-07-result.png)

- [x] **Outcome:** **42**.

<a id="js-array-search-example-08"></a>

### **Example 8: findLastIndex(x => x > 40)**

- [x] `findLastIndex` is the **index** of that last match.

Sandbox: `code_sandbox/js-array-search/findlastindex-gt-40.html`

```javascript
const temp = [27, 28, 30, 40, 42, 35, 30];
let pos = temp.findLastIndex(x => x > 40);
```

![js-array-search example 8 source](../code_sandbox/snaps/js-array-search-08-code.png)

![js-array-search example 8 result](../code_sandbox/snaps/js-array-search-08-result.png)

- [x] **Outcome:** **4**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-array-search/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Where is the first Apple, as the page prints it?

<details>
<summary>Answer</summary>

- [x] indexOf is **0**, plus 1 → position **1**.

</details>

### Question 2: Where is the last Apple, as the page prints it?

<details>
<summary>Answer</summary>

- [x] lastIndexOf is **2**, plus 1 → position **3**.

</details>

### Question 3: Does fruits include Mango?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 4: indexOf(NaN) vs includes(NaN)?

<details>
<summary>Answer</summary>

- [x] indexOf **−1**. includes **true**.

</details>

### Question 5: find first number > 18 in [4,9,16,25,29]?

<details>
<summary>Answer</summary>

- [x] **25**.

</details>

### Question 6: findIndex of that value?

<details>
<summary>Answer</summary>

- [x] **3**.

</details>

### Question 7: findLast x > 40 in [27,28,30,40,42,35,30]?

<details>
<summary>Answer</summary>

- [x] **42**.

</details>

### Question 8: findLastIndex of that value?

<details>
<summary>Answer</summary>

- [x] **4**.

</details>

### Question 9: What if find has no match?

<details>
<summary>Answer</summary>

- [x] **undefined**. findIndex returns **−1**.

</details>

### Question 10: Does includes need a callback?

<details>
<summary>Answer</summary>

- [x] **No.** It takes the search item. find* take a test function.

</details>


</details>

## Summary

Use indexOf for a first index, lastIndexOf for a last index, includes for a boolean (including NaN), and the find family when the test is a function. findLast* start from the end.

## References

- [JS Array Search (W3Schools)](https://www.w3schools.com/js/js_array_search.asp)
- [MDN: Array.prototype.indexOf](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)
- [MDN: Array.prototype.includes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)
- [MDN: Array.prototype.find](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
