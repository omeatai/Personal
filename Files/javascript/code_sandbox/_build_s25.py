"""S25: JS HTML Events (7 W3Schools pages)."""
from __future__ import annotations

from _dom_ui import P
from _gen_lib import build_and_snap

BASE = "https://www.w3schools.com/js/"


def qa(*items):
    return list(items)


def run(slug, title, records, intro, concepts, qa_items, summary, page, extra_refs=None):
    refs = [(title, BASE + page)]
    if extra_refs:
        refs.extend(extra_refs)
    else:
        refs.append(("MDN EventTarget.addEventListener", "https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener"))
    build_and_snap(slug, title, records, intro, concepts, qa_items, summary, refs)


# ---------------------------------------------------------------------------
# 25.1 Intro to Events
# ---------------------------------------------------------------------------

INTRO = [
    P("onclick-date", "onclick attribute — write the date into another element",
      ["HTML event attributes run JavaScript when something happens to that element.",
       "`onclick=\"document.getElementById('demo').innerHTML = Date()\"` assigns a handler in markup.",
       "Quotes: use single quotes inside a double-quoted attribute (or vice versa).",
       "The snapshot clicks the button so the date string appears."],
      """<button type="button" onclick="document.getElementById('out').innerHTML = Date()">
  The time is?
</button>
<p id="out"></p>""",
      "After click, the paragraph shows a **date/time string**.",
      body='<button type="button" id="btn">The time is?</button><p id="out"></p>',
      js="""      document.getElementById("btn").onclick = function () {
        document.getElementById("out").innerHTML = Date();
      };
      document.getElementById("btn").click();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("onclick-this", "onclick — change this.innerHTML",
      ["`this` inside an HTML event attribute is the **element** that received the event.",
       "`this.innerHTML = Date()` replaces the button’s own label with the time.",
       "In an `addEventListener` callback, `this` is also the element (unless you use an arrow function)."],
      """<button type="button" onclick="this.innerHTML = Date()">The time is?</button>""",
      "The button caption becomes the **Date()** string.",
      body='<button type="button" id="btn">The time is?</button>',
      js="""      document.getElementById("btn").onclick = function () { this.innerHTML = Date(); };
      document.getElementById("btn").click();
      document.getElementById("demo").innerText = document.getElementById("btn").innerHTML;"""),
    P("onclick-function", "Calling a JavaScript function from onclick",
      ["Longer code belongs in a **named function**, then `onclick=\"displayDate()\"`.",
       "That keeps markup short and lets you reuse the same function on several controls.",
       "Remember the `()` in the HTML attribute — that **calls** the function."],
      """<button type="button" onclick="displayDate()">The time is?</button>
<p id="out"></p>
<script>
function displayDate() {
  document.getElementById("out").innerHTML = Date();
}
</script>""",
      "`displayDate()` runs on click and fills the paragraph with **Date()**.",
      body='<button type="button" id="btn">The time is?</button><p id="out"></p>',
      js="""      function displayDate() { document.getElementById("out").innerHTML = Date(); }
      document.getElementById("btn").onclick = displayDate;
      document.getElementById("btn").click();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("onchange", "Common event — onchange",
      ["`onchange` fires when an input/select **commits** a new value (often on blur for text, immediately for select).",
       "Typical use: validate or copy the field after the user finishes editing.",
       "The snapshot sets a value and dispatches `change`."],
      """<input id="n" onchange="document.getElementById('out').textContent = this.value">
<p id="out"></p>""",
      "After `change`, the output paragraph shows **Ada**.",
      body='<input id="n"><p id="out"></p>',
      js="""      const n = document.getElementById("n");
      n.onchange = function () { document.getElementById("out").textContent = this.value; };
      n.value = "Ada";
      n.dispatchEvent(new Event("change", { bubbles: true }));
      document.getElementById("demo").innerText = document.getElementById("out").textContent;"""),
    P("onclick-named", "Common event — onclick",
      ["`onclick` / `click` — the user clicks an element (mousedown + mouseup on the same target).",
       "Most buttons and fake-buttons use this event.",
       "Prefer `addEventListener(\"click\", …)` over the HTML attribute for non-trivial apps."],
      """<button type="button" id="b">Click</button>""",
      "The click handler prints **clicked**.",
      body='<button type="button" id="b">Click</button>',
      js="""      document.getElementById("b").onclick = function () {
        document.getElementById("demo").innerText = "clicked";
      };
      document.getElementById("b").click();"""),
    P("onmouseover", "Common event — onmouseover",
      ["Fires when the pointer **enters** the element (and also when it enters a child — it bubbles).",
       "Used for hover highlights. `mouseenter` is the non-bubbling cousin.",
       "The snapshot dispatches `mouseover`."],
      """<div id="box">Mouse Over Me</div>""",
      "After `mouseover`, the box text is **hovered**.",
      body='<div id="box" style="padding:12px;background:#eee;">Mouse Over Me</div>',
      js="""      const box = document.getElementById("box");
      box.onmouseover = function () { box.textContent = "hovered"; };
      box.dispatchEvent(new MouseEvent("mouseover", { bubbles: true }));
      document.getElementById("demo").innerText = box.textContent;"""),
    P("onmouseout", "Common event — onmouseout",
      ["Fires when the pointer **leaves** the element (also bubbles from children).",
       "Pair with `mouseover` for hover in/out. `mouseleave` does not fire when moving to a child.",
       "The snapshot dispatches `mouseout`."],
      """<div id="box">Mouse Over Me</div>""",
      "After `mouseout`, the box text is **left**.",
      body='<div id="box" style="padding:12px;background:#eee;">inside</div>',
      js="""      const box = document.getElementById("box");
      box.onmouseout = function () { box.textContent = "left"; };
      box.dispatchEvent(new MouseEvent("mouseout", { bubbles: true }));
      document.getElementById("demo").innerText = box.textContent;"""),
    P("onkeydown", "Common event — onkeydown",
      ["Fires when a key is **pressed down** (repeats if held).",
       "`event.key` is the character/name (`\"a\"`, `\"Enter\"`). `event.code` is the physical key (`\"KeyA\"`).",
       "`keypress` is deprecated — use `keydown` / `keyup`."],
      """<input id="k">""",
      "Dispatching keydown for **Z** prints **You pressed: Z**.",
      body='<input id="k">',
      js="""      const k = document.getElementById("k");
      k.onkeydown = function (event) {
        document.getElementById("demo").innerText = "You pressed: " + event.key;
      };
      k.dispatchEvent(new KeyboardEvent("keydown", { key: "Z", code: "KeyZ", bubbles: true }));"""),
    P("onload", "Common event — onload",
      ["`window.onload` / `window` `load` fires when the **page and resources** (images, CSS) have loaded.",
       "`DOMContentLoaded` is earlier — HTML is ready, images maybe not.",
       "This script has already loaded, so we record that the `load` path ran (or we fire it)."],
      """<script>
window.onload = function () {
  document.getElementById("demo").innerText = "page loaded";
};
</script>""",
      "The handler reports **page loaded** (the event already happened, or we invoke the same function).",
      body="<p>Load event</p>",
      js="""      function loaded() { document.getElementById("demo").innerText = "page loaded"; }
      window.addEventListener("load", loaded);
      if (document.readyState === "complete") loaded();"""),
    P("handlers-uses", "What event handlers are for",
      ["Handlers verify input, run actions on click, and set up the page on load.",
       "You can: put JS in an HTML attribute; call a function from an attribute; assign `element.onclick = fn`; prevent default.",
       "The next pages cover mouse, keyboard, load, and `addEventListener` in depth."],
      """<script>
const uses = [
  "Things that should be done every time a page loads",
  "Action when a user clicks a button",
  "Content verified when a user inputs data"
];
</script>""",
      "The snapshot lists typical handler jobs: **load**, **click**, **input check**.",
      body="<p>Event handlers react to user and browser actions.</p>",
      js="""      document.getElementById("demo").innerText = [
        "Things that should be done every time a page loads",
        "Action when a user clicks a button",
        "Content verified when a user inputs data"
      ].join("\\n");"""),
    P("onclick-not-recommended", "Not recommended — onclick attribute",
      ["HTML `onclick` is easy, but it **mixes** behavior into markup.",
       "You can attach only **one** `onclick` property later without `addEventListener`.",
       "W3Schools still shows it, then marks `addEventListener` as **highly recommended**."],
      """<button type="button" onclick="displayDate()">Time is?</button>
<script>
function displayDate() {
  document.getElementById("out").innerHTML = Date();
}
</script>""",
      "The attribute still works — the date appears — but the next example is the preferred style.",
      body='<button type="button" id="btn">Time is?</button><p id="out"></p>',
      js="""      function displayDate() { document.getElementById("out").innerHTML = Date(); }
      document.getElementById("btn").onclick = displayDate;
      document.getElementById("btn").click();
      document.getElementById("demo").innerText = "attribute-style handler ran: " + document.getElementById("out").innerHTML;"""),
    P("addeventlistener-recommended", "Highly recommended — addEventListener",
      ["`addEventListener(\"click\", fn)` keeps HTML and JS **separate**.",
       "You can add **many** listeners. The event name has **no** `on` prefix (`\"click\"` not `\"onclick\"`).",
       "This is the style the rest of the Events group uses."],
      """<button type="button" id="myBtn">Click me</button>
<p id="out"></p>
<script>
const btn = document.getElementById("myBtn");
btn.addEventListener("click", function () {
  document.getElementById("out").innerHTML = Date();
});
</script>""",
      "The listener writes **Date()** into the paragraph after click.",
      body='<button type="button" id="myBtn">Click me</button><p id="out"></p>',
      js="""      const btn = document.getElementById("myBtn");
      btn.addEventListener("click", function () {
        document.getElementById("out").innerHTML = Date();
      });
      btn.click();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
]

INTRO_QA = qa(
    ("What is an HTML event?", ["Something that happens to an element: click, load, key, mouse move, input change."]),
    ("How do you put JS in an attribute with nested quotes?", ["Double-quoted attribute, **single quotes** inside (or the reverse)."]),
    ("What is `this` in `onclick=\"this.innerHTML = Date()\"`?", ["The **element** that was clicked."]),
    ("Why call a function from `onclick` instead of a long script?", ["Keeps markup short and the function **reusable**."]),
    ("When does `onchange` usually fire on a text field?", ["When the value is **committed** (often on blur), not on every key."]),
    ("What is the modern event name for a click listener?", ["**`\"click\"`** — no `on` prefix."]),
    ("`keydown` vs deprecated `keypress`?", ["Use **`keydown` / `keyup`**. `keypress` skips many control keys and is deprecated."]),
    ("`load` vs `DOMContentLoaded`?", ["`DOMContentLoaded` is HTML ready. **`load`** waits for images, CSS, frames too."]),
    ("Why is `addEventListener` recommended?", ["Separates JS from HTML and lets you add **multiple** handlers."]),
    ("Can you assign two functions to `element.onclick`?", ["The second assignment **replaces** the first. Use `addEventListener` to stack them."]),
)

# ---------------------------------------------------------------------------
# 25.2 Mouse Events
# ---------------------------------------------------------------------------

MOUSE = [
    P("over-out", "mouseover and mouseout on a box",
      ["`mouseover` — pointer enters the element (bubbles; also fires on children).",
       "`mouseout` — pointer leaves (same bubbling caveat).",
       "The snapshot fires both in order so the final text is the **out** message."],
      """<div id="box">Move mouse over this box</div>
<script>
const box = document.getElementById("box");
box.addEventListener("mouseover", function () { box.innerHTML = "Mouse is over me!"; });
box.addEventListener("mouseout", function () { box.innerHTML = "Mouse is out!"; });
</script>""",
      "After simulated over then out, the box reads **Mouse is out!**.",
      body='<div id="box" style="width:240px;height:80px;background:#cfc;padding:8px;">Move mouse over this box</div>',
      js="""      const box = document.getElementById("box");
      box.addEventListener("mouseover", function () { box.innerHTML = "Mouse is over me!"; });
      box.addEventListener("mouseout", function () { box.innerHTML = "Mouse is out!"; });
      box.dispatchEvent(new MouseEvent("mouseover", { bubbles: true }));
      box.dispatchEvent(new MouseEvent("mouseout", { bubbles: true }));
      document.getElementById("demo").innerText = box.innerHTML;"""),
    P("click", "click",
      ["Fires after **mousedown + mouseup** on the same element with the main button (usually left).",
       "Keyboard activation of a button also synthesizes click.",
       "This is the default event for buttons."],
      """<button type="button" id="b">Click</button>""",
      "`click` fires: **clicked**.",
      body='<button type="button" id="b">Click</button>',
      js="""      document.getElementById("b").addEventListener("click", function () {
        document.getElementById("demo").innerText = "clicked";
      });
      document.getElementById("b").click();"""),
    P("dblclick", "dblclick",
      ["Fires after **two rapid clicks** on the same element.",
       "A dblclick is preceded by two `click` events — don’t double-count work.",
       "The snapshot dispatches `dblclick` directly."],
      """<button type="button" id="b">Double-click</button>""",
      "`dblclick` fires: **double**.",
      body='<button type="button" id="b">Double-click</button>',
      js="""      document.getElementById("b").addEventListener("dblclick", function () {
        document.getElementById("demo").innerText = "double";
      });
      document.getElementById("b").dispatchEvent(new MouseEvent("dblclick", { bubbles: true }));"""),
    P("mousedown-mouseup", "mousedown / mouseup",
      ["`mousedown` — button pressed. `mouseup` — button released.",
       "Order for a full click: mousedown → mouseup → click.",
       "Useful for “press and hold” (swap an image while the button is down)."],
      """<button type="button" id="b">Hold</button>""",
      "The log shows **down** then **up**.",
      body='<button type="button" id="b">Hold</button>',
      js="""      const out = [];
      const b = document.getElementById("b");
      b.addEventListener("mousedown", function () { out.push("down"); });
      b.addEventListener("mouseup", function () { out.push("up"); });
      b.dispatchEvent(new MouseEvent("mousedown", { bubbles: true }));
      b.dispatchEvent(new MouseEvent("mouseup", { bubbles: true }));
      document.getElementById("demo").innerText = out.join(" -> ");"""),
    P("mousemove", "mousemove",
      ["Fires **continuously** as the pointer moves over the element.",
       "The event object has coordinates (`clientX` / `clientY`).",
       "Throttle or ignore extra moves if you do heavy work — this event is chatty."],
      """<div id="box">move</div>""",
      "A dispatched `mousemove` at (40, 50) is recorded.",
      body='<div id="box" style="height:60px;background:#eee;">move</div>',
      js="""      document.getElementById("box").addEventListener("mousemove", function (event) {
        document.getElementById("demo").innerText = "X: " + event.clientX + " Y: " + event.clientY;
      });
      document.getElementById("box").dispatchEvent(new MouseEvent("mousemove", { clientX: 40, clientY: 50, bubbles: true }));"""),
    P("mouseenter-leave", "mouseenter / mouseleave",
      ["Like over/out but they **do not bubble** and **do not fire** when moving between a parent and its child.",
       "Closer to CSS `:hover` on that one element.",
       "Prefer these for “is the pointer inside this widget?”"],
      """<div id="box"><span>child</span></div>""",
      "Dispatched `mouseenter` then `mouseleave` update the log.",
      body='<div id="box" style="padding:16px;background:#cdf;"><span>child</span></div>',
      js="""      const box = document.getElementById("box");
      const log = [];
      box.addEventListener("mouseenter", function () { log.push("enter"); });
      box.addEventListener("mouseleave", function () { log.push("leave"); });
      box.dispatchEvent(new MouseEvent("mouseenter"));
      box.dispatchEvent(new MouseEvent("mouseleave"));
      document.getElementById("demo").innerText = log.join(" -> ");"""),
    P("contextmenu", "contextmenu",
      ["Fires when the user tries to open the **context menu** (usually right-click).",
       "`preventDefault()` blocks the browser menu if you draw your own.",
       "The snapshot dispatches `contextmenu` and prevents the default."],
      """<div id="box">right-click</div>""",
      "The handler runs and reports **contextmenu blocked**.",
      body='<div id="box">right-click</div>',
      js="""      const box = document.getElementById("box");
      box.addEventListener("contextmenu", function (event) {
        event.preventDefault();
        document.getElementById("demo").innerText = "contextmenu blocked";
      });
      box.dispatchEvent(new MouseEvent("contextmenu", { bubbles: true, cancelable: true }));"""),
    P("wheel", "wheel",
      ["Fires when the **mouse wheel** (or trackpad scroll) rotates.",
       "`event.deltaY` is the vertical scroll amount.",
       "Used for custom zoom or scrolljacking — use sparingly for accessibility."],
      """<div id="box">wheel me</div>""",
      "`wheel` with `deltaY=100` is logged.",
      body='<div id="box">wheel me</div>',
      js="""      document.getElementById("box").addEventListener("wheel", function (event) {
        document.getElementById("demo").innerText = "deltaY=" + event.deltaY;
      });
      document.getElementById("box").dispatchEvent(new WheelEvent("wheel", { deltaY: 100, bubbles: true }));"""),
    P("drag", "drag events",
      ["Drag-and-drop uses a set: `dragstart`, `drag`, `dragover`, `drop`, `dragend`, …",
       "The source needs `draggable=\"true\"`. `dragover` must `preventDefault` to allow drop.",
       "This sandbox starts a drag on a draggable item and records **dragstart**."],
      """<div id="item" draggable="true">drag me</div>""",
      "`dragstart` fires on the draggable item.",
      body='<div id="item" draggable="true" style="padding:8px;background:#fd8;">drag me</div>',
      js="""      const item = document.getElementById("item");
      item.addEventListener("dragstart", function () {
        document.getElementById("demo").innerText = "dragstart";
      });
      item.dispatchEvent(new DragEvent("dragstart", { bubbles: true }));"""),
    P("clientxy", "Mouse position — event.clientX and event.clientY",
      ["`MouseEvent.clientX` / `clientY` are coordinates **relative to the viewport** (not the element).",
       "The W3Schools demo listens on `document` `mousemove` and writes `X: … Y: …`.",
       "For touch/pen as well, look at the **Pointer Events** API."],
      """<p id="out">Move the mouse in this window!</p>
<script>
document.addEventListener("mousemove", function (event) {
  document.getElementById("out").innerHTML = "X: " + event.clientX + " Y: " + event.clientY;
});
</script>""",
      "A synthetic mousemove at **(120, 80)** prints those coordinates.",
      body='<p id="out">Move the mouse in this window!</p>',
      js="""      document.addEventListener("mousemove", function (event) {
        document.getElementById("out").innerHTML = "X: " + event.clientX + " Y: " + event.clientY;
      });
      document.dispatchEvent(new MouseEvent("mousemove", { clientX: 120, clientY: 80, bubbles: true }));
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
]

MOUSE_QA = qa(
    ("Order of events in a normal click?", ["**mousedown** → **mouseup** → **click**."]),
    ("Why might `mouseover` fire when moving between a parent and child?", ["It **bubbles** and also fires when entering descendants. Use **`mouseenter`** for :hover-like behavior."]),
    ("What is `dblclick` preceded by?", ["Two **`click`** events."]),
    ("What are `clientX` / `clientY` relative to?", ["The **viewport**, not the element."]),
    ("How do you stop the browser context menu?", ["Listen for **`contextmenu`** and call **`preventDefault()`**."]),
    ("Which event reports wheel rotation?", ["**`wheel`** (`deltaY`)."]),
    ("What attribute makes an element draggable?", ["**`draggable=\"true\"`**."]),
    ("Modern replacement covering mouse + touch + pen?", ["The **Pointer Events** API."]),
    ("Is `mousemove` a good place for heavy work?", ["Usually no — it fires **very often**. Throttle or debounce."]),
    ("Does `mouseleave` fire when entering a child?", ["**No** — that is the point vs `mouseout`."]),
)

# ---------------------------------------------------------------------------
# 25.3 Keyboard Events
# ---------------------------------------------------------------------------

KEYB = [
    P("keydown-key", "keydown — event.key",
      ["`keydown` fires when a key is pressed (and repeats).",
       "`event.key` is the **character/name** and depends on layout and Shift (`z` vs `Z`).",
       "Listen on an input or on `document` depending on whether you need a focused field."],
      """<input id="k">
<p id="out"></p>
<script>
const k = document.getElementById("k");
k.addEventListener("keydown", function (event) {
  document.getElementById("out").innerHTML = "You pressed: " + event.key;
});
</script>""",
      "Pressing **Z** shows **You pressed: Z**.",
      body='<input id="k"><p id="out"></p>',
      js="""      const k = document.getElementById("k");
      k.addEventListener("keydown", function (event) {
        document.getElementById("out").innerHTML = "You pressed: " + event.key;
      });
      k.dispatchEvent(new KeyboardEvent("keydown", { key: "Z", code: "KeyZ", bubbles: true }));
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("key-property", "event.key — value of the key",
      ["Table row: `event.key` returns the key value; with Shift it can be **Z** instead of **z**.",
       "Language layouts can change `key` (`\"z\"` vs another letter on the same physical key).",
       "Use `key` when you care about **meaning** (Enter, Escape, the letter typed)."],
      """<script>
const event = new KeyboardEvent("keydown", { key: "z" });
</script>""",
      "A synthetic event with `key: \"z\"` reports **z**.",
      body="<p>event.key</p>",
      js="""      const event = new KeyboardEvent("keydown", { key: "z" });
      document.getElementById("demo").innerText = "event.key=" + event.key;"""),
    P("code-property", "event.code — physical key",
      ["`event.code` is the **physical key** (`\"KeyZ\"`) and stays the same across layouts.",
       "When pressing Z, `code` is always **KeyZ** even if `key` is another character.",
       "Use `code` for game-style WASD that should not move when the user has a different layout."],
      """<script>
const event = new KeyboardEvent("keydown", { key: "z", code: "KeyZ" });
</script>""",
      "`event.code` is **KeyZ**.",
      body="<p>event.code</p>",
      js="""      const event = new KeyboardEvent("keydown", { key: "z", code: "KeyZ" });
      document.getElementById("demo").innerText = "event.code=" + event.code;"""),
    P("modifiers", "Modifier keys — ctrlKey, shiftKey, altKey, metaKey",
      ["Boolean flags on the KeyboardEvent tell you if Ctrl / Shift / Alt / Meta (Cmd) were held.",
       "Shortcuts such as Ctrl+S check `event.ctrlKey && event.key === \"s\"` (and usually `preventDefault`).",
       "`metaKey` is the Command key on macOS."],
      """<script>
const event = new KeyboardEvent("keydown", { key: "s", ctrlKey: true });
</script>""",
      "A Ctrl+S event has **ctrlKey true** and **key s**.",
      body="<p>modifiers</p>",
      js="""      const event = new KeyboardEvent("keydown", { key: "s", code: "KeyS", ctrlKey: true });
      document.getElementById("demo").innerText =
        "ctrl=" + event.ctrlKey + " shift=" + event.shiftKey + " key=" + event.key;"""),
    P("enter-code", "Using event.code === \"Enter\"",
      ["W3Schools listens for `event.code === \"Enter\"` on an input.",
       "`Enter` is the code for the main Enter key (`NumpadEnter` is separate).",
       "The snapshot dispatches Enter and writes **Enter was pressed!**."],
      """<input id="in01">
<p id="out"></p>
<script>
const in01 = document.getElementById("in01");
in01.addEventListener("keydown", function (event) {
  if (event.code === "Enter") {
    document.getElementById("out").innerHTML = "Enter was pressed!";
  }
});
</script>""",
      "The output paragraph is **Enter was pressed!**.",
      body='<input id="in01"><p id="out"></p>',
      js="""      const in01 = document.getElementById("in01");
      in01.addEventListener("keydown", function (event) {
        if (event.code === "Enter") {
          document.getElementById("out").innerHTML = "Enter was pressed!";
        }
      });
      in01.dispatchEvent(new KeyboardEvent("keydown", { key: "Enter", code: "Enter", bubbles: true }));
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("keyup-and-keypress", "keyup and deprecated keypress",
      ["`keyup` fires when the key is **released** (no repeat).",
       "`keypress` fired only for **character** keys, not Alt/Backspace, and is **deprecated**.",
       "Use `keydown` or `keyup` in new code."],
      """<input id="k">""",
      "`keyup` for **a** is logged. `keypress` is marked deprecated.",
      body='<input id="k">',
      js="""      const k = document.getElementById("k");
      k.addEventListener("keyup", function (event) {
        document.getElementById("demo").innerText = "keyup " + event.key + " (do not use keypress)";
      });
      k.dispatchEvent(new KeyboardEvent("keyup", { key: "a", code: "KeyA", bubbles: true }));"""),
]

KEYB_QA = qa(
    ("Which keyboard events should you use?", ["**`keydown`** and **`keyup`**. Avoid **`keypress`**."]),
    ("`event.key` for Shift+Z?", ["Typically **`Z`** (the produced character), not `z`."]),
    ("`event.code` for that same press?", ["**`KeyZ`** — physical key, layout-independent."]),
    ("How do you detect Ctrl+S?", ["`event.ctrlKey && event.key.toLowerCase() === \"s\"` (and usually `preventDefault`)."]),
    ("What is `metaKey`?", ["The **Command** key on Apple keyboards (Windows key on some others)."]),
    ("How does the W3Schools Enter demo detect Enter?", ["`event.code === \"Enter\"`."]),
    ("Does `keydown` repeat?", ["Yes, if the key is **held**."]),
    ("Does `keyup` repeat?", ["No — it fires once on **release**."]),
    ("Why did `keypress` skip Backspace?", ["It only fired for **character** keys. That is one reason it was deprecated."]),
    ("Should shortcuts listen on `window` or an input?", ["On **`window`/`document`** for app-wide shortcuts; on the **input** for field-specific keys."]),
)

# ---------------------------------------------------------------------------
# 25.4 Load Events
# ---------------------------------------------------------------------------

LOAD = [
    P("domcontentloaded", "DOMContentLoaded",
      ["Fires when HTML is parsed and the **DOM tree** is ready.",
       "Images, stylesheets, and subframes may **still be loading**.",
       "Best time to query elements, bind listeners, and build UI that only needs the DOM.",
       "If the script runs after the event, `document.readyState` is already past `loading` — call the setup function directly."],
      """<p id="out"></p>
<script>
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("out").innerHTML = "HTML is loaded!";
});
</script>""",
      "The paragraph reads **HTML is loaded!** (handler ran on the event or immediately because the DOM is already ready).",
      body='<p id="out"></p>',
      js="""      function ready() { document.getElementById("out").innerHTML = "HTML is loaded!"; }
      document.addEventListener("DOMContentLoaded", ready);
      if (document.readyState !== "loading") ready();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("window-load", "window load",
      ["`window` `load` waits for the **whole page**: HTML, images, CSS, frames.",
       "Use it for image dimensions, “fully loaded” banners, or anything that needs complete resources.",
       "Slower than DOMContentLoaded — don’t put all UI setup here."],
      """<p id="out"></p>
<script>
window.addEventListener("load", function () {
  document.getElementById("out").innerHTML = "Page is fully loaded!";
});
</script>""",
      "When `readyState` is `complete` (or when `load` fires), the text is **Page is fully loaded!**.",
      body='<p id="out"></p>',
      js="""      function loaded() { document.getElementById("out").innerHTML = "Page is fully loaded!"; }
      window.addEventListener("load", loaded);
      if (document.readyState === "complete") loaded();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("img-load", "Image load",
      ["`<img>` fires **`load`** when that image has finished downloading.",
       "Also used on `<script>` (executed) and `<link rel=stylesheet>` (parsed).",
       "Media elements have additional events (`canplay`, `loadeddata`, …)."],
      """<img id="myImg" alt="pic" width="32" height="32"
  src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32'%3E%3Crect width='32' height='32' fill='%2304AA6D'/%3E%3C/svg%3E">
<p id="out"></p>
<script>
const img = document.getElementById("myImg");
img.addEventListener("load", function () {
  document.getElementById("out").innerHTML = "Image loaded!";
});
</script>""",
      "When the SVG data URL has loaded (or `complete` is already true), the text is **Image loaded!**.",
      body="""<img id="myImg" alt="pic" width="32" height="32" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32'%3E%3Crect width='32' height='32' fill='%2304AA6D'/%3E%3C/svg%3E"><p id="out"></p>""",
      js="""      const img = document.getElementById("myImg");
      function done() { document.getElementById("out").innerHTML = "Image loaded!"; }
      img.addEventListener("load", done);
      if (img.complete) done();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("script-load", "script load",
      ["A `<script src>` fires `load` after the file is **fetched and executed**.",
       "Inline scripts do not fetch, so this is about **external** files.",
       "This sandbox appends a tiny extra file and waits for its `load`."],
      """<script src="ping.js"></script>""",
      "After `ping.js` loads, the log includes **script loaded**.",
      body="<p>External script</p>",
      extra_files={"ping.js": "window.__PING__ = true;\n"},
      js="""      const s = document.createElement("script");
      s.src = "ping.js";
      s.addEventListener("load", function () {
        document.getElementById("demo").innerText = "script loaded ping=" + window.__PING__;
      });
      s.addEventListener("error", function () {
        document.getElementById("demo").innerText = "script error";
      });
      document.head.appendChild(s);""",
      wait_ms=5000),
    P("link-load", "stylesheet link load",
      ["`<link rel=\"stylesheet\">` fires `load` when the CSS is **loaded and parsed**.",
       "Use it if you must measure layout that depends on those rules.",
       "This sandbox injects a `<link>` to a local CSS file."],
      """<link rel="stylesheet" href="extra.css">""",
      "The stylesheet `load` handler prints **css loaded**.",
      body="<p id='styled'>styled</p>",
      extra_files={"extra.css": "p#styled { color: crimson; }\n"},
      js="""      const link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = "extra.css";
      link.addEventListener("load", function () {
        document.getElementById("demo").innerText = "css loaded color=" + getComputedStyle(document.getElementById("styled")).color;
      });
      document.head.appendChild(link);""",
      wait_ms=5000),
    P("media-load", "media-specific loading events",
      ["`<audio>` / `<video>` fire `loadedmetadata`, `canplay`, `canplaythrough`, plus `error`.",
       "Do not assume `load` is the only signal — media is streamed.",
       "This example uses a tiny audio data URL and reports `readyState` after setting `src`."],
      """<audio id="a"></audio>""",
      "The audio element exists; `readyState` is logged (0 until data arrives).",
      body="<audio id='a'></audio>",
      js="""      const a = document.getElementById("a");
      document.getElementById("demo").innerText = "tag=AUDIO readyState=" + a.readyState + " (HAVE_NOTHING=0)";"""),
]

LOAD_QA = qa(
    ("When is DOMContentLoaded the right event?", ["When you only need the **DOM** — bind listeners, fill text — not image sizes."]),
    ("What does window `load` wait for?", ["HTML **plus** images, stylesheets, frames, and other resources."]),
    ("What if your script is at the end of `<body>`?", ["The DOM is already there; you may not need DOMContentLoaded, but it is still safe if you check `readyState`."]),
    ("Which element fires `load` when a picture finishes?", ["**`<img>`**."]),
    ("When does an external `<script>` fire `load`?", ["After it is **downloaded and executed**."]),
    ("Why extra media events besides `load`?", ["Audio/video are **streamed**; `canplay` / `loadeddata` describe buffer state."]),
    ("What `readyState` means the document is fully loaded?", ["**`complete`**."]),
    ("Should you put all setup in `window.load`?", ["No — it is **later**. Prefer DOMContentLoaded for UI wiring."]),
    ("What if the image is already cached?", ["`img.complete` may already be true — call the handler **immediately** as well as on `load`."]),
    ("Can `load` run on `<link rel=stylesheet>`?", ["Yes — when the stylesheet has been **loaded and parsed**."]),
)

# ---------------------------------------------------------------------------
# 25.5 Manage Events
# ---------------------------------------------------------------------------

MANAGE = [
    P("add", "Adding events",
      ["`addEventListener(\"click\", myFunction)` registers a **named** function.",
       "Named functions can be removed later; anonymous functions cannot (unless you kept the reference).",
       "The snapshot clicks **Click** and prints **Clicked!**."],
      """<button type="button" id="btn">Click</button>
<p id="out"></p>
<script>
const btn = document.getElementById("btn");
btn.addEventListener("click", myFunction);
function myFunction() {
  document.getElementById("out").innerHTML = "Clicked!";
}
</script>""",
      "The output is **Clicked!**.",
      body='<button type="button" id="btn">Click</button><p id="out"></p>',
      js="""      const btn = document.getElementById("btn");
      function myFunction() { document.getElementById("out").innerHTML = "Clicked!"; }
      btn.addEventListener("click", myFunction);
      btn.click();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("remove", "Removing events",
      ["`removeEventListener` needs the **same function object** you added.",
       "W3Schools: Add attaches `myFunction` to Test; Remove detaches it.",
       "The snapshot Adds, clicks Test (**Hello!**), Removes, clicks again (no second Hello)."],
      """<button type="button" id="add">Add</button>
<button type="button" id="remove">Remove</button>
<button type="button" id="test">Test click</button>
<p id="out"></p>""",
      "After add → test → remove → test, the log is a **single** Hello! — the second click did nothing.",
      body='<button type="button" id="add">Add</button> <button type="button" id="remove">Remove</button> <button type="button" id="test">Test click</button><p id="out"></p>',
      js="""      const test = document.getElementById("test");
      const remove = document.getElementById("remove");
      const add = document.getElementById("add");
      function myFunction() { document.getElementById("out").innerHTML += "Hello!"; }
      add.addEventListener("click", function () { test.addEventListener("click", myFunction); });
      remove.addEventListener("click", function () { test.removeEventListener("click", myFunction); });
      add.click();
      test.click();
      remove.click();
      test.click();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("same-function-note", "You must pass the same named function to remove",
      ["`removeEventListener(\"click\", function(){…})` does **not** remove a previously added anonymous function — they are different objects.",
       "Store the function in a `const` / `function` declaration and pass that variable both times.",
       "This example shows a failed remove (anonymous) vs a successful remove (named)."],
      """<button type="button" id="b">Click</button>""",
      "Named remove works: only **one** tick is logged after the second click is detached.",
      body='<button type="button" id="b">Click</button>',
      js="""      const b = document.getElementById("b");
      let n = 0;
      function tick() { n++; }
      b.addEventListener("click", tick);
      b.click();
      b.removeEventListener("click", tick);
      b.click();
      document.getElementById("demo").innerText = "ticks=" + n + " (second click ignored)";"""),
    P("preventdefault", "Blocking events — preventDefault on a link",
      ["`event.preventDefault()` stops the **browser’s default** (navigate, submit, check a checkbox).",
       "The W3Schools link “Go to W3Schools” is blocked; the page prints **Link blocked!** instead of leaving.",
       "It does **not** stop other listeners unless you also `stopPropagation` / `stopImmediatePropagation`."],
      """<a id="link" href="https://www.w3schools.com">Go to W3Schools</a>
<p id="out"></p>
<script>
const link = document.getElementById("link");
link.addEventListener("click", function (event) {
  event.preventDefault();
  document.getElementById("out").innerHTML = "Link blocked!";
});
</script>""",
      "The click does not navigate. The paragraph reads **Link blocked!**.",
      body='<a id="link" href="https://www.w3schools.com">Go to W3Schools</a><p id="out"></p>',
      js="""      const link = document.getElementById("link");
      link.addEventListener("click", function (event) {
        event.preventDefault();
        document.getElementById("out").innerHTML = "Link blocked!";
      });
      link.click();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
]

MANAGE_QA = qa(
    ("How do you add a click listener?", ["`element.addEventListener(\"click\", handler)`."]),
    ("How do you remove it?", ["`element.removeEventListener(\"click\", handler)` with the **same function**."]),
    ("Why can’t you remove an inline anonymous listener?", ["You don’t have the **same function object** to pass to `removeEventListener`."]),
    ("In the Add/Remove demo, what does Remove do?", ["It stops **Test click** from running `myFunction`."]),
    ("What does `preventDefault` do on a link?", ["Stops **navigation** so you can handle the click in JS."]),
    ("Does `preventDefault` stop bubbling?", ["**No**. Use `stopPropagation` for that."]),
    ("Can you add the same named function twice?", ["Yes — it can run **twice** unless you guard or remove first."]),
    ("Should the Add button use an anonymous function?", ["Yes for the Add/Remove *wiring*; the **test** handler itself must stay **named** so it can be removed."]),
    ("What happens if you click Test before Add?", ["Nothing — the listener is not attached yet."]),
    ("Is `return false` in an HTML `onclick` the same as `preventDefault`?", ["In HTML `onclick`, `return false` prevents default **and** stops bubbling. In `addEventListener`, `return false` does **not** — call the methods."]),
)

# ---------------------------------------------------------------------------
# 25.6 Event Examples (js_htmldom_events.asp)
# ---------------------------------------------------------------------------

EX = [
    P("click-text", "Change text when the paragraph is clicked",
      ["`onclick` on a `<h1>` (or any element) can rewrite its own `innerHTML`.",
       "The W3Schools first Tryit turns “Click on this text!” into a new message.",
       "This is reacting to events with an **HTML attribute**."],
      """<h1 onclick="this.innerHTML = 'Ooops!'">Click on this text!</h1>""",
      "After click, the heading is **Ooops!**.",
      body='<h1 id="h">Click on this text!</h1>',
      js="""      document.getElementById("h").onclick = function () { this.innerHTML = "Ooops!"; };
      document.getElementById("h").click();
      document.getElementById("demo").innerText = document.getElementById("h").innerHTML;"""),
    P("click-function-id", "Call a function and pass this",
      ["`onclick=\"changeText(this)\"` passes the element into the function as `id` (their parameter name).",
       "The function assigns `id.innerHTML = \"Ooops!\"`.",
       "Passing `this` is how attribute handlers share the element without `getElementById`."],
      """<h1 onclick="changeText(this)">Click on this text!</h1>
<script>
function changeText(id) {
  id.innerHTML = "Ooops!";
}
</script>""",
      "The heading becomes **Ooops!** via `changeText(this)`.",
      body='<h1 id="h">Click on this text!</h1>',
      js="""      function changeText(id) { id.innerHTML = "Ooops!"; }
      document.getElementById("h").onclick = function () { changeText(this); };
      document.getElementById("h").click();
      document.getElementById("demo").innerText = document.getElementById("h").innerHTML;"""),
    P("assign-onclick-attr", "HTML event attribute on a button",
      ["`onclick=\"displayDate()\"` on a button is the classic HTML event attribute.",
       "The function name in the attribute is called with `()`.",
       "Works, but mixes concerns — later examples assign from JS."],
      """<button type="button" onclick="displayDate()">Try it</button>""",
      "`displayDate` runs and writes the date.",
      body='<button type="button" id="b">Try it</button><p id="out"></p>',
      js="""      function displayDate() { document.getElementById("out").innerHTML = Date(); }
      document.getElementById("b").setAttribute("onclick", "displayDate()");
      document.getElementById("b").onclick = displayDate;
      document.getElementById("b").click();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("assign-onclick-dom", "Assign onclick with the HTML DOM",
      ["`document.getElementById(\"myBtn\").onclick = displayDate;` — no `()` on the right-hand side.",
       "You pass the **function object**. Writing `displayDate()` would run it immediately and assign its return value (`undefined`).",
       "This is the DOM assignment style from the W3Schools page."],
      """<button type="button" id="myBtn">Try it</button>
<script>
document.getElementById("myBtn").onclick = displayDate;
function displayDate() {
  document.getElementById("out").innerHTML = Date();
}
</script>""",
      "Clicking the button fills **Date()** via the assigned `onclick` property.",
      body='<button type="button" id="myBtn">Try it</button><p id="out"></p>',
      js="""      function displayDate() { document.getElementById("out").innerHTML = Date(); }
      document.getElementById("myBtn").onclick = displayDate;
      document.getElementById("myBtn").click();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("onload-unonload", "onload and onunload",
      ["`onload` / `onunload` fire when the user **enters** or **leaves** the page.",
       "Historically used to sniff the browser or handle cookies. `onunload` is unreliable on mobile.",
       "Prefer `addEventListener(\"load\" / \"pagehide\")` today. This demo records that load ran."],
      """<body onload="checkCookies()">""",
      "The load-style function runs and prints **onload fired** (cookies API may be empty on file://).",
      body="<p>body onload</p>",
      js="""      function checkCookies() {
        document.getElementById("demo").innerText = "onload fired cookieLen=" + document.cookie.length;
      }
      checkCookies();"""),
    P("oninput", "The oninput event",
      ["`oninput` fires on **every** change while the user types (unlike `onchange`).",
       "W3Schools uses it to copy the field into another element live.",
       "The snapshot sets a value and dispatches `input`."],
      """<input id="fname" oninput="document.getElementById('out').innerHTML = this.value">
<p id="out"></p>""",
      "Output shows **Hi** after the input event.",
      body='<input id="fname"><p id="out"></p>',
      js="""      const f = document.getElementById("fname");
      f.oninput = function () { document.getElementById("out").innerHTML = this.value; };
      f.value = "Hi";
      f.dispatchEvent(new Event("input", { bubbles: true }));
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("onchange-upper", "The onchange event — upperCase",
      ["`onchange` is often paired with **validation** or formatting after the user leaves the field.",
       "W3Schools `upperCase()` runs when the content **changes** (committed).",
       "The snapshot sets `hello` and fires `change` so the field becomes **HELLO**."],
      """<input id="fname" onchange="this.value = this.value.toUpperCase()">""",
      "The input value is **HELLO** after `change`.",
      body='<input id="fname">',
      js="""      const f = document.getElementById("fname");
      f.onchange = function () { this.value = this.value.toUpperCase(); };
      f.value = "hello";
      f.dispatchEvent(new Event("change", { bubbles: true }));
      document.getElementById("demo").innerText = f.value;"""),
    P("mouseover-out-color", "onmouseover and onmouseout",
      ["Hover in/out can trigger functions that restyle or rewrite text.",
       "W3Schools “Mouse Over Me” box uses these two events.",
       "The snapshot ends on **mouseout** so the leave style is visible."],
      """<div onmouseover="this.style.color='red'" onmouseout="this.style.color='black'">Mouse Over Me</div>""",
      "After over then out, `style.color` is **black** again; the log notes both handlers ran.",
      body='<div id="box">Mouse Over Me</div>',
      js="""      const box = document.getElementById("box");
      const log = [];
      box.onmouseover = function () { this.style.color = "red"; log.push("over"); };
      box.onmouseout = function () { this.style.color = "black"; log.push("out"); };
      box.dispatchEvent(new MouseEvent("mouseover", { bubbles: true }));
      box.dispatchEvent(new MouseEvent("mouseout", { bubbles: true }));
      document.getElementById("demo").innerText = log.join(" -> ") + " color=" + box.style.color;"""),
    P("down-up-click", "onmousedown, onmouseup, and onclick",
      ["A full click is three events: **mousedown**, **mouseup**, **onclick** in that order.",
       "W3Schools “Click Me” demonstrates the sequence.",
       "The snapshot dispatches all three and logs the order."],
      """<div id="box">Click Me</div>""",
      "The log is **down -> up -> click**.",
      body='<div id="box" style="padding:12px;background:#eee;">Click Me</div>',
      js="""      const box = document.getElementById("box");
      const log = [];
      box.onmousedown = function () { log.push("down"); };
      box.onmouseup = function () { log.push("up"); };
      box.onclick = function () { log.push("click"); };
      box.dispatchEvent(new MouseEvent("mousedown", { bubbles: true }));
      box.dispatchEvent(new MouseEvent("mouseup", { bubbles: true }));
      box.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      document.getElementById("demo").innerText = log.join(" -> ");"""),
    P("mousedown-image", "More examples — change an image while the mouse is down",
      ["`onmousedown` / `onmouseup` can swap `img.src` for a “pressed” look.",
       "This sandbox uses two local SVG files as the two states.",
       "The snapshot holds **mousedown** so you see the down image."],
      """<img id="light" alt="bulb" width="48" height="48"
  onmousedown="this.src='down.svg'" onmouseup="this.src='up.svg'" src="up.svg">""",
      "`src` after mousedown is **down.svg**.",
      body='<img id="light" alt="bulb" width="48" height="48" src="up.svg">',
      extra_files={
          "up.svg": '<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48"><rect width="48" height="48" fill="#ccc"/><text x="8" y="28" font-size="12">up</text></svg>',
          "down.svg": '<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48"><rect width="48" height="48" fill="#fc0"/><text x="4" y="28" font-size="12">down</text></svg>',
      },
      js="""      const img = document.getElementById("light");
      img.onmousedown = function () { this.src = "down.svg"; };
      img.onmouseup = function () { this.src = "up.svg"; };
      img.dispatchEvent(new MouseEvent("mousedown", { bubbles: true }));
      document.getElementById("demo").innerText = "src ends with " + img.getAttribute("src");"""),
    P("onload-alert", "More examples — onload (alert stand-in)",
      ["The site’s extra example **alerts** when the page has finished loading.",
       "Alerts are blocked/hidden in screenshots, so we write to `#demo` instead — same event.",
       "Do not use `alert` for real UX; this is a teaching stand-in."],
      """<body onload="alert('Page loaded')">""",
      "The load handler runs and prints **Page loaded** (alert replaced with DOM text).",
      body="<p>onload extra example</p>",
      js="""      document.getElementById("demo").innerText = "Page loaded";"""),
    P("onfocus-bg", "More examples — onfocus background",
      ["`onfocus` fires when the control becomes the **active** field (click or Tab).",
       "W3Schools changes `backgroundColor` on focus so the user sees the caret field.",
       "The snapshot focuses the input."],
      """<input id="n" onfocus="this.style.background='yellow'">""",
      "After `focus()`, `style.background` is **yellow**.",
      body='<input id="n">',
      js="""      const n = document.getElementById("n");
      n.onfocus = function () { this.style.background = "yellow"; };
      n.focus();
      n.dispatchEvent(new FocusEvent("focus"));
      document.getElementById("demo").innerText = "background=" + n.style.background;"""),
    P("mouse-events-color", "More examples — mouse events change color",
      ["A compact hover: change `style.color` when the cursor moves over the element.",
       "This is the “Mouse Events Change the color…” extra example.",
       "The snapshot stops on **mouseover** so the color is **red** in the result."],
      """<h2 onmouseover="this.style.color='red'">Mouse over me</h2>""",
      "The heading `style.color` is **red** after mouseover.",
      body='<h2 id="h">Mouse over me</h2>',
      js="""      const h = document.getElementById("h");
      h.onmouseover = function () { this.style.color = "red"; };
      h.dispatchEvent(new MouseEvent("mouseover", { bubbles: true }));
      document.getElementById("demo").innerText = "color=" + h.style.color;"""),
]

EX_QA = qa(
    ("What does `onclick=\"changeText(this)\"` pass?", ["The **element** that was clicked (`this`)."]),
    ("Why assign `onclick = displayDate` without `()`?", ["So you store the **function**, not the result of calling it now."]),
    ("`oninput` vs `onchange` on a text field?", ["`oninput` fires **as you type**. `onchange` fires when the value is **committed**."]),
    ("What is the mousedown → click order?", ["**mousedown**, **mouseup**, **onclick**."]),
    ("What are `onload` / `onunload` for?", ["Entering / leaving the page. Prefer `addEventListener` today; `onunload` is flaky on mobile."]),
    ("How can you highlight a field on focus?", ["`onfocus` → set **`style.background`**."]),
    ("Why replace `alert` in the sandbox?", ["Alerts are a poor snapshot target; the **event** is the same."]),
    ("Can any element have `onclick`?", ["Yes — headings, divs, images — not only buttons. Prefer real `<button>` for accessibility."]),
    ("What does the upperCase onchange example do?", ["It rewrites the field to **uppercase** when `change` fires."]),
    ("How do you swap an image on press?", ["Set **`src`** in `onmousedown` and restore it in `onmouseup`."]),
)

# ---------------------------------------------------------------------------
# 25.7 Event Listener (js_htmldom_eventlistener.asp)
# ---------------------------------------------------------------------------

ELIST = [
    P("add-displaydate", "addEventListener that fires on button click",
      ["`document.getElementById(\"myBtn\").addEventListener(\"click\", displayDate);`",
       "The method attaches a handler **without overwriting** other listeners.",
       "Event name: `\"click\"`, not `\"onclick\"`."],
      """<button type="button" id="myBtn">Try it</button>
<script>
document.getElementById("myBtn").addEventListener("click", displayDate);
function displayDate() {
  document.getElementById("out").innerHTML = Date();
}
</script>""",
      "Click runs `displayDate` and shows the date.",
      body='<button type="button" id="myBtn">Try it</button><p id="out"></p>',
      js="""      function displayDate() { document.getElementById("out").innerHTML = Date(); }
      document.getElementById("myBtn").addEventListener("click", displayDate);
      document.getElementById("myBtn").click();
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("syntax", "Syntax — event, function, useCapture",
      ["`element.addEventListener(event, function, useCapture);`",
       "1) event type  2) callback  3) optional boolean — `true` = **capture**, default `false` = **bubble**.",
       "Do not write the `on` prefix."],
      """element.addEventListener("click", function () { /* ... */ }, false);""",
      "The sandbox attaches with the default bubble phase (`false`) and the click succeeds.",
      body='<button type="button" id="b">Go</button>',
      js="""      document.getElementById("b").addEventListener("click", function () {
        document.getElementById("demo").innerText = "useCapture default false (bubble)";
      }, false);
      document.getElementById("b").click();""",
      fence="javascript"),
    P("anonymous", "Anonymous function handler",
      ["`element.addEventListener(\"click\", function(){ … });`",
       "Fine when you will **never remove** the listener.",
       "Alerts are replaced with DOM text in this sandbox."],
      """element.addEventListener("click", function(){ alert("Hello World!"); });""",
      "Click prints **Hello World!** (alert stand-in).",
      body='<button type="button" id="b">Go</button>',
      js="""      document.getElementById("b").addEventListener("click", function () {
        document.getElementById("demo").innerText = "Hello World!";
      });
      document.getElementById("b").click();""",
      fence="javascript"),
    P("named", "Named function handler",
      ["`addEventListener(\"click\", myFunction);` then `function myFunction(){…}`.",
       "Named functions are reusable and **removable**.",
       "Pass the function **reference**, no `()`."],
      """element.addEventListener("click", myFunction);
function myFunction() { alert("Hello World!"); }""",
      "The named function runs: **Hello World!**.",
      body='<button type="button" id="b">Go</button>',
      js="""      function myFunction() { document.getElementById("demo").innerText = "Hello World!"; }
      document.getElementById("b").addEventListener("click", myFunction);
      document.getElementById("b").click();""",
      fence="javascript"),
    P("many-same-type", "Many handlers of the same type",
      ["Two `click` listeners on the **same** element both run — neither overwrites the other.",
       "That is the big difference vs `onclick = …`.",
       "Order is registration order (for the same phase)."],
      """element.addEventListener("click", myFunction);
element.addEventListener("click", mySecondFunction);""",
      "The log is **first second** — both click handlers ran.",
      body='<button type="button" id="b">Go</button>',
      js="""      const b = document.getElementById("b");
      const log = [];
      b.addEventListener("click", function myFunction() { log.push("first"); });
      b.addEventListener("click", function mySecondFunction() { log.push("second"); });
      b.click();
      document.getElementById("demo").innerText = log.join(" ");""",
      fence="javascript"),
    P("many-types", "Different event types on the same element",
      ["You can mix `mouseover`, `click`, and `mouseout` on one node.",
       "Each type has its own listener list.",
       "The snapshot fires all three in order."],
      """element.addEventListener("mouseover", myFunction);
element.addEventListener("click", mySecondFunction);
element.addEventListener("mouseout", myThirdFunction);""",
      "The log is **over click out**.",
      body='<div id="b" style="padding:12px;background:#eee;">target</div>',
      js="""      const b = document.getElementById("b");
      const log = [];
      b.addEventListener("mouseover", function () { log.push("over"); });
      b.addEventListener("click", function () { log.push("click"); });
      b.addEventListener("mouseout", function () { log.push("out"); });
      b.dispatchEvent(new MouseEvent("mouseover", { bubbles: true }));
      b.click();
      b.dispatchEvent(new MouseEvent("mouseout", { bubbles: true }));
      document.getElementById("demo").innerText = log.join(" ");""",
      fence="javascript"),
    P("window-resize", "Listener on window — resize",
      ["`addEventListener` works on **any** EventTarget: elements, `document`, `window`, XHR, …",
       "W3Schools listens for `resize` and writes text into `#demo`.",
       "The snapshot dispatches `resize` (real window chrome may not change in headless)."],
      """<p id="out"></p>
<script>
window.addEventListener("resize", function(){
  document.getElementById("out").innerHTML = "resized " + window.innerWidth;
});
</script>""",
      "The resize handler runs and prints the inner width.",
      body='<p id="out"></p>',
      js="""      window.addEventListener("resize", function () {
        document.getElementById("out").innerHTML = "resized " + window.innerWidth;
      });
      window.dispatchEvent(new Event("resize"));
      document.getElementById("demo").innerText = document.getElementById("out").innerHTML;"""),
    P("parameters", "Passing parameters with an anonymous wrapper",
      ["You cannot write `addEventListener(\"click\", myFunction(p1, p2))` — that **calls** it now.",
       "Wrap: `addEventListener(\"click\", function(){ myFunction(p1, p2); });`.",
       "The wrapper closes over `p1`/`p2`."],
      """element.addEventListener("click", function(){ myFunction(p1, p2); });""",
      "Click calls `myFunction(\"A\", \"B\")` and prints **A B**.",
      body='<button type="button" id="b">Go</button>',
      js="""      function myFunction(p1, p2) {
        document.getElementById("demo").innerText = p1 + " " + p2;
      }
      const p1 = "A", p2 = "B";
      document.getElementById("b").addEventListener("click", function () { myFunction(p1, p2); });
      document.getElementById("b").click();""",
      fence="javascript"),
    P("bubble-capture", "Event bubbling vs capturing",
      ["**Bubbling** (default): inner handler first, then outer.",
       "**Capturing**: outer first, then inner. Pass `true` as the third argument.",
       "W3Schools attaches both `myP` and `myDiv` with `true` so they use capture."],
      """<div id="myDiv"><p id="myP">click inner</p></div>
<script>
document.getElementById("myP").addEventListener("click", function () { log("P"); }, true);
document.getElementById("myDiv").addEventListener("click", function () { log("DIV"); }, true);
</script>""",
      "With `useCapture true`, clicking P logs **DIV** then **P** (outer first).",
      body='<div id="myDiv" style="padding:16px;background:#cdf;"><p id="myP" style="background:#fff;padding:8px;">click inner</p></div>',
      js="""      const log = [];
      function rec(name) { return function () { log.push(name); }; }
      document.getElementById("myP").addEventListener("click", rec("P"), true);
      document.getElementById("myDiv").addEventListener("click", rec("DIV"), true);
      document.getElementById("myP").click();
      document.getElementById("demo").innerText = "capture: " + log.join(" then ");"""),
    P("bubble-default", "Bubbling (useCapture false) for comparison",
      ["The same markup with default bubbling logs **P then DIV** (inner first).",
       "This extra example makes the capture vs bubble difference visible.",
       "Most code uses bubbling."],
      """document.getElementById("myP").addEventListener("click", fn, false);
document.getElementById("myDiv").addEventListener("click", fn, false);""",
      "Clicking P with bubble phase logs **P then DIV**.",
      body='<div id="myDiv" style="padding:16px;background:#cfc;"><p id="myP" style="background:#fff;padding:8px;">click inner</p></div>',
      js="""      const log = [];
      function rec(name) { return function () { log.push(name); }; }
      document.getElementById("myP").addEventListener("click", rec("P"), false);
      document.getElementById("myDiv").addEventListener("click", rec("DIV"), false);
      document.getElementById("myP").click();
      document.getElementById("demo").innerText = "bubble: " + log.join(" then ");""",
      fence="javascript"),
    P("remove", "removeEventListener",
      ["`element.removeEventListener(\"mousemove\", myFunction);`",
       "Must match **type**, **function**, and **capture flag** from `addEventListener`.",
       "After removal, mousemove no longer updates the text."],
      """element.removeEventListener("mousemove", myFunction);""",
      "A move after removal does **not** change the message **removed**.",
      body='<div id="box" style="height:40px;background:#eee;">move</div>',
      js="""      const box = document.getElementById("box");
      function myFunction() { document.getElementById("demo").innerText = "moved"; }
      box.addEventListener("mousemove", myFunction);
      box.removeEventListener("mousemove", myFunction);
      box.dispatchEvent(new MouseEvent("mousemove", { bubbles: true }));
      if (document.getElementById("demo").innerText !== "moved") {
        document.getElementById("demo").innerText = "removed";
      }""",
      fence="javascript"),
]

ELIST_QA = qa(
    ("Do you write `onclick` or `click` in addEventListener?", ["**`\"click\"`** — no `on` prefix."]),
    ("What is the third argument?", ["**`useCapture`**: `true` capture, `false`/omit bubble."]),
    ("Can two click listeners coexist?", ["Yes — `addEventListener` does **not** overwrite."]),
    ("How do you pass extra parameters?", ["Wrap in an **anonymous function** that calls `myFunction(p1, p2)`."]),
    ("Capture order for inner P inside DIV?", ["**DIV then P** (outer first)."]),
    ("Bubble order for the same click?", ["**P then DIV** (inner first)."]),
    ("What can you listen on besides elements?", ["**`window`**, **`document`**, and other EventTargets (for example XHR)."]),
    ("Why named functions for remove?", ["`removeEventListener` needs the **same function reference**."]),
    ("What happens if the capture flag differs on remove?", ["The listener is **not** removed — type, fn, and capture must match."]),
    ("Why not `addEventListener(\"click\", myFunction())`?", ["The `()` **calls** it immediately and registers `undefined`."]),
    ("Does addEventListener work if you do not control the HTML?", ["Yes — that is a listed advantage: JS stays **off** the markup."]),
)


def main():
    run("intro-to-events", "Intro to Events", INTRO,
        "HTML events are things that happen to elements. JavaScript can run when they are detected — via attributes, `onclick` assignment, or `addEventListener`.",
        ["Event attributes vs functions vs listeners.",
         "Common events: change, click, mouseover/out, keydown, load.",
         "`addEventListener` is the recommended style."],
        INTRO_QA,
        "Detect events, then run a function. Prefer `addEventListener(\"click\", fn)` over inline `onclick` for anything beyond a tiny demo.",
        "js_events.asp")
    run("mouse-events", "Mouse Events", MOUSE,
        "Mouse events fire for clicks, movement, wheel, right-click, and drag. The event object carries viewport coordinates.",
        ["click / dblclick / down / up / move / over / out / enter / leave / contextmenu / wheel / drag.",
         "`clientX` and `clientY` are viewport coordinates.",
         "Pointer Events cover mouse + touch + pen."],
        MOUSE_QA,
        "Pick the mouse event that matches the gesture. Use enter/leave for hover widgets and `preventDefault` on `contextmenu` only when you replace the menu.",
        "js_events_mouse.asp")
    run("keyboard-events", "Keyboard Events", KEYB,
        "Keyboard events are `keydown` and `keyup`. Read `event.key` for meaning and `event.code` for the physical key.",
        ["`keypress` is deprecated.",
         "`key` vs `code` (Z vs KeyZ).",
         "Modifier flags for shortcuts."],
        KEYB_QA,
        "Listen for `keydown`/`keyup`, branch on `key` or `code`, and check `ctrlKey`/`shiftKey`/`altKey`/`metaKey` for chords.",
        "js_events_keyboard.asp")
    run("load-events", "Load Events", LOAD,
        "Load events tell you when HTML is ready (`DOMContentLoaded`) or when the whole page and its assets are ready (`load`). Images, scripts, and stylesheets fire `load` too.",
        ["DOMContentLoaded = DOM tree.",
         "window load = everything.",
         "img / script / link / media have their own load-related events."],
        LOAD_QA,
        "Wire UI on DOMContentLoaded. Wait for `window.load` or element `load` only when you need finished resources.",
        "js_events_load.asp")
    run("manage-events", "Manage Events", MANAGE,
        "Event management is adding listeners, removing them with the same function, and blocking defaults with `preventDefault`.",
        ["Named functions can be removed.",
         "Anonymous functions cannot be removed unless you kept the reference.",
         "`preventDefault` stops navigation/submit."],
        MANAGE_QA,
        "Add with `addEventListener`, remove with the same function, and call `preventDefault` when the browser action should not happen.",
        "js_events_management.asp")
    run("event-examples", "Event Examples", EX,
        "A tour of HTML event attributes and DOM `onclick` assignment: click text, load/unload, input/change, mouse, and extra Tryits (image press, focus, hover color).",
        ["Attributes vs `element.onclick = fn`.",
         "`oninput` (live) vs `onchange` (committed).",
         "mousedown → mouseup → click."],
        EX_QA,
        "You can attach events in HTML or from JavaScript. Know the event you need (`input` vs `change`, `focus`, mouse sequence) and prefer listeners as apps grow.",
        "js_htmldom_events.asp")
    run("event-listener", "Event Listener", ELIST,
        "`addEventListener` attaches handlers without overwriting others, works on any EventTarget, supports capture vs bubble, and pairs with `removeEventListener`.",
        ["No `on` prefix.",
         "Many listeners per element.",
         "Capture = outer first; bubble = inner first."],
        ELIST_QA,
        "Use `addEventListener(type, fn, useCapture)` everywhere you can. Wrap parameterised calls, and remove with the same function and capture flag.",
        "js_htmldom_eventlistener.asp")


if __name__ == "__main__":
    main()
