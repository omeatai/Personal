# JS RegExp Classes

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A character class is a set in square brackets. [a] is one character, [abc] any of those letters, [a-z] a range, [0-9] digits. A leading ^ inside the brackets negates the set. Tryits on this page use [HW], [A-Z], [1234], and [1-4]; every table row is also an Example that match()es a sample string (array or null).

This section has **12** examples:

- [x] **Example 1:** /[HW]/g — Tryit [HW] [View](#js-regexp-classes-example-01)
- [x] **Example 2:** /[A-Z]/g — Tryit uppercase range [View](#js-regexp-classes-example-02)
- [x] **Example 3:** /[1234]/g — Tryit listed digits [View](#js-regexp-classes-example-03)
- [x] **Example 4:** /[1-4]/g — Tryit digit range [View](#js-regexp-classes-example-04)
- [x] **Example 5:** [a] — one character [View](#js-regexp-classes-example-05)
- [x] **Example 6:** [^a] — negated character [View](#js-regexp-classes-example-06)
- [x] **Example 7:** [abc] — any listed [View](#js-regexp-classes-example-07)
- [x] **Example 8:** [^abc] — none of listed [View](#js-regexp-classes-example-08)
- [x] **Example 9:** [a-z] — lowercase range [View](#js-regexp-classes-example-09)
- [x] **Example 10:** [^a-z] — not lowercase [View](#js-regexp-classes-example-10)
- [x] **Example 11:** [0-9] — digit range [View](#js-regexp-classes-example-11)
- [x] **Example 12:** [^0-9] — not a digit [View](#js-regexp-classes-example-12)

## Detailed Explanation

- [x] **`[abc]`** any listed character. **`[a-z]` / `[0-9]`** ranges.
- [x] **`[^…]`** means **not** those characters.
- [x] **`[1234]`** and **`[1-4]`** match the same digits on `123456789`.
- [x] `match` with **`g`** returns every matching **character**. Miss → **null**.

<a id="js-regexp-classes-example-01"></a>

### **Example 1: /[HW]/g — Tryit [HW]**

- [x] **`[HW]`** matches **H** or **W** (the `[abc]` idea with two letters).

Sandbox: `code_sandbox/js-regexp-classes/class-hw.html`

```javascript
let text = "Hello World!";
const pattern = /[HW]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 1 source](../code_sandbox/snaps/js-regexp-classes-01-code.png)

![js-regexp-classes example 1 result](../code_sandbox/snaps/js-regexp-classes-01-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["H","W"]**.

<a id="js-regexp-classes-example-02"></a>

### **Example 2: /[A-Z]/g — Tryit uppercase range**

- [x] **`[A-Z]`** is the uppercase range. **`[a-z]`** is the lowercase twin on the table.

Sandbox: `code_sandbox/js-regexp-classes/class-upper-A-Z.html`

```javascript
let text = "This is W3Schools";
const pattern = /[A-Z]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 2 source](../code_sandbox/snaps/js-regexp-classes-02-code.png)

![js-regexp-classes example 2 result](../code_sandbox/snaps/js-regexp-classes-02-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["T","W","S"]**.

<a id="js-regexp-classes-example-03"></a>

### **Example 3: /[1234]/g — Tryit listed digits**

- [x] **`[1234]`** lists characters. Same matches as **`[1-4]`** for these digits.

Sandbox: `code_sandbox/js-regexp-classes/class-1234.html`

```javascript
let text = "123456789";
const pattern = /[1234]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 3 source](../code_sandbox/snaps/js-regexp-classes-03-code.png)

![js-regexp-classes example 3 result](../code_sandbox/snaps/js-regexp-classes-03-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["1","2","3","4"]**.

<a id="js-regexp-classes-example-04"></a>

### **Example 4: /[1-4]/g — Tryit digit range**

- [x] **`[1-4]`** is a range. The page notes **`[01234]`** equals **`[0-4]`**.

Sandbox: `code_sandbox/js-regexp-classes/class-1-4.html`

```javascript
let text = "123456789";
const pattern = /[1-4]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 4 source](../code_sandbox/snaps/js-regexp-classes-04-code.png)

![js-regexp-classes example 4 result](../code_sandbox/snaps/js-regexp-classes-04-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["1","2","3","4"]**.

<a id="js-regexp-classes-example-05"></a>

### **Example 5: [a] — one character**

- [x] **`[a]`** matches that one character, anywhere.

Sandbox: `code_sandbox/js-regexp-classes/class-a.html`

```javascript
let text = "cat";
const pattern = /[a]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 5 source](../code_sandbox/snaps/js-regexp-classes-05-code.png)

![js-regexp-classes example 5 result](../code_sandbox/snaps/js-regexp-classes-05-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["a"]**. `"XYZ".match(/[a]/)` would be **null**.

<a id="js-regexp-classes-example-06"></a>

### **Example 6: [^a] — negated character**

- [x] **`[^a]`** matches any character **except** `a`.

Sandbox: `code_sandbox/js-regexp-classes/class-not-a.html`

```javascript
let text = "cat";
const pattern = /[^a]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 6 source](../code_sandbox/snaps/js-regexp-classes-06-code.png)

![js-regexp-classes example 6 result](../code_sandbox/snaps/js-regexp-classes-06-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["c","t"]**.

<a id="js-regexp-classes-example-07"></a>

### **Example 7: [abc] — any listed**

- [x] **`[abc]`** matches **a**, **b**, or **c**.

Sandbox: `code_sandbox/js-regexp-classes/class-abc.html`

```javascript
let text = "fabric";
const pattern = /[abc]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 7 source](../code_sandbox/snaps/js-regexp-classes-07-code.png)

![js-regexp-classes example 7 result](../code_sandbox/snaps/js-regexp-classes-07-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["a","b","c"]**.

<a id="js-regexp-classes-example-08"></a>

### **Example 8: [^abc] — none of listed**

- [x] **`[^abc]`** matches characters **not** in `{a,b,c}`.

Sandbox: `code_sandbox/js-regexp-classes/class-not-abc.html`

```javascript
let text = "fabric";
const pattern = /[^abc]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 8 source](../code_sandbox/snaps/js-regexp-classes-08-code.png)

![js-regexp-classes example 8 result](../code_sandbox/snaps/js-regexp-classes-08-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["f","r","i"]**.

<a id="js-regexp-classes-example-09"></a>

### **Example 9: [a-z] — lowercase range**

- [x] **`[a-z]`** is every lowercase English letter.

Sandbox: `code_sandbox/js-regexp-classes/class-lower-a-z.html`

```javascript
let text = "A1b";
const pattern = /[a-z]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 9 source](../code_sandbox/snaps/js-regexp-classes-09-code.png)

![js-regexp-classes example 9 result](../code_sandbox/snaps/js-regexp-classes-09-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["b"]**.

<a id="js-regexp-classes-example-10"></a>

### **Example 10: [^a-z] — not lowercase**

- [x] **`[^a-z]`** matches anything that is **not** a lowercase letter.

Sandbox: `code_sandbox/js-regexp-classes/class-not-a-z.html`

```javascript
let text = "A1b";
const pattern = /[^a-z]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 10 source](../code_sandbox/snaps/js-regexp-classes-10-code.png)

![js-regexp-classes example 10 result](../code_sandbox/snaps/js-regexp-classes-10-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["A","1"]**.

<a id="js-regexp-classes-example-11"></a>

### **Example 11: [0-9] — digit range**

- [x] **`[0-9]`** matches ASCII digits. **`[^0-9]`** is the complement.

Sandbox: `code_sandbox/js-regexp-classes/class-0-9-table.html`

```javascript
let text = "A1b";
const pattern = /[0-9]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 11 source](../code_sandbox/snaps/js-regexp-classes-11-code.png)

![js-regexp-classes example 11 result](../code_sandbox/snaps/js-regexp-classes-11-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["1"]**.

<a id="js-regexp-classes-example-12"></a>

### **Example 12: [^0-9] — not a digit**

- [x] **`[^0-9]`** matches non-digits (same idea as **`\D`** for ASCII).

Sandbox: `code_sandbox/js-regexp-classes/class-not-0-9.html`

```javascript
let text = "A1b";
const pattern = /[^0-9]/g;
let result = text.match(pattern);
```

![js-regexp-classes example 12 source](../code_sandbox/snaps/js-regexp-classes-12-code.png)

![js-regexp-classes example 12 result](../code_sandbox/snaps/js-regexp-classes-12-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["A","b"]**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-regexp-classes/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `[HW]` match in `Hello World!`?

<details>
<summary>Answer</summary>

- [x] **["H","W"]**.

</details>

### Question 2: What does `[A-Z]` match in `This is W3Schools`?

<details>
<summary>Answer</summary>

- [x] **["T","W","S"]**.

</details>

### Question 3: Is `[1234]` the same as `[1-4]` here?

<details>
<summary>Answer</summary>

- [x] **Yes** on `123456789` — both **["1","2","3","4"]**.

</details>

### Question 4: What is `[^a]` on `cat`?

<details>
<summary>Answer</summary>

- [x] **["c","t"]**.

</details>

### Question 5: What is `[a-z]` on `A1b`?

<details>
<summary>Answer</summary>

- [x] **["b"]** only.

</details>

### Question 6: What is `[^a-z]` on `A1b`?

<details>
<summary>Answer</summary>

- [x] **["A","1"]**.

</details>

### Question 7: What is `[0-9]` on `A1b`?

<details>
<summary>Answer</summary>

- [x] **["1"]**.

</details>

### Question 8: What is `[^0-9]` on `A1b`?

<details>
<summary>Answer</summary>

- [x] **["A","b"]**.

</details>

### Question 9: Does `[a]` match `XYZ`?

<details>
<summary>Answer</summary>

- [x] **null** — no `a`.

</details>

### Question 10: Does a class match a whole word?

<details>
<summary>Answer</summary>

- [x] **No.** Each match is **one character** unless you add a quantifier.

</details>


</details>

## Summary

Square brackets build a set or a range. ^ inside the brackets negates. Ranges like [0-9] and lists like [1234] can describe the same characters. Always JSON-stringify the match array (or null).

## References

- [JS RegExp Character Classes (W3Schools)](https://www.w3schools.com/js/js_regexp_characters.asp)
- [MDN: Character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
