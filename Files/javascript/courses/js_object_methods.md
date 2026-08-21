# JS Object Methods

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Methods are actions stored as functions on an object. Call them with parentheses. Skip the parentheses and you get the function itself. Inside a method, this is the owner object. You can add a method later by assigning a function to a property, and the method body can call other functions such as toUpperCase.

This section has **6** examples:

- [x] **Example 1:** person with fullName method [View](#js-object-methods-example-01)
- [x] **Example 2:** getId using this.id [View](#js-object-methods-example-02)
- [x] **Example 3:** person.fullName() call [View](#js-object-methods-example-03)
- [x] **Example 4:** person.fullName without () [View](#js-object-methods-example-04)
- [x] **Example 5:** Add method: person.name = function () {...} [View](#js-object-methods-example-05)
- [x] **Example 6:** toUpperCase inside a method [View](#js-object-methods-example-06)

## Detailed Explanation

- [x] A method is a **function stored as a property**. Call it with **`()`**.
- [x] Without `()` you get the **function object** (its source text if you stringify it).
- [x] In a method, **`this`** is the owner — `this.id`, `this.firstName`, `this.lastName`.
- [x] Add a method with `object.fn = function () { ... }`. The page’s second fullName Tryit is the same object as the first — shown once.

<a id="js-object-methods-example-01"></a>

### **Example 1: person with fullName method**

- [x] Methods are **functions stored as property values**.
- [x] The page repeats this same `fullName` object later as Example 2 under The this Keyword — shown once here.

Sandbox: `code_sandbox/js-object-methods/person-fullname.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  fullName: function () {
    return this.firstName + " " + this.lastName;
  },
};
```

![js-object-methods example 1 source](../code_sandbox/snaps/js-object-methods-01-code.png)

![js-object-methods example 1 result](../code_sandbox/snaps/js-object-methods-01-result.png)

- [x] **Outcome:** person.fullName() is **"John Doe"**.

<a id="js-object-methods-example-02"></a>

### **Example 2: getId using this.id**

- [x] In the method, **`this`** is `person`.
- [x] `this.id` means the `id` property of that object.

Sandbox: `code_sandbox/js-object-methods/getid-this.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,
  getId: function () {
    return this.id;
  },
};
let number = person.getId();
```

![js-object-methods example 2 source](../code_sandbox/snaps/js-object-methods-02-code.png)

![js-object-methods example 2 result](../code_sandbox/snaps/js-object-methods-02-result.png)

- [x] **Outcome:** number is **5566**.

<a id="js-object-methods-example-03"></a>

### **Example 3: person.fullName() call**

- [x] Call a method with **parentheses**: `objectName.methodName()`.
- [x] Parentheses **execute** the function.

Sandbox: `code_sandbox/js-object-methods/call-with-parens.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  fullName: function () {
    return this.firstName + " " + this.lastName;
  },
};
let name = person.fullName();
```

![js-object-methods example 3 source](../code_sandbox/snaps/js-object-methods-03-code.png)

![js-object-methods example 3 result](../code_sandbox/snaps/js-object-methods-03-result.png)

- [x] **Outcome:** name is **"John Doe"**.

<a id="js-object-methods-example-04"></a>

### **Example 4: person.fullName without ()**

- [x] Without `()` you get the **function itself**, not the return value.
- [x] `String(person.fullName)` shows the function text.

Sandbox: `code_sandbox/js-object-methods/without-parens.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  fullName: function () {
    return this.firstName + " " + this.lastName;
  },
};
let name = person.fullName;
```

![js-object-methods example 4 source](../code_sandbox/snaps/js-object-methods-04-code.png)

![js-object-methods example 4 result](../code_sandbox/snaps/js-object-methods-04-result.png)

- [x] **Outcome:** `typeof name` is **"function"**. The string form is the function source, not **"John Doe"**.

<a id="js-object-methods-example-05"></a>

### **Example 5: Add method: person.name = function () {...}**

- [x] Assign a function to a property to **add a method**.
- [x] `person.name` then behaves like any other method.

Sandbox: `code_sandbox/js-object-methods/add-method.html`

```javascript
const person = { firstName: "John", lastName: "Doe", age: 50 };
person.name = function () {
  return this.firstName + " " + this.lastName;
};
```

![js-object-methods example 5 source](../code_sandbox/snaps/js-object-methods-05-code.png)

![js-object-methods example 5 result](../code_sandbox/snaps/js-object-methods-05-result.png)

- [x] **Outcome:** person.name() is **"John Doe"**.

<a id="js-object-methods-example-06"></a>

### **Example 6: toUpperCase inside a method**

- [x] A method body can call **other** methods, such as `toUpperCase()`.
- [x] The full name is built, then converted to uppercase.

Sandbox: `code_sandbox/js-object-methods/touppercase-method.html`

```javascript
const person = { firstName: "John", lastName: "Doe" };
person.name = function () {
  return (this.firstName + " " + this.lastName).toUpperCase();
};
```

![js-object-methods example 6 source](../code_sandbox/snaps/js-object-methods-06-code.png)

![js-object-methods example 6 result](../code_sandbox/snaps/js-object-methods-06-result.png)

- [x] **Outcome:** person.name() is **"JOHN DOE"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-object-methods/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `person.fullName()`?

<details>
<summary>Answer</summary>

- [x] **"John Doe"**.

</details>

### Question 2: What is `person.getId()` if `id` is 5566?

<details>
<summary>Answer</summary>

- [x] **5566** — `this.id` is `person.id`.

</details>

### Question 3: What does `this` refer to in an object method?

<details>
<summary>Answer</summary>

- [x] The **object** that owns the method.

</details>

### Question 4: What is `let name = person.fullName()`?

<details>
<summary>Answer</summary>

- [x] **"John Doe"** — parentheses execute the method.

</details>

### Question 5: What is `let name = person.fullName` (no parentheses)?

<details>
<summary>Answer</summary>

- [x] The **function itself**.
- [x] `typeof name` is **"function"**, not the string John Doe.

</details>

### Question 6: How do you add a method to an existing object?

<details>
<summary>Answer</summary>

- [x] Assign a function: `person.name = function () { ... }`.

</details>

### Question 7: What is `person.name()` if the method uses `toUpperCase()`?

<details>
<summary>Answer</summary>

- [x] **"JOHN DOE"**.

</details>

### Question 8: Are methods different from properties?

<details>
<summary>Answer</summary>

- [x] Methods **are** properties whose values are **functions**.

</details>

### Question 9: Does the page show fullName twice?

<details>
<summary>Answer</summary>

- [x] **Yes.** The first Tryit and Example 2 under this are the same object — this section keeps one demo.

</details>

### Question 10: What is the call syntax?

<details>
<summary>Answer</summary>

- [x] **`objectName.methodName()`**.

</details>

</details>

## Summary

Store functions as properties and call them with parentheses. this is the owner object. Without parentheses you get the function, not the result. You can add methods later, including ones that call toUpperCase.

## References

- [JS Object Methods (W3Schools)](https://www.w3schools.com/js/js_object_methods.asp)
- [MDN: Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
- [MDN: this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
- [MDN: String.prototype.toUpperCase](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)
