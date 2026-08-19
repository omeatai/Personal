<details>
  <summary>JSON HTML</summary>

## Introduction

Show JSON in the page with textContent, lists, tables, and nested property paths. Stringify (optionally pretty) when you need the raw text. Prefer DOM APIs over innerHTML for untrusted values. Missing fields can use `??`.

This section has **18** examples:

- [x] **Example 1:** Displaying a property [View](#json-html-example-01)
- [x] **Example 2:** Displaying multiple properties [View](#json-html-example-02)
- [x] **Example 3:** Displaying an object without stringify [View](#json-html-example-03)
- [x] **Example 4:** Display an object via JSON.stringify [View](#json-html-example-04)
- [x] **Example 5:** Formatting JSON text in a <pre> [View](#json-html-example-05)
- [x] **Example 6:** Displaying a JSON array index [View](#json-html-example-06)
- [x] **Example 7:** Displaying all array values [View](#json-html-example-07)
- [x] **Example 8:** Displaying an array as a list [View](#json-html-example-08)
- [x] **Example 9:** Displaying an array of objects [View](#json-html-example-09)
- [x] **Example 10:** Displaying JSON in a table [View](#json-html-example-10)
- [x] **Example 11:** Displaying nested JSON [View](#json-html-example-11)
- [x] **Example 12:** Loading and displaying JSON [View](#json-html-example-12)
- [x] **Example 13:** Prefer textContent for untrusted data [View](#json-html-example-13)
- [x] **Example 14:** innerHTML is potentially unsafe [View](#json-html-example-14)
- [x] **Example 15:** Missing properties — nullish coalescing [View](#json-html-example-15)
- [x] **Example 16:** HTML table from JSON (local data stand-in for PHP) [View](#json-html-example-16)
- [x] **Example 17:** Dynamic table from a <select> [View](#json-html-example-17)
- [x] **Example 18:** HTML drop-down from JSON names [View](#json-html-example-18)

## Detailed Explanation

- [x] textContent over innerHTML for data.
- [x] createElement / insertRow.
- [x] `[object Object]` means you forgot stringify.

<a id="json-html-example-01"></a>

### **Example 1: Displaying a property**

- [x] Parse, then `textContent = person.name`.

Sandbox: `code_sandbox/json-html/one-prop.html`

```html
document.getElementById("demo").textContent = person.name;
```

<img alt="json-html example 1 source" src="./code_sandbox/snaps/json-html-01-code.png" />

<img alt="json-html example 1 result" src="./code_sandbox/snaps/json-html-01-result.png" />

- [x] **Outcome:** The node shows **John**.

<a id="json-html-example-02"></a>

### **Example 2: Displaying multiple properties**

- [x] Concatenate name, age, city with commas.

Sandbox: `code_sandbox/json-html/multi-prop.html`

```html
person.name + ", " + person.age + ", " + person.city
```

<img alt="json-html example 2 source" src="./code_sandbox/snaps/json-html-02-code.png" />

<img alt="json-html example 2 result" src="./code_sandbox/snaps/json-html-02-result.png" />

- [x] **Outcome:** **John, 30, New York**.

<a id="json-html-example-03"></a>

### **Example 3: Displaying an object without stringify**

- [x] `myDisplayer(person)` becomes **`[object Object]`**.
- [x] That is `ToString` on a plain object — not useful.

Sandbox: `code_sandbox/json-html/object-default.html`

```html
const person = {name: "John", age: 30};
myDisplayer(person);
```

<img alt="json-html example 3 source" src="./code_sandbox/snaps/json-html-03-code.png" />

<img alt="json-html example 3 result" src="./code_sandbox/snaps/json-html-03-result.png" />

- [x] **Outcome:** The output is **[object Object]**.

<a id="json-html-example-04"></a>

### **Example 4: Display an object via JSON.stringify**

- [x] Stringify first so humans can read the keys.

Sandbox: `code_sandbox/json-html/stringify-display.html`

```html
let text = JSON.stringify(person);
myDisplayer(text);
```

<img alt="json-html example 4 source" src="./code_sandbox/snaps/json-html-04-code.png" />

<img alt="json-html example 4 result" src="./code_sandbox/snaps/json-html-04-result.png" />

- [x] **Outcome:** JSON text with **John** and **30** is shown.

<a id="json-html-example-05"></a>

### **Example 5: Formatting JSON text in a <pre>**

- [x] `JSON.stringify(person, null, 2)` plus **`<pre>`** keeps indentation.

Sandbox: `code_sandbox/json-html/pretty.html`

```html
document.getElementById("demo").textContent =
  JSON.stringify(person, null, 2);
```

<img alt="json-html example 5 source" src="./code_sandbox/snaps/json-html-05-code.png" />

<img alt="json-html example 5 result" src="./code_sandbox/snaps/json-html-05-result.png" />

- [x] **Outcome:** Multi-line JSON with **2**-space indent is in the output.

<a id="json-html-example-06"></a>

### **Example 6: Displaying a JSON array index**

- [x] `cars[0]` after parse.

Sandbox: `code_sandbox/json-html/array-index.html`

```html
document.getElementById("demo").textContent = cars[0];
```

<img alt="json-html example 6 source" src="./code_sandbox/snaps/json-html-06-code.png" />

<img alt="json-html example 6 result" src="./code_sandbox/snaps/json-html-06-result.png" />

- [x] **Outcome:** **Ford**.

<a id="json-html-example-07"></a>

### **Example 7: Displaying all array values**

- [x] Loop `for (const car of cars)` and join with newlines.

Sandbox: `code_sandbox/json-html/array-loop.html`

```html
for (const car of cars) { output += car + "\n"; }
```

<img alt="json-html example 7 source" src="./code_sandbox/snaps/json-html-07-code.png" />

<img alt="json-html example 7 result" src="./code_sandbox/snaps/json-html-07-result.png" />

- [x] **Outcome:** Three lines: **Ford**, **Volvo**, **BMW**.

<a id="json-html-example-08"></a>

### **Example 8: Displaying an array as a list**

- [x] `createElement("li")`, `textContent`, `appendChild` — **safer** than innerHTML.

Sandbox: `code_sandbox/json-html/array-ul.html`

```html
const item = document.createElement("li");
item.textContent = car;
list.appendChild(item);
```

<img alt="json-html example 8 source" src="./code_sandbox/snaps/json-html-08-code.png" />

<img alt="json-html example 8 result" src="./code_sandbox/snaps/json-html-08-result.png" />

- [x] **Outcome:** The `<ul>` has **3** `<li>` nodes (Ford, Volvo, BMW).

<a id="json-html-example-09"></a>

### **Example 9: Displaying an array of objects**

- [x] Each product: `name + ": $" + price` in an `<li>`.

Sandbox: `code_sandbox/json-html/products-list.html`

```html
item.textContent = product.name + ": $" + product.price;
```

<img alt="json-html example 9 source" src="./code_sandbox/snaps/json-html-09-code.png" />

<img alt="json-html example 9 result" src="./code_sandbox/snaps/json-html-09-result.png" />

- [x] **Outcome:** List includes **Laptop: $899**.

<a id="json-html-example-10"></a>

### **Example 10: Displaying JSON in a table**

- [x] `insertRow` / `insertCell` / `textContent` — no HTML concatenation.

Sandbox: `code_sandbox/json-html/table.html`

```html
const row = table.insertRow();
nameCell.textContent = product.name;
priceCell.textContent = "$" + product.price;
```

<img alt="json-html example 10 source" src="./code_sandbox/snaps/json-html-10-code.png" />

<img alt="json-html example 10 result" src="./code_sandbox/snaps/json-html-10-result.png" />

- [x] **Outcome:** The table has a header plus **3** data rows; first name **Laptop**.

<a id="json-html-example-11"></a>

### **Example 11: Displaying nested JSON**

- [x] `person.address.city` after parse.

Sandbox: `code_sandbox/json-html/nested-city.html`

```html
person.address.city
```

<img alt="json-html example 11 source" src="./code_sandbox/snaps/json-html-11-code.png" />

<img alt="json-html example 11 result" src="./code_sandbox/snaps/json-html-11-result.png" />

- [x] **Outcome:** **New York**.

<a id="json-html-example-12"></a>

### **Example 12: Loading and displaying JSON**

- [x] fetch customer.json, check ok, show `name + ", " + city`.

Sandbox: `code_sandbox/json-html/load-display.html`

```html
document.getElementById("demo").textContent =
  customer.name + ", " + customer.city;
```

<img alt="json-html example 12 source" src="./code_sandbox/snaps/json-html-12-code.png" />

<img alt="json-html example 12 result" src="./code_sandbox/snaps/json-html-12-result.png" />

- [x] **Outcome:** **John Doe, New York**.

<a id="json-html-example-13"></a>

### **Example 13: Prefer textContent for untrusted data**

- [x] **Safer:** `element.textContent = customer.name`.
- [x] Values might contain HTML/script if you used innerHTML.

Sandbox: `code_sandbox/json-html/textcontent-safe.html`

```html
element.textContent = customer.name;
```

<img alt="json-html example 13 source" src="./code_sandbox/snaps/json-html-13-code.png" />

<img alt="json-html example 13 result" src="./code_sandbox/snaps/json-html-13-result.png" />

- [x] **Outcome:** `textContent` shows the name as **plain text** even if it contains `<` characters.

<a id="json-html-example-14"></a>

### **Example 14: innerHTML is potentially unsafe**

- [x] `innerHTML = customer.name` would **parse HTML**.
- [x] Only use it for HTML **your app** built, not API strings.

Sandbox: `code_sandbox/json-html/innerhtml-unsafe.html`

```html
element.innerHTML = customer.name;
```

<img alt="json-html example 14 source" src="./code_sandbox/snaps/json-html-14-code.png" />

<img alt="json-html example 14 result" src="./code_sandbox/snaps/json-html-14-result.png" />

- [x] **Outcome:** Setting innerHTML to `John <b>Doe</b>` creates a **`<b>`** element (`childElementCount` 1).

<a id="json-html-example-15"></a>

### **Example 15: Missing properties — nullish coalescing**

- [x] `person.city ?? "Unknown city"` when city is missing.

Sandbox: `code_sandbox/json-html/missing.html`

```html
person.city ?? "Unknown city" 
```

<img alt="json-html example 15 source" src="./code_sandbox/snaps/json-html-15-code.png" />

<img alt="json-html example 15 result" src="./code_sandbox/snaps/json-html-15-result.png" />

- [x] **Outcome:** With only `name`, the output is **Unknown city**.

<a id="json-html-example-16"></a>

### **Example 16: HTML table from JSON (local data stand-in for PHP)**

- [x] The page POSTs to `json_demo_html_table.php`. This sandbox builds the **same table** from a local array so the HTML pattern runs.
- [x] Prefer `textContent` in cells over string-built HTML.

Sandbox: `code_sandbox/json-html/html-table-xhr.html`

```html
let text = "<table border='1'>";
for (let x in myObj) {
  text += "<tr><td>" + myObj[x].name + "</td></tr>";
}
```

<img alt="json-html example 16 source" src="./code_sandbox/snaps/json-html-16-code.png" />

<img alt="json-html example 16 result" src="./code_sandbox/snaps/json-html-16-result.png" />

- [x] **Outcome:** A table of names includes **John** (and the other sample rows).

<a id="json-html-example-17"></a>

### **Example 17: Dynamic table from a <select>**

- [x] Changing the select would POST `{table, limit}` in the original.
- [x] Here, choosing **products** fills names from a local map — same UI idea.

Sandbox: `code_sandbox/json-html/dropdown-filter.html`

```html
<select id="myselect" onchange="change_myselect(this.value)">
```

<img alt="json-html example 17 source" src="./code_sandbox/snaps/json-html-17-code.png" />

<img alt="json-html example 17 result" src="./code_sandbox/snaps/json-html-17-result.png" />

- [x] **Outcome:** After selecting **products**, the table lists **Laptop**, **Mouse**, **Keyboard**.

<a id="json-html-example-18"></a>

### **Example 18: HTML drop-down from JSON names**

- [x] Build `<option>` from each `myObj[x].name`.
- [x] Use `new Option(text)` instead of innerHTML when you can.

Sandbox: `code_sandbox/json-html/select-options.html`

```html
text += "<option>" + myObj[x].name + "</option>";
```

<img alt="json-html example 18 source" src="./code_sandbox/snaps/json-html-18-code.png" />

<img alt="json-html example 18 result" src="./code_sandbox/snaps/json-html-18-result.png" />

- [x] **Outcome:** The select has **3** options: John, Anna, Peter.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/json-html/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you show one property?

<details>
<summary>Answer</summary>

- [x] Set **`textContent`** to `person.name`.

</details>

### Question 2: Why does logging an object show `[object Object]`?

<details>
<summary>Answer</summary>

- [x] Plain objects stringify via **ToString**, not JSON.

</details>

### Question 3: How do you pretty-print in the page?

<details>
<summary>Answer</summary>

- [x] **`JSON.stringify(obj, null, 2)`** inside a `<pre>`.

</details>

### Question 4: Safer than innerHTML for names?

<details>
<summary>Answer</summary>

- [x] **`textContent`** (or `createElement`).

</details>

### Question 5: What does `??` help with?

<details>
<summary>Answer</summary>

- [x] **Missing** properties — provide a fallback.

</details>

### Question 6: First product in the list example?

<details>
<summary>Answer</summary>

- [x] **Laptop: $899**.

</details>

### Question 7: Nested city path?

<details>
<summary>Answer</summary>

- [x] **`person.address.city`**.

</details>

### Question 8: Why not innerHTML for API strings?

<details>
<summary>Answer</summary>

- [x] They might contain **HTML/script**.

</details>

### Question 9: How many `<li>` for the three cars?

<details>
<summary>Answer</summary>

- [x] **3**.

</details>

### Question 10: How do you add a table row in the DOM?

<details>
<summary>Answer</summary>

- [x] **`insertRow` / `insertCell`** then `textContent`.

</details>


</details>

## Summary

Parse, then put values in the DOM with textContent or created nodes. Pretty-print with stringify(null, 2). Never innerHTML untrusted JSON strings.

## References

- [JSON HTML](https://www.w3schools.com/js/js_json_html.asp)
- [MDN JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

</details>
