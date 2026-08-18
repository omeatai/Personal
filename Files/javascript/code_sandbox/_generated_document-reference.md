<details>
  <summary>Document Reference</summary>

## Introduction

The HTML DOM Document object is the owner of the page. This catalog rebuilds **every** W3Schools Document property and method row (January 2026 table), including deprecated APIs.

This section has **55** examples:

- [x] **Example 1:** activeElement [View](#document-reference-example-01)
- [x] **Example 2:** addEventListener() [View](#document-reference-example-02)
- [x] **Example 3:** adoptNode() [View](#document-reference-example-03)
- [x] **Example 4:** anchors [View](#document-reference-example-04)
- [x] **Example 5:** applets [View](#document-reference-example-05)
- [x] **Example 6:** baseURI [View](#document-reference-example-06)
- [x] **Example 7:** body [View](#document-reference-example-07)
- [x] **Example 8:** charset [View](#document-reference-example-08)
- [x] **Example 9:** characterSet [View](#document-reference-example-09)
- [x] **Example 10:** close() [View](#document-reference-example-10)
- [x] **Example 11:** cookie [View](#document-reference-example-11)
- [x] **Example 12:** createAttribute() [View](#document-reference-example-12)
- [x] **Example 13:** createComment() [View](#document-reference-example-13)
- [x] **Example 14:** createDocumentFragment() [View](#document-reference-example-14)
- [x] **Example 15:** createElement() [View](#document-reference-example-15)
- [x] **Example 16:** createEvent() [View](#document-reference-example-16)
- [x] **Example 17:** createTextNode() [View](#document-reference-example-17)
- [x] **Example 18:** defaultView [View](#document-reference-example-18)
- [x] **Example 19:** designMode [View](#document-reference-example-19)
- [x] **Example 20:** doctype [View](#document-reference-example-20)
- [x] **Example 21:** documentElement [View](#document-reference-example-21)
- [x] **Example 22:** documentMode [View](#document-reference-example-22)
- [x] **Example 23:** documentURI [View](#document-reference-example-23)
- [x] **Example 24:** domain [View](#document-reference-example-24)
- [x] **Example 25:** domConfig [View](#document-reference-example-25)
- [x] **Example 26:** embeds [View](#document-reference-example-26)
- [x] **Example 27:** execCommand() [View](#document-reference-example-27)
- [x] **Example 28:** forms [View](#document-reference-example-28)
- [x] **Example 29:** getElementById() [View](#document-reference-example-29)
- [x] **Example 30:** getElementsByClassName() [View](#document-reference-example-30)
- [x] **Example 31:** getElementsByName() [View](#document-reference-example-31)
- [x] **Example 32:** getElementsByTagName() [View](#document-reference-example-32)
- [x] **Example 33:** hasFocus() [View](#document-reference-example-33)
- [x] **Example 34:** head [View](#document-reference-example-34)
- [x] **Example 35:** images [View](#document-reference-example-35)
- [x] **Example 36:** implementation [View](#document-reference-example-36)
- [x] **Example 37:** importNode() [View](#document-reference-example-37)
- [x] **Example 38:** inputEncoding [View](#document-reference-example-38)
- [x] **Example 39:** lastModified [View](#document-reference-example-39)
- [x] **Example 40:** links [View](#document-reference-example-40)
- [x] **Example 41:** normalize() [View](#document-reference-example-41)
- [x] **Example 42:** normalizeDocument() [View](#document-reference-example-42)
- [x] **Example 43:** open() [View](#document-reference-example-43)
- [x] **Example 44:** querySelector() [View](#document-reference-example-44)
- [x] **Example 45:** querySelectorAll() [View](#document-reference-example-45)
- [x] **Example 46:** readyState [View](#document-reference-example-46)
- [x] **Example 47:** referrer [View](#document-reference-example-47)
- [x] **Example 48:** removeEventListener() [View](#document-reference-example-48)
- [x] **Example 49:** renameNode() [View](#document-reference-example-49)
- [x] **Example 50:** scripts [View](#document-reference-example-50)
- [x] **Example 51:** strictErrorChecking [View](#document-reference-example-51)
- [x] **Example 52:** title [View](#document-reference-example-52)
- [x] **Example 53:** URL [View](#document-reference-example-53)
- [x] **Example 54:** write() [View](#document-reference-example-54)
- [x] **Example 55:** writeln() [View](#document-reference-example-55)

## Detailed Explanation

- [x] Selection methods (`getElementById`, `querySelector`, collections like `forms` / `images`).
- [x] Create methods (`createElement`, `createTextNode`, `createDocumentFragment`).
- [x] Deprecated rows still run (or catch) and tell you **not** to use them.

<a id="document-reference-example-01"></a>

### **Example 1: activeElement**

- [x] **`activeElement`** — Returns the currently focused element in the document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/activeelement.html`

```javascript
const inp = document.createElement("input");
      inp.id = "focusMe";
      document.body.insertBefore(inp, document.getElementById("demo"));
      inp.focus();
      document.getElementById("demo").innerText = document.activeElement && document.activeElement.id;
```

<img alt="document-reference example 1 source" src="./code_sandbox/snaps/document-reference-01-code.png" />

<img alt="document-reference example 1 result" src="./code_sandbox/snaps/document-reference-01-result.png" />

- [x] **Outcome:** After `focus()`, `document.activeElement.id` is **focusMe** (or `body` if the engine ignores focus in headless).

<a id="document-reference-example-02"></a>

### **Example 2: addEventListener()**

- [x] **`addEventListener()`** — Attaches an event handler to the document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/addeventlistener.html`

```javascript
document.addEventListener("click", function handler() {
        document.getElementById("demo").innerText = "document clicked";
        document.removeEventListener("click", handler);
      });
      document.dispatchEvent(new MouseEvent("click", { bubbles: true }));
```

<img alt="document-reference example 2 source" src="./code_sandbox/snaps/document-reference-02-code.png" />

<img alt="document-reference example 2 result" src="./code_sandbox/snaps/document-reference-02-result.png" />

- [x] **Outcome:** Dispatching click on the document runs the listener: **document clicked**.

<a id="document-reference-example-03"></a>

### **Example 3: adoptNode()**

- [x] **`adoptNode()`** — Adopts a node from another document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/adoptnode.html`

```javascript
const other = document.getElementById("f").contentDocument;
      other.body.innerHTML = "<span id='x'>from iframe</span>";
      const node = document.adoptNode(other.getElementById("x"));
      document.body.appendChild(node);
      document.getElementById("demo").innerText = node.textContent + " owner=" + (node.ownerDocument === document);
```

<img alt="document-reference example 3 source" src="./code_sandbox/snaps/document-reference-03-code.png" />

<img alt="document-reference example 3 result" src="./code_sandbox/snaps/document-reference-03-result.png" />

- [x] **Outcome:** `adoptNode` moves the span into this document; `ownerDocument === document` is **true**.

<a id="document-reference-example-04"></a>

### **Example 4: anchors**

- [x] **`anchors`** — DEPRECATED collection of named anchors
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] Do **not** use `document.anchors` in new pages. Use `id` + `getElementById`.

Sandbox: `code_sandbox/document-reference/anchors.html`

```javascript
let msg;
      try { msg = "anchors.length=" + (document.anchors ? document.anchors.length : document.anchors); }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\n(deprecated — do not use in new code)";
```

<img alt="document-reference example 4 source" src="./code_sandbox/snaps/document-reference-04-code.png" />

<img alt="document-reference example 4 result" src="./code_sandbox/snaps/document-reference-04-result.png" />

- [x] **Outcome:** The engine still exposes `anchors` or it is gone. Treat it as **deprecated**.

<a id="document-reference-example-05"></a>

### **Example 5: applets**

- [x] **`applets`** — DEPRECATED collection of applets
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] Do **not** use `document.applets`.

Sandbox: `code_sandbox/document-reference/applets.html`

```javascript
let msg;
      try { msg = "applets=" + document.applets; }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\n(deprecated — Java applets are gone)";
```

<img alt="document-reference example 5 source" src="./code_sandbox/snaps/document-reference-05-code.png" />

<img alt="document-reference example 5 result" src="./code_sandbox/snaps/document-reference-05-result.png" />

- [x] **Outcome:** `applets` is **deprecated**. Java applet plugins are not part of the modern web.

<a id="document-reference-example-06"></a>

### **Example 6: baseURI**

- [x] **`baseURI`** — Returns the absolute base URI of a document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/baseuri.html`

```javascript
document.getElementById("demo").innerText = document.baseURI;
```

<img alt="document-reference example 6 source" src="./code_sandbox/snaps/document-reference-06-code.png" />

<img alt="document-reference example 6 result" src="./code_sandbox/snaps/document-reference-06-result.png" />

- [x] **Outcome:** `document.baseURI` is the absolute URL of this file (a `file://` path in the snapshot pipeline).

<a id="document-reference-example-07"></a>

### **Example 7: body**

- [x] **`body`** — Sets or returns the document's <body> element
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/body.html`

```javascript
document.getElementById("demo").innerText = document.body.tagName + " children=" + document.body.children.length;
```

<img alt="document-reference example 7 source" src="./code_sandbox/snaps/document-reference-07-code.png" />

<img alt="document-reference example 7 result" src="./code_sandbox/snaps/document-reference-07-result.png" />

- [x] **Outcome:** `document.body.tagName` is **BODY**.

<a id="document-reference-example-08"></a>

### **Example 8: charset**

- [x] **`charset`** — DEPRECATED character-encoding alias
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] Use **`document.characterSet`**, not `charset`.

Sandbox: `code_sandbox/document-reference/charset.html`

```javascript
let msg;
      try { msg = "charset=" + document.charset; }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\nUse characterSet instead";
```

<img alt="document-reference example 8 source" src="./code_sandbox/snaps/document-reference-08-code.png" />

<img alt="document-reference example 8 result" src="./code_sandbox/snaps/document-reference-08-result.png" />

- [x] **Outcome:** `charset` may still equal UTF-8. Prefer **`characterSet`**. It is **deprecated**.

<a id="document-reference-example-09"></a>

### **Example 9: characterSet**

- [x] **`characterSet`** — Returns the character encoding for the document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/characterset.html`

```javascript
document.getElementById("demo").innerText = document.characterSet;
```

<img alt="document-reference example 9 source" src="./code_sandbox/snaps/document-reference-09-code.png" />

<img alt="document-reference example 9 result" src="./code_sandbox/snaps/document-reference-09-result.png" />

- [x] **Outcome:** `document.characterSet` is typically **UTF-8**.

<a id="document-reference-example-10"></a>

### **Example 10: close()**

- [x] **`close()`** — Closes the output stream previously opened with document.open()
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/close.html`

```javascript
const d = document.getElementById("f").contentDocument;
      d.open();
      d.write("<p>stream</p>");
      d.close();
      document.getElementById("demo").innerText = "iframe=" + d.body.innerText;
```

<img alt="document-reference example 10 source" src="./code_sandbox/snaps/document-reference-10-code.png" />

<img alt="document-reference example 10 result" src="./code_sandbox/snaps/document-reference-10-result.png" />

- [x] **Outcome:** After `open`/`write`/`close`, the iframe body contains **stream**.

<a id="document-reference-example-11"></a>

### **Example 11: cookie**

- [x] **`cookie`** — Returns all name/value pairs of cookies in the document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/cookie.html`

```javascript
document.cookie = "demo=1; SameSite=Lax";
      document.getElementById("demo").innerText = document.cookie || "(empty — file:// often blocks cookies)";
```

<img alt="document-reference example 11 source" src="./code_sandbox/snaps/document-reference-11-code.png" />

<img alt="document-reference example 11 result" src="./code_sandbox/snaps/document-reference-11-result.png" />

- [x] **Outcome:** `document.cookie` shows **demo=1** when cookies are allowed; on `file://` it may be **empty**.

<a id="document-reference-example-12"></a>

### **Example 12: createAttribute()**

- [x] **`createAttribute()`** — Creates an attribute node
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/createattribute.html`

```javascript
const a = document.createAttribute("data-k");
      a.value = "v";
      document.getElementById("t").setAttributeNode(a);
      document.getElementById("demo").innerText = document.getElementById("t").getAttribute("data-k");
```

<img alt="document-reference example 12 source" src="./code_sandbox/snaps/document-reference-12-code.png" />

<img alt="document-reference example 12 result" src="./code_sandbox/snaps/document-reference-12-result.png" />

- [x] **Outcome:** The paragraph gains **data-k="v"** via `createAttribute` + `setAttributeNode`.

<a id="document-reference-example-13"></a>

### **Example 13: createComment()**

- [x] **`createComment()`** — Creates a Comment node with the specified text
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/createcomment.html`

```javascript
const c = document.createComment("note");
      document.getElementById("t").appendChild(c);
      document.getElementById("demo").innerText = c.nodeName + " " + c.nodeValue;
```

<img alt="document-reference example 13 source" src="./code_sandbox/snaps/document-reference-13-code.png" />

<img alt="document-reference example 13 result" src="./code_sandbox/snaps/document-reference-13-result.png" />

- [x] **Outcome:** A comment node `#comment` with value **note** is appended.

<a id="document-reference-example-14"></a>

### **Example 14: createDocumentFragment()**

- [x] **`createDocumentFragment()`** — Creates an empty DocumentFragment node
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/createdocumentfragment.html`

```javascript
const frag = document.createDocumentFragment();
      const s = document.createElement("span");
      s.textContent = "frag";
      frag.appendChild(s);
      document.getElementById("t").appendChild(frag);
      document.getElementById("demo").innerText = document.getElementById("t").innerText;
```

<img alt="document-reference example 14 source" src="./code_sandbox/snaps/document-reference-14-code.png" />

<img alt="document-reference example 14 result" src="./code_sandbox/snaps/document-reference-14-result.png" />

- [x] **Outcome:** The fragment’s **frag** span is inserted in one operation; the fragment itself is empty after append.

<a id="document-reference-example-15"></a>

### **Example 15: createElement()**

- [x] **`createElement()`** — Creates an Element node
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/createelement.html`

```javascript
const el = document.createElement("em");
      el.textContent = "new";
      document.getElementById("t").appendChild(el);
      document.getElementById("demo").innerText = el.tagName + " " + el.textContent;
```

<img alt="document-reference example 15 source" src="./code_sandbox/snaps/document-reference-15-code.png" />

<img alt="document-reference example 15 result" src="./code_sandbox/snaps/document-reference-15-result.png" />

- [x] **Outcome:** `createElement("em")` builds an **EM** with text **new**.

<a id="document-reference-example-16"></a>

### **Example 16: createEvent()**

- [x] **`createEvent()`** — Creates a new event (legacy)
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/createevent.html`

```javascript
let msg;
      try {
        const ev = document.createEvent("Event");
        ev.initEvent("ping", true, true);
        msg = ev.type + " bubbles=" + ev.bubbles;
      } catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\nPrefer new Event('ping')";
```

<img alt="document-reference example 16 source" src="./code_sandbox/snaps/document-reference-16-code.png" />

<img alt="document-reference example 16 result" src="./code_sandbox/snaps/document-reference-16-result.png" />

- [x] **Outcome:** `createEvent`/`initEvent` still work in many engines, or they throw. Prefer **`new Event()`**.

<a id="document-reference-example-17"></a>

### **Example 17: createTextNode()**

- [x] **`createTextNode()`** — Creates a Text node
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/createtextnode.html`

```javascript
const t = document.createTextNode("plain");
      document.getElementById("t").appendChild(t);
      document.getElementById("demo").innerText = t.nodeName + " " + JSON.stringify(t.nodeValue);
```

<img alt="document-reference example 17 source" src="./code_sandbox/snaps/document-reference-17-code.png" />

<img alt="document-reference example 17 result" src="./code_sandbox/snaps/document-reference-17-result.png" />

- [x] **Outcome:** A `#text` node with value **plain** is appended.

<a id="document-reference-example-18"></a>

### **Example 18: defaultView**

- [x] **`defaultView`** — Returns the window object associated with a document, or null
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/defaultview.html`

```javascript
document.getElementById("demo").innerText = String(document.defaultView === window);
```

<img alt="document-reference example 18 source" src="./code_sandbox/snaps/document-reference-18-code.png" />

<img alt="document-reference example 18 result" src="./code_sandbox/snaps/document-reference-18-result.png" />

- [x] **Outcome:** `document.defaultView === window` is **true** in a normal browser tab.

<a id="document-reference-example-19"></a>

### **Example 19: designMode**

- [x] **`designMode`** — Controls whether the entire document should be editable
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/designmode.html`

```javascript
const d = document.getElementById("f").contentDocument;
      d.designMode = "on";
      document.getElementById("demo").innerText = "designMode=" + d.designMode;
```

<img alt="document-reference example 19 source" src="./code_sandbox/snaps/document-reference-19-code.png" />

<img alt="document-reference example 19 result" src="./code_sandbox/snaps/document-reference-19-result.png" />

- [x] **Outcome:** The iframe document’s `designMode` is **on** (the whole iframe body becomes editable).

<a id="document-reference-example-20"></a>

### **Example 20: doctype**

- [x] **`doctype`** — Returns the Document Type Declaration associated with the document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/doctype.html`

```javascript
const dt = document.doctype;
      document.getElementById("demo").innerText = dt ? (dt.name + " " + dt.publicId) : "null";
```

<img alt="document-reference example 20 source" src="./code_sandbox/snaps/document-reference-20-code.png" />

<img alt="document-reference example 20 result" src="./code_sandbox/snaps/document-reference-20-result.png" />

- [x] **Outcome:** `document.doctype.name` is **html** for a standard HTML5 doctype.

<a id="document-reference-example-21"></a>

### **Example 21: documentElement**

- [x] **`documentElement`** — Returns the Document Element (`<html>`)
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/documentelement.html`

```javascript
document.getElementById("demo").innerText = document.documentElement.tagName;
```

<img alt="document-reference example 21 source" src="./code_sandbox/snaps/document-reference-21-code.png" />

<img alt="document-reference example 21 result" src="./code_sandbox/snaps/document-reference-21-result.png" />

- [x] **Outcome:** `document.documentElement.tagName` is **HTML**.

<a id="document-reference-example-22"></a>

### **Example 22: documentMode**

- [x] **`documentMode`** — DEPRECATED IE document mode
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] Deprecated **Internet Explorer** API.

Sandbox: `code_sandbox/document-reference/documentmode.html`

```javascript
document.getElementById("demo").innerText = "documentMode=" + document.documentMode + " (deprecated IE-only)";
```

<img alt="document-reference example 22 source" src="./code_sandbox/snaps/document-reference-22-code.png" />

<img alt="document-reference example 22 result" src="./code_sandbox/snaps/document-reference-22-result.png" />

- [x] **Outcome:** `documentMode` is **undefined** in Chrome/Edge. It was an **IE** feature — do not use it.

<a id="document-reference-example-23"></a>

### **Example 23: documentURI**

- [x] **`documentURI`** — Sets or returns the location of the document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/documenturi.html`

```javascript
document.getElementById("demo").innerText = document.documentURI;
```

<img alt="document-reference example 23 source" src="./code_sandbox/snaps/document-reference-23-code.png" />

<img alt="document-reference example 23 result" src="./code_sandbox/snaps/document-reference-23-result.png" />

- [x] **Outcome:** `documentURI` is the document URL (same family as `document.URL`).

<a id="document-reference-example-24"></a>

### **Example 24: domain**

- [x] **`domain`** — Returns the domain name of the server that loaded the document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/domain.html`

```javascript
let msg;
      try { msg = "domain=" + JSON.stringify(document.domain); }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg;
```

<img alt="document-reference example 24 source" src="./code_sandbox/snaps/document-reference-24-code.png" />

<img alt="document-reference example 24 result" src="./code_sandbox/snaps/document-reference-24-result.png" />

- [x] **Outcome:** On `file://` this is often **`""`** or a security error. On http it is the host name.

<a id="document-reference-example-25"></a>

### **Example 25: domConfig**

- [x] **`domConfig`** — DEPRECATED
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] Do not use `domConfig`.

Sandbox: `code_sandbox/document-reference/domconfig.html`

```javascript
document.getElementById("demo").innerText = "domConfig=" + document.domConfig + " (deprecated — unused)";
```

<img alt="document-reference example 25 source" src="./code_sandbox/snaps/document-reference-25-code.png" />

<img alt="document-reference example 25 result" src="./code_sandbox/snaps/document-reference-25-result.png" />

- [x] **Outcome:** `domConfig` is **deprecated** and typically **undefined**.

<a id="document-reference-example-26"></a>

### **Example 26: embeds**

- [x] **`embeds`** — Returns a collection of all <embed> elements
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/embeds.html`

```javascript
document.getElementById("demo").innerText = "embeds=" + document.embeds.length;
```

<img alt="document-reference example 26 source" src="./code_sandbox/snaps/document-reference-26-code.png" />

<img alt="document-reference example 26 result" src="./code_sandbox/snaps/document-reference-26-result.png" />

- [x] **Outcome:** `document.embeds.length` is **1** in this page.

<a id="document-reference-example-27"></a>

### **Example 27: execCommand()**

- [x] **`execCommand()`** — DEPRECATED document editing command
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] Deprecated. Use the modern Selection / Clipboard APIs instead.

Sandbox: `code_sandbox/document-reference/execcommand.html`

```javascript
let msg;
      try {
        document.getElementById("t").focus();
        const ok = document.execCommand("selectAll");
        msg = "execCommand selectAll -> " + ok;
      } catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\n(deprecated)";
```

<img alt="document-reference example 27 source" src="./code_sandbox/snaps/document-reference-27-code.png" />

<img alt="document-reference example 27 result" src="./code_sandbox/snaps/document-reference-27-result.png" />

- [x] **Outcome:** `execCommand` may return a boolean or throw. It is **deprecated** — do not use it in new code.

<a id="document-reference-example-28"></a>

### **Example 28: forms**

- [x] **`forms`** — Returns a collection of all <form> elements
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/forms.html`

```javascript
document.getElementById("demo").innerText = "forms=" + document.forms.length + " id=" + document.forms[0].id;
```

<img alt="document-reference example 28 source" src="./code_sandbox/snaps/document-reference-28-code.png" />

<img alt="document-reference example 28 result" src="./code_sandbox/snaps/document-reference-28-result.png" />

- [x] **Outcome:** `document.forms.length` is **1** and the form id is **frm**.

<a id="document-reference-example-29"></a>

### **Example 29: getElementById()**

- [x] **`getElementById()`** — Returns the element that has the ID attribute with the specified value
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/getelementbyid.html`

```javascript
document.getElementById("demo").innerText = document.getElementById("t").textContent;
```

<img alt="document-reference example 29 source" src="./code_sandbox/snaps/document-reference-29-code.png" />

<img alt="document-reference example 29 result" src="./code_sandbox/snaps/document-reference-29-result.png" />

- [x] **Outcome:** `getElementById("t")` returns the Hello World paragraph.

<a id="document-reference-example-30"></a>

### **Example 30: getElementsByClassName()**

- [x] **`getElementsByClassName()`** — Returns an HTMLCollection of elements with the specified class name
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/getelementsbyclassname.html`

```javascript
document.getElementById("demo").innerText = "n=" + document.getElementsByClassName("k").length;
```

<img alt="document-reference example 30 source" src="./code_sandbox/snaps/document-reference-30-code.png" />

<img alt="document-reference example 30 result" src="./code_sandbox/snaps/document-reference-30-result.png" />

- [x] **Outcome:** Two `.k` nodes are found.

<a id="document-reference-example-31"></a>

### **Example 31: getElementsByName()**

- [x] **`getElementsByName()`** — Returns a live NodeList of elements with the specified name
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/getelementsbyname.html`

```javascript
document.getElementById("demo").innerText = "n=" + document.getElementsByName("user").length;
```

<img alt="document-reference example 31 source" src="./code_sandbox/snaps/document-reference-31-code.png" />

<img alt="document-reference example 31 result" src="./code_sandbox/snaps/document-reference-31-result.png" />

- [x] **Outcome:** `getElementsByName("user")` finds the named input (length **1**).

<a id="document-reference-example-32"></a>

### **Example 32: getElementsByTagName()**

- [x] **`getElementsByTagName()`** — Returns an HTMLCollection of elements with the specified tag name
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/getelementsbytagname.html`

```javascript
document.getElementById("demo").innerText = "p=" + document.getElementsByTagName("p").length;
```

<img alt="document-reference example 32 source" src="./code_sandbox/snaps/document-reference-32-code.png" />

<img alt="document-reference example 32 result" src="./code_sandbox/snaps/document-reference-32-result.png" />

- [x] **Outcome:** The page’s `<p>` count includes the sample paragraphs.

<a id="document-reference-example-33"></a>

### **Example 33: hasFocus()**

- [x] **`hasFocus()`** — Returns whether the document has focus
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/hasfocus.html`

```javascript
document.getElementById("demo").innerText = "hasFocus=" + document.hasFocus();
```

<img alt="document-reference example 33 source" src="./code_sandbox/snaps/document-reference-33-code.png" />

<img alt="document-reference example 33 result" src="./code_sandbox/snaps/document-reference-33-result.png" />

- [x] **Outcome:** `hasFocus()` is a boolean — often **false** in headless screenshots, **true** in an interactive tab.

<a id="document-reference-example-34"></a>

### **Example 34: head**

- [x] **`head`** — Returns the <head> element of the document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/head.html`

```javascript
document.getElementById("demo").innerText = document.head.tagName + " titleChild=" + !!document.head.querySelector("title");
```

<img alt="document-reference example 34 source" src="./code_sandbox/snaps/document-reference-34-code.png" />

<img alt="document-reference example 34 result" src="./code_sandbox/snaps/document-reference-34-result.png" />

- [x] **Outcome:** `document.head.tagName` is **HEAD**.

<a id="document-reference-example-35"></a>

### **Example 35: images**

- [x] **`images`** — Returns a collection of all <img> elements
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/images.html`

```javascript
document.getElementById("demo").innerText = "images=" + document.images.length + " alt=" + document.images[0].alt;
```

<img alt="document-reference example 35 source" src="./code_sandbox/snaps/document-reference-35-code.png" />

<img alt="document-reference example 35 result" src="./code_sandbox/snaps/document-reference-35-result.png" />

- [x] **Outcome:** `document.images.length` is **1**.

<a id="document-reference-example-36"></a>

### **Example 36: implementation**

- [x] **`implementation`** — Returns the DOMImplementation object that handles this document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/implementation.html`

```javascript
const im = document.implementation;
      document.getElementById("demo").innerText = "hasFeature=" + typeof im.hasFeature + " createHTMLDocument=" + typeof im.createHTMLDocument;
```

<img alt="document-reference example 36 source" src="./code_sandbox/snaps/document-reference-36-code.png" />

<img alt="document-reference example 36 result" src="./code_sandbox/snaps/document-reference-36-result.png" />

- [x] **Outcome:** `document.implementation` exposes `createHTMLDocument` (and legacy `hasFeature`).

<a id="document-reference-example-37"></a>

### **Example 37: importNode()**

- [x] **`importNode()`** — Imports a node from another document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/importnode.html`

```javascript
const other = document.getElementById("f").contentDocument;
      other.body.innerHTML = "<span id='x'>imported</span>";
      const copy = document.importNode(other.getElementById("x"), true);
      document.body.appendChild(copy);
      document.getElementById("demo").innerText = copy.textContent + " stillInIframe=" + !!other.getElementById("x");
```

<img alt="document-reference example 37 source" src="./code_sandbox/snaps/document-reference-37-code.png" />

<img alt="document-reference example 37 result" src="./code_sandbox/snaps/document-reference-37-result.png" />

- [x] **Outcome:** `importNode(..., true)` **copies** the node; the iframe original still exists.

<a id="document-reference-example-38"></a>

### **Example 38: inputEncoding**

- [x] **`inputEncoding`** — DEPRECATED
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] Deprecated alias of the encoding.

Sandbox: `code_sandbox/document-reference/inputencoding.html`

```javascript
document.getElementById("demo").innerText = "inputEncoding=" + document.inputEncoding + " (deprecated — use characterSet)";
```

<img alt="document-reference example 38 source" src="./code_sandbox/snaps/document-reference-38-code.png" />

<img alt="document-reference example 38 result" src="./code_sandbox/snaps/document-reference-38-result.png" />

- [x] **Outcome:** `inputEncoding` may still report UTF-8. Prefer **`characterSet`**. **Deprecated**.

<a id="document-reference-example-39"></a>

### **Example 39: lastModified**

- [x] **`lastModified`** — Returns the date and time the document was last modified
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/lastmodified.html`

```javascript
document.getElementById("demo").innerText = document.lastModified;
```

<img alt="document-reference example 39 source" src="./code_sandbox/snaps/document-reference-39-code.png" />

<img alt="document-reference example 39 result" src="./code_sandbox/snaps/document-reference-39-result.png" />

- [x] **Outcome:** `lastModified` is a date string from the server (or file mtime).

<a id="document-reference-example-40"></a>

### **Example 40: links**

- [x] **`links`** — Returns all <a> and <area> elements that have an href
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/links.html`

```javascript
document.getElementById("demo").innerText = "links=" + document.links.length;
```

<img alt="document-reference example 40 source" src="./code_sandbox/snaps/document-reference-40-code.png" />

<img alt="document-reference example 40 result" src="./code_sandbox/snaps/document-reference-40-result.png" />

- [x] **Outcome:** `document.links.length` is **1**.

<a id="document-reference-example-41"></a>

### **Example 41: normalize()**

- [x] **`normalize()`** — Removes empty Text nodes, and joins adjacent text nodes
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/normalize.html`

```javascript
const p = document.getElementById("t");
      p.appendChild(document.createTextNode("A"));
      p.appendChild(document.createTextNode("B"));
      const before = p.childNodes.length;
      p.normalize();
      document.getElementById("demo").innerText = "before=" + before + " after=" + p.childNodes.length;
```

<img alt="document-reference example 41 source" src="./code_sandbox/snaps/document-reference-41-code.png" />

<img alt="document-reference example 41 result" src="./code_sandbox/snaps/document-reference-41-result.png" />

- [x] **Outcome:** `normalize()` merges adjacent text nodes so `childNodes.length` **drops**.

<a id="document-reference-example-42"></a>

### **Example 42: normalizeDocument()**

- [x] **`normalizeDocument()`** — DEPRECATED
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] Do not use `normalizeDocument()`.

Sandbox: `code_sandbox/document-reference/normalizedocument.html`

```javascript
let msg;
      try { msg = "normalizeDocument=" + typeof document.normalizeDocument; document.normalizeDocument && document.normalizeDocument(); }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + "\n(deprecated)";
```

<img alt="document-reference example 42 source" src="./code_sandbox/snaps/document-reference-42-code.png" />

<img alt="document-reference example 42 result" src="./code_sandbox/snaps/document-reference-42-result.png" />

- [x] **Outcome:** `normalizeDocument` is **deprecated** and usually missing. Use `node.normalize()`.

<a id="document-reference-example-43"></a>

### **Example 43: open()**

- [x] **`open()`** — Opens an HTML output stream to collect output from document.write()
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/open.html`

```javascript
const d = document.getElementById("f").contentDocument;
      const stream = d.open();
      d.write("<p>opened</p>");
      d.close();
      document.getElementById("demo").innerText = "wrote into opened stream: " + d.body.innerText;
```

<img alt="document-reference example 43 source" src="./code_sandbox/snaps/document-reference-43-code.png" />

<img alt="document-reference example 43 result" src="./code_sandbox/snaps/document-reference-43-result.png" />

- [x] **Outcome:** `open()` starts a new stream; `write` then fills the iframe with **opened**.

<a id="document-reference-example-44"></a>

### **Example 44: querySelector()**

- [x] **`querySelector()`** — Returns the first element that matches a CSS selector
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/queryselector.html`

```javascript
document.getElementById("demo").innerText = document.querySelector("#t b").textContent;
```

<img alt="document-reference example 44 source" src="./code_sandbox/snaps/document-reference-44-code.png" />

<img alt="document-reference example 44 result" src="./code_sandbox/snaps/document-reference-44-result.png" />

- [x] **Outcome:** `querySelector("#t b")` returns **World**.

<a id="document-reference-example-45"></a>

### **Example 45: querySelectorAll()**

- [x] **`querySelectorAll()`** — Returns a static NodeList of all matching elements
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/queryselectorall.html`

```javascript
document.getElementById("demo").innerText = "n=" + document.querySelectorAll("p").length;
```

<img alt="document-reference example 45 source" src="./code_sandbox/snaps/document-reference-45-code.png" />

<img alt="document-reference example 45 result" src="./code_sandbox/snaps/document-reference-45-result.png" />

- [x] **Outcome:** `querySelectorAll("p")` counts the sample paragraphs.

<a id="document-reference-example-46"></a>

### **Example 46: readyState**

- [x] **`readyState`** — Returns the (loading) status of the document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/readystate.html`

```javascript
document.getElementById("demo").innerText = document.readyState;
```

<img alt="document-reference example 46 source" src="./code_sandbox/snaps/document-reference-46-code.png" />

<img alt="document-reference example 46 result" src="./code_sandbox/snaps/document-reference-46-result.png" />

- [x] **Outcome:** By the time this script runs, `readyState` is **interactive** or **complete**.

<a id="document-reference-example-47"></a>

### **Example 47: referrer**

- [x] **`referrer`** — Returns the URL of the document that loaded the current document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/referrer.html`

```javascript
document.getElementById("demo").innerText = JSON.stringify(document.referrer);
```

<img alt="document-reference example 47 source" src="./code_sandbox/snaps/document-reference-47-code.png" />

<img alt="document-reference example 47 result" src="./code_sandbox/snaps/document-reference-47-result.png" />

- [x] **Outcome:** `referrer` is often **`""`** for a `file://` screenshot (no previous page).

<a id="document-reference-example-48"></a>

### **Example 48: removeEventListener()**

- [x] **`removeEventListener()`** — Removes an event handler attached with addEventListener
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/removeeventlistener.html`

```javascript
function ping() { document.getElementById("demo").innerText = "should not run"; }
      document.addEventListener("keyup", ping);
      document.removeEventListener("keyup", ping);
      document.dispatchEvent(new KeyboardEvent("keyup"));
      document.getElementById("demo").innerText = (document.getElementById("demo").innerText === "should not run")
        ? "listener still there" : "removed — keyup did nothing";
```

<img alt="document-reference example 48 source" src="./code_sandbox/snaps/document-reference-48-code.png" />

<img alt="document-reference example 48 result" src="./code_sandbox/snaps/document-reference-48-result.png" />

- [x] **Outcome:** After `removeEventListener`, the `keyup` handler does **not** run.

<a id="document-reference-example-49"></a>

### **Example 49: renameNode()**

- [x] **`renameNode()`** — DEPRECATED
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] Do not use `renameNode()`.

Sandbox: `code_sandbox/document-reference/renamenode.html`

```javascript
let msg;
      try { msg = "renameNode=" + typeof document.renameNode; }
      catch (e) { msg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText = msg + " (deprecated)";
```

<img alt="document-reference example 49 source" src="./code_sandbox/snaps/document-reference-49-code.png" />

<img alt="document-reference example 49 result" src="./code_sandbox/snaps/document-reference-49-result.png" />

- [x] **Outcome:** `renameNode` is **deprecated** and not available in HTML browsers.

<a id="document-reference-example-50"></a>

### **Example 50: scripts**

- [x] **`scripts`** — Returns a collection of <script> elements
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/scripts.html`

```javascript
document.getElementById("demo").innerText = "scripts=" + document.scripts.length;
```

<img alt="document-reference example 50 source" src="./code_sandbox/snaps/document-reference-50-code.png" />

<img alt="document-reference example 50 result" src="./code_sandbox/snaps/document-reference-50-result.png" />

- [x] **Outcome:** `document.scripts.length` is at least **1**.

<a id="document-reference-example-51"></a>

### **Example 51: strictErrorChecking**

- [x] **`strictErrorChecking`** — DEPRECATED
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] Do not use `strictErrorChecking`.

Sandbox: `code_sandbox/document-reference/stricterrorchecking.html`

```javascript
document.getElementById("demo").innerText = "strictErrorChecking=" + document.strictErrorChecking + " (deprecated)";
```

<img alt="document-reference example 51 source" src="./code_sandbox/snaps/document-reference-51-code.png" />

<img alt="document-reference example 51 result" src="./code_sandbox/snaps/document-reference-51-result.png" />

- [x] **Outcome:** `strictErrorChecking` is **deprecated** / typically **undefined**.

<a id="document-reference-example-52"></a>

### **Example 52: title**

- [x] **`title`** — Sets or returns the title of the document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/title.html`

```javascript
document.title = "Doc Ref";
      document.getElementById("demo").innerText = document.title;
```

<img alt="document-reference example 52 source" src="./code_sandbox/snaps/document-reference-52-code.png" />

<img alt="document-reference example 52 result" src="./code_sandbox/snaps/document-reference-52-result.png" />

- [x] **Outcome:** `document.title` is set to **Doc Ref**.

<a id="document-reference-example-53"></a>

### **Example 53: URL**

- [x] **`URL`** — Returns the full URL of the HTML document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/url.html`

```javascript
document.getElementById("demo").innerText = document.URL;
```

<img alt="document-reference example 53 source" src="./code_sandbox/snaps/document-reference-53-code.png" />

<img alt="document-reference example 53 result" src="./code_sandbox/snaps/document-reference-53-result.png" />

- [x] **Outcome:** `document.URL` is the full document address.

<a id="document-reference-example-54"></a>

### **Example 54: write()**

- [x] **`write()`** — Writes HTML expressions or JavaScript code to a document
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.
- [x] After load, `write` **overwrites** the document. Use an iframe or `innerHTML` instead.

Sandbox: `code_sandbox/document-reference/write.html`

```javascript
const d = document.getElementById("f").contentDocument;
      d.open();
      d.write("<strong>written</strong>");
      d.close();
      document.getElementById("demo").innerText = d.body.innerHTML;
```

<img alt="document-reference example 54 source" src="./code_sandbox/snaps/document-reference-54-code.png" />

<img alt="document-reference example 54 result" src="./code_sandbox/snaps/document-reference-54-result.png" />

- [x] **Outcome:** The iframe contains **`<strong>written</strong>`**. Never `write` on a loaded main page.

<a id="document-reference-example-55"></a>

### **Example 55: writeln()**

- [x] **`writeln()`** — Same as write(), but adds a newline character after each statement
- [x] This sandbox **runs** the API from the W3Schools reference table (January 2026 revision).
- [x] Start from `document` (or an element). Wrap risky / deprecated calls in `try/catch` so a missing engine feature still prints a result.

Sandbox: `code_sandbox/document-reference/writeln.html`

```javascript
const d = document.getElementById("f").contentDocument;
      d.open();
      d.writeln("<pre>line1");
      d.writeln("line2</pre>");
      d.close();
      document.getElementById("demo").innerText = JSON.stringify(d.body.innerText);
```

<img alt="document-reference example 55 source" src="./code_sandbox/snaps/document-reference-55-code.png" />

<img alt="document-reference example 55 result" src="./code_sandbox/snaps/document-reference-55-result.png" />

- [x] **Outcome:** `writeln` inserts a **newline** after each call (visible inside `<pre>`).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/document-reference/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `document.documentElement`?

<details>
<summary>Answer</summary>

- [x] The root **`<html>`** element.

</details>

### Question 2: What encoding property should you use?

<details>
<summary>Answer</summary>

- [x] **`characterSet`**. `charset` / `inputEncoding` are deprecated.

</details>

### Question 3: Does `adoptNode` copy or move?

<details>
<summary>Answer</summary>

- [x] It **moves** the node to this document (`ownerDocument` changes).

</details>

### Question 4: Does `importNode` copy or move?

<details>
<summary>Answer</summary>

- [x] It **copies**. The original stays in the other document.

</details>

### Question 5: What does `readyState` become after load?

<details>
<summary>Answer</summary>

- [x] **`complete`** (it may be `interactive` while scripts still run).

</details>

### Question 6: Why is `document.write` dangerous after load?

<details>
<summary>Answer</summary>

- [x] It **replaces** the entire document.

</details>

### Question 7: How do you undo `addEventListener`?

<details>
<summary>Answer</summary>

- [x] Call **`removeEventListener`** with the **same** function reference.

</details>

### Question 8: What is `document.defaultView`?

<details>
<summary>Answer</summary>

- [x] The associated **`window`** (or `null`).

</details>

### Question 9: Should you use `execCommand`?

<details>
<summary>Answer</summary>

- [x] No — it is **deprecated**.

</details>

### Question 10: What does `normalize()` do on a node?

<details>
<summary>Answer</summary>

- [x] Merges adjacent **text** nodes and removes empty ones.

</details>

### Question 11: What is in `document.forms`?

<details>
<summary>Answer</summary>

- [x] Every **`<form>`** in the document.

</details>

### Question 12: What does `hasFocus()` tell you?

<details>
<summary>Answer</summary>

- [x] Whether **this document** currently has focus.

</details>


</details>

## Summary

Use `document` as the entry point. Prefer `characterSet`, `querySelector`, and `createElement`. Avoid write-after-load and the deprecated rows.

## References

- [HTML DOM Document](https://www.w3schools.com/js/js_htmldom_document.asp)
- [MDN Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)

</details>
