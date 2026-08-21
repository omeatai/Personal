# JS Set WeakSet

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A WeakSet holds objects weakly so they can be garbage collected when nothing else references them. add, delete, and has are the whole API. Primitives throw TypeError: Invalid value used in weak set. WeakSets are not iterable, have no size, and have no clear or logic methods. The visitor demo tracks first vs again without storing counts.

This section has **9** examples:

- [x] **Example 1:** new WeakSet() [View](#js-set-weakset-example-01)
- [x] **Example 2:** add(object) then has(object) [View](#js-set-weakset-example-02)
- [x] **Example 3:** delete(object) then has(object) [View](#js-set-weakset-example-03)
- [x] **Example 4:** has() is by reference [View](#js-set-weakset-example-04)
- [x] **Example 5:** Primitives throw on add() [View](#js-set-weakset-example-05)
- [x] **Example 6:** WeakSet is not iterable [View](#js-set-weakset-example-06)
- [x] **Example 7:** No size, clear(), or logic methods [View](#js-set-weakset-example-07)
- [x] **Example 8:** Track visitors with WeakSet [View](#js-set-weakset-example-08)
- [x] **Example 9:** Dropping the only reference (GC) [View](#js-set-weakset-example-09)

## Detailed Explanation

- [x] Values must be **objects**. `add('hello')` / `add(42)` / `add(null)` throw **Invalid value used in weak set**.
- [x] `has` is **reference** equality — a look-alike object is **false**.
- [x] **Not iterable:** `[...mySet]` → **mySet is not iterable**. No `forEach` / `values()`.
- [x] `size` is **undefined**. `clear()` is not a function. No `union`.
- [x] Visitor text matches the page: **age41** with no space after age. Paul then Ringo then Paul-again.
- [x] After `myObj = null` you cannot look the object up. GC is not a synchronous snapshot.

<a id="js-set-weakset-example-01"></a>

### **Example 1: new WeakSet()**

- [x] `new WeakSet()` creates an empty WeakSet.
- [x] Values **must be objects** (or unregistered symbols). The Set holds them **weakly**.

Sandbox: `code_sandbox/js-set-weakset/new-weakset.html`

```javascript
const mySet = new WeakSet();
```

![js-set-weakset example 1 source](../code_sandbox/snaps/js-set-weakset-01-code.png)

![js-set-weakset example 1 result](../code_sandbox/snaps/js-set-weakset-01-result.png)

- [x] **Outcome:** `typeof` is **object**. `instanceof WeakSet` is **true**.

<a id="js-set-weakset-example-02"></a>

### **Example 2: add(object) then has(object)**

- [x] `add(obj)` stores the object. `has(obj)` is **true** while that same reference is in the WeakSet.

Sandbox: `code_sandbox/js-set-weakset/add-has.html`

```javascript
const mySet = new WeakSet();
let myObj = {fname:"John", lname:"Doe"};
mySet.add(myObj);
const answer = mySet.has(myObj);
```

![js-set-weakset example 2 source](../code_sandbox/snaps/js-set-weakset-02-code.png)

![js-set-weakset example 2 result](../code_sandbox/snaps/js-set-weakset-02-result.png)

- [x] **Outcome:** `has(myObj)` is **true** after `add(myObj)`.

<a id="js-set-weakset-example-03"></a>

### **Example 3: delete(object) then has(object)**

- [x] `delete(obj)` removes that object. `has(obj)` is then **false**.

Sandbox: `code_sandbox/js-set-weakset/delete-has.html`

```javascript
const mySet = new WeakSet();
let myObj = {fname:"John", lname:"Doe"};
mySet.add(myObj);
mySet.delete(myObj);
const answer = mySet.has(myObj);
```

![js-set-weakset example 3 source](../code_sandbox/snaps/js-set-weakset-03-code.png)

![js-set-weakset example 3 result](../code_sandbox/snaps/js-set-weakset-03-result.png)

- [x] **Outcome:** After delete, `has(myObj)` is **false**. A second `delete(myObj)` is also **false**.

<a id="js-set-weakset-example-04"></a>

### **Example 4: has() is by reference**

- [x] Two objects with the same fields are **not** the same WeakSet value.

Sandbox: `code_sandbox/js-set-weakset/has-other-object.html`

```javascript
const mySet = new WeakSet();
const a = {fname:"John", lname:"Doe"};
const b = {fname:"John", lname:"Doe"};
mySet.add(a);
```

![js-set-weakset example 4 source](../code_sandbox/snaps/js-set-weakset-04-code.png)

![js-set-weakset example 4 result](../code_sandbox/snaps/js-set-weakset-04-result.png)

- [x] **Outcome:** `has(a)` is **true**. `has(b)` is **false** — `b` was never added.

<a id="js-set-weakset-example-05"></a>

### **Example 5: Primitives throw on add()**

- [x] Strings, numbers, and `null` **cannot** be WeakSet values.
- [x] V8 throws **TypeError: Invalid value used in weak set**.

Sandbox: `code_sandbox/js-set-weakset/primitive-throws.html`

```javascript
const mySet = new WeakSet();
const obj = {x: 1};
mySet.add(obj);
mySet.add("hello");
```

![js-set-weakset example 5 source](../code_sandbox/snaps/js-set-weakset-05-code.png)

![js-set-weakset example 5 result](../code_sandbox/snaps/js-set-weakset-05-result.png)

- [x] **Outcome:** `add(obj)` works (`has` **true**). `add("hello")` and `add(42)` throw **TypeError: Invalid value used in weak set**. `add(null)` throws the same.

<a id="js-set-weakset-example-06"></a>

### **Example 6: WeakSet is not iterable**

- [x] You **cannot** `for...of`, spread, `forEach`, or `values()` a WeakSet.
- [x] That is by design: members may vanish in garbage collection.

Sandbox: `code_sandbox/js-set-weakset/not-iterable.html`

```javascript
const mySet = new WeakSet();
const obj = {x: 1};
mySet.add(obj);
for (const x of mySet) {}
```

![js-set-weakset example 6 source](../code_sandbox/snaps/js-set-weakset-06-code.png)

![js-set-weakset example 6 result](../code_sandbox/snaps/js-set-weakset-06-result.png)

- [x] **Outcome:** `[...mySet]` and `for...of` throw **TypeError: mySet is not iterable**. `forEach` / `values()` throw **TypeError: mySet.forEach is not a function** (and the same for `values`).

<a id="js-set-weakset-example-07"></a>

### **Example 7: No size, clear(), or logic methods**

- [x] WeakSet has **no** `size`, **no** `clear()`, **no** `union` / `intersection` / …

Sandbox: `code_sandbox/js-set-weakset/no-size-clear-union.html`

```javascript
const mySet = new WeakSet();
mySet.size;
mySet.clear();
```

![js-set-weakset example 7 source](../code_sandbox/snaps/js-set-weakset-07-code.png)

![js-set-weakset example 7 result](../code_sandbox/snaps/js-set-weakset-07-result.png)

- [x] **Outcome:** `mySet.size` is **undefined**. `clear()` throws **TypeError: mySet.clear is not a function**. `typeof mySet.union` is **undefined**.

<a id="js-set-weakset-example-08"></a>

### **Example 8: Track visitors with WeakSet**

- [x] A WeakSet is handy for **membership** (seen / not seen) without extra data.
- [x] The page concatenates with **no space** after `age`.

Sandbox: `code_sandbox/js-set-weakset/track-visitors.html`

```javascript
let text = "";
const persons = new WeakSet();
const John = {name:"John", age:40};
const Paul = {name:"Paul", age:41};
const Ringo = {name:"Ringo", age:42};
const George = {name:"George", age:43};
function track(visitor) {
  if (persons.has(visitor)) {
    text += visitor.name + " is visiting again. ";
  } else {
    persons.add(visitor);
    text += visitor.name + ", age" + visitor.age + ", is visiting for the first time ";
  }
}
track(Paul);
track(Ringo);
track(Paul);
```

![js-set-weakset example 8 source](../code_sandbox/snaps/js-set-weakset-08-code.png)

![js-set-weakset example 8 result](../code_sandbox/snaps/js-set-weakset-08-result.png)

- [x] **Outcome:** text is **"Paul, age41, is visiting for the first time Ringo, age42, is visiting for the first time Paul is visiting again. "** (page spacing). `has(Paul)` is **true**. `has(John)` is **false** — John never called `track`.

<a id="js-set-weakset-example-09"></a>

### **Example 9: Dropping the only reference (GC)**

- [x] If nothing else points at the object, it **may** be garbage collected and dropped from the WeakSet.
- [x] You cannot list remaining members. `has(null)` is invalid.

Sandbox: `code_sandbox/js-set-weakset/gc-null.html`

```javascript
const mySet = new WeakSet();
let myObj = {fname:"John", lname:"Doe"};
mySet.add(myObj);
const held = mySet.has(myObj);
myObj = null;
```

![js-set-weakset example 9 source](../code_sandbox/snaps/js-set-weakset-09-code.png)

![js-set-weakset example 9 result](../code_sandbox/snaps/js-set-weakset-09-result.png)

- [x] **Outcome:** While the binding existed, `has` was **true**. After `myObj = null`, the variable is **null**. `has(null)` throws **TypeError: Invalid value used in weak set**. `[...mySet]` throws **TypeError: mySet is not iterable**. GC itself is **not** observable in the same turn.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-set-weakset/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What methods does WeakSet provide?

<details>
<summary>Answer</summary>

- [x] **add**, **delete**, **has** (plus the constructor).

</details>

### Question 2: What does add(myObj) then has(myObj) return?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 3: What does delete then has return?

<details>
<summary>Answer</summary>

- [x] **false**.

</details>

### Question 4: Does has() match another object with the same fields?

<details>
<summary>Answer</summary>

- [x] **No.** Different reference → **false**.

</details>

### Question 5: What does add('hello') throw?

<details>
<summary>Answer</summary>

- [x] **TypeError: Invalid value used in weak set**.

</details>

### Question 6: Can you for...of a WeakSet?

<details>
<summary>Answer</summary>

- [x] **No.** **TypeError: mySet is not iterable**.

</details>

### Question 7: What is mySet.size?

<details>
<summary>Answer</summary>

- [x] **undefined**.

</details>

### Question 8: What is the visitor text after Paul, Ringo, Paul?

<details>
<summary>Answer</summary>

- [x] **"Paul, age41, is visiting for the first time Ringo, age42, is visiting for the first time Paul is visiting again. "**

</details>

### Question 9: Did John visit in that demo?

<details>
<summary>Answer</summary>

- [x] **No.** `has(John)` is **false**.

</details>

### Question 10: Can you has(null) after nulling the object?

<details>
<summary>Answer</summary>

- [x] **No.** **Invalid value used in weak set**.

</details>


</details>

## Summary

Use WeakSet for object membership you do not want to keep alive. Stick to add/delete/has. Do not iterate, count, or store primitives.

## References

- [JS WeakSet (W3Schools)](https://www.w3schools.com/js/js_sets_weak.asp)
- [MDN: WeakSet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)
