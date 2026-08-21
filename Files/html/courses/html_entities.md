# HTML Entities

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

Reserved characters in HTML must be replaced with **character entities**. This chapter covers entity **names** (`&lt;`) and **numbers** (`&#60;`), the **non-breaking space**, a table of useful entities, and **combining diacritical marks**.

This section has **1** example:

- [x] **Example 1:** Main document [View](#html-entities-example-01)

## Detailed Explanation

- [x] **Reserved characters**
  - `<` (less than) and `>` (greater than) can be mixed up with tags if you type them as text.
  - Replace them: `<` → `&lt;` or `&#60;`; `>` → `&gt;`.
- [x] **Two forms**
  - Name: `&entity_name;`
  - Number: `&#entity_number;`
  - Names are easier to remember. **Entity names are case sensitive.**
- [x] **Non-breaking space (`&nbsp;` / `&#160;`)**
  - A space that will **not** wrap to a new line (handy for `§ 10`, `10 km/h`, `10 PM`).
  - Browsers collapse extra spaces: ten typed spaces become one. Use `&nbsp;` for extra spaces.
  - Non-breaking hyphen: `&#8209;` (`‑`).
- [x] **Useful entities** (name / number)
  - `&lt;` / `&#60;` — less than
  - `&gt;` / `&#62;` — greater than
  - `&amp;` / `&#38;` — ampersand
  - `&quot;` / `&#34;` — double quote
  - `&apos;` / `&#39;` — single quote
  - `&copy;` / `&#169;` — copyright
  - Also: `&cent;` `&pound;` `&yen;` `&euro;` `&reg;` `&trade;`
- [x] **Combining diacritical marks**
  - A glyph added to a letter (grave `` ` ``, acute ´). Combine with a letter: `a&#768;` → à, `a&#769;` → á, `a&#770;` → â, `a&#771;` → ã (same for `O`).

<a id="html-entities-example-01"></a>

### **Example 1: Main document**

- [x] This example runs the tested markup in `code_sandbox/html-entities/index.html`.

Sandbox: `code_sandbox/html-entities/index.html`

```html
<p>Less than: &lt;</p>
<p>Greater than: &gt;</p>
<p>Ampersand: &amp;</p>
<p>Copyright: &copy; W3Schools.com</p>
<p>10&nbsp;km/h &nbsp; 10&nbsp;PM</p>
<p>a grave: a&#768; &nbsp; a acute: a&#769;</p>
```

<img alt="html-entities source" src="../code_sandbox/snaps/html-entities-code.png" />

<img alt="html-entities result" src="../code_sandbox/snaps/html-entities-result.png" />

- [x] **Outcome:** the browser shows **Less than: &lt;**, **Greater than: &gt;**, **Ampersand: &amp;**, **Copyright: &copy; W3Schools.com**, **10&nbsp;km/h &nbsp; 10&nbsp;PM**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-entities/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you write a less-than sign as text?

<details>
<summary>Answer</summary>

- [x] `&lt;` or `&#60;`.

</details>

### Question 2: What is the difference between `&entity_name;` and `&#entity_number;`?

<details>
<summary>Answer</summary>

- [x] Names are easier to remember.
- [x] Numbers always work; names are **case sensitive**.

</details>

### Question 3: What does `&nbsp;` do?

<details>
<summary>Answer</summary>

- [x] A space that will **not** break onto a new line.
- [x] Also keeps extra spaces the browser would otherwise collapse.

</details>

### Question 4: What is the entity for ampersand?

<details>
<summary>Answer</summary>

- [x] `&amp;` or `&#38;`.

</details>

### Question 5: How do you combine a grave accent with the letter a?

<details>
<summary>Answer</summary>

- [x] `a&#768;` → à.

</details>

### Question 6: Are entity names case sensitive?

<details>
<summary>Answer</summary>

- [x] **Yes.**

</details>

</details>

## Summary

Use `&lt;` `&gt;` `&amp;` for reserved characters, `&nbsp;` for sticky or extra spaces, and named or numbered entities for symbols. Combining marks like `&#768;` add accents to letters.

## References

- [HTML Entities (W3Schools)](https://www.w3schools.com/html/html_entities.asp)
- [Try it Yourself: tryhtml_ent_lt](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_ent_lt)
- [Try it Yourself: tryhtml_ent_nbsp](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_ent_nbsp)
- [Try it Yourself: tryhtml_ent_copy](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_ent_copy)
- [HTML Character Sets](https://www.w3schools.com/charsets/default.asp)
- [MDN: Character references](https://developer.mozilla.org/en-US/docs/Glossary/Entity)
