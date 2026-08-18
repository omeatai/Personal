"""S22: JS Projects — Counter, Event Listener, To-Do, Modal, Form Validation."""
from __future__ import annotations

import html as html_lib

from _gen_lib import S, build_and_snap, out_script


def ui_page(title: str, body: str, script: str, css: str = "") -> str:
    return f"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="color-scheme" content="light" />
    <title>{html_lib.escape(title)}</title>
    <link rel="stylesheet" href="../sandbox.css" />
    <style>
      button {{ margin-right: 4px; }}
      {css}
    </style>
  </head>
  <body>
    {body}
    <pre id="log"></pre>
    <script>
{script}
    </script>
  </body>
</html>
"""


def log_js(lines: str) -> str:
    return f"""      const __log = [];
      function note(s) {{
        __log.push(s);
        const el = document.getElementById("log");
        if (el) el.innerText = __log.join("\\n");
      }}
{lines}"""


COUNTER_HTML = """<h2>Counter</h2>
<p id="count" style="font-size:40px;">0</p>
<button type="button" onclick="increaseCount()">+</button>
<button type="button" onclick="decreaseCount()">-</button>
<button type="button" onclick="resetCount()">Reset</button>
<button type="button" onclick="saveCount()">Save</button>
<button type="button" onclick="loadCount()">Load</button>"""

COUNTER_JS = """let count = 0;
function updateCount() {
  document.getElementById("count").innerHTML = count;
}
function increaseCount() {
  count++;
  updateCount();
}
function decreaseCount() {
  count--;
  updateCount();
}
function resetCount() {
  count = 0;
  updateCount();
}
function saveCount() {
  localStorage.setItem("count", count);
}
function loadCount() {
  let saved = localStorage.getItem("count");
  if (saved !== null) {
    count = Number(saved);
  }
  updateCount();
}"""

EL_HTML = """<h2>Counter</h2>
<p id="count" style="font-size:40px;">0</p>
<button type="button" id="btnPlus">+</button>
<button type="button" id="btnMinus">-</button>
<button type="button" id="btnReset">Reset</button>
<button type="button" id="btnSave">Save</button>
<button type="button" id="btnLoad">Load</button>
<p id="message"></p>"""

TODO_HTML = """<h2>To-Do List</h2>
<input type="text" id="task" placeholder="New task">
<button type="button" onclick="addTask()">Add</button>
<ul id="list"></ul>
<button type="button" onclick="clearAll()">Clear All</button>"""

MODAL_CSS = """
.modal-overlay {
  display: none;
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
}
.modal-overlay.show { display: block; }
.modal-box {
  background: white;
  width: 90%;
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
  border-radius: 10px;
  position: relative;
}
.modal-close {
  position: absolute;
  right: 12px;
  top: 8px;
  font-size: 24px;
  border: none;
  background: none;
  cursor: pointer;
}
"""

MODAL_HTML = """<h2>Modal Popup</h2>
<button type="button" id="openBtn">Open Modal</button>
<div id="modal" class="modal-overlay">
  <div class="modal-box">
    <button type="button" id="closeBtn" class="modal-close">&times;</button>
    <h3>Hello!</h3>
    <p>This is a modal popup.</p>
  </div>
</div>"""

FORM_CSS = """
input { padding: 8px; width: 260px; margin-bottom: 4px; }
.error { color: red; margin: 0; }
.ok { color: green; margin: 0; }
.field { margin-bottom: 12px; }
"""

FORM_HTML = """<h2>Sign Up</h2>
<form id="signupForm">
  <div class="field">
    <label for="name">Name:</label><br>
    <input type="text" id="name">
    <p class="error" id="nameError"></p>
  </div>
  <div class="field">
    <label for="email">Email:</label><br>
    <input type="text" id="email">
    <p class="error" id="emailError"></p>
  </div>
  <div class="field">
    <label for="password">Password:</label><br>
    <input type="password" id="password">
    <p class="error" id="passwordError"></p>
  </div>
  <div class="field">
    <label for="confirm">Confirm Password:</label><br>
    <input type="password" id="confirm">
    <p class="error" id="confirmError"></p>
  </div>
  <button type="submit">Create Account</button>
  <p id="result"></p>
</form>"""

FORM_JS = """const form = document.getElementById("signupForm");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const passInput = document.getElementById("password");
const confirmInput = document.getElementById("confirm");
const nameError = document.getElementById("nameError");
const emailError = document.getElementById("emailError");
const passError = document.getElementById("passwordError");
const confirmError = document.getElementById("confirmError");
const result = document.getElementById("result");
function showError(el, message) {
  el.innerHTML = message;
}
function clearError(el) {
  el.innerHTML = "";
}
function validateName() {
  let value = nameInput.value.trim();
  if (value.length < 2) {
    showError(nameError, "Name must be at least 2 characters.");
    return false;
  }
  clearError(nameError);
  return true;
}
function validateEmail() {
  let value = emailInput.value.trim();
  if (!(/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(value))) {
    showError(emailError, "Enter a valid email address.");
    return false;
  }
  clearError(emailError);
  return true;
}
function validatePassword() {
  let value = passInput.value;
  if (value.length < 8) {
    showError(passError, "Password must be at least 8 characters.");
    return false;
  }
  clearError(passError);
  return true;
}
function validateConfirm() {
  let pass = passInput.value;
  let confirm = confirmInput.value;
  if (confirm === "") {
    showError(confirmError, "Please confirm your password.");
    return false;
  }
  if (confirm !== pass) {
    showError(confirmError, "Passwords do not match.");
    return false;
  }
  clearError(confirmError);
  return true;
}
function validateForm() {
  let okName = validateName();
  let okEmail = validateEmail();
  let okPass = validatePassword();
  let okConfirm = validateConfirm();
  return okName && okEmail && okPass && okConfirm;
}
form.addEventListener("submit", function (event) {
  event.preventDefault();
  result.innerHTML = "";
  if (validateForm()) {
    result.innerHTML = "Form is valid!";
    result.className = "ok";
  } else {
    result.innerHTML = "Please fix the errors.";
    result.className = "error";
  }
});"""


# ---------------------------------------------------------------------------
# 22.1 JS Counter
# ---------------------------------------------------------------------------

COUNTER = [
    S(
        "full-project",
        "Full Tryit: + − Reset Save Load",
        [
            "The Tryit is a **counter** with five **`onclick`** buttons: **+**, **−**, **Reset**, **Save**, **Load**.",
            "**`count`** is a number. **`updateCount()`** writes it to **`#count`**.",
            "**Save** uses **`localStorage.setItem(\"count\", count)`**. Values are stored as **text**.",
            "**Load** reads the key, skips if **`null`**, then **`Number(saved)`**.",
            "This snap auto-runs **++ ++ − Save Reset Load** so you see the cycle without clicking.",
        ],
        COUNTER_HTML + "\n\n" + COUNTER_JS,
        outcome="After ++ ++ the display is **2**. After − it is **1**. Save stores **\"1\"**. Reset shows **0**. Load restores **1**.",
        script="",
        full_html=ui_page(
            "Full Tryit: + − Reset Save Load",
            COUNTER_HTML,
            log_js(
                COUNTER_JS
                + """
      increaseCount();
      increaseCount();
      note("after ++ ++ -> " + count);
      decreaseCount();
      note("after -- -> " + count);
      saveCount();
      note("localStorage count -> " + JSON.stringify(localStorage.getItem("count")));
      resetCount();
      note("after reset -> " + count);
      loadCount();
      note("after load -> " + count);
"""
            ),
        ),
        fence="html",
    ),
    S(
        "html-buttons",
        "HTML: #count and five onclick buttons",
        [
            "Header **Counter**, paragraph **`id=\"count\"`** (start **0**, large font), five **`<button onclick>`**.",
            "Without the script, clicks do **nothing** — the functions are not defined yet.",
        ],
        '<h2>Counter</h2>\n<p id="count" style="font-size:40px;">0</p>\n<button onclick="increaseCount()">+</button>\n<button onclick="decreaseCount()">-</button>\n<button onclick="resetCount()">Reset</button>\n<button onclick="saveCount()">Save</button>\n<button onclick="loadCount()">Load</button>',
        outcome="The page shows **0** and five buttons. Clicks are not wired in this HTML-only demo.",
        script="",
        full_html=ui_page(
            "HTML: #count and five onclick buttons",
            COUNTER_HTML,
            "      document.getElementById('log').innerText = 'HTML only — onclick names exist, functions are not defined yet';",
        ),
        fence="html",
    ),
    S(
        "update-count",
        "let count = 0 and updateCount()",
        [
            "`let count = 0` is the **variable**.",
            "`updateCount()` sets **`#count` innerHTML** to the current number.",
        ],
        "let count = 0;\nfunction updateCount() {\n  document.getElementById(\"count\").innerHTML = count;\n}",
        outcome="Calling `updateCount()` with `count = 7` shows **7** in the paragraph.",
        script="",
        full_html=ui_page(
            "let count = 0 and updateCount()",
            '<p id="count" style="font-size:40px;">0</p>',
            log_js(
                """      let count = 0;
      function updateCount() {
        document.getElementById("count").innerHTML = count;
      }
      count = 7;
      updateCount();
      note("count -> " + count);
      note("#count text -> " + document.getElementById("count").innerHTML);
"""
            ),
        ),
    ),
    S(
        "increase-count",
        "increaseCount() — count++ then updateCount()",
        [
            "`count++` adds **1**. Then **`updateCount()`** refreshes the page.",
        ],
        "function increaseCount() {\n  count++;\n  updateCount();\n}",
        outcome="From **0**, two clicks (auto) show **2**.",
        script="",
        full_html=ui_page(
            "increaseCount() — count++ then updateCount()",
            COUNTER_HTML,
            log_js(
                COUNTER_JS
                + """
      increaseCount();
      increaseCount();
      note("count -> " + count);
"""
            ),
        ),
    ),
    S(
        "decrease-count",
        "decreaseCount() — count-- then updateCount()",
        [
            "`count--` subtracts **1**. The first Tryit **does not** stop at 0 (it can go negative).",
        ],
        "function decreaseCount() {\n  count--;\n  updateCount();\n}",
        outcome="From **0**, one − shows **−1**. Exercise 2 later blocks that.",
        script="",
        full_html=ui_page(
            "decreaseCount() — count-- then updateCount()",
            COUNTER_HTML,
            log_js(
                COUNTER_JS
                + """
      decreaseCount();
      note("count -> " + count);
"""
            ),
        ),
    ),
    S(
        "reset-count",
        "resetCount() — count = 0",
        [
            "Reset **assigns 0** (it does not load from storage).",
        ],
        "function resetCount() {\n  count = 0;\n  updateCount();\n}",
        outcome="After ++ to **3**, Reset shows **0**.",
        script="",
        full_html=ui_page(
            "resetCount() — count = 0",
            COUNTER_HTML,
            log_js(
                COUNTER_JS
                + """
      increaseCount(); increaseCount(); increaseCount();
      note("before reset -> " + count);
      resetCount();
      note("after reset -> " + count);
"""
            ),
        ),
    ),
    S(
        "save-count",
        'saveCount() — localStorage.setItem("count", count)',
        [
            "**`localStorage.setItem(key, value)`** writes a **string**.",
            "The number **5** is stored as **`\"5\"`**.",
        ],
        'function saveCount() {\n  localStorage.setItem("count", count);\n}',
        outcome='After setting count to **5** and Save, `localStorage.getItem("count")` is **"5"** (string).',
        script="",
        full_html=ui_page(
            'saveCount() — localStorage.setItem("count", count)',
            COUNTER_HTML,
            log_js(
                COUNTER_JS
                + """
      count = 5;
      updateCount();
      saveCount();
      const raw = localStorage.getItem("count");
      note("stored -> " + JSON.stringify(raw));
      note("typeof stored -> " + typeof raw);
"""
            ),
        ),
    ),
    S(
        "load-count",
        "loadCount() — getItem + Number(saved)",
        [
            "`getItem` returns **`null`** if the key was never saved — **do not** `Number(null)` into count blindly; the `if` skips that.",
            "`Number(\"4\")` is **4**. `localStorage` cannot store a real number type.",
        ],
        'function loadCount() {\n  let saved = localStorage.getItem("count");\n  if (saved !== null) {\n    count = Number(saved);\n  }\n  updateCount();\n}',
        outcome="Save **4**, reset to **0**, Load → **4**. Missing key leaves the current count unchanged.",
        script="",
        full_html=ui_page(
            "loadCount() — getItem + Number(saved)",
            COUNTER_HTML,
            log_js(
                COUNTER_JS
                + """
      localStorage.removeItem("count");
      count = 2;
      updateCount();
      loadCount();
      note("load with no key (count stays) -> " + count);
      count = 4;
      saveCount();
      count = 0;
      updateCount();
      loadCount();
      note("load after save 4 -> " + count);
      note("Number(\\"4\\") -> " + Number("4"));
"""
            ),
        ),
    ),
    S(
        "ex-start-10",
        "Exercise 1: start at 10 instead of 0",
        [
            "Change the declaration: **`let count = 10`**.",
            "The solutions Tryit also resets **back to 10** (not 0).",
        ],
        "let count = 10;",
        outcome="Initial display is **10**. Reset in the solutions file also returns to **10**.",
        script="",
        full_html=ui_page(
            "Exercise 1: start at 10 instead of 0",
            COUNTER_HTML.replace(">0<", ">10<"),
            log_js(
                COUNTER_JS.replace("let count = 0;", "let count = 10;").replace(
                    "count = 0;", "count = 10;"
                )
                + """
      updateCount();
      note("start -> " + count);
      resetCount();
      note("reset -> " + count);
"""
            ),
        ),
    ),
    S(
        "ex-no-negative",
        "Exercise 2: do not go below 0",
        [
            "Wrap `count--` in **`if (count > 0)`**.",
            "At **0**, − does **nothing**.",
        ],
        "function decreaseCount() {\n  if (count > 0) {\n    count--;\n    updateCount();\n  }\n}",
        outcome="From **0**, − leaves **0**. From **2**, − twice lands on **0**, not **−1**.",
        script="",
        full_html=ui_page(
            "Exercise 2: do not go below 0",
            COUNTER_HTML,
            log_js(
                """      let count = 0;
      function updateCount() {
        document.getElementById("count").innerHTML = count;
      }
      function decreaseCount() {
        if (count > 0) {
          count--;
          updateCount();
        }
      }
      decreaseCount();
      note("from 0, minus -> " + count);
      count = 2;
      updateCount();
      decreaseCount();
      decreaseCount();
      decreaseCount();
      note("from 2, minus three times -> " + count);
"""
            ),
        ),
    ),
    S(
        "ex-autoload",
        "Exercise 3 + solutions: loadCount() when the page opens",
        [
            "Call **`loadCount()`** at the top (function declarations are **hoisted**).",
            "Save, reload — the saved number appears **without clicking Load**.",
            "This sandbox seeds storage with **10**, then runs `loadCount()` like a fresh page.",
        ],
        "let count = 10;\nloadCount();",
        outcome="With `localStorage.count = \"10\"`, the page opens at **10**. Auto-load ran.",
        script="",
        full_html=ui_page(
            "Exercise 3 + solutions: loadCount() when the page opens",
            COUNTER_HTML.replace(">0<", ">10<"),
            log_js(
                """      localStorage.setItem("count", "10");
      let count = 10;
      function updateCount() {
        document.getElementById("count").innerHTML = count;
      }
      function loadCount() {
        let saved = localStorage.getItem("count");
        if (saved !== null) {
          count = Number(saved);
        }
        updateCount();
      }
      loadCount();
      note("opened at -> " + count);
"""
            ),
        ),
    ),
]


# ---------------------------------------------------------------------------
# 22.2 JS Event Listener
# ---------------------------------------------------------------------------

EL_JS = """document.getElementById("btnPlus").addEventListener("click", increaseCount);
document.getElementById("btnMinus").addEventListener("click", decreaseCount);
document.getElementById("btnReset").addEventListener("click", resetCount);
document.getElementById("btnSave").addEventListener("click", saveCount);
document.getElementById("btnLoad").addEventListener("click", loadCount);
let count = 0;
loadCount();
function updateCount() {
  document.getElementById("count").innerHTML = count;
}
function increaseCount() {
  count++;
  updateCount();
}
function decreaseCount() {
  if (count > 0) {
    count--;
    updateCount();
  }
}
function resetCount() {
  count = 0;
  updateCount();
}
function saveCount() {
  localStorage.setItem("count", count);
}
function loadCount() {
  let saved = localStorage.getItem("count");
  if (saved !== null) {
    count = Number(saved);
  }
  updateCount();
}"""

COUNTER_JS_FILE = """document.addEventListener("DOMContentLoaded", function () {
  let count = 0;
  const countEl = document.getElementById("count");
  const msgEl = document.getElementById("message");
  const btnPlus = document.getElementById("btnPlus");
  const btnMinus = document.getElementById("btnMinus");
  const btnReset = document.getElementById("btnReset");
  const btnSave = document.getElementById("btnSave");
  const btnLoad = document.getElementById("btnLoad");
  btnPlus.addEventListener("click", increaseCount);
  btnMinus.addEventListener("click", decreaseCount);
  btnReset.addEventListener("click", resetCount);
  btnSave.addEventListener("click", saveCount);
  btnLoad.addEventListener("click", loadCount);
  function updateCount() {
    countEl.innerHTML = count;
  }
  function showMessage(text) {
    msgEl.innerHTML = text;
    setTimeout(function () {
      msgEl.innerHTML = "";
    }, 3000);
  }
  function increaseCount() {
    count++;
    updateCount();
  }
  function decreaseCount() {
    count--;
    updateCount();
  }
  function resetCount() {
    count = 0;
    updateCount();
  }
  function saveCount() {
    localStorage.setItem("count", count);
    showMessage("Saved!");
  }
  function loadCount() {
    let saved = localStorage.getItem("count");
    if (saved !== null) {
      count = Number(saved);
      showMessage("Loaded!");
    }
    updateCount();
  }
});
"""

EVENT = [
    S(
        "full-tryit",
        "Same counter, wired with addEventListener",
        [
            "HTML buttons have **ids**, **no `onclick` attributes**.",
            "`addEventListener(\"click\", increaseCount)` keeps **HTML and JS separate**.",
            "This Tryit also **`loadCount()`** on open and **blocks decrease below 0**.",
        ],
        EL_HTML.replace('<p id="message"></p>', "") + "\n\n" + EL_JS,
        outcome="Auto ++ ++ makes **2**. Minus to **1**. Listeners fired without `onclick=` in HTML.",
        script="",
        full_html=ui_page(
            "Same counter, wired with addEventListener",
            EL_HTML,
            log_js(
                EL_JS
                + """
      increaseCount();
      increaseCount();
      note("after ++ ++ -> " + count);
      decreaseCount();
      note("after -- -> " + count);
"""
            ),
        ),
        fence="html",
    ),
    S(
        "html-no-onclick",
        "HTML without onclick — ids only",
        [
            "`id=\"btnPlus\"` etc. JavaScript **finds** the nodes and attaches listeners.",
            "Put the **`<script>` at the bottom** (or use **DOMContentLoaded**) so the elements exist.",
        ],
        '<button type="button" id="btnPlus">+</button>',
        outcome="Five id’d buttons, no inline handlers. Clicks do nothing until listeners are added.",
        script="",
        full_html=ui_page(
            "HTML without onclick — ids only",
            EL_HTML,
            "      document.getElementById('log').innerText = 'ids present, no listeners yet';",
        ),
        fence="html",
    ),
    S(
        "add-listeners",
        "addEventListener('click', handler) on each button",
        [
            "Easier to add **multiple** events to one element, and to keep markup clean.",
        ],
        'document.getElementById("btnPlus").addEventListener("click", increaseCount);\ndocument.getElementById("btnMinus").addEventListener("click", decreaseCount);',
        outcome="`getElementById(\"btnPlus\")` is an element. After `addEventListener`, a click runs **increaseCount**.",
        script="",
        full_html=ui_page(
            "addEventListener('click', handler) on each button",
            EL_HTML,
            log_js(
                EL_JS
                + """
      note("btnPlus node -> " + document.getElementById("btnPlus").tagName);
      note("listeners attached: click -> increaseCount / decreaseCount / ...");
"""
            ),
        ),
    ),
    S(
        "two-listeners",
        "Two click listeners on the same button (why addEventListener)",
        [
            "`onclick = fn` **replaces**. **`addEventListener`** can stack **several** handlers.",
            "This extra demo logs **A** then **B** on one click.",
        ],
        'btn.addEventListener("click", handlerA);\nbtn.addEventListener("click", handlerB);',
        outcome="One auto-click runs **both** handlers: **A** and **B**.",
        script="",
        full_html=ui_page(
            "Two click listeners on the same button",
            '<button type="button" id="one">Click</button>',
            log_js(
                """      const btn = document.getElementById("one");
      btn.addEventListener("click", function () { note("handler A"); });
      btn.addEventListener("click", function () { note("handler B"); });
      btn.click();
"""
            ),
        ),
    ),
    S(
        "improvements-messages",
        "Improvements: Saved! / Loaded! via showMessage",
        [
            "Cache elements in **`const`**. **`showMessage(text)`** writes `#message` then clears after **3 seconds**.",
            "Save shows **Saved!**. Load shows **Loaded!** only if a value existed.",
            "The improved `decreaseCount` on this page is **unbounded** (`count--` with no `if`).",
        ],
        'function showMessage(text) {\n  msgEl.innerHTML = text;\n  setTimeout(function () {\n    msgEl.innerHTML = "";\n  }, 3000);\n}',
        outcome="After Save, `#message` reads **Saved!**. After Load, **Loaded!**.",
        script="",
        wait_ms=1500,
        full_html=ui_page(
            "Improvements: Saved! / Loaded! via showMessage",
            EL_HTML,
            log_js(
                """      let count = 0;
      const countEl = document.getElementById("count");
      const msgEl = document.getElementById("message");
      function updateCount() { countEl.innerHTML = count; }
      function showMessage(text) {
        msgEl.innerHTML = text;
        setTimeout(function () { msgEl.innerHTML = ""; }, 3000);
      }
      function saveCount() {
        localStorage.setItem("count", count);
        showMessage("Saved!");
      }
      function loadCount() {
        let saved = localStorage.getItem("count");
        if (saved !== null) {
          count = Number(saved);
          showMessage("Loaded!");
        }
        updateCount();
      }
      count = 3;
      updateCount();
      saveCount();
      note("message after save -> " + msgEl.innerHTML);
      count = 0;
      updateCount();
      loadCount();
      note("message after load -> " + msgEl.innerHTML);
      note("count -> " + count);
"""
            ),
        ),
    ),
    S(
        "external-file",
        "JavaScript in counter.js + script at the bottom",
        [
            "External files are **more organized**, separated from HTML, and closer to real projects.",
            "The page puts **`<script src=\"counter.js\">` before `</body>`**.",
        ],
        '<script src="counter.js"></script>',
        outcome="`counter.js` loaded. Buttons work (auto ++ shows **1**). Script tag has **no type**.",
        script="",
        extra_files={"counter.js": COUNTER_JS_FILE},
        full_html=ui_page(
            "JavaScript in counter.js + script at the bottom",
            EL_HTML + '\n<script src="counter.js"></script>',
            log_js(
                """      document.addEventListener("DOMContentLoaded", function () {
        setTimeout(function () {
          document.getElementById("btnPlus").click();
          note("after plus click -> " + document.getElementById("count").innerHTML);
        }, 50);
      });
"""
            ),
        ),
        fence="html",
        wait_ms=2000,
    ),
    S(
        "domcontentloaded",
        "DOMContentLoaded — run after HTML is ready",
        [
            "An external script in **`<head>`** can run **before** `#btnPlus` exists → **`getElementById` is null** → crash.",
            "`document.addEventListener(\"DOMContentLoaded\", function () { ... })` waits until the HTML is parsed.",
            "A script **at the bottom of body** is often ready without it; the page still wraps **counter.js** in DOMContentLoaded.",
        ],
        'document.addEventListener("DOMContentLoaded", function() {\n  // JavaScript code\n});',
        outcome="Inside DOMContentLoaded, `#btnPlus` is an element (not null). That is why the wrap exists.",
        script="",
        full_html=ui_page(
            "DOMContentLoaded — run after HTML is ready",
            EL_HTML,
            log_js(
                """      document.addEventListener("DOMContentLoaded", function () {
        const el = document.getElementById("btnPlus");
        note("btnPlus -> " + (el ? el.id : null));
      });
      const already = document.getElementById("btnPlus");
      note("script at end of body, element already there -> " + (already ? already.id : null));
"""
            ),
        ),
    ),
    S(
        "element-variables",
        "Cache getElementById in const variables",
        [
            "`const countEl = document.getElementById(\"count\")` — look up **once**, reuse.",
            "Matches the performance tip from JS Performance, and the improved counter.js.",
        ],
        'const countEl = document.getElementById("count");\nconst btnPlus = document.getElementById("btnPlus");',
        outcome="**countEl.id** is **count**. **btnPlus.id** is **btnPlus**.",
        script=out_script(
            'const countEl = document.getElementById("count");\nconst btnPlus = document.getElementById("btnPlus");',
            [("countEl.id", "countEl.id"), ("btnPlus.id", "btnPlus.id")],
        ),
        body=EL_HTML,
    ),
]


# ---------------------------------------------------------------------------
# 22.3 JS To-Do List
# ---------------------------------------------------------------------------

TODO_JS = """let tasks = [];
function displayTasks() {
  let html = "";
  for (let i = 0; i < tasks.length; i++) {
    html += "<li>" + tasks[i] + " <button type=\\"button\\" onclick=\\"removeTask(" + i + ")\\">x</button></li>";
  }
  document.getElementById("list").innerHTML = html;
}
function addTask() {
  let taskInput = document.getElementById("task");
  let text = taskInput.value;
  if (text === "") {
    return;
  }
  tasks.push(text);
  taskInput.value = "";
  saveTasks();
  displayTasks();
}
function removeTask(i) {
  tasks.splice(i, 1);
  saveTasks();
  displayTasks();
}
function clearAll() {
  tasks = [];
  saveTasks();
  displayTasks();
}
function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}
function loadTasks() {
  let saved = localStorage.getItem("tasks");
  if (saved !== null) {
    tasks = JSON.parse(saved);
  }
}
loadTasks();
displayTasks();"""

TODO = [
    S(
        "html-skeleton",
        "HTML: input #task, Add, ul #list, Clear All",
        [
            "Need **`id=\"task\"`**, **Add** → `addTask()`, **`<ul id=\"list\">`**, **Clear All** → `clearAll()`.",
            "Start with **`let tasks = []`**.",
        ],
        TODO_HTML + "\n<script>\nlet tasks = [];\n</script>",
        outcome="Empty list, input, two buttons. **tasks** is **[]**.",
        script="",
        full_html=ui_page(
            "HTML: input #task, Add, ul #list, Clear All",
            TODO_HTML,
            log_js("      let tasks = [];\n      note('tasks -> ' + JSON.stringify(tasks));"),
        ),
        fence="html",
    ),
    S(
        "display-tasks",
        "displayTasks() — loop and innerHTML the <ul>",
        [
            "Rebuild the list HTML whenever **tasks** changes.",
            "Each row is the text plus an **x** that calls **`removeTask(i)`**.",
        ],
        'function displayTasks() {\n  let html = "";\n  for (let i = 0; i < tasks.length; i++) {\n    html += "<li>" + tasks[i] + " x</li>";\n  }\n  document.getElementById("list").innerHTML = html;\n}',
        outcome="With tasks **Buy milk** and **Walk dog**, the ul shows **two** items.",
        script="",
        full_html=ui_page(
            "displayTasks() — loop and innerHTML the <ul>",
            TODO_HTML,
            log_js(
                TODO_JS
                + """
      tasks = ["Buy milk", "Walk dog"];
      displayTasks();
      note("li count -> " + document.querySelectorAll("#list li").length);
      note("html -> " + document.getElementById("list").innerText.replace(/\\n/g, " | "));
"""
            ),
        ),
    ),
    S(
        "add-task",
        "addTask() — push, clear input, save, display",
        [
            "Read **`#task`**. Empty string → **`return`** (no add).",
            "`tasks.push(text)`, clear the input, **`saveTasks()`**, **`displayTasks()`**.",
        ],
        'function addTask() {\n  let taskInput = document.getElementById("task");\n  let text = taskInput.value;\n  if (text === "") {\n    return;\n  }\n  tasks.push(text);\n  taskInput.value = "";\n  saveTasks();\n  displayTasks();\n}',
        outcome="Add **Read** then **Code**. List length **2**. Input cleared to **\"\"**. Empty add leaves the list unchanged.",
        script="",
        full_html=ui_page(
            "addTask() — push, clear input, save, display",
            TODO_HTML,
            log_js(
                TODO_JS
                + """
      localStorage.removeItem("tasks");
      tasks = [];
      document.getElementById("task").value = "Read";
      addTask();
      document.getElementById("task").value = "Code";
      addTask();
      document.getElementById("task").value = "";
      addTask();
      note("tasks -> " + JSON.stringify(tasks));
      note("input after add -> " + JSON.stringify(document.getElementById("task").value));
"""
            ),
        ),
    ),
    S(
        "remove-task",
        "removeTask(i) — splice(i, 1)",
        [
            "**`splice(i, 1)`** removes **1** item at index **i**.",
            "Then save + display so the **x** buttons get **new indexes**.",
        ],
        "function removeTask(i) {\n  tasks.splice(i, 1);\n  saveTasks();\n  displayTasks();\n}",
        outcome="Start **[A, B, C]**. `removeTask(1)` → **[A, C]**.",
        script="",
        full_html=ui_page(
            "removeTask(i) — splice(i, 1)",
            TODO_HTML,
            log_js(
                TODO_JS
                + """
      localStorage.removeItem("tasks");
      tasks = ["A", "B", "C"];
      displayTasks();
      removeTask(1);
      note("after removeTask(1) -> " + JSON.stringify(tasks));
"""
            ),
        ),
    ),
    S(
        "clear-all",
        "clearAll() — tasks = []",
        [
            "Replace the array with a **new empty** one, then save + display.",
        ],
        "function clearAll() {\n  tasks = [];\n  saveTasks();\n  displayTasks();\n}",
        outcome="After two tasks, Clear All → **[]** and **0** list items.",
        script="",
        full_html=ui_page(
            "clearAll() — tasks = []",
            TODO_HTML,
            log_js(
                TODO_JS
                + """
      localStorage.removeItem("tasks");
      tasks = ["A", "B"];
      displayTasks();
      clearAll();
      note("tasks -> " + JSON.stringify(tasks));
      note("li count -> " + document.querySelectorAll("#list li").length);
"""
            ),
        ),
    ),
    S(
        "save-tasks",
        'saveTasks() — JSON.stringify into localStorage',
        [
            "localStorage stores **strings**. Arrays need **`JSON.stringify`**.",
        ],
        'function saveTasks() {\n  localStorage.setItem("tasks", JSON.stringify(tasks));\n}',
        outcome='`["Read","Code"]` is stored as the text **\'["Read","Code"]\'**.',
        script="",
        full_html=ui_page(
            "saveTasks() — JSON.stringify into localStorage",
            TODO_HTML,
            log_js(
                TODO_JS
                + """
      localStorage.removeItem("tasks");
      tasks = ["Read", "Code"];
      saveTasks();
      note("raw -> " + localStorage.getItem("tasks"));
"""
            ),
        ),
    ),
    S(
        "load-tasks",
        "loadTasks() — JSON.parse back into the array",
        [
            "`JSON.parse` rebuilds the **array**. Skip if **`getItem` is null**.",
        ],
        'function loadTasks() {\n  let saved = localStorage.getItem("tasks");\n  if (saved !== null) {\n    tasks = JSON.parse(saved);\n  }\n}',
        outcome='Parse of **\'["Read"]\'** yields array **["Read"]**. Then **displayTasks()** (final project calls both on load).',
        script="",
        full_html=ui_page(
            "loadTasks() — JSON.parse back into the array",
            TODO_HTML,
            log_js(
                """      localStorage.setItem("tasks", JSON.stringify(["Read"]));
      let tasks = [];
      function loadTasks() {
        let saved = localStorage.getItem("tasks");
        if (saved !== null) {
          tasks = JSON.parse(saved);
        }
      }
      loadTasks();
      note("tasks -> " + JSON.stringify(tasks));
      note("Array.isArray -> " + Array.isArray(tasks));
"""
            ),
        ),
    ),
    S(
        "final-project",
        "Final project: load + display on page open",
        [
            "End of the file: **`loadTasks(); displayTasks();`** (the page omits a semicolon after `displayTasks()` — ASI still runs it).",
            "This snap seeds two tasks, reloads the list, then removes the first.",
        ],
        TODO_JS,
        outcome="List shows **Buy milk** and **Walk dog**. After `removeTask(0)` only **Walk dog** remains.",
        script="",
        full_html=ui_page(
            "Final project: load + display on page open",
            TODO_HTML,
            log_js(
                """      localStorage.setItem("tasks", JSON.stringify(["Buy milk", "Walk dog"]));
"""
                + TODO_JS
                + """
      note("loaded -> " + JSON.stringify(tasks));
      removeTask(0);
      note("after remove 0 -> " + JSON.stringify(tasks));
"""
            ),
        ),
        fence="html",
    ),
    S(
        "ex-alert-empty",
        'Exercise 1: alert if the task is empty',
        [
            "Replace the silent `return` with **`alert(...)`** so empty add is visible.",
        ],
        'if (text === "") {\n  alert("Please enter a task");\n  return;\n}',
        outcome="Empty add does **not** push. This sandbox records **Please enter a task** instead of a blocking `alert`.",
        script="",
        full_html=ui_page(
            "Exercise 1: alert if the task is empty",
            TODO_HTML,
            log_js(
                TODO_JS.replace(
                    'if (text === "") {\n    return;\n  }',
                    'if (text === "") {\n    note("Please enter a task");\n    return;\n  }',
                )
                + """
      localStorage.removeItem("tasks");
      tasks = [];
      document.getElementById("task").value = "";
      addTask();
      note("tasks still -> " + JSON.stringify(tasks));
"""
            ),
        ),
    ),
    S(
        "ex-enter-key",
        "Exercise 2: press Enter to add a task",
        [
            "Listen for **`keydown`** / **`keyup`** on `#task`. If **`event.key === \"Enter\"`**, call **`addTask()`**.",
        ],
        'taskInput.addEventListener("keydown", function (event) {\n  if (event.key === "Enter") {\n    addTask();\n  }\n});',
        outcome="Dispatching **Enter** with value **Ship it** adds that task. Length **1**.",
        script="",
        full_html=ui_page(
            "Exercise 2: press Enter to add a task",
            TODO_HTML,
            log_js(
                TODO_JS
                + """
      localStorage.removeItem("tasks");
      tasks = [];
      const taskInput = document.getElementById("task");
      taskInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
          addTask();
        }
      });
      taskInput.value = "Ship it";
      taskInput.dispatchEvent(new KeyboardEvent("keydown", { key: "Enter" }));
      note("after Enter -> " + JSON.stringify(tasks));
"""
            ),
        ),
    ),
    S(
        "ex-saved-message",
        'Exercise 3: show "Saved!" after saveTasks',
        [
            "The project already saves on every change. Add a **Saved!** message in **`saveTasks`**.",
        ],
        'function saveTasks() {\n  localStorage.setItem("tasks", JSON.stringify(tasks));\n  document.getElementById("msg").innerHTML = "Saved!";\n}',
        outcome="After add, the message is **Saved!** and storage holds the new array.",
        script="",
        full_html=ui_page(
            'Exercise 3: show "Saved!" after saveTasks',
            TODO_HTML + '<p id="msg"></p>',
            log_js(
                TODO_JS.replace(
                    'localStorage.setItem("tasks", JSON.stringify(tasks));',
                    'localStorage.setItem("tasks", JSON.stringify(tasks));\n  document.getElementById("msg").innerHTML = "Saved!";',
                )
                + """
      localStorage.removeItem("tasks");
      tasks = [];
      document.getElementById("task").value = "One";
      addTask();
      note("msg -> " + document.getElementById("msg").innerHTML);
      note("stored -> " + localStorage.getItem("tasks"));
"""
            ),
        ),
    ),
]


# ---------------------------------------------------------------------------
# 22.4 JS Modal Popup
# ---------------------------------------------------------------------------

MODAL_JS = """const modal = document.getElementById("modal");
const openBtn = document.getElementById("openBtn");
const closeBtn = document.getElementById("closeBtn");
function openModal() {
  modal.classList.add("show");
}
function closeModal() {
  modal.classList.remove("show");
}
openBtn.addEventListener("click", openModal);
closeBtn.addEventListener("click", closeModal);
modal.addEventListener("click", function (event) {
  if (event.target === modal) {
    closeModal();
  }
});
document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    closeModal();
  }
});"""

MODAL = [
    S(
        "html-structure",
        "HTML: Open button, overlay, box, close ×",
        [
            "Two layers: **`.modal-overlay`** (dim background) and **`.modal-box`** (the card).",
            "The page’s id typo **`openBth`** in the prose is **`openBtn`** in the working code — use **`openBtn`**.",
        ],
        MODAL_HTML,
        outcome="Open button is visible. Overlay exists in the DOM but is **hidden** (`display: none`) until `.show`.",
        script="",
        full_html=ui_page(
            "HTML: Open button, overlay, box, close ×",
            MODAL_HTML,
            log_js(
                """      const modal = document.getElementById("modal");
      note("overlay display -> " + getComputedStyle(modal).display);
      note("openBtn -> " + document.getElementById("openBtn").textContent.trim());
"""
            ),
            css=MODAL_CSS,
        ),
        fence="html",
    ),
    S(
        "css-hidden",
        "CSS: overlay display none by default",
        [
            "`.modal-overlay { display: none; }` **hides** the modal until JS adds **`.show`**.",
        ],
        ".modal-overlay {\n  display: none;\n}",
        outcome="Computed **display** is **none**. The Hello box is not shown.",
        script="",
        full_html=ui_page(
            "CSS: overlay display none by default",
            MODAL_HTML,
            log_js(
                """      note("display -> " + getComputedStyle(document.getElementById("modal")).display);
"""
            ),
            css=MODAL_CSS,
        ),
        fence="css",
    ),
    S(
        "css-show",
        "CSS: .modal-overlay.show { display: block }",
        [
            "JavaScript **adds/removes** the **`show`** class. No `style.display` juggling required.",
        ],
        ".modal-overlay.show {\n  display: block;\n}",
        outcome="After `classList.add(\"show\")`, display is **block** (modal visible).",
        script="",
        full_html=ui_page(
            "CSS: .modal-overlay.show { display: block }",
            MODAL_HTML,
            log_js(
                """      const modal = document.getElementById("modal");
      note("before -> " + getComputedStyle(modal).display);
      modal.classList.add("show");
      note("after .show -> " + getComputedStyle(modal).display);
"""
            ),
            css=MODAL_CSS,
        ),
        fence="css",
    ),
    S(
        "open-close",
        "openModal / closeModal — classList add/remove show",
        [
            "`openModal()` → **`classList.add(\"show\")`**. `closeModal()` → **`remove(\"show\")`**.",
        ],
        'function openModal() {\n  modal.classList.add("show");\n}\nfunction closeModal() {\n  modal.classList.remove("show");\n}',
        outcome="Open → has **show**. Close → does **not**.",
        script="",
        full_html=ui_page(
            "openModal / closeModal — classList add/remove show",
            MODAL_HTML,
            log_js(
                MODAL_JS
                + """
      openModal();
      note("open classList -> " + modal.className);
      closeModal();
      note("close classList -> " + modal.className);
"""
            ),
            css=MODAL_CSS,
        ),
    ),
    S(
        "full-js",
        "Full Tryit: three ways to close",
        [
            "Close with **×**, **click overlay**, or **Escape**.",
            "This snap **opens** the modal so the screenshot shows the popup on top of the page.",
        ],
        MODAL_JS,
        outcome="After `openModal()`, overlay has **show** and the **Hello!** box is visible in the snap.",
        script="",
        full_html=ui_page(
            "Full Tryit: three ways to close",
            MODAL_HTML,
            log_js(
                MODAL_JS
                + """
      openModal();
      note("open -> " + modal.classList.contains("show"));
"""
            ),
            css=MODAL_CSS,
        ),
    ),
    S(
        "click-overlay",
        "Click overlay (event.target === modal) closes",
        [
            "`event.target === modal` means the click hit the **overlay**, not the inner box.",
            "Clicks **inside `.modal-box`** do **not** close.",
        ],
        'modal.addEventListener("click", function (event) {\n  if (event.target === modal) {\n    closeModal();\n  }\n});',
        outcome="Click on overlay → closed. Click on the box → still open.",
        script="",
        full_html=ui_page(
            "Click overlay (event.target === modal) closes",
            MODAL_HTML,
            log_js(
                MODAL_JS
                + """
      openModal();
      modal.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      note("click overlay -> show? " + modal.classList.contains("show"));
      openModal();
      document.querySelector(".modal-box").dispatchEvent(new MouseEvent("click", { bubbles: true }));
      note("click box (bubbles) -> show? " + modal.classList.contains("show") + " (handler ignores inner target)");
"""
            ),
            css=MODAL_CSS,
        ),
    ),
    S(
        "escape-key",
        'Escape key closes the modal',
        [
            "`keydown` on **document**. If **`event.key === \"Escape\"`**, call **`closeModal()`**.",
            "The page notes Escape may fire even when hidden — optional extra check: only close if open.",
        ],
        'document.addEventListener("keydown", function (event) {\n  if (event.key === "Escape") {\n    closeModal();\n  }\n});',
        outcome="Open, then dispatch **Escape** → **show** is **false**.",
        script="",
        full_html=ui_page(
            "Escape key closes the modal",
            MODAL_HTML,
            log_js(
                MODAL_JS
                + """
      openModal();
      document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" }));
      note("after Escape -> show? " + modal.classList.contains("show"));
"""
            ),
            css=MODAL_CSS,
        ),
    ),
    S(
        "close-button",
        "Close button (×) calls closeModal",
        [
            "`closeBtn.addEventListener(\"click\", closeModal)` — the **×** in the corner.",
        ],
        'openBtn.addEventListener("click", openModal);\ncloseBtn.addEventListener("click", closeModal);',
        outcome="Open, click × → overlay no longer has **show**.",
        script="",
        full_html=ui_page(
            "Close button (×) calls closeModal",
            MODAL_HTML,
            log_js(
                MODAL_JS
                + """
      openBtn.click();
      note("after open click -> " + modal.classList.contains("show"));
      closeBtn.click();
      note("after × click -> " + modal.classList.contains("show"));
"""
            ),
            css=MODAL_CSS,
        ),
    ),
]


# ---------------------------------------------------------------------------
# 22.5 JS Form Validation
# ---------------------------------------------------------------------------

FORM = [
    S(
        "html-fields",
        "HTML form: Name, Email, Password, Confirm + error <p>s",
        [
            "Four fields, each with an **empty `<p class=\"error\">`** underneath for messages.",
            "**`id=\"signupForm\"`**. Submit button **Create Account**.",
        ],
        FORM_HTML,
        outcome="Four inputs and a submit button. Error paragraphs are **blank** until JS writes them.",
        script="",
        full_html=ui_page(
            "HTML form: Name, Email, Password, Confirm + error <p>s",
            FORM_HTML,
            log_js(
                """      note("fields -> " + ["name","email","password","confirm"].join(", "));
      note("nameError blank -> " + JSON.stringify(document.getElementById("nameError").innerHTML));
"""
            ),
            css=FORM_CSS,
        ),
        fence="html",
    ),
    S(
        "css-error-ok",
        "CSS: .error red, .ok green, .field spacing",
        [
            "**.error** is **red** (invalid). **.ok** is **green** (`Form is valid!`).",
        ],
        FORM_CSS.strip(),
        outcome="An `.error` paragraph is **red**. An `.ok` paragraph is **green**.",
        script="",
        full_html=ui_page(
            "CSS: .error red, .ok green, .field spacing",
            '<p class="error" id="e">Name must be at least 2 characters.</p>\n<p class="ok" id="o">Form is valid!</p>',
            log_js(
                """      note("error color -> " + getComputedStyle(document.getElementById("e")).color);
      note("ok color -> " + getComputedStyle(document.getElementById("o")).color);
"""
            ),
            css=FORM_CSS,
        ),
        fence="css",
    ),
    S(
        "field-objects",
        "Cache form, inputs, error nodes, result",
        [
            "One **`const`** per field and per error `<p>`.",
        ],
        'const form = document.getElementById("signupForm");\nconst nameInput = document.getElementById("name");',
        outcome="**form.tagName** is **FORM**. **nameInput.id** is **name**.",
        script="",
        full_html=ui_page(
            "Cache form, inputs, error nodes, result",
            FORM_HTML,
            log_js(
                FORM_JS
                + """
      note("form.tagName -> " + form.tagName);
      note("nameInput.id -> " + nameInput.id);
      note("result.id -> " + result.id);
"""
            ),
            css=FORM_CSS,
        ),
    ),
    S(
        "show-clear-error",
        "showError(el, message) and clearError(el)",
        [
            "`showError` writes **innerHTML**. `clearError` sets **\"\"**.",
            "The page later warns: prefer **text** for messages (don’t dump raw user input into innerHTML).",
        ],
        'function showError(el, message) {\n  el.innerHTML = message;\n}\nfunction clearError(el) {\n  el.innerHTML = "";\n}',
        outcome="showError writes **Name must be at least 2 characters.** clearError blanks it.",
        script="",
        full_html=ui_page(
            "showError(el, message) and clearError(el)",
            FORM_HTML,
            log_js(
                FORM_JS
                + """
      showError(nameError, "Name must be at least 2 characters.");
      note("shown -> " + nameError.innerHTML);
      clearError(nameError);
      note("cleared -> " + JSON.stringify(nameError.innerHTML));
"""
            ),
            css=FORM_CSS,
        ),
    ),
    S(
        "prevent-default",
        "submit + event.preventDefault() so the page does not reload",
        [
            "Without **`preventDefault`**, the browser **navigates** and you never see errors.",
            "Then run **`validateForm()`**. Valid → **Form is valid!** (green). Else → **Please fix the errors.**",
        ],
        'form.addEventListener("submit", function (event) {\n  event.preventDefault();\n  result.innerHTML = "";\n  if (validateForm()) {\n    result.innerHTML = "Form is valid!";\n    result.className = "ok";\n  } else {\n    result.innerHTML = "Please fix the errors.";\n    result.className = "error";\n  }\n});',
        outcome="Stub `validateForm()` that returns **false** → result **Please fix the errors.** and class **error**. Page did **not** reload.",
        script="",
        full_html=ui_page(
            "submit + event.preventDefault() so the page does not reload",
            FORM_HTML,
            log_js(
                """      const form = document.getElementById("signupForm");
      const result = document.getElementById("result");
      function validateForm() { return false; }
      form.addEventListener("submit", function (event) {
        event.preventDefault();
        result.innerHTML = "";
        if (validateForm()) {
          result.innerHTML = "Form is valid!";
          result.className = "ok";
        } else {
          result.innerHTML = "Please fix the errors.";
          result.className = "error";
        }
      });
      form.requestSubmit();
      note("result -> " + result.innerHTML);
      note("class -> " + result.className);
"""
            ),
            css=FORM_CSS,
        ),
    ),
    S(
        "validate-name",
        "validateName() — trim, at least 2 characters",
        [
            "**`trim()`** so spaces don’t count as a name.",
            "Length **< 2** → **Name must be at least 2 characters.**",
        ],
        'function validateName() {\n  let value = nameInput.value.trim();\n  if (value.length < 2) {\n    showError(nameError, "Name must be at least 2 characters.");\n    return false;\n  }\n  clearError(nameError);\n  return true;\n}',
        outcome='**"A"** fails. **"Ada"** passes.',
        script="",
        full_html=ui_page(
            "validateName() — trim, at least 2 characters",
            FORM_HTML,
            log_js(
                FORM_JS
                + """
      nameInput.value = "A";
      note("A -> " + validateName() + " | " + nameError.innerHTML);
      nameInput.value = "Ada";
      note("Ada -> " + validateName() + " | " + JSON.stringify(nameError.innerHTML));
      nameInput.value = "  ";
      note("spaces -> " + validateName() + " | " + nameError.innerHTML);
"""
            ),
            css=FORM_CSS,
        ),
    ),
    S(
        "validate-email",
        "validateEmail() — simple regex",
        [
            "Pattern **`/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/`** — not a full RFC parser, good enough here.",
            "Fail message: **Enter a valid email address.**",
        ],
        'function validateEmail() {\n  let value = emailInput.value.trim();\n  if (!(/[^\\s@]+@[^\\s@]+\\.[^\\s@]+/.test(value))) {\n    showError(emailError, "Enter a valid email address.");\n    return false;\n  }\n  clearError(emailError);\n  return true;\n}',
        outcome="**ada@example.com** true. **ada@** false with the error text.",
        script="",
        full_html=ui_page(
            "validateEmail() — simple regex",
            FORM_HTML,
            log_js(
                FORM_JS
                + """
      emailInput.value = "ada@example.com";
      note("ada@example.com -> " + validateEmail());
      emailInput.value = "ada@";
      note("ada@ -> " + validateEmail() + " | " + emailError.innerHTML);
"""
            ),
            css=FORM_CSS,
        ),
    ),
    S(
        "validate-password",
        "validatePassword() — at least 8 characters",
        [
            "Does **not** trim (spaces count). Length **< 8** → **Password must be at least 8 characters.**",
        ],
        'function validatePassword() {\n  let value = passInput.value;\n  if (value.length < 8) {\n    showError(passError, "Password must be at least 8 characters.");\n    return false;\n  }\n  clearError(passError);\n  return true;\n}',
        outcome="**secret** (6) fails. **secret12** (8) passes.",
        script="",
        full_html=ui_page(
            "validatePassword() — at least 8 characters",
            FORM_HTML,
            log_js(
                FORM_JS
                + """
      passInput.value = "secret";
      note("secret -> " + validatePassword() + " | " + passError.innerHTML);
      passInput.value = "secret12";
      note("secret12 -> " + validatePassword());
"""
            ),
            css=FORM_CSS,
        ),
    ),
    S(
        "validate-confirm",
        "validateConfirm() — required and must match",
        [
            "Empty confirm → **Please confirm your password.**",
            "Mismatch → **Passwords do not match.**",
        ],
        "function validateConfirm() {\n  let pass = passInput.value;\n  let confirm = confirmInput.value;\n  if (confirm === \"\") {\n    showError(confirmError, \"Please confirm your password.\");\n    return false;\n  }\n  if (confirm !== pass) {\n    showError(confirmError, \"Passwords do not match.\");\n    return false;\n  }\n  clearError(confirmError);\n  return true;\n}",
        outcome="Empty → confirm error. **secret12** vs **secret99** → do not match. Matching pair → true.",
        script="",
        full_html=ui_page(
            "validateConfirm() — required and must match",
            FORM_HTML,
            log_js(
                FORM_JS
                + """
      passInput.value = "secret12";
      confirmInput.value = "";
      note("empty -> " + validateConfirm() + " | " + confirmError.innerHTML);
      confirmInput.value = "secret99";
      note("mismatch -> " + validateConfirm() + " | " + confirmError.innerHTML);
      confirmInput.value = "secret12";
      note("match -> " + validateConfirm());
"""
            ),
            css=FORM_CSS,
        ),
    ),
    S(
        "finished-invalid",
        "Finished project: empty submit shows all errors",
        [
            "`validateForm()` runs **all four** checks (does not stop at the first failure).",
            "Result line: **Please fix the errors.**",
        ],
        FORM_JS,
        outcome="Empty submit: name/email/password/confirm errors all filled. Result **Please fix the errors.**",
        script="",
        full_html=ui_page(
            "Finished project: empty submit shows all errors",
            FORM_HTML,
            log_js(
                FORM_JS
                + """
      document.getElementById("signupForm").requestSubmit();
      note("result -> " + result.innerHTML);
      note("nameError -> " + nameError.innerHTML);
      note("emailError -> " + emailError.innerHTML);
      note("passError -> " + passError.innerHTML);
      note("confirmError -> " + confirmError.innerHTML);
"""
            ),
            css=FORM_CSS,
        ),
        fence="html",
    ),
    S(
        "finished-valid",
        "Finished project: valid submit → Form is valid!",
        [
            "Name **Ada**, email **ada@example.com**, password **secret12** twice.",
        ],
        FORM_JS,
        outcome="**Form is valid!** with class **ok**. Error paragraphs are empty.",
        script="",
        full_html=ui_page(
            "Finished project: valid submit → Form is valid!",
            FORM_HTML,
            log_js(
                FORM_JS
                + """
      nameInput.value = "Ada";
      emailInput.value = "ada@example.com";
      passInput.value = "secret12";
      confirmInput.value = "secret12";
      document.getElementById("signupForm").requestSubmit();
      note("result -> " + result.innerHTML);
      note("class -> " + result.className);
"""
            ),
            css=FORM_CSS,
        ),
    ),
    S(
        "ex-password-number",
        "Exercise 1: password must contain a digit",
        [
            "Add **`/\\d/`** (or `[0-9]`) to **validatePassword** after the length check.",
        ],
        'if (!/\\d/.test(value)) {\n  showError(passError, "Password must contain at least one number.");\n  return false;\n}',
        outcome="**password** (no digit) fails. **secret12** still passes.",
        script="",
        full_html=ui_page(
            "Exercise 1: password must contain a digit",
            FORM_HTML,
            log_js(
                FORM_JS.replace(
                    """  if (value.length < 8) {
    showError(passError, "Password must be at least 8 characters.");
    return false;
  }
  clearError(passError);
  return true;""",
                    """  if (value.length < 8) {
    showError(passError, "Password must be at least 8 characters.");
    return false;
  }
  if (!/\\d/.test(value)) {
    showError(passError, "Password must contain at least one number.");
    return false;
  }
  clearError(passError);
  return true;""",
                )
                + """
      passInput.value = "password";
      note("password -> " + validatePassword() + " | " + passError.innerHTML);
      passInput.value = "secret12";
      note("secret12 -> " + validatePassword());
"""
            ),
            css=FORM_CSS,
        ),
    ),
]


def run_all() -> None:
    sections = [
        (
            "js-counter",
            "JS Counter",
            COUNTER,
            "Build a localStorage counter with five onclick buttons: increase, decrease, reset, save, and load. count is a number in memory; updateCount writes it to #count. Save stores a string; Load converts with Number. The first Tryit can go negative. Exercises start at 10, block decrease below 0, and call loadCount when the page opens.",
            [
                "**onclick** attributes call **increaseCount / decreaseCount / resetCount / saveCount / loadCount**.",
                "**localStorage** stores **text**. Use **`Number(saved)`** on load. Skip if **`getItem` is null**.",
                "Exercises: start **10**, **no negatives**, **auto-load** (function declarations are hoisted).",
            ],
            [
                ("What does + twice do from 0?", ["**count** becomes **2**."]),
                ("Does the first Tryit’s − stop at 0?", ["**No.** From 0 it goes to **−1**."]),
                ("What type is `localStorage.getItem(\"count\")` after save 5?", ["A **string**: **\"5\"**."]),
                ("Why `Number(saved)`?", ["Storage is **text**. You need a **number** for `++` / `--`."]),
                ("What if the key was never saved?", ["**getItem** is **null**. Leave **count** as-is."]),
                ("Exercise 1 starting value?", ["**10** (and reset returns to **10** in the solutions file)."]),
                ("Exercise 2 at count 0, press −?", ["**Nothing.** `if (count > 0)` fails."]),
                ("How does auto-load work on open?", ["Call **`loadCount()`** at startup. Function declarations are **hoisted**."]),
            ],
            "Five onclick handlers around one count variable. Persist with localStorage strings plus Number on the way back. Guard decrease and auto-load if you want a friendlier app.",
            [
                ("JS Counter (W3Schools)", "https://www.w3schools.com/js/js_project_counter.asp"),
                ("MDN: Window.localStorage", "https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage"),
                ("MDN: Number()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number"),
            ],
        ),
        (
            "js-event-listener",
            "JS Event Listener",
            EVENT,
            "The same counter, but buttons have ids and JavaScript uses addEventListener('click', handler) instead of onclick attributes. That separates HTML from JS, allows multiple handlers on one node, and scales better. The improved version moves code into counter.js, wraps it in DOMContentLoaded, caches element variables, and shows Saved! / Loaded! for three seconds.",
            [
                "**No onclick in HTML.** **`addEventListener(\"click\", fn)`** per button.",
                "First Tryit **auto-loads** and **blocks decrease below 0**. The improved file’s `decreaseCount` is **unbounded** again.",
                "**DOMContentLoaded** (or a script at the **end of body**) so nodes exist.",
                "**showMessage** writes then clears after **3000 ms**.",
            ],
            [
                ("Where are the click handlers in the event-listener HTML?", ["**Not in HTML.** They are **`addEventListener`** calls."]),
                ("Can one button have two click listeners?", ["**Yes.** This page’s extra demo runs **A** then **B**."]),
                ("What does the first Tryit do on open?", ["**`loadCount()`** — restore if storage has a value."]),
                ("Improved decreaseCount vs first Tryit?", ["Improved **`count--`** with no floor. First Tryit uses **`if (count > 0)`**."]),
                ("What does Save show?", ["**Saved!** in `#message` for **3 seconds**."]),
                ("Why DOMContentLoaded?", ["So **`getElementById`** does not run against **missing** nodes."]),
                ("Where should `<script src=\"counter.js\">` go?", ["At the **bottom of `<body>`** (the page’s pattern), or in head **with** DOMContentLoaded."]),
                ("Why cache `const btnPlus = getElementById(...)`?", ["Look up **once**. Cleaner, and fewer DOM searches."]),
            ],
            "Prefer addEventListener and an external file. Wait for DOMContentLoaded (or place the script last). Optional Saved!/Loaded! feedback makes storage visible.",
            [
                ("JS Event Listener (W3Schools)", "https://www.w3schools.com/js/js_project_eventlistener.asp"),
                ("MDN: EventTarget.addEventListener()", "https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener"),
                ("MDN: DOMContentLoaded", "https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event"),
            ],
        ),
        (
            "js-todo-list",
            "JS To-Do List",
            TODO,
            "A to-do list stored as an array in localStorage. displayTasks rebuilds the ul. addTask pushes non-empty text. removeTask uses splice(i, 1). clearAll assigns []. JSON.stringify / JSON.parse round-trip the array. The final file loads and displays on open. Exercises: alert on empty, Enter to add, Saved! after save.",
            [
                "**`tasks` is an array.** Display with a **for** loop and **innerHTML**.",
                "**`splice(i, 1)`** deletes one row. Re-display so **x** indexes stay correct.",
                "Storage: **`JSON.stringify` / `JSON.parse`**. Skip parse when **getItem is null**.",
                "Empty add **returns**. Exercise 1 **alerts** instead.",
            ],
            [
                ("What does addTask do with \"\"?", ["**return** — no push. Exercise 1 **alerts**."]),
                ("`removeTask(1)` on [A,B,C]?", ["**[A, C]**. `splice(1, 1)`."]),
                ("What does clearAll store?", ["**[]** (stringified)."]),
                ("Why JSON.stringify?", ["localStorage only holds **strings**, not arrays."]),
                ("What runs on page load in the final file?", ["**`loadTasks()`** then **`displayTasks()`**."]),
                ("Enter key exercise?", ["**keydown** on `#task`; if **Enter**, **addTask()**."]),
                ("Saved! exercise?", ["Set a message inside **`saveTasks`** after setItem."]),
                ("Why rebuild innerHTML after splice?", ["The **x** buttons encode **indexes**. Old indexes would be wrong."]),
            ],
            "Keep tasks in an array, render the ul from scratch after each change, and persist with JSON in localStorage. Guard empty input; Enter and a Saved! note are small upgrades.",
            [
                ("JS To-Do List (W3Schools)", "https://www.w3schools.com/js/js_project_todo.asp"),
                ("MDN: Array.prototype.splice()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice"),
                ("MDN: JSON.stringify()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify"),
            ],
        ),
        (
            "js-modal-popup",
            "JS Modal Popup",
            MODAL,
            "A modal is a popup on top of the page: a full-screen overlay plus a box. Hidden with display:none; shown by adding class show. Close three ways: ×, click the overlay (event.target === modal), or Escape. Use openBtn (the prose typo openBth is wrong). Do not close when the click is inside the box.",
            [
                "**Overlay** + **box**. Default **display: none**. **`.show` → display: block**.",
                "**classList.add/remove(\"show\")** — not inline style.",
                "Overlay click: **`event.target === modal`**. **Escape** on document **keydown**.",
            ],
            [
                ("How is the modal hidden at first?", ["**.modal-overlay { display: none; }**."]),
                ("How does JS show it?", ["**`modal.classList.add(\"show\")`**."]),
                ("Three close methods?", ["**× button**, **click overlay**, **Escape**."]),
                ("Why `event.target === modal`?", ["The click hit the **overlay**, not the inner box."]),
                ("Does a click inside the box close it?", ["**No** — target is the box (or a child), not the overlay."]),
                ("What key closes it?", ["**Escape** (`event.key === \"Escape\"`)."]),
                ("Prose id `openBth`?", ["Typo. Working code uses **`openBtn`**."]),
                ("open then close classList?", ["**show** present, then **removed**."]),
            ],
            "Toggle a show class on the overlay. Close from the ×, overlay clicks (target === overlay), and Escape. Keep the box clicks from bubbling into a close.",
            [
                ("JS Modal Popup (W3Schools)", "https://www.w3schools.com/js/js_project_modal_popup.asp"),
                ("MDN: Element.classList", "https://developer.mozilla.org/en-US/docs/Web/API/Element/classList"),
                ("MDN: KeyboardEvent.key", "https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key"),
            ],
        ),
        (
            "js-form-validation",
            "JS Form Validation",
            FORM,
            "A signup form that never reloads: submit is preventDefault’d, then four validators run. Name ≥ 2 after trim, email matches a simple regex, password ≥ 8, confirm non-empty and equal. Errors go in red <p>s under each field. Success sets Form is valid! in green. Exercise 1 requires a digit in the password. Do not skip preventDefault, and trim where the page trims.",
            [
                "**`event.preventDefault()`** on submit or the page **reloads** and errors vanish.",
                "**validateForm** runs **every** field (name && email && password && confirm).",
                "Messages: **Name must be at least 2 characters.** / **Enter a valid email address.** / **Password must be at least 8 characters.** / **Please confirm your password.** / **Passwords do not match.**",
                "Prefer **text** for messages (the page warns against innerHTML with user input).",
            ],
            [
                ("What happens on empty submit?", ["All four errors fill. Result **Please fix the errors.**"]),
                ("Valid Ada / ada@example.com / secret12 / secret12?", ["**Form is valid!** class **ok**."]),
                ("Does `\"  \"` count as a name?", ["**No.** **trim** makes length **0**."]),
                ("Email `ada@`?", ["**false** — **Enter a valid email address.**"]),
                ("Password `secret`?", ["**false** — need **8** characters."]),
                ("Confirm empty vs mismatch?", ["**Please confirm your password.** vs **Passwords do not match.**"]),
                ("Without preventDefault?", ["The browser **submits/reloads**. You never see the JS result."]),
                ("Exercise 1 extra rule?", ["Password must contain a **digit**. **password** fails; **secret12** passes."]),
            ],
            "Stop the native submit, validate every field, write red errors under inputs, and only then show Form is valid!. Trim names/emails; require confirm to match. Add a digit rule if you want a slightly stronger password.",
            [
                ("JS Form Validation (W3Schools)", "https://www.w3schools.com/js/js_project_form_validation.asp"),
                ("MDN: Event.preventDefault()", "https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault"),
                ("MDN: Constraint validation", "https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation"),
            ],
        ),
    ]
    print("example counts:")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print(f"  {slug}: {len(recs)}  qa={len(qa)}")
        if not (8 <= len(qa) <= 15):
            raise SystemExit(f"{slug} Q&A {len(qa)}")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print("building", slug)
        build_and_snap(slug, title, recs, intro, concepts, qa, summary, refs)
        print("done", slug)


if __name__ == "__main__":
    run_all()
