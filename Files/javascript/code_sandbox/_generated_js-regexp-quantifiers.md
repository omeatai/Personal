<details>
  <summary>JS RegExp Quantifiers</summary>

## Introduction

Quantifiers say how many times the previous token may appear. + is one or more, * zero or more, ? zero or one. {n} is exactly n, {n,m} a range, {n,} n or more. They are greedy: {3,4} on 10000 takes four digits. Each table row has a Tryit and is its own Example.

This section has **6** examples:

- [x] **Example 1:** x+ — one or more [View](#js-regexp-quantifiers-example-01)
- [x] **Example 2:** x* — zero or more [View](#js-regexp-quantifiers-example-02)
- [x] **Example 3:** x? — zero or one [View](#js-regexp-quantifiers-example-03)
- [x] **Example 4:** x{n} — exactly n [View](#js-regexp-quantifiers-example-04)
- [x] **Example 5:** x{n,m} — from n to m [View](#js-regexp-quantifiers-example-05)
- [x] **Example 6:** x{n,} — n or more [View](#js-regexp-quantifiers-example-06)

## Detailed Explanation

- [x] **`+`** ≥1. **`*`** ≥0. **`?`** 0 or 1.
- [x] **`{n}`** exact. **`{n,m}`** inclusive range. **`{n,}`** at least n.
- [x] Quantifiers are **greedy** (take the longest match that still allows success).
- [x] `10?` is `1` plus optional `0`, not the number ten.

<a id="js-regexp-quantifiers-example-01"></a>

### **Example 1: x+ — one or more**

- [x] **`+`** means **one or more** of the previous token. `/o+/g` on the Hello/Schools sentence.

Sandbox: `code_sandbox/js-regexp-quantifiers/plus.html`

```javascript
let text = "Hellooo World! Hello W3Schools!";
const pattern = /o+/g;
let result = text.match(pattern);
```

<img alt="js-regexp-quantifiers example 1 source" src="./code_sandbox/snaps/js-regexp-quantifiers-01-code.png" />

<img alt="js-regexp-quantifiers example 1 result" src="./code_sandbox/snaps/js-regexp-quantifiers-01-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["ooo","o","o","oo"]**.

<a id="js-regexp-quantifiers-example-02"></a>

### **Example 2: x* — zero or more**

- [x] **`*`** means **zero or more**. `/lo*/g` is an `l` plus extra `o`s (including none).

Sandbox: `code_sandbox/js-regexp-quantifiers/star.html`

```javascript
let text = "Hellooo World! Hello W3Schools!";
const pattern = /lo*/g;
let result = text.match(pattern);
```

<img alt="js-regexp-quantifiers example 2 source" src="./code_sandbox/snaps/js-regexp-quantifiers-02-code.png" />

<img alt="js-regexp-quantifiers example 2 result" src="./code_sandbox/snaps/js-regexp-quantifiers-02-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["l","looo","l","l","lo","l"]**.

<a id="js-regexp-quantifiers-example-03"></a>

### **Example 3: x? — zero or one**

- [x] **`?`** means **zero or one**. `/10?/g` is `1` plus an optional `0`.

Sandbox: `code_sandbox/js-regexp-quantifiers/question.html`

```javascript
let text = "1, 100 or 1000?";
const pattern = /10?/g;
let result = text.match(pattern);
```

<img alt="js-regexp-quantifiers example 3 source" src="./code_sandbox/snaps/js-regexp-quantifiers-03-code.png" />

<img alt="js-regexp-quantifiers example 3 result" src="./code_sandbox/snaps/js-regexp-quantifiers-03-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["1","10","10"]**.

<a id="js-regexp-quantifiers-example-04"></a>

### **Example 4: x{n} — exactly n**

- [x] **`{4}`** wants exactly four digits. `100` is skipped; `10000` yields one four-digit slice.

Sandbox: `code_sandbox/js-regexp-quantifiers/exactly-n.html`

```javascript
let text = "100, 1000 or 10000?";
const pattern = /\d{4}/g;
let result = text.match(pattern);
```

<img alt="js-regexp-quantifiers example 4 source" src="./code_sandbox/snaps/js-regexp-quantifiers-04-code.png" />

<img alt="js-regexp-quantifiers example 4 result" src="./code_sandbox/snaps/js-regexp-quantifiers-04-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["1000","1000"]**.

<a id="js-regexp-quantifiers-example-05"></a>

### **Example 5: x{n,m} — from n to m**

- [x] **`{3,4}`** is greedy: `10000` contributes **`1000`**, leftover `0`.

Sandbox: `code_sandbox/js-regexp-quantifiers/n-to-m.html`

```javascript
let text = "100, 1000 or 10000?";
const pattern = /\d{3,4}/g;
let result = text.match(pattern);
```

<img alt="js-regexp-quantifiers example 5 source" src="./code_sandbox/snaps/js-regexp-quantifiers-05-code.png" />

<img alt="js-regexp-quantifiers example 5 result" src="./code_sandbox/snaps/js-regexp-quantifiers-05-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["100","1000","1000"]**.

<a id="js-regexp-quantifiers-example-06"></a>

### **Example 6: x{n,} — n or more**

- [x] **`{3,}`** takes the longest digit run of length ≥ 3.

Sandbox: `code_sandbox/js-regexp-quantifiers/n-or-more.html`

```javascript
let text = "100, 1000 or 10000?";
const pattern = /\d{3,}/g;
let result = text.match(pattern);
```

<img alt="js-regexp-quantifiers example 6 source" src="./code_sandbox/snaps/js-regexp-quantifiers-06-code.png" />

<img alt="js-regexp-quantifiers example 6 result" src="./code_sandbox/snaps/js-regexp-quantifiers-06-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["100","1000","10000"]**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-regexp-quantifiers/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `/o+/g` on the Hello/Schools sentence?

<details>
<summary>Answer</summary>

- [x] **["ooo","o","o","oo"]**.

</details>

### Question 2: What is `/lo*/g` there?

<details>
<summary>Answer</summary>

- [x] **["l","looo","l","l","lo","l"]**.

</details>

### Question 3: What is `/10?/g` on `1, 100 or 1000?`?

<details>
<summary>Answer</summary>

- [x] **["1","10","10"]**.

</details>

### Question 4: What is `/\d{4}/g` on `100, 1000 or 10000?`?

<details>
<summary>Answer</summary>

- [x] **["1000","1000"]** — `100` is too short.

</details>

### Question 5: What is `/\d{3,4}/g` on that string?

<details>
<summary>Answer</summary>

- [x] **["100","1000","1000"]** — greedy four on `10000`.

</details>

### Question 6: What is `/\d{3,}/g`?

<details>
<summary>Answer</summary>

- [x] **["100","1000","10000"]**.

</details>

### Question 7: Is `*` allowed to match nothing?

<details>
<summary>Answer</summary>

- [x] **Yes.** `lo*` can be a lone `l`.

</details>

### Question 8: Does `{3,4}` prefer 3 or 4?

<details>
<summary>Answer</summary>

- [x] **4** if possible (greedy).

</details>

### Question 9: Does a quantifier apply to a whole group?

<details>
<summary>Answer</summary>

- [x] Only if you **group** first: `(ha)+` vs `ha+` (`h` then extra `a`s).

</details>


</details>

## Summary

Attach +, *, ?, {n}, {n,m}, or {n,} to the token or group you want to count. They are greedy. JSON-stringify the global match array so runs of digits stay grouped as the engine found them.

## References

- [JS RegExp Quantifiers (W3Schools)](https://www.w3schools.com/js/js_regexp_quantifiers.asp)
- [MDN: Quantifiers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Quantifiers)

</details>
