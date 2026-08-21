# JS Object Display

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

If you treat an object as a string you get [object Object]. To show the contents, name the properties, loop with for..in using bracket access, convert values with Object.values, loop pairs with Object.entries, or serialize with JSON.stringify.

This section has **6** examples:

- [x] **Example 1:** let text = person → [object Object] [View](#js-object-display-example-01)
- [x] **Example 2:** person.name + age + city [View](#js-object-display-example-02)
- [x] **Example 3:** for..in loop: person[x] (not person.x) [View](#js-object-display-example-03)
- [x] **Example 4:** Object.values(person).toString() [View](#js-object-display-example-04)
- [x] **Example 5:** Object.entries fruits loop [View](#js-object-display-example-05)
- [x] **Example 6:** JSON.stringify(person) [View](#js-object-display-example-06)

## Detailed Explanation

- [x] `String(person)` is **[object Object]** — the default `toString`.
- [x] Name properties (`person.name`), or loop **`person[x]`** (not `person.x`).
- [x] `Object.values` → array of values. `Object.entries` → `[key, value]` pairs.
- [x] `JSON.stringify(person)` is a **JSON** string. Methods are not included.

<a id="js-object-display-example-01"></a>

### **Example 1: let text = person → [object Object]**

- [x] Displaying an object as a string yields **[object Object]**.
- [x] That is JavaScript’s default `toString` for a plain object.

Sandbox: `code_sandbox/js-object-display/object-object.html`

```javascript
const person = { name: "John", age: 30, city: "New York" };
let text = person;
```

![js-object-display example 1 source](../code_sandbox/snaps/js-object-display-01-code.png)

![js-object-display example 1 result](../code_sandbox/snaps/js-object-display-01-result.png)

- [x] **Outcome:** String(text) is **[object Object]**.

<a id="js-object-display-example-02"></a>

### **Example 2: person.name + age + city**

- [x] Build a string from **named** properties.
- [x] You pick each key yourself.

Sandbox: `code_sandbox/js-object-display/named-properties.html`

```javascript
const person = { name: "John", age: 30, city: "New York" };
let text = person.name + "," + person.age + "," + person.city;
```

![js-object-display example 2 source](../code_sandbox/snaps/js-object-display-02-code.png)

![js-object-display example 2 result](../code_sandbox/snaps/js-object-display-02-result.png)

- [x] **Outcome:** text is **"John,30,New York"**.

<a id="js-object-display-example-03"></a>

### **Example 3: for..in loop: person[x] (not person.x)**

- [x] `for (let x in person)` walks **keys**. You must use **`person[x]`**.
- [x] `person.x` looks up a property literally named `x` — it is **undefined** each time. Clarifying row shows that mistake.

Sandbox: `code_sandbox/js-object-display/for-in-loop.html`

```javascript
const person = { name: "John", age: 30, city: "New York" };
let text = "";
for (let x in person) {
  text += person[x] + " ";
}
let wrong = "";
for (let x in person) {
  wrong += person.x + " ";
}
```

![js-object-display example 3 source](../code_sandbox/snaps/js-object-display-03-code.png)

![js-object-display example 3 result](../code_sandbox/snaps/js-object-display-03-result.png)

- [x] **Outcome:** Correct loop: **"John 30 New York "**. `person.x` yields **"undefined undefined undefined "**.

<a id="js-object-display-example-04"></a>

### **Example 4: Object.values(person).toString()**

- [x] `Object.values(person)` is an **array** of the values.
- [x] `.toString()` joins them with commas.

Sandbox: `code_sandbox/js-object-display/object-values.html`

```javascript
const person = { name: "John", age: 30, city: "New York" };
const myArray = Object.values(person);
let text = myArray.toString();
```

![js-object-display example 4 source](../code_sandbox/snaps/js-object-display-04-code.png)

![js-object-display example 4 result](../code_sandbox/snaps/js-object-display-04-result.png)

- [x] **Outcome:** myArray is **["John",30,"New York"]**. text is **"John,30,New York"**.

<a id="js-object-display-example-05"></a>

### **Example 5: Object.entries fruits loop**

- [x] `Object.entries(fruits)` gives `[key, value]` pairs.
- [x] Destructure as `for (let [fruit, value] of ...)`.

Sandbox: `code_sandbox/js-object-display/object-entries.html`

```javascript
const fruits = { Bananas: 300, Oranges: 200, Apples: 500 };
let text = "";
for (let [fruit, value] of Object.entries(fruits)) {
  text += fruit + ": " + value + " ";
}
```

![js-object-display example 5 source](../code_sandbox/snaps/js-object-display-05-code.png)

![js-object-display example 5 result](../code_sandbox/snaps/js-object-display-05-result.png)

- [x] **Outcome:** text is **"Bananas: 300 Oranges: 200 Apples: 500 "**.

<a id="js-object-display-example-06"></a>

### **Example 6: JSON.stringify(person)**

- [x] `JSON.stringify` turns the object into a **JSON string**.
- [x] Functions are omitted; this person has only data properties.

Sandbox: `code_sandbox/js-object-display/json-stringify.html`

```javascript
const person = { name: "John", age: 30, city: "New York" };
let text = JSON.stringify(person);
```

![js-object-display example 6 source](../code_sandbox/snaps/js-object-display-06-code.png)

![js-object-display example 6 result](../code_sandbox/snaps/js-object-display-06-result.png)

- [x] **Outcome:** text is **{"name":"John","age":30,"city":"New York"}**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-object-display/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `let text = person` as a string?

<details>
<summary>Answer</summary>

- [x] **[object Object]**.

</details>

### Question 2: What is `person.name + "," + person.age + "," + person.city`?

<details>
<summary>Answer</summary>

- [x] **"John,30,New York"**.

</details>

### Question 3: In `for (let x in person)`, should you use `person.x` or `person[x]`?

<details>
<summary>Answer</summary>

- [x] **`person[x]`**.
- [x] `person.x` looks up a key named `x` and is **undefined**.

</details>

### Question 4: What is `Object.values(person).toString()`?

<details>
<summary>Answer</summary>

- [x] **"John,30,New York"**.

</details>

### Question 5: What does the fruits `Object.entries` loop build?

<details>
<summary>Answer</summary>

- [x] **"Bananas: 300 Oranges: 200 Apples: 500 "**.

</details>

### Question 6: What is `JSON.stringify(person)` for name/age/city?

<details>
<summary>Answer</summary>

- [x] **{"name":"John","age":30,"city":"New York"}**.

</details>

### Question 7: Why do you see [object Object]?

<details>
<summary>Answer</summary>

- [x] The object was coerced to a string, and the default `toString` does not list keys.

</details>

### Question 8: Does JSON.stringify include methods?

<details>
<summary>Answer</summary>

- [x] **No.** Function properties are omitted.

</details>

### Question 9: What does Object.values return?

<details>
<summary>Answer</summary>

- [x] An **array** of the object’s own enumerable **values**.

</details>

### Question 10: What does Object.entries return?

<details>
<summary>Answer</summary>

- [x] An array of **`[key, value]`** pairs, handy in `for...of`.

</details>

</details>

## Summary

Do not stringify an object directly unless you want [object Object]. Name the keys, loop with person[x], use Object.values or Object.entries, or call JSON.stringify.

## References

- [JS Display Objects (W3Schools)](https://www.w3schools.com/js/js_object_display.asp)
- [MDN: JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
- [MDN: Object.values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values)
- [MDN: Object.entries](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries)
- [MDN: for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
