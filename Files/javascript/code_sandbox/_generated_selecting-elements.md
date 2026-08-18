<details>
  <summary>Selecting Elements</summary>

## Introduction

Before you can change an element you must find it: id, tag, class, CSS selectors, or document collections.

This section has **15** examples:

- [x] **Example 1:** Finding HTML Element by Id [View](#selecting-elements-example-01)
- [x] **Example 2:** Finding HTML Elements by Tag Name [View](#selecting-elements-example-02)
- [x] **Example 3:** Tag name inside another element [View](#selecting-elements-example-03)
- [x] **Example 4:** Finding HTML Elements by Class Name [View](#selecting-elements-example-04)
- [x] **Example 5:** The querySelector() Method [View](#selecting-elements-example-05)
- [x] **Example 6:** The querySelectorAll() Method [View](#selecting-elements-example-06)
- [x] **Example 7:** querySelectorAll("p.intro") [View](#selecting-elements-example-07)
- [x] **Example 8:** Common mistake — `#` in getElementById() [View](#selecting-elements-example-08)
- [x] **Example 9:** Common mistake — querySelector returns only the first match [View](#selecting-elements-example-09)
- [x] **Example 10:** Finding elements via document.forms [View](#selecting-elements-example-10)
- [x] **Example 11:** document.images collection [View](#selecting-elements-example-11)
- [x] **Example 12:** document.links collection [View](#selecting-elements-example-12)
- [x] **Example 13:** document.scripts collection [View](#selecting-elements-example-13)
- [x] **Example 14:** document.body, document.title, document.head [View](#selecting-elements-example-14)
- [x] **Example 15:** document.embeds and document.anchors (legacy) [View](#selecting-elements-example-15)

## Detailed Explanation

- [x] `getElementById` returns one node or null (no `#` in the argument).
- [x] `querySelector` is first-match CSS; `querySelectorAll` is every match.
- [x] `document.forms`, `images`, `links`, `body`, `title` are HTML collections / shortcuts.

<a id="selecting-elements-example-01"></a>

### **Example 1: Finding HTML Element by Id**

- [x] Easiest lookup: **`document.getElementById("intro")`**.
- [x] Ids must be unique in the document. Duplicate ids make this method return the **first** one.
- [x] If found, you get the element object. If not, **`null`**.

Sandbox: `code_sandbox/selecting-elements/find-by-id.html`

```html
<p id="intro">Intro paragraph</p>
<script>
const element = document.getElementById("intro");
</script>
```

<img alt="selecting-elements example 1 source" src="./code_sandbox/snaps/selecting-elements-01-code.png" />

<img alt="selecting-elements example 1 result" src="./code_sandbox/snaps/selecting-elements-01-result.png" />

- [x] **Outcome:** `element` is the intro paragraph; a missing id returns **null**.

<a id="selecting-elements-example-02"></a>

### **Example 2: Finding HTML Elements by Tag Name**

- [x] `document.getElementsByTagName("p")` collects **every** `<p>` in the document.
- [x] The result is an HTMLCollection: use `[0]`, `[1]`, `.length`.
- [x] Order is **tree order** (top to bottom in the markup).

Sandbox: `code_sandbox/selecting-elements/find-by-tag.html`

```html
<p>Red</p><p>Blue</p>
<script>
const element = document.getElementsByTagName("p");
</script>
```

<img alt="selecting-elements example 2 source" src="./code_sandbox/snaps/selecting-elements-02-code.png" />

<img alt="selecting-elements example 2 result" src="./code_sandbox/snaps/selecting-elements-02-result.png" />

- [x] **Outcome:** Two paragraphs are listed: **Red** then **Blue**.

<a id="selecting-elements-example-03"></a>

### **Example 3: Tag name inside another element**

- [x] Elements also have `getElementsByTagName`. Scope the search to a subtree.
- [x] Here `#main` contains the paragraphs we want; paragraphs outside `#main` are ignored.
- [x] Pattern: find a root, then search **inside** it.

Sandbox: `code_sandbox/selecting-elements/find-tag-inside-id.html`

```html
<div id="main"><p>In</p><p>Also</p></div>
<p>Outside</p>
<script>
const x = document.getElementById("main");
const y = x.getElementsByTagName("p");
</script>
```

<img alt="selecting-elements example 3 source" src="./code_sandbox/snaps/selecting-elements-03-code.png" />

<img alt="selecting-elements example 3 result" src="./code_sandbox/snaps/selecting-elements-03-result.png" />

- [x] **Outcome:** `y.length` is **2**. The **Outside** paragraph is not included.

<a id="selecting-elements-example-04"></a>

### **Example 4: Finding HTML Elements by Class Name**

- [x] `getElementsByClassName("intro")` — class token only, no leading dot.
- [x] Elements with multiple classes (`class="intro note"`) still match `intro`.
- [x] Live HTMLCollection, same indexing rules as tag-name lists.

Sandbox: `code_sandbox/selecting-elements/find-by-class.html`

```html
<p class="intro">A</p>
<div class="intro">B</div>
<script>
const x = document.getElementsByClassName("intro");
</script>
```

<img alt="selecting-elements example 4 source" src="./code_sandbox/snaps/selecting-elements-04-code.png" />

<img alt="selecting-elements example 4 result" src="./code_sandbox/snaps/selecting-elements-04-result.png" />

- [x] **Outcome:** Both the paragraph and the div with class **intro** are returned (length **2**).

<a id="selecting-elements-example-05"></a>

### **Example 5: The querySelector() Method**

- [x] `querySelector` takes a **CSS** selector, so classes **do** use a leading `.`.
- [x] Only the first match is returned.
- [x] Returns `null` if nothing matches — check before you set `innerHTML`.

Sandbox: `code_sandbox/selecting-elements/qs-class.html`

```html
<p class="note">Hello World!</p>
<script>
const myPara = document.querySelector(".note");
myPara.innerHTML = "Hello World!";
</script>
```

<img alt="selecting-elements example 5 source" src="./code_sandbox/snaps/selecting-elements-05-code.png" />

<img alt="selecting-elements example 5 result" src="./code_sandbox/snaps/selecting-elements-05-result.png" />

- [x] **Outcome:** The first `.note` paragraph is set to **Hello World!**.

<a id="selecting-elements-example-06"></a>

### **Example 6: The querySelectorAll() Method**

- [x] `querySelectorAll(".demo")` returns **all** matches as a NodeList.
- [x] Index `[0]` is the first. Assigning `innerHTML` on `[0]` does not change the others.
- [x] NodeList is **static**: later DOM changes do not update this list.

Sandbox: `code_sandbox/selecting-elements/qsa-first-item.html`

```html
<p class="row">One</p><p class="row">Two</p>
<script>
const myItems = document.querySelectorAll(".row");
myItems[0].innerHTML = "First";
</script>
```

<img alt="selecting-elements example 6 source" src="./code_sandbox/snaps/selecting-elements-06-code.png" />

<img alt="selecting-elements example 6 result" src="./code_sandbox/snaps/selecting-elements-06-result.png" />

- [x] **Outcome:** Item 0 becomes **First**; item 1 stays **Two**.

<a id="selecting-elements-example-07"></a>

### **Example 7: querySelectorAll("p.intro")**

- [x] `p.intro` means **paragraphs** that also have class **intro** — not every `.intro`.
- [x] A `<div class="intro">` would **not** match this selector.
- [x] This is the compound-selector form the W3Schools page shows for “all p.intro”.

Sandbox: `code_sandbox/selecting-elements/qsa-p-intro.html`

```html
<p class="intro">yes</p>
<div class="intro">no</div>
<p>plain</p>
<script>
const x = document.querySelectorAll("p.intro");
</script>
```

<img alt="selecting-elements example 7 source" src="./code_sandbox/snaps/selecting-elements-07-code.png" />

<img alt="selecting-elements example 7 result" src="./code_sandbox/snaps/selecting-elements-07-result.png" />

- [x] **Outcome:** Only the **yes** paragraph matches `p.intro` (length **1**).

<a id="selecting-elements-example-08"></a>

### **Example 8: Common mistake — `#` in getElementById()**

- [x] **Wrong:** `getElementById("#demo")` looks for an id that is literally `#demo`.
- [x] **Right:** `getElementById("demo")`. The `#` is only for CSS / `querySelector`.
- [x] This sandbox shows the wrong call returning **null** and the right call succeeding.

Sandbox: `code_sandbox/selecting-elements/mistake-hash-id.html`

```html
<p id="demo-el">ok</p>
<script>
document.getElementById("#demo-el"); // null
document.getElementById("demo-el");  // the paragraph
</script>
```

<img alt="selecting-elements example 8 source" src="./code_sandbox/snaps/selecting-elements-08-code.png" />

<img alt="selecting-elements example 8 result" src="./code_sandbox/snaps/selecting-elements-08-result.png" />

- [x] **Outcome:** With `#` the result is **null**; without `#` you get the paragraph **ok**.

<a id="selecting-elements-example-09"></a>

### **Example 9: Common mistake — querySelector returns only the first match**

- [x] Beginners call `querySelector(".item")` and wonder why later items never change.
- [x] Loop `querySelectorAll`, or use a more specific selector if you need one particular node.
- [x] This example changes only index 0 even though two `.item` nodes exist.

Sandbox: `code_sandbox/selecting-elements/mistake-qs-first-only.html`

```html
<p class="item">A</p><p class="item">B</p>
<script>
document.querySelector(".item").textContent = "only first";
</script>
```

<img alt="selecting-elements example 9 source" src="./code_sandbox/snaps/selecting-elements-09-code.png" />

<img alt="selecting-elements example 9 result" src="./code_sandbox/snaps/selecting-elements-09-result.png" />

- [x] **Outcome:** A becomes **only first**; B stays **B**.

<a id="selecting-elements-example-10"></a>

### **Example 10: Finding elements via document.forms**

- [x] `document.forms["frm1"]` is the form with `id` or `name` **frm1** (HTMLFormControlsCollection).
- [x] `form.elements` lists controls in order. `.value` is each field’s current string.
- [x] This is the “HTML object collections” style on the W3Schools page — older than querySelector, still valid.

Sandbox: `code_sandbox/selecting-elements/forms-collection.html`

```html
<form id="frm1">
  <input name="a" value="Hello">
  <input name="b" value="World">
</form>
<script>
const x = document.forms["frm1"];
let text = "";
for (let i = 0; i < x.length; i++) {
  text += x.elements[i].value + " ";
}
</script>
```

<img alt="selecting-elements example 10 source" src="./code_sandbox/snaps/selecting-elements-10-code.png" />

<img alt="selecting-elements example 10 result" src="./code_sandbox/snaps/selecting-elements-10-result.png" />

- [x] **Outcome:** The loop prints **Hello World** (trailing space included, matching the site pattern).

<a id="selecting-elements-example-11"></a>

### **Example 11: document.images collection**

- [x] `document.images` is an HTMLCollection of every `<img>` in the document.
- [x] Useful for counting or looping pictures without a CSS selector.
- [x] Each item is an HTMLImageElement (`src`, `alt`, `width`).

Sandbox: `code_sandbox/selecting-elements/collection-images.html`

```html
<img alt="one" width="16" height="16" src="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg'/>">
<script>
const n = document.images.length;
</script>
```

<img alt="selecting-elements example 11 source" src="./code_sandbox/snaps/selecting-elements-11-code.png" />

<img alt="selecting-elements example 11 result" src="./code_sandbox/snaps/selecting-elements-11-result.png" />

- [x] **Outcome:** `document.images.length` is **1** in this sandbox (plus any others the chrome adds — we report the count).

<a id="selecting-elements-example-12"></a>

### **Example 12: document.links collection**

- [x] `document.links` is every `<a>` and `<area>` that has an **`href`**.
- [x] A `<a>` without href is **not** in this collection.
- [x] Older pages used this instead of `querySelectorAll("a[href]")`.

Sandbox: `code_sandbox/selecting-elements/collection-links.html`

```html
<a href="https://example.com">ex</a>
<a>no href</a>
<script>
const n = document.links.length;
</script>
```

<img alt="selecting-elements example 12 source" src="./code_sandbox/snaps/selecting-elements-12-code.png" />

<img alt="selecting-elements example 12 result" src="./code_sandbox/snaps/selecting-elements-12-result.png" />

- [x] **Outcome:** Only the real hyperlink is counted in **`document.links`**.

<a id="selecting-elements-example-13"></a>

### **Example 13: document.scripts collection**

- [x] `document.scripts` lists every `<script>` element.
- [x] Inline scripts and `src` scripts both appear.
- [x] Handy for debugging “how many scripts loaded on this page?”

Sandbox: `code_sandbox/selecting-elements/collection-scripts.html`

```html
<script>/* counted */</script>
```

<img alt="selecting-elements example 13 source" src="./code_sandbox/snaps/selecting-elements-13-code.png" />

<img alt="selecting-elements example 13 result" src="./code_sandbox/snaps/selecting-elements-13-result.png" />

- [x] **Outcome:** `document.scripts.length` is at least **1** (this page’s own script tags).

<a id="selecting-elements-example-14"></a>

### **Example 14: document.body, document.title, document.head**

- [x] `document.body` is the `<body>` element. `document.head` is `<head>`.
- [x] `document.title` is the **document title** (string), matching `<title>` — you can assign it.
- [x] `document.documentElement` is the root `<html>` element.

Sandbox: `code_sandbox/selecting-elements/collection-body-title-head.html`

```html
<script>
document.title = "Selecting Elements";
</script>
```

<img alt="selecting-elements example 14 source" src="./code_sandbox/snaps/selecting-elements-14-code.png" />

<img alt="selecting-elements example 14 result" src="./code_sandbox/snaps/selecting-elements-14-result.png" />

- [x] **Outcome:** The sandbox reports the **body** tagName, **head** presence, **html** root, and the title string.

<a id="selecting-elements-example-15"></a>

### **Example 15: document.embeds and document.anchors (legacy)**

- [x] `document.embeds` is a collection of `<embed>` elements.
- [x] `document.anchors` was `<a name="...">` bookmarks. It is **deprecated** — do not use it in new code.
- [x] This example still **reads** both so you recognize them if you meet old pages.

Sandbox: `code_sandbox/selecting-elements/collection-embeds-anchors.html`

```html
<embed id="e" type="text/plain" width="1" height="1">
<a name="old">named anchor</a>
<script>
document.embeds.length;
document.anchors && document.anchors.length;
</script>
```

<img alt="selecting-elements example 15 source" src="./code_sandbox/snaps/selecting-elements-15-code.png" />

<img alt="selecting-elements example 15 result" src="./code_sandbox/snaps/selecting-elements-15-result.png" />

- [x] **Outcome:** `embeds.length` is **1**. `anchors` is deprecated; the sandbox prints its length if the browser still exposes it.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/selecting-elements/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `getElementById` return when nothing matches?

<details>
<summary>Answer</summary>

- [x] **`null`**.

</details>

### Question 2: How do you find every `<p>` inside `#main`?

<details>
<summary>Answer</summary>

- [x] `document.getElementById("main").getElementsByTagName("p")`.

</details>

### Question 3: Do you pass `".intro"` to `getElementsByClassName`?

<details>
<summary>Answer</summary>

- [x] No — pass **`"intro"`**. The dot is for CSS / `querySelector`.

</details>

### Question 4: What is wrong with `getElementById("#demo")`?

<details>
<summary>Answer</summary>

- [x] The `#` is included in the id search, so you get **null** unless the id is literally `#demo`.

</details>

### Question 5: Why did only the first `.item` change after `querySelector`?

<details>
<summary>Answer</summary>

- [x] `querySelector` returns **one** node — the first match.

</details>

### Question 6: How do you read every control value in `id="frm1"`?

<details>
<summary>Answer</summary>

- [x] `document.forms["frm1"]` then loop `form.elements[i].value`.

</details>

### Question 7: What is in `document.links`?

<details>
<summary>Answer</summary>

- [x] `<a>` and `<area>` elements that have an **`href`**.

</details>

### Question 8: What is `document.documentElement`?

<details>
<summary>Answer</summary>

- [x] The root **`<html>`** element.

</details>

### Question 9: Should new code use `document.anchors`?

<details>
<summary>Answer</summary>

- [x] No — it is **deprecated**. Use `id` + `getElementById` or `querySelector`.

</details>

### Question 10: Is `querySelectorAll` live?

<details>
<summary>Answer</summary>

- [x] No — it returns a **static** NodeList taken at call time.

</details>


</details>

## Summary

Pick the lookup that matches your markup: unique id, CSS selector, or a document collection — and remember first-vs-all.

## References

- [Selecting Elements](https://www.w3schools.com/js/js_htmldom_elements.asp)
- [MDN Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)

</details>
