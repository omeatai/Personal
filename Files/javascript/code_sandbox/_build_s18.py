"""S18: JS Errors Intro, Silent, Statements, and Error Object."""
from __future__ import annotations

import json

from _gen_lib import S, build_and_snap, indent_js


def catch_script(
    setup: str,
    attempts: list[tuple[str, str]],
    *,
    strict: bool = False,
) -> str:
    """Run setup, then try/catch each (label, expr) and print name + message."""
    lines: list[str] = []
    if strict:
        lines.append('      "use strict";')
    if setup:
        for line in setup.split("\n"):
            lines.append(("      " + line) if line else "")
    for i, (_lab, expr) in enumerate(attempts):
        v = f"r{i}"
        lines.append(f"      let {v};")
        lines.append("      try {")
        lines.append(f"        {v} = {expr};")
        lines.append("      } catch (e) {")
        lines.append(f'        {v} = e.name + ": " + e.message;')
        lines.append("      }")
    parts = [
        f'{json.dumps(lab + " -> ")} + String(r{i})'
        for i, (lab, _expr) in enumerate(attempts)
    ]
    joined = ' + "\\n" + '.join(parts) if parts else '""'
    lines.append(f'      document.getElementById("demo").innerText = {joined};')
    return "\n".join(lines)


def nf_script(snippet: str) -> str:
    """Compile snippet with new Function so parse-time SyntaxError can be caught."""
    return f"""      let msg;
      try {{
        new Function({json.dumps(snippet)})();
        msg = "ran without error";
      }} catch (e) {{
        msg = e.name + ": " + e.message;
      }}
      document.getElementById("demo").innerText =
        msg + "\\n" + "(caught via new Function; a raw <script> would fail to parse)";"""


def nm_script(js_try: str) -> str:
    """Run a block in try/catch and print err.name + err.message (or no throw)."""
    return f"""      let name = "(no throw)";
      let message = "";
      try {{
{indent_js(js_try, 8)}
      }} catch (e) {{
        if (e !== null && typeof e === "object") {{
          name = String(e.name);
          message = String(e.message);
        }} else {{
          name = "(not an Error object)";
          message = String(e);
        }}
      }}
      document.getElementById("demo").innerText =
        "err.name -> " + name + "\\n" +
        "err.message -> " + message;"""


def out_script(js: str, lines: list[tuple[str, str]]) -> str:
    """Run js, then print label -> expr lines (js may set locals)."""
    parts = [f'{json.dumps(lab + " -> ")} + String({expr})' for lab, expr in lines]
    joined = ' + "\\n" + '.join(parts)
    return f"""{indent_js(js)}
      document.getElementById("demo").innerText = {joined};"""


# ---------------------------------------------------------------------------
# 18.1 JS Errors Intro
# ---------------------------------------------------------------------------

INTRO = [
    S(
        "try-block-no-error",
        "try — catch is skipped when nothing throws",
        [
            "The **`try`** block is the code you want to test for errors.",
            "If the block finishes **without** throwing, **`catch` is skipped**.",
        ],
        "let status = \"start\";\ntry {\n  status = \"try ran\";\n} catch (err) {\n  status = \"catch ran: \" + err;\n}",
        [("status", "status")],
        'status is **"try ran"**. The catch block did **not** run.',
    ),
    S(
        "catch-block-runs",
        "catch — runs when the try block throws",
        [
            "**`catch`** runs only if **`try`** throws.",
            "The parameter (`err`) is the thrown value. Built-in errors have **`name`** and **`message`**.",
        ],
        'try {\n  null.foo;\n} catch (err) {\n  let text = err.name;\n}',
        outcome="**TypeError**: Cannot read properties of **null** (reading **'foo'**). Catch ran.",
        script=nm_script("null.foo;"),
    ),
    S(
        "referenceerror-undeclared",
        "ReferenceError — y is not defined",
        [
            "A **`ReferenceError`** occurs if you use a variable that **does not exist**.",
            "The W3Schools table also lists `fname = foo` → **foo is not defined**. Same error name.",
        ],
        "let x = 5;\ntry {\n  x = y + 1;\n} catch (err) {\n  let text = err.name;\n}",
        outcome="**ReferenceError**: **y is not defined**.",
        script=catch_script("let x = 5;", [("x = y + 1", "(x = y + 1)")]),
    ),
    S(
        "referenceerror-tdz",
        "ReferenceError — Cannot access y before initialization",
        [
            "`let x = y` then `let y = 5` is **not** “y does not exist.”",
            "`let y` is in the **temporal dead zone** — **ReferenceError** before initialization.",
        ],
        "try {\n  let x = y;\n  let y = 5;\n} catch (err) {\n  let text = err.name;\n}",
        outcome="**ReferenceError**: **Cannot access 'y' before initialization**.",
        script=nm_script("let x = y;\nlet y = 5;"),
    ),
    S(
        "typeerror-not-a-function",
        "TypeError — anna is not a function",
        [
            "A **`TypeError`** occurs when a value is the **wrong type** for the operation.",
            "`anna` is the number **5**, so `anna(5)` is not a call.",
        ],
        "let anna = 5;\ntry {\n  anna(5);\n} catch (err) {\n  let text = err.name;\n}",
        outcome="**TypeError**: **anna is not a function**.",
        script=catch_script("let anna = 5;", [("anna(5)", "anna(5)")]),
    ),
    S(
        "typeerror-touppercase",
        "TypeError — num.toUpperCase is not a function",
        [
            "Numbers do not have **`toUpperCase`** (that is a **string** method).",
            "Calling it is a **TypeError**, not a silent no-op.",
        ],
        "let num = 1;\ntry {\n  num.toUpperCase();\n} catch (err) {\n  let text = err.name;\n}",
        outcome="**TypeError**: **num.toUpperCase is not a function**.",
        script=catch_script("let num = 1;", [("num.toUpperCase()", "num.toUpperCase()")]),
    ),
    S(
        "rangeerror-array-length",
        "RangeError — Invalid array length",
        [
            "A **`RangeError`** occurs when a value is **out of its valid range**.",
            "`new Array(-1)` is not a legal length.",
        ],
        "try {\n  new Array(-1);\n} catch (err) {\n  let text = err.name;\n}",
        outcome="**RangeError**: **Invalid array length**.",
        script=catch_script("", [("new Array(-1)", "new Array(-1)")]),
    ),
    S(
        "rangeerror-toprecision",
        "RangeError — toPrecision() argument must be between 1 and 100",
        [
            "`Number.prototype.toPrecision(precision)` only allows **1–100** significant digits.",
            "**500** is out of range.",
        ],
        "let num = 1;\ntry {\n  num.toPrecision(500);  // A number cannot have 500 significant digits\n} catch (err) {\n  let text = err.name;\n}",
        outcome="**RangeError**: **toPrecision() argument must be between 1 and 100**.",
        script=catch_script("let num = 1;", [("num.toPrecision(500)", "num.toPrecision(500)")]),
    ),
    S(
        "urierror-decodeuri",
        "URIError — decodeURI('%%%') URI malformed",
        [
            "A **`URIError`** occurs if you pass **illegal characters** to a URI function.",
            "`decodeURI(\"%%%\")` is not a valid percent-encoding.",
        ],
        'try {\n  decodeURI("%%%");  // You cannot URI decode percent signs\n} catch (err) {\n  document.getElementById("demo").innerHTML = err.name;\n}',
        outcome="**URIError**: **URI malformed**.",
        script=catch_script("", [('decodeURI("%%%")', 'decodeURI("%%%")')]),
    ),
    S(
        "syntaxerror-unclosed-string",
        "SyntaxError — unclosed string (not catchable in a raw script)",
        [
            "A **`SyntaxError`** means the source **violates JavaScript grammar**.",
            "The engine throws it **before runtime**. A raw `<script>` **does not load**.",
            "This sandbox compiles the snippet with **`new Function`** so the page can still render.",
        ],
        '// This line cannot be parsed by JavaScript\nlet text = "John Doe);\n// This line will not be executed',
        outcome="**SyntaxError**: **Invalid or unexpected token** (via `new Function`). A raw script would stop the page.",
        script=nf_script('let text = "John Doe);'),
    ),
    S(
        "syntaxerror-not-catchable",
        "SyntaxError — try/catch cannot catch Math.round(4.6;)",
        [
            "`Math.round(4.6;)` has an extra **`;`** inside the parentheses — **missing ) after argument list**.",
            "**`try...catch` does not help**: the **whole script** fails to parse, so `try` never starts.",
            "`err.description` on the W3Schools page is **IE-only**. This engine uses **`err.message`**.",
        ],
        "try {\n  let x = Math.round(4.6;)\n} catch (err) {\n  let text = err.name + \" \" + err.description;\n}",
        outcome="**SyntaxError**: **missing ) after argument list**. Inner `catch` never ran — the snippet did not parse.",
        script=nf_script("try { let x = Math.round(4.6;) } catch (err) { let text = err.name + ' ' + err.description; }"),
    ),
    S(
        "evalerror-deprecated",
        "EvalError — deprecated; eval throws SyntaxError instead",
        [
            "The page lists **EvalError** (deprecated). Newer engines **do not throw EvalError** from `eval()`.",
            "`new EvalError(...)` still constructs an object whose **`name`** is **EvalError**.",
            "Bad `eval` source is a **SyntaxError** (use that).",
        ],
        'const made = new EvalError("still constructable");\ntry {\n  eval("var = 1");\n} catch (err) {\n  // SyntaxError, not EvalError\n}',
        outcome="`new EvalError` has name **EvalError**. `eval(\"var = 1\")` throws **SyntaxError**: **Unexpected token '='** — not EvalError.",
        script="""      const made = new EvalError("still constructable");
      let evalMsg;
      try {
        eval("var = 1");
        evalMsg = "eval ran";
      } catch (e) {
        evalMsg = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "new EvalError().name -> " + made.name + "\\n" +
        "new EvalError().message -> " + made.message + "\\n" +
        "eval(\\"var = 1\\") -> " + evalMsg;""",
    ),
]


# ---------------------------------------------------------------------------
# 18.2 JS Errors Silent
# ---------------------------------------------------------------------------

SILENT = [
    S(
        "divide-by-zero-infinity",
        "1 / 0 is Infinity — silent vs throw",
        [
            "**Silent errors do not stop the program.** Execution **continues**.",
            "`1 / 0` is **Infinity** (IEEE 754). JavaScript does **not** throw.",
            "To fail loudly you must **`throw` yourself** after checking `Number.isFinite`.",
        ],
        "let x = 1 / 0;\ntry {\n  if (!Number.isFinite(x)) throw new Error(\"division produced Infinity\");\n} catch (err) {\n  // only the throw path stops here\n}",
        outcome="Silent `1 / 0` is **Infinity** (no throw). The explicit throw is **Error**: **division produced Infinity**.",
        script="""      let silent = 1 / 0;
      let thrown;
      try {
        let x = 1 / 0;
        if (!Number.isFinite(x)) throw new Error("division produced Infinity");
      } catch (e) {
        thrown = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "silent 1 / 0 -> " + String(silent) + "\\n" +
        "with throw -> " + thrown;""",
    ),
    S(
        "assignment-not-comparison",
        "if (isActive = true) — assignment, not comparison",
        [
            "`=` **assigns**. `isActive = true` sets the flag to **true** and the `if` condition is **true**.",
            "The Tryit then sets `result = \"Active!\"`. **No exception** — a logic bug.",
            "The `===` path with `isActive` still **false** does not enter; a **`throw`** makes that miss loud.",
        ],
        'let result = "Not Active.";\nlet isActive = false;\nif (isActive = true) {   // assignment, not comparison\n  result = "Active!";\n}',
        outcome='Silent path: result is **"Active!"** and `isActive` is **true** (no throw). '
        'With `===` and `throw`, `isActive` stays **false** and the catch is **Error**: **not active**.',
        script="""      let result = "Not Active.";
      let isActive = false;
      if (isActive = true) {
        result = "Active!";
      }
      let isActive2 = false;
      let thrown;
      try {
        if (isActive2 === true) {
          thrown = "entered";
        } else {
          throw new Error("not active");
        }
      } catch (e) {
        thrown = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "silent result -> " + result + "\\n" +
        "silent isActive -> " + isActive + "\\n" +
        "=== then throw -> " + thrown;""",
    ),
    S(
        "parseint-nan",
        "parseInt('abc') is NaN — silent vs throw",
        [
            "Many numeric failures produce **`NaN`**, not an exception.",
            "`parseInt(\"abc\")` is **NaN**. The program **keeps going**.",
            "`Number.isNaN` + **`throw`** turns that into a real error.",
        ],
        'const result = parseInt("abc");\n// NaN - no error, just wrong data',
        outcome='Silent result is **NaN**. The throw path is **Error**: **parseInt produced NaN**.',
        script="""      const silent = parseInt("abc");
      let thrown;
      try {
        const result = parseInt("abc");
        if (Number.isNaN(result)) throw new Error("parseInt produced NaN");
      } catch (e) {
        thrown = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "silent parseInt(\\"abc\\") -> " + String(silent) + "\\n" +
        "Number.isNaN(silent) -> " + Number.isNaN(silent) + "\\n" +
        "with throw -> " + thrown;""",
    ),
    S(
        "missing-property-undefined",
        "user.name on {} is undefined — silent vs throw",
        [
            "Reading a **missing property** returns **`undefined`**. No throw.",
            "That is easy to miss. Check and **`throw`** if the property is required.",
        ],
        "const user = {};\nlet result = user.name;",
        outcome="Silent `user.name` is **undefined**. The throw path is **Error**: **missing name**.",
        script="""      const user = {};
      let silent = user.name;
      let thrown;
      try {
        if (user.name === undefined) throw new Error("missing name");
      } catch (e) {
        thrown = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "silent user.name -> " + String(silent) + "\\n" +
        "with throw -> " + thrown;""",
    ),
    S(
        "plus-vs-minus-coercion",
        "'5' + '2' vs '5' - '2' — silent coercion",
        [
            "JavaScript **coerces** instead of throwing when types look numeric/stringy.",
            "`'5' + '2'` concatenates to **`\"52\"`**. `'5' - '2'` subtracts to **3**.",
            "A **`throw`** if `typeof` differs makes mixed-type `+` loud.",
        ],
        "let result1 = ('5' + '2');  // 52\nlet result2 = ('5' - '2');  // 3",
        outcome='Silent: result1 is **"52"** (string); result2 is **3** (number). '
        'Throw-if-types-differ on `"5" + 2` is **TypeError**: **mixed types in +**.',
        script="""      let result1 = ("5" + "2");
      let result2 = ("5" - "2");
      let thrown;
      try {
        const a = "5";
        const b = 2;
        if (typeof a !== typeof b) throw new TypeError("mixed types in +");
      } catch (e) {
        thrown = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "'5' + '2' -> " + result1 + " (typeof " + typeof result1 + ")\\n" +
        "'5' - '2' -> " + result2 + " (typeof " + typeof result2 + ")\\n" +
        '"5" + 2 with throw -> ' + thrown;""",
    ),
    S(
        "string-coercion-plus",
        'String coercion: "5" + 2 is "52"',
        [
            "If **any** operand of **`+`** is a string, JavaScript converts the other to a **string**.",
            '`"5" + 2` is **`"52"`**, not **7**. No throw.',
        ],
        'let x = "5" + 2;  // x = "52"',
        outcome='x is **"52"** (`typeof` **string**). `Number("5") + 2` is **7**.',
        script=out_script(
            'let x = "5" + 2;\nlet y = Number("5") + 2;',
            [("x", "x"), ("typeof x", "typeof x"), ("Number(\"5\") + 2", "y")],
        ),
    ),
    S(
        "numeric-coercion-minus",
        'Numeric coercion: "5" - 2 is 3',
        [
            "**`-` `*` `/` `%`** and unary **`+x`** force values to **numbers**.",
            '`"5" - 2` is **3**. `"abc" - 1` is **NaN** (still no throw).',
        ],
        'let x = "5" - 2;  // x = 3',
        outcome='`"5" - 2` is **3**. `"abc" - 1` is **NaN** — silent, not a TypeError.',
        script=out_script(
            'let x = "5" - 2;\nlet y = "abc" - 1;',
            [("x", "x"), ("typeof x", "typeof x"), ('"abc" - 1', "y"), ("Number.isNaN(y)", "Number.isNaN(y)")],
        ),
    ),
    S(
        "loose-equality",
        "Loose equality: 5 == '5' is true",
        [
            "**`==`** coerces to a common type. **`===`** does not.",
            '`5 == "5"` is **true**. `5 === "5"` is **false**. Prefer **`===`**.',
        ],
        'let x = (5 == "5");  // x = true',
        outcome='`5 == "5"` is **true**. `5 === "5"` is **false**. Throw-if-types-differ is **TypeError**: **loose compare mixed types**.',
        script="""      let loose = (5 == "5");
      let strictEq = (5 === "5");
      let thrown;
      try {
        const a = 5;
        const b = "5";
        if (typeof a !== typeof b) throw new TypeError("loose compare mixed types");
      } catch (e) {
        thrown = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        '5 == "5" -> ' + loose + "\\n" +
        '5 === "5" -> ' + strictEq + "\\n" +
        "with throw -> " + thrown;""",
    ),
]


# ---------------------------------------------------------------------------
# 18.3 JS Error Statements
# ---------------------------------------------------------------------------

STATEMENTS = [
    S(
        "try-syntax",
        "try block — code that might throw",
        [
            "The **`try`** block contains code that **might** throw.",
            "If nothing throws, **`catch` is skipped**.",
        ],
        "try {\n  // Code that may cause an error\n  let x = 1 + 1;\n} catch (error) {\n  // Code to handle the error\n}",
        outcome="`1 + 1` is **2**. Catch did **not** run.",
        script="""      let x;
      let caught = false;
      try {
        x = 1 + 1;
      } catch (error) {
        caught = true;
      }
      document.getElementById("demo").innerText =
        "x -> " + x + "\\n" +
        "catch ran -> " + caught;""",
    ),
    S(
        "catch-syntax",
        "catch block — handles the thrown value",
        [
            "**`catch`** runs **only** if `try` throws.",
            "For built-in errors the parameter is an **Error** object (`name`, `message`).",
        ],
        "try {\n  // Code that may cause an error\n  missing();\n} catch (error) {\n  // Code to handle the error\n}",
        outcome="**ReferenceError**: **missing is not defined**. Catch ran.",
        script=nm_script("missing();"),
    ),
    S(
        "finally-syntax",
        "finally — always runs, error or not",
        [
            "**`finally`** runs after `try` / `catch` **whether or not** an error occurred.",
            "Use it for **cleanup** (clear a field, hide a loader).",
        ],
        "try {\n  // Code that may cause an error\n} catch (error) {\n  // Code to handle the error\n} finally {\n  // Code that always runs, no matter what\n}",
        outcome="Success path: finally **yes**, catch **no**. Error path: catch **yes**, finally **yes**.",
        script="""      let ok = [];
      try {
        ok.push("try");
      } catch (error) {
        ok.push("catch");
      } finally {
        ok.push("finally");
      }
      let bad = [];
      try {
        missingFinallyDemo();
        bad.push("try-after");
      } catch (error) {
        bad.push("catch:" + error.name);
      } finally {
        bad.push("finally");
      }
      document.getElementById("demo").innerText =
        "no error -> " + ok.join(" | ") + "\\n" +
        "with error -> " + bad.join(" | ");""",
    ),
    S(
        "throw-string",
        'throw "Too big" — throw a text',
        [
            "**`throw`** creates a **custom** exception. It can be a **String**, **Number**, **Boolean**, or **Object**.",
            "A thrown string is **not** an Error object — `err.name` is **undefined**; `String(err)` is the text.",
        ],
        'throw "Too big";  // throw a text',
        outcome='Catch receives the string **"Too big"**. `err.name` is not an Error name (`(not an Error object)`).',
        script=nm_script('throw "Too big";'),
    ),
    S(
        "throw-number",
        "throw 500 — throw a number",
        [
            "You can **`throw` a number**. Same rule: it is **not** `{name, message}`.",
            "`String(err)` is **`\"500\"`**.",
        ],
        "throw 500;  // throw a number",
        outcome="Catch receives **500**. `String(err)` is **500** — not `Error: 500`.",
        script=nm_script("throw 500;"),
    ),
    S(
        "input-validation-throw",
        "Input validation — throw empty / not a number / too low / too high",
        [
            "Together, **`throw` + `try` + `catch`** control flow and show a **custom** message.",
            "This sandbox runs the Tryit function against several values (no clicking required).",
        ],
        'function myFunction(x) {\n  const message = { innerHTML: "" };\n  try {\n    if (x.trim() == "") throw "empty";\n    if (isNaN(x)) throw "not a number";\n    x = Number(x);\n    if (x < 5) throw "too low";\n    if (x > 10) throw "too high";\n  } catch (err) {\n    message.innerHTML = "Input is " + err;\n  }\n  return message.innerHTML;\n}',
        outcome='`""` → **Input is empty**. `"hello"` → **Input is not a number**. `"3"` → **Input is too low**. '
        '`"12"` → **Input is too high**. `"7"` → blank (valid; catch skipped).',
        script="""      function myFunction(raw) {
        const message = { innerHTML: "" };
        let x = raw;
        try {
          if (x.trim() == "") throw "empty";
          if (isNaN(x)) throw "not a number";
          x = Number(x);
          if (x < 5) throw "too low";
          if (x > 10) throw "too high";
        } catch (err) {
          message.innerHTML = "Input is " + err;
        }
        return message.innerHTML === "" ? "(blank — valid)" : message.innerHTML;
      }
      const samples = ["", "hello", "3", "12", "7"];
      document.getElementById("demo").innerText = samples.map(function (s) {
        return JSON.stringify(s) + " -> " + myFunction(s);
      }).join("\\n");""",
    ),
    S(
        "html-validation",
        "HTML validation — input type=number min=5 max=10",
        [
            "Modern browsers can validate with **HTML attributes** (`type`, `min`, `max`, `step`) instead of `throw`.",
            "`checkValidity()` is **true/false** — it does **not** throw a JavaScript Error.",
        ],
        '<input id="demo" type="number" min="5" max="10" step="1">',
        outcome='`3` is **invalid** (`rangeUnderflow`). `7` is **valid**. `11` is **invalid** (`rangeOverflow`). No JS **throw**.',
        script="""      function check(v) {
        const el = document.createElement("input");
        el.type = "number";
        el.min = "5";
        el.max = "10";
        el.step = "1";
        el.value = v;
        return "value=" + v +
          " checkValidity=" + el.checkValidity() +
          " validity.rangeUnderflow=" + el.validity.rangeUnderflow +
          " validity.rangeOverflow=" + el.validity.rangeOverflow;
      }
      document.getElementById("demo").innerText =
        check("3") + "\\n" + check("7") + "\\n" + check("11");""",
        body="<p>Native HTML constraint validation (not a JS throw):</p>",
    ),
    S(
        "finally-clears-input",
        "finally example — always clears the input",
        [
            "After `try` / `catch`, **`finally`** still runs.",
            "The Tryit **clears** the input field in `finally`, including on a **valid** value.",
        ],
        'function myFunction() {\n  const message = document.getElementById("p01");\n  message.innerHTML = "";\n  let x = document.getElementById("demo").value;\n  try {\n    if (x.trim() == "") throw "is empty";\n    if (isNaN(x)) throw "is not a number";\n    x = Number(x);\n    if (x > 10) throw "is too high";\n    if (x < 5) throw "is too low";\n  } catch (err) {\n    message.innerHTML = "Input " + err;\n  } finally {\n    document.getElementById("demo").value = "";\n  }\n}',
        outcome='`"3"` → **Input is too low** and field **cleared**. `"7"` → no error message, field **still cleared**.',
        script="""      function run(raw) {
        let msg = "";
        let field = raw;
        try {
          let x = field;
          if (x.trim() == "") throw "is empty";
          if (isNaN(x)) throw "is not a number";
          x = Number(x);
          if (x > 10) throw "is too high";
          if (x < 5) throw "is too low";
        } catch (err) {
          msg = "Input " + err;
        } finally {
          field = "";
        }
        return JSON.stringify(raw) + " -> message=" +
          (msg === "" ? "(blank)" : msg) +
          " fieldAfter=" + JSON.stringify(field);
      }
      document.getElementById("demo").innerText =
        run("") + "\\n" +
        run("hello") + "\\n" +
        run("3") + "\\n" +
        run("12") + "\\n" +
        run("7");""",
    ),
]


# ---------------------------------------------------------------------------
# 18.4 JS Error Object
# ---------------------------------------------------------------------------

OBJ = [
    S(
        "new-error",
        "new Error() — creates an Error object",
        [
            "`new Error()` builds a built-in **Error** object.",
            "With no message, **`message`** is **`\"\"`**. **`name`** is **`\"Error\"`**.",
        ],
        "const err = new Error();\nconst err2 = new Error(\"Something went wrong\");",
        outcome='`new Error()` → name **Error**, message **\"\"**. `new Error("Something went wrong")` → message **Something went wrong**.',
        script=out_script(
            'const err = new Error();\nconst err2 = new Error("Something went wrong");',
            [
                ("err.name", "err.name"),
                ("err.message", "JSON.stringify(err.message)"),
                ("err2.name", "err2.name"),
                ("err2.message", "err2.message"),
            ],
        ),
    ),
    S(
        "error-name",
        "name — sets or returns the error name",
        [
            "**`name`** is the error **kind** (`Error`, `TypeError`, `RangeError`, …).",
            "You can **read** it after `catch`, or **set** it on a custom Error.",
        ],
        'const err = new Error("boom");\nerr.name;\nerr.name = "MyError";',
        outcome='Default **`name`** is **"Error"**. After `err.name = "MyError"` it is **"MyError"** (message still **boom**).',
        script=out_script(
            'const err = new Error("boom");\nconst before = err.name;\nerr.name = "MyError";',
            [("before", "before"), ("after", "err.name"), ("message", "err.message")],
        ),
    ),
    S(
        "error-message",
        "message — sets or returns the error message",
        [
            "**`message`** is the human-readable description.",
            "Pass it to **`new Error(message)`**, or assign **`err.message`** later.",
        ],
        'const err = new Error("first");\nerr.message = "second";',
        outcome='Constructor message is **"first"**. After assign, **`err.message`** is **"second"**.',
        script=out_script(
            'const err = new Error("first");\nconst first = err.message;\nerr.message = "second";',
            [("first", "first"), ("after assign", "err.message")],
        ),
    ),
    S(
        "error-cause",
        "cause — sets or returns an error cause",
        [
            "**`cause`** chains the **underlying** error: `new Error(msg, { cause })`.",
            "Catch the inner error, wrap it, and still read **`err.cause`**.",
        ],
        'try {\n  throw new TypeError("inner");\n} catch (inner) {\n  throw new Error("outer", { cause: inner });\n}',
        outcome="Outer **Error**: **outer**. `err.cause` is **TypeError**: **inner**.",
        script="""      let name, message, causeName, causeMessage;
      try {
        try {
          throw new TypeError("inner");
        } catch (inner) {
          throw new Error("outer", { cause: inner });
        }
      } catch (e) {
        name = e.name;
        message = e.message;
        causeName = e.cause && e.cause.name;
        causeMessage = e.cause && e.cause.message;
      }
      document.getElementById("demo").innerText =
        "err.name -> " + name + "\\n" +
        "err.message -> " + message + "\\n" +
        "err.cause.name -> " + causeName + "\\n" +
        "err.cause.message -> " + causeMessage;""",
    ),
    S(
        "error-is-error",
        "Error.isError(x) — true only for real Error objects",
        [
            "**`Error.isError(x)`** is **true** if `x` is an Error (including TypeError, …).",
            "A plain `{ name: \"Error\" }` object is **false** — it only looks like one.",
        ],
        'Error.isError(new Error("x"));\nError.isError({ name: "Error", message: "x" });',
        outcome="**Error.isError** is a **function**. `new Error(\"x\")` → **true**. `{name:\"Error\", message:\"x\"}` → **false**.",
        script=out_script(
            'const real = new Error("x");\nconst fake = { name: "Error", message: "x" };',
            [
                ("typeof Error.isError", "typeof Error.isError"),
                ('Error.isError(new Error("x"))', "Error.isError(real)"),
                ("Error.isError(plain object)", "Error.isError(fake)"),
                ("Error.isError(null)", "Error.isError(null)"),
            ],
        ),
    ),
    S(
        "evalerror-name",
        "EvalError — deprecated name; use SyntaxError",
        [
            "Six values for **`name`**: EvalError, RangeError, ReferenceError, SyntaxError, TypeError, URIError.",
            "**EvalError is deprecated** — do not expect `eval()` to throw it.",
        ],
        'const e = new EvalError("legacy");\ntry {\n  eval("alert(\'Hello)");\n} catch (err) {\n  // SyntaxError\n}',
        outcome="`new EvalError` has name **EvalError**. `eval(\"alert('Hello)\")` throws **SyntaxError**: **Invalid or unexpected token**.",
        script="""      const e = new EvalError("legacy");
      let evalMsg;
      try {
        eval("alert('Hello)");
        evalMsg = "eval ran";
      } catch (err) {
        evalMsg = err.name + ": " + err.message;
      }
      document.getElementById("demo").innerText =
        "EvalError name -> " + e.name + "\\n" +
        "EvalError message -> " + e.message + "\\n" +
        "eval broken string -> " + evalMsg;""",
    ),
    S(
        "rangeerror-name",
        "RangeError — a number out of range",
        [
            "**RangeError**: a number is **out of range**.",
            "The page Tryit uses **`toPrecision(500)`**.",
        ],
        "let num = 1;\ntry {\n  num.toPrecision(500);\n} catch (err) {\n  let text = err.name + \"\\n\" + err.message;\n}",
        outcome="**RangeError**: **toPrecision() argument must be between 1 and 100**.",
        script=nm_script("let num = 1;\nnum.toPrecision(500);"),
    ),
    S(
        "referenceerror-name",
        "ReferenceError — an illegal reference",
        [
            "**ReferenceError**: an **illegal reference** (the page Tryit link is the undeclared-variable demo).",
            "`x = y + 1` when `y` was never declared.",
        ],
        "let x = 5;\ntry {\n  x = y + 1;\n} catch (err) {\n  let text = err.name + \"\\n\" + err.message;\n}",
        outcome="**ReferenceError**: **y is not defined**.",
        script=nm_script("let x = 5;\nx = y + 1;"),
    ),
    S(
        "syntaxerror-name",
        "SyntaxError — eval of invalid source",
        [
            "**SyntaxError**: the source is not valid JavaScript.",
            "The page Tryit uses **`eval(\"alert('Hello)\")`** so the error is **runtime-catchable** (eval parses later).",
            "A raw unclosed string in a `<script>` would **not** be catchable — see JS Errors Intro.",
        ],
        'try {\n  eval("alert(\'Hello)");\n} catch (err) {\n  let text = err.name + "\\n" + err.message;\n}',
        outcome="**SyntaxError**: **Invalid or unexpected token** (caught from `eval`, not from a parse-time script).",
        script=nm_script('eval("alert(\'Hello)");'),
    ),
    S(
        "typeerror-name",
        "TypeError — wrong type for the operation",
        [
            "**TypeError**: a value is the **wrong type**.",
            "The page Tryit is **`num.toUpperCase()`** on the number **1**.",
        ],
        "let num = 1;\ntry {\n  num.toUpperCase();\n} catch (err) {\n  let text = err.name + \"\\n\" + err.message;\n}",
        outcome="**TypeError**: **num.toUpperCase is not a function**.",
        script=nm_script("let num = 1;\nnum.toUpperCase();"),
    ),
    S(
        "urierror-name",
        "URIError — decodeURI / encodeURI malformed",
        [
            "**URIError**: illegal characters in a **URI** function (`decodeURI`, `encodeURI`, …).",
            "The Tryit is **`decodeURI(\"%%%\")`**. The table text also mentions **`encodeURI()`**.",
        ],
        'try {\n  decodeURI("%%%");\n} catch (err) {\n  let text = err.name + "\\n" + err.message;\n}',
        outcome="**URIError**: **URI malformed** for `decodeURI(\"%%%\")`. "
        "`encodeURI` of an unpaired surrogate is also **URIError**: **URI malformed**.",
        script="""      let dName, dMsg, eName, eMsg;
      try {
        decodeURI("%%%");
      } catch (e) {
        dName = e.name;
        dMsg = e.message;
      }
      try {
        encodeURI("\\uD800");
      } catch (e) {
        eName = e.name;
        eMsg = e.message;
      }
      document.getElementById("demo").innerText =
        "decodeURI(\\"%%%\\") -> " + dName + ": " + dMsg + "\\n" +
        "encodeURI(unpaired surrogate) -> " + eName + ": " + eMsg;""",
    ),
]


def run_all() -> None:
    sections = [
        (
            "js-errors-intro",
            "JS Errors Intro",
            INTRO,
            "When JavaScript runs, errors happen: programmer mistakes, bad input, and surprises. This page names the built-in kinds — ReferenceError, TypeError, RangeError, URIError, SyntaxError, and the deprecated EvalError — and introduces try/catch. Runtime errors can be caught. Syntax errors are thrown while the engine is still parsing, so a raw script never starts and try/catch on the same page cannot help. This sandbox uses new Function only so those parse errors can be shown without blanking the page.",
            [
                "**`try` / `catch`** come in pairs. `try` tests a block; `catch` runs only if that block throws.",
                "**ReferenceError** — missing name, or **TDZ** (`Cannot access 'y' before initialization`).",
                "**TypeError** — wrong type (`anna is not a function`, `num.toUpperCase is not a function`).",
                "**RangeError** — out of range (`Invalid array length`, `toPrecision() argument must be between 1 and 100`).",
                "**URIError** — `decodeURI(\"%%%\")` → **URI malformed**.",
                "**SyntaxError** is **not catchable** in the same `<script>`. Use **`new Function`** here to display it. `eval` of bad source **is** catchable (Error Object page).",
                "**EvalError** is **deprecated**. `eval(\"var = 1\")` throws **SyntaxError**, not EvalError.",
            ],
            [
                ("What does `try` do if nothing throws?", ["The **try** block finishes. **`catch` is skipped**.", "The demo status is **try ran**."]),
                ("What is `null.foo`?", ["**TypeError**: **Cannot read properties of null (reading 'foo')**.", "That is the dedicated **catch** demo (not the later TypeError Tryits)."]),
                ("What is `x = y + 1` when `y` was never declared?", ["**ReferenceError**: **y is not defined**."]),
                ("What is `let x = y; let y = 5`?", ["**ReferenceError**: **Cannot access 'y' before initialization** (TDZ).", "It is **not** “y is not defined.”"]),
                ("What is `anna(5)` if `anna` is `5`?", ["**TypeError**: **anna is not a function**."]),
                ("What is `(1).toUpperCase()`?", ["**TypeError**: **num.toUpperCase is not a function**."]),
                ("What is `new Array(-1)`?", ["**RangeError**: **Invalid array length**."]),
                ("What is `(1).toPrecision(500)`?", ["**RangeError**: **toPrecision() argument must be between 1 and 100**."]),
                ("What is `decodeURI(\"%%%\")`?", ["**URIError**: **URI malformed**."]),
                ("What is `let text = \"John Doe);`?", ["**SyntaxError**: **Invalid or unexpected token**.", "A raw script **does not parse**. This sandbox uses **`new Function`**."]),
                ("Can `try { Math.round(4.6;) }` catch the extra semicolon?", ["**No.** The **whole script** is a SyntaxError: **missing ) after argument list**.", "`try` never starts. `err.description` is **IE-only**; this engine has **`err.message`**."]),
                ("Does `eval(\"var = 1\")` throw EvalError?", ["**No.** **SyntaxError**: **Unexpected token '='**.", "`new EvalError` still exists; **`eval()` does not throw it** in this engine."]),
            ],
            "Catch runtime errors with try/catch. Read err.name and err.message. Syntax errors happen before the script runs — wrap demos in new Function if you need to display them. EvalError is a leftover name; bad eval source is SyntaxError.",
            [
                ("JS Errors Intro (W3Schools)", "https://www.w3schools.com/js/js_errors_intro.asp"),
                ("MDN: Error", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error"),
                ("MDN: try...catch", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch"),
                ("MDN: SyntaxError", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError"),
            ],
        ),
        (
            "js-errors-silent",
            "JS Errors Silent",
            SILENT,
            "JavaScript can fail without throwing. Execution continues: 1/0 is Infinity, parseInt('abc') is NaN, a missing property is undefined, and = inside if assigns instead of comparing. Type coercion hides more bugs: + concatenates if either side is a string, other arithmetic forces numbers, and == compares after converting types. These are historical silent failures — early JavaScript had no try/catch. Each Example shows the silent result and a throw you can add when you want a hard stop.",
            [
                "**Silent ≠ OK.** The program **keeps running** with **Infinity**, **NaN**, **undefined**, or the **wrong branch**.",
                "`1 / 0` is **Infinity**, not a throw. `parseInt(\"abc\")` is **NaN**.",
                "`if (isActive = true)` **assigns** and enters the block. The Tryit result is **Active!**.",
                "`user.name` on `{}` is **undefined**, not ReferenceError (that would be a bare `name`).",
                "**`+`** with a string concatenates. **`-` `*` `/`** coerce to numbers. **`==`** coerces; **`===`** does not.",
                "To stop execution you **`throw`** after an explicit check (`Number.isFinite`, `Number.isNaN`, `===`).",
            ],
            [
                ("Does `1 / 0` throw?", ["**No.** It is **Infinity**.", "A follow-up `throw new Error(\"division produced Infinity\")` is **Error**: **division produced Infinity**."]),
                ("What does `if (isActive = true)` do when `isActive` started false?", ["It **assigns true** and takes the branch.", "The Tryit sets result to **Active!** — no exception."]),
                ("How do you make the inactive path loud?", ["Use **`===`**. If it is still false, **`throw new Error(\"not active\")`** → **Error**: **not active**."]),
                ("What is `parseInt(\"abc\")`?", ["**NaN**. `Number.isNaN` is **true**. No throw.", "Optional throw: **Error**: **parseInt produced NaN**."]),
                ("What is `{}.name`?", ["**undefined** — missing property, **not** a ReferenceError.", "Optional throw: **Error**: **missing name**."]),
                ("What is `'5' + '2'` vs `'5' - '2'`?", ['**`"52"`** (string) vs **3** (number).']),
                ("What is `\"5\" + 2`?", ['**`"52"`** (`typeof` **string**). `Number("5") + 2` is **7**.']),
                ("What is `\"5\" - 2`?", ["**3**. `\"abc\" - 1` is **NaN**, still **no throw**."]),
                ("What is `5 == \"5\"` vs `5 === \"5\"`?", ["**true** vs **false**. Prefer **`===`**.", "Throw-if-types-differ: **TypeError**: **loose compare mixed types**."]),
                ("Why do silent errors exist?", ["Early JavaScript had **no try/catch**. Failures were designed **not** to stop the page."]),
                ("Does a silent error set `err.name`?", ["**No.** Nothing was thrown, so there is **no** Error object unless **you throw**."]),
            ],
            "Infinity, NaN, undefined, accidental assignment, and coercion all continue execution. Check explicitly and throw when a wrong value must stop the program. Prefer ===, Number(), and Number.isNaN / Number.isFinite over hoping the engine will yell.",
            [
                ("JS Errors Silent (W3Schools)", "https://www.w3schools.com/js/js_errors_silent.asp"),
                ("MDN: NaN", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN"),
                ("MDN: Equality comparisons", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness"),
                ("MDN: throw", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw"),
            ],
        ),
        (
            "js-error-statements",
            "JS Error Statements",
            STATEMENTS,
            "try tests a block, catch handles a throw, and finally always runs afterward. JavaScript normally stops and creates an Error with name and message; throw lets you raise a string, number, boolean, or object instead. The input-validation Tryit throws custom phrases (empty, not a number, too low, too high). HTML min/max on an input can reject values without any JavaScript throw. The finally Tryit clears the field even when the number was valid.",
            [
                "**`try`** — code that might throw. **`catch`** — only if it did. **`finally`** — **always** (cleanup).",
                "**`throw`** a String / Number / Boolean / Object. Thrown primitives are **not** Error objects (`name` is missing).",
                "Built-in throws **do** create `{ name, message }`.",
                "Validation Tryit messages: **Input is empty**, **not a number**, **too low**, **too high**. Valid **7** leaves the message **blank**.",
                "Finally Tryit: **Input is empty / is not a number / is too high / is too low**, then the **field is cleared**.",
                "HTML `type=\"number\" min=\"5\" max=\"10\"` uses **`checkValidity()`**, not `throw`.",
            ],
            [
                ("Does catch run after `try { 1 + 1 }`?", ["**No.** x is **2**. catch ran → **false**."]),
                ("What is `missing()`?", ["**ReferenceError**: **missing is not defined**."]),
                ("Does `finally` run when try succeeds?", ["**Yes.** Order: **try | finally**."]),
                ("Does `finally` run when try throws?", ["**Yes.** Order: **try, catch:ReferenceError | finally**."]),
                ("What is `throw \"Too big\"` in catch?", ["The string **Too big**. It is **not** an Error object."]),
                ("What is `throw 500` in catch?", ["The number **500**. `String(err)` is **500**."]),
                ("What does the validation Tryit print for `\"\"`, `\"hello\"`, `\"3\"`, `\"12\"`, `\"7\"`?", ["**Input is empty**.", "**Input is not a number**.", "**Input is too low**.", "**Input is too high**.", "**blank** (valid)."]),
                ("Does HTML `min`/`max` throw a JS Error?", ["**No.** `checkValidity()` is **false** for **3** (`rangeUnderflow`) and **11** (`rangeOverflow`), **true** for **7**."]),
                ("Does `finally` clear the input on a valid `7`?", ["**Yes.** Message stays **blank**; **fieldAfter** is **`\"\"`**."]),
                ("What is the finally message for `\"3\"`?", ["**Input is too low** (Tryit text is `\"Input \" + err`)."]),
                ("Can you `throw` a Boolean?", ["**Yes.** The page lists String, Number, Boolean, or Object. This section demos **string** and **number** as in the syntax lines."]),
            ],
            "Use try to protect code, catch to handle a throw, and finally to clean up. throw can be any value; only Error objects have name and message. The validation Tryits map empty / NaN / range into custom strings. HTML constraint validation is a separate, non-throwing path.",
            [
                ("JS Error Statements (W3Schools)", "https://www.w3schools.com/js/js_errors.asp"),
                ("MDN: try...catch", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch"),
                ("MDN: throw", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw"),
                ("MDN: Constraint validation", "https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation"),
            ],
        ),
        (
            "js-error-object",
            "JS Error Object",
            OBJ,
            "JavaScript’s built-in Error object carries name and message (and, in modern engines, cause). new Error() creates one. Error.isError(x) is true only for real Error instances, not look-alike objects. The name property is one of EvalError (deprecated), RangeError, ReferenceError, SyntaxError, TypeError, or URIError. The page Tryits catch those (SyntaxError via eval so it is runtime-catchable). Skip non-standard properties such as description, stack-as-API, and evalError().",
            [
                "**`new Error()`** / **`new Error(message)`**. **`name`** defaults to **Error**. **`message`** defaults to **`\"\"`**.",
                "**`cause`** wraps an inner error: `new Error(\"outer\", { cause: inner })`.",
                "**`Error.isError`**: **true** for `new Error`, **false** for `{ name: \"Error\" }` and **null**.",
                "**Six names:** EvalError (deprecated), RangeError, ReferenceError, SyntaxError, TypeError, URIError.",
                "Do **not** use **`err.description`** (Microsoft only) or the other non-standard rows.",
            ],
            [
                ("What is `new Error()` with no argument?", ["**name** **Error**, **message** **`\"\"`**."]),
                ("What is `new Error(\"Something went wrong\").message`?", ["**Something went wrong**."]),
                ("Can you assign `err.name = \"MyError\"`?", ["**Yes.** name becomes **MyError**; message stays **boom** in the demo."]),
                ("What is `cause` in `new Error(\"outer\", { cause: new TypeError(\"inner\") })`?", ["**err.cause.name** is **TypeError**. **err.cause.message** is **inner**."]),
                ("Is `{ name: \"Error\", message: \"x\" }` an Error?", ["**No.** `Error.isError(plain)` is **false**. `Error.isError(new Error(\"x\"))` is **true**.", "`Error.isError(null)` is **false**."]),
                ("Does `eval(\"alert('Hello)\")` throw EvalError?", ["**No.** **SyntaxError**: **Invalid or unexpected token**.", "`new EvalError(\"legacy\").name` is still **EvalError**."]),
                ("What is `num.toPrecision(500)`?", ["**RangeError**: **toPrecision() argument must be between 1 and 100**."]),
                ("What is `x = y + 1` with no `y`?", ["**ReferenceError**: **y is not defined**."]),
                ("Why can the SyntaxError Tryit use try/catch?", ["It uses **`eval(...)`**, which parses **at runtime**.", "A raw `let x = Math.round(4.6;)` in a script is **not** catchable."]),
                ("What is `(1).toUpperCase()`?", ["**TypeError**: **num.toUpperCase is not a function**."]),
                ("What is `decodeURI(\"%%%\")`?", ["**URIError**: **URI malformed**.", "`encodeURI` of an unpaired surrogate is the same **URIError**: **URI malformed**."]),
                ("Should you use `err.description`?", ["**No.** Microsoft-only / non-standard. Use **`err.message`**."]),
            ],
            "Create errors with new Error, read name and message, and chain with cause. Error.isError distinguishes real errors from plain objects. The six name values match the intro types; EvalError is only a constructor now. Catch eval SyntaxErrors at runtime; parse-time SyntaxErrors still need new Function if you want a demo page.",
            [
                ("JS Error Object (W3Schools)", "https://www.w3schools.com/js/js_error_object.asp"),
                ("MDN: Error", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error"),
                ("MDN: Error.isError", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/isError"),
                ("MDN: Error.cause", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause"),
            ],
        ),
    ]
    print("example counts:")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print(f"  {slug}: {len(recs)}")
        nqa = len(qa)
        if nqa < 8 or nqa > 15:
            raise SystemExit(f"{slug} Q&A count {nqa} not in 8-15")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print("building", slug, "examples", len(recs))
        build_and_snap(slug, title, recs, intro, concepts, qa, summary, refs)
        print("done", slug, "snaps", len(recs) * 2)


if __name__ == "__main__":
    run_all()
