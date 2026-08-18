"""S24: JS HTML DOM teaching pages (24.1–24.7). Reference catalogs are _build_s24_ref.py."""
from __future__ import annotations

from _dom_ui import P
from _gen_lib import build_and_snap

BASE = "https://www.w3schools.com/js/"


def qa(*items):
    return list(items)


# ---------------------------------------------------------------------------
# 24.1 HTML DOM
# ---------------------------------------------------------------------------

HTML_DOM = [
    P(
        "document-node",
        "Document node — owner of the tree",
        [
            "When a page loads, the browser builds a **DOM tree**. The **Document** node owns every other node.",
            "`document` is that object. It is not an HTML tag; it is the programming model of the page.",
            "`document.nodeType` is **9** (`DOCUMENT_NODE`). `document.nodeName` is **`#document`**.",
            "You always start from `document` when you look up elements, create nodes, or change the page.",
        ],
        """<p id="demo"></p>
<script>
document.getElementById("demo").innerText =
  "nodeType=" + document.nodeType +
  " nodeName=" + document.nodeName;
</script>""",
        "The running page prints **nodeType=9 nodeName=#document** — the Document is the tree owner.",
        body='<p>The HTML DOM is a tree of nodes that represents this page.</p>',
        js="""      document.getElementById("demo").innerText =
        "nodeType=" + document.nodeType + "\\n" +
        "nodeName=" + document.nodeName;""",
    ),
    P(
        "element-nodes",
        "Element nodes — html, body, headings, tags",
        [
            "Most visible parts of a page are **Element** nodes: `<html>`, `<body>`, `<h1>`, `<p>`, `<a>`.",
            "Element `nodeType` is **1**. `nodeName` is the tag name in **uppercase** (`P`, `H1`).",
            "Elements can nest: the `<html>` element contains `<head>` and `<body>`, which contain more elements.",
            "Selecting an element with `getElementById` returns that Element object so you can read or change it.",
        ],
        """<h1 id="hdr">My Header</h1>
<p id="intro">Hello</p>
<script>
const h = document.getElementById("hdr");
const p = document.getElementById("intro");
document.getElementById("demo").innerText =
  h.nodeName + " type=" + h.nodeType + "\\n" +
  p.nodeName + " type=" + p.nodeType;
</script>""",
        "**H1 type=1** and **P type=1** — both are Element nodes.",
        body='<h1 id="hdr">My Header</h1><p id="intro">Hello</p>',
        js="""      const h = document.getElementById("hdr");
      const p = document.getElementById("intro");
      document.getElementById("demo").innerText =
        h.nodeName + " type=" + h.nodeType + "\\n" +
        p.nodeName + " type=" + p.nodeType;""",
    ),
    P(
        "attribute-node",
        "Attribute node — href on a link",
        [
            "Attributes such as `href`, `id`, and `src` live on elements as **attribute nodes** (or as properties).",
            "`element.getAttribute(\"href\")` reads the HTML attribute string.",
            "`element.attributes` is a NamedNodeMap of those attributes.",
            "Changing `a.href` (or `setAttribute`) updates the live link the browser uses.",
        ],
        """<a id="w3" href="https://www.w3schools.com">W3Schools</a>
<script>
const a = document.getElementById("w3");
document.getElementById("demo").innerText =
  "href=" + a.getAttribute("href") + "\\n" +
  "attrCount=" + a.attributes.length;
</script>""",
        "The link reports **href=https://www.w3schools.com** and at least two attributes (`id` and `href`).",
        body='<a id="w3" href="https://www.w3schools.com">W3Schools</a>',
        js="""      const a = document.getElementById("w3");
      document.getElementById("demo").innerText =
        "href=" + a.getAttribute("href") + "\\n" +
        "attrCount=" + a.attributes.length + "\\n" +
        "names=" + Array.from(a.attributes).map(x => x.name).join(",");""",
    ),
    P(
        "text-node",
        "Text node — the words inside a heading",
        [
            "The words **My Header** in `<h1>My Header</h1>` are a **Text** node, not the heading element itself.",
            "Text `nodeType` is **3**. `nodeName` is **`#text`**. `nodeValue` is the actual string.",
            "`element.firstChild` is often that text node (watch out for extra whitespace text nodes).",
            "`textContent` / `innerText` walk text nodes for you so you rarely touch them directly.",
        ],
        """<h1 id="hdr">My Header</h1>
<script>
const t = document.getElementById("hdr").firstChild;
document.getElementById("demo").innerText =
  t.nodeName + " type=" + t.nodeType + " value=" + JSON.stringify(t.nodeValue);
</script>""",
        "The heading’s first child is a Text node whose value is **My Header**.",
        body='<h1 id="hdr">My Header</h1>',
        js="""      const t = document.getElementById("hdr").firstChild;
      document.getElementById("demo").innerText =
        t.nodeName + " type=" + t.nodeType +
        " value=" + JSON.stringify(t.nodeValue);""",
    ),
    P(
        "getelementbyid-innerhtml",
        "Access an element by id and set innerHTML",
        [
            "The usual lookup is **`document.getElementById(\"demo\")`**. The argument is the **id string**, not `#demo`.",
            "If the element exists you get an object; if not, you get **`null`** (calling methods on null throws).",
            "**`innerHTML`** is a property: assign a string and the browser parses it as HTML inside that element.",
            "On the W3Schools page: `id=\"demo\"` is HTML, `getElementById()` is a **DOM method**, `innerHTML` is a **DOM property**.",
        ],
        """<p id="hello"></p>
<script>
const myPara = document.getElementById("hello");
myPara.innerHTML = "Hello World!";
</script>""",
        "The empty paragraph is filled with **Hello World!**.",
        body='<p id="hello"></p>',
        js="""      const myPara = document.getElementById("hello");
      myPara.innerHTML = "Hello World!";
      document.getElementById("demo").innerText = "innerHTML is now: " + myPara.innerHTML;""",
    ),
    P(
        "id-method-property",
        "id is HTML, getElementById is a method, innerHTML is a property",
        [
            "**HTML property:** `id=\"demo\"` is written in the markup so the browser can find the node.",
            "**DOM method:** `getElementById` is a **function** you call on `document` — notice the `()`.",
            "**DOM property:** `innerHTML` is a **value** you read or assign — no parentheses.",
            "Mixing these up is a common beginner error: `getElementById.innerHTML` is wrong; you need the returned element first.",
        ],
        """<p id="demo-box">old</p>
<script>
const el = document.getElementById("demo-box");
el.innerHTML = "Hello World!";
</script>""",
        "The markup id, the lookup method, and the innerHTML property work together: the box now says **Hello World!**.",
        body='<p id="demo-box">old</p>',
        js="""      const el = document.getElementById("demo-box");
      el.innerHTML = "Hello World!";
      document.getElementById("demo").innerText =
        "id=" + el.id + "\\n" +
        "typeof getElementById=" + typeof document.getElementById + "\\n" +
        "innerHTML=" + el.innerHTML;""",
    ),
    P(
        "change-content-preview",
        "What you will learn — change element content",
        [
            "Later chapters change **content** (`innerHTML`, `textContent`) after the page has loaded.",
            "That is how clocks, counters, and error messages appear without a full reload.",
            "You look the element up, then assign a new string. The DOM updates immediately.",
        ],
        """<p id="msg">Waiting…</p>
<script>
document.getElementById("msg").textContent = "Content updated with the DOM.";
</script>""",
        "The paragraph switches from **Waiting…** to **Content updated with the DOM.**",
        body='<p id="msg">Waiting…</p>',
        js="""      document.getElementById("msg").textContent = "Content updated with the DOM.";
      document.getElementById("demo").innerText = document.getElementById("msg").textContent;""",
    ),
    P(
        "change-style-preview",
        "What you will learn — change CSS from JavaScript",
        [
            "`element.style.color = \"blue\"` writes an **inline** style on that one element.",
            "The CSS property in JS is **camelCase**: `backgroundColor`, not `background-color`.",
            "You will also hide, move, and animate elements this way in later pages.",
        ],
        """<p id="p2">Hello World!</p>
<script>
document.getElementById("p2").style.color = "blue";
</script>""",
        "The paragraph is drawn in **blue** via `style.color`.",
        body='<p id="p2">Hello World!</p>',
        js="""      const p = document.getElementById("p2");
      p.style.color = "blue";
      document.getElementById("demo").innerText = "color=" + p.style.color;""",
    ),
    P(
        "add-delete-preview",
        "What you will learn — add and delete elements",
        [
            "`document.createElement(\"p\")` builds a new Element that is **not** on the page yet.",
            "`parent.appendChild(node)` inserts it. `parent.removeChild(node)` (or `node.remove()`) takes it out.",
            "This is how lists, toasts, and extra form fields appear and disappear.",
        ],
        """<div id="box"></div>
<script>
const p = document.createElement("p");
p.textContent = "I was created with createElement.";
document.getElementById("box").appendChild(p);
</script>""",
        "A new paragraph is appended into `#box` and is visible on the page.",
        body='<div id="box"></div>',
        js="""      const p = document.createElement("p");
      p.textContent = "I was created with createElement.";
      document.getElementById("box").appendChild(p);
      document.getElementById("demo").innerText = "childCount=" + document.getElementById("box").children.length;""",
    ),
    P(
        "events-preview",
        "What you will learn — react to events",
        [
            "The DOM can run your function when the user **clicks**, types, or when the page **loads**.",
            "HTML can use attributes such as `onclick=\"...\"`. Modern code prefers `addEventListener`.",
            "Events are covered in the **JS HTML Events** group after this DOM group.",
        ],
        """<button type="button" id="btn">Click me</button>
<p id="out"></p>
<script>
document.getElementById("btn").onclick = function () {
  document.getElementById("out").textContent = "Clicked!";
};
</script>""",
        "The script clicks the button for the snapshot: **Clicked!** appears.",
        body='<button type="button" id="btn">Click me</button><p id="out"></p>',
        js="""      document.getElementById("btn").onclick = function () {
        document.getElementById("out").textContent = "Clicked!";
      };
      document.getElementById("btn").click();
      document.getElementById("demo").innerText = document.getElementById("out").textContent;""",
    ),
    P(
        "w3c-dom-parts",
        "W3C DOM: Core, XML, and HTML",
        [
            "The DOM is a **W3C / WHATWG** standard: a language-neutral interface to read and update a document.",
            "**Core DOM** — the shared model for all document types (nodes, trees).",
            "**XML DOM** — the model for XML documents.",
            "**HTML DOM** — the model for HTML documents, plus HTML-specific collections (`forms`, `images`).",
            "JavaScript is the language browsers use to talk to that API — the API is not “JavaScript itself”.",
        ],
        """<script>
const parts = [
  "Core DOM — all document types",
  "XML DOM — XML documents",
  "HTML DOM — HTML documents"
];
document.getElementById("demo").innerText = parts.join("\\n");
</script>""",
        "The snapshot lists the three W3C DOM parts: **Core**, **XML**, and **HTML**.",
        body="<p>The HTML DOM is a language-independent W3C/WHATWG standard.</p>",
        js="""      document.getElementById("demo").innerText = [
        "Core DOM — all document types",
        "XML DOM — XML documents",
        "HTML DOM — HTML documents"
      ].join("\\n");""",
    ),
]

HTML_DOM_QA = qa(
    ("What `nodeType` is the Document object?", ["**9** (`DOCUMENT_NODE`). `nodeName` is `#document`."]),
    ("What `nodeType` is an Element such as `<p>`?", ["**1**. `nodeName` is the uppercase tag (`P`)."]),
    ("Where do the words inside `<h1>My Header</h1>` live?", ["In a **Text** node (`nodeType` **3**) that is usually `h1.firstChild`."]),
    ("How do you look up `id=\"demo\"`?", ["`document.getElementById(\"demo\")` — **no** `#` in the argument."]),
    ("What happens if the id does not exist?", ["The method returns **`null`**. Using `.innerHTML` on it throws **TypeError**."]),
    ("Is `innerHTML` a method or a property?", ["A **property**. You assign a string; you do not call `innerHTML()`."]),
    ("How do you add a brand-new paragraph?", ["`document.createElement(\"p\")`, set its text, then `parent.appendChild(p)`."]),
    ("What are the three W3C DOM parts?", ["**Core DOM**, **XML DOM**, and **HTML DOM**."]),
    ("Does changing `style.color` edit the stylesheet file?", ["No. It sets an **inline** style on that one element."]),
    ("Why start from `document` every time?", ["The Document **owns** the tree; lookups and `createElement` are methods on it (or on elements)."]),
)

# ---------------------------------------------------------------------------
# 24.2 HTML DOM API
# ---------------------------------------------------------------------------

HTML_DOM_API = [
    P(
        "api-hello",
        "DOM API — getElementById and innerHTML",
        [
            "The **DOM API** is the set of **methods** (actions) and **properties** (values) that change HTML.",
            "`document` is the HTML document object — the entry point.",
            "`getElementById(\"demo\")` is a **document method** that returns the element (or `null`).",
            "`innerHTML` is an **element property**. Assigning it replaces the element’s HTML content.",
        ],
        """<p id="hello"></p>
<script>
const myPara = document.getElementById("hello");
myPara.innerHTML = "Hello World!";
</script>""",
        "The paragraph content becomes **Hello World!** through the API.",
        body='<p id="hello"></p>',
        js="""      const myPara = document.getElementById("hello");
      myPara.innerHTML = "Hello World!";
      document.getElementById("demo").innerText = myPara.innerHTML;""",
    ),
    P(
        "getelementbyid",
        "document.getElementById(id)",
        [
            "Finds **one** element whose `id` matches exactly (ids should be unique).",
            "Pass the id **without** `#`. `#demo` looks for an id that literally contains the hash.",
            "Return type: Element or **`null`**.",
        ],
        """<p id="intro">Found me</p>
<script>
const el = document.getElementById("intro");
</script>""",
        "`getElementById(\"intro\")` returns the paragraph; its text is **Found me**.",
        body='<p id="intro">Found me</p>',
        js="""      const el = document.getElementById("intro");
      document.getElementById("demo").innerText =
        (el ? el.textContent : "null") + " / missing=" + (document.getElementById("nope") === null);""",
    ),
    P(
        "getelementsbytagname",
        "document.getElementsByTagName(name)",
        [
            "Returns a **live HTMLCollection** of every element with that tag (`\"p\"`, `\"div\"`, `\"*\"`).",
            "Index it like an array: `list[0]`. Use `.length`. It is **not** a real Array (no `map` unless you convert).",
            "**Live** means if you add another `<p>` later, the collection grows.",
        ],
        """<p>One</p><p>Two</p>
<script>
const list = document.getElementsByTagName("p");
</script>""",
        "`getElementsByTagName(\"p\")` finds the demo paragraphs (length at least **2**).",
        body="<p>One</p><p>Two</p>",
        js="""      const list = document.getElementsByTagName("p");
      document.getElementById("demo").innerText =
        "length=" + list.length + " first=" + list[0].textContent;""",
    ),
    P(
        "getelementsbyclassname",
        "document.getElementsByClassName(name)",
        [
            "Finds elements that have that **class** (not id, not tag).",
            "Class name only: `\"intro\"`, not `\".intro\"`.",
            "Also returns a live HTMLCollection. An element with several classes still matches if it includes this one.",
        ],
        """<p class="intro">A</p><p>B</p><p class="intro">C</p>
<script>
const x = document.getElementsByClassName("intro");
</script>""",
        "Two `.intro` paragraphs are found; the middle `B` is skipped.",
        body='<p class="intro">A</p><p>B</p><p class="intro">C</p>',
        js="""      const x = document.getElementsByClassName("intro");
      document.getElementById("demo").innerText =
        "length=" + x.length + " " + x[0].textContent + "," + x[1].textContent;""",
    ),
    P(
        "queryselector",
        "document.querySelector(selector)",
        [
            "Uses a **CSS selector**. Returns the **first** match only, or `null`.",
            "Class: `\".demo\"`. Id: `\"#intro\"`. Tag: `\"p\"`. Compound: `\"p.intro\"`.",
            "This is the modern one-element lookup when you do not have a unique id.",
        ],
        """<p class="note">Hello World!</p>
<script>
const myPara = document.querySelector(".note");
myPara.innerHTML = "Hello World!";
</script>""",
        "`querySelector(\".note\")` selects the first matching paragraph.",
        body='<p class="note">old</p><p class="note">also</p>',
        js="""      const myPara = document.querySelector(".note");
      myPara.innerHTML = "Hello World!";
      document.getElementById("demo").innerText = myPara.innerHTML + " (second still " + document.querySelectorAll(".note")[1].textContent + ")";""",
    ),
    P(
        "queryselectorall",
        "document.querySelectorAll(selector)",
        [
            "Returns a **static NodeList** of **all** matches (not live like HTMLCollection).",
            "You can `.forEach` a NodeList in modern browsers.",
            "Use this when you need every `.item` or every `p.intro`, not just the first.",
        ],
        """<p class="item">One</p><p class="item">Two</p>
<script>
const myItems = document.querySelectorAll(".item");
myItems[0].innerHTML = "First";
</script>""",
        "The first `.item` becomes **First**; the second stays **Two**.",
        body='<p class="item">One</p><p class="item">Two</p>',
        js="""      const myItems = document.querySelectorAll(".item");
      myItems[0].innerHTML = "First";
      document.getElementById("demo").innerText =
        myItems[0].innerHTML + " / " + myItems[1].innerHTML + " length=" + myItems.length;""",
    ),
    P(
        "innerhtml-prop",
        "element.innerHTML",
        [
            "Gets or sets the element’s **HTML** as a string, including tags.",
            "Assigning HTML **parses** tags: `\"<b>Hi</b>\"` creates a `<b>` child.",
            "Do not put untrusted user text into `innerHTML` (XSS). Prefer `textContent` for plain text.",
        ],
        """<p id="box"><b>Hi</b></p>
<script>
const html = document.getElementById("box").innerHTML;
</script>""",
        "`innerHTML` includes the **`<b>`** markup, not only the word Hi.",
        body='<p id="box"><b>Hi</b></p>',
        js="""      const el = document.getElementById("box");
      document.getElementById("demo").innerText = el.innerHTML;
      el.innerHTML = "<i>new</i>";
      document.getElementById("demo").innerText += "\\nafter=" + el.innerHTML;""",
    ),
    P(
        "textcontent-prop",
        "element.textContent",
        [
            "Gets or sets **plain text**. Tags in the string are shown as characters, not parsed.",
            "Faster and safer than `innerHTML` when you only need words.",
            "It concatenates all descendant text nodes (hidden elements included).",
        ],
        """<p id="box"><b>Hi</b></p>
<script>
const t = document.getElementById("box").textContent;
</script>""",
        "`textContent` is **Hi** (no tags). Assigning `<i>x</i>` would show the angle brackets as text.",
        body='<p id="box"><b>Hi</b></p>',
        js="""      const el = document.getElementById("box");
      document.getElementById("demo").innerText = "read=" + JSON.stringify(el.textContent);
      el.textContent = "<i>x</i>";
      document.getElementById("demo").innerText += "\\nafter innerHTML=" + el.innerHTML;""",
    ),
    P(
        "element-attribute",
        "element.attribute — change src, href, id…",
        [
            "Many HTML attributes are exposed as **properties**: `img.src`, `a.href`, `input.value`.",
            "`img.src` is usually the **resolved absolute URL**, not the raw attribute string.",
            "Use `getAttribute` when you need the original markup value.",
        ],
        """<a id="n" href="next.html">next</a>
<script>
document.getElementById("n").href = "https://example.com";
</script>""",
        "The link’s `href` property is updated to **https://example.com/** (browser may add a trailing slash).",
        body='<a id="n" href="next.html">next</a>',
        js="""      const a = document.getElementById("n");
      a.href = "https://example.com";
      document.getElementById("demo").innerText =
        "href=" + a.href + "\\nattr=" + a.getAttribute("href");""",
    ),
    P(
        "element-style-property",
        "element.style.property",
        [
            "`element.style` is a **CSSStyleDeclaration** for **inline** styles only.",
            "JS names are camelCase: `style.backgroundColor = \"gold\"`.",
            "Reading `style.color` does **not** see stylesheet rules — only inline. Use `getComputedStyle` for the used value.",
        ],
        """<p id="p">Hello</p>
<script>
document.getElementById("p").style.color = "blue";
</script>""",
        "Inline **color** is set; `style.color` reads back **blue** (or `rgb(0, 0, 255)` depending on the engine).",
        body='<p id="p">Hello</p>',
        js="""      const p = document.getElementById("p");
      p.style.color = "blue";
      document.getElementById("demo").innerText = "style.color=" + p.style.color;""",
    ),
    P(
        "setattribute",
        "element.setAttribute()",
        [
            "`setAttribute(name, value)` creates or replaces an HTML attribute as a **string**.",
            "Works for any attribute, including `data-*` and ARIA names.",
            "Boolean attributes: `setAttribute(\"disabled\", \"\")` disables a control.",
        ],
        """<button type="button" id="b">Go</button>
<script>
document.getElementById("b").setAttribute("disabled", "");
</script>""",
        "The button is **disabled** after `setAttribute(\"disabled\", \"\")`.",
        body='<button type="button" id="b">Go</button>',
        js="""      const b = document.getElementById("b");
      b.setAttribute("disabled", "");
      document.getElementById("demo").innerText =
        "has disabled=" + b.hasAttribute("disabled") + " disabledProp=" + b.disabled;""",
    ),
    P(
        "createelement",
        "document.createElement()",
        [
            "Creates an Element that is **off-tree** until you insert it.",
            "Tag name is not case-sensitive in HTML: `\"P\"` and `\"p\"` both make a paragraph.",
            "Set properties before append if you want to avoid a flash of empty content.",
        ],
        """<div id="host"></div>
<script>
const p = document.createElement("p");
p.textContent = "created";
document.getElementById("host").appendChild(p);
</script>""",
        "A new `<p>created</p>` is in the document after `createElement` + `appendChild`.",
        body='<div id="host"></div>',
        js="""      const p = document.createElement("p");
      p.textContent = "created";
      document.getElementById("host").appendChild(p);
      document.getElementById("demo").innerText = document.getElementById("host").innerHTML;""",
    ),
    P(
        "appendchild",
        "document.appendChild() / parent.appendChild()",
        [
            "W3Schools lists `document.appendChild` in the table; you almost always call it on a **parent element**.",
            "If the node is already in the tree, `appendChild` **moves** it (it does not copy).",
            "Returns the appended node.",
        ],
        """<div id="host"></div>
<script>
const span = document.createElement("span");
span.textContent = "appended";
document.getElementById("host").appendChild(span);
</script>""",
        "**appended** is the last child of `#host`.",
        body='<div id="host"></div>',
        js="""      const span = document.createElement("span");
      span.textContent = "appended";
      document.getElementById("host").appendChild(span);
      document.getElementById("demo").innerText = document.getElementById("host").textContent;""",
    ),
    P(
        "removechild",
        "parent.removeChild()",
        [
            "Removes a **child** you already have a reference to. Throws if that node is not a child.",
            "Modern alternative: `child.remove()` — no parent needed.",
            "The removed node still exists in memory until you drop your variables; you can append it somewhere else.",
        ],
        """<div id="host"><span id="gone">x</span></div>
<script>
const host = document.getElementById("host");
host.removeChild(document.getElementById("gone"));
</script>""",
        "`#host` is empty after `removeChild`. The snapshot reports **childCount=0**.",
        body='<div id="host"><span id="gone">x</span></div>',
        js="""      const host = document.getElementById("host");
      host.removeChild(document.getElementById("gone"));
      document.getElementById("demo").innerText = "childCount=" + host.childNodes.length;""",
    ),
    P(
        "replacechild",
        "parent.replaceChild()",
        [
            "`parent.replaceChild(newNode, oldNode)` swaps them. `oldNode` must already be a child.",
            "Returns the replaced (old) node.",
            "`oldNode.replaceWith(newNode)` is the newer element method.",
        ],
        """<div id="host"><span id="old">old</span></div>
<script>
const neu = document.createElement("strong");
neu.textContent = "new";
document.getElementById("host").replaceChild(neu, document.getElementById("old"));
</script>""",
        "The span is replaced by **`<strong>new</strong>`**.",
        body='<div id="host"><span id="old">old</span></div>',
        js="""      const neu = document.createElement("strong");
      neu.textContent = "new";
      document.getElementById("host").replaceChild(neu, document.getElementById("old"));
      document.getElementById("demo").innerText = document.getElementById("host").innerHTML;""",
    ),
    P(
        "onclick-handler",
        "element.onclick = function(){…}",
        [
            "Assigning `onclick` sets **one** handler. A second assignment **overwrites** the first.",
            "`addEventListener(\"click\", …)` is preferred because you can add many listeners.",
            "The W3Schools table writes `document.getElementById(id).onclick = function(){code}`.",
        ],
        """<button type="button" id="myBtn">Click</button>
<script>
document.getElementById("myBtn").onclick = function () {
  document.getElementById("demo").innerText = "clicked";
};
</script>""",
        "The sandbox clicks the button: the handler runs and prints **clicked**.",
        body='<button type="button" id="myBtn">Click</button>',
        js="""      document.getElementById("myBtn").onclick = function () {
        document.getElementById("demo").innerText = "clicked";
      };
      document.getElementById("myBtn").click();""",
    ),
]

HTML_DOM_API_QA = qa(
    ("What is a DOM API method vs a property?", ["A **method** is an action you call (`getElementById()`). A **property** is a value (`innerHTML`)."]),
    ("What does `getElementById` return when the id is missing?", ["**`null`**."]),
    ("Does `querySelector(\".item\")` return every match?", ["No — only the **first**. Use `querySelectorAll` for all."]),
    ("Is `getElementsByTagName` live?", ["Yes — HTMLCollection updates when matching elements are added or removed."]),
    ("Why prefer `textContent` for user-supplied words?", ["It does not parse HTML, so it avoids **XSS** from tags in the string."]),
    ("Does `element.style.color` show stylesheet rules?", ["No — only **inline** styles. Use `getComputedStyle` for the used value."]),
    ("What does `setAttribute(\"disabled\", \"\")` do on a button?", ["It adds the boolean **disabled** attribute so the button cannot be clicked."]),
    ("Does `appendChild` copy a node that is already in the tree?", ["No — it **moves** that node to the new parent."]),
    ("What is the pitfall of `onclick = fn`?", ["A later assignment **replaces** the previous handler. `addEventListener` stacks them."]),
    ("Where do you start to reach any element?", ["The **`document`** object (or `window.document`)."]),
)

# ---------------------------------------------------------------------------
# 24.3 Selecting Elements
# ---------------------------------------------------------------------------

SELECTING = [
    P(
        "find-by-id",
        "Finding HTML Element by Id",
        [
            "Easiest lookup: **`document.getElementById(\"intro\")`**.",
            "Ids must be unique in the document. Duplicate ids make this method return the **first** one.",
            "If found, you get the element object. If not, **`null`**.",
        ],
        """<p id="intro">Intro paragraph</p>
<script>
const element = document.getElementById("intro");
</script>""",
        "`element` is the intro paragraph; a missing id returns **null**.",
        body='<p id="intro">Intro paragraph</p>',
        js="""      const element = document.getElementById("intro");
      document.getElementById("demo").innerText =
        element.textContent + "\\nmissing=" + document.getElementById("no-such");""",
    ),
    P(
        "find-by-tag",
        "Finding HTML Elements by Tag Name",
        [
            "`document.getElementsByTagName(\"p\")` collects **every** `<p>` in the document.",
            "The result is an HTMLCollection: use `[0]`, `[1]`, `.length`.",
            "Order is **tree order** (top to bottom in the markup).",
        ],
        """<p>Red</p><p>Blue</p>
<script>
const element = document.getElementsByTagName("p");
</script>""",
        "Two paragraphs are listed: **Red** then **Blue**.",
        body="<p>Red</p><p>Blue</p>",
        js="""      const element = document.getElementsByTagName("p");
      document.getElementById("demo").innerText =
        element.length + ": " + element[0].textContent + ", " + element[1].textContent;""",
    ),
    P(
        "find-tag-inside-id",
        "Tag name inside another element",
        [
            "Elements also have `getElementsByTagName`. Scope the search to a subtree.",
            "Here `#main` contains the paragraphs we want; paragraphs outside `#main` are ignored.",
            "Pattern: find a root, then search **inside** it.",
        ],
        """<div id="main"><p>In</p><p>Also</p></div>
<p>Outside</p>
<script>
const x = document.getElementById("main");
const y = x.getElementsByTagName("p");
</script>""",
        "`y.length` is **2**. The **Outside** paragraph is not included.",
        body='<div id="main"><p>In</p><p>Also</p></div><p>Outside</p>',
        js="""      const x = document.getElementById("main");
      const y = x.getElementsByTagName("p");
      document.getElementById("demo").innerText =
        "inside=" + y.length + " texts=" + y[0].textContent + "," + y[1].textContent;""",
    ),
    P(
        "find-by-class",
        "Finding HTML Elements by Class Name",
        [
            "`getElementsByClassName(\"intro\")` — class token only, no leading dot.",
            "Elements with multiple classes (`class=\"intro note\"`) still match `intro`.",
            "Live HTMLCollection, same indexing rules as tag-name lists.",
        ],
        """<p class="intro">A</p>
<div class="intro">B</div>
<script>
const x = document.getElementsByClassName("intro");
</script>""",
        "Both the paragraph and the div with class **intro** are returned (length **2**).",
        body='<p class="intro">A</p><div class="intro">B</div>',
        js="""      const x = document.getElementsByClassName("intro");
      document.getElementById("demo").innerText =
        "length=" + x.length + " " + x[0].tagName + "," + x[1].tagName;""",
    ),
    P(
        "qs-class",
        "The querySelector() Method",
        [
            "`querySelector` takes a **CSS** selector, so classes **do** use a leading `.`.",
            "Only the first match is returned.",
            "Returns `null` if nothing matches — check before you set `innerHTML`.",
        ],
        """<p class="note">Hello World!</p>
<script>
const myPara = document.querySelector(".note");
myPara.innerHTML = "Hello World!";
</script>""",
        "The first `.note` paragraph is set to **Hello World!**.",
        body='<p class="note">old</p>',
        js="""      const myPara = document.querySelector(".note");
      myPara.innerHTML = "Hello World!";
      document.getElementById("demo").innerText = myPara.innerHTML;""",
    ),
    P(
        "qsa-first-item",
        "The querySelectorAll() Method",
        [
            "`querySelectorAll(\".demo\")` returns **all** matches as a NodeList.",
            "Index `[0]` is the first. Assigning `innerHTML` on `[0]` does not change the others.",
            "NodeList is **static**: later DOM changes do not update this list.",
        ],
        """<p class="row">One</p><p class="row">Two</p>
<script>
const myItems = document.querySelectorAll(".row");
myItems[0].innerHTML = "First";
</script>""",
        "Item 0 becomes **First**; item 1 stays **Two**.",
        body='<p class="row">One</p><p class="row">Two</p>',
        js="""      const myItems = document.querySelectorAll(".row");
      myItems[0].innerHTML = "First";
      document.getElementById("demo").innerText = myItems[0].innerHTML + " / " + myItems[1].innerHTML;""",
    ),
    P(
        "qsa-p-intro",
        "querySelectorAll(\"p.intro\")",
        [
            "`p.intro` means **paragraphs** that also have class **intro** — not every `.intro`.",
            "A `<div class=\"intro\">` would **not** match this selector.",
            "This is the compound-selector form the W3Schools page shows for “all p.intro”.",
        ],
        """<p class="intro">yes</p>
<div class="intro">no</div>
<p>plain</p>
<script>
const x = document.querySelectorAll("p.intro");
</script>""",
        "Only the **yes** paragraph matches `p.intro` (length **1**).",
        body='<p class="intro">yes</p><div class="intro">no</div><p>plain</p>',
        js="""      const x = document.querySelectorAll("p.intro");
      document.getElementById("demo").innerText = "length=" + x.length + " text=" + x[0].textContent;""",
    ),
    P(
        "mistake-hash-id",
        "Common mistake — `#` in getElementById()",
        [
            "**Wrong:** `getElementById(\"#demo\")` looks for an id that is literally `#demo`.",
            "**Right:** `getElementById(\"demo\")`. The `#` is only for CSS / `querySelector`.",
            "This sandbox shows the wrong call returning **null** and the right call succeeding.",
        ],
        """<p id="demo-el">ok</p>
<script>
document.getElementById("#demo-el"); // null
document.getElementById("demo-el");  // the paragraph
</script>""",
        "With `#` the result is **null**; without `#` you get the paragraph **ok**.",
        body='<p id="demo-el">ok</p>',
        js="""      document.getElementById("demo").innerText =
        "wrong=" + document.getElementById("#demo-el") + "\\n" +
        "right=" + document.getElementById("demo-el").textContent;""",
    ),
    P(
        "mistake-qs-first-only",
        "Common mistake — querySelector returns only the first match",
        [
            "Beginners call `querySelector(\".item\")` and wonder why later items never change.",
            "Loop `querySelectorAll`, or use a more specific selector if you need one particular node.",
            "This example changes only index 0 even though two `.item` nodes exist.",
        ],
        """<p class="item">A</p><p class="item">B</p>
<script>
document.querySelector(".item").textContent = "only first";
</script>""",
        "A becomes **only first**; B stays **B**.",
        body='<p class="item">A</p><p class="item">B</p>',
        js="""      document.querySelector(".item").textContent = "only first";
      const all = document.querySelectorAll(".item");
      document.getElementById("demo").innerText = all[0].textContent + " / " + all[1].textContent;""",
    ),
    P(
        "forms-collection",
        "Finding elements via document.forms",
        [
            "`document.forms[\"frm1\"]` is the form with `id` or `name` **frm1** (HTMLFormControlsCollection).",
            "`form.elements` lists controls in order. `.value` is each field’s current string.",
            "This is the “HTML object collections” style on the W3Schools page — older than querySelector, still valid.",
        ],
        """<form id="frm1">
  <input name="a" value="Hello">
  <input name="b" value="World">
</form>
<script>
const x = document.forms["frm1"];
let text = "";
for (let i = 0; i < x.length; i++) {
  text += x.elements[i].value + " ";
}
</script>""",
        "The loop prints **Hello World** (trailing space included, matching the site pattern).",
        body='<form id="frm1"><input name="a" value="Hello"><input name="b" value="World"></form>',
        js="""      const x = document.forms["frm1"];
      let text = "";
      for (let i = 0; i < x.length; i++) {
        text += x.elements[i].value + " ";
      }
      document.getElementById("demo").innerText = text;""",
    ),
    P(
        "collection-images",
        "document.images collection",
        [
            "`document.images` is an HTMLCollection of every `<img>` in the document.",
            "Useful for counting or looping pictures without a CSS selector.",
            "Each item is an HTMLImageElement (`src`, `alt`, `width`).",
        ],
        """<img alt="one" width="16" height="16" src="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg'/>">
<script>
const n = document.images.length;
</script>""",
        "`document.images.length` is **1** in this sandbox (plus any others the chrome adds — we report the count).",
        body="""<img alt="one" width="16" height="16" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'/%3E">""",
        js="""      document.getElementById("demo").innerText =
        "images=" + document.images.length + " alt=" + document.images[0].alt;""",
    ),
    P(
        "collection-links",
        "document.links collection",
        [
            "`document.links` is every `<a>` and `<area>` that has an **`href`**.",
            "A `<a>` without href is **not** in this collection.",
            "Older pages used this instead of `querySelectorAll(\"a[href]\")`.",
        ],
        """<a href="https://example.com">ex</a>
<a>no href</a>
<script>
const n = document.links.length;
</script>""",
        "Only the real hyperlink is counted in **`document.links`**.",
        body='<a href="https://example.com">ex</a> <a>no href</a>',
        js="""      document.getElementById("demo").innerText =
        "links=" + document.links.length + " href=" + document.links[0].href;""",
    ),
    P(
        "collection-scripts",
        "document.scripts collection",
        [
            "`document.scripts` lists every `<script>` element.",
            "Inline scripts and `src` scripts both appear.",
            "Handy for debugging “how many scripts loaded on this page?”",
        ],
        """<script>/* counted */</script>""",
        "`document.scripts.length` is at least **1** (this page’s own script tags).",
        body="<p>Scripts on this page:</p>",
        js="""      document.getElementById("demo").innerText = "scripts=" + document.scripts.length;""",
    ),
    P(
        "collection-body-title-head",
        "document.body, document.title, document.head",
        [
            "`document.body` is the `<body>` element. `document.head` is `<head>`.",
            "`document.title` is the **document title** (string), matching `<title>` — you can assign it.",
            "`document.documentElement` is the root `<html>` element.",
        ],
        """<script>
document.title = "Selecting Elements";
</script>""",
        "The sandbox reports the **body** tagName, **head** presence, **html** root, and the title string.",
        body="<p>Document shortcuts</p>",
        js="""      document.title = "Selecting Elements";
      document.getElementById("demo").innerText = [
        "body=" + document.body.tagName,
        "head=" + document.head.tagName,
        "root=" + document.documentElement.tagName,
        "title=" + document.title
      ].join("\\n");""",
    ),
    P(
        "collection-embeds-anchors",
        "document.embeds and document.anchors (legacy)",
        [
            "`document.embeds` is a collection of `<embed>` elements.",
            "`document.anchors` was `<a name=\"...\">` bookmarks. It is **deprecated** — do not use it in new code.",
            "This example still **reads** both so you recognize them if you meet old pages.",
        ],
        """<embed id="e" type="text/plain" width="1" height="1">
<a name="old">named anchor</a>
<script>
document.embeds.length;
document.anchors && document.anchors.length;
</script>""",
        "`embeds.length` is **1**. `anchors` is deprecated; the sandbox prints its length if the browser still exposes it.",
        body='<embed id="e" type="text/plain" width="1" height="1"><a name="old">named anchor</a>',
        js="""      let anc = "(gone)";
      try { anc = String(document.anchors ? document.anchors.length : "undefined"); }
      catch (e) { anc = e.name; }
      document.getElementById("demo").innerText =
        "embeds=" + document.embeds.length + "\\nanchors=" + anc;""",
    ),
]

SELECTING_QA = qa(
    ("What does `getElementById` return when nothing matches?", ["**`null`**."]),
    ("How do you find every `<p>` inside `#main`?", ["`document.getElementById(\"main\").getElementsByTagName(\"p\")`."]),
    ("Do you pass `\".intro\"` to `getElementsByClassName`?", ["No — pass **`\"intro\"`**. The dot is for CSS / `querySelector`."]),
    ("What is wrong with `getElementById(\"#demo\")`?", ["The `#` is included in the id search, so you get **null** unless the id is literally `#demo`."]),
    ("Why did only the first `.item` change after `querySelector`?", ["`querySelector` returns **one** node — the first match."]),
    ("How do you read every control value in `id=\"frm1\"`?", ["`document.forms[\"frm1\"]` then loop `form.elements[i].value`."]),
    ("What is in `document.links`?", ["`<a>` and `<area>` elements that have an **`href`**."]),
    ("What is `document.documentElement`?", ["The root **`<html>`** element."]),
    ("Should new code use `document.anchors`?", ["No — it is **deprecated**. Use `id` + `getElementById` or `querySelector`."]),
    ("Is `querySelectorAll` live?", ["No — it returns a **static** NodeList taken at call time."]),
)

# ---------------------------------------------------------------------------
# 24.4 Changing HTML
# ---------------------------------------------------------------------------

SMILE = "data:image/svg+xml," + (
    "%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='48'%3E"
    "%3Ccircle cx='24' cy='24' r='22' fill='%23ffd54a'/%3E"
    "%3Ccircle cx='16' cy='20' r='3'/%3E%3Ccircle cx='32' cy='20' r='3'/%3E"
    "%3Cpath d='M14 30 Q24 40 34 30' stroke='%23000' fill='none' stroke-width='3'/%3E"
    "%3C/svg%3E"
)
LAND = "data:image/svg+xml," + (
    "%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='48'%3E"
    "%3Crect width='48' height='48' fill='%2387ceeb'/%3E"
    "%3Crect y='28' width='48' height='20' fill='%23228b22'/%3E"
    "%3Ccircle cx='38' cy='12' r='6' fill='%23ffdd33'/%3E"
    "%3C/svg%3E"
)

CHANGING_HTML = [
    P(
        "innerhtml-p",
        "Change the content of a p element",
        [
            "Syntax: `document.getElementById(id).innerHTML = new HTML`.",
            "The page has `<p id=\"p1\">Hello World!</p>`. JS replaces the text with **New text!**.",
            "Do not run this before the element exists (put the script **after** the HTML, or wait for DOMContentLoaded).",
            "Always quote the id: `\"p1\"`, not `p1` as a bare identifier.",
        ],
        """<p id="p1">Hello World!</p>
<script>
document.getElementById("p1").innerHTML = "New text!";
</script>""",
        "The paragraph that said **Hello World!** now says **New text!**.",
        body='<p id="p1">Hello World!</p>',
        js="""      document.getElementById("p1").innerHTML = "New text!";
      document.getElementById("demo").innerText = document.getElementById("p1").innerHTML;""",
    ),
    P(
        "innerhtml-heading",
        "Change the content of an h1 element",
        [
            "`innerHTML` works on **any** element, including headings.",
            "Here `#id01` starts as **Old Heading** and becomes **New Heading**.",
            "Same three steps: find by id → take the element → assign `innerHTML`.",
        ],
        """<h1 id="id01">Old Heading</h1>
<script>
const element = document.getElementById("id01");
element.innerHTML = "New Heading";
</script>""",
        "The heading reads **New Heading**.",
        body='<h1 id="id01">Old Heading</h1>',
        js="""      const element = document.getElementById("id01");
      element.innerHTML = "New Heading";
      document.getElementById("demo").innerText = element.innerHTML;""",
    ),
    P(
        "change-src",
        "Change an img src attribute",
        [
            "Syntax: `document.getElementById(id).attribute = new value`.",
            "Here `src` starts as a smiley SVG and is switched to a landscape SVG (stand-ins for the site’s `smiley.gif` / `landscape.jpg`).",
            "`img.src` after assignment is the **absolute** URL the browser resolved.",
            "Changing `src` starts a new image load.",
        ],
        """<img id="myImage" alt="demo" src="smiley.svg" width="48" height="48">
<script>
document.getElementById("myImage").src = "landscape.svg";
</script>""",
        "The image `src` is changed from the smiley file to **landscape.svg**.",
        body='<img id="myImage" alt="demo" src="smiley.svg" width="48" height="48">',
        js="""      const img = document.getElementById("myImage");
      const before = img.getAttribute("src");
      img.src = "landscape.svg";
      document.getElementById("demo").innerText =
        "beforeAttr=" + before + "\\nafterAttr=" + img.getAttribute("src");""",
        extra_files={
            "smiley.svg": (
                '<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48">'
                '<circle cx="24" cy="24" r="22" fill="#ffd54a"/>'
                '<circle cx="16" cy="20" r="3"/><circle cx="32" cy="20" r="3"/>'
                '<path d="M14 30 Q24 40 34 30" stroke="#000" fill="none" stroke-width="3"/>'
                "</svg>"
            ),
            "landscape.svg": (
                '<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48">'
                '<rect width="48" height="48" fill="#87ceeb"/>'
                '<rect y="28" width="48" height="20" fill="#228b22"/>'
                '<circle cx="38" cy="12" r="6" fill="#ffdd33"/>'
                "</svg>"
            ),
        },
    ),
    P(
        "dynamic-date",
        "Dynamic HTML content with Date()",
        [
            "JavaScript can write **live** values into the page, such as the current date.",
            "`Date()` with no `new` returns a date **string** (implementation dependent, usually locale-like).",
            "Re-run the assignment to refresh the clock (or use `setInterval` later).",
        ],
        """<p id="when"></p>
<script>
document.getElementById("when").innerHTML = "Date : " + Date();
</script>""",
        "The paragraph shows **Date :** followed by the current date/time string.",
        body='<p id="when"></p>',
        js="""      document.getElementById("when").innerHTML = "Date : " + Date();
      document.getElementById("demo").innerText = document.getElementById("when").innerHTML;""",
    ),
    P(
        "document-write-stream",
        "document.write() during parse",
        [
            "`document.write()` writes into the HTML **output stream** while the document is still loading.",
            "The W3Schools example places it between two “Bla bla bla” paragraphs so the date appears in the middle.",
            "This sandbox uses an **iframe** so we can `open` / `write` / `close` without wiping the tutorial page.",
            "During initial parse, `write` inserts at the current position; after load it **replaces the whole document**.",
        ],
        """<p>Bla bla bla</p>
<script>
document.write(Date());
</script>
<p>Bla bla bla</p>""",
        "The iframe document contains Bla, then the **date string**, then Bla — `write` ran as part of the stream.",
        body='<iframe id="f" style="width:100%;height:90px;border:1px solid #ccc;"></iframe>',
        js="""      const d = document.getElementById("f").contentDocument;
      d.open();
      d.write("<p>Bla bla bla</p><p>" + Date() + "</p><p>Bla bla bla</p>");
      d.close();
      document.getElementById("demo").innerText = d.body.innerText.replace(/\\s+/g, " ").trim();""",
    ),
    P(
        "document-write-warning",
        "Warning — never document.write() after the document is loaded",
        [
            "**Never** call `document.write()` after load. It calls `open()` implicitly and **overwrites** the page.",
            "That is why modern code uses `innerHTML`, `textContent`, or `appendChild` instead.",
            "This demo writes into an iframe **after** it has loaded so you can see the previous content vanish.",
        ],
        """<script>
window.addEventListener("load", function () {
  // This would wipe the real page. Do not do this on a live document.
  // document.write("oops");
});
</script>""",
        "The iframe first shows **keep me**, then after `write` it only shows **overwritten** — the original document is gone.",
        body='<iframe id="f" style="width:100%;height:70px;border:1px solid #ccc;"></iframe>',
        js="""      const d = document.getElementById("f").contentDocument;
      d.open();
      d.write("<p id='k'>keep me</p>");
      d.close();
      const before = d.body ? d.body.innerText : "";
      // After load, write() implies open() and replaces the document.
      // Use a fresh open/write/close so headless Chrome does not hang.
      d.open();
      d.write("overwritten");
      d.close();
      document.getElementById("demo").innerText =
        "before=" + before.trim() + "\\nafter=" + d.body.innerText.trim();""",
    ),
]

CHANGING_HTML_QA = qa(
    ("What is the `innerHTML` assignment syntax?", ["`document.getElementById(id).innerHTML = new HTML`."]),
    ("Why might `getElementById` be null if the markup looks correct?", ["The script ran **before** the element existed. Move the script below the HTML or wait for **DOMContentLoaded**."]),
    ("Does `innerHTML` work on headings?", ["Yes — any element, including **`<h1>`**."]),
    ("How do you change an image file from JS?", ["Set **`img.src`** (or `setAttribute(\"src\", …)`) to the new URL."]),
    ("What does `Date()` return when called as a function?", ["A **date string**, not a Date object (`new Date()` is the object)."]),
    ("When is `document.write` acceptable?", ["Only while the document is still **parsing** (or into a document you `open()` yourself)."]),
    ("What happens if you `document.write` after load?", ["It **overwrites** the entire document. The previous DOM is destroyed."]),
    ("How can you quote the id wrong?", ["Forgetting quotes (`p1` as a variable) or putting a script in `<head>` too early."]),
    ("Why does this sandbox use an iframe for `write`?", ["So the example can demonstrate overwriting **without** destroying the tutorial page around it."]),
    ("What should you use instead of `write` for updates?", ["**`innerHTML`**, **`textContent`**, or DOM methods like **`appendChild`**."]),
)

# ---------------------------------------------------------------------------
# 24.5 Changing CSS
# ---------------------------------------------------------------------------

CHANGING_CSS = [
    P(
        "style-color",
        "Change a paragraph’s color",
        [
            "Syntax: `document.getElementById(id).style.property = new style`.",
            "`style.color = \"blue\"` sets the CSS **color** as an inline style.",
            "Property names in JS drop the hyphen: `background-color` → `backgroundColor`.",
        ],
        """<p id="p2">Hello World!</p>
<script>
document.getElementById("p2").style.color = "blue";
</script>""",
        "The paragraph is **blue**. `style.color` reports the inline value.",
        body='<p id="p2">Hello World!</p>',
        js="""      const p = document.getElementById("p2");
      p.style.color = "blue";
      document.getElementById("demo").innerText = "color=" + p.style.color;""",
    ),
    P(
        "style-on-click",
        "Change style when a button is clicked",
        [
            "The DOM can run code when **events** happen: click, load, input change.",
            "This example sets `#id1` to red **fontSize 40px** when the button is clicked.",
            "The snapshot calls `.click()` so the result image shows the styled heading.",
        ],
        """<h1 id="id1">My Heading 1</h1>
<button type="button" onclick="document.getElementById('id1').style.color='red'; document.getElementById('id1').style.fontSize='40px';">
  Click Me!
</button>""",
        "After the click, the heading is **red** and **40px**.",
        body="""<h1 id="id1">My Heading 1</h1>
<button type="button" id="btn">Click Me!</button>""",
        js="""      document.getElementById("btn").onclick = function () {
        const h = document.getElementById("id1");
        h.style.color = "red";
        h.style.fontSize = "40px";
      };
      document.getElementById("btn").click();
      const h = document.getElementById("id1");
      document.getElementById("demo").innerText = "color=" + h.style.color + " fontSize=" + h.style.fontSize;""",
    ),
    P(
        "hide-element",
        "Make an element invisible with display:none",
        [
            "`style.display = \"none\"` removes the element from layout (it does not delete the node).",
            "`style.display = \"block\"` (or `\"\"` to revert) shows it again.",
            "`visibility: hidden` hides it but **keeps the gap**. `display:none` collapses the gap.",
        ],
        """<p id="hide">I can vanish</p>
<button type="button" id="btn">Click Me!</button>
<script>
document.getElementById("btn").onclick = function () {
  document.getElementById("hide").style.display = "none";
};
</script>""",
        "After click, `#hide` has **display:none** and is not visible in the result snap.",
        body='<p id="hide">I can vanish</p><button type="button" id="btn">Click Me!</button>',
        js="""      document.getElementById("btn").onclick = function () {
        document.getElementById("hide").style.display = "none";
      };
      document.getElementById("btn").click();
      document.getElementById("demo").innerText =
        "display=" + document.getElementById("hide").style.display;""",
    ),
    P(
        "style-object-ref",
        "HTML DOM Style object (inline only)",
        [
            "Every element has a **`style`** object. Assigning properties writes **inline** CSS.",
            "It does not list rules from your stylesheet. Use `getComputedStyle(el)` for the used value.",
            "Full property list: CSSStyleDeclaration / HTML DOM Style Object Reference on W3Schools.",
        ],
        """<p id="box">box</p>
<script>
const el = document.getElementById("box");
el.style.backgroundColor = "gold";
const used = getComputedStyle(el).backgroundColor;
</script>""",
        "Inline `backgroundColor` is **gold**; `getComputedStyle` returns the computed rgb color.",
        body='<p id="box">box</p>',
        js="""      const el = document.getElementById("box");
      el.style.backgroundColor = "gold";
      document.getElementById("demo").innerText =
        "inline=" + el.style.backgroundColor +
        "\\ncomputed=" + getComputedStyle(el).backgroundColor;""",
    ),
]

CHANGING_CSS_QA = qa(
    ("What is the CSS-from-JS syntax?", ["`document.getElementById(id).style.property = new style`."]),
    ("How is `background-color` written in JavaScript?", ["**`backgroundColor`** (camelCase)."]),
    ("Does `element.style` include stylesheet rules?", ["No — **inline** styles only. Use **`getComputedStyle`**."]),
    ("What event did the heading example use?", ["A **click** on the button (`onclick`)."]),
    ("What does `display = \"none\"` do?", ["The element is not rendered and **does not take up space**."]),
    ("How is that different from `visibility: hidden`?", ["Hidden still **occupies layout space**; `display:none` does not."]),
    ("Can you change `fontSize` from JS?", ["Yes — `style.fontSize = \"40px\"` (include the unit)."]),
    ("Why include `'px'`?", ["Most CSS length properties need a unit. `fontSize = 40` is invalid / ignored."]),
    ("Is the node deleted when display is none?", ["No — it stays in the DOM. You can show it again."]),
    ("Where do you look up every style property name?", ["The **HTML DOM Style Object** reference (CSSStyleDeclaration)."]),
)

# ---------------------------------------------------------------------------
# 24.6 Form Validation
# ---------------------------------------------------------------------------

FORM_VAL = [
    P(
        "js-empty-name",
        "JavaScript — reject an empty name",
        [
            "`document.forms[\"myForm\"][\"fname\"].value` reads the **Name** field.",
            "If it is `\"\"`, `alert` and **`return false`** cancel submit (with `onsubmit=\"return validateForm()\"`).",
            "Returning **true** (or nothing after checks pass) allows the submit.",
            "The sandbox submits an empty form and records that validation **blocked** it (`preventDefault` equivalent via `return false`).",
        ],
        """<form name="myForm" onsubmit="return validateForm()" action="#">
  Name: <input type="text" name="fname">
  <input type="submit" value="Submit">
</form>
<script>
function validateForm() {
  let x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }
}
</script>""",
        "Empty name → validation returns **false** and the form does not navigate away.",
        body="""<form name="myForm" action="#">
  Name: <input type="text" name="fname" id="fname">
  <button type="submit">Submit</button>
</form>""",
        js="""      function validateForm() {
        let x = document.forms["myForm"]["fname"].value;
        if (x == "") {
          document.getElementById("demo").innerText = "blocked: Name must be filled out";
          return false;
        }
        document.getElementById("demo").innerText = "would submit";
        return false;
      }
      document.forms["myForm"].onsubmit = function (e) {
        e.preventDefault();
        return validateForm();
      };
      document.forms["myForm"].requestSubmit();""",
    ),
    P(
        "js-numeric-range",
        "JavaScript — number between 1 and 10",
        [
            "Read the input, convert with `Number` or compare as numbers.",
            "If the value is outside **1–10** (or not a number), show a message and stop.",
            "The snapshot enters **15**, which fails the range check.",
        ],
        """<p>Please input a number between 1 and 10</p>
<input id="num" type="number">
<button type="button" id="go">Submit</button>
<script>
document.getElementById("go").onclick = function () {
  const v = Number(document.getElementById("num").value);
  if (Number.isNaN(v) || v < 1 || v > 10) {
    document.getElementById("demo").innerText = "Invalid: need 1–10";
  } else {
    document.getElementById("demo").innerText = "OK: " + v;
  }
};
</script>""",
        "Value **15** is rejected: **Invalid: need 1–10**.",
        body='<p>Please input a number between 1 and 10</p><input id="num" type="number"><button type="button" id="go">Submit</button>',
        js="""      document.getElementById("go").onclick = function () {
        const v = Number(document.getElementById("num").value);
        if (Number.isNaN(v) || v < 1 || v > 10) {
          document.getElementById("demo").innerText = "Invalid: need 1–10";
        } else {
          document.getElementById("demo").innerText = "OK: " + v;
        }
      };
      document.getElementById("num").value = "15";
      document.getElementById("go").click();""",
    ),
    P(
        "html-required",
        "Automatic HTML validation — required",
        [
            "The **`required`** attribute stops submit when the field is empty — **no JavaScript**.",
            "The browser shows its own message. This did not work in **IE 9** and earlier (historical note).",
            "`checkValidity()` returns false when empty. `reportValidity()` would show the native bubble.",
        ],
        """<form id="f" action="#">
  <input name="fname" required>
  <input type="submit">
</form>""",
        "`checkValidity()` is **false** on an empty required field — the browser would block submit.",
        body='<form id="f" action="#"><input name="fname" required id="fname"><button type="submit">Submit</button></form>',
        js="""      const f = document.getElementById("f");
      f.addEventListener("submit", function (e) { e.preventDefault(); });
      document.getElementById("demo").innerText =
        "checkValidity=" + f.checkValidity() +
        "\\nrequired empty=" + document.getElementById("fname").validity.valueMissing;""",
    ),
    P(
        "server-vs-client",
        "Data validation — client vs server",
        [
            "**Data validation** means input is clean, correct, and useful (required filled, dates valid, numbers in numeric fields).",
            "**Client-side** runs in the browser **before** send — fast UX, easy to skip (user can disable JS).",
            "**Server-side** runs **after** the request arrives — the one you must trust for security.",
            "Use both: client for instant help, server as the real gate.",
        ],
        """<script>
const kinds = [
  "Client-side: browser, before request",
  "Server-side: server, after request"
];
</script>""",
        "The snapshot lists **client-side** (before send) and **server-side** (after send).",
        body="<p>Typical checks: required fields, valid date, text not in a numeric field.</p>",
        js="""      document.getElementById("demo").innerText = [
        "Client-side: browser, before request",
        "Server-side: server, after request"
      ].join("\\n");""",
    ),
    P(
        "attr-disabled",
        "Constraint attribute — disabled",
        [
            "`disabled` means the control is not editable and is **not submitted**.",
            "CSS `:disabled` matches it. JS `el.disabled = true` toggles the same state.",
        ],
        """<input id="x" value="locked" disabled>""",
        "The input is **disabled**; `disabled` is **true** and it matches `:disabled`.",
        body='<input id="x" value="locked" disabled>',
        js="""      const x = document.getElementById("x");
      document.getElementById("demo").innerText =
        "disabled=" + x.disabled + " matches=:disabled " + x.matches(":disabled");""",
    ),
    P(
        "attr-min-max",
        "Constraint attributes — min and max",
        [
            "`min` / `max` bound numeric (and date) inputs.",
            "`validity.rangeUnderflow` / `rangeOverflow` tell you which way it failed.",
            "The snapshot sets **0** on a field with `min=\"1\" max=\"10\"`.",
        ],
        """<input id="n" type="number" min="1" max="10" value="0">""",
        "**0** is below min: `rangeUnderflow` is **true**, `checkValidity` is **false**.",
        body='<input id="n" type="number" min="1" max="10" value="0">',
        js="""      const n = document.getElementById("n");
      document.getElementById("demo").innerText =
        "valid=" + n.checkValidity() +
        " underflow=" + n.validity.rangeUnderflow +
        " overflow=" + n.validity.rangeOverflow;""",
    ),
    P(
        "attr-pattern",
        "Constraint attribute — pattern",
        [
            "`pattern` is a **regex** for the whole value (HTML already anchors it).",
            "Example: `[A-Za-z]{3}` means exactly three letters.",
            "`validity.patternMismatch` is true when the value does not match.",
        ],
        """<input id="p" pattern="[A-Za-z]{3}" value="12">""",
        "**12** fails `[A-Za-z]{3}`: **patternMismatch** is true.",
        body='<input id="p" pattern="[A-Za-z]{3}" value="12">',
        js="""      const p = document.getElementById("p");
      document.getElementById("demo").innerText =
        "valid=" + p.checkValidity() + " patternMismatch=" + p.validity.patternMismatch;""",
    ),
    P(
        "attr-required",
        "Constraint attribute — required",
        [
            "`required` means the field must have a value before submit.",
            "`validity.valueMissing` is the flag for “empty but required”.",
            "This is the same idea as the automatic HTML example, as a table row of its own.",
        ],
        """<input id="r" required value="">""",
        "Empty required input: **valueMissing** true, `checkValidity` false.",
        body='<input id="r" required value="">',
        js="""      const r = document.getElementById("r");
      document.getElementById("demo").innerText =
        "valid=" + r.checkValidity() + " valueMissing=" + r.validity.valueMissing;""",
    ),
    P(
        "attr-type",
        "Constraint attribute — type",
        [
            "`type` selects the control and its built-in checks (`email`, `number`, `url`, …).",
            "`type=\"email\"` with `not-an-email` sets `validity.typeMismatch`.",
            "Mobile browsers also pick a suitable keyboard from `type`.",
        ],
        """<input id="e" type="email" value="not-an-email">""",
        "**not-an-email** fails `type=\"email\"`: **typeMismatch** is true.",
        body='<input id="e" type="email" value="not-an-email">',
        js="""      const e = document.getElementById("e");
      document.getElementById("demo").innerText =
        "valid=" + e.checkValidity() + " typeMismatch=" + e.validity.typeMismatch;""",
    ),
    P(
        "pseudo-disabled",
        "CSS pseudo — :disabled",
        [
            "`:disabled` selects inputs that have the disabled attribute / property.",
            "Use it to grey out labels or hide helper text next to dead controls.",
        ],
        """<input id="d" disabled>
<script>
document.querySelector("input:disabled");
</script>""",
        "`querySelector(\"input:disabled\")` finds the disabled control.",
        body='<input id="d" disabled><input id="e" value="on">',
        css="input:disabled { outline: 2px solid gray; }",
        js="""      const el = document.querySelector("input:disabled");
      document.getElementById("demo").innerText = "id=" + el.id + " matches=" + el.matches(":disabled");""",
    ),
    P(
        "pseudo-invalid-valid",
        "CSS pseudo — :invalid and :valid",
        [
            "`:invalid` matches controls that fail constraint validation **right now**.",
            "`:valid` is the opposite. Empty non-required fields are usually valid.",
            "Great for red/green outlines without JavaScript.",
        ],
        """<input id="bad" type="email" value="x">
<input id="good" type="email" value="a@b.c">""",
        "`#bad` matches **:invalid**; `#good` matches **:valid**.",
        body='<input id="bad" type="email" value="x"><input id="good" type="email" value="a@b.c">',
        css=":invalid { outline: 2px solid red; } :valid { outline: 2px solid green; }",
        js="""      const bad = document.getElementById("bad");
      const good = document.getElementById("good");
      document.getElementById("demo").innerText =
        "bad invalid=" + bad.matches(":invalid") +
        "\\ngood valid=" + good.matches(":valid");""",
    ),
    P(
        "pseudo-required-optional",
        "CSS pseudo — :required and :optional",
        [
            "`:required` selects fields with the required attribute.",
            "`:optional` selects fields **without** required.",
            "Use them to mark mandatory fields in CSS alone.",
        ],
        """<input id="req" required>
<input id="opt">""",
        "`#req` matches **:required**; `#opt` matches **:optional**.",
        body='<input id="req" required><input id="opt">',
        js="""      document.getElementById("demo").innerText =
        "req=" + document.getElementById("req").matches(":required") +
        "\\nopt=" + document.getElementById("opt").matches(":optional");""",
    ),
]

FORM_VAL_QA = qa(
    ("How does the empty-name script cancel submit?", ["It **`return false`** from the `onsubmit` handler after `alert`."]),
    ("How do you read `fname` on `myForm`?", ["`document.forms[\"myForm\"][\"fname\"].value`."]),
    ("Is 15 valid for “number between 1 and 10”?", ["No — it is **outside** the range."]),
    ("What HTML attribute blocks empty submit without JS?", ["**`required`**."]),
    ("Why still validate on the server?", ["Client checks can be **skipped**. Security and correctness live on the **server**."]),
    ("What flag is set when a required field is empty?", ["**`validity.valueMissing`**."]),
    ("What flag is set for `type=\"email\"` with `not-an-email`?", ["**`typeMismatch`**."]),
    ("What does `pattern` use?", ["A **regular expression** for the whole value."]),
    ("Which CSS selector matches a failing control?", ["**:invalid**."]),
    ("Does `:optional` mean the value is wrong?", ["No — it means the field is **not required**."]),
    ("What does `disabled` do to submit data?", ["Disabled controls are **not successful** — they are omitted from the submit payload."]),
    ("IE 9 and `required`?", ["Automatic HTML5 validation **did not work** in IE 9 or earlier (historical)."]),
)

# ---------------------------------------------------------------------------
# 24.7 DOM Animations
# ---------------------------------------------------------------------------

ANIM_CSS = """
#container { width: 400px; height: 200px; position: relative; background: yellow; }
#animate { width: 50px; height: 50px; position: absolute; background: red; }
"""

ANIMATIONS = [
    P(
        "basic-page",
        "A basic web page for the animation",
        [
            "W3Schools starts with a heading and a placeholder: **My animation will go here**.",
            "You need a page **structure** first; the moving box comes next.",
            "Keep animation markup simple so the timer code is easy to see.",
        ],
        """<h2>My First JavaScript Animation</h2>
<div>My animation will go here</div>""",
        "The page shows the title and the placeholder box area.",
        body="<h2>My First JavaScript Animation</h2><div>My animation will go here</div>",
        js="""      document.getElementById("demo").innerText = "placeholder page ready";""",
    ),
    P(
        "container",
        "Create an animation container",
        [
            "All animations should be **relative to a container** so coordinates stay inside that box.",
            "The moving element is a child of the container, not of the whole page.",
            "Later CSS: container `position: relative`, mover `position: absolute`.",
        ],
        """<div id="container">
  <div id="animate">My animation will go here</div>
</div>""",
        "The red square lives **inside** the yellow `#container`.",
        body='<div id="container"><div id="animate"></div></div>',
        css=ANIM_CSS,
        js="""      document.getElementById("demo").innerText =
        "container=" + document.getElementById("container").id +
        " child=" + document.getElementById("animate").id;""",
    ),
    P(
        "style-relative-absolute",
        "Style the elements — relative container, absolute mover",
        [
            "Container: `position: relative` (and a size + background).",
            "Mover: `position: absolute` so `top` / `left` are relative to the container.",
            "W3Schools uses a **400×400** yellow field and a **50×50** red square (this snap uses 400×200 to fit).",
            "Without relative/absolute, `top`/`left` will not animate inside the box.",
        ],
        """#container {
  width: 400px;
  height: 400px;
  position: relative;
  background: yellow;
}
#animate {
  width: 50px;
  height: 50px;
  position: absolute;
  background: red;
}""",
        "Computed position of the container is **relative**; the square is **absolute**.",
        body='<div id="container"><div id="animate"></div></div>',
        css=ANIM_CSS,
        js="""      const c = getComputedStyle(document.getElementById("container"));
      const a = getComputedStyle(document.getElementById("animate"));
      document.getElementById("demo").innerText =
        "container=" + c.position + " " + c.width + "\\n" +
        "animate=" + a.position + " " + a.width;""",
        fence="css",
    ),
    P(
        "interval-skeleton",
        "Animation code — setInterval and clearInterval",
        [
            "JS animation = **small style changes** on a timer so it looks continuous.",
            "`id = setInterval(frame, 5)` calls `frame` every **5 ms**.",
            "When the end test is true, **`clearInterval(id)`** stops the timer (or it runs forever).",
            "Else, change `top`/`left` (or opacity, width, …).",
        ],
        """id = setInterval(frame, 5);
function frame() {
  if (/* test for finished */) {
    clearInterval(id);
  } else {
    /* code to change the element style */
  }
}""",
        "The sandbox starts a 5ms interval, increments a counter to 3, then **clears** it — the pattern of the skeleton.",
        body="<p>Timer skeleton</p>",
        js="""      let n = 0;
      let id = setInterval(frame, 5);
      function frame() {
        n++;
        if (n >= 3) {
          clearInterval(id);
          document.getElementById("demo").innerText = "stopped at n=" + n;
        }
      }""",
        wait_ms=1500,
        fence="javascript",
    ),
    P(
        "mymove",
        "Full animation — myMove() diagonal slide",
        [
            "`myMove` reads `#animate`, starts `pos` at 0, and every 5ms adds **1px** to `top` and `left`.",
            "When `pos == 350` it **clears** the interval (50px box in a 400px field → 350px of travel).",
            "`clearInterval(id)` at the start avoids stacking timers if you click Move twice.",
            "The snapshot calls `myMove()` immediately and waits so you see the square **away from the origin**.",
        ],
        """<button type="button" onclick="myMove()">Move</button>
<div id="container"><div id="animate"></div></div>
<script>
function myMove() {
  let id = null;
  const elem = document.getElementById("animate");
  let pos = 0;
  clearInterval(id);
  id = setInterval(frame, 5);
  function frame() {
    if (pos == 350) {
      clearInterval(id);
    } else {
      pos++;
      elem.style.top = pos + "px";
      elem.style.left = pos + "px";
    }
  }
}
</script>""",
        "After running, the red square has moved toward the bottom-right (`top`/`left` near **350px**, or mid-travel if the snap is early).",
        body='<button type="button" id="go">Move</button><div id="container"><div id="animate"></div></div>',
        css=ANIM_CSS,
        js="""      function myMove() {
        let id = null;
        const elem = document.getElementById("animate");
        let pos = 0;
        clearInterval(id);
        id = setInterval(frame, 5);
        function frame() {
          if (pos == 350) {
            clearInterval(id);
            document.getElementById("demo").innerText =
              "top=" + elem.style.top + " left=" + elem.style.left;
          } else {
            pos++;
            elem.style.top = pos + "px";
            elem.style.left = pos + "px";
            if (pos === 120) {
              document.getElementById("demo").innerText =
                "moving top=" + elem.style.top + " left=" + elem.style.left;
            }
          }
        }
      }
      myMove();""",
        wait_ms=8000,
    ),
]

ANIMATIONS_QA = qa(
    ("Why wrap the mover in a container?", ["So `top`/`left` are **relative to that box**, not the whole page."]),
    ("Which `position` values does W3Schools require?", ["Container **relative**, animated element **absolute**."]),
    ("How is the animation scheduled?", ["**`setInterval(frame, 5)`** — a 5ms timer."]),
    ("How do you stop it?", ["**`clearInterval(id)`** when the finish test is true."]),
    ("What does `myMove` change each tick?", ["`elem.style.top` and `elem.style.left` by **+1px**."]),
    ("Why `pos == 350`?", ["A 50px square in a 400px container travels **350px** before hitting the far edge."]),
    ("Why `clearInterval` at the start of `myMove`?", ["So a second click does not start a **second** timer on the same element."]),
    ("Is this the CSS `animation` property?", ["No — this page teaches **JavaScript timers** changing inline styles."]),
    ("What if the interval is large, like 500ms?", ["The motion looks **jerky**, not continuous."]),
    ("Can you animate `opacity` the same way?", ["Yes — any style you can set in JS, changed a little each frame."]),
)


def run(slug, title, records, intro, concepts, qa_items, summary, page):
    build_and_snap(
        slug,
        title,
        records,
        intro,
        concepts,
        qa_items,
        summary,
        [
            (title, BASE + page),
            ("MDN Document", "https://developer.mozilla.org/en-US/docs/Web/API/Document"),
        ],
    )


def main():
    run(
        "html-dom",
        "HTML DOM",
        HTML_DOM,
        "The HTML DOM is the browser’s tree of nodes for a page. JavaScript uses that tree to read and change HTML.",
        [
            "Document / Element / Attribute / Text are different **node types**.",
            "`getElementById` + `innerHTML` is the first practical access pattern.",
            "The DOM is a W3C/WHATWG standard (**Core**, **XML**, **HTML** parts).",
        ],
        HTML_DOM_QA,
        "Treat the page as a tree: look up nodes from `document`, then change content, style, structure, or events.",
        "js_htmldom.asp",
    )
    run(
        "html-dom-api",
        "HTML DOM API",
        HTML_DOM_API,
        "The DOM API is the methods and properties on `document` and elements that find, change, and create HTML.",
        [
            "Methods do actions; properties hold values.",
            "Selection: getElementById, getElementsByTagName, getElementsByClassName, querySelector, querySelectorAll.",
            "Content, attributes, structure (`createElement` / `appendChild` / `removeChild` / `replaceChild`), and `onclick`.",
        ],
        HTML_DOM_API_QA,
        "Start at `document`, select a node, then use properties (`innerHTML`, `style`) or methods (`setAttribute`, `appendChild`).",
        "js_htmldom_methods.asp",
    )
    run(
        "selecting-elements",
        "Selecting Elements",
        SELECTING,
        "Before you can change an element you must find it: id, tag, class, CSS selectors, or document collections.",
        [
            "`getElementById` returns one node or null (no `#` in the argument).",
            "`querySelector` is first-match CSS; `querySelectorAll` is every match.",
            "`document.forms`, `images`, `links`, `body`, `title` are HTML collections / shortcuts.",
        ],
        SELECTING_QA,
        "Pick the lookup that matches your markup: unique id, CSS selector, or a document collection — and remember first-vs-all.",
        "js_htmldom_elements.asp",
    )
    run(
        "changing-html",
        "Changing HTML",
        CHANGING_HTML,
        "The DOM lets JavaScript replace element HTML, change attributes such as `src`, and write the date into the page.",
        [
            "`innerHTML` replaces an element’s HTML content.",
            "Assign `element.attribute` (for example `img.src`) to change attributes.",
            "**Never** `document.write` after the document has loaded — it overwrites the page.",
        ],
        CHANGING_HTML_QA,
        "Prefer `innerHTML` / `textContent` / `src` assignments. Keep `document.write` off live pages.",
        "js_htmldom_html.asp",
    )
    run(
        "changing-css",
        "Changing CSS",
        CHANGING_CSS,
        "JavaScript sets inline CSS through `element.style.property`. Clicks can restyle or hide nodes.",
        [
            "Use camelCase CSS names on `element.style`.",
            "Events (click) are a natural time to change styles.",
            "`display:none` hides a node without deleting it.",
        ],
        CHANGING_CSS_QA,
        "`style` writes inline CSS. Combine it with events to restyle or hide elements on demand.",
        "js_htmldom_css.asp",
    )
    run(
        "form-validation",
        "Form Validation",
        FORM_VAL,
        "Forms can be checked with JavaScript (`return false`) or with HTML5 constraint validation (`required`, `min`, `pattern`, `:invalid`).",
        [
            "Client-side checks improve UX; **server-side** checks are required for safety.",
            "HTML `required` / `min` / `max` / `pattern` / `type` work without JS in modern browsers.",
            "CSS `:valid` / `:invalid` / `:required` / `:optional` / `:disabled` style those states.",
        ],
        FORM_VAL_QA,
        "Use HTML constraints first, add JS for custom rules, and always validate again on the server.",
        "js_validation.asp",
    )
    run(
        "dom-animations",
        "DOM Animations",
        ANIMATIONS,
        "A JavaScript animation is a timer that changes inline styles a little at a time inside a positioned container.",
        [
            "Container `position:relative`, mover `position:absolute`.",
            "`setInterval(frame, 5)` + `clearInterval` when done.",
            "`myMove` increments `top` and `left` until `pos == 350`.",
        ],
        ANIMATIONS_QA,
        "Position the box, then drive `top`/`left` (or any style) from a short interval until you clear it.",
        "js_htmldom_animate.asp",
    )


if __name__ == "__main__":
    main()
