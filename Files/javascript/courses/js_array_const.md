# JS Array const

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

const is the usual way to declare arrays since ES6. It is a constant reference, not a frozen list: you may change elements and push, but you may not assign a new array to that name. const requires an initializer (a parse-time SyntaxError otherwise). const is block-scoped, so an inner const cars does not overwrite the outer one; var does. Redeclaring var is allowed. Redeclaring const, or mixing var and const for the same name in one scope, is a SyntaxError. A const in another block is a different binding.

This section has **11** examples:

- [x] **Example 1:** Declare an array with const [View](#js-array-const-example-01)
- [x] **Example 2:** ERROR cannot reassign a const array [View](#js-array-const-example-02)
- [x] **Example 3:** Elements can be changed; push is allowed [View](#js-array-const-example-03)
- [x] **Example 4:** ERROR const without initializer [View](#js-array-const-example-04)
- [x] **Example 5:** var can be used before the declaration [View](#js-array-const-example-05)
- [x] **Example 6:** const has block scope [View](#js-array-const-example-06)
- [x] **Example 7:** var does not have block scope [View](#js-array-const-example-07)
- [x] **Example 8:** var may be redeclared and reassigned [View](#js-array-const-example-08)
- [x] **Example 9:** ERROR var then const in the same scope [View](#js-array-const-example-09)
- [x] **Example 10:** ERROR redeclare or reassign const in the same scope [View](#js-array-const-example-10)
- [x] **Example 11:** const in another block is allowed [View](#js-array-const-example-11)

## Detailed Explanation

- [x] `const` locks the **binding**, not the **contents**.
- [x] Reassigning the array is a **TypeError**. `const cars;` is a **SyntaxError**.
- [x] `cars[0] = ...` and `cars.push(...)` are **allowed**.
- [x] `const` is **block-scoped**. `var` is not — inner `var` leaks.
- [x] `var` may be redeclared. `const` may not, in the same scope.
- [x] Parse-time SyntaxErrors are compiled with **`new Function`** so the sandbox can catch them.

<a id="js-array-const-example-01"></a>

### **Example 1: Declare an array with const**

- [x] ES6 made **`const`** the usual way to declare arrays.

Sandbox: `code_sandbox/js-array-const/const-declare.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
```

![js-array-const example 1 source](../code_sandbox/snaps/js-array-const-01-code.png)

![js-array-const example 1 result](../code_sandbox/snaps/js-array-const-01-result.png)

- [x] **Outcome:** **["Saab","Volvo","BMW"]**.

<a id="js-array-const-example-02"></a>

### **Example 2: ERROR cannot reassign a const array**

- [x] `const` binds the **reference**. Replacing the whole array throws **TypeError**.

Sandbox: `code_sandbox/js-array-const/const-reassign-error.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
cars = ["Toyota", "Volvo", "Audi"]; // ERROR
```

![js-array-const example 2 source](../code_sandbox/snaps/js-array-const-02-code.png)

![js-array-const example 2 result](../code_sandbox/snaps/js-array-const-02-result.png)

- [x] **Outcome:** **TypeError: Assignment to constant variable.**

<a id="js-array-const-example-03"></a>

### **Example 3: Elements can be changed; push is allowed**

- [x] `const` is **not** a frozen array. You may change indexes and `push`.

Sandbox: `code_sandbox/js-array-const/const-mutate-ok.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
cars[0] = "Toyota";
cars.push("Audi");
```

![js-array-const example 3 source](../code_sandbox/snaps/js-array-const-03-code.png)

![js-array-const example 3 result](../code_sandbox/snaps/js-array-const-03-result.png)

- [x] **Outcome:** **["Toyota","Volvo","BMW","Audi"]**.

<a id="js-array-const-example-04"></a>

### **Example 4: ERROR const without initializer**

- [x] `const cars;` is a **SyntaxError**. It must be assigned **when declared**.
- [x] Caught with **`new Function`** so this page can still load.

Sandbox: `code_sandbox/js-array-const/const-no-init.html`

```javascript
const cars;
cars = ["Saab", "Volvo", "BMW"];
```

![js-array-const example 4 source](../code_sandbox/snaps/js-array-const-04-code.png)

![js-array-const example 4 result](../code_sandbox/snaps/js-array-const-04-result.png)

- [x] **Outcome:** **SyntaxError: Missing initializer in const declaration** (caught via `new Function`).

<a id="js-array-const-example-05"></a>

### **Example 5: var can be used before the declaration**

- [x] `var` is **hoisted**. Assigning before `var cars` is allowed.

Sandbox: `code_sandbox/js-array-const/var-hoist-init.html`

```javascript
cars = ["Saab", "Volvo", "BMW"];
var cars;
```

![js-array-const example 5 source](../code_sandbox/snaps/js-array-const-05-code.png)

![js-array-const example 5 result](../code_sandbox/snaps/js-array-const-05-result.png)

- [x] **Outcome:** **["Saab","Volvo","BMW"]**.

<a id="js-array-const-example-06"></a>

### **Example 6: const has block scope**

- [x] An inner `const cars` **shadows** the outer one only **inside `{ }`**.

Sandbox: `code_sandbox/js-array-const/const-block-scope.html`

```javascript
const cars = ["Saab", "Volvo", "BMW"];
let inside;
{
  const cars = ["Toyota", "Volvo", "BMW"];
  inside = cars[0];
}
let outside = cars[0];
```

![js-array-const example 6 source](../code_sandbox/snaps/js-array-const-06-code.png)

![js-array-const example 6 result](../code_sandbox/snaps/js-array-const-06-result.png)

- [x] **Outcome:** Inside the block **"Toyota"**. After the block **"Saab"**.

<a id="js-array-const-example-07"></a>

### **Example 7: var does not have block scope**

- [x] Inner `var cars` **overwrites** the outer one.

Sandbox: `code_sandbox/js-array-const/var-no-block-scope.html`

```javascript
var cars = ["Saab", "Volvo", "BMW"];
let inside;
{
  var cars = ["Toyota", "Volvo", "BMW"];
  inside = cars[0];
}
let outside = cars[0];
```

![js-array-const example 7 source](../code_sandbox/snaps/js-array-const-07-code.png)

![js-array-const example 7 result](../code_sandbox/snaps/js-array-const-07-result.png)

- [x] **Outcome:** Both inside and after the block: **"Toyota"**.

<a id="js-array-const-example-08"></a>

### **Example 8: var may be redeclared and reassigned**

- [x] Redeclaring `var` in the same scope is **allowed**.

Sandbox: `code_sandbox/js-array-const/var-redeclare-ok.html`

```javascript
var cars = ["Volvo", "BMW"];
var cars = ["Toyota", "BMW"];
cars = ["Volvo", "Saab"];
```

![js-array-const example 8 source](../code_sandbox/snaps/js-array-const-08-code.png)

![js-array-const example 8 result](../code_sandbox/snaps/js-array-const-08-result.png)

- [x] **Outcome:** **["Volvo","Saab"]**.

<a id="js-array-const-example-09"></a>

### **Example 9: ERROR var then const in the same scope**

- [x] The page’s “Not allowed” block: `const cars` after `var cars` is a **SyntaxError**.

Sandbox: `code_sandbox/js-array-const/var-then-const-error.html`

```javascript
var cars = ["Volvo", "BMW"];
const cars = ["Volvo", "BMW"]; // Not allowed
```

![js-array-const example 9 source](../code_sandbox/snaps/js-array-const-09-code.png)

![js-array-const example 9 result](../code_sandbox/snaps/js-array-const-09-result.png)

- [x] **Outcome:** **SyntaxError: Identifier 'cars' has already been declared** (caught via `new Function`).

<a id="js-array-const-example-10"></a>

### **Example 10: ERROR redeclare or reassign const in the same scope**

- [x] Second `const cars` in the same scope is a **SyntaxError**.

Sandbox: `code_sandbox/js-array-const/const-redeclare-error.html`

```javascript
const cars = ["Volvo", "BMW"];
const cars = ["Volvo", "BMW"]; // Not allowed
```

![js-array-const example 10 source](../code_sandbox/snaps/js-array-const-10-code.png)

![js-array-const example 10 result](../code_sandbox/snaps/js-array-const-10-result.png)

- [x] **Outcome:** **SyntaxError: Identifier 'cars' has already been declared** (caught via `new Function`).

<a id="js-array-const-example-11"></a>

### **Example 11: const in another block is allowed**

- [x] Each block may declare its **own** `const cars`.

Sandbox: `code_sandbox/js-array-const/const-other-blocks-ok.html`

```javascript
const cars = ["Volvo", "BMW"];
let inner1;
let inner2;
{
  const cars = ["Toyota", "BMW"];
  inner1 = JSON.stringify(cars);
}
{
  const cars = ["Saab", "Audi"];
  inner2 = JSON.stringify(cars);
}
let outer = JSON.stringify(cars);
```

![js-array-const example 11 source](../code_sandbox/snaps/js-array-const-11-code.png)

![js-array-const example 11 result](../code_sandbox/snaps/js-array-const-11-result.png)

- [x] **Outcome:** Inner blocks **["Toyota","BMW"]** and **["Saab","Audi"]**. Outer still **["Volvo","BMW"]**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-array-const/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Can you reassign a const array?

<details>
<summary>Answer</summary>

- [x] **No.** **TypeError: Assignment to constant variable.**

</details>

### Question 2: Can you change cars[0] or push?

<details>
<summary>Answer</summary>

- [x] **Yes.** This demo becomes **["Toyota","Volvo","BMW","Audi"]**.

</details>

### Question 3: What is const cars; then assign?

<details>
<summary>Answer</summary>

- [x] **SyntaxError: Missing initializer in const declaration**.

</details>

### Question 4: Can var be assigned before the declaration?

<details>
<summary>Answer</summary>

- [x] **Yes.** Hoisting: `cars = [...]; var cars;` works.

</details>

### Question 5: Does an inner const cars change the outer one?

<details>
<summary>Answer</summary>

- [x] **No.** Inside **Toyota**, outside **Saab**.

</details>

### Question 6: Does an inner var cars change the outer one?

<details>
<summary>Answer</summary>

- [x] **Yes.** Both read **Toyota**.

</details>

### Question 7: Can you redeclare var?

<details>
<summary>Answer</summary>

- [x] **Yes.** Last assignment wins: **["Volvo","Saab"]**.

</details>

### Question 8: var then const in the same scope?

<details>
<summary>Answer</summary>

- [x] **SyntaxError: Identifier 'cars' has already been declared**.

</details>

### Question 9: Two const cars in one scope?

<details>
<summary>Answer</summary>

- [x] The same **SyntaxError**.

</details>

### Question 10: Two const cars in different blocks?

<details>
<summary>Answer</summary>

- [x] **Allowed.** Each block has its own binding; the outer array stays.

</details>

### Question 11: Why new Function for some errors?

<details>
<summary>Answer</summary>

- [x] A raw `<script>` with a SyntaxError **does not parse**, so the page would be blank.

</details>


</details>

## Summary

Declare arrays with const. Mutate elements freely; never reassign the binding. Initialize at the declaration. Use blocks when you need a second const of the same name. Leave var for the hoisting demos — it is not block-scoped and it lets you redeclare.

## References

- [JS Array Const (W3Schools)](https://www.w3schools.com/js/js_array_const.asp)
- [MDN: const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
- [MDN: Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
