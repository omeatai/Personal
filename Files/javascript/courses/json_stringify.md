# JSON Stringify

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

`JSON.stringify(value, replacer, space)` builds JSON text. Replacer can pick keys or transform values. space pretty-prints. Functions/undefined/symbols are omitted in objects and become null in arrays. Circular objects and BigInt throw.

This section has **16** examples:

- [x] **Example 1:** JSON.stringify(value, replacer, space) [View](#json-stringify-example-01)
- [x] **Example 2:** Converting an object [View](#json-stringify-example-02)
- [x] **Example 3:** Converting an array [View](#json-stringify-example-03)
- [x] **Example 4:** Converting other values [View](#json-stringify-example-04)
- [x] **Example 5:** Selecting properties with a replacer array [View](#json-stringify-example-05)
- [x] **Example 6:** Transforming values with a replacer function [View](#json-stringify-example-06)
- [x] **Example 7:** Formatting JSON with space [View](#json-stringify-example-07)
- [x] **Example 8:** Functions and undefined are omitted from objects [View](#json-stringify-example-08)
- [x] **Example 9:** NaN and Infinity become null in objects [View](#json-stringify-example-09)
- [x] **Example 10:** In arrays, functions/undefined/NaN/Infinity become null [View](#json-stringify-example-10)
- [x] **Example 11:** Stringifying dates [View](#json-stringify-example-11)
- [x] **Example 12:** Storing JSON in localStorage [View](#json-stringify-example-12)
- [x] **Example 13:** Mistake — stringifying twice [View](#json-stringify-example-13)
- [x] **Example 14:** Circular objects throw TypeError [View](#json-stringify-example-14)
- [x] **Example 15:** BigInt throws TypeError [View](#json-stringify-example-15)
- [x] **Example 16:** Symbol omitted from objects, null in arrays [View](#json-stringify-example-16)

## Detailed Explanation

- [x] replacer array or function.
- [x] space for indent.
- [x] localStorage needs strings.

<a id="json-stringify-example-01"></a>

### **Example 1: JSON.stringify(value, replacer, space)**

- [x] **value** — what to convert.
- [x] **replacer** — a function or an array of keys to keep.
- [x] **space** — number or string for indentation.

Sandbox: `code_sandbox/json-stringify/syntax.html`

```html
JSON.stringify(value, replacer, space)
```

<img alt="json-stringify example 1 source" src="../code_sandbox/snaps/json-stringify-01-code.png" />

<img alt="json-stringify example 1 result" src="../code_sandbox/snaps/json-stringify-01-result.png" />

- [x] **Outcome:** `JSON.stringify.length` is **3**.

<a id="json-stringify-example-02"></a>

### **Example 2: Converting an object**

- [x] Stringify `{name, age, city}` to JSON text.

Sandbox: `code_sandbox/json-stringify/object.html`

```html
const person = { name: "John", age: 30, city: "New York" };
const text = JSON.stringify(person);
```

<img alt="json-stringify example 2 source" src="../code_sandbox/snaps/json-stringify-02-code.png" />

<img alt="json-stringify example 2 result" src="../code_sandbox/snaps/json-stringify-02-result.png" />

- [x] **Outcome:** Text contains **`"name":"John"`** and **`"age":30`**.

<a id="json-stringify-example-03"></a>

### **Example 3: Converting an array**

- [x] Arrays stringify to JSON arrays.

Sandbox: `code_sandbox/json-stringify/array.html`

```html
const cars = ["Ford", "Volvo", "BMW"];
const text = JSON.stringify(cars);
```

<img alt="json-stringify example 3 source" src="../code_sandbox/snaps/json-stringify-03-code.png" />

<img alt="json-stringify example 3 result" src="../code_sandbox/snaps/json-stringify-03-result.png" />

- [x] **Outcome:** Result is **`["Ford","Volvo","BMW"]`**.

<a id="json-stringify-example-04"></a>

### **Example 4: Converting other values**

- [x] The page stringifies a string, numbers, booleans, Boolean objects, undefined, null, NaN, Infinity.
- [x] `undefined` as a **root** value becomes `undefined` (the JS value), not a JSON text — `JSON.stringify(undefined)` returns **undefined**, so `String(...)` shows that.
- [x] `null`, `NaN`, `Infinity` become **`null`** as JSON text.

Sandbox: `code_sandbox/json-stringify/other-values.html`

```html
JSON.stringify("John");
JSON.stringify(42);
JSON.stringify(false);
JSON.stringify(Boolean(0));
JSON.stringify(true);
JSON.stringify(Boolean(1));
JSON.stringify(undefined);
JSON.stringify(null);
JSON.stringify(NaN);
JSON.stringify(Infinity);
```

<img alt="json-stringify example 4 source" src="../code_sandbox/snaps/json-stringify-04-code.png" />

<img alt="json-stringify example 4 result" src="../code_sandbox/snaps/json-stringify-04-result.png" />

- [x] **Outcome:** Each call’s JSON text (or `undefined`) is listed. Null/NaN/Infinity are **`null`**.

<a id="json-stringify-example-05"></a>

### **Example 5: Selecting properties with a replacer array**

- [x] `JSON.stringify(person, ["name", "city"])` keeps **only** those keys.
- [x] `age` is omitted.

Sandbox: `code_sandbox/json-stringify/select-keys.html`

```html
let text = JSON.stringify(person, ["name", "city"]);
```

<img alt="json-stringify example 5 source" src="../code_sandbox/snaps/json-stringify-05-code.png" />

<img alt="json-stringify example 5 result" src="../code_sandbox/snaps/json-stringify-05-result.png" />

- [x] **Outcome:** JSON has **name** and **city**, not **age**.

<a id="json-stringify-example-06"></a>

### **Example 6: Transforming values with a replacer function**

- [x] If `key == "age"`, return `value + 1`.
- [x] Other keys return `value`.

Sandbox: `code_sandbox/json-stringify/replacer-fn.html`

```html
JSON.stringify(person, function(key, value) {
  if (key == "age") { return value + 1; }
  return value;
});
```

<img alt="json-stringify example 6 source" src="../code_sandbox/snaps/json-stringify-06-code.png" />

<img alt="json-stringify example 6 result" src="../code_sandbox/snaps/json-stringify-06-result.png" />

- [x] **Outcome:** Age in the JSON text is **31**.

<a id="json-stringify-example-07"></a>

### **Example 7: Formatting JSON with space**

- [x] `JSON.stringify(person, null, 1)` pretty-prints with **1** space indent.
- [x] `2` or `"\t"` are common.

Sandbox: `code_sandbox/json-stringify/space.html`

```html
let text = JSON.stringify(person, null, 1);
```

<img alt="json-stringify example 7 source" src="../code_sandbox/snaps/json-stringify-07-code.png" />

<img alt="json-stringify example 7 result" src="../code_sandbox/snaps/json-stringify-07-result.png" />

- [x] **Outcome:** The result contains **newlines** and indented `"name"`.

<a id="json-stringify-example-08"></a>

### **Example 8: Functions and undefined are omitted from objects**

- [x] `greet: function(){}` and `age: undefined` disappear.
- [x] Only **name** remains.

Sandbox: `code_sandbox/json-stringify/omit-fn-undef.html`

```html
JSON.stringify({ name: "John", greet: function() {}, age: undefined })
```

<img alt="json-stringify example 8 source" src="../code_sandbox/snaps/json-stringify-08-code.png" />

<img alt="json-stringify example 8 result" src="../code_sandbox/snaps/json-stringify-08-result.png" />

- [x] **Outcome:** Result is **`{"name":"John"}`**.

<a id="json-stringify-example-09"></a>

### **Example 9: NaN and Infinity become null in objects**

- [x] W3Schools writes `NAN` (typo). The real value is **`NaN`**.
- [x] Both stringify to **null**.

Sandbox: `code_sandbox/json-stringify/nan-infinity-obj.html`

```html
JSON.stringify({ name: "John", greet: NaN, age: Infinity })
```

<img alt="json-stringify example 9 source" src="../code_sandbox/snaps/json-stringify-09-code.png" />

<img alt="json-stringify example 9 result" src="../code_sandbox/snaps/json-stringify-09-result.png" />

- [x] **Outcome:** JSON has **null** for both greet and age. (The page’s `NAN` identifier would be a ReferenceError — we use `NaN`.)

<a id="json-stringify-example-10"></a>

### **Example 10: In arrays, functions/undefined/NaN/Infinity become null**

- [x] Array stringify **keeps slots**: those values become **`null`**, they are not omitted.

Sandbox: `code_sandbox/json-stringify/array-holes.html`

```html
JSON.stringify(["Ford", "Volvo", function() {}, undefined, NaN, Infinity])
```

<img alt="json-stringify example 10 source" src="../code_sandbox/snaps/json-stringify-10-code.png" />

<img alt="json-stringify example 10 result" src="../code_sandbox/snaps/json-stringify-10-result.png" />

- [x] **Outcome:** Result includes **null** entries for the last four slots.

<a id="json-stringify-example-11"></a>

### **Example 11: Stringifying dates**

- [x] Date objects become **ISO strings** in JSON.
- [x] Parse will give a string unless you revive.

Sandbox: `code_sandbox/json-stringify/dates.html`

```html
const person = {name:"John", today:date, city:"New York"};
let text = JSON.stringify(person);
```

<img alt="json-stringify example 11 source" src="../code_sandbox/snaps/json-stringify-11-code.png" />

<img alt="json-stringify example 11 result" src="../code_sandbox/snaps/json-stringify-11-result.png" />

- [x] **Outcome:** `today` in the JSON is a string starting with **20** (ISO year).

<a id="json-stringify-example-12"></a>

### **Example 12: Storing JSON in localStorage**

- [x] stringify → `localStorage.setItem` → `getItem` → parse.
- [x] This is the standard “save object” pattern.
- [x] Storage is **string-only**.

Sandbox: `code_sandbox/json-stringify/local-storage.html`

```html
const myJSON = JSON.stringify(myObj);
localStorage.setItem("testJSON", myJSON);
let obj = JSON.parse(localStorage.getItem("testJSON"));
```

<img alt="json-stringify example 12 source" src="../code_sandbox/snaps/json-stringify-12-code.png" />

<img alt="json-stringify example 12 result" src="../code_sandbox/snaps/json-stringify-12-result.png" />

- [x] **Outcome:** Round-trip: **John**, age **31**, city **New York**.

<a id="json-stringify-example-13"></a>

### **Example 13: Mistake — stringifying twice**

- [x] Stringify of an object is a string. Stringify **that string** wraps it in extra quotes and escapes.
- [x] Parse once would still be a **string**, not an object.

Sandbox: `code_sandbox/json-stringify/double-stringify.html`

```html
const text = JSON.stringify(person);
const textAgain = JSON.stringify(text);
```

<img alt="json-stringify example 13 source" src="../code_sandbox/snaps/json-stringify-13-code.png" />

<img alt="json-stringify example 13 result" src="../code_sandbox/snaps/json-stringify-13-result.png" />

- [x] **Outcome:** `textAgain` starts with **`"`** and contains escaped quotes — it is JSON of a string.

<a id="json-stringify-example-14"></a>

### **Example 14: Circular objects throw TypeError**

- [x] `person.self = person` cannot be represented in JSON.
- [x] `JSON.stringify(person)` throws **TypeError**.

Sandbox: `code_sandbox/json-stringify/circular.html`

```html
person.self = person;
JSON.stringify(person);
```

<img alt="json-stringify example 14 source" src="../code_sandbox/snaps/json-stringify-14-code.png" />

<img alt="json-stringify example 14 result" src="../code_sandbox/snaps/json-stringify-14-result.png" />

- [x] **Outcome:** The catch block reports **TypeError** (circular structure).

<a id="json-stringify-example-15"></a>

### **Example 15: BigInt throws TypeError**

- [x] Table row: BigInt cannot be serialized.

Sandbox: `code_sandbox/json-stringify/bigint-throws.html`

```html
JSON.stringify(10n)
```

<img alt="json-stringify example 15 source" src="../code_sandbox/snaps/json-stringify-15-code.png" />

<img alt="json-stringify example 15 result" src="../code_sandbox/snaps/json-stringify-15-result.png" />

- [x] **Outcome:** **TypeError** is thrown.

<a id="json-stringify-example-16"></a>

### **Example 16: Symbol omitted from objects, null in arrays**

- [x] Table: Symbol is omitted in objects; in arrays it becomes **null**.

Sandbox: `code_sandbox/json-stringify/symbol-omit.html`

```html
JSON.stringify({ s: Symbol("x") })
JSON.stringify([Symbol("x")])
```

<img alt="json-stringify example 16 source" src="../code_sandbox/snaps/json-stringify-16-code.png" />

<img alt="json-stringify example 16 result" src="../code_sandbox/snaps/json-stringify-16-result.png" />

- [x] **Outcome:** Object → **`{}`**. Array → **`[null]`**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/json-stringify/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are stringify’s three parameters?

<details>
<summary>Answer</summary>

- [x] **value**, **replacer**, **space**.

</details>

### Question 2: How do you keep only some keys?

<details>
<summary>Answer</summary>

- [x] Pass an **array of key names** as replacer.

</details>

### Question 3: How do you pretty-print?

<details>
<summary>Answer</summary>

- [x] Pass a **space** number or string as the third argument.

</details>

### Question 4: What happens to functions in objects?

<details>
<summary>Answer</summary>

- [x] They are **omitted**.

</details>

### Question 5: What happens to functions in arrays?

<details>
<summary>Answer</summary>

- [x] They become **null**.

</details>

### Question 6: What happens to `undefined` in objects?

<details>
<summary>Answer</summary>

- [x] **Omitted**.

</details>

### Question 7: What happens to Date objects?

<details>
<summary>Answer</summary>

- [x] They become **ISO strings**.

</details>

### Question 8: How do you save an object in localStorage?

<details>
<summary>Answer</summary>

- [x] **stringify**, `setItem`, later `getItem` + **parse**.

</details>

### Question 9: What does a circular object do?

<details>
<summary>Answer</summary>

- [x] **Throws TypeError**.

</details>

### Question 10: What does BigInt do?

<details>
<summary>Answer</summary>

- [x] **Throws TypeError**.

</details>

### Question 11: Why is double stringify a mistake?

<details>
<summary>Answer</summary>

- [x] You store a **string of a string**, not the object.

</details>


</details>

## Summary

Stringify once, pretty-print with space, and store with localStorage via stringify/parse. Do not stringify twice. Catch TypeError for cycles and BigInt.

## References

- [JSON Stringify](https://www.w3schools.com/js/js_json_stringify.asp)
- [MDN JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
