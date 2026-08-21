# JS String Reference

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

This page is the **complete String reference** (revised July 2025): every **property and method** from **`at()`** through **`valueOf()`**, plus the old **HTML wrappers**. All methods return a **new** value — they do **not** change the original string. Each table row below is its own Example, the same grain as **JS Output**.

This section has **39** examples:

- [x] **Example 1:** `at()` [View](#js-string-reference-example-01)
- [x] **Example 2:** `charAt()` [View](#js-string-reference-example-02)
- [x] **Example 3:** `charCodeAt()` [View](#js-string-reference-example-03)
- [x] **Example 4:** `codePointAt()` [View](#js-string-reference-example-04)
- [x] **Example 5:** `concat()` [View](#js-string-reference-example-05)
- [x] **Example 6:** `constructor` [View](#js-string-reference-example-06)
- [x] **Example 7:** `endsWith()` [View](#js-string-reference-example-07)
- [x] **Example 8:** `String.fromCharCode()` [View](#js-string-reference-example-08)
- [x] **Example 9:** `includes()` [View](#js-string-reference-example-09)
- [x] **Example 10:** `indexOf()` [View](#js-string-reference-example-10)
- [x] **Example 11:** `isWellFormed()` [View](#js-string-reference-example-11)
- [x] **Example 12:** `lastIndexOf()` [View](#js-string-reference-example-12)
- [x] **Example 13:** `length` [View](#js-string-reference-example-13)
- [x] **Example 14:** `localeCompare()` [View](#js-string-reference-example-14)
- [x] **Example 15:** `match()` [View](#js-string-reference-example-15)
- [x] **Example 16:** `matchAll()` [View](#js-string-reference-example-16)
- [x] **Example 17:** `padEnd()` [View](#js-string-reference-example-17)
- [x] **Example 18:** `padStart()` [View](#js-string-reference-example-18)
- [x] **Example 19:** `prototype` [View](#js-string-reference-example-19)
- [x] **Example 20:** `repeat()` [View](#js-string-reference-example-20)
- [x] **Example 21:** `replace()` [View](#js-string-reference-example-21)
- [x] **Example 22:** `replaceAll()` [View](#js-string-reference-example-22)
- [x] **Example 23:** `search()` [View](#js-string-reference-example-23)
- [x] **Example 24:** `slice()` [View](#js-string-reference-example-24)
- [x] **Example 25:** `split()` [View](#js-string-reference-example-25)
- [x] **Example 26:** `startsWith()` [View](#js-string-reference-example-26)
- [x] **Example 27:** `substr()` (deprecated) [View](#js-string-reference-example-27)
- [x] **Example 28:** `substring()` [View](#js-string-reference-example-28)
- [x] **Example 29:** `toLocaleLowerCase()` [View](#js-string-reference-example-29)
- [x] **Example 30:** `toLocaleUpperCase()` [View](#js-string-reference-example-30)
- [x] **Example 31:** `toLowerCase()` [View](#js-string-reference-example-31)
- [x] **Example 32:** `toString()` [View](#js-string-reference-example-32)
- [x] **Example 33:** `toUpperCase()` [View](#js-string-reference-example-33)
- [x] **Example 34:** `toWellFormed()` [View](#js-string-reference-example-34)
- [x] **Example 35:** `trim()` [View](#js-string-reference-example-35)
- [x] **Example 36:** `trimEnd()` [View](#js-string-reference-example-36)
- [x] **Example 37:** `trimStart()` [View](#js-string-reference-example-37)
- [x] **Example 38:** `valueOf()` [View](#js-string-reference-example-38)
- [x] **Example 39:** HTML wrapper methods (deprecated — do not use) [View](#js-string-reference-example-39)

## Detailed Explanation

- [x] **Core idea** — string methods never mutate the original; they return a new string (or a number / boolean / array / iterator).
- [x] **Table grain** — one Example per reference-table row. Deprecated HTML wrappers are one grouped Example that still **runs every wrapper**.
- [x] **`substr()` is deprecated** — use `substring()` or `slice()`.

<a id="js-string-reference-example-01"></a>

### **Example 1: `at()`**

- [x] **`at(index)`** returns the character at that index (0-based).
- [x] **Negative indexes** count from the end (`at(-1)` is the last character).
- [x] ES2022. **`charAt()` cannot take negatives**; use `at()` when you want that.

Sandbox: `code_sandbox/js-string-reference/at.html`

```javascript
const name = "W3Schools";
name.at(2);
name.at(-5);
```

![js-string-reference example 1 source](../code_sandbox/snaps/js-string-reference-01-code.png)

![js-string-reference example 1 result](../code_sandbox/snaps/js-string-reference-01-result.png)

- [x] **Outcome:** `at(2)` is **S** (third character); `at(-5)` is **h**.

<a id="js-string-reference-example-02"></a>

### **Example 2: `charAt()`**

- [x] **`charAt(index)`** returns the character at that position.
- [x] A missing index returns **`""`** (empty string), not `undefined`.
- [x] Does **not** accept negative indexes.

Sandbox: `code_sandbox/js-string-reference/charAt.html`

```javascript
let text = "HELLO WORLD";
let char = text.charAt(0);
```

![js-string-reference example 2 source](../code_sandbox/snaps/js-string-reference-02-code.png)

![js-string-reference example 2 result](../code_sandbox/snaps/js-string-reference-02-result.png)

- [x] **Outcome:** `charAt(0)` is **H**. `charAt(99)` is an **empty string**.

<a id="js-string-reference-example-03"></a>

### **Example 3: `charCodeAt()`**

- [x] **`charCodeAt(index)`** returns the **UTF-16 code unit** (0–65535) at that index.
- [x] For `'H'` that code is **72**.

Sandbox: `code_sandbox/js-string-reference/charCodeAt.html`

```javascript
let text = "HELLO WORLD";
let char = text.charCodeAt(0);
```

![js-string-reference example 3 source](../code_sandbox/snaps/js-string-reference-03-code.png)

![js-string-reference example 3 result](../code_sandbox/snaps/js-string-reference-03-result.png)

- [x] **Outcome:** **72** — the UTF-16 code for **H**.

<a id="js-string-reference-example-04"></a>

### **Example 4: `codePointAt()`**

- [x] **`codePointAt(index)`** returns the Unicode **code point** at that index.
- [x] For BMP characters like `'H'` it matches `charCodeAt`. It is the right choice for characters outside the BMP (emoji).

Sandbox: `code_sandbox/js-string-reference/codePointAt.html`

```javascript
let text = "HELLO WORLD";
let code = text.codePointAt(0);
```

![js-string-reference example 4 source](../code_sandbox/snaps/js-string-reference-04-code.png)

![js-string-reference example 4 result](../code_sandbox/snaps/js-string-reference-04-result.png)

- [x] **Outcome:** **72** for `'H'`.

<a id="js-string-reference-example-05"></a>

### **Example 5: `concat()`**

- [x] **`concat()`** joins two or more strings and returns a **new** string.
- [x] Same result as **`+`**: `"Hello" + " " + "World!"`.

Sandbox: `code_sandbox/js-string-reference/concat.html`

```javascript
let text1 = "Hello";
let text2 = "World";
let text3 = text1.concat(" ", text2);
```

![js-string-reference example 5 source](../code_sandbox/snaps/js-string-reference-05-code.png)

![js-string-reference example 5 result](../code_sandbox/snaps/js-string-reference-05-result.png)

- [x] **Outcome:** The joined string is **Hello World**.

<a id="js-string-reference-example-06"></a>

### **Example 6: `constructor`**

- [x] The **`constructor`** property is the function that created the instance — for a string that is **`String`**.
- [x] This is a **property**, not a method you call for everyday text work.

Sandbox: `code_sandbox/js-string-reference/constructor.html`

```javascript
let text = "Hello";
text.constructor === String;
```

![js-string-reference example 6 source](../code_sandbox/snaps/js-string-reference-06-code.png)

![js-string-reference example 6 result](../code_sandbox/snaps/js-string-reference-06-result.png)

- [x] **Outcome:** `constructor === String` is **true**; the name is **String**.

<a id="js-string-reference-example-07"></a>

### **Example 7: `endsWith()`**

- [x] **`endsWith(search)`** returns **`true`** if the string ends with that text.
- [x] Case-sensitive. Optional second argument: treat the string as if it were only that long.

Sandbox: `code_sandbox/js-string-reference/endsWith.html`

```javascript
let text = "John Doe";
text.endsWith("Doe");
```

![js-string-reference example 7 source](../code_sandbox/snaps/js-string-reference-07-code.png)

![js-string-reference example 7 result](../code_sandbox/snaps/js-string-reference-07-result.png)

- [x] **Outcome:** **true** for "Doe"; **false** for "John".

<a id="js-string-reference-example-08"></a>

### **Example 8: `String.fromCharCode()`**

- [x] **Static** method on **`String`** (not `text.fromCharCode`).
- [x] Turns UTF-16 code units into a string: `72, 69, 76, 76, 79` → **HELLO**.

Sandbox: `code_sandbox/js-string-reference/fromCharCode.html`

```javascript
String.fromCharCode(72, 69, 76, 76, 79);
```

![js-string-reference example 8 source](../code_sandbox/snaps/js-string-reference-08-code.png)

![js-string-reference example 8 result](../code_sandbox/snaps/js-string-reference-08-result.png)

- [x] **Outcome:** The characters spell **HELLO**.

<a id="js-string-reference-example-09"></a>

### **Example 9: `includes()`**

- [x] **`includes(search)`** returns **`true`** if the substring exists anywhere.
- [x] Case-sensitive ES6 method. Optional start index.

Sandbox: `code_sandbox/js-string-reference/includes.html`

```javascript
let text = "Hello world, welcome to the universe.";
text.includes("world");
```

![js-string-reference example 9 source](../code_sandbox/snaps/js-string-reference-09-code.png)

![js-string-reference example 9 result](../code_sandbox/snaps/js-string-reference-09-result.png)

- [x] **Outcome:** **true** from the start; **false** if you start searching at index **12** (past "world").

<a id="js-string-reference-example-10"></a>

### **Example 10: `indexOf()`**

- [x] **`indexOf(search)`** returns the **first** index of the substring, or **`-1`** if missing.
- [x] Positions start at **0**. Optional second argument: start index.

Sandbox: `code_sandbox/js-string-reference/indexOf.html`

```javascript
let text = "Please locate where 'locate' occurs!";
let index = text.indexOf("locate");
```

![js-string-reference example 10 source](../code_sandbox/snaps/js-string-reference-10-code.png)

![js-string-reference example 10 result](../code_sandbox/snaps/js-string-reference-10-result.png)

- [x] **Outcome:** First "locate" is at **7**; from index 15 the next is **21**; missing text is **-1**.

<a id="js-string-reference-example-11"></a>

### **Example 11: `isWellFormed()`**

- [x] Returns **`true`** if the string has no **lone surrogates** (broken UTF-16 pairs).
- [x] A lone `\uD800` makes it **false**.

Sandbox: `code_sandbox/js-string-reference/isWellFormed.html`

```javascript
let ok = "Hello world!".isWellFormed();
let bad = "Hello World \uD800".isWellFormed();
```

![js-string-reference example 11 source](../code_sandbox/snaps/js-string-reference-11-code.png)

![js-string-reference example 11 result](../code_sandbox/snaps/js-string-reference-11-result.png)

- [x] **Outcome:** Normal text is **true**; a lone surrogate is **false**.

<a id="js-string-reference-example-12"></a>

### **Example 12: `lastIndexOf()`**

- [x] **`lastIndexOf(search)`** returns the **last** occurrence, or **`-1`**.
- [x] With a start index it searches **backward** from that position.

Sandbox: `code_sandbox/js-string-reference/lastIndexOf.html`

```javascript
let text = "Please locate where 'locate' occurs!";
text.lastIndexOf("locate");
```

![js-string-reference example 12 source](../code_sandbox/snaps/js-string-reference-12-code.png)

![js-string-reference example 12 result](../code_sandbox/snaps/js-string-reference-12-result.png)

- [x] **Outcome:** Last "locate" is **21**; searching backward from 15 finds **7**; "John" is **-1**.

<a id="js-string-reference-example-13"></a>

### **Example 13: `length`**

- [x] **`length`** is a **property**, not a method — no parentheses.
- [x] It counts UTF-16 code units (emoji can count as 2).

Sandbox: `code_sandbox/js-string-reference/length.html`

```javascript
let text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let length = text.length;
```

![js-string-reference example 13 source](../code_sandbox/snaps/js-string-reference-13-code.png)

![js-string-reference example 13 result](../code_sandbox/snaps/js-string-reference-13-result.png)

- [x] **Outcome:** A–Z is **26** characters.

<a id="js-string-reference-example-14"></a>

### **Example 14: `localeCompare()`**

- [x] Compares two strings in the **current locale** and returns a **negative / 0 / positive** number (sort order).
- [x] `"ab".localeCompare("cd")` is negative because **ab** comes first.

Sandbox: `code_sandbox/js-string-reference/localeCompare.html`

```javascript
"ab".localeCompare("cd");
"cd".localeCompare("ab");
"ab".localeCompare("ab");
```

![js-string-reference example 14 source](../code_sandbox/snaps/js-string-reference-14-code.png)

![js-string-reference example 14 result](../code_sandbox/snaps/js-string-reference-14-result.png)

- [x] **Outcome:** **ab** vs **cd** is negative; reverse is positive; equal strings return **0**.

<a id="js-string-reference-example-15"></a>

### **Example 15: `match()`**

- [x] Returns an **array** of matches (or `null` if none).
- [x] Without **`/g`**, you get details of the **first** match. With **`/g`** (and `/i`) you get all matches.

Sandbox: `code_sandbox/js-string-reference/match.html`

```javascript
let text = "The rain in SPAIN stays mainly in the plain";
text.match(/ain/gi);
```

![js-string-reference example 15 source](../code_sandbox/snaps/js-string-reference-15-code.png)

![js-string-reference example 15 result](../code_sandbox/snaps/js-string-reference-15-result.png)

- [x] **Outcome:** The global, case-insensitive match is **ain,AIN,ain,ain**.

<a id="js-string-reference-example-16"></a>

### **Example 16: `matchAll()`**

- [x] Returns an **iterator** of all matches (ES2020).
- [x] If you pass a regex, it **must** have the **`g`** flag or you get a **TypeError**.

Sandbox: `code_sandbox/js-string-reference/matchAll.html`

```javascript
let text = "I love Cats. Cats are great.";
Array.from(text.matchAll(/Cats/g), (m) => m[0]);
```

![js-string-reference example 16 source](../code_sandbox/snaps/js-string-reference-16-code.png)

![js-string-reference example 16 result](../code_sandbox/snaps/js-string-reference-16-result.png)

- [x] **Outcome:** The iterator yields **Cats, Cats** (two matches).

<a id="js-string-reference-example-17"></a>

### **Example 17: `padEnd()`**

- [x] Pads the **end** of the string until it reaches a given length.
- [x] It is a **string** method — convert numbers with **`toString()`** first.

Sandbox: `code_sandbox/js-string-reference/padEnd.html`

```javascript
let text = "5";
text.padEnd(4, "0");
text.padEnd(4, "x");
```

![js-string-reference example 17 source](../code_sandbox/snaps/js-string-reference-17-code.png)

![js-string-reference example 17 result](../code_sandbox/snaps/js-string-reference-17-result.png)

- [x] **Outcome:** **5000** and **5xxx**.

<a id="js-string-reference-example-18"></a>

### **Example 18: `padStart()`**

- [x] Pads the **start** of the string until it reaches a given length.
- [x] Useful for zero-padding: `"5".padStart(4, "0")` → **0005**.

Sandbox: `code_sandbox/js-string-reference/padStart.html`

```javascript
let text = "5";
text.padStart(4, "0");
text.padStart(4, "x");
```

![js-string-reference example 18 source](../code_sandbox/snaps/js-string-reference-18-code.png)

![js-string-reference example 18 result](../code_sandbox/snaps/js-string-reference-18-result.png)

- [x] **Outcome:** **0005** and **xxx5**.

<a id="js-string-reference-example-19"></a>

### **Example 19: `prototype`**

- [x] **`String.prototype`** is how you add methods that every string can use.
- [x] Do this only for demos or shared libraries — extra prototype methods surprise other code.

Sandbox: `code_sandbox/js-string-reference/prototype.html`

```javascript
String.prototype.exclaim = function () {
  return this + "!";
};
"Hi".exclaim();
```

![js-string-reference example 19 source](../code_sandbox/snaps/js-string-reference-19-code.png)

![js-string-reference example 19 result](../code_sandbox/snaps/js-string-reference-19-result.png)

- [x] **Outcome:** `"Hi".exclaim()` returns **Hi!**.

<a id="js-string-reference-example-20"></a>

### **Example 20: `repeat()`**

- [x] **`repeat(count)`** returns a **new** string with that many copies.
- [x] Does not change the original. `count` must be a non-negative integer.

Sandbox: `code_sandbox/js-string-reference/repeat.html`

```javascript
let text = "Ha";
text.repeat(3);
```

![js-string-reference example 20 source](../code_sandbox/snaps/js-string-reference-20-code.png)

![js-string-reference example 20 result](../code_sandbox/snaps/js-string-reference-20-result.png)

- [x] **Outcome:** **HaHa** and **HaHaHaHa**. The original `Ha` is unchanged.

<a id="js-string-reference-example-21"></a>

### **Example 21: `replace()`**

- [x] Replaces the **first** match only (unless you use a regex with **`/g`**).
- [x] Case-sensitive by default; use **`/i`** to ignore case.

Sandbox: `code_sandbox/js-string-reference/replace.html`

```javascript
let text = "Please visit Microsoft and Microsoft!";
text.replace("Microsoft", "W3Schools");
```

![js-string-reference example 21 source](../code_sandbox/snaps/js-string-reference-21-code.png)

![js-string-reference example 21 result](../code_sandbox/snaps/js-string-reference-21-result.png)

- [x] **Outcome:** Without `/g` only the **first** Microsoft changes; with `/g` **both** change.

<a id="js-string-reference-example-22"></a>

### **Example 22: `replaceAll()`**

- [x] Replaces **every** match (ES2021).
- [x] If the search is a regex, it **must** include **`g`** or you get a **TypeError**.

Sandbox: `code_sandbox/js-string-reference/replaceAll.html`

```javascript
let text = "I love Cats. Cats are great.";
text.replaceAll("Cats", "Dogs");
```

![js-string-reference example 22 source](../code_sandbox/snaps/js-string-reference-22-code.png)

![js-string-reference example 22 result](../code_sandbox/snaps/js-string-reference-22-result.png)

- [x] **Outcome:** Both **Cats** become **Dogs**: **I love Dogs. Dogs are great.**

<a id="js-string-reference-example-23"></a>

### **Example 23: `search()`**

- [x] Returns the **index** of a match (string or **regex**), or **`-1`**.
- [x] **Not** the same as `indexOf`: `search` has **no** start-index argument; `indexOf` cannot take a regex.

Sandbox: `code_sandbox/js-string-reference/search.html`

```javascript
let text = "Please locate where 'locate' occurs!";
text.search("locate");
text.search(/locate/);
```

![js-string-reference example 23 source](../code_sandbox/snaps/js-string-reference-23-code.png)

![js-string-reference example 23 result](../code_sandbox/snaps/js-string-reference-23-result.png)

- [x] **Outcome:** Both forms return **7** for this string.

<a id="js-string-reference-example-24"></a>

### **Example 24: `slice()`**

- [x] **`slice(start, end)`** copies a section; **end is not included**.
- [x] **Negative** indexes count from the end. Omit `end` to take the rest.

Sandbox: `code_sandbox/js-string-reference/slice.html`

```javascript
let text = "Apple, Banana, Kiwi";
text.slice(7, 13);
text.slice(7);
text.slice(-12, -6);
```

![js-string-reference example 24 source](../code_sandbox/snaps/js-string-reference-24-code.png)

![js-string-reference example 24 result](../code_sandbox/snaps/js-string-reference-24-result.png)

- [x] **Outcome:** `slice(7, 13)` is **Banana**; `slice(7)` is **Banana, Kiwi**; `slice(-12, -6)` is **Banana**.

<a id="js-string-reference-example-25"></a>

### **Example 25: `split()`**

- [x] Turns a string into an **array** of pieces.
- [x] `split("")` splits on every UTF-16 unit and is **unsafe for emoji**. Prefer **`Intl.Segmenter`** for graphemes.

Sandbox: `code_sandbox/js-string-reference/split.html`

```javascript
let text = "The quick brown fox.";
text.split(" ");
```

![js-string-reference example 25 source](../code_sandbox/snaps/js-string-reference-25-code.png)

![js-string-reference example 25 result](../code_sandbox/snaps/js-string-reference-25-result.png)

- [x] **Outcome:** `split(" ")` is **["The","quick","brown","fox."]**; `split("")` on `"Hi"` is **["H","i"]**.

<a id="js-string-reference-example-26"></a>

### **Example 26: `startsWith()`**

- [x] Returns **`true`** if the string **begins** with the given text.
- [x] Case-sensitive. Optional start index shifts where “the beginning” is.

Sandbox: `code_sandbox/js-string-reference/startsWith.html`

```javascript
let text = "Hello world, welcome to the universe.";
text.startsWith("Hello");
text.startsWith("world");
```

![js-string-reference example 26 source](../code_sandbox/snaps/js-string-reference-26-code.png)

![js-string-reference example 26 result](../code_sandbox/snaps/js-string-reference-26-result.png)

- [x] **Outcome:** **true** for "Hello"; **false** for "world" unless you start at index **6**.

<a id="js-string-reference-example-27"></a>

### **Example 27: `substr()` (deprecated)**

- [x] **Deprecated.** The second argument is a **length**, not an end index.
- [x] Still works for compatibility. **Use `substring()` or `slice()`** in new code.

Sandbox: `code_sandbox/js-string-reference/substr.html`

```javascript
let str = "Apple, Banana, Kiwi";
str.substr(7, 6);
str.substr(7);
str.substr(-4);
```

![js-string-reference example 27 source](../code_sandbox/snaps/js-string-reference-27-code.png)

![js-string-reference example 27 result](../code_sandbox/snaps/js-string-reference-27-result.png)

- [x] **Outcome:** `substr(7, 6)` is **Banana**; from 7 to the end is **Banana, Kiwi**; `-4` is **Kiwi**. Prefer **slice/substring**.

<a id="js-string-reference-example-28"></a>

### **Example 28: `substring()`**

- [x] Like `slice()`, but **negative start/end become 0** (they do not count from the end).
- [x] If start > end, `substring` **swaps** them; `slice` returns empty.

Sandbox: `code_sandbox/js-string-reference/substring.html`

```javascript
let str = "Apple, Banana, Kiwi";
str.substring(7, 13);
```

![js-string-reference example 28 source](../code_sandbox/snaps/js-string-reference-28-code.png)

![js-string-reference example 28 result](../code_sandbox/snaps/js-string-reference-28-result.png)

- [x] **Outcome:** `substring(7, 13)` is **Banana**. Negatives are treated as **0**, so you get the start of the string.

<a id="js-string-reference-example-29"></a>

### **Example 29: `toLocaleLowerCase()`**

- [x] Lowercases using the **host locale** (important for languages like Turkish `I` → `ı`).
- [x] For English text it matches `toLowerCase()`.

Sandbox: `code_sandbox/js-string-reference/toLocaleLowerCase.html`

```javascript
let text = "Hello WORLD!";
text.toLocaleLowerCase();
```

![js-string-reference example 29 source](../code_sandbox/snaps/js-string-reference-29-code.png)

![js-string-reference example 29 result](../code_sandbox/snaps/js-string-reference-29-result.png)

- [x] **Outcome:** The result is **hello world!**.

<a id="js-string-reference-example-30"></a>

### **Example 30: `toLocaleUpperCase()`**

- [x] Uppercases using the **host locale**.
- [x] Same idea as `toLocaleLowerCase()`, but toward capitals.

Sandbox: `code_sandbox/js-string-reference/toLocaleUpperCase.html`

```javascript
let text = "Hello World!";
text.toLocaleUpperCase();
```

![js-string-reference example 30 source](../code_sandbox/snaps/js-string-reference-30-code.png)

![js-string-reference example 30 result](../code_sandbox/snaps/js-string-reference-30-result.png)

- [x] **Outcome:** The result is **HELLO WORLD!**.

<a id="js-string-reference-example-31"></a>

### **Example 31: `toLowerCase()`**

- [x] Returns a **new** string with all letters in lower case.
- [x] The original string is unchanged.

Sandbox: `code_sandbox/js-string-reference/toLowerCase.html`

```javascript
let text1 = "Hello World!";
let text2 = text1.toLowerCase();
```

![js-string-reference example 31 source](../code_sandbox/snaps/js-string-reference-31-code.png)

![js-string-reference example 31 result](../code_sandbox/snaps/js-string-reference-31-result.png)

- [x] **Outcome:** The new string is **hello world!**; **Hello World!** is still the original.

<a id="js-string-reference-example-32"></a>

### **Example 32: `toString()`**

- [x] Returns the string **primitive**. Useful on a `new String('Hello')` object.
- [x] On a normal string literal it just returns the same text.

Sandbox: `code_sandbox/js-string-reference/toString.html`

```javascript
let obj = new String("Hello");
obj.toString();
```

![js-string-reference example 32 source](../code_sandbox/snaps/js-string-reference-32-code.png)

![js-string-reference example 32 result](../code_sandbox/snaps/js-string-reference-32-result.png)

- [x] **Outcome:** The object’s `toString()` is the primitive **Hello** (`typeof` **string**).

<a id="js-string-reference-example-33"></a>

### **Example 33: `toUpperCase()`**

- [x] Returns a **new** string with all letters in upper case.

Sandbox: `code_sandbox/js-string-reference/toUpperCase.html`

```javascript
let text1 = "Hello World!";
let text2 = text1.toUpperCase();
```

![js-string-reference example 33 source](../code_sandbox/snaps/js-string-reference-33-code.png)

![js-string-reference example 33 result](../code_sandbox/snaps/js-string-reference-33-result.png)

- [x] **Outcome:** The result is **HELLO WORLD!**.

<a id="js-string-reference-example-34"></a>

### **Example 34: `toWellFormed()`**

- [x] Returns a new string where **lone surrogates** are replaced with **U+FFFD** (`�`).
- [x] Use with `isWellFormed()` when you need to sanitize broken UTF-16.

Sandbox: `code_sandbox/js-string-reference/toWellFormed.html`

```javascript
let text = "Hello World \uD800";
text.toWellFormed();
```

![js-string-reference example 34 source](../code_sandbox/snaps/js-string-reference-34-code.png)

![js-string-reference example 34 result](../code_sandbox/snaps/js-string-reference-34-result.png)

- [x] **Outcome:** The original is **not** well formed; `toWellFormed()` replaces the lone surrogate with **�**.

<a id="js-string-reference-example-35"></a>

### **Example 35: `trim()`**

- [x] Removes **whitespace from both ends**. Does not change the original.
- [x] Spaces in the **middle** stay.

Sandbox: `code_sandbox/js-string-reference/trim.html`

```javascript
let original = " Hello ";
let trimmed = original.trim();
```

![js-string-reference example 35 source](../code_sandbox/snaps/js-string-reference-35-code.png)

![js-string-reference example 35 result](../code_sandbox/snaps/js-string-reference-35-result.png)

- [x] **Outcome:** The original still has spaces (`' Hello '`); `trim()` returns **`'Hello'`**.

<a id="js-string-reference-example-36"></a>

### **Example 36: `trimEnd()`**

- [x] Removes whitespace from the **end only** (ES2019). Alias: `trimRight()`.

Sandbox: `code_sandbox/js-string-reference/trimEnd.html`

```javascript
let text1 = " Hello World! ";
let text2 = text1.trimEnd();
```

![js-string-reference example 36 source](../code_sandbox/snaps/js-string-reference-36-code.png)

![js-string-reference example 36 result](../code_sandbox/snaps/js-string-reference-36-result.png)

- [x] **Outcome:** Leading space remains; the trailing space is gone: **`' Hello World!'`**.

<a id="js-string-reference-example-37"></a>

### **Example 37: `trimStart()`**

- [x] Removes whitespace from the **start only** (ES2019). Alias: `trimLeft()`.

Sandbox: `code_sandbox/js-string-reference/trimStart.html`

```javascript
let text1 = " Hello World! ";
let text2 = text1.trimStart();
```

![js-string-reference example 37 source](../code_sandbox/snaps/js-string-reference-37-code.png)

![js-string-reference example 37 result](../code_sandbox/snaps/js-string-reference-37-result.png)

- [x] **Outcome:** Trailing space remains; the leading space is gone: **`'Hello World! '`**.

<a id="js-string-reference-example-38"></a>

### **Example 38: `valueOf()`**

- [x] Returns the **primitive** string value (same idea as `toString()` for String objects).
- [x] JavaScript calls this automatically in most string operations.

Sandbox: `code_sandbox/js-string-reference/valueOf.html`

```javascript
let obj = new String("Hello");
obj.valueOf();
```

![js-string-reference example 38 source](../code_sandbox/snaps/js-string-reference-38-code.png)

![js-string-reference example 38 result](../code_sandbox/snaps/js-string-reference-38-result.png)

- [x] **Outcome:** `valueOf()` is the primitive **Hello** (`typeof` **string**), while `obj` itself is an **object**.

<a id="js-string-reference-example-39"></a>

### **Example 39: HTML wrapper methods (deprecated — do not use)**

- [x] These methods wrap the string in an **HTML tag** (`bold()` → `<b>…</b>`).
- [x] **Deprecated.** Not for new code. Style with **CSS** and create elements with the **DOM**.
- [x] They exist only for old-page compatibility. The sandbox still **runs every wrapper** so you can recognize them.

Sandbox: `code_sandbox/js-string-reference/html-wrappers.html`

```javascript
let t = "Hi";
t.bold();
t.italics();
t.link("https://example.com");
// also: anchor, big, blink, fixed, fontcolor, fontsize, small, strike, sub, sup
```

![js-string-reference example 39 source](../code_sandbox/snaps/js-string-reference-39-code.png)

![js-string-reference example 39 result](../code_sandbox/snaps/js-string-reference-39-result.png)

- [x] **Outcome:** Each call returns a **string of HTML** (for example `bold()` → `<b>Hi</b>`). Do **not** use these; use CSS/DOM instead.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-string-reference/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Do string methods change the original string?

<details>
<summary>Answer</summary>

- [x] **No.** They return a **new** value.
- [x] Assign the result if you want to keep it.

</details>

### Question 2: What does `at(-1)` return?

<details>
<summary>Answer</summary>

- [x] The **last** character.
- [x] `charAt()` cannot take a negative index.

</details>

### Question 3: What does `charAt(99)` return on a short string?

<details>
<summary>Answer</summary>

- [x] An **empty string** `""`.
- [x] `text[99]` would be **`undefined`** instead.

</details>

### Question 4: Is `length` a method?

<details>
<summary>Answer</summary>

- [x] **No.** It is a **property** — `text.length`, not `text.length()`.

</details>

### Question 5: What does `indexOf` return when the text is missing?

<details>
<summary>Answer</summary>

- [x] **`-1`.**

</details>

### Question 6: How do `indexOf` and `search` differ?

<details>
<summary>Answer</summary>

- [x] **`search`** can take a **regex** but **not** a start index.
- [x] **`indexOf`** can take a start index but **not** a regex.

</details>

### Question 7: Does `replace` change every match?

<details>
<summary>Answer</summary>

- [x] **No.** Only the **first**, unless you use a regex with **`/g`** or call **`replaceAll()`**.

</details>

### Question 8: What should you use instead of `substr()`?

<details>
<summary>Answer</summary>

- [x] **`substring()`** or **`slice()`**.
- [x] `substr()` is **deprecated**.

</details>

### Question 9: Should you use `bold()` / `italics()`?

<details>
<summary>Answer</summary>

- [x] **No.** HTML wrappers are **deprecated**.
- [x] Use **CSS** and the **DOM**.

</details>

### Question 10: What does `isWellFormed()` check?

<details>
<summary>Answer</summary>

- [x] Whether the string has **lone surrogates** (broken UTF-16).
- [x] Fix them with **`toWellFormed()`**, which inserts **�**.

</details>

### Question 11: What does `"5".padStart(4, "0")` return?

<details>
<summary>Answer</summary>

- [x] **0005**.
- [x] Pad a **string**; convert numbers with **`toString()`** first.

</details>

### Question 12: Why is `split("")` unsafe for emoji?

<details>
<summary>Answer</summary>

- [x] It splits **UTF-16 code units** and can break surrogate pairs.
- [x] Use **`Intl.Segmenter`** for graphemes.

</details>

### Question 13: What does `String.fromCharCode(72, 69, 76, 76, 79)` return?

<details>
<summary>Answer</summary>

- [x] **HELLO**.
- [x] It is a **static** method on `String`, not on a string value.

</details>

### Question 14: What does `match(/ain/gi)` find in the rain sentence?

<details>
<summary>Answer</summary>

- [x] **ain, AIN, ain, ain** — all matches, case-insensitive.

</details>

### Question 15: What do `toString()` and `valueOf()` do on `new String("Hello")`?

<details>
<summary>Answer</summary>

- [x] They return the primitive **"Hello"**.
- [x] `typeof` of the object is **object**; `typeof` of the return is **string**.

</details>

</details>

## Summary

Every String property and method has its own Example. Methods return new values. Skip **`substr`** and the **HTML wrappers**; style with CSS and the DOM. `at()` supports negatives, `length` is a property, `indexOf` returns `-1` when missing, `replace` changes the first match, `replaceAll` changes every match, and `split("")` is unsafe on emoji.

## References

- [JS String Reference (W3Schools)](https://www.w3schools.com/js/js_string_reference.asp)
- [MDN: String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
- [MDN: String.prototype.at()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/at)
- [MDN: String.prototype.slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
- [MDN: String.prototype.replaceAll()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
- [W3Schools JavaScript Reference](https://www.w3schools.com/jsref/default.asp)
