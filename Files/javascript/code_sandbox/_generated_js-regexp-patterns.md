<details>
  <summary>JS RegExp Patterns</summary>

## Introduction

This page is the full pattern catalog (revised July 2025): flags, character classes, metacharacters, assertions, and quantifiers. There are no Tryits. Every table row is an Example that runs the token against a sample string and JSON-stringifies match (array or null). Flags are demonstrated with the same samples as the flags chapter. Metacharacters include the wildcard dot, whitespace escapes, Unicode properties (\p{} / \P{} with u), octal/hex/Unicode numbers, and [\b] for backspace (not a word boundary).

This section has **51** examples:

- [x] **Example 1:** /d — hasIndices — start/end pairs on the match. [View](#js-regexp-patterns-example-01)
- [x] **Example 2:** /g — global — find all. [View](#js-regexp-patterns-example-02)
- [x] **Example 3:** /i — case-insensitive. [View](#js-regexp-patterns-example-03)
- [x] **Example 4:** /m — multiline — `^` / `$` per line. [View](#js-regexp-patterns-example-04)
- [x] **Example 5:** /s — dotAll — `.` matches line terminators. [View](#js-regexp-patterns-example-05)
- [x] **Example 6:** /u — Unicode code points. [View](#js-regexp-patterns-example-06)
- [x] **Example 7:** /v — Unicode sets / property escapes. [View](#js-regexp-patterns-example-07)
- [x] **Example 8:** /y — sticky — match only at `lastIndex`. [View](#js-regexp-patterns-example-08)
- [x] **Example 9:** [a] [View](#js-regexp-patterns-example-09)
- [x] **Example 10:** [^a] [View](#js-regexp-patterns-example-10)
- [x] **Example 11:** [abc] [View](#js-regexp-patterns-example-11)
- [x] **Example 12:** [^abc] [View](#js-regexp-patterns-example-12)
- [x] **Example 13:** [a-z] [View](#js-regexp-patterns-example-13)
- [x] **Example 14:** [^a-z] [View](#js-regexp-patterns-example-14)
- [x] **Example 15:** [0-9] [View](#js-regexp-patterns-example-15)
- [x] **Example 16:** [^0-9] [View](#js-regexp-patterns-example-16)
- [x] **Example 17:** a|b [View](#js-regexp-patterns-example-17)
- [x] **Example 18:** . [View](#js-regexp-patterns-example-18)
- [x] **Example 19:** \w [View](#js-regexp-patterns-example-19)
- [x] **Example 20:** \W [View](#js-regexp-patterns-example-20)
- [x] **Example 21:** \d [View](#js-regexp-patterns-example-21)
- [x] **Example 22:** \D [View](#js-regexp-patterns-example-22)
- [x] **Example 23:** \s [View](#js-regexp-patterns-example-23)
- [x] **Example 24:** \S [View](#js-regexp-patterns-example-24)
- [x] **Example 25:** [\b] [View](#js-regexp-patterns-example-25)
- [x] **Example 26:** \0 [View](#js-regexp-patterns-example-26)
- [x] **Example 27:** \n [View](#js-regexp-patterns-example-27)
- [x] **Example 28:** \f [View](#js-regexp-patterns-example-28)
- [x] **Example 29:** \r [View](#js-regexp-patterns-example-29)
- [x] **Example 30:** \t [View](#js-regexp-patterns-example-30)
- [x] **Example 31:** \v [View](#js-regexp-patterns-example-31)
- [x] **Example 32:** \p{} [View](#js-regexp-patterns-example-32)
- [x] **Example 33:** \P{} [View](#js-regexp-patterns-example-33)
- [x] **Example 34:** \ddd [View](#js-regexp-patterns-example-34)
- [x] **Example 35:** \xhh [View](#js-regexp-patterns-example-35)
- [x] **Example 36:** \uhhhh [View](#js-regexp-patterns-example-36)
- [x] **Example 37:** ^ [View](#js-regexp-patterns-example-37)
- [x] **Example 38:** ^ miss [View](#js-regexp-patterns-example-38)
- [x] **Example 39:** $ [View](#js-regexp-patterns-example-39)
- [x] **Example 40:** \b [View](#js-regexp-patterns-example-40)
- [x] **Example 41:** \B [View](#js-regexp-patterns-example-41)
- [x] **Example 42:** (?=...) [View](#js-regexp-patterns-example-42)
- [x] **Example 43:** (?!...) [View](#js-regexp-patterns-example-43)
- [x] **Example 44:** (?<=...) [View](#js-regexp-patterns-example-44)
- [x] **Example 45:** (?<!...) [View](#js-regexp-patterns-example-45)
- [x] **Example 46:** x+ [View](#js-regexp-patterns-example-46)
- [x] **Example 47:** x* [View](#js-regexp-patterns-example-47)
- [x] **Example 48:** x? [View](#js-regexp-patterns-example-48)
- [x] **Example 49:** x{n} [View](#js-regexp-patterns-example-49)
- [x] **Example 50:** x{n,m} [View](#js-regexp-patterns-example-50)
- [x] **Example 51:** x{n,} [View](#js-regexp-patterns-example-51)

## Detailed Explanation

- [x] No Tryits — **one Example per table row** across flags, classes, metacharacters, assertions, quantifiers.
- [x] **`.`** skips newlines unless **`s`**. **`[\b]`** is **backspace**; **`\b`** outside a class is a **word boundary**.
- [x] **`\p{L}` / `\P{L}`** need **`u` or `v`**. **`\0` `\n` `\t`** etc. match those controls.
- [x] Assertions still `match()`: hit → array of the consumed text (often the word), miss → **null**.

<a id="js-regexp-patterns-example-01"></a>

### **Example 1: /d — hasIndices — start/end pairs on the match.**

- [x] Flags table row **`/d`**: hasIndices — start/end pairs on the match.

Sandbox: `code_sandbox/js-regexp-patterns/flag-d.html`

```javascript
let text = "aaaabb";
const pattern = /(aa)(bb)/d;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 1 source" src="./code_sandbox/snaps/js-regexp-patterns-01-code.png" />

<img alt="js-regexp-patterns example 1 result" src="./code_sandbox/snaps/js-regexp-patterns-01-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["aabb","aa","bb"]**. `indices` is **[[2,6],[2,4],[4,6]]**.

<a id="js-regexp-patterns-example-02"></a>

### **Example 2: /g — global — find all.**

- [x] Flags table row **`/g`**: global — find all.

Sandbox: `code_sandbox/js-regexp-patterns/flag-g.html`

```javascript
let text = "Is this all there is?";
const pattern = /is/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 2 source" src="./code_sandbox/snaps/js-regexp-patterns-02-code.png" />

<img alt="js-regexp-patterns example 2 result" src="./code_sandbox/snaps/js-regexp-patterns-02-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["is","is"]**.

<a id="js-regexp-patterns-example-03"></a>

### **Example 3: /i — case-insensitive.**

- [x] Flags table row **`/i`**: case-insensitive.

Sandbox: `code_sandbox/js-regexp-patterns/flag-i.html`

```javascript
let text = "Visit W3Schools";
const pattern = /w3schools/i;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 3 source" src="./code_sandbox/snaps/js-regexp-patterns-03-code.png" />

<img alt="js-regexp-patterns example 3 result" src="./code_sandbox/snaps/js-regexp-patterns-03-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**.

<a id="js-regexp-patterns-example-04"></a>

### **Example 4: /m — multiline — `^` / `$` per line.**

- [x] Flags table row **`/m`**: multiline — `^` / `$` per line.

Sandbox: `code_sandbox/js-regexp-patterns/flag-m.html`

```javascript
let text = "\nIs th\nis it?";
let result = text.match(/^is/m);
```

<img alt="js-regexp-patterns example 4 source" src="./code_sandbox/snaps/js-regexp-patterns-04-code.png" />

<img alt="js-regexp-patterns example 4 result" src="./code_sandbox/snaps/js-regexp-patterns-04-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["is"]**.

<a id="js-regexp-patterns-example-05"></a>

### **Example 5: /s — dotAll — `.` matches line terminators.**

- [x] Flags table row **`/s`**: dotAll — `.` matches line terminators.

Sandbox: `code_sandbox/js-regexp-patterns/flag-s.html`

```javascript
let text = "Line\nLine.";
const pattern = /Line./gs;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 5 source" src="./code_sandbox/snaps/js-regexp-patterns-05-code.png" />

<img alt="js-regexp-patterns example 5 result" src="./code_sandbox/snaps/js-regexp-patterns-05-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["Line\n","Line."]** .

<a id="js-regexp-patterns-example-06"></a>

### **Example 6: /u — Unicode code points.**

- [x] Flags table row **`/u`**: Unicode code points.

Sandbox: `code_sandbox/js-regexp-patterns/flag-u.html`

```javascript
let text = "\u4DC0";
const pattern = /\u{04DC0}/u;
let result = pattern.test(text);
```

<img alt="js-regexp-patterns example 6 source" src="./code_sandbox/snaps/js-regexp-patterns-06-code.png" />

<img alt="js-regexp-patterns example 6 result" src="./code_sandbox/snaps/js-regexp-patterns-06-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-patterns-example-07"></a>

### **Example 7: /v — Unicode sets / property escapes.**

- [x] Flags table row **`/v`**: Unicode sets / property escapes.

Sandbox: `code_sandbox/js-regexp-patterns/flag-v.html`

```javascript
let text = "Hello \u{1F604}";
const pattern = /\p{Emoji}/v;
let result = pattern.test(text);
```

<img alt="js-regexp-patterns example 7 source" src="./code_sandbox/snaps/js-regexp-patterns-07-code.png" />

<img alt="js-regexp-patterns example 7 result" src="./code_sandbox/snaps/js-regexp-patterns-07-result.png" />

- [x] **Outcome:** **true**.

<a id="js-regexp-patterns-example-08"></a>

### **Example 8: /y — sticky — match only at `lastIndex`.**

- [x] Flags table row **`/y`**: sticky — match only at `lastIndex`.

Sandbox: `code_sandbox/js-regexp-patterns/flag-y.html`

```javascript
let text = "abc def ghi";
const pattern = /\w+/y;
pattern.lastIndex = 4;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 8 source" src="./code_sandbox/snaps/js-regexp-patterns-08-code.png" />

<img alt="js-regexp-patterns example 8 result" src="./code_sandbox/snaps/js-regexp-patterns-08-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["def"]**.

<a id="js-regexp-patterns-example-09"></a>

### **Example 9: [a]**

- [x] Character-class table row **`[a]`**. `match` is the array or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/class-a.html`

```javascript
let text = "cat";
const pattern = /[a]/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 9 source" src="./code_sandbox/snaps/js-regexp-patterns-09-code.png" />

<img alt="js-regexp-patterns example 9 result" src="./code_sandbox/snaps/js-regexp-patterns-09-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["a"]**.

<a id="js-regexp-patterns-example-10"></a>

### **Example 10: [^a]**

- [x] Character-class table row **`[^a]`**. `match` is the array or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/class-not-a.html`

```javascript
let text = "cat";
const pattern = /[^a]/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 10 source" src="./code_sandbox/snaps/js-regexp-patterns-10-code.png" />

<img alt="js-regexp-patterns example 10 result" src="./code_sandbox/snaps/js-regexp-patterns-10-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["c","t"]**.

<a id="js-regexp-patterns-example-11"></a>

### **Example 11: [abc]**

- [x] Character-class table row **`[abc]`**. `match` is the array or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/class-abc.html`

```javascript
let text = "fabric";
const pattern = /[abc]/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 11 source" src="./code_sandbox/snaps/js-regexp-patterns-11-code.png" />

<img alt="js-regexp-patterns example 11 result" src="./code_sandbox/snaps/js-regexp-patterns-11-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["a","b","c"]**.

<a id="js-regexp-patterns-example-12"></a>

### **Example 12: [^abc]**

- [x] Character-class table row **`[^abc]`**. `match` is the array or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/class-not-abc.html`

```javascript
let text = "fabric";
const pattern = /[^abc]/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 12 source" src="./code_sandbox/snaps/js-regexp-patterns-12-code.png" />

<img alt="js-regexp-patterns example 12 result" src="./code_sandbox/snaps/js-regexp-patterns-12-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["f","r","i"]**.

<a id="js-regexp-patterns-example-13"></a>

### **Example 13: [a-z]**

- [x] Character-class table row **`[a-z]`**. `match` is the array or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/class-az.html`

```javascript
let text = "A1b";
const pattern = /[a-z]/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 13 source" src="./code_sandbox/snaps/js-regexp-patterns-13-code.png" />

<img alt="js-regexp-patterns example 13 result" src="./code_sandbox/snaps/js-regexp-patterns-13-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["b"]**.

<a id="js-regexp-patterns-example-14"></a>

### **Example 14: [^a-z]**

- [x] Character-class table row **`[^a-z]`**. `match` is the array or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/class-not-az.html`

```javascript
let text = "A1b";
const pattern = /[^a-z]/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 14 source" src="./code_sandbox/snaps/js-regexp-patterns-14-code.png" />

<img alt="js-regexp-patterns example 14 result" src="./code_sandbox/snaps/js-regexp-patterns-14-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["A","1"]**.

<a id="js-regexp-patterns-example-15"></a>

### **Example 15: [0-9]**

- [x] Character-class table row **`[0-9]`**. `match` is the array or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/class-09.html`

```javascript
let text = "A1b";
const pattern = /[0-9]/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 15 source" src="./code_sandbox/snaps/js-regexp-patterns-15-code.png" />

<img alt="js-regexp-patterns example 15 result" src="./code_sandbox/snaps/js-regexp-patterns-15-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["1"]**.

<a id="js-regexp-patterns-example-16"></a>

### **Example 16: [^0-9]**

- [x] Character-class table row **`[^0-9]`**. `match` is the array or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/class-not-09.html`

```javascript
let text = "A1b";
const pattern = /[^0-9]/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 16 source" src="./code_sandbox/snaps/js-regexp-patterns-16-code.png" />

<img alt="js-regexp-patterns example 16 result" src="./code_sandbox/snaps/js-regexp-patterns-16-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["A","b"]**.

<a id="js-regexp-patterns-example-17"></a>

### **Example 17: a|b**

- [x] Metacharacter table row **`a|b`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-or.html`

```javascript
let text = "cat";
const pattern = /a|b/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 17 source" src="./code_sandbox/snaps/js-regexp-patterns-17-code.png" />

<img alt="js-regexp-patterns example 17 result" src="./code_sandbox/snaps/js-regexp-patterns-17-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["a"]**.

<a id="js-regexp-patterns-example-18"></a>

### **Example 18: .**

- [x] Metacharacter table row **`.`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-dot.html`

```javascript
let text = "a\nb";
const pattern = /./g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 18 source" src="./code_sandbox/snaps/js-regexp-patterns-18-code.png" />

<img alt="js-regexp-patterns example 18 result" src="./code_sandbox/snaps/js-regexp-patterns-18-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["a","b"]** — newline skipped.

<a id="js-regexp-patterns-example-19"></a>

### **Example 19: \w**

- [x] Metacharacter table row **`\w`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-w.html`

```javascript
let text = "Give 100%!";
const pattern = /\w/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 19 source" src="./code_sandbox/snaps/js-regexp-patterns-19-code.png" />

<img alt="js-regexp-patterns example 19 result" src="./code_sandbox/snaps/js-regexp-patterns-19-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["G","i","v","e","1","0","0"]**.

<a id="js-regexp-patterns-example-20"></a>

### **Example 20: \W**

- [x] Metacharacter table row **`\W`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-nonword.html`

```javascript
let text = "Give 100%!";
const pattern = /\W/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 20 source" src="./code_sandbox/snaps/js-regexp-patterns-20-code.png" />

<img alt="js-regexp-patterns example 20 result" src="./code_sandbox/snaps/js-regexp-patterns-20-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **[" ","%","!"]**.

<a id="js-regexp-patterns-example-21"></a>

### **Example 21: \d**

- [x] Metacharacter table row **`\d`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-d.html`

```javascript
let text = "Give 100%!";
const pattern = /\d/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 21 source" src="./code_sandbox/snaps/js-regexp-patterns-21-code.png" />

<img alt="js-regexp-patterns example 21 result" src="./code_sandbox/snaps/js-regexp-patterns-21-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["1","0","0"]**.

<a id="js-regexp-patterns-example-22"></a>

### **Example 22: \D**

- [x] Metacharacter table row **`\D`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-nondigit.html`

```javascript
let text = "Give 100%!";
const pattern = /\D/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 22 source" src="./code_sandbox/snaps/js-regexp-patterns-22-code.png" />

<img alt="js-regexp-patterns example 22 result" src="./code_sandbox/snaps/js-regexp-patterns-22-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["G","i","v","e"," ","%","!"]**.

<a id="js-regexp-patterns-example-23"></a>

### **Example 23: \s**

- [x] Metacharacter table row **`\s`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-s.html`

```javascript
let text = "Is this all there is?";
const pattern = /\s/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 23 source" src="./code_sandbox/snaps/js-regexp-patterns-23-code.png" />

<img alt="js-regexp-patterns example 23 result" src="./code_sandbox/snaps/js-regexp-patterns-23-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **[" "," "," "," "]**.

<a id="js-regexp-patterns-example-24"></a>

### **Example 24: \S**

- [x] Metacharacter table row **`\S`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-nonspace.html`

```javascript
let text = "Give 100%!";
const pattern = /\S/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 24 source" src="./code_sandbox/snaps/js-regexp-patterns-24-code.png" />

<img alt="js-regexp-patterns example 24 result" src="./code_sandbox/snaps/js-regexp-patterns-24-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["G","i","v","e","1","0","0","%","!"]**.

<a id="js-regexp-patterns-example-25"></a>

### **Example 25: [\b]**

- [x] Metacharacter table row **`[\b]`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-bs.html`

```javascript
let text = "a\bb";
const pattern = /[\b]/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 25 source" src="./code_sandbox/snaps/js-regexp-patterns-25-code.png" />

<img alt="js-regexp-patterns example 25 result" src="./code_sandbox/snaps/js-regexp-patterns-25-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["\b"]** — backspace, not a word boundary.

<a id="js-regexp-patterns-example-26"></a>

### **Example 26: \0**

- [x] Metacharacter table row **`\0`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-nul.html`

```javascript
let text = "a\u0000b";
const pattern = /\0/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 26 source" src="./code_sandbox/snaps/js-regexp-patterns-26-code.png" />

<img alt="js-regexp-patterns example 26 result" src="./code_sandbox/snaps/js-regexp-patterns-26-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["\u0000"]**.

<a id="js-regexp-patterns-example-27"></a>

### **Example 27: \n**

- [x] Metacharacter table row **`\n`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-n.html`

```javascript
let text = "a\nb";
const pattern = /\n/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 27 source" src="./code_sandbox/snaps/js-regexp-patterns-27-code.png" />

<img alt="js-regexp-patterns example 27 result" src="./code_sandbox/snaps/js-regexp-patterns-27-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["\n"]**.

<a id="js-regexp-patterns-example-28"></a>

### **Example 28: \f**

- [x] Metacharacter table row **`\f`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-f.html`

```javascript
let text = "a\fb";
const pattern = /\f/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 28 source" src="./code_sandbox/snaps/js-regexp-patterns-28-code.png" />

<img alt="js-regexp-patterns example 28 result" src="./code_sandbox/snaps/js-regexp-patterns-28-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["\f"]**.

<a id="js-regexp-patterns-example-29"></a>

### **Example 29: \r**

- [x] Metacharacter table row **`\r`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-r.html`

```javascript
let text = "a\rb";
const pattern = /\r/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 29 source" src="./code_sandbox/snaps/js-regexp-patterns-29-code.png" />

<img alt="js-regexp-patterns example 29 result" src="./code_sandbox/snaps/js-regexp-patterns-29-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["\r"]**.

<a id="js-regexp-patterns-example-30"></a>

### **Example 30: \t**

- [x] Metacharacter table row **`\t`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-t.html`

```javascript
let text = "a\tb";
const pattern = /\t/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 30 source" src="./code_sandbox/snaps/js-regexp-patterns-30-code.png" />

<img alt="js-regexp-patterns example 30 result" src="./code_sandbox/snaps/js-regexp-patterns-30-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["\t"]**.

<a id="js-regexp-patterns-example-31"></a>

### **Example 31: \v**

- [x] Metacharacter table row **`\v`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-v.html`

```javascript
let text = "a\u000bb";
const pattern = /\v/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 31 source" src="./code_sandbox/snaps/js-regexp-patterns-31-code.png" />

<img alt="js-regexp-patterns example 31 result" src="./code_sandbox/snaps/js-regexp-patterns-31-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["\u000b"]**.

<a id="js-regexp-patterns-example-32"></a>

### **Example 32: \p{}**

- [x] Metacharacter table row **`\p{}`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-p.html`

```javascript
let text = "Hello 1";
const pattern = /\p{L}/gu;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 32 source" src="./code_sandbox/snaps/js-regexp-patterns-32-code.png" />

<img alt="js-regexp-patterns example 32 result" src="./code_sandbox/snaps/js-regexp-patterns-32-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["H","e","l","l","o"]** — needs u/v.

<a id="js-regexp-patterns-example-33"></a>

### **Example 33: \P{}**

- [x] Metacharacter table row **`\P{}`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-not-prop.html`

```javascript
let text = "Hello 1";
const pattern = /\P{L}/gu;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 33 source" src="./code_sandbox/snaps/js-regexp-patterns-33-code.png" />

<img alt="js-regexp-patterns example 33 result" src="./code_sandbox/snaps/js-regexp-patterns-33-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **[" ","1"]**.

<a id="js-regexp-patterns-example-34"></a>

### **Example 34: \ddd**

- [x] Metacharacter table row **`\ddd`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-oct.html`

```javascript
let text = "Visit W3Schools. Hello World!";
const pattern = /\127/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 34 source" src="./code_sandbox/snaps/js-regexp-patterns-34-code.png" />

<img alt="js-regexp-patterns example 34 result" src="./code_sandbox/snaps/js-regexp-patterns-34-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W","W"]** (octal 127 = W).

<a id="js-regexp-patterns-example-35"></a>

### **Example 35: \xhh**

- [x] Metacharacter table row **`\xhh`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-x.html`

```javascript
let text = "Hello";
const pattern = /\x6F/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 35 source" src="./code_sandbox/snaps/js-regexp-patterns-35-code.png" />

<img alt="js-regexp-patterns example 35 result" src="./code_sandbox/snaps/js-regexp-patterns-35-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["o"]** (hex 6F).

<a id="js-regexp-patterns-example-36"></a>

### **Example 36: \uhhhh**

- [x] Metacharacter table row **`\uhhhh`**. Show `match` or **null**.

Sandbox: `code_sandbox/js-regexp-patterns/meta-u.html`

```javascript
let text = "Visit W3Schools. Hello World!";
const pattern = /\u0057/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 36 source" src="./code_sandbox/snaps/js-regexp-patterns-36-code.png" />

<img alt="js-regexp-patterns example 36 result" src="./code_sandbox/snaps/js-regexp-patterns-36-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W","W"]** (U+0057).

<a id="js-regexp-patterns-example-37"></a>

### **Example 37: ^**

- [x] Assertions table row **`^`**. `match` array or **null** (zero-width).

Sandbox: `code_sandbox/js-regexp-patterns/as-hat.html`

```javascript
let text = "W3Schools tutorial";
const pattern = /^W3Schools/;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 37 source" src="./code_sandbox/snaps/js-regexp-patterns-37-code.png" />

<img alt="js-regexp-patterns example 37 result" src="./code_sandbox/snaps/js-regexp-patterns-37-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**.

<a id="js-regexp-patterns-example-38"></a>

### **Example 38: ^ miss**

- [x] Assertions table row **`^ miss`**. `match` array or **null** (zero-width).

Sandbox: `code_sandbox/js-regexp-patterns/as-hat-miss.html`

```javascript
let text = "Hello W3Schools";
const pattern = /^W3Schools/;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 38 source" src="./code_sandbox/snaps/js-regexp-patterns-38-code.png" />

<img alt="js-regexp-patterns example 38 result" src="./code_sandbox/snaps/js-regexp-patterns-38-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **null**.

<a id="js-regexp-patterns-example-39"></a>

### **Example 39: $**

- [x] Assertions table row **`$`**. `match` array or **null** (zero-width).

Sandbox: `code_sandbox/js-regexp-patterns/as-dollar.html`

```javascript
let text = "Hello W3Schools";
const pattern = /W3Schools$/;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 39 source" src="./code_sandbox/snaps/js-regexp-patterns-39-code.png" />

<img alt="js-regexp-patterns example 39 result" src="./code_sandbox/snaps/js-regexp-patterns-39-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**.

<a id="js-regexp-patterns-example-40"></a>

### **Example 40: \b**

- [x] Assertions table row **`\b`**. `match` array or **null** (zero-width).

Sandbox: `code_sandbox/js-regexp-patterns/as-b.html`

```javascript
let text = "HELLO, LOOK AT YOU!";
const pattern = /\bLOOK/;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 40 source" src="./code_sandbox/snaps/js-regexp-patterns-40-code.png" />

<img alt="js-regexp-patterns example 40 result" src="./code_sandbox/snaps/js-regexp-patterns-40-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["LOOK"]**.

<a id="js-regexp-patterns-example-41"></a>

### **Example 41: \B**

- [x] Assertions table row **`\B`**. `match` array or **null** (zero-width).

Sandbox: `code_sandbox/js-regexp-patterns/as-not-b.html`

```javascript
let text = "JavaScript";
const pattern = /\BScript/;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 41 source" src="./code_sandbox/snaps/js-regexp-patterns-41-code.png" />

<img alt="js-regexp-patterns example 41 result" src="./code_sandbox/snaps/js-regexp-patterns-41-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["Script"]**.

<a id="js-regexp-patterns-example-42"></a>

### **Example 42: (?=...)**

- [x] Assertions table row **`(?=...)`**. `match` array or **null** (zero-width).

Sandbox: `code_sandbox/js-regexp-patterns/as-la.html`

```javascript
let text = "W3Schools Tutorials";
const pattern = /W3Schools(?= Tutorials)/;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 42 source" src="./code_sandbox/snaps/js-regexp-patterns-42-code.png" />

<img alt="js-regexp-patterns example 42 result" src="./code_sandbox/snaps/js-regexp-patterns-42-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**.

<a id="js-regexp-patterns-example-43"></a>

### **Example 43: (?!...)**

- [x] Assertions table row **`(?!...)`**. `match` array or **null** (zero-width).

Sandbox: `code_sandbox/js-regexp-patterns/as-nla.html`

```javascript
let text = "W3Schools Tutorials";
const pattern = /W3Schools(?! Tutorials)/;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 43 source" src="./code_sandbox/snaps/js-regexp-patterns-43-code.png" />

<img alt="js-regexp-patterns example 43 result" src="./code_sandbox/snaps/js-regexp-patterns-43-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **null**.

<a id="js-regexp-patterns-example-44"></a>

### **Example 44: (?<=...)**

- [x] Assertions table row **`(?<=...)`**. `match` array or **null** (zero-width).

Sandbox: `code_sandbox/js-regexp-patterns/as-lb.html`

```javascript
let text = "Hello W3Schools";
const pattern = /(?<=Hello )W3Schools/;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 44 source" src="./code_sandbox/snaps/js-regexp-patterns-44-code.png" />

<img alt="js-regexp-patterns example 44 result" src="./code_sandbox/snaps/js-regexp-patterns-44-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["W3Schools"]**.

<a id="js-regexp-patterns-example-45"></a>

### **Example 45: (?<!...)**

- [x] Assertions table row **`(?<!...)`**. `match` array or **null** (zero-width).

Sandbox: `code_sandbox/js-regexp-patterns/as-nlb.html`

```javascript
let text = "Hello W3Schools";
const pattern = /(?<!Hello )W3Schools/;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 45 source" src="./code_sandbox/snaps/js-regexp-patterns-45-code.png" />

<img alt="js-regexp-patterns example 45 result" src="./code_sandbox/snaps/js-regexp-patterns-45-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **null**.

<a id="js-regexp-patterns-example-46"></a>

### **Example 46: x+**

- [x] Quantifier table row **`x+`**.

Sandbox: `code_sandbox/js-regexp-patterns/q-plus.html`

```javascript
let text = "Hellooo World! Hello W3Schools!";
const pattern = /o+/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 46 source" src="./code_sandbox/snaps/js-regexp-patterns-46-code.png" />

<img alt="js-regexp-patterns example 46 result" src="./code_sandbox/snaps/js-regexp-patterns-46-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["ooo","o","o","oo"]**.

<a id="js-regexp-patterns-example-47"></a>

### **Example 47: x***

- [x] Quantifier table row **`x*`**.

Sandbox: `code_sandbox/js-regexp-patterns/q-star.html`

```javascript
let text = "Hellooo World! Hello W3Schools!";
const pattern = /lo*/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 47 source" src="./code_sandbox/snaps/js-regexp-patterns-47-code.png" />

<img alt="js-regexp-patterns example 47 result" src="./code_sandbox/snaps/js-regexp-patterns-47-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["l","looo","l","l","lo","l"]**.

<a id="js-regexp-patterns-example-48"></a>

### **Example 48: x?**

- [x] Quantifier table row **`x?`**.

Sandbox: `code_sandbox/js-regexp-patterns/q-q.html`

```javascript
let text = "1, 100 or 1000?";
const pattern = /10?/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 48 source" src="./code_sandbox/snaps/js-regexp-patterns-48-code.png" />

<img alt="js-regexp-patterns example 48 result" src="./code_sandbox/snaps/js-regexp-patterns-48-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["1","10","10"]**.

<a id="js-regexp-patterns-example-49"></a>

### **Example 49: x{n}**

- [x] Quantifier table row **`x{n}`**.

Sandbox: `code_sandbox/js-regexp-patterns/q-n.html`

```javascript
let text = "100, 1000 or 10000?";
const pattern = /\d{4}/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 49 source" src="./code_sandbox/snaps/js-regexp-patterns-49-code.png" />

<img alt="js-regexp-patterns example 49 result" src="./code_sandbox/snaps/js-regexp-patterns-49-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["1000","1000"]**.

<a id="js-regexp-patterns-example-50"></a>

### **Example 50: x{n,m}**

- [x] Quantifier table row **`x{n,m}`**.

Sandbox: `code_sandbox/js-regexp-patterns/q-nm.html`

```javascript
let text = "100, 1000 or 10000?";
const pattern = /\d{3,4}/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 50 source" src="./code_sandbox/snaps/js-regexp-patterns-50-code.png" />

<img alt="js-regexp-patterns example 50 result" src="./code_sandbox/snaps/js-regexp-patterns-50-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["100","1000","1000"]**.

<a id="js-regexp-patterns-example-51"></a>

### **Example 51: x{n,}**

- [x] Quantifier table row **`x{n,}`**.

Sandbox: `code_sandbox/js-regexp-patterns/q-nmore.html`

```javascript
let text = "100, 1000 or 10000?";
const pattern = /\d{3,}/g;
let result = text.match(pattern);
```

<img alt="js-regexp-patterns example 51 source" src="./code_sandbox/snaps/js-regexp-patterns-51-code.png" />

<img alt="js-regexp-patterns example 51 result" src="./code_sandbox/snaps/js-regexp-patterns-51-result.png" />

- [x] **Outcome:** `JSON.stringify(result)` is **["100","1000","10000"]**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-regexp-patterns/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does this page have Tryits?

<details>
<summary>Answer</summary>

- [x] **No.** Each **table row** is still an Example.

</details>

### Question 2: What does `.` match in `a\\nb` with `/g`?

<details>
<summary>Answer</summary>

- [x] **["a","b"]** — not the newline.

</details>

### Question 3: What is `[\\b]` vs `\\b`?

<details>
<summary>Answer</summary>

- [x] **`[\b]`** backspace character. **`\b`** word boundary.

</details>

### Question 4: What does `\\p{L}` need?

<details>
<summary>Answer</summary>

- [x] The **`u`** or **`v`** flag. On `Hello 1` → **["H","e","l","l","o"]**.

</details>

### Question 5: What is `\\127`?

<details>
<summary>Answer</summary>

- [x] Octal **W**. **["W","W"]** in the Visit/World sentence.

</details>

### Question 6: What is `^W3Schools` on `Hello W3Schools`?

<details>
<summary>Answer</summary>

- [x] **null**.

</details>

### Question 7: What is `(?= Tutorials)` on `W3Schools Tutorials`?

<details>
<summary>Answer</summary>

- [x] **["W3Schools"]** (lookahead not consumed). `(?! Tutorials)` → **null**.

</details>

### Question 8: What is `\d{3,}` on the 100/1000/10000 sample?

<details>
<summary>Answer</summary>

- [x] **["100","1000","10000"]**.

</details>

### Question 9: Which flag lets `.` match a newline?

<details>
<summary>Answer</summary>

- [x] **`s`** (dotAll).

</details>

### Question 10: Which flag makes `^` per line?

<details>
<summary>Answer</summary>

- [x] **`m`**.

</details>


</details>

## Summary

Treat this page as a catalog: run each token, stringify the match, and remember that lookarounds and anchors are zero-width (match text is only what was consumed). Unicode properties and the v flag need a Unicode mode. [\b] is not \b.

## References

- [JS RegExp Patterns (W3Schools)](https://www.w3schools.com/js/js_regexp_patterns.asp)
- [MDN: Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
- [MDN: RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)

</details>
