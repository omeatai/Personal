<details>
  <summary>JSON Parse</summary>

## Introduction

`JSON.parse(text, reviver)` turns JSON text into JS values. Use a reviver to convert ages or dates. Always try/catch untrusted text. Do not parse objects or parse twice.

This section has **16** examples:

- [x] **Example 1:** JSON.parse(text, reviver) syntax [View](#json-parse-example-01)
- [x] **Example 2:** Parsing a JSON object [View](#json-parse-example-02)
- [x] **Example 3:** Parsing a JSON array [View](#json-parse-example-03)
- [x] **Example 4:** Parsing a JSON string value [View](#json-parse-example-04)
- [x] **Example 5:** Parsing a JSON number value [View](#json-parse-example-05)
- [x] **Example 6:** Parsing JSON true [View](#json-parse-example-06)
- [x] **Example 7:** Parsing JSON null [View](#json-parse-example-07)
- [x] **Example 8:** Common use — parse then show in HTML [View](#json-parse-example-08)
- [x] **Example 9:** Reviver — convert age to a number [View](#json-parse-example-09)
- [x] **Example 10:** Reviver — convert a date string to Date [View](#json-parse-example-10)
- [x] **Example 11:** Invalid JSON throws [View](#json-parse-example-11)
- [x] **Example 12:** Valid JSON object text [View](#json-parse-example-12)
- [x] **Example 13:** Invalid variants — single quotes, unquoted name, unquoted value [View](#json-parse-example-13)
- [x] **Example 14:** Handling parse errors with try/catch [View](#json-parse-example-14)
- [x] **Example 15:** Mistake — parsing a JavaScript object [View](#json-parse-example-15)
- [x] **Example 16:** Mistake — parsing JSON twice [View](#json-parse-example-16)

## Detailed Explanation

- [x] text + optional reviver.
- [x] SyntaxError on bad JSON.
- [x] Parse strings, not live objects.

<a id="json-parse-example-01"></a>

### **Example 1: JSON.parse(text, reviver) syntax**

- [x] First argument: the **JSON text** (a string).
- [x] Second: optional **reviver(key, value)** that can transform values.
- [x] Throws **SyntaxError** if the text is not JSON.

Sandbox: `code_sandbox/json-parse/syntax.html`

```html
JSON.parse(text, reviver)
```

<img alt="json-parse example 1 source" src="./code_sandbox/snaps/json-parse-01-code.png" />

<img alt="json-parse example 1 result" src="./code_sandbox/snaps/json-parse-01-result.png" />

- [x] **Outcome:** `JSON.parse` is a function of **2** parameters (`length` 2).

<a id="json-parse-example-02"></a>

### **Example 2: Parsing a JSON object**

- [x] Parse an object and read `person.name`.

Sandbox: `code_sandbox/json-parse/parse-object.html`

```html
const text = '{"name":"John","age":30,"city":"New York"}';
const person = JSON.parse(text);
let name = person.name;
```

<img alt="json-parse example 2 source" src="./code_sandbox/snaps/json-parse-02-code.png" />

<img alt="json-parse example 2 result" src="./code_sandbox/snaps/json-parse-02-result.png" />

- [x] **Outcome:** **name** is **John**.

<a id="json-parse-example-03"></a>

### **Example 3: Parsing a JSON array**

- [x] A root array parses to a JS **Array**.
- [x] `cars[0]` is **Ford**.

Sandbox: `code_sandbox/json-parse/parse-array.html`

```html
const text = '["Ford","Volvo","BMW"]';
const cars = JSON.parse(text);
let name = cars[0];
```

<img alt="json-parse example 3 source" src="./code_sandbox/snaps/json-parse-03-code.png" />

<img alt="json-parse example 3 result" src="./code_sandbox/snaps/json-parse-03-result.png" />

- [x] **Outcome:** **Ford** is at index 0.

<a id="json-parse-example-04"></a>

### **Example 4: Parsing a JSON string value**

- [x] `JSON.parse('"John"')` is the string John.

Sandbox: `code_sandbox/json-parse/parse-string.html`

```html
value = JSON.parse('"John"');
```

<img alt="json-parse example 4 source" src="./code_sandbox/snaps/json-parse-04-code.png" />

<img alt="json-parse example 4 result" src="./code_sandbox/snaps/json-parse-04-result.png" />

- [x] **Outcome:** Result is string **John**.

<a id="json-parse-example-05"></a>

### **Example 5: Parsing a JSON number value**

- [x] `JSON.parse('42')` is number 42.

Sandbox: `code_sandbox/json-parse/parse-number.html`

```html
value = JSON.parse('42');
```

<img alt="json-parse example 5 source" src="./code_sandbox/snaps/json-parse-05-code.png" />

<img alt="json-parse example 5 result" src="./code_sandbox/snaps/json-parse-05-result.png" />

- [x] **Outcome:** typeof **number**, value **42**.

<a id="json-parse-example-06"></a>

### **Example 6: Parsing JSON true**

- [x] `JSON.parse('true')` is boolean true.

Sandbox: `code_sandbox/json-parse/parse-true.html`

```html
value = JSON.parse('true');
```

<img alt="json-parse example 6 source" src="./code_sandbox/snaps/json-parse-06-code.png" />

<img alt="json-parse example 6 result" src="./code_sandbox/snaps/json-parse-06-result.png" />

- [x] **Outcome:** typeof **boolean**, value **true**.

<a id="json-parse-example-07"></a>

### **Example 7: Parsing JSON null**

- [x] `JSON.parse('null')` is **null** (and `typeof` is the quirky `'object'`).

Sandbox: `code_sandbox/json-parse/parse-null.html`

```html
value = JSON.parse('null');
```

<img alt="json-parse example 7 source" src="./code_sandbox/snaps/json-parse-07-code.png" />

<img alt="json-parse example 7 result" src="./code_sandbox/snaps/json-parse-07-result.png" />

- [x] **Outcome:** Value is **null**.

<a id="json-parse-example-08"></a>

### **Example 8: Common use — parse then show in HTML**

- [x] Typical pattern: parse, then `textContent` / `innerHTML` a property.

Sandbox: `code_sandbox/json-parse/display-name.html`

```html
document.getElementById("demo").innerHTML = person.name;
```

<img alt="json-parse example 8 source" src="./code_sandbox/snaps/json-parse-08-code.png" />

<img alt="json-parse example 8 result" src="./code_sandbox/snaps/json-parse-08-result.png" />

- [x] **Outcome:** The page shows **John**.

<a id="json-parse-example-09"></a>

### **Example 9: Reviver — convert age to a number**

- [x] If JSON stored age as `"30"` (string), a reviver can `return Number(value)` when `key == "age"`.
- [x] Other keys return `value` unchanged.
- [x] The reviver walks **from the inside out**.

Sandbox: `code_sandbox/json-parse/reviver-age.html`

```html
const person = JSON.parse(text, function(key, value) {
  if (key == "age") { return Number(value); }
  return value;
});
typeof person.age; // number
```

<img alt="json-parse example 9 source" src="./code_sandbox/snaps/json-parse-09-code.png" />

<img alt="json-parse example 9 result" src="./code_sandbox/snaps/json-parse-09-result.png" />

- [x] **Outcome:** `typeof person.age` is **number** (30).

<a id="json-parse-example-10"></a>

### **Example 10: Reviver — convert a date string to Date**

- [x] When `key === "date"`, `return new Date(value)`.
- [x] `typeof myObject.date` is **object** (Date).

Sandbox: `code_sandbox/json-parse/reviver-date.html`

```html
const myObject = JSON.parse(text, (key, value) => {
  if (key === "date") { return new Date(value); }
  return value;
});
typeof myObject.date; // object
```

<img alt="json-parse example 10 source" src="./code_sandbox/snaps/json-parse-10-code.png" />

<img alt="json-parse example 10 result" src="./code_sandbox/snaps/json-parse-10-result.png" />

- [x] **Outcome:** `date` is a **Date** object; `getUTCFullYear()` is **2026**.

<a id="json-parse-example-11"></a>

### **Example 11: Invalid JSON throws**

- [x] `{name:'John'}` is not JSON.
- [x] Bare `JSON.parse` throws — always **try/catch** untrusted text.

Sandbox: `code_sandbox/json-parse/invalid-parse.html`

```html
const text = "{name:'John'}";
JSON.parse(text);
```

<img alt="json-parse example 11 source" src="./code_sandbox/snaps/json-parse-11-code.png" />

<img alt="json-parse example 11 result" src="./code_sandbox/snaps/json-parse-11-result.png" />

- [x] **Outcome:** Uncaught this would abort; the sandbox catches **SyntaxError**.

<a id="json-parse-example-12"></a>

### **Example 12: Valid JSON object text**

- [x] Valid: `{"name":"John"}`.

Sandbox: `code_sandbox/json-parse/valid-form.html`

```html
{"name":"John"}
```

<img alt="json-parse example 12 source" src="./code_sandbox/snaps/json-parse-12-code.png" />

<img alt="json-parse example 12 result" src="./code_sandbox/snaps/json-parse-12-result.png" />

- [x] **Outcome:** Parse succeeds.

<a id="json-parse-example-13"></a>

### **Example 13: Invalid variants — single quotes, unquoted name, unquoted value**

- [x] Invalid: `{'name':"John"}`, `{"name":'John'}`, `{name:"John"}`, `{"name":John}`.

Sandbox: `code_sandbox/json-parse/invalid-variants.html`

```html
{'name':"John"}
{"name":'John'}
{name:"John"}
{"name":John}
```

<img alt="json-parse example 13 source" src="./code_sandbox/snaps/json-parse-13-code.png" />

<img alt="json-parse example 13 result" src="./code_sandbox/snaps/json-parse-13-result.png" />

- [x] **Outcome:** Each variant throws **SyntaxError** (four errors counted).

<a id="json-parse-example-14"></a>

### **Example 14: Handling parse errors with try/catch**

- [x] Wrap `JSON.parse` in **try/catch** and display `err`.

Sandbox: `code_sandbox/json-parse/try-catch.html`

```html
try {
  const person = JSON.parse(text);
} catch(err) {
  myDisplayer(err);
}
```

<img alt="json-parse example 14 source" src="./code_sandbox/snaps/json-parse-14-code.png" />

<img alt="json-parse example 14 result" src="./code_sandbox/snaps/json-parse-14-result.png" />

- [x] **Outcome:** The catch block receives a **SyntaxError** for `{name:'John'}`.

<a id="json-parse-example-15"></a>

### **Example 15: Mistake — parsing a JavaScript object**

- [x] `JSON.parse(person)` when `person` is already an object **coerces** it to `"[object Object]"`, which is not JSON.
- [x] That throws **SyntaxError**.

Sandbox: `code_sandbox/json-parse/parse-object-wrong.html`

```html
const person = {name: "John"};
const result = JSON.parse(person);
```

<img alt="json-parse example 15 source" src="./code_sandbox/snaps/json-parse-15-code.png" />

<img alt="json-parse example 15 result" src="./code_sandbox/snaps/json-parse-15-result.png" />

- [x] **Outcome:** The call throws **SyntaxError** (`[object Object]` is not JSON).

<a id="json-parse-example-16"></a>

### **Example 16: Mistake — parsing JSON twice**

- [x] After one parse you have an **object**. Parsing that object again fails the same way.
- [x] Or if you parse a string that is already a JS string value, a second parse of that string value may throw or return something else.
- [x] W3Schools: `JSON.parse(person)` after `person` is already parsed.

Sandbox: `code_sandbox/json-parse/parse-twice-wrong.html`

```html
const person = JSON.parse('{"name":"John"}');
const result = JSON.parse(person);
```

<img alt="json-parse example 16 source" src="./code_sandbox/snaps/json-parse-16-code.png" />

<img alt="json-parse example 16 result" src="./code_sandbox/snaps/json-parse-16-result.png" />

- [x] **Outcome:** The second parse throws **SyntaxError**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/json-parse/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are the two `JSON.parse` parameters?

<details>
<summary>Answer</summary>

- [x] **text** and optional **reviver**.

</details>

### Question 2: What is `cars[0]` after parsing the cars array?

<details>
<summary>Answer</summary>

- [x] **Ford**.

</details>

### Question 3: What does a reviver receive?

<details>
<summary>Answer</summary>

- [x] **key** and **value** for each nested value.

</details>

### Question 4: How do you turn a date string into a Date?

<details>
<summary>Answer</summary>

- [x] In the reviver, `if (key === "date") return new Date(value)`.

</details>

### Question 5: What exception does bad JSON throw?

<details>
<summary>Answer</summary>

- [x] **SyntaxError**.

</details>

### Question 6: Should you parse a JS object?

<details>
<summary>Answer</summary>

- [x] **No** — parse **text** only.

</details>

### Question 7: What happens if you parse twice?

<details>
<summary>Answer</summary>

- [x] The second call gets an **object** and **throws**.

</details>

### Question 8: What is `JSON.parse('null')`?

<details>
<summary>Answer</summary>

- [x] **null**.

</details>

### Question 9: What is `JSON.parse('42')`?

<details>
<summary>Answer</summary>

- [x] The number **42**.

</details>

### Question 10: Why try/catch?

<details>
<summary>Answer</summary>

- [x] Untrusted or hand-written JSON may be **invalid**.

</details>


</details>

## Summary

Parse text once, optionally revive dates/numbers, and catch SyntaxError. Passing an already-parsed object is a common mistake.

## References

- [JSON Parse](https://www.w3schools.com/js/js_json_parse.asp)
- [MDN JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

</details>
