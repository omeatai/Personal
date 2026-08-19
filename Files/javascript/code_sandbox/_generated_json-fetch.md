<details>
  <summary>JSON Fetch</summary>

## Introduction

Load JSON with `fetch` + `response.json()`. Check `ok`. POST with Content-Type application/json and a stringify body. Promise.all loads several files. XHR + JSON.parse is the older path. This sandbox uses local files; `/api/person` is mocked with result.json.

This section has **19** examples:

- [x] **Example 1:** A JSON file — customer.json [View](#json-fetch-example-01)
- [x] **Example 2:** Loading JSON with fetch + response.json() [View](#json-fetch-example-02)
- [x] **Example 3:** Loading a JSON array — products.json [View](#json-fetch-example-03)
- [x] **Example 4:** loadProducts — first name and price [View](#json-fetch-example-04)
- [x] **Example 5:** Checking response.ok and status [View](#json-fetch-example-05)
- [x] **Example 6:** Handling HTTP errors with throw [View](#json-fetch-example-06)
- [x] **Example 7:** Loading multiple JSON files with Promise.all [View](#json-fetch-example-07)
- [x] **Example 8:** Sending JSON — method, headers, body [View](#json-fetch-example-08)
- [x] **Example 9:** The Content-Type header [View](#json-fetch-example-09)
- [x] **Example 10:** The request body is JSON.stringify(person) [View](#json-fetch-example-10)
- [x] **Example 11:** Reading the server response as JSON [View](#json-fetch-example-11)
- [x] **Example 12:** Checking the POST response [View](#json-fetch-example-12)
- [x] **Example 13:** Complete sendPerson with try/catch [View](#json-fetch-example-13)
- [x] **Example 14:** Complete example — send name and age from inputs [View](#json-fetch-example-14)
- [x] **Example 15:** What response.json() can return [View](#json-fetch-example-15)
- [x] **Example 16:** Older pattern — stringify onto a query string [View](#json-fetch-example-16)
- [x] **Example 17:** Receiving data — JSON.parse a text payload [View](#json-fetch-example-17)
- [x] **Example 18:** JSON from a server with XMLHttpRequest [View](#json-fetch-example-18)
- [x] **Example 19:** Array as JSON via XHR [View](#json-fetch-example-19)

## Detailed Explanation

- [x] response.json() already parses.
- [x] 404 does not throw.
- [x] body must be a string.

<a id="json-fetch-example-01"></a>

### **Example 1: A JSON file — customer.json**

- [x] JSON on disk is just text with a **`.json`** name.
- [x] This file has id, name, city, member.

Sandbox: `code_sandbox/json-fetch/customer-file.html`

```javascript
{
  "id": 101,
  "name": "John Doe",
  "city": "New York",
  "member": true
}
```

<img alt="json-fetch example 1 source" src="./code_sandbox/snaps/json-fetch-01-code.png" />

<img alt="json-fetch example 1 result" src="./code_sandbox/snaps/json-fetch-01-result.png" />

- [x] **Outcome:** Fetched object: **John Doe** in **New York**.

<a id="json-fetch-example-02"></a>

### **Example 2: Loading JSON with fetch + response.json()**

- [x] `await fetch` then **`await response.json()`** — already parsed.
- [x] Do **not** `JSON.parse` the result of `.json()`.

Sandbox: `code_sandbox/json-fetch/load-json.html`

```javascript
async function loadJSON() {
  const response = await fetch("customer.json");
  const customer = await response.json();
  myDisplayer(customer.name);
}
loadJSON();
```

<img alt="json-fetch example 2 source" src="./code_sandbox/snaps/json-fetch-02-code.png" />

<img alt="json-fetch example 2 result" src="./code_sandbox/snaps/json-fetch-02-result.png" />

- [x] **Outcome:** Displayed name is **John Doe**.

<a id="json-fetch-example-03"></a>

### **Example 3: Loading a JSON array — products.json**

- [x] A file may be a **root array**.
- [x] `response.json()` then returns a JS array.

Sandbox: `code_sandbox/json-fetch/products-file.html`

```javascript
[
  {"name":"Laptop","price":899},
  {"name":"Mouse","price":29},
  {"name":"Keyboard","price":79}
]
```

<img alt="json-fetch example 3 source" src="./code_sandbox/snaps/json-fetch-03-code.png" />

<img alt="json-fetch example 3 result" src="./code_sandbox/snaps/json-fetch-03-result.png" />

- [x] **Outcome:** First product is **Laptop** at **899**.

<a id="json-fetch-example-04"></a>

### **Example 4: loadProducts — first name and price**

- [x] W3Schools displays `products[0].name` and `.price`.

Sandbox: `code_sandbox/json-fetch/load-products.html`

```javascript
const products = await response.json();
myDisplayer(products[0].name);
myDisplayer(products[0].price);
```

<img alt="json-fetch example 4 source" src="./code_sandbox/snaps/json-fetch-04-code.png" />

<img alt="json-fetch example 4 result" src="./code_sandbox/snaps/json-fetch-04-result.png" />

- [x] **Outcome:** **Laptop** and **899**.

<a id="json-fetch-example-05"></a>

### **Example 5: Checking response.ok and status**

- [x] Log `ok` and `status` before reading JSON.
- [x] 200 + true for a real file.

Sandbox: `code_sandbox/json-fetch/check-ok-status.html`

```javascript
myDisplayer(response.ok);
myDisplayer(response.status);
```

<img alt="json-fetch example 5 source" src="./code_sandbox/snaps/json-fetch-05-code.png" />

<img alt="json-fetch example 5 result" src="./code_sandbox/snaps/json-fetch-05-result.png" />

- [x] **Outcome:** **true** and **200**, then **John Doe**.

<a id="json-fetch-example-06"></a>

### **Example 6: Handling HTTP errors with throw**

- [x] If `!response.ok`, **throw** `HTTP error ` + status.
- [x] `catch` shows `err.message`.
- [x] Missing file → **HTTP error 404**.

Sandbox: `code_sandbox/json-fetch/http-error-throw.html`

```javascript
if (!response.ok) {
  throw new Error("HTTP error " + response.status);
}
```

<img alt="json-fetch example 6 source" src="./code_sandbox/snaps/json-fetch-06-code.png" />

<img alt="json-fetch example 6 result" src="./code_sandbox/snaps/json-fetch-06-result.png" />

- [x] **Outcome:** Fetching a missing file prints **HTTP error 404**.

<a id="json-fetch-example-07"></a>

### **Example 7: Loading multiple JSON files with Promise.all**

- [x] `Promise.all([fetch(...), ...])` waits for **all**.
- [x] Then `.json()` each response.
- [x] W3Schools typo “Custome name” is kept in spirit as customer name.

Sandbox: `code_sandbox/json-fetch/promise-all.html`

```javascript
const [customerResponse, productsResponse, newsResponse] = await Promise.all([
  fetch("customer.json"),
  fetch("products.json"),
  fetch("news.json")
]);
```

<img alt="json-fetch example 7 source" src="./code_sandbox/snaps/json-fetch-07-code.png" />

<img alt="json-fetch example 7 result" src="./code_sandbox/snaps/json-fetch-07-result.png" />

- [x] **Outcome:** Logs **John Doe**, **3 products**, **2 news items**.

<a id="json-fetch-example-08"></a>

### **Example 8: Sending JSON — method, headers, body**

- [x] POST options: **method**, **headers** `Content-Type: application/json`, **body** `JSON.stringify(person)`.
- [x] The live `/api/person` server is not in this sandbox. We still **build the same body** and read a local mock `result.json` for the reply shape.

Sandbox: `code_sandbox/json-fetch/post-options.html`

```javascript
const response = await fetch("/api/person", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(person)
});
```

<img alt="json-fetch example 8 source" src="./code_sandbox/snaps/json-fetch-08-code.png" />

<img alt="json-fetch example 8 result" src="./code_sandbox/snaps/json-fetch-08-result.png" />

- [x] **Outcome:** The stringified body is **`{"name":"John","age":30}`**. Mock response message is **Person saved**.

<a id="json-fetch-example-09"></a>

### **Example 9: The Content-Type header**

- [x] Servers expect **`application/json`** when the body is JSON.
- [x] Missing this header is a common API 400.

Sandbox: `code_sandbox/json-fetch/content-type.html`

```html
headers: { "Content-Type": "application/json" }
```

<img alt="json-fetch example 9 source" src="./code_sandbox/snaps/json-fetch-09-code.png" />

<img alt="json-fetch example 9 result" src="./code_sandbox/snaps/json-fetch-09-result.png" />

- [x] **Outcome:** The header value is **application/json**.

<a id="json-fetch-example-10"></a>

### **Example 10: The request body is JSON.stringify(person)**

- [x] `body` must be a **string** (or stream). Pass **`JSON.stringify(person)`**, not the object.

Sandbox: `code_sandbox/json-fetch/request-body.html`

```html
body: JSON.stringify(person)
```

<img alt="json-fetch example 10 source" src="./code_sandbox/snaps/json-fetch-10-code.png" />

<img alt="json-fetch example 10 result" src="./code_sandbox/snaps/json-fetch-10-result.png" />

- [x] **Outcome:** `typeof` of the body is **string**.

<a id="json-fetch-example-11"></a>

### **Example 11: Reading the server response as JSON**

- [x] After POST, `const result = await response.json()` then show `result.message`.
- [x] Sandbox reads **result.json** as that response.

Sandbox: `code_sandbox/json-fetch/read-server.html`

```javascript
const result = await response.json();
document.getElementById("demo").textContent = result.message;
```

<img alt="json-fetch example 11 source" src="./code_sandbox/snaps/json-fetch-11-code.png" />

<img alt="json-fetch example 11 result" src="./code_sandbox/snaps/json-fetch-11-result.png" />

- [x] **Outcome:** Message is **Person saved**.

<a id="json-fetch-example-12"></a>

### **Example 12: Checking the POST response**

- [x] Still check **`response.ok`** after POST.
- [x] Then parse JSON.

Sandbox: `code_sandbox/json-fetch/check-post-ok.html`

```javascript
if (!response.ok) {
  throw new Error("HTTP error " + response.status);
}
const result = await response.json();
```

<img alt="json-fetch example 12 source" src="./code_sandbox/snaps/json-fetch-12-code.png" />

<img alt="json-fetch example 12 result" src="./code_sandbox/snaps/json-fetch-12-result.png" />

- [x] **Outcome:** Mock GET of result.json is **ok**; message **Person saved**. A real POST would use the same check.

<a id="json-fetch-example-13"></a>

### **Example 13: Complete sendPerson with try/catch**

- [x] Full pattern: build object, fetch POST, check ok, read JSON, catch errors.
- [x] Sandbox still uses a static mock for the response.

Sandbox: `code_sandbox/json-fetch/complete-post.html`

```javascript
async function sendPerson() {
  const person = { name: "John", age: 30 };
  try {
    const response = await fetch("/api/person", { method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(person) });
    if (!response.ok) { throw new Error("HTTP error " + response.status); }
    const result = await response.json();
    document.getElementById("demo").textContent = result.message;
  } catch (error) {
    document.getElementById("demo").textContent = error.message;
  }
}
```

<img alt="json-fetch example 13 source" src="./code_sandbox/snaps/json-fetch-13-code.png" />

<img alt="json-fetch example 13 result" src="./code_sandbox/snaps/json-fetch-13-result.png" />

- [x] **Outcome:** Mock path prints **Person saved**. The **body** that would have been posted is shown too.

<a id="json-fetch-example-14"></a>

### **Example 14: Complete example — send name and age from inputs**

- [x] Read `#name` and `#age`, `Number(...)` the age, then the same POST pattern.
- [x] Inputs default to **John** / **30** like the page.

Sandbox: `code_sandbox/json-fetch/form-send.html`

```html
<input id="name" value="John">
<input id="age" type="number" value="30">
<button onclick="sendPerson()">Send</button>
```

<img alt="json-fetch example 14 source" src="./code_sandbox/snaps/json-fetch-14-code.png" />

<img alt="json-fetch example 14 result" src="./code_sandbox/snaps/json-fetch-14-result.png" />

- [x] **Outcome:** The built person is **John** / **30**; mock reply **Person saved**.

<a id="json-fetch-example-15"></a>

### **Example 15: What response.json() can return**

- [x] `.json()` already parses. Result may be object, array, string, number, boolean, or null.
- [x] Do **not** pass it to `JSON.parse` again.

Sandbox: `code_sandbox/json-fetch/json-method-types.html`

```javascript
The response.json() method already parses the JSON.
```

<img alt="json-fetch example 15 source" src="./code_sandbox/snaps/json-fetch-15-code.png" />

<img alt="json-fetch example 15 result" src="./code_sandbox/snaps/json-fetch-15-result.png" />

- [x] **Outcome:** customer.json → **object**; products.json → **array**.

<a id="json-fetch-example-16"></a>

### **Example 16: Older pattern — stringify onto a query string**

- [x] Older W3Schools snippet: `window.location = "demo_json.php?x=" + myJSON`.
- [x] That **navigates** the page. Prefer `fetch` POST.
- [x] We show the URL that would be built, without leaving.

Sandbox: `code_sandbox/json-fetch/query-string-send.html`

```html
const myJSON = JSON.stringify(myObj);
window.location = "demo_json.php?x=" + myJSON;
```

<img alt="json-fetch example 16 source" src="./code_sandbox/snaps/json-fetch-16-code.png" />

<img alt="json-fetch example 16 result" src="./code_sandbox/snaps/json-fetch-16-result.png" />

- [x] **Outcome:** The would-be URL contains **`x=`** and encoded/plain JSON with **John**.

<a id="json-fetch-example-17"></a>

### **Example 17: Receiving data — JSON.parse a text payload**

- [x] If you already have a JSON **string**, `JSON.parse` then `myObj.name`.

Sandbox: `code_sandbox/json-fetch/parse-received.html`

```html
const myObj = JSON.parse(myJSON);
document.getElementById("demo").innerHTML = myObj.name;
```

<img alt="json-fetch example 17 source" src="./code_sandbox/snaps/json-fetch-17-code.png" />

<img alt="json-fetch example 17 result" src="./code_sandbox/snaps/json-fetch-17-result.png" />

- [x] **Outcome:** **John**.

<a id="json-fetch-example-18"></a>

### **Example 18: JSON from a server with XMLHttpRequest**

- [x] Legacy: `XMLHttpRequest`, `onload`, `JSON.parse(this.responseText)`.
- [x] Prefer Fetch. This still works.
- [x] Sandbox GET `json_demo.txt`.

Sandbox: `code_sandbox/json-fetch/xhr-get.html`

```javascript
const xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  const myObj = JSON.parse(this.responseText);
  document.getElementById("demo").innerHTML = myObj.name;
};
xmlhttp.open("GET", "json_demo.txt");
xmlhttp.send();
```

<img alt="json-fetch example 18 source" src="./code_sandbox/snaps/json-fetch-18-code.png" />

<img alt="json-fetch example 18 result" src="./code_sandbox/snaps/json-fetch-18-result.png" />

- [x] **Outcome:** XHR parse shows **John Doe**.

<a id="json-fetch-example-19"></a>

### **Example 19: Array as JSON via XHR**

- [x] Parsing JSON that is an array yields a **JS array** (`myArr[0]`).
- [x] File `json_demo_array.txt` is `["Ford",...]`.

Sandbox: `code_sandbox/json-fetch/xhr-array.html`

```javascript
const myArr = JSON.parse(this.responseText);
document.getElementById("demo").innerHTML = myArr[0];
```

<img alt="json-fetch example 19 source" src="./code_sandbox/snaps/json-fetch-19-code.png" />

<img alt="json-fetch example 19 result" src="./code_sandbox/snaps/json-fetch-19-result.png" />

- [x] **Outcome:** **Ford**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/json-fetch/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you load a .json file?

<details>
<summary>Answer</summary>

- [x] `fetch(url)` then **`response.json()`**.

</details>

### Question 2: Should you `JSON.parse` the result of `.json()`?

<details>
<summary>Answer</summary>

- [x] **No** — it is already parsed.

</details>

### Question 3: What is `products[0].name` in the sample?

<details>
<summary>Answer</summary>

- [x] **Laptop**.

</details>

### Question 4: Does fetch throw on 404?

<details>
<summary>Answer</summary>

- [x] **No** — check **`ok`** and throw yourself.

</details>

### Question 5: How do you load three files together?

<details>
<summary>Answer</summary>

- [x] **`Promise.all([fetch...])`** then `.json()` each.

</details>

### Question 6: What Content-Type do you send with JSON?

<details>
<summary>Answer</summary>

- [x] **`application/json`**.

</details>

### Question 7: What do you pass as `body`?

<details>
<summary>Answer</summary>

- [x] **`JSON.stringify(object)`**, not the raw object.

</details>

### Question 8: What can `.json()` return?

<details>
<summary>Answer</summary>

- [x] Object, array, string, number, boolean, or **null**.

</details>

### Question 9: What is `myArr[0]` for the array file?

<details>
<summary>Answer</summary>

- [x] **Ford**.

</details>

### Question 10: Is XHR required?

<details>
<summary>Answer</summary>

- [x] **No** — Fetch is the modern API; XHR is the older example.

</details>


</details>

## Summary

fetch the resource, check ok, then json(). For POST, set the JSON content type and stringify the body. Do not JSON.parse the result of response.json().

## References

- [JSON Fetch](https://www.w3schools.com/js/js_json_server.asp)
- [MDN fetch()](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch)

</details>
