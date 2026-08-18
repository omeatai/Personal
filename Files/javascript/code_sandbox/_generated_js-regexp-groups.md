<details>
  <summary>JS RegExp Groups</summary>

## Introduction

Groups treat several tokens as one unit. (x) captures into the match array (index 0 = full match). (?<name>x) also fills match.groups. (?:x) groups without capturing. Lookahead/lookbehind are grouped assertions. (?i:x) / (?-i:x) are ES2025 group flag modifiers. Backreferences (\1) replay a capture. match and exec both return the same shape without /g; JSON.stringify hides index/input.

This section has **12** examples:

- [x] **Example 1:** match — capturing groups (x) [View](#js-regexp-groups-example-01)
- [x] **Example 2:** exec — capturing groups (Tryit period) [View](#js-regexp-groups-example-02)
- [x] **Example 3:** exec — capturing groups (Tryit hyphen) [View](#js-regexp-groups-example-03)
- [x] **Example 4:** (\d{4})-(\d{2})-(\d{2}) — result array indices [View](#js-regexp-groups-example-04)
- [x] **Example 5:** (?<name>x) — named capturing groups [View](#js-regexp-groups-example-05)
- [x] **Example 6:** (?:x) — non-capturing group [View](#js-regexp-groups-example-06)
- [x] **Example 7:** (?=x) — lookahead group [View](#js-regexp-groups-example-07)
- [x] **Example 8:** (?<=x) — lookbehind group [View](#js-regexp-groups-example-08)
- [x] **Example 9:** (?i:x) — enable flag in group [View](#js-regexp-groups-example-09)
- [x] **Example 10:** (?i:x) — enable flag, tail fails [View](#js-regexp-groups-example-10)
- [x] **Example 11:** (?-i:x) — disable flag in group [View](#js-regexp-groups-example-11)
- [x] **Example 12:** \1 — backreference [View](#js-regexp-groups-example-12)

## Detailed Explanation

- [x] **`(x)`** capture. **`(?:x)`** group only. **`(?<name>x)`** named (`.groups`).
- [x] `match` / `exec` without **`g`**: `[full, cap1, cap2, …]`.
- [x] **`(?=x)` / `(?<=x)`** assert; they do not add extra captures of the peek.
- [x] **`(?i:x)`** enables **`i`** in the group. **`(?-i:x)`** can disable it.
- [x] **`\1`** is a backreference to capture 1.

<a id="js-regexp-groups-example-01"></a>

### **Example 1: match — capturing groups (x)**

- [x] **`(x)`** captures. `match` without **`g`** puts the full match at **[0]**, then groups.
- [x] This is the page’s `text.match` snippet (the Tryits both use `exec`).

Sandbox: `code_sandbox/js-regexp-groups/capturing-match.html`

```javascript
let text = "Alice loves Bob-";
const pattern = /(\w+) loves (\w+)/;
let result = text.match(pattern);
```

<img alt="js-regexp-groups example 1 source" src="./code_sandbox/snaps/js-regexp-groups-01-code.png" />

<img alt="js-regexp-groups example 1 result" src="./code_sandbox/snaps/js-regexp-groups-01-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["Alice loves Bob","Alice","Bob"]**. The hyphen is outside the match.

<a id="js-regexp-groups-example-02"></a>

### **Example 2: exec — capturing groups (Tryit period)**

- [x] `RegExp.exec(text)` also returns **[full, group1, group2, …]** (or **null**).
- [x] This Tryit uses `Alice loves Bob.`

Sandbox: `code_sandbox/js-regexp-groups/capturing-exec-dot.html`

```javascript
let text = "Alice loves Bob.";
const pattern = /(\w+) loves (\w+)/;
let result = pattern.exec(text);
```

<img alt="js-regexp-groups example 2 source" src="./code_sandbox/snaps/js-regexp-groups-02-code.png" />

<img alt="js-regexp-groups example 2 result" src="./code_sandbox/snaps/js-regexp-groups-02-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["Alice loves Bob","Alice","Bob"]**. `result.index` is **0**.

<a id="js-regexp-groups-example-03"></a>

### **Example 3: exec — capturing groups (Tryit hyphen)**

- [x] Second Tryit: `Alice loves Bob-`. Same groups; punctuation after **Bob** is not captured.

Sandbox: `code_sandbox/js-regexp-groups/capturing-exec-hyphen.html`

```javascript
let text = "Alice loves Bob-";
const pattern = /(\w+) loves (\w+)/;
let result = pattern.exec(text);
```

<img alt="js-regexp-groups example 3 source" src="./code_sandbox/snaps/js-regexp-groups-03-code.png" />

<img alt="js-regexp-groups example 3 result" src="./code_sandbox/snaps/js-regexp-groups-03-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["Alice loves Bob","Alice","Bob"]**.

<a id="js-regexp-groups-example-04"></a>

### **Example 4: (\d{4})-(\d{2})-(\d{2}) — result array indices**

- [x] The page’s date demo: **[0]** whole match, **[1..n]** parenthesis groups.

Sandbox: `code_sandbox/js-regexp-groups/result-array-date.html`

```javascript
const regex = /(\d{4})-(\d{2})-(\d{2})/;
const text = "2026-05-21";
const result = text.match(regex);
```

<img alt="js-regexp-groups example 4 source" src="./code_sandbox/snaps/js-regexp-groups-04-code.png" />

<img alt="js-regexp-groups example 4 result" src="./code_sandbox/snaps/js-regexp-groups-04-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["2026-05-21","2026","05","21"]**.

<a id="js-regexp-groups-example-05"></a>

### **Example 5: (?<name>x) — named capturing groups**

- [x] **`(?<name>x)`** stores captures on **`match.groups`** (ES2018).
- [x] The Tryit prints only `lastName`; this sandbox JSON-prints the groups object too.

Sandbox: `code_sandbox/js-regexp-groups/named-groups.html`

```javascript
const text = "Name: John Doe";
const regex = /(?<firstName>\w+) (?<lastName>\w+)/;
const result = text.match(regex);
let fName = result.groups.firstName;
let lName = result.groups.lastName;
```

<img alt="js-regexp-groups example 5 source" src="./code_sandbox/snaps/js-regexp-groups-05-code.png" />

<img alt="js-regexp-groups example 5 result" src="./code_sandbox/snaps/js-regexp-groups-05-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["John Doe","John","Doe"]**. `groups` is **{"firstName":"John","lastName":"Doe"}**.

<a id="js-regexp-groups-example-06"></a>

### **Example 6: (?:x) — non-capturing group**

- [x] **`(?:x)`** groups for quantifiers **without** creating a capture.
- [x] `/(?:ha)+/` vs `/(ha)+/` on `hahaha`.

Sandbox: `code_sandbox/js-regexp-groups/non-capturing.html`

```javascript
let text = "hahaha";
let result = text.match(/(?:ha)+/);
let cap = text.match(/(ha)+/);
```

<img alt="js-regexp-groups example 6 source" src="./code_sandbox/snaps/js-regexp-groups-06-code.png" />

<img alt="js-regexp-groups example 6 result" src="./code_sandbox/snaps/js-regexp-groups-06-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["hahaha"]** (no group 1). `cap` is **["hahaha","ha"]** (last `ha` is group 1).

<a id="js-regexp-groups-example-07"></a>

### **Example 7: (?=x) — lookahead group**

- [x] Lookahead is listed as a group type: it **asserts**, it does **not** capture the peek.

Sandbox: `code_sandbox/js-regexp-groups/group-lookahead.html`

```javascript
let text = "W3Schools Tutorials";
let result = text.match(/W3Schools(?= Tutorials)/);
```

<img alt="js-regexp-groups example 7 source" src="./code_sandbox/snaps/js-regexp-groups-07-code.png" />

<img alt="js-regexp-groups example 7 result" src="./code_sandbox/snaps/js-regexp-groups-07-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**.

<a id="js-regexp-groups-example-08"></a>

### **Example 8: (?<=x) — lookbehind group**

- [x] Lookbehind asserts the **previous** text; the match is still only `W3Schools`.

Sandbox: `code_sandbox/js-regexp-groups/group-lookbehind.html`

```javascript
let text = "Hello W3Schools";
let result = text.match(/(?<=Hello )W3Schools/);
```

<img alt="js-regexp-groups example 8 source" src="./code_sandbox/snaps/js-regexp-groups-08-code.png" />

<img alt="js-regexp-groups example 8 result" src="./code_sandbox/snaps/js-regexp-groups-08-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**.

<a id="js-regexp-groups-example-09"></a>

### **Example 9: (?i:x) — enable flag in group**

- [x] **`(?flag:x)`** enables flag(s) for **`x` only**.

Sandbox: `code_sandbox/js-regexp-groups/flag-enable.html`

```javascript
let text = "W3Schools tutorials.";
const pattern = /(?i:W3Schools) tutorials/;
let result = pattern.test(text);
```

<img alt="js-regexp-groups example 9 source" src="./code_sandbox/snaps/js-regexp-groups-09-code.png" />

<img alt="js-regexp-groups example 9 result" src="./code_sandbox/snaps/js-regexp-groups-09-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-groups-example-10"></a>

### **Example 10: (?i:x) — enable flag, tail fails**

- [x] Second Tryit: capital **Tutorials** vs lowercase ` tutorials`.

Sandbox: `code_sandbox/js-regexp-groups/flag-enable-false.html`

```javascript
let text = "W3Schools Tutorials.";
const pattern = /(?i:W3Schools) tutorials/;
let result = pattern.test(text);
```

<img alt="js-regexp-groups example 10 source" src="./code_sandbox/snaps/js-regexp-groups-10-code.png" />

<img alt="js-regexp-groups example 10 result" src="./code_sandbox/snaps/js-regexp-groups-10-result.png" />

- [x] **Outcome:** **false**.

<a id="js-regexp-groups-example-11"></a>

### **Example 11: (?-i:x) — disable flag in group**

- [x] **`(?flag-flag:x)`** can **turn off** a flag inside a group.
- [x] No Tryit on the page. Pattern is **`/(?-i:W3Schools) tutorials/i`** — outer **`i`**, group turns **`i` off**.

Sandbox: `code_sandbox/js-regexp-groups/flag-disable.html`

```javascript
let text = "w3schools tutorials";
const pattern = /(?-i:W3Schools) tutorials/i;
let result = pattern.test(text);
```

<img alt="js-regexp-groups example 11 source" src="./code_sandbox/snaps/js-regexp-groups-11-code.png" />

<img alt="js-regexp-groups example 11 result" src="./code_sandbox/snaps/js-regexp-groups-11-result.png" />

- [x] **Outcome:** **false** if modifier groups work — `W3Schools` is case-sensitive inside the group, so `w3schools` fails. Engines without ES2025 modifiers report **SyntaxError: Invalid group**.

<a id="js-regexp-groups-example-12"></a>

### **Example 12: \1 — backreference**

- [x] Capturing groups can be **replayed** with **`\1`**, **`\2`**, …
- [x] `(\w+)\s+\1` matches a word, space, and **the same** word again.

Sandbox: `code_sandbox/js-regexp-groups/backreference.html`

```javascript
let text = "hello hello";
let result = text.match(/(\w+)\s+\1/);
let miss = "hello world".match(/(\w+)\s+\1/);
```

<img alt="js-regexp-groups example 12 source" src="./code_sandbox/snaps/js-regexp-groups-12-code.png" />

<img alt="js-regexp-groups example 12 result" src="./code_sandbox/snaps/js-regexp-groups-12-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["hello hello","hello"]**. `miss` is **null**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-regexp-groups/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Where is the full match in the result array?

<details>
<summary>Answer</summary>

- [x] **Index 0**. Groups follow at **1, 2, …**.

</details>

### Question 2: What does `/(\w+) loves (\w+)/` capture in `Alice loves Bob-`?

<details>
<summary>Answer</summary>

- [x] **["Alice loves Bob","Alice","Bob"]**.

</details>

### Question 3: Does `exec` differ from `match` without `/g`?

<details>
<summary>Answer</summary>

- [x] Same captures. `exec` is a **RegExp** method; `match` is a **string** method.

</details>

### Question 4: How do you read named groups?

<details>
<summary>Answer</summary>

- [x] **`match.groups.firstName`** — here **John** and **Doe**.

</details>

### Question 5: Why use `(?:ha)+`?

<details>
<summary>Answer</summary>

- [x] Repeat **`ha`** without a capture. Result **["hahaha"]**, not an extra **`ha`** group.

</details>

### Question 6: Does lookahead add a group?

<details>
<summary>Answer</summary>

- [x] **No.** `/W3Schools(?= Tutorials)/` → **["W3Schools"]**.

</details>

### Question 7: Does `(?i:W3Schools) tutorials` match `W3Schools Tutorials.`?

<details>
<summary>Answer</summary>

- [x] **false** — ` tutorials` stays case-sensitive.

</details>

### Question 8: What does `(?-i:W3Schools)` do inside `/i`?

<details>
<summary>Answer</summary>

- [x] Turns **case-sensitivity back on** for that group (ES2025).

</details>

### Question 9: What does `(\w+)\s+\1` match?

<details>
<summary>Answer</summary>

- [x] A word repeated: **["hello hello","hello"]**. `hello world` is **null**.

</details>

### Question 10: Which flags are legal in group modifiers?

<details>
<summary>Answer</summary>

- [x] **`i`**, **`m`**, **`s`**.

</details>


</details>

## Summary

Use (x) to extract, (?:x) to structure, (?<name>x) to label, lookaround to assert, and \1 to repeat a capture. match/exec share the [full, groups…] shape without /g. Inline (?i:…) is ES2025.

## References

- [JS RegExp Groups (W3Schools)](https://www.w3schools.com/js/js_regexp_groups.asp)
- [MDN: Groups and backreferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences)

</details>
