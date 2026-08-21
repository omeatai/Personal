# JS undefined

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

undefined means a variable was declared but not given a value. typeof is also undefined. Missing object properties and functions without return produce undefined. An empty string is not undefined. The W3Schools snippet that reassigns a const person to undefined is a TypeError in real JS — use let. Reading a name that was never declared is ReferenceError; typeof that name is still undefined. undefined == null is true; === is false.

This section has **10** examples:

- [x] **Example 1:** let car — value undefined [View](#js-undefined-example-01)
- [x] **Example 2:** typeof car — type undefined [View](#js-undefined-example-02)
- [x] **Example 3:** Empty string "" vs undefined [View](#js-undefined-example-03)
- [x] **Example 4:** Missing object property is undefined [View](#js-undefined-example-04)
- [x] **Example 5:** Function without return yields undefined [View](#js-undefined-example-05)
- [x] **Example 6:** const person = undefined — TypeError [View](#js-undefined-example-06)
- [x] **Example 7:** let person = undefined — empties the binding [View](#js-undefined-example-07)
- [x] **Example 8:** let person = null — emptied with null [View](#js-undefined-example-08)
- [x] **Example 9:** Reading an undeclared name is ReferenceError [View](#js-undefined-example-09)
- [x] **Example 10:** undefined == null is true; === is false [View](#js-undefined-example-10)

## Detailed Explanation

- [x] `let car;` → value **undefined**, typeof **"undefined"**.
- [x] Empty string **`""`** is a **string**, not undefined.
- [x] Missing property **person.age** is **undefined** (no throw).
- [x] No `return` → **undefined**.
- [x] `const person = …; person = undefined` is **TypeError**. **`let`** can be emptied.
- [x] Undeclared read is **ReferenceError**. `typeof missing` is **"undefined"**.

<a id="js-undefined-example-01"></a>

### **Example 1: let car — value undefined**

- [x] A variable declared without a value is **`undefined`**.

Sandbox: `code_sandbox/js-undefined/declared-no-value.html`

```javascript
let car;
```

![js-undefined example 1 source](../code_sandbox/snaps/js-undefined-01-code.png)

![js-undefined example 1 result](../code_sandbox/snaps/js-undefined-01-result.png)

- [x] **Outcome:** car is **undefined**.

<a id="js-undefined-example-02"></a>

### **Example 2: typeof car — type undefined**

- [x] `typeof` of that variable is **"undefined"**.

Sandbox: `code_sandbox/js-undefined/typeof-undefined.html`

```javascript
let car;
typeof car;
```

![js-undefined example 2 source](../code_sandbox/snaps/js-undefined-02-code.png)

![js-undefined example 2 result](../code_sandbox/snaps/js-undefined-02-result.png)

- [x] **Outcome:** typeof car is **"undefined"**.

<a id="js-undefined-example-03"></a>

### **Example 3: Empty string "" vs undefined**

- [x] An empty string has a **value** and a **type**. It is **not** undefined.

Sandbox: `code_sandbox/js-undefined/empty-string-not-undefined.html`

```javascript
let text = "";
```

![js-undefined example 3 source](../code_sandbox/snaps/js-undefined-03-code.png)

![js-undefined example 3 result](../code_sandbox/snaps/js-undefined-03-result.png)

- [x] **Outcome:** text is **""**. typeof is **"string"**. Concatenation `text + " " + typeof text` would be **" string"**.

<a id="js-undefined-example-04"></a>

### **Example 4: Missing object property is undefined**

- [x] Reading a **non-existing** property returns **`undefined`** (it does not throw).

Sandbox: `code_sandbox/js-undefined/missing-property.html`

```javascript
const person = {firstName:"John", lastName:"Doe"};
```

![js-undefined example 4 source](../code_sandbox/snaps/js-undefined-04-code.png)

![js-undefined example 4 result](../code_sandbox/snaps/js-undefined-04-result.png)

- [x] **Outcome:** person.age is **undefined**. typeof is **"undefined"**.

<a id="js-undefined-example-05"></a>

### **Example 5: Function without return yields undefined**

- [x] A function with **no `return`** returns **`undefined`**.

Sandbox: `code_sandbox/js-undefined/function-no-return.html`

```javascript
function myFunction() {
  let x = 5;
}
```

![js-undefined example 5 source](../code_sandbox/snaps/js-undefined-05-code.png)

![js-undefined example 5 result](../code_sandbox/snaps/js-undefined-05-result.png)

- [x] **Outcome:** myFunction() is **undefined**. typeof is **"undefined"**. The inner `x` is unused.

<a id="js-undefined-example-06"></a>

### **Example 6: const person = undefined — TypeError**

- [x] The page assigns `person = undefined` after **`const person`**. That is a **TypeError**.
- [x] `const` cannot be reassigned. Use **`let`** if you need to empty the binding.

Sandbox: `code_sandbox/js-undefined/const-assign-typeerror.html`

```javascript
const person = {firstName:"John", lastName:"Doe"};
person = undefined;
```

![js-undefined example 6 source](../code_sandbox/snaps/js-undefined-06-code.png)

![js-undefined example 6 result](../code_sandbox/snaps/js-undefined-06-result.png)

- [x] **Outcome:** **TypeError: Assignment to constant variable.** The object is unchanged. Use `let` to reassign.

<a id="js-undefined-example-07"></a>

### **Example 7: let person = undefined — empties the binding**

- [x] With **`let`**, assigning **`undefined`** empties the variable.

Sandbox: `code_sandbox/js-undefined/let-assign-undefined.html`

```javascript
let person = {firstName:"John", lastName:"Doe"};
person = undefined;
```

![js-undefined example 7 source](../code_sandbox/snaps/js-undefined-07-code.png)

![js-undefined example 7 result](../code_sandbox/snaps/js-undefined-07-result.png)

- [x] **Outcome:** person is **undefined**. typeof is **"undefined"**.

<a id="js-undefined-example-08"></a>

### **Example 8: let person = null — emptied with null**

- [x] Objects can also be emptied with **`null`**. typeof becomes **"object"** (legacy).

Sandbox: `code_sandbox/js-undefined/let-assign-null.html`

```javascript
let person = {firstName:"John", lastName:"Doe"};
person = null;
```

![js-undefined example 8 source](../code_sandbox/snaps/js-undefined-08-code.png)

![js-undefined example 8 result](../code_sandbox/snaps/js-undefined-08-result.png)

- [x] **Outcome:** person is **null**. typeof is **"object"**.

<a id="js-undefined-example-09"></a>

### **Example 9: Reading an undeclared name is ReferenceError**

- [x] `typeof missing` is safe. **Reading** `missing` throws **ReferenceError**.
- [x] Declared-but-empty is **undefined**; never-declared is an **error** (except typeof).

Sandbox: `code_sandbox/js-undefined/undeclared-referenceerror.html`

```javascript
missing;
```

![js-undefined example 9 source](../code_sandbox/snaps/js-undefined-09-code.png)

![js-undefined example 9 result](../code_sandbox/snaps/js-undefined-09-result.png)

- [x] **Outcome:** **ReferenceError: missing is not defined**. `typeof missing` would be **"undefined"** without throwing.

<a id="js-undefined-example-10"></a>

### **Example 10: undefined == null is true; === is false**

- [x] `undefined` is a **value** meaning declared but not assigned.
- [x] It is **==** null and **not ===** null.

Sandbox: `code_sandbox/js-undefined/undefined-eq-null.html`

```javascript
undefined == null;
undefined === null;
```

![js-undefined example 10 source](../code_sandbox/snaps/js-undefined-10-code.png)

![js-undefined example 10 result](../code_sandbox/snaps/js-undefined-10-result.png)

- [x] **Outcome:** `==` is **true**. `===` is **false**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-undefined/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the value of `let car;`?

<details>
<summary>Answer</summary>

- [x] **undefined**.

</details>

### Question 2: What is `typeof car` then?

<details>
<summary>Answer</summary>

- [x] **"undefined"**.

</details>

### Question 3: Is `""` undefined?

<details>
<summary>Answer</summary>

- [x] **No.** typeof **"string"**.

</details>

### Question 4: What is `person.age` if age was never set?

<details>
<summary>Answer</summary>

- [x] **undefined**.

</details>

### Question 5: What does a function with no return return?

<details>
<summary>Answer</summary>

- [x] **undefined**.

</details>

### Question 6: Does `const person = {}; person = undefined` work?

<details>
<summary>Answer</summary>

- [x] **No. TypeError: Assignment to constant variable.**

</details>

### Question 7: How do you empty a binding?

<details>
<summary>Answer</summary>

- [x] Use **`let`**, then assign **undefined** or **null**.

</details>

### Question 8: What is `typeof` after assigning null?

<details>
<summary>Answer</summary>

- [x] **"object"** (legacy). After undefined: **"undefined"**.

</details>

### Question 9: What is reading a never-declared `missing`?

<details>
<summary>Answer</summary>

- [x] **ReferenceError: missing is not defined**.
- [x] `typeof missing` is still **"undefined"**.

</details>

### Question 10: Is `undefined == null`?

<details>
<summary>Answer</summary>

- [x] **true**. `===` is **false**.

</details>

### Question 11: Does undefined mean the variable does not exist?

<details>
<summary>Answer</summary>

- [x] **No.** It exists but has **no assigned value**. Never-declared is a **ReferenceError**.

</details>


</details>

## Summary

undefined is a value, not a missing binding. Empty string and null are different. const cannot be emptied by assignment. typeof is the safe probe for undeclared names.

## References

- [JS undefined (W3Schools)](https://www.w3schools.com/js/js_undefined.asp)
- [MDN: undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
- [MDN: ReferenceError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
