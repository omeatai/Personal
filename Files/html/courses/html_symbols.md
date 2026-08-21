# HTML Symbols

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

Symbols that are **not on the keyboard** can be added with entity **names**, **decimal** numbers, or **hex** numbers. This chapter shows the euro sign three ways, then tables of common symbols, math operators, and Greek letters.

This section has **1** example:

- [x] **Example 1:** Main document [View](#html-symbols-example-01)

## Detailed Explanation

- [x] **Three ways to write a symbol** (euro example)
  - Name: `&euro;`
  - Decimal: `&#8364;`
  - Hex: `&#x20AC;`
  - All three display **€**.
- [x] **Common symbol entities**
  - `&copy;` ©, `&reg;` ®, `&trade;` ™, `&euro;` €
  - Arrows: `&larr;` `&uarr;` `&rarr;` `&darr;`
  - Cards: `&spades;` `&clubs;` `&hearts;` `&diams;`
- [x] **Math entities** (examples): `&forall;` `&part;` `&exist;` `&empty;` `&nabla;` `&isin;` `&notin;` `&ni;` `&prod;` `&sum;`
- [x] **Greek letters** (examples): `&Alpha;` `&Beta;` `&Gamma;` `&Delta;` `&Epsilon;` `&Zeta;`
- [x] The page also shows more Unicode groups (currency, arrows, weather, chess, music, and so on) as a gallery, with links to full charset references.

<a id="html-symbols-example-01"></a>

### **Example 1: Main document**

- [x] This example runs the tested markup in `code_sandbox/html-symbols/index.html`.

Sandbox: `code_sandbox/html-symbols/index.html`

```html
<p>I will display &euro;</p>
<p>I will display &#8364;</p>
<p>I will display &#x20AC;</p>
<p>&copy; &reg; &trade; &larr; &uarr; &rarr; &darr;</p>
<p>&spades; &clubs; &hearts; &diams;</p>
<p>&sum; &infin; &Alpha; &Omega;</p>
```

<img alt="html-symbols source" src="../code_sandbox/snaps/html-symbols-code.png" />

<img alt="html-symbols result" src="../code_sandbox/snaps/html-symbols-result.png" />

- [x] **Outcome:** the browser shows **I will display &euro;**, **I will display &#8364;**, **I will display &#x20AC;**, **&copy; &reg; &trade; &larr; &uarr; &rarr; &darr;**, **&spades; &clubs; &hearts; &diams;**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-symbols/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How can you write the euro sign in HTML?

<details>
<summary>Answer</summary>

- [x] `&euro;` (name), `&#8364;` (decimal), or `&#x20AC;` (hex).

</details>

### Question 2: Why use entities for symbols?

<details>
<summary>Answer</summary>

- [x] Many symbols are **not on the keyboard**.
- [x] Names, decimal numbers, or hex numbers all work.

</details>

### Question 3: What entities are ©, ®, and ™?

<details>
<summary>Answer</summary>

- [x] `&copy;`, `&reg;`, `&trade;`.

</details>

### Question 4: What entities are the four card suits?

<details>
<summary>Answer</summary>

- [x] `&spades;` `&clubs;` `&hearts;` `&diams;`.

</details>

### Question 5: What is `&sum;`?

<details>
<summary>Answer</summary>

- [x] N-ary summation (Σ).

</details>

### Question 6: What is `&Alpha;`?

<details>
<summary>Answer</summary>

- [x] Greek capital letter Alpha (Α).

</details>

</details>

## Summary

Add off-keyboard symbols with a name, a decimal (`&#8364;`), or a hex (`&#x20AC;`) entity. The same pattern covers arrows, cards, math, and Greek letters.

## References

- [HTML Symbols (W3Schools)](https://www.w3schools.com/html/html_symbols.asp)
- [Try it Yourself: tryhtml_utf_euro](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_utf_euro)
- [Full Symbols Reference](https://www.w3schools.com/charsets/ref_utf_symbols_intro.asp)
- [Full Math Symbols Reference](https://www.w3schools.com/charsets/ref_utf_math.asp)
- [Full Greek Reference](https://www.w3schools.com/charsets/ref_utf_greek.asp)
- [MDN: Named character references](https://developer.mozilla.org/en-US/docs/Glossary/Entity)
