"""S26: JS HTML First (4 W3Schools pages)."""
from __future__ import annotations

from _dom_ui import P
from _gen_lib import build_and_snap

BASE = "https://www.w3schools.com/js/"


def qa(*items):
    return list(items)


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
            ("MDN Progressive enhancement", "https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement"),
        ],
    )


# ---------------------------------------------------------------------------
# 26.1 HTML First
# ---------------------------------------------------------------------------

FIRST = [
    P("works-without-js", "A page that works without JavaScript",
      ["HTML-First means **HTML is the foundation**. The page should be readable and usable with basic HTML and CSS.",
       "This is the same idea as **progressive enhancement**: start with a working document, then add JS.",
       "The example is a heading + paragraph — no script required for the content to appear."],
      """<!doctype html>
<html>
<body>
  <h1>HTML First</h1>
  <p>Welcome This page works without JavaScript.</p>
</body>
</html>""",
      "The heading **HTML First** and the welcome paragraph render with **zero** script.",
      body="<h1>HTML First</h1><p>Welcome This page works without JavaScript.</p>",
      js="""      document.getElementById("demo").innerText = "scripts needed for this content: 0";"""),
    P("avoid-unnecessary-js", "Avoid unnecessary JavaScript",
      ["JS is powerful, but extra JS makes sites **slower** and harder to maintain.",
       "HTML-first can improve page speed, accessibility, SEO, maintainability, and reliability.",
       "Ask: can native HTML/CSS do this? If yes, skip the library."],
      """<p>Benefits: speed, accessibility, search, maintainability, reliability.</p>""",
      "The snapshot lists the five benefits from the W3Schools page.",
      body="<p>Many sites can be built with more HTML, CSS, and less JavaScript.</p>",
      js="""      document.getElementById("demo").innerText = [
        "Page speed",
        "Accessibility",
        "Search engine visibility",
        "Maintainability",
        "Reliability"
      ].join("\\n");"""),
    P("form-html-validation", "Progressive enhancement — form without JavaScript",
      ["An HTML form should **still submit** if JS fails.",
       "`type=\"email\"` + `required` give built-in checks with **no script**.",
       "The W3Schools Subscribe form uses native validation only."],
      """<form action="#" method="post">
  <label>Email: <input type="email" name="email" required></label>
  <button type="submit">Subscribe</button>
</form>""",
      "Empty email: `checkValidity()` is **false**. Filling a valid email would allow submit even with JS disabled.",
      body='<form id="f" action="#" method="post"><label>Email: <input id="em" type="email" name="email" required></label> <button type="submit">Subscribe</button></form>',
      js="""      const f = document.getElementById("f");
      f.addEventListener("submit", function (e) { e.preventDefault(); });
      document.getElementById("demo").innerText = "empty valid=" + f.checkValidity();"""),
    P("not-rejecting-js", "Why HTML-First is not “no JavaScript”",
      ["HTML-first is **not** rejecting JS. It is using **browser features first**.",
       "Many UI pieces used to need JS and now exist as HTML/CSS.",
       "Add JS when the browser cannot do the job natively."],
      """<p>HTML-first does not mean JavaScript never. It means HTML before JavaScript.</p>""",
      "The note prints the W3Schools line: HTML **before** JavaScript.",
      body="<p>Use the browser's built-in features before adding extra complexity.</p>",
      js="""      document.getElementById("demo").innerText = "HTML-first does not mean JavaScript never. It means HTML before JavaScript.";"""),
    P("details-native", "Browsers already understand details/summary",
      ["`<details>` / `<summary>` open and close **without JS**.",
       "Also native: `<dialog>`, `<form>` validation, `<search>` (where supported).",
       "This is “browsers are already powerful.”"],
      """<details>
  <summary>Click to read more</summary>
  This text can be opened and closed without JavaScript.
</details>""",
      "`details` is in the document; opening it is a **user/browser** behavior, not a script.",
      body="<details open><summary>Click to read more</summary>This text can be opened and closed without JavaScript.</details>",
      js="""      const d = document.querySelector("details");
      document.getElementById("demo").innerText = "open=" + d.open + " (native widget, no JS toggle)";"""),
    P("html-before-scripts-load", "HTML is visible before JavaScript loads",
      ["The browser can **paint HTML** as it arrives.",
       "Users may start reading before scripts finish. That matters on slow phones.",
       "Tutorials, articles, product pages, docs, and forms often need nothing more for first paint."],
      """<article>
  <h1>Article title</h1>
  <p>Readable immediately.</p>
</article>
<script src="app.js" defer></script>""",
      "The article text is in the DOM even if `app.js` is slow or missing.",
      body="<article><h1>Article title</h1><p>Readable immediately.</p></article>",
      js="""      document.getElementById("demo").innerText = document.querySelector("article").innerText.replace(/\\s+/g, " ").trim();"""),
    P("semantic-html", "Semantic HTML improves accessibility",
      ["Use elements for their **meaning**: `<header>`, `<main>`, `<article>`, `<nav>`, `<button>` — not empty `<div>` soup.",
       "Screen readers, search engines, and keyboard users get a real outline.",
       "W3Schools: “Use meaningful HTML first.”"],
      """<main>
  <article>
    <h1>Use meaningful HTML first.</h1>
  </article>
</main>""",
      "`querySelector(\"article h1\")` finds the heading because the markup is **semantic**, not a generic div.",
      body="<main><article><h1>Use meaningful HTML first.</h1></article></main>",
      js="""      document.getElementById("demo").innerText =
        "h1 in article=" + document.querySelector("article h1").textContent;"""),
    P("when-js-useful", "When JavaScript is still useful",
      ["JS is still the right tool for **logic**, live data, storage, and talking to servers.",
       "The rule is: add it **when it is needed**, not before.",
       "HTML-first = HTML **before** JS, not HTML **instead of** JS forever."],
      """<button type="button" id="b">Load extra (needs JS)</button>
<p id="out">Base content always here.</p>""",
      "Base content is visible without the click. JS only fills the extra line when the button is used.",
      body='<button type="button" id="b">Load extra (needs JS)</button><p id="out">Base content always here.</p>',
      js="""      document.getElementById("b").onclick = function () {
        document.getElementById("out").textContent += " Extra loaded.";
      };
      document.getElementById("b").click();
      document.getElementById("demo").innerText = document.getElementById("out").textContent;"""),
]

FIRST_QA = qa(
    ("What is HTML-First?", ["Build so the page works with **HTML (and CSS)** as the foundation; JS is extra."]),
    ("Is it the same as progressive enhancement?", ["**Closely related** — start with a working basic page, then enhance."]),
    ("Name two benefits of less JS.", ["Any two of: **speed**, **accessibility**, **SEO**, **maintainability**, **reliability**."]),
    ("Should a form work if JS fails?", ["**Yes** — native `action` + `required` / `type=email` still function."]),
    ("Does HTML-first mean never write JavaScript?", ["**No** — it means HTML **before** JavaScript."]),
    ("Which element toggles extra text with no script?", ["**`<details>`** + **`<summary>`**."]),
    ("Why can users read before scripts finish?", ["HTML is **parsed and painted** as it arrives; JS must download and run."]),
    ("What is semantic HTML?", ["Using tags for **meaning** (`article`, `nav`, `button`) instead of anonymous divs."]),
    ("When is JS still the right tool?", ["**Logic**, data, storage, server communication, widgets HTML cannot provide."]),
    ("What question should you ask first?", ["**Can the browser already do this?**"]),
)

# ---------------------------------------------------------------------------
# 26.2 HTML Progressive
# ---------------------------------------------------------------------------

PROG = [
    P("start-html", "Start with HTML — a working form",
      ["Step 1: meaningful HTML that works if CSS and JS **fail to load**.",
       "The newsletter form still posts with a normal submit.",
       "No script is required for the baseline."],
      """<form action="#" method="post">
  <h2>Newsletter Signup</h2>
  <label>Email: <input type="email" name="email" required></label>
  <button type="submit">Join</button>
</form>""",
      "The form is in the page and uses **required** + **email** with no JavaScript.",
      body='<form id="f" action="#" method="post"><h2>Newsletter Signup</h2><label>Email: <input type="email" name="email" required></label> <button type="submit">Join</button></form>',
      js="""      document.getElementById("demo").innerText = "method=" + document.getElementById("f").method + " required=" + document.querySelector("input").required;"""),
    P("add-css", "Add CSS for better design",
      ["Step 2: CSS improves **appearance** after the HTML already works.",
       "W3Schools styles the button green with padding and no border.",
       "If CSS fails, the form is still usable (unstyled)."],
      """button {
  background-color: #04AA6D;
  color: white;
  padding: 10px;
  border: none;
}""",
      "Computed button background is the W3Schools **green** `#04AA6D`.",
      body='<button type="button" id="b">Join</button>',
      css="button { background-color:#04AA6D; color:white; padding:10px; border:none; }",
      js="""      document.getElementById("demo").innerText = getComputedStyle(document.getElementById("b")).backgroundColor;""",
      fence="css"),
    P("add-js-enhance", "Add JavaScript as an enhancement",
      ["Step 3: JS can add instant feedback, but the form **must not depend** on it.",
       "W3Schools `submit` listener `alert(\"Form submitted!\")` — we print instead.",
       "If this script does not load, native submit still works."],
      """const form = document.querySelector("form");
form.addEventListener("submit", function () {
  alert("Form submitted!");
});""",
      "Submit is enhanced: the log shows **Form submitted!** and `preventDefault` keeps the sandbox from navigating.",
      body='<form id="f" action="#"><input name="email" value="a@b.c"><button type="submit">Join</button></form>',
      js="""      const form = document.querySelector("form");
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        document.getElementById("demo").innerText = "Form submitted!";
      });
      form.requestSubmit();""",
      fence="javascript"),
    P("why-matters", "Why progressive enhancement matters",
      ["Users have different devices, browsers, speeds. Some **disable JS**.",
       "Others use old browsers or assistive tech.",
       "Tip from the page: test with **JavaScript disabled**."],
      """<p>Everybody should still access the content.</p>""",
      "The snapshot records the testing tip: try the site with **JS off**.",
      body="<p>Different devices, browsers, and internet speeds.</p>",
      js="""      document.getElementById("demo").innerText = "Tip: try testing your website with JavaScript disabled.";"""),
    P("pe-starts-simple", "Progressive Enhancement — starts simple",
      ["Table row: PE **starts simple** and adds features later.",
       "Graceful degradation **starts advanced** and tries to keep old browsers working.",
       "This example is the PE column: a plain form first."],
      """<form action="#"><button>Works with no extras</button></form>""",
      "Baseline UI is a **plain HTML** form — PE starts simple.",
      body='<form action="#"><button type="submit">Works with no extras</button></form>',
      js="""      document.getElementById("demo").innerText = "Progressive Enhancement: starts simple";"""),
    P("gd-starts-advanced", "Graceful Degradation — starts advanced",
      ["GD builds the **full** experience first, then tries to peel features off for weaker browsers.",
       "That often leaves a worse baseline than PE.",
       "Named contrast from the W3Schools table."],
      """<div id="app">Imagine a JS-only SPA here</div>""",
      "A JS-only shell is the **starts advanced** story — if JS fails, there may be nothing.",
      body='<div id="app">Imagine a JS-only SPA here</div>',
      js="""      document.getElementById("demo").innerText = "Graceful Degradation: starts advanced";"""),
    P("pe-adds-later", "PE adds features later vs GD removes unsupported ones",
      ["PE: **add** features when the browser supports them (`@supports`, `required`, JS if present).",
       "GD: **remove** or replace features that old browsers cannot handle.",
       "Feature detection (`'open' in document.createElement('dialog')`) is a PE move."],
      """<script>
const hasDialog = "showModal" in document.createElement("dialog");
</script>""",
      "`showModal` in `HTMLDialogElement` is **true** in this browser — a feature we can add, not assume.",
      body="<p>Feature detect, then enhance.</p>",
      js="""      document.getElementById("demo").innerText =
        "dialog.showModal=" + ("showModal" in document.createElement("dialog"));"""),
    P("pe-a11y-vs-gd-compat", "PE focuses on accessibility; GD focuses on compatibility",
      ["PE’s mindset is **everyone can use the content** (keyboard, AT, no-JS).",
       "GD’s mindset is **make the fancy version limp along** on old engines.",
       "Both mention compatibility, but the starting point differs."],
      """<button type="button">Real button (accessible)</button>
<div role="button">Fake div button (harder)</div>""",
      "A real **`<button>`** is the PE-friendly control; a clickable div is the “rebuild accessibility later” trap.",
      body='<button type="button" id="b">Real button (accessible)</button> <div id="d" role="button">Fake div button (harder)</div>',
      js="""      document.getElementById("demo").innerText =
        "button focusable=" + (document.getElementById("b").tabIndex >= 0) +
        "\\ndiv role=" + document.getElementById("d").getAttribute("role");"""),
    P("modern-html-helps", "Modern HTML that used to need JavaScript",
      ["`required` validation, `<details>`, `loading=\"lazy\"`, CSS animations — all used to be JS jobs.",
       "That makes PE **easier** than a decade ago.",
       "Reach for these before writing a widget library."],
      """<details><summary>Native</summary>No JS accordion.</details>
<img alt="" loading="lazy" width="1" height="1" src="data:image/gif;base64,R0lGODlhAQABAAAAACw=">""",
      "`details` and `loading=\"lazy\"` are present as **native** features.",
      body='<details open><summary>Native</summary>No JS accordion.</details><img alt="" id="i" loading="lazy" width="1" height="1" src="data:image/gif;base64,R0lGODlhAQABAAAAACw=">',
      js="""      document.getElementById("demo").innerText =
        "details=" + document.querySelector("details").tagName +
        " lazy=" + document.getElementById("i").loading;"""),
]

PROG_QA = qa(
    ("What is the first PE step?", ["**Meaningful HTML** that still works if CSS/JS fail."]),
    ("What is the second step?", ["**CSS** for appearance."]),
    ("What is the third step?", ["**JavaScript** as an enhancement, not a requirement."]),
    ("Does the W3Schools submit alert replace the form?", ["No — if the script is missing the form **still works**."]),
    ("How does PE start vs GD?", ["PE **starts simple**. GD **starts advanced**."]),
    ("How do they treat features?", ["PE **adds** later. GD **removes** unsupported bits."]),
    ("Where does PE put its focus?", ["**Accessibility** (everyone can use the content)."]),
    ("Where does GD put its focus?", ["**Compatibility** with older/weaker clients."]),
    ("Name a modern HTML feature that replaced a JS widget.", ["**`required`**, **`<details>`**, **`loading=\"lazy\"`**, or **CSS animation**."]),
    ("What does W3Schools tell you to try?", ["Test the site with **JavaScript disabled**."]),
)

# ---------------------------------------------------------------------------
# 26.3 HTML First Features
# ---------------------------------------------------------------------------

FEAT = [
    P("details", "The details element",
      ["`<details>` is a disclosure widget. `<summary>` is the always-visible heading.",
       "No JavaScript. The `open` attribute (or `.open` property) controls state.",
       "W3Schools: “This works without any JavaScript.”"],
      """<details>
  <summary>More information</summary>
  This text is hidden until the user opens it.
</details>""",
      "With `open` set for the snapshot, the extra text is visible; `open` is **true**.",
      body="<details open><summary>More information</summary>This text is hidden until the user opens it.</details>",
      js="""      document.getElementById("demo").innerText = "open=" + document.querySelector("details").open;"""),
    P("form-validation-native", "HTML form validation attributes",
      ["`required`, `minlength`, `maxlength`, `pattern` run **in the browser** before submit.",
       "The Register form checks username + email automatically.",
       "JS is optional for extra messages; the constraint API still works without it."],
      """<form>
  <label>Username: <input name="user" required minlength="3"></label>
  <label>Email: <input name="email" type="email" required></label>
  <button>Register</button>
</form>""",
      "Empty fields: `checkValidity()` is **false**. The browser would block Register.",
      body='<form id="f"><label>Username: <input name="user" required minlength="3"></label> <label>Email: <input name="email" type="email" required></label> <button type="submit">Register</button></form>',
      js="""      const f = document.getElementById("f");
      f.addEventListener("submit", function (e) { e.preventDefault(); });
      document.getElementById("demo").innerText = "checkValidity=" + f.checkValidity();"""),
    P("type-email", "Input type — email",
      ["`type=\"email\"` adds format checking and a friendlier **mobile keyboard**.",
       "Invalid strings set `typeMismatch`.",
       "Listed on the page as a common native type."],
      """<input id="e" type="email" value="not-an-email">""",
      "**not-an-email** is invalid: `typeMismatch` is **true**.",
      body='<input id="e" type="email" value="not-an-email">',
      js="""      const e = document.getElementById("e");
      document.getElementById("demo").innerText = "valid=" + e.checkValidity() + " typeMismatch=" + e.validity.typeMismatch;"""),
    P("type-number", "Input type — number",
      ["`type=\"number\"` is for numeric values; combine with `min`/`max`/`step`.",
       "Some mobile browsers show a numeric keypad.",
       "Non-numeric input is rejected by the control."],
      """<input id="n" type="number" min="1" value="3">""",
      "Value **3** with `min=1` is **valid**.",
      body='<input id="n" type="number" min="1" value="3">',
      js="""      const n = document.getElementById("n");
      document.getElementById("demo").innerText = "value=" + n.value + " valid=" + n.checkValidity();"""),
    P("type-date", "Input type — date (Birthday example)",
      ["`type=\"date\"` shows a date picker in supporting browsers.",
       "W3Schools Birthday field is this control.",
       "The value is `yyyy-mm-dd` when set."],
      """<label>Birthday: <input id="b" type="date" value="2000-01-31"></label>""",
      "The date input holds **2000-01-31**.",
      body='<label>Birthday: <input id="b" type="date" value="2000-01-31"></label>',
      js="""      document.getElementById("demo").innerText = "value=" + document.getElementById("b").value + " type=" + document.getElementById("b").type;"""),
    P("type-url", "Input type — url",
      ["`type=\"url\"` expects a full URL (usually including a scheme).",
       "`example.com` without `https://` is often **invalid**.",
       "Mobile keyboards may offer `/` and `.com` shortcuts."],
      """<input id="u" type="url" value="https://example.com">""",
      "`https://example.com` is **valid** for `type=url`.",
      body='<input id="u" type="url" value="https://example.com">',
      js="""      const u = document.getElementById("u");
      document.getElementById("demo").innerText = "valid=" + u.checkValidity();"""),
    P("type-search", "Input type — search",
      ["`type=\"search\"` looks like text but may show a **clear ×** and a search keyboard.",
       "Semantics help password managers and AT less than `email`, but it is the dedicated search control.",
       "Listed among the page’s input types."],
      """<input id="s" type="search" value="html first">""",
      "`type` reports **search** and the value is kept.",
      body='<input id="s" type="search" value="html first">',
      js="""      const s = document.getElementById("s");
      document.getElementById("demo").innerText = "type=" + s.type + " value=" + s.value;"""),
    P("datalist", "The datalist element",
      ["`<datalist>` suggests values; the user may **pick or type something else**.",
       "Hook it up with `input list=\"id\"` matching `datalist id`.",
       "This is autocomplete **without** a JS widget."],
      """<label>Choose a browser:
  <input list="browsers" name="browser">
</label>
<datalist id="browsers">
  <option value="Edge">
  <option value="Firefox">
  <option value="Chrome">
  <option value="Opera">
  <option value="Safari">
</datalist>""",
      "The datalist has **5** options; the input’s `list` id is **browsers**.",
      body='<label>Choose a browser: <input id="i" list="browsers" name="browser"></label><datalist id="browsers"><option value="Edge"><option value="Firefox"><option value="Chrome"><option value="Opera"><option value="Safari"></datalist>',
      js="""      const dl = document.getElementById("browsers");
      document.getElementById("demo").innerText =
        "options=" + dl.options.length + " list=" + document.getElementById("i").getAttribute("list");"""),
    P("dialog", "The dialog element",
      ["`<dialog>` is a native modal/non-modal dialog.",
       "Opening usually needs a **small** script: `dialog.show()` / `showModal()`. Closing: `close()`.",
       "Behavior (focus trap, backdrop for modal) is **built into the browser** — not a JS overlay library."],
      """<dialog id="d" open>
  This is an open dialog window.
</dialog>""",
      "The dialog is **open** in the snapshot (`open` attribute / `.open` true).",
      body='<dialog id="d">This is an open dialog window.</dialog>',
      js="""      const d = document.getElementById("d");
      if (d.show) d.show();
      document.getElementById("demo").innerText = "open=" + d.open + " tag=" + d.tagName;"""),
    P("lazy", "Lazy loading images",
      ["`loading=\"lazy\"` defers off-screen images (and iframes) until near the viewport.",
       "Native performance win — used to need IntersectionObserver JS.",
       "W3Schools: use native HTML first; add JS only when native HTML cannot solve the problem."],
      """<img alt="later" loading="lazy" width="16" height="16"
  src="data:image/gif;base64,R0lGODlhAQABAAAAACw=">""",
      "`img.loading` is **lazy**.",
      body='<img id="i" alt="later" loading="lazy" width="16" height="16" src="data:image/gif;base64,R0lGODlhAQABAAAAACw=">',
      js="""      document.getElementById("demo").innerText = "loading=" + document.getElementById("i").loading;"""),
]

FEAT_QA = qa(
    ("What tag pair makes an accordion without JS?", ["**`<details>`** and **`<summary>`**."]),
    ("Which attributes validate a username of at least 3 characters?", ["**`required`** and **`minlength=\"3\"`**."]),
    ("Does the browser check `type=\"email\"` without JS?", ["**Yes** — constraint validation is native."]),
    ("What value format does `type=\"date\"` use?", ["**`yyyy-mm-dd`**."]),
    ("Can a user type a value that is not in a datalist?", ["**Yes** — suggestions are not a closed list."]),
    ("How do you attach a datalist?", ["`input list=\"the-id\"` matching **`<datalist id>`**."]),
    ("Does `<dialog>` need JS?", ["A **little** to open/close (`showModal`/`close`); the widget itself is native."]),
    ("What does `loading=\"lazy\"` do?", ["Defers loading until the image is **near the viewport**."]),
    ("Name two `type` values from the page list.", ["Any two of **email, number, date, url, search**."]),
    ("When do you add JavaScript according to this page?", ["Only when **native HTML cannot** solve the problem."]),
)

# ---------------------------------------------------------------------------
# 26.4 HTML First CSS
# ---------------------------------------------------------------------------

HOVER_CSS = """
button { background-color:#04AA6D; color:white; padding:10px; border:none; }
button:hover, button.forced { background-color:#059862; }
"""

TRANS_CSS = """
.box { width:100px; height:100px; background-color:#04AA6D; transition:width 0.5s; }
.box:hover, .box.forced { width:200px; }
"""

MENU_CSS = """
.menu-content { display:none; background:#eee; padding:8px; }
.menu:hover .menu-content, .menu.forced .menu-content { display:block; }
"""

GRID_CSS = """
.container { display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; }
.container div { background:#ddd; padding:12px; }
@media (max-width:600px) {
  .container { grid-template-columns:1fr; }
}
"""

SPIN_CSS = """
.spinner {
  width:40px; height:40px;
  border:6px solid #ddd;
  border-top:6px solid #04AA6D;
  border-radius:50%;
  animation:spin 1s linear infinite;
}
@keyframes spin { to { transform:rotate(360deg); } }
"""

CSSJS = [
    P("hover", "Hover effects with :hover",
      ["`:hover` changes an element when the pointer is over it — **no JS**.",
       "W3Schools button goes from `#04AA6D` to `#059862`.",
       "The snapshot adds class `forced` so the result image shows the hover colors (headless has no pointer)."],
      """button:hover { background-color:#059862; }
<button>Hover Over Me</button>""",
      "Forced hover style: background is the darker **#059862** green.",
      body="<button type='button' id='b'>Hover Over Me</button>",
      css=HOVER_CSS,
      js="""      document.getElementById("b").classList.add("forced");
      document.getElementById("demo").innerText = "background=" + getComputedStyle(document.getElementById("b")).backgroundColor;""",
      fence="css"),
    P("transition", "CSS transitions",
      ["`transition:width 0.5s` animates width changes smoothly.",
       "Hover (or a class) sets `width:200px`; the browser tweens from 100px.",
       "No `setInterval` — this is the CSS alternative to the DOM Animations chapter."],
      """ .box { width:100px; height:100px; background-color:#04AA6D; transition:width 0.5s; }
 .box:hover { width:200px; }""",
      "With `.forced`, computed width is **200px** (end of the hover transition).",
      body='<div class="box" id="box"></div>',
      css=TRANS_CSS,
      js="""      document.getElementById("box").classList.add("forced");
      document.getElementById("demo").innerText = "width=" + getComputedStyle(document.getElementById("box")).width;""",
      wait_ms=1500,
      fence="css"),
    P("show-hide", "Show and hide content with CSS (menu)",
      ["`.menu-content { display:none }` then `.menu:hover .menu-content { display:block }`.",
       "Simple menus/dropdowns without JS. Keyboard users may still need a focus-based variant (`:focus-within`).",
       "The snapshot forces the open state so **Link 1 / Link 2** are visible."],
      """ .menu-content { display:none; }
 .menu:hover .menu-content { display:block; }
<div class="menu">Menu
  <div class="menu-content">Link 1<br>Link 2</div>
</div>""",
      "Forced open menu: the content `display` is **block** and the links are in the tree.",
      body='<div class="menu" id="m">Menu<div class="menu-content">Link 1<br>Link 2</div></div>',
      css=MENU_CSS,
      js="""      document.getElementById("m").classList.add("forced");
      const c = document.querySelector(".menu-content");
      document.getElementById("demo").innerText = "display=" + getComputedStyle(c).display + "\\n" + c.innerText.replace(/\\s+/g, " ");""",
      fence="css"),
    P("responsive-grid", "Responsive layouts with media queries",
      ["CSS Grid `1fr 1fr 1fr` becomes **one column** at `max-width:600px`.",
       "No JS breakpoint listeners (`matchMedia` is optional, not required).",
       "The snapshot reports the computed `grid-template-columns` at this window size (900px wide chrome → three columns)."],
      """ .container { display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; }
 @media (max-width:600px) {
   .container { grid-template-columns:1fr; }
 }""",
      "At 900px screenshot width the grid stays **three columns**. Shrink below 600px and it becomes one (the media query).",
      body='<div class="container" id="c"><div>A</div><div>B</div><div>C</div></div>',
      css=GRID_CSS,
      js="""      document.getElementById("demo").innerText =
        "grid-template-columns=" + getComputedStyle(document.getElementById("c")).gridTemplateColumns;""",
      fence="css"),
    P("css-animation", "CSS animations — spinner",
      ["`@keyframes spin` + `animation: spin 1s linear infinite` rotates forever **without JS**.",
       "This is the CSS answer to a loading indicator.",
       "The snapshot waits so you can see the spinner mid-rotation."],
      """ .spinner {
   width:40px; height:40px;
   border:6px solid #ddd;
   border-top:6px solid #04AA6D;
   border-radius:50%;
   animation:spin 1s linear infinite;
 }
 @keyframes spin { to { transform:rotate(360deg); } }""",
      "Computed `animation-name` is **spin** and the box is a 40px circle.",
      body='<div class="spinner" id="s"></div>',
      css=SPIN_CSS,
      js="""      const s = document.getElementById("s");
      const cs = getComputedStyle(s);
      document.getElementById("demo").innerText =
        "animation=" + cs.animationName + " size=" + cs.width;""",
      wait_ms=1500,
      fence="css"),
    P("when-css-enough", "When CSS is enough vs when you need JavaScript",
      ["CSS is enough for **visual** change: color, size, spacing, layout, motion, simple show/hide.",
       "JavaScript is for **logic**, data, storage, and server communication.",
       "W3Schools: “If the problem is visual, try CSS first.”"],
      """<p>Visual → CSS. Logic/data/network → JS.</p>""",
      "The snapshot prints the split: **visual → CSS**, **logic → JS**.",
      body="<p>CSS is often the second step after HTML.</p>",
      js="""      document.getElementById("demo").innerText = [
        "CSS: colors, sizes, spacing, layout, motion, simple visibility",
        "JS: logic, data processing, storage, talking to a server"
      ].join("\\n");"""),
]

CSSJS_QA = qa(
    ("How do you restyle a button on hover without JS?", ["A **`:hover`** rule."]),
    ("What property animates the box width?", ["**`transition: width 0.5s`** (plus a hover width)."]),
    ("How does the CSS menu show links?", ["`.menu:hover .menu-content { display:block }` after hiding with **`display:none`**."]),
    ("How do you change columns for small screens?", ["A **`@media (max-width:600px)`** rule that sets **one** grid column."]),
    ("Does the spinner use `setInterval`?", ["**No** — **`@keyframes`** + the **`animation`** property."]),
    ("When is CSS the right tool?", ["When the change is **visual** (color, layout, motion, simple hide)."]),
    ("When is JS required?", ["**Logic**, data, **storage**, or **server** communication."]),
    ("What is the page’s closing advice?", ["If the problem is visual, **try CSS first**."]),
    ("Why force a `.forced` class in the sandbox?", ["Headless screenshots have **no pointer**, so `:hover` would not apply; the class duplicates the hover rule."]),
    ("Can CSS replace `myMove()` from DOM Animations?", ["For many motions **yes** — transitions/animations. JS timers are for logic-driven motion."]),
)


def main():
    run("html-first", "HTML First", FIRST,
        "HTML-First builds pages so HTML (and CSS) already work. JavaScript is added later, only when the browser cannot do the job natively.",
        ["Related to progressive enhancement.",
         "Less JS can mean faster, more accessible, more reliable pages.",
         "Semantic HTML and native widgets (`details`, forms) come first."],
        FIRST_QA,
        "Ship a usable HTML document first. Enhance with CSS, then JS. Do not start with a framework when a form or article only needs markup.",
        "js_htmlfirst.asp")
    run("html-progressive", "HTML Progressive", PROG,
        "Progressive enhancement starts with a working basic page, then adds CSS and JS. Graceful degradation starts fancy and tries to cope with older browsers.",
        ["HTML → CSS → JS as layers.",
         "PE starts simple and adds; GD starts advanced and strips.",
         "Modern HTML (`required`, `details`, lazy images, CSS animation) makes PE easier."],
        PROG_QA,
        "Build the usable core in HTML, dress it with CSS, and treat JS as an optional layer. Prefer PE’s “start simple” over a JS-only shell.",
        "js_htmlfirst_progressive.asp")
    run("html-first-features", "HTML First Features", FEAT,
        "Native HTML can replace small JavaScript widgets: disclosures, validation, specialized inputs, datalist, dialog, and lazy images.",
        ["Ask: can the browser already do this?",
         "`details`, constraint validation, input types, `datalist`, `dialog`, `loading=lazy`.",
         "Add JS only when native HTML is not enough."],
        FEAT_QA,
        "Reach for `details`, form attributes, input types, `datalist`, `dialog`, and `loading=\"lazy\"` before writing a custom widget.",
        "js_htmlfirst_features.asp")
    run("html-first-css", "HTML First CSS", CSSJS,
        "After HTML, CSS handles hover, transitions, simple menus, responsive layout, and animations so you often do not need JavaScript for visual behavior.",
        [":hover, transition, display toggling, grid + media queries, @keyframes.",
         "Visual problems → CSS first.",
         "Logic/data/network → JavaScript."],
        CSSJS_QA,
        "If the change is visual, write CSS. Save JavaScript for behavior that CSS cannot express.",
        "js_htmlfirst_css.asp")


if __name__ == "__main__":
    main()
