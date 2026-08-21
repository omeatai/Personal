# JS String Search

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Search methods find text **inside** a string: **position** (`indexOf`, `lastIndexOf`, `search`), **matches** (`match`, `matchAll`), or **true/false** (`includes`, `startsWith`, `endsWith`). Positions start at **0**. Missing text is **`-1`**. Each Tryit is its own Example.

This section has **22** examples:

- [x] **Example 1:** `indexOf("locate")` [View](#js-string-search-example-01)
- [x] **Example 2:** `lastIndexOf("locate")` [View](#js-string-search-example-02)
- [x] **Example 3:** `lastIndexOf("John")` is -1 [View](#js-string-search-example-03)
- [x] **Example 4:** `indexOf("locate", 15)` [View](#js-string-search-example-04)
- [x] **Example 5:** `lastIndexOf("locate", 15)` [View](#js-string-search-example-05)
- [x] **Example 6:** `search("locate")` [View](#js-string-search-example-06)
- [x] **Example 7:** `search(/locate/)` [View](#js-string-search-example-07)
- [x] **Example 8:** `match("ain")` [View](#js-string-search-example-08)
- [x] **Example 9:** `match(/ain/)` [View](#js-string-search-example-09)
- [x] **Example 10:** `match(/ain/g)` [View](#js-string-search-example-10)
- [x] **Example 11:** `match(/ain/gi)` [View](#js-string-search-example-11)
- [x] **Example 12:** `matchAll("Cats")` [View](#js-string-search-example-12)
- [x] **Example 13:** `matchAll(/Cats/g)` [View](#js-string-search-example-13)
- [x] **Example 14:** `matchAll(/Cats/gi)` [View](#js-string-search-example-14)
- [x] **Example 15:** `includes("world")` [View](#js-string-search-example-15)
- [x] **Example 16:** `includes("world", 12)` [View](#js-string-search-example-16)
- [x] **Example 17:** `startsWith("Hello")` [View](#js-string-search-example-17)
- [x] **Example 18:** `startsWith("world")` [View](#js-string-search-example-18)
- [x] **Example 19:** `startsWith("world", 5)` [View](#js-string-search-example-19)
- [x] **Example 20:** `startsWith("world", 6)` [View](#js-string-search-example-20)
- [x] **Example 21:** `endsWith("Doe")` [View](#js-string-search-example-21)
- [x] **Example 22:** `endsWith("world", 11)` [View](#js-string-search-example-22)

## Detailed Explanation

- [x] **`indexOf` / `lastIndexOf`** — first vs last occurrence; **`-1`** if missing. Optional start index; `lastIndexOf` searches **backward**.
- [x] **`search`** — string or **regex**; no start-index argument. `indexOf` cannot take a regex.
- [x] **`match` / `matchAll`** — `match` returns an array (`/g` for all; `/gi` also ignores case). `matchAll` returns an iterator and needs **`g`** on a regex.
- [x] **Booleans (ES6)** — `includes`, `startsWith`, `endsWith` are case-sensitive; optional start (or length for `endsWith`).

<a id="js-string-search-example-01"></a>

### **Example 1: `indexOf("locate")`**

- [x] **`indexOf(search)`** returns the **first** index, or **`-1`** if missing.
- [x] Positions start at **0**.

Sandbox: `code_sandbox/js-string-search/indexOf.html`

```javascript
let text = "Please locate where 'locate' occurs!";
let index = text.indexOf("locate");
```

![js-string-search example 1 source](../code_sandbox/snaps/js-string-search-01-code.png)

![js-string-search example 1 result](../code_sandbox/snaps/js-string-search-01-result.png)

- [x] **Outcome:** First **locate** is at index **7**.

<a id="js-string-search-example-02"></a>

### **Example 2: `lastIndexOf("locate")`**

- [x] **`lastIndexOf`** returns the **last** occurrence, or **`-1`**.

Sandbox: `code_sandbox/js-string-search/lastIndexOf.html`

```javascript
let text = "Please locate where 'locate' occurs!";
let index = text.lastIndexOf("locate");
```

![js-string-search example 2 source](../code_sandbox/snaps/js-string-search-02-code.png)

![js-string-search example 2 result](../code_sandbox/snaps/js-string-search-02-result.png)

- [x] **Outcome:** Last **locate** is at index **21**.

<a id="js-string-search-example-03"></a>

### **Example 3: `lastIndexOf("John")` is -1**

- [x] Both `indexOf` and `lastIndexOf` return **`-1`** when the text is not found.

Sandbox: `code_sandbox/js-string-search/lastIndexOf-missing.html`

```javascript
let text = "Please locate where 'locate' occurs!";
let index = text.lastIndexOf("John");
```

![js-string-search example 3 source](../code_sandbox/snaps/js-string-search-03-code.png)

![js-string-search example 3 result](../code_sandbox/snaps/js-string-search-03-result.png)

- [x] **Outcome:** **John** is missing, so the result is **-1**.

<a id="js-string-search-example-04"></a>

### **Example 4: `indexOf("locate", 15)`**

- [x] The optional second argument is the **start index** (search forward from there).

Sandbox: `code_sandbox/js-string-search/indexOf-start.html`

```javascript
let text = "Please locate where 'locate' occurs!";
let index = text.indexOf("locate", 15);
```

![js-string-search example 4 source](../code_sandbox/snaps/js-string-search-04-code.png)

![js-string-search example 4 result](../code_sandbox/snaps/js-string-search-04-result.png)

- [x] **Outcome:** From index 15 the next **locate** is at **21**.

<a id="js-string-search-example-05"></a>

### **Example 5: `lastIndexOf("locate", 15)`**

- [x] `lastIndexOf` with a start index searches **backward** from that position.
- [x] Start at 15 and walk toward the beginning — you hit the first **locate**.

Sandbox: `code_sandbox/js-string-search/lastIndexOf-start.html`

```javascript
let text = "Please locate where 'locate' occurs!";
text.lastIndexOf("locate", 15);
```

![js-string-search example 5 source](../code_sandbox/snaps/js-string-search-05-code.png)

![js-string-search example 5 result](../code_sandbox/snaps/js-string-search-05-result.png)

- [x] **Outcome:** Searching backward from 15 finds **7**.

<a id="js-string-search-example-06"></a>

### **Example 6: `search("locate")`**

- [x] **`search()`** returns the **position** of a match (string or regex), or **`-1`**.

Sandbox: `code_sandbox/js-string-search/search-string.html`

```javascript
let text = "Please locate where 'locate' occurs!";
text.search("locate");
```

![js-string-search example 6 source](../code_sandbox/snaps/js-string-search-06-code.png)

![js-string-search example 6 result](../code_sandbox/snaps/js-string-search-06-result.png)

- [x] **Outcome:** `search("locate")` returns **7**.

<a id="js-string-search-example-07"></a>

### **Example 7: `search(/locate/)`**

- [x] `search` can take a **regular expression**; `indexOf` cannot.
- [x] `search` has **no** start-index argument; `indexOf` does.

Sandbox: `code_sandbox/js-string-search/search-regex.html`

```javascript
let text = "Please locate where 'locate' occurs!";
text.search(/locate/);
```

![js-string-search example 7 source](../code_sandbox/snaps/js-string-search-07-code.png)

![js-string-search example 7 result](../code_sandbox/snaps/js-string-search-07-result.png)

- [x] **Outcome:** `search(/locate/)` also returns **7**.

<a id="js-string-search-example-08"></a>

### **Example 8: `match("ain")`**

- [x] `match` returns an **array** of match info (or `null`).
- [x] A plain string search finds the **first** **ain** (inside **rain**).

Sandbox: `code_sandbox/js-string-search/match-string.html`

```javascript
let text = "The rain in SPAIN stays mainly in the plain";
text.match("ain");
```

![js-string-search example 8 source](../code_sandbox/snaps/js-string-search-08-code.png)

![js-string-search example 8 result](../code_sandbox/snaps/js-string-search-08-result.png)

- [x] **Outcome:** The first **ain** is at index **5** (in **rain**).

<a id="js-string-search-example-09"></a>

### **Example 9: `match(/ain/)`**

- [x] A regex **without `/g`** also returns details of the **first** match only.

Sandbox: `code_sandbox/js-string-search/match-regex.html`

```javascript
let text = "The rain in SPAIN stays mainly in the plain";
text.match(/ain/);
```

![js-string-search example 9 source](../code_sandbox/snaps/js-string-search-09-code.png)

![js-string-search example 9 result](../code_sandbox/snaps/js-string-search-09-result.png)

- [x] **Outcome:** First regex match is still **ain** at index **5**.

<a id="js-string-search-example-10"></a>

### **Example 10: `match(/ain/g)`**

- [x] **`/g`** (global) returns **all** matches as a simple array of strings.
- [x] Without `/i`, **AIN** in SPAIN is **not** included.

Sandbox: `code_sandbox/js-string-search/match-g.html`

```javascript
let text = "The rain in SPAIN stays mainly in the plain";
text.match(/ain/g);
```

![js-string-search example 10 source](../code_sandbox/snaps/js-string-search-10-code.png)

![js-string-search example 10 result](../code_sandbox/snaps/js-string-search-10-result.png)

- [x] **Outcome:** The matches are **ain,ain,ain** (rain, mainly, plain).

<a id="js-string-search-example-11"></a>

### **Example 11: `match(/ain/gi)`**

- [x] **`/gi`** is global **and** case-insensitive, so **AIN** in SPAIN is included.

Sandbox: `code_sandbox/js-string-search/match-gi.html`

```javascript
let text = "The rain in SPAIN stays mainly in the plain";
text.match(/ain/gi);
```

![js-string-search example 11 source](../code_sandbox/snaps/js-string-search-11-code.png)

![js-string-search example 11 result](../code_sandbox/snaps/js-string-search-11-result.png)

- [x] **Outcome:** The matches are **ain,AIN,ain,ain**.

<a id="js-string-search-example-12"></a>

### **Example 12: `matchAll("Cats")`**

- [x] **`matchAll()`** (ES2020) returns an **iterator** of all matches.
- [x] Turn it into an array with **`Array.from`**.

Sandbox: `code_sandbox/js-string-search/matchAll-string.html`

```javascript
let text = "I love cats. Cats are very easy to love. Cats are very popular.";
const iterator = text.matchAll("Cats");
```

![js-string-search example 12 source](../code_sandbox/snaps/js-string-search-12-code.png)

![js-string-search example 12 result](../code_sandbox/snaps/js-string-search-12-result.png)

- [x] **Outcome:** The iterator yields **Cats, Cats** (two capitalized matches).

<a id="js-string-search-example-13"></a>

### **Example 13: `matchAll(/Cats/g)`**

- [x] If the argument is a regex, it **must** have the **`g`** flag or you get a **TypeError**.

Sandbox: `code_sandbox/js-string-search/matchAll-g.html`

```javascript
let text = "I love cats. Cats are very easy to love. Cats are very popular.";
const iterator = text.matchAll(/Cats/g);
```

![js-string-search example 13 source](../code_sandbox/snaps/js-string-search-13-code.png)

![js-string-search example 13 result](../code_sandbox/snaps/js-string-search-13-result.png)

- [x] **Outcome:** The iterator yields **Cats, Cats**.

<a id="js-string-search-example-14"></a>

### **Example 14: `matchAll(/Cats/gi)`**

- [x] Add **`i`** to match **cats** as well as **Cats**.

Sandbox: `code_sandbox/js-string-search/matchAll-gi.html`

```javascript
let text = "I love cats. Cats are very easy to love. Cats are very popular.";
const iterator = text.matchAll(/Cats/gi);
```

![js-string-search example 14 source](../code_sandbox/snaps/js-string-search-14-code.png)

![js-string-search example 14 result](../code_sandbox/snaps/js-string-search-14-result.png)

- [x] **Outcome:** The iterator yields **cats, Cats, Cats** (three matches).

<a id="js-string-search-example-15"></a>

### **Example 15: `includes("world")`**

- [x] **`includes`** returns **`true`** if the substring exists anywhere.
- [x] Case-sensitive ES6 method.

Sandbox: `code_sandbox/js-string-search/includes.html`

```javascript
let text = "Hello world, welcome to the universe.";
text.includes("world");
```

![js-string-search example 15 source](../code_sandbox/snaps/js-string-search-15-code.png)

![js-string-search example 15 result](../code_sandbox/snaps/js-string-search-15-result.png)

- [x] **Outcome:** **true** — **world** is in the string.

<a id="js-string-search-example-16"></a>

### **Example 16: `includes("world", 12)`**

- [x] The optional second argument is the **start index**.
- [x] **world** ends before index 12, so the search misses it.

Sandbox: `code_sandbox/js-string-search/includes-start.html`

```javascript
let text = "Hello world, welcome to the universe.";
text.includes("world", 12);
```

![js-string-search example 16 source](../code_sandbox/snaps/js-string-search-16-code.png)

![js-string-search example 16 result](../code_sandbox/snaps/js-string-search-16-result.png)

- [x] **Outcome:** **false** — the search starts past **world**.

<a id="js-string-search-example-17"></a>

### **Example 17: `startsWith("Hello")`**

- [x] **`startsWith`** is **true** if the string **begins** with that text.
- [x] Case-sensitive ES6 method.

Sandbox: `code_sandbox/js-string-search/startsWith-hello.html`

```javascript
let text = "Hello world, welcome to the universe.";
text.startsWith("Hello");
```

![js-string-search example 17 source](../code_sandbox/snaps/js-string-search-17-code.png)

![js-string-search example 17 result](../code_sandbox/snaps/js-string-search-17-result.png)

- [x] **Outcome:** **true**.

<a id="js-string-search-example-18"></a>

### **Example 18: `startsWith("world")`**

- [x] The string begins with **Hello**, not **world**.

Sandbox: `code_sandbox/js-string-search/startsWith-world.html`

```javascript
let text = "Hello world, welcome to the universe.";
text.startsWith("world");
```

![js-string-search example 18 source](../code_sandbox/snaps/js-string-search-18-code.png)

![js-string-search example 18 result](../code_sandbox/snaps/js-string-search-18-result.png)

- [x] **Outcome:** **false**.

<a id="js-string-search-example-19"></a>

### **Example 19: `startsWith("world", 5)`**

- [x] The optional start index shifts where “the beginning” is.
- [x] Index **5** is the **space** before **world**, so this is still false.

Sandbox: `code_sandbox/js-string-search/startsWith-world-5.html`

```javascript
let text = "Hello world, welcome to the universe.";
text.startsWith("world", 5);
```

![js-string-search example 19 source](../code_sandbox/snaps/js-string-search-19-code.png)

![js-string-search example 19 result](../code_sandbox/snaps/js-string-search-19-result.png)

- [x] **Outcome:** **false** — index 5 is a space, not **w**.

<a id="js-string-search-example-20"></a>

### **Example 20: `startsWith("world", 6)`**

- [x] Index **6** is the **w** of **world**, so the check succeeds.

Sandbox: `code_sandbox/js-string-search/startsWith-world-6.html`

```javascript
let text = "Hello world, welcome to the universe.";
text.startsWith("world", 6);
```

![js-string-search example 20 source](../code_sandbox/snaps/js-string-search-20-code.png)

![js-string-search example 20 result](../code_sandbox/snaps/js-string-search-20-result.png)

- [x] **Outcome:** **true**.

<a id="js-string-search-example-21"></a>

### **Example 21: `endsWith("Doe")`**

- [x] **`endsWith`** is **true** if the string **ends** with that text.

Sandbox: `code_sandbox/js-string-search/endsWith-doe.html`

```javascript
let text = "John Doe";
text.endsWith("Doe");
```

![js-string-search example 21 source](../code_sandbox/snaps/js-string-search-21-code.png)

![js-string-search example 21 result](../code_sandbox/snaps/js-string-search-21-result.png)

- [x] **Outcome:** **true**.

<a id="js-string-search-example-22"></a>

### **Example 22: `endsWith("world", 11)`**

- [x] The optional second argument is a **length**: treat the string as if it were only that long.
- [x] The first **11** characters of `"Hello world, ..."` are `"Hello world"`, which ends with **world**.

Sandbox: `code_sandbox/js-string-search/endsWith-world-11.html`

```javascript
let text = "Hello world, welcome to the universe.";
text.endsWith("world", 11);
```

![js-string-search example 22 source](../code_sandbox/snaps/js-string-search-22-code.png)

![js-string-search example 22 result](../code_sandbox/snaps/js-string-search-22-result.png)

- [x] **Outcome:** **true** — the 11-character prefix ends with **world**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-string-search/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `indexOf("locate")` return on the Please locate string?

<details>
<summary>Answer</summary>

- [x] **7** — the first **locate**.

</details>

### Question 2: What does `lastIndexOf("locate")` return on that string?

<details>
<summary>Answer</summary>

- [x] **21** — the last **locate**.

</details>

### Question 3: What does `lastIndexOf("John")` return?

<details>
<summary>Answer</summary>

- [x] **-1** — the text is missing.

</details>

### Question 4: What does `indexOf("locate", 15)` return?

<details>
<summary>Answer</summary>

- [x] **21** — search forward from index 15.

</details>

### Question 5: What does `lastIndexOf("locate", 15)` return?

<details>
<summary>Answer</summary>

- [x] **7** — search **backward** from 15.

</details>

### Question 6: How do `indexOf` and `search` differ?

<details>
<summary>Answer</summary>

- [x] **`search`** can take a **regex** but **not** a start index.
- [x] **`indexOf`** can take a start index but **not** a regex.
- [x] Both return **7** for `"locate"` here.

</details>

### Question 7: What does `match(/ain/g)` find in the rain sentence?

<details>
<summary>Answer</summary>

- [x] **ain,ain,ain** — rain, mainly, plain.
- [x] **AIN** is skipped without `/i`.

</details>

### Question 8: What does `match(/ain/gi)` find?

<details>
<summary>Answer</summary>

- [x] **ain,AIN,ain,ain**.

</details>

### Question 9: What does `matchAll(/Cats/gi)` yield on the cats sentence?

<details>
<summary>Answer</summary>

- [x] **cats, Cats, Cats** (three matches).
- [x] `matchAll("Cats")` without `/i` yields only **Cats, Cats**.

</details>

### Question 10: What does `includes("world")` return? From index 12?

<details>
<summary>Answer</summary>

- [x] **true** from the start.
- [x] **false** if you start at **12** (past **world**).

</details>

### Question 11: When is `startsWith("world")` true on the Hello world string?

<details>
<summary>Answer</summary>

- [x] **false** from the start or from index **5** (a space).
- [x] **true** from index **6**.

</details>

### Question 12: What does `endsWith("Doe")` return for `"John Doe"`?

<details>
<summary>Answer</summary>

- [x] **true.**

</details>

### Question 13: What does `endsWith("world", 11)` return?

<details>
<summary>Answer</summary>

- [x] **true** — the first 11 characters are **Hello world**.

</details>

</details>

## Summary

Use **`indexOf` / `lastIndexOf` / `search`** for positions (`locate` at **7** / **21**, missing is **-1**), **`match` / `matchAll`** for match lists (`/ain/gi` → ain,AIN,ain,ain), and **`includes` / `startsWith` / `endsWith`** for booleans. `search` takes regex; `indexOf` takes a start index. `startsWith("world", 6)` is true; `endsWith("world", 11)` is true.

## References

- [JS String Search (W3Schools)](https://www.w3schools.com/js/js_string_search.asp)
- [MDN: String.prototype.indexOf()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf)
- [MDN: String.prototype.search()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search)
- [MDN: String.prototype.match()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
- [MDN: String.prototype.includes()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes)
