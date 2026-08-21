# HTML Formatting

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

HTML has several elements for text with a **special meaning**: bold, important, italic, emphasized, small, marked, deleted, inserted, subscript, and superscript. Some tags change **look** (`<b>`, `<i>`); others add **meaning** (`<strong>`, `<em>`).

This section has **11** examples:

- [x] **Example 1:** Formatting elements [View](#html-formatting-example-01)
- [x] **Example 2:** Bold [View](#html-formatting-example-02)
- [x] **Example 3:** Strong [View](#html-formatting-example-03)
- [x] **Example 4:** Italic [View](#html-formatting-example-04)
- [x] **Example 5:** Emphasized [View](#html-formatting-example-05)
- [x] **Example 6:** Small [View](#html-formatting-example-06)
- [x] **Example 7:** Mark [View](#html-formatting-example-07)
- [x] **Example 8:** Deleted [View](#html-formatting-example-08)
- [x] **Example 9:** Inserted [View](#html-formatting-example-09)
- [x] **Example 10:** Subscript [View](#html-formatting-example-10)
- [x] **Example 11:** Superscript [View](#html-formatting-example-11)

## Detailed Explanation

<a id="html-formatting-example-01"></a>

### **Example 1: Formatting elements**

- [x] **Formatting elements**
  - `<b>` bold (no extra importance)
  - `<strong>` important (usually bold)
  - `<i>` italic / alternate voice or mood
  - `<em>` emphasized (usually italic; screen readers stress it)
  - `<small>` smaller text
  - `<mark>` marked / highlighted
  - `<del>` deleted (usually strikethrough)
  - `<ins>` inserted (usually underlined)
  - `<sub>` subscript (e.g. H₂O)
  - `<sup>` superscript (e.g. footnotes)
  - Intro demo: bold, italic, subscript, and superscript.

Sandbox: `code_sandbox/html-formatting/index.html`

```html
<p><b>This text is bold</b></p>
<p><i>This text is italic</i></p>
<p>This is<sub> subscript</sub> and <sup>superscript</sup></p>
```

<img alt="html-formatting source" src="../code_sandbox/snaps/html-formatting-code.png" />

<img alt="html-formatting result" src="../code_sandbox/snaps/html-formatting-result.png" />

- [x] **Outcome:** the browser shows **This text is bold**, **This text is italic**, **This is subscript and superscript**.

<a id="html-formatting-example-02"></a>

### **Example 2: Bold**

- [x] **`<b>` and `<strong>`**
  - `<b>` is **bold** without extra importance.
  - `<strong>` is **strong importance**; typically displayed bold.

Sandbox: `code_sandbox/html-formatting/b.html`

```html
<b>This text is bold</b>
```

<img alt="html-formatting b source" src="../code_sandbox/snaps/html-formatting-01-code.png" />

<img alt="html-formatting b result" src="../code_sandbox/snaps/html-formatting-01-result.png" />

- [x] **Outcome:** the browser shows **This text is bold**.

<a id="html-formatting-example-03"></a>

### **Example 3: Strong**

- [x] **`<b>` and `<strong>`**
  - `<b>` is **bold** without extra importance.
  - `<strong>` is **strong importance**; typically displayed bold.

Sandbox: `code_sandbox/html-formatting/strong.html`

```html
<strong>This text is important!</strong>
```

<img alt="html-formatting strong source" src="../code_sandbox/snaps/html-formatting-02-code.png" />

<img alt="html-formatting strong result" src="../code_sandbox/snaps/html-formatting-02-result.png" />

- [x] **Outcome:** the browser shows **This text is important!**.

<a id="html-formatting-example-04"></a>

### **Example 4: Italic**

- [x] **`<i>` and `<em>`**
  - `<i>` is an **alternate voice or mood** (technical term, other language, thought, ship name); typically italic.
  - `<em>` is **emphasized**; typically italic. A screen reader stresses the words.

Sandbox: `code_sandbox/html-formatting/i.html`

```html
<i>This text is italic</i>
```

<img alt="html-formatting i source" src="../code_sandbox/snaps/html-formatting-03-code.png" />

<img alt="html-formatting i result" src="../code_sandbox/snaps/html-formatting-03-result.png" />

- [x] **Outcome:** the browser shows **This text is italic**.

<a id="html-formatting-example-05"></a>

### **Example 5: Emphasized**

- [x] **`<i>` and `<em>`**
  - `<i>` is an **alternate voice or mood** (technical term, other language, thought, ship name); typically italic.
  - `<em>` is **emphasized**; typically italic. A screen reader stresses the words.

Sandbox: `code_sandbox/html-formatting/em.html`

```html
<em>This text is emphasized</em>
```

<img alt="html-formatting em source" src="../code_sandbox/snaps/html-formatting-04-code.png" />

<img alt="html-formatting em result" src="../code_sandbox/snaps/html-formatting-04-result.png" />

- [x] **Outcome:** the browser shows **This text is emphasized**.

<a id="html-formatting-example-06"></a>

### **Example 6: Small**

- [x] **`<small>`**
  - Defines **smaller** text.

Sandbox: `code_sandbox/html-formatting/small.html`

```html
<small>This is some smaller text.</small>
```

<img alt="html-formatting small source" src="../code_sandbox/snaps/html-formatting-05-code.png" />

<img alt="html-formatting small result" src="../code_sandbox/snaps/html-formatting-05-result.png" />

- [x] **Outcome:** the browser shows **This is some smaller text.**.

<a id="html-formatting-example-07"></a>

### **Example 7: Mark**

- [x] **`<mark>`**
  - Defines text that should be **marked or highlighted**.

Sandbox: `code_sandbox/html-formatting/mark.html`

```html
<p>Do not forget to buy <mark>milk</mark> today.</p>
```

<img alt="html-formatting mark source" src="../code_sandbox/snaps/html-formatting-06-code.png" />

<img alt="html-formatting mark result" src="../code_sandbox/snaps/html-formatting-06-result.png" />

- [x] **Outcome:** the browser shows **Do not forget to buy milk today.**.

<a id="html-formatting-example-08"></a>

### **Example 8: Deleted**

- [x] **`<del>` and `<ins>`**
  - `<del>` is **deleted** text; browsers usually **strike through**.
  - `<ins>` is **inserted** text; browsers usually **underline**.

Sandbox: `code_sandbox/html-formatting/del.html`

```html
<p>My favorite color is <del>blue</del> red.</p>
```

<img alt="html-formatting del source" src="../code_sandbox/snaps/html-formatting-07-code.png" />

<img alt="html-formatting del result" src="../code_sandbox/snaps/html-formatting-07-result.png" />

- [x] **Outcome:** the browser shows **My favorite color is blue red.**.

<a id="html-formatting-example-09"></a>

### **Example 9: Inserted**

- [x] **`<del>` and `<ins>`**
  - `<del>` is **deleted** text; browsers usually **strike through**.
  - `<ins>` is **inserted** text; browsers usually **underline**.

Sandbox: `code_sandbox/html-formatting/ins.html`

```html
<p>My favorite color is <del>blue</del> <ins>red</ins>.</p>
```

<img alt="html-formatting ins source" src="../code_sandbox/snaps/html-formatting-08-code.png" />

<img alt="html-formatting ins result" src="../code_sandbox/snaps/html-formatting-08-result.png" />

- [x] **Outcome:** the browser shows **My favorite color is blue red .**.

<a id="html-formatting-example-10"></a>

### **Example 10: Subscript**

- [x] **`<sub>` and `<sup>`**
  - `<sub>` sits **half a character below** the line (chemical formulas).
  - `<sup>` sits **half a character above** the line (footnotes).

Sandbox: `code_sandbox/html-formatting/sub.html`

```html
<p>This is <sub>subscripted</sub> text.</p>
```

<img alt="html-formatting sub source" src="../code_sandbox/snaps/html-formatting-09-code.png" />

<img alt="html-formatting sub result" src="../code_sandbox/snaps/html-formatting-09-result.png" />

- [x] **Outcome:** the browser shows **This is subscripted text.**.

<a id="html-formatting-example-11"></a>

### **Example 11: Superscript**

- [x] **`<sub>` and `<sup>`**
  - `<sub>` sits **half a character below** the line (chemical formulas).
  - `<sup>` sits **half a character above** the line (footnotes).

Sandbox: `code_sandbox/html-formatting/sup.html`

```html
<p>This is <sup>superscripted</sup> text.</p>
```

<img alt="html-formatting sup source" src="../code_sandbox/snaps/html-formatting-10-code.png" />

<img alt="html-formatting sup result" src="../code_sandbox/snaps/html-formatting-10-result.png" />

- [x] **Outcome:** the browser shows **This is superscripted text.**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-formatting/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the difference between `<b>` and `<strong>`?

<details>
<summary>Answer</summary>

- [x] `<b>` is **bold** without extra importance.
- [x] `<strong>` marks **strong importance** (usually displayed bold).

</details>

### Question 2: What is the difference between `<i>` and `<em>`?

<details>
<summary>Answer</summary>

- [x] `<i>` is an **alternate voice or mood** (typically italic).
- [x] `<em>` is **emphasized** text (typically italic).
- [x] A screen reader **stresses** words in `<em>`.

</details>

### Question 3: What does `<mark>` do?

<details>
<summary>Answer</summary>

- [x] It **marks or highlights** text.
- [x] Example: “Do not forget to buy **milk** today.”

</details>

### Question 4: How do browsers usually show `<del>` and `<ins>`?

<details>
<summary>Answer</summary>

- [x] `<del>`: **strikethrough** (deleted).
- [x] `<ins>`: **underline** (inserted).

</details>

### Question 5: When do you use `<sub>` vs `<sup>`?

<details>
<summary>Answer</summary>

- [x] `<sub>`: **below** the line (chemical formulas such as H₂O).
- [x] `<sup>`: **above** the line (footnotes).

</details>

### Question 6: What does `<small>` define?

<details>
<summary>Answer</summary>

- [x] **Smaller** text.

</details>

### Question 7: Name the ten formatting elements from this chapter.

<details>
<summary>Answer</summary>

- [x] `<b>`, `<strong>`, `<i>`, `<em>`, `<small>`, `<mark>`, `<del>`, `<ins>`, `<sub>`, `<sup>`.

</details>

</details>

## Summary

Use formatting tags for **meaning** and look: `<b>`/`<strong>`, `<i>`/`<em>`, `<small>`, `<mark>`, `<del>`/`<ins>`, `<sub>`/`<sup>`. Prefer `<strong>` and `<em>` when importance or emphasis is the point.

## References

- [HTML Text Formatting (W3Schools)](https://www.w3schools.com/html/html_formatting.asp)
- [Try it Yourself: tryhtml_formatting_intro](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_intro)
- [Try it Yourself: tryhtml_formatting_b](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_b)
- [Try it Yourself: tryhtml_formatting_strong](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_strong)
- [Try it Yourself: tryhtml_formatting_i](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_i)
- [Try it Yourself: tryhtml_formatting_em](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_em)
- [Try it Yourself: tryhtml_formatting_small](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_small)
- [Try it Yourself: tryhtml_formatting_mark](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_mark)
- [Try it Yourself: tryhtml_formatting_del](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_del)
- [Try it Yourself: tryhtml_formatting_del_ins](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_del_ins)
- [Try it Yourself: tryhtml_formatting_sub](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_sub)
- [Try it Yourself: tryhtml_formatting_sup](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_sup)
- [MDN: `<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b)
- [MDN: `<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong)
- [MDN: `<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i)
- [MDN: `<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em)
- [MDN: `<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
- [MDN: `<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
- [MDN: `<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
- [MDN: `<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
- [MDN: `<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)
