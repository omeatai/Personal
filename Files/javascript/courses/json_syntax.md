# JSON Syntax

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

JSON syntax is stricter than JavaScript: quoted names, double-quoted strings, no trailing commas, no comments. Whitespace is optional.

This section has **21** examples:

- [x] **Example 1:** JSON object literal as text [View](#json-syntax-example-01)
- [x] **Example 2:** JSON array literal [View](#json-syntax-example-02)
- [x] **Example 3:** JSON array of strings (pretty) [View](#json-syntax-example-03)
- [x] **Example 4:** JSON array of numbers [View](#json-syntax-example-04)
- [x] **Example 5:** Property names must be double-quoted (valid) [View](#json-syntax-example-05)
- [x] **Example 6:** Unquoted property names are invalid JSON [View](#json-syntax-example-06)
- [x] **Example 7:** JSON strings use double quotes (valid) [View](#json-syntax-example-07)
- [x] **Example 8:** Single-quoted strings are invalid JSON [View](#json-syntax-example-08)
- [x] **Example 9:** Whitespace is optional — compact form [View](#json-syntax-example-09)
- [x] **Example 10:** Equivalent pretty JSON [View](#json-syntax-example-10)
- [x] **Example 11:** Trailing commas are invalid [View](#json-syntax-example-11)
- [x] **Example 12:** No trailing comma (correct) [View](#json-syntax-example-12)
- [x] **Example 13:** Comments are not allowed [View](#json-syntax-example-13)
- [x] **Example 14:** JSON value type — String [View](#json-syntax-example-14)
- [x] **Example 15:** JSON value type — Number [View](#json-syntax-example-15)
- [x] **Example 16:** JSON value type — Boolean [View](#json-syntax-example-16)
- [x] **Example 17:** JSON value type — Null [View](#json-syntax-example-17)
- [x] **Example 18:** JSON vs JS — unquoted names [View](#json-syntax-example-18)
- [x] **Example 19:** JSON vs JS — single-quoted strings [View](#json-syntax-example-19)
- [x] **Example 20:** JSON vs JS — trailing commas [View](#json-syntax-example-20)
- [x] **Example 21:** JSON vs JS — comments [View](#json-syntax-example-21)

## Detailed Explanation

- [x] Six value types.
- [x] Invalid JSON throws on parse.
- [x] JS object literals are not automatically JSON.

<a id="json-syntax-example-01"></a>

### **Example 1: JSON object literal as text**

- [x] A JSON object is `{ "name": value, ... }` inside a **string** if you parse it in JS.
- [x] Values may be string, number, boolean, null, object, or array.
- [x] `car` here is **null**.

Sandbox: `code_sandbox/json-syntax/object-literal.html`

```html
{"name":"John", "age":30, "car":null}
```

<img alt="json-syntax example 1 source" src="../code_sandbox/snaps/json-syntax-01-code.png" />

<img alt="json-syntax example 1 result" src="../code_sandbox/snaps/json-syntax-01-result.png" />

- [x] **Outcome:** Parse: **John**, age **30**, car **null**.

<a id="json-syntax-example-02"></a>

### **Example 2: JSON array literal**

- [x] Arrays use square brackets: `["Ford", "BMW", "Fiat"]`.
- [x] In JS you often keep that as a string then parse.

Sandbox: `code_sandbox/json-syntax/array-literal.html`

```html
["Ford", "BMW", "Fiat"]
```

<img alt="json-syntax example 2 source" src="../code_sandbox/snaps/json-syntax-02-code.png" />

<img alt="json-syntax example 2 result" src="../code_sandbox/snaps/json-syntax-02-result.png" />

- [x] **Outcome:** Parsed array length is **3**; index 0 is **Ford**.

<a id="json-syntax-example-03"></a>

### **Example 3: JSON array of strings (pretty)**

- [x] Whitespace between tokens is **allowed** and ignored.
- [x] Pretty-printed JSON is still the same data.

Sandbox: `code_sandbox/json-syntax/array-strings.html`

```html
[
  "Apple",
  "Banana",
  "Orange"
]
```

<img alt="json-syntax example 3 source" src="../code_sandbox/snaps/json-syntax-03-code.png" />

<img alt="json-syntax example 3 result" src="../code_sandbox/snaps/json-syntax-03-result.png" />

- [x] **Outcome:** Three fruits; index 1 is **Banana**.

<a id="json-syntax-example-04"></a>

### **Example 4: JSON array of numbers**

- [x] Numbers are **not** quoted.
- [x] `[1, 2, 3, 4, 5]` parses to actual numbers.

Sandbox: `code_sandbox/json-syntax/array-numbers.html`

```html
[1, 2, 3, 4, 5]
```

<img alt="json-syntax example 4 source" src="../code_sandbox/snaps/json-syntax-04-code.png" />

<img alt="json-syntax example 4 result" src="../code_sandbox/snaps/json-syntax-04-result.png" />

- [x] **Outcome:** `typeof a[0]` is **number** and the sum is **15**.

<a id="json-syntax-example-05"></a>

### **Example 5: Property names must be double-quoted (valid)**

- [x] Valid: `{ "name": "John" }`.
- [x] This is the JSON rule that bites JS developers first.

Sandbox: `code_sandbox/json-syntax/quoted-names-valid.html`

```html
{ "name": "John" }
```

<img alt="json-syntax example 5 source" src="../code_sandbox/snaps/json-syntax-05-code.png" />

<img alt="json-syntax example 5 result" src="../code_sandbox/snaps/json-syntax-05-result.png" />

- [x] **Outcome:** Parse succeeds; `name` is **John**.

<a id="json-syntax-example-06"></a>

### **Example 6: Unquoted property names are invalid JSON**

- [x] Invalid: `{ name: "John" }` — legal JS, **illegal JSON**.
- [x] `JSON.parse` throws **SyntaxError**.

Sandbox: `code_sandbox/json-syntax/unquoted-names-invalid.html`

```html
{ name: "John" }
```

<img alt="json-syntax example 6 source" src="../code_sandbox/snaps/json-syntax-06-code.png" />

<img alt="json-syntax example 6 result" src="../code_sandbox/snaps/json-syntax-06-result.png" />

- [x] **Outcome:** Parse throws **SyntaxError**.

<a id="json-syntax-example-07"></a>

### **Example 7: JSON strings use double quotes (valid)**

- [x] Valid: `{ "city": "London" }`.
- [x] Only **double** quotes wrap strings.

Sandbox: `code_sandbox/json-syntax/double-quoted-string.html`

```html
{ "city": "London" }
```

<img alt="json-syntax example 7 source" src="../code_sandbox/snaps/json-syntax-07-code.png" />

<img alt="json-syntax example 7 result" src="../code_sandbox/snaps/json-syntax-07-result.png" />

- [x] **Outcome:** Parse succeeds; city is **London**.

<a id="json-syntax-example-08"></a>

### **Example 8: Single-quoted strings are invalid JSON**

- [x] Invalid: `{ "city": 'London' }`.
- [x] JSON has no single-quoted strings.

Sandbox: `code_sandbox/json-syntax/single-quoted-string.html`

```html
{ "city": 'London' }
```

<img alt="json-syntax example 8 source" src="../code_sandbox/snaps/json-syntax-08-code.png" />

<img alt="json-syntax example 8 result" src="../code_sandbox/snaps/json-syntax-08-result.png" />

- [x] **Outcome:** Parse throws **SyntaxError**.

<a id="json-syntax-example-09"></a>

### **Example 9: Whitespace is optional — compact form**

- [x] `{"name":"John", "age":30}` is valid.
- [x] Spaces after colons/commas are optional.

Sandbox: `code_sandbox/json-syntax/whitespace-compact.html`

```html
{"name":"John", "age":30}
```

<img alt="json-syntax example 9 source" src="../code_sandbox/snaps/json-syntax-09-code.png" />

<img alt="json-syntax example 9 result" src="../code_sandbox/snaps/json-syntax-09-result.png" />

- [x] **Outcome:** Parse works; age is **30**.

<a id="json-syntax-example-10"></a>

### **Example 10: Equivalent pretty JSON**

- [x] The same object with newlines is **equivalent**.
- [x] Pretty print is for humans; parsers ignore the extra space.

Sandbox: `code_sandbox/json-syntax/whitespace-pretty.html`

```html
{
  "name": "John",
  "age": 30
}
```

<img alt="json-syntax example 10 source" src="../code_sandbox/snaps/json-syntax-10-code.png" />

<img alt="json-syntax example 10 result" src="../code_sandbox/snaps/json-syntax-10-result.png" />

- [x] **Outcome:** Pretty and compact parse to **equal** data (`age` 30).

<a id="json-syntax-example-11"></a>

### **Example 11: Trailing commas are invalid**

- [x] Wrong: `{ "name": "John", "age": 30, }` — comma after the last property.
- [x] JS objects allow trailing commas; **JSON does not**.

Sandbox: `code_sandbox/json-syntax/trailing-comma-wrong.html`

```html
{
  "name": "John",
  "age": 30,
}
```

<img alt="json-syntax example 11 source" src="../code_sandbox/snaps/json-syntax-11-code.png" />

<img alt="json-syntax example 11 result" src="../code_sandbox/snaps/json-syntax-11-result.png" />

- [x] **Outcome:** Parse throws **SyntaxError** because of the trailing comma.

<a id="json-syntax-example-12"></a>

### **Example 12: No trailing comma (correct)**

- [x] Remove the last comma: `{ "name": "John", "age": 30 }`.

Sandbox: `code_sandbox/json-syntax/trailing-comma-correct.html`

```html
{
  "name": "John",
  "age": 30
}
```

<img alt="json-syntax example 12 source" src="../code_sandbox/snaps/json-syntax-12-code.png" />

<img alt="json-syntax example 12 result" src="../code_sandbox/snaps/json-syntax-12-result.png" />

- [x] **Outcome:** Parse succeeds.

<a id="json-syntax-example-13"></a>

### **Example 13: Comments are not allowed**

- [x] Wrong: `// Customer name` inside JSON.
- [x] JSON has **no comments**. Put comments in docs, not in the payload.

Sandbox: `code_sandbox/json-syntax/comments-wrong.html`

```html
{
  // Customer name
  "name": "John"
}
```

<img alt="json-syntax example 13 source" src="../code_sandbox/snaps/json-syntax-13-code.png" />

<img alt="json-syntax example 13 result" src="../code_sandbox/snaps/json-syntax-13-result.png" />

- [x] **Outcome:** Parse throws **SyntaxError** on the comment.

<a id="json-syntax-example-14"></a>

### **Example 14: JSON value type — String**

- [x] Allowed types include **String**: `"John"`.
- [x] Must use double quotes.

Sandbox: `code_sandbox/json-syntax/type-string.html`

```html
"John"
```

<img alt="json-syntax example 14 source" src="../code_sandbox/snaps/json-syntax-14-code.png" />

<img alt="json-syntax example 14 result" src="../code_sandbox/snaps/json-syntax-14-result.png" />

- [x] **Outcome:** `JSON.parse('"John"')` is the string **John**.

<a id="json-syntax-example-15"></a>

### **Example 15: JSON value type — Number**

- [x] **Number**: `42` with no quotes.
- [x] Quoted `"42"` would be a string.

Sandbox: `code_sandbox/json-syntax/type-number.html`

```html
42
```

<img alt="json-syntax example 15 source" src="../code_sandbox/snaps/json-syntax-15-code.png" />

<img alt="json-syntax example 15 result" src="../code_sandbox/snaps/json-syntax-15-result.png" />

- [x] **Outcome:** `JSON.parse('42')` is number **42**.

<a id="json-syntax-example-16"></a>

### **Example 16: JSON value type — Boolean**

- [x] **Boolean**: `true` or `false` (lowercase).

Sandbox: `code_sandbox/json-syntax/type-boolean.html`

```html
true
```

<img alt="json-syntax example 16 source" src="../code_sandbox/snaps/json-syntax-16-code.png" />

<img alt="json-syntax example 16 result" src="../code_sandbox/snaps/json-syntax-16-result.png" />

- [x] **Outcome:** `JSON.parse('true')` is boolean **true**.

<a id="json-syntax-example-17"></a>

### **Example 17: JSON value type — Null**

- [x] **Null**: the literal `null` (empty value).

Sandbox: `code_sandbox/json-syntax/type-null.html`

```html
null
```

<img alt="json-syntax example 17 source" src="../code_sandbox/snaps/json-syntax-17-code.png" />

<img alt="json-syntax example 17 result" src="../code_sandbox/snaps/json-syntax-17-result.png" />

- [x] **Outcome:** `JSON.parse('null')` is **null**.

<a id="json-syntax-example-18"></a>

### **Example 18: JSON vs JS — unquoted names**

- [x] JSON: **No**. JS: **Yes**.

Sandbox: `code_sandbox/json-syntax/vs-js-unquoted.html`

```html
JSON: { "name": "John" }
JS:   { name: "John" }
```

<img alt="json-syntax example 18 source" src="../code_sandbox/snaps/json-syntax-18-code.png" />

<img alt="json-syntax example 18 result" src="../code_sandbox/snaps/json-syntax-18-result.png" />

- [x] **Outcome:** JSON parse of unquoted names **fails**; a JS object literal works.

<a id="json-syntax-example-19"></a>

### **Example 19: JSON vs JS — single-quoted strings**

- [x] JSON: **No**. JS: **Yes**.

Sandbox: `code_sandbox/json-syntax/vs-js-single-quotes.html`

```html
JSON cannot use 'London'
```

<img alt="json-syntax example 19 source" src="../code_sandbox/snaps/json-syntax-19-code.png" />

<img alt="json-syntax example 19 result" src="../code_sandbox/snaps/json-syntax-19-result.png" />

- [x] **Outcome:** JSON parse of single quotes **fails**.

<a id="json-syntax-example-20"></a>

### **Example 20: JSON vs JS — trailing commas**

- [x] JSON: **No**. JS: **Yes** (in modern engines).

Sandbox: `code_sandbox/json-syntax/vs-js-trailing.html`

```html
JSON forbids a comma after the last item
```

<img alt="json-syntax example 20 source" src="../code_sandbox/snaps/json-syntax-20-code.png" />

<img alt="json-syntax example 20 result" src="../code_sandbox/snaps/json-syntax-20-result.png" />

- [x] **Outcome:** Covered by the trailing-comma examples: JSON **SyntaxError**, JS objects allow it.

<a id="json-syntax-example-21"></a>

### **Example 21: JSON vs JS — comments**

- [x] JSON: **No**. JS: **Yes** (`//` and `/* */`).

Sandbox: `code_sandbox/json-syntax/vs-js-comments.html`

```html
// not legal in JSON
```

<img alt="json-syntax example 21 source" src="../code_sandbox/snaps/json-syntax-21-code.png" />

<img alt="json-syntax example 21 result" src="../code_sandbox/snaps/json-syntax-21-result.png" />

- [x] **Outcome:** JSON with a comment **throws**; JavaScript comments are fine in `.js` files.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/json-syntax/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Must property names be quoted in JSON?

<details>
<summary>Answer</summary>

- [x] **Yes** — double quotes.

</details>

### Question 2: Can JSON use single-quoted strings?

<details>
<summary>Answer</summary>

- [x] **No**.

</details>

### Question 3: Are trailing commas allowed?

<details>
<summary>Answer</summary>

- [x] **No** — that is a SyntaxError.

</details>

### Question 4: Can JSON contain `//` comments?

<details>
<summary>Answer</summary>

- [x] **No**.

</details>

### Question 5: Is whitespace significant?

<details>
<summary>Answer</summary>

- [x] **No** — extra spaces/newlines between tokens are ignored.

</details>

### Question 6: Name the six JSON value types.

<details>
<summary>Answer</summary>

- [x] **String, Number, Boolean, Null, Object, Array**.

</details>

### Question 7: What does `JSON.parse('{ name: "John" }')` do?

<details>
<summary>Answer</summary>

- [x] **Throws SyntaxError** (unquoted name).

</details>

### Question 8: Is `{ name: "John" }` valid JavaScript?

<details>
<summary>Answer</summary>

- [x] **Yes** — JS object literals allow unquoted names.

</details>

### Question 9: What is `car` in the first example?

<details>
<summary>Answer</summary>

- [x] **null**.

</details>

### Question 10: Does pretty-printed JSON change the data?

<details>
<summary>Answer</summary>

- [x] **No** — it is equivalent.

</details>


</details>

## Summary

Write JSON with double quotes and no trailing commas or comments. Pretty printing does not change the data. Do not copy JS object syntax into a .json file.

## References

- [JSON Syntax](https://www.w3schools.com/js/js_json_syntax.asp)
- [MDN JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
