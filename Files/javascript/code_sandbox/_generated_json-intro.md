<details>
  <summary>JSON Intro</summary>

## Introduction

JSON is a language-independent **text** format. JavaScript converts it with `JSON.parse` and `JSON.stringify`. Objects and arrays are the two main structures.

This section has **11** examples:

- [x] **Example 1:** A JSON example — name, age, city [View](#json-intro-example-01)
- [x] **Example 2:** Same data as a JavaScript object [View](#json-intro-example-02)
- [x] **Example 3:** JSON is text [View](#json-intro-example-03)
- [x] **Example 4:** JSON.parse — JSON text to JavaScript [View](#json-intro-example-04)
- [x] **Example 5:** JSON.stringify — JavaScript to JSON text [View](#json-intro-example-05)
- [x] **Example 6:** JSON round trip — stringify then parse [View](#json-intro-example-06)
- [x] **Example 7:** JSON files — customer.json [View](#json-intro-example-07)
- [x] **Example 8:** JSON objects — firstName / lastName [View](#json-intro-example-08)
- [x] **Example 9:** JSON arrays — employees [View](#json-intro-example-09)
- [x] **Example 10:** JSON text built from concatenated strings [View](#json-intro-example-10)
- [x] **Example 11:** Display parsed employees[1] in HTML [View](#json-intro-example-11)

## Detailed Explanation

- [x] JSON is text until you parse it.
- [x] Property names are double-quoted.
- [x] The employees sample uses an array of objects.

<a id="json-intro-example-01"></a>

### **Example 1: A JSON example — name, age, city**

- [x] JSON is a **text** format for data: curly braces, quoted names, values.
- [x] This object has a string, a number, and a string.
- [x] JSON is **not** a JavaScript program — it is data you parse.

Sandbox: `code_sandbox/json-intro/json-example.html`

```html
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

<img alt="json-intro example 1 source" src="./code_sandbox/snaps/json-intro-01-code.png" />

<img alt="json-intro example 1 result" src="./code_sandbox/snaps/json-intro-01-result.png" />

- [x] **Outcome:** `JSON.parse` of that text gives `name` **John** and `age` **30** (a number).

<a id="json-intro-example-02"></a>

### **Example 2: Same data as a JavaScript object**

- [x] In JavaScript, property names **may** be unquoted (`name: "John"`).
- [x] JSON **requires** double-quoted names.
- [x] The values can look similar; the rules are stricter in JSON.

Sandbox: `code_sandbox/json-intro/js-object.html`

```html
const person = {
  name: "John",
  age: 30,
  city: "New York"
};
```

<img alt="json-intro example 2 source" src="./code_sandbox/snaps/json-intro-02-code.png" />

<img alt="json-intro example 2 result" src="./code_sandbox/snaps/json-intro-02-result.png" />

- [x] **Outcome:** The JS object prints **John 30 New York** without `JSON.parse`.

<a id="json-intro-example-03"></a>

### **Example 3: JSON is text**

- [x] A JSON document is a **string** until you parse it.
- [x] `typeof` of the raw payload is **`string`**.
- [x] After `JSON.parse`, `typeof person` is **`object`**.

Sandbox: `code_sandbox/json-intro/json-is-text.html`

```html
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

<img alt="json-intro example 3 source" src="./code_sandbox/snaps/json-intro-03-code.png" />

<img alt="json-intro example 3 result" src="./code_sandbox/snaps/json-intro-03-result.png" />

- [x] **Outcome:** Before parse: **string**. After parse: **object** with `name` John.

<a id="json-intro-example-04"></a>

### **Example 4: JSON.parse — JSON text to JavaScript**

- [x] `JSON.parse(text)` turns JSON **text** into a JS value.
- [x] Invalid JSON **throws** `SyntaxError`.
- [x] This is how APIs become objects you can use.

Sandbox: `code_sandbox/json-intro/parse.html`

```html
const text = '{"name":"John", "age":30, "city":"New York"}';
const person = JSON.parse(text);
```

<img alt="json-intro example 4 source" src="./code_sandbox/snaps/json-intro-04-code.png" />

<img alt="json-intro example 4 result" src="./code_sandbox/snaps/json-intro-04-result.png" />

- [x] **Outcome:** `person.name` is **John** after parse.

<a id="json-intro-example-05"></a>

### **Example 5: JSON.stringify — JavaScript to JSON text**

- [x] `JSON.stringify(value)` does the reverse: JS value → **string**.
- [x] The W3Schools demo writes that string into the page.
- [x] Names become quoted; `undefined`/functions are dropped (later page).

Sandbox: `code_sandbox/json-intro/stringify.html`

```html
const person = { name: "John", age: 30, city: "New York" };
const text = JSON.stringify(person);
document.getElementById("demo").innerHTML = text;
```

<img alt="json-intro example 5 source" src="./code_sandbox/snaps/json-intro-05-code.png" />

<img alt="json-intro example 5 result" src="./code_sandbox/snaps/json-intro-05-result.png" />

- [x] **Outcome:** The page shows JSON text like **`{"name":"John","age":30,"city":"New York"}`**.

<a id="json-intro-example-06"></a>

### **Example 6: JSON round trip — stringify then parse**

- [x] stringify → parse returns a **new** object with the same enumerable JSON data.
- [x] It is not `===` the original object.
- [x] Dates become strings unless you use a reviver (Parse page).

Sandbox: `code_sandbox/json-intro/round-trip.html`

```html
const person = { name: "John", age: 30 };
const text = JSON.stringify(person);
const copy = JSON.parse(text);
```

<img alt="json-intro example 6 source" src="./code_sandbox/snaps/json-intro-06-code.png" />

<img alt="json-intro example 6 result" src="./code_sandbox/snaps/json-intro-06-result.png" />

- [x] **Outcome:** `copy.name` is **John**, and `copy === person` is **false**.

<a id="json-intro-example-07"></a>

### **Example 7: JSON files — customer.json**

- [x] JSON often lives in a **`.json` file** on a server.
- [x] The sample has id, name, city, and boolean **member**.
- [x] Load it later with `fetch` + `response.json()`.

Sandbox: `code_sandbox/json-intro/customer-file.html`

```html
{
  "id": 101,
  "name": "John Doe",
  "city": "New York",
  "member": true
}
```

<img alt="json-intro example 7 source" src="./code_sandbox/snaps/json-intro-07-code.png" />

<img alt="json-intro example 7 result" src="./code_sandbox/snaps/json-intro-07-result.png" />

- [x] **Outcome:** Parsed `customer.json` has **id 101**, name **John Doe**, **member true**.

<a id="json-intro-example-08"></a>

### **Example 8: JSON objects — firstName / lastName**

- [x] A JSON **object** is `{ "key": value, ... }`.
- [x] Keys are strings in double quotes.
- [x] This tiny object is one employee.

Sandbox: `code_sandbox/json-intro/json-object.html`

```html
{"firstName":"John", "lastName":"Doe"}
```

<img alt="json-intro example 8 source" src="./code_sandbox/snaps/json-intro-08-code.png" />

<img alt="json-intro example 8 result" src="./code_sandbox/snaps/json-intro-08-result.png" />

- [x] **Outcome:** Parse gives **John Doe**.

<a id="json-intro-example-09"></a>

### **Example 9: JSON arrays — employees**

- [x] A JSON **array** is `[ value, value, ... ]`.
- [x] Here the value of `employees` is an array of objects.
- [x] Index **1** is Anna Smith in the W3Schools sample.

Sandbox: `code_sandbox/json-intro/json-array.html`

```html
"employees":[
  {"firstName":"John", "lastName":"Doe"},
  {"firstName":"Anna", "lastName":"Smith"},
  {"firstName":"Peter", "lastName":"Jones"}
]
```

<img alt="json-intro example 9 source" src="./code_sandbox/snaps/json-intro-09-code.png" />

<img alt="json-intro example 9 result" src="./code_sandbox/snaps/json-intro-09-result.png" />

- [x] **Outcome:** `employees[1]` is **Anna Smith**.

<a id="json-intro-example-10"></a>

### **Example 10: JSON text built from concatenated strings**

- [x] Tutorials often build JSON with **string concatenation**.
- [x] That is easy to typo. Prefer a real `.json` file or `JSON.stringify`.
- [x] After concat, you still must **`JSON.parse`**.

Sandbox: `code_sandbox/json-intro/employees-text.html`

```html
let text = '{ "employees" : [' +
'{ "firstName":"John" , "lastName":"Doe" },' +
'{ "firstName":"Anna" , "lastName":"Smith" },' +
'{ "firstName":"Peter" , "lastName":"Jones" } ]}';
```

<img alt="json-intro example 10 source" src="./code_sandbox/snaps/json-intro-10-code.png" />

<img alt="json-intro example 10 result" src="./code_sandbox/snaps/json-intro-10-result.png" />

- [x] **Outcome:** `text` is a **string**; `JSON.parse(text)` succeeds and has **3** employees.

<a id="json-intro-example-11"></a>

### **Example 11: Display parsed employees[1] in HTML**

- [x] After parse, use **property access** like any JS object.
- [x] W3Schools writes `obj.employees[1].firstName` into `#demo`.
- [x] Index 1 is the **second** person (zero-based).

Sandbox: `code_sandbox/json-intro/display-anna.html`

```html
document.getElementById("demo").innerHTML =
  obj.employees[1].firstName + " " + obj.employees[1].lastName;
```

<img alt="json-intro example 11 source" src="./code_sandbox/snaps/json-intro-11-code.png" />

<img alt="json-intro example 11 result" src="./code_sandbox/snaps/json-intro-11-result.png" />

- [x] **Outcome:** The paragraph shows **Anna Smith**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/json-intro/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Is JSON a programming language?

<details>
<summary>Answer</summary>

- [x] **No** — it is a **text data** format.

</details>

### Question 2: Must JSON property names be quoted?

<details>
<summary>Answer</summary>

- [x] **Yes** — double quotes.

</details>

### Question 3: What does `JSON.parse` return?

<details>
<summary>Answer</summary>

- [x] A JavaScript **value** (object, array, string, number, boolean, or null).

</details>

### Question 4: What does `JSON.stringify` return?

<details>
<summary>Answer</summary>

- [x] A **string** of JSON text.

</details>

### Question 5: Who is `employees[1]` in the sample?

<details>
<summary>Answer</summary>

- [x] **Anna Smith**.

</details>

### Question 6: What is `typeof` of raw JSON text?

<details>
<summary>Answer</summary>

- [x] **string**.

</details>

### Question 7: Does stringify+parse keep the same object reference?

<details>
<summary>Answer</summary>

- [x] **No** — you get a **new** object.

</details>

### Question 8: What file extension is common?

<details>
<summary>Answer</summary>

- [x] **`.json`**.

</details>

### Question 9: Is JSON language-independent?

<details>
<summary>Answer</summary>

- [x] **Yes** — many languages parse it.

</details>

### Question 10: Can you use unquoted names in JSON?

<details>
<summary>Answer</summary>

- [x] **No** — that is only valid in **JavaScript** objects.

</details>


</details>

## Summary

Keep data as JSON text on the wire. Parse to use it, stringify to send or store it. Index 1 of the sample employees is Anna Smith.

## References

- [JSON Intro](https://www.w3schools.com/js/js_json.asp)
- [MDN JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

</details>
