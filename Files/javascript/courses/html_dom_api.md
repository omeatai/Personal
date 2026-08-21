# HTML DOM API

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The DOM API is the methods and properties on `document` and elements that find, change, and create HTML.

This section has **16** examples:

- [x] **Example 1:** DOM API — getElementById and innerHTML [View](#html-dom-api-example-01)
- [x] **Example 2:** document.getElementById(id) [View](#html-dom-api-example-02)
- [x] **Example 3:** document.getElementsByTagName(name) [View](#html-dom-api-example-03)
- [x] **Example 4:** document.getElementsByClassName(name) [View](#html-dom-api-example-04)
- [x] **Example 5:** document.querySelector(selector) [View](#html-dom-api-example-05)
- [x] **Example 6:** document.querySelectorAll(selector) [View](#html-dom-api-example-06)
- [x] **Example 7:** element.innerHTML [View](#html-dom-api-example-07)
- [x] **Example 8:** element.textContent [View](#html-dom-api-example-08)
- [x] **Example 9:** element.attribute — change src, href, id… [View](#html-dom-api-example-09)
- [x] **Example 10:** element.style.property [View](#html-dom-api-example-10)
- [x] **Example 11:** element.setAttribute() [View](#html-dom-api-example-11)
- [x] **Example 12:** document.createElement() [View](#html-dom-api-example-12)
- [x] **Example 13:** document.appendChild() / parent.appendChild() [View](#html-dom-api-example-13)
- [x] **Example 14:** parent.removeChild() [View](#html-dom-api-example-14)
- [x] **Example 15:** parent.replaceChild() [View](#html-dom-api-example-15)
- [x] **Example 16:** element.onclick = function(){…} [View](#html-dom-api-example-16)

## Detailed Explanation

- [x] Methods do actions; properties hold values.
- [x] Selection: getElementById, getElementsByTagName, getElementsByClassName, querySelector, querySelectorAll.
- [x] Content, attributes, structure (`createElement` / `appendChild` / `removeChild` / `replaceChild`), and `onclick`.

<a id="html-dom-api-example-01"></a>

### **Example 1: DOM API — getElementById and innerHTML**

- [x] The **DOM API** is the set of **methods** (actions) and **properties** (values) that change HTML.
- [x] `document` is the HTML document object — the entry point.
- [x] `getElementById("demo")` is a **document method** that returns the element (or `null`).
- [x] `innerHTML` is an **element property**. Assigning it replaces the element’s HTML content.

Sandbox: `code_sandbox/html-dom-api/api-hello.html`

```html
<p id="hello"></p>
<script>
const myPara = document.getElementById("hello");
myPara.innerHTML = "Hello World!";
</script>
```

<img alt="html-dom-api example 1 source" src="../code_sandbox/snaps/html-dom-api-01-code.png" />

<img alt="html-dom-api example 1 result" src="../code_sandbox/snaps/html-dom-api-01-result.png" />

- [x] **Outcome:** The paragraph content becomes **Hello World!** through the API.

<a id="html-dom-api-example-02"></a>

### **Example 2: document.getElementById(id)**

- [x] Finds **one** element whose `id` matches exactly (ids should be unique).
- [x] Pass the id **without** `#`. `#demo` looks for an id that literally contains the hash.
- [x] Return type: Element or **`null`**.

Sandbox: `code_sandbox/html-dom-api/getelementbyid.html`

```html
<p id="intro">Found me</p>
<script>
const el = document.getElementById("intro");
</script>
```

<img alt="html-dom-api example 2 source" src="../code_sandbox/snaps/html-dom-api-02-code.png" />

<img alt="html-dom-api example 2 result" src="../code_sandbox/snaps/html-dom-api-02-result.png" />

- [x] **Outcome:** `getElementById("intro")` returns the paragraph; its text is **Found me**.

<a id="html-dom-api-example-03"></a>

### **Example 3: document.getElementsByTagName(name)**

- [x] Returns a **live HTMLCollection** of every element with that tag (`"p"`, `"div"`, `"*"`).
- [x] Index it like an array: `list[0]`. Use `.length`. It is **not** a real Array (no `map` unless you convert).
- [x] **Live** means if you add another `<p>` later, the collection grows.

Sandbox: `code_sandbox/html-dom-api/getelementsbytagname.html`

```html
<p>One</p><p>Two</p>
<script>
const list = document.getElementsByTagName("p");
</script>
```

<img alt="html-dom-api example 3 source" src="../code_sandbox/snaps/html-dom-api-03-code.png" />

<img alt="html-dom-api example 3 result" src="../code_sandbox/snaps/html-dom-api-03-result.png" />

- [x] **Outcome:** `getElementsByTagName("p")` finds the demo paragraphs (length at least **2**).

<a id="html-dom-api-example-04"></a>

### **Example 4: document.getElementsByClassName(name)**

- [x] Finds elements that have that **class** (not id, not tag).
- [x] Class name only: `"intro"`, not `".intro"`.
- [x] Also returns a live HTMLCollection. An element with several classes still matches if it includes this one.

Sandbox: `code_sandbox/html-dom-api/getelementsbyclassname.html`

```html
<p class="intro">A</p><p>B</p><p class="intro">C</p>
<script>
const x = document.getElementsByClassName("intro");
</script>
```

<img alt="html-dom-api example 4 source" src="../code_sandbox/snaps/html-dom-api-04-code.png" />

<img alt="html-dom-api example 4 result" src="../code_sandbox/snaps/html-dom-api-04-result.png" />

- [x] **Outcome:** Two `.intro` paragraphs are found; the middle `B` is skipped.

<a id="html-dom-api-example-05"></a>

### **Example 5: document.querySelector(selector)**

- [x] Uses a **CSS selector**. Returns the **first** match only, or `null`.
- [x] Class: `".demo"`. Id: `"#intro"`. Tag: `"p"`. Compound: `"p.intro"`.
- [x] This is the modern one-element lookup when you do not have a unique id.

Sandbox: `code_sandbox/html-dom-api/queryselector.html`

```html
<p class="note">Hello World!</p>
<script>
const myPara = document.querySelector(".note");
myPara.innerHTML = "Hello World!";
</script>
```

<img alt="html-dom-api example 5 source" src="../code_sandbox/snaps/html-dom-api-05-code.png" />

<img alt="html-dom-api example 5 result" src="../code_sandbox/snaps/html-dom-api-05-result.png" />

- [x] **Outcome:** `querySelector(".note")` selects the first matching paragraph.

<a id="html-dom-api-example-06"></a>

### **Example 6: document.querySelectorAll(selector)**

- [x] Returns a **static NodeList** of **all** matches (not live like HTMLCollection).
- [x] You can `.forEach` a NodeList in modern browsers.
- [x] Use this when you need every `.item` or every `p.intro`, not just the first.

Sandbox: `code_sandbox/html-dom-api/queryselectorall.html`

```html
<p class="item">One</p><p class="item">Two</p>
<script>
const myItems = document.querySelectorAll(".item");
myItems[0].innerHTML = "First";
</script>
```

<img alt="html-dom-api example 6 source" src="../code_sandbox/snaps/html-dom-api-06-code.png" />

<img alt="html-dom-api example 6 result" src="../code_sandbox/snaps/html-dom-api-06-result.png" />

- [x] **Outcome:** The first `.item` becomes **First**; the second stays **Two**.

<a id="html-dom-api-example-07"></a>

### **Example 7: element.innerHTML**

- [x] Gets or sets the element’s **HTML** as a string, including tags.
- [x] Assigning HTML **parses** tags: `"<b>Hi</b>"` creates a `<b>` child.
- [x] Do not put untrusted user text into `innerHTML` (XSS). Prefer `textContent` for plain text.

Sandbox: `code_sandbox/html-dom-api/innerhtml-prop.html`

```html
<p id="box"><b>Hi</b></p>
<script>
const html = document.getElementById("box").innerHTML;
</script>
```

<img alt="html-dom-api example 7 source" src="../code_sandbox/snaps/html-dom-api-07-code.png" />

<img alt="html-dom-api example 7 result" src="../code_sandbox/snaps/html-dom-api-07-result.png" />

- [x] **Outcome:** `innerHTML` includes the **`<b>`** markup, not only the word Hi.

<a id="html-dom-api-example-08"></a>

### **Example 8: element.textContent**

- [x] Gets or sets **plain text**. Tags in the string are shown as characters, not parsed.
- [x] Faster and safer than `innerHTML` when you only need words.
- [x] It concatenates all descendant text nodes (hidden elements included).

Sandbox: `code_sandbox/html-dom-api/textcontent-prop.html`

```html
<p id="box"><b>Hi</b></p>
<script>
const t = document.getElementById("box").textContent;
</script>
```

<img alt="html-dom-api example 8 source" src="../code_sandbox/snaps/html-dom-api-08-code.png" />

<img alt="html-dom-api example 8 result" src="../code_sandbox/snaps/html-dom-api-08-result.png" />

- [x] **Outcome:** `textContent` is **Hi** (no tags). Assigning `<i>x</i>` would show the angle brackets as text.

<a id="html-dom-api-example-09"></a>

### **Example 9: element.attribute — change src, href, id…**

- [x] Many HTML attributes are exposed as **properties**: `img.src`, `a.href`, `input.value`.
- [x] `img.src` is usually the **resolved absolute URL**, not the raw attribute string.
- [x] Use `getAttribute` when you need the original markup value.

Sandbox: `code_sandbox/html-dom-api/element-attribute.html`

```html
<a id="n" href="next.html">next</a>
<script>
document.getElementById("n").href = "https://example.com";
</script>
```

<img alt="html-dom-api example 9 source" src="../code_sandbox/snaps/html-dom-api-09-code.png" />

<img alt="html-dom-api example 9 result" src="../code_sandbox/snaps/html-dom-api-09-result.png" />

- [x] **Outcome:** The link’s `href` property is updated to **https://example.com/** (browser may add a trailing slash).

<a id="html-dom-api-example-10"></a>

### **Example 10: element.style.property**

- [x] `element.style` is a **CSSStyleDeclaration** for **inline** styles only.
- [x] JS names are camelCase: `style.backgroundColor = "gold"`.
- [x] Reading `style.color` does **not** see stylesheet rules — only inline. Use `getComputedStyle` for the used value.

Sandbox: `code_sandbox/html-dom-api/element-style-property.html`

```html
<p id="p">Hello</p>
<script>
document.getElementById("p").style.color = "blue";
</script>
```

<img alt="html-dom-api example 10 source" src="../code_sandbox/snaps/html-dom-api-10-code.png" />

<img alt="html-dom-api example 10 result" src="../code_sandbox/snaps/html-dom-api-10-result.png" />

- [x] **Outcome:** Inline **color** is set; `style.color` reads back **blue** (or `rgb(0, 0, 255)` depending on the engine).

<a id="html-dom-api-example-11"></a>

### **Example 11: element.setAttribute()**

- [x] `setAttribute(name, value)` creates or replaces an HTML attribute as a **string**.
- [x] Works for any attribute, including `data-*` and ARIA names.
- [x] Boolean attributes: `setAttribute("disabled", "")` disables a control.

Sandbox: `code_sandbox/html-dom-api/setattribute.html`

```html
<button type="button" id="b">Go</button>
<script>
document.getElementById("b").setAttribute("disabled", "");
</script>
```

<img alt="html-dom-api example 11 source" src="../code_sandbox/snaps/html-dom-api-11-code.png" />

<img alt="html-dom-api example 11 result" src="../code_sandbox/snaps/html-dom-api-11-result.png" />

- [x] **Outcome:** The button is **disabled** after `setAttribute("disabled", "")`.

<a id="html-dom-api-example-12"></a>

### **Example 12: document.createElement()**

- [x] Creates an Element that is **off-tree** until you insert it.
- [x] Tag name is not case-sensitive in HTML: `"P"` and `"p"` both make a paragraph.
- [x] Set properties before append if you want to avoid a flash of empty content.

Sandbox: `code_sandbox/html-dom-api/createelement.html`

```html
<div id="host"></div>
<script>
const p = document.createElement("p");
p.textContent = "created";
document.getElementById("host").appendChild(p);
</script>
```

<img alt="html-dom-api example 12 source" src="../code_sandbox/snaps/html-dom-api-12-code.png" />

<img alt="html-dom-api example 12 result" src="../code_sandbox/snaps/html-dom-api-12-result.png" />

- [x] **Outcome:** A new `<p>created</p>` is in the document after `createElement` + `appendChild`.

<a id="html-dom-api-example-13"></a>

### **Example 13: document.appendChild() / parent.appendChild()**

- [x] W3Schools lists `document.appendChild` in the table; you almost always call it on a **parent element**.
- [x] If the node is already in the tree, `appendChild` **moves** it (it does not copy).
- [x] Returns the appended node.

Sandbox: `code_sandbox/html-dom-api/appendchild.html`

```html
<div id="host"></div>
<script>
const span = document.createElement("span");
span.textContent = "appended";
document.getElementById("host").appendChild(span);
</script>
```

<img alt="html-dom-api example 13 source" src="../code_sandbox/snaps/html-dom-api-13-code.png" />

<img alt="html-dom-api example 13 result" src="../code_sandbox/snaps/html-dom-api-13-result.png" />

- [x] **Outcome:** **appended** is the last child of `#host`.

<a id="html-dom-api-example-14"></a>

### **Example 14: parent.removeChild()**

- [x] Removes a **child** you already have a reference to. Throws if that node is not a child.
- [x] Modern alternative: `child.remove()` — no parent needed.
- [x] The removed node still exists in memory until you drop your variables; you can append it somewhere else.

Sandbox: `code_sandbox/html-dom-api/removechild.html`

```html
<div id="host"><span id="gone">x</span></div>
<script>
const host = document.getElementById("host");
host.removeChild(document.getElementById("gone"));
</script>
```

<img alt="html-dom-api example 14 source" src="../code_sandbox/snaps/html-dom-api-14-code.png" />

<img alt="html-dom-api example 14 result" src="../code_sandbox/snaps/html-dom-api-14-result.png" />

- [x] **Outcome:** `#host` is empty after `removeChild`. The snapshot reports **childCount=0**.

<a id="html-dom-api-example-15"></a>

### **Example 15: parent.replaceChild()**

- [x] `parent.replaceChild(newNode, oldNode)` swaps them. `oldNode` must already be a child.
- [x] Returns the replaced (old) node.
- [x] `oldNode.replaceWith(newNode)` is the newer element method.

Sandbox: `code_sandbox/html-dom-api/replacechild.html`

```html
<div id="host"><span id="old">old</span></div>
<script>
const neu = document.createElement("strong");
neu.textContent = "new";
document.getElementById("host").replaceChild(neu, document.getElementById("old"));
</script>
```

<img alt="html-dom-api example 15 source" src="../code_sandbox/snaps/html-dom-api-15-code.png" />

<img alt="html-dom-api example 15 result" src="../code_sandbox/snaps/html-dom-api-15-result.png" />

- [x] **Outcome:** The span is replaced by **`<strong>new</strong>`**.

<a id="html-dom-api-example-16"></a>

### **Example 16: element.onclick = function(){…}**

- [x] Assigning `onclick` sets **one** handler. A second assignment **overwrites** the first.
- [x] `addEventListener("click", …)` is preferred because you can add many listeners.
- [x] The W3Schools table writes `document.getElementById(id).onclick = function(){code}`.

Sandbox: `code_sandbox/html-dom-api/onclick-handler.html`

```html
<button type="button" id="myBtn">Click</button>
<script>
document.getElementById("myBtn").onclick = function () {
  document.getElementById("demo").innerText = "clicked";
};
</script>
```

<img alt="html-dom-api example 16 source" src="../code_sandbox/snaps/html-dom-api-16-code.png" />

<img alt="html-dom-api example 16 result" src="../code_sandbox/snaps/html-dom-api-16-result.png" />

- [x] **Outcome:** The sandbox clicks the button: the handler runs and prints **clicked**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/html-dom-api/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is a DOM API method vs a property?

<details>
<summary>Answer</summary>

- [x] A **method** is an action you call (`getElementById()`). A **property** is a value (`innerHTML`).

</details>

### Question 2: What does `getElementById` return when the id is missing?

<details>
<summary>Answer</summary>

- [x] **`null`**.

</details>

### Question 3: Does `querySelector(".item")` return every match?

<details>
<summary>Answer</summary>

- [x] No — only the **first**. Use `querySelectorAll` for all.

</details>

### Question 4: Is `getElementsByTagName` live?

<details>
<summary>Answer</summary>

- [x] Yes — HTMLCollection updates when matching elements are added or removed.

</details>

### Question 5: Why prefer `textContent` for user-supplied words?

<details>
<summary>Answer</summary>

- [x] It does not parse HTML, so it avoids **XSS** from tags in the string.

</details>

### Question 6: Does `element.style.color` show stylesheet rules?

<details>
<summary>Answer</summary>

- [x] No — only **inline** styles. Use `getComputedStyle` for the used value.

</details>

### Question 7: What does `setAttribute("disabled", "")` do on a button?

<details>
<summary>Answer</summary>

- [x] It adds the boolean **disabled** attribute so the button cannot be clicked.

</details>

### Question 8: Does `appendChild` copy a node that is already in the tree?

<details>
<summary>Answer</summary>

- [x] No — it **moves** that node to the new parent.

</details>

### Question 9: What is the pitfall of `onclick = fn`?

<details>
<summary>Answer</summary>

- [x] A later assignment **replaces** the previous handler. `addEventListener` stacks them.

</details>

### Question 10: Where do you start to reach any element?

<details>
<summary>Answer</summary>

- [x] The **`document`** object (or `window.document`).

</details>


</details>

## Summary

Start at `document`, select a node, then use properties (`innerHTML`, `style`) or methods (`setAttribute`, `appendChild`).

## References

- [HTML DOM API](https://www.w3schools.com/js/js_htmldom_methods.asp)
- [MDN Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)
