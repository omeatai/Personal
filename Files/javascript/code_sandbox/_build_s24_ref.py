"""S24.8–24.9: Document Reference and Element Reference (one Example per table row)."""
from __future__ import annotations

from _dom_ui import P
from _gen_lib import build_and_snap

BASE = "https://www.w3schools.com/js/"


def qa(*items):
    return list(items)


def R(stem, title, desc, js, outcome, body="<p id='t'>Hello <b>World</b></p><p id='u'>Next</p>", extra=None, wait_ms=0):
    bullets = [
        f"**`{title}`** — {desc}",
        "This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).",
        "Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.",
    ]
    if extra:
        bullets.extend(extra)
    return P(stem, title, bullets, js.strip(), outcome, body=body, js=js, wait_ms=wait_ms, fence="javascript")


IFRAME = '<iframe id="f" style="width:100%;height:70px;border:1px solid #ccc;"></iframe>'

DOC = [
    R("activeelement", "activeElement", "Returns the currently focused element in the document",
      """      const inp = document.createElement("input");
      inp.id = "focusMe";
      document.body.insertBefore(inp, document.getElementById("demo"));
      inp.focus();
      document.getElementById("demo").innerText = document.activeElement && document.activeElement.id;""",
      "After `focus()`, `document.activeElement.id` is **focusMe** (or `body` if the engine ignores focus in headless).",
      body="<p>Focus target is created in script.</p>"),
    R("addeventlistener", "addEventListener()", "Attaches an event handler to the document",
      """      document.addEventListener("click", function handler() {
        document.getElementById("demo").innerText = "document clicked";
        document.removeEventListener("click", handler);
      });
      document.dispatchEvent(new MouseEvent("click", { bubbles: true }));""",
      "Dispatching click on the document runs the listener: **document clicked**."),
    R("adoptnode", "adoptNode()", "Adopts a node from another document",
      """      const other = document.getElementById("f").contentDocument;
      other.body.innerHTML = "<span id='x'>from iframe</span>";
      const node = document.adoptNode(other.getElementById("x"));
      document.body.appendChild(node);
      document.getElementById("demo").innerText = node.textContent + " owner=" + (node.ownerDocument === document);""",
      "`adoptNode` moves the span into this document; `ownerDocument === document` is **true**.",
      body=IFRAME),
    R("anchors", "anchors", "DEPRECATED collection of named anchors",
      """      let msg;
      try { msg = "anchors.length=" + (document.anchors ? document.anchors.length : document.anchors); }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\\n(deprecated — do not use in new code)";""",
      "The engine still exposes `anchors` or it is gone. Treat it as **deprecated**.",
      body='<a name="top">top</a>', extra=["Do **not** use `document.anchors` in new pages. Use `id` + `getElementById`."]),
    R("applets", "applets", "DEPRECATED collection of applets",
      """      let msg;
      try { msg = "applets=" + document.applets; }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\\n(deprecated — Java applets are gone)";""",
      "`applets` is **deprecated**. Java applet plugins are not part of the modern web.",
      extra=["Do **not** use `document.applets`."]),
    R("baseuri", "baseURI", "Returns the absolute base URI of a document",
      """      document.getElementById("demo").innerText = document.baseURI;""",
      "`document.baseURI` is the absolute URL of this file (a `file://` path in the snapshot pipeline)."),
    R("body", "body", "Sets or returns the document's <body> element",
      """      document.getElementById("demo").innerText = document.body.tagName + " children=" + document.body.children.length;""",
      "`document.body.tagName` is **BODY**."),
    R("charset", "charset", "DEPRECATED character-encoding alias",
      """      let msg;
      try { msg = "charset=" + document.charset; }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\\nUse characterSet instead";""",
      "`charset` may still equal UTF-8. Prefer **`characterSet`**. It is **deprecated**.",
      extra=["Use **`document.characterSet`**, not `charset`."]),
    R("characterset", "characterSet", "Returns the character encoding for the document",
      """      document.getElementById("demo").innerText = document.characterSet;""",
      "`document.characterSet` is typically **UTF-8**."),
    R("close", "close()", "Closes the output stream previously opened with document.open()",
      """      const d = document.getElementById("f").contentDocument;
      d.open();
      d.write("<p>stream</p>");
      d.close();
      document.getElementById("demo").innerText = "iframe=" + d.body.innerText;""",
      "After `open`/`write`/`close`, the iframe body contains **stream**.",
      body=IFRAME),
    R("cookie", "cookie", "Returns all name/value pairs of cookies in the document",
      """      document.cookie = "demo=1; SameSite=Lax";
      document.getElementById("demo").innerText = document.cookie || "(empty — file:// often blocks cookies)";""",
      "`document.cookie` shows **demo=1** when cookies are allowed; on `file://` it may be **empty**."),
    R("createattribute", "createAttribute()", "Creates an attribute node",
      """      const a = document.createAttribute("data-k");
      a.value = "v";
      document.getElementById("t").setAttributeNode(a);
      document.getElementById("demo").innerText = document.getElementById("t").getAttribute("data-k");""",
      "The paragraph gains **data-k=\"v\"** via `createAttribute` + `setAttributeNode`."),
    R("createcomment", "createComment()", "Creates a Comment node with the specified text",
      """      const c = document.createComment("note");
      document.getElementById("t").appendChild(c);
      document.getElementById("demo").innerText = c.nodeName + " " + c.nodeValue;""",
      "A comment node `#comment` with value **note** is appended."),
    R("createdocumentfragment", "createDocumentFragment()", "Creates an empty DocumentFragment node",
      """      const frag = document.createDocumentFragment();
      const s = document.createElement("span");
      s.textContent = "frag";
      frag.appendChild(s);
      document.getElementById("t").appendChild(frag);
      document.getElementById("demo").innerText = document.getElementById("t").innerText;""",
      "The fragment’s **frag** span is inserted in one operation; the fragment itself is empty after append."),
    R("createelement", "createElement()", "Creates an Element node",
      """      const el = document.createElement("em");
      el.textContent = "new";
      document.getElementById("t").appendChild(el);
      document.getElementById("demo").innerText = el.tagName + " " + el.textContent;""",
      "`createElement(\"em\")` builds an **EM** with text **new**."),
    R("createevent", "createEvent()", "Creates a new event (legacy)",
      """      let msg;
      try {
        const ev = document.createEvent("Event");
        ev.initEvent("ping", true, true);
        msg = ev.type + " bubbles=" + ev.bubbles;
      } catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\\nPrefer new Event('ping')";""",
      "`createEvent`/`initEvent` still work in many engines, or they throw. Prefer **`new Event()`**."),
    R("createtextnode", "createTextNode()", "Creates a Text node",
      """      const t = document.createTextNode("plain");
      document.getElementById("t").appendChild(t);
      document.getElementById("demo").innerText = t.nodeName + " " + JSON.stringify(t.nodeValue);""",
      "A `#text` node with value **plain** is appended."),
    R("defaultview", "defaultView", "Returns the window object associated with a document, or null",
      """      document.getElementById("demo").innerText = String(document.defaultView === window);""",
      "`document.defaultView === window` is **true** in a normal browser tab."),
    R("designmode", "designMode", "Controls whether the entire document should be editable",
      """      const d = document.getElementById("f").contentDocument;
      d.designMode = "on";
      document.getElementById("demo").innerText = "designMode=" + d.designMode;""",
      "The iframe document’s `designMode` is **on** (the whole iframe body becomes editable).",
      body=IFRAME),
    R("doctype", "doctype", "Returns the Document Type Declaration associated with the document",
      """      const dt = document.doctype;
      document.getElementById("demo").innerText = dt ? (dt.name + " " + dt.publicId) : "null";""",
      "`document.doctype.name` is **html** for a standard HTML5 doctype."),
    R("documentelement", "documentElement", "Returns the Document Element (`<html>`)",
      """      document.getElementById("demo").innerText = document.documentElement.tagName;""",
      "`document.documentElement.tagName` is **HTML**."),
    R("documentmode", "documentMode", "DEPRECATED IE document mode",
      """      document.getElementById("demo").innerText = "documentMode=" + document.documentMode + " (deprecated IE-only)";""",
      "`documentMode` is **undefined** in Chrome/Edge. It was an **IE** feature — do not use it.",
      extra=["Deprecated **Internet Explorer** API."]),
    R("documenturi", "documentURI", "Sets or returns the location of the document",
      """      document.getElementById("demo").innerText = document.documentURI;""",
      "`documentURI` is the document URL (same family as `document.URL`)."),
    R("domain", "domain", "Returns the domain name of the server that loaded the document",
      """      let msg;
      try { msg = "domain=" + JSON.stringify(document.domain); }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg;""",
      "On `file://` this is often **`\"\"`** or a security error. On http it is the host name."),
    R("domconfig", "domConfig", "DEPRECATED",
      """      document.getElementById("demo").innerText = "domConfig=" + document.domConfig + " (deprecated — unused)";""",
      "`domConfig` is **deprecated** and typically **undefined**.",
      extra=["Do not use `domConfig`."]),
    R("embeds", "embeds", "Returns a collection of all <embed> elements",
      """      document.getElementById("demo").innerText = "embeds=" + document.embeds.length;""",
      "`document.embeds.length` is **1** in this page.",
      body='<embed type="text/plain" width="1" height="1">'),
    R("execcommand", "execCommand()", "DEPRECATED document editing command",
      """      let msg;
      try {
        document.getElementById("t").focus();
        const ok = document.execCommand("selectAll");
        msg = "execCommand selectAll -> " + ok;
      } catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\\n(deprecated)";""",
      "`execCommand` may return a boolean or throw. It is **deprecated** — do not use it in new code.",
      extra=["Deprecated. Use the modern Selection / Clipboard APIs instead."]),
    R("forms", "forms", "Returns a collection of all <form> elements",
      """      document.getElementById("demo").innerText = "forms=" + document.forms.length + " id=" + document.forms[0].id;""",
      "`document.forms.length` is **1** and the form id is **frm**.",
      body='<form id="frm"><input name="n" value="x"></form>'),
    R("getelementbyid", "getElementById()", "Returns the element that has the ID attribute with the specified value",
      """      document.getElementById("demo").innerText = document.getElementById("t").textContent;""",
      "`getElementById(\"t\")` returns the Hello World paragraph."),
    R("getelementsbyclassname", "getElementsByClassName()", "Returns an HTMLCollection of elements with the specified class name",
      """      document.getElementById("demo").innerText = "n=" + document.getElementsByClassName("k").length;""",
      "Two `.k` nodes are found.",
      body='<p class="k">a</p><p class="k">b</p>'),
    R("getelementsbyname", "getElementsByName()", "Returns a live NodeList of elements with the specified name",
      """      document.getElementById("demo").innerText = "n=" + document.getElementsByName("user").length;""",
      "`getElementsByName(\"user\")` finds the named input (length **1**).",
      body='<input name="user" value="Ada">'),
    R("getelementsbytagname", "getElementsByTagName()", "Returns an HTMLCollection of elements with the specified tag name",
      """      document.getElementById("demo").innerText = "p=" + document.getElementsByTagName("p").length;""",
      "The page’s `<p>` count includes the sample paragraphs."),
    R("hasfocus", "hasFocus()", "Returns whether the document has focus",
      """      document.getElementById("demo").innerText = "hasFocus=" + document.hasFocus();""",
      "`hasFocus()` is a boolean — often **false** in headless screenshots, **true** in an interactive tab."),
    R("head", "head", "Returns the <head> element of the document",
      """      document.getElementById("demo").innerText = document.head.tagName + " titleChild=" + !!document.head.querySelector("title");""",
      "`document.head.tagName` is **HEAD**."),
    R("images", "images", "Returns a collection of all <img> elements",
      """      document.getElementById("demo").innerText = "images=" + document.images.length + " alt=" + document.images[0].alt;""",
      "`document.images.length` is **1**.",
      body="""<img alt="pic" width="16" height="16" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'/%3E">"""),
    R("implementation", "implementation", "Returns the DOMImplementation object that handles this document",
      """      const im = document.implementation;
      document.getElementById("demo").innerText = "hasFeature=" + typeof im.hasFeature + " createHTMLDocument=" + typeof im.createHTMLDocument;""",
      "`document.implementation` exposes `createHTMLDocument` (and legacy `hasFeature`)."),
    R("importnode", "importNode()", "Imports a node from another document",
      """      const other = document.getElementById("f").contentDocument;
      other.body.innerHTML = "<span id='x'>imported</span>";
      const copy = document.importNode(other.getElementById("x"), true);
      document.body.appendChild(copy);
      document.getElementById("demo").innerText = copy.textContent + " stillInIframe=" + !!other.getElementById("x");""",
      "`importNode(..., true)` **copies** the node; the iframe original still exists.",
      body=IFRAME),
    R("inputencoding", "inputEncoding", "DEPRECATED",
      """      document.getElementById("demo").innerText = "inputEncoding=" + document.inputEncoding + " (deprecated — use characterSet)";""",
      "`inputEncoding` may still report UTF-8. Prefer **`characterSet`**. **Deprecated**.",
      extra=["Deprecated alias of the encoding."]),
    R("lastmodified", "lastModified", "Returns the date and time the document was last modified",
      """      document.getElementById("demo").innerText = document.lastModified;""",
      "`lastModified` is a date string from the server (or file mtime)."),
    R("links", "links", "Returns all <a> and <area> elements that have an href",
      """      document.getElementById("demo").innerText = "links=" + document.links.length;""",
      "`document.links.length` is **1**.",
      body='<a href="https://example.com">ex</a>'),
    R("normalize", "normalize()", "Removes empty Text nodes, and joins adjacent text nodes",
      """      const p = document.getElementById("t");
      p.appendChild(document.createTextNode("A"));
      p.appendChild(document.createTextNode("B"));
      const before = p.childNodes.length;
      p.normalize();
      document.getElementById("demo").innerText = "before=" + before + " after=" + p.childNodes.length;""",
      "`normalize()` merges adjacent text nodes so `childNodes.length` **drops**."),
    R("normalizedocument", "normalizeDocument()", "DEPRECATED",
      """      let msg;
      try { msg = "normalizeDocument=" + typeof document.normalizeDocument; document.normalizeDocument && document.normalizeDocument(); }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\\n(deprecated)";""",
      "`normalizeDocument` is **deprecated** and usually missing. Use `node.normalize()`.",
      extra=["Do not use `normalizeDocument()`."]),
    R("open", "open()", "Opens an HTML output stream to collect output from document.write()",
      """      const d = document.getElementById("f").contentDocument;
      const stream = d.open();
      d.write("<p>opened</p>");
      d.close();
      document.getElementById("demo").innerText = "wrote into opened stream: " + d.body.innerText;""",
      "`open()` starts a new stream; `write` then fills the iframe with **opened**.",
      body=IFRAME),
    R("queryselector", "querySelector()", "Returns the first element that matches a CSS selector",
      """      document.getElementById("demo").innerText = document.querySelector("#t b").textContent;""",
      "`querySelector(\"#t b\")` returns **World**."),
    R("queryselectorall", "querySelectorAll()", "Returns a static NodeList of all matching elements",
      """      document.getElementById("demo").innerText = "n=" + document.querySelectorAll("p").length;""",
      "`querySelectorAll(\"p\")` counts the sample paragraphs."),
    R("readystate", "readyState", "Returns the (loading) status of the document",
      """      document.getElementById("demo").innerText = document.readyState;""",
      "By the time this script runs, `readyState` is **interactive** or **complete**."),
    R("referrer", "referrer", "Returns the URL of the document that loaded the current document",
      """      document.getElementById("demo").innerText = JSON.stringify(document.referrer);""",
      "`referrer` is often **`\"\"`** for a `file://` screenshot (no previous page)."),
    R("removeeventlistener", "removeEventListener()", "Removes an event handler attached with addEventListener",
      """      function ping() { document.getElementById("demo").innerText = "should not run"; }
      document.addEventListener("keyup", ping);
      document.removeEventListener("keyup", ping);
      document.dispatchEvent(new KeyboardEvent("keyup"));
      document.getElementById("demo").innerText = (document.getElementById("demo").innerText === "should not run")
        ? "listener still there" : "removed — keyup did nothing";""",
      "After `removeEventListener`, the `keyup` handler does **not** run."),
    R("renamenode", "renameNode()", "DEPRECATED",
      """      let msg;
      try { msg = "renameNode=" + typeof document.renameNode; }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + " (deprecated)";""",
      "`renameNode` is **deprecated** and not available in HTML browsers.",
      extra=["Do not use `renameNode()`."]),
    R("scripts", "scripts", "Returns a collection of <script> elements",
      """      document.getElementById("demo").innerText = "scripts=" + document.scripts.length;""",
      "`document.scripts.length` is at least **1**."),
    R("stricterrorchecking", "strictErrorChecking", "DEPRECATED",
      """      document.getElementById("demo").innerText = "strictErrorChecking=" + document.strictErrorChecking + " (deprecated)";""",
      "`strictErrorChecking` is **deprecated** / typically **undefined**.",
      extra=["Do not use `strictErrorChecking`."]),
    R("title", "title", "Sets or returns the title of the document",
      """      document.title = "Doc Ref";
      document.getElementById("demo").innerText = document.title;""",
      "`document.title` is set to **Doc Ref**."),
    R("url", "URL", "Returns the full URL of the HTML document",
      """      document.getElementById("demo").innerText = document.URL;""",
      "`document.URL` is the full document address."),
    R("write", "write()", "Writes HTML expressions or JavaScript code to a document",
      """      const d = document.getElementById("f").contentDocument;
      d.open();
      d.write("<strong>written</strong>");
      d.close();
      document.getElementById("demo").innerText = d.body.innerHTML;""",
      "The iframe contains **`<strong>written</strong>`**. Never `write` on a loaded main page.",
      body=IFRAME,
      extra=["After load, `write` **overwrites** the document. Use an iframe or `innerHTML` instead."]),
    R("writeln", "writeln()", "Same as write(), but adds a newline character after each statement",
      """      const d = document.getElementById("f").contentDocument;
      d.open();
      d.writeln("<pre>line1");
      d.writeln("line2</pre>");
      d.close();
      document.getElementById("demo").innerText = JSON.stringify(d.body.innerText);""",
      "`writeln` inserts a **newline** after each call (visible inside `<pre>`).",
      body=IFRAME),
]

DOC_QA = qa(
    ("What is `document.documentElement`?", ["The root **`<html>`** element."]),
    ("What encoding property should you use?", ["**`characterSet`**. `charset` / `inputEncoding` are deprecated."]),
    ("Does `adoptNode` copy or move?", ["It **moves** the node to this document (`ownerDocument` changes)."]),
    ("Does `importNode` copy or move?", ["It **copies**. The original stays in the other document."]),
    ("What does `readyState` become after load?", ["**`complete`** (it may be `interactive` while scripts still run)."]),
    ("Why is `document.write` dangerous after load?", ["It **replaces** the entire document."]),
    ("How do you undo `addEventListener`?", ["Call **`removeEventListener`** with the **same** function reference."]),
    ("What is `document.defaultView`?", ["The associated **`window`** (or `null`)."]),
    ("Should you use `execCommand`?", ["No — it is **deprecated**."]),
    ("What does `normalize()` do on a node?", ["Merges adjacent **text** nodes and removes empty ones."]),
    ("What is in `document.forms`?", ["Every **`<form>`** in the document."]),
    ("What does `hasFocus()` tell you?", ["Whether **this document** currently has focus."]),
)


EL_BODY = """
<div id="wrap" title="box" lang="en" dir="ltr" accesskey="w" tabindex="0" style="padding:8px;border:4px solid navy;width:220px;height:80px;overflow:auto;">
  <p id="t" class="note item" data-k="v">Hello <b id="b">World</b></p>
  <p id="u">Next</p>
</div>
<input id="inp" value="x">
"""


def E(stem, title, desc, js, outcome, extra=None, body=EL_BODY, wait_ms=0):
    return R(stem, title, desc, js, outcome, body=body, extra=extra, wait_ms=wait_ms)


EL = [
    E("accesskey", "accessKey", "Sets or returns the accesskey attribute of an element",
      """      const w = document.getElementById("wrap");
      document.getElementById("demo").innerText = "accessKey=" + w.accessKey;
      w.accessKey = "q";
      document.getElementById("demo").innerText += "\\nafter=" + w.accessKey;""",
      "`accessKey` starts as **w** and is set to **q**."),
    E("addeventlistener", "addEventListener()", "Attaches an event handler to an element",
      """      const t = document.getElementById("t");
      t.addEventListener("click", function () { document.getElementById("demo").innerText = "p clicked"; });
      t.click();""",
      "The paragraph listener runs on `click()`: **p clicked**."),
    E("after", "after()", "Inserts nodes or strings after an element",
      """      document.getElementById("t").after("AFTER");
      document.getElementById("demo").innerText = document.getElementById("wrap").innerText.replace(/\\s+/g, " ");""",
      "The string **AFTER** is inserted as a sibling after `#t`."),
    E("append", "append()", "Appends nodes or strings after the last child",
      """      document.getElementById("t").append("!");
      document.getElementById("demo").innerText = document.getElementById("t").textContent;""",
      "`append(\"!\")` adds **!** after Hello World."),
    E("appendchild", "appendChild()", "Adds a new child node after the last child",
      """      const s = document.createElement("span");
      s.textContent = "+";
      document.getElementById("t").appendChild(s);
      document.getElementById("demo").innerText = document.getElementById("t").innerHTML;""",
      "A `<span>+</span>` is the last child of `#t`."),
    E("attributes", "attributes", "Returns a NamedNodeMap of an element's attributes",
      """      const a = document.getElementById("t").attributes;
      document.getElementById("demo").innerText = "n=" + a.length + " id=" + a.getNamedItem("id").value;""",
      "`attributes` includes **id**, **class**, and **data-k**."),
    E("before", "before()", "Inserts nodes or strings before an element",
      """      document.getElementById("u").before("BEFORE");
      document.getElementById("demo").innerText = document.getElementById("wrap").innerText.replace(/\\s+/g, " ");""",
      "**BEFORE** is inserted as a sibling in front of `#u`."),
    E("blur", "blur()", "Removes focus from an element",
      """      const inp = document.getElementById("inp");
      inp.focus();
      const a = document.activeElement && document.activeElement.id;
      inp.blur();
      const b = document.activeElement && document.activeElement.id;
      document.getElementById("demo").innerText = "focused=" + a + " afterBlur=" + b;""",
      "`blur()` moves focus off the input (`afterBlur` is no longer **inp** if focus worked)."),
    E("childelementcount", "childElementCount", "Returns an element's number of child elements",
      """      document.getElementById("demo").innerText = "wrap=" + document.getElementById("wrap").childElementCount;""",
      "`#wrap` has **2** child elements (`#t` and `#u`)."),
    E("childnodes", "childNodes", "Returns a NodeList of an element's child nodes",
      """      document.getElementById("demo").innerText = "t.childNodes=" + document.getElementById("t").childNodes.length;""",
      "`#t.childNodes` includes the Hello text node and the `<b>` (length **2** or more if whitespace)."),
    E("children", "children", "Returns an HTMLCollection of an element's child elements",
      """      document.getElementById("demo").innerText = "t.children=" + document.getElementById("t").children.length + " " + document.getElementById("t").children[0].tagName;""",
      "`#t.children.length` is **1** (`B`)."),
    E("classlist", "classList", "Returns the class name(s) of an element as a DOMTokenList",
      """      const cl = document.getElementById("t").classList;
      cl.add("extra");
      document.getElementById("demo").innerText = [...cl].join(",");""",
      "`classList` is **note,item,extra** after `add`."),
    E("classname", "className", "Sets or returns the value of the class attribute",
      """      const t = document.getElementById("t");
      document.getElementById("demo").innerText = t.className;
      t.className = "only";
      document.getElementById("demo").innerText += " -> " + t.className;""",
      "`className` starts as **note item** and is replaced with **only**."),
    E("click", "click()", "Simulates a mouse-click on an element",
      """      const t = document.getElementById("t");
      t.addEventListener("click", () => { document.getElementById("demo").innerText = "got click()"; });
      t.click();""",
      "`click()` fires the listener: **got click()**."),
    E("clientheight", "clientHeight", "Returns the height of an element, including padding",
      """      document.getElementById("demo").innerText = "clientHeight=" + document.getElementById("wrap").clientHeight;""",
      "`clientHeight` is the inner height including padding (a pixel number around the styled 80px box)."),
    E("clientleft", "clientLeft", "Returns the width of the left border of an element",
      """      document.getElementById("demo").innerText = "clientLeft=" + document.getElementById("wrap").clientLeft;""",
      "`clientLeft` is **4** (the navy border width) in this sandbox."),
    E("clienttop", "clientTop", "Returns the width of the top border of an element",
      """      document.getElementById("demo").innerText = "clientTop=" + document.getElementById("wrap").clientTop;""",
      "`clientTop` is **4** — the top border width."),
    E("clientwidth", "clientWidth", "Returns the width of an element, including padding",
      """      document.getElementById("demo").innerText = "clientWidth=" + document.getElementById("wrap").clientWidth;""",
      "`clientWidth` includes padding, excludes border and scrollbar."),
    E("clonenode", "cloneNode()", "Clones an element",
      """      const c = document.getElementById("t").cloneNode(true);
      document.getElementById("demo").innerText = "clone=" + c.innerHTML + " sameId=" + (c.id === "t");""",
      "`cloneNode(true)` deep-copies HTML. The clone is **not** the same node (`isSameNode` would be false)."),
    E("closest", "closest()", "Searches the DOM tree for the closest ancestor that matches a CSS selector",
      """      document.getElementById("demo").innerText = document.getElementById("b").closest("#wrap").id;""",
      "`#b.closest(\"#wrap\")` is the wrapper **wrap**."),
    E("comparedocumentposition", "compareDocumentPosition()", "Compares the document position of two elements",
      """      const t = document.getElementById("t");
      const u = document.getElementById("u");
      document.getElementById("demo").innerText = "t vs u = " + t.compareDocumentPosition(u);""",
      "The bitmask is non-zero; `DOCUMENT_POSITION_FOLLOWING` (4) is typically set because `#u` follows `#t`."),
    E("contains", "contains()", "Returns true if a node is a descendant of a node",
      """      const w = document.getElementById("wrap");
      document.getElementById("demo").innerText = "wrap contains b=" + w.contains(document.getElementById("b"));""",
      "`wrap.contains(#b)` is **true**."),
    E("contenteditable", "contentEditable", "Sets or returns whether the content of an element is editable",
      """      const t = document.getElementById("t");
      t.contentEditable = "true";
      document.getElementById("demo").innerText = t.contentEditable;""",
      "`contentEditable` is **true** after assignment."),
    E("dir", "dir", "Sets or returns the value of the dir attribute",
      """      const w = document.getElementById("wrap");
      document.getElementById("demo").innerText = w.dir;
      w.dir = "rtl";
      document.getElementById("demo").innerText += " -> " + w.dir;""",
      "`dir` starts as **ltr** and is set to **rtl**."),
    E("firstchild", "firstChild", "Returns the first child node of an element",
      """      const n = document.getElementById("t").firstChild;
      document.getElementById("demo").innerText = n.nodeName + " " + JSON.stringify(n.nodeValue);""",
      "`#t.firstChild` is the **Hello ** text node (or a whitespace text node)."),
    E("firstelementchild", "firstElementChild", "Returns the first child element of an element",
      """      document.getElementById("demo").innerText = document.getElementById("t").firstElementChild.tagName;""",
      "`firstElementChild` of `#t` is **B** (skips text nodes)."),
    E("focus", "focus()", "Gives focus to an element",
      """      document.getElementById("inp").focus();
      document.getElementById("demo").innerText = "active=" + (document.activeElement && document.activeElement.id);""",
      "After `focus()`, `activeElement` is **inp** when the engine allows it."),
    E("getattribute", "getAttribute()", "Returns the value of an element's attribute",
      """      document.getElementById("demo").innerText = document.getElementById("t").getAttribute("data-k");""",
      "`getAttribute(\"data-k\")` is **v**."),
    E("getattributenode", "getAttributeNode()", "Returns an attribute node",
      """      const n = document.getElementById("t").getAttributeNode("id");
      document.getElementById("demo").innerText = n.name + "=" + n.value;""",
      "The `id` Attr node has value **t**."),
    E("getboundingclientrect", "getBoundingClientRect()", "Returns size and position relative to the viewport",
      """      const r = document.getElementById("wrap").getBoundingClientRect();
      document.getElementById("demo").innerText = "w=" + Math.round(r.width) + " h=" + Math.round(r.height) + " top=" + Math.round(r.top);""",
      "The rect reports **width/height/top** in CSS pixels for `#wrap`."),
    E("getelementsbyclassname", "getElementsByClassName()", "Returns child elements with a given class name",
      """      document.getElementById("demo").innerText = "n=" + document.getElementById("wrap").getElementsByClassName("note").length;""",
      "`wrap.getElementsByClassName(\"note\")` finds **#t** (length **1**)."),
    E("getelementsbytagname", "getElementsByTagName()", "Returns child elements with a given tag name",
      """      document.getElementById("demo").innerText = "p=" + document.getElementById("wrap").getElementsByTagName("p").length;""",
      "Two `<p>` children live under `#wrap`."),
    E("hasattribute", "hasAttribute()", "Returns true if an element has a given attribute",
      """      const t = document.getElementById("t");
      document.getElementById("demo").innerText = "data-k=" + t.hasAttribute("data-k") + " href=" + t.hasAttribute("href");""",
      "`hasAttribute(\"data-k\")` is **true**; `href` is **false**."),
    E("hasattributes", "hasAttributes()", "Returns true if an element has any attributes",
      """      document.getElementById("demo").innerText = "t=" + document.getElementById("t").hasAttributes();""",
      "`#t.hasAttributes()` is **true**."),
    E("haschildnodes", "hasChildNodes()", "Returns true if an element has any child nodes",
      """      document.getElementById("demo").innerText = "t=" + document.getElementById("t").hasChildNodes();""",
      "`hasChildNodes()` is **true** for `#t`."),
    E("id", "id", "Sets or returns the value of the id attribute",
      """      const t = document.getElementById("t");
      document.getElementById("demo").innerText = t.id;
      t.id = "renamed";
      document.getElementById("demo").innerText += " -> " + document.getElementById("renamed").id;""",
      "`id` is rewritten from **t** to **renamed**."),
    E("innerhtml", "innerHTML", "Sets or returns the content of an element",
      """      const t = document.getElementById("t");
      document.getElementById("demo").innerText = t.innerHTML;
      t.innerHTML = "<i>x</i>";
      document.getElementById("demo").innerText += " -> " + t.innerHTML;""",
      "`innerHTML` includes **`<b>`**, then is replaced with **`<i>x</i>`**."),
    E("innertext", "innerText", "Sets or returns the rendered text content of a node",
      """      document.getElementById("demo").innerText = JSON.stringify(document.getElementById("t").innerText);""",
      "`innerText` is the visible string **Hello World** (layout-aware)."),
    E("insertadjacentelement", "insertAdjacentElement()", "Inserts a new element at a position relative to an element",
      """      const s = document.createElement("span");
      s.textContent = "X";
      document.getElementById("t").insertAdjacentElement("afterend", s);
      document.getElementById("demo").innerText = document.getElementById("wrap").innerText.replace(/\\s+/g, " ");""",
      "**X** is inserted after `#t` (`afterend`)."),
    E("insertadjacenthtml", "insertAdjacentHTML()", "Inserts HTML at a position relative to an element",
      """      document.getElementById("t").insertAdjacentHTML("beforeend", "<i>!</i>");
      document.getElementById("demo").innerText = document.getElementById("t").innerHTML;""",
      "`beforeend` adds **`<i>!</i>`** inside `#t`."),
    E("insertadjacenttext", "insertAdjacentText()", "Inserts text at a position relative to an element",
      """      document.getElementById("t").insertAdjacentText("beforeend", "!!");
      document.getElementById("demo").innerText = document.getElementById("t").textContent;""",
      "Plain **!!** is appended as text (not parsed as HTML)."),
    E("insertbefore", "insertBefore()", "Inserts a new child node before an existing child node",
      """      const s = document.createElement("span");
      s.textContent = "0";
      const wrap = document.getElementById("wrap");
      wrap.insertBefore(s, document.getElementById("u"));
      document.getElementById("demo").innerText = wrap.innerText.replace(/\\s+/g, " ");""",
      "**0** is inserted before `#u`."),
    E("iscontenteditable", "isContentEditable", "Returns true if an element's content is editable",
      """      const t = document.getElementById("t");
      document.getElementById("demo").innerText = "before=" + t.isContentEditable;
      t.contentEditable = "true";
      document.getElementById("demo").innerText += " after=" + t.isContentEditable;""",
      "`isContentEditable` becomes **true** after `contentEditable = \"true\"`."),
    E("isdefaultnamespace", "isDefaultNamespace()", "Returns true if a given namespaceURI is the default",
      """      const htmlNS = "http://www.w3.org/1999/xhtml";
      document.getElementById("demo").innerText = String(document.getElementById("t").isDefaultNamespace(htmlNS));""",
      "For an HTML element, `isDefaultNamespace(XHTML ns)` is **true**."),
    E("isequalnode", "isEqualNode()", "Checks if two elements are equal",
      """      const a = document.createElement("p");
      const b = document.createElement("p");
      a.className = b.className = "x";
      document.getElementById("demo").innerText = "equal=" + a.isEqualNode(b) + " same=" + a.isSameNode(b);""",
      "Two separately created equal `<p class=\"x\">` nodes: **isEqualNode true**, **isSameNode false**."),
    E("issamenode", "isSameNode()", "Checks if two elements are the same node",
      """      const t = document.getElementById("t");
      document.getElementById("demo").innerText = "same=" + t.isSameNode(document.getElementById("t")) + " other=" + t.isSameNode(document.getElementById("u"));""",
      "`t.isSameNode(t)` is **true**; vs `#u` is **false**."),
    E("issupported", "isSupported()", "DEPRECATED",
      """      let msg;
      try { msg = "isSupported=" + typeof document.getElementById("t").isSupported; }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + " (deprecated)";""",
      "`isSupported()` is **deprecated** and typically missing.",
      extra=["Do not use `isSupported()`."]),
    E("lang", "lang", "Sets or returns the value of the lang attribute",
      """      const w = document.getElementById("wrap");
      document.getElementById("demo").innerText = w.lang + " -> ";
      w.lang = "fr";
      document.getElementById("demo").innerText += w.lang;""",
      "`lang` goes from **en** to **fr**."),
    E("lastchild", "lastChild", "Returns the last child node of an element",
      """      const n = document.getElementById("wrap").lastChild;
      document.getElementById("demo").innerText = n.nodeName + " id=" + (n.id || "");""",
      "`wrap.lastChild` is `#u` or a trailing whitespace text node — the snap prints its `nodeName`."),
    E("lastelementchild", "lastElementChild", "Returns the last child element of an element",
      """      document.getElementById("demo").innerText = document.getElementById("wrap").lastElementChild.id;""",
      "`lastElementChild` of `#wrap` is **u**."),
    E("matches", "matches()", "Returns true if an element is matched by a given CSS selector",
      """      document.getElementById("demo").innerText = "p.note=" + document.getElementById("t").matches("p.note");""",
      "`#t.matches(\"p.note\")` is **true**."),
    E("namespaceuri", "namespaceURI", "Returns the namespace URI of an element",
      """      document.getElementById("demo").innerText = document.getElementById("t").namespaceURI;""",
      "HTML elements use **`http://www.w3.org/1999/xhtml`**."),
    E("nextsibling", "nextSibling", "Returns the next node at the same tree level",
      """      const n = document.getElementById("t").nextSibling;
      document.getElementById("demo").innerText = n && (n.nodeName + " " + (n.id || JSON.stringify(n.nodeValue)));""",
      "`nextSibling` may be a **whitespace text node** between `#t` and `#u`."),
    E("nextelementsibling", "nextElementSibling", "Returns the next element at the same tree level",
      """      document.getElementById("demo").innerText = document.getElementById("t").nextElementSibling.id;""",
      "`nextElementSibling` of `#t` is **u** (skips text)."),
    E("nodename", "nodeName", "Returns the name of a node",
      """      document.getElementById("demo").innerText = document.getElementById("t").nodeName;""",
      "`nodeName` for a paragraph is **P**."),
    E("nodetype", "nodeType", "Returns the node type of a node",
      """      document.getElementById("demo").innerText = "el=" + document.getElementById("t").nodeType + " text=" + document.getElementById("t").firstChild.nodeType;""",
      "Element is **1**; text is **3**."),
    E("nodevalue", "nodeValue", "Sets or returns the value of a node",
      """      const text = document.getElementById("t").firstChild;
      document.getElementById("demo").innerText = JSON.stringify(text.nodeValue);""",
      "`nodeValue` of the first text child is **Hello ** (element `nodeValue` is null)."),
    E("normalize", "normalize()", "Joins adjacent text nodes and removes empty text nodes",
      """      const t = document.getElementById("t");
      t.appendChild(document.createTextNode("A"));
      t.appendChild(document.createTextNode("B"));
      const before = t.childNodes.length;
      t.normalize();
      document.getElementById("demo").innerText = "before=" + before + " after=" + t.childNodes.length;""",
      "`normalize()` reduces `childNodes.length` by merging **A** and **B**."),
    E("offsetheight", "offsetHeight", "Returns height including padding, border and scrollbar",
      """      document.getElementById("demo").innerText = "offsetHeight=" + document.getElementById("wrap").offsetHeight;""",
      "`offsetHeight` is larger than `clientHeight` because it includes the **border**."),
    E("offsetwidth", "offsetWidth", "Returns width including padding, border and scrollbar",
      """      document.getElementById("demo").innerText = "offsetWidth=" + document.getElementById("wrap").offsetWidth;""",
      "`offsetWidth` includes the 4px border on both sides."),
    E("offsetleft", "offsetLeft", "Returns the horizontal offset position of an element",
      """      document.getElementById("demo").innerText = "offsetLeft=" + document.getElementById("wrap").offsetLeft;""",
      "`offsetLeft` is the pixel offset from `offsetParent`."),
    E("offsetparent", "offsetParent", "Returns the offset container of an element",
      """      const p = document.getElementById("wrap").offsetParent;
      document.getElementById("demo").innerText = p ? p.tagName : "null";""",
      "`offsetParent` is typically **BODY** (or a positioned ancestor)."),
    E("offsettop", "offsetTop", "Returns the vertical offset position of an element",
      """      document.getElementById("demo").innerText = "offsetTop=" + document.getElementById("wrap").offsetTop;""",
      "`offsetTop` is the vertical offset from `offsetParent`."),
    E("outerhtml", "outerHTML", "Sets or returns the element including its start and end tags",
      """      document.getElementById("demo").innerText = document.getElementById("u").outerHTML;""",
      "`#u.outerHTML` includes **`<p id=\"u\">Next</p>`**."),
    E("outertext", "outerText", "Sets or returns the outer text content of a node",
      """      document.getElementById("demo").innerText = "outerText=" + document.getElementById("u").outerText;""",
      "`outerText` of `#u` is **Next**. Assigning it would **replace the element** with text."),
    E("ownerdocument", "ownerDocument", "Returns the root document object for an element",
      """      document.getElementById("demo").innerText = String(document.getElementById("t").ownerDocument === document);""",
      "`ownerDocument === document` is **true**."),
    E("parentnode", "parentNode", "Returns the parent node of an element",
      """      document.getElementById("demo").innerText = document.getElementById("t").parentNode.id;""",
      "`#t.parentNode` is **wrap**."),
    E("parentelement", "parentElement", "Returns the parent element node of an element",
      """      document.getElementById("demo").innerText = document.getElementById("t").parentElement.id;""",
      "`parentElement` is also **wrap** (null if the parent is not an Element)."),
    E("previoussibling", "previousSibling", "Returns the previous node at the same tree level",
      """      const n = document.getElementById("u").previousSibling;
      document.getElementById("demo").innerText = n && (n.nodeName + " " + (n.id || ""));""",
      "`previousSibling` of `#u` may be whitespace text, not `#t`."),
    E("previouselementsibling", "previousElementSibling", "Returns the previous element at the same tree level",
      """      document.getElementById("demo").innerText = document.getElementById("u").previousElementSibling.id;""",
      "`previousElementSibling` of `#u` is **t**."),
    E("queryselector", "querySelector()", "Returns the first descendant that matches a CSS selector",
      """      document.getElementById("demo").innerText = document.getElementById("wrap").querySelector("b").id;""",
      "`wrap.querySelector(\"b\")` is **b**."),
    E("queryselectorall", "querySelectorAll()", "Returns all descendants that match a CSS selector",
      """      document.getElementById("demo").innerText = "p=" + document.getElementById("wrap").querySelectorAll("p").length;""",
      "`querySelectorAll(\"p\")` under wrap is **2**."),
    E("remove", "remove()", "Removes an element from the DOM",
      """      document.getElementById("u").remove();
      document.getElementById("demo").innerText = "u=" + document.getElementById("u");""",
      "After `remove()`, `getElementById(\"u\")` is **null**."),
    E("removeattribute", "removeAttribute()", "Removes an attribute from an element",
      """      const t = document.getElementById("t");
      t.removeAttribute("data-k");
      document.getElementById("demo").innerText = "has=" + t.hasAttribute("data-k");""",
      "`data-k` is gone: `hasAttribute` is **false**."),
    E("removeattributenode", "removeAttributeNode()", "Removes an attribute node, and returns the removed node",
      """      const t = document.getElementById("t");
      const node = t.removeAttributeNode(t.getAttributeNode("data-k"));
      document.getElementById("demo").innerText = node.name + "=" + node.value + " has=" + t.hasAttribute("data-k");""",
      "The removed Attr is **data-k=v**; the element no longer has that attribute."),
    E("removechild", "removeChild()", "Removes a child node from an element",
      """      const wrap = document.getElementById("wrap");
      wrap.removeChild(document.getElementById("u"));
      document.getElementById("demo").innerText = "u=" + document.getElementById("u");""",
      "`removeChild(#u)` detaches Next; `getElementById(\"u\")` is **null**."),
    E("removeeventlistener", "removeEventListener()", "Removes an event handler attached with addEventListener",
      """      const t = document.getElementById("t");
      function ping() { document.getElementById("demo").innerText = "ran"; }
      t.addEventListener("click", ping);
      t.removeEventListener("click", ping);
      t.click();
      if (document.getElementById("demo").innerText !== "ran") {
        document.getElementById("demo").innerText = "listener removed";
      }""",
      "After removal, `click()` does **not** print **ran**."),
    E("replacechild", "replaceChild()", "Replaces a child node in an element",
      """      const neu = document.createElement("p");
      neu.id = "v";
      neu.textContent = "Replaced";
      document.getElementById("wrap").replaceChild(neu, document.getElementById("u"));
      document.getElementById("demo").innerText = document.getElementById("v").textContent;""",
      "`#u` is replaced by **Replaced** (`#v`)."),
    E("scrollheight", "scrollHeight", "Returns the entire height of an element, including padding",
      """      document.getElementById("demo").innerText = "scrollHeight=" + document.getElementById("wrap").scrollHeight;""",
      "`scrollHeight` is the content height, which can exceed the visible box."),
    E("scrollintoview", "scrollIntoView()", "Scrolls the element into the visible area of the browser window",
      """      document.getElementById("u").scrollIntoView();
      document.getElementById("demo").innerText = "scrollTop=" + document.getElementById("wrap").scrollTop;""",
      "`scrollIntoView()` may change `scrollTop` so `#u` is visible (0 if everything already fits)."),
    E("scrollleft", "scrollLeft", "Sets or returns horizontal scroll pixels",
      """      const w = document.getElementById("wrap");
      w.scrollLeft = 10;
      document.getElementById("demo").innerText = "scrollLeft=" + w.scrollLeft;""",
      "`scrollLeft` is set to **10** (may clamp to **0** if there is no overflow-x)."),
    E("scrolltop", "scrollTop", "Sets or returns vertical scroll pixels",
      """      const w = document.getElementById("wrap");
      w.scrollTop = 20;
      document.getElementById("demo").innerText = "scrollTop=" + w.scrollTop;""",
      "`scrollTop` is set toward **20** when the box can scroll."),
    E("scrollwidth", "scrollWidth", "Returns the entire width of an element, including padding",
      """      document.getElementById("demo").innerText = "scrollWidth=" + document.getElementById("wrap").scrollWidth;""",
      "`scrollWidth` is the full content width including overflow."),
    E("setattribute", "setAttribute()", "Sets or changes an attribute's value",
      """      const t = document.getElementById("t");
      t.setAttribute("data-k", "z");
      document.getElementById("demo").innerText = t.getAttribute("data-k");""",
      "`data-k` is now **z**."),
    E("setattributenode", "setAttributeNode()", "Sets or changes an attribute node",
      """      const a = document.createAttribute("data-n");
      a.value = "9";
      document.getElementById("t").setAttributeNode(a);
      document.getElementById("demo").innerText = document.getElementById("t").getAttribute("data-n");""",
      "`setAttributeNode` attaches **data-n=\"9\"**."),
    E("style", "style", "Sets or returns the value of the style attribute",
      """      const t = document.getElementById("t");
      t.style.color = "crimson";
      document.getElementById("demo").innerText = t.style.color;""",
      "`style.color` is **crimson** (inline)."),
    E("tabindex", "tabIndex", "Sets or returns the value of the tabindex attribute",
      """      const w = document.getElementById("wrap");
      document.getElementById("demo").innerText = String(w.tabIndex);
      w.tabIndex = 3;
      document.getElementById("demo").innerText += " -> " + w.tabIndex;""",
      "`tabIndex` starts at **0** and is set to **3**."),
    E("tagname", "tagName", "Returns the tag name of an element",
      """      document.getElementById("demo").innerText = document.getElementById("t").tagName;""",
      "`tagName` is **P**."),
    E("textcontent", "textContent", "Sets or returns the textual content of a node and its descendants",
      """      document.getElementById("demo").innerText = JSON.stringify(document.getElementById("t").textContent);""",
      "`textContent` concatenates descendant text: **Hello World**."),
    E("title", "title", "Sets or returns the value of the title attribute (tooltip)",
      """      const w = document.getElementById("wrap");
      document.getElementById("demo").innerText = w.title;
      w.title = "tip";
      document.getElementById("demo").innerText += " -> " + w.title;""",
      "`title` goes from **box** to **tip**."),
    E("tostring", "toString()", "Converts an element to a string",
      """      document.getElementById("demo").innerText = document.getElementById("t").toString();""",
      "`toString()` on an element is typically **`[object HTMLParagraphElement]`**."),
]

EL_QA = qa(
    ("What is the difference between `childNodes` and `children`?", ["`childNodes` includes **text/comment** nodes. `children` is **elements only**."]),
    ("`nextSibling` vs `nextElementSibling`?", ["The first can be **whitespace**. The second skips to the next **element**."]),
    ("Does `cloneNode(true)` copy descendants?", ["Yes — **deep** clone. `false` copies only the node itself."]),
    ("What does `closest(\"#wrap\")` do from `#b`?", ["Walks **up** the tree until it finds `#wrap`."]),
    ("`isEqualNode` vs `isSameNode`?", ["Equal means same structure/values. Same means **one object** in memory."]),
    ("What does `remove()` do?", ["Detaches **that element** from the tree (no parent argument)."]),
    ("Does `innerHTML` include the element’s own tags?", ["No — that is **`outerHTML`**."]),
    ("What unit are `clientWidth` / `offsetWidth` in?", ["**CSS pixels** (numbers, not `\"px\"` strings)."]),
    ("How do you add a class without wiping others?", ["Use **`classList.add`**, not `className = ...` (that replaces the whole string)."]),
    ("What does `matches(\"p.note\")` return for `#t`?", ["**true** — it is a `p` with class `note`."]),
    ("Should you call `isSupported()`?", ["No — **deprecated**."]),
    ("What does `append(\"!\")` accept that `appendChild` does not?", ["**Strings** (and several nodes). `appendChild` needs a Node."]),
)


def main():
    build_and_snap(
        "document-reference",
        "Document Reference",
        DOC,
        "The HTML DOM Document object is the owner of the page. This catalog rebuilds **every** W3Schools Document property and method row (January 2026 table), including deprecated APIs.",
        [
            "Selection methods (`getElementById`, `querySelector`, collections like `forms` / `images`).",
            "Create methods (`createElement`, `createTextNode`, `createDocumentFragment`).",
            "Deprecated rows still run (or catch) and tell you **not** to use them.",
        ],
        DOC_QA,
        "Use `document` as the entry point. Prefer `characterSet`, `querySelector`, and `createElement`. Avoid write-after-load and the deprecated rows.",
        [
            ("HTML DOM Document", BASE + "js_htmldom_document.asp"),
            ("MDN Document", "https://developer.mozilla.org/en-US/docs/Web/API/Document"),
        ],
    )
    build_and_snap(
        "element-reference",
        "Element Reference",
        EL,
        "Every HTML element is an object with properties and methods. This catalog rebuilds **every** W3Schools Element row (January 2026 table).",
        [
            "Tree walking: `parentElement`, `children`, `nextElementSibling`, `closest`.",
            "Content: `innerHTML`, `textContent`, `innerText`, `outerHTML`.",
            "Geometry: `client*`, `offset*`, `scroll*`, `getBoundingClientRect`.",
        ],
        EL_QA,
        "Look up a node, then read tree, content, attributes, or box geometry. Prefer `classList`, `before`/`after`/`append`, and `remove()` over the oldest APIs.",
        [
            ("HTML DOM Element Reference", BASE + "js_htmldom_element_reference.asp"),
            ("MDN Element", "https://developer.mozilla.org/en-US/docs/Web/API/Element"),
        ],
    )


if __name__ == "__main__":
    main()
