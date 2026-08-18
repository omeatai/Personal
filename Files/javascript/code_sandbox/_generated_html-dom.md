<details>
  <summary>HTML DOM</summary>

## Introduction

The HTML DOM is the browser’s tree of nodes for a page. JavaScript uses that tree to read and change HTML.

This section has **11** examples:

- [x] **Example 1:** Document node — owner of the tree [View](#html-dom-example-01)
- [x] **Example 2:** Element nodes — html, body, headings, tags [View](#html-dom-example-02)
- [x] **Example 3:** Attribute node — href on a link [View](#html-dom-example-03)
- [x] **Example 4:** Text node — the words inside a heading [View](#html-dom-example-04)
- [x] **Example 5:** Access an element by id and set innerHTML [View](#html-dom-example-05)
- [x] **Example 6:** id is HTML, getElementById is a method, innerHTML is a property [View](#html-dom-example-06)
- [x] **Example 7:** What you will learn — change element content [View](#html-dom-example-07)
- [x] **Example 8:** What you will learn — change CSS from JavaScript [View](#html-dom-example-08)
- [x] **Example 9:** What you will learn — add and delete elements [View](#html-dom-example-09)
- [x] **Example 10:** What you will learn — react to events [View](#html-dom-example-10)
- [x] **Example 11:** W3C DOM: Core, XML, and HTML [View](#html-dom-example-11)

## Detailed Explanation

- [x] Document / Element / Attribute / Text are different **node types**.
- [x] `getElementById` + `innerHTML` is the first practical access pattern.
- [x] The DOM is a W3C/WHATWG standard (**Core**, **XML**, **HTML** parts).

<a id="html-dom-example-01"></a>

### **Example 1: Document node — owner of the tree**

- [x] When a page loads, the browser builds a **DOM tree**. The **Document** node owns every other node.
- [x] `document` is that object. It is not an HTML tag; it is the programming model of the page.
- [x] `document.nodeType` is **9** (`DOCUMENT_NODE`). `document.nodeName` is **`#document`**.
- [x] You always start from `document` when you look up elements, create nodes, or change the page.

Sandbox: `code_sandbox/html-dom/document-node.html`

```html
<p id="demo"></p>
<script>
document.getElementById("demo").innerText =
  "nodeType=" + document.nodeType +
  " nodeName=" + document.nodeName;
</script>
```

<img alt="html-dom example 1 source" src="./code_sandbox/snaps/html-dom-01-code.png" />

<img alt="html-dom example 1 result" src="./code_sandbox/snaps/html-dom-01-result.png" />

- [x] **Outcome:** The running page prints **nodeType=9 nodeName=#document** — the Document is the tree owner.

<a id="html-dom-example-02"></a>

### **Example 2: Element nodes — html, body, headings, tags**

- [x] Most visible parts of a page are **Element** nodes: `<html>`, `<body>`, `<h1>`, `<p>`, `<a>`.
- [x] Element `nodeType` is **1**. `nodeName` is the tag name in **uppercase** (`P`, `H1`).
- [x] Elements can nest: the `<html>` element contains `<head>` and `<body>`, which contain more elements.
- [x] Selecting an element with `getElementById` returns that Element object so you can read or change it.

Sandbox: `code_sandbox/html-dom/element-nodes.html`

```html
<h1 id="hdr">My Header</h1>
<p id="intro">Hello</p>
<script>
const h = document.getElementById("hdr");
const p = document.getElementById("intro");
document.getElementById("demo").innerText =
  h.nodeName + " type=" + h.nodeType + "\n" +
  p.nodeName + " type=" + p.nodeType;
</script>
```

<img alt="html-dom example 2 source" src="./code_sandbox/snaps/html-dom-02-code.png" />

<img alt="html-dom example 2 result" src="./code_sandbox/snaps/html-dom-02-result.png" />

- [x] **Outcome:** **H1 type=1** and **P type=1** — both are Element nodes.

<a id="html-dom-example-03"></a>

### **Example 3: Attribute node — href on a link**

- [x] Attributes such as `href`, `id`, and `src` live on elements as **attribute nodes** (or as properties).
- [x] `element.getAttribute("href")` reads the HTML attribute string.
- [x] `element.attributes` is a NamedNodeMap of those attributes.
- [x] Changing `a.href` (or `setAttribute`) updates the live link the browser uses.

Sandbox: `code_sandbox/html-dom/attribute-node.html`

```html
<a id="w3" href="https://www.w3schools.com">W3Schools</a>
<script>
const a = document.getElementById("w3");
document.getElementById("demo").innerText =
  "href=" + a.getAttribute("href") + "\n" +
  "attrCount=" + a.attributes.length;
</script>
```

<img alt="html-dom example 3 source" src="./code_sandbox/snaps/html-dom-03-code.png" />

<img alt="html-dom example 3 result" src="./code_sandbox/snaps/html-dom-03-result.png" />

- [x] **Outcome:** The link reports **href=https://www.w3schools.com** and at least two attributes (`id` and `href`).

<a id="html-dom-example-04"></a>

### **Example 4: Text node — the words inside a heading**

- [x] The words **My Header** in `<h1>My Header</h1>` are a **Text** node, not the heading element itself.
- [x] Text `nodeType` is **3**. `nodeName` is **`#text`**. `nodeValue` is the actual string.
- [x] `element.firstChild` is often that text node (watch out for extra whitespace text nodes).
- [x] `textContent` / `innerText` walk text nodes for you so you rarely touch them directly.

Sandbox: `code_sandbox/html-dom/text-node.html`

```html
<h1 id="hdr">My Header</h1>
<script>
const t = document.getElementById("hdr").firstChild;
document.getElementById("demo").innerText =
  t.nodeName + " type=" + t.nodeType + " value=" + JSON.stringify(t.nodeValue);
</script>
```

<img alt="html-dom example 4 source" src="./code_sandbox/snaps/html-dom-04-code.png" />

<img alt="html-dom example 4 result" src="./code_sandbox/snaps/html-dom-04-result.png" />

- [x] **Outcome:** The heading’s first child is a Text node whose value is **My Header**.

<a id="html-dom-example-05"></a>

### **Example 5: Access an element by id and set innerHTML**

- [x] The usual lookup is **`document.getElementById("demo")`**. The argument is the **id string**, not `#demo`.
- [x] If the element exists you get an object; if not, you get **`null`** (calling methods on null throws).
- [x] **`innerHTML`** is a property: assign a string and the browser parses it as HTML inside that element.
- [x] On the W3Schools page: `id="demo"` is HTML, `getElementById()` is a **DOM method**, `innerHTML` is a **DOM property**.

Sandbox: `code_sandbox/html-dom/getelementbyid-innerhtml.html`

```html
<p id="hello"></p>
<script>
const myPara = document.getElementById("hello");
myPara.innerHTML = "Hello World!";
</script>
```

<img alt="html-dom example 5 source" src="./code_sandbox/snaps/html-dom-05-code.png" />

<img alt="html-dom example 5 result" src="./code_sandbox/snaps/html-dom-05-result.png" />

- [x] **Outcome:** The empty paragraph is filled with **Hello World!**.

<a id="html-dom-example-06"></a>

### **Example 6: id is HTML, getElementById is a method, innerHTML is a property**

- [x] **HTML property:** `id="demo"` is written in the markup so the browser can find the node.
- [x] **DOM method:** `getElementById` is a **function** you call on `document` — notice the `()`.
- [x] **DOM property:** `innerHTML` is a **value** you read or assign — no parentheses.
- [x] Mixing these up is a common beginner error: `getElementById.innerHTML` is wrong; you need the returned element first.

Sandbox: `code_sandbox/html-dom/id-method-property.html`

```html
<p id="demo-box">old</p>
<script>
const el = document.getElementById("demo-box");
el.innerHTML = "Hello World!";
</script>
```

<img alt="html-dom example 6 source" src="./code_sandbox/snaps/html-dom-06-code.png" />

<img alt="html-dom example 6 result" src="./code_sandbox/snaps/html-dom-06-result.png" />

- [x] **Outcome:** The markup id, the lookup method, and the innerHTML property work together: the box now says **Hello World!**.

<a id="html-dom-example-07"></a>

### **Example 7: What you will learn — change element content**

- [x] Later chapters change **content** (`innerHTML`, `textContent`) after the page has loaded.
- [x] That is how clocks, counters, and error messages appear without a full reload.
- [x] You look the element up, then assign a new string. The DOM updates immediately.

Sandbox: `code_sandbox/html-dom/change-content-preview.html`

```html
<p id="msg">Waiting…</p>
<script>
document.getElementById("msg").textContent = "Content updated with the DOM.";
</script>
```

<img alt="html-dom example 7 source" src="./code_sandbox/snaps/html-dom-07-code.png" />

<img alt="html-dom example 7 result" src="./code_sandbox/snaps/html-dom-07-result.png" />

- [x] **Outcome:** The paragraph switches from **Waiting…** to **Content updated with the DOM.**

<a id="html-dom-example-08"></a>

### **Example 8: What you will learn — change CSS from JavaScript**

- [x] `element.style.color = "blue"` writes an **inline** style on that one element.
- [x] The CSS property in JS is **camelCase**: `backgroundColor`, not `background-color`.
- [x] You will also hide, move, and animate elements this way in later pages.

Sandbox: `code_sandbox/html-dom/change-style-preview.html`

```html
<p id="p2">Hello World!</p>
<script>
document.getElementById("p2").style.color = "blue";
</script>
```

<img alt="html-dom example 8 source" src="./code_sandbox/snaps/html-dom-08-code.png" />

<img alt="html-dom example 8 result" src="./code_sandbox/snaps/html-dom-08-result.png" />

- [x] **Outcome:** The paragraph is drawn in **blue** via `style.color`.

<a id="html-dom-example-09"></a>

### **Example 9: What you will learn — add and delete elements**

- [x] `document.createElement("p")` builds a new Element that is **not** on the page yet.
- [x] `parent.appendChild(node)` inserts it. `parent.removeChild(node)` (or `node.remove()`) takes it out.
- [x] This is how lists, toasts, and extra form fields appear and disappear.

Sandbox: `code_sandbox/html-dom/add-delete-preview.html`

```html
<div id="box"></div>
<script>
const p = document.createElement("p");
p.textContent = "I was created with createElement.";
document.getElementById("box").appendChild(p);
</script>
```

<img alt="html-dom example 9 source" src="./code_sandbox/snaps/html-dom-09-code.png" />

<img alt="html-dom example 9 result" src="./code_sandbox/snaps/html-dom-09-result.png" />

- [x] **Outcome:** A new paragraph is appended into `#box` and is visible on the page.

<a id="html-dom-example-10"></a>

### **Example 10: What you will learn — react to events**

- [x] The DOM can run your function when the user **clicks**, types, or when the page **loads**.
- [x] HTML can use attributes such as `onclick="..."`. Modern code prefers `addEventListener`.
- [x] Events are covered in the **JS HTML Events** group after this DOM group.

Sandbox: `code_sandbox/html-dom/events-preview.html`

```html
<button type="button" id="btn">Click me</button>
<p id="out"></p>
<script>
document.getElementById("btn").onclick = function () {
  document.getElementById("out").textContent = "Clicked!";
};
</script>
```

<img alt="html-dom example 10 source" src="./code_sandbox/snaps/html-dom-10-code.png" />

<img alt="html-dom example 10 result" src="./code_sandbox/snaps/html-dom-10-result.png" />

- [x] **Outcome:** The script clicks the button for the snapshot: **Clicked!** appears.

<a id="html-dom-example-11"></a>

### **Example 11: W3C DOM: Core, XML, and HTML**

- [x] The DOM is a **W3C / WHATWG** standard: a language-neutral interface to read and update a document.
- [x] **Core DOM** — the shared model for all document types (nodes, trees).
- [x] **XML DOM** — the model for XML documents.
- [x] **HTML DOM** — the model for HTML documents, plus HTML-specific collections (`forms`, `images`).
- [x] JavaScript is the language browsers use to talk to that API — the API is not “JavaScript itself”.

Sandbox: `code_sandbox/html-dom/w3c-dom-parts.html`

```html
<script>
const parts = [
  "Core DOM — all document types",
  "XML DOM — XML documents",
  "HTML DOM — HTML documents"
];
document.getElementById("demo").innerText = parts.join("\n");
</script>
```

<img alt="html-dom example 11 source" src="./code_sandbox/snaps/html-dom-11-code.png" />

<img alt="html-dom example 11 result" src="./code_sandbox/snaps/html-dom-11-result.png" />

- [x] **Outcome:** The snapshot lists the three W3C DOM parts: **Core**, **XML**, and **HTML**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/html-dom/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What `nodeType` is the Document object?

<details>
<summary>Answer</summary>

- [x] **9** (`DOCUMENT_NODE`). `nodeName` is `#document`.

</details>

### Question 2: What `nodeType` is an Element such as `<p>`?

<details>
<summary>Answer</summary>

- [x] **1**. `nodeName` is the uppercase tag (`P`).

</details>

### Question 3: Where do the words inside `<h1>My Header</h1>` live?

<details>
<summary>Answer</summary>

- [x] In a **Text** node (`nodeType` **3**) that is usually `h1.firstChild`.

</details>

### Question 4: How do you look up `id="demo"`?

<details>
<summary>Answer</summary>

- [x] `document.getElementById("demo")` — **no** `#` in the argument.

</details>

### Question 5: What happens if the id does not exist?

<details>
<summary>Answer</summary>

- [x] The method returns **`null`**. Using `.innerHTML` on it throws **TypeError**.

</details>

### Question 6: Is `innerHTML` a method or a property?

<details>
<summary>Answer</summary>

- [x] A **property**. You assign a string; you do not call `innerHTML()`.

</details>

### Question 7: How do you add a brand-new paragraph?

<details>
<summary>Answer</summary>

- [x] `document.createElement("p")`, set its text, then `parent.appendChild(p)`.

</details>

### Question 8: What are the three W3C DOM parts?

<details>
<summary>Answer</summary>

- [x] **Core DOM**, **XML DOM**, and **HTML DOM**.

</details>

### Question 9: Does changing `style.color` edit the stylesheet file?

<details>
<summary>Answer</summary>

- [x] No. It sets an **inline** style on that one element.

</details>

### Question 10: Why start from `document` every time?

<details>
<summary>Answer</summary>

- [x] The Document **owns** the tree; lookups and `createElement` are methods on it (or on elements).

</details>


</details>

## Summary

Treat the page as a tree: look up nodes from `document`, then change content, style, structure, or events.

## References

- [HTML DOM](https://www.w3schools.com/js/js_htmldom.asp)
- [MDN Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)

</details>
