# HTML Lists

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

HTML lists group related items. This chapter covers **unordered** lists (`<ul>`), **ordered** lists (`<ol>`), and **description** lists (`<dl>` / `<dt>` / `<dd>`). Nested sidebar pages cover unordered, ordered, and other lists in more detail.

This section has **3** examples:

- [x] **Example 1:** Unordered [View](#html-lists-example-01)
- [x] **Example 2:** Ordered [View](#html-lists-example-02)
- [x] **Example 3:** Description [View](#html-lists-example-03)

## Detailed Explanation

<a id="html-lists-example-01"></a>

### **Example 1: Unordered**

- [x] **Unordered list**
  - Starts with `<ul>`. Each item is `<li>`.
  - Default marker: **bullets** (small black circles).
  - Example: Coffee, Tea, Milk.

Sandbox: `code_sandbox/html-lists/index.html`

```html
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```

<img alt="html-lists unordered source" src="../code_sandbox/snaps/html-lists-code.png" />

<img alt="html-lists unordered result" src="../code_sandbox/snaps/html-lists-result.png" />

- [x] **Outcome:** the browser shows **Coffee**, **Tea**, **Milk**.

<a id="html-lists-example-02"></a>

### **Example 2: Ordered**

- [x] **Ordered list**
  - Starts with `<ol>`. Each item is `<li>`.
  - Default marker: **numbers**.
  - Same three drinks, numbered.
  - Sandbox: `ordered.html`.

Sandbox: `code_sandbox/html-lists/ordered.html`

```html
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```

<img alt="html-lists ordered source" src="../code_sandbox/snaps/html-lists-01-code.png" />

<img alt="html-lists ordered result" src="../code_sandbox/snaps/html-lists-01-result.png" />

- [x] **Outcome:** the browser shows **Coffee**, **Tea**, **Milk**.

<a id="html-lists-example-03"></a>

### **Example 3: Description**

- [x] **Description list**
  - A list of **terms** with a **description** of each.
  - `<dl>` — the list. `<dt>` — the term. `<dd>` — the description.
  - Example: Coffee — black hot drink; Milk — white cold drink.
  - Sandbox: `description.html`.
    | Tag | Description |
    | ------ | ---------------------------------------- |
    | `<ul>` | Defines an unordered list |
    | `<ol>` | Defines an ordered list |
    | `<li>` | Defines a list item |
    | `<dl>` | Defines a description list |
    | `<dt>` | Defines a term in a description list |
    | `<dd>` | Describes the term in a description list |

Sandbox: `code_sandbox/html-lists/description.html`

```html
<dl>
  <dt>Coffee</dt>
  <dd>- black hot drink</dd>
  <dt>Milk</dt>
  <dd>- white cold drink</dd>
</dl>
```

<img alt="html-lists description source" src="../code_sandbox/snaps/html-lists-02-code.png" />

<img alt="html-lists description result" src="../code_sandbox/snaps/html-lists-02-result.png" />

- [x] **Outcome:** the browser shows **Coffee - black hot drink Milk - white cold drink**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-lists/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Which tags make an unordered list, and what is the default marker?

<details>
<summary>Answer</summary>

- [x] `<ul>` with `<li>` items.
- [x] Default marker: **bullets** (small black circles).

</details>

### Question 2: Which tags make an ordered list, and what is the default marker?

<details>
<summary>Answer</summary>

- [x] `<ol>` with `<li>` items.
- [x] Default marker: **numbers**.

</details>

### Question 3: Which three tags make a description list?

<details>
<summary>Answer</summary>

- [x] `<dl>` — the list.
- [x] `<dt>` — the term.
- [x] `<dd>` — the description.

</details>

### Question 4: What is a description list for?

<details>
<summary>Answer</summary>

- [x] A list of **terms**, each with a **description**.

</details>

### Question 5: Which tag is a list item in both unordered and ordered lists?

<details>
<summary>Answer</summary>

- [x] **`<li>`**.

</details>

### Question 6: Where does this chapter send you for more list detail?

<details>
<summary>Answer</summary>

- [x] **Unordered Lists**, **Ordered Lists**, and **Other Lists**.

</details>

</details>

## Summary

Use `<ul>` for bullets, `<ol>` for numbers, and `<li>` for items in both. Use `<dl>`, `<dt>`, and `<dd>` for terms and their descriptions.

## References

- [HTML Lists (W3Schools)](https://www.w3schools.com/html/html_lists.asp)
- [Try it Yourself: tryhtml_lists_unordered](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_lists_unordered)
- [Try it Yourself: tryhtml_lists_ordered](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_lists_ordered)
- [Try it Yourself: tryhtml_lists_description](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_lists_description)
- [Unordered Lists](https://www.w3schools.com/html/html_lists_unordered.asp)
- [Ordered Lists](https://www.w3schools.com/html/html_lists_ordered.asp)
- [Other Lists](https://www.w3schools.com/html/html_lists_other.asp)
- [MDN: `<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
- [MDN: `<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)
- [MDN: `<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
