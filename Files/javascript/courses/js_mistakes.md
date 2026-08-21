# JS Mistakes

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Common mistakes: = inside if (assignment is truthy/falsy), == vs ===, switch’s strict case matching, + adding vs concatenating, 0.1+0.2, breaking strings, a semicolon after if (), breaking after return (ASI → undefined), named array indexes, trailing commas in JSON, and testing null before typeof on an undeclared name.

This section has **26** examples:

- [x] **Example 1:** if (x == 10) is false when x is 0 [View](#js-mistakes-example-01)
- [x] **Example 2:** if (x = 10) is true — assignment, not comparison [View](#js-mistakes-example-02)
- [x] **Example 3:** if (x = 0) is false — 0 is falsy [View](#js-mistakes-example-03)
- [x] **Example 4:** 10 == "10" is true (loose comparison) [View](#js-mistakes-example-04)
- [x] **Example 5:** 10 === "10" is false (strict comparison) [View](#js-mistakes-example-05)
- [x] **Example 6:** switch(x) case 10 matches number 10 [View](#js-mistakes-example-06)
- [x] **Example 7:** switch(x) case "10" does not match number 10 [View](#js-mistakes-example-07)
- [x] **Example 8:** 10 + 5 is 15; 10 += "5" is "105" [View](#js-mistakes-example-08)
- [x] **Example 9:** x + y is 15 or "105" depending on y's type [View](#js-mistakes-example-09)
- [x] **Example 10:** 0.1 + 0.2 is not 0.3 [View](#js-mistakes-example-10)
- [x] **Example 11:** (x * 10 + y * 10) / 10 is 0.3 [View](#js-mistakes-example-11)
- [x] **Example 12:** You may break a statement after = across two lines [View](#js-mistakes-example-12)
- [x] **Example 13:** Breaking in the middle of a string is a SyntaxError [View](#js-mistakes-example-13)
- [x] **Example 14:** Backslash continues a string across lines [View](#js-mistakes-example-14)
- [x] **Example 15:** if (x == 19);{ } always runs the block [View](#js-mistakes-example-15)
- [x] **Example 16:** return a * power works without semicolons (ASI) [View](#js-mistakes-example-16)
- [x] **Example 17:** return a * power with semicolons — same result [View](#js-mistakes-example-17)
- [x] **Example 18:** You may break after `return a *` onto the next line [View](#js-mistakes-example-18)
- [x] **Example 19:** Never break after return — it becomes return; [View](#js-mistakes-example-19)
- [x] **Example 20:** ASI reads that as return; a * power; [View](#js-mistakes-example-20)
- [x] **Example 21:** Arrays use numbered indexes — length 3, person[0] is John [View](#js-mistakes-example-21)
- [x] **Example 22:** person["firstName"] turns the array into a plain object [View](#js-mistakes-example-22)
- [x] **Example 23:** Trailing commas in objects/arrays are legal in ES5 [View](#js-mistakes-example-23)
- [x] **Example 24:** JSON.parse rejects trailing commas [View](#js-mistakes-example-24)
- [x] **Example 25:** if (typeof myObj === "undefined") is safe [View](#js-mistakes-example-25)
- [x] **Example 26:** Test typeof !== undefined before !== null [View](#js-mistakes-example-26)

## Detailed Explanation

- [x] `if (x = 10)` **assigns**. `if (x = 0)` is **falsy**.
- [x] **switch** uses **`===`**. `case "10":` misses number **10**.
- [x] `0.1 + 0.2 !== 0.3`. Scale by **10** to fix this example.
- [x] **Never** put **`;` after `if ()`**. **Never** break after **`return`**.
- [x] Named array indexes **drop** `length`. JSON **forbids** trailing commas. **`typeof` first**, then **`!== null`**.

<a id="js-mistakes-example-01"></a>

### **Example 1: if (x == 10) is false when x is 0**

- [x] `==` **compares**. `x` is **0**, so the condition is **false** (as expected).

Sandbox: `code_sandbox/js-mistakes/if-eqeq-10.html`

```javascript
let x = 0;
if (x == 10) { /* ... */ }
```

<img alt="js-mistakes example 1 source" src="../code_sandbox/snaps/js-mistakes-01-code.png" />

<img alt="js-mistakes example 1 result" src="../code_sandbox/snaps/js-mistakes-01-result.png" />

- [x] **Outcome:** Condition is **false**. The block does **not** run.

<a id="js-mistakes-example-02"></a>

### **Example 2: if (x = 10) is true — assignment, not comparison**

- [x] `x = 10` **assigns 10**. The value of an assignment is the assigned value.
- [x] **10 is truthy**, so the `if` runs — maybe **not** what you expected.

Sandbox: `code_sandbox/js-mistakes/if-assign-10.html`

```javascript
let x = 0;
if (x = 10) { /* ... */ }
```

<img alt="js-mistakes example 2 source" src="../code_sandbox/snaps/js-mistakes-02-code.png" />

<img alt="js-mistakes example 2 result" src="../code_sandbox/snaps/js-mistakes-02-result.png" />

- [x] **Outcome:** Condition is **true**. **x** is now **10**. Block **ran**.

<a id="js-mistakes-example-03"></a>

### **Example 3: if (x = 0) is false — 0 is falsy**

- [x] Assignment of **0** yields **0**, which is **falsy**.
- [x] The block **does not run** — also surprising if you thought you were comparing.

Sandbox: `code_sandbox/js-mistakes/if-assign-0.html`

```javascript
let x = 0;
if (x = 0) { /* ... */ }
```

<img alt="js-mistakes example 3 source" src="../code_sandbox/snaps/js-mistakes-03-code.png" />

<img alt="js-mistakes example 3 result" src="../code_sandbox/snaps/js-mistakes-03-result.png" />

- [x] **Outcome:** Condition is **false**. **x** is **0**. Block **did not run**.

<a id="js-mistakes-example-04"></a>

### **Example 4: 10 == "10" is true (loose comparison)**

- [x] With **`==`**, data type **does not matter**. `10 == "10"` is **true**.

Sandbox: `code_sandbox/js-mistakes/loose-eq-string-10.html`

```javascript
let x = 10;
let y = "10";
if (x == y) { /* true */ }
```

<img alt="js-mistakes example 4 source" src="../code_sandbox/snaps/js-mistakes-04-code.png" />

<img alt="js-mistakes example 4 result" src="../code_sandbox/snaps/js-mistakes-04-result.png" />

- [x] **Outcome:** **true**. The `if` **runs**.

<a id="js-mistakes-example-05"></a>

### **Example 5: 10 === "10" is false (strict comparison)**

- [x] With **`===`**, type **matters**. Number **10** is not string **"10"**.

Sandbox: `code_sandbox/js-mistakes/strict-eq-string-10.html`

```javascript
let x = 10;
let y = "10";
if (x === y) { /* false */ }
```

<img alt="js-mistakes example 5 source" src="../code_sandbox/snaps/js-mistakes-05-code.png" />

<img alt="js-mistakes example 5 result" src="../code_sandbox/snaps/js-mistakes-05-result.png" />

- [x] **Outcome:** **false**. The `if` does **not** run.

<a id="js-mistakes-example-06"></a>

### **Example 6: switch(x) case 10 matches number 10**

- [x] **`switch` uses strict comparison** (`===`).
- [x] `case 10:` matches number **10** — the page’s alert **Hello** would fire.

Sandbox: `code_sandbox/js-mistakes/switch-case-10.html`

```javascript
let x = 10;
switch(x) {
  case 10:
    alert("Hello");
}
```

<img alt="js-mistakes example 6 source" src="../code_sandbox/snaps/js-mistakes-06-code.png" />

<img alt="js-mistakes example 6 result" src="../code_sandbox/snaps/js-mistakes-06-result.png" />

- [x] **Outcome:** Match: this sandbox records **Hello** instead of `alert`.

<a id="js-mistakes-example-07"></a>

### **Example 7: switch(x) case "10" does not match number 10**

- [x] `case "10":` does **not** match number **10**. No alert.

Sandbox: `code_sandbox/js-mistakes/switch-case-string-10.html`

```javascript
let x = 10;
switch(x) {
  case "10":
    alert("Hello");
}
```

<img alt="js-mistakes example 7 source" src="../code_sandbox/snaps/js-mistakes-07-code.png" />

<img alt="js-mistakes example 7 result" src="../code_sandbox/snaps/js-mistakes-07-result.png" />

- [x] **Outcome:** **no match**. Strict `===` fails between **10** and **"10"**.

<a id="js-mistakes-example-08"></a>

### **Example 8: 10 + 5 is 15; 10 += "5" is "105"**

- [x] **`+`** adds numbers **or** concatenates strings.
- [x] `x = 10 + 5` → **15**. `y += "5"` → **`"105"`**.

Sandbox: `code_sandbox/js-mistakes/plus-vs-concat.html`

```javascript
let x = 10;
x = 10 + 5;
let y = 10;
y += "5";
```

<img alt="js-mistakes example 8 source" src="../code_sandbox/snaps/js-mistakes-08-code.png" />

<img alt="js-mistakes example 8 result" src="../code_sandbox/snaps/js-mistakes-08-result.png" />

- [x] **Outcome:** **x** is **15** (number). **y** is **"105"** (string).

<a id="js-mistakes-example-09"></a>

### **Example 9: x + y is 15 or "105" depending on y's type**

- [x] When both are numbers: **15**. When `y` is **"5"**: **`"105"`**.

Sandbox: `code_sandbox/js-mistakes/plus-two-variables.html`

```javascript
let x = 10;
let y = 5;
let z = x + y;
let y2 = "5";
let z2 = x + y2;
```

<img alt="js-mistakes example 9 source" src="../code_sandbox/snaps/js-mistakes-09-code.png" />

<img alt="js-mistakes example 9 result" src="../code_sandbox/snaps/js-mistakes-09-result.png" />

- [x] **Outcome:** **z** is **15**. **z2** is **"105"**.

<a id="js-mistakes-example-10"></a>

### **Example 10: 0.1 + 0.2 is not 0.3**

- [x] JS numbers are **IEEE-754 floats**. `0.1 + 0.2` is **0.30000000000000004**, not **0.3**.

Sandbox: `code_sandbox/js-mistakes/float-0-1-0-2.html`

```javascript
let x = 0.1;
let y = 0.2;
let z = x + y;
```

<img alt="js-mistakes example 10 source" src="../code_sandbox/snaps/js-mistakes-10-code.png" />

<img alt="js-mistakes example 10 result" src="../code_sandbox/snaps/js-mistakes-10-result.png" />

- [x] **Outcome:** **z === 0.3** is **false**. **z** prints as **0.30000000000000004**.

<a id="js-mistakes-example-11"></a>

### **Example 11: (x * 10 + y * 10) / 10 is 0.3**

- [x] Multiply to integers, add, divide back.

Sandbox: `code_sandbox/js-mistakes/float-fix.html`

```javascript
let z = (x * 10 + y * 10) / 10;
```

<img alt="js-mistakes example 11 source" src="../code_sandbox/snaps/js-mistakes-11-code.png" />

<img alt="js-mistakes example 11 result" src="../code_sandbox/snaps/js-mistakes-11-result.png" />

- [x] **Outcome:** **z** is **0.3**. **z === 0.3** is **true**.

<a id="js-mistakes-example-12"></a>

### **Example 12: You may break a statement after = across two lines**

- [x] A statement may continue on the next line after **`=`**.

Sandbox: `code_sandbox/js-mistakes/break-statement-ok.html`

```javascript
let x =
"Hello World!";
```

<img alt="js-mistakes example 12 source" src="../code_sandbox/snaps/js-mistakes-12-code.png" />

<img alt="js-mistakes example 12 result" src="../code_sandbox/snaps/js-mistakes-12-result.png" />

- [x] **Outcome:** **x** is **"Hello World!"**.

<a id="js-mistakes-example-13"></a>

### **Example 13: Breaking in the middle of a string is a SyntaxError**

- [x] A newline **inside quotes** (no backslash) **does not parse**.

Sandbox: `code_sandbox/js-mistakes/break-string-bad.html`

```javascript
let x = "Hello
World!";
```

<img alt="js-mistakes example 13 source" src="../code_sandbox/snaps/js-mistakes-13-code.png" />

<img alt="js-mistakes example 13 result" src="../code_sandbox/snaps/js-mistakes-13-result.png" />

- [x] **Outcome:** **SyntaxError: Invalid or unexpected token** (unterminated string).

<a id="js-mistakes-example-14"></a>

### **Example 14: Backslash continues a string across lines**

- [x] Use a **backslash** at the end of the line to continue the string.
- [x] Modern code often prefers a **template literal** instead.

Sandbox: `code_sandbox/js-mistakes/break-string-backslash.html`

```javascript
let x = "Hello \
World!";
```

<img alt="js-mistakes example 14 source" src="../code_sandbox/snaps/js-mistakes-14-code.png" />

<img alt="js-mistakes example 14 result" src="../code_sandbox/snaps/js-mistakes-14-result.png" />

- [x] **Outcome:** **x** is **"Hello World!"** (the newline after `\` is not in the string).

<a id="js-mistakes-example-15"></a>

### **Example 15: if (x == 19);{ } always runs the block**

- [x] The **`;` after `if (...)`** ends the `if` with an **empty** statement.
- [x] The `{ }` that follows is a **separate block** that **always runs**.

Sandbox: `code_sandbox/js-mistakes/misplaced-semicolon.html`

```javascript
if (x == 19);
{
  // code block
}
```

<img alt="js-mistakes example 15 source" src="../code_sandbox/snaps/js-mistakes-15-code.png" />

<img alt="js-mistakes example 15 result" src="../code_sandbox/snaps/js-mistakes-15-result.png" />

- [x] **Outcome:** Even with **x = 0**, the block **runs** (`ran` is **true**). Without the extra `;`, it would not.

<a id="js-mistakes-example-16"></a>

### **Example 16: return a * power works without semicolons (ASI)**

- [x] ASI will insert semicolons. This function still returns **`a * 10`**.

Sandbox: `code_sandbox/js-mistakes/return-no-semicolons.html`

```javascript
function myFunction(a) {
  let power = 10
  return a * power
}
```

<img alt="js-mistakes example 16 source" src="../code_sandbox/snaps/js-mistakes-16-code.png" />

<img alt="js-mistakes example 16 result" src="../code_sandbox/snaps/js-mistakes-16-result.png" />

- [x] **Outcome:** **myFunction(2)** is **20**.

<a id="js-mistakes-example-17"></a>

### **Example 17: return a * power with semicolons — same result**

- [x] Explicit semicolons: same **20**.

Sandbox: `code_sandbox/js-mistakes/return-with-semicolons.html`

```javascript
function myFunction(a) {
  let power = 10;
  return a * power;
}
```

<img alt="js-mistakes example 17 source" src="../code_sandbox/snaps/js-mistakes-17-code.png" />

<img alt="js-mistakes example 17 result" src="../code_sandbox/snaps/js-mistakes-17-result.png" />

- [x] **Outcome:** **myFunction(2)** is **20**.

<a id="js-mistakes-example-18"></a>

### **Example 18: You may break after `return a *` onto the next line**

- [x] `return a *` is an **incomplete** statement, so ASI waits for **`power`**.

Sandbox: `code_sandbox/js-mistakes/return-break-after-star.html`

```javascript
function myFunction(a) {
  let power = 10;
  return a *
  power;
}
```

<img alt="js-mistakes example 18 source" src="../code_sandbox/snaps/js-mistakes-18-code.png" />

<img alt="js-mistakes example 18 result" src="../code_sandbox/snaps/js-mistakes-18-result.png" />

- [x] **Outcome:** **myFunction(2)** is still **20**.

<a id="js-mistakes-example-19"></a>

### **Example 19: Never break after return — it becomes return;**

- [x] `return` on its own line is a **complete** statement. ASI inserts **`return;`**.
- [x] The next line `a * power` is **dead code**. The function returns **`undefined`**.

Sandbox: `code_sandbox/js-mistakes/return-newline.html`

```javascript
function myFunction(a) {
  let power = 10;
  return
  a * power;
}
```

<img alt="js-mistakes example 19 source" src="../code_sandbox/snaps/js-mistakes-19-code.png" />

<img alt="js-mistakes example 19 result" src="../code_sandbox/snaps/js-mistakes-19-result.png" />

- [x] **Outcome:** **myFunction(2)** is **undefined**.

<a id="js-mistakes-example-20"></a>

### **Example 20: ASI reads that as return; a * power;**

- [x] Equivalent code: `return;` then `a * power;` as a useless expression statement.
- [x] **Never break a return statement.**

Sandbox: `code_sandbox/js-mistakes/return-semicolon-explained.html`

```javascript
function myFunction(a) {
  let power = 10;
  return;
  a * power;
}
```

<img alt="js-mistakes example 20 source" src="../code_sandbox/snaps/js-mistakes-20-code.png" />

<img alt="js-mistakes example 20 result" src="../code_sandbox/snaps/js-mistakes-20-result.png" />

- [x] **Outcome:** Same as the broken line-break: **undefined**.

<a id="js-mistakes-example-21"></a>

### **Example 21: Arrays use numbered indexes — length 3, person[0] is John**

- [x] JS arrays are **not** associative. Use **numbers**.

Sandbox: `code_sandbox/js-mistakes/array-numbered-indexes.html`

```javascript
const person = [];
person[0] = "John";
person[1] = "Doe";
person[2] = 46;
```

<img alt="js-mistakes example 21 source" src="../code_sandbox/snaps/js-mistakes-21-code.png" />

<img alt="js-mistakes example 21 result" src="../code_sandbox/snaps/js-mistakes-21-result.png" />

- [x] **Outcome:** **length** is **3**. **person[0]** is **John**.

<a id="js-mistakes-example-22"></a>

### **Example 22: person["firstName"] turns the array into a plain object**

- [x] Named indexes **do not** make an associative array. The value becomes a **normal object**.
- [x] **`length`** is **0**. **`person[0]`** is **undefined**. Array methods break.

Sandbox: `code_sandbox/js-mistakes/array-named-indexes.html`

```javascript
const person = [];
person["firstName"] = "John";
person["lastName"] = "Doe";
person["age"] = 46;
```

<img alt="js-mistakes example 22 source" src="../code_sandbox/snaps/js-mistakes-22-code.png" />

<img alt="js-mistakes example 22 result" src="../code_sandbox/snaps/js-mistakes-22-result.png" />

- [x] **Outcome:** **length** is **0**. **person[0]** is **undefined**. **person.firstName** is **John**.

<a id="js-mistakes-example-23"></a>

### **Example 23: Trailing commas in objects/arrays are legal in ES5**

- [x] `{age:46,}` and `[10,]` are **legal** in modern JavaScript.
- [x] The page **warns**: IE8 could crash. **JSON does not allow** trailing commas.

Sandbox: `code_sandbox/js-mistakes/trailing-comma-js.html`

```javascript
person = {firstName:"John", lastName:"Doe", age:46,};
points = [40, 100, 1, 5, 25, 10,];
```

<img alt="js-mistakes example 23 source" src="../code_sandbox/snaps/js-mistakes-23-code.png" />

<img alt="js-mistakes example 23 result" src="../code_sandbox/snaps/js-mistakes-23-result.png" />

- [x] **Outcome:** JS accepts both. **person.age** is **46**. **points.length** is **6**.

<a id="js-mistakes-example-24"></a>

### **Example 24: JSON.parse rejects trailing commas**

- [x] JSON must **not** have a trailing comma.

Sandbox: `code_sandbox/js-mistakes/trailing-comma-json.html`

```javascript
JSON.parse('{"firstName":"John","age":46,}')
```

<img alt="js-mistakes example 24 source" src="../code_sandbox/snaps/js-mistakes-24-code.png" />

<img alt="js-mistakes example 24 result" src="../code_sandbox/snaps/js-mistakes-24-result.png" />

- [x] **Outcome:** **SyntaxError: Expected double-quoted property name** (or unexpected token) — JSON parse fails.

<a id="js-mistakes-example-25"></a>

### **Example 25: if (typeof myObj === "undefined") is safe**

- [x] **`typeof`** of a missing binding is **`"undefined"`** and does **not throw**.

Sandbox: `code_sandbox/js-mistakes/typeof-undefined.html`

```javascript
if (typeof myObj === "undefined") { /* missing */ }
```

<img alt="js-mistakes example 25 source" src="../code_sandbox/snaps/js-mistakes-25-code.png" />

<img alt="js-mistakes example 25 result" src="../code_sandbox/snaps/js-mistakes-25-result.png" />

- [x] **Outcome:** **typeof myObj** is **"undefined"**. The `if` is **true**.

<a id="js-mistakes-example-26"></a>

### **Example 26: Test typeof !== undefined before !== null**

- [x] `if (myObj === null)` **throws ReferenceError** if `myObj` was never declared.
- [x] `if (myObj !== null && typeof myObj !== "undefined")` still **throws** — it **reads `myObj` first**.
- [x] **Correct:** `typeof myObj !== "undefined" && myObj !== null`.

Sandbox: `code_sandbox/js-mistakes/null-check-order.html`

```javascript
if (typeof myObj !== "undefined" && myObj !== null) { /* ok */ }
```

<img alt="js-mistakes example 26 source" src="../code_sandbox/snaps/js-mistakes-26-code.png" />

<img alt="js-mistakes example 26 result" src="../code_sandbox/snaps/js-mistakes-26-result.png" />

- [x] **Outcome:** Correct order: **false** (undeclared), **no throw**. Reversed `myObj !== null` first is **ReferenceError: myObj is not defined**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-mistakes/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: `if (x = 10)` when x started 0?

<details>
<summary>Answer</summary>

- [x] **true**. **x** becomes **10**. Block runs.

</details>

### Question 2: `if (x = 0)`?

<details>
<summary>Answer</summary>

- [x] **false** (0 is falsy). Block skipped.

</details>

### Question 3: `10 == "10"` vs `10 === "10"`?

<details>
<summary>Answer</summary>

- [x] **true** vs **false**.

</details>

### Question 4: `switch(10) { case "10": }`?

<details>
<summary>Answer</summary>

- [x] **No match** (strict).

</details>

### Question 5: `10 + 5` vs `10 += "5"`?

<details>
<summary>Answer</summary>

- [x] **15** vs **`"105"`**.

</details>

### Question 6: `0.1 + 0.2 === 0.3`?

<details>
<summary>Answer</summary>

- [x] **false**.

</details>

### Question 7: `(0.1*10 + 0.2*10)/10 === 0.3`?

<details>
<summary>Answer</summary>

- [x] **true**.

</details>

### Question 8: `if (x==19); { ran = true }` with x=0?

<details>
<summary>Answer</summary>

- [x] The block **still runs**. The `;` emptied the if.

</details>

### Question 9: `return` then newline then `a * power`?

<details>
<summary>Answer</summary>

- [x] Returns **undefined** (ASI inserted `return;`).

</details>

### Question 10: `person["firstName"] = "John"` on `[]`?

<details>
<summary>Answer</summary>

- [x] **length 0**, **person[0]** undefined, **person.firstName** John.

</details>

### Question 11: `JSON.parse` with a trailing comma?

<details>
<summary>Answer</summary>

- [x] **SyntaxError**.

</details>

### Question 12: Safe undeclared null check?

<details>
<summary>Answer</summary>

- [x] `typeof myObj !== "undefined" && myObj !== null`.

</details>


</details>

## Summary

Compare with ===, never assign inside if, remember switch is strict, watch +, fix floats by scaling, do not break strings or return, do not name-index arrays, and typeof before null.

## References

- [JS Mistakes (W3Schools)](https://www.w3schools.com/js/js_mistakes.asp)
- [MDN: Automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
- [MDN: switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
- [ECMA-262: Number values](https://tc39.es/ecma262/#sec-ecmascript-language-types-number-type)
