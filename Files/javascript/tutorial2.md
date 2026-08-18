# JavaScript Tutorial — Part 2

Continues the W3Schools JavaScript notes from [Part 1](./tutorial.md) (through **JS Destructuring**). Each accordion is one tutorial page: explained, coded in `code_sandbox`, run in the browser, and snapped.

**[← Back to PART 1](./tutorial.md)**

<details>
  <summary>JS Errors Intro</summary>

## Introduction

When JavaScript runs, errors happen: programmer mistakes, bad input, and surprises. This page names the built-in kinds — ReferenceError, TypeError, RangeError, URIError, SyntaxError, and the deprecated EvalError — and introduces try/catch. Runtime errors can be caught. Syntax errors are thrown while the engine is still parsing, so a raw script never starts and try/catch on the same page cannot help. This sandbox uses new Function only so those parse errors can be shown without blanking the page.

This section has **12** examples:

- [x] **Example 1:** try — catch is skipped when nothing throws [View](#js-errors-intro-example-01)
- [x] **Example 2:** catch — runs when the try block throws [View](#js-errors-intro-example-02)
- [x] **Example 3:** ReferenceError — y is not defined [View](#js-errors-intro-example-03)
- [x] **Example 4:** ReferenceError — Cannot access y before initialization [View](#js-errors-intro-example-04)
- [x] **Example 5:** TypeError — anna is not a function [View](#js-errors-intro-example-05)
- [x] **Example 6:** TypeError — num.toUpperCase is not a function [View](#js-errors-intro-example-06)
- [x] **Example 7:** RangeError — Invalid array length [View](#js-errors-intro-example-07)
- [x] **Example 8:** RangeError — toPrecision() argument must be between 1 and 100 [View](#js-errors-intro-example-08)
- [x] **Example 9:** URIError — decodeURI('%%%') URI malformed [View](#js-errors-intro-example-09)
- [x] **Example 10:** SyntaxError — unclosed string (not catchable in a raw script) [View](#js-errors-intro-example-10)
- [x] **Example 11:** SyntaxError — try/catch cannot catch Math.round(4.6;) [View](#js-errors-intro-example-11)
- [x] **Example 12:** EvalError — deprecated; eval throws SyntaxError instead [View](#js-errors-intro-example-12)

## Detailed Explanation

- [x] **`try` / `catch`** come in pairs. `try` tests a block; `catch` runs only if that block throws.
- [x] **ReferenceError** — missing name, or **TDZ** (`Cannot access 'y' before initialization`).
- [x] **TypeError** — wrong type (`anna is not a function`, `num.toUpperCase is not a function`).
- [x] **RangeError** — out of range (`Invalid array length`, `toPrecision() argument must be between 1 and 100`).
- [x] **URIError** — `decodeURI("%%%")` → **URI malformed**.
- [x] **SyntaxError** is **not catchable** in the same `<script>`. Use **`new Function`** here to display it. `eval` of bad source **is** catchable (Error Object page).
- [x] **EvalError** is **deprecated**. `eval("var = 1")` throws **SyntaxError**, not EvalError.

<a id="js-errors-intro-example-01"></a>

### **Example 1: try — catch is skipped when nothing throws**

- [x] The **`try`** block is the code you want to test for errors.
- [x] If the block finishes **without** throwing, **`catch` is skipped**.

Sandbox: `code_sandbox/js-errors-intro/try-block-no-error.html`

```javascript
let status = "start";
try {
  status = "try ran";
} catch (err) {
  status = "catch ran: " + err;
}
```

<img alt="js-errors-intro example 1 source" src="./code_sandbox/snaps/js-errors-intro-01-code.png" />

<img alt="js-errors-intro example 1 result" src="./code_sandbox/snaps/js-errors-intro-01-result.png" />

- [x] **Outcome:** status is **"try ran"**. The catch block did **not** run.

<a id="js-errors-intro-example-02"></a>

### **Example 2: catch — runs when the try block throws**

- [x] **`catch`** runs only if **`try`** throws.
- [x] The parameter (`err`) is the thrown value. Built-in errors have **`name`** and **`message`**.

Sandbox: `code_sandbox/js-errors-intro/catch-block-runs.html`

```javascript
try {
  null.foo;
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 2 source" src="./code_sandbox/snaps/js-errors-intro-02-code.png" />

<img alt="js-errors-intro example 2 result" src="./code_sandbox/snaps/js-errors-intro-02-result.png" />

- [x] **Outcome:** **TypeError**: Cannot read properties of **null** (reading **'foo'**). Catch ran.

<a id="js-errors-intro-example-03"></a>

### **Example 3: ReferenceError — y is not defined**

- [x] A **`ReferenceError`** occurs if you use a variable that **does not exist**.
- [x] The W3Schools table also lists `fname = foo` → **foo is not defined**. Same error name.

Sandbox: `code_sandbox/js-errors-intro/referenceerror-undeclared.html`

```javascript
let x = 5;
try {
  x = y + 1;
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 3 source" src="./code_sandbox/snaps/js-errors-intro-03-code.png" />

<img alt="js-errors-intro example 3 result" src="./code_sandbox/snaps/js-errors-intro-03-result.png" />

- [x] **Outcome:** **ReferenceError**: **y is not defined**.

<a id="js-errors-intro-example-04"></a>

### **Example 4: ReferenceError — Cannot access y before initialization**

- [x] `let x = y` then `let y = 5` is **not** “y does not exist.”
- [x] `let y` is in the **temporal dead zone** — **ReferenceError** before initialization.

Sandbox: `code_sandbox/js-errors-intro/referenceerror-tdz.html`

```javascript
try {
  let x = y;
  let y = 5;
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 4 source" src="./code_sandbox/snaps/js-errors-intro-04-code.png" />

<img alt="js-errors-intro example 4 result" src="./code_sandbox/snaps/js-errors-intro-04-result.png" />

- [x] **Outcome:** **ReferenceError**: **Cannot access 'y' before initialization**.

<a id="js-errors-intro-example-05"></a>

### **Example 5: TypeError — anna is not a function**

- [x] A **`TypeError`** occurs when a value is the **wrong type** for the operation.
- [x] `anna` is the number **5**, so `anna(5)` is not a call.

Sandbox: `code_sandbox/js-errors-intro/typeerror-not-a-function.html`

```javascript
let anna = 5;
try {
  anna(5);
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 5 source" src="./code_sandbox/snaps/js-errors-intro-05-code.png" />

<img alt="js-errors-intro example 5 result" src="./code_sandbox/snaps/js-errors-intro-05-result.png" />

- [x] **Outcome:** **TypeError**: **anna is not a function**.

<a id="js-errors-intro-example-06"></a>

### **Example 6: TypeError — num.toUpperCase is not a function**

- [x] Numbers do not have **`toUpperCase`** (that is a **string** method).
- [x] Calling it is a **TypeError**, not a silent no-op.

Sandbox: `code_sandbox/js-errors-intro/typeerror-touppercase.html`

```javascript
let num = 1;
try {
  num.toUpperCase();
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 6 source" src="./code_sandbox/snaps/js-errors-intro-06-code.png" />

<img alt="js-errors-intro example 6 result" src="./code_sandbox/snaps/js-errors-intro-06-result.png" />

- [x] **Outcome:** **TypeError**: **num.toUpperCase is not a function**.

<a id="js-errors-intro-example-07"></a>

### **Example 7: RangeError — Invalid array length**

- [x] A **`RangeError`** occurs when a value is **out of its valid range**.
- [x] `new Array(-1)` is not a legal length.

Sandbox: `code_sandbox/js-errors-intro/rangeerror-array-length.html`

```javascript
try {
  new Array(-1);
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 7 source" src="./code_sandbox/snaps/js-errors-intro-07-code.png" />

<img alt="js-errors-intro example 7 result" src="./code_sandbox/snaps/js-errors-intro-07-result.png" />

- [x] **Outcome:** **RangeError**: **Invalid array length**.

<a id="js-errors-intro-example-08"></a>

### **Example 8: RangeError — toPrecision() argument must be between 1 and 100**

- [x] `Number.prototype.toPrecision(precision)` only allows **1–100** significant digits.
- [x] **500** is out of range.

Sandbox: `code_sandbox/js-errors-intro/rangeerror-toprecision.html`

```javascript
let num = 1;
try {
  num.toPrecision(500);  // A number cannot have 500 significant digits
} catch (err) {
  let text = err.name;
}
```

<img alt="js-errors-intro example 8 source" src="./code_sandbox/snaps/js-errors-intro-08-code.png" />

<img alt="js-errors-intro example 8 result" src="./code_sandbox/snaps/js-errors-intro-08-result.png" />

- [x] **Outcome:** **RangeError**: **toPrecision() argument must be between 1 and 100**.

<a id="js-errors-intro-example-09"></a>

### **Example 9: URIError — decodeURI('%%%') URI malformed**

- [x] A **`URIError`** occurs if you pass **illegal characters** to a URI function.
- [x] `decodeURI("%%%")` is not a valid percent-encoding.

Sandbox: `code_sandbox/js-errors-intro/urierror-decodeuri.html`

```javascript
try {
  decodeURI("%%%");  // You cannot URI decode percent signs
} catch (err) {
  document.getElementById("demo").innerHTML = err.name;
}
```

<img alt="js-errors-intro example 9 source" src="./code_sandbox/snaps/js-errors-intro-09-code.png" />

<img alt="js-errors-intro example 9 result" src="./code_sandbox/snaps/js-errors-intro-09-result.png" />

- [x] **Outcome:** **URIError**: **URI malformed**.

<a id="js-errors-intro-example-10"></a>

### **Example 10: SyntaxError — unclosed string (not catchable in a raw script)**

- [x] A **`SyntaxError`** means the source **violates JavaScript grammar**.
- [x] The engine throws it **before runtime**. A raw `<script>` **does not load**.
- [x] This sandbox compiles the snippet with **`new Function`** so the page can still render.

Sandbox: `code_sandbox/js-errors-intro/syntaxerror-unclosed-string.html`

```javascript
// This line cannot be parsed by JavaScript
let text = "John Doe);
// This line will not be executed
```

<img alt="js-errors-intro example 10 source" src="./code_sandbox/snaps/js-errors-intro-10-code.png" />

<img alt="js-errors-intro example 10 result" src="./code_sandbox/snaps/js-errors-intro-10-result.png" />

- [x] **Outcome:** **SyntaxError**: **Invalid or unexpected token** (via `new Function`). A raw script would stop the page.

<a id="js-errors-intro-example-11"></a>

### **Example 11: SyntaxError — try/catch cannot catch Math.round(4.6;)**

- [x] `Math.round(4.6;)` has an extra **`;`** inside the parentheses — **missing ) after argument list**.
- [x] **`try...catch` does not help**: the **whole script** fails to parse, so `try` never starts.
- [x] `err.description` on the W3Schools page is **IE-only**. This engine uses **`err.message`**.

Sandbox: `code_sandbox/js-errors-intro/syntaxerror-not-catchable.html`

```javascript
try {
  let x = Math.round(4.6;)
} catch (err) {
  let text = err.name + " " + err.description;
}
```

<img alt="js-errors-intro example 11 source" src="./code_sandbox/snaps/js-errors-intro-11-code.png" />

<img alt="js-errors-intro example 11 result" src="./code_sandbox/snaps/js-errors-intro-11-result.png" />

- [x] **Outcome:** **SyntaxError**: **missing ) after argument list**. Inner `catch` never ran — the snippet did not parse.

<a id="js-errors-intro-example-12"></a>

### **Example 12: EvalError — deprecated; eval throws SyntaxError instead**

- [x] The page lists **EvalError** (deprecated). Newer engines **do not throw EvalError** from `eval()`.
- [x] `new EvalError(...)` still constructs an object whose **`name`** is **EvalError**.
- [x] Bad `eval` source is a **SyntaxError** (use that).

Sandbox: `code_sandbox/js-errors-intro/evalerror-deprecated.html`

```javascript
const made = new EvalError("still constructable");
try {
  eval("var = 1");
} catch (err) {
  // SyntaxError, not EvalError
}
```

<img alt="js-errors-intro example 12 source" src="./code_sandbox/snaps/js-errors-intro-12-code.png" />

<img alt="js-errors-intro example 12 result" src="./code_sandbox/snaps/js-errors-intro-12-result.png" />

- [x] **Outcome:** `new EvalError` has name **EvalError**. `eval("var = 1")` throws **SyntaxError**: **Unexpected token '='** — not EvalError.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-errors-intro/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `try` do if nothing throws?

<details>
<summary>Answer</summary>

- [x] The **try** block finishes. **`catch` is skipped**.
- [x] The demo status is **try ran**.

</details>

### Question 2: What is `null.foo`?

<details>
<summary>Answer</summary>

- [x] **TypeError**: **Cannot read properties of null (reading 'foo')**.
- [x] That is the dedicated **catch** demo (not the later TypeError Tryits).

</details>

### Question 3: What is `x = y + 1` when `y` was never declared?

<details>
<summary>Answer</summary>

- [x] **ReferenceError**: **y is not defined**.

</details>

### Question 4: What is `let x = y; let y = 5`?

<details>
<summary>Answer</summary>

- [x] **ReferenceError**: **Cannot access 'y' before initialization** (TDZ).
- [x] It is **not** “y is not defined.”

</details>

### Question 5: What is `anna(5)` if `anna` is `5`?

<details>
<summary>Answer</summary>

- [x] **TypeError**: **anna is not a function**.

</details>

### Question 6: What is `(1).toUpperCase()`?

<details>
<summary>Answer</summary>

- [x] **TypeError**: **num.toUpperCase is not a function**.

</details>

### Question 7: What is `new Array(-1)`?

<details>
<summary>Answer</summary>

- [x] **RangeError**: **Invalid array length**.

</details>

### Question 8: What is `(1).toPrecision(500)`?

<details>
<summary>Answer</summary>

- [x] **RangeError**: **toPrecision() argument must be between 1 and 100**.

</details>

### Question 9: What is `decodeURI("%%%")`?

<details>
<summary>Answer</summary>

- [x] **URIError**: **URI malformed**.

</details>

### Question 10: What is `let text = "John Doe);`?

<details>
<summary>Answer</summary>

- [x] **SyntaxError**: **Invalid or unexpected token**.
- [x] A raw script **does not parse**. This sandbox uses **`new Function`**.

</details>

### Question 11: Can `try { Math.round(4.6;) }` catch the extra semicolon?

<details>
<summary>Answer</summary>

- [x] **No.** The **whole script** is a SyntaxError: **missing ) after argument list**.
- [x] `try` never starts. `err.description` is **IE-only**; this engine has **`err.message`**.

</details>

### Question 12: Does `eval("var = 1")` throw EvalError?

<details>
<summary>Answer</summary>

- [x] **No.** **SyntaxError**: **Unexpected token '='**.
- [x] `new EvalError` still exists; **`eval()` does not throw it** in this engine.

</details>


</details>

## Summary

Catch runtime errors with try/catch. Read err.name and err.message. Syntax errors happen before the script runs — wrap demos in new Function if you need to display them. EvalError is a leftover name; bad eval source is SyntaxError.

## References

- [JS Errors Intro (W3Schools)](https://www.w3schools.com/js/js_errors_intro.asp)
- [MDN: Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
- [MDN: try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
- [MDN: SyntaxError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

</details>

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

<details>
  <summary>JS Error Statements</summary>

## Introduction

try tests a block, catch handles a throw, and finally always runs afterward. JavaScript normally stops and creates an Error with name and message; throw lets you raise a string, number, boolean, or object instead. The input-validation Tryit throws custom phrases (empty, not a number, too low, too high). HTML min/max on an input can reject values without any JavaScript throw. The finally Tryit clears the field even when the number was valid.

This section has **8** examples:

- [x] **Example 1:** try block — code that might throw [View](#js-error-statements-example-01)
- [x] **Example 2:** catch block — handles the thrown value [View](#js-error-statements-example-02)
- [x] **Example 3:** finally — always runs, error or not [View](#js-error-statements-example-03)
- [x] **Example 4:** throw "Too big" — throw a text [View](#js-error-statements-example-04)
- [x] **Example 5:** throw 500 — throw a number [View](#js-error-statements-example-05)
- [x] **Example 6:** Input validation — throw empty / not a number / too low / too high [View](#js-error-statements-example-06)
- [x] **Example 7:** HTML validation — input type=number min=5 max=10 [View](#js-error-statements-example-07)
- [x] **Example 8:** finally example — always clears the input [View](#js-error-statements-example-08)

## Detailed Explanation

- [x] **`try`** — code that might throw. **`catch`** — only if it did. **`finally`** — **always** (cleanup).
- [x] **`throw`** a String / Number / Boolean / Object. Thrown primitives are **not** Error objects (`name` is missing).
- [x] Built-in throws **do** create `{ name, message }`.
- [x] Validation Tryit messages: **Input is empty**, **not a number**, **too low**, **too high**. Valid **7** leaves the message **blank**.
- [x] Finally Tryit: **Input is empty / is not a number / is too high / is too low**, then the **field is cleared**.
- [x] HTML `type="number" min="5" max="10"` uses **`checkValidity()`**, not `throw`.

<a id="js-error-statements-example-01"></a>

### **Example 1: try block — code that might throw**

- [x] The **`try`** block contains code that **might** throw.
- [x] If nothing throws, **`catch` is skipped**.

Sandbox: `code_sandbox/js-error-statements/try-syntax.html`

```javascript
try {
  // Code that may cause an error
  let x = 1 + 1;
} catch (error) {
  // Code to handle the error
}
```

<img alt="js-error-statements example 1 source" src="./code_sandbox/snaps/js-error-statements-01-code.png" />

<img alt="js-error-statements example 1 result" src="./code_sandbox/snaps/js-error-statements-01-result.png" />

- [x] **Outcome:** `1 + 1` is **2**. Catch did **not** run.

<a id="js-error-statements-example-02"></a>

### **Example 2: catch block — handles the thrown value**

- [x] **`catch`** runs **only** if `try` throws.
- [x] For built-in errors the parameter is an **Error** object (`name`, `message`).

Sandbox: `code_sandbox/js-error-statements/catch-syntax.html`

```javascript
try {
  // Code that may cause an error
  missing();
} catch (error) {
  // Code to handle the error
}
```

<img alt="js-error-statements example 2 source" src="./code_sandbox/snaps/js-error-statements-02-code.png" />

<img alt="js-error-statements example 2 result" src="./code_sandbox/snaps/js-error-statements-02-result.png" />

- [x] **Outcome:** **ReferenceError**: **missing is not defined**. Catch ran.

<a id="js-error-statements-example-03"></a>

### **Example 3: finally — always runs, error or not**

- [x] **`finally`** runs after `try` / `catch` **whether or not** an error occurred.
- [x] Use it for **cleanup** (clear a field, hide a loader).

Sandbox: `code_sandbox/js-error-statements/finally-syntax.html`

```javascript
try {
  // Code that may cause an error
} catch (error) {
  // Code to handle the error
} finally {
  // Code that always runs, no matter what
}
```

<img alt="js-error-statements example 3 source" src="./code_sandbox/snaps/js-error-statements-03-code.png" />

<img alt="js-error-statements example 3 result" src="./code_sandbox/snaps/js-error-statements-03-result.png" />

- [x] **Outcome:** Success path: finally **yes**, catch **no**. Error path: catch **yes**, finally **yes**.

<a id="js-error-statements-example-04"></a>

### **Example 4: throw "Too big" — throw a text**

- [x] **`throw`** creates a **custom** exception. It can be a **String**, **Number**, **Boolean**, or **Object**.
- [x] A thrown string is **not** an Error object — `err.name` is **undefined**; `String(err)` is the text.

Sandbox: `code_sandbox/js-error-statements/throw-string.html`

```javascript
throw "Too big";  // throw a text
```

<img alt="js-error-statements example 4 source" src="./code_sandbox/snaps/js-error-statements-04-code.png" />

<img alt="js-error-statements example 4 result" src="./code_sandbox/snaps/js-error-statements-04-result.png" />

- [x] **Outcome:** Catch receives the string **"Too big"**. `err.name` is not an Error name (`(not an Error object)`).

<a id="js-error-statements-example-05"></a>

### **Example 5: throw 500 — throw a number**

- [x] You can **`throw` a number**. Same rule: it is **not** `{name, message}`.
- [x] `String(err)` is **`"500"`**.

Sandbox: `code_sandbox/js-error-statements/throw-number.html`

```javascript
throw 500;  // throw a number
```

<img alt="js-error-statements example 5 source" src="./code_sandbox/snaps/js-error-statements-05-code.png" />

<img alt="js-error-statements example 5 result" src="./code_sandbox/snaps/js-error-statements-05-result.png" />

- [x] **Outcome:** Catch receives **500**. `String(err)` is **500** — not `Error: 500`.

<a id="js-error-statements-example-06"></a>

### **Example 6: Input validation — throw empty / not a number / too low / too high**

- [x] Together, **`throw` + `try` + `catch`** control flow and show a **custom** message.
- [x] This sandbox runs the Tryit function against several values (no clicking required).

Sandbox: `code_sandbox/js-error-statements/input-validation-throw.html`

```javascript
function myFunction(x) {
  const message = { innerHTML: "" };
  try {
    if (x.trim() == "") throw "empty";
    if (isNaN(x)) throw "not a number";
    x = Number(x);
    if (x < 5) throw "too low";
    if (x > 10) throw "too high";
  } catch (err) {
    message.innerHTML = "Input is " + err;
  }
  return message.innerHTML;
}
```

<img alt="js-error-statements example 6 source" src="./code_sandbox/snaps/js-error-statements-06-code.png" />

<img alt="js-error-statements example 6 result" src="./code_sandbox/snaps/js-error-statements-06-result.png" />

- [x] **Outcome:** `""` → **Input is empty**. `"hello"` → **Input is not a number**. `"3"` → **Input is too low**. `"12"` → **Input is too high**. `"7"` → blank (valid; catch skipped).

<a id="js-error-statements-example-07"></a>

### **Example 7: HTML validation — input type=number min=5 max=10**

- [x] Modern browsers can validate with **HTML attributes** (`type`, `min`, `max`, `step`) instead of `throw`.
- [x] `checkValidity()` is **true/false** — it does **not** throw a JavaScript Error.

Sandbox: `code_sandbox/js-error-statements/html-validation.html`

```javascript
<input id="demo" type="number" min="5" max="10" step="1">
```

<img alt="js-error-statements example 7 source" src="./code_sandbox/snaps/js-error-statements-07-code.png" />

<img alt="js-error-statements example 7 result" src="./code_sandbox/snaps/js-error-statements-07-result.png" />

- [x] **Outcome:** `3` is **invalid** (`rangeUnderflow`). `7` is **valid**. `11` is **invalid** (`rangeOverflow`). No JS **throw**.

<a id="js-error-statements-example-08"></a>

### **Example 8: finally example — always clears the input**

- [x] After `try` / `catch`, **`finally`** still runs.
- [x] The Tryit **clears** the input field in `finally`, including on a **valid** value.

Sandbox: `code_sandbox/js-error-statements/finally-clears-input.html`

```javascript
function myFunction() {
  const message = document.getElementById("p01");
  message.innerHTML = "";
  let x = document.getElementById("demo").value;
  try {
    if (x.trim() == "") throw "is empty";
    if (isNaN(x)) throw "is not a number";
    x = Number(x);
    if (x > 10) throw "is too high";
    if (x < 5) throw "is too low";
  } catch (err) {
    message.innerHTML = "Input " + err;
  } finally {
    document.getElementById("demo").value = "";
  }
}
```

<img alt="js-error-statements example 8 source" src="./code_sandbox/snaps/js-error-statements-08-code.png" />

<img alt="js-error-statements example 8 result" src="./code_sandbox/snaps/js-error-statements-08-result.png" />

- [x] **Outcome:** `"3"` → **Input is too low** and field **cleared**. `"7"` → no error message, field **still cleared**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-error-statements/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does catch run after `try { 1 + 1 }`?

<details>
<summary>Answer</summary>

- [x] **No.** x is **2**. catch ran → **false**.

</details>

### Question 2: What is `missing()`?

<details>
<summary>Answer</summary>

- [x] **ReferenceError**: **missing is not defined**.

</details>

### Question 3: Does `finally` run when try succeeds?

<details>
<summary>Answer</summary>

- [x] **Yes.** Order: **try | finally**.

</details>

### Question 4: Does `finally` run when try throws?

<details>
<summary>Answer</summary>

- [x] **Yes.** Order: **try, catch:ReferenceError | finally**.

</details>

### Question 5: What is `throw "Too big"` in catch?

<details>
<summary>Answer</summary>

- [x] The string **Too big**. It is **not** an Error object.

</details>

### Question 6: What is `throw 500` in catch?

<details>
<summary>Answer</summary>

- [x] The number **500**. `String(err)` is **500**.

</details>

### Question 7: What does the validation Tryit print for `""`, `"hello"`, `"3"`, `"12"`, `"7"`?

<details>
<summary>Answer</summary>

- [x] **Input is empty**.
- [x] **Input is not a number**.
- [x] **Input is too low**.
- [x] **Input is too high**.
- [x] **blank** (valid).

</details>

### Question 8: Does HTML `min`/`max` throw a JS Error?

<details>
<summary>Answer</summary>

- [x] **No.** `checkValidity()` is **false** for **3** (`rangeUnderflow`) and **11** (`rangeOverflow`), **true** for **7**.

</details>

### Question 9: Does `finally` clear the input on a valid `7`?

<details>
<summary>Answer</summary>

- [x] **Yes.** Message stays **blank**; **fieldAfter** is **`""`**.

</details>

### Question 10: What is the finally message for `"3"`?

<details>
<summary>Answer</summary>

- [x] **Input is too low** (Tryit text is `"Input " + err`).

</details>

### Question 11: Can you `throw` a Boolean?

<details>
<summary>Answer</summary>

- [x] **Yes.** The page lists String, Number, Boolean, or Object. This section demos **string** and **number** as in the syntax lines.

</details>


</details>

## Summary

Use try to protect code, catch to handle a throw, and finally to clean up. throw can be any value; only Error objects have name and message. The validation Tryits map empty / NaN / range into custom strings. HTML constraint validation is a separate, non-throwing path.

## References

- [JS Error Statements (W3Schools)](https://www.w3schools.com/js/js_errors.asp)
- [MDN: try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
- [MDN: throw](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
- [MDN: Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation)

</details>

<details>
  <summary>JS Error Object</summary>

## Introduction

JavaScript’s built-in Error object carries name and message (and, in modern engines, cause). new Error() creates one. Error.isError(x) is true only for real Error instances, not look-alike objects. The name property is one of EvalError (deprecated), RangeError, ReferenceError, SyntaxError, TypeError, or URIError. The page Tryits catch those (SyntaxError via eval so it is runtime-catchable). Skip non-standard properties such as description, stack-as-API, and evalError().

This section has **11** examples:

- [x] **Example 1:** new Error() — creates an Error object [View](#js-error-object-example-01)
- [x] **Example 2:** name — sets or returns the error name [View](#js-error-object-example-02)
- [x] **Example 3:** message — sets or returns the error message [View](#js-error-object-example-03)
- [x] **Example 4:** cause — sets or returns an error cause [View](#js-error-object-example-04)
- [x] **Example 5:** Error.isError(x) — true only for real Error objects [View](#js-error-object-example-05)
- [x] **Example 6:** EvalError — deprecated name; use SyntaxError [View](#js-error-object-example-06)
- [x] **Example 7:** RangeError — a number out of range [View](#js-error-object-example-07)
- [x] **Example 8:** ReferenceError — an illegal reference [View](#js-error-object-example-08)
- [x] **Example 9:** SyntaxError — eval of invalid source [View](#js-error-object-example-09)
- [x] **Example 10:** TypeError — wrong type for the operation [View](#js-error-object-example-10)
- [x] **Example 11:** URIError — decodeURI / encodeURI malformed [View](#js-error-object-example-11)

## Detailed Explanation

- [x] **`new Error()`** / **`new Error(message)`**. **`name`** defaults to **Error**. **`message`** defaults to **`""`**.
- [x] **`cause`** wraps an inner error: `new Error("outer", { cause: inner })`.
- [x] **`Error.isError`**: **true** for `new Error`, **false** for `{ name: "Error" }` and **null**.
- [x] **Six names:** EvalError (deprecated), RangeError, ReferenceError, SyntaxError, TypeError, URIError.
- [x] Do **not** use **`err.description`** (Microsoft only) or the other non-standard rows.

<a id="js-error-object-example-01"></a>

### **Example 1: new Error() — creates an Error object**

- [x] `new Error()` builds a built-in **Error** object.
- [x] With no message, **`message`** is **`""`**. **`name`** is **`"Error"`**.

Sandbox: `code_sandbox/js-error-object/new-error.html`

```javascript
const err = new Error();
const err2 = new Error("Something went wrong");
```

<img alt="js-error-object example 1 source" src="./code_sandbox/snaps/js-error-object-01-code.png" />

<img alt="js-error-object example 1 result" src="./code_sandbox/snaps/js-error-object-01-result.png" />

- [x] **Outcome:** `new Error()` → name **Error**, message **""**. `new Error("Something went wrong")` → message **Something went wrong**.

<a id="js-error-object-example-02"></a>

### **Example 2: name — sets or returns the error name**

- [x] **`name`** is the error **kind** (`Error`, `TypeError`, `RangeError`, …).
- [x] You can **read** it after `catch`, or **set** it on a custom Error.

Sandbox: `code_sandbox/js-error-object/error-name.html`

```javascript
const err = new Error("boom");
err.name;
err.name = "MyError";
```

<img alt="js-error-object example 2 source" src="./code_sandbox/snaps/js-error-object-02-code.png" />

<img alt="js-error-object example 2 result" src="./code_sandbox/snaps/js-error-object-02-result.png" />

- [x] **Outcome:** Default **`name`** is **"Error"**. After `err.name = "MyError"` it is **"MyError"** (message still **boom**).

<a id="js-error-object-example-03"></a>

### **Example 3: message — sets or returns the error message**

- [x] **`message`** is the human-readable description.
- [x] Pass it to **`new Error(message)`**, or assign **`err.message`** later.

Sandbox: `code_sandbox/js-error-object/error-message.html`

```javascript
const err = new Error("first");
err.message = "second";
```

<img alt="js-error-object example 3 source" src="./code_sandbox/snaps/js-error-object-03-code.png" />

<img alt="js-error-object example 3 result" src="./code_sandbox/snaps/js-error-object-03-result.png" />

- [x] **Outcome:** Constructor message is **"first"**. After assign, **`err.message`** is **"second"**.

<a id="js-error-object-example-04"></a>

### **Example 4: cause — sets or returns an error cause**

- [x] **`cause`** chains the **underlying** error: `new Error(msg, { cause })`.
- [x] Catch the inner error, wrap it, and still read **`err.cause`**.

Sandbox: `code_sandbox/js-error-object/error-cause.html`

```javascript
try {
  throw new TypeError("inner");
} catch (inner) {
  throw new Error("outer", { cause: inner });
}
```

<img alt="js-error-object example 4 source" src="./code_sandbox/snaps/js-error-object-04-code.png" />

<img alt="js-error-object example 4 result" src="./code_sandbox/snaps/js-error-object-04-result.png" />

- [x] **Outcome:** Outer **Error**: **outer**. `err.cause` is **TypeError**: **inner**.

<a id="js-error-object-example-05"></a>

### **Example 5: Error.isError(x) — true only for real Error objects**

- [x] **`Error.isError(x)`** is **true** if `x` is an Error (including TypeError, …).
- [x] A plain `{ name: "Error" }` object is **false** — it only looks like one.

Sandbox: `code_sandbox/js-error-object/error-is-error.html`

```javascript
Error.isError(new Error("x"));
Error.isError({ name: "Error", message: "x" });
```

<img alt="js-error-object example 5 source" src="./code_sandbox/snaps/js-error-object-05-code.png" />

<img alt="js-error-object example 5 result" src="./code_sandbox/snaps/js-error-object-05-result.png" />

- [x] **Outcome:** **Error.isError** is a **function**. `new Error("x")` → **true**. `{name:"Error", message:"x"}` → **false**.

<a id="js-error-object-example-06"></a>

### **Example 6: EvalError — deprecated name; use SyntaxError**

- [x] Six values for **`name`**: EvalError, RangeError, ReferenceError, SyntaxError, TypeError, URIError.
- [x] **EvalError is deprecated** — do not expect `eval()` to throw it.

Sandbox: `code_sandbox/js-error-object/evalerror-name.html`

```javascript
const e = new EvalError("legacy");
try {
  eval("alert('Hello)");
} catch (err) {
  // SyntaxError
}
```

<img alt="js-error-object example 6 source" src="./code_sandbox/snaps/js-error-object-06-code.png" />

<img alt="js-error-object example 6 result" src="./code_sandbox/snaps/js-error-object-06-result.png" />

- [x] **Outcome:** `new EvalError` has name **EvalError**. `eval("alert('Hello)")` throws **SyntaxError**: **Invalid or unexpected token**.

<a id="js-error-object-example-07"></a>

### **Example 7: RangeError — a number out of range**

- [x] **RangeError**: a number is **out of range**.
- [x] The page Tryit uses **`toPrecision(500)`**.

Sandbox: `code_sandbox/js-error-object/rangeerror-name.html`

```javascript
let num = 1;
try {
  num.toPrecision(500);
} catch (err) {
  let text = err.name + "\n" + err.message;
}
```

<img alt="js-error-object example 7 source" src="./code_sandbox/snaps/js-error-object-07-code.png" />

<img alt="js-error-object example 7 result" src="./code_sandbox/snaps/js-error-object-07-result.png" />

- [x] **Outcome:** **RangeError**: **toPrecision() argument must be between 1 and 100**.

<a id="js-error-object-example-08"></a>

### **Example 8: ReferenceError — an illegal reference**

- [x] **ReferenceError**: an **illegal reference** (the page Tryit link is the undeclared-variable demo).
- [x] `x = y + 1` when `y` was never declared.

Sandbox: `code_sandbox/js-error-object/referenceerror-name.html`

```javascript
let x = 5;
try {
  x = y + 1;
} catch (err) {
  let text = err.name + "\n" + err.message;
}
```

<img alt="js-error-object example 8 source" src="./code_sandbox/snaps/js-error-object-08-code.png" />

<img alt="js-error-object example 8 result" src="./code_sandbox/snaps/js-error-object-08-result.png" />

- [x] **Outcome:** **ReferenceError**: **y is not defined**.

<a id="js-error-object-example-09"></a>

### **Example 9: SyntaxError — eval of invalid source**

- [x] **SyntaxError**: the source is not valid JavaScript.
- [x] The page Tryit uses **`eval("alert('Hello)")`** so the error is **runtime-catchable** (eval parses later).
- [x] A raw unclosed string in a `<script>` would **not** be catchable — see JS Errors Intro.

Sandbox: `code_sandbox/js-error-object/syntaxerror-name.html`

```javascript
try {
  eval("alert('Hello)");
} catch (err) {
  let text = err.name + "\n" + err.message;
}
```

<img alt="js-error-object example 9 source" src="./code_sandbox/snaps/js-error-object-09-code.png" />

<img alt="js-error-object example 9 result" src="./code_sandbox/snaps/js-error-object-09-result.png" />

- [x] **Outcome:** **SyntaxError**: **Invalid or unexpected token** (caught from `eval`, not from a parse-time script).

<a id="js-error-object-example-10"></a>

### **Example 10: TypeError — wrong type for the operation**

- [x] **TypeError**: a value is the **wrong type**.
- [x] The page Tryit is **`num.toUpperCase()`** on the number **1**.

Sandbox: `code_sandbox/js-error-object/typeerror-name.html`

```javascript
let num = 1;
try {
  num.toUpperCase();
} catch (err) {
  let text = err.name + "\n" + err.message;
}
```

<img alt="js-error-object example 10 source" src="./code_sandbox/snaps/js-error-object-10-code.png" />

<img alt="js-error-object example 10 result" src="./code_sandbox/snaps/js-error-object-10-result.png" />

- [x] **Outcome:** **TypeError**: **num.toUpperCase is not a function**.

<a id="js-error-object-example-11"></a>

### **Example 11: URIError — decodeURI / encodeURI malformed**

- [x] **URIError**: illegal characters in a **URI** function (`decodeURI`, `encodeURI`, …).
- [x] The Tryit is **`decodeURI("%%%")`**. The table text also mentions **`encodeURI()`**.

Sandbox: `code_sandbox/js-error-object/urierror-name.html`

```javascript
try {
  decodeURI("%%%");
} catch (err) {
  let text = err.name + "\n" + err.message;
}
```

<img alt="js-error-object example 11 source" src="./code_sandbox/snaps/js-error-object-11-code.png" />

<img alt="js-error-object example 11 result" src="./code_sandbox/snaps/js-error-object-11-result.png" />

- [x] **Outcome:** **URIError**: **URI malformed** for `decodeURI("%%%")`. `encodeURI` of an unpaired surrogate is also **URIError**: **URI malformed**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-error-object/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `new Error()` with no argument?

<details>
<summary>Answer</summary>

- [x] **name** **Error**, **message** **`""`**.

</details>

### Question 2: What is `new Error("Something went wrong").message`?

<details>
<summary>Answer</summary>

- [x] **Something went wrong**.

</details>

### Question 3: Can you assign `err.name = "MyError"`?

<details>
<summary>Answer</summary>

- [x] **Yes.** name becomes **MyError**; message stays **boom** in the demo.

</details>

### Question 4: What is `cause` in `new Error("outer", { cause: new TypeError("inner") })`?

<details>
<summary>Answer</summary>

- [x] **err.cause.name** is **TypeError**. **err.cause.message** is **inner**.

</details>

### Question 5: Is `{ name: "Error", message: "x" }` an Error?

<details>
<summary>Answer</summary>

- [x] **No.** `Error.isError(plain)` is **false**. `Error.isError(new Error("x"))` is **true**.
- [x] `Error.isError(null)` is **false**.

</details>

### Question 6: Does `eval("alert('Hello)")` throw EvalError?

<details>
<summary>Answer</summary>

- [x] **No.** **SyntaxError**: **Invalid or unexpected token**.
- [x] `new EvalError("legacy").name` is still **EvalError**.

</details>

### Question 7: What is `num.toPrecision(500)`?

<details>
<summary>Answer</summary>

- [x] **RangeError**: **toPrecision() argument must be between 1 and 100**.

</details>

### Question 8: What is `x = y + 1` with no `y`?

<details>
<summary>Answer</summary>

- [x] **ReferenceError**: **y is not defined**.

</details>

### Question 9: Why can the SyntaxError Tryit use try/catch?

<details>
<summary>Answer</summary>

- [x] It uses **`eval(...)`**, which parses **at runtime**.
- [x] A raw `let x = Math.round(4.6;)` in a script is **not** catchable.

</details>

### Question 10: What is `(1).toUpperCase()`?

<details>
<summary>Answer</summary>

- [x] **TypeError**: **num.toUpperCase is not a function**.

</details>

### Question 11: What is `decodeURI("%%%")`?

<details>
<summary>Answer</summary>

- [x] **URIError**: **URI malformed**.
- [x] `encodeURI` of an unpaired surrogate is the same **URIError**: **URI malformed**.

</details>

### Question 12: Should you use `err.description`?

<details>
<summary>Answer</summary>

- [x] **No.** Microsoft-only / non-standard. Use **`err.message`**.

</details>


</details>

## Summary

Create errors with new Error, read name and message, and chain with cause. Error.isError distinguishes real errors from plain objects. The six name values match the intro types; EvalError is only a constructor now. Catch eval SyntaxErrors at runtime; parse-time SyntaxErrors still need new Function if you want a demo page.

## References

- [JS Error Object (W3Schools)](https://www.w3schools.com/js/js_error_object.asp)
- [MDN: Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
- [MDN: Error.isError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/isError)
- [MDN: Error.cause](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause)

</details>
