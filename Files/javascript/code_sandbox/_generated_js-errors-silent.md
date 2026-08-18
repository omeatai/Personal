<details>
  <summary>JS Errors Silent</summary>

## Introduction

JavaScript can fail without throwing. Execution continues: 1/0 is Infinity, parseInt('abc') is NaN, a missing property is undefined, and = inside if assigns instead of comparing. Type coercion hides more bugs: + concatenates if either side is a string, other arithmetic forces numbers, and == compares after converting types. These are historical silent failures — early JavaScript had no try/catch. Each Example shows the silent result and a throw you can add when you want a hard stop.

This section has **8** examples:

- [x] **Example 1:** 1 / 0 is Infinity — silent vs throw [View](#js-errors-silent-example-01)
- [x] **Example 2:** if (isActive = true) — assignment, not comparison [View](#js-errors-silent-example-02)
- [x] **Example 3:** parseInt('abc') is NaN — silent vs throw [View](#js-errors-silent-example-03)
- [x] **Example 4:** user.name on {} is undefined — silent vs throw [View](#js-errors-silent-example-04)
- [x] **Example 5:** '5' + '2' vs '5' - '2' — silent coercion [View](#js-errors-silent-example-05)
- [x] **Example 6:** String coercion: "5" + 2 is "52" [View](#js-errors-silent-example-06)
- [x] **Example 7:** Numeric coercion: "5" - 2 is 3 [View](#js-errors-silent-example-07)
- [x] **Example 8:** Loose equality: 5 == '5' is true [View](#js-errors-silent-example-08)

## Detailed Explanation

- [x] **Silent ≠ OK.** The program **keeps running** with **Infinity**, **NaN**, **undefined**, or the **wrong branch**.
- [x] `1 / 0` is **Infinity**, not a throw. `parseInt("abc")` is **NaN**.
- [x] `if (isActive = true)` **assigns** and enters the block. The Tryit result is **Active!**.
- [x] `user.name` on `{}` is **undefined**, not ReferenceError (that would be a bare `name`).
- [x] **`+`** with a string concatenates. **`-` `*` `/`** coerce to numbers. **`==`** coerces; **`===`** does not.
- [x] To stop execution you **`throw`** after an explicit check (`Number.isFinite`, `Number.isNaN`, `===`).

<a id="js-errors-silent-example-01"></a>

### **Example 1: 1 / 0 is Infinity — silent vs throw**

- [x] **Silent errors do not stop the program.** Execution **continues**.
- [x] `1 / 0` is **Infinity** (IEEE 754). JavaScript does **not** throw.
- [x] To fail loudly you must **`throw` yourself** after checking `Number.isFinite`.

Sandbox: `code_sandbox/js-errors-silent/divide-by-zero-infinity.html`

```javascript
let x = 1 / 0;
try {
  if (!Number.isFinite(x)) throw new Error("division produced Infinity");
} catch (err) {
  // only the throw path stops here
}
```

<img alt="js-errors-silent example 1 source" src="./code_sandbox/snaps/js-errors-silent-01-code.png" />

<img alt="js-errors-silent example 1 result" src="./code_sandbox/snaps/js-errors-silent-01-result.png" />

- [x] **Outcome:** Silent `1 / 0` is **Infinity** (no throw). The explicit throw is **Error**: **division produced Infinity**.

<a id="js-errors-silent-example-02"></a>

### **Example 2: if (isActive = true) — assignment, not comparison**

- [x] `=` **assigns**. `isActive = true` sets the flag to **true** and the `if` condition is **true**.
- [x] The Tryit then sets `result = "Active!"`. **No exception** — a logic bug.
- [x] The `===` path with `isActive` still **false** does not enter; a **`throw`** makes that miss loud.

Sandbox: `code_sandbox/js-errors-silent/assignment-not-comparison.html`

```javascript
let result = "Not Active.";
let isActive = false;
if (isActive = true) {   // assignment, not comparison
  result = "Active!";
}
```

<img alt="js-errors-silent example 2 source" src="./code_sandbox/snaps/js-errors-silent-02-code.png" />

<img alt="js-errors-silent example 2 result" src="./code_sandbox/snaps/js-errors-silent-02-result.png" />

- [x] **Outcome:** Silent path: result is **"Active!"** and `isActive` is **true** (no throw). With `===` and `throw`, `isActive` stays **false** and the catch is **Error**: **not active**.

<a id="js-errors-silent-example-03"></a>

### **Example 3: parseInt('abc') is NaN — silent vs throw**

- [x] Many numeric failures produce **`NaN`**, not an exception.
- [x] `parseInt("abc")` is **NaN**. The program **keeps going**.
- [x] `Number.isNaN` + **`throw`** turns that into a real error.

Sandbox: `code_sandbox/js-errors-silent/parseint-nan.html`

```javascript
const result = parseInt("abc");
// NaN - no error, just wrong data
```

<img alt="js-errors-silent example 3 source" src="./code_sandbox/snaps/js-errors-silent-03-code.png" />

<img alt="js-errors-silent example 3 result" src="./code_sandbox/snaps/js-errors-silent-03-result.png" />

- [x] **Outcome:** Silent result is **NaN**. The throw path is **Error**: **parseInt produced NaN**.

<a id="js-errors-silent-example-04"></a>

### **Example 4: user.name on {} is undefined — silent vs throw**

- [x] Reading a **missing property** returns **`undefined`**. No throw.
- [x] That is easy to miss. Check and **`throw`** if the property is required.

Sandbox: `code_sandbox/js-errors-silent/missing-property-undefined.html`

```javascript
const user = {};
let result = user.name;
```

<img alt="js-errors-silent example 4 source" src="./code_sandbox/snaps/js-errors-silent-04-code.png" />

<img alt="js-errors-silent example 4 result" src="./code_sandbox/snaps/js-errors-silent-04-result.png" />

- [x] **Outcome:** Silent `user.name` is **undefined**. The throw path is **Error**: **missing name**.

<a id="js-errors-silent-example-05"></a>

### **Example 5: '5' + '2' vs '5' - '2' — silent coercion**

- [x] JavaScript **coerces** instead of throwing when types look numeric/stringy.
- [x] `'5' + '2'` concatenates to **`"52"`**. `'5' - '2'` subtracts to **3**.
- [x] A **`throw`** if `typeof` differs makes mixed-type `+` loud.

Sandbox: `code_sandbox/js-errors-silent/plus-vs-minus-coercion.html`

```javascript
let result1 = ('5' + '2');  // 52
let result2 = ('5' - '2');  // 3
```

<img alt="js-errors-silent example 5 source" src="./code_sandbox/snaps/js-errors-silent-05-code.png" />

<img alt="js-errors-silent example 5 result" src="./code_sandbox/snaps/js-errors-silent-05-result.png" />

- [x] **Outcome:** Silent: result1 is **"52"** (string); result2 is **3** (number). Throw-if-types-differ on `"5" + 2` is **TypeError**: **mixed types in +**.

<a id="js-errors-silent-example-06"></a>

### **Example 6: String coercion: "5" + 2 is "52"**

- [x] If **any** operand of **`+`** is a string, JavaScript converts the other to a **string**.
- [x] `"5" + 2` is **`"52"`**, not **7**. No throw.

Sandbox: `code_sandbox/js-errors-silent/string-coercion-plus.html`

```javascript
let x = "5" + 2;  // x = "52"
```

<img alt="js-errors-silent example 6 source" src="./code_sandbox/snaps/js-errors-silent-06-code.png" />

<img alt="js-errors-silent example 6 result" src="./code_sandbox/snaps/js-errors-silent-06-result.png" />

- [x] **Outcome:** x is **"52"** (`typeof` **string**). `Number("5") + 2` is **7**.

<a id="js-errors-silent-example-07"></a>

### **Example 7: Numeric coercion: "5" - 2 is 3**

- [x] **`-` `*` `/` `%`** and unary **`+x`** force values to **numbers**.
- [x] `"5" - 2` is **3**. `"abc" - 1` is **NaN** (still no throw).

Sandbox: `code_sandbox/js-errors-silent/numeric-coercion-minus.html`

```javascript
let x = "5" - 2;  // x = 3
```

<img alt="js-errors-silent example 7 source" src="./code_sandbox/snaps/js-errors-silent-07-code.png" />

<img alt="js-errors-silent example 7 result" src="./code_sandbox/snaps/js-errors-silent-07-result.png" />

- [x] **Outcome:** `"5" - 2` is **3**. `"abc" - 1` is **NaN** — silent, not a TypeError.

<a id="js-errors-silent-example-08"></a>

### **Example 8: Loose equality: 5 == '5' is true**

- [x] **`==`** coerces to a common type. **`===`** does not.
- [x] `5 == "5"` is **true**. `5 === "5"` is **false**. Prefer **`===`**.

Sandbox: `code_sandbox/js-errors-silent/loose-equality.html`

```javascript
let x = (5 == "5");  // x = true
```

<img alt="js-errors-silent example 8 source" src="./code_sandbox/snaps/js-errors-silent-08-code.png" />

<img alt="js-errors-silent example 8 result" src="./code_sandbox/snaps/js-errors-silent-08-result.png" />

- [x] **Outcome:** `5 == "5"` is **true**. `5 === "5"` is **false**. Throw-if-types-differ is **TypeError**: **loose compare mixed types**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-errors-silent/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does `1 / 0` throw?

<details>
<summary>Answer</summary>

- [x] **No.** It is **Infinity**.
- [x] A follow-up `throw new Error("division produced Infinity")` is **Error**: **division produced Infinity**.

</details>

### Question 2: What does `if (isActive = true)` do when `isActive` started false?

<details>
<summary>Answer</summary>

- [x] It **assigns true** and takes the branch.
- [x] The Tryit sets result to **Active!** — no exception.

</details>

### Question 3: How do you make the inactive path loud?

<details>
<summary>Answer</summary>

- [x] Use **`===`**. If it is still false, **`throw new Error("not active")`** → **Error**: **not active**.

</details>

### Question 4: What is `parseInt("abc")`?

<details>
<summary>Answer</summary>

- [x] **NaN**. `Number.isNaN` is **true**. No throw.
- [x] Optional throw: **Error**: **parseInt produced NaN**.

</details>

### Question 5: What is `{}.name`?

<details>
<summary>Answer</summary>

- [x] **undefined** — missing property, **not** a ReferenceError.
- [x] Optional throw: **Error**: **missing name**.

</details>

### Question 6: What is `'5' + '2'` vs `'5' - '2'`?

<details>
<summary>Answer</summary>

- [x] **`"52"`** (string) vs **3** (number).

</details>

### Question 7: What is `"5" + 2`?

<details>
<summary>Answer</summary>

- [x] **`"52"`** (`typeof` **string**). `Number("5") + 2` is **7**.

</details>

### Question 8: What is `"5" - 2`?

<details>
<summary>Answer</summary>

- [x] **3**. `"abc" - 1` is **NaN**, still **no throw**.

</details>

### Question 9: What is `5 == "5"` vs `5 === "5"`?

<details>
<summary>Answer</summary>

- [x] **true** vs **false**. Prefer **`===`**.
- [x] Throw-if-types-differ: **TypeError**: **loose compare mixed types**.

</details>

### Question 10: Why do silent errors exist?

<details>
<summary>Answer</summary>

- [x] Early JavaScript had **no try/catch**. Failures were designed **not** to stop the page.

</details>

### Question 11: Does a silent error set `err.name`?

<details>
<summary>Answer</summary>

- [x] **No.** Nothing was thrown, so there is **no** Error object unless **you throw**.

</details>


</details>

## Summary

Infinity, NaN, undefined, accidental assignment, and coercion all continue execution. Check explicitly and throw when a wrong value must stop the program. Prefer ===, Number(), and Number.isNaN / Number.isFinite over hoping the engine will yell.

## References

- [JS Errors Silent (W3Schools)](https://www.w3schools.com/js/js_errors_silent.asp)
- [MDN: NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
- [MDN: Equality comparisons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness)
- [MDN: throw](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)

</details>
