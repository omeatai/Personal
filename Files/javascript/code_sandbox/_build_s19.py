"""S19: Debug Intro, Console, Breakpoints, Errors, Async, Reference."""
from __future__ import annotations

from _gen_lib import (
    S,
    build_and_snap,
    console_script,
    indent_js,
    nf_script,
    out_script,
    CONSOLE_BOOT,
)


def console_async_script(code: str, delay_ms: int = 500) -> str:
    return f"""{CONSOLE_BOOT}
{indent_js(code)}
      Promise.resolve()
        .then(function () {{
          return new Promise(function (resolve) {{ setTimeout(resolve, {delay_ms}); }});
        }})
        .then(__flush)
        .catch(function (e) {{
          __out.push(e.name + ": " + e.message);
          __flush();
        }});"""


# ---------------------------------------------------------------------------
# 19.1 Debug Intro
# ---------------------------------------------------------------------------

INTRO = [
    S(
        "console-hello",
        'console.log("Hello!")',
        [
            "If the page **does nothing**, open the **console** (usually **F12** → **Console**).",
            "**`console.log()`** prints a value. It does **not** change the HTML.",
            "The Tryit is a full page: heading **My First Web Page**, then `console.log(\"Hello!\")`.",
        ],
        '<!DOCTYPE html>\n<html>\n<body>\n<h1>My First Web Page</h1>\n<script>\nconsole.log("Hello!");\n</script>\n</body>\n</html>',
        outcome='The mirrored console shows **log: Hello!**. The heading is unchanged — the message is **not** in the page body.',
        script=console_script('console.log("Hello!");'),
        body="<h1>My First Web Page</h1>",
    ),
    S(
        "console-variables",
        "console.log price, quantity, and total",
        [
            "Log **variables** to see what the program is doing.",
            "**Tip:** log **before and after** a suspect line to see where values go wrong.",
        ],
        'let price = 50;\nlet quantity = 3;\nlet total = price * quantity;\nconsole.log("Total:", total);',
        outcome='**log: Total: 150**. `price * quantity` is **150**.',
        script=console_script(
            'let price = 50;\nlet quantity = 3;\nlet total = price * quantity;\nconsole.log("Total:", total);'
        ),
    ),
    S(
        "string-vs-number",
        '5 + "5" is "55"; 5 + Number("5") is 10',
        [
            "Many bugs are **wrong assumptions** about a value or its **type**.",
            '`5 + "5"` concatenates (**`"55"`**). `5 + Number("5")` adds (**10**).',
            "Check the value. Check the type. Do not guess.",
        ],
        'let x = 5;\nlet y = "5";\nconsole.log(x + y);  // 55 (string!)\nconsole.log(x + Number(y));  // 10 (number)',
        outcome='First log is **"55"** (string). Second log is **10** (number).',
        script=console_script(
            'let x = 5;\nlet y = "5";\nconsole.log(x + y);\nconsole.log(x + Number(y));'
        ),
    ),
    S(
        "referenceerror-myvalue",
        "ReferenceError: myValue is not defined",
        [
            "**ReferenceError** means **this name does not exist** (misspelling or never declared).",
            "The console usually includes a **line number**. Click it to jump to the line.",
        ],
        "console.log(myValue);  // ReferenceError: myValue is not defined",
        outcome="**ReferenceError: myValue is not defined**. Nothing is logged first — the throw happens immediately.",
        script=console_script("console.log(myValue);", catch=True),
    ),
    S(
        "typeerror-undefined-length",
        "TypeError: Cannot read properties of undefined (reading 'length')",
        [
            "**TypeError** means you used a value in an **impossible** way.",
            "`let x;` leaves `x` as **`undefined`**. `undefined` has no **`length`**.",
        ],
        "let x;\nconsole.log(x.length);  // TypeError: Cannot read properties of undefined",
        outcome="**TypeError: Cannot read properties of undefined (reading 'length')**.",
        script=console_script("let x;\nconsole.log(x.length);", catch=True),
    ),
    S(
        "assignment-in-if",
        "Mistake: if (x = 5) assigns and always runs",
        [
            "`=` **assigns**. `==` / `===` **compare**.",
            "`if (x = 5)` sets `x` to **5** (truthy) and the block **runs** even when `x` started as **10**.",
        ],
        'let x = 10;\nif (x = 5) {\n  console.log("This runs");\n}',
        outcome='**log: This runs**. After the `if`, `x` is **5** (not 10).',
        script=console_script(
            'let x = 10;\nif (x = 5) {\n  console.log("This runs");\n}\nconsole.log("x after if:", x);'
        ),
    ),
    S(
        "strict-equals-in-if",
        "Fix: if (x === 5) compares without assigning",
        [
            "Use **`===`** (or `==` if you really want coercion).",
            "With `x = 10`, `if (x === 5)` is **false** — the log **does not run**.",
        ],
        'let x = 10;\nif (x === 5) {\n  console.log("This runs only if x is 5");\n}',
        outcome="No **This runs only if x is 5** line. `x` stays **10**.",
        script=console_script(
            'let x = 10;\nif (x === 5) {\n  console.log("This runs only if x is 5");\n}\nconsole.log("x stays:", x);'
        ),
    ),
    S(
        "console-sum",
        "console.log(c) after a + b",
        [
            "A tiny script: `a = 5`, `b = 6`, `c = a + b`, then **`console.log(c)`**.",
            "This is the page’s last Tryit (under browser debugging tools).",
        ],
        "let a = 5;\nlet b = 6;\nlet c = a + b;\nconsole.log(c);",
        outcome="**log: 11**.",
        script=console_script("let a = 5;\nlet b = 6;\nlet c = a + b;\nconsole.log(c);"),
    ),
    S(
        "read-reproduce-reduce-fix",
        "Habit: Read → Reproduce → Reduce → Fix",
        [
            "Debugging is **not guessing**. The page’s habit: **Read** the error → **Reproduce** → **Reduce** to a small example → **Fix**.",
            "Here a **reduced** snippet is `total = price + qty` with `qty` as a **string** — the bug is visible in one log.",
        ],
        'let price = 50;\nlet qty = "3";\nlet total = price + qty;\nconsole.log("total", total, typeof total);\nlet fixed = price + Number(qty);\nconsole.log("fixed", fixed, typeof fixed);',
        outcome='Broken **total** is **"503"** (string). **fixed** is **53** (number).',
        script=console_script(
            'let price = 50;\nlet qty = "3";\nlet total = price + qty;\nconsole.log("total", total, typeof total);\nlet fixed = price + Number(qty);\nconsole.log("fixed", fixed, typeof fixed);'
        ),
    ),
    S(
        "open-console-f12",
        "Open the browser console (F12)",
        [
            "All modern browsers have a built-in **JavaScript debugger**.",
            "Usually **F12**, then the **Console** tab. You can also: right-click → **Inspect** → **Console**.",
            "**Chrome:** More tools → Developer tools → Console. **Firefox:** Web Developer → Web Console. **Edge:** Developer Tools → Console. **Opera:** Developer → Developer tools → Console. **Safari:** Preferences → Advanced → Enable Develop menu, then Develop → Show Error Console.",
            "If you do **one** thing when code fails: **look at the console**.",
        ],
        "console.log(\"F12 then Console\");",
        outcome='**log: F12 then Console**. The sandbox mirrors DevTools output onto the page so the snap is visible without opening F12.',
        script=console_script('console.log("F12 then Console");'),
    ),
]


# ---------------------------------------------------------------------------
# 19.2 Debug Console
# ---------------------------------------------------------------------------

CONSOLE = [
    S(
        "log-hello",
        'console.log("Hello from JavaScript!")',
        [
            "**`console.log()`** is the most common console method.",
            "Use it to print values and see what the program is doing.",
        ],
        'console.log("Hello from JavaScript!");',
        outcome="**log: Hello from JavaScript!**",
        script=console_script('console.log("Hello from JavaScript!");'),
    ),
    S(
        "log-variables",
        "console.log(name) and console.log(age)",
        [
            "You can log **each** variable on its own line.",
            "That is clearer than guessing which value is wrong.",
        ],
        'let name = "John";\nlet age = 25;\nconsole.log(name);\nconsole.log(age);',
        outcome='**log: John** then **log: 25**.',
        script=console_script(
            'let name = "John";\nlet age = 25;\nconsole.log(name);\nconsole.log(age);'
        ),
    ),
    S(
        "console-warn",
        'console.warn("This is a warning!")',
        [
            "**`console.warn()`** is a **warning** (often yellow). The program **still runs**.",
            "Use it for something **suspicious**, not a hard failure.",
        ],
        'console.warn("This is a warning!");',
        outcome="**warn: This is a warning!**",
        script=console_script('console.warn("This is a warning!");'),
    ),
    S(
        "console-error",
        'console.error("Something went wrong!")',
        [
            "**`console.error()`** prints an **error-styled** message (often red).",
            "It does **not** throw. Execution **continues**. Use `throw` if you need to stop.",
        ],
        'console.error("Something went wrong!");',
        outcome="**error: Something went wrong!** — and the next line can still run.",
        script=console_script(
            'console.error("Something went wrong!");\nconsole.log("still running");'
        ),
    ),
    S(
        "log-multiple",
        'console.log("x =", x, "y =", y)',
        [
            "`console.log` accepts **multiple arguments**. They print separated by spaces.",
            "Useful for labeling values: `\"x =\", x, \"y =\", y`.",
        ],
        'let x = 10;\nlet y = 5;\nconsole.log("x =", x, "y =", y);',
        outcome="**log: x = 10 y = 5**.",
        script=console_script(
            'let x = 10;\nlet y = 5;\nconsole.log("x =", x, "y =", y);'
        ),
    ),
    S(
        "log-object",
        "console.log(user) inspects an object",
        [
            "Logging an **object** shows its properties.",
            "In DevTools you can **click to expand**. Here JSON shows **name** and **age**.",
        ],
        'let user = {name: "John", age: 25};\nconsole.log(user);',
        outcome='**log: {"name":"John","age":25}**.',
        script=console_script(
            'let user = {name: "John", age: 25};\nconsole.log(user);'
        ),
    ),
    S(
        "console-table",
        "console.table(users) for arrays of objects",
        [
            "**`console.table()`** renders rows as a **table** (index, name, age).",
            "Much easier to scan than a nested object dump.",
        ],
        'let users = [\n  {name: "John", age: 25},\n  {name: "Anna", age: 30}\n];\nconsole.table(users);',
        outcome='**table:** `[{"name":"John","age":25},{"name":"Anna","age":30}]`. In DevTools this is a grid with columns **name** and **age**.',
        script=console_script(
            'let users = [\n  {name: "John", age: 25},\n  {name: "Anna", age: 30}\n];\nconsole.table(users);'
        ),
    ),
    S(
        "stop-guessing",
        "Stop guessing — log the value",
        [
            "Beginners **guess**. Professionals **log and confirm**.",
            "If code misbehaves, do not invent a theory first — **`console.log` the actual value**.",
        ],
        'let cart = { items: 2, total: 0 };\nconsole.log("cart before", cart);\ncart.total = 19.9 * cart.items;\nconsole.log("cart after", cart);',
        outcome='Before: **total 0**. After: **total 39.8**. The log **confirms** the write.',
        script=console_script(
            'let cart = { items: 2, total: 0 };\nconsole.log("cart before", cart);\ncart.total = 19.9 * cart.items;\nconsole.log("cart after", cart);'
        ),
    ),
]


# ---------------------------------------------------------------------------
# 19.3 Debug Breakpoints
# ---------------------------------------------------------------------------

BREAKPOINTS = [
    S(
        "add-function-breakpoints",
        "add(a, b) — pause on a line, then inspect result",
        [
            "A **breakpoint** pauses on a **specific line**. You then inspect variables and **step**.",
            "Set them in DevTools **Sources**: click a **line number**, **reload**, use **play** to continue.",
            "This Tryit calls `add` four times (5, 50, 500, 5000). Without a breakpoint the last write wins: **5010**.",
            "Headless snaps cannot pause DevTools. The sandbox still **runs** the function so you see the final DOM value.",
        ],
        'function add(a, b) {\n  let result = a + b;\n  return result;\n}\ndocument.getElementById("demo").innerHTML = add(10, 5);\ndocument.getElementById("demo").innerHTML = add(10, 50);\ndocument.getElementById("demo").innerHTML = add(10, 500);\ndocument.getElementById("demo").innerHTML = add(10, 5000);',
        outcome="The paragraph ends as **5010** (`10 + 5000`). Earlier results **15**, **60**, **510** were overwritten.",
        script="""      function add(a, b) {
        let result = a + b;
        return result;
      }
      const results = [add(10, 5), add(10, 50), add(10, 500), add(10, 5000)];
      document.getElementById("demo").innerText =
        "add(10, 5) -> " + results[0] + "\\n" +
        "add(10, 50) -> " + results[1] + "\\n" +
        "add(10, 500) -> " + results[2] + "\\n" +
        "add(10, 5000) -> " + results[3] + "\\n" +
        "final innerHTML if assigned four times -> " + results[3];""",
    ),
    S(
        "debugger-keyword",
        "debugger; pauses like a breakpoint",
        [
            "The **`debugger`** keyword stops execution and opens the debugger **if DevTools is open**.",
            "If no debugger is attached, **`debugger` has no effect**.",
            "The page’s Tryit: `let x = 15 * 5; debugger; document.getElementById(\"demo\").innerHTML = x;`",
            "This sandbox **omits** `debugger` so the screenshot can finish. With DevTools open, the original line would pause **before** writing **75**.",
        ],
        "let x = 15 * 5;\n// debugger;  // omitted in the live demo so the page can finish\ndocument.getElementById(\"demo\").innerHTML = x;",
        outcome="**x** is **75**. A live `debugger;` would pause **before** that assignment when DevTools is open.",
        script="""      let x = 15 * 5;
      document.getElementById("demo").innerText =
        "x -> " + x + "\\n" +
        "(debugger omitted so this page can finish)";""",
    ),
    S(
        "step-over-into-out",
        "Step Over, Step Into, Step Out",
        [
            "When paused: **Step Over** runs the **next line** (does not enter a call). **Step Into** **enters** a function. **Step Out** **finishes** the current function.",
            "Watch values change as you step. This demo shows the same calls without pausing.",
        ],
        "function double(n) {\n  return n * 2;\n}\nfunction total(a, b) {\n  return double(a) + double(b);\n}\nconsole.log(total(3, 4));",
        outcome="**log: 14** (`double(3)+double(4)` → 6+8). Step Into from `total` would enter **`double`**.",
        script=console_script(
            "function double(n) {\n  return n * 2;\n}\nfunction total(a, b) {\n  return double(a) + double(b);\n}\nconsole.log(total(3, 4));"
        ),
    ),
    S(
        "scope-panel",
        "Scope: local y vs global x",
        [
            "The **Scope** panel lists variables **at the current line**.",
            "**Local** variables exist **inside** the function. **Global** variables exist **everywhere**.",
            "At a breakpoint inside `test()`, **`y` exists only there**. **`x`** is still visible (global).",
        ],
        "let x = 10;\nfunction test() {\n  let y = 5;\n  console.log(x + y);\n}\ntest();",
        outcome="**log: 15**. Inside `test`, local **y** is **5** and global **x** is **10**. Outside `test`, **`y` is not defined**.",
        script=console_script(
            "let x = 10;\nfunction test() {\n  let y = 5;\n  console.log(x + y);\n}\ntest();\ntry {\n  console.log(y);\n} catch (e) {\n  console.log(e.name + \": \" + e.message);\n}"
        ),
    ),
    S(
        "watch-panel",
        "Watch a variable instead of many console.log calls",
        [
            "The **Watch** panel tracks an expression **live** as you step.",
            "Add a name (or `result`, `i`, `user.age`). The value **updates** as the code runs.",
            "Prefer Watch for values that change **many times** (loops).",
        ],
        "let sum = 0;\nfor (let i = 1; i <= 3; i++) {\n  sum += i;\n  console.log(\"i\", i, \"sum\", sum);\n}",
        outcome="Watch **`sum`** would show **1**, then **3**, then **6**. Logs: **i 1 sum 1**, **i 2 sum 3**, **i 3 sum 6**.",
        script=console_script(
            'let sum = 0;\nfor (let i = 1; i <= 3; i++) {\n  sum += i;\n  console.log("i", i, "sum", sum);\n}'
        ),
    ),
    S(
        "breakpoint-gotchas",
        "Reload after setting a breakpoint; loops fire often",
        [
            "A common miss: you set a breakpoint **then forget to reload** — old code already ran.",
            "A breakpoint **inside a loop** pauses **every iteration**. Disable it if that gets noisy.",
            "Use breakpoints when values change **unexpectedly**, results are **wrong**, or logic is **complex**.",
        ],
        'for (let i = 0; i < 3; i++) {\n  console.log("loop", i);\n}',
        outcome="**loop 0**, **loop 1**, **loop 2** — a breakpoint on that log would pause **three** times.",
        script=console_script(
            'for (let i = 0; i < 3; i++) {\n  console.log("loop", i);\n}'
        ),
    ),
]


# ---------------------------------------------------------------------------
# 19.4 Debug Errors
# ---------------------------------------------------------------------------

ERRORS = [
    S(
        "read-error-parts",
        "An error message has type, text, and a line number",
        [
            "Read **three** parts: the **error type**, a **short explanation**, and a **line number**.",
            "Click the line number in the console to jump to the code.",
        ],
        "let x = 1;\ntry {\n  x = missing + 1;\n} catch (e) {\n  console.log(e.name);\n  console.log(e.message);\n}",
        outcome="**name:** ReferenceError. **message:** **missing is not defined**. Those two lines are the type + explanation.",
        script=console_script(
            "let x = 1;\ntry {\n  x = missing + 1;\n} catch (e) {\n  console.log(e.name);\n  console.log(e.message);\n}"
        ),
    ),
    S(
        "referenceerror",
        "ReferenceError — a name does not exist",
        [
            "Often a **typo** or a missing **`let` / `const`**.",
            "JavaScript cannot find **`myValue`**.",
        ],
        "console.log(myValue);",
        outcome="**ReferenceError: myValue is not defined**.",
        script=console_script("console.log(myValue);", catch=True),
    ),
    S(
        "typeerror",
        "TypeError — invalid use of a value",
        [
            "Usually **`undefined`** or **`null`**.",
            "`let x;` exists, but has **no value**. You cannot read **`.length`** from `undefined`.",
            "**Log the value before using it.**",
        ],
        "let x;\nconsole.log(x.length);",
        outcome="**TypeError: Cannot read properties of undefined (reading 'length')**.",
        script=console_script("let x;\nconsole.log(x.length);", catch=True),
    ),
    S(
        "syntaxerror",
        "SyntaxError — missing ) in if (x == 5 {",
        [
            "JavaScript **cannot parse** the file. Missing **brackets or parentheses** are typical.",
            "`if (x == 5 {` is missing **`)`**. The **whole script** fails — `try/catch` in the same file cannot help.",
            "This sandbox compiles with **`new Function`** so the page can still render.",
        ],
        'if (x == 5 {\n  console.log("Hello");\n}',
        outcome="**SyntaxError** (missing `)` after argument list / unexpected `{`). A raw `<script>` would not load.",
        script=nf_script('if (x == 5 {\n  console.log("Hello");\n}'),
    ),
    S(
        "nan-errors",
        'NaN — "abc" * 5 is not a number',
        [
            "**NaN** means **Not a Number**. Invalid math often **does not throw**.",
            '`"abc" * 5` is **NaN**. Check both sides are numbers **before** multiplying.',
        ],
        'let result = "abc" * 5;\nconsole.log(result);',
        outcome="**log: NaN**. `Number.isNaN(result)` is **true**. No exception.",
        script=console_script(
            'let result = "abc" * 5;\nconsole.log(result);\nconsole.log("Number.isNaN", Number.isNaN(result));'
        ),
    ),
    S(
        "cannot-read-property",
        "Cannot read property of undefined — user.name",
        [
            "One of the most common beginner errors: using **something that is not there**.",
            "`let user;` — the variable exists, the **object does not**. `user.name` is a TypeError.",
        ],
        "let user;\nconsole.log(user.name);",
        outcome="**TypeError: Cannot read properties of undefined (reading 'name')**.",
        script=console_script("let user;\nconsole.log(user.name);", catch=True),
    ),
    S(
        "error-meanings",
        "Cheat sheet: ReferenceError, TypeError, SyntaxError, NaN",
        [
            "**ReferenceError** — a **name** is not defined.",
            "**TypeError** — a **value** is used incorrectly.",
            "**SyntaxError** — **broken structure** (the script does not parse).",
            "**NaN** — **invalid math** (often silent).",
        ],
        'console.log("see outcomes");',
        outcome="Four labels, four different failures — do not treat them as the same bug.",
        script="""      function label(fn) {
        try { return fn(); }
        catch (e) { return e.name + ": " + e.message; }
      }
      let syn;
      try { new Function("if (x == 5 {"); syn = "ran"; }
      catch (e) { syn = e.name + ": " + e.message; }
      document.getElementById("demo").innerText =
        "ReferenceError -> " + label(function () { return myValue; }) + "\\n" +
        "TypeError -> " + label(function () { return (undefined).n; }) + "\\n" +
        "SyntaxError -> " + syn + "\\n" +
        "NaN -> " + String("abc" * 5);""",
    ),
    S(
        "fix-first-error",
        "Fix the first error before moving on",
        [
            "Do **not** ignore errors. **One** error often causes **many** later ones.",
            "Fix the **first** message in the console, reload, then look again.",
        ],
        'function first() { missingFn(); }\nfunction second() { console.log("never"); }\ntry { first(); second(); } catch (e) { console.log("stopped at", e.message); }',
        outcome='**stopped at missingFn is not defined**. **never** is **not** logged — `second()` did not run.',
        script=console_script(
            'function first() { missingFn(); }\nfunction second() { console.log("never"); }\ntry { first(); second(); } catch (e) { console.log("stopped at", e.message); }'
        ),
    ),
]


# ---------------------------------------------------------------------------
# 19.5 Debug Async
# ---------------------------------------------------------------------------

DATA_BLOB = (
    "const dataUrl = URL.createObjectURL(new Blob("
    '[JSON.stringify({ name: "Ada", ok: true })], { type: "application/json" }));\n'
)

ASYNC = [
    S(
        "fetch-then",
        'fetch("data.json").then(...).then(data => console.log(data))',
        [
            "**`fetch()` is asynchronous.** It does **not** return the JSON immediately.",
            "The page writes `fetch(\"data.json\")`. This sandbox uses a **Blob URL** so `fetch` works from `file://` (same `.then` shape).",
            "If **nothing appears**, check the console first.",
        ],
        'fetch("data.json")\n  .then(response => response.json())\n  .then(data => console.log(data));',
        outcome='After the promise resolves: **log: {"name":"Ada","ok":true}**. The `fetch("data.json")` form is what the page shows; the snap uses a Blob URL with the same chain.',
        script=console_async_script(
            DATA_BLOB
            + "fetch(dataUrl)\n  .then(response => response.json())\n  .then(data => console.log(data));"
        ),
        wait_ms=2500,
    ),
    S(
        "fetch-log-response",
        "Log the Response before calling .json()",
        [
            "Always **log the response** before using the data.",
            "`response.ok` / `response.status` tell you if the HTTP call **worked**.",
        ],
        'fetch("data.json")\n  .then(response => {\n    console.log(response);\n    return response.json();\n  })\n  .then(data => console.log(data));',
        outcome="First a **Response** snapshot (`ok`, `status` **200**), then the JSON **Ada** object.",
        script=console_async_script(
            DATA_BLOB
            + """fetch(dataUrl)
  .then(response => {
    console.log({ ok: response.ok, status: response.status, type: response.type });
    return response.json();
  })
  .then(data => console.log(data));"""
        ),
        wait_ms=2500,
    ),
    S(
        "network-tab-404",
        "Network tab: failed request / wrong path",
        [
            "Async bugs are often **network** problems. The **Network** tab shows status and path.",
            "Check **status**, **file path**, and whether the server returned an **error**.",
            "`fetch(\"wrong.json\")` fails here (no such file) — **TypeError: Failed to fetch** or a 404 depending on how the page is served.",
        ],
        'fetch("wrong.json")\n  .then(response => response.json())\n  .then(data => console.log(data))\n  .catch(error => console.error(error));',
        outcome="**error:** a failed fetch (TypeError **Failed to fetch**, or HTTP **404** when served over http). The catch ran; no JSON was logged.",
        script=console_async_script(
            """fetch("wrong.json")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));"""
        ),
        wait_ms=2500,
    ),
    S(
        "async-await",
        "async function loadData() { await fetch(...) }",
        [
            "**`async` / `await`** still run **later**. They only **look** synchronous.",
            "You can set breakpoints on **`await`** lines and step the same way as normal code.",
        ],
        'async function loadData() {\n  let response = await fetch("data.json");\n  let data = await response.json();\n  console.log(data);\n}\nloadData();',
        outcome='**log: {"name":"Ada","ok":true}** after both awaits finish.',
        script=console_async_script(
            DATA_BLOB
            + """async function loadData() {
  let response = await fetch(dataUrl);
  let data = await response.json();
  console.log(data);
}
loadData();"""
        ),
        wait_ms=2500,
    ),
    S(
        "async-try-catch",
        "try/catch around await — errors must be handled",
        [
            "Async errors **fail silently** unless you handle them.",
            "Wrap `await` in **`try...catch`** (or `.catch` on the promise).",
            "The page fetches **`wrong.json`** on purpose.",
        ],
        'async function loadData() {\n  try {\n    let response = await fetch("wrong.json");\n    let data = await response.json();\n    console.log(data);\n  } catch (error) {\n    console.error(error);\n  }\n}',
        outcome="**error:** fetch failed (or JSON parse on a 404 HTML page). **catch** ran; `console.log(data)` did not.",
        script=console_async_script(
            """async function loadData() {
  try {
    let response = await fetch("wrong.json");
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
loadData();"""
        ),
        wait_ms=2500,
    ),
    S(
        "missing-return",
        "Forgotten return — the promise result is dropped",
        [
            "A promise that **never seems to finish** is often a **missing `return`**.",
            "`getData()` calls `fetch` but **does not return** the chain. The caller gets **`undefined`**, not JSON.",
            "**Always return** promises when chaining.",
        ],
        'function getData() {\n  fetch("data.json")\n    .then(response => response.json());\n}',
        outcome="`getData()` returns **undefined**. The inner fetch still logs the JSON if you add a log inside, but **callers cannot `await` the data**.",
        script=console_async_script(
            DATA_BLOB
            + """function getDataBroken() {
  fetch(dataUrl).then(response => response.json());
}
function getDataFixed() {
  return fetch(dataUrl).then(response => response.json());
}
console.log("broken return", getDataBroken());
getDataFixed().then(function (data) {
  console.log("fixed data", data);
});"""
        ),
        wait_ms=2500,
    ),
    S(
        "async-checklist",
        "Async debugging checklist",
        [
            "Check the **console** for errors.",
            "Check the **Network** tab.",
            "**Log responses** before using them.",
            "Use **`try...catch`** with async functions.",
            "Set breakpoints on **`await`** lines.",
        ],
        "console.log(\"checklist: console, Network, log response, try/catch, await breakpoints\");",
        outcome="Five checks. Debugging is a **habit**, not a talent — the page’s closing line.",
        script=console_script(
            'console.log("checklist: console, Network, log response, try/catch, await breakpoints");'
        ),
    ),
]


# ---------------------------------------------------------------------------
# 19.6 Debug Reference — one Example per console method row
# ---------------------------------------------------------------------------

REFERENCE = [
    S(
        "assert",
        "assert() — logs only when the assertion is false",
        [
            "**`console.assert(condition, ...msg)`** writes **only if `condition` is falsy**.",
            "A **true** assertion prints **nothing** (keeps logs clean).",
        ],
        'console.assert(1 === 1, "this stays quiet");\nconsole.assert(1 === 2, "math is broken");',
        outcome="True assert: **no line**. False assert: **assert: Assertion failed: math is broken**.",
        script=console_script(
            'console.assert(1 === 1, "this stays quiet");\nconsole.assert(1 === 2, "math is broken");\nconsole.log("done");'
        ),
    ),
    S(
        "clear",
        "clear() — clears the console",
        [
            "**`console.clear()`** wipes previous console output.",
        ],
        'console.log("before");\nconsole.clear();\nconsole.log("after");',
        outcome="Capture shows **(console cleared)** then **log: after**. **before** is gone.",
        script=console_script(
            'console.log("before");\nconsole.clear();\nconsole.log("after");'
        ),
    ),
    S(
        "dir",
        "dir() — interactive listing of object properties",
        [
            "**`console.dir(obj)`** is a **property tree**, often more detailed than `log` for DOM nodes / complex objects.",
        ],
        'console.dir({ name: "John", age: 25 });',
        outcome='**dir: {"name":"John","age":25}**.',
        script=console_script('console.dir({ name: "John", age: 25 });'),
    ),
    S(
        "count",
        "count() — how many times this call ran",
        [
            "**`console.count(label)`** increments a counter for that **label** (default label is **`default`**).",
        ],
        'console.count("click");\nconsole.count("click");\nconsole.count("click");',
        outcome="**click: 1**, **click: 2**, **click: 3**.",
        script=console_script(
            'console.count("click");\nconsole.count("click");\nconsole.count("click");'
        ),
    ),
    S(
        "error",
        "error() — error-styled console message",
        [
            "**`console.error()`** highlights **critical** issues (often red). It does **not** throw.",
        ],
        'console.error("Something went wrong!");',
        outcome="**error: Something went wrong!**",
        script=console_script('console.error("Something went wrong!");'),
    ),
    S(
        "group",
        "group() — indent following messages until groupEnd()",
        [
            "**`console.group(label)`** starts an **expanded** inline group.",
            "Later messages are **indented** until **`console.groupEnd()`**.",
        ],
        'console.group("user");\nconsole.log("John");\nconsole.groupEnd();',
        outcome="**group: user**, then indented **log: John**, then **groupEnd**.",
        script=console_script(
            'console.group("user");\nconsole.log("John");\nconsole.groupEnd();'
        ),
    ),
    S(
        "group-collapsed",
        "groupCollapsed() — same group, starts collapsed",
        [
            "**`console.groupCollapsed()`** creates a group that is **collapsed** until you expand it in DevTools.",
        ],
        'console.groupCollapsed("details");\nconsole.log("hidden until expanded");\nconsole.groupEnd();',
        outcome="**groupCollapsed: details**, indented **log: hidden until expanded**, **groupEnd**.",
        script=console_script(
            'console.groupCollapsed("details");\nconsole.log("hidden until expanded");\nconsole.groupEnd();'
        ),
    ),
    S(
        "group-end",
        "groupEnd() — exits the current inline group",
        [
            "**`console.groupEnd()`** pops one group. Nested groups need **one `groupEnd` per `group`**.",
        ],
        'console.group("outer");\nconsole.group("inner");\nconsole.log("in");\nconsole.groupEnd();\nconsole.log("out");\nconsole.groupEnd();',
        outcome="**in** is indented twice. **out** is indented once (still in **outer**).",
        script=console_script(
            'console.group("outer");\nconsole.group("inner");\nconsole.log("in");\nconsole.groupEnd();\nconsole.log("out");\nconsole.groupEnd();'
        ),
    ),
    S(
        "info",
        "info() — informational console message",
        [
            "**`console.info()`** is an **info** log (filterable in DevTools). Similar to `log` with a different **level**.",
        ],
        'console.info("loaded");',
        outcome="**info: loaded**.",
        script=console_script('console.info("loaded");'),
    ),
    S(
        "log",
        "log() — general message; accepts multiple arguments",
        [
            "**`console.log()`** is the default. It accepts **multiple arguments** (text + objects).",
        ],
        'console.log("x", 10, { ok: true });',
        outcome='**log: x 10 {"ok":true}**.',
        script=console_script('console.log("x", 10, { ok: true });'),
    ),
    S(
        "table",
        "table() — tabular data as a table",
        [
            "**`console.table()`** is ideal for **arrays of objects**.",
        ],
        'console.table([{name:"John", age:25},{name:"Anna", age:30}]);',
        outcome='**table:** two rows with **name** / **age**.',
        script=console_script(
            'console.table([{name:"John", age:25},{name:"Anna", age:30}]);'
        ),
    ),
    S(
        "time",
        "time() — starts a named timer",
        [
            "**`console.time(label)`** starts a timer you later stop with **`timeEnd`**.",
        ],
        'console.time("work");\nconsole.log("timer running");',
        outcome='**time: started "work"** then **log: timer running**. Duration appears in **timeEnd**.',
        script=console_script(
            'console.time("work");\nconsole.log("timer running");'
        ),
    ),
    S(
        "time-end",
        "timeEnd() — stops a timer started by time()",
        [
            "**`console.timeEnd(label)`** prints elapsed milliseconds for that label.",
            "The exact ms **varies**. Expect a **small positive** number, not a fixed digit.",
        ],
        'console.time("work");\nfor (let i = 0; i < 10000; i++) {}\nconsole.timeEnd("work");',
        outcome='**timeEnd: "work":** a duration in **ms** (this engine; not a promised exact number).',
        script=console_script(
            'console.time("work");\nfor (let i = 0; i < 10000; i++) {}\nconsole.timeEnd("work");'
        ),
    ),
    S(
        "trace",
        "trace() — stack trace to the console",
        [
            "**`console.trace()`** prints a **stack** showing **how you got here**.",
        ],
        "function inner() { console.trace(\"from inner\"); }\nfunction outer() { inner(); }\nouter();",
        outcome="**trace:** a stack that includes **inner** then **outer** (plus the page script).",
        script=console_script(
            'function inner() { console.trace("from inner"); }\nfunction outer() { inner(); }\nouter();'
        ),
    ),
    S(
        "warn",
        "warn() — warning-styled message (often yellow)",
        [
            "**`console.warn()`** is like `log` with a **warning** level (filterable, often yellow).",
        ],
        'console.warn("This is a warning!");',
        outcome="**warn: This is a warning!**",
        script=console_script('console.warn("This is a warning!");'),
    ),
]


def run_all() -> None:
    sections = [
        (
            "js-debugging",
            "Debug Intro",
            INTRO,
            "Debugging is finding and fixing bugs. Code fails because of syntax errors or logic errors, and beginners often guess. The useful habit is Read the error → Reproduce → Reduce to a small example → Fix. If nothing visible happens, open the console (F12). This page’s Tryits: console.log Hello, log a total, string vs number +, ReferenceError, TypeError, = inside if vs ===, and a+b. The first known computer bug was a real insect in the electronics — the word stuck.",
            [
                "Bugs are **normal**. The skill is **locating** them quickly.",
                "**Read → Reproduce → Reduce → Fix.** Check **facts**, do not guess.",
                "Open **F12 → Console**. **`console.log`** is the first tool.",
                "**ReferenceError** = missing name. **TypeError** = impossible use of a value (often `undefined`).",
                "`if (x = 5)` **assigns**. Use **`===`** to compare.",
            ],
            [
                ('What does `console.log("Hello!")` put on the page?', ["**Nothing** in the HTML body.", "The **console** shows **Hello!**."]),
                ("What is `50 * 3` in the Total log?", ["**150**."]),
                ('What is `5 + "5"` vs `5 + Number("5")`?', ['**`"55"`** (string) vs **10** (number).']),
                ("What is `console.log(myValue)`?", ["**ReferenceError: myValue is not defined**."]),
                ("What is `(undefined).length`?", ["**TypeError: Cannot read properties of undefined (reading 'length')**."]),
                ("Does `if (x = 5)` run when `x` started at 10?", ["**Yes.** It **assigns 5** and the block runs.", "`x` is **5** afterward."]),
                ("Does `if (x === 5)` run when `x` is 10?", ["**No.** `x` stays **10**."]),
                ("What is `console.log(5 + 6)` in the last Tryit?", ["**11**."]),
                ("What is the four-step habit?", ["**Read → Reproduce → Reduce → Fix**."]),
                ("How do you open the console in Chrome?", ["**F12**, or More tools → Developer tools → **Console**.", "Or right-click → Inspect → Console."]),
            ],
            "Open the console first. Log values and types. ReferenceError is a missing name; TypeError is a bad operation (often undefined). Never use = when you meant ===. Reduce the bug to a tiny snippet, then fix one thing.",
            [
                ("JS Debugging (W3Schools)", "https://www.w3schools.com/js/js_debugging.asp"),
                ("MDN: console.log()", "https://developer.mozilla.org/en-US/docs/Web/API/console/log_static"),
                ("MDN: ReferenceError", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError"),
                ("MDN: TypeError", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError"),
            ],
        ),
        (
            "js-debugging-console",
            "Debug Console",
            CONSOLE,
            "The browser console is the main debugging tool for beginners. Keep it open while testing. This page’s Tryits cover console.log (message and variables), console.warn, console.error, logging several values, logging an object, and console.table for arrays of objects. Professionals log the value instead of guessing.",
            [
                "Right-click → **Inspect** → **Console** (Chrome / Edge), or **F12**.",
                "**`log`** general, **`warn`** suspicious, **`error`** failed (styled, **not** a throw).",
                "Pass **multiple arguments**. Log **objects**. Use **`table`** for arrays of objects.",
                "Do **not guess** — log the value.",
            ],
            [
                ('What does `console.log("Hello from JavaScript!")` print?', ["**Hello from JavaScript!**"]),
                ('What do `console.log(name)` and `console.log(age)` print for John / 25?', ["**John** then **25**."]),
                ("Does `console.warn` stop the script?", ["**No.** It is a **warning**. Execution continues."]),
                ('Does `console.error("Something went wrong!")` throw?', ["**No.** It only **styles** a message. The next statement can still run."]),
                ('What is `console.log("x =", 10, "y =", 5)`?', ["**x = 10 y = 5**."]),
                ("What does logging `{name:\"John\", age:25}` show?", ['**{"name":"John","age":25}** (expandable in DevTools).']),
                ("Why `console.table(users)`?", ["It shows **rows** (John 25, Anna 30) instead of a nested dump."]),
                ("What should you do instead of guessing a value?", ["**`console.log` it** and confirm."]),
            ],
            "Keep the console open. Use log, warn, error, multi-arg log, object log, and table. Confirm values; do not guess. Breakpoints come next when you need to pause.",
            [
                ("JS Debugging Console (W3Schools)", "https://www.w3schools.com/js/js_debugging_console.asp"),
                ("MDN: console", "https://developer.mozilla.org/en-US/docs/Web/API/console"),
                ("MDN: console.table()", "https://developer.mozilla.org/en-US/docs/Web/API/console/table_static"),
            ],
        ),
        (
            "js-debugging-breakpoints",
            "Debug Breakpoints",
            BREAKPOINTS,
            "Breakpoints pause JavaScript on a line so you can inspect real values. Set them in Sources by clicking line numbers, then reload. The debugger keyword is the same idea in source. When paused, Step Over / Into / Out control the next line. Scope shows locals vs globals. Watch tracks a name as it changes. Reload after adding a breakpoint; a breakpoint in a loop fires every iteration.",
            [
                "Click a **line number** in **Sources**, **reload**, use **play** to continue.",
                "**`debugger;`** pauses if DevTools is attached; otherwise it is a no-op.",
                "**Step Over / Into / Out**. **Scope** = locals vs globals. **Watch** = live expressions.",
                "Reload after setting. Loops pause **repeatedly**.",
            ],
            [
                ("What is the last `innerHTML` after four `add` calls?", ["**5010** (`add(10, 5000)`). Earlier results were overwritten."]),
                ("What is `add(10, 5)`?", ["**15**."]),
                ("What does `debugger` do with DevTools closed?", ["**Nothing.** No debugger is available."]),
                ("What is `15 * 5` in the debugger Tryit?", ["**75** — written to `#demo` after the pause point."]),
                ("Step Into vs Step Over at `total(3, 4)`?", ["**Into** enters **`double`**. **Over** runs the call as one line."]),
                ("Where does `y` exist in `function test() { let y = 5; }`?", ["**Only inside `test`.** Outside, `y` is **not defined**."]),
                ("What values would Watch `sum` show for `for (i=1; i<=3; i++) sum += i`?", ["**1**, then **3**, then **6**."]),
                ("Why did my new breakpoint never hit?", ["You probably **did not reload**. The previous run already finished."]),
            ],
            "Pause with a breakpoint or debugger, step through, read Scope and Watch, then resume. Reload after setting breakpoints. Use them when logging is not enough.",
            [
                ("JS Debugging Breakpoints (W3Schools)", "https://www.w3schools.com/js/js_debugging_breakpoints.asp"),
                ("MDN: debugger", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger"),
                ("MDN: Chrome DevTools breakpoints", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#debugging"),
            ],
        ),
        (
            "js-debugging-errors",
            "Debug Errors",
            ERRORS,
            "Error messages look scary; they are clues. Read the type, the short text, and the line number. ReferenceError is a missing name, TypeError is an illegal operation (often undefined/null), SyntaxError is broken source, and NaN is invalid math that usually does not throw. Fix the first error; it often causes the rest.",
            [
                "Parts: **type**, **message**, **line**.",
                "**ReferenceError** — name missing. **TypeError** — bad use (`.length` on `undefined`, `.name` on missing object).",
                "**SyntaxError** — will not parse (`if (x == 5 {`). **NaN** — `\"abc\" * 5`.",
                "Fix the **first** console error, then re-run.",
            ],
            [
                ("What three parts does an error message have?", ["**Type**, **explanation**, **line number**."]),
                ("What is `console.log(myValue)`?", ["**ReferenceError: myValue is not defined**."]),
                ("What is `let x; x.length`?", ["**TypeError: Cannot read properties of undefined (reading 'length')**."]),
                ("What is `if (x == 5 {`?", ["**SyntaxError**. The script does not parse."]),
                ('What is `"abc" * 5`?', ["**NaN**. It does **not** throw."]),
                ("What is `let user; user.name`?", ["**TypeError: Cannot read properties of undefined (reading 'name')**."]),
                ("Does SyntaxError get caught by try/catch in the same file?", ["**No.** Parsing fails **before** runtime."]),
                ("Why fix the first error first?", ["One failure **stops later lines** (or causes a cascade)."]),
            ],
            "Read type + message + line. ReferenceError vs TypeError vs SyntaxError vs silent NaN. Click the line number. Fix the first error, then look again.",
            [
                ("JS Debugging Errors (W3Schools)", "https://www.w3schools.com/js/js_debugging_errors.asp"),
                ("MDN: SyntaxError", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError"),
                ("MDN: NaN", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN"),
            ],
        ),
        (
            "js-debugging-async",
            "Debug Async",
            ASYNC,
            "Async code runs later, so bugs feel invisible. fetch does not return JSON immediately — chain .then or await. Log the Response before .json(). Use the Network tab for status and path. Handle errors with try/catch on async functions. A missing return drops the promise so callers see undefined. Debugging async is a checklist: console, Network, log responses, try/catch, breakpoints on await.",
            [
                "`fetch` / `await` run **when the work finishes**, not on the next source line.",
                "Log **`response`** (`ok`, `status`) before **`.json()`**.",
                "Failed paths (`wrong.json`) need **`.catch`** or **`try/catch`**.",
                "**Return** the promise if the caller needs the data.",
            ],
            [
                ("Does `fetch` return the JSON immediately?", ["**No.** You **`then`** or **`await`** the body."]),
                ("What JSON does the sandbox Blob fetch resolve to?", ['**{"name":"Ada","ok":true}** (stand-in for the page’s `data.json`).']),
                ("Why log `response` before `.json()`?", ["To see **ok** / **status** if the HTTP call failed."]),
                ("What happens on `fetch(\"wrong.json\")`?", ["**catch** / **console.error** — failed fetch or 404. No data log."]),
                ("Is `async/await` synchronous?", ["**No.** It still waits. It only **reads** top-to-bottom."]),
                ("What if you omit `try/catch` in an async function?", ["Rejections can look **silent** (unhandled promise)."]),
                ("What does `function getData() { fetch(...).then(...) }` return?", ["**`undefined`**. The promise is **not returned**."]),
                ("Name three async checklist items.", ["**Console**, **Network tab**, **log the response** (also try/catch and await breakpoints)."]),
            ],
            "Async runs later. Log responses, watch Network, catch errors, return promises, and breakpoint on await. The skill is habit, not talent.",
            [
                ("JS Debugging Async (W3Schools)", "https://www.w3schools.com/js/js_debugging_async.asp"),
                ("MDN: fetch()", "https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch"),
                ("MDN: async function", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function"),
                ("MDN: Using promises", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises"),
            ],
        ),
        (
            "js-debugging-reference",
            "Debug Reference",
            REFERENCE,
            "Full console method list (revised December 2026 on the page): assert, clear, dir, count, error, group, groupCollapsed, groupEnd, info, log, table, time, timeEnd, trace, warn. Each row below is a runnable demo. assert is silent when true. clear wipes the log. dir/table inspect structures. count tallies calls. group* indents. time/timeEnd measure. trace prints a stack.",
            [
                "One **Example per table row** — not a name list.",
                "**assert** silent if true. **clear** empties. **count** increments a label.",
                "**group / groupCollapsed / groupEnd** nest. **time / timeEnd** pair by **label**.",
                "**error** / **warn** / **info** / **log** differ by **level**, not by throwing.",
            ],
            [
                ("When does `console.assert` print?", ["Only when the condition is **falsy**."]),
                ("What does `console.clear()` do to earlier logs?", ["They **disappear**. Next logs start fresh."]),
                ("`console.count(\"click\")` three times?", ["**click: 1**, **2**, **3**."]),
                ("Does `console.error` throw?", ["**No.** It is a **styled log**."]),
                ("What does `group` + log + `groupEnd` do?", ["The log is **indented** inside the group label."]),
                ("`groupCollapsed` vs `group`?", ["Same grouping; collapsed **starts shut** in DevTools."]),
                ('`console.log("x", 10, {ok:true})`?', ['**x 10 {"ok":true}** — multiple arguments.']),
                ("What is `console.table` for?", ["**Arrays of objects** (rows/columns)."]),
                ("What does `time` / `timeEnd` print?", ["Elapsed **ms** for that **label** (exact value varies)."]),
                ("What is `console.trace()`?", ["A **stack trace** of the current call chain."]),
            ],
            "Use log/info/warn/error for levels, table/dir for structure, count for tallies, group* for nesting, time* for duration, assert for quiet checks, trace for stacks, and clear to reset.",
            [
                ("JS Debugging Reference (W3Schools)", "https://www.w3schools.com/js/js_debugging_reference.asp"),
                ("MDN: console", "https://developer.mozilla.org/en-US/docs/Web/API/console"),
                ("MDN: console.assert()", "https://developer.mozilla.org/en-US/docs/Web/API/console/assert_static"),
                ("MDN: console.time()", "https://developer.mozilla.org/en-US/docs/Web/API/console/time_static"),
            ],
        ),
    ]
    print("example counts:")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print(f"  {slug}: {len(recs)}  qa={len(qa)}")
        if not (8 <= len(qa) <= 15):
            raise SystemExit(f"{slug} Q&A count {len(qa)} not in 8-15")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print("building", slug, "examples", len(recs))
        build_and_snap(slug, title, recs, intro, concepts, qa, summary, refs)
        print("done", slug)


if __name__ == "__main__":
    run_all()
