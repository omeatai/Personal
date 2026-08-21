# JS Generators

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A generator function (function*) returns a Generator object that is both iterable and an iterator. yield pauses and produces a value; the function resumes on next(). return finishes with done:true — for...of does not print that value, but next() still reports it. Generator methods are next, return, and throw.

This section has **5** examples:

- [x] **Example 1:** function* with yield 1, yield 2, return 3 [View](#js-generators-example-01)
- [x] **Example 2:** function* with three yield values [View](#js-generators-example-02)
- [x] **Example 3:** next() objects: value and done (including return) [View](#js-generators-example-03)
- [x] **Example 4:** generator.return(99) [View](#js-generators-example-04)
- [x] **Example 5:** generator.throw() caught inside the generator [View](#js-generators-example-05)

## Detailed Explanation

- [x] Declare with **`function*`**. The call returns a **Generator**, not the first value.
- [x] **`yield`** → `{value, done:false}` and pause. **`return`** → `{value, done:true}` and finish.
- [x] **`for...of` exits when done is true** — a final `return 3` is **not** looped.
- [x] Yield all values you want in `for...of`. The second Tryit uses **`yield 3`** (the page typo `yeald` is not in the Tryit).
- [x] Methods: **`next()`**, **`return(v)`** finish now, **`throw(e)`** inject an error at the pause.

<a id="js-generators-example-01"></a>

### **Example 1: function* with yield 1, yield 2, return 3**

- [x] `function*` returns a **Generator** object (iterable **and** iterator).
- [x] `yield` pauses and produces `{value, done:false}`. **`return`** finishes with `{done:true}`.
- [x] `for...of` **stops at done:true** and does **not** include the return value.

Sandbox: `code_sandbox/js-generators/yield-then-return.html`

```javascript
function* myStream() {
  yield 1;
  yield 2;
  return 3;
}
let myGenerator = myStream();
let text = "";
for (let value of myGenerator) {
  text += value + "\n";
}
```

![js-generators example 1 source](../code_sandbox/snaps/js-generators-01-code.png)

![js-generators example 1 result](../code_sandbox/snaps/js-generators-01-result.png)

- [x] **Outcome:** text is **1** then **2**. **3 is omitted** because `return 3` sets **done: true**.

<a id="js-generators-example-02"></a>

### **Example 2: function* with three yield values**

- [x] To have `for...of` print a value, **`yield` it** — do not `return` it as the last step.
- [x] The page’s prose had a `yeald` typo; the Tryit correctly uses **`yield 3`**.

Sandbox: `code_sandbox/js-generators/three-yields.html`

```javascript
function* myStream() {
  yield 1;
  yield 2;
  yield 3;
}
let myGenerator = myStream();
let text = "";
for (let value of myGenerator) {
  text += value + "\n";
}
```

![js-generators example 2 source](../code_sandbox/snaps/js-generators-02-code.png)

![js-generators example 2 result](../code_sandbox/snaps/js-generators-02-result.png)

- [x] **Outcome:** text is **1**, **2**, **3**.

<a id="js-generators-example-03"></a>

### **Example 3: next() objects: value and done (including return)**

- [x] `generator.next()` resumes until the next `yield` or `return`.
- [x] The object is always **`{value, done}`**. A `return` value is in **`value` with done:true**.
- [x] Table row **next()** — no Tryit on the page. Still run it.

Sandbox: `code_sandbox/js-generators/next-done-return-value.html`

```javascript
function* myStream() {
  yield 1;
  yield 2;
  return 3;
}
let g = myStream();
const a = g.next();
const b = g.next();
const c = g.next();
const d = g.next();
```

![js-generators example 3 source](../code_sandbox/snaps/js-generators-03-code.png)

![js-generators example 3 result](../code_sandbox/snaps/js-generators-03-result.png)

- [x] **Outcome:** a **{"value":1,"done":false}**, b **{"value":2,"done":false}**, c **{"value":3,"done":true}** (the **return** value), d **{"done":true}** (`value` **undefined**).

<a id="js-generators-example-04"></a>

### **Example 4: generator.return(99)**

- [x] `return(v)` **finishes** the generator now and yields **`{value:v, done:true}`**.
- [x] Later `next()` stays done. Table row **return()** — no Tryit.

Sandbox: `code_sandbox/js-generators/generator-return-method.html`

```javascript
function* myStream() {
  yield 1;
  yield 2;
  yield 3;
}
let g = myStream();
const a = g.next();
const b = g.return(99);
const c = g.next();
```

![js-generators example 4 source](../code_sandbox/snaps/js-generators-04-code.png)

![js-generators example 4 result](../code_sandbox/snaps/js-generators-04-result.png)

- [x] **Outcome:** a **{"value":1,"done":false}**, b **{"value":99,"done":true}**, c **{"done":true}** (no more yields).

<a id="js-generators-example-05"></a>

### **Example 5: generator.throw() caught inside the generator**

- [x] `throw(err)` injects an exception **at the pause point**.
- [x] If the generator **catches** it, it can `yield` again. Table row **throw()** — no Tryit.

Sandbox: `code_sandbox/js-generators/generator-throw-method.html`

```javascript
function* myStream() {
  try {
    yield 1;
    yield 2;
  } catch (e) {
    yield "caught:" + e;
  }
  yield 3;
}
let g = myStream();
const a = g.next();
const b = g.throw("boom");
const c = g.next();
```

![js-generators example 5 source](../code_sandbox/snaps/js-generators-05-code.png)

![js-generators example 5 result](../code_sandbox/snaps/js-generators-05-result.png)

- [x] **Outcome:** a **{"value":1,"done":false}**, b **{"value":"caught:boom","done":false}**, c **{"value":3,"done":false}**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-generators/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `function*` return when called?

<details>
<summary>Answer</summary>

- [x] A **Generator object**, not a single return value.

</details>

### Question 2: What does `for...of` print for `yield 1; yield 2; return 3`?

<details>
<summary>Answer</summary>

- [x] **1** and **2** only. **3** is the completion value (`done:true`).

</details>

### Question 3: How do you include 3 in `for...of`?

<details>
<summary>Answer</summary>

- [x] **`yield 3`**, not `return 3`.

</details>

### Question 4: What is the third `next()` after two yields and `return 3`?

<details>
<summary>Answer</summary>

- [x] **`{"value":3,"done":true}`**. A fourth `next()` is done with **undefined** value.

</details>

### Question 5: What does `return(99)` do after the first yield?

<details>
<summary>Answer</summary>

- [x] Finishes immediately: **`{"value":99,"done":true}`**. Further `next()` stays done.

</details>

### Question 6: What does `throw("boom")` do if the generator catches it?

<details>
<summary>Answer</summary>

- [x] It resumes in the `catch`; this demo then **`yield "caught:boom"`** and later **yield 3**.

</details>

### Question 7: Is a generator iterable?

<details>
<summary>Answer</summary>

- [x] **Yes.** It is both **iterable** and an **iterator** (`for...of` and `next()` both work).

</details>

### Question 8: Does `yield` lose local state?

<details>
<summary>Answer</summary>

- [x] **No.** Locals are kept until the next `next()` resumes at that `yield`.

</details>

### Question 9: What are the three generator object methods?

<details>
<summary>Answer</summary>

- [x] **`next()`**, **`return()`**, **`throw()`**.

</details>

### Question 10: Did the live Tryit use `yeald`?

<details>
<summary>Answer</summary>

- [x] **No.** The Tryit is **`yield 3`**. The tutorial prose typo is not in the runnable code.

</details>


</details>

## Summary

Write function*, yield values you want in for...of, and use next() to see {value, done}. return on the generator (or a return in the body) completes the stream. throw injects an error at the pause point.

## References

- [JS Generators (W3Schools)](https://www.w3schools.com/js/js_generators.asp)
- [MDN: function*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
- [MDN: Generator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
