# JS String Templates

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Template strings (also called **template literals**) use **backticks** `` ` ``. They allow quotes inside the string, **multiline** text, and **`${...}` interpolation** of variables and expressions. ES6; modern browsers since 2017. Each Tryit is its own Example.

This section has **6** examples:

- [x] **Example 1:** Back-tick syntax [View](#js-string-templates-example-01)
- [x] **Example 2:** Quotes inside a template [View](#js-string-templates-example-02)
- [x] **Example 3:** Multiline template [View](#js-string-templates-example-03)
- [x] **Example 4:** Variable interpolation [View](#js-string-templates-example-04)
- [x] **Example 5:** Expression substitution [View](#js-string-templates-example-05)
- [x] **Example 6:** HTML templates [View](#js-string-templates-example-06)

## Detailed Explanation

- [x] **Back-tick syntax** — ``let text = `Hello World!`;``
- [x] **Quotes and multiline** — both `'` and `"` are legal inside; newlines are kept.
- [x] **Interpolation** — `` `Welcome ${firstName}, ${lastName}!` `` and expressions such as `` `Total: ${(price * (1 + VAT)).toFixed(2)}` ``.
- [x] **HTML templates** — build markup with backticks and a loop over tags.

<a id="js-string-templates-example-01"></a>

### **Example 1: Back-tick syntax**

- [x] Template strings use **backticks** `` ` `` rather than `""` or `''`.
- [x] Also called **template literals**. ES6; modern browsers since 2017.

Sandbox: `code_sandbox/js-string-templates/backticks.html`

```javascript
let text = `Hello World!`;
```

![js-string-templates example 1 source](../code_sandbox/snaps/js-string-templates-01-code.png)

![js-string-templates example 1 result](../code_sandbox/snaps/js-string-templates-01-result.png)

- [x] **Outcome:** The template stores **Hello World!**

<a id="js-string-templates-example-02"></a>

### **Example 2: Quotes inside a template**

- [x] Templates allow **both** single and double quotes inside the string.
- [x] No escape is required for `'` or `"` when the wrapper is a backtick.

Sandbox: `code_sandbox/js-string-templates/quotes-inside.html`

```javascript
let text = `He's often called "Johnny"`;
```

![js-string-templates example 2 source](../code_sandbox/snaps/js-string-templates-02-code.png)

![js-string-templates example 2 result](../code_sandbox/snaps/js-string-templates-02-result.png)

- [x] **Outcome:** The result is **He's often called "Johnny"**.

<a id="js-string-templates-example-03"></a>

### **Example 3: Multiline template**

- [x] Newlines typed inside backticks become **real newlines** in the string.
- [x] You do not need `\n` or `+` to span lines.

Sandbox: `code_sandbox/js-string-templates/multiline.html`

```javascript
let text = `The quick
brown fox
jumps over
the lazy dog`;
```

![js-string-templates example 3 source](../code_sandbox/snaps/js-string-templates-03-code.png)

![js-string-templates example 3 result](../code_sandbox/snaps/js-string-templates-03-result.png)

- [x] **Outcome:** The four lines are kept, starting with **The quick**.

<a id="js-string-templates-example-04"></a>

### **Example 4: Variable interpolation**

- [x] Syntax: **`${...}`** inside backticks.
- [x] Variables are substituted where the placeholders sit.

Sandbox: `code_sandbox/js-string-templates/interpolation.html`

```javascript
let firstName = "John";
let lastName = "Doe";
let text = `Welcome ${firstName}, ${lastName}!`;
```

![js-string-templates example 4 source](../code_sandbox/snaps/js-string-templates-04-code.png)

![js-string-templates example 4 result](../code_sandbox/snaps/js-string-templates-04-result.png)

- [x] **Outcome:** The result is **Welcome John, Doe!**

<a id="js-string-templates-example-05"></a>

### **Example 5: Expression substitution**

- [x] `${}` can hold a full **expression**, not just a variable name.
- [x] `(price * (1 + VAT)).toFixed(2)` with **price 10** and **VAT 0.25** is **12.50**.

Sandbox: `code_sandbox/js-string-templates/expression.html`

```javascript
let price = 10;
let VAT = 0.25;
let total = `Total: ${(price * (1 + VAT)).toFixed(2)}`;
```

![js-string-templates example 5 source](../code_sandbox/snaps/js-string-templates-05-code.png)

![js-string-templates example 5 result](../code_sandbox/snaps/js-string-templates-05-result.png)

- [x] **Outcome:** The result is **Total: 12.50**.

<a id="js-string-templates-example-06"></a>

### **Example 6: HTML templates**

- [x] Templates are handy for building **markup** strings.
- [x] Start with a header, **loop** the tags into list items, then close the list.
- [x] This sandbox prints the generated HTML as text (same string W3Schools assigns with `innerHTML`).

Sandbox: `code_sandbox/js-string-templates/html-template.html`

```javascript
let header = "Template Strings";
let tags = ["template strings", "javascript", "es6"];
let html = `<h2>${header}</h2><ul>`;
for (const x of tags) {
  html += `<li>${x}</li>`;
}
html += `</ul>`;
```

![js-string-templates example 6 source](../code_sandbox/snaps/js-string-templates-06-code.png)

![js-string-templates example 6 result](../code_sandbox/snaps/js-string-templates-06-result.png)

- [x] **Outcome:** The generated markup is `<h2>Template Strings</h2><ul><li>template strings</li><li>javascript</li><li>es6</li></ul>`.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-string-templates/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What characters wrap a template string?

<details>
<summary>Answer</summary>

- [x] **Backticks** `` ` ``, not `'` or `"`.

</details>

### Question 2: What does `` `Hello World!` `` store?

<details>
<summary>Answer</summary>

- [x] **Hello World!**

</details>

### Question 3: Can a template contain both `'` and `"`?

<details>
<summary>Answer</summary>

- [x] **Yes.** Example: **He's often called "Johnny"**.

</details>

### Question 4: Do multiline templates keep the line breaks?

<details>
<summary>Answer</summary>

- [x] **Yes.** You do not need `\n` or `+`.

</details>

### Question 5: How do you insert a variable?

<details>
<summary>Answer</summary>

- [x] **`${variable}`** inside the backticks.

</details>

### Question 6: What does `` `Welcome ${firstName}, ${lastName}!` `` print for John / Doe?

<details>
<summary>Answer</summary>

- [x] **Welcome John, Doe!**

</details>

### Question 7: What is `` `Total: ${(price * (1 + VAT)).toFixed(2)}` `` when price is 10 and VAT is 0.25?

<details>
<summary>Answer</summary>

- [x] **Total: 12.50**.
- [x] 10 \* 1.25 = 12.5, then `toFixed(2)` adds the cent.

</details>

### Question 8: What HTML does the tags loop produce?

<details>
<summary>Answer</summary>

- [x] **Outcome:** The generated markup is `<h2>Template Strings</h2><ul><li>template strings</li><li>javascript</li><li>es6</li></ul>`.

</details>

</details>

## Summary

Templates use backticks. They keep mixed quotes and multiline text, substitute `${variables}` and `${expressions}` (Welcome **John, Doe!**; **Total: 12.50**), and are a convenient way to build HTML strings in a loop.

## References

- [JS String Templates (W3Schools)](https://www.w3schools.com/js/js_string_templates.asp)
- [MDN: Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
