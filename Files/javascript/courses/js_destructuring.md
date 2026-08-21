# JS Destructuring

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Destructuring unpacks objects and iterables into bindings without changing the source. Object patterns match by name (order does not matter) and can set defaults or rename with {lastName: name}. Array patterns match by position; extra commas skip holes; ...rest gathers the tail; {[0]: x} picks an index by name. Nested patterns unpack inner objects and arrays. Map loops yield [key, value] pairs. [a, b] = [b, a] swaps. Strings destructure into characters because they are iterable.

This section has **16** examples:

- [x] **Example 1:** Object destructuring — {firstName, lastName} [View](#js-destructuring-example-01)
- [x] **Example 2:** Object destructuring — order does not matter [View](#js-destructuring-example-02)
- [x] **Example 3:** Object default — country = "US" [View](#js-destructuring-example-03)
- [x] **Example 4:** Object alias — {lastName : name} [View](#js-destructuring-example-04)
- [x] **Example 5:** String destructuring — characters [View](#js-destructuring-example-05)
- [x] **Example 6:** Array destructuring — first two [View](#js-destructuring-example-06)
- [x] **Example 7:** Array skip — [fruit1,,,fruit2] [View](#js-destructuring-example-07)
- [x] **Example 8:** Array position values — {[0]:fruit1, [1]:fruit2} [View](#js-destructuring-example-08)
- [x] **Example 9:** Array rest — [a, b, ...rest] [View](#js-destructuring-example-09)
- [x] **Example 10:** Array defaults — [a = 'A', b = 'B'] [View](#js-destructuring-example-10)
- [x] **Example 11:** Object rest — {firstName, ...rest} [View](#js-destructuring-example-11)
- [x] **Example 12:** Nested object destructuring [View](#js-destructuring-example-12)
- [x] **Example 13:** Nested array destructuring [View](#js-destructuring-example-13)
- [x] **Example 14:** Destructuring Map entries in for...of [View](#js-destructuring-example-14)
- [x] **Example 15:** Swap two variables [View](#js-destructuring-example-15)
- [x] **Example 16:** Destructuring does not change the source [View](#js-destructuring-example-16)

## Detailed Explanation

- [x] Objects: `{firstName, lastName}`, defaults `{country = "US"}`, alias `{lastName: name}`, rest `{firstName, ...rest}`.
- [x] Arrays: `[a, b]`, skip `[a, , , b]`, index `{[0]: a}`, rest `[a, b, ...rest]`, defaults `[a = "A", b = "B"]`.
- [x] **Nested:** `{ address: { city } }` and `[a, [b, c], d]`.
- [x] **Swap:** `[firstName, lastName] = [lastName, firstName]` → **Doe / John**.
- [x] Not destructive: changing the binding does **not** change the source object.

<a id="js-destructuring-example-01"></a>

### **Example 1: Object destructuring — {firstName, lastName}**

- [x] Object destructuring unpacks **matching property names** into variables.

Sandbox: `code_sandbox/js-destructuring/object-basic.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50
};
let {firstName, lastName} = person;
```

![js-destructuring example 1 source](../code_sandbox/snaps/js-destructuring-01-code.png)

![js-destructuring example 1 result](../code_sandbox/snaps/js-destructuring-01-result.png)

- [x] **Outcome:** firstName is **"John"**. lastName is **"Doe"**. age is not unpacked.

<a id="js-destructuring-example-02"></a>

### **Example 2: Object destructuring — order does not matter**

- [x] You may list properties in **any order**. Names match, not positions.

Sandbox: `code_sandbox/js-destructuring/object-order.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50
};
let {lastName, firstName} = person;
```

![js-destructuring example 2 source](../code_sandbox/snaps/js-destructuring-02-code.png)

![js-destructuring example 2 result](../code_sandbox/snaps/js-destructuring-02-result.png)

- [x] **Outcome:** Still **"John"** and **"Doe"** — swapping the names in `{ }` does not swap the values.

<a id="js-destructuring-example-03"></a>

### **Example 3: Object default — country = "US"**

- [x] Missing properties can take a **default**. Present properties keep their value.

Sandbox: `code_sandbox/js-destructuring/object-defaults.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50
};
let {firstName, lastName, country = "US"} = person;
```

![js-destructuring example 3 source](../code_sandbox/snaps/js-destructuring-03-code.png)

![js-destructuring example 3 result](../code_sandbox/snaps/js-destructuring-03-result.png)

- [x] **Outcome:** country is **"US"** (default). firstName/lastName still **"John"** / **"Doe"**. The original object is unchanged.

<a id="js-destructuring-example-04"></a>

### **Example 4: Object alias — {lastName : name}**

- [x] `{lastName : name}` reads **lastName** into a variable called **name**.

Sandbox: `code_sandbox/js-destructuring/object-alias.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50
};
let {lastName: name} = person;
```

![js-destructuring example 4 source](../code_sandbox/snaps/js-destructuring-04-code.png)

![js-destructuring example 4 result](../code_sandbox/snaps/js-destructuring-04-result.png)

- [x] **Outcome:** name is **"Doe"**. There is no `lastName` binding from this pattern.

<a id="js-destructuring-example-05"></a>

### **Example 5: String destructuring — characters**

- [x] Strings are **iterable**. Destructuring takes characters in order.

Sandbox: `code_sandbox/js-destructuring/string-chars.html`

```javascript
let name = "W3Schools";
let [a1, a2, a3, a4, a5] = name;
```

![js-destructuring example 5 source](../code_sandbox/snaps/js-destructuring-05-code.png)

![js-destructuring example 5 result](../code_sandbox/snaps/js-destructuring-05-result.png)

- [x] **Outcome:** a1–a5 are **"W"**, **"3"**, **"S"**, **"c"**, **"h"**.

<a id="js-destructuring-example-06"></a>

### **Example 6: Array destructuring — first two**

- [x] Array patterns bind by **position**: first variable ← index 0.

Sandbox: `code_sandbox/js-destructuring/array-basic.html`

```javascript
const fruits = ["Bananas", "Oranges", "Apples", "Mangos"];
let [fruit1, fruit2] = fruits;
```

![js-destructuring example 6 source](../code_sandbox/snaps/js-destructuring-06-code.png)

![js-destructuring example 6 result](../code_sandbox/snaps/js-destructuring-06-result.png)

- [x] **Outcome:** fruit1 is **"Bananas"**. fruit2 is **"Oranges"**.

<a id="js-destructuring-example-07"></a>

### **Example 7: Array skip — [fruit1,,,fruit2]**

- [x] Extra **commas skip** holes. `[a,,,b]` takes index **0** and index **3**.

Sandbox: `code_sandbox/js-destructuring/array-skip.html`

```javascript
const fruits = ["Bananas", "Oranges", "Apples", "Mangos"];
let [fruit1, , , fruit2] = fruits;
```

![js-destructuring example 7 source](../code_sandbox/snaps/js-destructuring-07-code.png)

![js-destructuring example 7 result](../code_sandbox/snaps/js-destructuring-07-result.png)

- [x] **Outcome:** fruit1 is **"Bananas"**. fruit2 is **"Mangos"** (Oranges and Apples skipped).

<a id="js-destructuring-example-08"></a>

### **Example 8: Array position values — {[0]:fruit1, [1]:fruit2}**

- [x] You can pick **named indexes** with computed property names on the pattern.

Sandbox: `code_sandbox/js-destructuring/array-index-names.html`

```javascript
const fruits = ["Bananas", "Oranges", "Apples", "Mangos"];
let {[0]: fruit1, [1]: fruit2} = fruits;
```

![js-destructuring example 8 source](../code_sandbox/snaps/js-destructuring-08-code.png)

![js-destructuring example 8 result](../code_sandbox/snaps/js-destructuring-08-result.png)

- [x] **Outcome:** fruit1 is **"Bananas"**. fruit2 is **"Oranges"**.

<a id="js-destructuring-example-09"></a>

### **Example 9: Array rest — [a, b, ...rest]**

- [x] **`...rest`** gathers **remaining** elements into a **new array**.

Sandbox: `code_sandbox/js-destructuring/array-rest.html`

```javascript
const numbers = [10, 20, 30, 40, 50, 60, 70];
const [a, b, ...rest] = numbers;
```

![js-destructuring example 9 source](../code_sandbox/snaps/js-destructuring-09-code.png)

![js-destructuring example 9 result](../code_sandbox/snaps/js-destructuring-09-result.png)

- [x] **Outcome:** a is **10**, b is **20**, rest is **30,40,50,60,70**.

<a id="js-destructuring-example-10"></a>

### **Example 10: Array defaults — [a = 'A', b = 'B']**

- [x] Array holes / missing items take **defaults**, same idea as object defaults.

Sandbox: `code_sandbox/js-destructuring/array-defaults.html`

```javascript
let [a = "A", b = "B"] = ["Bananas"];
```

![js-destructuring example 10 source](../code_sandbox/snaps/js-destructuring-10-code.png)

![js-destructuring example 10 result](../code_sandbox/snaps/js-destructuring-10-result.png)

- [x] **Outcome:** a is **"Bananas"** (provided). b is **"B"** (default).

<a id="js-destructuring-example-11"></a>

### **Example 11: Object rest — {firstName, ...rest}**

- [x] Object **`...rest`** is a **new object** of the leftover enumerable string keys.

Sandbox: `code_sandbox/js-destructuring/object-rest.html`

```javascript
const person = { firstName: "John", lastName: "Doe", age: 50 };
let {firstName, ...rest} = person;
```

![js-destructuring example 11 source](../code_sandbox/snaps/js-destructuring-11-code.png)

![js-destructuring example 11 result](../code_sandbox/snaps/js-destructuring-11-result.png)

- [x] **Outcome:** firstName is **"John"**. rest is **{"lastName":"Doe","age":50}**.

<a id="js-destructuring-example-12"></a>

### **Example 12: Nested object destructuring**

- [x] Nest patterns to unpack **inner** objects: `{ address: { city } }`.

Sandbox: `code_sandbox/js-destructuring/nested-object.html`

```javascript
const user = {
  name: "John",
  address: { city: "Oslo", zip: "0001" }
};
let { name, address: { city, zip } } = user;
```

![js-destructuring example 12 source](../code_sandbox/snaps/js-destructuring-12-code.png)

![js-destructuring example 12 result](../code_sandbox/snaps/js-destructuring-12-result.png)

- [x] **Outcome:** name **"John"**, city **"Oslo"**, zip **"0001"**. There is no `address` binding unless you also name it.

<a id="js-destructuring-example-13"></a>

### **Example 13: Nested array destructuring**

- [x] Nest `[ ]` inside `[ ]` to unpack inner arrays.

Sandbox: `code_sandbox/js-destructuring/nested-array.html`

```javascript
const pair = [1, [2, 3], 4];
let [a, [b, c], d] = pair;
```

![js-destructuring example 13 source](../code_sandbox/snaps/js-destructuring-13-code.png)

![js-destructuring example 13 result](../code_sandbox/snaps/js-destructuring-13-result.png)

- [x] **Outcome:** a **1**, b **2**, c **3**, d **4**.

<a id="js-destructuring-example-14"></a>

### **Example 14: Destructuring Map entries in for...of**

- [x] Maps iterate as **`[key, value]`** pairs — destructure them in the loop.

Sandbox: `code_sandbox/js-destructuring/map-entries.html`

```javascript
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);
let text = "";
for (const [key, value] of fruits) {
  text += key + " is " + value;
}
```

![js-destructuring example 14 source](../code_sandbox/snaps/js-destructuring-14-code.png)

![js-destructuring example 14 result](../code_sandbox/snaps/js-destructuring-14-result.png)

- [x] **Outcome:** text is **"apples is 500bananas is 300oranges is 200"** (no extra spaces between entries — as written).

<a id="js-destructuring-example-15"></a>

### **Example 15: Swap two variables**

- [x] `[a, b] = [b, a]` **swaps** without a temp variable.

Sandbox: `code_sandbox/js-destructuring/swap.html`

```javascript
let firstName = "John";
let lastName = "Doe";
[firstName, lastName] = [lastName, firstName];
```

![js-destructuring example 15 source](../code_sandbox/snaps/js-destructuring-15-code.png)

![js-destructuring example 15 result](../code_sandbox/snaps/js-destructuring-15-result.png)

- [x] **Outcome:** After the swap, firstName is **"Doe"**. lastName is **"John"**.

<a id="js-destructuring-example-16"></a>

### **Example 16: Destructuring does not change the source**

- [x] Unpacking copies values into bindings. The **original** object/array stays.

Sandbox: `code_sandbox/js-destructuring/not-destructive.html`

```javascript
const person = { firstName: "John", lastName: "Doe" };
let { firstName } = person;
firstName = "Jane";
```

![js-destructuring example 16 source](../code_sandbox/snaps/js-destructuring-16-code.png)

![js-destructuring example 16 result](../code_sandbox/snaps/js-destructuring-16-result.png)

- [x] **Outcome:** The variable is **"Jane"**. person.firstName is still **"John"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-destructuring/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does property order matter in object destructuring?

<details>
<summary>Answer</summary>

- [x] **No.** `{lastName, firstName}` still gets John and Doe.

</details>

### Question 2: What is `country` when it is missing and defaulted to `"US"`?

<details>
<summary>Answer</summary>

- [x] **"US"**.

</details>

### Question 3: What is `{lastName: name}`?

<details>
<summary>Answer</summary>

- [x] A variable **name** holding **"Doe"**.

</details>

### Question 4: What are a1–a5 of `"W3Schools"`?

<details>
<summary>Answer</summary>

- [x] **W, 3, S, c, h**.

</details>

### Question 5: What is `[fruit1, fruit2]` of the fruits array?

<details>
<summary>Answer</summary>

- [x] **"Bananas"**, **"Oranges"**.

</details>

### Question 6: What is `[fruit1,,,fruit2]`?

<details>
<summary>Answer</summary>

- [x] **"Bananas"** and **"Mangos"** (two skipped).

</details>

### Question 7: What is `[a, b, ...rest]` of 10..70?

<details>
<summary>Answer</summary>

- [x] a **10**, b **20**, rest **30,40,50,60,70**.

</details>

### Question 8: What is object rest after taking firstName?

<details>
<summary>Answer</summary>

- [x] **{"lastName":"Doe","age":50}**.

</details>

### Question 9: What does nested `{ address: { city, zip } }` bind?

<details>
<summary>Answer</summary>

- [x] city **"Oslo"**, zip **"0001"**. Not `address` unless named.

</details>

### Question 10: What is the Map loop text?

<details>
<summary>Answer</summary>

- [x] **"apples is 500bananas is 300oranges is 200"** — no extra separators.

</details>

### Question 11: How do you swap firstName and lastName?

<details>
<summary>Answer</summary>

- [x] `[firstName, lastName] = [lastName, firstName]` → **Doe**, **John**.

</details>

### Question 12: Does destructuring mutate the object?

<details>
<summary>Answer</summary>

- [x] **No.** Assigning the binding leaves **person.firstName** **"John"**.

</details>

### Question 13: What is array default `b` when only one element is provided?

<details>
<summary>Answer</summary>

- [x] The default **"B"**.

</details>


</details>

## Summary

Match objects by name and arrays by position. Use defaults, aliases, rest, skips, and nesting as separate patterns. Swapping with a destructuring assignment is the temp-free idiom. The source value is not mutated.

## References

- [JS Destructuring (W3Schools)](https://www.w3schools.com/js/js_destructuring.asp)
- [MDN: Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
