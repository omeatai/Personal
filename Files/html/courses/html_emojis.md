# HTML Emojis

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

Emojis look like images, but they are **UTF-8 characters**. This chapter sets `charset="UTF-8"`, shows entity numbers for letters and emojis, and sizes emojis with CSS `font-size` like any other character.

This section has **1** example:

- [x] **Example 1:** Main document [View](#html-emojis-example-01)

## Detailed Explanation

- [x] **Emojis are characters**, not images — they come from the UTF-8 (Unicode) set (😄 😍 💗). UTF-8 covers almost all characters and symbols.
- [x] **`charset`**: `<meta charset="UTF-8">`. If omitted, **UTF-8 is the HTML default**.
- [x] **Entity numbers** for characters you cannot type: start with `&#` and end with `;`.
  - A is 65, B is 66, C is 67 → `&#65; &#66; &#67;` displays **A B C**.
- [x] **Emoji numbers** (examples)
  - 😀 `&#128512;`
  - 😄 `&#128516;`
  - 😍 `&#128525;`
  - 💗 `&#128151;`
- [x] **Size like text**: `font-size:48px` on a paragraph of emoji entities.

<a id="html-emojis-example-01"></a>

### **Example 1: Main document**

- [x] This example runs the tested markup in `code_sandbox/html-emojis/index.html`.

Sandbox: `code_sandbox/html-emojis/index.html`

```html
<h1>My First Emoji</h1>
<p>&#128512;</p>
<h1>Sized Emojis</h1>
<p style="font-size: 48px">&#128512; &#128516; &#128525; &#128151;</p>
<p>I will display A B C</p>
<p>I will display &#65; &#66; &#67;</p>
```

<img alt="html-emojis source" src="../code_sandbox/snaps/html-emojis-code.png" />

<img alt="html-emojis result" src="../code_sandbox/snaps/html-emojis-result.png" />

- [x] **Outcome:** the browser shows **My First Emoji**, **&#128512;**, **Sized Emojis**, **&#128512; &#128516; &#128525; &#128151;**, **I will display A B C**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-emojis/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Are emojis images?

<details>
<summary>Answer</summary>

- [x] **No.** They look like images but are **UTF-8 characters**.

</details>

### Question 2: How do you declare UTF-8 on the page?

<details>
<summary>Answer</summary>

- [x] `<meta charset="UTF-8">`.
- [x] UTF-8 is already the **HTML default** if you omit it.

</details>

### Question 3: How must an entity number be written?

<details>
<summary>Answer</summary>

- [x] Start with `&#` and end with `;` (example: `&#65;` is A).

</details>

### Question 4: What entity is the grinning face 😀?

<details>
<summary>Answer</summary>

- [x] `&#128512;`.

</details>

### Question 5: How do you make emojis larger?

<details>
<summary>Answer</summary>

- [x] Treat them as text: set **`font-size`** (the chapter uses `48px`).

</details>

### Question 6: What numbers are A, B, and C?

<details>
<summary>Answer</summary>

- [x] 65, 66, and 67.

</details>

</details>

## Summary

Emojis are UTF-8 letters. Declare `charset="UTF-8"`, write them as `&#number;`, and size them with CSS like any other character.

## References

- [HTML Emojis (W3Schools)](https://www.w3schools.com/html/html_emojis.asp)
- [Full HTML Emoji Reference](https://www.w3schools.com/charsets/ref_emoji.asp)
- [Try it Yourself: tryhtml_emoji_128512](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_emoji_128512)
- [Unicode Emoji Charts](https://unicode.org/emoji/charts/full-emoji-list.html)
- [MDN: Unicode](https://developer.mozilla.org/en-US/docs/Glossary/Unicode)
