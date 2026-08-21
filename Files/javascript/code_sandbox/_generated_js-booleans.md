<details>
  <summary>JS Booleans</summary>

## Introduction

A **Boolean** is only **`true`** or **`false`** (lowercase, unquoted). Comparisons, `if` tests, and loop conditions all produce or use booleans. **`Boolean(value)`** converts. Most values are **truthy**; **0, -0, "", undefined, null, false, NaN** are **falsy**. Do **not** use **`new Boolean()`**.

This section has **25** examples:

- [x] **Example 1:** Equal to — (x == 8) is false [View](#js-booleans-example-01)
- [x] **Example 2:** Not equal — (x != 8) is true [View](#js-booleans-example-02)
- [x] **Example 3:** Greater than — (x > 8) is false [View](#js-booleans-example-03)
- [x] **Example 4:** Less than — (x < 8) is true [View](#js-booleans-example-04)
- [x] **Example 5:** if (day == "Monday") [View](#js-booleans-example-05)
- [x] **Example 6:** if (salary > 9000) [View](#js-booleans-example-06)
- [x] **Example 7:** if (age < 18) [View](#js-booleans-example-07)
- [x] **Example 8:** if / else greeting uses a boolean test [View](#js-booleans-example-08)
- [x] **Example 9:** for (i = 0; i < 5; i++) [View](#js-booleans-example-09)
- [x] **Example 10:** while (i < 10) [View](#js-booleans-example-10)
- [x] **Example 11:** for (x in person) [View](#js-booleans-example-11)
- [x] **Example 12:** for (x of cars) [View](#js-booleans-example-12)
- [x] **Example 13:** Boolean(10 > 9) [View](#js-booleans-example-13)
- [x] **Example 14:** (10 > 9) without Boolean() [View](#js-booleans-example-14)
- [x] **Example 15:** Everything with a value is true [View](#js-booleans-example-15)
- [x] **Example 16:** Boolean(0) is false [View](#js-booleans-example-16)
- [x] **Example 17:** Boolean(-0) is false [View](#js-booleans-example-17)
- [x] **Example 18:** Boolean("") is false [View](#js-booleans-example-18)
- [x] **Example 19:** Boolean(undefined) is false [View](#js-booleans-example-19)
- [x] **Example 20:** Boolean(null) is false [View](#js-booleans-example-20)
- [x] **Example 21:** Boolean(false) is false [View](#js-booleans-example-21)
- [x] **Example 22:** Boolean(NaN) is false [View](#js-booleans-example-22)
- [x] **Example 23:** typeof primitive boolean vs new Boolean() [View](#js-booleans-example-23)
- [x] **Example 24:** Boolean(false) == new Boolean(false) [View](#js-booleans-example-24)
- [x] **Example 25:** Comparing two Boolean objects is false [View](#js-booleans-example-25)

## Detailed Explanation

- [x] **true** / **false** are the only boolean primitives. Write them **lowercase** without quotes.
- [x] Comparisons (`==`, `!=`, `<`, `>`) **return** booleans. `if` and loops **test** them.
- [x] **Truthy:** numbers other than 0, non-empty strings (including `"false"`), arrays, objects. **Falsy:** 0, -0, "", undefined, null, false, NaN.
- [x] `Boolean()` converts. `(10 > 9)` is already a boolean. **`new Boolean()`** makes an **object** — avoid it.

<a id="js-booleans-example-01"></a>

### **Example 1: Equal to — (x == 8) is false**

- [x] A **Boolean** is a primitive that is only **`true`** or **`false`** (lowercase, **no quotes**).
- [x] Comparison operators **return** booleans. Given **`x = 5`**, **`(x == 8)`** is **false**.

Sandbox: `code_sandbox/js-booleans/eq-false.html`

```javascript
let x = 5;
let result = (x == 8);
```

<img alt="js-booleans example 1 source" src="./code_sandbox/snaps/js-booleans-01-code.png" />

<img alt="js-booleans example 1 result" src="./code_sandbox/snaps/js-booleans-01-result.png" />

- [x] **Outcome:** **5 == 8** is **false**.

<a id="js-booleans-example-02"></a>

### **Example 2: Not equal — (x != 8) is true**

- [x] Same **`x = 5`**. **`(x != 8)`** is **true**.
- [x] This is the second row of the page’s comparison table (and half of the combined Tryit).

Sandbox: `code_sandbox/js-booleans/neq-true.html`

```javascript
let x = 5;
let result = (x != 8);
```

<img alt="js-booleans example 2 source" src="./code_sandbox/snaps/js-booleans-02-code.png" />

<img alt="js-booleans example 2 result" src="./code_sandbox/snaps/js-booleans-02-result.png" />

- [x] **Outcome:** **5 != 8** is **true**.

<a id="js-booleans-example-03"></a>

### **Example 3: Greater than — (x > 8) is false**

- [x] **`(x > 8)`** with **x = 5** is **false**.
- [x] Booleans from comparisons are what `if` tests.

Sandbox: `code_sandbox/js-booleans/gt-false.html`

```javascript
let x = 5;
let result = (x > 8);
```

<img alt="js-booleans example 3 source" src="./code_sandbox/snaps/js-booleans-03-code.png" />

<img alt="js-booleans example 3 result" src="./code_sandbox/snaps/js-booleans-03-result.png" />

- [x] **Outcome:** **5 > 8** is **false**.

<a id="js-booleans-example-04"></a>

### **Example 4: Less than — (x < 8) is true**

- [x] **`(x < 8)`** with **x = 5** is **true**.
- [x] The page’s comparison Tryit shows `==` and `!=`; this row completes the table.

Sandbox: `code_sandbox/js-booleans/lt-true.html`

```javascript
let x = 5;
let result = (x < 8);
```

<img alt="js-booleans example 4 source" src="./code_sandbox/snaps/js-booleans-04-code.png" />

<img alt="js-booleans example 4 result" src="./code_sandbox/snaps/js-booleans-04-result.png" />

- [x] **Outcome:** **5 < 8** is **true**.

<a id="js-booleans-example-05"></a>

### **Example 5: if (day == "Monday")**

- [x] `if` conditions are booleans. **`day == "Monday"`** is true or false.
- [x] Pin **`day = "Monday"`** so the test is **true** and the block runs.

Sandbox: `code_sandbox/js-booleans/if-monday.html`

```javascript
let day = "Monday";
let text = "not Monday";
if (day == "Monday") {
  text = "It is Monday";
}
```

<img alt="js-booleans example 5 source" src="./code_sandbox/snaps/js-booleans-05-code.png" />

<img alt="js-booleans example 5 result" src="./code_sandbox/snaps/js-booleans-05-result.png" />

- [x] **Outcome:** **day** is **Monday**, so the `if` is **true** and text is **It is Monday**.

<a id="js-booleans-example-06"></a>

### **Example 6: if (salary > 9000)**

- [x] Numeric comparisons are booleans too. Pin **`salary = 12000`**.
- [x] **12000 > 9000** is **true**.

Sandbox: `code_sandbox/js-booleans/if-salary.html`

```javascript
let salary = 12000;
let text = "below";
if (salary > 9000) {
  text = "above 9000";
}
```

<img alt="js-booleans example 6 source" src="./code_sandbox/snaps/js-booleans-06-code.png" />

<img alt="js-booleans example 6 result" src="./code_sandbox/snaps/js-booleans-06-result.png" />

- [x] **Outcome:** **12000 > 9000** is **true**, so text is **above 9000**.

<a id="js-booleans-example-07"></a>

### **Example 7: if (age < 18)**

- [x] Pin **`age = 16`**. **16 < 18** is **true** (too young in this test).

Sandbox: `code_sandbox/js-booleans/if-age.html`

```javascript
let age = 16;
let text = "adult path";
if (age < 18) {
  text = "too young";
}
```

<img alt="js-booleans example 7 source" src="./code_sandbox/snaps/js-booleans-07-code.png" />

<img alt="js-booleans example 7 result" src="./code_sandbox/snaps/js-booleans-07-result.png" />

- [x] **Outcome:** **16 < 18** is **true**, so text is **too young**.

<a id="js-booleans-example-08"></a>

### **Example 8: if / else greeting uses a boolean test**

- [x] The page’s condition Tryit is the familiar **hour < 18** greeting.
- [x] Pin **`hour = 10`**. The `if` condition is **true**, so greeting is **Good day**.

Sandbox: `code_sandbox/js-booleans/if-else-hour.html`

```javascript
let hour = 10;
let greeting;
if (hour < 18) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}
```

<img alt="js-booleans example 8 source" src="./code_sandbox/snaps/js-booleans-08-code.png" />

<img alt="js-booleans example 8 result" src="./code_sandbox/snaps/js-booleans-08-result.png" />

- [x] **Outcome:** **hour < 18** is **true**, so greeting is **Good day**.

<a id="js-booleans-example-09"></a>

### **Example 9: for (i = 0; i < 5; i++)**

- [x] Loop conditions are booleans. **`i < 5`** is re-tested every iteration.
- [x] The loop body runs while that test is **true** (i = 0,1,2,3,4).

Sandbox: `code_sandbox/js-booleans/for-loop.html`

```javascript
let text = "";
for (let i = 0; i < 5; i++) {
  text += i;
}
```

<img alt="js-booleans example 9 source" src="./code_sandbox/snaps/js-booleans-09-code.png" />

<img alt="js-booleans example 9 result" src="./code_sandbox/snaps/js-booleans-09-result.png" />

- [x] **Outcome:** The loop appends **0** through **4**, so text is **01234**.

<a id="js-booleans-example-10"></a>

### **Example 10: while (i < 10)**

- [x] The page’s loop Tryit: **`while (i < 10) { text += i; i++; }`**.
- [x] `i < 10` is the boolean that keeps the loop going.

Sandbox: `code_sandbox/js-booleans/while-loop.html`

```javascript
let text = "";
let i = 0;
while (i < 10) {
  text += i;
  i++;
}
```

<img alt="js-booleans example 10 source" src="./code_sandbox/snaps/js-booleans-10-code.png" />

<img alt="js-booleans example 10 result" src="./code_sandbox/snaps/js-booleans-10-result.png" />

- [x] **Outcome:** text is **0123456789** and **i** is **10** (the test is then false).

<a id="js-booleans-example-11"></a>

### **Example 11: for (x in person)**

- [x] **`for…in`** walks **enumerable keys**. The loop *runs* while there are keys left (the engine’s condition is still boolean under the hood).
- [x] This sandbox uses `{fname:"John", lname:"Doe"}` and concatenates values.

Sandbox: `code_sandbox/js-booleans/for-in-loop.html`

```javascript
const person = {fname: "John", lname: "Doe"};
let text = "";
for (let x in person) {
  text += person[x];
}
```

<img alt="js-booleans example 11 source" src="./code_sandbox/snaps/js-booleans-11-code.png" />

<img alt="js-booleans example 11 result" src="./code_sandbox/snaps/js-booleans-11-result.png" />

- [x] **Outcome:** text is **JohnDoe** (fname then lname).

<a id="js-booleans-example-12"></a>

### **Example 12: for (x of cars)**

- [x] **`for…of`** walks **iterable values** (array elements), not keys.
- [x] `["BMW", "Volvo"]` yields two iterations.

Sandbox: `code_sandbox/js-booleans/for-of-loop.html`

```javascript
const cars = ["BMW", "Volvo"];
let text = "";
for (let x of cars) {
  text += x;
}
```

<img alt="js-booleans example 12 source" src="./code_sandbox/snaps/js-booleans-12-code.png" />

<img alt="js-booleans example 12 result" src="./code_sandbox/snaps/js-booleans-12-result.png" />

- [x] **Outcome:** text is **BMWVolvo**.

<a id="js-booleans-example-13"></a>

### **Example 13: Boolean(10 > 9)**

- [x] **`Boolean(expression)`** converts a value to **true** or **false**.
- [x] **`Boolean(10 > 9)`** is **true** because the comparison is already true.

Sandbox: `code_sandbox/js-booleans/boolean-fn.html`

```javascript
let result = Boolean(10 > 9);
```

<img alt="js-booleans example 13 source" src="./code_sandbox/snaps/js-booleans-13-code.png" />

<img alt="js-booleans example 13 result" src="./code_sandbox/snaps/js-booleans-13-result.png" />

- [x] **Outcome:** **Boolean(10 > 9)** is **true**.

<a id="js-booleans-example-14"></a>

### **Example 14: (10 > 9) without Boolean()**

- [x] The page says you can skip `Boolean()`: **`(10 > 9)`** already is a boolean.
- [x] That is “even easier” than wrapping it.

Sandbox: `code_sandbox/js-booleans/bare-compare.html`

```javascript
let result = (10 > 9);
```

<img alt="js-booleans example 14 source" src="./code_sandbox/snaps/js-booleans-14-code.png" />

<img alt="js-booleans example 14 result" src="./code_sandbox/snaps/js-booleans-14-result.png" />

- [x] **Outcome:** **(10 > 9)** is **true**, and **typeof** is **boolean**.

<a id="js-booleans-example-15"></a>

### **Example 15: Everything with a value is true**

- [x] Values that are **truthy** become **true** in a boolean context: numbers other than 0, non-empty strings, `true`, arrays, objects.
- [x] The string **`"false"`** is truthy — it is not the boolean `false`.
- [x] **`[]`** and **`{}`** are truthy because **all objects** are true in a boolean context, even when empty.

Sandbox: `code_sandbox/js-booleans/truthy-values.html`

```javascript
let rows = [
  ["100", Boolean(100)],
  ["3.14", Boolean(3.14)],
  ["-15", Boolean(-15)],
  ["true", Boolean(true)],
  ['"Hello"', Boolean("Hello")],
  ['"false"', Boolean("false")],
  ["7+1+3.14", Boolean(7 + 1 + 3.14)],
  ["[]", Boolean([])],
  ["{}", Boolean({})]
];
```

<img alt="js-booleans example 15 source" src="./code_sandbox/snaps/js-booleans-15-code.png" />

<img alt="js-booleans example 15 result" src="./code_sandbox/snaps/js-booleans-15-result.png" />

- [x] **Outcome:** Every listed value is **true**, including **`"false"`**, **`[]`**, and **`{}`**.

<a id="js-booleans-example-16"></a>

### **Example 16: Boolean(0) is false**

- [x] Values **without a “value”** are **falsy**. **`0`** is false.
- [x] This is its own Tryit on the page.

Sandbox: `code_sandbox/js-booleans/falsy-zero.html`

```javascript
let x = 0;
let result = Boolean(x);
```

<img alt="js-booleans example 16 source" src="./code_sandbox/snaps/js-booleans-16-code.png" />

<img alt="js-booleans example 16 result" src="./code_sandbox/snaps/js-booleans-16-result.png" />

- [x] **Outcome:** **Boolean(0)** is **false**.

<a id="js-booleans-example-17"></a>

### **Example 17: Boolean(-0) is false**

- [x] **`-0`** (minus zero) is also false. JavaScript has a signed zero; both are falsy.

Sandbox: `code_sandbox/js-booleans/falsy-negzero.html`

```javascript
let x = -0;
let result = Boolean(x);
```

<img alt="js-booleans example 17 source" src="./code_sandbox/snaps/js-booleans-17-code.png" />

<img alt="js-booleans example 17 result" src="./code_sandbox/snaps/js-booleans-17-result.png" />

- [x] **Outcome:** **Boolean(-0)** is **false**. **Object.is(x, -0)** is **true** so this really is minus zero.

<a id="js-booleans-example-18"></a>

### **Example 18: Boolean("") is false**

- [x] An **empty string** `""` is false. Any non-empty string (even `"0"` or `"false"`) is true.

Sandbox: `code_sandbox/js-booleans/falsy-empty-string.html`

```javascript
let x = "";
let result = Boolean(x);
```

<img alt="js-booleans example 18 source" src="./code_sandbox/snaps/js-booleans-18-code.png" />

<img alt="js-booleans example 18 result" src="./code_sandbox/snaps/js-booleans-18-result.png" />

- [x] **Outcome:** **Boolean("")** is **false**.

<a id="js-booleans-example-19"></a>

### **Example 19: Boolean(undefined) is false**

- [x] A declared-but-unassigned variable is **`undefined`**, which is false.

Sandbox: `code_sandbox/js-booleans/falsy-undefined.html`

```javascript
let x;
let result = Boolean(x);
```

<img alt="js-booleans example 19 source" src="./code_sandbox/snaps/js-booleans-19-code.png" />

<img alt="js-booleans example 19 result" src="./code_sandbox/snaps/js-booleans-19-result.png" />

- [x] **Outcome:** **Boolean(undefined)** is **false**.

<a id="js-booleans-example-20"></a>

### **Example 20: Boolean(null) is false**

- [x] **`null`** is the intentional empty value. It is false.

Sandbox: `code_sandbox/js-booleans/falsy-null.html`

```javascript
let x = null;
let result = Boolean(x);
```

<img alt="js-booleans example 20 source" src="./code_sandbox/snaps/js-booleans-20-code.png" />

<img alt="js-booleans example 20 result" src="./code_sandbox/snaps/js-booleans-20-result.png" />

- [x] **Outcome:** **Boolean(null)** is **false**.

<a id="js-booleans-example-21"></a>

### **Example 21: Boolean(false) is false**

- [x] The boolean **`false`** is (you guessed it) false.

Sandbox: `code_sandbox/js-booleans/falsy-false.html`

```javascript
let x = false;
let result = Boolean(x);
```

<img alt="js-booleans example 21 source" src="./code_sandbox/snaps/js-booleans-21-code.png" />

<img alt="js-booleans example 21 result" src="./code_sandbox/snaps/js-booleans-21-result.png" />

- [x] **Outcome:** **Boolean(false)** is **false**.

<a id="js-booleans-example-22"></a>

### **Example 22: Boolean(NaN) is false**

- [x] The page uses **`10 / "Hallo"`** to get **`NaN`**. **`Boolean(NaN)`** is false.

Sandbox: `code_sandbox/js-booleans/falsy-nan.html`

```javascript
let x = 10 / "Hallo";
let result = Boolean(x);
```

<img alt="js-booleans example 22 source" src="./code_sandbox/snaps/js-booleans-22-code.png" />

<img alt="js-booleans example 22 result" src="./code_sandbox/snaps/js-booleans-22-result.png" />

- [x] **Outcome:** **x** is **NaN**, and **Boolean(NaN)** is **false**.

<a id="js-booleans-example-23"></a>

### **Example 23: typeof primitive boolean vs new Boolean()**

- [x] Normal booleans are **primitives**: `let x = false` → **typeof boolean**.
- [x] **`new Boolean(false)`** is an **object**. **Do not** create Boolean objects — they slow code and confuse `===`.

Sandbox: `code_sandbox/js-booleans/bool-object-typeof.html`

```javascript
let x = false;
let y = new Boolean(false);
```

<img alt="js-booleans example 23 source" src="./code_sandbox/snaps/js-booleans-23-code.png" />

<img alt="js-booleans example 23 result" src="./code_sandbox/snaps/js-booleans-23-result.png" />

- [x] **Outcome:** **typeof x** is **boolean**; **typeof y** is **object**.

<a id="js-booleans-example-24"></a>

### **Example 24: Boolean(false) == new Boolean(false)**

- [x] `Boolean(false)` (the function, **without** `new`) returns the primitive **false**.
- [x] `new Boolean(false)` is an object. **`==`** is **true** (object converted); **`===`** is **false** (different types).
- [x] The page warns: booleans and boolean objects cannot be compared safely.

Sandbox: `code_sandbox/js-booleans/bool-object-compare.html`

```javascript
let x = Boolean(false);
let y = new Boolean(false);
```

<img alt="js-booleans example 24 source" src="./code_sandbox/snaps/js-booleans-24-code.png" />

<img alt="js-booleans example 24 result" src="./code_sandbox/snaps/js-booleans-24-result.png" />

- [x] **Outcome:** **x == y** is **true**; **x === y** is **false**.

<a id="js-booleans-example-25"></a>

### **Example 25: Comparing two Boolean objects is false**

- [x] Comparing **two objects** with `==` or `===` is **false** unless they are the **same reference**.
- [x] Two `new Boolean(false)` values are two objects, so **`a == b`** is **false**.

Sandbox: `code_sandbox/js-booleans/two-objects-false.html`

```javascript
let a = new Boolean(false);
let b = new Boolean(false);
```

<img alt="js-booleans example 25 source" src="./code_sandbox/snaps/js-booleans-25-code.png" />

<img alt="js-booleans example 25 result" src="./code_sandbox/snaps/js-booleans-25-result.png" />

- [x] **Outcome:** **a == b** and **a === b** are both **false** (two different objects).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-booleans/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What values can a boolean primitive hold?

<details>
<summary>Answer</summary>

- [x] Only **true** and **false**.

</details>

### Question 2: Must they be lowercase and unquoted?

<details>
<summary>Answer</summary>

- [x] **Yes.** `True` or `"false"` are not the boolean keywords.

</details>

### Question 3: With `x = 5`, what is `x == 8` and `x != 8`?

<details>
<summary>Answer</summary>

- [x] **false** and **true**.

</details>

### Question 4: What is `Boolean(10 > 9)`?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 5: Is `Boolean("false")` false?

<details>
<summary>Answer</summary>

- [x] **No.** A non-empty string is **true**.

</details>

### Question 6: Are `[]` and `{}` true or false?

<details>
<summary>Answer</summary>

- [x] **true** — they are objects, and objects are truthy.

</details>

### Question 7: Name the falsy values from this page.

<details>
<summary>Answer</summary>

- [x] **0**, **-0**, **""**, **undefined**, **null**, **false**, **NaN**.

</details>

### Question 8: What is `typeof new Boolean(false)`?

<details>
<summary>Answer</summary>

- [x] **object** (the primitive is **boolean**).

</details>

### Question 9: Does `Boolean(false) === new Boolean(false)`?

<details>
<summary>Answer</summary>

- [x] **No** (`===` is false). Loose `==` can be **true**.

</details>

### Question 10: Does `new Boolean(false) == new Boolean(false)`?

<details>
<summary>Answer</summary>

- [x] **No.** Two objects compare **false**.

</details>


</details>

## Summary

Booleans are **true**/**false**. Comparisons and `if`/`while` use them. **`Boolean(10 > 9)`** is **true**. Most values are truthy; **0, -0, "", undefined, null, false, NaN** are not. Skip **`new Boolean()`**.

## References

- [JS Booleans (W3Schools)](https://www.w3schools.com/js/js_booleans.asp)
- [MDN: Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
- [JS Boolean Reference (W3Schools)](https://www.w3schools.com/jsref/jsref_obj_boolean.asp)

</details>
