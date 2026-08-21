# JS Introduction

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

JavaScript is the **programming language of the web**. This section shows what it can do in a page: **change HTML content**, **change attribute values**, **change CSS**, and **hide or show** elements. It also separates JavaScript from **Java**, and names **Brendan Eich (1995)** and the **ECMAScript / ECMA-262** standard.

This section has **4** examples:

- [x] **Example 1:** Change HTML content [View](#js-introduction-example-01)
- [x] **Example 2:** Change an HTML attribute value [View](#js-introduction-example-02)
- [x] **Example 3:** Change an HTML style (CSS) [View](#js-introduction-example-03)
- [x] **Example 4:** Hide and show elements [View](#js-introduction-example-04)

## Detailed Explanation

- [x] **JavaScript is the programming language of the web**
  - It can **calculate**, **manipulate**, and **validate** data.
  - It can **update and change** both **HTML** and **CSS** live in the page.
- [x] **The common pattern in every example below**
  - **Select** an element, then **change** something about it.
  - Selection here uses **`document.getElementById("id")`** — it finds the one element whose `id` matches.
  - What you change is either its **content** (`innerHTML`), an **attribute** (`src`), or its **style** (`style.fontSize`, `style.display`).
- [x] **How the sandbox demos capture the "after" state**
  - Each demo keeps the original button so you can click it yourself.
  - It also runs the same statement automatically when the URL ends in **`?run`**, so the screenshots below show the exact outcome the click produces.

<a id="js-introduction-example-01"></a>

### **Example 1: Change HTML content**

- [x] **`document.getElementById("demo")`** finds the `<p id="demo">`, and **`.innerHTML = "Hello JavaScript"`** replaces everything inside that paragraph.
- [x] The statement lives in the button's **`onclick`**, so it runs **once per click**.
- [x] **Quotes are interchangeable:** `innerHTML = "Hello JavaScript"` and `innerHTML = 'Hello JavaScript'` behave identically — JavaScript accepts both **double** and **single** quotes for strings.
- [x] `innerHTML` parses its value as **HTML**, so `"<b>Hi</b>"` would render bold, not literal tags.

Sandbox: `code_sandbox/js-introduction/index.html`

```html
<h2>What Can JavaScript Do?</h2>
<p id="demo">JavaScript can change HTML content.</p>
<button
  type="button"
  onclick="document.getElementById('demo').innerHTML = 'Hello JavaScript'"
>
  Click Me!
</button>
```

![js-introduction example 1 source](../code_sandbox/snaps/js-introduction-01-code.png)

![js-introduction example 1 result](../code_sandbox/snaps/js-introduction-01-result.png)

- [x] **Outcome:** before the click the paragraph reads **JavaScript can change HTML content.**; after the click (shown above) it reads **Hello JavaScript**.

<a id="js-introduction-example-02"></a>

### **Example 2: Change an HTML attribute value**

- [x] The light-bulb demo swaps the **`src`** attribute of an `<img id="myImage">` between two files.
- [x] **Turn on the light** sets `src = "pic_bulbon.svg"`; **Turn off the light** sets `src = "pic_bulboff.svg"`.
- [x] Changing an attribute is the same select-then-assign pattern; only the property (`.src`) differs.
- [x] The sandbox uses local **SVG** on/off bulbs instead of the site's GIF files, so it works fully offline.

Sandbox: `code_sandbox/js-introduction/lightbulb.html`

```html
<p>JavaScript can change HTML attribute values.</p>
<button onclick="document.getElementById('myImage').src = 'pic_bulbon.svg'">
  Turn on the light
</button>
<button onclick="document.getElementById('myImage').src = 'pic_bulboff.svg'">
  Turn off the light
</button>
<img id="myImage" src="pic_bulboff.svg" width="100" height="180" />
```

![js-introduction example 2 source](../code_sandbox/snaps/js-introduction-02-code.png)

![js-introduction example 2 result](../code_sandbox/snaps/js-introduction-02-result.png)

- [x] **Outcome:** the page starts on the grey **off** bulb; running the "on" statement swaps the image to the yellow **on** bulb (shown above) without reloading the page.

<a id="js-introduction-example-03"></a>

### **Example 3: Change an HTML style (CSS)**

- [x] Changing style is a variant of changing an attribute — you assign to properties on the element's **`style`** object.
- [x] `document.getElementById("demo").style.fontSize = "35px"` enlarges the paragraph text.
- [x] CSS property names become **camelCase** in JavaScript: `font-size` → `fontSize`, `background-color` → `backgroundColor`.
- [x] The value is a **string with units** (`"35px"`), not a bare number.

Sandbox: `code_sandbox/js-introduction/style.html`

```html
<p id="demo">JavaScript can change the style of an HTML element.</p>
<button onclick="document.getElementById('demo').style.fontSize = '35px'">
  Click Me!
</button>
```

![js-introduction example 3 source](../code_sandbox/snaps/js-introduction-03-code.png)

![js-introduction example 3 result](../code_sandbox/snaps/js-introduction-03-result.png)

- [x] **Outcome:** the paragraph jumps from normal size to a large **35px** heading-sized line (shown above).

<a id="js-introduction-example-04"></a>

### **Example 4: Hide and show elements**

- [x] Visibility is controlled through the **`display`** style.
- [x] **Hide:** `style.display = "none"` removes the element from the layout (it disappears and takes no space).
- [x] **Show:** `style.display = "block"` puts it back.
- [x] One demo holds both buttons so you can toggle the paragraph off and on.

Sandbox: `code_sandbox/js-introduction/hide-show.html`

```html
<p id="demo">JavaScript can hide and show HTML elements.</p>
<button onclick="document.getElementById('demo').style.display = 'none'">
  Hide
</button>
<button onclick="document.getElementById('demo').style.display = 'block'">
  Show
</button>
```

![js-introduction example 4 source](../code_sandbox/snaps/js-introduction-04-code.png)

![js-introduction example 4 result](../code_sandbox/snaps/js-introduction-04-result.png)

- [x] **Outcome:** the demo loads with the paragraph visible plus **Hide** / **Show** buttons (shown above). Clicking **Hide** makes the paragraph vanish; clicking **Show** brings it back.

### **Did You Know? Java vs JavaScript**

- [x] **JavaScript and Java** are **completely different** languages, in both concept and design — the shared word "Java" is historical marketing, not a technical relationship.
- [x] JavaScript was invented by **Brendan Eich** in **1995** and became an **ECMA** standard in **1997**.
- [x] **ECMA-262** is the official name of the **standard**; **ECMAScript** is the official name of the **language**.
- [x] **Page exercise —** _True or False: "JAVA is short for JavaScript."_ → **False.**

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

Serve the sandbox so the Cursor browser can load the example (it cannot open `file://`).

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-introduction/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is JavaScript in this tutorial?

<details>
<summary>Answer</summary>

- [x] The **programming language of the web**.
- [x] It can calculate, manipulate, and validate data.
- [x] It can update and change **HTML** and **CSS**.

</details>

### Question 2: Which method finds the element with `id="demo"`?

<details>
<summary>Answer</summary>

- [x] **`document.getElementById("demo")`**.

</details>

### Question 3: How does the first example change the paragraph text?

<details>
<summary>Answer</summary>

- [x] It sets the element’s **`innerHTML`**.
- [x] The new content is **`Hello JavaScript`**.

</details>

### Question 4: Does JavaScript allow single quotes as well as double quotes?

<details>
<summary>Answer</summary>

- [x] **Yes.** Both **double** and **single** quotes are accepted.

</details>

### Question 5: How can JavaScript change an image?

<details>
<summary>Answer</summary>

- [x] By changing an HTML **attribute value**.
- [x] The light-bulb demo changes the **`src`** of an `<img>`.

</details>

### Question 6: How do you change an element’s CSS from JavaScript?

<details>
<summary>Answer</summary>

- [x] Assign to the element’s **`style`** properties.
- [x] Example: `document.getElementById("demo").style.fontSize = "35px";`
- [x] Changing style is a variant of changing an **attribute**.

</details>

### Question 7: How do you hide or show an HTML element?

<details>
<summary>Answer</summary>

- [x] Hide: `style.display = "none"`.
- [x] Show: `style.display = "block"`.

</details>

### Question 8: Are Java and JavaScript the same language?

<details>
<summary>Answer</summary>

- [x] **No.** They are **completely different** in concept and design.
- [x] **JAVA is not short for JavaScript.**

</details>

### Question 9: Who invented JavaScript, and when did it become an ECMA standard?

<details>
<summary>Answer</summary>

- [x] Invented by **Brendan Eich** in **1995**.
- [x] Became an **ECMA** standard in **1997**.

</details>

### Question 10: What are ECMA-262 and ECMAScript?

<details>
<summary>Answer</summary>

- [x] **ECMA-262** is the official name of the **standard**.
- [x] **ECMAScript** is the official name of the **language**.

</details>

</details>

## Summary

JavaScript is the **programming language of the web**. It can change **HTML content** (`getElementById` + `innerHTML`), **attribute values** (for example an image `src`), **CSS** (`style.fontSize`), and **visibility** (`display` `none` / `block`). Quotes may be **single or double**. JavaScript is **not** Java: Eich invented it in **1995**; **ECMA-262** is the standard and **ECMAScript** is the language name.

## References

- [JS Introduction (W3Schools)](https://www.w3schools.com/js/js_intro.asp)
- [Try it Yourself: tryjs_intro_inner_html](https://www.w3schools.com/js/tryit.asp?filename=tryjs_intro_inner_html)
- [Try it Yourself: tryjs_intro_inner_html_quotes](https://www.w3schools.com/js/tryit.asp?filename=tryjs_intro_inner_html_quotes)
- [Try it Yourself: tryjs_intro_lightbulb](https://www.w3schools.com/js/tryit.asp?filename=tryjs_intro_lightbulb)
- [Try it Yourself: tryjs_intro_style](https://www.w3schools.com/js/tryit.asp?filename=tryjs_intro_style)
- [Try it Yourself: tryjs_intro_hide](https://www.w3schools.com/js/tryit.asp?filename=tryjs_intro_hide)
- [Try it Yourself: tryjs_intro_show](https://www.w3schools.com/js/tryit.asp?filename=tryjs_intro_show)
- [See all JavaScript Versions](https://www.w3schools.com/js/js_versions.asp)
- [MDN: JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [MDN: Document.getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)
- [ECMA-262](https://tc39.es/ecma262/)
