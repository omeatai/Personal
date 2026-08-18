"""S17: JS Data Types through JS Destructuring (12 W3Schools pages)."""
from __future__ import annotations

import json

from _gen_lib import S, build_and_snap

# Date-only ISO is UTC midnight. This machine is Mountain (UTC−6 / UTC−7).
TZ = (
    "Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**. "
    "In this Mountain zone, local `toString` / `toLocaleString` can fall on the **previous** calendar evening."
)
FIX = 'const d = new Date("2021-03-25T15:30:45.123Z");'


def catch_script(
    setup: str,
    attempts: list[tuple[str, str]],
    *,
    strict: bool = False,
) -> str:
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
    return f"""      let msg;
      try {{
        new Function({json.dumps(snippet)})();
        msg = "ran without error";
      }} catch (e) {{
        msg = e.name + ": " + e.message;
      }}
      document.getElementById("demo").innerText =
        msg + "\\n" + "(caught via new Function; a raw <script> would fail to parse)";"""


def builtins() -> list[dict]:
    """Built-in object types table — one Example per named row."""
    return [
        S(
            "obj-array",
            "Array",
            [
                "An **Array** is a list of values at a **numeric index** (0-based).",
                "`typeof` an array is **\"object\"**. Use **`Array.isArray`** to recognize it.",
            ],
            'const cars = ["Saab", "Volvo", "BMW"];',
            [
                ("cars", "String(cars)"),
                ("cars[0]", "cars[0]"),
                ("typeof cars", "typeof cars"),
                ("Array.isArray(cars)", "Array.isArray(cars)"),
            ],
            'Print is **Saab,Volvo,BMW**. cars[0] is **"Saab"**. typeof is **"object"**. `Array.isArray` is **true**.',
        ),
        S(
            "obj-map",
            "Map",
            [
                "A **Map** holds **key-value** pairs. Keys may be **any** type (not just strings).",
            ],
            'const m = new Map([["apples", 500], ["bananas", 300]]);\nlet n = m.get("apples");',
            [
                ('m.get("apples")', "n"),
                ("m.size", "m.size"),
                ("typeof m", "typeof m"),
            ],
            'get("apples") is **500**. size is **2**. typeof is **"object"**.',
        ),
        S(
            "obj-set",
            "Set",
            [
                "A **Set** stores **unique** values. Duplicates are kept once.",
            ],
            'const s = new Set(["A", "B", "A"]);\nlet n = s.size;',
            [
                ("s.size", "n"),
                ("s.has(\"A\")", 's.has("A")'),
                ("typeof s", "typeof s"),
            ],
            "size is **2** (the second **\"A\"** was ignored). `has(\"A\")` is **true**. typeof is **\"object\"**.",
        ),
        S(
            "obj-weakmap",
            "WeakMap",
            [
                "A **WeakMap** is a Map whose keys are **objects** held **weakly** (not enumerable).",
                "You cannot list keys. You **can** `get` / `set` / `has` while the key object lives.",
            ],
            'const key = { id: 1 };\nconst wm = new WeakMap();\nwm.set(key, "secret");',
            [
                ("wm.get(key)", "wm.get(key)"),
                ("wm.has(key)", "wm.has(key)"),
                ("String(wm)", "String(wm)"),
            ],
            'get(key) is **"secret"**. has(key) is **true**. String(wm) is **[object WeakMap]**.',
        ),
        S(
            "obj-weakset",
            "WeakSet",
            [
                "A **WeakSet** is a Set of **objects** with **weak** references. Not enumerable.",
            ],
            "const item = { id: 1 };\nconst ws = new WeakSet();\nws.add(item);",
            [
                ("ws.has(item)", "ws.has(item)"),
                ("String(ws)", "String(ws)"),
            ],
            "has(item) is **true**. String(ws) is **[object WeakSet]**.",
        ),
        S(
            "obj-math",
            "Math",
            [
                "**Math** is a built-in object of constants and functions (`PI`, `abs`, …).",
                "It is **not** a constructor — do not call `new Math()`.",
            ],
            "let pi = Math.PI;\nlet abs = Math.abs(-3);",
            [
                ("Math.PI", "pi"),
                ("Math.abs(-3)", "abs"),
                ("typeof Math", "typeof Math"),
            ],
            "Math.PI is **3.141592653589793**. abs(-3) is **3**. typeof Math is **\"object\"**.",
        ),
        S(
            "obj-date",
            "Date",
            [
                "A **Date** object stores an instant in time.",
                TZ,
            ],
            'const date = new Date("2022-03-25");',
            [
                ("date", "String(date)"),
                ("date.toISOString()", "date.toISOString()"),
                ("typeof date", "typeof date"),
            ],
            "ISO is **2022-03-25T00:00:00.000Z**. Local print is **Thu Mar 24 2022 18:00:00 GMT-0600**. typeof is **\"object\"**.",
        ),
        S(
            "obj-regexp",
            "RegExp",
            [
                "A **RegExp** tests and matches text patterns.",
            ],
            'const pat = /w3/i;\nlet ok = pat.test("W3Schools");',
            [
                ("String(pat)", "String(pat)"),
                ('pat.test("W3Schools")', "ok"),
                ("typeof pat", "typeof pat"),
            ],
            'String(pat) is **/w3/i**. test("W3Schools") is **true**. typeof is **"object"**.',
        ),
        S(
            "obj-error",
            "Error",
            [
                "An **Error** object represents a failure (`name` + `message`).",
            ],
            'const err = new Error("Oops");',
            [
                ("err.name", "err.name"),
                ("err.message", "err.message"),
                ("String(err)", "String(err)"),
            ],
            'name is **"Error"**. message is **"Oops"**. String(err) is **"Error: Oops"**.',
        ),
        S(
            "obj-json",
            "JSON",
            [
                "**JSON** is an object with **`stringify`** and **`parse`** — not a constructor.",
            ],
            'const obj = { name: "John" };\nlet text = JSON.stringify(obj);\nlet back = JSON.parse(text);',
            [
                ("text", "text"),
                ("back.name", "back.name"),
                ("typeof JSON", "typeof JSON"),
            ],
            'stringify is **{"name":"John"}**. back.name is **"John"**. typeof JSON is **"object"**.',
        ),
        S(
            "obj-promise",
            "Promise",
            [
                "A **Promise** represents completion or failure of an async operation.",
                "`typeof` a Promise is **\"object\"**. Check with **`instanceof Promise`**.",
            ],
            'const p = Promise.resolve("ok");',
            [
                ("typeof p", "typeof p"),
                ("p instanceof Promise", "p instanceof Promise"),
                ("String(p)", "String(p)"),
            ],
            'typeof is **"object"**. instanceof Promise is **true**. String(p) is **[object Promise]**.',
        ),
        S(
            "obj-int8array",
            "Int8Array",
            [
                "**Int8Array** stores fixed-size **8-bit signed** integers (−128…127).",
            ],
            "const a = new Int8Array([1, 2, 3]);",
            [("a", "String(a)"), ("a.length", "a.length"), ("a.BYTES_PER_ELEMENT", "a.BYTES_PER_ELEMENT")],
            "Print is **1,2,3**. length **3**. BYTES_PER_ELEMENT **1**.",
        ),
        S(
            "obj-int16array",
            "Int16Array",
            [
                "**Int16Array** stores fixed-size **16-bit signed** integers.",
            ],
            "const a = new Int16Array([1, 2, 3]);",
            [("a", "String(a)"), ("a.BYTES_PER_ELEMENT", "a.BYTES_PER_ELEMENT")],
            "Print is **1,2,3**. BYTES_PER_ELEMENT **2**.",
        ),
        S(
            "obj-int32array",
            "Int32Array",
            [
                "**Int32Array** stores fixed-size **32-bit signed** integers.",
            ],
            "const a = new Int32Array([1, 2, 3]);",
            [("a", "String(a)"), ("a.BYTES_PER_ELEMENT", "a.BYTES_PER_ELEMENT")],
            "Print is **1,2,3**. BYTES_PER_ELEMENT **4**.",
        ),
        S(
            "obj-float16array",
            "Float16Array",
            [
                "**Float16Array** stores fixed-size **16-bit** floating-point values (newer engines).",
                "This Chrome screenshot engine **does** define it.",
            ],
            "const a = new Float16Array([1.5, 2]);",
            [("a", "String(a)"), ("a.constructor.name", "a.constructor.name"), ("typeof Float16Array", "typeof Float16Array")],
            "Print is **1.5,2**. constructor.name is **Float16Array**. typeof Float16Array is **\"function\"**.",
        ),
        S(
            "obj-float32array",
            "Float32Array",
            [
                "**Float32Array** stores fixed-size **32-bit** floating-point values.",
            ],
            "const a = new Float32Array([1.5, 2]);",
            [("a", "String(a)"), ("a.BYTES_PER_ELEMENT", "a.BYTES_PER_ELEMENT")],
            "Print is **1.5,2**. BYTES_PER_ELEMENT **4**.",
        ),
        S(
            "obj-float64array",
            "Float64Array",
            [
                "**Float64Array** stores fixed-size **64-bit** floating-point values (same width as Number).",
            ],
            "const a = new Float64Array([1.5, 2]);",
            [("a", "String(a)"), ("a.BYTES_PER_ELEMENT", "a.BYTES_PER_ELEMENT")],
            "Print is **1.5,2**. BYTES_PER_ELEMENT **8**.",
        ),
        S(
            "obj-bigint64array",
            "BigInt64Array",
            [
                "**BigInt64Array** stores fixed-size **64-bit BigInt** values. Elements are **`n`** integers.",
            ],
            "const a = new BigInt64Array([10n, 20n]);",
            [("a", "String(a)"), ("a[0]", "a[0]"), ("typeof a[0]", "typeof a[0]")],
            "Print is **10,20**. a[0] is **10n**. typeof a[0] is **\"bigint\"**.",
        ),
    ]


# ---------------------------------------------------------------------------
# 17.1 JS Data Types
# ---------------------------------------------------------------------------

DATA_TYPES = [
    S(
        "type-number",
        "Number",
        [
            "**Number** is a numeric value. JavaScript numbers are **64-bit floats** (IEEE-754).",
            "Integers and decimals use the **same** type.",
        ],
        "let length = 16;\nlet weight = 7.5;",
        [("length", "length"), ("weight", "weight"), ("typeof length", "typeof length")],
        "length is **16**, weight is **7.5**. typeof length is **\"number\"**.",
    ),
    S(
        "type-bigint-n",
        "BigInt — n suffix (exact)",
        [
            "**BigInt** holds integers bigger than `Number.MAX_SAFE_INTEGER`.",
            "A trailing **`n`** makes a BigInt **literal** — exact.",
        ],
        "let x = 1234567890123456789012345n;",
        [("x", "x"), ("typeof x", "typeof x")],
        "x is **1234567890123456789012345n**. typeof is **\"bigint\"**.",
    ),
    S(
        "type-bigint-number-arg",
        "BigInt(number) loses precision",
        [
            "`BigInt(1234567890123456789012345)` first creates a **Number**, then converts.",
            "That Number is **not** exact past 2^53 − 1, so the BigInt is **wrong**.",
        ],
        "let y = BigInt(1234567890123456789012345);\nlet x = 1234567890123456789012345n;",
        [("y", "y"), ("x === y", "x === y")],
        "y is **1234567890123456824475648n**, not the digits in the source. `x === y` is **false**. Prefer **`n`** or **`BigInt(\"…\")`**.",
    ),
    S(
        "type-string",
        "String",
        [
            "A **String** is text in **quotes** (single or double).",
        ],
        'let color = "Yellow";\nlet lastName = "Johnson";',
        [("color", "color"), ("lastName", "lastName"), ("typeof color", "typeof color")],
        'color is **"Yellow"**, lastName is **"Johnson"**. typeof is **"string"**.',
    ),
    S(
        "type-boolean",
        "Boolean",
        [
            "A **Boolean** is only **`true`** or **`false`**.",
        ],
        "let x = true;\nlet y = false;",
        [("x", "x"), ("y", "y"), ("typeof x", "typeof x")],
        "x is **true**, y is **false**. typeof is **\"boolean\"**.",
    ),
    S(
        "type-undefined",
        "Undefined",
        [
            "A declared variable with **no assignment** is **`undefined`**. The type is also **undefined**.",
        ],
        "let x;\nlet y;",
        [("x", "x"), ("typeof x", "typeof x")],
        "x is **undefined**. typeof x is **\"undefined\"**.",
    ),
    S(
        "type-null",
        "Null",
        [
            "**`null`** is an assignment value meaning **intentional absence**.",
            "`typeof null` is **\"object\"** — a **legacy bug**, not proof that null is an object.",
        ],
        "let x = null;\nlet y = null;",
        [("x", "x"), ("typeof x", "typeof x")],
        "x is **null**. typeof x is **\"object\"** (legacy).",
    ),
    S(
        "type-symbol",
        "Symbol",
        [
            "A **Symbol** is a unique primitive identifier. Two `Symbol()` calls are **never** `===`.",
        ],
        "const x = Symbol();\nconst y = Symbol();",
        [("typeof x", "typeof x"), ("x === y", "x === y")],
        'typeof x is **"symbol"**. `x === y` is **false**.',
    ),
    S(
        "type-object",
        "Object",
        [
            "An **Object** is a collection of **name:value** properties in `{ }`.",
        ],
        'const person = {firstName:"John", lastName:"Doe"};',
        [
            ("person.firstName", "person.firstName"),
            ("typeof person", "typeof person"),
            ("String(person)", "String(person)"),
        ],
        'firstName is **"John"**. typeof is **"object"**. String(person) is **[object Object]**.',
    ),
    S(
        "add-number-string",
        '16 + "Volvo" — number then string',
        [
            "When you **add** a number and a string, JS treats the number as a **string**.",
        ],
        'let x = 16 + "Volvo";',
        [("x", "x"), ("typeof x", "typeof x")],
        'x is **"16Volvo"**. typeof is **"string"**.',
    ),
    S(
        "add-string-number",
        '"Volvo" + 16 — string then number',
        [
            "Same rule from the other side: **`+`** with a string **concatenates**.",
        ],
        'let x = "Volvo" + 16;',
        [("x", "x")],
        'x is **"Volvo16"**.',
    ),
    S(
        "add-left-numbers-then-string",
        '16 + 4 + "Volvo" — left to right',
        [
            "JS evaluates **left to right**. `16 + 4` is numeric **20**, then `20 + \"Volvo\"` concatenates.",
        ],
        'let x = 16 + 4 + "Volvo";',
        [("x", "x")],
        'x is **"20Volvo"**.',
    ),
    S(
        "add-string-then-numbers",
        '"Volvo" + 16 + 4 — string first',
        [
            "If the **first** operand is a string, later `+` operands become strings too.",
        ],
        'let x = "Volvo" + 16 + 4;',
        [("x", "x")],
        'x is **"Volvo164"** (not Volvo20).',
    ),
    S(
        "dynamic-types",
        "Dynamic types — same variable, new type",
        [
            "JavaScript types are **dynamic**: one variable may hold **undefined**, then a **number**, then a **string**.",
        ],
        'let x;          // undefined\nx = 5;          // Number\nx = "John";     // String',
        [("x", "x"), ("typeof x", "typeof x")],
        'After the last assignment, x is **"John"** and typeof is **"string"**.',
    ),
    S(
        "typeof-strings",
        'typeof strings — "", "John", "John Doe"',
        [
            "`typeof` returns **\"string\"** for every string, including **empty**.",
        ],
        'typeof "";\ntypeof "John";\ntypeof "John Doe";',
        [
            ('typeof ""', 'typeof ""'),
            ('typeof "John"', 'typeof "John"'),
            ('typeof "John Doe"', 'typeof "John Doe"'),
        ],
        'All three are **"string"**.',
    ),
    S(
        "typeof-numbers",
        "typeof numbers — 0, 314, 3.14, (3), (3+4)",
        [
            "`typeof` a number (integer, decimal, or parenthesized expression) is **\"number\"**.",
        ],
        "typeof 0;\ntypeof 314;\ntypeof 3.14;\ntypeof (3);\ntypeof (3 + 4);",
        [
            ("typeof 0", "typeof 0"),
            ("typeof 314", "typeof 314"),
            ("typeof 3.14", "typeof 3.14"),
            ("typeof (3)", "typeof (3)"),
            ("typeof (3 + 4)", "typeof (3 + 4)"),
        ],
        'All five are **"number"**. `(3 + 4)` is **7**, still a number.',
    ),
] + builtins()


# ---------------------------------------------------------------------------
# 17.2 JS Primitive Data
# ---------------------------------------------------------------------------

PRIMITIVES = [
    S(
        "string-quotes",
        "Strings — double or single quotes",
        [
            "Strings use **double** or **single** quotes. Both are the same type.",
        ],
        'let carName1 = "Volvo XC60";\nlet carName2 = \'Volvo XC60\';',
        [("carName1", "carName1"), ("carName2", "carName2"), ("carName1 === carName2", "carName1 === carName2")],
        'Both are **"Volvo XC60"**. They **===** each other.',
    ),
    S(
        "string-quotes-inside",
        "Quotes inside a string",
        [
            "You may put quotes **inside** a string if they **differ** from the outer quotes.",
        ],
        'let answer1 = "It\'s alright";\nlet answer2 = "He is called \'Johnny\'";\nlet answer3 = \'He is called "Johnny"\';',
        [("answer1", "answer1"), ("answer2", "answer2"), ("answer3", "answer3")],
        'answer1 is **"It\'s alright"**. answer2 is **"He is called \'Johnny\'"**. answer3 is **"He is called \\"Johnny\\""**.',
    ),
    S(
        "number-decimals",
        "Numbers with or without decimals",
        [
            "All JS numbers are **64-bit floating point**. `34.00` and `34` are the same numeric value.",
        ],
        "let x1 = 34.00;\nlet x2 = 34;",
        [("x1", "x1"), ("x2", "x2"), ("x1 === x2", "x1 === x2"), ("typeof x1", "typeof x1")],
        "Both are **34**. `x1 === x2` is **true**. typeof is **\"number\"**.",
    ),
    S(
        "number-exponential",
        "Exponential notation — 123e5 and 123e-5",
        [
            "**Scientific notation**: `e5` means × 10^5, `e-5` means × 10^−5.",
        ],
        "let y = 123e5;\nlet z = 123e-5;",
        [("y", "y"), ("z", "z")],
        "y is **12300000**. z is **0.00123**.",
    ),
    S(
        "bigint-from-string",
        'BigInt("123456789012345678901234567890")',
        [
            "`BigInt(\"…\")` parses a **string** of digits — exact, unlike `BigInt(number)`.",
        ],
        'let x = BigInt("123456789012345678901234567890");',
        [("x", "x"), ("typeof x", "typeof x")],
        "x is **123456789012345678901234567890n**. typeof is **\"bigint\"**.",
    ),
    S(
        "bigint-mix-typeerror",
        "BigInt + Number is TypeError",
        [
            "You **cannot mix** BigInt and Number in arithmetic. The engine throws **TypeError**.",
        ],
        "1n + 1;",
        outcome="**TypeError: Cannot mix BigInt and other types, use explicit conversions**.",
        script=catch_script("", [("1n + 1", "1n + 1")]),
    ),
    S(
        "boolean-compare",
        "Boolean from == comparison",
        [
            "Booleans are only **true** / **false**. Comparisons produce booleans.",
        ],
        "let x = 5;\nlet y = 5;\nlet z = 6;",
        [("x == y", "x == y"), ("x == z", "x == z")],
        "`x == y` is **true**. `x == z` is **false**.",
    ),
    S(
        "typeof-strings",
        'typeof strings — "", "John", "John Doe"',
        [
            "`typeof` on string values returns **\"string\"**.",
        ],
        'typeof "";\ntypeof "John";\ntypeof "John Doe";',
        [
            ('typeof ""', 'typeof ""'),
            ('typeof "John"', 'typeof "John"'),
            ('typeof "John Doe"', 'typeof "John Doe"'),
        ],
        'All three are **"string"**.',
    ),
    S(
        "typeof-numbers",
        "typeof numbers — 0, 314, 3.14, (3), (3+4)",
        [
            "`typeof` on number values returns **\"number\"**.",
        ],
        "typeof 0;\ntypeof 314;\ntypeof 3.14;\ntypeof (3);\ntypeof (3 + 4);",
        [
            ("typeof 0", "typeof 0"),
            ("typeof 314", "typeof 314"),
            ("typeof 3.14", "typeof 3.14"),
            ("typeof (3)", "typeof (3)"),
            ("typeof (3 + 4)", "typeof (3 + 4)"),
        ],
        'All five are **"number"**.',
    ),
    S(
        "undefined-declared",
        "let car — value and type undefined",
        [
            "A variable declared with **no value** is **`undefined`**. `typeof` is also **\"undefined\"**.",
        ],
        "let car;",
        [("car", "car"), ("typeof car", "typeof car")],
        "car is **undefined**. typeof is **\"undefined\"**.",
    ),
    S(
        "set-undefined",
        "car = undefined — emptied",
        [
            "Any variable can be **emptied** by assigning **`undefined`**. Type stays **undefined**.",
        ],
        'let car = "Volvo";\ncar = undefined;',
        [("car", "car"), ("typeof car", "typeof car")],
        "After the assignment, car is **undefined** and typeof is **\"undefined\"**.",
    ),
    S(
        "empty-string",
        'Empty string "" is not undefined',
        [
            "An **empty string** is a real value with type **string**. It is **not** undefined.",
        ],
        'let car = "";',
        [("car", "JSON.stringify(car)"), ("typeof car", "typeof car")],
        'value is **""**. typeof is **"string"** (JSON.stringify shows the quotes).',
    ),
    S(
        "null-assign",
        "let carName = null",
        [
            "You may assign **`null`** to mean “no object”.",
        ],
        "let carName = null;",
        [("carName", "carName"), ("typeof carName", "typeof carName")],
        "carName is **null**. typeof is **\"object\"** (legacy quirk — **null is still a primitive**).",
    ),
    S(
        "null-typeof-object",
        'typeof null is "object" (legacy)',
        [
            "`typeof null` returns **\"object\"**. This is a **historical bug**, not a classification.",
            "Null is still a **primitive**.",
        ],
        "typeof null;",
        [("typeof null", "typeof null")],
        'typeof null is **"object"**.',
    ),
    S(
        "null-eq-undefined",
        "null === vs == undefined",
        [
            "**`===`** needs the same type: `null === undefined` is **false**.",
            "**`==`** coerces: `null == undefined` is **true**. Prefer **`===`** when checking null.",
        ],
        "null === null;\nnull === undefined;\nnull == undefined;",
        [
            ("null === null", "null === null"),
            ("null === undefined", "null === undefined"),
            ("null == undefined", "null == undefined"),
        ],
        "`null === null` is **true**. `null === undefined` is **false**. `null == undefined` is **true**.",
    ),
]


# ---------------------------------------------------------------------------
# 17.3 JS Object Types
# ---------------------------------------------------------------------------

OBJECT_TYPES = [
    S(
        "person-object",
        "Person object with 4 properties",
        [
            "Objects use **`{ }`**. Properties are **name:value** pairs separated by commas.",
        ],
        'const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};',
        [
            ("person.firstName", "person.firstName"),
            ("person.age", "person.age"),
            ("typeof person", "typeof person"),
        ],
        'firstName is **"John"**, age is **50**. typeof is **"object"**.',
    ),
    S(
        "array-tryit",
        'Array cars = ["Saab", "Volvo", "BMW"]',
        [
            "Arrays use **`[ ]`**. Indexes are **0-based**: first item is `[0]`.",
        ],
        'const cars = ["Saab", "Volvo", "BMW"];',
        [
            ("cars[0]", "cars[0]"),
            ("cars[1]", "cars[1]"),
            ("cars[2]", "cars[2]"),
            ("cars.length", "cars.length"),
        ],
        '[0] **"Saab"**, [1] **"Volvo"**, [2] **"BMW"**. length **3**.',
    ),
    S(
        "typeof-strings",
        'typeof strings — "", "John", "John Doe"',
        [
            "This page repeats the string `typeof` Tryit. Strings are **not** objects.",
        ],
        'typeof "";\ntypeof "John";\ntypeof "John Doe";',
        [
            ('typeof ""', 'typeof ""'),
            ('typeof "John"', 'typeof "John"'),
            ('typeof "John Doe"', 'typeof "John Doe"'),
        ],
        'All three are **"string"**.',
    ),
    S(
        "typeof-numbers",
        "typeof numbers — 0, 314, 3.14, (3), (3+4)",
        [
            "This page repeats the number `typeof` Tryit. Numbers are **not** objects.",
        ],
        "typeof 0;\ntypeof 314;\ntypeof 3.14;\ntypeof (3);\ntypeof (3 + 4);",
        [
            ("typeof 0", "typeof 0"),
            ("typeof 314", "typeof 314"),
            ("typeof 3.14", "typeof 3.14"),
            ("typeof (3)", "typeof (3)"),
            ("typeof (3 + 4)", "typeof (3 + 4)"),
        ],
        'All five are **"number"**.',
    ),
    S(
        "math-not-constructor",
        "new Math() is TypeError",
        [
            "**Math** is listed as a built-in object, but it is **not constructable**.",
        ],
        "new Math();",
        outcome="**TypeError: Math is not a constructor**.",
        script=catch_script("", [("new Math()", "new Math()")]),
    ),
] + builtins()


# ---------------------------------------------------------------------------
# 17.4 JS Symbols
# ---------------------------------------------------------------------------

SYMBOLS = [
    S(
        "symbol-unique",
        "Symbol() === Symbol() is false",
        [
            "Every `Symbol()` call creates a **new unique** value, even with no description.",
        ],
        "const id1 = Symbol();\nconst id2 = Symbol();\nlet result = (id1 === id2);",
        [("result", "result"), ("typeof id1", "typeof id1")],
        "result is **false**. typeof is **\"symbol\"**.",
    ),
    S(
        "symbol-same-description",
        'Symbol("id") === Symbol("id") is false',
        [
            "The description is **only for debugging**. It does **not** make two symbols equal.",
        ],
        'const id1 = Symbol("id");\nconst id2 = Symbol("id");\nlet result = (id1 === id2);',
        [("result", "result"), ('String(id1)', "String(id1)")],
        'result is **false**. String(id1) is **"Symbol(id)"**.',
    ),
    S(
        "symbol-object-key",
        "Symbol as an object key",
        [
            "Symbols are often used as **hidden / unique property keys**: `person[id]`.",
        ],
        'const id = Symbol("id");\nconst person = { firstName: "John", lastName: "Doe" };\nperson[id] = 123;',
        [
            ("person[id]", "person[id]"),
            ("person.firstName", "person.firstName"),
        ],
        "person[id] is **123**. firstName is still **\"John\"**.",
    ),
    S(
        "symbol-typeof",
        'typeof Symbol("id") is "symbol"',
        [
            "Symbol is a **primitive**. `typeof` is **\"symbol\"**, not \"object\".",
        ],
        'const id = Symbol("id");\nlet type = typeof id;',
        [("type", "type")],
        'type is **"symbol"**.',
    ),
    S(
        "symbol-hidden-vs-id",
        "person[id] vs person.id",
        [
            "`person[id]` (symbol key) does **not** create `person.id` (string key).",
            "Two programmers adding `id` as a **string** can clash; **Symbol** keys do not.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50,\n  eyeColor: "blue"\n};\nlet id = Symbol("id");\nperson[id] = 140353;',
        [
            ("person[id]", "person[id]"),
            ("person.id", "person.id"),
        ],
        "person[id] is **140353**. person.id (string key) is **undefined**.",
    ),
    S(
        "symbol-for-in",
        "for...in ignores symbol keys",
        [
            "**`for...in`** lists enumerable **string** keys only. Symbol keys are skipped.",
        ],
        'const id = Symbol("id");\nconst person = { firstName: "John", lastName: "Doe" };\nperson[id] = 123;\nlet text = "";\nfor (let x in person) {\n  text += x + " ";\n}',
        [("text", "text"), ("person[id]", "person[id]")],
        'text is **"firstName lastName "** (trailing space). person[id] is still **123**.',
    ),
    S(
        "symbol-json",
        "JSON.stringify ignores symbol keys",
        [
            "**`JSON.stringify`** omits symbol properties.",
        ],
        'const id = Symbol("id");\nconst person = { name: "John" };\nperson[id] = 123;\nlet text = JSON.stringify(person);',
        [("text", "text"), ("person[id]", "person[id]")],
        'text is **{"name":"John"}**. The symbol value **123** is omitted.',
    ),
    S(
        "symbol-for-global",
        'Symbol.for("id") is reused',
        [
            "**`Symbol.for(key)`** uses a **global registry**. Same key → **same** symbol.",
        ],
        'const id1 = Symbol.for("id");\nconst id2 = Symbol.for("id");\nlet result = (id1 === id2);',
        [("result", "result")],
        "result is **true** (unlike `Symbol(\"id\")`).",
    ),
    S(
        "symbol-keyfor",
        "Symbol.keyFor — registry lookup",
        [
            "`Symbol.keyFor(sym)` returns the **global** key, or **undefined** for a local `Symbol()`.",
        ],
        'const g = Symbol.for("id");\nconst local = Symbol("id");',
        [("Symbol.keyFor(g)", "Symbol.keyFor(g)"), ("Symbol.keyFor(local)", "Symbol.keyFor(local)")],
        'keyFor(g) is **"id"**. keyFor(local) is **undefined**.',
    ),
    S(
        "symbol-plus-typeerror",
        "Symbol + string is TypeError",
        [
            "Implicit string coercion of a Symbol **throws**. Use **`String(sym)`** or **`sym.description`**.",
        ],
        'Symbol("id") + "";',
        outcome='**TypeError: Cannot convert a Symbol value to a string**. `String(Symbol("id"))` would be **"Symbol(id)"**.',
        script=catch_script("", [('Symbol("id") + ""', 'Symbol("id") + ""'), ('String(Symbol("id"))', 'String(Symbol("id"))')]),
    ),
    S(
        "wellknown-iterator",
        "Symbol.iterator — custom for...of",
        [
            "**`Symbol.iterator`** makes an object work with **`for...of`** (and spread).",
        ],
        'const myObject = {\n  data: ["A", "B", "C"],\n  [Symbol.iterator]() {\n    let index = 0;\n    let data = this.data;\n    return {\n      next() {\n        if (index < data.length) {\n          return {value: data[index++], done: false};\n        }\n        return {done: true};\n      }\n    };\n  }\n};\nlet text = "";\nfor (const x of myObject) {\n  text += x + " ";\n}',
        [("text", "text"), ("typeof Symbol.iterator", "typeof Symbol.iterator")],
        'text is **"A B C "**. typeof Symbol.iterator is **"symbol"**.',
    ),
    S(
        "wellknown-asynciterator",
        "Symbol.asyncIterator (well-known)",
        [
            "**`Symbol.asyncIterator`** is the well-known symbol for **async** iteration (`for await...of`).",
        ],
        "typeof Symbol.asyncIterator;\nSymbol.asyncIterator === Symbol.asyncIterator;",
        [
            ("typeof Symbol.asyncIterator", "typeof Symbol.asyncIterator"),
            ("String(Symbol.asyncIterator)", "String(Symbol.asyncIterator)"),
        ],
        'typeof is **"symbol"**. String is **"Symbol(Symbol.asyncIterator)"**.',
    ),
    S(
        "wellknown-tostringtag",
        "Symbol.toStringTag",
        [
            "**`Symbol.toStringTag`** customizes `Object.prototype.toString` (the `[object …]` tag).",
        ],
        'const o = { [Symbol.toStringTag]: "Foo" };\nlet tag = Object.prototype.toString.call(o);',
        [("tag", "tag"), ("String(o)", "String(o)")],
        'Object.prototype.toString.call(o) is **"[object Foo]"**. Default String(o) is still **[object Foo]** here via toString.',
    ),
    S(
        "wellknown-toprimitive",
        "Symbol.toPrimitive",
        [
            "**`Symbol.toPrimitive`** runs when the engine needs a **primitive** (hint number / string / default).",
        ],
        'const o = {\n  [Symbol.toPrimitive](hint) {\n    if (hint === "number") return 42;\n    return "ok";\n  }\n};',
        [("Number(o)", "Number(o)"), ("String(o)", "String(o)"), ("o + 1", "o + 1")],
        'Number(o) is **42**. String(o) is **"ok"**. `o + 1` uses hint **"default"** → **"ok1"** (string concat).',
    ),
]


# ---------------------------------------------------------------------------
# 17.5 JS typeof
# ---------------------------------------------------------------------------

def _tof(stem: str, expr: str, result: str, note: str = "") -> dict:
    bullets = [f"`{expr}` is a **typeof** table row."]
    if note:
        bullets.append(note)
    return S(
        stem,
        expr,
        bullets,
        f"{expr};",
        [(expr, expr)],
        f"`{expr}` is **\"{result}\"**.",
    )


TYPEOF = [
    _tof("typeof-john", 'typeof "John"', "string"),
    _tof("typeof-john-doe-concat", 'typeof ("John" + "Doe")', "string", "`\"John\"+\"Doe\"` is **\"JohnDoe\"**, still a string."),
    _tof("typeof-3-14", "typeof 3.14", "number"),
    _tof("typeof-33", "typeof 33", "number"),
    _tof("typeof-33-plus-66", "typeof (33 + 66)", "number", "`33 + 66` is **99**, still a number."),
    _tof("typeof-true", "typeof true", "boolean"),
    _tof("typeof-false", "typeof false", "boolean"),
    _tof("typeof-bigint", "typeof 1234n", "bigint"),
    _tof("typeof-symbol", "typeof Symbol()", "symbol"),
    _tof(
        "typeof-undeclared-x",
        "typeof x",
        "undefined",
        "`typeof` on an **undeclared** name is **\"undefined\"** — it does **not** throw.",
    ),
    S(
        "typeof-null",
        "typeof null — returns object (legacy)",
        [
            "`null` is a **primitive**, but `typeof null` is **\"object\"**.",
            "This is a well-known **legacy bug**. Do not use typeof to test for null; use **`=== null`**.",
        ],
        "typeof null;",
        [("typeof null", "typeof null")],
        'typeof null is **"object"**.',
    ),
    _tof("typeof-nan", "typeof NaN", "number", "**NaN** is a number. The type of Not-a-Number is still **\"number\"**."),
    S(
        "typeof-object-literal",
        "typeof {name:'John'} — object",
        [
            "A plain object’s typeof is **\"object\"**.",
        ],
        "typeof {name: 'John'};",
        [("typeof {name: 'John'}", "typeof {name: 'John'}")],
        'typeof {name:\'John\'} is **"object"**.',
    ),
    _tof("typeof-array-lit", "typeof [1, 2, 3, 4]", "object", "Arrays are objects. Use **Array.isArray** to tell them apart."),
    _tof("typeof-empty-object", "typeof {}", "object"),
    _tof("typeof-empty-array", "typeof []", "object"),
    _tof("typeof-new-object", "typeof new Object()", "object"),
    _tof("typeof-new-array", "typeof new Array()", "object"),
    _tof("typeof-new-date", "typeof new Date()", "object"),
    _tof("typeof-new-set", "typeof new Set()", "object"),
    _tof("typeof-new-map", "typeof new Map()", "object"),
    _tof("typeof-function", "typeof function () {}", "function", "Functions are the **other** typeof result besides object for callables."),
    S(
        "array-isarray",
        "Array.isArray(fruits)",
        [
            "`typeof` cannot tell an array from a date. **`Array.isArray`** can.",
        ],
        'const fruits = ["apples", "bananas", "oranges"];\nArray.isArray(fruits);',
        [("Array.isArray(fruits)", "Array.isArray(fruits)"), ("Array.isArray({a:1})", "Array.isArray({a: 1})")],
        "Array.isArray(fruits) is **true**. Array.isArray({a:1}) is **false**.",
    ),
    S(
        "instanceof-date",
        "time instanceof Date",
        [
            "**`instanceof`** is **true** if the object was created from that constructor (prototype chain).",
        ],
        "const time = new Date();\n(time instanceof Date);",
        [("time instanceof Date", "time instanceof Date"), ("time instanceof Array", "time instanceof Array")],
        "`time instanceof Date` is **true**. `time instanceof Array` is **false**.",
    ),
    S(
        "instanceof-array",
        "fruits instanceof Array",
        [
            "Array instances are `instanceof Array`.",
        ],
        'const fruits = ["apples", "bananas", "oranges"];\n(fruits instanceof Array);',
        [("fruits instanceof Array", "fruits instanceof Array")],
        "`fruits instanceof Array` is **true**.",
    ),
    S(
        "instanceof-map",
        "fruits instanceof Map",
        [
            "`new Map(...)` instances are `instanceof Map`.",
        ],
        'const fruits = new Map([\n  ["apples", 500],\n  ["bananas", 300],\n  ["oranges", 200]\n]);\n(fruits instanceof Map);',
        [("fruits instanceof Map", "fruits instanceof Map"), ("fruits instanceof Array", "fruits instanceof Array")],
        "`instanceof Map` is **true**. `instanceof Array` is **false**.",
    ),
    S(
        "instanceof-set",
        "fruits instanceof Set",
        [
            "`new Set(...)` instances are `instanceof Set`.",
        ],
        'const fruits = new Set(["apples", "bananas", "oranges"]);\n(fruits instanceof Set);',
        [("fruits instanceof Set", "fruits instanceof Set")],
        "`fruits instanceof Set` is **true**.",
    ),
    S(
        "typeof-undeclared-car",
        "typeof car — undeclared variable",
        [
            "`typeof car` when **car was never declared** is **\"undefined\"**, not a ReferenceError.",
        ],
        "typeof car;",
        [("typeof car", "typeof car")],
        'typeof car is **"undefined"**.',
    ),
    S(
        "typeof-declared-no-value",
        "let car; typeof car",
        [
            "A declared variable with no value: value **undefined**, typeof **\"undefined\"**.",
        ],
        "let car;\ntypeof car;",
        [("car", "car"), ("typeof car", "typeof car")],
        "car is **undefined**. typeof is **\"undefined\"**.",
    ),
    S(
        "emptied-undefined",
        'car = undefined after "Volvo"',
        [
            "Assigning **`undefined`** empties the variable. Type becomes **undefined**.",
        ],
        'let car = "Volvo";\ncar = undefined;',
        [("car", "car"), ("typeof car", "typeof car")],
        "car is **undefined**. typeof is **\"undefined\"**.",
    ),
    S(
        "empty-string-typeof",
        'let car = ""; typeof car',
        [
            "An empty string is **not** undefined. typeof is **\"string\"**.",
        ],
        'let car = "";\ntypeof car;',
        [("JSON.stringify(car)", "JSON.stringify(car)"), ("typeof car", "typeof car")],
        'value is **""**. typeof is **"string"**.',
    ),
    S(
        "object-set-null",
        "person = null — value null, typeof object",
        [
            "Setting an object variable to **`null`** empties it. `typeof` stays **\"object\"** (legacy).",
        ],
        'let person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};\nperson = null;',
        [("person", "person"), ("typeof person", "typeof person")],
        "person is **null**. typeof is **\"object\"**.",
    ),
    S(
        "object-set-undefined",
        "person = undefined — value and type undefined",
        [
            "Setting the same variable to **`undefined`** makes **both** value and type undefined.",
        ],
        'let person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};\nperson = undefined;',
        [("person", "person"), ("typeof person", "typeof person")],
        "person is **undefined**. typeof is **\"undefined\"**.",
    ),
    S(
        "null-vs-undefined",
        "undefined vs null — type and == / ===",
        [
            "`undefined` and `null` are **equal in value** under **`==`**, **different types** under **`===`**.",
        ],
        "typeof undefined;\ntypeof null;\nnull === undefined;\nnull == undefined;",
        [
            ("typeof undefined", "typeof undefined"),
            ("typeof null", "typeof null"),
            ("null === undefined", "null === undefined"),
            ("null == undefined", "null == undefined"),
        ],
        'typeof undefined is **"undefined"**. typeof null is **"object"**. `===` is **false**. `==` is **true**.',
    ),
    S(
        "constructor-object",
        "{name:'John',age:34}.constructor",
        [
            "**`constructor`** is the function that created the value’s prototype.",
        ],
        "let c = {name: 'John', age: 34}.constructor;",
        [("String(c)", "String(c)"), ("c === Object", "c === Object")],
        'String(c) is **"function Object() { [native code] }"**. `c === Object` is **true**.',
    ),
    S(
        "constructor-array",
        "[1,2,3,4].constructor",
        [
            "Array instances have **`Array`** as their constructor function.",
        ],
        "let c = [1, 2, 3, 4].constructor;",
        [("String(c)", "String(c)"), ("c === Array", "c === Array")],
        'String(c) is **"function Array() { [native code] }"**. `c === Array` is **true**.',
    ),
    S(
        "constructor-date",
        "new Date().constructor",
        [
            "Date instances have **`Date`** as constructor.",
        ],
        f"{FIX}\nlet c = d.constructor;",
        [("String(c)", "String(c)"), ("c === Date", "c === Date")],
        'String(c) is **"function Date() { [native code] }"**. `c === Date` is **true**.',
    ),
    S(
        "constructor-set",
        "new Set().constructor",
        [
            "Set instances have **`Set`** as constructor.",
        ],
        "let c = new Set().constructor;",
        [("String(c)", "String(c)"), ("c === Set", "c === Set")],
        'String(c) is **"function Set() { [native code] }"**. `c === Set` is **true**.',
    ),
    S(
        "constructor-map",
        "new Map().constructor",
        [
            "Map instances have **`Map`** as constructor.",
        ],
        "let c = new Map().constructor;",
        [("String(c)", "String(c)"), ("c === Map", "c === Map")],
        'String(c) is **"function Map() { [native code] }"**. `c === Map` is **true**.',
    ),
    S(
        "constructor-function",
        "function () {}.constructor",
        [
            "Functions have **`Function`** as constructor.",
        ],
        "let c = function () {}.constructor;",
        [("String(c)", "String(c)"), ("c === Function", "c === Function")],
        'String(c) is **"function Function() { [native code] }"**. `c === Function` is **true**.',
    ),
    S(
        "constructor-eq-array",
        "myArray.constructor === Array",
        [
            "You can recognize an array with **`constructor === Array`** (or prefer **Array.isArray**).",
        ],
        "const myArray = [1, 2, 3, 4];\n(myArray.constructor === Array);",
        [("myArray.constructor === Array", "myArray.constructor === Array")],
        "`myArray.constructor === Array` is **true**.",
    ),
    S(
        "constructor-eq-date",
        "myDate.constructor === Date",
        [
            "You can recognize a Date with **`constructor === Date`**.",
        ],
        f"{FIX}\nconst myDate = d;\n(myDate.constructor === Date);",
        [("myDate.constructor === Date", "myDate.constructor === Date")],
        "`myDate.constructor === Date` is **true**.",
    ),
    S(
        "void-operator",
        "void 0 returns undefined",
        [
            "**`void`** evaluates an expression and returns **`undefined`**.",
            'Often written **`void(0)`** / **`void 0`**. The page also uses `javascript:void(0)` on a link.',
        ],
        "void 0;\nvoid (0);",
        [("void 0", "void 0"), ("typeof void 0", "typeof void 0"), ("void (0)", "void (0)")],
        "`void 0` is **undefined**. typeof is **\"undefined\"**. `void (0)` is the same.",
        body='<p><a href="javascript:void(0)">Useless link</a></p>',
        buttons='<p><button type="button" onclick="document.body.style.backgroundColor=\'red\'">Click me to change the background color of body to red</button></p>',
    ),
]
# ---------------------------------------------------------------------------
# 17.6 JS undefined
# ---------------------------------------------------------------------------

UNDEFINED = [
    S(
        "declared-no-value",
        "let car — value undefined",
        [
            "A variable declared without a value is **`undefined`**.",
        ],
        "let car;",
        [("car", "car")],
        "car is **undefined**.",
    ),
    S(
        "typeof-undefined",
        "typeof car — type undefined",
        [
            "`typeof` of that variable is **\"undefined\"**.",
        ],
        "let car;\ntypeof car;",
        [("typeof car", "typeof car")],
        'typeof car is **"undefined"**.',
    ),
    S(
        "empty-string-not-undefined",
        'Empty string "" vs undefined',
        [
            "An empty string has a **value** and a **type**. It is **not** undefined.",
        ],
        'let text = "";',
        [("JSON.stringify(text)", "JSON.stringify(text)"), ("typeof text", "typeof text")],
        'text is **""**. typeof is **"string"**. Concatenation `text + " " + typeof text` would be **" string"**.',
    ),
    S(
        "missing-property",
        "Missing object property is undefined",
        [
            "Reading a **non-existing** property returns **`undefined`** (it does not throw).",
        ],
        'const person = {firstName:"John", lastName:"Doe"};',
        [("person.age", "person.age"), ("typeof person.age", "typeof person.age")],
        "person.age is **undefined**. typeof is **\"undefined\"**.",
    ),
    S(
        "function-no-return",
        "Function without return yields undefined",
        [
            "A function with **no `return`** returns **`undefined`**.",
        ],
        "function myFunction() {\n  let x = 5;\n}",
        [("myFunction()", "myFunction()"), ("typeof myFunction()", "typeof myFunction()")],
        "myFunction() is **undefined**. typeof is **\"undefined\"**. The inner `x` is unused.",
    ),
    S(
        "const-assign-typeerror",
        "const person = undefined — TypeError",
        [
            "The page assigns `person = undefined` after **`const person`**. That is a **TypeError**.",
            "`const` cannot be reassigned. Use **`let`** if you need to empty the binding.",
        ],
        'const person = {firstName:"John", lastName:"Doe"};\nperson = undefined;',
        outcome="**TypeError: Assignment to constant variable.** The object is unchanged. Use `let` to reassign.",
        script=catch_script(
            'const person = {firstName:"John", lastName:"Doe"};',
            [("person = undefined", "(person = undefined)")],
        ),
    ),
    S(
        "let-assign-undefined",
        "let person = undefined — empties the binding",
        [
            "With **`let`**, assigning **`undefined`** empties the variable.",
        ],
        'let person = {firstName:"John", lastName:"Doe"};\nperson = undefined;',
        [("person", "person"), ("typeof person", "typeof person")],
        "person is **undefined**. typeof is **\"undefined\"**.",
    ),
    S(
        "let-assign-null",
        "let person = null — emptied with null",
        [
            "Objects can also be emptied with **`null`**. typeof becomes **\"object\"** (legacy).",
        ],
        'let person = {firstName:"John", lastName:"Doe"};\nperson = null;',
        [("person", "person"), ("typeof person", "typeof person")],
        "person is **null**. typeof is **\"object\"**.",
    ),
    S(
        "undeclared-referenceerror",
        "Reading an undeclared name is ReferenceError",
        [
            "`typeof missing` is safe. **Reading** `missing` throws **ReferenceError**.",
            "Declared-but-empty is **undefined**; never-declared is an **error** (except typeof).",
        ],
        "missing;",
        outcome="**ReferenceError: missing is not defined**. `typeof missing` would be **\"undefined\"** without throwing.",
        script=catch_script("", [("missing", "missing"), ("typeof missing", "typeof missing")]),
    ),
    S(
        "undefined-eq-null",
        "undefined == null is true; === is false",
        [
            "`undefined` is a **value** meaning declared but not assigned.",
            "It is **==** null and **not ===** null.",
        ],
        "undefined == null;\nundefined === null;",
        [("undefined == null", "undefined == null"), ("undefined === null", "undefined === null")],
        "`==` is **true**. `===` is **false**.",
    ),
]


# ---------------------------------------------------------------------------
# 17.7 JS NaN
# ---------------------------------------------------------------------------

NAN = [
    S(
        "div-apple",
        '100 / "Apple" is NaN',
        [
            "You get **NaN** when JS **cannot** calculate a number.",
        ],
        'let x = 100 / "Apple";',
        [("x", "x"), ("typeof x", "typeof x")],
        "x is **NaN**. typeof is **\"number\"**.",
    ),
    S(
        "typeof-nan",
        "typeof NaN is number",
        [
            "**NaN** belongs to the **number** type. The name means Not-a-Number; the type is still number.",
        ],
        "let x = NaN;",
        [("typeof x", "typeof x")],
        'typeof NaN is **"number"**.',
    ),
    S(
        "div-numeric-string",
        '100 / "10" is 10',
        [
            "A **numeric string** is coerced to a number in **arithmetic** (`/`, `-`, `*`).",
        ],
        'let x = 100 / "10";',
        [("x", "x"), ("typeof x", "typeof x")],
        "x is **10**. typeof is **\"number\"**.",
    ),
    S(
        "isnan-apple",
        'isNaN(100 / "Apple")',
        [
            "The global **`isNaN()`** is **true** if the value (after number coercion) is NaN.",
        ],
        'let x = 100 / "Apple";\nisNaN(x);',
        [("isNaN(x)", "isNaN(x)")],
        "isNaN(x) is **true**.",
    ),
    S(
        "nan-ne-nan-eq",
        "NaN == NaN is false",
        [
            "**NaN is not equal to itself** with `==` or `===`.",
        ],
        "let x = NaN;\nx == x;",
        [("x == x", "x == x"), ("x === x", "x === x")],
        "`x == x` is **false**. `x === x` is also **false**.",
    ),
    S(
        "nan-strict-ne",
        "NaN !== NaN is true",
        [
            "`NaN !== NaN` is **true**. Never test with `x === NaN`.",
        ],
        "NaN !== NaN;",
        [("NaN !== NaN", "NaN !== NaN"), ("NaN === NaN", "NaN === NaN")],
        "`NaN !== NaN` is **true**. `NaN === NaN` is **false**.",
    ),
    S(
        "number-isnan",
        "Number.isNaN(NaN) is the right test",
        [
            "**`Number.isNaN`** is true **only** for the real NaN value. It does **not** coerce.",
        ],
        "Number.isNaN(NaN);\nNumber.isNaN(100 / \"Apple\");",
        [
            ("Number.isNaN(NaN)", "Number.isNaN(NaN)"),
            ('Number.isNaN(100 / "Apple")', 'Number.isNaN(100 / "Apple")'),
        ],
        "Both are **true** (the division already produced NaN).",
    ),
    S(
        "isnan-coerces-string",
        'isNaN("Apple") vs Number.isNaN("Apple")',
        [
            "Global **`isNaN(\"Apple\")`** coerces the string → NaN → **true**.",
            "**`Number.isNaN(\"Apple\")`** does **not** coerce → **false** (it is not the NaN value).",
        ],
        'isNaN("Apple");\nNumber.isNaN("Apple");',
        [
            ('isNaN("Apple")', 'isNaN("Apple")'),
            ('Number.isNaN("Apple")', 'Number.isNaN("Apple")'),
        ],
        'isNaN("Apple") is **true**. Number.isNaN("Apple") is **false**. Prefer **Number.isNaN**.',
    ),
    S(
        "nan-plus-5",
        "NaN + 5 is NaN",
        [
            "Any math with **NaN** stays **NaN**.",
        ],
        "let x = NaN;\nlet y = 5;",
        [("x + y", "x + y")],
        "NaN + 5 is **NaN**.",
    ),
    S(
        "zero-div-zero",
        "0 / 0 is NaN",
        [
            "**`0 / 0`** is NaN. (`1 / 0` is **Infinity**, not NaN.)",
        ],
        "let x = 0 / 0;\nlet inf = 1 / 0;",
        [("0 / 0", "x"), ("1 / 0", "inf")],
        "0 / 0 is **NaN**. 1 / 0 is **Infinity**.",
    ),
    S(
        "object-is-nan",
        "Object.is(NaN, NaN) is true",
        [
            "**`Object.is(NaN, NaN)`** is **true** — another correct NaN test besides **Number.isNaN**.",
        ],
        "Object.is(NaN, NaN);",
        [("Object.is(NaN, NaN)", "Object.is(NaN, NaN)")],
        "Object.is(NaN, NaN) is **true**.",
    ),
    S(
        "parseint-abc",
        'parseInt("abc") is NaN',
        [
            "Parsing a **non-numeric** string with `parseInt` / `parseFloat` yields **NaN**.",
        ],
        'parseInt("abc");\nparseFloat("abc");',
        [('parseInt("abc")', 'parseInt("abc")'), ('parseFloat("abc")', 'parseFloat("abc")')],
        "Both are **NaN**.",
    ),
]


# ---------------------------------------------------------------------------
# 17.8 JS toString()
# ---------------------------------------------------------------------------

TOSTRING = [
    S(
        "array-tostring",
        "Array.prototype.toString — comma list",
        [
            "Array **`toString()`** joins elements with **commas** (no spaces).",
        ],
        'const fruits = ["Banana", "Orange", "Apple", "Mango"];\nlet myList = fruits.toString();',
        [("myList", "myList")],
        'myList is **"Banana,Orange,Apple,Mango"**.',
    ),
    S(
        "date-tostring",
        "Date.prototype.toString — local date/time",
        [
            "Date **`toString()`** is a human-readable **local** date, time, and zone.",
            "This Tryit uses **`new Date()`** (now). The snap is the **browser's current local** clock.",
        ],
        "const d = new Date();\nlet text = d.toString();",
        [("text", "text")],
        "The snap shows this engine's **current local** `toString()` (Mountain, GMT-0600 / GMT-0700).",
    ),
    S(
        "date-tostring-fixed",
        "Date toString on a fixed instant",
        [
            "Same method on a **fixed** UTC instant so the outcome is stable.",
        ],
        f"{FIX}\nlet text = d.toString();",
        [("text", "text")],
        'text is **"Thu Mar 25 2021 09:30:45 GMT-0600 (Mountain Daylight Time)"**.',
    ),
    S(
        "number-tostring",
        "Number.prototype.toString — decimal",
        [
            "Number **`toString()`** (no argument) is the decimal string.",
        ],
        "let x = 123;\nlet text = x.toString();",
        [("text", "text"), ("typeof text", "typeof text")],
        'text is **"123"**. typeof is **"string"**.',
    ),
    S(
        "number-tostring-binary",
        "Number toString(2) — binary",
        [
            "`toString(radix)` with **2** is **binary**.",
        ],
        "let x = 123;\nlet text = x.toString(2);",
        [("text", "text")],
        'text is **"1111011"** (123 in base 2).',
    ),
    S(
        "function-tostring",
        "Function.prototype.toString — source",
        [
            "Function **`toString()`** returns the **source text** of the function.",
            "Named on the page; no Tryit — still run it.",
        ],
        "function add(a, b) { return a + b; }\nlet text = add.toString();",
        [("text", "text")],
        'text is **"function add(a, b) { return a + b; }"**.',
    ),
    S(
        "object-tostring-default",
        'Object toString default — "[object Object]"',
        [
            "Default object **`toString()`** is **[object Object]** — not the keys.",
        ],
        'let person = {\n  firstname: "John",\n  lastname: "Doe"\n};\nlet text = person.toString();',
        [("text", "text")],
        'text is **"[object Object]"**.',
    ),
    S(
        "object-tostring-override",
        "Object toString override",
        [
            "Override **`toString`** on the object (or prototype) for a useful string.",
        ],
        'let person = {\n  firstname: "John",\n  lastname: "Doe",\n  toString: function () {\n    return this.firstname + " " + this.lastname;\n  }\n};\nlet text = person.toString();',
        [("text", "text"), ("String(person)", "String(person)")],
        'text is **"John Doe"**. String(person) also uses the override: **"John Doe"**.',
    ),
    S(
        "boolean-tostring",
        "Boolean.prototype.toString",
        [
            "`true.toString()` / `false.toString()` are the strings **\"true\"** / **\"false\"**.",
        ],
        "true.toString();\nfalse.toString();",
        [("true.toString()", "true.toString()"), ("false.toString()", "false.toString()")],
        'true → **"true"**. false → **"false"**.',
    ),
    S(
        "null-tostring-typeerror",
        "null.toString() is TypeError",
        [
            "**`null`** and **`undefined`** have no `toString` method. Calling it throws **TypeError**.",
            "Use **`String(null)`** instead (**\"null\"**).",
        ],
        "null.toString();",
        outcome=(
            'null.toString() is **TypeError: Cannot read properties of null (reading \'toString\')**. '
            'undefined.toString() is the same kind of TypeError. String(null) is **"null"**. String(undefined) is **"undefined"**.'
        ),
        script=catch_script(
            "",
            [
                ("null.toString()", "null.toString()"),
                ("undefined.toString()", "undefined.toString()"),
                ("String(null)", "String(null)"),
                ("String(undefined)", "String(undefined)"),
            ],
        ),
    ),
]


# ---------------------------------------------------------------------------
# 17.9 JS toLocaleString()
# ---------------------------------------------------------------------------

TOLOCALE = [
    S(
        "number-default",
        "Number toLocaleString() — default locale",
        [
            "`toLocaleString()` uses **this engine's** locale when you omit the locale argument.",
            "This Chrome reports **en-US**. The grouping character is a comma.",
        ],
        "let num = 1234567.89;\nlet text = num.toLocaleString();",
        [("text", "text"), ("navigator.language", "navigator.language")],
        'This engine printed **"1,234,567.89"**. navigator.language is **"en-US"**.',
    ),
    S(
        "number-locales",
        'Locales en-US, de-DE, no-NO',
        [
            "Pass a **locale** (`language-COUNTRY`) to pick grouping and decimal marks.",
            "`no-NO` uses a **nbsp** thousands separator in this engine.",
        ],
        'let num = 1234567.89;\nlet us = num.toLocaleString("en-US");\nlet de = num.toLocaleString("de-DE");\nlet no = num.toLocaleString("no-NO");',
        [("us", "us"), ("de", "de"), ("no", "no")],
        'en-US **"1,234,567.89"**. de-DE **"1.234.567,89"**. no-NO **"1 234 567,89"** (nbsp spaces).',
    ),
    S(
        "currency",
        "style currency — USD, EUR, NOK",
        [
            "`style:\"currency\"` plus **`currency`** formats money for that locale.",
        ],
        'let price = 1299.95;\nlet dollars = price.toLocaleString("en-US", {style:"currency", currency:"USD"});\nlet euros = price.toLocaleString("de-DE", {style:"currency", currency:"EUR"});\nlet kroner = price.toLocaleString("no-NO", {style:"currency", currency:"NOK"});',
        [("dollars", "dollars"), ("euros", "euros"), ("kroner", "kroner")],
        'USD **"$1,299.95"**. EUR **"1.299,95 €"** (nbsp before €). NOK **"1 299,95 kr"** (nbsp grouping).',
    ),
    S(
        "percent",
        'style percent — 0.875 → 88%',
        [
            '`style:"percent"` multiplies by 100 and adds a percent sign.',
        ],
        'let score = 0.875;\nlet result = score.toLocaleString("en-US", {style:"percent"});',
        [("result", "result")],
        'result is **"88%"**.',
    ),
    S(
        "fraction-digits",
        "minimumFractionDigits / maximumFractionDigits",
        [
            "Pin the number of fraction digits with **minimumFractionDigits** and **maximumFractionDigits**.",
        ],
        'let num = 3.14159;\nlet text = num.toLocaleString("en-US", {\n  minimumFractionDigits: 2,\n  maximumFractionDigits: 2\n});',
        [("text", "text")],
        'text is **"3.14"**.',
    ),
    S(
        "date-en-us",
        'Date toLocaleString("en-US")',
        [
            "Dates format with the locale too. **`new Date()`** is **now** on the page Tryit.",
            "This sandbox uses a **fixed** instant so the snap is stable: `2021-03-25T15:30:45.123Z`.",
        ],
        f'{FIX}\nlet text = d.toLocaleString("en-US");',
        [("text", "text")],
        'This engine printed **"3/25/2021, 9:30:45 AM"** (Mountain, UTC−6).',
    ),
    S(
        "date-options",
        "Date options weekday/year/month/day",
        [
            "Options control **weekday**, **year**, **month**, and **day** words vs numbers.",
        ],
        f'{FIX}\nlet text = d.toLocaleString("en-US", {{\n  weekday: "long",\n  year: "numeric",\n  month: "long",\n  day: "numeric"\n}});',
        [("text", "text")],
        'This engine printed **"Thursday, March 25, 2021"** (local calendar day — still March 25).',
    ),
    S(
        "filesize",
        "Readable file sizes",
        [
            "A common trick: divide bytes, then **`toLocaleString`** with **maximumFractionDigits: 1**.",
        ],
        'function fileSize(bytes) {\n  if (bytes < 1024) return bytes + " bytes";\n  if (bytes < 1024 * 1024) {\n    return (bytes / 1024).toLocaleString("en-US", {maximumFractionDigits: 1}) + " KB";\n  }\n  return (bytes / 1024 / 1024).toLocaleString("en-US", {maximumFractionDigits: 1}) + " MB";\n}\nlet size = 1536000;\nlet text = fileSize(size);',
        [("text", "text")],
        '1536000 bytes → **"1.5 MB"** in this engine.',
    ),
    S(
        "array-dates",
        "Array toLocaleString — each element",
        [
            "Array **`toLocaleString`** converts **each** element, then joins with commas.",
            TZ + " These ISO dates are UTC midnight, so Mountain prints the **previous evening**.",
        ],
        'const dates = [\n  new Date("2026-01-01"),\n  new Date("2026-12-24")\n];\nlet text = dates.toLocaleString("en-US");',
        [
            ("text", "text"),
            ("dates[0].toISOString()", "dates[0].toISOString()"),
            ("dates[1].toISOString()", "dates[1].toISOString()"),
        ],
        'This engine printed **"12/31/2025, 5:00:00 PM,12/23/2026, 5:00:00 PM"** — not Jan 1 / Dec 24 local. ISO stays **2026-01-01T00:00:00.000Z** and **2026-12-24T00:00:00.000Z**.',
    ),
    S(
        "bigint-locale",
        "BigInt toLocaleString (named type on the page)",
        [
            "The page lists **BigInt** as supporting `toLocaleString`. No Tryit — still run it.",
        ],
        'let n = 1234567890123456789n;\nlet text = n.toLocaleString("en-US");',
        [("text", "text")],
        'This engine printed **"1,234,567,890,123,456,789"**.',
    ),
]


# ---------------------------------------------------------------------------
# 17.10 JS Type Coercion
# ---------------------------------------------------------------------------

COERCION = [
    S(
        "plus-vs-minus-strings",
        "('5' + '2') vs ('5' - '2')",
        [
            "**Coercion is implicit.** `+` with strings **concatenates**. `-` forces **numbers**.",
        ],
        "let result1 = ('5' + '2');\nlet result2 = ('5' - '2');",
        [("result1", "result1"), ("typeof result1", "typeof result1"), ("result2", "result2"), ("typeof result2", "typeof result2")],
        'result1 is **"52"** (string). result2 is **3** (number).',
    ),
    S(
        "string-plus",
        '"5" + 2 — string coercion of +',
        [
            "If **any** operand of **`+`** is a string, the other becomes a string and they **concatenate**.",
        ],
        'let x = "5" + 2;',
        [("x", "x"), ("typeof x", "typeof x")],
        'x is **"52"**. typeof is **"string"**.',
    ),
    S(
        "numeric-minus",
        '"5" - 2 — numeric coercion of -',
        [
            "**`-`** always does numeric subtraction (after coercion).",
        ],
        'let x = "5" - 2;',
        [("x", "x"), ("typeof x", "typeof x")],
        "x is **3**. typeof is **\"number\"**.",
    ),
    S(
        "numeric-times",
        '"5" * 2 — numeric *',
        [
            "**`*`** coerces both sides to numbers.",
        ],
        'let x = "5" * 2;',
        [("x", "x")],
        "x is **10**.",
    ),
    S(
        "numeric-div",
        '"5" / 2 — numeric /',
        [
            "**`/`** coerces both sides to numbers.",
        ],
        'let x = "5" / 2;',
        [("x", "x")],
        "x is **2.5**.",
    ),
    S(
        "numeric-mod",
        '"5" % 2 — numeric %',
        [
            "**`%`** (remainder) coerces both sides to numbers.",
        ],
        'let x = "5" % 2;',
        [("x", "x")],
        "x is **1**.",
    ),
    S(
        "unary-plus",
        '+"5" — unary plus to number',
        [
            "**Unary `+`** forces a number (same idea as `Number()`).",
        ],
        'let x = +"5";',
        [("x", "x"), ("typeof x", "typeof x")],
        "x is **5**. typeof is **\"number\"**.",
    ),
    S(
        "loose-eq-number-string",
        '5 == "5" — loose equality',
        [
            "**`==`** coerces to a common type before comparing. `5 == \"5\"` is **true**.",
        ],
        'let x = (5 == "5");',
        [("x", "x")],
        "x is **true**.",
    ),
    S(
        "strict-eq-number-string",
        '5 === "5" — strict equality',
        [
            "**`===`** does **not** coerce. Different types → **false**.",
        ],
        'let x = (5 === "5");',
        [("x", "x")],
        "x is **false**.",
    ),
    S(
        "abc-minus-1",
        '"abc" - 1 is NaN',
        [
            "If a string **cannot** become a valid number, numeric coercion yields **NaN**.",
        ],
        'let x = "abc" - 1;',
        [("x", "x")],
        "x is **NaN**.",
    ),
    S(
        "falsy-0",
        "Boolean coercion — !!0",
        [
            "**Falsy:** `0`, `\"\"`, `null`, `undefined`, `NaN`, `false`.",
            "`!!` is the usual explicit boolean coercion demo.",
        ],
        "!!0;",
        [("!!0", "!!0")],
        "`!!0` is **false**.",
    ),
    S(
        "falsy-empty-string",
        'Boolean coercion — !!""',
        [
            "The empty string is **falsy**.",
        ],
        '!!"";',
        [('!!""', '!!""')],
        '`!!""` is **false**.',
    ),
    S(
        "falsy-null",
        "Boolean coercion — !!null",
        [
            "**null** is falsy.",
        ],
        "!!null;",
        [("!!null", "!!null")],
        "`!!null` is **false**.",
    ),
    S(
        "falsy-undefined",
        "Boolean coercion — !!undefined",
        [
            "**undefined** is falsy.",
        ],
        "!!undefined;",
        [("!!undefined", "!!undefined")],
        "`!!undefined` is **false**.",
    ),
    S(
        "falsy-nan",
        "Boolean coercion — !!NaN",
        [
            "**NaN** is falsy.",
        ],
        "!!NaN;",
        [("!!NaN", "!!NaN")],
        "`!!NaN` is **false**.",
    ),
    S(
        "falsy-false",
        "Boolean coercion — !!false",
        [
            "**false** is falsy.",
        ],
        "!!false;",
        [("!!false", "!!false")],
        "`!!false` is **false**.",
    ),
    S(
        "truthy-object",
        "Boolean coercion — !!{}",
        [
            "Empty objects **`{}`** are **truthy**.",
        ],
        "!!{};",
        [("!!{}", "!!{}")],
        "`!!{}` is **true**.",
    ),
    S(
        "truthy-array",
        "Boolean coercion — !![]",
        [
            "Empty arrays **`[]`** are **truthy** (unlike `\"\"`).",
        ],
        "!![];",
        [("!![]", "!![]")],
        "`!![]` is **true**.",
    ),
    S(
        "loose-eq-zero-false",
        "0 == false is true; 0 === false is false",
        [
            "`==` coerces **false** to **0**. `===` sees number vs boolean.",
        ],
        "0 == false;\n0 === false;",
        [("0 == false", "0 == false"), ("0 === false", "0 === false")],
        "`==` is **true**. `===` is **false**.",
    ),
    S(
        "loose-eq-empty-zero",
        '"" == 0 is true',
        [
            "Empty string **`==`** 0 after numeric coercion.",
        ],
        '"" == 0;',
        [('"" == 0', '"" == 0'), ('"" === 0', '"" === 0')],
        '`"" == 0` is **true**. `"" === 0` is **false**.',
    ),
]


# ---------------------------------------------------------------------------
# 17.11 JS Type Conversion
# ---------------------------------------------------------------------------

CONVERSION = [
    S(
        "number-3-14",
        'Number("3.14")',
        ["A numeric string converts to that number."],
        'Number("3.14");',
        [('Number("3.14")', 'Number("3.14")')],
        'Number("3.14") is **3.14**.',
    ),
    S(
        "number-math-pi",
        "Number(Math.PI)",
        ["Number() on an already-numeric value returns that number."],
        "Number(Math.PI);",
        [("Number(Math.PI)", "Number(Math.PI)")],
        "Number(Math.PI) is **3.141592653589793**.",
    ),
    S(
        "number-space",
        'Number(" ")',
        ["A string of **whitespace** converts to **0**."],
        'Number(" ");',
        [('Number(" ")', 'Number(" ")')],
        'Number(" ") is **0**.',
    ),
    S(
        "number-empty",
        'Number("")',
        ["An **empty string** converts to **0**."],
        'Number("");',
        [('Number("")', 'Number("")')],
        'Number("") is **0**.',
    ),
    S(
        "number-99-88",
        'Number("99 88") — does not convert',
        ["A string with an **internal space** is not a numeric string → **NaN**."],
        'Number("99 88");',
        [('Number("99 88")', 'Number("99 88")')],
        'Number("99 88") is **NaN**.',
    ),
    S(
        "number-john",
        'Number("John") — does not convert',
        ["A **non-numeric** string → **NaN**."],
        'Number("John");',
        [('Number("John")', 'Number("John")')],
        'Number("John") is **NaN**.',
    ),
    S(
        "parsefloat",
        'parseFloat("10.33")',
        [
            "**parseFloat** parses a leading float. Trailing junk may be ignored (unlike Number()).",
        ],
        'parseFloat("10.33");\nparseFloat("99 88");',
        [
            ('parseFloat("10.33")', 'parseFloat("10.33")'),
            ('parseFloat("99 88")', 'parseFloat("99 88")'),
        ],
        'parseFloat("10.33") is **10.33**. parseFloat("99 88") is **99** (Number("99 88") was NaN).',
    ),
    S(
        "parseint",
        'parseInt("10.33")',
        [
            "**parseInt** parses a leading **integer** (stops at the decimal point).",
        ],
        'parseInt("10.33");\nparseInt("99 88");',
        [
            ('parseInt("10.33")', 'parseInt("10.33")'),
            ('parseInt("99 88")', 'parseInt("99 88")'),
        ],
        'parseInt("10.33") is **10**. parseInt("99 88") is **99**.',
    ),
    S(
        "unary-plus-5",
        'unary + on "5"',
        [
            "Unary **`+`** converts a numeric string to a number.",
        ],
        'let y = "5";\nlet x = + y;',
        [("y", "y"), ("x", "x"), ("typeof y", "typeof y"), ("typeof x", "typeof x")],
        'y is **"5"** (string). x is **5** (number).',
    ),
    S(
        "unary-plus-john",
        'unary + on "John" is NaN',
        [
            "If unary `+` cannot convert, the result is still a **number**, but the value is **NaN**.",
        ],
        'let y = "John";\nlet x = + y;',
        [("x", "x"), ("typeof x", "typeof x")],
        "x is **NaN**. typeof is **\"number\"**.",
    ),
    S(
        "string-variable",
        "String(x) from a number variable",
        [
            "Global **`String()`** converts any value to a string.",
        ],
        "let x = 123;\nString(x);",
        [("String(x)", "String(x)"), ("typeof String(x)", "typeof String(x)")],
        'String(x) is **"123"**. typeof is **"string"**.',
    ),
    S(
        "string-literal",
        "String(123)",
        ["String() on a number **literal**."],
        "String(123);",
        [("String(123)", "String(123)")],
        'String(123) is **"123"**.',
    ),
    S(
        "string-expression",
        "String(100 + 23)",
        ["String() on an **expression** (adds first, then stringifies)."],
        "String(100 + 23);",
        [("String(100 + 23)", "String(100 + 23)")],
        'String(100 + 23) is **"123"**.',
    ),
    S(
        "tostring-variable",
        "x.toString()",
        ["Number **`toString()`** does the same as String(x) for a number."],
        "let x = 123;\nx.toString();",
        [("x.toString()", "x.toString()")],
        'x.toString() is **"123"**.',
    ),
    S(
        "tostring-literal",
        "(123).toString()",
        ["Parentheses are required on a **literal**: `(123).toString()`."],
        "(123).toString();",
        [("(123).toString()", "(123).toString()")],
        '(123).toString() is **"123"**.',
    ),
    S(
        "tostring-expression",
        "(100 + 23).toString()",
        ["toString on an expression."],
        "(100 + 23).toString();",
        [("(100 + 23).toString()", "(100 + 23).toString()")],
        '(100 + 23).toString() is **"123"**.',
    ),
    S(
        "toexponential",
        "toExponential()",
        [
            "**toExponential()** returns a string in **exponential** notation.",
        ],
        "let x = 123;\nx.toExponential();",
        [("x.toExponential()", "(123).toExponential()")],
        'this engine printed **"1.23e+2"** for 123.',
    ),
    S(
        "tofixed",
        "toFixed(2)",
        [
            "**toFixed(n)** is a string with **n** digits after the decimal (rounded).",
        ],
        "let x = 123.456;\nx.toFixed(2);",
        [("x.toFixed(2)", "(123.456).toFixed(2)")],
        'toFixed(2) is **"123.46"**.',
    ),
    S(
        "toprecision",
        "toPrecision(4)",
        [
            "**toPrecision(n)** is a string with **n** significant digits.",
        ],
        "let x = 123.456;\nx.toPrecision(4);",
        [("x.toPrecision(4)", "(123.456).toPrecision(4)")],
        'toPrecision(4) is **"123.5"**.',
    ),
    S(
        "date-to-number",
        "Number(date) — ms since epoch",
        [
            "**Number(date)** is the same millisecond count as **`getTime()`**.",
            "Fixed instant so the snap is stable.",
        ],
        f"{FIX}\nNumber(d);\nd.getTime();",
        [("Number(d)", "Number(d)"), ("d.getTime()", "d.getTime()")],
        "Both are **1616686245123**.",
    ),
    S(
        "string-date-now",
        "String(Date()) — Date() as a function",
        [
            "**`Date()`** (no `new`) already returns a **string** of **now**.",
            "String(Date()) stringifies that string (no change). Snap is the **current local** clock.",
        ],
        "String(Date());",
        [("String(Date())", "String(Date())")],
        "The snap shows this engine's **current local** date/time string.",
    ),
    S(
        "date-fn-tostring",
        "Date().toString() — already a string",
        [
            "`Date()` returns a string, and strings have **toString()** (identity).",
        ],
        "Date().toString();",
        [("Date().toString()", "Date().toString()")],
        "The snap shows this engine's **current local** date/time string (same family as String(Date())).",
    ),
    S(
        "getfullyear-tostring",
        "getFullYear().toString()",
        [
            "Date-part getters return **numbers**. **toString()** makes a string.",
            "W3Schools Tryit uses now; this sandbox uses the **fixed** instant.",
        ],
        f"{FIX}\nd.getFullYear().toString();",
        [("d.getFullYear()", "d.getFullYear()"), ("d.getFullYear().toString()", "d.getFullYear().toString()")],
        'getFullYear is **2021**. toString is **"2021"**.',
    ),
    S(
        "getmonth-tostring",
        "getMonth().toString() — 0-based",
        [
            "`getMonth()` is **0–11**. March is **2**.",
        ],
        f"{FIX}\nd.getMonth().toString();",
        [("d.getMonth()", "d.getMonth()"), ("d.getMonth().toString()", "d.getMonth().toString()")],
        'getMonth is **2**. toString is **"2"**.',
    ),
    S(
        "getdate-tostring",
        "getDate().toString()",
        [
            "`getDate()` is the local **day of month** (1–31).",
        ],
        f"{FIX}\nd.getDate().toString();",
        [("d.getDate()", "d.getDate()"), ("d.getDate().toString()", "d.getDate().toString()")],
        'getDate is **25**. toString is **"25"**.',
    ),
    S(
        "getday-tostring",
        "getDay().toString() — weekday 0–6",
        [
            "`getDay()` is the local **weekday**. **0 is Sunday**. This instant is Thursday.",
        ],
        f"{FIX}\nd.getDay().toString();",
        [("d.getDay()", "d.getDay()"), ("d.getDay().toString()", "d.getDay().toString()")],
        'getDay is **4**. toString is **"4"**.',
    ),
    S(
        "gethours-tostring",
        "getHours().toString()",
        [
            "`getHours()` is local **0–23**. This UTC 15:30 is **09** Mountain (UTC−6).",
        ],
        f"{FIX}\nd.getHours().toString();",
        [("d.getHours()", "d.getHours()"), ("d.getHours().toString()", "d.getHours().toString()")],
        'getHours is **9**. toString is **"9"**.',
    ),
    S(
        "getminutes-tostring",
        "getMinutes().toString() — 0–59 (not 0–23)",
        [
            "The W3Schools table says getMinutes 0–23; the real range is **0–59**.",
        ],
        f"{FIX}\nd.getMinutes().toString();",
        [("d.getMinutes()", "d.getMinutes()"), ("d.getMinutes().toString()", "d.getMinutes().toString()")],
        'getMinutes is **30**. toString is **"30"**.',
    ),
    S(
        "getseconds-tostring",
        "getSeconds().toString()",
        [
            "`getSeconds()` is **0–59**.",
        ],
        f"{FIX}\nd.getSeconds().toString();",
        [("d.getSeconds()", "d.getSeconds()"), ("d.getSeconds().toString()", "d.getSeconds().toString()")],
        'getSeconds is **45**. toString is **"45"**.',
    ),
    S(
        "getmilliseconds-tostring",
        "getMilliseconds().toString()",
        [
            "`getMilliseconds()` is **0–999**.",
        ],
        f"{FIX}\nd.getMilliseconds().toString();",
        [("d.getMilliseconds()", "d.getMilliseconds()"), ("d.getMilliseconds().toString()", "d.getMilliseconds().toString()")],
        'getMilliseconds is **123**. toString is **"123"**.',
    ),
    S(
        "month-plus-one",
        "(getMonth()+1).toString() — 1–12",
        [
            "Add **1** to getMonth for a **1–12** month number.",
        ],
        f"{FIX}\n(d.getMonth() + 1).toString();",
        [("d.getMonth() + 1", "d.getMonth() + 1"), ("(d.getMonth() + 1).toString()", "(d.getMonth() + 1).toString()")],
        'getMonth()+1 is **3**. toString is **"3"**.',
    ),
    S(
        "month-long-name",
        "toLocaleString month:'long'",
        [
            "`toLocaleString` with `{ month: 'long' }` is the **month name**.",
        ],
        f"{FIX}\nd.toLocaleString('default', {{ month: 'long' }});",
        [("month", "d.toLocaleString('default', { month: 'long' })")],
        'This engine printed **"March"**.',
    ),
    S(
        "number-false",
        "Number(false) is 0",
        ["**Number(false)** is **0**."],
        "Number(false);",
        [("Number(false)", "Number(false)")],
        "Number(false) is **0**.",
    ),
    S(
        "number-true",
        "Number(true) is 1",
        ["**Number(true)** is **1**."],
        "Number(true);",
        [("Number(true)", "Number(true)")],
        "Number(true) is **1**.",
    ),
    S(
        "string-false",
        'String(false) is "false"',
        ["**String(false)** is the string **\"false\"**."],
        "String(false);",
        [("String(false)", "String(false)")],
        'String(false) is **"false"**.',
    ),
    S(
        "string-true",
        'String(true) is "true"',
        ["**String(true)** is the string **\"true\"**."],
        "String(true);",
        [("String(true)", "String(true)")],
        'String(true) is **"true"**.',
    ),
    S(
        "false-tostring",
        'false.toString() is "false"',
        ["Boolean **toString** matches String()."],
        "false.toString();",
        [("false.toString()", "false.toString()")],
        'false.toString() is **"false"**.',
    ),
    S(
        "true-tostring",
        'true.toString() is "true"',
        ["Boolean **toString** matches String()."],
        "true.toString();",
        [("true.toString()", "true.toString()")],
        'true.toString() is **"true"**.',
    ),
    S(
        "auto-5-plus-null",
        "5 + null — null becomes 0",
        ["Automatic conversion: **null** becomes **0** in numeric `+`."],
        "5 + null;",
        [("5 + null", "5 + null")],
        "5 + null is **5**.",
    ),
    S(
        "auto-str5-plus-null",
        '"5" + null — null becomes "null"',
        ["With string `+`, **null** becomes the string **\"null\"**."],
        '"5" + null;',
        [('"5" + null', '"5" + null')],
        '"5" + null is **"5null"**.',
    ),
    S(
        "auto-str5-plus-2",
        '"5" + 2 — 2 becomes "2"',
        ["String `+` concatenates."],
        '"5" + 2;',
        [('"5" + 2', '"5" + 2')],
        '"5" + 2 is **"52"**.',
    ),
    S(
        "auto-str5-minus-2",
        '"5" - 2 — "5" becomes 5',
        ["`-` forces numbers."],
        '"5" - 2;',
        [('"5" - 2', '"5" - 2')],
        '"5" - 2 is **3**.',
    ),
    S(
        "auto-str5-times-str2",
        '"5" * "2" — both become numbers',
        ["`*` forces numbers on both strings."],
        '"5" * "2";',
        [('"5" * "2"', '"5" * "2"')],
        '"5" * "2" is **10**.',
    ),
    S(
        "auto-string-object",
        'Automatic toString — object → "[object Object]"',
        ["Output / string context calls **toString** on the value."],
        'let myVar = {name: "Fjohn"};\nString(myVar);',
        [("String(myVar)", "String(myVar)")],
        'String({name:"Fjohn"}) is **"[object Object]"**.',
    ),
    S(
        "auto-string-array",
        'Automatic toString — array → "1,2,3,4"',
        ["Arrays stringify as a comma list."],
        "let myVar = [1, 2, 3, 4];\nString(myVar);",
        [("String(myVar)", "String(myVar)")],
        'String([1,2,3,4]) is **"1,2,3,4"**.',
    ),
    S(
        "auto-string-date",
        "Automatic toString — Date",
        ["Dates stringify like `toString()` (local)."],
        f"{FIX}\nString(d);",
        [("String(d)", "String(d)")],
        'String(d) is **"Thu Mar 25 2021 09:30:45 GMT-0600 (Mountain Daylight Time)"**.',
    ),
    S(
        "auto-string-number",
        'Automatic toString — 123 → "123"',
        ["Numbers stringify in decimal."],
        "String(123);",
        [("String(123)", "String(123)")],
        'String(123) is **"123"**.',
    ),
    S(
        "auto-string-true",
        'Automatic toString — true → "true"',
        ["Booleans stringify as **\"true\"** / **\"false\"**."],
        "String(true);\nString(false);",
        [("String(true)", "String(true)"), ("String(false)", "String(false)")],
        'true → **"true"**. false → **"false"**.',
    ),
]


def _conv(stem: str, label: str, setup: str, expr: str, n: str, s: str, b: str) -> dict:
    return S(
        stem,
        f"Convert {label}",
        [
            f"Conversion-table row: original **{label}**.",
            "**Number()**, **String()**, and **Boolean()** are separate conversions on the same value.",
        ],
        setup,
        [
            (f"Number({expr})", f"Number({expr})"),
            (f"String({expr})", f"String({expr})"),
            (f"Boolean({expr})", f"Boolean({expr})"),
        ],
        f"Number → **{n}**. String → **{s}**. Boolean → **{b}**.",
    )


CONVERSION += [
    _conv("conv-false", "false", "let v = false;", "v", "0", '"false"', "false"),
    _conv("conv-true", "true", "let v = true;", "v", "1", '"true"', "true"),
    _conv("conv-0", "0", "let v = 0;", "v", "0", '"0"', "false"),
    _conv("conv-1", "1", "let v = 1;", "v", "1", '"1"', "true"),
    _conv("conv-str-0", '"0"', 'let v = "0";', "v", "0", '"0"', "true"),
    _conv("conv-str-000", '"000"', 'let v = "000";', "v", "0", '"000"', "true"),
    _conv("conv-str-1", '"1"', 'let v = "1";', "v", "1", '"1"', "true"),
    _conv("conv-nan", "NaN", "let v = NaN;", "v", "NaN", '"NaN"', "false"),
    _conv("conv-infinity", "Infinity", "let v = Infinity;", "v", "Infinity", '"Infinity"', "true"),
    _conv("conv-neginfinity", "-Infinity", "let v = -Infinity;", "v", "-Infinity", '"-Infinity"', "true"),
    _conv("conv-empty-str", '""', 'let v = "";', "v", "0", '""', "false"),
    _conv("conv-str-20", '"20"', 'let v = "20";', "v", "20", '"20"', "true"),
    _conv("conv-str-twenty", '"twenty"', 'let v = "twenty";', "v", "NaN", '"twenty"', "true"),
    _conv("conv-empty-arr", "[ ]", "let v = [];", "v", "0", '""', "true"),
    _conv("conv-arr-20", "[20]", "let v = [20];", "v", "20", '"20"', "true"),
    _conv("conv-arr-10-20", "[10,20]", "let v = [10, 20];", "v", "NaN", '"10,20"', "true"),
    _conv("conv-arr-twenty", '["twenty"]', 'let v = ["twenty"];', "v", "NaN", '"twenty"', "true"),
    _conv("conv-arr-ten-twenty", '["ten","twenty"]', 'let v = ["ten", "twenty"];', "v", "NaN", '"ten,twenty"', "true"),
    _conv("conv-function", "function(){}", "let v = function(){};", "v", "NaN", '"function(){}"', "true"),
    _conv("conv-object", "{ }", "let v = {};", "v", "NaN", '"[object Object]"', "true"),
    _conv("conv-null", "null", "let v = null;", "v", "0", '"null"', "false"),
    _conv("conv-undefined", "undefined", "let v = undefined;", "v", "NaN", '"undefined"', "false"),
]


# ---------------------------------------------------------------------------
# 17.12 JS Destructuring
# ---------------------------------------------------------------------------

DESTRUCTURING = [
    S(
        "object-basic",
        "Object destructuring — {firstName, lastName}",
        [
            "Object destructuring unpacks **matching property names** into variables.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50\n};\nlet {firstName, lastName} = person;',
        [("firstName", "firstName"), ("lastName", "lastName")],
        'firstName is **"John"**. lastName is **"Doe"**. age is not unpacked.',
    ),
    S(
        "object-order",
        "Object destructuring — order does not matter",
        [
            "You may list properties in **any order**. Names match, not positions.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50\n};\nlet {lastName, firstName} = person;',
        [("firstName", "firstName"), ("lastName", "lastName")],
        'Still **"John"** and **"Doe"** — swapping the names in `{ }` does not swap the values.',
    ),
    S(
        "object-defaults",
        'Object default — country = "US"',
        [
            "Missing properties can take a **default**. Present properties keep their value.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50\n};\nlet {firstName, lastName, country = "US"} = person;',
        [("firstName", "firstName"), ("lastName", "lastName"), ("country", "country")],
        'country is **"US"** (default). firstName/lastName still **"John"** / **"Doe"**. The original object is unchanged.',
    ),
    S(
        "object-alias",
        "Object alias — {lastName : name}",
        [
            "`{lastName : name}` reads **lastName** into a variable called **name**.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50\n};\nlet {lastName: name} = person;',
        [("name", "name")],
        'name is **"Doe"**. There is no `lastName` binding from this pattern.',
    ),
    S(
        "string-chars",
        "String destructuring — characters",
        [
            "Strings are **iterable**. Destructuring takes characters in order.",
        ],
        'let name = "W3Schools";\nlet [a1, a2, a3, a4, a5] = name;',
        [("a1", "a1"), ("a2", "a2"), ("a3", "a3"), ("a4", "a4"), ("a5", "a5")],
        'a1–a5 are **"W"**, **"3"**, **"S"**, **"c"**, **"h"**.',
    ),
    S(
        "array-basic",
        "Array destructuring — first two",
        [
            "Array patterns bind by **position**: first variable ← index 0.",
        ],
        'const fruits = ["Bananas", "Oranges", "Apples", "Mangos"];\nlet [fruit1, fruit2] = fruits;',
        [("fruit1", "fruit1"), ("fruit2", "fruit2")],
        'fruit1 is **"Bananas"**. fruit2 is **"Oranges"**.',
    ),
    S(
        "array-skip",
        "Array skip — [fruit1,,,fruit2]",
        [
            "Extra **commas skip** holes. `[a,,,b]` takes index **0** and index **3**.",
        ],
        'const fruits = ["Bananas", "Oranges", "Apples", "Mangos"];\nlet [fruit1, , , fruit2] = fruits;',
        [("fruit1", "fruit1"), ("fruit2", "fruit2")],
        'fruit1 is **"Bananas"**. fruit2 is **"Mangos"** (Oranges and Apples skipped).',
    ),
    S(
        "array-index-names",
        "Array position values — {[0]:fruit1, [1]:fruit2}",
        [
            "You can pick **named indexes** with computed property names on the pattern.",
        ],
        'const fruits = ["Bananas", "Oranges", "Apples", "Mangos"];\nlet {[0]: fruit1, [1]: fruit2} = fruits;',
        [("fruit1", "fruit1"), ("fruit2", "fruit2")],
        'fruit1 is **"Bananas"**. fruit2 is **"Oranges"**.',
    ),
    S(
        "array-rest",
        "Array rest — [a, b, ...rest]",
        [
            "**`...rest`** gathers **remaining** elements into a **new array**.",
        ],
        "const numbers = [10, 20, 30, 40, 50, 60, 70];\nconst [a, b, ...rest] = numbers;",
        [("a", "a"), ("b", "b"), ("rest", "String(rest)")],
        "a is **10**, b is **20**, rest is **30,40,50,60,70**.",
    ),
    S(
        "array-defaults",
        "Array defaults — [a = 'A', b = 'B']",
        [
            "Array holes / missing items take **defaults**, same idea as object defaults.",
        ],
        'let [a = "A", b = "B"] = ["Bananas"];',
        [("a", "a"), ("b", "b")],
        'a is **"Bananas"** (provided). b is **"B"** (default).',
    ),
    S(
        "object-rest",
        "Object rest — {firstName, ...rest}",
        [
            "Object **`...rest`** is a **new object** of the leftover enumerable string keys.",
        ],
        'const person = { firstName: "John", lastName: "Doe", age: 50 };\nlet {firstName, ...rest} = person;',
        [("firstName", "firstName"), ("JSON.stringify(rest)", "JSON.stringify(rest)")],
        'firstName is **"John"**. rest is **{"lastName":"Doe","age":50}**.',
    ),
    S(
        "nested-object",
        "Nested object destructuring",
        [
            "Nest patterns to unpack **inner** objects: `{ address: { city } }`.",
        ],
        'const user = {\n  name: "John",\n  address: { city: "Oslo", zip: "0001" }\n};\nlet { name, address: { city, zip } } = user;',
        [("name", "name"), ("city", "city"), ("zip", "zip")],
        'name **"John"**, city **"Oslo"**, zip **"0001"**. There is no `address` binding unless you also name it.',
    ),
    S(
        "nested-array",
        "Nested array destructuring",
        [
            "Nest `[ ]` inside `[ ]` to unpack inner arrays.",
        ],
        "const pair = [1, [2, 3], 4];\nlet [a, [b, c], d] = pair;",
        [("a", "a"), ("b", "b"), ("c", "c"), ("d", "d")],
        "a **1**, b **2**, c **3**, d **4**.",
    ),
    S(
        "map-entries",
        "Destructuring Map entries in for...of",
        [
            "Maps iterate as **`[key, value]`** pairs — destructure them in the loop.",
        ],
        'const fruits = new Map([\n  ["apples", 500],\n  ["bananas", 300],\n  ["oranges", 200]\n]);\nlet text = "";\nfor (const [key, value] of fruits) {\n  text += key + " is " + value;\n}',
        [("text", "text")],
        'text is **"apples is 500bananas is 300oranges is 200"** (no extra spaces between entries — as written).',
    ),
    S(
        "swap",
        "Swap two variables",
        [
            "`[a, b] = [b, a]` **swaps** without a temp variable.",
        ],
        'let firstName = "John";\nlet lastName = "Doe";\n[firstName, lastName] = [lastName, firstName];',
        [("firstName", "firstName"), ("lastName", "lastName")],
        'After the swap, firstName is **"Doe"**. lastName is **"John"**.',
    ),
    S(
        "not-destructive",
        "Destructuring does not change the source",
        [
            "Unpacking copies values into bindings. The **original** object/array stays.",
        ],
        'const person = { firstName: "John", lastName: "Doe" };\nlet { firstName } = person;\nfirstName = "Jane";',
        [("firstName", "firstName"), ("person.firstName", "person.firstName")],
        'The variable is **"Jane"**. person.firstName is still **"John"**.',
    ),
]
def run_all() -> None:
    sections = [
        (
            "js-data-types",
            "JS Data Types",
            DATA_TYPES,
            "A JavaScript variable can hold eight kinds of data: seven primitives (Number, BigInt, String, Boolean, Undefined, Null, Symbol) and Object. The Object kind includes many built-in types (Array, Map, Date, typed arrays, and more). Types are dynamic: the same binding can hold undefined, then a number, then a string. The + operator concatenates as soon as a string appears; 16 + 4 + \"Volvo\" is 20Volvo because addition runs left to right until the string. typeof reports the runtime type. typeof null is the legacy string \"object\". BigInt literals with n are exact; BigInt(aNumber) is not, because the Number is rounded first.",
            [
                "**8 types:** Number, BigInt, String, Boolean, Undefined, Null, Symbol, Object.",
                "**+ with a string concatenates.** `16 + 4 + \"Volvo\"` is **20Volvo**. `\"Volvo\" + 16 + 4` is **Volvo164**.",
                "Types are **dynamic** — one variable can change from undefined → number → string.",
                "`typeof null` is **\"object\"** (legacy). Null is still a primitive.",
                "**`1234567890123456789012345n`** is exact. **`BigInt(1234567890123456789012345)`** is **1234567890123456824475648n**.",
                "Every built-in object-table row is its own Example, including **Float16Array** (this Chrome has it) and **WeakMap** / **WeakSet**.",
            ],
            [
                ("How many data types can a variable hold?", ["**8** — **7 primitives** plus **Object**."]),
                ("What is `16 + \"Volvo\"`?", ['**"16Volvo"** (string).']),
                ("Why is `16 + 4 + \"Volvo\"` different from `\"Volvo\" + 16 + 4`?", ["Left to right: **20Volvo** vs **Volvo164**.", "A leading string makes later `+` concatenate."]),
                ("Can one variable hold a number then a string?", ["**Yes.** Types are dynamic: `let x; x = 5; x = \"John\"` ends as a **string**."]),
                ("What is `typeof null`?", ['**"object"** — a legacy bug. Use `=== null` to test for null.']),
                ("Are `Symbol()` and `Symbol()` equal?", ["**No.** `===` is **false**. Every Symbol() is unique."]),
                ("What did `BigInt(1234567890123456789012345)` produce here?", ["**1234567890123456824475648n**, not the source digits.", "The argument is a Number first. Prefer **`n`** or **`BigInt(\"…\")`**."]),
                ("What is `typeof` of an array?", ['**"object"**. Use **Array.isArray** to recognize arrays.']),
                ("Is `new Math()` legal?", ["**No.** Math is an object of functions, not a constructor (see Object Types)."]),
                ("What is `new Date(\"2022-03-25\")` locally here?", ["**Thu Mar 24 2022 18:00:00 GMT-0600** — date-only ISO is UTC midnight."]),
                ("What did Float16Array print in this Chrome?", ["**1.5,2**. typeof Float16Array is **\"function\"**."]),
                ("What is `typeof Promise.resolve(\"ok\")`?", ['**"object"**. `instanceof Promise` is **true**.']),
            ],
            "Remember the eight types, that + concatenates once a string appears, and that typeof null is the string object. Prefer BigInt literals or BigInt of a string. Built-in objects still typeof as object except functions.",
            [
                ("JS Data Types (W3Schools)", "https://www.w3schools.com/js/js_datatypes.asp"),
                ("MDN: JavaScript data types and data structures", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures"),
                ("MDN: BigInt", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt"),
            ],
        ),
        (
            "js-primitive-data",
            "JS Primitive Data",
            PRIMITIVES,
            "The seven primitives are Number, BigInt, String, Boolean, Undefined, Null, and Symbol. Strings use single or double quotes; inner quotes must differ from the outer pair. All ordinary numbers are 64-bit floats, so 34.00 equals 34, and 123e5 is 12300000. BigInt(\"…\") keeps long integers exact; mixing BigInt with Number throws TypeError. A declared variable with no value is undefined. An empty string is a real string, not undefined. null is a primitive whose typeof is still \"object\". Prefer === when checking null — == also matches undefined.",
            [
                "Seven primitives: **string, number, boolean, bigint, symbol, null, undefined**.",
                "`34.00 === 34` is **true**. `123e5` is **12300000**. `123e-5` is **0.00123**.",
                '`BigInt("123…890")` is exact. **`1n + 1` is TypeError**.',
                '`let car;` is **undefined**. `let car = ""` is a **string**. `let carName = null` is **null**.',
                "`typeof null` is **\"object\"**. `null === undefined` is **false**; `null == undefined` is **true**.",
            ],
            [
                ("Are `'Volvo XC60'` and `\"Volvo XC60\"` different types?", ["**No.** Both are strings and **===** each other."]),
                ("Can you put a single quote inside double quotes?", ['**Yes.** `"It\'s alright"` and `"He is called \'Johnny\'"` run.']),
                ("Is `34.00` a different type from `34`?", ["**No.** Both are **number**. `34.00 === 34` is **true**."]),
                ("What is `123e5`?", ["**12300000**."]),
                ("What is `123e-5`?", ["**0.00123**."]),
                ("What happens with `1n + 1`?", ["**TypeError: Cannot mix BigInt and other types, use explicit conversions**."]),
                ("What is `(5 == 5)` vs `(5 == 6)`?", ["**true** and **false** — booleans from comparison."]),
                ("Is `\"\"` undefined?", ["**No.** Value `\"\"`, typeof **\"string\"**."]),
                ("How do you test for null?", ["Use **`=== null`**. Avoid `==`, which is also true for **undefined**."]),
                ("What is `typeof null`?", ['**"object"** (legacy). Null is still a primitive.']),
                ("What is `null === null`?", ["**true**."]),
                ("Does emptying with `undefined` change the type?", ["**Yes** — both value and type become **undefined**."]),
            ],
            "Primitives are not objects. Empty string is not undefined. null is not an object despite typeof. Keep BigInt math in BigInt-land or convert explicitly.",
            [
                ("JS Primitives (W3Schools)", "https://www.w3schools.com/js/js_datatypes_primitives.asp"),
                ("MDN: Primitive", "https://developer.mozilla.org/en-US/docs/Glossary/Primitive"),
                ("MDN: null", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null"),
            ],
        ),
        (
            "js-object-types",
            "JS Object Types",
            OBJECT_TYPES,
            "Besides primitives, JavaScript has objects: literal { } collections, arrays, maps, sets, dates, regexps, errors, JSON, promises, and typed arrays. typeof is \"object\" for almost all of them (functions are \"function\"). Math and JSON are singleton objects, not constructors — new Math() is TypeError. Arrays are 0-based. WeakMap and WeakSet hold objects weakly and cannot be listed. Date-only ISO strings are UTC midnight, so this Mountain zone prints the previous evening.",
            [
                "Literal objects: **`{ firstName:\"John\", … }`**. Arrays: **`[\"Saab\", \"Volvo\", \"BMW\"]`** with **`[0]`** first.",
                "Table rows each have an Example: Array, Map, Set, WeakMap, WeakSet, Math, Date, RegExp, Error, JSON, Promise, and the typed arrays including **Float16Array**.",
                "**`new Math()`** is **TypeError: Math is not a constructor**.",
                "typeof array/map/set/date is **\"object\"**. Recognize arrays with **Array.isArray**.",
            ],
            [
                ("What are the four person properties in the Tryit?", ["**firstName, lastName, age, eyeColor**. firstName is **\"John\"**, age **50**."]),
                ("What is `cars[0]`?", ['**"Saab"**. Indexes are 0-based.']),
                ("What is `typeof` of a Map?", ['**"object"**. Use **instanceof Map**.']),
                ("Does a Set keep duplicate `\"A\"`?", ["**No.** size is **2** for `[\"A\",\"B\",\"A\"]`."]),
                ("Can you iterate a WeakMap?", ["**No.** You can `get`/`set`/`has` while the key object lives. String is **[object WeakMap]**."]),
                ("What is Math.PI?", ["**3.141592653589793**. typeof Math is **\"object\"**."]),
                ("What happens with `new Math()`?", ["**TypeError: Math is not a constructor**."]),
                ("What is `JSON.stringify({name:\"John\"})`?", ['**{"name":"John"}**. JSON is not a constructor.']),
                ("What is `typeof` of a Promise?", ['**"object"**. instanceof Promise is **true**.']),
                ("What did `new Date(\"2022-03-25\")` print locally?", ["**Thu Mar 24 2022 18:00:00 GMT-0600**."]),
                ("What is Int8Array BYTES_PER_ELEMENT?", ["**1**. Int16 → **2**, Int32 → **4**, Float32 → **4**, Float64 → **8**."]),
                ("Does this Chrome have Float16Array?", ["**Yes.** `new Float16Array([1.5, 2])` prints **1.5,2**."]),
            ],
            "Treat arrays, dates, maps, and typed arrays as objects with specialized APIs. Do not construct Math or JSON. Date-only ISO is UTC.",
            [
                ("JS Built-In Objects (W3Schools)", "https://www.w3schools.com/js/js_datatypes_objects.asp"),
                ("MDN: Object", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object"),
                ("MDN: Indexed collections", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections"),
            ],
        ),
        (
            "js-symbols",
            "JS Symbols",
            SYMBOLS,
            "A Symbol is a unique primitive identifier. Symbol() is never === another Symbol(), even with the same description — the description is only for debugging. Symbol.for(key) reuses a global registry, so the same key returns the same symbol. Symbol keys on objects are skipped by for...in and JSON.stringify, and they do not create a string property like person.id. Well-known symbols (iterator, asyncIterator, toStringTag, toPrimitive) hook language behavior. Implicit Symbol + string throws TypeError; use String(sym).",
            [
                "`Symbol()` is always **unique**. `Symbol(\"id\") === Symbol(\"id\")` is **false**.",
                "`Symbol.for(\"id\") === Symbol.for(\"id\")` is **true**. `Symbol.keyFor` reads the registry key.",
                "Symbol keys are hidden from **for...in** and **JSON.stringify**. `person.id` stays **undefined**.",
                "`typeof` a symbol is **\"symbol\"**. `Symbol + \"\"` is **TypeError**.",
                "Well-known: **iterator**, **asyncIterator**, **toStringTag**, **toPrimitive**.",
            ],
            [
                ("Are two `Symbol()` values equal?", ["**No.** `===` is **false**."]),
                ("Does a matching description make them equal?", ["**No.** `Symbol(\"id\") === Symbol(\"id\")` is still **false**."]),
                ("What does `Symbol.for(\"id\")` do?", ["Reuses a **global** symbol. Two calls with `\"id\"` are **=== true**."]),
                ("What is `Symbol.keyFor(Symbol(\"id\"))`?", ["**undefined** — local symbols are not in the registry."]),
                ("What is `person[id]` vs `person.id` after `person[id] = 140353`?", ["Symbol key **140353**. String key **undefined**."]),
                ("Does `for...in` show symbol keys?", ["**No.** text is **\"firstName lastName \"**."]),
                ("Does `JSON.stringify` include symbol keys?", ["**No.** `{\"name\":\"John\"}` only."]),
                ("What is `typeof Symbol(\"id\")`?", ['**"symbol"**.']),
                ("What happens with `Symbol(\"id\") + \"\"`?", ["**TypeError: Cannot convert a Symbol value to a string**.", '`String(Symbol("id"))` is **"Symbol(id)"**.']),
                ("What did the custom iterator print?", ['**"A B C "** from for...of.']),
                ("What is `Object.prototype.toString.call({[Symbol.toStringTag]:\"Foo\"})`?", ['**"[object Foo]"**.']),
                ("What does `Symbol.toPrimitive` return for Number(o) in the demo?", ["**42**. String(o) is **\"ok\"**. `o + 1` is **\"ok1\"**."]),
            ],
            "Use Symbol when you need unique hidden keys or well-known hooks. Use Symbol.for only when you want a shared global identity. Never concatenate a Symbol with a string.",
            [
                ("JS Symbols (W3Schools)", "https://www.w3schools.com/js/js_datatypes_symbol.asp"),
                ("MDN: Symbol", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol"),
                ("MDN: Well-known symbols", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#well-known_symbols"),
            ],
        ),
        (
            "js-typeof",
            "JS typeof",
            TYPEOF,
            "typeof returns a type string: string, number, boolean, bigint, symbol, undefined, object, or function. It does not distinguish arrays, dates, maps, or sets — those are all object. typeof null is object (legacy). typeof of an undeclared name is undefined and does not throw. Array.isArray and instanceof (and constructor) tell object kinds apart. undefined and null compare equal with == and unequal with ===. void 0 is a reliable undefined. NaN’s typeof is number.",
            [
                "Primitives: **string / number / boolean / bigint / symbol / undefined**. **null → \"object\"** (bug).",
                "Complex: **object** for `{}`, `[]`, Date, Map, Set. **function** for functions.",
                "**Array.isArray** and **instanceof** (Date, Array, Map, Set) split object kinds. **constructor** also works.",
                "`typeof` of an **undeclared** name is **\"undefined\"**. Reading the name is **ReferenceError**.",
                "`null == undefined` **true**; `null === undefined` **false**. **`void 0`** is **undefined**.",
                "**typeof NaN** is **\"number\"**.",
            ],
            [
                ("What is `typeof \"John\"`?", ['**"string"**.']),
                ("What is `typeof 3.14`?", ['**"number"**.']),
                ("What is `typeof 1234n`?", ['**"bigint"**.']),
                ("What is `typeof Symbol()`?", ['**"symbol"**.']),
                ("What is `typeof null`?", ['**"object"** — legacy. Test with `=== null`.']),
                ("What is `typeof NaN`?", ['**"number"**.']),
                ("What is `typeof function () {}`?", ['**"function"**.']),
                ("What is `typeof [1,2,3,4]`?", ['**"object"**. Use **Array.isArray** — **true** for that array.']),
                ("Does `typeof car` throw if car was never declared?", ["**No.** It is **\"undefined\"**."]),
                ("person = null vs person = undefined — types?", ["null → typeof **\"object\"**. undefined → typeof **\"undefined\"**."]),
                ("`null === undefined` and `null == undefined`?", ["**false** and **true**."]),
                ("What is `{name:'John',age:34}.constructor === Object`?", ["**true**. String(constructor) is **function Object() { [native code] }**."]),
                ("What is `void 0`?", ["**undefined**. typeof is **\"undefined\"**."]),
                ("Can typeof tell a Date from an Array?", ["**No.** Both **\"object\"**. Use **instanceof** / **constructor** / **Array.isArray**."]),
            ],
            "Trust typeof for primitives and functions. For objects, follow up with Array.isArray, instanceof, or constructor. Remember the null bug and that NaN is a number. void 0 is undefined.",
            [
                ("JS typeof (W3Schools)", "https://www.w3schools.com/js/js_typeof.asp"),
                ("MDN: typeof", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof"),
                ("MDN: instanceof", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof"),
                ("MDN: void operator", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void"),
            ],
        ),
        (
            "js-undefined",
            "JS undefined",
            UNDEFINED,
            "undefined means a variable was declared but not given a value. typeof is also undefined. Missing object properties and functions without return produce undefined. An empty string is not undefined. The W3Schools snippet that reassigns a const person to undefined is a TypeError in real JS — use let. Reading a name that was never declared is ReferenceError; typeof that name is still undefined. undefined == null is true; === is false.",
            [
                "`let car;` → value **undefined**, typeof **\"undefined\"**.",
                'Empty string **`""`** is a **string**, not undefined.',
                "Missing property **person.age** is **undefined** (no throw).",
                "No `return` → **undefined**.",
                "`const person = …; person = undefined` is **TypeError**. **`let`** can be emptied.",
                "Undeclared read is **ReferenceError**. `typeof missing` is **\"undefined\"**.",
            ],
            [
                ("What is the value of `let car;`?", ["**undefined**."]),
                ("What is `typeof car` then?", ['**"undefined"**.']),
                ("Is `\"\"` undefined?", ["**No.** typeof **\"string\"**."]),
                ("What is `person.age` if age was never set?", ["**undefined**."]),
                ("What does a function with no return return?", ["**undefined**."]),
                ("Does `const person = {}; person = undefined` work?", ["**No. TypeError: Assignment to constant variable.**"]),
                ("How do you empty a binding?", ["Use **`let`**, then assign **undefined** or **null**."]),
                ("What is `typeof` after assigning null?", ['**"object"** (legacy). After undefined: **"undefined"**.']),
                ("What is reading a never-declared `missing`?", ["**ReferenceError: missing is not defined**.", '`typeof missing` is still **"undefined"**.']),
                ("Is `undefined == null`?", ["**true**. `===` is **false**."]),
                ("Does undefined mean the variable does not exist?", ["**No.** It exists but has **no assigned value**. Never-declared is a **ReferenceError**."]),
            ],
            "undefined is a value, not a missing binding. Empty string and null are different. const cannot be emptied by assignment. typeof is the safe probe for undeclared names.",
            [
                ("JS undefined (W3Schools)", "https://www.w3schools.com/js/js_undefined.asp"),
                ("MDN: undefined", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined"),
                ("MDN: ReferenceError", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError"),
            ],
        ),
        (
            "js-nan",
            "JS NaN",
            NAN,
            "NaN means Not a Number, but typeof NaN is number. You get NaN from invalid math such as 100 / \"Apple\" or 0 / 0. Numeric strings still work: 100 / \"10\" is 10. NaN is the only value that is not == or === to itself. Do not write x === NaN. Use Number.isNaN (no coercion). Global isNaN(\"Apple\") is true because it coerces; Number.isNaN(\"Apple\") is false. Math with NaN stays NaN. Object.is(NaN, NaN) is true.",
            [
                '`100 / "Apple"` is **NaN**. `100 / "10"` is **10**.',
                "**typeof NaN** is **\"number\"**.",
                "**NaN !== NaN**. `NaN == NaN` is **false**. Use **Number.isNaN**.",
                '`isNaN("Apple")` is **true** (coerces). `Number.isNaN("Apple")` is **false**.',
                "**NaN + 5** is **NaN**. **0 / 0** is **NaN**. **1 / 0** is **Infinity**.",
            ],
            [
                ("What is `100 / \"Apple\"`?", ["**NaN**."]),
                ("What is `typeof NaN`?", ['**"number"**.']),
                ("What is `100 / \"10\"`?", ["**10** — numeric strings coerce in arithmetic."]),
                ("Is `NaN === NaN`?", ["**false**. `NaN !== NaN` is **true**."]),
                ("How should you test for NaN?", ["**Number.isNaN(x)**. Not `x === NaN`."]),
                ("Why is `isNaN(\"Apple\")` true?", ["Global isNaN **coerces** the string to NaN. **Number.isNaN(\"Apple\")** is **false**."]),
                ("What is `NaN + 5`?", ["**NaN**."]),
                ("What is `0 / 0` vs `1 / 0`?", ["**NaN** vs **Infinity**."]),
                ("What is `Object.is(NaN, NaN)`?", ["**true**."]),
                ("What is `parseInt(\"abc\")`?", ["**NaN**."]),
                ("Is NaN a legal number value?", ["It is a **number** that is **not a legal numeric result** — Not a Number."]),
            ],
            "Treat NaN as a number that failed. Compare with Number.isNaN or Object.is, never ===. Arithmetic that cannot produce a number, including 0/0, yields NaN.",
            [
                ("JS NaN (W3Schools)", "https://www.w3schools.com/js/js_nan.asp"),
                ("MDN: NaN", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN"),
                ("MDN: Number.isNaN", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN"),
            ],
        ),
        (
            "js-tostring",
            "JS toString()",
            TOSTRING,
            "toString() turns a value into a string. Arrays become comma-separated lists with no spaces. Dates become a local date/time/zone string. Numbers become decimal text, or another radix such as toString(2) for binary. Functions return their source. Plain objects return [object Object] unless you override toString. null and undefined have no toString method — calling it is TypeError; use String(null) instead.",
            [
                '`["Banana","Orange","Apple","Mango"].toString()` is **"Banana,Orange,Apple,Mango"**.',
                "`(123).toString()` is **\"123\"**. `(123).toString(2)` is **\"1111011\"**.",
                'Default object toString is **"[object Object]"**. Override it to print real fields.',
                "`null.toString()` / `undefined.toString()` are **TypeError**. Use **String(null)**.",
                "Date toString is **local**. Fixed instant: **Thu Mar 25 2021 09:30:45 GMT-0600 (Mountain Daylight Time)**.",
            ],
            [
                ("What is fruits.toString() for Banana/Orange/Apple/Mango?", ['**"Banana,Orange,Apple,Mango"** (no spaces).']),
                ("What is `(123).toString()`?", ['**"123"**.']),
                ("What is `(123).toString(2)`?", ['**"1111011"**.']),
                ("What is a function’s toString?", ["Its **source text**, e.g. **function add(a, b) { return a + b; }**."]),
                ("What is `{firstname, lastname}.toString()` by default?", ['**"[object Object]"**.']),
                ("How do you make an object print usefully?", ["Override **toString**. The demo returns **\"John Doe\"**."]),
                ("What is `true.toString()`?", ['**"true"**. false → **"false"**.']),
                ("Can you call `null.toString()`?", ["**No. TypeError.** Use **String(null)** → **\"null\"**."]),
                ("Is Date toString UTC?", ["**No.** It is **local** plus a zone name. ISO is `toISOString()`."]),
                ("Does array toString add spaces after commas?", ["**No.**"]),
            ],
            "Use toString for a readable string, but know the defaults: arrays join with commas, objects say [object Object], and null/undefined throw. Override object toString when you need a real dump.",
            [
                ("JS toString() (W3Schools)", "https://www.w3schools.com/js/js_tostring.asp"),
                ("MDN: Object.prototype.toString", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString"),
                ("MDN: Number.prototype.toString", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString"),
            ],
        ),
        (
            "js-tolocalestring",
            "JS toLocaleString()",
            TOLOCALE,
            "toLocaleString formats a value using locale rules. This Chrome is en-US: 1234567.89 prints 1,234,567.89 by default. de-DE uses 1.234.567,89. no-NO uses nbsp grouping: 1 234 567,89. Currency, percent, and fraction-digit options change the output. Date-only ISO strings are UTC midnight, so an array of 2026-01-01 and 2026-12-24 printed 12/31/2025, 5:00:00 PM and 12/23/2026, 5:00:00 PM in Mountain time — not the UTC calendar dates. BigInt also supports toLocaleString.",
            [
                "This engine: **en-US**. Default number **" + "1,234,567.89**.",
                'de-DE **"1.234.567,89"**. no-NO **"1 234 567,89"** (nbsp).',
                'USD **"$1,299.95"**. EUR **"1.299,95 €"**. NOK **"1 299,95 kr"**. percent **"88%"**. 3.14159 → **"3.14"**.',
                "Date `en-US` on the fixed instant: **" + "3/25/2021, 9:30:45 AM**. Long: **Thursday, March 25, 2021**.",
                TZ + " Array demo printed **12/31/2025, 5:00:00 PM,12/23/2026, 5:00:00 PM**.",
                "The method name is **toLocaleString** (locale, not local).",
            ],
            [
                ("What did `num.toLocaleString()` print here?", ['**"1,234,567.89"**. navigator.language **"en-US"**.']),
                ("What is de-DE for that number?", ['**"1.234.567,89"** (dot thousands, comma decimal).']),
                ("What is no-NO for that number?", ['**"1 234 567,89"** with nbsp grouping.']),
                ("What is 1299.95 as USD / EUR / NOK here?", ['**"$1,299.95"**, **"1.299,95 €"**, **"1 299,95 kr"**.']),
                ("What is `0.875` as percent en-US?", ['**"88%"**.']),
                ("What is 3.14159 with min/max fraction digits 2?", ['**"3.14"**.']),
                ("What is the fixed Date in en-US?", ['**"3/25/2021, 9:30:45 AM"** (Mountain).']),
                ("What is the long weekday form?", ['**"Thursday, March 25, 2021"**.']),
                ("What did `fileSize(1536000)` return?", ['**"1.5 MB"**.']),
                ("Why did the date array show Dec 31 2025?", ["Date-only ISO is **UTC midnight**. Mountain is **17:00 the previous day** in winter."]),
                ("Does BigInt support toLocaleString?", ["**Yes.** 1234567890123456789n → **\"1,234,567,890,123,456,789\"** here."]),
                ("Is the method `toLocalString`?", ["**No.** It is **toLocaleString** (locale = language + country)."]),
            ],
            "Always report what this engine printed — locales differ. Pass an explicit locale for stable formatting. Treat date-only ISO as UTC when you locale-format Dates.",
            [
                ("JS toLocaleString() (W3Schools)", "https://www.w3schools.com/js/js_tolocalestring.asp"),
                ("MDN: Number.prototype.toLocaleString", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toLocaleString"),
                ("MDN: Date.prototype.toLocaleString", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString"),
            ],
        ),
        (
            "js-type-coercion",
            "JS Type Coercion",
            COERCION,
            "Coercion is implicit conversion when operators mix types. + concatenates if either side is a string (\"5\"+2 is \"52\"). -, *, /, %, and unary + force numbers (\"5\"-2 is 3). Boolean contexts treat 0, \"\", null, undefined, NaN, and false as falsy; everything else is truthy, including {} and []. == coerces (5==\"5\" is true; 0==false is true). === does not (both false). A failed numeric coerce is NaN (\"abc\"-1).",
            [
                "**Implicit** vs **explicit** (Number/String/Boolean). JS is weakly typed — mixed types rarely throw.",
                "`+` with a string → **concat**. Other arithmetic → **numbers**.",
                "Falsy: **0, \"\", null, undefined, NaN, false**. Truthy: **{}**, **[]**, and the rest.",
                "`==` coerces. `===` does not. Prefer **===**.",
                '`"abc" - 1` is **NaN**.',
            ],
            [
                ("What is `'5' + '2'` vs `'5' - '2'`?", ['**"52"** (string) vs **3** (number).']),
                ("What is `\"5\" + 2`?", ['**"52"**.']),
                ("What is `\"5\" - 2`?", ["**3**."]),
                ("What is `\"5\" * 2`?", ["**10**."]),
                ("What is `\"5\" / 2`?", ["**2.5**."]),
                ("What is `\"5\" % 2`?", ["**1**."]),
                ("What is `+\"5\"`?", ["**5** (number)."]),
                ("What is `5 == \"5\"` vs `5 === \"5\"`?", ["**true** vs **false**."]),
                ("Name the falsy values.", ["**0, \"\", null, undefined, NaN, false**."]),
                ("Are `{}` and `[]` falsy?", ["**No.** `!!{}` and `!![]` are **true**."]),
                ("What is `0 == false`?", ["**true**. `0 === false` is **false**."]),
                ("What is `\"\" == 0`?", ["**true**. `===` is **false**."]),
                ("What is `\"abc\" - 1`?", ["**NaN**."]),
            ],
            "Do not rely on + to add when a string might be present. Use === unless you truly want coercion. List the six falsy values; empty objects and arrays are not among them.",
            [
                ("JS Type Coercion (W3Schools)", "https://www.w3schools.com/js/js_type_coercion.asp"),
                ("MDN: Type coercion", "https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion"),
                ("MDN: Equality comparisons", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness"),
            ],
        ),
        (
            "js-type-conversion",
            "JS Type Conversion",
            CONVERSION,
            "Conversion is explicit: Number(), String(), Boolean(), unary +, parseInt, parseFloat, and toString / toFixed / toExponential / toPrecision. Number(\"3.14\") is 3.14; Number(\"\") and Number(\" \") are 0; Number(\"John\") and Number(\"99 88\") are NaN. parseInt/parseFloat can parse a prefix where Number cannot. Date-part getters return numbers you can toString; getMonth is 0–11 so add 1 for 1–12. The conversion table is one Example per original value. Surprises: Boolean(\"0\") is true, Number([]) is 0, Number(null) is 0, Number(undefined) is NaN, empty arrays are truthy.",
            [
                "**Number()** / **String()** / **Boolean()** are explicit. Unary **`+`** is a number cast.",
                '`Number("")` and `Number(" ")` are **0**. `Number("99 88")` is **NaN**. `parseFloat("99 88")` is **99**.',
                "Date **Number(d)** equals **getTime()**. Date() without new is already a **string of now**.",
                "Table rows (not collapsed): false, true, 0, 1, \"0\", \"000\", \"1\", NaN, ±Infinity, \"\", \"20\", \"twenty\", [], [20], [10,20], function, {}, null, undefined.",
                "Red surprises: **Boolean(\"0\") true**, **Number([]) 0**, **Boolean([]) true**, **Number(null) 0**.",
            ],
            [
                ("What is `Number(\"3.14\")`?", ["**3.14**."]),
                ("What is `Number(\"\")` and `Number(\" \")`?", ["Both **0**."]),
                ("What is `Number(\"99 88\")` vs `parseInt(\"99 88\")`?", ["**NaN** vs **99**."]),
                ("What is `+\"John\"`?", ["**NaN**, typeof **\"number\"**."]),
                ("What is `String(100 + 23)`?", ['**"123"**.']),
                ("What is `(123.456).toFixed(2)`?", ['**"123.46"**.']),
                ("What is `(123.456).toPrecision(4)`?", ['**"123.5"**.']),
                ("What is Number(false) / Number(true)?", ["**0** and **1**."]),
                ("What is `5 + null` vs `\"5\" + null`?", ["**5** vs **\"5null\"**."]),
                ("What is `Boolean(\"0\")`?", ["**true** — non-empty strings are truthy, even **\"0\"** and **\"000\"**."]),
                ("What is `Number([])` and `Boolean([])`?", ["**0** and **true**."]),
                ("What is `Number(null)` vs `Number(undefined)`?", ["**0** vs **NaN**. Both are falsy as Boolean."]),
                ("What is `Number([10,20])`?", ["**NaN**. String is **\"10,20\"**. Boolean **true**."]),
                ("What is getMonth()+1 on the fixed March date?", ["**3**, string **\"3\"**. getMonth itself is **2**."]),
                ("Is getMinutes 0–23 as the page table says?", ["**No.** Real range is **0–59**. This instant is **30**."]),
            ],
            "Prefer explicit Number/String/Boolean. Remember empty strings become 0, whitespace strings become 0, and Boolean of a non-empty string is true even if that string looks like 0. The table rows are the checklist for surprises.",
            [
                ("JS Type Conversion (W3Schools)", "https://www.w3schools.com/js/js_type_conversion.asp"),
                ("MDN: Number", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number"),
                ("MDN: parseInt", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt"),
                ("MDN: Boolean", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean"),
            ],
        ),
        (
            "js-destructuring",
            "JS Destructuring",
            DESTRUCTURING,
            "Destructuring unpacks objects and iterables into bindings without changing the source. Object patterns match by name (order does not matter) and can set defaults or rename with {lastName: name}. Array patterns match by position; extra commas skip holes; ...rest gathers the tail; {[0]: x} picks an index by name. Nested patterns unpack inner objects and arrays. Map loops yield [key, value] pairs. [a, b] = [b, a] swaps. Strings destructure into characters because they are iterable.",
            [
                "Objects: `{firstName, lastName}`, defaults `{country = \"US\"}`, alias `{lastName: name}`, rest `{firstName, ...rest}`.",
                "Arrays: `[a, b]`, skip `[a, , , b]`, index `{[0]: a}`, rest `[a, b, ...rest]`, defaults `[a = \"A\", b = \"B\"]`.",
                "**Nested:** `{ address: { city } }` and `[a, [b, c], d]`.",
                "**Swap:** `[firstName, lastName] = [lastName, firstName]` → **Doe / John**.",
                "Not destructive: changing the binding does **not** change the source object.",
            ],
            [
                ("Does property order matter in object destructuring?", ["**No.** `{lastName, firstName}` still gets John and Doe."]),
                ("What is `country` when it is missing and defaulted to `\"US\"`?", ['**"US"**.']),
                ("What is `{lastName: name}`?", ['A variable **name** holding **"Doe"**.']),
                ("What are a1–a5 of `\"W3Schools\"`?", ['**W, 3, S, c, h**.']),
                ("What is `[fruit1, fruit2]` of the fruits array?", ['**"Bananas"**, **"Oranges"**.']),
                ("What is `[fruit1,,,fruit2]`?", ['**"Bananas"** and **"Mangos"** (two skipped).']),
                ("What is `[a, b, ...rest]` of 10..70?", ["a **10**, b **20**, rest **30,40,50,60,70**."]),
                ("What is object rest after taking firstName?", ['**{"lastName":"Doe","age":50}**.']),
                ("What does nested `{ address: { city, zip } }` bind?", ['city **"Oslo"**, zip **"0001"**. Not `address` unless named.']),
                ("What is the Map loop text?", ['**"apples is 500bananas is 300oranges is 200"** — no extra separators.']),
                ("How do you swap firstName and lastName?", ["`[firstName, lastName] = [lastName, firstName]` → **Doe**, **John**."]),
                ("Does destructuring mutate the object?", ["**No.** Assigning the binding leaves **person.firstName** **\"John\"**."]),
                ("What is array default `b` when only one element is provided?", ['The default **"B"**.']),
            ],
            "Match objects by name and arrays by position. Use defaults, aliases, rest, skips, and nesting as separate patterns. Swapping with a destructuring assignment is the temp-free idiom. The source value is not mutated.",
            [
                ("JS Destructuring (W3Schools)", "https://www.w3schools.com/js/js_destructuring.asp"),
                ("MDN: Destructuring assignment", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring"),
            ],
        ),
    ]

    print("example counts:")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print(f"  {slug}: {len(recs)}  qa={len(qa)}")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        if not (8 <= len(qa) <= 15):
            raise SystemExit(f"QA count {len(qa)} out of 8-15 for {slug}")
        print("building", slug, "examples", len(recs))
        build_and_snap(slug, title, recs, intro, concepts, qa, summary, refs)
        print("done", slug)


if __name__ == "__main__":
    run_all()
