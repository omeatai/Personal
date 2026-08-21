# JS If Conditions

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The **`if`** statement runs a block when a condition is **true**. Write **`if` in lowercase** — `If` or `IF` is a JavaScript **error**. This page walks a greeting, two driving ages, a **nested** country/age check, and the same check flattened with **`&&`**.

This section has **5** examples:

- [x] **Example 1:** `if` hour < 18 greeting [View](#js-if-conditions-example-01)
- [x] **Example 2:** Age 18 can drive [View](#js-if-conditions-example-02)
- [x] **Example 3:** Age 16 cannot drive [View](#js-if-conditions-example-03)
- [x] **Example 4:** Nested `if` (USA, age 16) [View](#js-if-conditions-example-04)
- [x] **Example 5:** Logical AND instead of nested `if` [View](#js-if-conditions-example-05)

## Detailed Explanation

- [x] **`if` must be lowercase** — `If` / `IF` are not the keyword and throw an error.
- [x] **Default then overwrite** — start with a fallback string; the `if` block replaces it only when the test is true.
- [x] **Nested `if` works** but gets busy; **`country == "USA" && age >= 16`** is the usual replacement.

<a id="js-if-conditions-example-01"></a>

### **Example 1: `if` hour < 18 greeting**

- [x] Write **`if` in lowercase**. **`If`** or **`IF`** is a JavaScript **error** (it is not the `if` keyword).
- [x] Syntax: `if (condition) { // code if true }`.
- [x] Pin **`hour = 10`**. **10 < 18** is true, so `greeting` becomes **Good day**.
- [x] The live Tryit often uses `new Date().getHours()`. Pinning the hour keeps the snap deterministic.

Sandbox: `code_sandbox/js-if-conditions/if-hour.html`

```javascript
let hour = 10;
let greeting;
if (hour < 18) {
  greeting = "Good day";
}
```

![js-if-conditions example 1 source](../code_sandbox/snaps/js-if-conditions-01-code.png)

![js-if-conditions example 1 result](../code_sandbox/snaps/js-if-conditions-01-result.png)

- [x] **Outcome:** **hour = 10** makes `hour < 18` **true**, so greeting is **Good day**.

<a id="js-if-conditions-example-02"></a>

### **Example 2: Age 18 can drive**

- [x] Start with a **default** string, then **overwrite** it inside `if` when the test is true.
- [x] `let text = "You can Not drive"` then `if (age >= 18) { text = "You can drive"; }`.
- [x] Pin **`age = 18`**. **18 >= 18** is true, so the block runs.

Sandbox: `code_sandbox/js-if-conditions/age-18-drive.html`

```javascript
let age = 18;
let text = "You can Not drive";
if (age >= 18) {
  text = "You can drive";
}
```

![js-if-conditions example 2 source](../code_sandbox/snaps/js-if-conditions-02-code.png)

![js-if-conditions example 2 result](../code_sandbox/snaps/js-if-conditions-02-result.png)

- [x] **Outcome:** With **age = 18**, the `if` runs and text is **You can drive**.

<a id="js-if-conditions-example-03"></a>

### **Example 3: Age 16 cannot drive**

- [x] Same code as the previous Example, but **`age = 16`**.
- [x] **16 >= 18** is **false**, so the `if` block is **skipped**.
- [x] The default **You can Not drive** stays. (W3Schools capitalizes **Not** that way.)

Sandbox: `code_sandbox/js-if-conditions/age-16-no-drive.html`

```javascript
let age = 16;
let text = "You can Not drive";
if (age >= 18) {
  text = "You can drive";
}
```

![js-if-conditions example 3 source](../code_sandbox/snaps/js-if-conditions-03-code.png)

![js-if-conditions example 3 result](../code_sandbox/snaps/js-if-conditions-03-result.png)

- [x] **Outcome:** With **age = 16**, the `if` does not run, so text stays **You can Not drive**.

<a id="js-if-conditions-example-04"></a>

### **Example 4: Nested `if` (USA, age 16)**

- [x] You can put an **`if` inside another `if`**. The inner test runs only if the outer test is true.
- [x] Here: outer checks **`country == "USA"`**, inner checks **`age >= 16`**.
- [x] With **country = USA** and **age = 16**, both tests pass, so text becomes **You can drive!**.
- [x] Nested `if` works, but it can make code **harder to read**. The next Example flattens this with **`&&`**.

Sandbox: `code_sandbox/js-if-conditions/nested-if.html`

```javascript
let age = 16;
let country = "USA";
let text = "You can Not drive!";
if (country == "USA") {
  if (age >= 16) {
    text = "You can drive!";
  }
}
```

![js-if-conditions example 4 source](../code_sandbox/snaps/js-if-conditions-04-code.png)

![js-if-conditions example 4 result](../code_sandbox/snaps/js-if-conditions-04-result.png)

- [x] **Outcome:** **USA** and **age 16** both pass, so nested `if` sets text to **You can drive!**.

<a id="js-if-conditions-example-05"></a>

### **Example 5: Logical AND instead of nested `if`**

- [x] A **better** (flatter) form of the nested test: `if (country == "USA" && age >= 16)`.
- [x] **`&&`** is true only when **both** sides are true. If country is not USA, `age` is not even required for the combined condition to fail.
- [x] Same inputs (**USA**, **16**) produce the same result: **You can drive!**.
- [x] Prefer **`&&`** for two required checks unless you truly need different inner/outer side effects.

Sandbox: `code_sandbox/js-if-conditions/logical-and.html`

```javascript
let age = 16;
let country = "USA";
let text = "You can Not drive!";
if (country == "USA" && age >= 16) {
  text = "You can drive!";
}
```

![js-if-conditions example 5 source](../code_sandbox/snaps/js-if-conditions-05-code.png)

![js-if-conditions example 5 result](../code_sandbox/snaps/js-if-conditions-05-result.png)

- [x] **Outcome:** **`&&`** is true for **USA** and **age 16**, so text is **You can drive!** — same outcome as the nested `if`, with one condition.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-if-conditions/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Must `if` be written in lowercase?

<details>
<summary>Answer</summary>

- [x] **Yes.** `If` or `IF` is **not** the `if` keyword and causes a JavaScript **error**.

</details>

### Question 2: With `hour = 10`, what is `greeting` after `if (hour < 18)`?

<details>
<summary>Answer</summary>

- [x] **Good day**.
- [x] `10 < 18` is **true**.

</details>

### Question 3: With `age = 18`, what is `text` after the driving `if`?

<details>
<summary>Answer</summary>

- [x] **You can drive**.
- [x] The default **You can Not drive** is overwritten because `18 >= 18`.

</details>

### Question 4: With `age = 16`, what is `text` after the same driving `if`?

<details>
<summary>Answer</summary>

- [x] **You can Not drive**.
- [x] `16 >= 18` is **false**, so the block is skipped.

</details>

### Question 5: What is the starting value of `text` before those driving `if`s run?

<details>
<summary>Answer</summary>

- [x] **You can Not drive** (no exclamation on the simple age examples).
- [x] The nested / `&&` examples start with **You can Not drive!**.

</details>

### Question 6: Nested `if` with `country = "USA"` and `age = 16`: what is `text`?

<details>
<summary>Answer</summary>

- [x] **You can drive!**.
- [x] The outer country test is true, then the inner age test is true.

</details>

### Question 7: How do you write that nested check as one condition?

<details>
<summary>Answer</summary>

- [x] `if (country == "USA" && age >= 16)`
- [x] The sandbox result is still **You can drive!**.

</details>

### Question 8: If `country` were not `"USA"`, would the nested inner `if` run?

<details>
<summary>Answer</summary>

- [x] **No.** The inner `if` only runs when the **outer** condition is true.
- [x] With `&&`, the whole condition is false if country is wrong.

</details>

### Question 9: Does `if` without `else` leave the default string in place when the test is false?

<details>
<summary>Answer</summary>

- [x] **Yes.** That is why age 16 still reads **You can Not drive**.

</details>

### Question 10: Why prefer `&&` over nested `if` for two required checks?

<details>
<summary>Answer</summary>

- [x] Nested `if` can make the code **more complex**.
- [x] One combined condition is easier to read when both tests must pass.

</details>

</details>

## Summary

`if` (lowercase only) runs a block when a condition is true. **hour 10** → **Good day**. **age 18** → **You can drive**; **age 16** → **You can Not drive**. Nested **USA / age 16** and **`&&`** both yield **You can drive!**. `else` / `else if` are covered in the surrounding conditional chapters.

## References

- [JS If Conditions (W3Schools)](https://www.w3schools.com/js/js_if.asp)
- [MDN: if...else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
- [MDN: Logical AND (&&)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND)
