# JS Object Intro

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Objects are variables that store values as properties and functions as methods. The usual way to create one is an object literal: curly braces with key:value pairs. You can write that literal on one line or many, start empty and add keys, or (unnecessarily) use new Object(). Read keys with dots or brackets. Methods use this to reach the owner object. Almost everything except primitives is an object.

This section has **9** examples:

- [x] **Example 1:** const car = { type, model, color } [View](#js-object-intro-example-01)
- [x] **Example 2:** Example 1: person object on one line [View](#js-object-intro-example-02)
- [x] **Example 3:** Example 2: person object multiline [View](#js-object-intro-example-03)
- [x] **Example 4:** Example 3: empty object then add properties [View](#js-object-intro-example-04)
- [x] **Example 5:** Example 4: new Object({...}) [View](#js-object-intro-example-05)
- [x] **Example 6:** Dot notation: person.firstName [View](#js-object-intro-example-06)
- [x] **Example 7:** Bracket notation: person["firstName"] [View](#js-object-intro-example-07)
- [x] **Example 8:** Method fullName with this [View](#js-object-intro-example-08)
- [x] **Example 9:** Objects are king — typeof primitives vs objects [View](#js-object-intro-example-09)

## Detailed Explanation

- [x] An object literal is `{ key: value, ... }` inside curly braces. Prefer **`const`** and prefer literals over **`new Object()`**.
- [x] **Dot** `person.firstName` and **bracket** `person["firstName"]` read the same property.
- [x] A **method** is a function property. Inside it, **`this`** is the object.
- [x] Seven **primitives** are not objects (except the `typeof null === "object"` quirk). Dates, arrays, maps, sets, regexp, errors, and Math are objects; functions have typeof **function**.

<a id="js-object-intro-example-01"></a>

### **Example 1: const car = { type, model, color }**

- [x] `type`, `model`, and `color` are **properties**.
- [x] `"Fiat"`, `"500"`, and `"white"` are the **property values**.

Sandbox: `code_sandbox/js-object-intro/car-literal.html`

```javascript
const car = { type: "Fiat", model: "500", color: "white" };
```

![js-object-intro example 1 source](../code_sandbox/snaps/js-object-intro-01-code.png)

![js-object-intro example 1 result](../code_sandbox/snaps/js-object-intro-01-result.png)

- [x] **Outcome:** car is a Fiat **500** that is **white**.

<a id="js-object-intro-example-02"></a>

### **Example 2: Example 1: person object on one line**

- [x] An **object literal** is curly braces with `key: value` pairs.
- [x] The page also shows the same `{firstName:"John", ...}` literal without a variable — this Example is that object assigned to `person`.

Sandbox: `code_sandbox/js-object-intro/person-one-line.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue",
};
```

![js-object-intro example 2 source](../code_sandbox/snaps/js-object-intro-02-code.png)

![js-object-intro example 2 result](../code_sandbox/snaps/js-object-intro-02-result.png)

- [x] **Outcome:** person is **John Doe**, age **50**, eyeColor **blue**.

<a id="js-object-intro-example-03"></a>

### **Example 3: Example 2: person object multiline**

- [x] Spaces and line breaks do **not** change the object.
- [x] The same literal as Example 1, written across several lines.

Sandbox: `code_sandbox/js-object-intro/person-multiline.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue",
};
```

![js-object-intro example 3 source](../code_sandbox/snaps/js-object-intro-03-code.png)

![js-object-intro example 3 result](../code_sandbox/snaps/js-object-intro-03-result.png)

- [x] **Outcome:** Same object as Example 1: **John**, **50**, **blue**.

<a id="js-object-intro-example-04"></a>

### **Example 4: Example 3: empty object then add properties**

- [x] You can start with `{}` and **assign** properties afterward.
- [x] Declare objects with **`const`** — the binding stays, the contents can change.

Sandbox: `code_sandbox/js-object-intro/empty-then-add.html`

```javascript
const person = {};
person.firstName = "John";
person.lastName = "Doe";
person.age = 50;
person.eyeColor = "blue";
```

![js-object-intro example 4 source](../code_sandbox/snaps/js-object-intro-04-code.png)

![js-object-intro example 4 result](../code_sandbox/snaps/js-object-intro-04-result.png)

- [x] **Outcome:** After adding keys, person is again **John Doe**, **50**, **blue**.

<a id="js-object-intro-example-05"></a>

### **Example 5: Example 4: new Object({...})**

- [x] `new Object({...})` can wrap a literal, but you **do not need** `new Object()`.
- [x] For readability, simplicity, and speed, **prefer an object literal** `{}`.

Sandbox: `code_sandbox/js-object-intro/new-object.html`

```javascript
const person = new Object({
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue",
});
```

![js-object-intro example 5 source](../code_sandbox/snaps/js-object-intro-05-code.png)

![js-object-intro example 5 result](../code_sandbox/snaps/js-object-intro-05-result.png)

- [x] **Outcome:** Works, and `instanceof Object` is **true** — but a literal is the usual choice.

<a id="js-object-intro-example-06"></a>

### **Example 6: Dot notation: person.firstName**

- [x] Read a property with **`objectName.propertyName`**.
- [x] `person.firstName` is the value of the `firstName` key.

Sandbox: `code_sandbox/js-object-intro/dot-notation.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue",
};
let name = person.firstName;
```

![js-object-intro example 6 source](../code_sandbox/snaps/js-object-intro-06-code.png)

![js-object-intro example 6 result](../code_sandbox/snaps/js-object-intro-06-result.png)

- [x] **Outcome:** name is **"John"**.

<a id="js-object-intro-example-07"></a>

### **Example 7: Bracket notation: person["firstName"]**

- [x] The other way is **`objectName["propertyName"]`**.
- [x] Brackets are required when the key is in a **variable** or is not a valid identifier.

Sandbox: `code_sandbox/js-object-intro/bracket-notation.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue",
};
let name = person["firstName"];
```

![js-object-intro example 7 source](../code_sandbox/snaps/js-object-intro-07-code.png)

![js-object-intro example 7 result](../code_sandbox/snaps/js-object-intro-07-result.png)

- [x] **Outcome:** name is **"John"** — same value as the dot form.

<a id="js-object-intro-example-08"></a>

### **Example 8: Method fullName with this**

- [x] A **method** is a function stored as a property.
- [x] Inside the method, **`this`** is the object (`person`).

Sandbox: `code_sandbox/js-object-intro/method-fullname.html`

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

![js-object-intro example 8 source](../code_sandbox/snaps/js-object-intro-08-code.png)

![js-object-intro example 8 result](../code_sandbox/snaps/js-object-intro-08-result.png)

- [x] **Outcome:** person.fullName() is **"John Doe"**.

<a id="js-object-intro-example-09"></a>

### **Example 9: Objects are king — typeof primitives vs objects**

- [x] Almost everything in JavaScript is an object except **primitives**.
- [x] There are **7 primitives**: string, number, bigint, boolean, undefined, symbol, null. `typeof null` is the well-known **"object"** quirk.

Sandbox: `code_sandbox/js-object-intro/objects-are-king.html`

```javascript
const primitives = [
  typeof "John",
  typeof 3.14,
  typeof 10n,
  typeof true,
  typeof undefined,
  typeof Symbol("id"),
  typeof null,
];
const objects = [
  typeof { x: 1 },
  typeof [1, 2],
  typeof new Date(),
  typeof Math,
  typeof new Map(),
  typeof new Set(),
  typeof /()/,
  typeof new Error("e"),
  typeof function () {},
];
```

![js-object-intro example 9 source](../code_sandbox/snaps/js-object-intro-09-code.png)

![js-object-intro example 9 result](../code_sandbox/snaps/js-object-intro-09-result.png)

- [x] **Outcome:** Primitives: **string, number, bigint, boolean, undefined, symbol, object** (`null`). Objects (and **function**): **object** except a function, whose typeof is **"function"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-object-intro/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are `type`, `model`, and `color` on the car object?

<details>
<summary>Answer</summary>

- [x] **Properties.** Their values are **"Fiat"**, **"500"**, and **"white"**.

</details>

### Question 2: Do one-line and multiline person literals create different objects?

<details>
<summary>Answer</summary>

- [x] **No.** Spaces and line breaks are not important. Both are John Doe, 50, blue.

</details>

### Question 3: Can you start with `{}` and add properties later?

<details>
<summary>Answer</summary>

- [x] **Yes.** `person.firstName = "John"` adds the key.

</details>

### Question 4: Do you need `new Object({...})`?

<details>
<summary>Answer</summary>

- [x] **No.** Use an object literal for readability, simplicity, and speed.

</details>

### Question 5: How do you read `firstName` with dots vs brackets?

<details>
<summary>Answer</summary>

- [x] `person.firstName` and `person["firstName"]` — both **"John"**.

</details>

### Question 6: What does `person.fullName()` return?

<details>
<summary>Answer</summary>

- [x] **"John Doe"** — `this` is `person`.

</details>

### Question 7: Should you declare objects with const?

<details>
<summary>Answer</summary>

- [x] **Yes.** The page says to declare objects with **`const`**.

</details>

### Question 8: How many primitive types does JavaScript define?

<details>
<summary>Answer</summary>

- [x] **7:** string, number, bigint, boolean, undefined, symbol, null.

</details>

### Question 9: What is `typeof null`?

<details>
<summary>Answer</summary>

- [x] **"object"** — a long-standing language quirk. `null` is still a primitive.

</details>

### Question 10: What is `typeof function () {}`?

<details>
<summary>Answer</summary>

- [x] **"function"** — functions are callable objects.

</details>

### Question 11: Are arrays and dates objects?

<details>
<summary>Answer</summary>

- [x] **Yes.** `typeof []` and `typeof new Date()` are **"object"**.

</details>

### Question 12: What is an object method vs a property?

<details>
<summary>Answer</summary>

- [x] A property stores a **value**. A method stores a **function** you call with `()`.

</details>

</details>

## Summary

Create objects with literals (one line, many lines, or empty then add). Skip new Object(). Read keys with dots or brackets. Methods use this. Primitives are the exception to “objects are king”; typeof null is the odd “object” among them.

## References

- [JS Objects intro (W3Schools)](https://www.w3schools.com/js/js_object_intro.asp)
- [MDN: Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
- [MDN: Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
- [MDN: typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
