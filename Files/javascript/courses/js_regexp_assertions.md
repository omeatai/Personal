# JS RegExp Assertions

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Assertions are zero-width: they check a position or a neighbor without consuming it. ^ and $ are string (or line) ends. \b / \B are word boundaries. Lookahead (?=) / (?!) and lookbehind (?<=) / (?<!) (ES2018) test the subsequent or previous text. The W3Schools lookahead Tryit uses an empty (?=) which always succeeds; a filled (?= Tutorials) is the real table meaning.

This section has **12** examples:

- [x] **Example 1:** ^ — beginning (true) [View](#js-regexp-assertions-example-01)
- [x] **Example 2:** ^ — beginning (false) [View](#js-regexp-assertions-example-02)
- [x] **Example 3:** $ — end (true) [View](#js-regexp-assertions-example-03)
- [x] **Example 4:** $ — end (false) [View](#js-regexp-assertions-example-04)
- [x] **Example 5:** \bLO — word boundary at start of LO [View](#js-regexp-assertions-example-05)
- [x] **Example 6:** LO\b — word boundary at end of LO [View](#js-regexp-assertions-example-06)
- [x] **Example 7:** \B — not a word boundary [View](#js-regexp-assertions-example-07)
- [x] **Example 8:** (?=) empty lookahead — Tryit [View](#js-regexp-assertions-example-08)
- [x] **Example 9:** (?=...) — subsequent string [View](#js-regexp-assertions-example-09)
- [x] **Example 10:** (?!...) — not the subsequent string [View](#js-regexp-assertions-example-10)
- [x] **Example 11:** (?<=...) — previous string [View](#js-regexp-assertions-example-11)
- [x] **Example 12:** (?<!...) — not the previous string [View](#js-regexp-assertions-example-12)

## Detailed Explanation

- [x] **`^` / `$`** start / end of string (or line with **`m`**).
- [x] **`\b`** word edge; **`\B`** not a word edge (`Script` inside `JavaScript`).
- [x] **`(?=…)` / `(?!…)`** lookahead. **`(?<=…)` / `(?<!…)`** lookbehind.
- [x] Lookarounds do **not** appear in the match array — only the consumed text does.
- [x] The Tryit’s **`(?=)`** is empty (always true). Use a filled lookahead to test a following string.

<a id="js-regexp-assertions-example-01"></a>

### **Example 1: ^ — beginning (true)**

- [x] **`^`** is a **string** (or line, with **`m`**) boundary — it consumes no characters.

Sandbox: `code_sandbox/js-regexp-assertions/hat-true.html`

```javascript
const pattern = /^W3Schools/;
let text = "W3Schools tutorial";
let result = pattern.test(text);
```

![js-regexp-assertions example 1 source](../code_sandbox/snaps/js-regexp-assertions-01-code.png)

![js-regexp-assertions example 1 result](../code_sandbox/snaps/js-regexp-assertions-01-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-assertions-example-02"></a>

### **Example 2: ^ — beginning (false)**

- [x] `Hello W3Schools` does not start with `W3Schools`.

Sandbox: `code_sandbox/js-regexp-assertions/hat-false.html`

```javascript
const pattern = /^W3Schools/;
let text = "Hello W3Schools";
let result = pattern.test(text);
```

![js-regexp-assertions example 2 source](../code_sandbox/snaps/js-regexp-assertions-02-code.png)

![js-regexp-assertions example 2 result](../code_sandbox/snaps/js-regexp-assertions-02-result.png)

- [x] **Outcome:** **false**.

<a id="js-regexp-assertions-example-03"></a>

### **Example 3: $ — end (true)**

- [x] **`$`** matches the end of the string.

Sandbox: `code_sandbox/js-regexp-assertions/dollar-true.html`

```javascript
const pattern = /W3Schools$/;
let text = "Hello W3Schools";
let result = pattern.test(text);
```

![js-regexp-assertions example 3 source](../code_sandbox/snaps/js-regexp-assertions-03-code.png)

![js-regexp-assertions example 3 result](../code_sandbox/snaps/js-regexp-assertions-03-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-assertions-example-04"></a>

### **Example 4: $ — end (false)**

- [x] `W3Schools tutorial` does not **end** with `W3Schools`.

Sandbox: `code_sandbox/js-regexp-assertions/dollar-false.html`

```javascript
const pattern = /W3Schools$/;
let text = "W3Schools tutorial";
let result = pattern.test(text);
```

![js-regexp-assertions example 4 source](../code_sandbox/snaps/js-regexp-assertions-04-code.png)

![js-regexp-assertions example 4 result](../code_sandbox/snaps/js-regexp-assertions-04-result.png)

- [x] **Outcome:** **false**.

<a id="js-regexp-assertions-example-05"></a>

### **Example 5: \bLO — word boundary at start of LO**

- [x] **`\b`** is a **word boundary** (between `\w` and `\W`, or at the string edge).
- [x] `search(/\bLO/)` finds **LOOK**, not the `LO` inside **HELLO**.

Sandbox: `code_sandbox/js-regexp-assertions/word-boundary-start.html`

```javascript
let text = "HELLO, LOOK AT YOU!";
let result = text.search(/\bLO/);
```

![js-regexp-assertions example 5 source](../code_sandbox/snaps/js-regexp-assertions-05-code.png)

![js-regexp-assertions example 5 result](../code_sandbox/snaps/js-regexp-assertions-05-result.png)

- [x] **Outcome:** **7** — index of **LOOK** (`HELLO, ` is 7 characters).

<a id="js-regexp-assertions-example-06"></a>

### **Example 6: LO\b — word boundary at end of LO**

- [x] **`LO\b`** wants `LO` at the **end** of a word.
- [x] That is the **LO** ending **HELLO** (before the comma).

Sandbox: `code_sandbox/js-regexp-assertions/word-boundary-end.html`

```javascript
let text = "HELLO, LOOK AT YOU!";
let result = text.search(/LO\b/);
```

![js-regexp-assertions example 6 source](../code_sandbox/snaps/js-regexp-assertions-06-code.png)

![js-regexp-assertions example 6 result](../code_sandbox/snaps/js-regexp-assertions-06-result.png)

- [x] **Outcome:** **3** — `LO` in **HELLO** starting at index 3.

<a id="js-regexp-assertions-example-07"></a>

### **Example 7: \B — not a word boundary**

- [x] **`\B`** is the opposite of **`\b`**. No Tryit on the table — still run it.
- [x] `JavaScript` has no boundary before **Script**; `Hello Script` would.

Sandbox: `code_sandbox/js-regexp-assertions/not-word-boundary.html`

```javascript
let text = "JavaScript";
let result = text.match(/\BScript/);
let edge = text.match(/\bScript/);
```

![js-regexp-assertions example 7 source](../code_sandbox/snaps/js-regexp-assertions-07-code.png)

![js-regexp-assertions example 7 result](../code_sandbox/snaps/js-regexp-assertions-07-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["Script"]**. `edge` is **null**.

<a id="js-regexp-assertions-example-08"></a>

### **Example 8: (?=) empty lookahead — Tryit**

- [x] The Tryit compiles **`W3Schools(?=) Tutorials`** — an **empty** lookahead.
- [x] An empty `(?=)` always succeeds, so this is just `W3Schools Tutorials`.

Sandbox: `code_sandbox/js-regexp-assertions/lookahead-empty-tryit.html`

```javascript
let text = "W3Schools Tutorials";
let pattern = new RegExp("W3Schools(?=) Tutorials");
let result = pattern.test(text);
```

![js-regexp-assertions example 8 source](../code_sandbox/snaps/js-regexp-assertions-08-code.png)

![js-regexp-assertions example 8 result](../code_sandbox/snaps/js-regexp-assertions-08-result.png)

- [x] **Outcome:** **true** (empty lookahead does not test a following string).

<a id="js-regexp-assertions-example-09"></a>

### **Example 9: (?=...) — subsequent string**

- [x] **`(?=...)`** is a **lookahead**: the following text must match, but is **not consumed**.
- [x] `match` returns **["W3Schools"]**, not the trailing ` Tutorials`.

Sandbox: `code_sandbox/js-regexp-assertions/lookahead-filled.html`

```javascript
let text = "W3Schools Tutorials";
const pattern = /W3Schools(?= Tutorials)/;
let result = text.match(pattern);
```

![js-regexp-assertions example 9 source](../code_sandbox/snaps/js-regexp-assertions-09-code.png)

![js-regexp-assertions example 9 result](../code_sandbox/snaps/js-regexp-assertions-09-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**.

<a id="js-regexp-assertions-example-10"></a>

### **Example 10: (?!...) — not the subsequent string**

- [x] **`(?!...)`** succeeds only if the following text does **not** match.

Sandbox: `code_sandbox/js-regexp-assertions/neg-lookahead.html`

```javascript
let text = "W3Schools Tutorials";
let pattern = /W3Schools(?! Tutorials)/;
let result = pattern.test(text);
```

![js-regexp-assertions example 10 source](../code_sandbox/snaps/js-regexp-assertions-10-code.png)

![js-regexp-assertions example 10 result](../code_sandbox/snaps/js-regexp-assertions-10-result.png)

- [x] **Outcome:** **false** — the text **is** followed by ` Tutorials`.

<a id="js-regexp-assertions-example-11"></a>

### **Example 11: (?<=...) — previous string**

- [x] **`(?<=...)`** is a **lookbehind** (ES2018): previous text must match, not consumed.

Sandbox: `code_sandbox/js-regexp-assertions/lookbehind.html`

```javascript
let text = "Hello W3Schools";
let pattern = /(?<=Hello )W3Schools/;
let result = pattern.test(text);
```

![js-regexp-assertions example 11 source](../code_sandbox/snaps/js-regexp-assertions-11-code.png)

![js-regexp-assertions example 11 result](../code_sandbox/snaps/js-regexp-assertions-11-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-assertions-example-12"></a>

### **Example 12: (?<!...) — not the previous string**

- [x] **`(?<!...)`** succeeds only if the previous text does **not** match.

Sandbox: `code_sandbox/js-regexp-assertions/neg-lookbehind.html`

```javascript
let text = "Hello W3Schools";
let pattern = /(?<!Hello )W3Schools/;
let result = pattern.test(text);
```

![js-regexp-assertions example 12 source](../code_sandbox/snaps/js-regexp-assertions-12-code.png)

![js-regexp-assertions example 12 result](../code_sandbox/snaps/js-regexp-assertions-12-result.png)

- [x] **Outcome:** **false** — it **is** preceded by `Hello `.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-regexp-assertions/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does `^W3Schools` match `Hello W3Schools`?

<details>
<summary>Answer</summary>

- [x] **false**.

</details>

### Question 2: Does `W3Schools$` match `Hello W3Schools`?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 3: Where is `\bLO` in `HELLO, LOOK AT YOU!`?

<details>
<summary>Answer</summary>

- [x] Index **7** — **LOOK**, not the `LO` in HELLO.

</details>

### Question 4: Where is `LO\b`?

<details>
<summary>Answer</summary>

- [x] Index **3** — the `LO` ending **HELLO**.

</details>

### Question 5: Does `\bScript` match `JavaScript`?

<details>
<summary>Answer</summary>

- [x] **null**. **`\BScript`** matches **["Script"]**.

</details>

### Question 6: What does the Tryit `W3Schools(?=) Tutorials` test?

<details>
<summary>Answer</summary>

- [x] An **empty** lookahead. **true**, but it does not check a following word.

</details>

### Question 7: What does `W3Schools(?= Tutorials)` match?

<details>
<summary>Answer</summary>

- [x] **["W3Schools"]** — lookahead is not consumed.

</details>

### Question 8: What is `W3Schools(?! Tutorials)` on that string?

<details>
<summary>Answer</summary>

- [x] **false** / **null** — it **is** followed by ` Tutorials`.

</details>

### Question 9: What is `(?<=Hello )W3Schools` on `Hello W3Schools`?

<details>
<summary>Answer</summary>

- [x] **true** / **["W3Schools"]**.

</details>

### Question 10: What is `(?<!Hello )W3Schools` on that string?

<details>
<summary>Answer</summary>

- [x] **false** / **null**.

</details>


</details>

## Summary

Assertions check a place in the string. Anchors (^ $) and word boundaries (\b \B) are positions. Lookaheads and lookbehinds inspect neighbors without eating them. Do not copy the empty (?=) Tryit when you meant to require a following word.

## References

- [JS RegExp Assertions (W3Schools)](https://www.w3schools.com/js/js_regexp_assertions.asp)
- [MDN: Assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions)
