<details>
  <summary>JS RegExp Flags</summary>

## Introduction

Flags sit after the closing slash and change how a pattern runs. /g finds all matches. /i ignores case. /d adds result.indices. /s (dotAll) lets the dot match newlines. /m makes ^ and $ line-aware. /y (sticky) matches only at lastIndex. /u and /v enable Unicode (v adds set notation and \p{}). Group modifiers (?i:…) apply flags to part of a pattern (ES2025). Each flag also has a boolean property (global, ignoreCase, …).

This section has **21** examples:

- [x] **Example 1:** /is/g — global [View](#js-regexp-flags-example-01)
- [x] **Example 2:** /w3schools/i — insensitive [View](#js-regexp-flags-example-02)
- [x] **Example 3:** /(aa)(bb)/d — indices [View](#js-regexp-flags-example-03)
- [x] **Example 4:** /Line./gs — dotAll [View](#js-regexp-flags-example-04)
- [x] **Example 5:** /^is/m — multiline [View](#js-regexp-flags-example-05)
- [x] **Example 6:** /\w+/y — sticky from lastIndex [View](#js-regexp-flags-example-06)
- [x] **Example 7:** /\w+/ without y — lastIndex ignored [View](#js-regexp-flags-example-07)
- [x] **Example 8:** /\u{04DC0}/u — Unicode code point [View](#js-regexp-flags-example-08)
- [x] **Example 9:** /\u{04DC0}/ without u [View](#js-regexp-flags-example-09)
- [x] **Example 10:** /\p{Emoji}/v — Unicode sets [View](#js-regexp-flags-example-10)
- [x] **Example 11:** /\p{Emoji}/ without v [View](#js-regexp-flags-example-11)
- [x] **Example 12:** (?i:W3Schools) tutorials — inline i (true) [View](#js-regexp-flags-example-12)
- [x] **Example 13:** (?i:W3Schools) tutorials — inline i (false) [View](#js-regexp-flags-example-13)
- [x] **Example 14:** pattern.dotAll [View](#js-regexp-flags-example-14)
- [x] **Example 15:** pattern.global [View](#js-regexp-flags-example-15)
- [x] **Example 16:** pattern.hasIndices [View](#js-regexp-flags-example-16)
- [x] **Example 17:** pattern.ignoreCase [View](#js-regexp-flags-example-17)
- [x] **Example 18:** pattern.multiline [View](#js-regexp-flags-example-18)
- [x] **Example 19:** pattern.sticky [View](#js-regexp-flags-example-19)
- [x] **Example 20:** pattern.unicode [View](#js-regexp-flags-example-20)
- [x] **Example 21:** pattern.unicodeSets [View](#js-regexp-flags-example-21)

## Detailed Explanation

- [x] **`/g`** find all. **`/i`** ignore case. **`/m`** `^`$` per line. **`/s`** dot matches newline.
- [x] **`/y`** sticky at **`lastIndex`**. Without **`y`**, `String.match` ignores `lastIndex`.
- [x] **`/d`** adds **`indices`**. **`/u`** Unicode code points. **`/v`** Unicode sets.
- [x] Without **`u`/`v`**, `/\p{Emoji}/` is the source **`p{Emoji}`** and `test` is **false**.
- [x] `/\u{04DC0}/` **without** `/u` is **true** in this V8 (the page said false).
- [x] **`(?i:…)`** is a group modifier (ES2025). Properties: `global`, `dotAll`, `unicodeSets`, …

<a id="js-regexp-flags-example-01"></a>

### **Example 1: /is/g — global**

- [x] **`/g`** finds **all** matches. `match` then returns an array of strings.
- [x] Case-sensitive: **`Is`** is not **`is`**.

Sandbox: `code_sandbox/js-regexp-flags/flag-g.html`

```javascript
let text = "Is this all there is?";
const pattern = /is/g;
let result = text.match(pattern);
```

<img alt="js-regexp-flags example 1 source" src="./code_sandbox/snaps/js-regexp-flags-01-code.png" />

<img alt="js-regexp-flags example 1 result" src="./code_sandbox/snaps/js-regexp-flags-01-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["is","is"]**.

<a id="js-regexp-flags-example-02"></a>

### **Example 2: /w3schools/i — insensitive**

- [x] **`/i`** ignores case.

Sandbox: `code_sandbox/js-regexp-flags/flag-i.html`

```javascript
let text = "Visit W3Schools";
const pattern = /w3schools/i;
let result = text.match(pattern);
```

<img alt="js-regexp-flags example 2 source" src="./code_sandbox/snaps/js-regexp-flags-02-code.png" />

<img alt="js-regexp-flags example 2 result" src="./code_sandbox/snaps/js-regexp-flags-02-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**.

<a id="js-regexp-flags-example-03"></a>

### **Example 3: /(aa)(bb)/d — indices**

- [x] **`/d`** (hasIndices) adds **`result.indices`**: `[start, end)` pairs per group.
- [x] It does **not** change what text matches. `aaaabb` matches **`aabb`** at index **2**.

Sandbox: `code_sandbox/js-regexp-flags/flag-d.html`

```javascript
let text = "aaaabb";
const pattern = /(aa)(bb)/d;
let result = text.match(pattern);
let indexes = result.indices;
```

<img alt="js-regexp-flags example 3 source" src="./code_sandbox/snaps/js-regexp-flags-03-code.png" />

<img alt="js-regexp-flags example 3 result" src="./code_sandbox/snaps/js-regexp-flags-03-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["aabb","aa","bb"]**. `indices` is **[[2,6],[2,4],[4,6]]**.

<a id="js-regexp-flags-example-04"></a>

### **Example 4: /Line./gs — dotAll**

- [x] **`/s`** lets **`.`** match line terminators.
- [x] Combined with **`g`**: `Line\n` and `Line.`.

Sandbox: `code_sandbox/js-regexp-flags/flag-s.html`

```javascript
let text = "Line\nLine.";
const pattern = /Line./gs;
let result = text.match(pattern);
```

<img alt="js-regexp-flags example 4 source" src="./code_sandbox/snaps/js-regexp-flags-04-code.png" />

<img alt="js-regexp-flags example 4 result" src="./code_sandbox/snaps/js-regexp-flags-04-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["Line\n","Line."]** (the first match includes the newline).

<a id="js-regexp-flags-example-05"></a>

### **Example 5: /^is/m — multiline**

- [x] **`/m`** makes **`^` / `$`** match at **each line** start/end, not only the whole string.
- [x] The Tryit text is `"\nIs th\nis it?"`. **`/^is/m`** is still case-sensitive.

Sandbox: `code_sandbox/js-regexp-flags/flag-m.html`

```javascript
let text = "\nIs th\nis it?";
let result = text.match(/^is/m);
```

<img alt="js-regexp-flags example 5 source" src="./code_sandbox/snaps/js-regexp-flags-05-code.png" />

<img alt="js-regexp-flags example 5 result" src="./code_sandbox/snaps/js-regexp-flags-05-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["is"]** (start of the line `is it?`). `Is th` does not match.

<a id="js-regexp-flags-example-06"></a>

### **Example 6: /\w+/y — sticky from lastIndex**

- [x] **`/y`** (sticky) matches **only** at **`lastIndex`**, not later.
- [x] `lastIndex = 4` on `abc def ghi` is the **`d`** of `def`.

Sandbox: `code_sandbox/js-regexp-flags/flag-y.html`

```javascript
let text = "abc def ghi";
const pattern = /\w+/y;
pattern.lastIndex = 4;
let result = text.match(pattern);
```

<img alt="js-regexp-flags example 6 source" src="./code_sandbox/snaps/js-regexp-flags-06-code.png" />

<img alt="js-regexp-flags example 6 result" src="./code_sandbox/snaps/js-regexp-flags-06-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["def"]**. After the match, `lastIndex` is **7**.

<a id="js-regexp-flags-example-07"></a>

### **Example 7: /\w+/ without y — lastIndex ignored**

- [x] Without **`y`** (and without using **`exec`/`test` with `g`**), `String.match` does **not** honor `lastIndex`.
- [x] The Tryit still **sets** `lastIndex = 4`, then matches from the start.

Sandbox: `code_sandbox/js-regexp-flags/flag-y-without.html`

```javascript
let text = "abc def ghi";
const pattern = /\w+/;
pattern.lastIndex = 4;
let result = text.match(pattern);
```

<img alt="js-regexp-flags example 7 source" src="./code_sandbox/snaps/js-regexp-flags-07-code.png" />

<img alt="js-regexp-flags example 7 result" src="./code_sandbox/snaps/js-regexp-flags-07-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["abc"]**. `lastIndex` stays **4** (unused).

<a id="js-regexp-flags-example-08"></a>

### **Example 8: /\u{04DC0}/u — Unicode code point**

- [x] **`/u`** treats the pattern as Unicode **code points** (not UTF-16 surrogates).
- [x] `\u{04DC0}` is hexagram **䷀** (U+4DC0).

Sandbox: `code_sandbox/js-regexp-flags/flag-u.html`

```javascript
let text = "\u4DC0";
const pattern = /\u{04DC0}/u;
let result = pattern.test(text);
```

<img alt="js-regexp-flags example 8 source" src="./code_sandbox/snaps/js-regexp-flags-08-code.png" />

<img alt="js-regexp-flags example 8 result" src="./code_sandbox/snaps/js-regexp-flags-08-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-flags-example-09"></a>

### **Example 9: /\u{04DC0}/ without u**

- [x] The page says this is **false**. This V8 engine still compiles `\u{04DC0}` to that character.
- [x] Run the engine you ship — do not assume the page’s **false**.

Sandbox: `code_sandbox/js-regexp-flags/flag-u-without.html`

```javascript
let text = "\u4DC0";
const pattern = /\u{04DC0}/;
let result = pattern.test(text);
```

<img alt="js-regexp-flags example 9 source" src="./code_sandbox/snaps/js-regexp-flags-09-code.png" />

<img alt="js-regexp-flags example 9 result" src="./code_sandbox/snaps/js-regexp-flags-09-result.png" />

- [x] **Outcome:** **true** in this V8 (the pattern source is the hexagram). The page’s **false** is outdated here.

<a id="js-regexp-flags-example-10"></a>

### **Example 10: /\p{Emoji}/v — Unicode sets**

- [x] **`/v`** is an upgrade to **`/u`**: Unicode property escapes and set notation.
- [x] `\p{Emoji}` matches emoji (needs **`u`** or **`v`**).

Sandbox: `code_sandbox/js-regexp-flags/flag-v.html`

```javascript
let text = "Hello \u{1F604}";
const pattern = /\p{Emoji}/v;
let result = pattern.test(text);
```

<img alt="js-regexp-flags example 10 source" src="./code_sandbox/snaps/js-regexp-flags-10-code.png" />

<img alt="js-regexp-flags example 10 result" src="./code_sandbox/snaps/js-regexp-flags-10-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-flags-example-11"></a>

### **Example 11: /\p{Emoji}/ without v**

- [x] Without **`u`/`v`**, `\p{Emoji}` is **not** a property escape: the source becomes **`p{Emoji}`**.
- [x] That pattern does **not** match the emoji, so `test` is **false** (not a throw).

Sandbox: `code_sandbox/js-regexp-flags/flag-v-without.html`

```javascript
let text = "Hello \u{1F604}";
const pattern = /\p{Emoji}/;
let result = pattern.test(text);
```

<img alt="js-regexp-flags example 11 source" src="./code_sandbox/snaps/js-regexp-flags-11-code.png" />

<img alt="js-regexp-flags example 11 result" src="./code_sandbox/snaps/js-regexp-flags-11-result.png" />

- [x] **Outcome:** **false**. `pattern.source` is **`p{Emoji}`**.

<a id="js-regexp-flags-example-12"></a>

### **Example 12: (?i:W3Schools) tutorials — inline i (true)**

- [x] **`(?flags:pattern)`** turns flags **on** for that group only (ES2025).
- [x] Only **`i`**, **`m`**, and **`s`** are valid group modifiers.

Sandbox: `code_sandbox/js-regexp-flags/group-modifier-true.html`

```javascript
let text = "W3Schools tutorials.";
const pattern = /(?i:W3Schools) tutorials/;
let result = pattern.test(text);
```

<img alt="js-regexp-flags example 12 source" src="./code_sandbox/snaps/js-regexp-flags-12-code.png" />

<img alt="js-regexp-flags example 12 result" src="./code_sandbox/snaps/js-regexp-flags-12-result.png" />

- [x] **Outcome:** **true** — the group is case-insensitive; ` tutorials` matches as written.

<a id="js-regexp-flags-example-13"></a>

### **Example 13: (?i:W3Schools) tutorials — inline i (false)**

- [x] `Tutorials` (capital **T**) does **not** match the case-sensitive ` tutorials` tail.
- [x] The **`i`** flag does **not** leak out of the group.

Sandbox: `code_sandbox/js-regexp-flags/group-modifier-false.html`

```javascript
let text = "W3Schools Tutorials.";
const pattern = /(?i:W3Schools) tutorials/;
let result = pattern.test(text);
```

<img alt="js-regexp-flags example 13 source" src="./code_sandbox/snaps/js-regexp-flags-13-code.png" />

<img alt="js-regexp-flags example 13 result" src="./code_sandbox/snaps/js-regexp-flags-13-result.png" />

- [x] **Outcome:** **false**.

<a id="js-regexp-flags-example-14"></a>

### **Example 14: pattern.dotAll**

- [x] **`dotAll`** is **true** when **`/s`** is set.

Sandbox: `code_sandbox/js-regexp-flags/prop-dotall.html`

```javascript
const pattern = /W3Schools/s;
let result = pattern.dotAll;
```

<img alt="js-regexp-flags example 14 source" src="./code_sandbox/snaps/js-regexp-flags-14-code.png" />

<img alt="js-regexp-flags example 14 result" src="./code_sandbox/snaps/js-regexp-flags-14-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-flags-example-15"></a>

### **Example 15: pattern.global**

- [x] **`global`** is **true** when **`/g`** is set.

Sandbox: `code_sandbox/js-regexp-flags/prop-global.html`

```javascript
const pattern = /W3Schools/g;
let result = pattern.global;
```

<img alt="js-regexp-flags example 15 source" src="./code_sandbox/snaps/js-regexp-flags-15-code.png" />

<img alt="js-regexp-flags example 15 result" src="./code_sandbox/snaps/js-regexp-flags-15-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-flags-example-16"></a>

### **Example 16: pattern.hasIndices**

- [x] **`hasIndices`** is **true** when **`/d`** is set.

Sandbox: `code_sandbox/js-regexp-flags/prop-hasindices.html`

```javascript
const pattern = /W3Schools/d;
let result = pattern.hasIndices;
```

<img alt="js-regexp-flags example 16 source" src="./code_sandbox/snaps/js-regexp-flags-16-code.png" />

<img alt="js-regexp-flags example 16 result" src="./code_sandbox/snaps/js-regexp-flags-16-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-flags-example-17"></a>

### **Example 17: pattern.ignoreCase**

- [x] **`ignoreCase`** is **true** when **`/i`** is set.

Sandbox: `code_sandbox/js-regexp-flags/prop-ignorecase.html`

```javascript
const pattern = /W3Schools/i;
let result = pattern.ignoreCase;
```

<img alt="js-regexp-flags example 17 source" src="./code_sandbox/snaps/js-regexp-flags-17-code.png" />

<img alt="js-regexp-flags example 17 result" src="./code_sandbox/snaps/js-regexp-flags-17-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-flags-example-18"></a>

### **Example 18: pattern.multiline**

- [x] **`multiline`** is **true** when **`/m`** is set.

Sandbox: `code_sandbox/js-regexp-flags/prop-multiline.html`

```javascript
const pattern = /W3Schools/m;
let result = pattern.multiline;
```

<img alt="js-regexp-flags example 18 source" src="./code_sandbox/snaps/js-regexp-flags-18-code.png" />

<img alt="js-regexp-flags example 18 result" src="./code_sandbox/snaps/js-regexp-flags-18-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-flags-example-19"></a>

### **Example 19: pattern.sticky**

- [x] **`sticky`** is **true** when **`/y`** is set.

Sandbox: `code_sandbox/js-regexp-flags/prop-sticky.html`

```javascript
const pattern = /W3Schools/y;
let result = pattern.sticky;
```

<img alt="js-regexp-flags example 19 source" src="./code_sandbox/snaps/js-regexp-flags-19-code.png" />

<img alt="js-regexp-flags example 19 result" src="./code_sandbox/snaps/js-regexp-flags-19-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-flags-example-20"></a>

### **Example 20: pattern.unicode**

- [x] **`unicode`** is **true** when **`/u`** is set.

Sandbox: `code_sandbox/js-regexp-flags/prop-unicode.html`

```javascript
let text = "\u4DC0";
const pattern = /\u{04DC0}/u;
let result = pattern.unicode;
```

<img alt="js-regexp-flags example 20 source" src="./code_sandbox/snaps/js-regexp-flags-20-code.png" />

<img alt="js-regexp-flags example 20 result" src="./code_sandbox/snaps/js-regexp-flags-20-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-flags-example-21"></a>

### **Example 21: pattern.unicodeSets**

- [x] **`unicodeSets`** is **true** when **`/v`** is set.

Sandbox: `code_sandbox/js-regexp-flags/prop-unicodesets.html`

```javascript
let text = "Hello \u{1F604}";
const pattern = /\p{Emoji}/v;
let result = pattern.unicodeSets;
```

<img alt="js-regexp-flags example 21 source" src="./code_sandbox/snaps/js-regexp-flags-21-code.png" />

<img alt="js-regexp-flags example 21 result" src="./code_sandbox/snaps/js-regexp-flags-21-result.png" />

- [x] **Outcome:** **true**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-regexp-flags/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `/g` change about `match`?

<details>
<summary>Answer</summary>

- [x] It returns **all** matches as strings. `/is/g` on the sample is **["is","is"]**.

</details>

### Question 2: What does `/d` add?

<details>
<summary>Answer</summary>

- [x] **`result.indices`**: `[start, end)` for the match and each group. Here **[[2,6],[2,4],[4,6]]**.

</details>

### Question 3: What does `/s` do to `.`?

<details>
<summary>Answer</summary>

- [x] `.` can match **newlines**. `/Line./gs` → **["Line\n","Line."]**.

</details>

### Question 4: What does `/m` change?

<details>
<summary>Answer</summary>

- [x] **`^` and `$`** match at **line** starts/ends too. `/^is/m` matches `is it?`.

</details>

### Question 5: Does sticky `/y` use `lastIndex`?

<details>
<summary>Answer</summary>

- [x] **Yes.** `lastIndex = 4` + `/\w+/y` → **["def"]**, then `lastIndex` **7**.

</details>

### Question 6: Without `/y`, does `match` use `lastIndex`?

<details>
<summary>Answer</summary>

- [x] **No.** Same `lastIndex = 4` still matches **["abc"]**.

</details>

### Question 7: Does `/\u{04DC0}/` without `u` fail here?

<details>
<summary>Answer</summary>

- [x] **No** — this V8 still matches the hexagram (**true**). The page’s **false** is not what this engine did.

</details>

### Question 8: What is `/\p{Emoji}/` without `v`?

<details>
<summary>Answer</summary>

- [x] Source **`p{Emoji}`**. `test("Hello 😄")` is **false**.

</details>

### Question 9: Does `(?i:W3Schools) tutorials` match `W3Schools Tutorials.`?

<details>
<summary>Answer</summary>

- [x] **No.** Only the group is case-insensitive. The tail ` tutorials` is not.

</details>

### Question 10: Which flags work in `(?flags:…)`?

<details>
<summary>Answer</summary>

- [x] **`i`**, **`m`**, and **`s`** only.

</details>

### Question 11: How do you read flags without matching?

<details>
<summary>Answer</summary>

- [x] Boolean properties: **`global`**, **`ignoreCase`**, **`dotAll`**, **`sticky`**, **`unicode`**, **`unicodeSets`**, **`hasIndices`**, **`multiline`**.

</details>

### Question 12: Is `/v` the same as `/u`?

<details>
<summary>Answer</summary>

- [x] **`v`** is an **upgrade** to **`u`** (sets, `\p{}` on strings). `unicodeSets` is the property.

</details>


</details>

## Summary

Pick flags for the job: g for all matches, i for case, m for line anchors, s for dot-newline, y for sticky lastIndex, d for indices, u/v for Unicode. Read them back with the boolean properties. Group modifiers scope i/m/s to part of a pattern.

## References

- [JS RegExp Flags (W3Schools)](https://www.w3schools.com/js/js_regexp_flags.asp)
- [MDN: RegExp flags](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags)
- [MDN: RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)

</details>
