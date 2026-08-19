"""S27: JS Window API / BOM (8 W3Schools pages)."""
from __future__ import annotations

from _dom_ui import P, lines_js, show_js
from _gen_lib import build_and_snap

BASE = "https://www.w3schools.com/js/"


def qa(*items):
    return list(items)


def run(slug, title, records, intro, concepts, qa_items, summary, page, extra_refs=None, port=8771):
    refs = [(title, BASE + page)]
    refs.extend(
        extra_refs
        or [("MDN Window", "https://developer.mozilla.org/en-US/docs/Web/API/Window")]
    )
    build_and_snap(
        slug, title, records, intro, concepts, qa_items, summary, refs, use_http=True, port=port
    )


FETCH_TXT = "Hello Fetch API\nThis is fetch.txt from the sandbox."
CUSTOMER_JSON = """{
  "id": 101,
  "name": "John Doe",
  "city": "New York",
  "member": true
}
"""
# ---------------------------------------------------------------------------
# 27.1 JS Window
# ---------------------------------------------------------------------------

WIN = [
    P("window-document", "window.document is the same object as document",
      ["The **BOM** (Browser Object Model) is everything the browser exposes besides the page tree.",
       "The **Window** object is the global. All global variables and functions become properties/methods of `window`.",
       "The HTML DOM `document` is a **property** of `window`. `window.document.getElementById` and `document.getElementById` are the same call.",
       "You may omit `window.` for globals. `window` itself cannot be omitted if you need the Window object (size, open, …)."],
      """window.document.getElementById("header");
document.getElementById("header");""",
      "`window.document === document` is **true**. Both lookups find the same **header** element.",
      body='<h1 id="header">Header</h1>',
      js="""      const a = window.document.getElementById("header");
      const b = document.getElementById("header");
      document.getElementById("demo").innerText =
        "sameNode=" + (a === b) +
        "\\nwindow.document===document=" + (window.document === document) +
        "\\ntext=" + a.textContent;"""),
    P("inner-width", "window.innerWidth — viewport width in pixels",
      ["`window.innerWidth` is the **inner** width of the browser window (the viewport), in CSS pixels.",
       "It does **not** include toolbars, window chrome, or (usually) the vertical scrollbar gutter the same way `outerWidth` does.",
       "The W3Schools Tryit stores `let w = window.innerWidth` then writes it to the page.",
       "This value changes when the user resizes the window or rotates a phone."],
      """let w = window.innerWidth;""",
      "The snapshot window is **900px** wide, so `innerWidth` reports **900** (or very close).",
      js=show_js("window.innerWidth")),
    P("inner-height", "window.innerHeight — viewport height in pixels",
      ["`window.innerHeight` is the **inner** height of the viewport, not including browser UI.",
       "W3Schools pairs it with `innerWidth` in one Tryit: `let h = window.innerHeight`.",
       "Use these — not `screen.height` — when you care about **how much page is visible**.",
       "Headless screenshots use `--window-size=900,640`, so height is in that neighborhood."],
      """let h = window.innerHeight;""",
      "`innerHeight` is a positive pixel count for the visible viewport (around **640** in this snap).",
      js=show_js("window.innerHeight")),
    P("open", "window.open() — open a new window",
      ["`window.open(url)` asks the browser to open **another** browsing context (tab or popup).",
       "Popup blockers often return **`null`** if the call is not tied to a user gesture.",
       "Always check the return value before calling methods on it.",
       "The snapshot calls `open` without a click, so a blocker is likely — that is the realistic result."],
      """window.open() - open a new window""",
      "The call returns either a **Window** or **`null`** (blocked). The snapshot reports which happened.",
      js="""      let win = null;
      try { win = window.open("about:blank", "_blank"); } catch (e) { win = null; }
      const kind = win ? ("Window, closed=" + win.closed) : "null (blocked)";
      if (win && !win.closed) { try { win.close(); } catch (e) {} }
      document.getElementById("demo").innerText = "window.open -> " + kind;"""),
    P("close", "window.close() — close the current window",
      ["`window.close()` closes **this** window, but browsers only allow it for windows **your script opened** with `open()`.",
       "Calling it on a tab the user opened themselves is ignored (or prompts).",
       "Do not put `close()` in onload — it will not do what tutorial snippets imply on a normal tab.",
       "The snapshot does **not** close the page; it only proves the method exists."],
      """window.close() - close the current window""",
      "`typeof window.close` is **function**. The page stays open so the snapshot can be taken.",
      js=show_js('"typeof close=" + typeof window.close')),
    P("move-to", "window.moveTo() — move the current window",
      ["`window.moveTo(x, y)` moves the **window** to screen coordinates.",
       "Modern browsers **ignore** this for ordinary tabs (only some popup windows allow it).",
       "Treat it as a legacy BOM method, not something you should rely on.",
       "The snapshot calls it and then reports `screenX`/`screenY` (often unchanged)."],
      """window.moveTo() - move the current window""",
      "After `moveTo(0, 0)`, `screenX`/`screenY` are reported. Tabs usually **do not move**.",
      js="""      try { window.moveTo(0, 0); } catch (e) {}
      document.getElementById("demo").innerText =
        "after moveTo(0,0) screenX=" + window.screenX + " screenY=" + window.screenY;"""),
    P("resize-to", "window.resizeTo() — resize the current window",
      ["`window.resizeTo(width, height)` resizes the **outer** window.",
       "Like `moveTo`, this is **blocked** for most tabs.",
       "Prefer CSS layout and `innerWidth` over trying to resize the browser.",
       "The snapshot calls `resizeTo(800, 600)` and reports inner size (typically unchanged)."],
      """window.resizeTo() - resize the current window""",
      "`resizeTo` is a function; the viewport size after the call is still the screenshot window.",
      js="""      try { window.resizeTo(800, 600); } catch (e) {}
      document.getElementById("demo").innerText =
        "typeof resizeTo=" + typeof window.resizeTo +
        "\\ninnerWidth=" + window.innerWidth + " innerHeight=" + window.innerHeight;"""),
]

WIN_QA = qa(
    ("What is the BOM?", ["The **Browser Object Model** — `window` and objects it owns (`document`, `location`, `history`, `navigator`, `screen`)."]),
    ("Are `document` and `window.document` different?", ["**No** — `document` is a property of `window`; they are the **same** object."]),
    ("What does `innerWidth` measure?", ["The **viewport** width in pixels, not the monitor and not browser chrome."]),
    ("Does `innerHeight` include toolbars?", ["**No** — it is the inner viewport height."]),
    ("What does `window.open` return if a popup is blocked?", ["**`null`** (or a closed window). Always check before using it."]),
    ("Can you `close()` any tab?", ["**No** — browsers only let scripts close windows they **opened**."]),
    ("Do `moveTo` and `resizeTo` work on normal tabs?", ["Usually **no** — they are ignored except for some script-opened popups."]),
    ("Can you omit the `window.` prefix?", ["**Yes** for globals (`document`, `alert`). Use `window` when you mean the Window object itself."]),
    ("What becomes a property of `window`?", ["**Global variables** (and global functions become **methods**)."]),
    ("Which size should you use for “visible page”?", ["**`innerWidth` / `innerHeight`**, not `screen.width`."]),
)

# ---------------------------------------------------------------------------
# 27.2 JS Screen
# ---------------------------------------------------------------------------

SCR = [
    P("width", "screen.width — visitor screen width",
      ["`window.screen` (or just `screen`) describes the **monitor**, not the browser viewport.",
       "`screen.width` is the full screen width in pixels.",
       "This is **not** the same as `window.innerWidth` (the tab).",
       "W3Schools writes: `Screen Width: ` + `screen.width`."],
      """document.getElementById("demo").innerHTML = "Screen Width: " + screen.width;""",
      "The page prints **Screen Width:** followed by this machine’s pixel width.",
      js="""      document.getElementById("demo").innerText = "Screen Width: " + screen.width;"""),
    P("height", "screen.height — visitor screen height",
      ["`screen.height` is the full screen height in pixels.",
       "It includes areas covered by the taskbar in the **total** height (unlike `availHeight`).",
       "Use it for “how big is the display?”, not “how big is my page?”."],
      """document.getElementById("demo").innerHTML = "Screen Height: " + screen.height;""",
      "The page prints **Screen Height:** and the monitor height in pixels.",
      js="""      document.getElementById("demo").innerText = "Screen Height: " + screen.height;"""),
    P("avail-width", "screen.availWidth — width minus OS chrome",
      ["`availWidth` subtracts **interface features** such as a Windows taskbar if it reduces usable width.",
       "On many desktops it equals `screen.width` because the taskbar is on the bottom.",
       "On a vertical taskbar it can be smaller than `width`."],
      """document.getElementById("demo").innerHTML = "Available Screen Width: " + screen.availWidth;""",
      "**Available Screen Width:** is `availWidth` (≤ `screen.width`).",
      js="""      document.getElementById("demo").innerText = "Available Screen Width: " + screen.availWidth;"""),
    P("avail-height", "screen.availHeight — height minus OS chrome",
      ["`availHeight` is height minus the taskbar (and similar OS UI).",
       "Typically `availHeight < height` when a bottom taskbar is present.",
       "This is still **not** the browser viewport — that is `innerHeight`."],
      """document.getElementById("demo").innerHTML = "Available Screen Height: " + screen.availHeight;""",
      "**Available Screen Height:** is `availHeight` (often less than `screen.height`).",
      js="""      document.getElementById("demo").innerText = "Available Screen Height: " + screen.availHeight;"""),
    P("color-depth", "screen.colorDepth — bits per color",
      ["`colorDepth` is how many bits are used to display one color.",
       "Modern displays: **24** (“True Color”, 16,777,216 colors) or **32** (“Deep Color”).",
       "Older: **16** High Color; very old: **8** VGA (256 colors).",
       "32-bit often still means 24-bit color plus 8-bit alpha at the hardware level — the property still reports 24 or 32."],
      """document.getElementById("demo").innerHTML = "Screen Color Depth: " + screen.colorDepth;""",
      "**Screen Color Depth:** is typically **24** or **32** on a current machine.",
      js="""      document.getElementById("demo").innerText = "Screen Color Depth: " + screen.colorDepth;"""),
    P("pixel-depth", "screen.pixelDepth — bits per pixel",
      ["`pixelDepth` is the bit depth of the screen.",
       "On modern browsers it is usually **the same number as `colorDepth`**.",
       "Do not use either property to detect “the user’s device type” — they are about color, not phone vs desktop."],
      """document.getElementById("demo").innerHTML = "Screen Pixel Depth: " + screen.pixelDepth;""",
      "**Screen Pixel Depth:** matches this display’s reported bit depth (often equal to `colorDepth`).",
      js="""      document.getElementById("demo").innerText = "Screen Pixel Depth: " + screen.pixelDepth;"""),
]

SCR_QA = qa(
    ("Is `screen.width` the browser width?", ["**No** — it is the **monitor**. Use `innerWidth` for the viewport."]),
    ("What does `availHeight` leave out?", ["OS UI such as the **taskbar**."]),
    ("Typical modern `colorDepth`?", ["**24** or **32** bits."]),
    ("How many colors is 24-bit?", ["**16,777,216** (“True Color”)."]),
    ("Can you skip the `window.` prefix?", ["**Yes** — `screen.width` is the same as `window.screen.width`."]),
    ("Is `pixelDepth` usually different from `colorDepth`?", ["Usually **the same** on current browsers."]),
    ("16-bit color is called what on the page?", ["**High Color** (65,536 colors)."]),
    ("8-bit color is called what?", ["**VGA colors** (256)."]),
    ("When would `availWidth` be smaller than `width`?", ["When a **vertical taskbar** (or similar) reduces usable width."]),
    ("Which object is this page about?", ["**`window.screen`**."]),
)

# ---------------------------------------------------------------------------
# 27.3 JS Location
# ---------------------------------------------------------------------------

LOC = [
    P("href", "window.location.href — full URL of this page",
      ["`location` (or `window.location`) is the current **address** and a way to **navigate**.",
       "`href` is the entire URL: protocol, host, port, path, query, hash.",
       "Assigning to `href` loads a new page (same as clicking a link).",
       "The sandbox is served from `http://127.0.0.1:8771/...` so `href` includes that."],
      """document.getElementById("demo").innerHTML = "Page location is " + window.location.href;""",
      "**Page location is** the full sandbox URL (http, 127.0.0.1, port, path).",
      js="""      document.getElementById("demo").innerText = "Page location is " + window.location.href;"""),
    P("hostname", "window.location.hostname — host name",
      ["`hostname` is the **domain** (or IP) without protocol or port.",
       "On this sandbox it is **`127.0.0.1`**.",
       "It does not include `:8771` — that is `port`."],
      """document.getElementById("demo").innerHTML = "Page hostname is " + window.location.hostname;""",
      "**Page hostname is 127.0.0.1** (or `localhost` if you used that host).",
      js="""      document.getElementById("demo").innerText = "Page hostname is " + window.location.hostname;"""),
    P("pathname", "window.location.pathname — path and file name",
      ["`pathname` is the path after the host, starting with `/`.",
       "It does **not** include the query string or hash.",
       "Here it ends with the example file name under `/js-location/`."],
      """document.getElementById("demo").innerHTML = "Page path is " + window.location.pathname;""",
      "**Page path is** `/js-location/pathname.html` (this file).",
      js="""      document.getElementById("demo").innerText = "Page path is " + window.location.pathname;"""),
    P("protocol", "window.location.protocol — http: or https:",
      ["`protocol` includes the colon: **`http:`** or **`https:`**.",
       "The sandbox server is not TLS, so this page is **`http:`**.",
       "Use this if you need to know whether the page is secure."],
      """document.getElementById("demo").innerHTML = "Page protocol is " + window.location.protocol;""",
      "**Page protocol is http:** on the local static server.",
      js="""      document.getElementById("demo").innerText = "Page protocol is " + window.location.protocol;"""),
    P("port", "window.location.port — host port number",
      ["`port` is the port as a **string**. Default ports (80/443) are often **empty**.",
       "This sandbox uses **8771**, so `port` is **`8771`**.",
       "The W3Schools Tryit title says “Display the name of the host” but the code reads **`port`** — we follow the code."],
      """document.getElementById("demo").innerHTML = "Port number is " + window.location.port;""",
      "**Port number is 8771** for this HTTP screenshot server.",
      js="""      document.getElementById("demo").innerText = "Port number is " + window.location.port;"""),
    P("assign", "window.location.assign() — load a new document",
      ["`assign(url)` loads `url` and **pushes** a history entry (Back can return).",
       "`location.href = url` does the same for most purposes.",
       "`replace(url)` also navigates but **does not** keep the current page in history.",
       "The snapshot does **not** leave this page (that would blank the result). It shows the handler that *would* assign."],
      """<input type="button" value="Load new document" onclick="newDoc()">
<script>
function newDoc() {
  window.location.assign("https://www.w3schools.com");
}
</script>""",
      "The button is present; the snapshot prints that `newDoc` would **assign** `https://www.w3schools.com` rather than navigating away.",
      body='<input id="b" type="button" value="Load new document">',
      js="""      function newDoc() {
        document.getElementById("demo").innerText =
          "would assign https://www.w3schools.com (not followed in snapshot)";
      }
      document.getElementById("b").onclick = newDoc;
      newDoc();"""),
]

LOC_QA = qa(
    ("What object reads the current URL?", ["**`window.location`** (also just `location`)."]),
    ("Which property is the full URL?", ["**`href`**."]),
    ("Does `hostname` include the port?", ["**No** — port is **`location.port`**."]),
    ("What does `pathname` start with?", ["A **slash**, e.g. `/js-location/pathname.html`."]),
    ("What is `protocol` for this sandbox?", ["**`http:`** (colon included)."]),
    ("When is `port` an empty string?", ["When the URL uses the **default** port (80 or 443)."]),
    ("What does `assign` do to history?", ["It **adds** an entry so Back can return."]),
    ("How is `replace` different?", ["It **overwrites** the current history entry."]),
    ("Name three location properties from the page.", ["Any three of **href, hostname, pathname, protocol, port**."]),
    ("Does assigning `href` load a new page?", ["**Yes** — it navigates."]),
)

# ---------------------------------------------------------------------------
# 27.4 JS History
# ---------------------------------------------------------------------------

HIST = [
    P("back", "history.back() — previous session entry",
      ["`history.back()` is the same as the browser **Back** button.",
       "It loads the previous **session history** entry (may be another site).",
       "There is no previous page in this snapshot, so we do not call it (it would leave or no-op).",
       "The button in the Tryit is `onclick=\"history.back()\"`."],
      """<button onclick="history.back()">Go Back</button>""",
      "The **Go Back** button is in the page. `typeof history.back` is **function**; it is not invoked here.",
      body='<button type="button" id="b">Go Back</button>',
      js="""      document.getElementById("b").onclick = function () { history.back(); };
      document.getElementById("demo").innerText =
        "typeof back=" + typeof history.back + " length=" + history.length + " (not clicked)";"""),
    P("forward", "history.forward() — next session entry",
      ["`history.forward()` is the **Forward** button.",
       "It only works if the user already went Back (there is a “next” entry).",
       "Equivalent to `history.go(1)`."],
      """<button onclick="history.forward()">Go Forward</button>""",
      "**Go Forward** is wired to `history.forward`. The snapshot does not navigate away.",
      body='<button type="button" id="b">Go Forward</button>',
      js="""      document.getElementById("b").onclick = function () { history.forward(); };
      document.getElementById("demo").innerText =
        "typeof forward=" + typeof history.forward + " (not clicked)";"""),
    P("go-back-two", "history.go(-2) — two steps back",
      ["`go(delta)` moves **relative** to the current entry.",
       "`go(-2)` is “back two pages”.",
       "If there are not enough entries, the call does nothing useful."],
      """<button onclick="history.go(-2)">Go Back</button>""",
      "The button would call **`history.go(-2)`**. Not clicked in the snapshot.",
      body='<button type="button" id="b">Go Back</button>',
      js="""      document.getElementById("demo").innerText = "button would call history.go(-2)";"""),
    P("go-forward-one", "history.go(1) — one step forward",
      ["`go(1)` is the same as **`forward()`**.",
       "Positive numbers go forward; negative go back."],
      """<button onclick="history.go(1)">Go Forward</button>""",
      "The control is labeled **Go Forward** and would call `go(1)`.",
      body='<button type="button">Go Forward</button>',
      js="""      document.getElementById("demo").innerText = "history.go(1) === history.forward()";"""),
    P("go-zero", "history.go(0) reloads the current page",
      ["`go(0)` **reloads** the current entry.",
       "`back()` ≡ `go(-1)`. `forward()` ≡ `go(1)`.",
       "Do not call `go(0)` in a screenshot — the reload races the capture.",
       "Prefer `location.reload()` when you mean reload."],
      """history.go(0) reloads the current page.
history.back() is equivalent to history.go(-1).
history.forward() is equivalent to history.go(1).""",
      "The note is printed; **no reload** is performed.",
      js="""      document.getElementById("demo").innerText =
        "go(0) reloads\\nback() === go(-1)\\nforward() === go(1)";"""),
    P("length", "history.length — number of session entries",
      ["`length` is how many entries are in **this tab’s** session history.",
       "It is at least **1** (the current page).",
       "You cannot read other tabs’ history (privacy)."],
      """let length = history.length;""",
      "`history.length` is an integer **≥ 1** for this tab.",
      js=show_js("history.length")),
    P("state-null", "history.state is null until pushState/replaceState",
      ["`state` is the **data object** stored with the current history entry.",
       "On a normal first load it is **`null`**.",
       "It becomes an object after `pushState` or `replaceState`."],
      """let state = history.state;""",
      "On this fresh example page, `history.state` is **null**.",
      js="""      document.getElementById("demo").innerText = "state=" + JSON.stringify(history.state);"""),
    P("push-state", "history.pushState(state, \"\", url)",
      ["`pushState(state, unused, url)` **adds** an entry without loading a document.",
       "The second argument is unused (was `title`; pass `\"\"`).",
       "`url` must be **same-origin**. Here we use `?page=2`.",
       "The page content does **not** change unless you update the DOM yourself."],
      """let state = {name:"example", page: 2};
let url = "page2.html";
history.pushState(state, "", url);""",
      "After `pushState`, `history.state.page` is **2** and the query/path reflects the new URL. The heading text is still this page — no load.",
      js="""      history.pushState({name:"example", page: 2}, "", "?page=2");
      document.getElementById("demo").innerText =
        "state=" + JSON.stringify(history.state) +
        "\\nsearch=" + location.search +
        "\\nstill this document (no load)";"""),
    P("push-no-load", "pushState does not load a new page",
      ["If you need new HTML from the server, set `location.href` (or `assign`).",
       "`pushState` only updates **history + URL**. SPAs then render in JS.",
       "W3Schools notes a separate `location.href = \"page2.html\"` if content should change."],
      """history.pushState() method does not load a new page.""",
      "`document.title` is unchanged after `pushState` — proof the document was not replaced.",
      js="""      const before = document.title;
      history.pushState({n: 1}, "", "?n=1");
      document.getElementById("demo").innerText =
        "title still=" + document.title + " same=" + (document.title === before);"""),
    P("replace-state", "history.replaceState(state, \"\", url)",
      ["`replaceState` **overwrites** the current entry — history length does not grow.",
       "Useful to fix a URL without creating a Back step.",
       "Same-origin rules still apply."],
      """let state = {name:"example", page: 2};
let url = "page2.html";
history.replaceState(state, "", url);""",
      "`replaceState` sets `state.page` to **2**. Length does not increase because of this call.",
      js="""      const before = history.length;
      history.replaceState({name:"example", page: 2}, "", "?page=2");
      document.getElementById("demo").innerText =
        "state=" + JSON.stringify(history.state) +
        "\\nlength before=" + before + " after=" + history.length;"""),
    P("replace-no-load", "replaceState does not load a new page",
      ["Like `pushState`, it only changes the **current** history slot.",
       "You must still update the DOM if the UI should match the new URL."],
      """history.replaceState() method does not load a new page.""",
      "The document is the same; only `history.state` / URL change.",
      js="""      history.replaceState({ok: true}, "", "?replaced=1");
      document.getElementById("demo").innerText =
        "href has replaced=" + /replaced=1/.test(location.href) +
        " body still this page";"""),
    P("popstate", "popstate fires on Back/Forward",
      ["`popstate` runs when the **active** history entry changes via Back/Forward/`go`.",
       "It does **not** fire for the `pushState`/`replaceState` call itself.",
       "Listen on `window`."],
      """window.addEventListener("popstate", function(event) {
  myDisplayer("Page changed");
});""",
      "After `pushState` then `history.back()`, the listener runs and prints **Page changed**.",
      js="""      window.addEventListener("popstate", function () {
        document.getElementById("demo").innerText = "Page changed";
      });
      history.pushState({page: "a"}, "", "?a=1");
      history.pushState({page: "b"}, "", "?b=1");
      history.back();""",
      wait_ms=1500),
    P("popstate-state", "popstate event.state",
      ["The event’s **`state`** is the object you stored with `pushState`.",
       "It can be `null` for entries that were never given state.",
       "Use it to restore the SPA view."],
      """window.addEventListener("popstate", function(event) {
  if (event.state) {
    myDisplayer(event.state.page);
  }
});""",
      "Going back to the `about` state prints **about** from `event.state.page`.",
      js="""      window.addEventListener("popstate", function (event) {
        if (event.state) {
          document.getElementById("demo").innerText = String(event.state.page);
        }
      });
      history.pushState({page: "home"}, "", "?page=home");
      history.pushState({page: "about"}, "", "?page=about");
      history.back();""",
      wait_ms=1500),
    P("spa-example", "Simple History API example (Home / About)",
      ["Buttons call `showPage`, which updates the paragraph **and** `pushState`.",
       "`popstate` restores the paragraph when the user hits Back.",
       "This is the SPA pattern in miniature."],
      """<button onclick="showPage('home')">Home</button>
<button onclick="showPage('about')">About</button>
<p id="out">Home</p>
<script>
function showPage(page) {
  myDisplayer(page);
  history.pushState({page: page}, "", "?page=" + page);
}
window.addEventListener("popstate", function(event) {
  if (event.state) { myDisplayer(event.state.page); }
});
</script>""",
      "After clicking **About**, the paragraph is **about** and the URL has `?page=about`.",
      body='<button type="button" id="home">Home</button> <button type="button" id="about">About</button><p id="out">Home</p>',
      js="""      function myDisplayer(page) {
        document.getElementById("out").textContent = page;
      }
      function showPage(page) {
        myDisplayer(page);
        history.pushState({page: page}, "", "?page=" + page);
      }
      document.getElementById("home").onclick = function () { showPage("home"); };
      document.getElementById("about").onclick = function () { showPage("about"); };
      showPage("about");
      document.getElementById("demo").innerText =
        "out=" + document.getElementById("out").textContent + " search=" + location.search;"""),
    P("scroll-restoration", "history.scrollRestoration",
      ["`scrollRestoration` is **`\"auto\"`** (browser restores scroll) or **`\"manual\"`** (you restore it).",
       "SPAs often set **`manual`** so Back does not jump to a leftover scroll position.",
       "W3Schools: `history.scrollRestoration = \"manual\"`."],
      """history.scrollRestoration = "manual";""",
      "After assignment, `scrollRestoration` is **manual**.",
      js="""      history.scrollRestoration = "manual";
      document.getElementById("demo").innerText = "scrollRestoration=" + history.scrollRestoration;"""),
]

HIST_QA = qa(
    ("What is `history.back()` equal to?", ["The browser **Back** button, and `history.go(-1)`."]),
    ("What does `go(0)` do?", ["**Reloads** the current page."]),
    ("Does `pushState` fetch new HTML?", ["**No** — it only adds a history entry and may change the URL."]),
    ("How is `replaceState` different?", ["It **changes the current** entry and does not add one."]),
    ("When is `history.state` null?", ["Until you call **`pushState` or `replaceState`** (and for entries without state)."]),
    ("When does `popstate` fire?", ["On **Back / Forward / go**, not on the `pushState` call itself."]),
    ("What is `event.state`?", ["The **object** you stored with that history entry."]),
    ("What does `length` count?", ["Entries in **this tab’s** session history."]),
    ("Why set `scrollRestoration = \"manual\"`?", ["So **you** control scroll when the user navigates history (common in SPAs)."]),
    ("Must `pushState` URLs be same-origin?", ["**Yes**."]),
    ("In the Home/About demo, who updates the paragraph on Back?", ["The **`popstate`** listener reading `event.state.page`."]),
)

# ---------------------------------------------------------------------------
# 27.5 JS Navigator
# ---------------------------------------------------------------------------

NAV = [
    P("cookie-enabled", "navigator.cookieEnabled",
      ["`navigator` describes the **browser / user agent**.",
       "`cookieEnabled` is **true** if cookies are enabled.",
       "It does not tell you whether *your* cookie was stored — only the preference.",
       "Can be written `window.navigator` or `navigator`."],
      """document.getElementById("demo").innerHTML =
  "cookiesEnabled is " + navigator.cookieEnabled;""",
      "**cookiesEnabled is true** (or false if cookies are off in this browser).",
      js="""      document.getElementById("demo").innerText =
        "cookiesEnabled is " + navigator.cookieEnabled;"""),
    P("language", "navigator.language — browser language",
      ["`language` is a BCP 47 tag such as `en-US` or `en`.",
       "It is the UI/preferred language, not the page’s `<html lang>`."],
      """document.getElementById("demo").innerHTML = navigator.language;""",
      "The page prints the browser language tag (for example **en-US**).",
      js=show_js("navigator.language")),
    P("online", "navigator.onLine — is the browser online?",
      ["`onLine` is **true** if the browser thinks it has a network.",
       "It can be **wrong** (captive portal, “online” but no internet).",
       "Listen to `window` events `online` / `offline` for changes."],
      """document.getElementById("demo").innerHTML = navigator.onLine;""",
      "`navigator.onLine` is **true** or **false** as a boolean (printed as such).",
      js=show_js("navigator.onLine")),
    P("app-name", "navigator.appName — application name (do not trust)",
      ["`appName` historically returned the browser product name.",
       "**Warning (W3Schools + MDN):** it is unreliable. Chrome/Firefox often report **`Netscape`** for compatibility.",
       "Do not use it for feature detection."],
      """document.getElementById("demo").innerHTML =
  "navigator.appName is " + navigator.appName;""",
      "**navigator.appName is** typically **Netscape** even in Chrome — which is why the page warns you.",
      js="""      document.getElementById("demo").innerText =
        "navigator.appName is " + navigator.appName;"""),
    P("app-code-name", "navigator.appCodeName — code name (do not trust)",
      ["`appCodeName` is another frozen compatibility string, usually **`Mozilla`**.",
       "The page warns: do not use it to identify the browser."],
      """document.getElementById("demo").innerHTML =
  "navigator.appCodeName is " + navigator.appCodeName;""",
      "**navigator.appCodeName is Mozilla** on almost every modern engine.",
      js="""      document.getElementById("demo").innerText =
        "navigator.appCodeName is " + navigator.appCodeName;"""),
    P("product", "navigator.product — engine product (do not trust)",
      ["`product` is supposed to be the engine name; it is usually **`Gecko`** even in Chromium.",
       "Same warning: **not** a real browser sniff."],
      """document.getElementById("demo").innerHTML =
  "navigator.product is " + navigator.product;""",
      "**navigator.product is Gecko** on this engine (compatibility value).",
      js="""      document.getElementById("demo").innerText =
        "navigator.product is " + navigator.product;"""),
    P("app-version", "navigator.appVersion — version string (do not trust)",
      ["`appVersion` is a long compatibility string, not a clean version number.",
       "The page warns it does **not** return the correct browser version.",
       "Use feature detection, not this string."],
      """document.getElementById("demo").innerHTML = navigator.appVersion;""",
      "`appVersion` prints a long UA-like string; do not parse it as “the version”.",
      js=show_js("navigator.appVersion")),
    P("user-agent", "navigator.userAgent — UA header (do not trust)",
      ["`userAgent` is what the browser sends as **User-Agent**.",
       "It is spoofable, frozen in places, and a poor way to detect features.",
       "The page still shows it because many tutorials mention it — then warns you."],
      """document.getElementById("demo").innerHTML = navigator.userAgent;""",
      "The full user-agent string is printed. Treat it as **unreliable** for branching.",
      js=show_js("navigator.userAgent")),
    P("platform", "navigator.platform — OS/platform (do not trust)",
      ["`platform` was meant to be the OS (e.g. `Win32`).",
       "The page warns it is **not** correct in all browsers (and some lie for privacy).",
       "`userAgentData.platform` (where supported) is the newer hint — still not for capability checks."],
      """document.getElementById("demo").innerHTML = navigator.platform;""",
      "`platform` prints a string such as **Win32**. Do not use it as a hard OS check.",
      js=show_js("navigator.platform")),
    P("java-enabled", "navigator.javaEnabled() always false",
      ["`javaEnabled()` used to report whether **Java** (the plugin) was on.",
       "W3Schools warning: it **always returns false** now — the plugin is gone.",
       "Calling it is harmless; do not build logic on it."],
      """document.getElementById("demo").innerHTML = navigator.javaEnabled();""",
      "`javaEnabled()` returns **false**.",
      js="""      document.getElementById("demo").innerText = String(navigator.javaEnabled());"""),
]

NAV_QA = qa(
    ("How do you know if cookies are enabled?", ["**`navigator.cookieEnabled`** (boolean)."]),
    ("What does `language` return?", ["A **language tag** such as `en-US`."]),
    ("Is `onLine` a perfect network test?", ["**No** — it is the browser’s guess."]),
    ("Why is `appName` useless?", ["Engines lie and often report **Netscape**."]),
    ("What is a typical `appCodeName`?", ["**Mozilla**."]),
    ("What is a typical `product`?", ["**Gecko** (even in Chrome)."]),
    ("Should you parse `userAgent` to detect Chrome?", ["**No** — use **feature detection**."]),
    ("What does `javaEnabled()` return today?", ["Always **false**."]),
    ("Can you omit `window.`?", ["**Yes** — `navigator` is a `window` property."]),
    ("Name two navigator properties that are still somewhat useful.", ["**`cookieEnabled`**, **`language`**, **`onLine`** (with caveats)."]),
)

# ---------------------------------------------------------------------------
# 27.6 JS Popup Alert
# ---------------------------------------------------------------------------

POP_BOOT = """
      window.alert = function (msg) {
        document.getElementById("demo").innerText = "alert:\\n" + String(msg);
      };
      window.confirm = function (msg) {
        document.getElementById("demo").innerText =
          (document.getElementById("demo").innerText + "\\nconfirm: " + msg).trim();
        return true;
      };
      window.prompt = function (msg, deflt) {
        document.getElementById("demo").innerText =
          "prompt: " + msg + " default=" + deflt;
        return deflt;
      };
"""

POP = [
    P("alert", "alert() — alert box",
      ["`window.alert(text)` (or `alert`) shows a modal message with **OK**.",
       "It **blocks** script until dismissed — avoid it in real UIs.",
       "You may omit the `window.` prefix.",
       "Headless Chrome cannot show a native dialog in the PNG, so the sandbox **mirrors** the message on the page (same approach as JS Output)."],
      """alert("I am an alert box!");""",
      "The mirrored output is **alert: I am an alert box!**",
      js=POP_BOOT + """
      alert("I am an alert box!");"""),
    P("confirm", "confirm() — OK / Cancel",
      ["`confirm(text)` returns **`true`** for OK and **`false`** for Cancel.",
       "Use the return value in an `if`.",
       "Also modal and blocking — prefer a `<dialog>` for in-page UI.",
       "The snapshot stubs `confirm` to return **true** (OK)."],
      """if (confirm("Press a button!")) {
  txt = "You pressed OK!";
} else {
  txt = "You pressed Cancel!";
}""",
      "With OK stubbed, `txt` is **You pressed OK!**",
      js=POP_BOOT + """
      let txt;
      if (confirm("Press a button!")) {
        txt = "You pressed OK!";
      } else {
        txt = "You pressed Cancel!";
      }
      document.getElementById("demo").innerText += "\\n" + txt;"""),
    P("prompt", "prompt() — ask for text",
      ["`prompt(message, defaultText)` returns the string, or **`null`** if cancelled.",
       "Empty OK yields `\"\"`. Always check `null` and `\"\"`.",
       "The W3Schools default is **Harry Potter**.",
       "The snapshot returns that default (as if the user clicked OK)."],
      """let person = prompt("Please enter your name", "Harry Potter");
let text;
if (person == null || person == "") {
  text = "User cancelled the prompt.";
} else {
  text = "Hello " + person + "! How are you today?";
}""",
      "With default **Harry Potter** accepted, the greeting is **Hello Harry Potter! How are you today?**",
      js=POP_BOOT + """
      let person = prompt("Please enter your name", "Harry Potter");
      let text;
      if (person == null || person == "") {
        text = "User cancelled the prompt.";
      } else {
        text = "Hello " + person + "! How are you today?";
      }
      document.getElementById("demo").innerText += "\\n" + text;"""),
    P("line-breaks", "Line breaks in popup text with \\n",
      ["Popup text is **plain text**, not HTML.",
       "Use **`\\n`** for a new line (`alert(\"Hello\\nHow are you?\")`).",
       "`<br>` would show as those characters, not a break."],
      """alert("Hello\\nHow are you?");""",
      "The mirrored alert shows two lines: **Hello** then **How are you?**",
      js=POP_BOOT + """
      alert("Hello\\nHow are you?");"""),
]

POP_QA = qa(
    ("What does `alert` show?", ["A **modal** message with OK."]),
    ("What does `confirm` return?", ["**`true`** (OK) or **`false`** (Cancel)."]),
    ("What does `prompt` return on Cancel?", ["**`null`**."]),
    ("Can you omit `window.`?", ["**Yes** for `alert`, `confirm`, and `prompt`."]),
    ("How do you put two lines in an alert?", ["A **`\\n`** in the string."]),
    ("Does `alert` accept HTML?", ["**No** — it is plain text."]),
    ("Why avoid these in production UIs?", ["They **block** the thread and cannot be styled."]),
    ("What is the W3Schools prompt default?", ["**Harry Potter**."]),
    ("What text appears if confirm is cancelled?", ["**You pressed Cancel!** in their if/else."]),
    ("What is a modern in-page alternative?", ["The HTML **`<dialog>`** element (or non-modal UI)."]),
)

# ---------------------------------------------------------------------------
# 27.7 JS Cookies
# ---------------------------------------------------------------------------

COOKIE_HELPERS = r"""
      function setCookie(cname, cvalue, exdays) {
        const d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        let expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
      }
      function getCookie(cname) {
        let name = cname + "=";
        let decodedCookie = decodeURIComponent(document.cookie);
        let ca = decodedCookie.split(";");
        for (let i = 0; i < ca.length; i++) {
          let c = ca[i];
          while (c.charAt(0) == " ") {
            c = c.substring(1);
          }
          if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
          }
        }
        return "";
      }
      function clearNameCookie() {
        document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      }
"""

CK = [
    P("create", "Create a cookie — document.cookie = name=value",
      ["A cookie is a small **name=value** string the browser stores for a site.",
       "`document.cookie = \"username=John Doe\"` **adds** (or updates) that cookie.",
       "Reading `document.cookie` later returns the name/value pairs, not the expires/path you wrote.",
       "Must be served over **http(s)** — `file://` often will not store cookies."],
      """document.cookie = "username=John Doe";""",
      "After setting, `document.cookie` contains **username=John Doe** (among any others).",
      js=COOKIE_HELPERS + """
      clearNameCookie();
      document.cookie = "username=John Doe";
      document.getElementById("demo").innerText = document.cookie;"""),
    P("expires", "Cookie with expires date",
      ["Add **`expires=UTC-date`** so the cookie survives the session.",
       "Without expires, it is often a **session** cookie (cleared when the browser closes).",
       "The W3Schools sample date is in the **past** (`18 Dec 2013`) — that would **delete** the cookie today. The sandbox uses a **future** date so the create-with-expires idea actually sticks."],
      """document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC";""",
      "With a future `expires`, the cookie is stored and `username=John Doe` is readable. A 2013 expiry (as on the page) would expire immediately.",
      js=COOKIE_HELPERS + """
      clearNameCookie();
      const future = new Date(Date.now() + 864e5).toUTCString();
      document.cookie = "username=John Doe; expires=" + future;
      document.getElementById("demo").innerText =
        "cookie=" + document.cookie + "\\n(used a future expires; page sample 2013 would delete it)";"""),
    P("path", "Cookie with path=/",
      ["**`path=/`** makes the cookie available on the whole site, not only the current folder.",
       "If you omit path, it defaults to the **current path**, which surprises people later.",
       "Always set `path=/` unless you have a reason not to."],
      """document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";""",
      "The cookie is set with **path=/** and the name/value is visible on this path.",
      js=COOKIE_HELPERS + """
      clearNameCookie();
      const future = new Date(Date.now() + 864e5).toUTCString();
      document.cookie = "username=John Doe; expires=" + future + "; path=/";
      document.getElementById("demo").innerText = document.cookie;"""),
    P("read", "Read cookies — let x = document.cookie",
      ["Reading `document.cookie` returns **all** cookies as one string: `n=v; n2=v2`.",
       "You do **not** get expires, path, or httpOnly flags.",
       "`HttpOnly` cookies are invisible to JavaScript by design."],
      """let x = document.cookie;""",
      "`x` is the cookie string, including **username=…** after we set it.",
      js=COOKIE_HELPERS + """
      document.cookie = "username=John Doe; path=/";
      let x = document.cookie;
      document.getElementById("demo").innerText = x;"""),
    P("change", "Change a cookie by setting the same name",
      ["To change a cookie, **set it again** with the same name (and the same path).",
       "`username=John Smith` replaces `username=John Doe`.",
       "A different `path` looks like a different cookie."],
      """document.cookie = "username=John Smith; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";""",
      "After the change, the stored username is **John Smith**.",
      js=COOKIE_HELPERS + """
      const future = new Date(Date.now() + 864e5).toUTCString();
      document.cookie = "username=John Doe; expires=" + future + "; path=/";
      document.cookie = "username=John Smith; expires=" + future + "; path=/";
      document.getElementById("demo").innerText = "cookie=" + document.cookie;"""),
    P("delete", "Delete a cookie with an expired date",
      ["There is no `deleteCookie`. Set **`expires` in the past** (Unix epoch is conventional).",
       "You must match **name + path** (and domain if you set one).",
       "`username=; expires=Thu, 01 Jan 1970 …; path=/;`"],
      """document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";""",
      "After the epoch expiry, `getCookie(\"username\")` is empty.",
      js=COOKIE_HELPERS + """
      document.cookie = "username=John Doe; path=/";
      document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      document.getElementById("demo").innerText =
        "username via getCookie=" + JSON.stringify(getCookie("username"));"""),
    P("cookie-string", "Reading cookie returns only name=value pairs",
      ["Even if you write `expires` and `path`, **read-back is only** `name=value` pairs.",
       "Setting a **new** name **adds**; it does not wipe other cookies.",
       "The page’s buttons (display / create 1 / create 2 / delete) are this idea."],
      """document.cookie will return all cookies in one string much like:
cookie1=value; cookie2=value; cookie3=value;""",
      "After creating **c1=one** and **c2=two**, the read-back string contains both names and **no** expires text.",
      js="""      document.cookie = "c1=one; path=/";
      document.cookie = "c2=two; path=/";
      document.getElementById("demo").innerText = document.cookie;"""),
    P("set-cookie-fn", "setCookie(cname, cvalue, exdays)",
      ["W3Schools helper: compute `expires` from **days**, then write `name=value;expires;path=/`.",
       "`exdays * 24 * 60 * 60 * 1000` is milliseconds.",
       "Always include **path=/** in the helper so later `getCookie` works site-wide."],
      """function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  let expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}""",
      "`setCookie(\"username\", \"Ada\", 1)` stores **Ada** for one day.",
      js=COOKIE_HELPERS + """
      clearNameCookie();
      setCookie("username", "Ada", 1);
      document.getElementById("demo").innerText = "username=" + getCookie("username");"""),
    P("get-cookie-fn", "getCookie(cname) — parse the cookie string",
      ["Split `document.cookie` on **`;`**, trim spaces, find `name=`.",
       "`decodeURIComponent` undoes encoding in values.",
       "Return `\"\"` if the name is missing — that is what `checkCookie` tests."],
      """function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') { c = c.substring(1); }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}""",
      "`getCookie(\"username\")` returns **Ada** after `setCookie`.",
      js=COOKIE_HELPERS + """
      setCookie("username", "Ada", 1);
      document.getElementById("demo").innerText =
        "getCookie username=" + getCookie("username") +
        "\\nmissing=" + JSON.stringify(getCookie("nope"));"""),
    P("check-cookie-fn", "checkCookie() — welcome or prompt",
      ["If `getCookie(\"username\")` is non-empty, **`alert(\"Welcome again \" + username)`**.",
       "Otherwise **`prompt`** for a name and `setCookie(..., 365)` if they typed one.",
       "Native dialogs are stubbed in the snapshot: prompt returns **Sam**, then welcome can be shown on a second check."],
      """function checkCookie() {
  let username = getCookie("username");
  if (username != "") {
    alert("Welcome again " + username);
  } else {
    username = prompt("Please enter your name:", "");
    if (username != "" && username != null) {
      setCookie("username", username, 365);
    }
  }
}""",
      "With no cookie, the stub prompt returns **Sam**, `setCookie` runs, and a second `checkCookie` would welcome Sam. The snapshot prints the stored name.",
      js=COOKIE_HELPERS + """
      clearNameCookie();
      window.alert = function (m) { document.getElementById("demo").innerText = m; };
      window.prompt = function () { return "Sam"; };
      function checkCookie() {
        let username = getCookie("username");
        if (username != "") {
          alert("Welcome again " + username);
        } else {
          username = prompt("Please enter your name:", "");
          if (username != "" && username != null) {
            setCookie("username", username, 365);
          }
        }
      }
      checkCookie();
      document.getElementById("demo").innerText =
        "after first visit username=" + getCookie("username");
      checkCookie();"""),
    P("all-together", "All together — setCookie + getCookie + checkCookie on load",
      ["The full page example defines all three functions and runs **`checkCookie()`** when the page loads.",
       "First visit: prompt. Later visits: welcome alert.",
       "The snapshot pre-sets **username=Taylor** so load looks like a returning visitor."],
      """function setCookie(cname, cvalue, exdays) { /* ... */ }
function getCookie(cname) { /* ... */ }
function checkCookie() {
  let user = getCookie("username");
  if (user != "") { alert("Welcome again " + user); }
  else {
    user = prompt("Please enter your name:", "");
    if (user != "" && user != null) { setCookie("username", user, 365); }
  }
}
checkCookie();""",
      "On load with an existing cookie, the mirrored alert is **Welcome again Taylor**.",
      js=COOKIE_HELPERS + """
      window.alert = function (m) { document.getElementById("demo").innerText = m; };
      setCookie("username", "Taylor", 1);
      function checkCookie() {
        let user = getCookie("username");
        if (user != "") { alert("Welcome again " + user); }
        else {
          user = prompt("Please enter your name:", "");
          if (user != "" && user != null) { setCookie("username", user, 365); }
        }
      }
      checkCookie();"""),
]

CK_QA = qa(
    ("How do you create a cookie?", ["Assign **`document.cookie = \"name=value\"`**."]),
    ("Does a new assignment erase other cookies?", ["**No** — it **adds** or updates that **name** (same path)."]),
    ("How do you delete a cookie?", ["Set it again with **`expires` in the past** (1970) and the **same path**."]),
    ("What do you see when you read `document.cookie`?", ["Only **name=value** pairs, not expires/path."]),
    ("Why set `path=/`?", ["So the cookie is visible on **the whole site**, not just this folder."]),
    ("What does `getCookie` return if the name is missing?", ["An **empty string**."]),
    ("What does `checkCookie` do on a returning visitor?", ["**`alert(\"Welcome again \" + username)`**."]),
    ("What if `prompt` is cancelled?", ["It returns **`null`** — do not call `setCookie`."]),
    ("Why did the page’s 2013 `expires` need a note?", ["That date is **in the past**, so it would **delete** the cookie today."]),
    ("Can JS read `HttpOnly` cookies?", ["**No**."]),
    ("Must examples run on http(s)?", ["**Yes** — `file://` often cannot store cookies."]),
)

# ---------------------------------------------------------------------------
# 27.8 JS Fetch API
# ---------------------------------------------------------------------------

FETCH_FILES = {
    "fetch.txt": FETCH_TXT,
    "customer.json": CUSTOMER_JSON,
}

async_js = """      (async function () {
        const out = [];
        function show(v) { out.push(String(v)); }
        try {
%s
        } catch (e) {
          out.push(e.name + ": " + e.message);
        }
        document.getElementById("demo").innerText = out.join("\\n");
      })();"""


def AF(stem, title, bullets, code, outcome, inner_js, extra=None, wait=2500):
    return P(
        stem,
        title,
        bullets,
        code,
        outcome,
        js=async_js % inner_js,
        extra_files=extra or FETCH_FILES,
        wait_ms=wait,
        fence="javascript",
    )


FT = [
    AF("then-text", "fetch().then — read a text file",
       ["`fetch(url)` returns a **Promise** of a **Response**.",
        "The first `.then` receives the Response; **`response.text()`** is another Promise of the body string.",
        "The second `.then` receives that string (W3Schools `myDisplayer(data)`).",
        "Fetch needs **http(s)** — not `file://`."],
       """fetch(file)
  .then(function(response) {
    return response.text();
  })
  .then(function(data) {
    myDisplayer(data);
  });""",
       "The body of **fetch.txt** is displayed: **Hello Fetch API** on the first line.",
       """          const response = await fetch("fetch.txt");
          const data = await response.text();
          show(data.trim());"""),
    AF("then-arrows", "fetch with arrow functions",
       ["Same flow, shorter: `response => response.text()` then `data => myDisplayer(data)`.",
        "Arrows here are just functions — still two async steps.",
        "Errors still need `.catch` or `try/catch` in `async`."],
       """fetch(file)
  .then(response => response.text())
  .then(data => myDisplayer(data));""",
       "Arrow-style fetch also prints the **fetch.txt** contents.",
       """          const data = await fetch("fetch.txt").then(r => r.text());
          show(data.trim());"""),
    AF("async-fn", "async function loadText — await fetch",
       ["`async function` lets you **`await fetch(file)`** then **`await response.text()`**.",
        "This is the same two Promises, written as if they were sequential.",
        "W3Schools `loadText` then calls `myDisplayer`."],
       """async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(await response.text());
}""",
       "`loadText(\"fetch.txt\")` displays the file text.",
       """          const response = await fetch("fetch.txt");
          show((await response.text()).trim());"""),
    AF("response-object", "The Response object",
       ["If you `myDisplayer(response)` without `.text()`, you get a **Response**, not the file contents.",
        "Useful properties: `ok`, `status`, `statusText`, `url`.",
        "`String(response)` is not the body — you must call a reader method."],
       """async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(response);
}""",
       "`response` is an object; `ok` is **true** for fetch.txt. The default string is not the file body.",
       """          const response = await fetch("fetch.txt");
          show("ok=" + response.ok);
          show("ctor=" + response.constructor.name);"""),
    AF("ok", "response.ok",
       ["`ok` is **true** for status **200–299**.",
        "It is **false** for 404/500. Fetch **does not throw** on HTTP errors — check `ok`.",
        "Network failure (offline, CORS) **does** reject the Promise."],
       """async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(response.ok);
}""",
       "`response.ok` is **true** for the existing file.",
       """          const response = await fetch("fetch.txt");
          show(String(response.ok));"""),
    AF("status", "response.status",
       ["`status` is the **HTTP code**: 200, 404, 500, …",
        "Pair it with `ok` when you log errors."],
       """async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(response.status);
}""",
       "`status` is **200** for fetch.txt.",
       """          const response = await fetch("fetch.txt");
          show(String(response.status));"""),
    AF("status-text", "response.statusText",
       ["`statusText` is the reason phrase, e.g. **OK** or **Not Found**.",
        "It can be empty in HTTP/2. Prefer `status` + `ok` for logic."],
       """response.statusText""",
       "For 200, `statusText` is typically **OK**.",
       """          const response = await fetch("fetch.txt");
          show(response.status + " " + response.statusText);"""),
    AF("url", "response.url",
       ["`url` is the **final** URL after redirects.",
        "Useful to see where the browser actually landed."],
       """async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(response.url);
}""",
       "`response.url` ends with **`/js-fetch-api/fetch.txt`**.",
       """          const response = await fetch("fetch.txt");
          show(response.url);"""),
    AF("async-continues", "JavaScript continues while fetch is in flight",
       ["`loadText(\"fetch.txt\")` starts work and **returns immediately**.",
        "The next line `myDisplayer(\"JavaScript continues.\")` runs **before** the file arrives.",
        "That is why the page shows “continues” first, then the file — unless you `await loadText` at the top level."],
       """async function loadText(file) {
  const response = await fetch(file);
  myDisplayer(response.url);
}
loadText("fetch.txt");
myDisplayer("JavaScript continues.");""",
       "The log order is **JavaScript continues.** first, then the response URL — proving fetch is asynchronous.",
       """          const order = [];
          function myDisplayer(v) { order.push(String(v)); }
          async function loadText(file) {
            const response = await fetch(file);
            myDisplayer(response.url);
          }
          const p = loadText("fetch.txt");
          myDisplayer("JavaScript continues.");
          await p;
          show(order.join("\\n"));"""),
    AF("http-error", "Checking HTTP errors — if (!response.ok)",
       ["Fetch **fulfills** on 404. You must **`if (!response.ok)`** and show `status + statusText`.",
        "Then `return` so you do not parse an error page as success.",
        "The sandbox fetches a missing file to force **404**."],
       """async function loadText(file) {
  const response = await fetch(file);
  if (!response.ok) {
    myDisplayer(response.status + " " + response.statusText);
    return;
  }
  myDisplayer(await response.text());
}""",
       "Fetching a missing path prints **404** and a status text (often **Not Found**).",
       """          const response = await fetch("no-such-file.txt");
          if (!response.ok) {
            show(response.status + " " + response.statusText);
            return;
          }
          show(await response.text());"""),
    AF("json-method", "response.json() — parse JSON body",
       ["`json()` reads the body and **`JSON.parse`s** it.",
        "Do **not** call `JSON.parse` again on the result.",
        "Wrong Content-Type still often parses if the bytes are JSON."],
       """const data = await response.json();""",
       "`customer.json` parses to an object whose **name** is **John Doe**.",
       """          const response = await fetch("customer.json");
          const customer = await response.json();
          show(customer.name);"""),
    AF("blob-method", "response.blob() — binary Blob",
       ["`blob()` is for files you might download or put in an `<img>` via `URL.createObjectURL`.",
        "The Blob has `size` and `type`."],
       """const data = await response.blob();""",
       "`fetch.txt` as a Blob has a **size** > 0 and a MIME `type` (often `text/plain`).",
       """          const response = await fetch("fetch.txt");
          const blob = await response.blob();
          show("size=" + blob.size + " type=" + blob.type);"""),
    AF("bytes-method", "response.bytes() — Uint8Array",
       ["`bytes()` is a newer method that returns a **Uint8Array**.",
        "If missing, fall back to `new Uint8Array(await response.arrayBuffer())`.",
        "W3Schools lists it on the Response methods table."],
       """const data = await response.bytes();""",
       "`bytes()` (or the ArrayBuffer fallback) yields a **Uint8Array** whose first bytes decode as **Hello**.",
       """          const response = await fetch("fetch.txt");
          let u8;
          if (typeof response.bytes === "function") {
            u8 = await response.bytes();
            show("via bytes() length=" + u8.length);
          } else {
            u8 = new Uint8Array(await response.arrayBuffer());
            show("bytes() missing; arrayBuffer length=" + u8.length);
          }
          show("start=" + new TextDecoder().decode(u8.slice(0, 5)));"""),
    AF("array-buffer", "response.arrayBuffer() — ArrayBuffer",
       ["`arrayBuffer()` is the raw binary buffer (WebGL, WASM, manual parsing).",
        "`byteLength` is the size in bytes."],
       """const data = await response.arrayBuffer();""",
       "`byteLength` is the file size in bytes (same as the Blob size).",
       """          const response = await fetch("fetch.txt");
          const buf = await response.arrayBuffer();
          show("byteLength=" + buf.byteLength);"""),
    P("xhr-syntax", "Fetch vs XHR — Promise-based vs callback-based",
      ["Fetch is **Promise-based** (`then` / `await`).",
       "XHR is **callback-based** (`onload`, `onerror`).",
       "That is the first row of the comparison table."],
      """fetch(url).then(r => r.text());
// vs
xhr.onload = function () { /* this.responseText */ };""",
      "The snapshot labels the two styles: **Promise-based** vs **callback-based**.",
      js="""      document.getElementById("demo").innerText =
        "Fetch: Promise-based\\nXHR: Callback-based";"""),
    P("xhr-errors", "Fetch vs XHR — error handling",
      ["Fetch **rejects on network failure**, not on 404.",
       "XHR needs **manual** `status` checks in `onload` plus `onerror`.",
       "Always check `response.ok` with Fetch."],
      """if (!response.ok) { /* HTTP error */ }
// XHR: if (xhr.status >= 200 && xhr.status < 300)""",
      "The note prints: Fetch rejects on **network** failure; HTTP errors need **`ok`**.",
      js="""      document.getElementById("demo").innerText =
        "Fetch: rejects on network failure; check response.ok for HTTP errors\\n" +
        "XHR: needs manual status checking";"""),
    P("xhr-streams", "Fetch vs XHR — streams",
      ["Fetch **supports streams** (`response.body` is a ReadableStream).",
       "XHR **does not** give you that streaming body API.",
       "Large downloads can be consumed chunk by chunk with Fetch."],
      """response.body // ReadableStream in Fetch""",
      "`response.body` exists as a **ReadableStream** on this Response.",
      extra_files=FETCH_FILES,
      wait_ms=2500,
      js="""      (async function () {
        const response = await fetch("fetch.txt");
        document.getElementById("demo").innerText =
          "body is ReadableStream=" + (response.body != null) +
          "\\nFetch supports streams; XHR does not";
      })();"""),
]

FT_QA = qa(
    ("What does `fetch` return?", ["A **Promise** that resolves to a **Response**."]),
    ("How do you read a text body?", ["**`response.text()`** (another Promise)."]),
    ("Does Fetch throw on 404?", ["**No** — check **`response.ok`** or `status`."]),
    ("What does `ok` mean?", ["Status is in **200–299**."]),
    ("Why does “JavaScript continues” print first?", ["`fetch` is **asynchronous**; the next line runs before the response."]),
    ("What is `response.url`?", ["The **final** URL after redirects."]),
    ("How do you parse JSON?", ["**`await response.json()`** — do not `JSON.parse` that result again."]),
    ("When does Fetch **reject**?", ["**Network** failure (and some CORS/abort cases), not HTTP 404."]),
    ("Fetch vs XHR syntax?", ["Fetch is **Promise-based**; XHR is **callback-based**."]),
    ("Does XHR support body streams like Fetch?", ["**No**."]),
    ("Why serve these examples over http?", ["Browsers **block** `fetch` of local files from `file://`."]),
)


def main():
    run(
        "js-window",
        "JS Window",
        WIN,
        "The Window object is the browser’s global. The BOM (Browser Object Model) is how JavaScript talks to the browser itself: size, tabs, and the objects hanging off `window`.",
        ["`document` is `window.document`.",
         "`innerWidth` / `innerHeight` are the viewport.",
         "`open` / `close` / `moveTo` / `resizeTo` are legacy window controls and are often blocked."],
        WIN_QA,
        "Treat `window` as the global. Read viewport size with innerWidth/innerHeight. Do not depend on open/move/resize in ordinary tabs.",
        "js_window.asp",
        port=8771,
    )
    run(
        "js-screen",
        "JS Screen",
        SCR,
        "`window.screen` describes the visitor’s monitor: width, height, available area, and color depth — not the browser viewport.",
        ["`screen` can be written without `window.`.",
         "avail* subtracts OS chrome such as a taskbar.",
         "colorDepth / pixelDepth are usually 24 or 32 today."],
        SCR_QA,
        "Use screen.* for the monitor and innerWidth/innerHeight for the tab. availHeight is often smaller than height because of the taskbar.",
        "js_window_screen.asp",
        extra_refs=[("MDN Screen", "https://developer.mozilla.org/en-US/docs/Web/API/Screen")],
        port=8772,
    )
    run(
        "js-location",
        "JS Location",
        LOC,
        "`window.location` reads the current URL (href, hostname, pathname, protocol, port) and can load another document with `assign`.",
        ["Omit the `window.` prefix if you want: `location.href`.",
         "`assign` adds history; `replace` does not.",
         "Default ports often make `port` an empty string."],
        LOC_QA,
        "Read location.href for the full URL and the other properties for the pieces. assign() navigates; do not call it if you still need the current page.",
        "js_window_location.asp",
        extra_refs=[("MDN Location", "https://developer.mozilla.org/en-US/docs/Web/API/Location")],
        port=8773,
    )
    run(
        "js-history",
        "JS History",
        HIST,
        "The History API is Back/Forward (`back`, `forward`, `go`) plus SPA tools: `pushState`, `replaceState`, `state`, `popstate`, and `scrollRestoration`.",
        ["`pushState` / `replaceState` do not load a document.",
         "`popstate` fires on Back/Forward, not on pushState itself.",
         "`state` is null until you store an object."],
        HIST_QA,
        "Use back/forward/go for real navigation. Use pushState + popstate when the URL should change without a reload, and update the DOM yourself.",
        "js_window_history.asp",
        extra_refs=[("MDN History", "https://developer.mozilla.org/en-US/docs/Web/API/History")],
        port=8774,
    )
    run(
        "js-navigator",
        "JS Navigator",
        NAV,
        "`navigator` reports cookies, language, and online state. Most of the old “what browser is this?” properties (`appName`, `userAgent`, `javaEnabled`, …) are compatibility lies — the page warns you on each one.",
        ["Useful-ish: cookieEnabled, language, onLine.",
         "Do not sniff appName / appCodeName / product / appVersion / userAgent / platform.",
         "javaEnabled() is always false."],
        NAV_QA,
        "Trust cookieEnabled, language, and onLine (with caution). Ignore the legacy sniff properties and javaEnabled(). Detect features, not browsers.",
        "js_window_navigator.asp",
        extra_refs=[("MDN Navigator", "https://developer.mozilla.org/en-US/docs/Web/API/Navigator")],
        port=8775,
    )
    run(
        "js-popup-alert",
        "JS Popup Alert",
        POP,
        "The BOM popup trio is `alert`, `confirm`, and `prompt`. They are modal, blocking, and unstyled. Use `\\n` for line breaks. Native dialogs cannot appear in these snapshots, so the sandbox mirrors the text on the page.",
        ["alert — message.",
         "confirm — true/false.",
         "prompt — string or null.",
         "`\\n` for a new line."],
        POP_QA,
        "alert/confirm/prompt still work but block the page. Prefer in-page UI. Remember confirm’s boolean and prompt’s null-on-cancel.",
        "js_popup.asp",
        extra_refs=[("MDN Window.alert()", "https://developer.mozilla.org/en-US/docs/Web/API/Window/alert")],
        port=8776,
    )
    run(
        "js-cookies",
        "JS Cookies",
        CK,
        "Cookies are `document.cookie` name=value pairs. You create/change them by assignment, delete them with a past `expires`, and parse the read-back string with helpers (`setCookie`, `getCookie`, `checkCookie`).",
        ["Write `name=value; expires=…; path=/`.",
         "Read-back is only name=value pairs.",
         "Match path when deleting.",
         "The page’s 2013 sample expiry would delete a cookie today."],
        CK_QA,
        "Set cookies with document.cookie and path=/. Parse with getCookie. Delete with a 1970 expires. Prefer Web Storage for non-secret client data; never store secrets in JS-visible cookies.",
        "js_cookies.asp",
        extra_refs=[("MDN Document.cookie", "https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie")],
        port=8777,
    )
    run(
        "js-fetch-api",
        "JS Fetch API",
        FT,
        "Fetch is the modern way to load a URL. You get a Response, then read it with text/json/blob/bytes/arrayBuffer. Always check `ok` — Fetch does not throw on 404. Work is asynchronous, so later lines run first unless you await.",
        ["then / arrows / async await are the same two steps.",
         "ok, status, statusText, url describe the Response.",
         "HTTP errors need an explicit check.",
         "Fetch is Promise-based and stream-capable vs XHR."],
        FT_QA,
        "Call fetch, await the Response, check ok, then read the body with the matching method. Remember that JavaScript continues while the request is in flight.",
        "js_api_fetch.asp",
        extra_refs=[("MDN fetch()", "https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch")],
        port=8778,
    )


if __name__ == "__main__":
    main()
