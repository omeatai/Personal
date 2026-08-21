# JS Object this

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The this keyword refers to an object. In a method it is the owner, which is why the same method pattern can greet John and Anna. Used alone, or in a regular non-strict function, this is the global object (window in a browser). In a strict-mode function, this is undefined.

This section has **5** examples:

- [x] **Example 1:** fullName with this [View](#js-object-this-example-01)
- [x] **Example 2:** person1.hello() vs person2.hello() [View](#js-object-this-example-02)
- [x] **Example 3:** this alone (global / window) [View](#js-object-this-example-03)
- [x] **Example 4:** this in a regular function (non-strict) [View](#js-object-this-example-04)
- [x] **Example 5:** "use strict" function: this is undefined [View](#js-object-this-example-05)

## Detailed Explanation

- [x] In a **method**, `this` is the **owner object**.
- [x] That is why `hello` can return **Hello John** and **Hello Anna** from two objects.
- [x] Used **alone** or in a **regular non-strict function**, `this` is **`window`** in a browser.
- [x] In a function with **`"use strict"`**, `this` is **undefined** (clarifying extra the page mentions).

<a id="js-object-this-example-01"></a>

### **Example 1: fullName with this**

- [x] `this.firstName` is the `firstName` of the **owner object**.
- [x] `this.lastName` is that object’s `lastName`.

Sandbox: `code_sandbox/js-object-this/fullname-this.html`

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

![js-object-this example 1 source](../code_sandbox/snaps/js-object-this-01-code.png)

![js-object-this example 1 result](../code_sandbox/snaps/js-object-this-01-result.png)

- [x] **Outcome:** person.fullName() is **"John Doe"**.

<a id="js-object-this-example-02"></a>

### **Example 2: person1.hello() vs person2.hello()**

- [x] `this` lets the **same method pattern** work on different objects.
- [x] The page only prints `person1.hello()`. This demo shows **both** greetings.

Sandbox: `code_sandbox/js-object-this/hello-two-people.html`

```javascript
const person1 = {
  name: "John",
  hello: function () {
    return "Hello " + this.name;
  },
};
const person2 = {
  name: "Anna",
  hello: function () {
    return "Hello " + this.name;
  },
};
```

![js-object-this example 2 source](../code_sandbox/snaps/js-object-this-02-code.png)

![js-object-this example 2 result](../code_sandbox/snaps/js-object-this-02-result.png)

- [x] **Outcome:** person1.hello() is **"Hello John"**. person2.hello() is **"Hello Anna"**.

<a id="js-object-this-example-03"></a>

### **Example 3: this alone (global / window)**

- [x] Used **alone**, `this` is the **global object**.
- [x] In a browser that object is **`window`**. The page assigns `let x = this` and displays it.

Sandbox: `code_sandbox/js-object-this/this-alone.html`

```javascript
let x = this;
```

![js-object-this example 3 source](../code_sandbox/snaps/js-object-this-03-code.png)

![js-object-this example 3 result](../code_sandbox/snaps/js-object-this-03-result.png)

- [x] **Outcome:** `String(this)` is **[object Window]**. `this === window` is **true** in this non-strict classic script.

<a id="js-object-this-example-04"></a>

### **Example 4: this in a regular function (non-strict)**

- [x] In a **regular function** (not a method), `this` is also the global object when you are **not** in strict mode.
- [x] `myFunction()` therefore returns **`window`** here.

Sandbox: `code_sandbox/js-object-this/this-in-function.html`

```javascript
function myFunction() {
  return this;
}
let x = myFunction();
```

![js-object-this example 4 source](../code_sandbox/snaps/js-object-this-04-code.png)

![js-object-this example 4 result](../code_sandbox/snaps/js-object-this-04-result.png)

- [x] **Outcome:** `String(this)` is **[object Window]**. `this === window` is **true** (non-strict).

<a id="js-object-this-example-05"></a>

### **Example 5: "use strict" function: this is undefined**

- [x] Clarifying extra: the page notes that in **strict mode**, `this` used alone is **undefined**.
- [x] A function that starts with `"use strict"` does **not** get `window` as `this`.

Sandbox: `code_sandbox/js-object-this/strict-this.html`

```javascript
function strictThis() {
  "use strict";
  return this;
}
let x = strictThis();
```

![js-object-this example 5 source](../code_sandbox/snaps/js-object-this-05-code.png)

![js-object-this example 5 result](../code_sandbox/snaps/js-object-this-05-result.png)

- [x] **Outcome:** `strictThis()` is **undefined**. `typeof this` is **undefined**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-object-this/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `person.fullName()` with this.firstName / this.lastName?

<details>
<summary>Answer</summary>

- [x] **"John Doe"**.

</details>

### Question 2: What do `person1.hello()` and `person2.hello()` return?

<details>
<summary>Answer</summary>

- [x] **"Hello John"** and **"Hello Anna"**.
- [x] `this.name` is each object’s own name.

</details>

### Question 3: Why use this instead of writing person.name inside the method?

<details>
<summary>Answer</summary>

- [x] So the **same method pattern** works on **different** objects.

</details>

### Question 4: What is `this` used alone in a browser script?

<details>
<summary>Answer</summary>

- [x] The **global object** — **`window`**.
- [x] `String(this)` is **[object Window]**.

</details>

### Question 5: Is `this === window` true at the top level of this sandbox?

<details>
<summary>Answer</summary>

- [x] **Yes** — the example script is not in strict mode.

</details>

### Question 6: What is `this` inside `function myFunction() { return this; }` (non-strict)?

<details>
<summary>Answer</summary>

- [x] Also **`window`**. `myFunction() === window` is **true**.

</details>

### Question 7: What is `this` in a `"use strict"` function?

<details>
<summary>Answer</summary>

- [x] **undefined**.

</details>

### Question 8: Does this in a method mean the function?

<details>
<summary>Answer</summary>

- [x] **No.** It means the **object** that is calling the method.

</details>

### Question 9: What does the page display for `let x = this`?

<details>
<summary>Answer</summary>

- [x] The window object, which stringifies to **[object Window]**.

</details>

### Question 10: When is this not window?

<details>
<summary>Answer</summary>

- [x] In an **object method** (the owner), in **strict** functions (**undefined**), and in other later cases (bind, arrows) covered on advanced pages.

</details>

</details>

## Summary

In a method, this is the owner object, so one method pattern can serve many objects. Alone or in a non-strict function, this is window. In a strict function, this is undefined.

## References

- [JS this in Objects (W3Schools)](https://www.w3schools.com/js/js_object_this.asp)
- [MDN: this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
- [MDN: Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
- [MDN: window](https://developer.mozilla.org/en-US/docs/Web/API/Window)
