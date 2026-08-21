# JS String Methods

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Strings are **primitive and immutable**. Every method returns a **new** value; the original is unchanged. This page walks **every Tryit**: `length`, character access, `concat`, `slice` / `substring` / deprecated `substr`, case, well-formed, trim, pad, repeat, `replace` / `replaceAll`, and `split` (including why `split("")` is unsafe on emoji). Same grain as **JS Output** — one Example per Tryit.

This section has **46** examples:

- [x] **Example 1:** `length` [View](#js-string-methods-example-01)
- [x] **Example 2:** `charAt(0)` [View](#js-string-methods-example-02)
- [x] **Example 3:** `charCodeAt(0)` [View](#js-string-methods-example-03)
- [x] **Example 4:** `codePointAt(0)` [View](#js-string-methods-example-04)
- [x] **Example 5:** `at(2)` [View](#js-string-methods-example-05)
- [x] **Example 6:** Property access `[2]` [View](#js-string-methods-example-06)
- [x] **Example 7:** `at(-5)` [View](#js-string-methods-example-07)
- [x] **Example 8:** Property access `[0]` [View](#js-string-methods-example-08)
- [x] **Example 9:** Sloppy mode `text[0] = "A"` [View](#js-string-methods-example-09)
- [x] **Example 10:** `concat()` Hello World [View](#js-string-methods-example-10)
- [x] **Example 11:** `slice(7, 13)` [View](#js-string-methods-example-11)
- [x] **Example 12:** `slice(7)` [View](#js-string-methods-example-12)
- [x] **Example 13:** `slice(-12)` [View](#js-string-methods-example-13)
- [x] **Example 14:** `slice(-12, -6)` [View](#js-string-methods-example-14)
- [x] **Example 15:** `substring(7, 13)` [View](#js-string-methods-example-15)
- [x] **Example 16:** `substr(7, 6)` (deprecated) [View](#js-string-methods-example-16)
- [x] **Example 17:** `substr(7)` (deprecated) [View](#js-string-methods-example-17)
- [x] **Example 18:** `substr(-4)` (deprecated) [View](#js-string-methods-example-18)
- [x] **Example 19:** `toUpperCase()` [View](#js-string-methods-example-19)
- [x] **Example 20:** `toLowerCase()` [View](#js-string-methods-example-20)
- [x] **Example 21:** `isWellFormed()` true [View](#js-string-methods-example-21)
- [x] **Example 22:** `isWellFormed()` lone surrogate [View](#js-string-methods-example-22)
- [x] **Example 23:** `toWellFormed()` [View](#js-string-methods-example-23)
- [x] **Example 24:** `trim()` [View](#js-string-methods-example-24)
- [x] **Example 25:** `trimStart()` [View](#js-string-methods-example-25)
- [x] **Example 26:** `trimEnd()` [View](#js-string-methods-example-26)
- [x] **Example 27:** `padStart(4, "0")` [View](#js-string-methods-example-27)
- [x] **Example 28:** `padStart(4, "x")` [View](#js-string-methods-example-28)
- [x] **Example 29:** `padStart` on a number via `toString()` [View](#js-string-methods-example-29)
- [x] **Example 30:** `padEnd(4, "0")` [View](#js-string-methods-example-30)
- [x] **Example 31:** `padEnd(4, "x")` [View](#js-string-methods-example-31)
- [x] **Example 32:** `padEnd` on a number via `toString()` [View](#js-string-methods-example-32)
- [x] **Example 33:** `repeat(2)` [View](#js-string-methods-example-33)
- [x] **Example 34:** `repeat(4)` [View](#js-string-methods-example-34)
- [x] **Example 35:** `replace()` first Microsoft [View](#js-string-methods-example-35)
- [x] **Example 36:** `replace()` only the first of two [View](#js-string-methods-example-36)
- [x] **Example 37:** `replace("MICROSOFT")` case fail [View](#js-string-methods-example-37)
- [x] **Example 38:** `replace(/MICROSOFT/i)` [View](#js-string-methods-example-38)
- [x] **Example 39:** `replace(/Microsoft/g)` [View](#js-string-methods-example-39)
- [x] **Example 40:** `replaceAll("Cats")` [View](#js-string-methods-example-40)
- [x] **Example 41:** `replaceAll(/Cats/g)` [View](#js-string-methods-example-41)
- [x] **Example 42:** `split("")` [View](#js-string-methods-example-42)
- [x] **Example 43:** `split(" ")` [View](#js-string-methods-example-43)
- [x] **Example 44:** `split()` with no separator [View](#js-string-methods-example-44)
- [x] **Example 45:** `split("")` is unsafe for emoji [View](#js-string-methods-example-45)
- [x] **Example 46:** `Intl.Segmenter` safe split [View](#js-string-methods-example-46)

## Detailed Explanation

- [x] **Immutable** — methods never edit in place; assign the return value if you need it.
- [x] **Characters** — `charAt`, `charCodeAt`, `codePointAt`, ES2022 **`at()`** (negatives work), and `text[i]`. `text[0] = "A"` does not change the string.
- [x] **Parts** — `slice(start, end)` (end not included; negatives from the end). `substring` treats negatives as 0. **`substr` is deprecated** (second arg is a length).
- [x] **Replace / split** — `replace` changes the **first** match; `/g` or `replaceAll` changes every match. `split("")` breaks emoji; use **`Intl.Segmenter`**.

<a id="js-string-methods-example-01"></a>

### **Example 1: `length`**

- [x] Strings are **primitive and immutable** — methods return a **new** string.
- [x] **`length`** is a property. A-Z has **26** characters.

Sandbox: `code_sandbox/js-string-methods/length.html`

```javascript
let text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let length = text.length;
```

![js-string-methods example 1 source](../code_sandbox/snaps/js-string-methods-01-code.png)

![js-string-methods example 1 result](../code_sandbox/snaps/js-string-methods-01-result.png)

- [x] **Outcome:** The length is **26**.

<a id="js-string-methods-example-02"></a>

### **Example 2: `charAt(0)`**

- [x] **`charAt(index)`** returns the character at that **0-based** position.
- [x] A missing index returns **`""`**, not `undefined`.

Sandbox: `code_sandbox/js-string-methods/charAt.html`

```javascript
let text = "HELLO WORLD";
let char = text.charAt(0);
```

![js-string-methods example 2 source](../code_sandbox/snaps/js-string-methods-02-code.png)

![js-string-methods example 2 result](../code_sandbox/snaps/js-string-methods-02-result.png)

- [x] **Outcome:** `charAt(0)` is **H**.

<a id="js-string-methods-example-03"></a>

### **Example 3: `charCodeAt(0)`**

- [x] **`charCodeAt(index)`** returns the **UTF-16 code unit** (0-65535).
- [x] For `'H'` that code is **72**.

Sandbox: `code_sandbox/js-string-methods/charCodeAt.html`

```javascript
let text = "HELLO WORLD";
let char = text.charCodeAt(0);
```

![js-string-methods example 3 source](../code_sandbox/snaps/js-string-methods-03-code.png)

![js-string-methods example 3 result](../code_sandbox/snaps/js-string-methods-03-result.png)

- [x] **Outcome:** The code is **72**.

<a id="js-string-methods-example-04"></a>

### **Example 4: `codePointAt(0)`**

- [x] **`codePointAt(index)`** returns the Unicode **code point**.
- [x] For BMP characters like `'H'` it matches `charCodeAt`. Prefer it for emoji.

Sandbox: `code_sandbox/js-string-methods/codePointAt.html`

```javascript
let text = "HELLO WORLD";
let code = text.codePointAt(0);
```

![js-string-methods example 4 source](../code_sandbox/snaps/js-string-methods-04-code.png)

![js-string-methods example 4 result](../code_sandbox/snaps/js-string-methods-04-result.png)

- [x] **Outcome:** The code point of **H** is **72**.

<a id="js-string-methods-example-05"></a>

### **Example 5: `at(2)`**

- [x] ES2022 **`at(index)`** returns the character at that index.
- [x] `at(2)` is the **third** character (indexes start at 0).

Sandbox: `code_sandbox/js-string-methods/at.html`

```javascript
const name = "W3Schools";
let letter = name.at(2);
```

![js-string-methods example 5 source](../code_sandbox/snaps/js-string-methods-05-code.png)

![js-string-methods example 5 result](../code_sandbox/snaps/js-string-methods-05-result.png)

- [x] **Outcome:** `at(2)` is **S**.

<a id="js-string-methods-example-06"></a>

### **Example 6: Property access `[2]`**

- [x] `name[2]` is the older **property-access** way to get the third character.
- [x] Same result as `at(2)` for a non-negative index.

Sandbox: `code_sandbox/js-string-methods/property-2.html`

```javascript
const name = "W3Schools";
let letter = name[2];
```

![js-string-methods example 6 source](../code_sandbox/snaps/js-string-methods-06-code.png)

![js-string-methods example 6 result](../code_sandbox/snaps/js-string-methods-06-result.png)

- [x] **Outcome:** `name[2]` is **S**.

<a id="js-string-methods-example-07"></a>

### **Example 7: `at(-5)`**

- [x] **`at()` allows negative indexes**; `charAt()` does not.
- [x] `at(-5)` is the fifth character **from the end**.

Sandbox: `code_sandbox/js-string-methods/at-neg5.html`

```javascript
const name = "W3Schools";
let letter = name.at(-5);
```

![js-string-methods example 7 source](../code_sandbox/snaps/js-string-methods-07-code.png)

![js-string-methods example 7 result](../code_sandbox/snaps/js-string-methods-07-result.png)

- [x] **Outcome:** `at(-5)` is **h**.

<a id="js-string-methods-example-08"></a>

### **Example 8: Property access `[0]`**

- [x] `text[0]` looks like an array index, but **strings are not arrays**.
- [x] A missing index is **`undefined`** (`charAt` would return `""`).
- [x] Property access is **read-only**.

Sandbox: `code_sandbox/js-string-methods/property-0.html`

```javascript
let text = "HELLO WORLD";
let char = text[0];
```

![js-string-methods example 8 source](../code_sandbox/snaps/js-string-methods-08-code.png)

![js-string-methods example 8 result](../code_sandbox/snaps/js-string-methods-08-result.png)

- [x] **Outcome:** `text[0]` is **H**. `text[99]` is **undefined**.

<a id="js-string-methods-example-09"></a>

### **Example 9: Sloppy mode `text[0] = "A"`**

- [x] In **sloppy mode**, `text[0] = "A"` does **not** throw and does **not** change the string.
- [x] Strings are immutable. The assignment is silently ignored.

Sandbox: `code_sandbox/js-string-methods/sloppy-assign.html`

```javascript
let text = "HELLO WORLD";
try {
  text[0] = "A";
} catch (err) {
  text = err.message;
}
```

![js-string-methods example 9 source](../code_sandbox/snaps/js-string-methods-09-code.png)

![js-string-methods example 9 result](../code_sandbox/snaps/js-string-methods-09-result.png)

- [x] **Outcome:** No exception. The string is still **HELLO WORLD** (`text[0]` remains **H**).

<a id="js-string-methods-example-10"></a>

### **Example 10: `concat()` Hello World**

- [x] **`concat()`** joins two or more strings and returns a **new** string.
- [x] Same result as **`+`**: `"Hello" + " " + "World"`.

Sandbox: `code_sandbox/js-string-methods/concat.html`

```javascript
let text1 = "Hello";
let text2 = "World";
let text3 = text1.concat(" ", text2);
```

![js-string-methods example 10 source](../code_sandbox/snaps/js-string-methods-10-code.png)

![js-string-methods example 10 result](../code_sandbox/snaps/js-string-methods-10-result.png)

- [x] **Outcome:** The joined string is **Hello World**.

<a id="js-string-methods-example-11"></a>

### **Example 11: `slice(7, 13)`**

- [x] **`slice(start, end)`** copies a section; **end is not included**.
- [x] Positions start at **0**. On `"Apple, Banana, Kiwi"`, index 7 is **B**.

Sandbox: `code_sandbox/js-string-methods/slice-7-13.html`

```javascript
let text = "Apple, Banana, Kiwi";
let part = text.slice(7, 13);
```

![js-string-methods example 11 source](../code_sandbox/snaps/js-string-methods-11-code.png)

![js-string-methods example 11 result](../code_sandbox/snaps/js-string-methods-11-result.png)

- [x] **Outcome:** `slice(7, 13)` is **Banana**.

<a id="js-string-methods-example-12"></a>

### **Example 12: `slice(7)`**

- [x] Omit the second parameter to take **the rest** of the string.

Sandbox: `code_sandbox/js-string-methods/slice-7.html`

```javascript
let text = "Apple, Banana, Kiwi";
let part = text.slice(7);
```

![js-string-methods example 12 source](../code_sandbox/snaps/js-string-methods-12-code.png)

![js-string-methods example 12 result](../code_sandbox/snaps/js-string-methods-12-result.png)

- [x] **Outcome:** `slice(7)` is **Banana, Kiwi**.

<a id="js-string-methods-example-13"></a>

### **Example 13: `slice(-12)`**

- [x] A **negative** parameter counts from the **end** of the string.

Sandbox: `code_sandbox/js-string-methods/slice-neg12.html`

```javascript
let text = "Apple, Banana, Kiwi";
let part = text.slice(-12);
```

![js-string-methods example 13 source](../code_sandbox/snaps/js-string-methods-13-code.png)

![js-string-methods example 13 result](../code_sandbox/snaps/js-string-methods-13-result.png)

- [x] **Outcome:** `slice(-12)` is **Banana, Kiwi**.

<a id="js-string-methods-example-14"></a>

### **Example 14: `slice(-12, -6)`**

- [x] Both start and end may be negative; end is still **not included**.

Sandbox: `code_sandbox/js-string-methods/slice-neg12-neg6.html`

```javascript
let text = "Apple, Banana, Kiwi";
let part = text.slice(-12, -6);
```

![js-string-methods example 14 source](../code_sandbox/snaps/js-string-methods-14-code.png)

![js-string-methods example 14 result](../code_sandbox/snaps/js-string-methods-14-result.png)

- [x] **Outcome:** `slice(-12, -6)` is **Banana**.

<a id="js-string-methods-example-15"></a>

### **Example 15: `substring(7, 13)`**

- [x] `substring()` is like `slice()`, but **negative** start/end become **0**.
- [x] If start > end, `substring` **swaps** them; `slice` returns empty.

Sandbox: `code_sandbox/js-string-methods/substring.html`

```javascript
let str = "Apple, Banana, Kiwi";
let part = str.substring(7, 13);
```

![js-string-methods example 15 source](../code_sandbox/snaps/js-string-methods-15-code.png)

![js-string-methods example 15 result](../code_sandbox/snaps/js-string-methods-15-result.png)

- [x] **Outcome:** `substring(7, 13)` is **Banana**.

<a id="js-string-methods-example-16"></a>

### **Example 16: `substr(7, 6)` (deprecated)**

- [x] **Deprecated.** The second argument is a **length**, not an end index.
- [x] Use **`substring()`** or **`slice()`** in new code. Still runs for compatibility.

Sandbox: `code_sandbox/js-string-methods/substr-7-6.html`

```javascript
let str = "Apple, Banana, Kiwi";
let part = str.substr(7, 6);
```

![js-string-methods example 16 source](../code_sandbox/snaps/js-string-methods-16-code.png)

![js-string-methods example 16 result](../code_sandbox/snaps/js-string-methods-16-result.png)

- [x] **Outcome:** `substr(7, 6)` is **Banana**. Prefer **slice/substring**.

<a id="js-string-methods-example-17"></a>

### **Example 17: `substr(7)` (deprecated)**

- [x] Omit the second parameter and `substr` takes the **rest** of the string.
- [x] Still **deprecated**.

Sandbox: `code_sandbox/js-string-methods/substr-7.html`

```javascript
let str = "Apple, Banana, Kiwi";
let part = str.substr(7);
```

![js-string-methods example 17 source](../code_sandbox/snaps/js-string-methods-17-code.png)

![js-string-methods example 17 result](../code_sandbox/snaps/js-string-methods-17-result.png)

- [x] **Outcome:** `substr(7)` is **Banana, Kiwi**.

<a id="js-string-methods-example-18"></a>

### **Example 18: `substr(-4)` (deprecated)**

- [x] A **negative** start counts from the end (length 4 here is **Kiwi**).
- [x] Do not use `substr` in new code.

Sandbox: `code_sandbox/js-string-methods/substr-neg4.html`

```javascript
let str = "Apple, Banana, Kiwi";
let part = str.substr(-4);
```

![js-string-methods example 18 source](../code_sandbox/snaps/js-string-methods-18-code.png)

![js-string-methods example 18 result](../code_sandbox/snaps/js-string-methods-18-result.png)

- [x] **Outcome:** `substr(-4)` is **Kiwi**.

<a id="js-string-methods-example-19"></a>

### **Example 19: `toUpperCase()`**

- [x] Returns a **new** string with all letters in upper case.
- [x] The original string is unchanged.

Sandbox: `code_sandbox/js-string-methods/toUpperCase.html`

```javascript
let text1 = "Hello World!";
let text2 = text1.toUpperCase();
```

![js-string-methods example 19 source](../code_sandbox/snaps/js-string-methods-19-code.png)

![js-string-methods example 19 result](../code_sandbox/snaps/js-string-methods-19-result.png)

- [x] **Outcome:** The new string is **HELLO WORLD!**; the original is still **Hello World!**

<a id="js-string-methods-example-20"></a>

### **Example 20: `toLowerCase()`**

- [x] Returns a **new** string with all letters in lower case.

Sandbox: `code_sandbox/js-string-methods/toLowerCase.html`

```javascript
let text1 = "Hello World!";
let text2 = text1.toLowerCase();
```

![js-string-methods example 20 source](../code_sandbox/snaps/js-string-methods-20-code.png)

![js-string-methods example 20 result](../code_sandbox/snaps/js-string-methods-20-result.png)

- [x] **Outcome:** The result is **hello world!**

<a id="js-string-methods-example-21"></a>

### **Example 21: `isWellFormed()` true**

- [x] Returns **`true`** if the string has no **lone surrogates** (broken UTF-16 pairs).
- [x] Ordinary text like `Hello world!` is well formed.

Sandbox: `code_sandbox/js-string-methods/isWellFormed-ok.html`

```javascript
let text = "Hello world!";
let result = text.isWellFormed();
```

![js-string-methods example 21 source](../code_sandbox/snaps/js-string-methods-21-code.png)

![js-string-methods example 21 result](../code_sandbox/snaps/js-string-methods-21-result.png)

- [x] **Outcome:** **true** — this string is well formed.

<a id="js-string-methods-example-22"></a>

### **Example 22: `isWellFormed()` lone surrogate**

- [x] A lone `\uD800` is not a valid UTF-16 pair, so the string is **not** well formed.

Sandbox: `code_sandbox/js-string-methods/isWellFormed-bad.html`

```javascript
let text = "Hello World \uD800";
let result = text.isWellFormed();
```

![js-string-methods example 22 source](../code_sandbox/snaps/js-string-methods-22-code.png)

![js-string-methods example 22 result](../code_sandbox/snaps/js-string-methods-22-result.png)

- [x] **Outcome:** **false** — the lone surrogate makes the string ill-formed.

<a id="js-string-methods-example-23"></a>

### **Example 23: `toWellFormed()`**

- [x] Returns a new string where **lone surrogates** are replaced with **U+FFFD** (`�`).

Sandbox: `code_sandbox/js-string-methods/toWellFormed.html`

```javascript
let text = "Hello World \uD800";
let result = text.toWellFormed();
```

![js-string-methods example 23 source](../code_sandbox/snaps/js-string-methods-23-code.png)

![js-string-methods example 23 result](../code_sandbox/snaps/js-string-methods-23-result.png)

- [x] **Outcome:** The original is **not** well formed; `toWellFormed()` replaces the lone surrogate with **�**.

<a id="js-string-methods-example-24"></a>

### **Example 24: `trim()`**

- [x] Removes **whitespace from both ends**. Spaces in the **middle** stay.

Sandbox: `code_sandbox/js-string-methods/trim.html`

```javascript
let text1 = " Hello World! ";
let text2 = text1.trim();
```

![js-string-methods example 24 source](../code_sandbox/snaps/js-string-methods-24-code.png)

![js-string-methods example 24 result](../code_sandbox/snaps/js-string-methods-24-result.png)

- [x] **Outcome:** The trimmed value is **'Hello World!'**.

<a id="js-string-methods-example-25"></a>

### **Example 25: `trimStart()`**

- [x] Removes whitespace from the **start only** (ES2019). Alias: `trimLeft()`.

Sandbox: `code_sandbox/js-string-methods/trimStart.html`

```javascript
let text1 = " Hello World! ";
let text2 = text1.trimStart();
```

![js-string-methods example 25 source](../code_sandbox/snaps/js-string-methods-25-code.png)

![js-string-methods example 25 result](../code_sandbox/snaps/js-string-methods-25-result.png)

- [x] **Outcome:** Leading space is gone; trailing space remains: **'Hello World! '**.

<a id="js-string-methods-example-26"></a>

### **Example 26: `trimEnd()`**

- [x] Removes whitespace from the **end only** (ES2019). Alias: `trimRight()`.

Sandbox: `code_sandbox/js-string-methods/trimEnd.html`

```javascript
let text1 = " Hello World! ";
let text2 = text1.trimEnd();
```

![js-string-methods example 26 source](../code_sandbox/snaps/js-string-methods-26-code.png)

![js-string-methods example 26 result](../code_sandbox/snaps/js-string-methods-26-result.png)

- [x] **Outcome:** Trailing space is gone; leading space remains: **' Hello World!'**.

<a id="js-string-methods-example-27"></a>

### **Example 27: `padStart(4, "0")`**

- [x] Pads the **start** until the string reaches the given length.
- [x] `"5".padStart(4, "0")` is a typical **zero-pad**.

Sandbox: `code_sandbox/js-string-methods/padStart-0.html`

```javascript
let text = "5";
let padded = text.padStart(4, "0");
```

![js-string-methods example 27 source](../code_sandbox/snaps/js-string-methods-27-code.png)

![js-string-methods example 27 result](../code_sandbox/snaps/js-string-methods-27-result.png)

- [x] **Outcome:** The result is **0005**.

<a id="js-string-methods-example-28"></a>

### **Example 28: `padStart(4, "x")`**

- [x] The pad string can be any text, not just zeros.

Sandbox: `code_sandbox/js-string-methods/padStart-x.html`

```javascript
let text = "5";
let padded = text.padStart(4, "x");
```

![js-string-methods example 28 source](../code_sandbox/snaps/js-string-methods-28-code.png)

![js-string-methods example 28 result](../code_sandbox/snaps/js-string-methods-28-result.png)

- [x] **Outcome:** The result is **xxx5**.

<a id="js-string-methods-example-29"></a>

### **Example 29: `padStart` on a number via `toString()`**

- [x] `padStart` is a **string** method. Convert a number with **`toString()`** first.

Sandbox: `code_sandbox/js-string-methods/padStart-number.html`

```javascript
let numb = 5;
let text = numb.toString();
let padded = text.padStart(4, "0");
```

![js-string-methods example 29 source](../code_sandbox/snaps/js-string-methods-29-code.png)

![js-string-methods example 29 result](../code_sandbox/snaps/js-string-methods-29-result.png)

- [x] **Outcome:** The padded number-as-string is **0005**.

<a id="js-string-methods-example-30"></a>

### **Example 30: `padEnd(4, "0")`**

- [x] Pads the **end** until the string reaches the given length.

Sandbox: `code_sandbox/js-string-methods/padEnd-0.html`

```javascript
let text = "5";
let padded = text.padEnd(4, "0");
```

![js-string-methods example 30 source](../code_sandbox/snaps/js-string-methods-30-code.png)

![js-string-methods example 30 result](../code_sandbox/snaps/js-string-methods-30-result.png)

- [x] **Outcome:** The result is **5000**.

<a id="js-string-methods-example-31"></a>

### **Example 31: `padEnd(4, "x")`**

- [x] Pad character **x** is appended until length 4.

Sandbox: `code_sandbox/js-string-methods/padEnd-x.html`

```javascript
let text = "5";
let padded = text.padEnd(4, "x");
```

![js-string-methods example 31 source](../code_sandbox/snaps/js-string-methods-31-code.png)

![js-string-methods example 31 result](../code_sandbox/snaps/js-string-methods-31-result.png)

- [x] **Outcome:** The result is **5xxx**.

<a id="js-string-methods-example-32"></a>

### **Example 32: `padEnd` on a number via `toString()`**

- [x] Same rule as `padStart`: convert the number **first**.

Sandbox: `code_sandbox/js-string-methods/padEnd-number.html`

```javascript
let numb = 5;
let text = numb.toString();
let padded = text.padEnd(4, "0");
```

![js-string-methods example 32 source](../code_sandbox/snaps/js-string-methods-32-code.png)

![js-string-methods example 32 result](../code_sandbox/snaps/js-string-methods-32-result.png)

- [x] **Outcome:** The padded number-as-string is **5000**.

<a id="js-string-methods-example-33"></a>

### **Example 33: `repeat(2)`**

- [x] **`repeat(count)`** returns a **new** string with that many copies.
- [x] Does not change the original. `count` must be a non-negative integer.

Sandbox: `code_sandbox/js-string-methods/repeat-2.html`

```javascript
let text = "Hello world!";
let result = text.repeat(2);
```

![js-string-methods example 33 source](../code_sandbox/snaps/js-string-methods-33-code.png)

![js-string-methods example 33 result](../code_sandbox/snaps/js-string-methods-33-result.png)

- [x] **Outcome:** The result is **Hello world!Hello world!**

<a id="js-string-methods-example-34"></a>

### **Example 34: `repeat(4)`**

- [x] Four copies of `Hello world!` are concatenated, original unchanged.

Sandbox: `code_sandbox/js-string-methods/repeat-4.html`

```javascript
let text = "Hello world!";
let result = text.repeat(4);
```

![js-string-methods example 34 source](../code_sandbox/snaps/js-string-methods-34-code.png)

![js-string-methods example 34 result](../code_sandbox/snaps/js-string-methods-34-result.png)

- [x] **Outcome:** The result is **Hello world!** repeated **four** times.

<a id="js-string-methods-example-35"></a>

### **Example 35: `replace()` first Microsoft**

- [x] `replace` returns a **new** string. It does **not** change the original.
- [x] By default it replaces only the **first** match.

Sandbox: `code_sandbox/js-string-methods/replace-first.html`

```javascript
let text = "Please visit Microsoft!";
let newText = text.replace("Microsoft", "W3Schools");
```

![js-string-methods example 35 source](../code_sandbox/snaps/js-string-methods-35-code.png)

![js-string-methods example 35 result](../code_sandbox/snaps/js-string-methods-35-result.png)

- [x] **Outcome:** The result is **Please visit W3Schools!**

<a id="js-string-methods-example-36"></a>

### **Example 36: `replace()` only the first of two**

- [x] With two **Microsoft**s, a string search still changes **only the first**.

Sandbox: `code_sandbox/js-string-methods/replace-first-of-two.html`

```javascript
let text = "Please visit Microsoft and Microsoft!";
let newText = text.replace("Microsoft", "W3Schools");
```

![js-string-methods example 36 source](../code_sandbox/snaps/js-string-methods-36-code.png)

![js-string-methods example 36 result](../code_sandbox/snaps/js-string-methods-36-result.png)

- [x] **Outcome:** Only the first match changes: **Please visit W3Schools and Microsoft!**

<a id="js-string-methods-example-37"></a>

### **Example 37: `replace("MICROSOFT")` case fail**

- [x] `replace` is **case-sensitive** by default.
- [x] Searching for **MICROSOFT** does not match **Microsoft**.

Sandbox: `code_sandbox/js-string-methods/replace-case-fail.html`

```javascript
let text = "Please visit Microsoft!";
let newText = text.replace("MICROSOFT", "W3Schools");
```

![js-string-methods example 37 source](../code_sandbox/snaps/js-string-methods-37-code.png)

![js-string-methods example 37 result](../code_sandbox/snaps/js-string-methods-37-result.png)

- [x] **Outcome:** Nothing changes: **Please visit Microsoft!**

<a id="js-string-methods-example-38"></a>

### **Example 38: `replace(/MICROSOFT/i)`**

- [x] A regex with the **`/i`** flag ignores case.
- [x] Regular expressions are written **without quotes**.

Sandbox: `code_sandbox/js-string-methods/replace-i.html`

```javascript
let text = "Please visit Microsoft!";
let newText = text.replace(/MICROSOFT/i, "W3Schools");
```

![js-string-methods example 38 source](../code_sandbox/snaps/js-string-methods-38-code.png)

![js-string-methods example 38 result](../code_sandbox/snaps/js-string-methods-38-result.png)

- [x] **Outcome:** Case-insensitive replace yields **Please visit W3Schools!**

<a id="js-string-methods-example-39"></a>

### **Example 39: `replace(/Microsoft/g)`**

- [x] The **`/g`** flag replaces **every** match.
- [x] Without `/g` (or `replaceAll`) only the first match changes.

Sandbox: `code_sandbox/js-string-methods/replace-g.html`

```javascript
let text = "Please visit Microsoft and Microsoft!";
let newText = text.replace(/Microsoft/g, "W3Schools");
```

![js-string-methods example 39 source](../code_sandbox/snaps/js-string-methods-39-code.png)

![js-string-methods example 39 result](../code_sandbox/snaps/js-string-methods-39-result.png)

- [x] **Outcome:** Both matches change: **Please visit W3Schools and W3Schools!**

<a id="js-string-methods-example-40"></a>

### **Example 40: `replaceAll("Cats")`**

- [x] **`replaceAll()`** (ES2021) replaces **every** string match.
- [x] This Tryit then lowercases **cats** as well, so both casings become dogs.

Sandbox: `code_sandbox/js-string-methods/replaceAll-cats.html`

```javascript
let text = "I love cats. Cats are very easy to love. Cats are very popular.";
text = text.replaceAll("Cats", "Dogs");
text = text.replaceAll("cats", "dogs");
```

![js-string-methods example 40 source](../code_sandbox/snaps/js-string-methods-40-code.png)

![js-string-methods example 40 result](../code_sandbox/snaps/js-string-methods-40-result.png)

- [x] **Outcome:** The result is **I love dogs. Dogs are very easy to love. Dogs are very popular.**

<a id="js-string-methods-example-41"></a>

### **Example 41: `replaceAll(/Cats/g)`**

- [x] If the search is a **regex**, it **must** include **`g`** or you get a **TypeError**.
- [x] A second `/cats/g` pass handles the lowercase word.

Sandbox: `code_sandbox/js-string-methods/replaceAll-regex.html`

```javascript
let text = "I love cats. Cats are very easy to love. Cats are very popular.";
text = text.replaceAll(/Cats/g, "Dogs");
text = text.replaceAll(/cats/g, "dogs");
```

![js-string-methods example 41 source](../code_sandbox/snaps/js-string-methods-41-code.png)

![js-string-methods example 41 result](../code_sandbox/snaps/js-string-methods-41-result.png)

- [x] **Outcome:** Same result: **I love dogs. Dogs are very easy to love. Dogs are very popular.**

<a id="js-string-methods-example-42"></a>

### **Example 42: `split("")`**

- [x] `split("")` returns an array of **single UTF-16 units**.
- [x] Fine for plain ASCII; **unsafe for emoji** (see later examples).

Sandbox: `code_sandbox/js-string-methods/split-chars.html`

```javascript
let text = "Hi fox!";
const myArr = text.split("");
```

![js-string-methods example 42 source](../code_sandbox/snaps/js-string-methods-42-code.png)

![js-string-methods example 42 result](../code_sandbox/snaps/js-string-methods-42-result.png)

- [x] **Outcome:** The array is **["H","i"," ","f","o","x","!"]**.

<a id="js-string-methods-example-43"></a>

### **Example 43: `split(" ")`**

- [x] Splitting on a **space** yields an array of **words**.
- [x] The W3Schools snippet for this Tryit accidentally shows `split("")`; the intended separator is `" "`.

Sandbox: `code_sandbox/js-string-methods/split-spaces.html`

```javascript
let text = "The quick brown fox.";
const myArr = text.split(" ");
```

![js-string-methods example 43 source](../code_sandbox/snaps/js-string-methods-43-code.png)

![js-string-methods example 43 result](../code_sandbox/snaps/js-string-methods-43-result.png)

- [x] **Outcome:** The array is **["The","quick","brown","fox."]**.

<a id="js-string-methods-example-44"></a>

### **Example 44: `split()` with no separator**

- [x] If the separator is **omitted**, the array contains the **whole string** at index `[0]`.

Sandbox: `code_sandbox/js-string-methods/split-omitted.html`

```javascript
let text = "The quick brown fox.";
const myArr = text.split();
```

![js-string-methods example 44 source](../code_sandbox/snaps/js-string-methods-44-code.png)

![js-string-methods example 44 result](../code_sandbox/snaps/js-string-methods-44-result.png)

- [x] **Outcome:** The array is **["The quick brown fox."]**.

<a id="js-string-methods-example-45"></a>

### **Example 45: `split("")` is unsafe for emoji**

- [x] `split("")` splits **UTF-16 code units** and **breaks** surrogate pairs and ZWJ sequences.
- [x] The family emoji is sliced into many broken fragments.

Sandbox: `code_sandbox/js-string-methods/split-emoji.html`

```javascript
let text = "👨‍👩‍👧‍👦";
const myArr = text.split("");
```

![js-string-methods example 45 source](../code_sandbox/snaps/js-string-methods-45-code.png)

![js-string-methods example 45 result](../code_sandbox/snaps/js-string-methods-45-result.png)

- [x] **Outcome:** The family emoji splits into **many** UTF-16 pieces (length **11**), not one character.

<a id="js-string-methods-example-46"></a>

### **Example 46: `Intl.Segmenter` safe split**

- [x] **`Intl.Segmenter`** with `granularity: "grapheme"` keeps complex emoji together.
- [x] This is the **safe** way to walk visible characters.

Sandbox: `code_sandbox/js-string-methods/segmenter.html`

```javascript
let text = "👨‍👩‍👧‍👦";
const segmenter = new Intl.Segmenter("en", { granularity: "grapheme" });
const myArr = Array.from(segmenter.segment(text), (s) => s.segment);
```

![js-string-methods example 46 source](../code_sandbox/snaps/js-string-methods-46-code.png)

![js-string-methods example 46 result](../code_sandbox/snaps/js-string-methods-46-result.png)

- [x] **Outcome:** The segmenter yields **one** grapheme: the family emoji (length **1**).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-string-methods/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Do string methods change the original string?

<details>
<summary>Answer</summary>

- [x] **No.** Strings are **immutable**.
- [x] Methods return a **new** string.

</details>

### Question 2: What is `"ABCDEFGHIJKLMNOPQRSTUVWXYZ".length`?

<details>
<summary>Answer</summary>

- [x] **26.**

</details>

### Question 3: What does `"HELLO WORLD".charAt(0)` return?

<details>
<summary>Answer</summary>

- [x] **H.**

</details>

### Question 4: What does `charCodeAt(0)` / `codePointAt(0)` return for `'H'`?

<details>
<summary>Answer</summary>

- [x] **72.**

</details>

### Question 5: What is `"W3Schools".at(2)`? What about `at(-5)`?

<details>
<summary>Answer</summary>

- [x] `at(2)` is **S**.
- [x] `at(-5)` is **h** (fifth from the end).

</details>

### Question 6: Does `text[0] = "A"` change `"HELLO WORLD"` in sloppy mode?

<details>
<summary>Answer</summary>

- [x] **No.** The assignment is ignored.
- [x] The string stays **HELLO WORLD**.

</details>

### Question 7: What does `"Hello".concat(" ", "World")` return?

<details>
<summary>Answer</summary>

- [x] **Hello World.**

</details>

### Question 8: What does `"Apple, Banana, Kiwi".slice(7, 13)` return?

<details>
<summary>Answer</summary>

- [x] **Banana** (end index not included).

</details>

### Question 9: What does `slice(7)` return on that fruit string?

<details>
<summary>Answer</summary>

- [x] **Banana, Kiwi.**

</details>

### Question 10: Should you use `substr()`?

<details>
<summary>Answer</summary>

- [x] **No.** It is **deprecated**.
- [x] Use **`slice()`** or **`substring()`**.
- [x] `substr(7, 6)` is still **Banana** if you run it.

</details>

### Question 11: What does `"5".padStart(4, "0")` return? `padEnd`?

<details>
<summary>Answer</summary>

- [x] `padStart` → **0005**.
- [x] `padEnd` → **5000**.
- [x] Convert numbers with **`toString()`** first.

</details>

### Question 12: Does `replace("MICROSOFT", ...)` change `Please visit Microsoft!`?

<details>
<summary>Answer</summary>

- [x] **No.** `replace` is case-sensitive.
- [x] Use **`/MICROSOFT/i`** to ignore case.

</details>

### Question 13: How do you replace every Microsoft?

<details>
<summary>Answer</summary>

- [x] A regex with **`/g`**, or **`replaceAll()`**.

</details>

### Question 14: What does `"Hi fox!".split("")` return?

<details>
<summary>Answer</summary>

- [x] **["H","i"," ","f","o","x","!"]**.

</details>

### Question 15: Why is `split("")` unsafe for the family emoji?

<details>
<summary>Answer</summary>

- [x] It splits **UTF-16 code units** and breaks the ZWJ sequence (length **11**).
- [x] **`Intl.Segmenter`** keeps **one** grapheme.

</details>

</details>

## Summary

String methods return **new** strings. Use `length`, `charAt` / `at` (negatives), `slice` / `substring` (not deprecated `substr`), case / well-formed / trim / pad / repeat, `replace` / `replaceAll`, and `split`. `text[0] = "A"` does nothing. `replace` changes the first match unless `/g`. Avoid `split("")` on emoji; use `Intl.Segmenter`.

## References

- [JS String Methods (W3Schools)](https://www.w3schools.com/js/js_string_methods.asp)
- [MDN: String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
- [MDN: String.prototype.slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
- [MDN: String.prototype.replaceAll()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
- [MDN: Intl.Segmenter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter)
