# JS RegExp Objects

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

RegExp is an object. test returns a boolean. exec returns a match array or null (not {}). You can write a literal /e/ or new RegExp("e"). Constructor strings eat backslashes, so \\d is required to get \d. lastIndex moves on each exec/test when g or y is set, and a failed match resets it to 0. RegExp.escape (ES2025) quotes syntax characters so a user string can be matched literally.

This section has **7** examples:

- [x] **Example 1:** pattern.test(text) [View](#js-regexp-objects-example-01)
- [x] **Example 2:** /e/.test(text) — no variable [View](#js-regexp-objects-example-02)
- [x] **Example 3:** regex.exec(text) [View](#js-regexp-objects-example-03)
- [x] **Example 4:** exec — no match is null [View](#js-regexp-objects-example-04)
- [x] **Example 5:** Literal /ab+c/i vs new RegExp [View](#js-regexp-objects-example-05)
- [x] **Example 6:** lastIndex mutation with /g and exec [View](#js-regexp-objects-example-06)
- [x] **Example 7:** RegExp.escape('[*]') then replace [View](#js-regexp-objects-example-07)

## Detailed Explanation

- [x] **`test`** → boolean. **`exec`** → array or **`null`**.
- [x] Literal **`/pattern/flags`** vs **`new RegExp(string, flags)`** (double backslashes).
- [x] With **`/g`**, **`exec`/`test` mutate `lastIndex`**. **null** resets it to **0**.
- [x] **`RegExp.escape`** (ES2025) makes `[*]` a literal pattern. Node 22 may not have it; Chromium 136+ does.

<a id="js-regexp-objects-example-01"></a>

### **Example 1: pattern.test(text)**

- [x] `RegExp.test(string)` returns **true** or **false**.
- [x] The Tryit searches for **`e`** in the famous sentence.

Sandbox: `code_sandbox/js-regexp-objects/test.html`

```javascript
const pattern = /e/;
let result = pattern.test("The best things in life are free!");
```

![js-regexp-objects example 1 source](../code_sandbox/snaps/js-regexp-objects-01-code.png)

![js-regexp-objects example 1 result](../code_sandbox/snaps/js-regexp-objects-01-result.png)

- [x] **Outcome:** **true** — there is an `e` in `The`.

<a id="js-regexp-objects-example-02"></a>

### **Example 2: /e/.test(text) — no variable**

- [x] You can call **`test`** on a regex **literal**.

Sandbox: `code_sandbox/js-regexp-objects/test-oneliner.html`

```javascript
let result = /e/.test("The best things in life are free!");
```

![js-regexp-objects example 2 source](../code_sandbox/snaps/js-regexp-objects-02-code.png)

![js-regexp-objects example 2 result](../code_sandbox/snaps/js-regexp-objects-02-result.png)

- [x] **Outcome:** **true**.

<a id="js-regexp-objects-example-03"></a>

### **Example 3: regex.exec(text)**

- [x] `exec` returns a match **array** (or **null**). `[0]` is the match; **`index`** / **`input`** hang off the array.
- [x] `JSON.stringify` drops `index` and `input` — print them separately.

Sandbox: `code_sandbox/js-regexp-objects/exec.html`

```javascript
const result = /e/.exec("The best things in life are free!");
```

![js-regexp-objects example 3 source](../code_sandbox/snaps/js-regexp-objects-03-code.png)

![js-regexp-objects example 3 result](../code_sandbox/snaps/js-regexp-objects-03-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["e"]**. `result[0]` is **"e"**, `index` is **2**, `input` is the full sentence.

<a id="js-regexp-objects-example-04"></a>

### **Example 4: exec — no match is null**

- [x] The page says “empty (null) object”. In JS it is **`null`**, not `{}`.

Sandbox: `code_sandbox/js-regexp-objects/exec-null.html`

```javascript
let result = /z/.exec("The best things in life are free!");
```

![js-regexp-objects example 4 source](../code_sandbox/snaps/js-regexp-objects-04-code.png)

![js-regexp-objects example 4 result](../code_sandbox/snaps/js-regexp-objects-04-result.png)

- [x] **Outcome:** **null**.

<a id="js-regexp-objects-example-05"></a>

### **Example 5: Literal /ab+c/i vs new RegExp**

- [x] **`/pattern/flags`** is a regex literal. **`new RegExp(string, flags)`** is the constructor.
- [x] In a constructor **string**, backslashes are doubled: `new RegExp("\\d+")` not `"\d+"`.

Sandbox: `code_sandbox/js-regexp-objects/literal-vs-constructor.html`

```javascript
const lit = /ab+c/i;
const ctor = new RegExp("ab+c", "i");
const goodDigits = new RegExp("\\d+");
const badDigits = new RegExp("\d+");
```

![js-regexp-objects example 5 source](../code_sandbox/snaps/js-regexp-objects-05-code.png)

![js-regexp-objects example 5 result](../code_sandbox/snaps/js-regexp-objects-05-result.png)

- [x] **Outcome:** `lit` and `ctor` both print **`/ab+c/i`**. `goodDigits` is **`/\d+/`** and **`test("12")` is true**. `badDigits` is **`/d+/`** (the JS string `"\d+"` is just `d+`) so **`test("12")` is false**.

<a id="js-regexp-objects-example-06"></a>

### **Example 6: lastIndex mutation with /g and exec**

- [x] With **`/g`**, **`exec`** (and **`test`**) start at **`lastIndex`** and **write it back**.
- [x] A **null** match **resets `lastIndex` to 0**, so the next call starts over.

Sandbox: `code_sandbox/js-regexp-objects/lastIndex-g.html`

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

![js-regexp-objects example 6 source](../code_sandbox/snaps/js-regexp-objects-06-code.png)

![js-regexp-objects example 6 result](../code_sandbox/snaps/js-regexp-objects-06-result.png)

- [x] **Outcome:** First `exec` is **["is"]** at index **5** (`this`), `lastIndex` **7**. Second is **["is"]** at **18**, `lastIndex` **20**. Third is **null**, `lastIndex` **0**.

<a id="js-regexp-objects-example-07"></a>

### **Example 7: RegExp.escape('[*]') then replace**

- [x] **`RegExp.escape(text)`** (ES2025) backslash-escapes regex syntax so the text is **literal**.
- [x] Then `new RegExp(safe)` can match `[*]` as characters, not a character class.

Sandbox: `code_sandbox/js-regexp-objects/escape.html`

```javascript
const oldText = "[*] is a web school.";
let safe;
let result;
try {
  safe = RegExp.escape("[*]");
  const regex = new RegExp(safe);
  result = oldText.replace(regex, "W3Schools");
} catch (e) {
  safe = e.name + ": " + e.message;
  result = oldText;
}
```

![js-regexp-objects example 7 source](../code_sandbox/snaps/js-regexp-objects-07-code.png)

![js-regexp-objects example 7 result](../code_sandbox/snaps/js-regexp-objects-07-result.png)

- [x] **Outcome:** When `RegExp.escape` exists: `safe` is **`"\\[\\*\\]"`** (JSON) and `result` is **"W3Schools is a web school."** Node 22 has no `RegExp.escape` — then `safe` is the error string.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-regexp-objects/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `/e/.test(the free sentence)` return?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 2: What does `exec` return when nothing matches?

<details>
<summary>Answer</summary>

- [x] **`null`**, not `{}`.

</details>

### Question 3: What is `exec(/e/)` on that sentence?

<details>
<summary>Answer</summary>

- [x] **["e"]** at **index 2** (`The`).

</details>

### Question 4: How do you put `\d` in `new RegExp`?

<details>
<summary>Answer</summary>

- [x] **`new RegExp("\\d+")`**. `new RegExp("\d+")` is **`/d+/`**.

</details>

### Question 5: Do ` /ab+c/i ` and `new RegExp("ab+c", "i")` look the same?

<details>
<summary>Answer</summary>

- [x] **Yes** — both **`/ab+c/i`**.

</details>

### Question 6: What happens to `lastIndex` after a failed `/g` `exec`?

<details>
<summary>Answer</summary>

- [x] It goes back to **0**.

</details>

### Question 7: What are the `lastIndex` steps for `/is/g` on `Is this all there is?`?

<details>
<summary>Answer</summary>

- [x] Match at **5** → **7**; match at **18** → **20**; **null** → **0**.

</details>

### Question 8: Why `RegExp.escape("[*]")`?

<details>
<summary>Answer</summary>

- [x] So `[` `*` `]` are **literal**, not a character class. Then replace can turn `[*]` into `W3Schools`.

</details>

### Question 9: Can you skip the variable and call `/e/.test(s)`?

<details>
<summary>Answer</summary>

- [x] **Yes.**

</details>


</details>

## Summary

Carry a RegExp as a literal or a constructor, remember constructor escaping, use test for yes/no and exec for the match object, and treat lastIndex as mutable state whenever g or y is on. Escape user text before embedding it in a pattern.

## References

- [JS RegExp Objects (W3Schools)](https://www.w3schools.com/js/js_regexp_objects.asp)
- [MDN: RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
- [MDN: RegExp.escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/escape)
