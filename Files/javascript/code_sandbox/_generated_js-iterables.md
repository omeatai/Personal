<details>
  <summary>JS Iterables</summary>

## Introduction

An iterable can be walked with for...of because it implements Symbol.iterator. Strings, Arrays, Typed Arrays, Sets, and Maps are iterable. for...of on a Map yields [key, value] pairs. A homemade object with only next() is an iterator, not an iterable — for...of needs Symbol.iterator. When done is true, for...of and a manual while(result.done) break omit that completion value.

This section has **8** examples:

- [x] **Example 1:** for...of over "W3Schools" [View](#js-iterables-example-01)
- [x] **Example 2:** for...of over ["a","b","c"] [View](#js-iterables-example-02)
- [x] **Example 3:** for...of over [2, 4, 6, 8] [View](#js-iterables-example-03)
- [x] **Example 4:** for...of over Set(["a","b","c"]) [View](#js-iterables-example-04)
- [x] **Example 5:** for...of over a Map of fruits [View](#js-iterables-example-05)
- [x] **Example 6:** Home-made iterator: next() never done [View](#js-iterables-example-06)
- [x] **Example 7:** Symbol.iterator homemade iterable + for...of [View](#js-iterables-example-07)
- [x] **Example 8:** Manual iterator.next() until done [View](#js-iterables-example-08)

## Detailed Explanation

- [x] **Iterating** means looping a sequence. **`for...of`** is the language loop for iterables.
- [x] Built-in iterables: **String, Array, TypedArray, Set, Map** (their prototypes have **`Symbol.iterator`**).
- [x] An **iterator** implements **`next()` → `{value, done}`**. An **iterable** implements **`Symbol.iterator`**.
- [x] Home-made `next()`-only objects **do not** support `for...of`.
- [x] `for...of` / `if (result.done) break` **do not yield** the `{done:true}` value (here: **100** is omitted).

<a id="js-iterables-example-01"></a>

### **Example 1: for...of over "W3Schools"**

- [x] A **string** is iterable. `for...of` yields each **code unit** (here: each character).
- [x] `const x of name` — `x` is the **character**, not an index.

Sandbox: `code_sandbox/js-iterables/for-of-string.html`

```javascript
const name = "W3Schools";
let text = "";
for (const x of name) {
  text += x + "\n";
}
```

<img alt="js-iterables example 1 source" src="./code_sandbox/snaps/js-iterables-01-code.png" />

<img alt="js-iterables example 1 result" src="./code_sandbox/snaps/js-iterables-01-result.png" />

- [x] **Outcome:** Nine lines: **W**, **3**, **S**, **c**, **h**, **o**, **o**, **l**, **s**.

<a id="js-iterables-example-02"></a>

### **Example 2: for...of over ["a","b","c"]**

- [x] An **Array** is iterable. `for...of` yields each **element**.

Sandbox: `code_sandbox/js-iterables/for-of-letters.html`

```javascript
const letters = ["a","b","c"];
let text = "";
for (const x of letters) {
  text += x + "\n";
}
```

<img alt="js-iterables example 2 source" src="./code_sandbox/snaps/js-iterables-02-code.png" />

<img alt="js-iterables example 2 result" src="./code_sandbox/snaps/js-iterables-02-result.png" />

- [x] **Outcome:** Lines **a**, **b**, **c**.

<a id="js-iterables-example-03"></a>

### **Example 3: for...of over [2, 4, 6, 8]**

- [x] Same loop over a **numbers** array.

Sandbox: `code_sandbox/js-iterables/for-of-numbers.html`

```javascript
const numbers = [2,4,6,8];
let text = "";
for (const x of numbers) {
  text += x + "\n";
}
```

<img alt="js-iterables example 3 source" src="./code_sandbox/snaps/js-iterables-03-code.png" />

<img alt="js-iterables example 3 result" src="./code_sandbox/snaps/js-iterables-03-result.png" />

- [x] **Outcome:** Lines **2**, **4**, **6**, **8**.

<a id="js-iterables-example-04"></a>

### **Example 4: for...of over Set(["a","b","c"])**

- [x] A **Set** is iterable. Values appear **once**, in insertion order.

Sandbox: `code_sandbox/js-iterables/for-of-set.html`

```javascript
const letters = new Set(["a","b","c"]);
let text = "";
for (const x of letters) {
  text += x + "\n";
}
```

<img alt="js-iterables example 4 source" src="./code_sandbox/snaps/js-iterables-04-code.png" />

<img alt="js-iterables example 4 result" src="./code_sandbox/snaps/js-iterables-04-result.png" />

- [x] **Outcome:** Lines **a**, **b**, **c**.

<a id="js-iterables-example-05"></a>

### **Example 5: for...of over a Map of fruits**

- [x] A **Map** is iterable. Each step yields a **`[key, value]` pair** (an Array).
- [x] `String(["apples", 500])` is **`apples,500`** (Array `toString`).

Sandbox: `code_sandbox/js-iterables/for-of-map.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
let text = "";
for (const x of fruits) {
  text += x + "\n";
}
```

<img alt="js-iterables example 5 source" src="./code_sandbox/snaps/js-iterables-05-code.png" />

<img alt="js-iterables example 5 result" src="./code_sandbox/snaps/js-iterables-05-result.png" />

- [x] **Outcome:** text is **apples,500**, **bananas,300**, **oranges,200**. The first pair JSON is **["apples",500]**.

<a id="js-iterables-example-06"></a>

### **Example 6: Home-made iterator: next() never done**

- [x] An object is an **iterator** when it has **`next()`** returning `{value, done}`.
- [x] This factory returns `{value: n, done: false}` forever (**10, 20, 30, …**).
- [x] It is **not** iterable: there is no `Symbol.iterator`, so **`for...of` will not work**.

Sandbox: `code_sandbox/js-iterables/homemade-next.html`

```javascript
function myNumbers() {
  let n = 0;
  return {
    next: function() {
      n += 10;
      return {value:n, done:false};
    }
  };
}
const n = myNumbers();
const a = n.next();
const b = n.next();
const c = n.next();
const d = n.next();
```

<img alt="js-iterables example 6 source" src="./code_sandbox/snaps/js-iterables-06-code.png" />

<img alt="js-iterables example 6 result" src="./code_sandbox/snaps/js-iterables-06-result.png" />

- [x] **Outcome:** a/b/c are **{"value":10,"done":false}**, **20**, **30**. The Tryit then prints `n.next().value` → **40**. `done` stays **false**.

<a id="js-iterables-example-07"></a>

### **Example 7: Symbol.iterator homemade iterable + for...of**

- [x] A true **iterable** has **`obj[Symbol.iterator]`** — a function that returns an iterator.
- [x] `for...of` calls that method automatically.
- [x] This demo sets `done: true` when `n == 100`. **`for...of` does not yield the done value.**

Sandbox: `code_sandbox/js-iterables/symbol-iterator-for-of.html`

```javascript
const myNumbers = {};
myNumbers[Symbol.iterator] = function() {
  let n = 0;
  let done = false;
  return {
    next() {
      n += 10;
      if (n == 100) { done = true; }
      return {value:n, done:done};
    }
  };
};
let text = "";
for (const num of myNumbers) {
  text += num + "\n";
}
```

<img alt="js-iterables example 7 source" src="./code_sandbox/snaps/js-iterables-07-code.png" />

<img alt="js-iterables example 7 result" src="./code_sandbox/snaps/js-iterables-07-result.png" />

- [x] **Outcome:** Lines **10** through **90**. When `n` hits **100**, `done` is **true**, so **100 is omitted**. (The page assigns `done` as a sloppy global; this sandbox uses `let done`.)

<a id="js-iterables-example-08"></a>

### **Example 8: Manual iterator.next() until done**

- [x] You can call **`obj[Symbol.iterator]()`** yourself and loop on **`next()`**.
- [x] `if (result.done) break` skips the completion `{value, done:true}` — same as `for...of`.

Sandbox: `code_sandbox/js-iterables/symbol-iterator-manual.html`

```javascript
const myNumbers = {};
myNumbers[Symbol.iterator] = function() {
  let n = 0;
  let done = false;
  return {
    next() {
      n += 10;
      if (n == 100) { done = true; }
      return {value:n, done:done};
    }
  };
};
let iterator = myNumbers[Symbol.iterator]();
let text = "";
while (true) {
  const result = iterator.next();
  if (result.done) break;
  text += result.value + "\n";
}
```

<img alt="js-iterables example 8 source" src="./code_sandbox/snaps/js-iterables-08-code.png" />

<img alt="js-iterables example 8 result" src="./code_sandbox/snaps/js-iterables-08-result.png" />

- [x] **Outcome:** Same as `for...of`: **10** through **90**. The `{value:100, done:true}` step is not printed.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-iterables/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What makes an object iterable?

<details>
<summary>Answer</summary>

- [x] It has **`obj[Symbol.iterator]`**, a function that returns an iterator.

</details>

### Question 2: What must `next()` return?

<details>
<summary>Answer</summary>

- [x] An object with **`value`** and **`done`** (boolean).

</details>

### Question 3: What does `for...of` on `"W3Schools"` print?

<details>
<summary>Answer</summary>

- [x] Each character: **W 3 S c h o o l s**.

</details>

### Question 4: What does `for...of` on a Map yield?

<details>
<summary>Answer</summary>

- [x] **`[key, value]`** pairs. `String` of `['apples',500]` is **apples,500**.

</details>

### Question 5: Can the home-made `myNumbers()` next-only object use `for...of`?

<details>
<summary>Answer</summary>

- [x] **No.** It has `next` but no **`Symbol.iterator`**.

</details>

### Question 6: What does that next-only demo display after four `next()` calls?

<details>
<summary>Answer</summary>

- [x] **40** (`10, 20, 30`, then the displayed fourth value). `done` stays **false**.

</details>

### Question 7: What numbers does the `Symbol.iterator` homemade object yield?

<details>
<summary>Answer</summary>

- [x] **10 through 90**. **100** has `done:true` and is **not** printed.

</details>

### Question 8: Does calling `Symbol.iterator()` yourself change the sequence?

<details>
<summary>Answer</summary>

- [x] **No.** The manual `while` loop prints the same **10–90**.

</details>

### Question 9: Which built-ins are listed as iterable?

<details>
<summary>Answer</summary>

- [x] **Strings, Arrays, Typed Arrays, Sets, Maps**.

</details>

### Question 10: What is `done`?

<details>
<summary>Answer</summary>

- [x] **true** when the iterator has finished; **false** when it produced a new `value`.

</details>

### Question 11: Is a string iterated by index or by character?

<details>
<summary>Answer</summary>

- [x] By **character** (`for...of`). Indexes would be a `for` loop or `for...in`.

</details>


</details>

## Summary

Use for...of on strings, arrays, maps, and sets. Custom sequences need Symbol.iterator returning next(). A next()-only object is an iterator, not an iterable. done:true values are completion results, not loop items.

## References

- [JS Iterables (W3Schools)](https://www.w3schools.com/js/js_iterables.asp)
- [MDN: Iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
- [MDN: Symbol.iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator)

</details>
