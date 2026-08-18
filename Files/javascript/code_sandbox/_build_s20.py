"""S20: JS Style Guide, Best Practices, Mistakes, Performance."""
from __future__ import annotations

from _gen_lib import S, build_and_snap, console_script, nf_script, out_script


def catch_assign(js: str, expr: str) -> str:
    return f"""{js}
      let thrown = "(no throw)";
      try {{
        {expr}
      }} catch (e) {{
        thrown = e.name + ": " + e.message;
      }}
      document.getElementById("demo").innerText =
        document.getElementById("demo").innerText
          ? document.getElementById("demo").innerText + "\\n" + thrown
          : thrown;"""


# ---------------------------------------------------------------------------
# 20.1 JS Style Guide
# ---------------------------------------------------------------------------

STYLE = [
    S(
        "camelcase-names",
        "camelCase identifier names (firstName, lastName)",
        [
            "W3Schools uses **camelCase** for variables and functions. Names **start with a letter**.",
            "`firstName`, `lastName`, `fullPrice` — not `first_name` in their examples.",
        ],
        'firstName = "John";\nlastName = "Doe";\nprice = 19.90;\ntax = 0.20;\nfullPrice = price + (price * tax);',
        outcome='**fullPrice** is **23.88**. These assignments without `let`/`const` create **globals** in sloppy mode — the next chapter says to avoid that. The **names** are the lesson here.',
        script=out_script(
            'let firstName = "John";\nlet lastName = "Doe";\nlet price = 19.90;\nlet tax = 0.20;\nlet fullPrice = price + (price * tax);',
            [
                ("firstName", "firstName"),
                ("lastName", "lastName"),
                ("fullPrice", "fullPrice.toFixed(2)"),
            ],
        ),
    ),
    S(
        "spaces-around-operators",
        "Spaces around operators and after commas",
        [
            "Always put **spaces around operators** `= + - * /` and **after commas**.",
            "`let x = y + z;` not `let x=y+z;`.",
        ],
        'let x = y + z;\nconst myArray = ["Volvo", "Saab", "Fiat"];',
        outcome="`x` is **5** (`2 + 3`). `myArray` is **Volvo, Saab, Fiat**.",
        script=out_script(
            'let y = 2;\nlet z = 3;\nlet x = y + z;\nconst myArray = ["Volvo", "Saab", "Fiat"];',
            [("x", "x"), ("myArray", "myArray.join(\", \")")],
        ),
    ),
    S(
        "indent-two-spaces",
        "Indent code blocks with 2 spaces (not tabs)",
        [
            "Always use **2 spaces** for indentation.",
            "**Do not use tabs** — editors disagree on tab width.",
        ],
        "function toCelsius(fahrenheit) {\n  return (5 / 9) * (fahrenheit - 32);\n}",
        outcome="**toCelsius(32)** is **0**. **toCelsius(212)** is **100**.",
        script=out_script(
            "function toCelsius(fahrenheit) {\n  return (5 / 9) * (fahrenheit - 32);\n}",
            [("toCelsius(32)", "toCelsius(32)"), ("toCelsius(212)", "toCelsius(212)")],
        ),
    ),
    S(
        "semicolon-simple-statements",
        "End simple statements with a semicolon",
        [
            "Simple statements **end with `;`**.",
            "Arrays and objects used as **values** are simple statements when assigned.",
        ],
        'const cars = ["Volvo", "Saab", "Fiat"];\nconst person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50,\n  eyeColor: "blue"\n};',
        outcome="**cars.length** is **3**. **person.firstName** is **John**.",
        script=out_script(
            'const cars = ["Volvo", "Saab", "Fiat"];\nconst person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50,\n  eyeColor: "blue"\n};',
            [("cars.length", "cars.length"), ("person.firstName", "person.firstName")],
        ),
    ),
    S(
        "function-brackets",
        "Functions: `{` at end of first line; no semicolon after `}`",
        [
            "Compound statements: opening **`{` at the end of the first line**, one space before `{`.",
            "Closing **`}` on its own line**, **no leading spaces**, **no semicolon** after the block.",
        ],
        "function toCelsius(fahrenheit) {\n  return (5 / 9) * (fahrenheit - 32);\n}",
        outcome="Same function as the indent example. The **style** is: `{` on the signature line, `}` alone, no `;` after `}`.",
        script=out_script(
            "function toCelsius(fahrenheit) {\n  return (5 / 9) * (fahrenheit - 32);\n}",
            [("toCelsius(68)", "Math.round(toCelsius(68) * 100) / 100")],
        ),
    ),
    S(
        "loop-brackets",
        "for loop: `{` on the `for` line",
        [
            "Same bracket rule as functions: `for (...) {` then the body, then `}`.",
        ],
        "for (let i = 0; i < 5; i++) {\n  x += i;\n}",
        outcome="Starting `x = 0`, after `i = 0..4`, **x** is **10** (0+1+2+3+4).",
        script=out_script(
            "let x = 0;\nfor (let i = 0; i < 5; i++) {\n  x += i;\n}",
            [("x", "x")],
        ),
    ),
    S(
        "if-else-brackets",
        "if / else: `{` on the same line as if/else",
        [
            "`if (time < 20) {` ... `} else {` ... `}`.",
            "Do **not** put `{` on the next line in this style guide.",
        ],
        'if (time < 20) {\n  greeting = "Good day";\n} else {\n  greeting = "Good evening";\n}',
        outcome='With **time = 15**, greeting is **"Good day"**. With **time = 21**, **"Good evening"**.',
        script="""      function greet(time) {
        let greeting;
        if (time < 20) {
          greeting = "Good day";
        } else {
          greeting = "Good evening";
        }
        return greeting;
      }
      document.getElementById("demo").innerText =
        "time 15 -> " + greet(15) + "\\n" +
        "time 21 -> " + greet(21);""",
    ),
    S(
        "object-rules",
        "Object rules: `{` same line, colon-space, no trailing comma, `};`",
        [
            "Opening `{` on the **same line** as the assignment.",
            "**Colon + space** between property and value. **Quotes** around **strings**, not around numbers.",
            "**No comma** after the last property (W3Schools rule; trailing commas are legal in modern JS — they still warn for old IE / JSON).",
            "Closing `}` on a new line. **Always** end the definition with **`;`**.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50,\n  eyeColor: "blue"\n};',
        outcome="**person.age** is **50** (number, unquoted). **eyeColor** is **blue**.",
        script=out_script(
            'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50,\n  eyeColor: "blue"\n};',
            [("age", "person.age"), ("typeof age", "typeof person.age"), ("eyeColor", "person.eyeColor")],
        ),
    ),
    S(
        "short-object",
        "Short objects may be one compressed line",
        [
            "Short objects can sit on **one line**, spaces **between properties**.",
        ],
        'const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};',
        outcome="Same data as the multi-line object. **firstName** is **John**.",
        script=out_script(
            'const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};',
            [("firstName", "person.firstName"), ("age", "person.age")],
        ),
    ),
    S(
        "line-length-80",
        "Break long lines after an operator or comma (line length < 80)",
        [
            "Avoid lines **longer than 80 characters**.",
            "If a statement does not fit, break **after an operator or a comma**.",
            "This is the page’s Tryit: assign **Hello Dolly.** across two lines after `=`.",
        ],
        'document.getElementById("demo").innerHTML =\n"Hello Dolly.";',
        outcome="The paragraph reads **Hello Dolly.**",
        script="""      document.getElementById("demo").innerText =
"Hello Dolly.";""",
    ),
    S(
        "naming-hyphens-illegal",
        "Hyphens are not allowed in JavaScript names",
        [
            "HTML/CSS use hyphens (`data-price`, `font-size`). **JavaScript names cannot**.",
            "`first-name` is parsed as **subtraction** (`first - name`), or is a SyntaxError as a binding.",
        ],
        "// first-name = \"John\";  // illegal as a variable name\nconst firstName = \"John\";",
        outcome="**firstName** works. `let first-name` is a **SyntaxError**.",
        script=nf_script("let first-name = 'John';"),
    ),
    S(
        "naming-styles",
        "camelCase vs under_score vs PascalCase vs $",
        [
            "**camelCase** — JavaScript itself, jQuery, most JS libraries.",
            "**under_score** — common in SQL / PHP docs (`date_of_birth`).",
            "**PascalCase** — often constructors / classes (C-style too).",
            "**UPPERCASE** — common for globals/constants like **PI** (W3Schools say they don’t, but it is common).",
            "Do **not** start names with **`$`** — that collides with many library names.",
        ],
        'const firstName = "camel";\nconst date_of_birth = "underscore";\nconst Person = { kind: "PascalCase constructor style" };\nconst PI = 3.14;',
        outcome="All four bind. `$foo` as a name is **legal JS** but the style guide says **avoid it**.",
        script=out_script(
            'const firstName = "camel";\nconst date_of_birth = "underscore";\nconst Person = { kind: "PascalCase constructor style" };\nconst PI = 3.14;\nconst $foo = "legal but avoid";',
            [
                ("firstName", "firstName"),
                ("date_of_birth", "date_of_birth"),
                ("Person.kind", "Person.kind"),
                ("PI", "PI"),
                ("$foo", "$foo"),
            ],
        ),
    ),
    S(
        "script-src-no-type",
        'Load scripts with <script src="myscript.js"> (no type)',
        [
            "Use simple syntax for external scripts. The **`type` attribute is not necessary** (`text/javascript` is the default).",
        ],
        '<script src="myscript.js"></script>',
        outcome="The sandbox `myscript.js` sets **loaded = yes**. No `type=` needed.",
        script="""      document.getElementById("demo").innerText = "use: <script src=\\"myscript.js\\"></script>\\n(type attribute omitted)";""",
        body='<p id="note">External file: <code>myscript.js</code></p>',
    ),
    S(
        "html-id-case",
        'getElementById("Demo") vs getElementById("demo")',
        [
            "HTML **id** matching in `getElementById` is **case-sensitive**.",
            '`id="demo"` is **not** found as `"Demo"`. Untidy HTML + JS naming causes **null** and then TypeErrors.',
            "Use the **same** convention in HTML as in JS (camelCase / lowercase).",
        ],
        'const obj = document.getElementById("Demo");\nconst obj2 = document.getElementById("demo");',
        outcome="**Demo** is **null**. **demo** is the paragraph element. Always match case.",
        script="""      const obj = document.getElementById("Demo");
      const obj2 = document.getElementById("demo");
      document.getElementById("demo").innerText =
        'getElementById("Demo") -> ' + obj + "\\n" +
        'getElementById("demo") -> ' + (obj2 ? obj2.tagName + "#" + obj2.id : null);""",
        body='<p id="demo">target</p>',
    ),
    S(
        "file-extensions",
        "File extensions: .html .css .js",
        [
            "HTML: **`.html`** (`.htm` allowed). CSS: **`.css`**. JavaScript: **`.js`**.",
        ],
        "const files = [\"index.html\", \"style.css\", \"app.js\"];",
        outcome="Three conventional extensions. Servers and editors rely on them.",
        script=out_script(
            'const files = ["index.html", "style.css", "app.js"];',
            [("files", "files.join(\", \")")],
        ),
    ),
    S(
        "lowercase-filenames",
        "Use lower-case file names",
        [
            "**Apache / Unix** file names are **case-sensitive**: `london.jpg` ≠ `London.jpg`.",
            "**IIS / Windows** often are **not**. Mixing case **breaks** when you deploy to Linux.",
            "Prefer **all lower-case** names.",
        ],
        'const unix = "london.jpg" === "London.jpg";',
        outcome="In JavaScript string compare, **london.jpg === London.jpg** is **false** — same trap as a case-sensitive server.",
        script=out_script(
            'const unix = "london.jpg" === "London.jpg";',
            [("london.jpg === London.jpg", "unix")],
        ),
    ),
    S(
        "readability-vs-minify",
        "Readability in development; minify production",
        [
            "Computers **ignore** extra spaces. Conventions are for **humans**.",
            "Prefer **readability** while developing. **Minify** large production scripts.",
        ],
        "let x = 1 + 2;\nlet y=1+2;",
        outcome="Both **x** and **y** are **3**. Spaces did not change the result — only the **read** of the source.",
        script=out_script("let x = 1 + 2;\nlet y=1+2;", [("x", "x"), ("y", "y")]),
    ),
]


# ---------------------------------------------------------------------------
# 20.2 JS Best Practices
# ---------------------------------------------------------------------------

BEST = [
    S(
        "avoid-globals",
        "Avoid global variables — they can be overwritten",
        [
            "Minimize **globals** (all types, objects, functions). Another script can **overwrite** them.",
            "Prefer **local** variables and **closures**.",
        ],
        'var leaked = "global";\nfunction hide() {\n  let local = "local";\n  return local;\n}',
        outcome="**leaked** is visible as a global. **local** is **not** visible outside `hide` (**ReferenceError**).",
        script="""      var leaked = "global";
      function hide() {
        let local = "local";
        return local;
      }
      let localMsg;
      try { localMsg = local; } catch (e) { localMsg = e.name + ": " + e.message; }
      document.getElementById("demo").innerText =
        "leaked -> " + leaked + "\\n" +
        "hide() -> " + hide() + "\\n" +
        "bare local -> " + localMsg;""",
    ),
    S(
        "declare-locals",
        "Always declare local variables (var / let / const)",
        [
            "Undeclared assignments become **globals** (sloppy mode).",
            "**Strict mode** does **not** allow undeclared variables (**ReferenceError**).",
        ],
        'function sloppy() {\n  implicit = 1;\n}\nfunction strictish() {\n  "use strict";\n  implicit2 = 1;\n}',
        outcome="Sloppy `implicit = 1` creates a **global**. Strict assignment to `implicit2` is **ReferenceError: implicit2 is not defined**.",
        script="""      function sloppy() { implicit = 1; }
      sloppy();
      let strictMsg;
      try {
        (function () {
          "use strict";
          implicit2 = 1;
        })();
        strictMsg = "assigned";
      } catch (e) {
        strictMsg = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "global implicit -> " + implicit + "\\n" +
        "strict implicit2 -> " + strictMsg;""",
    ),
    S(
        "declarations-on-top",
        "Put all declarations at the top of the script or function",
        [
            "Cleaner code, one place to look, fewer implied globals, fewer accidental re-declarations.",
            "Also declare **loop** variables in the `for` head: `for (let i = 0; ...)`.",
        ],
        'let firstName, lastName, price, discount, fullPrice;\nfirstName = "John";\nlastName = "Doe";\nprice = 19.90;\ndiscount = 0.10;\nfullPrice = price - discount;',
        outcome="**fullPrice** is **19.8**. Names were declared **first**, assigned **later**.",
        script=out_script(
            'let firstName, lastName, price, discount, fullPrice;\nfirstName = "John";\nlastName = "Doe";\nprice = 19.90;\ndiscount = 0.10;\nfullPrice = price - discount;',
            [("firstName", "firstName"), ("fullPrice", "fullPrice")],
        ),
    ),
    S(
        "initialize-variables",
        "Initialize variables when you declare them",
        [
            "Avoid **undefined** placeholders. Initialization documents the **intended type**: `\"\"`, `0`, `[]`, `{}`.",
        ],
        'let firstName = "";\nlet lastName = "";\nlet price = 0;\nlet discount = 0;\nlet fullPrice = 0;\nconst myArray = [];\nconst myObject = {};',
        outcome='**firstName** is **`""`**. **price** is **0**. **myArray** is **[]**. **myObject** is **{}**. None are **undefined**.',
        script=out_script(
            'let firstName = "";\nlet price = 0;\nconst myArray = [];\nconst myObject = {};',
            [
                ("firstName", "JSON.stringify(firstName)"),
                ("price", "price"),
                ("Array.isArray(myArray)", "Array.isArray(myArray)"),
                ("typeof myObject", "typeof myObject"),
            ],
        ),
    ),
    S(
        "var-redeclare",
        "var carName = \"Volvo\"; var carName; keeps the value (not recommended)",
        [
            "Re-declaring **`var`** does **not** reset the value.",
            "Still **not recommended**. Prefer **`let` / `const`** (you **cannot** re-declare those).",
        ],
        'var carName = "Volvo";\nvar carName;',
        outcome="**carName** is still **Volvo** after the second `var carName;`.",
        script=out_script(
            'var carName = "Volvo";\nvar carName;',
            [("carName", "carName")],
        ),
    ),
    S(
        "let-redeclare",
        "let carName twice — SyntaxError",
        [
            "You **cannot** re-declare **`let`** in the same scope.",
        ],
        'let carName = "Volvo";\nlet carName;',
        outcome="**SyntaxError: Identifier 'carName' has already been declared** (via `new Function`; a raw script would not parse).",
        script=nf_script('let carName = "Volvo";\nlet carName;'),
    ),
    S(
        "const-redeclare",
        "const carName twice — SyntaxError",
        [
            "You **cannot** re-declare **`const`** in the same scope either.",
        ],
        'const carName = "Volvo";\nconst carName;',
        outcome="**SyntaxError: Identifier 'carName' has already been declared**.",
        script=nf_script('const carName = "Volvo";\nconst carName;'),
    ),
    S(
        "let-object-reassign",
        'let car = {...}; car = "Fiat" changes the type',
        [
            "`let` **allows** replacing an object with a string. That is a **type change** bug.",
        ],
        'let car = {type:"Fiat", model:"500", color:"white"};\ncar = "Fiat";  // Changes object to string',
        outcome='After assign, **car** is **"Fiat"** (`typeof` **string**), not an object.',
        script=out_script(
            'let car = {type:"Fiat", model:"500", color:"white"};\ncar = "Fiat";',
            [("car", "car"), ("typeof car", "typeof car")],
        ),
    ),
    S(
        "const-object-reassign",
        "const car = {...}; car = \"Fiat\" is not possible",
        [
            "**`const`** prevents **rebinding**. You may still **mutate** properties (`car.color = ...`).",
            "`car = \"Fiat\"` is **TypeError: Assignment to constant variable**.",
        ],
        'const car = {type:"Fiat", model:"500", color:"white"};\ncar = "Fiat";  // Not possible',
        outcome="**TypeError: Assignment to constant variable**. The object is unchanged.",
        script="""      const car = {type:"Fiat", model:"500", color:"white"};
      let thrown;
      try { car = "Fiat"; } catch (e) { thrown = e.name + ": " + e.message; }
      document.getElementById("demo").innerText =
        "thrown -> " + thrown + "\\n" +
        "car.type still -> " + car.type;""",
    ),
    S(
        "let-array-reassign",
        "let cars = [...]; cars = 3 changes array to number",
        [
            "Same type-change hole as objects: `let` arrays can be replaced with a number.",
        ],
        'let cars = ["Saab", "Volvo", "BMW"];\ncars = 3;',
        outcome="**cars** is **3**. **Array.isArray** is **false**.",
        script=out_script(
            'let cars = ["Saab", "Volvo", "BMW"];\ncars = 3;',
            [("cars", "cars"), ("Array.isArray(cars)", "Array.isArray(cars)")],
        ),
    ),
    S(
        "const-array-reassign",
        "const cars = [...]; cars = 3 is not possible",
        [
            "**`const`** blocks replacing the array. **`.push` still works** (mutating contents).",
        ],
        'const cars = ["Saab", "Volvo", "BMW"];\ncars = 3;  // Not possible',
        outcome="**TypeError: Assignment to constant variable**. `cars[0]` is still **Saab**.",
        script="""      const cars = ["Saab", "Volvo", "BMW"];
      let thrown;
      try { cars = 3; } catch (e) { thrown = e.name + ": " + e.message; }
      document.getElementById("demo").innerText =
        "thrown -> " + thrown + "\\n" +
        "cars[0] -> " + cars[0];""",
    ),
    S(
        "no-new-object",
        "Don't use new Object() — use literals",
        [
            'Use **`""`** not `new String()`, **`0`** not `new Number()`, **`false`** not `new Boolean()`.',
            "Use **`{}`** not `new Object()`, **`[]`** not `new Array()`, **`/()/`** not `new RegExp()`, **`function (){}`** not `new Function()`.",
        ],
        'let x1 = "";\nlet x2 = 0;\nlet x3 = false;\nconst x4 = {};\nconst x5 = [];\nconst x6 = /()/;\nconst x7 = function(){};',
        outcome="typeof: **string**, **number**, **boolean**, **object**, **object** (array), **object** (regexp), **function**.",
        script=out_script(
            'let x1 = "";\nlet x2 = 0;\nlet x3 = false;\nconst x4 = {};\nconst x5 = [];\nconst x6 = /()/;\nconst x7 = function(){};',
            [
                ("typeof x1", "typeof x1"),
                ("typeof x2", "typeof x2"),
                ("typeof x3", "typeof x3"),
                ("typeof x4", "typeof x4"),
                ("Array.isArray(x5)", "Array.isArray(x5)"),
                ("x6 instanceof RegExp", "x6 instanceof RegExp"),
                ("typeof x7", "typeof x7"),
            ],
        ),
    ),
    S(
        "type-change",
        'let x = "Hello"; x = 5 changes typeof to number',
        [
            "JavaScript is **loosely typed**. A variable can **change** data type.",
        ],
        'let x = "Hello";\nx = 5;',
        outcome='First **typeof** is **string**. After `x = 5`, **typeof** is **number**.',
        script="""      let x = "Hello";
      const first = typeof x;
      x = 5;
      document.getElementById("demo").innerText =
        "first typeof -> " + first + "\\n" +
        "after x = 5 -> " + typeof x;""",
    ),
    S(
        "plus-vs-minus-coercion",
        "5 + 7 is 12; 5 + \"7\" is \"57\"; 5 - \"7\" is -2",
        [
            "`+` with a string **concatenates**. `-` **coerces to number**.",
            '`5 - "x"` is **NaN** (`typeof` still **number**).',
        ],
        'let a = 5 + 7;\nlet b = 5 + "7";\nlet c = "5" + 7;\nlet d = 5 - 7;\nlet e = 5 - "7";\nlet f = "5" - 7;\nlet g = 5 - "x";',
        outcome="**12** number, **\"57\"** string, **\"57\"** string, **-2** number, **-2**, **-2**, **NaN**.",
        script=out_script(
            'let a = 5 + 7;\nlet b = 5 + "7";\nlet c = "5" + 7;\nlet d = 5 - 7;\nlet e = 5 - "7";\nlet f = "5" - 7;\nlet g = 5 - "x";',
            [
                ("5 + 7", "a + \" \" + typeof a"),
                ('5 + "7"', "JSON.stringify(b) + \" \" + typeof b"),
                ('"5" + 7', "JSON.stringify(c) + \" \" + typeof c"),
                ("5 - 7", "d"),
                ('5 - "7"', "e"),
                ('"5" - 7', "f"),
                ('5 - "x"', "String(g)"),
            ],
        ),
    ),
    S(
        "hello-minus-dolly",
        '"Hello" - "Dolly" returns NaN',
        [
            "Subtracting two strings does **not throw**. It returns **NaN**.",
        ],
        '"Hello" - "Dolly"',
        outcome="**NaN**. `Number.isNaN` is **true**.",
        script=out_script(
            'let x = "Hello" - "Dolly";',
            [("x", "String(x)"), ("Number.isNaN(x)", "Number.isNaN(x)")],
        ),
    ),
    S(
        "triple-equals",
        "Use === — 0 == \"\" is true; 0 === \"\" is false",
        [
            "**`==`** converts types first. **`===`** compares **value and type**.",
            '`0 == ""` **true**, `1 == "1"` **true**, `1 == true` **true**. All **false** with **`===`**.',
        ],
        '0 == "";\n1 == "1";\n1 == true;\n0 === "";\n1 === "1";\n1 === true;',
        outcome="Loose: **true, true, true**. Strict: **false, false, false**.",
        script=out_script(
            "",
            [
                ('0 == ""', '0 == ""'),
                ('1 == "1"', '1 == "1"'),
                ("1 == true", "1 == true"),
                ('0 === ""', '0 === ""'),
                ('1 === "1"', '1 === "1"'),
                ("1 === true", "1 === true"),
            ],
        ),
    ),
    S(
        "parameter-defaults-if",
        "Default a missing argument: if (y === undefined) y = 0",
        [
            "Missing arguments are **`undefined`** and can break math.",
            "Old pattern: `if (y === undefined) { y = 0; }`.",
        ],
        "function myFunction(x, y) {\n  if (y === undefined) {\n    y = 0;\n  }\n  return x + y;\n}",
        outcome="**myFunction(5)** is **5** (`y` defaulted to **0**). **myFunction(5, 2)** is **7**.",
        script=out_script(
            "function myFunction(x, y) {\n  if (y === undefined) {\n    y = 0;\n  }\n  return x + y;\n}",
            [("myFunction(5)", "myFunction(5)"), ("myFunction(5, 2)", "myFunction(5, 2)")],
        ),
    ),
    S(
        "default-parameters",
        "ES2015 default parameters: function (a = 1, b = 1)",
        [
            "ES2015: defaults in the **signature**. Cleaner than the `undefined` check.",
        ],
        "function add(a = 1, b = 1) {\n  return a + b;\n}",
        outcome="**add()** is **2**. **add(5)** is **6**. **add(5, 3)** is **8**.",
        script=out_script(
            "function add(a = 1, b = 1) {\n  return a + b;\n}",
            [("add()", "add()"), ("add(5)", "add(5)"), ("add(5, 3)", "add(5, 3)")],
        ),
    ),
    S(
        "switch-default",
        "Always end switch with default",
        [
            "Even if you think every case is covered, add **`default`**.",
            "The Tryit maps `getDay()` 0–6, then **Unknown**.",
        ],
        'switch (new Date().getDay()) {\n  case 0: day = "Sunday"; break;\n  case 1: day = "Monday"; break;\n  case 2: day = "Tuesday"; break;\n  case 3: day = "Wednesday"; break;\n  case 4: day = "Thursday"; break;\n  case 5: day = "Friday"; break;\n  case 6: day = "Saturday"; break;\n  default: day = "Unknown";\n}',
        outcome="A real weekday name for 0–6. Force **`switch (99)`** and **default** is **Unknown**.",
        script="""      function nameDay(n) {
        let day;
        switch (n) {
          case 0: day = "Sunday"; break;
          case 1: day = "Monday"; break;
          case 2: day = "Tuesday"; break;
          case 3: day = "Wednesday"; break;
          case 4: day = "Thursday"; break;
          case 5: day = "Friday"; break;
          case 6: day = "Saturday"; break;
          default: day = "Unknown";
        }
        return day;
      }
      document.getElementById("demo").innerText =
        "getDay() " + new Date().getDay() + " -> " + nameDay(new Date().getDay()) + "\\n" +
        "switch(99) -> " + nameDay(99);""",
    ),
    S(
        "string-vs-new-string",
        '"John" === new String("John") is false',
        [
            "Treat numbers, strings, booleans as **primitives**, not objects.",
            "`new String` is an **object**. Primitive **`===`** object is **false**. Also **slower**.",
        ],
        'let x = "John";\nlet y = new String("John");\n(x === y)',
        outcome="**x === y** is **false**. **typeof x** is **string**. **typeof y** is **object**.",
        script=out_script(
            'let x = "John";\nlet y = new String("John");',
            [("x === y", "x === y"), ("typeof x", "typeof x"), ("typeof y", "typeof y")],
        ),
    ),
    S(
        "new-string-equals-new-string",
        "new String(\"John\") == new String(\"John\") is false",
        [
            "Even **worse**: two String **objects** are never `==` equal (different references).",
        ],
        'let x = new String("John");\nlet y = new String("John");\n(x == y)',
        outcome="**x == y** is **false**. **x.valueOf() == y.valueOf()** is **true**.",
        script=out_script(
            'let x = new String("John");\nlet y = new String("John");',
            [("x == y", "x == y"), ("x.valueOf() == y.valueOf()", "x.valueOf() == y.valueOf()")],
        ),
    ),
    S(
        "avoid-eval",
        "Avoid eval() — it runs text as code",
        [
            "**`eval()`** runs a string as code. Almost never needed.",
            "It is a **security** problem (arbitrary code) and is slower.",
        ],
        'let x = eval("2 + 2");',
        outcome="**eval(\"2 + 2\")** is **4** — it **works**, and you still **should not** use it. `2 + 2` in source is the same result without eval.",
        script=out_script(
            'let x = eval("2 + 2");\nlet y = 2 + 2;',
            [("eval", "x"), ("plain 2 + 2", "y")],
        ),
    ),
]


# ---------------------------------------------------------------------------
# 20.3 JS Mistakes
# ---------------------------------------------------------------------------

MISTAKES = [
    S(
        "if-eqeq-10",
        "if (x == 10) is false when x is 0",
        [
            "`==` **compares**. `x` is **0**, so the condition is **false** (as expected).",
        ],
        "let x = 0;\nif (x == 10) { /* ... */ }",
        outcome="Condition is **false**. The block does **not** run.",
        script=out_script(
            "let x = 0;\nlet ran = false;\nif (x == 10) { ran = true; }",
            [("x == 10", "x == 10"), ("block ran", "ran")],
        ),
    ),
    S(
        "if-assign-10",
        "if (x = 10) is true — assignment, not comparison",
        [
            "`x = 10` **assigns 10**. The value of an assignment is the assigned value.",
            "**10 is truthy**, so the `if` runs — maybe **not** what you expected.",
        ],
        "let x = 0;\nif (x = 10) { /* ... */ }",
        outcome="Condition is **true**. **x** is now **10**. Block **ran**.",
        script=out_script(
            "let x = 0;\nlet ran = false;\nif (x = 10) { ran = true; }",
            [("x after", "x"), ("block ran", "ran")],
        ),
    ),
    S(
        "if-assign-0",
        "if (x = 0) is false — 0 is falsy",
        [
            "Assignment of **0** yields **0**, which is **falsy**.",
            "The block **does not run** — also surprising if you thought you were comparing.",
        ],
        "let x = 0;\nif (x = 0) { /* ... */ }",
        outcome="Condition is **false**. **x** is **0**. Block **did not run**.",
        script=out_script(
            "let x = 5;\nlet ran = false;\nif (x = 0) { ran = true; }",
            [("x after", "x"), ("block ran", "ran")],
        ),
    ),
    S(
        "loose-eq-string-10",
        '10 == "10" is true (loose comparison)',
        [
            "With **`==`**, data type **does not matter**. `10 == \"10\"` is **true**.",
        ],
        'let x = 10;\nlet y = "10";\nif (x == y) { /* true */ }',
        outcome="**true**. The `if` **runs**.",
        script=out_script(
            'let x = 10;\nlet y = "10";',
            [("x == y", "x == y")],
        ),
    ),
    S(
        "strict-eq-string-10",
        '10 === "10" is false (strict comparison)',
        [
            "With **`===`**, type **matters**. Number **10** is not string **\"10\"**.",
        ],
        'let x = 10;\nlet y = "10";\nif (x === y) { /* false */ }',
        outcome="**false**. The `if` does **not** run.",
        script=out_script(
            'let x = 10;\nlet y = "10";',
            [("x === y", "x === y")],
        ),
    ),
    S(
        "switch-case-10",
        "switch(x) case 10 matches number 10",
        [
            "**`switch` uses strict comparison** (`===`).",
            "`case 10:` matches number **10** — the page’s alert **Hello** would fire.",
        ],
        'let x = 10;\nswitch(x) {\n  case 10:\n    alert("Hello");\n}',
        outcome="Match: this sandbox records **Hello** instead of `alert`.",
        script="""      let x = 10;
      let msg = "(no match)";
      switch (x) {
        case 10:
          msg = "Hello";
      }
      document.getElementById("demo").innerText = "msg -> " + msg;""",
    ),
    S(
        "switch-case-string-10",
        'switch(x) case "10" does not match number 10',
        [
            '`case "10":` does **not** match number **10**. No alert.',
        ],
        'let x = 10;\nswitch(x) {\n  case "10":\n    alert("Hello");\n}',
        outcome="**no match**. Strict `===` fails between **10** and **\"10\"**.",
        script="""      let x = 10;
      let msg = "(no match)";
      switch (x) {
        case "10":
          msg = "Hello";
      }
      document.getElementById("demo").innerText = "msg -> " + msg;""",
    ),
    S(
        "plus-vs-concat",
        '10 + 5 is 15; 10 += "5" is "105"',
        [
            "**`+`** adds numbers **or** concatenates strings.",
            '`x = 10 + 5` → **15**. `y += "5"` → **`"105"`**.',
        ],
        'let x = 10;\nx = 10 + 5;\nlet y = 10;\ny += "5";',
        outcome="**x** is **15** (number). **y** is **\"105\"** (string).",
        script=out_script(
            'let x = 10;\nx = 10 + 5;\nlet y = 10;\ny += "5";',
            [("x", "x"), ("typeof x", "typeof x"), ("y", "JSON.stringify(y)"), ("typeof y", "typeof y")],
        ),
    ),
    S(
        "plus-two-variables",
        'x + y is 15 or "105" depending on y\'s type',
        [
            "When both are numbers: **15**. When `y` is **\"5\"**: **`\"105\"`**.",
        ],
        'let x = 10;\nlet y = 5;\nlet z = x + y;\nlet y2 = "5";\nlet z2 = x + y2;',
        outcome="**z** is **15**. **z2** is **\"105\"**.",
        script=out_script(
            'let x = 10;\nlet y = 5;\nlet z = x + y;\nlet y2 = "5";\nlet z2 = x + y2;',
            [("z", "z"), ("z2", "JSON.stringify(z2)")],
        ),
    ),
    S(
        "float-0-1-0-2",
        "0.1 + 0.2 is not 0.3",
        [
            "JS numbers are **IEEE-754 floats**. `0.1 + 0.2` is **0.30000000000000004**, not **0.3**.",
        ],
        "let x = 0.1;\nlet y = 0.2;\nlet z = x + y;",
        outcome="**z === 0.3** is **false**. **z** prints as **0.30000000000000004**.",
        script=out_script(
            "let x = 0.1;\nlet y = 0.2;\nlet z = x + y;",
            [("z", "z"), ("z === 0.3", "z === 0.3")],
        ),
    ),
    S(
        "float-fix",
        "(x * 10 + y * 10) / 10 is 0.3",
        [
            "Multiply to integers, add, divide back.",
        ],
        "let z = (x * 10 + y * 10) / 10;",
        outcome="**z** is **0.3**. **z === 0.3** is **true**.",
        script=out_script(
            "let x = 0.1;\nlet y = 0.2;\nlet z = (x * 10 + y * 10) / 10;",
            [("z", "z"), ("z === 0.3", "z === 0.3")],
        ),
    ),
    S(
        "break-statement-ok",
        "You may break a statement after = across two lines",
        [
            "A statement may continue on the next line after **`=`**.",
        ],
        'let x =\n"Hello World!";',
        outcome='**x** is **"Hello World!"**.',
        script=out_script(
            'let x =\n"Hello World!";',
            [("x", "x")],
        ),
    ),
    S(
        "break-string-bad",
        "Breaking in the middle of a string is a SyntaxError",
        [
            "A newline **inside quotes** (no backslash) **does not parse**.",
        ],
        'let x = "Hello\nWorld!";',
        outcome="**SyntaxError: Invalid or unexpected token** (unterminated string).",
        script=nf_script('let x = "Hello\nWorld!";'),
    ),
    S(
        "break-string-backslash",
        r"Backslash continues a string across lines",
        [
            "Use a **backslash** at the end of the line to continue the string.",
            "Modern code often prefers a **template literal** instead.",
        ],
        'let x = "Hello \\\nWorld!";',
        outcome='**x** is **"Hello World!"** (the newline after `\\` is not in the string).',
        script=out_script(
            'let x = "Hello \\\nWorld!";',
            [("x", "JSON.stringify(x)")],
        ),
    ),
    S(
        "misplaced-semicolon",
        "if (x == 19);{ } always runs the block",
        [
            "The **`;` after `if (...)`** ends the `if` with an **empty** statement.",
            "The `{ }` that follows is a **separate block** that **always runs**.",
        ],
        "if (x == 19);\n{\n  // code block\n}",
        outcome="Even with **x = 0**, the block **runs** (`ran` is **true**). Without the extra `;`, it would not.",
        script="""      let x = 0;
      let ranBad = false;
      if (x == 19);
      {
        ranBad = true;
      }
      let ranGood = false;
      if (x == 19) {
        ranGood = true;
      }
      document.getElementById("demo").innerText =
        "with extra semicolon, block ran -> " + ranBad + "\\n" +
        "normal if, block ran -> " + ranGood;""",
    ),
    S(
        "return-no-semicolons",
        "return a * power works without semicolons (ASI)",
        [
            "ASI will insert semicolons. This function still returns **`a * 10`**.",
        ],
        "function myFunction(a) {\n  let power = 10\n  return a * power\n}",
        outcome="**myFunction(2)** is **20**.",
        script=out_script(
            "function myFunction(a) {\n  let power = 10\n  return a * power\n}",
            [("myFunction(2)", "myFunction(2)")],
        ),
    ),
    S(
        "return-with-semicolons",
        "return a * power with semicolons — same result",
        [
            "Explicit semicolons: same **20**.",
        ],
        "function myFunction(a) {\n  let power = 10;\n  return a * power;\n}",
        outcome="**myFunction(2)** is **20**.",
        script=out_script(
            "function myFunction(a) {\n  let power = 10;\n  return a * power;\n}",
            [("myFunction(2)", "myFunction(2)")],
        ),
    ),
    S(
        "return-break-after-star",
        "You may break after `return a *` onto the next line",
        [
            "`return a *` is an **incomplete** statement, so ASI waits for **`power`**.",
        ],
        "function myFunction(a) {\n  let power = 10;\n  return a *\n  power;\n}",
        outcome="**myFunction(2)** is still **20**.",
        script=out_script(
            "function myFunction(a) {\n  let power = 10;\n  return a *\n  power;\n}",
            [("myFunction(2)", "myFunction(2)")],
        ),
    ),
    S(
        "return-newline",
        "Never break after return — it becomes return;",
        [
            "`return` on its own line is a **complete** statement. ASI inserts **`return;`**.",
            "The next line `a * power` is **dead code**. The function returns **`undefined`**.",
        ],
        "function myFunction(a) {\n  let power = 10;\n  return\n  a * power;\n}",
        outcome="**myFunction(2)** is **undefined**.",
        script=out_script(
            "function myFunction(a) {\n  let power = 10;\n  return\n  a * power;\n}",
            [("myFunction(2)", "String(myFunction(2))")],
        ),
    ),
    S(
        "return-semicolon-explained",
        "ASI reads that as return; a * power;",
        [
            "Equivalent code: `return;` then `a * power;` as a useless expression statement.",
            "**Never break a return statement.**",
        ],
        "function myFunction(a) {\n  let power = 10;\n  return;\n  a * power;\n}",
        outcome="Same as the broken line-break: **undefined**.",
        script=out_script(
            "function myFunction(a) {\n  let power = 10;\n  return;\n  a * power;\n}",
            [("myFunction(2)", "String(myFunction(2))")],
        ),
    ),
    S(
        "array-numbered-indexes",
        "Arrays use numbered indexes — length 3, person[0] is John",
        [
            "JS arrays are **not** associative. Use **numbers**.",
        ],
        'const person = [];\nperson[0] = "John";\nperson[1] = "Doe";\nperson[2] = 46;',
        outcome="**length** is **3**. **person[0]** is **John**.",
        script=out_script(
            'const person = [];\nperson[0] = "John";\nperson[1] = "Doe";\nperson[2] = 46;',
            [("length", "person.length"), ("person[0]", "person[0]")],
        ),
    ),
    S(
        "array-named-indexes",
        'person["firstName"] turns the array into a plain object',
        [
            "Named indexes **do not** make an associative array. The value becomes a **normal object**.",
            "**`length`** is **0**. **`person[0]`** is **undefined**. Array methods break.",
        ],
        'const person = [];\nperson["firstName"] = "John";\nperson["lastName"] = "Doe";\nperson["age"] = 46;',
        outcome="**length** is **0**. **person[0]** is **undefined**. **person.firstName** is **John**.",
        script=out_script(
            'const person = [];\nperson["firstName"] = "John";\nperson["lastName"] = "Doe";\nperson["age"] = 46;',
            [
                ("length", "person.length"),
                ("person[0]", "String(person[0])"),
                ("person.firstName", "person.firstName"),
                ("Array.isArray(person)", "Array.isArray(person)"),
            ],
        ),
    ),
    S(
        "trailing-comma-js",
        "Trailing commas in objects/arrays are legal in ES5",
        [
            "`{age:46,}` and `[10,]` are **legal** in modern JavaScript.",
            "The page **warns**: IE8 could crash. **JSON does not allow** trailing commas.",
        ],
        'person = {firstName:"John", lastName:"Doe", age:46,};\npoints = [40, 100, 1, 5, 25, 10,];',
        outcome="JS accepts both. **person.age** is **46**. **points.length** is **6**.",
        script=out_script(
            'const person = {firstName:"John", lastName:"Doe", age:46,};\nconst points = [40, 100, 1, 5, 25, 10,];',
            [("person.age", "person.age"), ("points.length", "points.length")],
        ),
    ),
    S(
        "trailing-comma-json",
        "JSON.parse rejects trailing commas",
        [
            "JSON must **not** have a trailing comma.",
        ],
        'JSON.parse(\'{"firstName":"John","age":46,}\')',
        outcome="**SyntaxError: Expected double-quoted property name** (or unexpected token) — JSON parse fails.",
        script="""      let ok, bad;
      try { ok = JSON.parse('{"firstName":"John","age":46}'); }
      catch (e) { ok = e.name + ": " + e.message; }
      try { bad = JSON.parse('{"firstName":"John","age":46,}'); }
      catch (e) { bad = e.name + ": " + e.message; }
      document.getElementById("demo").innerText =
        "valid JSON -> " + JSON.stringify(ok) + "\\n" +
        "trailing comma -> " + bad;""",
    ),
    S(
        "typeof-undefined",
        'if (typeof myObj === "undefined") is safe',
        [
            "**`typeof`** of a missing binding is **`\"undefined\"`** and does **not throw**.",
        ],
        'if (typeof myObj === "undefined") { /* missing */ }',
        outcome='**typeof myObj** is **"undefined"**. The `if` is **true**.',
        script=out_script(
            "",
            [('typeof myObj === "undefined"', 'typeof myObj === "undefined"')],
        ),
    ),
    S(
        "null-check-order",
        "Test typeof !== undefined before !== null",
        [
            "`if (myObj === null)` **throws ReferenceError** if `myObj` was never declared.",
            "`if (myObj !== null && typeof myObj !== \"undefined\")` still **throws** — it **reads `myObj` first**.",
            "**Correct:** `typeof myObj !== \"undefined\" && myObj !== null`.",
        ],
        'if (typeof myObj !== "undefined" && myObj !== null) { /* ok */ }',
        outcome="Correct order: **false** (undeclared), **no throw**. Reversed `myObj !== null` first is **ReferenceError: myObj is not defined**.",
        script="""      let correct;
      try {
        correct = (typeof myObj !== "undefined" && myObj !== null);
      } catch (e) {
        correct = e.name + ": " + e.message;
      }
      let wrong;
      try {
        wrong = (myObj !== null && typeof myObj !== "undefined");
      } catch (e) {
        wrong = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "typeof first -> " + correct + "\\n" +
        "myObj first -> " + wrong;""",
    ),
]


# ---------------------------------------------------------------------------
# 20.4 JS Performance
# ---------------------------------------------------------------------------

PERF = [
    S(
        "loop-length-inside",
        "Bad: arr.length read every iteration",
        [
            "Every statement in a loop runs **each** iteration — including `i < arr.length`.",
            "That **works**, but re-reads **`.length`** every time.",
        ],
        "for (let i = 0; i < arr.length; i++) {\n  // ...\n}",
        outcome="With 4 items, the loop still visits **0..3**. Result **sum** is **10** (1+2+3+4).",
        script=out_script(
            "const arr = [1, 2, 3, 4];\nlet sum = 0;\nfor (let i = 0; i < arr.length; i++) {\n  sum += arr[i];\n}",
            [("sum", "sum")],
        ),
    ),
    S(
        "loop-length-cached",
        "Better: cache arr.length outside the comparison",
        [
            "`let l = arr.length;` then `i < l` — **length** is read **once**.",
            "Same results; fewer property lookups (the page’s performance tip).",
        ],
        "let l = arr.length;\nfor (let i = 0; i < l; i++) {\n  // ...\n}",
        outcome="**sum** is still **10**. **l** is **4**.",
        script=out_script(
            "const arr = [1, 2, 3, 4];\nlet l = arr.length;\nlet sum = 0;\nfor (let i = 0; i < l; i++) {\n  sum += arr[i];\n}",
            [("l", "l"), ("sum", "sum")],
        ),
    ),
    S(
        "reduce-dom-access",
        "Cache getElementById instead of searching the DOM twice",
        [
            "**DOM access is slow** compared with plain JS.",
            "If you need the node **several times**, store it: `const obj = document.getElementById(\"demo\")`.",
        ],
        'const obj = document.getElementById("demo");\nobj.innerHTML = "Hello";',
        outcome="The paragraph reads **Hello** after **one** lookup.",
        script="""      const obj = document.getElementById("demo");
      obj.innerText = "Hello";""",
        body="<p id=\"demo\">(empty)</p>",
    ),
    S(
        "reduce-dom-size",
        "Keep the DOM small — search is cheaper",
        [
            "Fewer elements → faster **load**, **render**, and **`getElementsByTagName` / query**.",
            "This demo counts **p** nodes in a tiny vs larger subtree.",
        ],
        "document.getElementsByTagName(\"p\").length",
        outcome="**small** subtree has **2** paragraphs. **large** has **20**. Searching the large tree visits more nodes.",
        script="""      function countP(n) {
        const root = document.createElement("div");
        for (let i = 0; i < n; i++) root.appendChild(document.createElement("p"));
        return root.getElementsByTagName("p").length;
      }
      document.getElementById("demo").innerText =
        "small (2) -> " + countP(2) + "\\n" +
        "large (20) -> " + countP(20);""",
    ),
    S(
        "avoid-extra-variable",
        "Don't create a variable you never reuse",
        [
            "If you only use `fullName` once, write the expression **in place**.",
        ],
        'let fullName = firstName + " " + lastName;\ndocument.getElementById("demo").innerHTML = fullName;\n// better:\ndocument.getElementById("demo").innerHTML = firstName + " " + lastName;',
        outcome='Both paths write **"Ada Lovelace"**. The second skips the extra binding.',
        script="""      const firstName = "Ada";
      const lastName = "Lovelace";
      const withVar = firstName + " " + lastName;
      const inline = firstName + " " + lastName;
      document.getElementById("demo").innerText =
        "with variable -> " + withVar + "\\n" +
        "inline -> " + inline;""",
    ),
    S(
        "defer-script",
        'Delay JS: put scripts at the bottom, or defer, or onload inject',
        [
            "A script at the **bottom of `<body>`** lets HTML parse first.",
            "**`defer`** (external scripts) runs after parse. The page writes `defer=\"true\"`; HTML boolean **`defer`** is enough (`<script src=\"...\" defer>`).",
            "Or inject after load: `window.onload = function () { const el = document.createElement(\"script\"); el.src = \"myScript.js\"; document.body.appendChild(el); };`",
            "While a script downloads, the browser may **block** other work. HTTP/1.1 also limited parallel downloads (the page still mentions **two** parallel components — modern HTTP/2+ is more parallel).",
        ],
        'window.onload = function() {\n  const element = document.createElement("script");\n  element.src = "myScript.js";\n  document.body.appendChild(element);\n};',
        outcome="This page already loaded, so the demo **appends** a tiny inline script immediately and records **injected**. Same idea as onload injection.",
        script="""      const element = document.createElement("script");
      element.textContent = "window.__injected = true;";
      document.body.appendChild(element);
      document.getElementById("demo").innerText =
        "injected -> " + window.__injected + "\\n" +
        "prefer: script at end of body, or src + defer";""",
    ),
    S(
        "avoid-with",
        "Avoid with — slow, clutters scope, illegal in strict mode",
        [
            "**`with`** is a performance and **scope** hazard.",
            "In **strict mode** it is a **SyntaxError**.",
        ],
        'with (Math) {\n  x = cos(0);\n}',
        outcome="Sloppy `with (Math) { cos(0) }` is **1**. Strict `with` is **SyntaxError: Strict mode code may not include a with statement**.",
        script="""      let sloppy;
      (function () {
        let x;
        with (Math) { x = cos(0); }
        sloppy = x;
      })();
      let strictMsg;
      try {
        new Function('"use strict"; with (Math) { return cos(0); }')();
        strictMsg = "ran";
      } catch (e) {
        strictMsg = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "sloppy with cos(0) -> " + sloppy + "\\n" +
        "strict with -> " + strictMsg;""",
    ),
]


def run_all() -> None:
    sections = [
        (
            "js-style-guide",
            "JS Style Guide",
            STYLE,
            "Coding conventions are agreed style: names, whitespace, indentation, comments, and practices. They improve readability and maintenance. W3Schools uses camelCase, spaces around operators, 2-space indent (not tabs), semicolons on simple statements, K&R braces for functions/loops/ifs, object rules (colon-space, no trailing comma in their guide, `};`), lines under 80 characters, script src without type, matching HTML ids, .html/.css/.js extensions, and lower-case file names. Computers ignore extra spaces — minify only for production.",
            [
                "**camelCase** names. **Spaces** around `= + - * /` and after commas.",
                "**2 spaces**, not tabs. Simple statements end with **`;`. Compound `}` has **no** semicolon.",
                "Objects: `{` same line, **colon space**, optional short one-liner, **`;`** after `}`.",
                "Break long lines **after** an operator/comma. **No hyphens** in JS names. Avoid leading **`$`**.",
                "`getElementById` is **case-sensitive**. Prefer **lower-case** file names.",
            ],
            [
                ("What naming style does W3Schools use?", ["**camelCase**, starting with a **letter**."]),
                ("Spaces around `+`?", ["**Yes.** `let x = y + z;` not `x=y+z;`."]),
                ("Tabs for indent?", ["**No.** Use **2 spaces**."]),
                ("Semicolon after a function `}`?", ["**No.** Compound blocks do **not** take a trailing `;`."]),
                ("Where do you break a long line?", ["After an **operator** or **comma**. Keep under **~80** chars."]),
                ("Is `first-name` a legal JS variable?", ["**No.** Hyphens are **subtraction** / **SyntaxError**."]),
                ('Does `getElementById("Demo")` find `id="demo"`?', ["**No.** It returns **null**. IDs are **case-sensitive**."]),
                ("`london.jpg` vs `London.jpg` on Unix?", ["**Different files.** Use **lower-case** names."]),
                ("Do extra spaces change `1+2`?", ["**No.** `1 + 2` is still **3**. Minify for **production size**, not correctness."]),
                ("Need `type=\"text/javascript\"` on `<script src>`?", ["**No.** The default is already JavaScript."]),
            ],
            "Pick one style and keep it: camelCase, 2 spaces, operator spacing, K&R braces, semicolons on simple statements, short lines, matching HTML ids, lower-case filenames. Style is for readers; minify only when shipping large scripts.",
            [
                ("JS Style Guide (W3Schools)", "https://www.w3schools.com/js/js_conventions.asp"),
                ("MDN: JavaScript guidelines", "https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide/Code_style_guide/JavaScript"),
                ("HTML Style Guide (W3Schools)", "https://www.w3schools.com/html/html5_syntax.asp"),
            ],
        ),
        (
            "js-best-practices",
            "JS Best Practices",
            BEST,
            "Avoid global variables, avoid new wrappers, avoid ==, avoid eval(). Declare locals with let/const (strict mode forbids undeclared assigns). Declare at the top and initialize. var redeclare keeps the value; let/const redeclare is a SyntaxError. const stops rebinding objects/arrays (not mutation). Prefer literals over new String/Number/Boolean/Object/Array/RegExp/Function. Watch + concatenation vs - coercion. Use ===. Default parameters. End switch with default. Never treat primitives as objects. eval is a security footgun.",
            [
                "**No implied globals.** Strict mode throws **ReferenceError** on undeclared assigns.",
                "**`const`** for objects/arrays you must not **replace**. **`let`** still allows type changes.",
                "Literals, not **`new String()`** etc. **`===`**, not **`==`**. **No `eval`**.",
                "Default parameters (or `y === undefined`). **`default:`** on every **switch**.",
            ],
            [
                ("What is an undeclared `implicit = 1` in sloppy mode?", ["A **global**."]),
                ("Same assign in strict mode?", ["**ReferenceError: implicit2 is not defined**."]),
                ('`var carName = "Volvo"; var carName;`?', ["Still **Volvo**. Do not rely on this."]),
                ("`let carName` twice?", ["**SyntaxError: Identifier 'carName' has already been declared**."]),
                ('`const car = {}; car = "Fiat"`?', ["**TypeError: Assignment to constant variable**."]),
                ('`5 + "7"` vs `5 - "7"`?', ['**`"57"`** (string) vs **-2** (number).']),
                ('`0 == ""` vs `0 === ""`?', ["**true** vs **false**."]),
                ("`add()` with `function add(a=1,b=1)`?", ["**2**."]),
                ('`"John" === new String("John")`?', ["**false** (primitive vs object)."]),
                ("`new String(\"John\") == new String(\"John\")`?", ["**false** (two objects)."]),
                ("Should you use `eval(\"2+2\")`?", ["**No.** It works (**4**) but is **unsafe** and unnecessary."]),
                ("`switch(99)` with a default?", ["**Unknown** in this demo."]),
            ],
            "Declare locals, initialize, prefer const, literals, ===, default parameters, and switch default. Do not leak globals, wrap primitives with new, or call eval.",
            [
                ("JS Best Practices (W3Schools)", "https://www.w3schools.com/js/js_best_practices.asp"),
                ("MDN: Strict mode", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode"),
                ("MDN: Equality comparisons", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness"),
                ("MDN: eval()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval"),
            ],
        ),
        (
            "js-mistakes",
            "JS Mistakes",
            MISTAKES,
            "Common mistakes: = inside if (assignment is truthy/falsy), == vs ===, switch’s strict case matching, + adding vs concatenating, 0.1+0.2, breaking strings, a semicolon after if (), breaking after return (ASI → undefined), named array indexes, trailing commas in JSON, and testing null before typeof on an undeclared name.",
            [
                "`if (x = 10)` **assigns**. `if (x = 0)` is **falsy**.",
                "**switch** uses **`===`**. `case \"10\":` misses number **10**.",
                "`0.1 + 0.2 !== 0.3`. Scale by **10** to fix this example.",
                "**Never** put **`;` after `if ()`**. **Never** break after **`return`**.",
                "Named array indexes **drop** `length`. JSON **forbids** trailing commas. **`typeof` first**, then **`!== null`**.",
            ],
            [
                ("`if (x = 10)` when x started 0?", ["**true**. **x** becomes **10**. Block runs."]),
                ("`if (x = 0)`?", ["**false** (0 is falsy). Block skipped."]),
                ('`10 == "10"` vs `10 === "10"`?', ["**true** vs **false**."]),
                ('`switch(10) { case "10": }`?', ["**No match** (strict)."]),
                ('`10 + 5` vs `10 += "5"`?', ["**15** vs **`\"105\"`**."]),
                ("`0.1 + 0.2 === 0.3`?", ["**false**."]),
                ("`(0.1*10 + 0.2*10)/10 === 0.3`?", ["**true**."]),
                ("`if (x==19); { ran = true }` with x=0?", ["The block **still runs**. The `;` emptied the if."]),
                ("`return` then newline then `a * power`?", ["Returns **undefined** (ASI inserted `return;`)."]),
                ('`person["firstName"] = "John"` on `[]`?', ["**length 0**, **person[0]** undefined, **person.firstName** John."]),
                ("`JSON.parse` with a trailing comma?", ["**SyntaxError**."]),
                ("Safe undeclared null check?", ['`typeof myObj !== "undefined" && myObj !== null`.']),
            ],
            "Compare with ===, never assign inside if, remember switch is strict, watch +, fix floats by scaling, do not break strings or return, do not name-index arrays, and typeof before null.",
            [
                ("JS Mistakes (W3Schools)", "https://www.w3schools.com/js/js_mistakes.asp"),
                ("MDN: Automatic semicolon insertion", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion"),
                ("MDN: switch", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch"),
                ("ECMA-262: Number values", "https://tc39.es/ecma262/#sec-ecmascript-language-types-number-type"),
            ],
        ),
        (
            "js-performance",
            "JS Performance",
            PERF,
            "Speed tips from the page: cache array length outside the loop, cache DOM lookups, keep the DOM small, skip variables you never reuse, delay script loading (bottom of body, defer, or inject on load), and never use with (illegal in strict mode). Extra spaces do not matter to the CPU in small scripts; DOM and network usually dominate.",
            [
                "Hoist **`arr.length`**. Cache **`getElementById`**.",
                "Fewer DOM nodes → faster search/render.",
                "Load JS **late** (`defer` / bottom / onload inject).",
                "**No `with`.** Strict mode **SyntaxError**.",
            ],
            [
                ("Why cache `arr.length`?", ["So each iteration does not **re-read** the property."]),
                ("Does caching length change 1+2+3+4?", ["**No.** **sum** is still **10**."]),
                ("How should you set innerHTML twice on #demo?", ["**One** `getElementById`, reuse the **node**."]),
                ("Why a small DOM?", ["Faster **load**, **render**, and **tag searches**."]),
                ("Need `fullName` if you print it once?", ["**No.** Inline `firstName + \" \" + lastName`."]),
                ("What does `defer` do?", ["Runs the **external** script **after HTML parse**."]),
                ("Is `with` allowed in strict mode?", ["**No.** **SyntaxError: Strict mode code may not include a with statement**."]),
                ("Sloppy `with (Math) { cos(0) }`?", ["**1** — and you still should **not** write this."]),
            ],
            "Cache lengths and DOM nodes, keep markup lean, load scripts late, and avoid with. Measure real bottlenecks (DOM, network) before micro-optimizing arithmetic.",
            [
                ("JS Performance (W3Schools)", "https://www.w3schools.com/js/js_performance.asp"),
                ("MDN: <script> defer", "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#defer"),
                ("MDN: with", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with"),
                ("MDN: Document.getElementById()", "https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById"),
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
