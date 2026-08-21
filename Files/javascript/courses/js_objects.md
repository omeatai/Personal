# JS Objects

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

This study-path page is the map for JavaScript objects: what they store, how properties and methods work, what this means, how to display an object, and how constructors build many objects of one type. Each beginner step below is a small runnable demo of that idea.

This section has **6** examples:

- [x] **Example 1:** JavaScript Objects [View](#js-objects-example-01)
- [x] **Example 2:** Object Properties [View](#js-objects-example-02)
- [x] **Example 3:** Object Methods [View](#js-objects-example-03)
- [x] **Example 4:** Object this [View](#js-objects-example-04)
- [x] **Example 5:** Object Display [View](#js-objects-example-05)
- [x] **Example 6:** Object Constructors [View](#js-objects-example-06)

## Detailed Explanation

- [x] An object holds **properties** (values) and **methods** (functions) together.
- [x] You can **change, add, and delete** properties. Call methods with `()`. In a method, **`this`** is the owner object.
- [x] Default display is **[object Object]** — use named properties or **`JSON.stringify`**. **`new Constructor()`** builds many similar objects.
- [x] The **Advanced Objects** path (definitions, iterations, get/set, management, protection, prototypes, reference) is a later track — those chapters are not duplicated here.

<a id="js-objects-example-01"></a>

### **Example 1: JavaScript Objects**

- [x] An **object** stores **values** (properties) and **functions** (methods) together.
- [x] `type` is a property. `start` is a method — call it with `()`.

Sandbox: `code_sandbox/js-objects/javascript-objects.html`

```javascript
const car = {
  type: "Fiat",
  start: function () {
    return "started";
  },
};
```

![js-objects example 1 source](../code_sandbox/snaps/js-objects-01-code.png)

![js-objects example 1 result](../code_sandbox/snaps/js-objects-01-result.png)

- [x] **Outcome:** car.type is **"Fiat"**. car.start() returns **"started"**.

<a id="js-objects-example-02"></a>

### **Example 2: Object Properties**

- [x] Objects are collections of **properties** you can **change**, **add**, and **delete**.
- [x] After `delete car.color`, that key is gone (`undefined` if you read it).

Sandbox: `code_sandbox/js-objects/object-properties.html`

```javascript
const car = { type: "Fiat", color: "white" };
car.type = "Volvo";
car.model = "500";
delete car.color;
```

![js-objects example 2 source](../code_sandbox/snaps/js-objects-02-code.png)

![js-objects example 2 result](../code_sandbox/snaps/js-objects-02-result.png)

- [x] **Outcome:** type is **"Volvo"**, model is **"500"**, color is **undefined**, and `"color" in car` is **false**.

<a id="js-objects-example-03"></a>

### **Example 3: Object Methods**

- [x] A **method** is a function stored as a property.
- [x] Call it with **parentheses**: `car.start()`.

Sandbox: `code_sandbox/js-objects/object-methods.html`

```javascript
const car = {
  start: function () {
    return "started";
  },
};
let msg = car.start();
```

![js-objects example 3 source](../code_sandbox/snaps/js-objects-03-code.png)

![js-objects example 3 result](../code_sandbox/snaps/js-objects-03-result.png)

- [x] **Outcome:** msg is **"started"**. `typeof car.start` is **"function"**.

<a id="js-objects-example-04"></a>

### **Example 4: Object this**

- [x] Inside a method, **`this`** is the object that owns the method.
- [x] `this.firstName` reads the `firstName` property of that object.

Sandbox: `code_sandbox/js-objects/object-this.html`

```javascript
const person = {
  firstName: "John",
  greet: function () {
    return this.firstName;
  },
};
```

![js-objects example 4 source](../code_sandbox/snaps/js-objects-04-code.png)

![js-objects example 4 result](../code_sandbox/snaps/js-objects-04-result.png)

- [x] **Outcome:** person.greet() is **"John"** because `this` is `person`.

<a id="js-objects-example-05"></a>

### **Example 5: Object Display**

- [x] Putting an object in a string context shows **[object Object]**.
- [x] Show **named properties**, or use **`JSON.stringify`**.

Sandbox: `code_sandbox/js-objects/object-display.html`

```javascript
const person = { name: "John", age: 30 };
let asObject = String(person);
let named = person.name + ", " + person.age;
let json = JSON.stringify(person);
```

![js-objects example 5 source](../code_sandbox/snaps/js-objects-05-code.png)

![js-objects example 5 result](../code_sandbox/snaps/js-objects-05-result.png)

- [x] **Outcome:** String(person) is **[object Object]**. Named: **"John, 30"**. JSON: **{"name":"John","age":30}**.

<a id="js-objects-example-06"></a>

### **Example 6: Object Constructors**

- [x] A **constructor** is a function that builds many objects of the same type.
- [x] `new Person("John")` creates an object with `this.firstName = first`.

Sandbox: `code_sandbox/js-objects/object-constructors.html`

```javascript
function Person(first) {
  this.firstName = first;
}
const p = new Person("John");
```

![js-objects example 6 source](../code_sandbox/snaps/js-objects-06-code.png)

![js-objects example 6 result](../code_sandbox/snaps/js-objects-06-result.png)

- [x] **Outcome:** p.firstName is **"John"**. `p instanceof Person` is **true**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-objects/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does a JavaScript object store?

<details>
<summary>Answer</summary>

- [x] **Values** (properties) and **functions** (methods) together.

</details>

### Question 2: What is `car.start()` if `start` returns `"started"`?

<details>
<summary>Answer</summary>

- [x] **"started"**.
- [x] The parentheses call the method.

</details>

### Question 3: How do you change, add, and delete a property?

<details>
<summary>Answer</summary>

- [x] Change: `car.type = "Volvo"`.
- [x] Add: `car.model = "500"`.
- [x] Delete: `delete car.color`.

</details>

### Question 4: What is a method?

<details>
<summary>Answer</summary>

- [x] A **function stored as a property**.
- [x] Call it with `()`.

</details>

### Question 5: What is `this` inside a method?

<details>
<summary>Answer</summary>

- [x] The **object that owns** the method.
- [x] `this.firstName` reads that object’s `firstName`.

</details>

### Question 6: Why does `String(person)` show [object Object]?

<details>
<summary>Answer</summary>

- [x] That is the default string form of a plain object.
- [x] Use named properties or **`JSON.stringify`** instead.

</details>

### Question 7: What does `new Person("John")` do if the constructor sets `this.firstName = first`?

<details>
<summary>Answer</summary>

- [x] Creates a Person whose `firstName` is **"John"**.

</details>

### Question 8: Should you use `new Object()` for a simple object?

<details>
<summary>Answer</summary>

- [x] **No.** Prefer an object **literal** `{}` — later pages cover this.

</details>

### Question 9: Why is there an Advanced Objects path?

<details>
<summary>Answer</summary>

- [x] For later topics: definitions, iterations, getters/setters, protection, prototypes.
- [x] This page only introduces the beginner steps.

</details>

### Question 10: Are objects important in JavaScript?

<details>
<summary>Answer</summary>

- [x] **Yes.** If you understand objects, you understand a large part of JavaScript.

</details>

</details>

## Summary

Objects store properties and methods. Change, add, or delete keys; call methods with parentheses; use this inside methods; display with named keys or JSON; and use constructors when you need many objects of the same type. Advanced object topics are a separate path.

## References

- [JS Objects (W3Schools)](https://www.w3schools.com/js/js_objects.asp)
- [MDN: Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
- [MDN: Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
