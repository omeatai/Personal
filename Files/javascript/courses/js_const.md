# JS Const

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

**`const`** (ES6, 2015) declares a **block-scoped** binding that **cannot be redeclared or reassigned**. It must be **assigned when declared**. It is a constant **reference**, so you can still change **array elements** and **object properties**.

This section has **4** examples:

- [x] **Example 1:** `const` cannot be reassigned [View](#js-const-example-01)
- [x] **Example 2:** Constant arrays (mutate, don't reassign) [View](#js-const-example-02)
- [x] **Example 3:** Constant objects (change properties, don't reassign) [View](#js-const-example-03)
- [x] **Example 4:** Block scope & hoisting [View](#js-const-example-04)

## Detailed Explanation

- [x] **`const` (ES6, 2015)** declares a **block-scoped** binding that **cannot be redeclared or reassigned**, and it **must be assigned when declared**.
- [x] Use `const` whenever you know a value should **not** be reassigned — a common choice for a new **Array**, **Object**, **Function**, or **RegExp**.
- [x] The key subtlety: `const` locks the **binding (the reference)**, not the **contents**. You can still mutate what an array or object holds.

<a id="js-const-example-01"></a>

### **Example 1: `const` cannot be reassigned**

- [x] Assigning a new value to a `const` throws a **`TypeError`** at runtime (here caught with `try/catch`).
- [x] A `const` **must be initialized on the same line** — `const PI;` (no value) is a **`SyntaxError`**.
- [x] So a `const` value is fixed the moment it is created.

Sandbox: `code_sandbox/js-const/reassign.html`

```javascript
const PI = 3.14159265359;

PI = 3.14; // TypeError: cannot reassign a const

// const PI;     // SyntaxError: must assign at declaration
// PI = 3.14;
```

![js-const example 1 source](../code_sandbox/snaps/js-const-01-code.png)

![js-const example 1 result](../code_sandbox/snaps/js-const-01-result.png)

- [x] **Outcome:** `PI` keeps **3.14159265359**; the reassignment reports **TypeError**, and the note reminds that a value‑less `const` is a `SyntaxError`.

<a id="js-const-example-02"></a>

### **Example 2: Constant arrays (mutate, don't reassign)**

- [x] With a `const` array you **can** change elements (`cars[0] = "Toyota"`) and **add** items (`cars.push("Audi")`).
- [x] What you **cannot** do is point the name at a **new array** (`cars = [...]`) — that is reassigning the binding → **`TypeError`**.
- [x] The array's **contents** are not constant; only the **reference** is.

Sandbox: `code_sandbox/js-const/arrays.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];

cars[0] = "Toyota"; // change an element - OK
cars.push("Audi"); // add an element   - OK

cars = ["Toyota"]; // TypeError: cannot reassign the array
```

![js-const example 2 source](../code_sandbox/snaps/js-const-02-code.png)

![js-const example 2 result](../code_sandbox/snaps/js-const-02-result.png)

- [x] **Outcome:** after edits the array is **Toyota, Volvo, BMW, Audi**; trying to reassign the whole array raises **TypeError**.

<a id="js-const-example-03"></a>

### **Example 3: Constant objects (change properties, don't reassign)**

- [x] With a `const` object you **can** change existing properties (`car.color = "red"`) and **add** new ones (`car.owner = "Johnson"`).
- [x] You **cannot** replace the object itself (`car = {...}`) → **`TypeError`**.
- [x] Same rule as arrays: the **binding** is constant, the **object body** is not.

Sandbox: `code_sandbox/js-const/objects.html`

```javascript
const car = { type: "Fiat", model: "500", color: "white" };

car.color = "red"; // change a property - OK
car.owner = "Johnson"; // add a property    - OK

car = { type: "Volvo" }; // TypeError: cannot reassign the object
```

![js-const example 3 source](../code_sandbox/snaps/js-const-03-code.png)

![js-const example 3 result](../code_sandbox/snaps/js-const-03-result.png)

- [x] **Outcome:** the object updates to **type=Fiat, color=red, owner=Johnson**; reassigning the object reports **TypeError**.

<a id="js-const-example-04"></a>

### **Example 4: Block scope & hoisting**

- [x] Like `let`, a `const` inside `{ }` is a **separate** variable — a block `const x` does **not** affect the outer `x`.
- [x] `const` is hoisted but **not initialized**, so using it before its line throws a **`ReferenceError`** (the temporal dead zone).
- [x] These are the same scoping/hoisting rules as `let`, plus the no‑reassignment rule.

Sandbox: `code_sandbox/js-const/scope.html`

```javascript
const x = 10;
{
  const x = 2; // a separate block-scoped const
  // here x is 2
}
// here x is 10 again

y; // ReferenceError: temporal dead zone
const y = 5;
```

![js-const example 4 source](../code_sandbox/snaps/js-const-04-code.png)

![js-const example 4 result](../code_sandbox/snaps/js-const-04-result.png)

- [x] **Outcome:** outer `x` stays **10** while the block's `x` is **2**, and touching `y` before its declaration raises **ReferenceError**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-const/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Can you reassign a `const` variable?

<details>
<summary>Answer</summary>

- [x] **No.** Reassignment throws an error.

</details>

### Question 2: Must `const` be assigned when declared?

<details>
<summary>Answer</summary>

- [x] **Yes.** `const PI;` then assign later is **incorrect**.

</details>

### Question 3: Does `const` freeze array/object contents?

<details>
<summary>Answer</summary>

- [x] **No.** It is a constant **reference**.
- [x] You can change **elements** and **properties**.
- [x] You cannot **reassign** the array or object.

</details>

### Question 4: What scope does `const` have?

<details>
<summary>Answer</summary>

- [x] **Block scope**, like `let`.

</details>

### Question 5: Can you change elements of a `const` array?

<details>
<summary>Answer</summary>

- [x] **Yes.** You can change elements and `push` new ones.
- [x] You **cannot** reassign the array itself.

</details>

### Question 6: Can you add properties to a `const` object?

<details>
<summary>Answer</summary>

- [x] **Yes.** You can change and add properties.
- [x] You **cannot** reassign the object itself.

</details>

### Question 7: What error do you get when reassigning a `const`?

<details>
<summary>Answer</summary>

- [x] A **`TypeError`** at runtime.

</details>

### Question 8: What happens if you use a `const` before its line?

<details>
<summary>Answer</summary>

- [x] A **`ReferenceError`** (temporal dead zone), just like `let`.

</details>

### Question 9: When should you prefer `const` over `let`?

<details>
<summary>Answer</summary>

- [x] Whenever the **binding** should not be reassigned.
- [x] Typical for new arrays, objects, functions, and regexes.

</details>

</details>

## Summary

**`const`** is block-scoped, must be initialized, and cannot be reassigned (`TypeError`). It locks the **binding**, not the insides of objects/arrays — you can still change array elements and object properties. Like `let`, using it before declaration is a `ReferenceError`. Prefer `const` by default; switch to `let` only when you must reassign.

## References

- [JS Const (W3Schools)](https://www.w3schools.com/js/js_const.asp)
- [MDN: const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
