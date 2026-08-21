# HTML Tables

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

HTML tables arrange data in **rows** and **columns**. A table is cells inside rows. Nested sidebar pages cover borders, sizes, headers in more depth, padding, colspan/rowspan, styling, and colgroup. This chapter is the **HTML Tables** overview.

This section has **4** examples:

- [x] **Example 1:** Company table [View](#html-tables-example-01)
- [x] **Example 2:** Cells [View](#html-tables-example-02)
- [x] **Example 3:** Rows [View](#html-tables-example-03)
- [x] **Example 4:** Headers [View](#html-tables-example-04)

## Detailed Explanation

<a id="html-tables-example-01"></a>

### **Example 1: Company table**

- [x] **Define a table**
  - `<table>` wraps the grid.
  - Example: Company / Contact / Country with Alfreds Futterkiste (Germany) and Centro comercial Moctezuma (Mexico).

Sandbox: `code_sandbox/html-tables/index.html`

```html
<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>
```

<img alt="html-tables company source" src="../code_sandbox/snaps/html-tables-code.png" />

<img alt="html-tables company result" src="../code_sandbox/snaps/html-tables-result.png" />

- [x] **Outcome:** the browser shows **Company Contact Country Alfreds Futterkiste Maria Anders Germany Centro comercial Moctezuma Francisco Chang Mexico**.

<a id="html-tables-example-02"></a>

### **Example 2: Cells**

- [x] **Table cells (`<td>`)**
  - **td** = table data. Content is between `<td>` and `</td>`.
  - A cell can hold text, images, lists, links, even other tables.
  - Example: Emil, Tobias, Linus in one row.
  - Sandbox: `cells.html`.

Sandbox: `code_sandbox/html-tables/cells.html`

```html
<table>
  <tr>
    <td>Emil</td>
    <td>Tobias</td>
    <td>Linus</td>
  </tr>
</table>
```

<img alt="html-tables cells source" src="../code_sandbox/snaps/html-tables-01-code.png" />

<img alt="html-tables cells result" src="../code_sandbox/snaps/html-tables-01-result.png" />

- [x] **Outcome:** the browser shows **Emil Tobias Linus**.

<a id="html-tables-example-03"></a>

### **Example 3: Rows**

- [x] **Table rows (`<tr>`)**
  - **tr** = table row. Starts with `<tr>`, ends with `</tr>`.
  - You can have as many rows as you like; keep the **same number of cells** in each row (uneven rows come in a later chapter).
  - Example: names row plus 16 / 14 / 10.
  - Sandbox: `rows.html`.

Sandbox: `code_sandbox/html-tables/rows.html`

```html
<table>
  <tr>
    <td>Emil</td>
    <td>Tobias</td>
    <td>Linus</td>
  </tr>
  <tr>
    <td>16</td>
    <td>14</td>
    <td>10</td>
  </tr>
</table>
```

<img alt="html-tables rows source" src="../code_sandbox/snaps/html-tables-02-code.png" />

<img alt="html-tables rows result" src="../code_sandbox/snaps/html-tables-02-result.png" />

- [x] **Outcome:** the browser shows **Emil Tobias Linus 16 14 10**.

<a id="html-tables-example-04"></a>

### **Example 4: Headers**

- [x] **Table headers (`<th>`)**
  - Use `<th>` instead of `<td>` for header cells.
  - **th** = table header. Default: **bold** and **centered** (changeable with CSS).
  - Example: Person 1 / 2 / 3, then names, then ages.
  - Sandbox: `headers.html`.
    | Tag | Description |
    | ------------ | ------------------------------------- |
    | `<table>` | Defines a table |
    | `<th>` | Defines a header cell |
    | `<tr>` | Defines a row |
    | `<td>` | Defines a cell |
    | `<caption>` | Defines a table caption |
    | `<colgroup>` | Group of columns for formatting |
    | `<col>` | Column properties inside `<colgroup>` |
    | `<thead>` | Groups header content |
    | `<tbody>` | Groups body content |
    | `<tfoot>` | Groups footer content |

Sandbox: `code_sandbox/html-tables/headers.html`

```html
<table>
  <tr>
    <th>Person 1</th>
    <th>Person 2</th>
    <th>Person 3</th>
  </tr>
  <tr>
    <td>Emil</td>
    <td>Tobias</td>
    <td>Linus</td>
  </tr>
  <tr>
    <td>16</td>
    <td>14</td>
    <td>10</td>
  </tr>
</table>
```

<img alt="html-tables headers source" src="../code_sandbox/snaps/html-tables-03-code.png" />

<img alt="html-tables headers result" src="../code_sandbox/snaps/html-tables-03-result.png" />

- [x] **Outcome:** the browser shows **Person 1 Person 2 Person 3 Emil Tobias Linus 16 14 10**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-tables/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does an HTML table consist of?

<details>
<summary>Answer</summary>

- [x] **Table cells** inside **rows** and **columns**.
- [x] Wrapped in **`<table>`**.

</details>

### Question 2: What does `<td>` stand for, and what can a cell contain?

<details>
<summary>Answer</summary>

- [x] **Table data**.
- [x] Text, images, lists, links, other tables, and more.

</details>

### Question 3: What does `<tr>` stand for, and how many cells per row?

<details>
<summary>Answer</summary>

- [x] **Table row**.
- [x] Keep the **same number of cells** in each row (exceptions later).

</details>

### Question 4: How do header cells differ from data cells?

<details>
<summary>Answer</summary>

- [x] Use **`<th>`** instead of **`<td>`**.
- [x] Default look: **bold** and **centered**.

</details>

### Question 5: Which extra table tags does this chapter list?

<details>
<summary>Answer</summary>

- [x] `<caption>`, `<colgroup>`, `<col>`.
- [x] `<thead>`, `<tbody>`, `<tfoot>`.

</details>

### Question 6: How did the Try it examples make the grid visible?

<details>
<summary>Answer</summary>

- [x] CSS: `table, th, td { border: 1px solid black; }`.

</details>

</details>

## Summary

Use `<table>` with `<tr>` rows and `<td>` cells. `<th>` is a header cell (bold, centered by default). Keep cell counts even across rows unless a later chapter covers spanning.

## References

- [HTML Tables (W3Schools)](https://www.w3schools.com/html/html_tables.asp)
- [Try it Yourself: tryhtml_table_intro](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro)
- [Try it Yourself: tryhtml_table3](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table3)
- [Try it Yourself: tryhtml_table4](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table4)
- [Try it Yourself: tryhtml_table5](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table5)
- [Try it Yourself: tryhtml_table6](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table6)
- [Table Borders](https://www.w3schools.com/html/html_table_borders.asp)
- [MDN: `<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
- [MDN: `<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th)
- [MDN: `<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td)
