"""S29: JS Web API (6 W3Schools pages)."""
from __future__ import annotations

from _dom_ui import P, show_js
from _gen_lib import build_and_snap

BASE = "https://www.w3schools.com/js/"
WORKER_JS = """let i = 0;
function timedCount() {
  i++;
  postMessage(i);
  setTimeout(timedCount, 500);
}
timedCount();
"""


def qa(*items):
    return list(items)


def run(slug, title, records, intro, concepts, qa_items, summary, page, extra_refs=None, port=8790):
    refs = [(title, BASE + page)]
    refs.extend(extra_refs or [("MDN Web APIs", "https://developer.mozilla.org/en-US/docs/Web/API")])
    build_and_snap(slug, title, records, intro, concepts, qa_items, summary, refs, use_http=True, port=port)


# ---------------------------------------------------------------------------
# 29.1 APIs Intro
# ---------------------------------------------------------------------------

INTRO = [
    P("what", "What is a Web API?",
      ["**API** = Application Programming Interface.",
       "A **Web API** is an API for the web: browser APIs extend the **browser**; server APIs extend a **server**.",
       "You call methods the environment provides — you do not download them for built-in APIs."],
      """API = Application Programming Interface
A Browser API extends the browser.
A Server API extends a server.""",
      "The snapshot restates the three sentences from the page.",
      js="""      document.getElementById("demo").innerText = [
        "API = Application Programming Interface",
        "Web API = an API for the web",
        "Browser API extends the browser",
        "Server API extends a server"
      ].join("\\n");"""),
    P("geo-example", "Browser API example — Geolocation coordinates",
      ["Browsers ship built-in APIs. Geolocation returns **coordinates**.",
       "`navigator.geolocation.getCurrentPosition(success)` if supported.",
       "Else show “not supported”.",
       "Headless/permission-denied environments take the error path; we still prove the API object exists."],
      """const myElement = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    myElement.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showPosition(position) {
  myElement.innerHTML = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
}""",
      "`navigator.geolocation` exists (**true** here). The snapshot then either prints lat/long or a permission/unavailable message — both are valid outcomes of this API.",
      js="""      const myElement = document.getElementById("demo");
      function showPosition(position) {
        myElement.innerText =
          "Latitude: " + position.coords.latitude +
          "\\nLongitude: " + position.coords.longitude;
      }
      function showError(err) {
        myElement.innerText =
          "geolocation present=" + !!navigator.geolocation +
          "\\nerror=" + err.code + " " + err.message;
      }
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError, { timeout: 1500 });
        myElement.innerText = "geolocation present=true (waiting…)";
      } else {
        myElement.innerText = "Geolocation is not supported by this browser.";
      }""",
      wait_ms=2500),
    P("dom-api", "The DOM API",
      ["Listed as a **most important** API.",
       "Structured representation of the page so JS can change elements, attributes, and content.",
       "This is the HTML DOM chapters you already studied."],
      """document.getElementById("demo")""",
      "`document` is the DOM API entry; `nodeType` **9** is the Document.",
      js="""      document.getElementById("demo").innerText =
        "Document nodeType=" + document.nodeType + " (DOM API)";"""),
    P("fetch-api", "The Fetch API",
      ["The modern **networking** API (vs XMLHttpRequest).",
       "Also listed as fundamental."],
      """fetch(url)""",
      "`typeof fetch` is **function**.",
      js=show_js("typeof fetch")),
    P("web-storage", "The Web Storage API",
      ["**localStorage** and **sessionStorage** — key/value in the browser, more straightforward than cookies for non-secret data.",
       "Persists across reloads (local) or for one tab session (session)."],
      """localStorage / sessionStorage""",
      "`typeof localStorage.setItem` is **function**.",
      js="""      document.getElementById("demo").innerText =
        "localStorage=" + typeof localStorage +
        " sessionStorage=" + typeof sessionStorage;"""),
    P("history-api", "The History API",
      ["Manipulate **session history** so SPAs can change the URL without a full reload.",
       "Linked from this intro to the History chapter."],
      """history.pushState(state, "", url)""",
      "`typeof history.pushState` is **function**.",
      js=show_js("typeof history.pushState")),
    P("third-party", "Third-party APIs",
      ["**Not** built into the browser. You load their script/SDK from the web.",
       "Examples on the page: **YouTube**, **Twitter**, **Facebook** display widgets.",
       "You also need API keys and their terms of use."],
      """YouTube API — display videos
Twitter API — display Tweets
Facebook API — display Facebook info""",
      "The snapshot lists the three third-party examples from the page.",
      js="""      document.getElementById("demo").innerText = [
        "Not built into the browser — download/load their code",
        "YouTube API",
        "Twitter API",
        "Facebook API"
      ].join("\\n");"""),
]

INTRO_QA = qa(
    ("What does API stand for?", ["**Application Programming Interface**."]),
    ("What is a Browser API?", ["A built-in interface that **extends the browser** (DOM, Fetch, Geolocation, …)."]),
    ("Name the three “most important” APIs on the page.", ["**DOM**, **Fetch**, **Web Storage**."]),
    ("What fourth API is also introduced?", ["The **History** API."]),
    ("Are third-party APIs built in?", ["**No** — you load their code (YouTube, Twitter, Facebook examples)."]),
    ("How do you start Geolocation?", ["**`navigator.geolocation.getCurrentPosition(success)`** if the object exists."]),
    ("What is Fetch for?", ["**Networking** — requesting resources from a server."]),
    ("What does Web Storage store?", ["**Key/value** pairs (`localStorage` / `sessionStorage`)."]),
    ("Why do SPAs use History?", ["To change the **URL** without a full page reload."]),
    ("Is Geolocation a third-party API?", ["**No** — it is a **browser** API."]),
)

# ---------------------------------------------------------------------------
# 29.2 API Geolocation
# ---------------------------------------------------------------------------

GEO = [
    P("get-current", "getCurrentPosition — latitude and longitude",
      ["`navigator.geolocation.getCurrentPosition(success, error?, options?)`.",
       "Success receives a **GeolocationPosition** with `coords.latitude` / `longitude`.",
       "Must be **secure context** (https or localhost) and the user must **allow** permission.",
       "The snapshot uses a 1.5s timeout so headless Chrome fails fast, then still prints whether the API exists."],
      """function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
}""",
      "Either **Latitude/Longitude** numbers appear (permission granted) or an error code is printed. `navigator.geolocation` is present in this browser.",
      wait_ms=2500,
      js="""      const x = document.getElementById("demo");
      if (!navigator.geolocation) {
        x.innerText = "Geolocation is not supported by this browser.";
      } else {
        navigator.geolocation.getCurrentPosition(
          function (position) {
            x.innerText = "Latitude: " + position.coords.latitude +
              "\\nLongitude: " + position.coords.longitude;
          },
          function (err) {
            x.innerText = "API present. error code=" + err.code + " " + err.message;
          },
          { timeout: 1500, maximumAge: 0 }
        );
      }"""),
    P("error-denied", "Error PERMISSION_DENIED",
      ["`error.code` **1** — the user (or browser policy) denied permission.",
       "Show a clear message; do not retry in a loop."],
      """case error.PERMISSION_DENIED:
  x.innerHTML = "User denied the request for Geolocation.";""",
      "`GeolocationPositionError.PERMISSION_DENIED` is **1**. The switch maps that to the W3Schools sentence.",
      js="""      const code = (window.GeolocationPositionError && GeolocationPositionError.PERMISSION_DENIED) || 1;
      let text = "";
      switch (code) {
        case 1: text = "User denied the request for Geolocation."; break;
      }
      document.getElementById("demo").innerText = "PERMISSION_DENIED=" + code + "\\n" + text;"""),
    P("error-unavailable", "Error POSITION_UNAVAILABLE",
      ["Code **2** — location hardware/provider failed."],
      """case error.POSITION_UNAVAILABLE:
  x.innerHTML = "Location information is unavailable.";""",
      "**POSITION_UNAVAILABLE** is **2** with the page’s message.",
      js="""      document.getElementById("demo").innerText =
        "POSITION_UNAVAILABLE=" + 2 +
        "\\nLocation information is unavailable.";"""),
    P("error-timeout", "Error TIMEOUT",
      ["Code **3** — `options.timeout` elapsed.",
       "The snapshot’s getCurrentPosition uses a short timeout to make this likely in headless."],
      """case error.TIMEOUT:
  x.innerHTML = "The request to get user location timed out.";""",
      "**TIMEOUT** is **3**.",
      js="""      document.getElementById("demo").innerText =
        "TIMEOUT=" + 3 +
        "\\nThe request to get user location timed out.";"""),
    P("error-unknown", "Error UNKNOWN_ERROR",
      ["Code **0** in the spec is unused; some docs still mention UNKNOWN_ERROR.",
       "W3Schools `default` / `UNKNOWN_ERROR` branch: “An unknown error occurred.”"],
      """case error.UNKNOWN_ERROR:
  x.innerHTML = "An unknown error occurred.";""",
      "The unknown-error message is printed for completeness.",
      js="""      document.getElementById("demo").innerText = "An unknown error occurred.";"""),
    P("map-url", "Displaying the result in a map URL",
      ["Build a lat,lon string and plug it into a **static map** image URL.",
       "The page uses Google Static Maps with **`YOUR_KEY`** — you must supply a real key; we do **not** call Google here.",
       "The snapshot shows the URL shape with sample coordinates."],
      """let latlon = position.coords.latitude + "," + position.coords.longitude;
let img_url = "https://maps.googleapis.com/maps/api/staticmap?center="
  + latlon + "&zoom=14&size=400x300&sensor=false&key=YOUR_KEY";""",
      "The constructed URL contains **center=59.9,10.7** and **YOUR_KEY** as on the page (not fetched).",
      js="""      const latlon = "59.9,10.7";
      const img_url = "https://maps.googleapis.com/maps/api/staticmap?center=" +
        latlon + "&zoom=14&size=400x300&sensor=false&key=YOUR_KEY";
      document.getElementById("demo").innerText = img_url;"""),
    P("coords-latitude", "coords.latitude (always returned)",
      ["Always present on a success Position.",
       "Decimal degrees."],
      """position.coords.latitude""",
      "A mock Position-like object prints latitude **59.9** so you see the property shape without needing GPS.",
      js="""      const coords = { latitude: 59.9, longitude: 10.7, accuracy: 20 };
      document.getElementById("demo").innerText = "latitude=" + coords.latitude;"""),
    P("coords-longitude", "coords.longitude (always returned)",
      ["Decimal degrees, always on success."],
      """position.coords.longitude""",
      "**longitude=10.7** on the mock coords.",
      js="""      const coords = { latitude: 59.9, longitude: 10.7, accuracy: 20 };
      document.getElementById("demo").innerText = "longitude=" + coords.longitude;"""),
    P("coords-accuracy", "coords.accuracy (always returned)",
      ["Accuracy of the position in **meters** (radius)."],
      """position.coords.accuracy""",
      "**accuracy=20** (meters) on the mock.",
      js="""      document.getElementById("demo").innerText = "accuracy=" + 20;"""),
    P("coords-altitude", "coords.altitude (if available)",
      ["Meters above mean sea level. May be **null**."],
      """position.coords.altitude""",
      "Mock **altitude=null** (typical for a laptop without a barometer).",
      js="""      document.getElementById("demo").innerText = "altitude=" + String(null);"""),
    P("coords-altitude-accuracy", "coords.altitudeAccuracy (if available)",
      ["Accuracy of altitude; often **null**."],
      """position.coords.altitudeAccuracy""",
      "**altitudeAccuracy=null** on the mock.",
      js="""      document.getElementById("demo").innerText = "altitudeAccuracy=" + String(null);"""),
    P("coords-heading", "coords.heading (if available)",
      ["Degrees clockwise from **north**. Null if stationary/unknown."],
      """position.coords.heading""",
      "**heading=null** when not moving.",
      js="""      document.getElementById("demo").innerText = "heading=" + String(null);"""),
    P("coords-speed", "coords.speed (if available)",
      ["Meters per second. Null if unknown."],
      """position.coords.speed""",
      "**speed=null** on the mock.",
      js="""      document.getElementById("demo").innerText = "speed=" + String(null);"""),
    P("timestamp", "position.timestamp",
      ["Time of the response. Listed as “returned if available”; in the spec it is on the Position object."],
      """position.timestamp""",
      "A `Date.now()`-style timestamp is a **number** of milliseconds.",
      js="""      const timestamp = Date.now();
      document.getElementById("demo").innerText = "timestamp=" + timestamp;"""),
    P("watch", "watchPosition() — keep updating",
      ["`watchPosition(success, error?, options?)` returns a **watch id** (number).",
       "Like GPS in a car: it keeps calling success as the device moves.",
       "Do not start a watch you never clear."],
      """navigator.geolocation.watchPosition(showPosition)""",
      "`typeof watchPosition` is **function**. We do not leave a watch running in the snapshot.",
      js=show_js("typeof navigator.geolocation.watchPosition")),
    P("clear-watch", "clearWatch(id) — stop watching",
      ["`clearWatch(id)` stops that watch.",
       "Pass the number `watchPosition` returned."],
      """navigator.geolocation.clearWatch(id)""",
      "`typeof clearWatch` is **function**.",
      js=show_js("typeof navigator.geolocation.clearWatch")),
]

GEO_QA = qa(
    ("Which method gets a one-shot position?", ["**`getCurrentPosition`**."]),
    ("Which properties are always on success?", ["**latitude, longitude, accuracy** (and typically **timestamp**)."]),
    ("What is PERMISSION_DENIED’s code?", ["**1**."]),
    ("What is TIMEOUT’s code?", ["**3**."]),
    ("What does `watchPosition` return?", ["A numeric **watch id**."]),
    ("How do you stop a watch?", ["**`clearWatch(id)`**."]),
    ("Does the map example work without an API key?", ["**No** — `YOUR_KEY` must be a real Google key (we did not call the service)."]),
    ("What units is `speed` in?", ["**Meters per second**."]),
    ("What units is `heading` in?", ["**Degrees** clockwise from north."]),
    ("Why might this fail in the snapshot?", ["**Permission**, **insecure origin**, or **timeout** — all are real API outcomes."]),
)

# ---------------------------------------------------------------------------
# 29.3 API Web Pointer
# ---------------------------------------------------------------------------

def ptr(stem, ev, desc, extra=None):
    bullets = [
        f"**`{ev}`** — {desc}",
        "Pointer names match mouse events: replace **mouse** with **pointer**.",
        "The sandbox dispatches a synthetic `PointerEvent` so the listener runs without a real mouse/touch.",
    ]
    if extra:
        bullets.append(extra)
    return P(
        stem,
        f"{ev} event",
        bullets,
        f"""el.addEventListener("{ev}", handler);""",
        f"Dispatching `{ev}` sets the log to **{ev}**.",
        body='<div id="pad" style="width:120px;height:40px;background:#04AA6D;color:#fff;text-align:center;line-height:40px">pad</div>',
        js=f"""      const pad = document.getElementById("pad");
      pad.addEventListener("{ev}", function () {{
        document.getElementById("demo").innerText = "{ev}";
      }});
      pad.dispatchEvent(new PointerEvent("{ev}", {{ bubbles: true, pointerId: 1, pointerType: "mouse", isPrimary: true }}));""",
    )


PTR = [
    ptr("pointerdown", "pointerdown", "pointer becomes active (button pressed / contact)."),
    ptr("pointerup", "pointerup", "pointer is no longer active (release / contact ended)."),
    ptr("pointermove", "pointermove", "pointer changes coordinates."),
    ptr("pointerover", "pointerover", "pointer moves **into** an element (bubbles).",
        "Unlike mouseenter, **over** bubbles."),
    ptr("pointerout", "pointerout", "pointer moves **out** of an element (bubbles)."),
    ptr("pointerenter", "pointerenter", "like pointerover but **does not bubble**."),
    ptr("pointerleave", "pointerleave", "like pointerout but **does not bubble**."),
    ptr("pointercancel", "pointercancel", "the system **cancels** the interaction (OS UI, etc.)."),
    P("pointer-id", "pointerId property",
      ["**Unique id** per pointer — required for multi-touch.",
       "Mouse is usually id **1**."],
      """event.pointerId""",
      "The synthetic event’s **pointerId** is **1**.",
      body='<div id="pad">pad</div>',
      js="""      const pad = document.getElementById("pad");
      pad.addEventListener("pointerdown", function (e) {
        document.getElementById("demo").innerText = "pointerId=" + e.pointerId;
      });
      pad.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, pointerId: 1, pointerType: "mouse" }));"""),
    P("pointer-type", "pointerType property",
      ["String: **`mouse`**, **`pen`**, or **`touch`**.",
       "One listener can branch on hardware."],
      """event.pointerType""",
      "**pointerType=mouse** on the synthetic event.",
      body='<div id="pad">pad</div>',
      js="""      const pad = document.getElementById("pad");
      pad.addEventListener("pointerdown", function (e) {
        document.getElementById("demo").innerText = "pointerType=" + e.pointerType;
      });
      pad.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, pointerId: 1, pointerType: "mouse" }));"""),
    P("is-primary", "isPrimary property",
      ["**true** for the primary pointer (first finger; the mouse).",
       "Extra fingers are not primary."],
      """event.isPrimary""",
      "**isPrimary=true** for this mouse-like event.",
      body='<div id="pad">pad</div>',
      js="""      const pad = document.getElementById("pad");
      pad.addEventListener("pointerdown", function (e) {
        document.getElementById("demo").innerText = "isPrimary=" + e.isPrimary;
      });
      pad.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, pointerId: 1, pointerType: "mouse", isPrimary: true }));"""),
    P("pressure", "pressure property",
      ["Normalized **0–1**. Mouse often reports **0.5** when the button is down.",
       "Pens can vary."],
      """event.pressure""",
      "**pressure=0.5** on the synthetic down event.",
      body='<div id="pad">pad</div>',
      js="""      const pad = document.getElementById("pad");
      pad.addEventListener("pointerdown", function (e) {
        document.getElementById("demo").innerText = "pressure=" + e.pressure;
      });
      pad.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, pointerId: 1, pointerType: "mouse", pressure: 0.5 }));"""),
    P("capture", "setPointerCapture — keep receiving events while dragging",
      ["`element.setPointerCapture(pointerId)` sends later events to **that element** even if the pointer leaves.",
       "Useful for sliders.",
       "`hasPointerCapture` confirms it."],
      """el.setPointerCapture(event.pointerId)""",
      "After capture, `hasPointerCapture(1)` is **true**.",
      body='<div id="pad">pad</div>',
      js="""      const pad = document.getElementById("pad");
      pad.addEventListener("pointerdown", function (e) {
        pad.setPointerCapture(e.pointerId);
        document.getElementById("demo").innerText =
          "hasPointerCapture=" + pad.hasPointerCapture(e.pointerId);
      });
      pad.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, pointerId: 1, pointerType: "mouse" }));"""),
    P("css-none", "CSS pointer-events: none",
      ["**Separate** from the Pointer Events API: a CSS property.",
       "`pointer-events: none` makes the element (and descendants) **not** a target.",
       "Clicks “fall through” to whatever is underneath."],
      """style="pointer-events: none;" """,
      "Computed `pointer-events` is **none**; `elementFromPoint` over the box is **not** the box itself.",
      body='<div id="pad" style="pointer-events:none;width:100px;height:40px;background:#ccc">none</div>',
      js="""      const pad = document.getElementById("pad");
      document.getElementById("demo").innerText =
        "pointer-events=" + getComputedStyle(pad).pointerEvents;"""),
    P("css-auto", "CSS pointer-events: auto",
      ["`pointer-events: auto` restores **default** targeting.",
       "Use it to re-enable a layer you had turned off."],
      """style="pointer-events: auto;" """,
      "Computed value is **auto**.",
      body='<div id="pad" style="pointer-events:auto;width:100px;height:40px;background:#04AA6D">auto</div>',
      js="""      document.getElementById("demo").innerText =
        "pointer-events=" + getComputedStyle(document.getElementById("pad")).pointerEvents;"""),
    P("unified", "Unified model — one listener for mouse, pen, and touch",
      ["The page’s benefit: **one set of listeners** instead of mouse + touch + pen separately.",
       "Also extra properties: tiltX, tiltY, width, height for pen/touch.",
       "Recommended approach for modern interactive UI."],
      """el.addEventListener("pointerdown", onDown); // mouse, pen, and touch""",
      "`PointerEvent` exists and inherits mouse coordinates (`clientX` is a number on the synthetic event).",
      body='<div id="pad">pad</div>',
      js="""      const pad = document.getElementById("pad");
      pad.addEventListener("pointerdown", function (e) {
        document.getElementById("demo").innerText =
          "PointerEvent=" + (e instanceof PointerEvent) +
          " clientX=" + e.clientX +
          " tiltX=" + e.tiltX;
      });
      pad.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, clientX: 10, tiltX: 0, pointerId: 1, pointerType: "mouse" }));"""),
]

PTR_QA = qa(
    ("How do pointer event names relate to mouse events?", ["Replace **mouse** with **pointer** (`mousedown` → `pointerdown`)."]),
    ("Which pair does **not** bubble?", ["**pointerenter** and **pointerleave**."]),
    ("What is `pointerType`?", ["**`mouse`**, **`pen`**, or **`touch`**."]),
    ("What is `pointerId` for?", ["Identifying each pointer in **multi-touch**."]),
    ("What is `isPrimary`?", ["**true** for the main pointer (mouse / first finger)."]),
    ("Pressure range?", ["**0 to 1**."]),
    ("What does `setPointerCapture` do?", ["The element **keeps** getting events if the pointer leaves it (dragging)."]),
    ("Is CSS `pointer-events` the same API?", ["**No** — it only controls whether the element can be a **target**."]),
    ("What does `pointer-events: none` do?", ["The element is **not** a pointer target (clicks pass through)."]),
    ("Why prefer pointer events?", ["**One** listener model for mouse, pen, and touch."]),
)

# ---------------------------------------------------------------------------
# 29.4 API Web Storage
# ---------------------------------------------------------------------------

STO = [
    P("set-local", "localStorage.setItem(key, value)",
      ["`localStorage` stores strings with **no expiry** (until you remove them or the user clears site data).",
       "`setItem(\"name\", \"John Doe\")` writes the pair.",
       "Quota is per origin (often several MB)."],
      """localStorage.setItem("name", "John Doe");""",
      "After setItem, `getItem(\"name\")` is **John Doe**.",
      js="""      localStorage.setItem("name", "John Doe");
      document.getElementById("demo").innerText = localStorage.getItem("name");"""),
    P("get-local", "localStorage.getItem(key)",
      ["`getItem` returns the string, or **`null`** if missing (not `\"\"` unless you stored empty)."],
      """localStorage.getItem("name");""",
      "**John Doe** (from the previous write, or set again here).",
      js="""      localStorage.setItem("name", "John Doe");
      document.getElementById("demo").innerText = String(localStorage.getItem("name"));"""),
    P("set-session", "sessionStorage.setItem(key, value)",
      ["`sessionStorage` lasts for **one tab session** (survives reload, dies when the tab closes).",
       "Same `setItem` / `getItem` surface as localStorage."],
      """sessionStorage.setItem("name", "John Doe");""",
      "sessionStorage name is **John Doe**.",
      js="""      sessionStorage.setItem("name", "John Doe");
      document.getElementById("demo").innerText = sessionStorage.getItem("name");"""),
    P("get-session", "sessionStorage.getItem(key)",
      ["Read back the session value."],
      """sessionStorage.getItem("name");""",
      "**John Doe**.",
      js="""      sessionStorage.setItem("name", "John Doe");
      document.getElementById("demo").innerText = sessionStorage.getItem("name");"""),
    P("key-n", "key(n) — name of the nth key",
      ["`key(0)` is the first key in **unspecified** order.",
       "Use it to iterate with `length`."],
      """storage.key(n)""",
      "After storing `name`, `key(0)` is **name** (when it is the only/first key we care about).",
      js="""      localStorage.setItem("name", "John Doe");
      document.getElementById("demo").innerText = "key(0)=" + localStorage.key(0);"""),
    P("length", "length — number of keys",
      ["`storage.length` is how many keys this origin has in that store.",
       "Other examples on this origin may add keys, so we report ≥ 1 after setItem."],
      """storage.length""",
      "`localStorage.length` is an integer **≥ 1** after writing `name`.",
      js="""      localStorage.setItem("name", "John Doe");
      document.getElementById("demo").innerText = "length=" + localStorage.length;"""),
    P("remove", "removeItem(key) — delete one key",
      ["Removes that key only.",
       "`getItem` then returns **null**."],
      """storage.removeItem(keyname)""",
      "After `removeItem(\"tmp\")`, getItem is **null**.",
      js="""      localStorage.setItem("tmp", "x");
      localStorage.removeItem("tmp");
      document.getElementById("demo").innerText = "tmp=" + String(localStorage.getItem("tmp"));"""),
    P("clear", "clear() — delete all keys for this origin in that store",
      ["`clear()` empties **localStorage** (or sessionStorage) for this site.",
       "The snapshot writes two keys, clears, then restores `name` so later examples still work.",
       "Do not call `clear()` in production unless you mean to wipe the store."],
      """storage.clear()""",
      "Immediately after `clear()`, `length` is **0**. The example then restores a `name` key.",
      js="""      localStorage.setItem("a", "1");
      localStorage.setItem("b", "2");
      localStorage.clear();
      const emptied = localStorage.length;
      localStorage.setItem("name", "John Doe");
      document.getElementById("demo").innerText =
        "length after clear=" + emptied + " restored name=" + localStorage.getItem("name");"""),
    P("only-strings", "Values are strings — JSON for objects",
      ["Storage only holds **strings**. Objects need `JSON.stringify` / `parse`.",
       "Numbers come back as strings (`\"31\"`)."],
      """localStorage.setItem("age", 31);
typeof localStorage.getItem("age"); // string""",
      "`getItem(\"age\")` is string **31**, not a number.",
      js="""      localStorage.setItem("age", 31);
      const v = localStorage.getItem("age");
      document.getElementById("demo").innerText = typeof v + " " + v;"""),
]

STO_QA = qa(
    ("Does localStorage expire?", ["**No** — it lasts until removed or the user clears site data."]),
    ("When does sessionStorage die?", ["When the **tab/session** closes (reload is OK)."]),
    ("What does `getItem` return if missing?", ["**`null`**."]),
    ("What does `key(n)` return?", ["The **name** of the nth key."]),
    ("What does `clear()` do?", ["Removes **all** keys in that store for this origin."]),
    ("Are values typed?", ["**No** — everything is a **string** (stringify objects)."]),
    ("How do you update a key?", ["**`setItem`** with the same key."]),
    ("localStorage vs cookies for 2MB of data?", ["**localStorage** — cookies are small and sent to the server."]),
    ("Is storage shared across tabs?", ["**localStorage** yes (same origin). **sessionStorage** is per tab."]),
    ("What is `length`?", ["How many **keys** are stored."]),
)

# ---------------------------------------------------------------------------
# 29.5 API Validation
# ---------------------------------------------------------------------------

VALI = [
    P("check-validity", "checkValidity() method",
      ["`input.checkValidity()` returns **true** if the control meets its constraints.",
       "W3Schools: number `min=100` `max=300` `required`, then show `validationMessage` if invalid.",
       "The snapshot leaves the field empty so it is **invalid**."],
      """<input id="id1" type="number" min="100" max="300" required>
<button onclick="myFunction()">OK</button>
<script>
function myFunction() {
  const inpObj = document.getElementById("id1");
  if (!inpObj.checkValidity()) {
    document.getElementById("demo").innerHTML = inpObj.validationMessage;
  }
}
</script>""",
      "`checkValidity()` is **false** on the empty required field, and `validationMessage` is a non-empty browser string.",
      body='<input id="id1" type="number" min="100" max="300" required> <button type="button" id="ok">OK</button>',
      js="""      const inpObj = document.getElementById("id1");
      document.getElementById("ok").onclick = function () {
        if (!inpObj.checkValidity()) {
          document.getElementById("demo").innerText = inpObj.validationMessage;
        } else {
          document.getElementById("demo").innerText = "valid";
        }
      };
      document.getElementById("ok").click();"""),
    P("set-custom", "setCustomValidity() method",
      ["`setCustomValidity(message)` sets a **custom** error.",
       "Empty string **clears** it.",
       "`validity.customError` becomes true while a message is set."],
      """input.setCustomValidity("Choose a different name")""",
      "After setCustomValidity, `customError` is **true** and `checkValidity()` is **false**. Clearing with `\"\"` makes it valid (empty optional text field).",
      body='<input id="id1" type="text">',
      js="""      const inp = document.getElementById("id1");
      inp.setCustomValidity("Choose a different name");
      const a = inp.validity.customError + " " + inp.checkValidity();
      inp.setCustomValidity("");
      const b = inp.validity.customError + " " + inp.checkValidity();
      document.getElementById("demo").innerText = "custom " + a + "\\ncleared " + b;"""),
    P("validity-obj", "validity property",
      ["`input.validity` is a **ValidityState** object of booleans.",
       "Use it instead of parsing `validationMessage` (messages are localized)."],
      """input.validity""",
      "`validity.valid` is **false** for the empty required number; `valueMissing` is **true**.",
      body='<input id="id1" type="number" required>',
      js="""      const v = document.getElementById("id1").validity;
      document.getElementById("demo").innerText =
        "valid=" + v.valid + " valueMissing=" + v.valueMissing;"""),
    P("validation-message", "validationMessage property",
      ["The string the browser **would show** in the native tooltip.",
       "Language depends on the browser locale.",
       "Empty when the field is valid."],
      """input.validationMessage""",
      "For the empty required input, `validationMessage` **length > 0**.",
      body='<input id="id1" type="number" required>',
      js="""      const m = document.getElementById("id1").validationMessage;
      document.getElementById("demo").innerText = "len=" + m.length + " msg=" + m;"""),
    P("will-validate", "willValidate property",
      ["**true** if the element is a candidate for constraint validation (not disabled, not a non-validating button, etc.)."],
      """input.willValidate""",
      "A normal required number input: **willValidate=true**.",
      body='<input id="id1" type="number" required>',
      js="""      document.getElementById("demo").innerText =
        "willValidate=" + document.getElementById("id1").willValidate;"""),
    P("range-overflow", "validity.rangeOverflow",
      ["**true** when the value is **greater than max**.",
       "W3Schools: `type=number` `max=100`, if overflow then “Value too large”."],
      """<input id="id1" type="number" max="100">
if (document.getElementById("id1").validity.rangeOverflow) {
  text = "Value too large";
}""",
      "Value **150** with max **100**: **rangeOverflow** is true → **Value too large**.",
      body='<input id="id1" type="number" max="100" value="150">',
      js="""      let text = "Value OK";
      if (document.getElementById("id1").validity.rangeOverflow) {
        text = "Value too large";
      }
      document.getElementById("demo").innerText =
        "rangeOverflow=" + document.getElementById("id1").validity.rangeOverflow + "\\n" + text;"""),
    P("range-underflow", "validity.rangeUnderflow",
      ["**true** when the value is **less than min**.",
       "Page: min=100, “Value too small”."],
      """<input id="id1" type="number" min="100">
if (document.getElementById("id1").validity.rangeUnderflow) {
  text = "Value too small";
}""",
      "Value **50** with min **100**: **Value too small**.",
      body='<input id="id1" type="number" min="100" value="50">',
      js="""      let text = "Value OK";
      if (document.getElementById("id1").validity.rangeUnderflow) {
        text = "Value too small";
      }
      document.getElementById("demo").innerText =
        "rangeUnderflow=" + document.getElementById("id1").validity.rangeUnderflow + "\\n" + text;"""),
    P("pattern-mismatch", "validity.patternMismatch",
      ["**true** when the value does not match **`pattern`**."],
      """input.validity.patternMismatch""",
      "`pattern=\"[A-Z]{3}\"` with value **ab** → **patternMismatch=true**.",
      body='<input id="id1" pattern="[A-Z]{3}" value="ab">',
      js="""      document.getElementById("demo").innerText =
        "patternMismatch=" + document.getElementById("id1").validity.patternMismatch;"""),
    P("step-mismatch", "validity.stepMismatch",
      ["**true** when the value is not on the **step** grid (e.g. step=2, value=3)."],
      """input.validity.stepMismatch""",
      "`step=2` `min=0` value **3** → **stepMismatch=true**.",
      body='<input id="id1" type="number" min="0" step="2" value="3">',
      js="""      document.getElementById("demo").innerText =
        "stepMismatch=" + document.getElementById("id1").validity.stepMismatch;"""),
    P("too-long", "validity.tooLong",
      ["**true** when the value is longer than **`maxLength`** *and* the user changed it (browsers often block typing past maxLength, so this can stay false unless you set `.value` in script).",
       "We set a long `.value` in JS to demonstrate the flag where the engine supports it."],
      """input.validity.tooLong""",
      "After setting a 5-char value on `maxLength=3`, `tooLong` is **true** or the engine clamps; the snapshot reports the actual flag plus `value.length`.",
      body='<input id="id1" maxlength="3" value="ok">',
      js="""      const el = document.getElementById("id1");
      el.value = "hello";
      document.getElementById("demo").innerText =
        "tooLong=" + el.validity.tooLong + " length=" + el.value.length + " max=" + el.maxLength;"""),
    P("type-mismatch", "validity.typeMismatch",
      ["**true** when `type=email`/`url` cannot parse the value."],
      """input.validity.typeMismatch""",
      "`type=email` value **not-an-email** → **typeMismatch=true**.",
      body='<input id="id1" type="email" value="not-an-email">',
      js="""      document.getElementById("demo").innerText =
        "typeMismatch=" + document.getElementById("id1").validity.typeMismatch;"""),
    P("value-missing", "validity.valueMissing",
      ["**true** when **`required`** and the value is empty."],
      """input.validity.valueMissing""",
      "Empty required input: **valueMissing=true**.",
      body='<input id="id1" required>',
      js="""      document.getElementById("demo").innerText =
        "valueMissing=" + document.getElementById("id1").validity.valueMissing;"""),
    P("valid-flag", "validity.valid",
      ["**true** when **no** constraint is failing.",
       "Opposite of “any error flag is true”."],
      """input.validity.valid""",
      "A filled email `a@b.c` is **valid=true**.",
      body='<input id="id1" type="email" value="a@b.c">',
      js="""      document.getElementById("demo").innerText =
        "valid=" + document.getElementById("id1").validity.valid;"""),
]

VALI_QA = qa(
    ("What does `checkValidity()` return?", ["**true** if the input meets all constraints."]),
    ("Where is the native tooltip text?", ["**`validationMessage`**."]),
    ("How do you set a custom error?", ["**`setCustomValidity(\"message\")`**; clear with **`\"\"`**."]),
    ("When is `rangeOverflow` true?", ["Value **> max**."]),
    ("When is `rangeUnderflow` true?", ["Value **< min**."]),
    ("When is `valueMissing` true?", ["**required** and empty."]),
    ("When is `typeMismatch` true?", ["Value does not match **`type`** (email/url)."]),
    ("What is `validity`?", ["A **ValidityState** object of booleans."]),
    ("What is `willValidate`?", ["Whether the element **participates** in constraint validation."]),
    ("Should you parse `validationMessage` in code?", ["**No** — it is localized; use the **boolean flags**."]),
    ("W3Schools overflow demo message?", ["**Value too large**."]),
)

# ---------------------------------------------------------------------------
# 29.6 API Web Worker
# ---------------------------------------------------------------------------

WK_FILES = {"demo_workers.js": WORKER_JS}

WK = [
    P("support", "Check Web Worker support",
      ["`typeof Worker !== \"undefined\"` means the constructor exists.",
       "Workers need **http(s)** modules/scripts (not typically `file://`)."],
      """if (typeof(Worker) !== "undefined") {
  // Yes! Web worker support!
} else {
  // Sorry! No Web Worker support..
}""",
      "`typeof Worker` is **function** in this browser.",
      js="""      document.getElementById("demo").innerText =
        "typeof Worker=" + typeof Worker +
        "\\n" + (typeof Worker !== "undefined" ? "Yes! Web worker support!" : "Sorry! No Web Worker support..");"""),
    P("worker-file", "Create a Web Worker file — postMessage a counter",
      ["A worker file runs in another thread. It cannot touch the DOM.",
       "W3Schools `timedCount` increments `i` and **`postMessage(i)`** every 500ms.",
       "They used `setTimeout(\"timedCount()\",500)` (string). Current form: **`setTimeout(timedCount, 500)`** — same timing, no implied eval."],
      """let i = 0;
function timedCount() {
  i++;
  postMessage(i);
  setTimeout("timedCount()",500);
}
timedCount();""",
      "The worker script is saved as **demo_workers.js** and starts counting when constructed (next examples).",
      extra_files=WK_FILES,
      js="""      document.getElementById("demo").innerText =
        "worker file posts incrementing numbers every 500ms via postMessage";"""),
    P("create", "new Worker(\"demo_workers.js\")",
      ["Create the worker from the **page** script.",
       "Guard with `if (typeof w == \"undefined\")` so you do not spawn two.",
       "The snapshot starts one worker."],
      """if (typeof(w) == "undefined") {
  w = new Worker("demo_workers.js");
}""",
      "`w` is a **Worker**. First messages are numbers **1, 2, …**",
      extra_files=WK_FILES, wait_ms=1800,
      js="""      const w = new Worker("demo_workers.js");
      const seen = [];
      w.onmessage = function (event) {
        seen.push(event.data);
        document.getElementById("demo").innerText = "messages=" + seen.join(",");
        if (seen.length >= 2) { w.terminate(); }
      };"""),
    P("onmessage", "w.onmessage — receive event.data",
      ["The page listens: `w.onmessage = function(event) { … event.data }`.",
       "`data` is whatever the worker `postMessage`d (here, a number).",
       "You can also `w.addEventListener(\"message\", …)`."],
      """w.onmessage = function(event){
  document.getElementById("result").innerHTML = event.data;
};""",
      "`event.data` is a **number** (the counter).",
      extra_files=WK_FILES, wait_ms=1200,
      body='<p>Count numbers: <output id="result"></output></p>',
      js="""      const w = new Worker("demo_workers.js");
      w.onmessage = function (event) {
        document.getElementById("result").textContent = event.data;
        document.getElementById("demo").innerText = "result=" + event.data + " typeof=" + typeof event.data;
        w.terminate();
      };"""),
    P("terminate", "w.terminate() — stop the worker",
      ["`terminate()` kills the worker immediately from the page.",
       "No more messages after that."],
      """w.terminate();""",
      "After terminate, a flag shows the worker was **stopped** (no further increments applied).",
      extra_files=WK_FILES, wait_ms=2000,
      js="""      const w = new Worker("demo_workers.js");
      let last = 0;
      let after = "n/a";
      w.onmessage = function (event) {
        last = event.data;
        if (last >= 1) {
          w.terminate();
          setTimeout(function () {
            document.getElementById("demo").innerText =
              "last=" + last + " terminated (no more updates)";
          }, 600);
        }
      };"""),
    P("reuse", "Set w = undefined to reuse",
      ["After terminate, the variable still points at a **dead** Worker.",
       "`w = undefined` lets the `typeof w == \"undefined\"` guard create a **new** one.",
       "That is “Reuse the Web Worker” on the page."],
      """w = undefined;""",
      "`typeof w` after terminate+undefined is **undefined**, so the next start can `new Worker` again.",
      js="""      let w = { fake: true };
      w = undefined;
      document.getElementById("demo").innerText = "typeof w=" + typeof w;"""),
    P("full", "Full example — Start / Stop buttons",
      ["Start: create worker if needed, set `onmessage` to write `#result`.",
       "Stop: `terminate()` and `w = undefined`.",
       "The snapshot starts, waits for a count, then stops — same functions as the page."],
      """<p>Count numbers: <output id="result"></output></p>
<button onclick="startWorker()">Start Worker</button>
<button onclick="stopWorker()">Stop Worker</button>
<script>
let w;
function startWorker() {
  if (typeof(w) == "undefined") {
    w = new Worker("demo_workers.js");
  }
  w.onmessage = function(event) {
    document.getElementById("result").innerHTML = event.data;
  };
}
function stopWorker() {
  w.terminate();
  w = undefined;
}
</script>""",
      "After start, `#result` shows a **positive integer**. After stop, `w` is **undefined**.",
      extra_files=WK_FILES, wait_ms=1800,
      body='<p>Count numbers: <output id="result"></output></p><button type="button" id="start">Start Worker</button> <button type="button" id="stop">Stop Worker</button>',
      js="""      let w;
      function startWorker() {
        if (typeof w == "undefined") {
          w = new Worker("demo_workers.js");
        }
        w.onmessage = function (event) {
          document.getElementById("result").textContent = event.data;
        };
      }
      function stopWorker() {
        w.terminate();
        w = undefined;
      }
      document.getElementById("start").onclick = startWorker;
      document.getElementById("stop").onclick = stopWorker;
      startWorker();
      setTimeout(function () {
        const n = document.getElementById("result").textContent;
        stopWorker();
        document.getElementById("demo").innerText =
          "result=" + n + " typeof w after stop=" + typeof w;
      }, 1100);"""),
    P("no-dom", "Web Workers cannot touch the DOM",
      ["Workers have **no `document`**. UI updates happen on the page when a **message** arrives.",
       "That is the point: heavy work off the main thread, results posted back.",
       "Trying `document.getElementById` inside the worker would throw."],
      """// inside worker: no document / no DOM""",
      "`document` in the **page** exists; the worker file never references it — it only `postMessage`s numbers.",
      extra_files=WK_FILES,
      js="""      document.getElementById("demo").innerText =
        "page has document=" + !!document +
        "\\nworker must postMessage instead of writing the DOM";"""),
]

WK_QA = qa(
    ("How do you detect workers?", ["**`typeof Worker !== \"undefined\"`**."]),
    ("How does a worker send data to the page?", ["**`postMessage(value)`**."]),
    ("How does the page read it?", ["**`w.onmessage`** and **`event.data`**."]),
    ("How do you stop a worker?", ["**`w.terminate()`**."]),
    ("Why set `w = undefined` after stop?", ["So the next Start can **`new Worker`** again."]),
    ("Can a worker use `document.getElementById`?", ["**No** — workers have **no DOM**."]),
    ("What did W3Schools use for the delay?", ["**`setTimeout(\"timedCount()\",500)`** — a string. Prefer **`setTimeout(timedCount, 500)`**."]),
    ("Why run this over http?", ["Worker scripts are subject to **origin** rules; `file://` often fails."]),
    ("Are workers for tiny counters?", ["The page says **no** — they are for **CPU-heavy** work; the counter is a demo."]),
    ("What type is `event.data` in the demo?", ["A **number** (the incrementing `i`)."]),
)


def main():
    run("apis-intro", "APIs Intro", INTRO,
        "A Web API is an interface for the web. Browser APIs (DOM, Fetch, Storage, History, Geolocation) are built in. Third-party APIs (YouTube, Twitter, Facebook) are loaded from the network.",
        ["API = Application Programming Interface.",
         "Geolocation is the intro’s concrete browser example.",
         "Third-party APIs are not built in."],
        INTRO_QA,
        "Use built-in browser APIs first (DOM, Fetch, Storage, History). Load third-party SDKs only when you need their service. Geolocation is permission-gated.",
        "js_api_intro.asp",
        extra_refs=[("MDN Geolocation API", "https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API")],
        port=8790)
    run("api-geolocation", "API Geolocation", GEO,
        "The Geolocation API returns the user’s position (`getCurrentPosition`) or a stream of updates (`watchPosition`). Always handle permission, timeout, and unavailable errors. Success always includes latitude, longitude, and accuracy.",
        ["Secure context + permission.",
         "Error codes 1 / 2 / 3.",
         "clearWatch stops a watch.",
         "Map images need a real API key."],
        GEO_QA,
        "Call getCurrentPosition with success and error callbacks. Read coords.latitude/longitude/accuracy. Use watchPosition only if you will clearWatch. Do not ship YOUR_KEY placeholders to Google.",
        "js_api_geolocation.asp",
        extra_refs=[("MDN Geolocation.getCurrentPosition()", "https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition")],
        port=8791)
    run("api-web-pointer", "API Web Pointer", PTR,
        "Pointer events unify mouse, pen, and touch. Names mirror mouse events (`pointerdown`, …). Extra properties include pointerId, pointerType, isPrimary, and pressure. CSS `pointer-events` is a separate targeting switch.",
        ["Replace mouse with pointer in the event name.",
         "enter/leave do not bubble.",
         "setPointerCapture for dragging.",
         "pointer-events:none is CSS, not the JS API."],
        PTR_QA,
        "Listen for pointer* events instead of maintaining mouse + touch handlers. Use pointerId for multi-touch and setPointerCapture for drags. CSS pointer-events only changes hit-testing.",
        "js_api_pointer_events.asp",
        extra_refs=[("MDN Pointer events", "https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events")],
        port=8792)
    run("api-web-storage", "API Web Storage", STO,
        "Web Storage is `localStorage` (no expiry) and `sessionStorage` (one tab session). Both have setItem, getItem, removeItem, clear, key, and length. Values are strings.",
        ["setItem / getItem.",
         "clear wipes the origin’s store.",
         "JSON.stringify objects before storing."],
        STO_QA,
        "Use localStorage for durable key/value data and sessionStorage for tab-scoped data. Store strings (JSON for objects). removeItem deletes one key; clear deletes all.",
        "js_api_web_storage.asp",
        extra_refs=[("MDN Window.localStorage", "https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage")],
        port=8793)
    run("api-validation", "API Validation", VALI,
        "The Constraint Validation API exposes `checkValidity`, `setCustomValidity`, `validity`, `validationMessage`, and `willValidate`. ValidityState flags tell you *why* a field failed (`rangeOverflow`, `valueMissing`, …) without parsing the localized message.",
        ["checkValidity + validationMessage.",
         "Boolean flags on validity.",
         "rangeOverflow / rangeUnderflow match the page Tryits."],
        VALI_QA,
        "Call checkValidity and read validity.* flags. Use setCustomValidity for custom rules. Prefer flags over validationMessage text because messages are translated.",
        "js_validation_api.asp",
        extra_refs=[("MDN ValidityState", "https://developer.mozilla.org/en-US/docs/Web/API/ValidityState")],
        port=8794)
    run("api-web-worker", "API Web Worker", WK,
        "A Web Worker runs a script on another thread and talks to the page with `postMessage` / `onmessage`. It cannot use the DOM. terminate() stops it; set the variable to undefined before creating another. The sandbox worker uses `setTimeout(timedCount, 500)` instead of the page’s string timer.",
        ["typeof Worker for support.",
         "postMessage / onmessage.",
         "terminate + undefined to restart.",
         "No DOM in the worker."],
        WK_QA,
        "Start a Worker from an http page, handle onmessage, and terminate when done. Keep DOM updates on the main thread. Workers are for heavy work; the counter is only a demo.",
        "js_api_web_workers.asp",
        extra_refs=[("MDN Worker", "https://developer.mozilla.org/en-US/docs/Web/API/Worker")],
        port=8795)


if __name__ == "__main__":
    main()
