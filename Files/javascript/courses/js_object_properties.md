# JS Object Properties

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A JavaScript object is a collection of properties you can read, change, add, and delete. Access a key with a dot, with brackets, or with an expression in brackets. Nested objects chain those same forms. The in operator checks whether a key exists. Assume a person with firstName John, lastName Doe, and age 50 unless an example defines something else.

This section has **13** examples:

- [x] **Example 1:** Dot: person.firstName + age [View](#js-object-properties-example-01)
- [x] **Example 2:** Bracket: person["firstName"] + age [View](#js-object-properties-example-02)
- [x] **Example 3:** Property names in variables (page typo + fix) [View](#js-object-properties-example-03)
- [x] **Example 4:** Expression access: person[x] [View](#js-object-properties-example-04)
- [x] **Example 5:** person.age = 10 [View](#js-object-properties-example-05)
- [x] **Example 6:** person.nationality = "English" [View](#js-object-properties-example-06)
- [x] **Example 7:** delete person.age [View](#js-object-properties-example-07)
- [x] **Example 8:** delete person["age"] [View](#js-object-properties-example-08)
- [x] **Example 9:** "firstName" in person [View](#js-object-properties-example-09)
- [x] **Example 10:** Nested: myObj.myCars.car2 [View](#js-object-properties-example-10)
- [x] **Example 11:** Nested: myObj.myCars["car2"] [View](#js-object-properties-example-11)
- [x] **Example 12:** Nested: myObj["myCars"]["car2"] [View](#js-object-properties-example-12)
- [x] **Example 13:** Nested: myObj[p1][p2] [View](#js-object-properties-example-13)

## Detailed Explanation

- [x] **Dot** `person.firstName` is preferred when the name is a valid identifier.
- [x] **Brackets** `person["firstName"]` or `person[x]` are required for variables and unusual names.
- [x] `delete` removes the property. **`in`** tests whether it exists.
- [x] The W3Schools Tryits use `person.firstname` (lowercase n). The object key is **`firstName`** — we use that so the demos are not undefined.

<a id="js-object-properties-example-01"></a>

### **Example 1: Dot: person.firstName + age**

- [x] Dot notation: `person.firstName` and `person.age`.
- [x] The W3Schools Tryit writes `person.firstname` (lowercase **n**). This object uses **`firstName`**, so that page spelling would be **undefined** — we use `firstName`.

Sandbox: `code_sandbox/js-object-properties/dot-access.html`

```javascript
const person = { firstName: "John", lastName: "Doe", age: 50 };
let text = person.firstName + " is " + person.age;
```

![js-object-properties example 1 source](../code_sandbox/snaps/js-object-properties-01-code.png)

![js-object-properties example 1 result](../code_sandbox/snaps/js-object-properties-01-result.png)

- [x] **Outcome:** text is **"John is 50"**.

<a id="js-object-properties-example-02"></a>

### **Example 2: Bracket: person["firstName"] + age**

- [x] `person["firstName"]` is the same value as `person.firstName`.
- [x] The page again uses `firstname` in the Tryit — we keep **`firstName`** so the result is not undefined.

Sandbox: `code_sandbox/js-object-properties/bracket-access.html`

```javascript
const person = { firstName: "John", lastName: "Doe", age: 50 };
let text = person["firstName"] + " is " + person["age"];
```

![js-object-properties example 2 source](../code_sandbox/snaps/js-object-properties-02-code.png)

![js-object-properties example 2 result](../code_sandbox/snaps/js-object-properties-02-result.png)

- [x] **Outcome:** text is **"John is 50"**.

<a id="js-object-properties-example-03"></a>

### **Example 3: Property names in variables (page typo + fix)**

- [x] Brackets can take a **variable** that holds the key name.
- [x] The page runs `person[n2] + " " + person[n2]` (both **n2**) — that prints **Doe Doe**. The clarifying row uses `n1` then `n2`.

Sandbox: `code_sandbox/js-object-properties/variable-names.html`

```javascript
const person = { firstName: "John", lastName: "Doe", age: 50 };
let n1 = "firstName";
let n2 = "lastName";
let name = person[n2] + " " + person[n2];
let clarified = person[n1] + " " + person[n2];
```

![js-object-properties example 3 source](../code_sandbox/snaps/js-object-properties-03-code.png)

![js-object-properties example 3 result](../code_sandbox/snaps/js-object-properties-03-result.png)

- [x] **Outcome:** Page code is **"Doe Doe"**. Clarifying example is **"John Doe"**.

<a id="js-object-properties-example-04"></a>

### **Example 4: Expression access: person[x]**

- [x] The third access form is **`objectName[expression]`**.
- [x] If `x` holds `"age"`, then `person[x]` is `person.age`. This is the named construct from the page (not the n1/n2 Tryit).

Sandbox: `code_sandbox/js-object-properties/expression-access.html`

```javascript
const person = { firstName: "John", lastName: "Doe", age: 50 };
let x = "age";
let age = person[x];
```

![js-object-properties example 4 source](../code_sandbox/snaps/js-object-properties-04-code.png)

![js-object-properties example 4 result](../code_sandbox/snaps/js-object-properties-04-result.png)

- [x] **Outcome:** x is **"age"**; age is **50**.

<a id="js-object-properties-example-05"></a>

### **Example 5: person.age = 10**

- [x] Assign a new value to **change** a property.
- [x] `person.age = 10` overwrites **50**.

Sandbox: `code_sandbox/js-object-properties/change-age.html`

```javascript
const person = { firstName: "John", lastName: "Doe", age: 50 };
person.age = 10;
```

![js-object-properties example 5 source](../code_sandbox/snaps/js-object-properties-05-code.png)

![js-object-properties example 5 result](../code_sandbox/snaps/js-object-properties-05-result.png)

- [x] **Outcome:** person.age is **10**.

<a id="js-object-properties-example-06"></a>

### **Example 6: person.nationality = "English"**

- [x] Assigning a **new name** adds a property.
- [x] `nationality` did not exist before this line.

Sandbox: `code_sandbox/js-object-properties/add-nationality.html`

```javascript
const person = { firstName: "John", lastName: "Doe", age: 50 };
person.nationality = "English";
```

![js-object-properties example 6 source](../code_sandbox/snaps/js-object-properties-06-code.png)

![js-object-properties example 6 result](../code_sandbox/snaps/js-object-properties-06-result.png)

- [x] **Outcome:** person.nationality is **"English"**.

<a id="js-object-properties-example-07"></a>

### **Example 7: delete person.age**

- [x] `delete` removes **both** the value and the property.
- [x] Reading it afterward is **undefined**. `"age" in person` is **false**.

Sandbox: `code_sandbox/js-object-properties/delete-dot.html`

```javascript
const person = { firstName: "John", lastName: "Doe", age: 50 };
delete person.age;
```

![js-object-properties example 7 source](../code_sandbox/snaps/js-object-properties-07-code.png)

![js-object-properties example 7 result](../code_sandbox/snaps/js-object-properties-07-result.png)

- [x] **Outcome:** person.age is **undefined**. `"age" in person` is **false**.

<a id="js-object-properties-example-08"></a>

### **Example 8: delete person["age"]**

- [x] The same delete with **bracket** notation.
- [x] The page repeats delete with `person["age"]` — same outcome as the dot form.

Sandbox: `code_sandbox/js-object-properties/delete-bracket.html`

```javascript
const person = { firstName: "John", lastName: "Doe", age: 50 };
delete person["age"];
```

![js-object-properties example 8 source](../code_sandbox/snaps/js-object-properties-08-code.png)

![js-object-properties example 8 result](../code_sandbox/snaps/js-object-properties-08-result.png)

- [x] **Outcome:** person.age is **undefined**. `"age" in person` is **false**.

<a id="js-object-properties-example-09"></a>

### **Example 9: "firstName" in person**

- [x] The **`in`** operator is **true** if the property exists (own or inherited).
- [x] This Tryit’s person has `firstName` and `lastName` only — no `age`.

Sandbox: `code_sandbox/js-object-properties/in-operator.html`

```javascript
const person = { firstName: "John", lastName: "Doe" };
let hasFirst = "firstName" in person;
let hasAge = "age" in person;
```

![js-object-properties example 9 source](../code_sandbox/snaps/js-object-properties-09-code.png)

![js-object-properties example 9 result](../code_sandbox/snaps/js-object-properties-09-result.png)

- [x] **Outcome:** `"firstName" in person` is **true**. `"age" in person` is **false**.

<a id="js-object-properties-example-10"></a>

### **Example 10: Nested: myObj.myCars.car2**

- [x] A property value can be **another object**.
- [x] Chain dots: `myObj.myCars.car2`.

Sandbox: `code_sandbox/js-object-properties/nested-dot.html`

```javascript
const myObj = {
  name: "John",
  age: 30,
  myCars: {
    car1: "Ford",
    car2: "BMW",
    car3: "Fiat",
  },
};
```

![js-object-properties example 10 source](../code_sandbox/snaps/js-object-properties-10-code.png)

![js-object-properties example 10 result](../code_sandbox/snaps/js-object-properties-10-result.png)

- [x] **Outcome:** myObj.myCars.car2 is **"BMW"**.

<a id="js-object-properties-example-11"></a>

### **Example 11: Nested: myObj.myCars["car2"]**

- [x] Mix **dot** on the outer object with **brackets** on the inner key.
- [x] Useful when the inner name is not a valid identifier.

Sandbox: `code_sandbox/js-object-properties/nested-dot-bracket.html`

```javascript
const myObj = {
  name: "John",
  age: 30,
  myCars: { car1: "Ford", car2: "BMW", car3: "Fiat" },
};
```

![js-object-properties example 11 source](../code_sandbox/snaps/js-object-properties-11-code.png)

![js-object-properties example 11 result](../code_sandbox/snaps/js-object-properties-11-result.png)

- [x] **Outcome:** Still **"BMW"**.

<a id="js-object-properties-example-12"></a>

### **Example 12: Nested: myObj["myCars"]["car2"]**

- [x] Both levels can use **brackets**.
- [x] Equivalent to the mixed form above.

Sandbox: `code_sandbox/js-object-properties/nested-brackets.html`

```javascript
const myObj = {
  name: "John",
  age: 30,
  myCars: { car1: "Ford", car2: "BMW", car3: "Fiat" },
};
```

![js-object-properties example 12 source](../code_sandbox/snaps/js-object-properties-12-code.png)

![js-object-properties example 12 result](../code_sandbox/snaps/js-object-properties-12-result.png)

- [x] **Outcome:** Still **"BMW"**.

<a id="js-object-properties-example-13"></a>

### **Example 13: Nested: myObj[p1][p2]**

- [x] Store each key in a variable, then chain **bracket** access.
- [x] `p1` is `"myCars"`, `p2` is `"car2"`.

Sandbox: `code_sandbox/js-object-properties/nested-variables.html`

```javascript
const myObj = {
  name: "John",
  age: 30,
  myCars: { car1: "Ford", car2: "BMW", car3: "Fiat" },
};
let p1 = "myCars";
let p2 = "car2";
let car = myObj[p1][p2];
```

![js-object-properties example 13 source](../code_sandbox/snaps/js-object-properties-13-code.png)

![js-object-properties example 13 result](../code_sandbox/snaps/js-object-properties-13-result.png)

- [x] **Outcome:** car is **"BMW"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-object-properties/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `person.firstName + " is " + person.age`?

<details>
<summary>Answer</summary>

- [x] **"John is 50"**.
- [x] Use `firstName` (capital N). The page’s `firstname` would be undefined.

</details>

### Question 2: What is `person["firstName"] + " is " + person["age"]`?

<details>
<summary>Answer</summary>

- [x] **"John is 50"** — same as the dot form.

</details>

### Question 3: What does the page’s `person[n2] + " " + person[n2]` print?

<details>
<summary>Answer</summary>

- [x] **"Doe Doe"** — both lookups use **n2** (`lastName`).
- [x] Clarifying: `person[n1] + " " + person[n2]` is **"John Doe"**.

</details>

### Question 4: What is `person[x]` if `x` is `"age"`?

<details>
<summary>Answer</summary>

- [x] **50** — expression access.

</details>

### Question 5: What is `person.age` after `person.age = 10`?

<details>
<summary>Answer</summary>

- [x] **10**.

</details>

### Question 6: What does `person.nationality = "English"` do?

<details>
<summary>Answer</summary>

- [x] It **adds** a new property. Value **"English"**.

</details>

### Question 7: What is `person.age` after `delete person.age`?

<details>
<summary>Answer</summary>

- [x] **undefined**. `"age" in person` is **false**.

</details>

### Question 8: Is `delete person["age"]` different from `delete person.age`?

<details>
<summary>Answer</summary>

- [x] **No.** Same deletion; the page shows both Tryits.

</details>

### Question 9: What is `"firstName" in person`?

<details>
<summary>Answer</summary>

- [x] **true** if the object has that key (this Tryit person has firstName and lastName only).

</details>

### Question 10: What is `myObj.myCars.car2`?

<details>
<summary>Answer</summary>

- [x] **"BMW"**.

</details>

### Question 11: What are `myObj.myCars["car2"]` and `myObj["myCars"]["car2"]`?

<details>
<summary>Answer</summary>

- [x] Both **"BMW"**.

</details>

### Question 12: What is `myObj[p1][p2]` with p1 `myCars` and p2 `car2`?

<details>
<summary>Answer</summary>

- [x] **"BMW"**.

</details>

### Question 13: When must you use brackets instead of dots?

<details>
<summary>Answer</summary>

- [x] When the name is in a **variable**, or is not a valid identifier (for example `"last-name"`).

</details>

### Question 14: Does delete remove the property or only the value?

<details>
<summary>Answer</summary>

- [x] **Both.** The key is gone afterward.

</details>

</details>

## Summary

Read properties with dots, brackets, or an expression in brackets. Change by assigning, add by assigning a new name, remove with delete, and test with in. Nested objects chain the same access forms. Watch firstName vs firstname, and the page’s n2/n2 typo.

## References

- [JS Object Properties (W3Schools)](https://www.w3schools.com/js/js_object_properties.asp)
- [MDN: Property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
- [MDN: delete](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
- [MDN: in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
