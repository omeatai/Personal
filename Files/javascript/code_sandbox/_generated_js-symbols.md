<details>
  <summary>JS Symbols</summary>

## Introduction

A Symbol is a unique primitive identifier. Symbol() is never === another Symbol(), even with the same description — the description is only for debugging. Symbol.for(key) reuses a global registry, so the same key returns the same symbol. Symbol keys on objects are skipped by for...in and JSON.stringify, and they do not create a string property like person.id. Well-known symbols (iterator, asyncIterator, toStringTag, toPrimitive) hook language behavior. Implicit Symbol + string throws TypeError; use String(sym).

This section has **14** examples:

- [x] **Example 1:** Symbol() === Symbol() is false [View](#js-symbols-example-01)
- [x] **Example 2:** Symbol("id") === Symbol("id") is false [View](#js-symbols-example-02)
- [x] **Example 3:** Symbol as an object key [View](#js-symbols-example-03)
- [x] **Example 4:** typeof Symbol("id") is "symbol" [View](#js-symbols-example-04)
- [x] **Example 5:** person[id] vs person.id [View](#js-symbols-example-05)
- [x] **Example 6:** for...in ignores symbol keys [View](#js-symbols-example-06)
- [x] **Example 7:** JSON.stringify ignores symbol keys [View](#js-symbols-example-07)
- [x] **Example 8:** Symbol.for("id") is reused [View](#js-symbols-example-08)
- [x] **Example 9:** Symbol.keyFor — registry lookup [View](#js-symbols-example-09)
- [x] **Example 10:** Symbol + string is TypeError [View](#js-symbols-example-10)
- [x] **Example 11:** Symbol.iterator — custom for...of [View](#js-symbols-example-11)
- [x] **Example 12:** Symbol.asyncIterator (well-known) [View](#js-symbols-example-12)
- [x] **Example 13:** Symbol.toStringTag [View](#js-symbols-example-13)
- [x] **Example 14:** Symbol.toPrimitive [View](#js-symbols-example-14)

## Detailed Explanation

- [x] `Symbol()` is always **unique**. `Symbol("id") === Symbol("id")` is **false**.
- [x] `Symbol.for("id") === Symbol.for("id")` is **true**. `Symbol.keyFor` reads the registry key.
- [x] Symbol keys are hidden from **for...in** and **JSON.stringify**. `person.id` stays **undefined**.
- [x] `typeof` a symbol is **"symbol"**. `Symbol + ""` is **TypeError**.
- [x] Well-known: **iterator**, **asyncIterator**, **toStringTag**, **toPrimitive**.

<a id="js-symbols-example-01"></a>

### **Example 1: Symbol() === Symbol() is false**

- [x] Every `Symbol()` call creates a **new unique** value, even with no description.

Sandbox: `code_sandbox/js-symbols/symbol-unique.html`

```javascript
const id1 = Symbol();
const id2 = Symbol();
let result = (id1 === id2);
```

<img alt="js-symbols example 1 source" src="./code_sandbox/snaps/js-symbols-01-code.png" />

<img alt="js-symbols example 1 result" src="./code_sandbox/snaps/js-symbols-01-result.png" />

- [x] **Outcome:** result is **false**. typeof is **"symbol"**.

<a id="js-symbols-example-02"></a>

### **Example 2: Symbol("id") === Symbol("id") is false**

- [x] The description is **only for debugging**. It does **not** make two symbols equal.

Sandbox: `code_sandbox/js-symbols/symbol-same-description.html`

```javascript
const id1 = Symbol("id");
const id2 = Symbol("id");
let result = (id1 === id2);
```

<img alt="js-symbols example 2 source" src="./code_sandbox/snaps/js-symbols-02-code.png" />

<img alt="js-symbols example 2 result" src="./code_sandbox/snaps/js-symbols-02-result.png" />

- [x] **Outcome:** result is **false**. String(id1) is **"Symbol(id)"**.

<a id="js-symbols-example-03"></a>

### **Example 3: Symbol as an object key**

- [x] Symbols are often used as **hidden / unique property keys**: `person[id]`.

Sandbox: `code_sandbox/js-symbols/symbol-object-key.html`

```javascript
const id = Symbol("id");
const person = { firstName: "John", lastName: "Doe" };
person[id] = 123;
```

<img alt="js-symbols example 3 source" src="./code_sandbox/snaps/js-symbols-03-code.png" />

<img alt="js-symbols example 3 result" src="./code_sandbox/snaps/js-symbols-03-result.png" />

- [x] **Outcome:** person[id] is **123**. firstName is still **"John"**.

<a id="js-symbols-example-04"></a>

### **Example 4: typeof Symbol("id") is "symbol"**

- [x] Symbol is a **primitive**. `typeof` is **"symbol"**, not "object".

Sandbox: `code_sandbox/js-symbols/symbol-typeof.html`

```javascript
const id = Symbol("id");
let type = typeof id;
```

<img alt="js-symbols example 4 source" src="./code_sandbox/snaps/js-symbols-04-code.png" />

<img alt="js-symbols example 4 result" src="./code_sandbox/snaps/js-symbols-04-result.png" />

- [x] **Outcome:** type is **"symbol"**.

<a id="js-symbols-example-05"></a>

### **Example 5: person[id] vs person.id**

- [x] `person[id]` (symbol key) does **not** create `person.id` (string key).
- [x] Two programmers adding `id` as a **string** can clash; **Symbol** keys do not.

Sandbox: `code_sandbox/js-symbols/symbol-hidden-vs-id.html`

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};
let id = Symbol("id");
person[id] = 140353;
```

<img alt="js-symbols example 5 source" src="./code_sandbox/snaps/js-symbols-05-code.png" />

<img alt="js-symbols example 5 result" src="./code_sandbox/snaps/js-symbols-05-result.png" />

- [x] **Outcome:** person[id] is **140353**. person.id (string key) is **undefined**.

<a id="js-symbols-example-06"></a>

### **Example 6: for...in ignores symbol keys**

- [x] **`for...in`** lists enumerable **string** keys only. Symbol keys are skipped.

Sandbox: `code_sandbox/js-symbols/symbol-for-in.html`

```javascript
const id = Symbol("id");
const person = { firstName: "John", lastName: "Doe" };
person[id] = 123;
let text = "";
for (let x in person) {
  text += x + " ";
}
```

<img alt="js-symbols example 6 source" src="./code_sandbox/snaps/js-symbols-06-code.png" />

<img alt="js-symbols example 6 result" src="./code_sandbox/snaps/js-symbols-06-result.png" />

- [x] **Outcome:** text is **"firstName lastName "** (trailing space). person[id] is still **123**.

<a id="js-symbols-example-07"></a>

### **Example 7: JSON.stringify ignores symbol keys**

- [x] **`JSON.stringify`** omits symbol properties.

Sandbox: `code_sandbox/js-symbols/symbol-json.html`

```javascript
const id = Symbol("id");
const person = { name: "John" };
person[id] = 123;
let text = JSON.stringify(person);
```

<img alt="js-symbols example 7 source" src="./code_sandbox/snaps/js-symbols-07-code.png" />

<img alt="js-symbols example 7 result" src="./code_sandbox/snaps/js-symbols-07-result.png" />

- [x] **Outcome:** text is **{"name":"John"}**. The symbol value **123** is omitted.

<a id="js-symbols-example-08"></a>

### **Example 8: Symbol.for("id") is reused**

- [x] **`Symbol.for(key)`** uses a **global registry**. Same key → **same** symbol.

Sandbox: `code_sandbox/js-symbols/symbol-for-global.html`

```javascript
const id1 = Symbol.for("id");
const id2 = Symbol.for("id");
let result = (id1 === id2);
```

<img alt="js-symbols example 8 source" src="./code_sandbox/snaps/js-symbols-08-code.png" />

<img alt="js-symbols example 8 result" src="./code_sandbox/snaps/js-symbols-08-result.png" />

- [x] **Outcome:** result is **true** (unlike `Symbol("id")`).

<a id="js-symbols-example-09"></a>

### **Example 9: Symbol.keyFor — registry lookup**

- [x] `Symbol.keyFor(sym)` returns the **global** key, or **undefined** for a local `Symbol()`.

Sandbox: `code_sandbox/js-symbols/symbol-keyfor.html`

```javascript
const g = Symbol.for("id");
const local = Symbol("id");
```

<img alt="js-symbols example 9 source" src="./code_sandbox/snaps/js-symbols-09-code.png" />

<img alt="js-symbols example 9 result" src="./code_sandbox/snaps/js-symbols-09-result.png" />

- [x] **Outcome:** keyFor(g) is **"id"**. keyFor(local) is **undefined**.

<a id="js-symbols-example-10"></a>

### **Example 10: Symbol + string is TypeError**

- [x] Implicit string coercion of a Symbol **throws**. Use **`String(sym)`** or **`sym.description`**.

Sandbox: `code_sandbox/js-symbols/symbol-plus-typeerror.html`

```javascript
Symbol("id") + "";
```

<img alt="js-symbols example 10 source" src="./code_sandbox/snaps/js-symbols-10-code.png" />

<img alt="js-symbols example 10 result" src="./code_sandbox/snaps/js-symbols-10-result.png" />

- [x] **Outcome:** **TypeError: Cannot convert a Symbol value to a string**. `String(Symbol("id"))` would be **"Symbol(id)"**.

<a id="js-symbols-example-11"></a>

### **Example 11: Symbol.iterator — custom for...of**

- [x] **`Symbol.iterator`** makes an object work with **`for...of`** (and spread).

Sandbox: `code_sandbox/js-symbols/wellknown-iterator.html`

```javascript
const myObject = {
  data: ["A", "B", "C"],
  [Symbol.iterator]() {
    let index = 0;
    let data = this.data;
    return {
      next() {
        if (index < data.length) {
          return {value: data[index++], done: false};
        }
        return {done: true};
      }
    };
  }
};
let text = "";
for (const x of myObject) {
  text += x + " ";
}
```

<img alt="js-symbols example 11 source" src="./code_sandbox/snaps/js-symbols-11-code.png" />

<img alt="js-symbols example 11 result" src="./code_sandbox/snaps/js-symbols-11-result.png" />

- [x] **Outcome:** text is **"A B C "**. typeof Symbol.iterator is **"symbol"**.

<a id="js-symbols-example-12"></a>

### **Example 12: Symbol.asyncIterator (well-known)**

- [x] **`Symbol.asyncIterator`** is the well-known symbol for **async** iteration (`for await...of`).

Sandbox: `code_sandbox/js-symbols/wellknown-asynciterator.html`

```javascript
typeof Symbol.asyncIterator;
Symbol.asyncIterator === Symbol.asyncIterator;
```

<img alt="js-symbols example 12 source" src="./code_sandbox/snaps/js-symbols-12-code.png" />

<img alt="js-symbols example 12 result" src="./code_sandbox/snaps/js-symbols-12-result.png" />

- [x] **Outcome:** typeof is **"symbol"**. String is **"Symbol(Symbol.asyncIterator)"**.

<a id="js-symbols-example-13"></a>

### **Example 13: Symbol.toStringTag**

- [x] **`Symbol.toStringTag`** customizes `Object.prototype.toString` (the `[object …]` tag).

Sandbox: `code_sandbox/js-symbols/wellknown-tostringtag.html`

```javascript
const o = { [Symbol.toStringTag]: "Foo" };
let tag = Object.prototype.toString.call(o);
```

<img alt="js-symbols example 13 source" src="./code_sandbox/snaps/js-symbols-13-code.png" />

<img alt="js-symbols example 13 result" src="./code_sandbox/snaps/js-symbols-13-result.png" />

- [x] **Outcome:** Object.prototype.toString.call(o) is **"[object Foo]"**. Default String(o) is still **[object Foo]** here via toString.

<a id="js-symbols-example-14"></a>

### **Example 14: Symbol.toPrimitive**

- [x] **`Symbol.toPrimitive`** runs when the engine needs a **primitive** (hint number / string / default).

Sandbox: `code_sandbox/js-symbols/wellknown-toprimitive.html`

```javascript
const o = {
  [Symbol.toPrimitive](hint) {
    if (hint === "number") return 42;
    return "ok";
  }
};
```

<img alt="js-symbols example 14 source" src="./code_sandbox/snaps/js-symbols-14-code.png" />

<img alt="js-symbols example 14 result" src="./code_sandbox/snaps/js-symbols-14-result.png" />

- [x] **Outcome:** Number(o) is **42**. String(o) is **"ok"**. `o + 1` uses hint **"default"** → **"ok1"** (string concat).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-symbols/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Are two `Symbol()` values equal?

<details>
<summary>Answer</summary>

- [x] **No.** `===` is **false**.

</details>

### Question 2: Does a matching description make them equal?

<details>
<summary>Answer</summary>

- [x] **No.** `Symbol("id") === Symbol("id")` is still **false**.

</details>

### Question 3: What does `Symbol.for("id")` do?

<details>
<summary>Answer</summary>

- [x] Reuses a **global** symbol. Two calls with `"id"` are **=== true**.

</details>

### Question 4: What is `Symbol.keyFor(Symbol("id"))`?

<details>
<summary>Answer</summary>

- [x] **undefined** — local symbols are not in the registry.

</details>

### Question 5: What is `person[id]` vs `person.id` after `person[id] = 140353`?

<details>
<summary>Answer</summary>

- [x] Symbol key **140353**. String key **undefined**.

</details>

### Question 6: Does `for...in` show symbol keys?

<details>
<summary>Answer</summary>

- [x] **No.** text is **"firstName lastName "**.

</details>

### Question 7: Does `JSON.stringify` include symbol keys?

<details>
<summary>Answer</summary>

- [x] **No.** `{"name":"John"}` only.

</details>

### Question 8: What is `typeof Symbol("id")`?

<details>
<summary>Answer</summary>

- [x] **"symbol"**.

</details>

### Question 9: What happens with `Symbol("id") + ""`?

<details>
<summary>Answer</summary>

- [x] **TypeError: Cannot convert a Symbol value to a string**.
- [x] `String(Symbol("id"))` is **"Symbol(id)"**.

</details>

### Question 10: What did the custom iterator print?

<details>
<summary>Answer</summary>

- [x] **"A B C "** from for...of.

</details>

### Question 11: What is `Object.prototype.toString.call({[Symbol.toStringTag]:"Foo"})`?

<details>
<summary>Answer</summary>

- [x] **"[object Foo]"**.

</details>

### Question 12: What does `Symbol.toPrimitive` return for Number(o) in the demo?

<details>
<summary>Answer</summary>

- [x] **42**. String(o) is **"ok"**. `o + 1` is **"ok1"**.

</details>


</details>

## Summary

Use Symbol when you need unique hidden keys or well-known hooks. Use Symbol.for only when you want a shared global identity. Never concatenate a Symbol with a string.

## References

- [JS Symbols (W3Schools)](https://www.w3schools.com/js/js_datatypes_symbol.asp)
- [MDN: Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
- [MDN: Well-known symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#well-known_symbols)

</details>
