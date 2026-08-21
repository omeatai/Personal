# HTML vs. XHTML

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

**XHTML** is a **stricter, XML-based** version of HTML. This chapter defines XHTML, why it exists (well-formed markup and stricter error handling), and the rules that differ from HTML: a mandatory XHTML doctype and `xmlns`, required document elements, proper nesting, closed tags (including empty elements), lowercase names, quoted attributes, and **no attribute minimization**.

This section has **4** examples:

- [x] **Example 1:** Minimum document [View](#html-vs-xhtml-example-01)
- [x] **Example 2:** Nested and closed [View](#html-vs-xhtml-example-02)
- [x] **Example 3:** Empty elements [View](#html-vs-xhtml-example-03)
- [x] **Example 4:** Attributes [View](#html-vs-xhtml-example-04)

## Detailed Explanation

- [x] **What is XHTML?**
  - **X**HTML = **EX**tensible **H**yper**T**ext **M**arkup **L**anguage.
  - A **stricter**, more **XML-based** version of HTML.
  - HTML defined as an **XML application**.
  - Supported by all major browsers.
- [x] **Why XHTML?**
  - XML documents must be **well-formed**.
  - XHTML makes HTML more **extensible** and easier to mix with other data formats (such as XML).
  - Browsers **ignore many HTML errors** and still try to display the page. XHTML uses **much stricter error handling**.
- [x] **Most important differences from HTML**
  - `<!DOCTYPE>` is **mandatory**.
  - The **`xmlns`** attribute on `<html>` is **mandatory**.
  - `<html>`, `<head>`, `<title>`, and `<body>` are **mandatory**.
  - Elements must always be **properly nested**.
  - Elements must always be **closed**.
  - Elements must always be in **lowercase**.
  - Attribute names must always be in **lowercase**.
  - Attribute values must always be **quoted**.
  - Attribute **minimization is forbidden**.
- [x] **Minimum XHTML document**
  - Use an **XHTML 1.1** doctype and `xmlns="http://www.w3.org/1999/xhtml"` on `<html>`.
  - Sandbox: `code_sandbox/html-xhtml/index.html`.
  - The page shows **some content here...** (tab title: **Title of document**).
  - Served here as `text/html` so Chrome still displays it. True XHTML is `application/xhtml+xml` and **stops on well-formedness errors**.

<img alt="html-xhtml result" src="../code_sandbox/snaps/html-xhtml-result.png" />
- [x] **Validate**
  - The chapter links a **W3C Markup Validation Service** box for checking a URL.

<a id="html-vs-xhtml-example-01"></a>

### **Example 1: Minimum document**

- [x] This example runs the tested markup in `code_sandbox/html-vs-xhtml/index.html`.

Sandbox: `code_sandbox/html-vs-xhtml/index.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Title of document</title>
  </head>
  <body>
    some content here...
  </body>
</html>
```

<img alt="html-xhtml source" src="../code_sandbox/snaps/html-xhtml-code.png" />

<img alt="html-xhtml result" src="../code_sandbox/snaps/html-xhtml-result.png" />

- [x] **Outcome:** the browser shows **Title of document some content here...**.

<a id="html-vs-xhtml-example-02"></a>

### **Example 2: Nested and closed**

- [x] **Proper nesting and closed elements**
  - Correct: `<b><i>Some text</i></b>`. Wrong: `<b><i>Some text</b></i>`.
  - Every `<p>` needs `</p>`. Unclosed paragraphs are invalid XHTML.
  - Sandbox: `nested.html`.

Sandbox: `code_sandbox/html-vs-xhtml/nested.html`

```html
<b><i>Some text</i></b>
<p>This is a paragraph</p>
<p>This is another paragraph</p>
```

<img alt="html-xhtml nested source" src="../code_sandbox/snaps/html-xhtml-01-code.png" />

<img alt="html-xhtml nested result" src="../code_sandbox/snaps/html-xhtml-01-result.png" />

- [x] **Outcome:** the browser shows **Some text This is a paragraph**, **This is another paragraph**.

<a id="html-vs-xhtml-example-03"></a>

### **Example 3: Empty elements**

- [x] **Empty elements must be closed**
  - Sandbox: `empty.html`.

Sandbox: `code_sandbox/html-vs-xhtml/empty.html`

```html
A break: <br />
A horizontal rule:
<hr />
An image: <img src="happy.gif" alt="Happy face" />
```

<img alt="html-xhtml empty source" src="../code_sandbox/snaps/html-xhtml-02-code.png" />

<img alt="html-xhtml empty result" src="../code_sandbox/snaps/html-xhtml-02-result.png" />

- [x] **Outcome:** the browser shows **A break: A horizontal rule: An image:**.

<a id="html-vs-xhtml-example-04"></a>

### **Example 4: Attributes**

- [x] **Lowercase names, quoted values, no minimization**
  - Use `<body>` / `<p>` / `href`, not `<BODY>` / `<P>` / `HREF`.
  - Quote values: `href="https://www.w3schools.com/html/"` — not `href=https://www.w3schools.com/html/`.
  - Write `checked="checked"` and `disabled="disabled"`, not bare `checked` / `disabled`.
  - Sandbox: `attributes.html`.

Sandbox: `code_sandbox/html-vs-xhtml/attributes.html`

```html
<a href="https://www.w3schools.com/html/">Visit our HTML tutorial</a>
<input type="checkbox" name="vehicle" value="car" checked="checked" />
<input type="text" name="lastname" disabled="disabled" />
```

<img alt="html-xhtml attributes source" src="../code_sandbox/snaps/html-xhtml-03-code.png" />

<img alt="html-xhtml attributes result" src="../code_sandbox/snaps/html-xhtml-03-result.png" />

- [x] **Outcome:** the browser shows **Visit our HTML tutorial**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-xhtml/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does XHTML stand for?

<details>
<summary>Answer</summary>

- [x] **EXtensible HyperText Markup Language**.
- [x] A stricter, more **XML-based** version of HTML.

</details>

### Question 2: How is XHTML related to XML?

<details>
<summary>Answer</summary>

- [x] XHTML is HTML defined as an **XML application**.
- [x] XML documents must be **well-formed**.

</details>

### Question 3: Why was XHTML developed?

<details>
<summary>Answer</summary>

- [x] To make HTML more **extensible** and flexible with other formats (such as XML).
- [x] HTML browsers often **ignore errors**; XHTML uses **stricter error handling**.

</details>

### Question 4: Which doctype and namespace does the minimum example use?

<details>
<summary>Answer</summary>

- [x] XHTML **1.1** doctype: `-//W3C//DTD XHTML 1.1//EN`.
- [x] `xmlns="http://www.w3.org/1999/xhtml"` on `<html>`.

</details>

### Question 5: Which elements are mandatory in XHTML?

<details>
<summary>Answer</summary>

- [x] `<!DOCTYPE>`, `<html>` with **`xmlns`**, `<head>`, `<title>`, and `<body>`.

</details>

### Question 6: What is wrong with `<b><i>Some text</b></i>`?

<details>
<summary>Answer</summary>

- [x] The tags **cross**; they are not properly nested.
- [x] Correct: `<b><i>Some text</i></b>`.

</details>

### Question 7: How must empty elements be written?

<details>
<summary>Answer</summary>

- [x] They must be **closed**: `<br />`, `<hr />`, `<img ... />`.
- [x] Bare `<br>` / `<hr>` / `<img>` is wrong in XHTML.

</details>

### Question 8: Must element and attribute names be lowercase?

<details>
<summary>Answer</summary>

- [x] **Yes.** `<BODY>` and `HREF` are invalid XHTML.
- [x] Use `<body>` and `href`.

</details>

### Question 9: Must attribute values be quoted?

<details>
<summary>Answer</summary>

- [x] **Yes.** `href="https://www.w3schools.com/html/"` is correct.
- [x] Unquoted `href=https://www.w3schools.com/html/` is wrong.

</details>

### Question 10: What is attribute minimization, and is it allowed?

<details>
<summary>Answer</summary>

- [x] Writing `checked` or `disabled` with **no value**.
- [x] **Forbidden** in XHTML: use `checked="checked"` and `disabled="disabled"`.

</details>

</details>

## Summary

XHTML is HTML as XML: well-formed, lowercase, fully nested and closed (including `<br />`), with quoted attributes and no minimization. A valid document needs the XHTML doctype, `xmlns` on `<html>`, plus `<head>`, `<title>`, and `<body>`. Browsers forgive HTML errors; XHTML does not.

## References

- [HTML Versus XHTML (W3Schools)](https://www.w3schools.com/html/html_xhtml.asp)
- [XML Tutorial (W3Schools)](https://www.w3schools.com/xml/default.asp)
- [W3C Markup Validation Service](https://validator.w3.org/)
- [MDN: XHTML](https://developer.mozilla.org/en-US/docs/Glossary/XHTML)
- [XHTML 1.1 (W3C)](https://www.w3.org/TR/xhtml11/)
