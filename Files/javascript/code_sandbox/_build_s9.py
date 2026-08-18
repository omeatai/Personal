"""S9: JS Scope through JS Dates (not Date Formats)."""
from __future__ import annotations

import json

from _gen_lib import S, build_and_snap


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


# ---------------------------------------------------------------------------
# 9.1 JS Scope
# ---------------------------------------------------------------------------

SCOPE = [
    S(
        "three-scope-types",
        "Three types of scope",
        [
            "JavaScript has **global**, **function**, and **block** scope.",
            "Outside any function or `{ }`, `var` / `let` / `const` are all **global**.",
        ],
        "var x = 1;  // Global scope\nlet y = 2;  // Global scope\nconst z = 3;  // Global scope\nfunction show() {\n  return x + \", \" + y + \", \" + z;\n}",
        [("x", "x"), ("y", "y"), ("z", "z"), ("show()", "show()")],
        "x, y, and z are **1**, **2**, **3**. `show()` can read all three: **1, 2, 3**.",
    ),
    S(
        "global-let-carname",
        "Global let carName used inside a function",
        [
            "A variable declared **outside** a function is **global**.",
            "Functions on the same page can **read** that global.",
        ],
        'let carName = "Volvo";\nfunction myFunction() {\n  return carName;\n}',
        [("carName", "carName"), ("myFunction()", "myFunction()")],
        'Both the outer code and the function see **"Volvo"**.',
    ),
    S(
        "function-local-carname",
        "Function-local carName — outside is ReferenceError",
        [
            "A variable declared **inside** a function is **local** (function scope).",
            "Reading it **outside** throws **ReferenceError**.",
        ],
        '// code here can NOT use carName\nfunction myFunction() {\n  let carName = "Volvo";\n  return carName;  // code here CAN use carName\n}\n// code here can NOT use carName',
        outcome='Inside the function, carName is **"Volvo"**. Outside, reading it throws **ReferenceError**.',
        script="""      function myFunction() {
        let carName = "Volvo";
        return carName;
      }
      let inside = myFunction();
      let outside;
      try {
        outside = carName;
      } catch (e) {
        outside = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "inside myFunction -> " + inside + "\\n" +
        "outside -> " + outside;""",
    ),
    S(
        "block-let-x",
        "Block let x = 2 — outside is ReferenceError",
        [
            "`let` (and `const`) inside `{ }` have **block scope**.",
            "Outside the braces, `x` is not declared — **ReferenceError**.",
        ],
        "{\n  let x = 2;\n}\n// x can NOT be used here",
        outcome="Inside the block, x is **2**. Outside, reading x throws **ReferenceError**.",
        script="""      let inside;
      {
        let x = 2;
        inside = x;
      }
      let outside;
      try {
        outside = x;
      } catch (e) {
        outside = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "inside block -> " + inside + "\\n" +
        "outside -> " + outside;""",
    ),
    S(
        "block-var-x",
        "Block var x = 2 — still 2 outside (not recommended)",
        [
            "`var` does **not** have block scope.",
            "`var` inside `{ }` **leaks** and can be used after the block. Avoid this.",
        ],
        "{\n  var x = 2;\n}\n// x CAN be used here",
        [("x", "x")],
        "x is **2** outside the block. `var` in a block is **not recommended**.",
    ),
    S(
        "automatically-global",
        "Undeclared assignment is automatically global",
        [
            "In **sloppy** mode, assigning to a name that was never declared creates a **global**.",
            "In **strict mode**, undeclared assignment is **not** auto-global (see **JS Strict Mode**).",
        ],
        'myFunction();\n// code here can use carName\nfunction myFunction() {\n  carName = "Volvo";\n}',
        [("carName", "carName")],
        'After the call, outer code can use carName: **"Volvo"**. Do not rely on this.',
    ),
    S(
        "var-window-carname",
        "var carName belongs to window",
        [
            "In HTML, the global object is **`window`**.",
            "A global **`var`** becomes **`window.carName`**. Not recommended.",
        ],
        'var carName = "Volvo";\n// code here can use window.carName',
        outcome='`carName` and `window.carName` are both **"Volvo"**.',
        script="""      var carName = "Volvo";
      document.getElementById("demo").innerText =
        "carName -> " + carName + "\\n" +
        "window.carName -> " + window.carName;""",
    ),
    S(
        "let-window-carname",
        "let carName does not belong to window",
        [
            "A global **`let`** is **not** a property of `window`.",
            "`window.carName` is **undefined** even though `carName` holds Volvo.",
        ],
        'let carName = "Volvo";\n// code here can NOT use window.carName',
        outcome='`carName` is **"Volvo"**. `window.carName` is **undefined**.',
        script="""      let carName = "Volvo";
      document.getElementById("demo").innerText =
        "carName -> " + carName + "\\n" +
        "window.carName -> " + String(window.carName);""",
    ),
]


# ---------------------------------------------------------------------------
# 9.2 JS Code Blocks
# ---------------------------------------------------------------------------

BLOCKS = [
    S(
        "function-body-block",
        "Function body is a code block",
        [
            "A **code block** is statements inside curly braces `{ }`.",
            "A function **body** is always a block.",
        ],
        "function myFunction() {\n  // This is a code block\n  let a = 1;\n  let b = 2;\n  return a + b;\n}\nlet result = myFunction();",
        [("result", "result")],
        "The block runs when the function is called. result is **3**.",
    ),
    S(
        "if-else-blocks",
        "if / else blocks",
        [
            "`if` and `else` each take a **block** of statements.",
            "This demo runs a **true** branch and a **false** branch so both outputs show.",
        ],
        'function check(n) {\n  if (n > 5) {\n    return "if block: " + n + " is greater than 5";\n  } else {\n    return "else block: " + n + " is not greater than 5";\n  }\n}',
        [("check(10)", "check(10)"), ("check(3)", "check(3)")],
        '`check(10)` uses the **if** block; `check(3)` uses the **else** block.',
    ),
    S(
        "for-loop-block",
        "for loop block",
        [
            "The body of a **`for`** loop is a code block.",
            "`let i` in the loop head is **block-scoped** to that loop.",
        ],
        'let text = "";\nfor (let i = 0; i < 3; i++) {\n  text += i + " ";\n}',
        [("text", "text")],
        'text is **"0 1 2 "** after three iterations.',
    ),
    S(
        "while-loop-block",
        "while loop block",
        [
            "The body of a **`while`** loop is a code block.",
            "The loop repeats the block while the condition is true.",
        ],
        'let i = 0;\nlet text = "";\nwhile (i < 3) {\n  text += i + " ";\n  i++;\n}',
        [("text", "text"), ("i", "i")],
        'text is **"0 1 2 "**. i is **3** after the loop.',
    ),
    S(
        "block-let-not-outside",
        "{ let x = 10 } — x not accessible outside",
        [
            "`let` inside a block is visible **only in that block**.",
            "Outside, `x` throws **ReferenceError**.",
        ],
        "{\n  let x = 10;\n  // x is accessible here\n}\n// x is not accessible here",
        outcome="Inside, x is **10**. Outside, reading x throws **ReferenceError**.",
        script="""      let inside;
      {
        let x = 10;
        inside = x;
      }
      let outside;
      try {
        outside = x;
      } catch (e) {
        outside = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "inside block -> " + inside + "\\n" +
        "outside -> " + outside;""",
    ),
    S(
        "standalone-block-areal",
        "Standalone block: areal inside, ReferenceError outside",
        [
            "A **standalone** `{ }` is a block not tied to `if`, `for`, or a function.",
            "Use it to keep `let` / `const` **temporary** and off the global scope.",
        ],
        "{\n  let x = 10;\n  let y = 100;\n  let areal = x * y;\n}",
        outcome="Inside, **areal** is **1000**. Outside, `x`, `y`, and `areal` each throw **ReferenceError**.",
        script="""      let inside;
      {
        let x = 10;
        let y = 100;
        let areal = x * y;
        inside = areal;
      }
      let ox, oy, oa;
      try { ox = x; } catch (e) { ox = e.name + ": " + e.message; }
      try { oy = y; } catch (e) { oy = e.name + ": " + e.message; }
      try { oa = areal; } catch (e) { oa = e.name + ": " + e.message; }
      document.getElementById("demo").innerText =
        "areal inside -> " + inside + "\\n" +
        "x outside -> " + ox + "\\n" +
        "y outside -> " + oy + "\\n" +
        "areal outside -> " + oa;""",
    ),
]


# ---------------------------------------------------------------------------
# 9.3 JS Hoisting
# ---------------------------------------------------------------------------

HOISTING = [
    S(
        "assign-then-var",
        "x = 5 then var x — displays 5",
        [
            "**Hoisting** moves `var` **declarations** to the top of the scope.",
            "`x = 5` then `var x` behaves like `var x; x = 5`.",
        ],
        "x = 5;\nvar x;",
        [("x", "x")],
        "x is **5**. The declaration was hoisted; the assignment ran first in source order.",
    ),
    S(
        "var-then-assign",
        "var x then x = 5 — same result 5",
        [
            "Declaring first, then assigning, is the **readable** form of the same idea.",
            "Example 1 and Example 2 print the **same** value.",
        ],
        "var x;\nx = 5;",
        [("x", "x")],
        "x is **5** — same result as assigning before `var x`.",
    ),
    S(
        "let-tdz",
        "carName = Volvo then let carName — ReferenceError (TDZ)",
        [
            "`let` is hoisted but **not initialized**.",
            "Using it before the `let` line is the **temporal dead zone** → **ReferenceError**.",
        ],
        'carName = "Volvo";\nlet carName;',
        outcome='**ReferenceError** — cannot access `carName` before initialization (TDZ).',
        script="""      let early;
      try {
        carName = "Volvo";
      } catch (e) {
        early = e.name + ": " + e.message;
      }
      let carName;
      document.getElementById("demo").innerText =
        "before let carName -> " + early + "\\n" +
        "after let carName -> " + String(carName);""",
    ),
    S(
        "const-syntax-error",
        "carName = Volvo then const carName — SyntaxError",
        [
            "This snippet is a **parse-time SyntaxError**: `const` **must** have an initializer (`const carName;` is illegal).",
            "W3Schools says the page “will not run.” A `<script>` with this source **fails to parse**, so nothing on that page runs.",
            "If it were `const carName = \"Volvo\"` after an earlier use, the engine would throw **ReferenceError** (TDZ), like `let` — not SyntaxError.",
            "This sandbox compiles the snippet with **`new Function(...)`** at **runtime** so the error can be caught and shown.",
        ],
        'carName = "Volvo";\nconst carName;',
        outcome="**SyntaxError** (missing initializer in const declaration), caught via `new Function`. A raw script tag would not load.",
        script=nf_script("carName = 'Volvo'; const carName;"),
    ),
    S(
        "both-initialized",
        "var x = 5; var y = 7 — show 5 7",
        [
            "**Initializations** are **not** hoisted — only declarations.",
            "When both `var` lines run before you read them, you get both values.",
        ],
        'var x = 5;\nvar y = 7;\nlet text = x + " " + y;',
        [("text", "text")],
        'text is **"5 7"**.',
    ),
    S(
        "y-used-before-init",
        "use y before var y = 7 — y is undefined",
        [
            "`var y` is hoisted, so `y` **exists** before that line.",
            "The **`= 7`** is not hoisted, so `y` is **undefined** when first read.",
        ],
        'var x = 5;\nlet text = x + " " + y;\nvar y = 7;',
        [("text", "text"), ("y after", "y")],
        'text is **"5 undefined"**. After the init line, y is **7**.',
    ),
    S(
        "equivalent-var-y",
        "Equivalent: var y; display; y = 7",
        [
            "The previous example is the same as declaring `y` first, reading it, then assigning.",
            "Always **declare at the top** of the scope so hoisting cannot surprise you.",
        ],
        'var x = 5;\nvar y;\nlet text = x + " " + y;\ny = 7;',
        [("text", "text"), ("y after assign", "y")],
        'text is **"5 undefined"**, then y becomes **7**. Same as Example 6.',
    ),
]


# The let-tdz script above is wrong: catch_script runs the expr, THEN I append `let carName`
# but catch_script already closed with innerText assignment. Also `carName = "Volvo"` in
# the attempt happens BEFORE `let carName` is in the generated script... wait.
# catch_script with setup="" and then I concatenate `let carName` AFTER the innerText line.
# That means `carName = "Volvo"` runs in a script that has `let carName` LATER.
# In JS, `let carName` is hoisted to the top of the script, so the assignment is in the TDZ.
# BUT I appended after innerText, so the full script is:
#   let r0; try { r0 = (carName = "Volvo"); } catch ...
#   document.getElementById("demo").innerText = ...
#   let carName;
#   document.getElementById("demo").innerText += ...
# Yes, `let carName` is in the same script scope, hoisted, TDZ applies. Good.
#
# However catch_script already sets innerText, then I += after let carName.
# After `let carName` without init, carName is undefined. That's a nice extra line.
# This should work. Keep it.

# ---------------------------------------------------------------------------
# 9.4 JS var / let / const
# ---------------------------------------------------------------------------

VARLET = [
    S(
        "var-leak-vs-let-block",
        "Table demo: var leaks, let does not",
        [
            "The comparison table: **`var`** is function/global scoped; **`let` / `const`** are **block** scoped.",
            "`typeof` of an undeclared name is **`\"undefined\"`** (no throw). That is how the Tryit tests `lastName`.",
        ],
        'if (true) {\n  var firstName = "John";\n  let lastName = "Doe";\n}\nlet text1 = text2 = "unknown";\nif (typeof firstName !== "undefined") text1 = firstName;\nif (typeof lastName !== "undefined") text2 = lastName;',
        [
            ("text1", "text1"),
            ("text2", "text2"),
            ("typeof firstName", "typeof firstName"),
            ("typeof lastName", "typeof lastName"),
        ],
        'text1 is **"John"** (var leaked). text2 stays **"unknown"** (let stayed in the `if` block).',
    ),
    S(
        "const-object-mutate",
        "const object: mutate property vs reassign",
        [
            "`const` prevents **reassigning** the binding, not changing **object properties**.",
            "`user.name = \"Bob\"` works. `user = { ... }` throws **TypeError**.",
        ],
        'const user = { name: "Alice" };\nuser.name = "Bob";\ntry {\n  user = { name: "Charlie" };\n} catch (err) {\n  // TypeError\n}',
        outcome='After mutate, `user.name` is **"Bob"**. Replacing `user` throws **TypeError**.',
        script="""      const user = { name: "Alice" };
      user.name = "Bob";
      let afterMutate = user.name;
      let afterReplace;
      try {
        user = { name: "Charlie" };
        afterReplace = user.name;
      } catch (e) {
        afterReplace = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "user.name after mutate -> " + afterMutate + "\\n" +
        "user = { name: \\"Charlie\\" } -> " + afterReplace;""",
    ),
    S(
        "var-redeclare",
        "var redeclare is allowed",
        [
            "`var` can be **redeclared** in the same scope and silently overwrites.",
            "This is a common source of bugs. Prefer `let` / `const`.",
        ],
        'var x = 1;\nvar x = 2;',
        [("x", "x")],
        "x is **2**. The second `var x` replaced the first.",
    ),
    S(
        "let-redeclare-syntax",
        "let redeclare same scope — SyntaxError",
        [
            "`let` **cannot** be redeclared in the same scope.",
            "That is a **parse-time SyntaxError**, so this demo uses `new Function`.",
        ],
        "let x = 1;\nlet x = 2;",
        outcome="**SyntaxError** — Identifier `x` has already been declared.",
        script=nf_script("let x = 1; let x = 2;"),
    ),
    S(
        "const-no-reassign",
        "const cannot reassign — TypeError",
        [
            "`const` bindings are **read-only** after init.",
            "Assigning a new value throws **TypeError** (runtime, so try/catch works).",
        ],
        "const PI = 3.14;\nPI = 3.14159;",
        outcome="**TypeError** — Assignment to constant variable. PI stays **3.14**.",
        script="""      const PI = 3.14;
      let msg;
      try {
        PI = 3.14159;
        msg = "PI -> " + PI;
      } catch (e) {
        msg = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "PI -> " + PI + "\\n" +
        "PI = 3.14159 -> " + msg;""",
    ),
    S(
        "var-hoisted-undefined",
        "var used before declare is undefined",
        [
            "`var` is hoisted and initialized as **undefined**.",
            "You can read it before the `var` line without a ReferenceError.",
        ],
        "let shown = x;\nvar x = 5;",
        [("shown", "shown"), ("x after", "x")],
        "shown is **undefined**. After the init line, x is **5**.",
    ),
    S(
        "let-tdz-before-declare",
        "let TDZ — ReferenceError before declare",
        [
            "`let` is hoisted but **uninitialized** until its line.",
            "Reading it in the TDZ throws **ReferenceError**.",
        ],
        "x = x + 1;  // error\nlet x = 5;",
        outcome="**ReferenceError** before `let x = 5`. After the line, x is **5**.",
        script="""      let early;
      try {
        x = x + 1;
      } catch (e) {
        early = e.name + ": " + e.message;
      }
      let x = 5;
      document.getElementById("demo").innerText =
        "before let x -> " + early + "\\n" +
        "after let x -> " + x;""",
    ),
    S(
        "const-tdz-before-declare",
        "const TDZ — ReferenceError before declare",
        [
            "`const` is also hoisted and uninitialized (TDZ), same as `let`.",
            "This uses `const x = 5` **with** an initializer — unlike the hoisting page’s `const carName;` (SyntaxError).",
        ],
        "console.log(x);  // error\nconst x = 5;",
        outcome="**ReferenceError** before `const x = 5`. After the line, x is **5**.",
        script="""      let early;
      try {
        early = x;
      } catch (e) {
        early = e.name + ": " + e.message;
      }
      const x = 5;
      document.getElementById("demo").innerText =
        "before const x -> " + early + "\\n" +
        "after const x -> " + x;""",
    ),
    S(
        "const-by-default",
        "Best practice: const by default",
        [
            "Use **`const`** unless you know the binding will change.",
            "Use **`let`** for a counter (or other reassignment). Avoid **`var`**.",
        ],
        "const MAX = 100;\nlet count = 0;\ncount = count + 1;",
        [("MAX", "MAX"), ("count", "count")],
        "MAX stays **100**. count is reassigned to **1**.",
    ),
]


# ---------------------------------------------------------------------------
# 9.5 JS Strict Mode
# ---------------------------------------------------------------------------

STRICT = [
    S(
        "undeclared-x",
        '"use strict"; x = 3.14 — undeclared variable',
        [
            '`"use strict";` at the **start of the script** enables strict mode for this whole file.',
            "Assigning to an **undeclared** name throws **ReferenceError** (no auto-global).",
            "The later “Not Allowed” Tryit is the **same** snippet — included once.",
        ],
        '"use strict";\nx = 3.14;',
        outcome="**ReferenceError** (x is not defined). Strict mode does not create a global `x`.",
        script=catch_script("", [("x = 3.14", "(x = 3.14)")], strict=True),
    ),
    S(
        "global-strict-in-function",
        "Global strict: undeclared y inside a function",
        [
            "Global strict mode applies **inside functions** in the same script too.",
            "`y = 3.14` in `myFunction` still throws **ReferenceError**.",
        ],
        '"use strict";\nmyFunction();\nfunction myFunction() {\n  y = 3.14;\n}',
        outcome="Calling `myFunction()` throws **ReferenceError** because `y` is not declared.",
        script="""      "use strict";
      function myFunction() {
        y = 3.14;
      }
      let msg;
      try {
        myFunction();
        msg = "y -> " + y;
      } catch (e) {
        msg = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText = msg;""",
    ),
    S(
        "local-strict-only",
        "Local strict in a function; outer assignment OK",
        [
            '`"use strict";` **inside a function** is local — only that function is strict.',
            "This sandbox script is **not** globally strict, so outer `x = 3.14` is allowed.",
        ],
        'x = 3.14;\nmyFunction();\nfunction myFunction() {\n  "use strict";\n  y = 3.14;\n}',
        outcome="Outer `x` is **3.14**. Inner `y = 3.14` throws **ReferenceError**.",
        script="""      x = 3.14;
      function myFunction() {
        "use strict";
        y = 3.14;
      }
      let inner;
      try {
        myFunction();
        inner = "y -> " + y;
      } catch (e) {
        inner = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "outer x -> " + x + "\\n" +
        "inner y = 3.14 -> " + inner;""",
    ),
    S(
        "undeclared-object",
        "Undeclared object x = {p1, p2}",
        [
            "Objects are values assigned to variables — they still need a **declaration**.",
            "In strict mode, `x = { ... }` without `let`/`var`/`const` throws **ReferenceError**.",
        ],
        '"use strict";\nx = {p1: 10, p2: 20};',
        outcome="**ReferenceError** — undeclared `x` (same rule as a number).",
        script=catch_script("", [("x = {p1:10, p2:20}", "(x = {p1:10, p2:20})")], strict=True),
    ),
    S(
        "delete-variable",
        "delete x (let x) — not allowed",
        [
            "`delete` on a **variable** (unqualified identifier) is a **SyntaxError** in strict mode.",
            "Caught with `new Function` so this page can still render.",
        ],
        '"use strict";\nlet x = 3.14;\ndelete x;',
        outcome="**SyntaxError** — applying `delete` to an unqualified identifier.",
        script=nf_script('"use strict"; let x = 3.14; delete x;'),
    ),
    S(
        "delete-function",
        "delete function — not allowed",
        [
            "Deleting a **function declaration** is also a strict **SyntaxError**.",
        ],
        '"use strict";\nfunction x(p1, p2) {}\ndelete x;',
        outcome="**SyntaxError** — cannot `delete` the function name `x`.",
        script=nf_script('"use strict"; function x(p1, p2) {}; delete x;'),
    ),
    S(
        "duplicate-params",
        "Duplicate parameter names — SyntaxError",
        [
            "Strict mode forbids **two parameters with the same name**.",
            "Parse-time **SyntaxError** via `new Function`.",
        ],
        '"use strict";\nfunction x(p1, p1) {}',
        outcome="**SyntaxError** — duplicate parameter name `p1`.",
        script=nf_script('"use strict"; function x(p1, p1) {}'),
    ),
    S(
        "octal-literal",
        "Octal literal 010 — SyntaxError",
        [
            "Legacy octal `010` (leading zero) is **forbidden** in strict mode.",
            "**SyntaxError** at parse time (`new Function`).",
        ],
        '"use strict";\nlet x = 010;',
        outcome="**SyntaxError** — octal literals are not allowed in strict mode.",
        script=nf_script('"use strict"; let x = 010;'),
    ),
    S(
        "octal-escape",
        r'Octal escape "\010"',
        [
            r"Octal escape sequences like `\010` are not allowed in strict mode.",
            "**SyntaxError** at parse time.",
        ],
        '"use strict";\nlet x = "\\010";',
        outcome=r"**SyntaxError** — octal escape `\010` in a string.",
        script=nf_script('"use strict"; let x = "\\010";'),
    ),
    S(
        "write-readonly",
        "Write a read-only defineProperty (writable: false)",
        [
            "In sloppy mode, writing a non-writable property **fails silently**.",
            "In strict mode it throws **TypeError**.",
        ],
        '"use strict";\nconst obj = {};\nObject.defineProperty(obj, "x", {value: 0, writable: false});\nobj.x = 3.14;',
        outcome="**TypeError** — cannot assign to read-only property `x`.",
        script="""      "use strict";
      const obj = {};
      Object.defineProperty(obj, "x", {value: 0, writable: false});
      let msg;
      try {
        obj.x = 3.14;
        msg = "obj.x -> " + obj.x;
      } catch (e) {
        msg = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "obj.x stays -> " + obj.x + "\\n" +
        "obj.x = 3.14 -> " + msg;""",
    ),
    S(
        "write-getter-only",
        "Write a getter-only property",
        [
            "An object with only a **getter** for `x` has no setter.",
            "Assigning `obj.x = 3.14` throws **TypeError** in strict mode.",
        ],
        '"use strict";\nconst obj = { get x() { return 0; } };\nobj.x = 3.14;',
        outcome="**TypeError** — property `x` has only a getter.",
        script="""      "use strict";
      const obj = { get x() { return 0; } };
      let msg;
      try {
        obj.x = 3.14;
        msg = "obj.x -> " + obj.x;
      } catch (e) {
        msg = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "obj.x getter -> " + obj.x + "\\n" +
        "obj.x = 3.14 -> " + msg;""",
    ),
    S(
        "delete-object-prototype",
        "delete Object.prototype",
        [
            "`Object.prototype` is **non-configurable**.",
            "`delete Object.prototype` throws **TypeError** in strict mode.",
        ],
        '"use strict";\ndelete Object.prototype;',
        outcome="**TypeError** — cannot delete undeletable `Object.prototype`.",
        script=catch_script("", [("delete Object.prototype", "delete Object.prototype")], strict=True),
    ),
    S(
        "let-eval",
        "let eval = 3.14",
        [
            "`eval` is a **reserved name** in strict mode — you cannot bind it.",
            "**SyntaxError** via `new Function`.",
        ],
        '"use strict";\nlet eval = 3.14;',
        outcome="**SyntaxError** — unexpected `eval` in strict mode.",
        script=nf_script('"use strict"; let eval = 3.14;'),
    ),
    S(
        "let-arguments",
        "let arguments = 3.14",
        [
            "`arguments` is also reserved as a binding name in strict mode.",
            "**SyntaxError** via `new Function`.",
        ],
        '"use strict";\nlet arguments = 3.14;',
        outcome="**SyntaxError** — unexpected `arguments` in strict mode.",
        script=nf_script('"use strict"; let arguments = 3.14;'),
    ),
    S(
        "with-statement",
        "with (Math) — SyntaxError",
        [
            "The **`with`** statement is forbidden in strict mode.",
            "**SyntaxError** via `new Function`.",
        ],
        '"use strict";\nwith (Math) {\n  x = cos(2);\n}',
        outcome="**SyntaxError** — strict mode code may not include a `with` statement.",
        script=nf_script('"use strict"; with (Math) { x = cos(2); }'),
    ),
    S(
        "eval-assign-x",
        'eval("x=2") then x — error',
        [
            "In strict mode, `eval` does **not** create a variable in the caller’s scope.",
            '`eval("x = 2")` is an undeclared assignment inside eval → **ReferenceError**.',
        ],
        '"use strict";\neval("x = 2");\n// x is not available here',
        outcome='**ReferenceError** — `x` is not created in this scope (and the eval assignment itself fails).',
        script="""      "use strict";
      let evalMsg;
      try {
        eval("x = 2");
        evalMsg = "eval ran";
      } catch (e) {
        evalMsg = e.name + ": " + e.message;
      }
      let readX;
      try {
        readX = x;
      } catch (e) {
        readX = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "eval(\\"x = 2\\") -> " + evalMsg + "\\n" +
        "x after eval -> " + readX;""",
    ),
    S(
        "eval-var-x",
        'eval("var x=2") then x — error in strict',
        [
            "Strict `eval` **does not leak** `var` into the surrounding scope.",
            "Reading `x` afterward is **ReferenceError**.",
        ],
        '"use strict";\neval("var x = 2");\n// x is not available here',
        outcome="**ReferenceError** when reading `x` after `eval(\"var x = 2\")` in strict mode.",
        script="""      "use strict";
      eval("var x = 2");
      let readX;
      try {
        readX = x;
      } catch (e) {
        readX = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "eval(\\"var x = 2\\") then x -> " + readX;""",
    ),
    S(
        "eval-let-x",
        'eval("let x=2") then x — error',
        [
            "`let` inside `eval` is scoped to the eval itself (the page Tryit does not even need use strict).",
            "Outer `x` is still **ReferenceError**.",
        ],
        'eval("let x = 2");\n// x is not available here',
        outcome="**ReferenceError** — `let` in eval does not create an outer `x`.",
        script="""      eval("let x = 2");
      let readX;
      try {
        readX = x;
      } catch (e) {
        readX = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "eval(\\"let x = 2\\") then x -> " + readX;""",
    ),
    S(
        "strict-this-undefined",
        "Strict function this is undefined",
        [
            "A **bare** function call in strict mode sets `this` to **undefined** (not `window`).",
            "In sloppy mode the same call would use the global object.",
        ],
        '"use strict";\nfunction myFunction() {\n  return this;\n}\nmyFunction();',
        outcome="`myFunction()` returns **undefined**. `this === undefined` is **true**.",
        script="""      "use strict";
      function myFunction() {
        return this;
      }
      let t = myFunction();
      document.getElementById("demo").innerText =
        "this -> " + String(t) + "\\n" +
        "this === undefined -> " + (t === undefined);""",
    ),
]


# ---------------------------------------------------------------------------
# 10.1 JS Dates
# ---------------------------------------------------------------------------

DATES = [
    S(
        "new-date-now",
        "new Date() — current date and time",
        [
            "`new Date()` with **no arguments** is **now** (local timezone when printed).",
            "The W3Schools page repeats this Tryit; included **once**.",
            "Date objects are **static snapshots** — the clock on the object is not running.",
        ],
        "const d = new Date();",
        [("d", "String(d)")],
        "The snap shows the **browser's current local date/time** when it was taken (not a fake clock).",
    ),
    S(
        "date-iso-string",
        'new Date("2022-03-25")',
        [
            "A date-only **ISO** string (`YYYY-MM-DD`) is parsed as **UTC midnight**.",
            "Local display may be the **previous evening** in US time zones. The page repeats this Tryit; included once.",
        ],
        'const d = new Date("2022-03-25");',
        [("d", "String(d)")],
        'A Date for **2022-03-25** (UTC). The printed string uses the **browser local** zone.',
    ),
    S(
        "date-long-string",
        'new Date("October 13, 2014 11:13:00")',
        [
            "A **date string** is parsed by the Date constructor.",
            "This form is treated as **local** time in most engines.",
        ],
        'const d = new Date("October 13, 2014 11:13:00");',
        [("d", "String(d)")],
        "**October 13, 2014, 11:13:00** local (string form).",
    ),
    S(
        "seven-numbers",
        "new Date(2018, 11, 24, 10, 33, 30, 0) — month 11 is December",
        [
            "Seven numbers: **year, month, day, hours, minutes, seconds, ms**.",
            "Months are **0–11**. **11** means **December**, not November.",
        ],
        "const d = new Date(2018, 11, 24, 10, 33, 30, 0);",
        [("d", "String(d)")],
        "**December 24, 2018, 10:33:30** local time.",
    ),
    S(
        "month-overflow",
        "new Date(2018, 15, ...) — month overflow to April 2019",
        [
            "A month **greater than 11** does not error; it **overflows** into the next year.",
            "Month **15** is 12 + 3 → **April 2019** (month 3).",
        ],
        "const d = new Date(2018, 15, 24, 10, 33, 30);",
        [("d", "String(d)")],
        "**April 24, 2019, 10:33:30** local (overflow from month 15).",
    ),
    S(
        "month-overflow-equiv",
        "new Date(2019, 3, ...) — same as month overflow",
        [
            "This is the **same instant** as `new Date(2018, 15, 24, 10, 33, 30)`.",
            "Month **3** is **April**.",
        ],
        "const d = new Date(2019, 3, 24, 10, 33, 30);",
        [("d", "String(d)")],
        "**April 24, 2019, 10:33:30** local — same as the overflow example.",
    ),
    S(
        "day-overflow",
        "new Date(2018, 5, 35, ...) — day overflow",
        [
            "A **day** past the end of the month also overflows.",
            "June has 30 days (month **5**). Day **35** is 5 days into **July**.",
        ],
        "const d = new Date(2018, 5, 35, 10, 33, 30);",
        [("d", "String(d)")],
        "**July 5, 2018, 10:33:30** local.",
    ),
    S(
        "day-overflow-equiv",
        "new Date(2018, 6, 5, ...) — same as day overflow",
        [
            "Month **6** is **July**. Same instant as `new Date(2018, 5, 35, ...)`.",
        ],
        "const d = new Date(2018, 6, 5, 10, 33, 30);",
        [("d", "String(d)")],
        "**July 5, 2018, 10:33:30** local — same as the day-overflow example.",
    ),
    S(
        "six-numbers",
        "6 numbers: year through seconds",
        [
            "Six numbers omit milliseconds (they default to **0**).",
        ],
        "const d = new Date(2018, 11, 24, 10, 33, 30);",
        [("d", "String(d)")],
        "**December 24, 2018, 10:33:30** local.",
    ),
    S(
        "five-numbers",
        "5 numbers: year through minutes",
        [
            "Five numbers: seconds default to **0**.",
        ],
        "const d = new Date(2018, 11, 24, 10, 33);",
        [("d", "String(d)")],
        "**December 24, 2018, 10:33:00** local.",
    ),
    S(
        "four-numbers",
        "4 numbers: year, month, day, hours",
        [
            "Four numbers: minutes and seconds default to **0**.",
        ],
        "const d = new Date(2018, 11, 24, 10);",
        [("d", "String(d)")],
        "**December 24, 2018, 10:00:00** local.",
    ),
    S(
        "three-numbers",
        "3 numbers: year, month, day",
        [
            "Three numbers: time defaults to **00:00:00** local.",
        ],
        "const d = new Date(2018, 11, 24);",
        [("d", "String(d)")],
        "**December 24, 2018** at local midnight.",
    ),
    S(
        "two-numbers",
        "2 numbers: year and month",
        [
            "Two numbers: day defaults to **1**.",
            "You **cannot** omit month. One argument is milliseconds, not a year.",
        ],
        "const d = new Date(2018, 11);",
        [("d", "String(d)")],
        "**December 1, 2018** at local midnight.",
    ),
    S(
        "one-number-ms",
        "1 number: new Date(2018) is milliseconds, not year",
        [
            "**One** argument is **milliseconds since the epoch**, not the year 2018.",
            "2018 ms after 1970-01-01 UTC is still **1 January 1970**.",
        ],
        "const d = new Date(2018);",
        [("d", "String(d)"), ("d.getTime()", "d.getTime()")],
        "**~2 seconds after** 1970-01-01 UTC (2018 milliseconds), **not** the year 2018.",
    ),
    S(
        "year-99",
        "new Date(99, 11, 24) → 1999",
        [
            "Years **0–99** are treated as **19xx** (previous century).",
            "**99** means **1999**.",
        ],
        "const d = new Date(99, 11, 24);",
        [("d", "String(d)"), ("d.getFullYear()", "d.getFullYear()")],
        "**December 24, 1999**. `getFullYear()` is **1999**.",
    ),
    S(
        "year-9",
        "new Date(9, 11, 24) → 1909",
        [
            "**9** is **1909**, not 2009 and not year 9.",
        ],
        "const d = new Date(9, 11, 24);",
        [("d", "String(d)"), ("d.getFullYear()", "d.getFullYear()")],
        "**December 24, 1909**. `getFullYear()` is **1909**.",
    ),
    S(
        "ms-positive",
        "new Date(100000000000)",
        [
            "Dates are stored as **ms since 1 January 1970 UTC** (the epoch).",
            "100 000 000 000 ms is that many milliseconds **after** the epoch.",
        ],
        "const d = new Date(100000000000);",
        [("d", "String(d)")],
        "About **3 March 1973** UTC (plus local offset when printed).",
    ),
    S(
        "ms-negative",
        "new Date(-100000000000)",
        [
            "A **negative** millisecond value is **before** the epoch.",
        ],
        "const d = new Date(-100000000000);",
        [("d", "String(d)")],
        "About **31 October 1966** UTC (plus local offset when printed).",
    ),
    S(
        "one-day-ms",
        "new Date(24*60*60*1000) / 86400000",
        [
            "One day is **86 400 000** ms (`24 * 60 * 60 * 1000`).",
            "The page Tryit shows both forms; they are the **same** instant.",
        ],
        "const d1 = new Date(24 * 60 * 60 * 1000);\nconst d2 = new Date(86400000);",
        [
            ("d1", "String(d1)"),
            ("d2", "String(d2)"),
            ("d1.getTime() === d2.getTime()", "d1.getTime() === d2.getTime()"),
        ],
        "Both are **one day after** the epoch. The two constructors match.",
    ),
    S(
        "epoch-zero",
        "new Date(0) — epoch",
        [
            "**Zero time** is 1 January 1970 00:00:00 **UTC**.",
            "Local `toString()` may show **31 December 1969** in US time zones.",
        ],
        "const d = new Date(0);",
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "**Epoch.** `toISOString()` is **1970-01-01T00:00:00.000Z**.",
    ),
    S(
        "to-string",
        "d.toString()",
        [
            "HTML and string conversion use **`toString()`** by default.",
            "Includes **local** date, time, and time zone.",
        ],
        "const d = new Date();\nd.toString();",
        [("d.toString()", "d.toString()")],
        "The snap shows the **browser's current local date/time** via **toString()**.",
    ),
    S(
        "to-date-string",
        "d.toDateString()",
        [
            "`toDateString()` is a **shorter** readable date (no time).",
        ],
        "const d = new Date();\nd.toDateString();",
        [("d.toDateString()", "d.toDateString()")],
        "The snap shows the **browser's current local date** (date part only).",
    ),
    S(
        "to-utc-string",
        "d.toUTCString()",
        [
            "`toUTCString()` formats the same instant in **UTC** (GMT).",
        ],
        "const d = new Date();\nd.toUTCString();",
        [("d.toUTCString()", "d.toUTCString()")],
        "The snap shows the **browser's current** instant as a **UTC** string.",
    ),
    S(
        "to-iso-string",
        "d.toISOString()",
        [
            "`toISOString()` is the **ISO 8601** UTC form (`...Z`).",
        ],
        "const d = new Date();\nd.toISOString();",
        [("d.toISOString()", "d.toISOString()")],
        "The snap shows the **browser's current** instant as **ISO UTC**.",
    ),
]


def run_all() -> None:
    sections = [
        (
            "js-scope",
            "JS Scope",
            SCOPE,
            "Scope is where a variable is visible. JavaScript has global scope, function scope, and (since ES6) block scope. Globals can be read from anywhere on the page. Locals exist only inside their function. Block lets and consts stay inside their braces. Undeclared assignment in sloppy mode becomes global; strict mode does not do that. In HTML, var globals hang off window and let globals do not.",
            [
                "**Three scopes:** global, function, and block (`let` / `const` in `{ }`).",
                "**Function locals** are created when the call starts and gone when it finishes. Same names can exist in different functions.",
                "**`var` is not block-scoped** — it leaks out of `{ }`. Prefer `let` / `const`.",
                "**Automatically global** only in sloppy mode. **Strict mode** undeclared assignment is an error (next chapter).",
                "HTML global object is **`window`**. Global **`var`** is `window.name`; global **`let` is not**.",
                "Do **not** create globals unless you mean to — they can clash with `window` properties.",
            ],
            [
                ("What are the three kinds of JavaScript scope?", ["**Global**, **function**, and **block**."]),
                ("Can a global `let carName` be used inside a function?", ["**Yes.** Globals are visible everywhere on the page."]),
                ("What happens if you read a function-local `carName` outside the function?", ["**ReferenceError**."]),
                ("Does `let x = 2` inside `{ }` leak?", ["**No.** Outside is **ReferenceError**."]),
                ("Does `var x = 2` inside `{ }` leak?", ["**Yes.** Outside, x is still **2**. Not recommended."]),
                ("What is an automatically global variable?", ["An **assignment without a declaration** in sloppy mode.", "It can be used **outside** the function that assigned it."]),
                ("Does strict mode still auto-create globals?", ["**No.** Undeclared assignment is an error. Covered in JS Strict Mode."]),
                ("Is `window.carName` set by `var carName`?", ["**Yes** (HTML). Not recommended."]),
                ("Is `window.carName` set by `let carName`?", ["**No.** `window.carName` is **undefined**."]),
                ("When are local variables deleted?", ["When the **function call finishes**.", "Browser globals last until the **tab** closes."]),
                ("Do `var`, `let`, and `const` all have function scope inside a function?", ["**Yes.** Inside a function they are all **local** to that function."]),
                ("Should you create globals by default?", ["**No.** Only when you intend a page-wide value."]),
            ],
            "Pick the smallest scope that works. Use let and const in blocks, keep function data local, and treat undeclared assignment and window-bound var as habits to drop — especially once strict mode is on.",
            [
                ("JS Scope (W3Schools)", "https://www.w3schools.com/js/js_scope.asp"),
                ("MDN: Scope", "https://developer.mozilla.org/en-US/docs/Glossary/Scope"),
                ("MDN: let", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let"),
            ],
        ),
        (
            "js-code-blocks",
            "JS Code Blocks",
            BLOCKS,
            "A code block is a group of statements inside curly braces. Function bodies, if/else branches, and loop bodies are blocks. let and const declared in a block stay in that block. You can also write a standalone pair of braces to give variables a short lifetime without wrapping them in a function.",
            [
                "A **block** `{ }` is one unit of statements — required for function bodies, `if`/`else`, `for`, and `while`.",
                "`let` / `const` in a block are **block-scoped**. They do not leak.",
                "A **standalone** block is valid: use it to encapsulate a calculation (`areal`) without polluting globals.",
                "Inside the block you can read the bindings; **outside** they throw **ReferenceError**.",
            ],
            [
                ("What is a code block?", ["Statements grouped in **`{ }`**, treated as one unit."]),
                ("Is a function body a block?", ["**Yes.** The body is always wrapped in braces."]),
                ("Why do `if` / `else` use blocks?", ["So each branch can run **several statements** as one unit."]),
                ("What did `check(10)` vs `check(3)` show?", ["**if block** vs **else block** — both ran in the demo."]),
                ("What is the body of `for` / `while`?", ["A **code block** that repeats."]),
                ("Can you read `let x = 10` after its `{ }`?", ["**No.** **ReferenceError**."]),
                ("What is a standalone block for?", ["A **temporary scope** for `let` / `const` without a function.", "Avoids polluting the global scope and name clashes."]),
                ("What is `areal` inside `{ let x = 10; let y = 100; let areal = x * y }`?", ["**1000** inside. **ReferenceError** outside."]),
                ("Does a standalone block run immediately?", ["**Yes.** It is not a function — the statements run when that part of the script runs."]),
                ("Can you reuse the names `x` and `y` after the block?", ["**Yes.** They were never declared in the outer scope."]),
            ],
            "Braces group statements for functions, branches, and loops, and they also define let/const scope. A standalone block is a lightweight way to keep short-lived names off the global object.",
            [
                ("JS Code Blocks (W3Schools)", "https://www.w3schools.com/js/js_codeblocks.asp"),
                ("MDN: block", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block"),
            ],
        ),
        (
            "js-hoisting",
            "JS Hoisting",
            HOISTING,
            "Hoisting is the engine treating declarations as if they exist at the top of the current scope. var can be assigned before its line and still work. let and const are hoisted too but stay uninitialized in a temporal dead zone, so using them early is a ReferenceError. A const with no initializer is a SyntaxError at parse time, which is why a raw script tag would not run at all. Only declarations hoist, not the = value. Declare at the top of each scope.",
            [
                "**Declarations** hoist; **initializations** do not.",
                "`var` is hoisted and set to **undefined** until its assignment runs.",
                "`let` / `const` hoist into the **TDZ**. Early use → **ReferenceError**.",
                "`const name;` (no initializer) is a **SyntaxError**. That fails **parse** of a whole `<script>`. This section catches it with **`new Function`**.",
                "A `const` **with** an initializer used early is **ReferenceError** (TDZ), same as `let` — that is the engine; the W3Schools const Tryit is the missing-initializer SyntaxError.",
                "Declare variables at the **top** of every scope. Strict mode (next chapter) forbids undeclared names.",
            ],
            [
                ("What is hoisting?", ["Declarations are treated as existing at the **top** of the current scope (script or function)."]),
                ("Are initializations hoisted?", ["**No.** Only the declaration. `= 7` stays where you wrote it."]),
                ("What is `x` after `x = 5; var x;`?", ["**5** — same as `var x; x = 5`."]),
                ("What is `carName = \"Volvo\"; let carName`?", ["**ReferenceError** (temporal dead zone)."]),
                ("What is `carName = \"Volvo\"; const carName;`?", ["**SyntaxError** — `const` requires an initializer.", "A `<script>` containing that source **does not parse**, so the page would show nothing.", "This sandbox uses **`new Function`** to compile it at runtime and **catch** the error."]),
                ("If the const line were `const carName = \"Volvo\"` after an early assignment, what error?", ["**ReferenceError** (TDZ), like `let` — not SyntaxError."]),
                ("What is `x + \" \" + y` when `var x = 5` then display then `var y = 7`?", ['**`"5 undefined"`**.']),
                ("Why is y undefined there?", ["`var y` was **declared** (hoisted) but **not yet assigned** 7."]),
                ("What is the equivalent rewrite?", ["`var y;` then display, then `y = 7`."]),
                ("Should you rely on hoisting in new code?", ["**No.** Declare at the **top** of the scope so the source matches the engine."]),
                ("Does strict mode allow using a name that was never declared?", ["**No.** That is the next chapter."]),
            ],
            "var declarations rise to the top as undefined; let and const rise into a dead zone; a const with no initializer never even parses. Write declarations first so you do not depend on hoisting.",
            [
                ("JS Hoisting (W3Schools)", "https://www.w3schools.com/js/js_hoisting.asp"),
                ("MDN: Hoisting", "https://developer.mozilla.org/en-US/docs/Glossary/Hoisting"),
                ("MDN: Temporal dead zone", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz"),
            ],
        ),
        (
            "js-varletconst",
            "JS var/let/const",
            VARLET,
            "var, let, and const differ in scope, redeclaration, reassignment, and hoisting. var leaks out of blocks, can be redeclared, and reads as undefined before its line. let and const are block-scoped, cannot be redeclared in the same scope, and throw ReferenceError in the temporal dead zone. const cannot be reassigned, but object properties can still change. Modern style is const by default, let when the binding must change, and no var.",
            [
                "**var:** function/global scope, redeclare yes, reassign yes, hoisted as **undefined**.",
                "**let:** block scope, redeclare no (**SyntaxError**), reassign yes, hoisted **uninitialized** (TDZ → **ReferenceError**).",
                "**const:** block scope, redeclare no, reassign no (**TypeError**), TDZ like let. Properties of a const **object** can still change.",
                "**Best practice:** `const` by default, `let` if you reassign, never `var`.",
            ],
            [
                ("Does `var` leak out of an `if` block?", ["**Yes.** `firstName` is John outside.", "`let lastName` does **not** leak; the Tryit leaves text2 as unknown."]),
                ("Can you set `user.name` on a `const` object?", ["**Yes.** That mutates a property, not the binding."]),
                ("Can you replace a `const` object with a new one?", ["**No.** **TypeError**."]),
                ("Can `var x` be declared twice in one scope?", ["**Yes.** The second declaration overwrites."]),
                ("Can `let x` be declared twice in one scope?", ["**No.** **SyntaxError** (parse time — this demo uses `new Function`)."]),
                ("What does `PI = 3.14159` do if `const PI = 3.14`?", ["**TypeError.** PI stays **3.14**."]),
                ("What is a `var` value if you read it before its line?", ["**undefined** (hoisted)."]),
                ("What is a `let` or `const` value if you read it before its line?", ["**ReferenceError** (TDZ)."]),
                ("Is `const x;` without a value legal?", ["**No.** That is a **SyntaxError**. `const` must be initialized on the same line."]),
                ("What should you use by default?", ["**`const`.** Use **`let`** only when the binding will change. Avoid **`var`**."]),
                ("Are let and const hoisted?", ["**Yes**, but they are **not initialized**. The gap is the **temporal dead zone**."]),
            ],
            "Use const unless the binding must change, then let. Skip var: it leaks from blocks, allows silent redeclaration, and reads as undefined before its line. const objects can still have their properties updated.",
            [
                ("JS var, let, const (W3Schools)", "https://www.w3schools.com/js/js_varletconst.asp"),
                ("MDN: let", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let"),
                ("MDN: const", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const"),
                ("MDN: var", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var"),
            ],
        ),
        (
            "js-strict-mode",
            "JS Strict Mode",
            STRICT,
            "Strict mode turns sloppy mistakes into errors. Place use strict at the very beginning of a script (this sandbox file) or a function. Undeclared assignments, duplicate parameters, with, octal literals, binding the names eval or arguments, and delete on a variable name are all rejected. Some of those are SyntaxErrors at parse time, so this section compiles them with new Function in order to catch and print the error. A function called without an owner has this equal to undefined. The W3Schools undeclared-variable Tryit appears twice; it is shown once.",
            [
                '`"use strict";` is a **directive**. It must be **first** in a script or function or it is ignored.',
                "This sandbox script **is** the script — global examples put use strict at the top of that script.",
                "**ReferenceError / TypeError** can be try/caught in the same script. **SyntaxError** would blank the page, so those snippets run inside **`new Function`**.",
                "Strict `eval` does not leak `var`/`let` into the caller. Bare-call **`this`** is **undefined**.",
            ],
            [
                ("Where must `\"use strict\";` go?", ["The **first** statement of a **script** or a **function**."]),
                ("What does `x = 3.14` do in strict mode?", ["**ReferenceError** — x was never declared."]),
                ("If only the function has `\"use strict\"`, is outer `x = 3.14` OK?", ["**Yes** (sloppy outer script). Inner undeclared `y` still errors."]),
                ("Why skip a second undeclared-`x` Tryit?", ["It is an **exact duplicate** of the first “Not Allowed” example."]),
                ("What error is `delete x` on a `let` in strict mode?", ["**SyntaxError** (unqualified identifier). Caught with `new Function`."]),
                ("Duplicate parameter names?", ["**SyntaxError** in strict mode."]),
                ("What about `let x = 010` or `\"\\010\"`?", ["**SyntaxError** — octal literals and octal escapes are banned."]),
                ("Writing a `writable: false` property?", ["**TypeError** in strict mode (silent fail in sloppy mode)."]),
                ("`delete Object.prototype`?", ["**TypeError** — the property is undeletable."]),
                ("`let eval` or `let arguments`?", ["**SyntaxError** — those names are reserved in strict mode."]),
                ("Is `with` allowed?", ["**No.** **SyntaxError**."]),
                ("Does `eval(\"var x = 2\")` create an outer `x` in strict mode?", ["**No.** Reading `x` is **ReferenceError**."]),
                ("What is `this` in a strict function called as `myFunction()`?", ["**undefined** (not `window`)."]),
            ],
            "Put use strict first. Undeclared names, with, octals, duplicate parameters, and delete-on-variable become errors. Parse-time SyntaxErrors are demonstrated with new Function so the sandbox page can still load. Strict this on a bare call is undefined.",
            [
                ("JS Strict Mode (W3Schools)", "https://www.w3schools.com/js/js_strict.asp"),
                ("MDN: Strict mode", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode"),
            ],
        ),
        (
            "js-dates",
            "JS Dates",
            DATES,
            "Date objects store an instant as milliseconds since 1 January 1970 UTC. new Date() captures now; the object does not keep ticking. You can pass a date string, a millisecond count, or 2–7 numbers (year, month, …). Months are 0–11. Extra months or days overflow instead of throwing. A single number is milliseconds, not a year. Years 0–99 become 19xx. Display helpers include toString, toDateString, toUTCString, and toISOString. Date string formats are the next chapter — not this one.",
            [
                "Date objects are **static**. Creating `new Date()` copies **now**; the object’s clock does **not** run.",
                "**Nine constructors:** no-arg now, date string, 2–7 numbers, or milliseconds.",
                "Months are **0–11**. Overflow months/days **roll** into later months/years (no error).",
                "**One** argument = **milliseconds**, not a year. **0–99** years map to **19xx**.",
                "Epoch is **1970-01-01T00:00:00.000Z**. One day = **86400000** ms.",
                "Default print is **`toString()`** (local). Also: `toDateString`, `toUTCString`, `toISOString`.",
            ],
            [
                ("Does a Date object keep ticking?", ["**No.** It is a **snapshot**. The computer clock still ticks."]),
                ("What is `new Date()`?", ["The **current** date and time in the **browser**. Snaps are not a fake clock."]),
                ("What month is `11` in `new Date(2018, 11, 24, …)`?", ["**December.** Months are **0–11**."]),
                ("What is `new Date(2018, 15, 24, 10, 33, 30)`?", ["**April 24, 2019** — month 15 overflows. Same as `new Date(2019, 3, 24, …)`."]),
                ("What is `new Date(2018, 5, 35, …)`?", ["**July 5, 2018** — day 35 overflows June. Same as `new Date(2018, 6, 5, …)`."]),
                ("What does one argument `new Date(2018)` mean?", ["**2018 milliseconds** after the epoch, **not** the year 2018."]),
                ("What year is `new Date(99, 11, 24)`?", ["**1999**."]),
                ("What year is `new Date(9, 11, 24)`?", ["**1909**."]),
                ("What is `new Date(0)`?", ["The **epoch**: 1 January 1970 00:00:00 UTC.", "Local `toString()` may show **31 Dec 1969** in US zones."]),
                ("How many ms is one day?", ["**86400000**. `24 * 60 * 60 * 1000` is the same."]),
                ("`toString` vs `toDateString` vs `toUTCString` vs `toISOString`?", ["**toString**: local date+time+zone.", "**toDateString**: local date only.", "**toUTCString**: UTC / GMT text.", "**toISOString**: ISO 8601 UTC with `Z`."]),
                ("Is `YYYY-MM-DD` local midnight?", ["**No.** Date-only ISO is **UTC midnight**, which can print as the **previous local evening**."]),
            ],
            "Create dates with new Date, remember months start at zero, and expect overflow instead of errors. One number is milliseconds. Two-digit years are 19xx. The object is a frozen snapshot of an instant; formatting methods only change how that instant is printed.",
            [
                ("JS Dates (W3Schools)", "https://www.w3schools.com/js/js_dates.asp"),
                ("MDN: Date", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date"),
            ],
        ),
    ]
    print("example counts:")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print(f"  {slug}: {len(recs)}")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print("building", slug, "examples", len(recs))
        build_and_snap(slug, title, recs, intro, concepts, qa, summary, refs)
        print("done", slug)


if __name__ == "__main__":
    run_all()
