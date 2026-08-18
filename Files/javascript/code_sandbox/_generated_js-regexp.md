<details>
  <summary>JS RegExp</summary>

## Introduction

A regular expression is a search pattern. JavaScript’s RegExp object is used with string methods (search, match, replace) and with RegExp.test / exec. The literal form is /pattern/flags. This landing page is a tour: case-insensitive search, match/replace, alternation with |, the g and i flags, \d and \w, the ? quantifier, ^ and $, and [0-9]. Later pages expand each topic. match arrays are JSON-stringified so commas inside matches stay visible.

This section has **15** examples:

- [x] **Example 1:** text.search(/w3Schools/i) [View](#js-regexp-example-01)
- [x] **Example 2:** text.match(/W3Schools/) [View](#js-regexp-example-02)
- [x] **Example 3:** text.replace(/Microsoft/, "W3Schools") [View](#js-regexp-example-03)
- [x] **Example 4:** text.search(/W3Schools/) [View](#js-regexp-example-04)
- [x] **Example 5:** /red|green|blue/g — alternation [View](#js-regexp-example-05)
- [x] **Example 6:** /is/g — global [View](#js-regexp-example-06)
- [x] **Example 7:** /w3schools/i — insensitive [View](#js-regexp-example-07)
- [x] **Example 8:** /\d/g — digits [View](#js-regexp-example-08)
- [x] **Example 9:** /\w/g — word characters [View](#js-regexp-example-09)
- [x] **Example 10:** /10?/g — optional 0 [View](#js-regexp-example-10)
- [x] **Example 11:** /^W3Schools/ — starts with (true) [View](#js-regexp-example-11)
- [x] **Example 12:** /^W3Schools/ — starts with (false) [View](#js-regexp-example-12)
- [x] **Example 13:** /W3Schools$/ — ends with (true) [View](#js-regexp-example-13)
- [x] **Example 14:** /W3Schools$/ — ends with (false) [View](#js-regexp-example-14)
- [x] **Example 15:** /[0-9]/g — digit class [View](#js-regexp-example-15)

## Detailed Explanation

- [x] Syntax is **`/pattern/flags`**. **`i`** = ignore case, **`g`** = find all.
- [x] `search` → **index**. `match` → **array or null**. `replace` → **new string**.
- [x] **`|`** is alternation (OR).
- [x] **`\d`** digits, **`\w`** word chars `[A-Za-z0-9_]`.
- [x] **`?`** is zero-or-one of the previous token (`10?` is not “the number ten”).
- [x] **`^` / `$`** are string ends. **`[0-9]`** is a character class.
- [x] `JSON.stringify` on a match array prints captures only — not `index` / `input`.

<a id="js-regexp-example-01"></a>

### **Example 1: text.search(/w3Schools/i)**

- [x] A regex literal is **`/pattern/flags`**. **`i`** makes the search case-insensitive.
- [x] `String.search(regex)` returns the **index** of the first match, or **-1**.

Sandbox: `code_sandbox/js-regexp/search-insensitive.html`

```javascript
let text = "Visit W3Schools!";
let result = text.search(/w3Schools/i);
```

<img alt="js-regexp example 1 source" src="./code_sandbox/snaps/js-regexp-01-code.png" />

<img alt="js-regexp example 1 result" src="./code_sandbox/snaps/js-regexp-01-result.png" />

- [x] **Outcome:** **6** — `W3Schools` starts at index 6 in `Visit W3Schools!`.

<a id="js-regexp-example-02"></a>

### **Example 2: text.match(/W3Schools/)**

- [x] `String.match(regex)` without **`g`** returns one match **array** (or **null**).
- [x] The page snippet used `/W3schools/` (wrong case) which is **null**. This Tryit uses **`/W3Schools/`**.

Sandbox: `code_sandbox/js-regexp/match-first.html`

```javascript
let text = "Visit W3Schools!";
let result = text.match(/W3Schools/);
```

<img alt="js-regexp example 2 source" src="./code_sandbox/snaps/js-regexp-02-code.png" />

<img alt="js-regexp example 2 result" src="./code_sandbox/snaps/js-regexp-02-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**. Extra fields `index` / `input` are omitted by JSON.

<a id="js-regexp-example-03"></a>

### **Example 3: text.replace(/Microsoft/, "W3Schools")**

- [x] `String.replace(regex, s)` returns a **new** string. The original is unchanged.
- [x] This Tryit is **case-sensitive** (no **`i`**).

Sandbox: `code_sandbox/js-regexp/replace-microsoft.html`

```javascript
let text = "Please visit Microsoft!";
let result = text.replace(/Microsoft/, "W3Schools");
```

<img alt="js-regexp example 3 source" src="./code_sandbox/snaps/js-regexp-03-code.png" />

<img alt="js-regexp example 3 result" src="./code_sandbox/snaps/js-regexp-03-result.png" />

- [x] **Outcome:** result is **"Please visit W3Schools!"**.

<a id="js-regexp-example-04"></a>

### **Example 4: text.search(/W3Schools/)**

- [x] `search` without **`i`** is case-sensitive.
- [x] It still returns an **index**, not the matched text.

Sandbox: `code_sandbox/js-regexp/search-exact.html`

```javascript
let text = "Visit W3Schools!";
let result = text.search(/W3Schools/);
```

<img alt="js-regexp example 4 source" src="./code_sandbox/snaps/js-regexp-04-code.png" />

<img alt="js-regexp example 4 result" src="./code_sandbox/snaps/js-regexp-04-result.png" />

- [x] **Outcome:** **6**.

<a id="js-regexp-example-05"></a>

### **Example 5: /red|green|blue/g — alternation**

- [x] **`|`** is OR: match **red** or **green** or **blue**.
- [x] **`g`** finds **all** alternatives, not only the first.

Sandbox: `code_sandbox/js-regexp/alternation-or.html`

```javascript
let text = "Black, white, red, green, blue, yellow.";
let result = text.match(/red|green|blue/g);
```

<img alt="js-regexp example 5 source" src="./code_sandbox/snaps/js-regexp-05-code.png" />

<img alt="js-regexp example 5 result" src="./code_sandbox/snaps/js-regexp-05-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["red","green","blue"]**.

<a id="js-regexp-example-06"></a>

### **Example 6: /is/g — global**

- [x] Without **`g`**, `match` stops at the first `is`.
- [x] **`/is/g`** is case-sensitive, so the leading **`Is`** is skipped.

Sandbox: `code_sandbox/js-regexp/flag-g.html`

```javascript
let text = "Is this all there is?";
const pattern = /is/g;
let result = text.match(pattern);
```

<img alt="js-regexp example 6 source" src="./code_sandbox/snaps/js-regexp-06-code.png" />

<img alt="js-regexp example 6 result" src="./code_sandbox/snaps/js-regexp-06-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["is","is"]** (`this` and the final `is`).

<a id="js-regexp-example-07"></a>

### **Example 7: /w3schools/i — insensitive**

- [x] **`i`** matches any case: `w3schools` finds **`W3Schools`**.

Sandbox: `code_sandbox/js-regexp/flag-i.html`

```javascript
let text = "Visit W3Schools";
const pattern = /w3schools/i;
let result = text.match(pattern);
```

<img alt="js-regexp example 7 source" src="./code_sandbox/snaps/js-regexp-07-code.png" />

<img alt="js-regexp example 7 result" src="./code_sandbox/snaps/js-regexp-07-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**.

<a id="js-regexp-example-08"></a>

### **Example 8: /\d/g — digits**

- [x] **`\d`** matches a digit **0–9**.

Sandbox: `code_sandbox/js-regexp/meta-d.html`

```javascript
let text = "Give 100%!";
const pattern = /\d/g;
let result = text.match(pattern);
```

<img alt="js-regexp example 8 source" src="./code_sandbox/snaps/js-regexp-08-code.png" />

<img alt="js-regexp example 8 result" src="./code_sandbox/snaps/js-regexp-08-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["1","0","0"]**.

<a id="js-regexp-example-09"></a>

### **Example 9: /\w/g — word characters**

- [x] **`\w`** is **`[A-Za-z0-9_]`**. Space, `%`, and `!` are not word characters.

Sandbox: `code_sandbox/js-regexp/meta-w.html`

```javascript
let text = "Give 100%!";
const pattern = /\w/g;
let result = text.match(pattern);
```

<img alt="js-regexp example 9 source" src="./code_sandbox/snaps/js-regexp-09-code.png" />

<img alt="js-regexp example 9 result" src="./code_sandbox/snaps/js-regexp-09-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["G","i","v","e","1","0","0"]**.

<a id="js-regexp-example-10"></a>

### **Example 10: /10?/g — optional 0**

- [x] **`?`** means **zero or one** of the previous token.
- [x] `10?` is a `1` plus an optional `0` — **not** “ten, maybe”.

Sandbox: `code_sandbox/js-regexp/quant-10-optional.html`

```javascript
let text = "1, 100 or 1000?";
const pattern = /10?/g;
let result = text.match(pattern);
```

<img alt="js-regexp example 10 source" src="./code_sandbox/snaps/js-regexp-10-code.png" />

<img alt="js-regexp example 10 result" src="./code_sandbox/snaps/js-regexp-10-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["1","10","10"]** (the lone `1`, then `10` from `100` and `1000`).

<a id="js-regexp-example-11"></a>

### **Example 11: /^W3Schools/ — starts with (true)**

- [x] **`^`** matches the **start** of the string (or of each line with **`m`**).

Sandbox: `code_sandbox/js-regexp/assert-hat-true.html`

```javascript
const pattern = /^W3Schools/;
let text = "W3Schools tutorial";
let result = pattern.test(text);
```

<img alt="js-regexp example 11 source" src="./code_sandbox/snaps/js-regexp-11-code.png" />

<img alt="js-regexp example 11 result" src="./code_sandbox/snaps/js-regexp-11-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-example-12"></a>

### **Example 12: /^W3Schools/ — starts with (false)**

- [x] `Hello W3Schools` does **not** start with `W3Schools`.

Sandbox: `code_sandbox/js-regexp/assert-hat-false.html`

```javascript
const pattern = /^W3Schools/;
let text = "Hello W3Schools";
let result = pattern.test(text);
```

<img alt="js-regexp example 12 source" src="./code_sandbox/snaps/js-regexp-12-code.png" />

<img alt="js-regexp example 12 result" src="./code_sandbox/snaps/js-regexp-12-result.png" />

- [x] **Outcome:** **false**.

<a id="js-regexp-example-13"></a>

### **Example 13: /W3Schools$/ — ends with (true)**

- [x] **`$`** matches the **end** of the string.

Sandbox: `code_sandbox/js-regexp/assert-dollar-true.html`

```javascript
const pattern = /W3Schools$/;
let text = "Hello W3Schools";
let result = pattern.test(text);
```

<img alt="js-regexp example 13 source" src="./code_sandbox/snaps/js-regexp-13-code.png" />

<img alt="js-regexp example 13 result" src="./code_sandbox/snaps/js-regexp-13-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-example-14"></a>

### **Example 14: /W3Schools$/ — ends with (false)**

- [x] `W3Schools tutorial` ends with **tutorial**, not `W3Schools`.

Sandbox: `code_sandbox/js-regexp/assert-dollar-false.html`

```javascript
const pattern = /W3Schools$/;
let text = "W3Schools tutorial";
let result = pattern.test(text);
```

<img alt="js-regexp example 14 source" src="./code_sandbox/snaps/js-regexp-14-code.png" />

<img alt="js-regexp example 14 result" src="./code_sandbox/snaps/js-regexp-14-result.png" />

- [x] **Outcome:** **false**.

<a id="js-regexp-example-15"></a>

### **Example 15: /[0-9]/g — digit class**

- [x] **`[0-9]`** is a character class: any digit. Same idea as **`\d`** for ASCII digits.

Sandbox: `code_sandbox/js-regexp/class-0-9.html`

```javascript
let text = "More than 1000 times";
const pattern = /[0-9]/g;
let result = text.match(pattern);
```

<img alt="js-regexp example 15 source" src="./code_sandbox/snaps/js-regexp-15-code.png" />

<img alt="js-regexp example 15 result" src="./code_sandbox/snaps/js-regexp-15-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["1","0","0","0"]**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-regexp/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a regex literal?

<details>
<summary>Answer</summary>

- [x] **`/pattern/flags`** — slashes around the pattern, then flags like **`i`** or **`g`**.

</details>

### Question 2: What does `search` return?

<details>
<summary>Answer</summary>

- [x] The **index** of the first match, or **-1**. `"Visit W3Schools!".search(/w3Schools/i)` is **6**.

</details>

### Question 3: What does `match` return on a miss?

<details>
<summary>Answer</summary>

- [x] **`null`**, not an empty array. `/W3schools/` on `Visit W3Schools` is **null** (case).

</details>

### Question 4: Does `replace` change the original string?

<details>
<summary>Answer</summary>

- [x] **No.** It returns a **new** string.

</details>

### Question 5: What does `|` mean?

<details>
<summary>Answer</summary>

- [x] **Alternation (OR)**. `/red|green|blue/g` → **["red","green","blue"]**.

</details>

### Question 6: Does `/is/g` match `Is`?

<details>
<summary>Answer</summary>

- [x] **No** — **`g`** is not **`i`**. Result **["is","is"]**.

</details>

### Question 7: What is `\w`?

<details>
<summary>Answer</summary>

- [x] A word character: **letter, digit, or `_`**.

</details>

### Question 8: What does `10?` match in `1, 100 or 1000?`?

<details>
<summary>Answer</summary>

- [x] **["1","10","10"]** — `1` plus an optional `0`.

</details>

### Question 9: When is `^W3Schools` true?

<details>
<summary>Answer</summary>

- [x] When the string **starts** with `W3Schools`. `Hello W3Schools` is **false**.

</details>

### Question 10: When is `W3Schools$` true?

<details>
<summary>Answer</summary>

- [x] When the string **ends** with `W3Schools`.

</details>

### Question 11: Why JSON.stringify match arrays?

<details>
<summary>Answer</summary>

- [x] So you see **["1","0","0"]** instead of `1,0,0`, and **null** stays **null**.

</details>


</details>

## Summary

RegExp is a pattern object used with search, match, replace, test, and exec. Remember /g vs /i, JSON-stringify match arrays, and that ^ $ | [] and the common metacharacters show up on later pages in full.

## References

- [JS RegExp (W3Schools)](https://www.w3schools.com/js/js_regexp.asp)
- [MDN: Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)

</details>
