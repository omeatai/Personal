<details>
  <summary>HTML Entities</summary>

## Introduction

Reserved characters in HTML must be replaced with **character entities**. This chapter covers entity **names** (`&lt;`) and **numbers** (`&#60;`), the **non-breaking space**, a table of useful entities, and **combining diacritical marks**.

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
- [x] Sandbox: `code_sandbox/html-entities/index.html`.

<img alt="html-entities result" src="./code_sandbox/snaps/html-entities-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Render reserved characters, copyright, non-breaking spaces, and combining accents.

### **Overview**

- [ ] Serve `code_sandbox` and open `html-entities/`.
- [ ] Success: `<` `>` `&` `© W3Schools.com`, `10 km/h` / `10 PM`, à and á.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-entities/`

<img alt="html-entities result" src="./code_sandbox/snaps/html-entities-result.png" />

The entity examples match the chapter.

</details>

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
  <summary>Code</summary>

## Code

Sandbox: `code_sandbox/html-entities/index.html`

<img alt="html-entities source" src="./code_sandbox/snaps/html-entities-code.png" />

```html
<p>Less than: &lt;</p>
<p>Greater than: &gt;</p>
<p>Ampersand: &amp;</p>
<p>Copyright: &copy; W3Schools.com</p>
<p>10&nbsp;km/h &nbsp; 10&nbsp;PM</p>
<p>a grave: a&#768; &nbsp; a acute: a&#769;</p>
```

<img alt="html-entities result" src="./code_sandbox/snaps/html-entities-result.png" />

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

</details>

<details>
  <summary>HTML Symbols</summary>

## Introduction

Symbols that are **not on the keyboard** can be added with entity **names**, **decimal** numbers, or **hex** numbers. This chapter shows the euro sign three ways, then tables of common symbols, math operators, and Greek letters.

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
- [x] Sandbox: `code_sandbox/html-symbols/index.html`.

<img alt="html-symbols result" src="./code_sandbox/snaps/html-symbols-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Show the euro three ways, then copyright/arrows, card suits, and a few math/Greek symbols.

### **Overview**

- [ ] Serve `code_sandbox` and open `html-symbols/`.
- [ ] Success: three **€** lines, then © ® ™ arrows, ♠♣♥♦, and Σ ∞ Α Ω.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-symbols/`

<img alt="html-symbols result" src="./code_sandbox/snaps/html-symbols-result.png" />

The symbol examples match the chapter.

</details>

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
  <summary>Code</summary>

## Code

Sandbox: `code_sandbox/html-symbols/index.html`

<img alt="html-symbols source" src="./code_sandbox/snaps/html-symbols-code.png" />

```html
<p>I will display &euro;</p>
<p>I will display &#8364;</p>
<p>I will display &#x20AC;</p>
<p>&copy; &reg; &trade; &larr; &uarr; &rarr; &darr;</p>
<p>&spades; &clubs; &hearts; &diams;</p>
<p>&sum; &infin; &Alpha; &Omega;</p>
```

<img alt="html-symbols result" src="./code_sandbox/snaps/html-symbols-result.png" />

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

</details>

<details>
  <summary>HTML Emojis</summary>

## Introduction

Emojis look like images, but they are **UTF-8 characters**. This chapter sets `charset="UTF-8"`, shows entity numbers for letters and emojis, and sizes emojis with CSS `font-size` like any other character.

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
- [x] Sandbox: `code_sandbox/html-emojis/index.html` (first emoji, sized row, and A B C vs `&#65; &#66; &#67;`).

<img alt="html-emojis result" src="./code_sandbox/snaps/html-emojis-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Show a grinning face, a 48px emoji row, and A B C written both as letters and as entity numbers.

### **Overview**

- [ ] Serve `code_sandbox` and open `html-emojis/`.
- [ ] Success: **My First Emoji** with 😀; **Sized Emojis** at 48px (😀 😄 😍 💗); two lines that both read **I will display A B C**.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-emojis/`

<img alt="html-emojis result" src="./code_sandbox/snaps/html-emojis-result.png" />

The emoji examples match the chapter.

</details>

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
  <summary>Code</summary>

## Code

Sandbox: `code_sandbox/html-emojis/index.html`

<img alt="html-emojis source" src="./code_sandbox/snaps/html-emojis-code.png" />

```html
<h1>My First Emoji</h1>
<p>&#128512;</p>
<h1>Sized Emojis</h1>
<p style="font-size: 48px">&#128512; &#128516; &#128525; &#128151;</p>
<p>I will display A B C</p>
<p>I will display &#65; &#66; &#67;</p>
```

<img alt="html-emojis result" src="./code_sandbox/snaps/html-emojis-result.png" />

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

</details>

<details>
  <summary>HTML Charsets</summary>

## Introduction

A browser must know the **character set** to display a page correctly. This chapter sets `charset` in `<meta>`, compares **ASCII**, **ANSI (Windows-1252)**, **ISO-8859-1**, and **UTF-8**, and shows why UTF-8 is the HTML recommendation.

## Detailed Explanation

- [x] **Specify the set** in a meta tag: `<meta charset="UTF-8">`.
- [x] The HTML spec encourages **UTF-8** — it covers almost all characters and symbols in the world.
- [x] **ASCII** — first web encoding; **128** Latin characters: a–z A–Z, 0–9, and some punctuation (`! $ + - ( ) @ < > . # ?`).
- [x] **ANSI (Windows-1252)** — first Windows set: ASCII for 0–127, extra characters 128–159, same as UTF-8 from 160–255. `<meta charset="Windows-1252">`.
- [x] **ISO-8859-1** — default for **HTML 4**; 256 characters. ASCII for 0–127, unused 128–159, same as ANSI/UTF-8 from 160–255.
  - HTML 4: `<meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1">`
  - HTML 5: `<meta charset="ISO-8859-1">`
- [x] **UTF-8**
  - Same as ASCII for 0–127; unused 128–159; same as ANSI and 8859-1 for 160–255; then continues from 256 to **10 000+** characters.
  - `<meta charset="UTF-8">`
- [x] The page galleries **HTML UTF-8 Characters** (Basic Latin, Latin Extended A–E, IPA, punctuation, super/subscript, Braille). Sandbox: `code_sandbox/html-charsets/index.html`.

<img alt="html-charsets result" src="./code_sandbox/snaps/html-charsets-result.png" />

<details>
  <summary>Lab</summary>

## Lab

The chapter has no Try it Yourself editor. The sandbox is a UTF-8 page that shows Latin, punctuation, and combining diacritics.

### **Overview**

- [ ] Serve `code_sandbox` and open `html-charsets/`.
- [ ] Success: Basic Latin, Ā Ć Ē, ‰ ‼ ⁇, and à á â ã all render (the file is saved as UTF-8 with `<meta charset="UTF-8">`).

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-charsets/`

<img alt="html-charsets result" src="./code_sandbox/snaps/html-charsets-result.png" />

UTF-8 characters display correctly.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-charsets/`.

</details>

<details>
  <summary>Code</summary>

## Code

Declare UTF-8, then put Unicode in the file:

<img alt="html-charsets source" src="./code_sandbox/snaps/html-charsets-code.png" />

```html
<meta charset="UTF-8" />
```

Sandbox body (`html-charsets/index.html`):

```html
<p>Basic Latin: ABCD abcd 0123 ?#$%</p>
<p>Latin Extended: Ā Ć Ē</p>
<p>Punctuation: ‰ ‼ ⁇</p>
<p>Diacritics: à á â ã</p>
```

<img alt="html-charsets result" src="./code_sandbox/snaps/html-charsets-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you tell the browser the character set?

<details>
<summary>Answer</summary>

- [x] `<meta charset="UTF-8">` (or another set name).

</details>

### Question 2: Which character set does the HTML spec encourage?

<details>
<summary>Answer</summary>

- [x] **UTF-8**.

</details>

### Question 3: How many characters did ASCII define?

<details>
<summary>Answer</summary>

- [x] **128** Latin characters.

</details>

### Question 4: What was the default character set for HTML 4?

<details>
<summary>Answer</summary>

- [x] **ISO-8859-1**.

</details>

### Question 5: How did HTML 4 vs HTML 5 declare ISO-8859-1?

<details>
<summary>Answer</summary>

- [x] HTML 4: `<meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1">`.
- [x] HTML 5: `<meta charset="ISO-8859-1">`.

</details>

### Question 6: How does UTF-8 relate to ASCII?

<details>
<summary>Answer</summary>

- [x] Identical to ASCII for values **0–127**.
- [x] Then it continues from 256 to thousands more characters.

</details>

</details>

## Summary

Put `<meta charset="UTF-8">` in the head. ASCII, ANSI, and ISO-8859-1 cover a small Latin range; UTF-8 includes those values and almost every other character.

## References

- [HTML Encoding / Charsets (W3Schools)](https://www.w3schools.com/html/html_charset.asp)
- [Full UTF-8 Reference](https://www.w3schools.com/charsets/ref_html_utf8.asp)
- [HTML Character Sets](https://www.w3schools.com/charsets/default.asp)
- [MDN: `<meta>` charset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#charset)
- [WHATWG: Encoding](https://html.spec.whatwg.org/multipage/semantics.html#character-encoding-declaration)

</details>

<details>
  <summary>HTML URL Encode</summary>

## Introduction

A **URL** is a web address. This chapter explains URL **syntax**, common **schemes**, and **URL encoding**: non-ASCII characters become `%` plus hex, and spaces become `+` or `%20`.

## Detailed Explanation

- [x] **URL = web address** — words (`w3schools.com`) or an IP (`192.68.20.50`). Names are easier to remember.
- [x] Browsers request pages with a URL. Example: `https://www.w3schools.com/html/default.asp`.
- [x] **Syntax:** `scheme://prefix.domain:port/path/filename`
  - **scheme** — service type (`http` or `https`)
  - **prefix** — domain prefix (default `www` for http)
  - **domain** — name like `w3schools.com`
  - **port** — host port (default **80** for http)
  - **path** — path on the server (omit = site root)
  - **filename** — document or resource name
- [x] **Common schemes**

| Scheme  | Short for                          | Used for                        |
| ------- | ---------------------------------- | ------------------------------- |
| `http`  | HyperText Transfer Protocol        | Common web pages. Not encrypted |
| `https` | Secure HyperText Transfer Protocol | Secure web pages. Encrypted     |
| `ftp`   | File Transfer Protocol             | Downloading or uploading files  |
| `file`  |                                    | A file on your computer         |

- [x] **URL encoding**
  - URLs can only be sent using the **ASCII** character set. Non-ASCII must be converted.
  - Encoding replaces non-ASCII with **`%` + hexadecimal digits**.
  - URLs cannot contain spaces: a space becomes **`+`** or **`%20`**.
- [x] **Try It Yourself:** a form `GET`s the input; the browser encodes it before the request. After Submit, the query string shows `+` / `%20` (and UTF-8 sequences such as `%E2%82%AC` for €).
- [x] **ASCII encoding examples** (page charset is UTF-8 by default in HTML5)

| Character | From Windows-1252 | From UTF-8  |
| --------- | ----------------- | ----------- |
| €         | `%80`             | `%E2%82%AC` |
| £         | `%A3`             | `%C2%A3`    |
| ©         | `%A9`             | `%C2%A9`    |
| ®         | `%AE`             | `%C2%AE`    |
| À         | `%C0`             | `%C3%80`    |
| Á         | `%C1`             | `%C3%81`    |
| Â         | `%C2`             | `%C3%82`    |
| Ã         | `%C3`             | `%C3%83`    |
| Ä         | `%C4`             | `%C3%84`    |
| Å         | `%C5`             | `%C3%85`    |

- [x] Sandbox: `code_sandbox/html-url-encode/index.html` (syntax notes + local GET form; the live W3Schools form posts to their server).

<img alt="html-url-encode result" src="./code_sandbox/snaps/html-url-encode-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Read the URL parts, then submit the form and look at the address bar for encoding.

### **Overview**

- [ ] Serve `code_sandbox` and open `html-url-encode/`.
- [ ] Success: example URL, syntax line, encoding note, and a **Hello World** field with Submit.
- [ ] After Submit, the URL includes `?text=Hello+World` (or `%20` depending on the browser).

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-url-encode/`

<img alt="html-url-encode result" src="./code_sandbox/snaps/html-url-encode-result.png" />

The URL-encode demo matches the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-url-encode/`.

</details>

<details>
  <summary>Code</summary>

## Code

Sandbox: `code_sandbox/html-url-encode/index.html`

<img alt="html-url-encode source" src="./code_sandbox/snaps/html-url-encode-code.png" />

```html
<p>Example URL: https://www.w3schools.com/html/default.asp</p>
<p>Syntax: scheme://prefix.domain:port/path/filename</p>
<p>Spaces become + or %20. Euro in UTF-8 is %E2%82%AC.</p>
<form action="" method="get">
  <label>Try It Yourself: <input name="text" value="Hello World" /></label>
  <button type="submit">Submit</button>
</form>
```

<img alt="html-url-encode result" src="./code_sandbox/snaps/html-url-encode-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a URL?

<details>
<summary>Answer</summary>

- [x] Another word for a **web address**.
- [x] Browsers use it to request a page from a server.

</details>

### Question 2: What is the URL syntax pattern?

<details>
<summary>Answer</summary>

- [x] `scheme://prefix.domain:port/path/filename`.

</details>

### Question 3: What is the difference between `http` and `https`?

<details>
<summary>Answer</summary>

- [x] `http` — common web pages, **not encrypted**.
- [x] `https` — secure web pages, **encrypted**.

</details>

### Question 4: Why encode URLs?

<details>
<summary>Answer</summary>

- [x] URLs may only use the **ASCII** character set.
- [x] Non-ASCII characters are replaced with `%` plus hex digits.

</details>

### Question 5: How is a space encoded in a URL?

<details>
<summary>Answer</summary>

- [x] As a plus (`+`) or as `%20`.

</details>

### Question 6: How is € encoded in UTF-8 vs Windows-1252?

<details>
<summary>Answer</summary>

- [x] UTF-8: `%E2%82%AC`.
- [x] Windows-1252: `%80`.

</details>

</details>

## Summary

A URL is `scheme://prefix.domain:port/path/filename`. Use `https` for encrypted pages. Encode non-ASCII as `%HH` and spaces as `+` or `%20`; the encoding depends on the page charset (HTML5 default: UTF-8).

## References

- [HTML URL Encoding (W3Schools)](https://www.w3schools.com/html/html_urlencode.asp)
- [URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp)
- [MDN: URLs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)
- [MDN: `encodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)

</details>
