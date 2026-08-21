<details>
  <summary>JS Ternary</summary>

## Introduction

The **conditional (ternary) operator** `(condition) ? a : b` is a one-line **`if…else` that returns a value**. This page uses it for **Minor / Adult** and a **member discount**. Age and membership flags are pinned.

This section has **6** examples:

- [x] **Example 1:** age < 18 ? Minor : Adult — age 16 [View](#js-ternary-example-01)
- [x] **Example 2:** age < 18 ? Minor : Adult — age 21 [View](#js-ternary-example-02)
- [x] **Example 3:** isMember true → discount 0.2 [View](#js-ternary-example-03)
- [x] **Example 4:** isMember false → discount 0 [View](#js-ternary-example-04)
- [x] **Example 5:** Ternary vs the equivalent if…else [View](#js-ternary-example-05)
- [x] **Example 6:** The three operands: condition, ?, expressions [View](#js-ternary-example-06)

## Detailed Explanation

- [x] It is called **ternary** because it takes **three** operands — the only JavaScript operator that does.
- [x] Syntax: **condition ? expression1 : expression2**. All parts in the parameter table are required.
- [x] ES1 (1997); supported in all current browsers.

<a id="js-ternary-example-01"></a>

### **Example 1: age < 18 ? Minor : Adult — age 16**

- [x] The **conditional (ternary) operator** is shorthand for `if…else` that **returns a value**.
- [x] Syntax: `(condition) ? expression1 : expression2` — **three** operands (the only JS operator that takes three).
- [x] Pin **`age = 16`**. **16 < 18** is true, so the result is **Minor**.

Sandbox: `code_sandbox/js-ternary/age-minor.html`

```javascript
let age = 16;
let text = (age < 18) ? "Minor" : "Adult";
```

<img alt="js-ternary example 1 source" src="./code_sandbox/snaps/js-ternary-01-code.png" />

<img alt="js-ternary example 1 result" src="./code_sandbox/snaps/js-ternary-01-result.png" />

- [x] **Outcome:** **age = 16** makes `age < 18` **true**, so text is **Minor**.

<a id="js-ternary-example-02"></a>

### **Example 2: age < 18 ? Minor : Adult — age 21**

- [x] Same operator as Example 1, with **`age = 21`** so you see **expression2** (the `:` side).
- [x] **21 < 18** is **false**, so the result is **Adult**.
- [x] Read it as: *if the test is true, take the value after `?`; otherwise take the value after `:`*.

Sandbox: `code_sandbox/js-ternary/age-adult.html`

```javascript
let age = 21;
let text = (age < 18) ? "Minor" : "Adult";
```

<img alt="js-ternary example 2 source" src="./code_sandbox/snaps/js-ternary-02-code.png" />

<img alt="js-ternary example 2 result" src="./code_sandbox/snaps/js-ternary-02-result.png" />

- [x] **Outcome:** **age = 21** makes `age < 18` **false**, so text is **Adult**.

<a id="js-ternary-example-03"></a>

### **Example 3: isMember true → discount 0.2**

- [x] A boolean condition works the same way: `isMember ? 0.2 : 0`.
- [x] **`isMember = true`** selects **0.2** (20% off).
- [x] You do not write `if (isMember === true)` — the value already is a boolean.

Sandbox: `code_sandbox/js-ternary/member-true.html`

```javascript
let isMember = true;
let discount = isMember ? 0.2 : 0;
```

<img alt="js-ternary example 3 source" src="./code_sandbox/snaps/js-ternary-03-code.png" />

<img alt="js-ternary example 3 result" src="./code_sandbox/snaps/js-ternary-03-result.png" />

- [x] **Outcome:** **isMember** is **true**, so discount is **0.2**.

<a id="js-ternary-example-04"></a>

### **Example 4: isMember false → discount 0**

- [x] Same expression as Example 3, with **`isMember = false`**.
- [x] The `:` branch runs and discount is **0** (no member rate).
- [x] This is the page’s second membership Tryit.

Sandbox: `code_sandbox/js-ternary/member-false.html`

```javascript
let isMember = false;
let discount = isMember ? 0.2 : 0;
```

<img alt="js-ternary example 4 source" src="./code_sandbox/snaps/js-ternary-04-code.png" />

<img alt="js-ternary example 4 result" src="./code_sandbox/snaps/js-ternary-04-result.png" />

- [x] **Outcome:** **isMember** is **false**, so discount is **0**.

<a id="js-ternary-example-05"></a>

### **Example 5: Ternary vs the equivalent if…else**

- [x] The page says the operator is a **shorthand for `if…else`**. This Example writes both forms with **age 16**.
- [x] `if (age < 18) { text = "Minor"; } else { text = "Adult"; }` assigns the same string as `(age < 18) ? "Minor" : "Adult"`.
- [x] Prefer `if` when the branches are **statements** (several lines). Prefer `? :` when you need **one value**.

Sandbox: `code_sandbox/js-ternary/same-as-if-else.html`

```javascript
let age = 16;
let textIf;
if (age < 18) {
  textIf = "Minor";
} else {
  textIf = "Adult";
}
let textTernary = (age < 18) ? "Minor" : "Adult";
```

<img alt="js-ternary example 5 source" src="./code_sandbox/snaps/js-ternary-05-code.png" />

<img alt="js-ternary example 5 result" src="./code_sandbox/snaps/js-ternary-05-result.png" />

- [x] **Outcome:** Both forms produce **Minor**, and **same** is **true**.

<a id="js-ternary-example-06"></a>

### **Example 6: The three operands: condition, ?, expressions**

- [x] **condition** — required, evaluated as true/false.
- [x] **`?`** separates the condition from the true-value; **`:`** separates the two result expressions.
- [x] **expression1** returns if the condition is true; **expression2** if false. All five pieces in the page’s parameter table are required.
- [x] This operator is an **ES1** (1997) feature and is supported in all current browsers.

Sandbox: `code_sandbox/js-ternary/syntax-parts.html`

```javascript
let condition = (10 > 9);
let expression1 = "yes";
let expression2 = "no";
let result = condition ? expression1 : expression2;
```

<img alt="js-ternary example 6 source" src="./code_sandbox/snaps/js-ternary-06-code.png" />

<img alt="js-ternary example 6 result" src="./code_sandbox/snaps/js-ternary-06-result.png" />

- [x] **Outcome:** **10 > 9** is **true**, so result is **yes** (expression1). expression2 (**no**) is not used.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-ternary/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How many operands does `? :` take?

<details>
<summary>Answer</summary>

- [x] **Three** — condition, true-value, false-value.

</details>

### Question 2: With `age = 16`, what is `(age < 18) ? "Minor" : "Adult"`?

<details>
<summary>Answer</summary>

- [x] **Minor**.

</details>

### Question 3: With `age = 21`, what is that expression?

<details>
<summary>Answer</summary>

- [x] **Adult**.

</details>

### Question 4: With `isMember = true`, what is `isMember ? 0.2 : 0`?

<details>
<summary>Answer</summary>

- [x] **0.2**.

</details>

### Question 5: With `isMember = false`, what is the discount?

<details>
<summary>Answer</summary>

- [x] **0**.

</details>

### Question 6: Is `? :` a replacement for every `if`?

<details>
<summary>Answer</summary>

- [x] **No.** Use `if` for multi-line **statements**. Use `? :` to pick **one value**.

</details>

### Question 7: What does `?` separate?

<details>
<summary>Answer</summary>

- [x] The **condition** from the **true** expression.

</details>

### Question 8: What does `:` separate?

<details>
<summary>Answer</summary>

- [x] The **true** expression from the **false** expression.

</details>

### Question 9: Do `if…else` and the ternary agree for age 16?

<details>
<summary>Answer</summary>

- [x] **Yes.** Both produce **Minor**.

</details>

### Question 10: Is this a new operator?

<details>
<summary>Answer</summary>

- [x] **No.** It is **ES1** (1997) and works in all browsers.

</details>


</details>

## Summary

Write `(condition) ? ifTrue : ifFalse`. **age 16** → **Minor**; **age 21** → **Adult**. **isMember true** → **0.2**; **false** → **0**. Same result as `if…else` when you only need a value.

## References

- [JS Ternary (W3Schools)](https://www.w3schools.com/js/js_if_ternary.asp)
- [MDN: Conditional (ternary) operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)

</details>
