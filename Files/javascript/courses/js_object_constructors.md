# JS Object Constructors

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

When you need many objects of the same type, write a constructor function and call it with new. Defaults go in the constructor. A property or method added to one instance stays on that instance. Assigning to the constructor function itself does not add anything to instances and calling a missing method is a TypeError. Shared features belong on the prototype. Prefer literals over new Object, new Array, and friends. Math is not a constructor.

This section has **12** examples:

- [x] **Example 1:** function Person(...) { this.firstName = ... } [View](#js-object-constructors-example-01)
- [x] **Example 2:** new Person: myFather / myMother / mySister / mySelf [View](#js-object-constructors-example-02)
- [x] **Example 3:** Default nationality = "English" in the constructor [View](#js-object-constructors-example-03)
- [x] **Example 4:** Add property to one object: myFather.nationality [View](#js-object-constructors-example-04)
- [x] **Example 5:** Person.nationality does not add to instances [View](#js-object-constructors-example-05)
- [x] **Example 6:** Person.prototype.nationality = "English" [View](#js-object-constructors-example-06)
- [x] **Example 7:** Constructor method: fullName [View](#js-object-constructors-example-07)
- [x] **Example 8:** Add method to one object: myMother.changeName [View](#js-object-constructors-example-08)
- [x] **Example 9:** Person.changeName then myMother.changeName → TypeError [View](#js-object-constructors-example-09)
- [x] **Example 10:** Person.prototype.changeName then myMother.changeName works [View](#js-object-constructors-example-10)
- [x] **Example 11:** Built-in constructors (Math cannot use new) [View](#js-object-constructors-example-11)
- [x] **Example 12:** Literals vs new (working function expression) [View](#js-object-constructors-example-12)

## Detailed Explanation

- [x] Name constructors with an **uppercase** first letter. Call them with **`new`** so `this` becomes the new object.
- [x] A value set in the constructor is a **default** on every instance. A value set on **one object** is only for that object.
- [x] `Person.nationality = ...` or `Person.changeName = ...` does **not** add to instances. Use **`Person.prototype`**. Otherwise **TypeError**.
- [x] Built-ins: `new Object/Array/Map/Set/Date/RegExp/Function`. **`new Math()`** throws. Prefer `{}`, `[]`, `/()/`, and `const f = function () {}` — the page’s `function(){};` statement is a **SyntaxError**.

<a id="js-object-constructors-example-01"></a>

### **Example 1: function Person(...) { this.firstName = ... }**

- [x] A constructor is an ordinary function. Name it with an **uppercase** first letter by convention.
- [x] `this` has **no value** until you call it with **`new`** — then `this` is the new object.

Sandbox: `code_sandbox/js-object-constructors/person-constructor.html`

```javascript
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}
const sample = new Person("John", "Doe", 50, "blue");
```

![js-object-constructors example 1 source](../code_sandbox/snaps/js-object-constructors-01-code.png)

![js-object-constructors example 1 result](../code_sandbox/snaps/js-object-constructors-01-result.png)

- [x] **Outcome:** `typeof Person` is **"function"**. sample is **John** with **blue** eyes.

<a id="js-object-constructors-example-02"></a>

### **Example 2: new Person: myFather / myMother / mySister / mySelf**

- [x] `new Person(...)` creates **many** objects of the same type.
- [x] Each instance has its own `firstName`, `lastName`, `age`, and `eyeColor`.

Sandbox: `code_sandbox/js-object-constructors/many-persons.html`

```javascript
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}
const myFather = new Person("John", "Doe", 50, "blue");
const myMother = new Person("Sally", "Rally", 48, "green");
const mySister = new Person("Anna", "Rally", 18, "green");
const mySelf = new Person("Johnny", "Rally", 22, "green");
```

![js-object-constructors example 2 source](../code_sandbox/snaps/js-object-constructors-02-code.png)

![js-object-constructors example 2 result](../code_sandbox/snaps/js-object-constructors-02-result.png)

- [x] **Outcome:** **John**, **Sally**, **Anna**, and **Johnny** — four Person objects.

<a id="js-object-constructors-example-03"></a>

### **Example 3: Default nationality = "English" in the constructor**

- [x] A value assigned in the constructor is a **default** on every new object.
- [x] You do not pass `nationality` as a parameter.

Sandbox: `code_sandbox/js-object-constructors/default-nationality.html`

```javascript
function Person(first, last, age, eyecolor) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eyecolor;
  this.nationality = "English";
}
const myFather = new Person("John", "Doe", 50, "blue");
const myMother = new Person("Sally", "Rally", 48, "green");
```

![js-object-constructors example 3 source](../code_sandbox/snaps/js-object-constructors-03-code.png)

![js-object-constructors example 3 result](../code_sandbox/snaps/js-object-constructors-03-result.png)

- [x] **Outcome:** Both myFather and myMother have nationality **"English"**.

<a id="js-object-constructors-example-04"></a>

### **Example 4: Add property to one object: myFather.nationality**

- [x] Adding a property on **one instance** does not add it to the others.
- [x] `myFather.nationality` is set; `myMother.nationality` stays **undefined**.

Sandbox: `code_sandbox/js-object-constructors/add-property-one.html`

```javascript
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}
const myFather = new Person("John", "Doe", 50, "blue");
const myMother = new Person("Sally", "Rally", 48, "green");
myFather.nationality = "English";
```

![js-object-constructors example 4 source](../code_sandbox/snaps/js-object-constructors-04-code.png)

![js-object-constructors example 4 result](../code_sandbox/snaps/js-object-constructors-04-result.png)

- [x] **Outcome:** myFather.nationality is **"English"**. myMother.nationality is **undefined**.

<a id="js-object-constructors-example-05"></a>

### **Example 5: Person.nationality does not add to instances**

- [x] You **cannot** add a property to instances by assigning `Person.nationality`.
- [x] That sets a property on the **function object**, not on `myFather`.

Sandbox: `code_sandbox/js-object-constructors/person-nationality-fails.html`

```javascript
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}
const myFather = new Person("John", "Doe", 50, "blue");
Person.nationality = "English";
```

![js-object-constructors example 5 source](../code_sandbox/snaps/js-object-constructors-05-code.png)

![js-object-constructors example 5 result](../code_sandbox/snaps/js-object-constructors-05-result.png)

- [x] **Outcome:** Person.nationality is **"English"**. myFather.nationality is **undefined**.

<a id="js-object-constructors-example-06"></a>

### **Example 6: Person.prototype.nationality = "English"**

- [x] Add a shared property on **`Person.prototype`**.
- [x] Instances then **inherit** `nationality`.

Sandbox: `code_sandbox/js-object-constructors/prototype-nationality.html`

```javascript
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}
const myFather = new Person("John", "Doe", 50, "blue");
const myMother = new Person("Sally", "Rally", 48, "green");
Person.prototype.nationality = "English";
```

![js-object-constructors example 6 source](../code_sandbox/snaps/js-object-constructors-06-code.png)

![js-object-constructors example 6 result](../code_sandbox/snaps/js-object-constructors-06-result.png)

- [x] **Outcome:** Both instances read **"English"** from the prototype.

<a id="js-object-constructors-example-07"></a>

### **Example 7: Constructor method: fullName**

- [x] A constructor can assign **methods** to `this` as well as data.
- [x] Each new Person gets its own `fullName` function.

Sandbox: `code_sandbox/js-object-constructors/constructor-method.html`

```javascript
function Person(first, last, age, eyecolor) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eyecolor;
  this.fullName = function () {
    return this.firstName + " " + this.lastName;
  };
}
const myFather = new Person("John", "Doe", 50, "blue");
```

![js-object-constructors example 7 source](../code_sandbox/snaps/js-object-constructors-07-code.png)

![js-object-constructors example 7 result](../code_sandbox/snaps/js-object-constructors-07-result.png)

- [x] **Outcome:** myFather.fullName() is **"John Doe"**.

<a id="js-object-constructors-example-08"></a>

### **Example 8: Add method to one object: myMother.changeName**

- [x] Assigning a method on **one object** does not add it to the others.
- [x] `myMother.changeName("Doe")` changes only her `lastName`.

Sandbox: `code_sandbox/js-object-constructors/add-method-one.html`

```javascript
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}
const myFather = new Person("John", "Doe", 50, "blue");
const myMother = new Person("Sally", "Rally", 48, "green");
myMother.changeName = function (name) {
  this.lastName = name;
};
myMother.changeName("Doe");
```

![js-object-constructors example 8 source](../code_sandbox/snaps/js-object-constructors-08-code.png)

![js-object-constructors example 8 result](../code_sandbox/snaps/js-object-constructors-08-result.png)

- [x] **Outcome:** myMother.lastName is **"Doe"**. `typeof myFather.changeName` is **"undefined"**. myFather.lastName is still **"Doe"** (his original name).

<a id="js-object-constructors-example-09"></a>

### **Example 9: Person.changeName then myMother.changeName → TypeError**

- [x] Assigning `Person.changeName` does **not** put the method on instances.
- [x] `myMother.changeName("Doe")` throws **TypeError**. Caught here so the sandbox can show the message.

Sandbox: `code_sandbox/js-object-constructors/person-changename-typeerror.html`

```javascript
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}
const myMother = new Person("Sally", "Rally", 48, "green");
Person.changeName = function (name) {
  this.lastName = name;
};
myMother.changeName("Doe");
```

![js-object-constructors example 9 source](../code_sandbox/snaps/js-object-constructors-09-code.png)

![js-object-constructors example 9 result](../code_sandbox/snaps/js-object-constructors-09-result.png)

- [x] **Outcome:** **TypeError: myMother.changeName is not a function** (caught). myMother.lastName stays **"Rally"**.

<a id="js-object-constructors-example-10"></a>

### **Example 10: Person.prototype.changeName then myMother.changeName works**

- [x] Put the method on **`Person.prototype`** so every instance can call it.
- [x] `this` inside `changeName` is `myMother` for that call.

Sandbox: `code_sandbox/js-object-constructors/prototype-changename.html`

```javascript
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}
const myMother = new Person("Sally", "Rally", 48, "green");
Person.prototype.changeName = function (name) {
  this.lastName = name;
};
myMother.changeName("Doe");
```

![js-object-constructors example 10 source](../code_sandbox/snaps/js-object-constructors-10-code.png)

![js-object-constructors example 10 result](../code_sandbox/snaps/js-object-constructors-10-result.png)

- [x] **Outcome:** myMother.lastName is **"Doe"** after the prototype method runs.

<a id="js-object-constructors-example-11"></a>

### **Example 11: Built-in constructors (Math cannot use new)**

- [x] JavaScript has built-in constructors: **Object, Array, Map, Set, Date, RegExp, Function**.
- [x] `Math` is a global object, **not** a constructor — `new Math()` throws **TypeError** (caught).

Sandbox: `code_sandbox/js-object-constructors/builtin-constructors.html`

```javascript
const o = new Object();
const a = new Array();
const m = new Map();
const s = new Set();
const d = new Date();
const r = new RegExp();
const f = new Function();
new Math();
```

![js-object-constructors example 11 source](../code_sandbox/snaps/js-object-constructors-11-code.png)

![js-object-constructors example 11 result](../code_sandbox/snaps/js-object-constructors-11-result.png)

- [x] **Outcome:** Object/Array/Map/Set/Date/RegExp/Function all construct. **`new Math()` → TypeError: Math is not a constructor**.

<a id="js-object-constructors-example-12"></a>

### **Example 12: Literals vs new (working function expression)**

- [x] Prefer **literals**: `{}`, `[]`, `/()/`, and a **function expression**.
- [x] The page listed `function(){};` as a statement — that is a **SyntaxError**. A bare `{}` is also an empty **block**, not an object. This demo uses `const` bindings (current correct syntax).

Sandbox: `code_sandbox/js-object-constructors/literals-vs-new.html`

```javascript
const primStr = "";
const primNum = 0;
const primBool = false;
const obj = {};
const arr = [];
const re = /()/;
const f = function () {};
```

![js-object-constructors example 12 source](../code_sandbox/snaps/js-object-constructors-12-code.png)

![js-object-constructors example 12 result](../code_sandbox/snaps/js-object-constructors-12-result.png)

- [x] **Outcome:** Primitives: **string, number, boolean**. `{}` / `[]` / `/()/` are **object**. `const f = function () {}` is **"function"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-object-constructors/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `new Person("John", "Doe", 50, "blue").firstName`?

<details>
<summary>Answer</summary>

- [x] **"John"**. `this` in the constructor is the new object.

</details>

### Question 2: Can one constructor make myFather, myMother, mySister, and mySelf?

<details>
<summary>Answer</summary>

- [x] **Yes.** Each `new Person(...)` is a separate object.

</details>

### Question 3: What is `nationality` if the constructor sets `this.nationality = "English"`?

<details>
<summary>Answer</summary>

- [x] **"English"** on every new Person — a default value.

</details>

### Question 4: If only `myFather.nationality = "English"`, what is `myMother.nationality`?

<details>
<summary>Answer</summary>

- [x] **undefined**. The new property is only on myFather.

</details>

### Question 5: Does `Person.nationality = "English"` set `myFather.nationality`?

<details>
<summary>Answer</summary>

- [x] **No.** That property is on the **function**, not on instances. myFather.nationality is **undefined**.

</details>

### Question 6: How do all instances get nationality?

<details>
<summary>Answer</summary>

- [x] `Person.prototype.nationality = "English"` — instances inherit it.

</details>

### Question 7: What is `myFather.fullName()` if the constructor defines that method?

<details>
<summary>Answer</summary>

- [x] **"John Doe"**.

</details>

### Question 8: If only `myMother.changeName` is assigned, can `myFather.changeName` run?

<details>
<summary>Answer</summary>

- [x] **No.** `typeof myFather.changeName` is **"undefined"**.

</details>

### Question 9: What happens if you set `Person.changeName` then call `myMother.changeName("Doe")`?

<details>
<summary>Answer</summary>

- [x] **TypeError: myMother.changeName is not a function**.

</details>

### Question 10: What happens after `Person.prototype.changeName` then `myMother.changeName("Doe")`?

<details>
<summary>Answer</summary>

- [x] It **works**. myMother.lastName becomes **"Doe"**.

</details>

### Question 11: Which built-ins can you call with `new`?

<details>
<summary>Answer</summary>

- [x] **Object, Array, Map, Set, Date, RegExp, Function**.
- [x] `new Math()` is **TypeError: Math is not a constructor**.

</details>

### Question 12: Why not write `function(){};` as a statement like the page listed?

<details>
<summary>Answer</summary>

- [x] It is a **SyntaxError**. Use `const f = function () {};`.
- [x] A bare `{}` as a statement is an empty **block**, not an object — assign it: `const obj = {}`.

</details>

### Question 13: When does `this` get a value in a constructor?

<details>
<summary>Answer</summary>

- [x] When you call the function with **`new`**. Until then it has no instance value.

</details>

### Question 14: Should you prefer `{}` over `new Object()`?

<details>
<summary>Answer</summary>

- [x] **Yes.** Also prefer `[]` over `new Array()` and `/()/` over `new RegExp()`.

</details>

</details>

## Summary

Use a constructor plus new to stamp out many similar objects. Defaults belong in the constructor; shared methods and properties belong on the prototype. Assigning to the function does not update instances and calling a missing method throws TypeError. Prefer literals, and never new Math(). The page’s function(){}; list item needs a const function expression to run.

## References

- [JS Object Constructors (W3Schools)](https://www.w3schools.com/js/js_object_constructors.asp)
- [MDN: new](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
- [MDN: Object.prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/prototype)
- [MDN: Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)
- [MDN: Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
