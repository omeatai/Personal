# JS RegExp Methods

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The complete RegExp reference (revised July 2025) lists instance properties, exec/test, deprecated compile, toString, static escape, and the string methods match/matchAll/replace/replaceAll/search/split. Each row is an Example. lastIndex with /g is shown mutating across exec calls. match with /g drops groups; matchAll keeps them. replace without g changes one hit; replaceAll requires g. compile still runs and must not be used.

This section has **24** examples:

- [x] **Example 1:** compile() — deprecated [View](#js-regexp-methods-example-01)
- [x] **Example 2:** constructor [View](#js-regexp-methods-example-02)
- [x] **Example 3:** dotAll [View](#js-regexp-methods-example-03)
- [x] **Example 4:** escape() — RegExp.escape [View](#js-regexp-methods-example-04)
- [x] **Example 5:** exec() [View](#js-regexp-methods-example-05)
- [x] **Example 6:** flags [View](#js-regexp-methods-example-06)
- [x] **Example 7:** global [View](#js-regexp-methods-example-07)
- [x] **Example 8:** hasIndices [View](#js-regexp-methods-example-08)
- [x] **Example 9:** ignoreCase [View](#js-regexp-methods-example-09)
- [x] **Example 10:** lastIndex [View](#js-regexp-methods-example-10)
- [x] **Example 11:** multiline [View](#js-regexp-methods-example-11)
- [x] **Example 12:** source [View](#js-regexp-methods-example-12)
- [x] **Example 13:** sticky [View](#js-regexp-methods-example-13)
- [x] **Example 14:** test() [View](#js-regexp-methods-example-14)
- [x] **Example 15:** toString() [View](#js-regexp-methods-example-15)
- [x] **Example 16:** unicode [View](#js-regexp-methods-example-16)
- [x] **Example 17:** unicodeSets [View](#js-regexp-methods-example-17)
- [x] **Example 18:** String.match(regexp) [View](#js-regexp-methods-example-18)
- [x] **Example 19:** String.matchAll(regexp) [View](#js-regexp-methods-example-19)
- [x] **Example 20:** String.replace(regexp, s) [View](#js-regexp-methods-example-20)
- [x] **Example 21:** String.replaceAll(regexp, s) [View](#js-regexp-methods-example-21)
- [x] **Example 22:** String.search(regexp) [View](#js-regexp-methods-example-22)
- [x] **Example 23:** String.split(regexp) [View](#js-regexp-methods-example-23)
- [x] **Example 24:** exec vs match with /g [View](#js-regexp-methods-example-24)

## Detailed Explanation

- [x] **Every table row is an Example**, plus **`exec` vs `match` with `/g`**.
- [x] **`compile`** is **deprecated** but still mutates the object here (`/abc/g` → `/def/i`).
- [x] **`lastIndex`** + **`/g`**: exec at 5 → 7, at 18 → 20, null → **0**.
- [x] `match` + **`g`** → strings only. **`matchAll`** → iterator of arrays **with groups** (needs **`g`**).
- [x] `search` → index or **-1**. `split` → pieces. `flags` / `source` / `toString` inspect the pattern.

<a id="js-regexp-methods-example-01"></a>

### **Example 1: compile() — deprecated**

- [x] **Deprecated.** `compile(pattern, flags)` mutates the same RegExp. **Do not use it** in new code.

Sandbox: `code_sandbox/js-regexp-methods/compile.html`

```javascript
const pattern = /abc/g;
pattern.compile("def", "i");
```

![js-regexp-methods example 1 source](../code_sandbox/snaps/js-regexp-methods-01-code.png)

![js-regexp-methods example 1 result](../code_sandbox/snaps/js-regexp-methods-01-result.png)

- [x] **Outcome:** After `compile("def", "i")`, `source` is **"def"**, `flags` is **"i"**, `String(pattern)` is **`/def/i`**. Still **deprecated**.

<a id="js-regexp-methods-example-02"></a>

### **Example 2: constructor**

- [x] Instance **`constructor`** is the function that created the prototype: **`RegExp`**.

Sandbox: `code_sandbox/js-regexp-methods/constructor.html`

```javascript
const pattern = /W3Schools/gi;
const result = pattern.constructor;
```

![js-regexp-methods example 2 source](../code_sandbox/snaps/js-regexp-methods-02-code.png)

![js-regexp-methods example 2 result](../code_sandbox/snaps/js-regexp-methods-02-result.png)

- [x] **Outcome:** `String(pattern.constructor)` is **function RegExp() { [native code] }**. `=== RegExp` is **true**.

<a id="js-regexp-methods-example-03"></a>

### **Example 3: dotAll**

- [x] **`dotAll`** is **true** if **`s`** is set.

Sandbox: `code_sandbox/js-regexp-methods/dotAll.html`

```javascript
const pattern = /W3Schools/s;
let result = pattern.dotAll;
```

![js-regexp-methods example 3 source](../code_sandbox/snaps/js-regexp-methods-03-code.png)

![js-regexp-methods example 3 result](../code_sandbox/snaps/js-regexp-methods-03-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-methods-example-04"></a>

### **Example 4: escape() — RegExp.escape**

- [x] Static **`RegExp.escape`** (ES2025) returns a string safe to embed in a pattern.

Sandbox: `code_sandbox/js-regexp-methods/escape.html`

```javascript
let result;
try {
  result = RegExp.escape("[*]");
} catch (e) {
  result = e.name + ": " + e.message;
}
```

![js-regexp-methods example 4 source](../code_sandbox/snaps/js-regexp-methods-04-code.png)

![js-regexp-methods example 4 result](../code_sandbox/snaps/js-regexp-methods-04-result.png)

- [x] **Outcome:** With ES2025: JSON **`"\\[\\*\\]"`**. Otherwise a **TypeError** / missing-function message.

<a id="js-regexp-methods-example-05"></a>

### **Example 5: exec()**

- [x] `exec` returns a result array for **one** match, or **null**.
- [x] With **`/g`**, it advances **`lastIndex`** (see lastIndex row).

Sandbox: `code_sandbox/js-regexp-methods/exec.html`

```javascript
const result = /e/.exec("The best things in life are free!");
```

![js-regexp-methods example 5 source](../code_sandbox/snaps/js-regexp-methods-05-code.png)

![js-regexp-methods example 5 result](../code_sandbox/snaps/js-regexp-methods-05-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["e"]**. `index` is **2**.

<a id="js-regexp-methods-example-06"></a>

### **Example 6: flags**

- [x] **`flags`** is the modifier letters actually set, in a standard order (e.g. `gim`).

Sandbox: `code_sandbox/js-regexp-methods/flags.html`

```javascript
const pattern = /W3Schools/gim;
let result = pattern.flags;
```

![js-regexp-methods example 6 source](../code_sandbox/snaps/js-regexp-methods-06-code.png)

![js-regexp-methods example 6 result](../code_sandbox/snaps/js-regexp-methods-06-result.png)

- [x] **Outcome:** **"gim"** (`g`, `i`, `m` alphabetically in the spec order `dgimsuvy`).

<a id="js-regexp-methods-example-07"></a>

### **Example 7: global**

- [x] **`global`** is **true** if **`g`** is set.

Sandbox: `code_sandbox/js-regexp-methods/global.html`

```javascript
const pattern = /W3Schools/g;
let result = pattern.global;
```

![js-regexp-methods example 7 source](../code_sandbox/snaps/js-regexp-methods-07-code.png)

![js-regexp-methods example 7 result](../code_sandbox/snaps/js-regexp-methods-07-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-methods-example-08"></a>

### **Example 8: hasIndices**

- [x] **`hasIndices`** is **true** if **`d`** is set.

Sandbox: `code_sandbox/js-regexp-methods/hasIndices.html`

```javascript
const pattern = /W3Schools/d;
let result = pattern.hasIndices;
```

![js-regexp-methods example 8 source](../code_sandbox/snaps/js-regexp-methods-08-code.png)

![js-regexp-methods example 8 result](../code_sandbox/snaps/js-regexp-methods-08-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-methods-example-09"></a>

### **Example 9: ignoreCase**

- [x] **`ignoreCase`** is **true** if **`i`** is set.

Sandbox: `code_sandbox/js-regexp-methods/ignoreCase.html`

```javascript
const pattern = /W3Schools/i;
let result = pattern.ignoreCase;
```

![js-regexp-methods example 9 source](../code_sandbox/snaps/js-regexp-methods-09-code.png)

![js-regexp-methods example 9 result](../code_sandbox/snaps/js-regexp-methods-09-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-methods-example-10"></a>

### **Example 10: lastIndex**

- [x] **`lastIndex`** is where the next **`exec` / `test`** starts when **`g` or `y`** is set.
- [x] A failed match **resets it to 0**.

Sandbox: `code_sandbox/js-regexp-methods/lastIndex.html`

```javascript
const pattern = /is/g;
const text = "Is this all there is?";
const a = pattern.exec(text);
const li1 = pattern.lastIndex;
const b = pattern.exec(text);
const li2 = pattern.lastIndex;
const c = pattern.exec(text);
const li3 = pattern.lastIndex;
```

![js-regexp-methods example 10 source](../code_sandbox/snaps/js-regexp-methods-10-code.png)

![js-regexp-methods example 10 result](../code_sandbox/snaps/js-regexp-methods-10-result.png)

- [x] **Outcome:** Match at **5** → `lastIndex` **7**; match at **18** → **20**; then **null** and **`lastIndex` 0**.

<a id="js-regexp-methods-example-11"></a>

### **Example 11: multiline**

- [x] **`multiline`** is **true** if **`m`** is set.

Sandbox: `code_sandbox/js-regexp-methods/multiline.html`

```javascript
const pattern = /W3Schools/m;
let result = pattern.multiline;
```

![js-regexp-methods example 11 source](../code_sandbox/snaps/js-regexp-methods-11-code.png)

![js-regexp-methods example 11 result](../code_sandbox/snaps/js-regexp-methods-11-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-methods-example-12"></a>

### **Example 12: source**

- [x] **`source`** is the pattern text **without** slashes or flags.

Sandbox: `code_sandbox/js-regexp-methods/source.html`

```javascript
const pattern = /W3Schools/gi;
let result = pattern.source;
```

![js-regexp-methods example 12 source](../code_sandbox/snaps/js-regexp-methods-12-code.png)

![js-regexp-methods example 12 result](../code_sandbox/snaps/js-regexp-methods-12-result.png)

- [x] **Outcome:** **"W3Schools"** (not `"/W3Schools/gi"`).

<a id="js-regexp-methods-example-13"></a>

### **Example 13: sticky**

- [x] **`sticky`** is **true** if **`y`** is set.

Sandbox: `code_sandbox/js-regexp-methods/sticky.html`

```javascript
const pattern = /W3Schools/y;
let result = pattern.sticky;
```

![js-regexp-methods example 13 source](../code_sandbox/snaps/js-regexp-methods-13-code.png)

![js-regexp-methods example 13 result](../code_sandbox/snaps/js-regexp-methods-13-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-methods-example-14"></a>

### **Example 14: test()**

- [x] `test` returns **true** or **false**.
- [x] With **`/g`**, **`test` also mutates `lastIndex`** — easy to get alternating true/false.

Sandbox: `code_sandbox/js-regexp-methods/test.html`

```javascript
const pattern = /e/;
let result = pattern.test("The best things in life are free!");
```

![js-regexp-methods example 14 source](../code_sandbox/snaps/js-regexp-methods-14-code.png)

![js-regexp-methods example 14 result](../code_sandbox/snaps/js-regexp-methods-14-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-methods-example-15"></a>

### **Example 15: toString()**

- [x] **`toString()`** is the literal form including slashes and flags.

Sandbox: `code_sandbox/js-regexp-methods/toString.html`

```javascript
const pattern = /W3Schools/gim;
let result = pattern.toString();
```

![js-regexp-methods example 15 source](../code_sandbox/snaps/js-regexp-methods-15-code.png)

![js-regexp-methods example 15 result](../code_sandbox/snaps/js-regexp-methods-15-result.png)

- [x] **Outcome:** **"/W3Schools/gim"**.

<a id="js-regexp-methods-example-16"></a>

### **Example 16: unicode**

- [x] **`unicode`** is **true** if **`u`** is set.

Sandbox: `code_sandbox/js-regexp-methods/unicode.html`

```javascript
const pattern = /\u{04DC0}/u;
let result = pattern.unicode;
```

![js-regexp-methods example 16 source](../code_sandbox/snaps/js-regexp-methods-16-code.png)

![js-regexp-methods example 16 result](../code_sandbox/snaps/js-regexp-methods-16-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-methods-example-17"></a>

### **Example 17: unicodeSets**

- [x] **`unicodeSets`** is **true** if **`v`** is set.

Sandbox: `code_sandbox/js-regexp-methods/unicodeSets.html`

```javascript
const pattern = /\p{Emoji}/v;
let result = pattern.unicodeSets;
```

![js-regexp-methods example 17 source](../code_sandbox/snaps/js-regexp-methods-17-code.png)

![js-regexp-methods example 17 result](../code_sandbox/snaps/js-regexp-methods-17-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-methods-example-18"></a>

### **Example 18: String.match(regexp)**

- [x] Without **`g`**: one match array **with groups**. With **`g`**: all full matches, **no groups**.
- [x] No match → **null** (not `[]`).

Sandbox: `code_sandbox/js-regexp-methods/match.html`

```javascript
const text = "a1 a2";
const result = text.match(/a(\d)/);
const all = text.match(/a(\d)/g);
const miss = text.match(/z/);
```

![js-regexp-methods example 18 source](../code_sandbox/snaps/js-regexp-methods-18-code.png)

![js-regexp-methods example 18 result](../code_sandbox/snaps/js-regexp-methods-18-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["a1","1"]**. `all` is **["a1","a2"]** (groups dropped). `miss` is **null**.

<a id="js-regexp-methods-example-19"></a>

### **Example 19: String.matchAll(regexp)**

- [x] `matchAll` returns an **iterator** of match arrays **with groups**. The regex **must** be **`g`**.

Sandbox: `code_sandbox/js-regexp-methods/matchAll.html`

```javascript
const text = "a1 a2";
const result = [...text.matchAll(/a(\d)/g)].map((m) => [...m]);
```

![js-regexp-methods example 19 source](../code_sandbox/snaps/js-regexp-methods-19-code.png)

![js-regexp-methods example 19 result](../code_sandbox/snaps/js-regexp-methods-19-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **[["a1","1"],["a2","2"]]**.

<a id="js-regexp-methods-example-20"></a>

### **Example 20: String.replace(regexp, s)**

- [x] `replace` with a regex replaces the **first** match unless **`g`** is set.
- [x] It returns a **new** string.

Sandbox: `code_sandbox/js-regexp-methods/replace.html`

```javascript
let text = "Please visit Microsoft and Microsoft!";
let result = text.replace(/Microsoft/, "W3Schools");
```

![js-regexp-methods example 20 source](../code_sandbox/snaps/js-regexp-methods-20-code.png)

![js-regexp-methods example 20 result](../code_sandbox/snaps/js-regexp-methods-20-result.png)

- [x] **Outcome:** **"Please visit W3Schools and Microsoft!"** (only the first).

<a id="js-regexp-methods-example-21"></a>

### **Example 21: String.replaceAll(regexp, s)**

- [x] `replaceAll` with a regex **requires `g`**. It replaces **every** match.

Sandbox: `code_sandbox/js-regexp-methods/replaceAll.html`

```javascript
let text = "a1b2";
let result = text.replaceAll(/\d/g, "*");
```

![js-regexp-methods example 21 source](../code_sandbox/snaps/js-regexp-methods-21-code.png)

![js-regexp-methods example 21 result](../code_sandbox/snaps/js-regexp-methods-21-result.png)

- [x] **Outcome:** **"a*b*"**.

<a id="js-regexp-methods-example-22"></a>

### **Example 22: String.search(regexp)**

- [x] `search` returns the **index** of the first match, or **-1**.
- [x] It does **not** use `lastIndex` the way `exec` does.

Sandbox: `code_sandbox/js-regexp-methods/search.html`

```javascript
const text = "Visit W3Schools!";
const hit = text.search(/W3Schools/);
const miss = text.search(/z/);
```

![js-regexp-methods example 22 source](../code_sandbox/snaps/js-regexp-methods-22-code.png)

![js-regexp-methods example 22 result](../code_sandbox/snaps/js-regexp-methods-22-result.png)

- [x] **Outcome:** `hit` is **6**. `miss` is **-1**.

<a id="js-regexp-methods-example-23"></a>

### **Example 23: String.split(regexp)**

- [x] `split(regex)` cuts the string on each match and returns an **array of pieces**.

Sandbox: `code_sandbox/js-regexp-methods/split.html`

```javascript
let result = "a,b;c".split(/[,;]/);
```

![js-regexp-methods example 23 source](../code_sandbox/snaps/js-regexp-methods-23-code.png)

![js-regexp-methods example 23 result](../code_sandbox/snaps/js-regexp-methods-23-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["a","b","c"]**.

<a id="js-regexp-methods-example-24"></a>

### **Example 24: exec vs match with /g**

- [x] Named construct: **`match` + `g`** vs **`exec` + `g`**.
- [x] `match` returns all full matches and **resets** `lastIndex`. `exec` returns **one** match **with groups** and **moves** `lastIndex`.

Sandbox: `code_sandbox/js-regexp-methods/exec-vs-match-g.html`

```javascript
const text = "a1 a2";
const pattern = /a(\d)/g;
const viaMatch = text.match(pattern);
const liAfterMatch = pattern.lastIndex;
const viaExec = pattern.exec(text);
const liAfterExec = pattern.lastIndex;
```

![js-regexp-methods example 24 source](../code_sandbox/snaps/js-regexp-methods-24-code.png)

![js-regexp-methods example 24 result](../code_sandbox/snaps/js-regexp-methods-24-result.png)

- [x] **Outcome:** `viaMatch` is **["a1","a2"]**, `lastIndex` **0**. Then `exec` is **["a1","1"]**, `lastIndex` **2**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-regexp-methods/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What should you use instead of `compile()`?

<details>
<summary>Answer</summary>

- [x] Build a **new** `RegExp`. `compile` is **deprecated** (here it still became `/def/i`).

</details>

### Question 2: What is `pattern.constructor`?

<details>
<summary>Answer</summary>

- [x] **`RegExp`** (`function RegExp() { [native code] }`).

</details>

### Question 3: What does `flags` return for `/W3Schools/gim`?

<details>
<summary>Answer</summary>

- [x] **"gim"**.

</details>

### Question 4: What does `source` return?

<details>
<summary>Answer</summary>

- [x] The body only: **"W3Schools"**.

</details>

### Question 5: What does `toString()` return?

<details>
<summary>Answer</summary>

- [x] **"/W3Schools/gim"**.

</details>

### Question 6: Does `test` with `/g` move `lastIndex`?

<details>
<summary>Answer</summary>

- [x] **Yes** — same as `exec`. Easy to flip true/false on repeats.

</details>

### Question 7: `match` with `/g` vs without?

<details>
<summary>Answer</summary>

- [x] Without: **one** match **plus groups**. With: **all full matches**, **no groups**. Miss → **null**.

</details>

### Question 8: Why `matchAll`?

<details>
<summary>Answer</summary>

- [x] All matches **with groups**. Must be **`/g`**. Here **[["a1","1"],["a2","2"]]**.

</details>

### Question 9: `replace` vs `replaceAll`?

<details>
<summary>Answer</summary>

- [x] `replace` without **`g`** changes **one**. `replaceAll` needs **`g`** and changes **all**.

</details>

### Question 10: What does `search` return on a miss?

<details>
<summary>Answer</summary>

- [x] **-1**.

</details>

### Question 11: After `text.match(/a(\d)/g)`, what is `lastIndex`?

<details>
<summary>Answer</summary>

- [x] **0** — `match` with **`g`** resets it. A following `exec` starts at the beginning.

</details>

### Question 12: Is `RegExp.escape` an instance method?

<details>
<summary>Answer</summary>

- [x] **No.** Static **`RegExp.escape(string)`** (ES2025).

</details>


</details>

## Summary

The reference is a catalog of getters, exec/test, string search-and-replace, and a deprecated compile. Watch lastIndex whenever g or y is set. Prefer matchAll when you need groups for every hit. Skip compile; use a new RegExp.

## References

- [JS RegExp Methods (W3Schools)](https://www.w3schools.com/js/js_regexp_methods.asp)
- [MDN: RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
- [MDN: String.prototype.match](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
- [MDN: RegExp.prototype.exec](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
