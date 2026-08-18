"""S6 rest: Number Methods, Properties, Reference, Bitwise, BigInt."""
from __future__ import annotations

from _gen_lib import S, build_and_snap, display_script

# ---------------------------------------------------------------------------
# 6.2 JS Number Methods
# ---------------------------------------------------------------------------

METHODS = [
    S(
        "tostring",
        "`toString()`",
        [
            "**`toString()`** returns a number as a **string**.",
            "It works on **literals**, **variables**, and **expressions**. A literal needs parentheses: `(123).toString()`.",
        ],
        "let x = 123;\nx.toString();\n(123).toString();\n(100 + 23).toString();",
        [
            ("x.toString()", "x.toString()"),
            ("(123).toString()", "(123).toString()"),
            ("(100 + 23).toString()", "(100 + 23).toString()"),
            ("typeof x.toString()", "typeof x.toString()"),
        ],
        'All three return **"123"** (a string).',
    ),
    S(
        "tostring-radix",
        "`toString(2)` radix",
        [
            "An optional **radix** converts the number to that base.",
            "`123.toString(2)` is the **binary** representation of 123.",
        ],
        "let x = 123;\nlet text = x.toString(2);",
        [("text", "x.toString(2)")],
        'text is **"1111011"** (123 in binary).',
    ),
    S(
        "toexponential",
        "`toExponential()`",
        [
            "**`toExponential(n)`** returns a string in **exponential notation**, rounded to **n** digits after the decimal.",
            "The parameter is **optional**. Omit it and JavaScript does **not** round the same way.",
        ],
        "let x = 9.656;\nx.toExponential(2);\nx.toExponential(4);\nx.toExponential(6);",
        [
            ("toExponential()", "x.toExponential()"),
            ("toExponential(2)", "x.toExponential(2)"),
            ("toExponential(4)", "x.toExponential(4)"),
            ("toExponential(6)", "x.toExponential(6)"),
        ],
        "With 2, 4, and 6 digits you get **9.66e+0**, **9.6560e+0**, **9.656000e+0**.",
    ),
    S(
        "tofixed",
        "`toFixed()`",
        [
            "**`toFixed(n)`** returns a string with **n** digits after the decimal (rounded).",
            "**`toFixed(2)`** is the usual choice for **money**.",
        ],
        "let x = 9.656;\nx.toFixed(0);\nx.toFixed(2);\nx.toFixed(4);\nx.toFixed(6);",
        [
            ("toFixed(0)", "x.toFixed(0)"),
            ("toFixed(2)", "x.toFixed(2)"),
            ("toFixed(4)", "x.toFixed(4)"),
            ("toFixed(6)", "x.toFixed(6)"),
        ],
        "Results: **10**, **9.66**, **9.6560**, **9.656000** (all strings).",
    ),
    S(
        "toprecision",
        "`toPrecision()`",
        [
            "**`toPrecision(n)`** returns a string with **n significant digits** (total length), not “digits after the point”.",
            "With no argument it returns the same as a normal string conversion.",
        ],
        "let x = 9.656;\nx.toPrecision();\nx.toPrecision(2);\nx.toPrecision(4);\nx.toPrecision(6);",
        [
            ("toPrecision()", "x.toPrecision()"),
            ("toPrecision(2)", "x.toPrecision(2)"),
            ("toPrecision(4)", "x.toPrecision(4)"),
            ("toPrecision(6)", "x.toPrecision(6)"),
        ],
        "Results: **9.656**, **9.7**, **9.656**, **9.65600**.",
    ),
    S(
        "valueof",
        "`valueOf()`",
        [
            "**`valueOf()`** returns a number as a **number** (the primitive).",
            "JavaScript calls it **internally** to unwrap Number objects. There is **no reason** to call it in your code.",
            "Every data type has `valueOf()` and `toString()`.",
        ],
        "let x = 123;\nx.valueOf();\n(123).valueOf();\n(100 + 23).valueOf();",
        [
            ("x.valueOf()", "x.valueOf()"),
            ("typeof x.valueOf()", "typeof x.valueOf()"),
        ],
        "All three expressions are the primitive **123**.",
    ),
    S(
        "number-convert",
        "`Number()` conversions",
        [
            "**`Number()`**, **`parseFloat()`**, and **`parseInt()`** are **global** methods (not `x.Number()`).",
            "`Number` converts the **whole** value. Spaces around a number are OK. Commas, extra text, or two numbers → **NaN**.",
            "`true` → **1**, `false` → **0**.",
        ],
        """Number(true);
Number(false);
Number("10");
Number("  10");
Number("10  ");
Number(" 10  ");
Number("10.33");
Number("10,33");
Number("10 33");
Number("John");""",
        [
            ("Number(true)", "Number(true)"),
            ("Number(false)", "Number(false)"),
            ('Number("10")', 'Number("10")'),
            ('Number("  10")', 'Number("  10")'),
            ('Number("10  ")', 'Number("10  ")'),
            ('Number(" 10  ")', 'Number(" 10  ")'),
            ('Number("10.33")', 'Number("10.33")'),
            ('Number("10,33")', 'Number("10,33")'),
            ('Number("10 33")', 'Number("10 33")'),
            ('Number("John")', 'Number("John")'),
        ],
        "**1**, **0**, **10**, **10**, **10**, **10**, **10.33**, then **NaN** for comma, space-inside, and John.",
    ),
    S(
        "number-date-epoch",
        '`Number(new Date("1970-01-01"))`',
        [
            "`Number(date)` is milliseconds since **1 Jan 1970 UTC** (Unix epoch).",
            "The date-only ISO string is treated as **UTC midnight**, so this is **0**.",
        ],
        'Number(new Date("1970-01-01"));',
        [("ms", 'Number(new Date("1970-01-01"))')],
        "**0** — the epoch itself.",
    ),
    S(
        "number-date-next-day",
        '`Number(new Date("1970-01-02"))`',
        [
            "One day is **86400000** milliseconds (24 × 60 × 60 × 1000).",
        ],
        'Number(new Date("1970-01-02"));',
        [("ms", 'Number(new Date("1970-01-02"))')],
        "**86400000**.",
    ),
    S(
        "number-date-2017",
        '`Number(new Date("2017-09-30"))`',
        [
            "Any date converts to its epoch milliseconds.",
            "This is useful for **comparing** or **sorting** dates as numbers.",
        ],
        'Number(new Date("2017-09-30"));',
        [("ms", 'Number(new Date("2017-09-30"))')],
        "**1506729600000** (UTC midnight on that day).",
    ),
    S(
        "parseint",
        "`parseInt()`",
        [
            "**`parseInt()`** reads a string and returns a **whole number**.",
            "Spaces are allowed. Only the **first number** is used. A trailing decimal is **truncated**, not rounded.",
            '`"years 10"` starts with letters → **NaN**.',
        ],
        """parseInt("-10");
parseInt("-10.33");
parseInt("10");
parseInt("10.33");
parseInt("10 20 30");
parseInt("10 years");
parseInt("years 10");""",
        [
            ('parseInt("-10")', 'parseInt("-10")'),
            ('parseInt("-10.33")', 'parseInt("-10.33")'),
            ('parseInt("10")', 'parseInt("10")'),
            ('parseInt("10.33")', 'parseInt("10.33")'),
            ('parseInt("10 20 30")', 'parseInt("10 20 30")'),
            ('parseInt("10 years")', 'parseInt("10 years")'),
            ('parseInt("years 10")', 'parseInt("years 10")'),
        ],
        "**-10**, **-10**, **10**, **10**, **10**, **10**, **NaN**.",
    ),
    S(
        "parsefloat",
        "`parseFloat()`",
        [
            "**`parseFloat()`** keeps the **decimal** part.",
            "Same “first number / leading junk → NaN” rules as `parseInt`.",
        ],
        """parseFloat("10");
parseFloat("10.33");
parseFloat("10 20 30");
parseFloat("10 years");
parseFloat("years 10");""",
        [
            ('parseFloat("10")', 'parseFloat("10")'),
            ('parseFloat("10.33")', 'parseFloat("10.33")'),
            ('parseFloat("10 20 30")', 'parseFloat("10 20 30")'),
            ('parseFloat("10 years")', 'parseFloat("10 years")'),
            ('parseFloat("years 10")', 'parseFloat("years 10")'),
        ],
        "**10**, **10.33**, **10**, **10**, **NaN**.",
    ),
    S(
        "isinteger",
        "`Number.isInteger()`",
        [
            "Static methods live on **`Number`**, not on a value. Call **`Number.isInteger(x)`**, never `x.isInteger()`.",
            "Returns **true** only for an integer (no fractional part).",
        ],
        "Number.isInteger(10);\nNumber.isInteger(10.5);",
        [
            ("Number.isInteger(10)", "Number.isInteger(10)"),
            ("Number.isInteger(10.5)", "Number.isInteger(10.5)"),
        ],
        "**true** for 10; **false** for 10.5.",
    ),
    S(
        "isfinite",
        "`Number.isFinite()`",
        [
            "**`Number.isFinite(x)`** is **true** when x is a finite number — not **Infinity**, **−Infinity**, or **NaN**.",
            "Unlike global `isFinite`, it does **not** coerce strings: `Number.isFinite(\"123\")` is **false**.",
        ],
        "Number.isFinite(123);",
        [
            ("Number.isFinite(123)", "Number.isFinite(123)"),
            ("Number.isFinite(Infinity)", "Number.isFinite(Infinity)"),
            ("Number.isFinite(NaN)", "Number.isFinite(NaN)"),
        ],
        "**true** for 123; **false** for Infinity and NaN.",
    ),
    S(
        "isnan",
        "`Number.isNaN()`",
        [
            "**`Number.isNaN(x)`** is **true** only if x is **NaN**.",
            "You **cannot** test NaN with `==` or `===` (`NaN === NaN` is false). Prefer `Number.isNaN`.",
            "Unlike global `isNaN`, it does **not** coerce: `Number.isNaN(\"NaN\")` is **false**.",
        ],
        "Number.isNaN(123);",
        [
            ("Number.isNaN(123)", "Number.isNaN(123)"),
            ("Number.isNaN(NaN)", "Number.isNaN(NaN)"),
            ("NaN === NaN", "NaN === NaN"),
        ],
        "**false** for 123; **true** for NaN. `NaN === NaN` is **false**.",
    ),
    S(
        "issafeinteger",
        "`Number.isSafeInteger()`",
        [
            "A **safe integer** is exactly representable as a double: from **−(2⁵³−1)** to **+(2⁵³−1)**.",
            "**9007199254740991** is safe. **9007199254740992** is not.",
            "A huge literal like `12345678901234567890` is **not** a safe integer (it already rounded as a Number).",
        ],
        "Number.isSafeInteger(10);\nNumber.isSafeInteger(12345678901234567890);",
        [
            ("Number.isSafeInteger(10)", "Number.isSafeInteger(10)"),
            ("Number.isSafeInteger(12345678901234567890)", "Number.isSafeInteger(12345678901234567890)"),
            ("Number.isSafeInteger(9007199254740991)", "Number.isSafeInteger(9007199254740991)"),
            ("Number.isSafeInteger(9007199254740992)", "Number.isSafeInteger(9007199254740992)"),
        ],
        "**true** for 10 and 2⁵³−1; **false** for the 20-digit literal and 2⁵³.",
    ),
    S(
        "number-parsefloat",
        "`Number.parseFloat()`",
        [
            "**`Number.parseFloat`** is the same function as global **`parseFloat`**.",
            "It exists so code can avoid globals (modules / non-browser JS).",
        ],
        """Number.parseFloat("10");
Number.parseFloat("10.33");
Number.parseFloat("10 20 30");
Number.parseFloat("10 years");
Number.parseFloat("years 10");""",
        [
            ('Number.parseFloat("10")', 'Number.parseFloat("10")'),
            ('Number.parseFloat("10.33")', 'Number.parseFloat("10.33")'),
            ('Number.parseFloat("10 20 30")', 'Number.parseFloat("10 20 30")'),
            ('Number.parseFloat("10 years")', 'Number.parseFloat("10 years")'),
            ('Number.parseFloat("years 10")', 'Number.parseFloat("years 10")'),
        ],
        "**10**, **10.33**, **10**, **10**, **NaN** — same as `parseFloat`.",
    ),
    S(
        "number-parseint",
        "`Number.parseInt()`",
        [
            "**`Number.parseInt`** is the same function as global **`parseInt`**.",
        ],
        """Number.parseInt("-10");
Number.parseInt("-10.33");
Number.parseInt("10");
Number.parseInt("10.33");
Number.parseInt("10 20 30");
Number.parseInt("10 years");
Number.parseInt("years 10");""",
        [
            ('Number.parseInt("-10")', 'Number.parseInt("-10")'),
            ('Number.parseInt("-10.33")', 'Number.parseInt("-10.33")'),
            ('Number.parseInt("10")', 'Number.parseInt("10")'),
            ('Number.parseInt("10.33")', 'Number.parseInt("10.33")'),
            ('Number.parseInt("10 20 30")', 'Number.parseInt("10 20 30")'),
            ('Number.parseInt("10 years")', 'Number.parseInt("10 years")'),
            ('Number.parseInt("years 10")', 'Number.parseInt("years 10")'),
        ],
        "Same results as `parseInt`: **-10**, **-10**, **10**, **10**, **10**, **10**, **NaN**.",
    ),
    S(
        "static-not-on-value",
        "Static methods are not on variables",
        [
            "`Number.isInteger` belongs to the **Number object**.",
            "Calling **`x.isInteger()`** on a number variable throws **TypeError: x.isInteger is not a function**.",
            "The page repeats `isInteger` / `isSafeInteger` at the bottom; those Tryits are the same as Examples 13 and 16.",
        ],
        "let x = 10;\nx.isInteger();  // TypeError",
        outcome="The sandbox catches the error: **TypeError** — use `Number.isInteger(x)` instead.",
        script="""      let x = 10;
      let msg;
      try {
        x.isInteger();
        msg = "no error";
      } catch (e) {
        msg = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText = msg;""",
    ),
]


# ---------------------------------------------------------------------------
# 6.3 JS Number Properties
# ---------------------------------------------------------------------------

PROPS = [
    S(
        "epsilon",
        "`Number.EPSILON`",
        [
            "**`Number.EPSILON`** is the difference between **1** and the next representable number above 1 (~ **2.22e-16**).",
            "ES6. Use it as a **tolerance** when comparing floats.",
        ],
        "let x = Number.EPSILON;",
        [("x", "x")],
        "x is **2.220446049250313e-16**.",
    ),
    S(
        "max-value",
        "`Number.MAX_VALUE`",
        [
            "**`Number.MAX_VALUE`** is the **largest finite** number (~ **1.8e+308**).",
            "Bigger results overflow to **Infinity**.",
        ],
        "let x = Number.MAX_VALUE;",
        [("x", "x")],
        "x is **1.7976931348623157e+308**.",
    ),
    S(
        "prop-on-variable",
        "Properties are not on variables",
        [
            "Number properties live on **`Number`**, not on a value.",
            "`x.MAX_VALUE` where x is **6** is **`undefined`** — it does not throw, it just is not there.",
        ],
        "let x = 6;\nx.MAX_VALUE;",
        [("x.MAX_VALUE", "x.MAX_VALUE")],
        "**undefined** — write `Number.MAX_VALUE` instead.",
    ),
    S(
        "min-value",
        "`Number.MIN_VALUE`",
        [
            "**`Number.MIN_VALUE`** is the **smallest positive** number (closest to 0), ~ **5e-324**.",
            "It is **not** the most-negative number (that is `-Number.MAX_VALUE`).",
        ],
        "let x = Number.MIN_VALUE;",
        [("x", "x")],
        "x is **5e-324**.",
    ),
    S(
        "min-safe",
        "`Number.MIN_SAFE_INTEGER`",
        [
            "**`Number.MIN_SAFE_INTEGER`** is **−(2⁵³−1)** = **-9007199254740991**.",
            "ES6 pair with `MAX_SAFE_INTEGER`.",
        ],
        "let x = Number.MIN_SAFE_INTEGER;",
        [("x", "x")],
        "x is **-9007199254740991**.",
    ),
    S(
        "max-safe",
        "`Number.MAX_SAFE_INTEGER`",
        [
            "**`Number.MAX_SAFE_INTEGER`** is **2⁵³−1** = **9007199254740991**.",
        ],
        "let x = Number.MAX_SAFE_INTEGER;",
        [("x", "x")],
        "x is **9007199254740991**.",
    ),
    S(
        "pos-inf",
        "`Number.POSITIVE_INFINITY`",
        [
            "The constant for **Infinity**.",
        ],
        "let x = Number.POSITIVE_INFINITY;",
        [("x", "x"), ("x === Infinity", "x === Infinity")],
        "x is **Infinity**.",
    ),
    S(
        "pos-inf-overflow",
        "POSITIVE_INFINITY on overflow",
        [
            "`1 / 0` returns **Infinity**, the same value as `Number.POSITIVE_INFINITY`.",
        ],
        "let x = 1 / 0;",
        [("x", "x")],
        "x is **Infinity**.",
    ),
    S(
        "neg-inf",
        "`Number.NEGATIVE_INFINITY`",
        [
            "The constant for **−Infinity**.",
        ],
        "let x = Number.NEGATIVE_INFINITY;",
        [("x", "x")],
        "x is **-Infinity**.",
    ),
    S(
        "neg-inf-overflow",
        "NEGATIVE_INFINITY on overflow",
        [
            "`-1 / 0` returns **−Infinity**.",
        ],
        "let x = -1 / 0;",
        [("x", "x")],
        "x is **-Infinity**.",
    ),
    S(
        "number-nan",
        "`Number.NaN`",
        [
            "**`Number.NaN`** is the same value as the global **`NaN`**.",
        ],
        "let x = Number.NaN;",
        [("x", "x"), ("Number.isNaN(x)", "Number.isNaN(x)")],
        "x is **NaN**.",
    ),
    S(
        "nan-from-math",
        'NaN from 100 / "Apple"',
        [
            "Illegal arithmetic produces **NaN** — the same reserved value.",
        ],
        'let x = 100 / "Apple";',
        [("x", "x")],
        "x is **NaN**.",
    ),
]


# ---------------------------------------------------------------------------
# 6.4 JS Number Reference
# ---------------------------------------------------------------------------

def ref_row(stem, title, bullets, code, displays, outcome):
    return S(stem, title, bullets, code, displays, outcome)


REF = [
    ref_row(
        "constructor",
        "`constructor`",
        [
            "**`constructor`** is the function that created the prototype — for a number that is **`Number`**.",
            "Rarely useful in day-to-day code.",
        ],
        "let x = 123;\nx.constructor;",
        [("x.constructor === Number", "x.constructor === Number"), ("x.constructor.name", "x.constructor.name")],
        "`x.constructor` is the **Number** function.",
    ),
    ref_row(
        "epsilon",
        "`EPSILON`",
        [
            "Difference between 1 and the next number above 1.",
        ],
        "Number.EPSILON;",
        [("Number.EPSILON", "Number.EPSILON")],
        "**2.220446049250313e-16**.",
    ),
    ref_row(
        "isfinite",
        "`isFinite()`",
        [
            "Static: **`Number.isFinite(value)`** — true for finite numbers only.",
        ],
        "Number.isFinite(123);\nNumber.isFinite(Infinity);",
        [("Number.isFinite(123)", "Number.isFinite(123)"), ("Number.isFinite(Infinity)", "Number.isFinite(Infinity)")],
        "**true**, **false**.",
    ),
    ref_row(
        "isinteger",
        "`isInteger()`",
        [
            "Static: **`Number.isInteger(value)`**.",
        ],
        "Number.isInteger(10);\nNumber.isInteger(10.5);",
        [("Number.isInteger(10)", "Number.isInteger(10)"), ("Number.isInteger(10.5)", "Number.isInteger(10.5)")],
        "**true**, **false**.",
    ),
    ref_row(
        "isnan",
        "`isNaN()`",
        [
            "Static: **`Number.isNaN(value)`** — true only for NaN.",
        ],
        "Number.isNaN(123);\nNumber.isNaN(NaN);",
        [("Number.isNaN(123)", "Number.isNaN(123)"), ("Number.isNaN(NaN)", "Number.isNaN(NaN)")],
        "**false**, **true**.",
    ),
    ref_row(
        "issafeinteger",
        "`isSafeInteger()`",
        [
            "Static: integer in **[−(2⁵³−1), 2⁵³−1]**.",
        ],
        "Number.isSafeInteger(10);\nNumber.isSafeInteger(9007199254740992);",
        [
            ("Number.isSafeInteger(10)", "Number.isSafeInteger(10)"),
            ("Number.isSafeInteger(9007199254740992)", "Number.isSafeInteger(9007199254740992)"),
        ],
        "**true**, **false**.",
    ),
    ref_row(
        "max-safe",
        "`MAX_SAFE_INTEGER`",
        ["Maximum safe integer: **2⁵³−1**."],
        "Number.MAX_SAFE_INTEGER;",
        [("Number.MAX_SAFE_INTEGER", "Number.MAX_SAFE_INTEGER")],
        "**9007199254740991**.",
    ),
    ref_row(
        "min-safe",
        "`MIN_SAFE_INTEGER`",
        ["Minimum safe integer: **−(2⁵³−1)**."],
        "Number.MIN_SAFE_INTEGER;",
        [("Number.MIN_SAFE_INTEGER", "Number.MIN_SAFE_INTEGER")],
        "**-9007199254740991**.",
    ),
    ref_row(
        "max-value",
        "`MAX_VALUE`",
        ["Largest finite number."],
        "Number.MAX_VALUE;",
        [("Number.MAX_VALUE", "Number.MAX_VALUE")],
        "**1.7976931348623157e+308**.",
    ),
    ref_row(
        "min-value",
        "`MIN_VALUE`",
        ["Smallest **positive** number (closest to zero)."],
        "Number.MIN_VALUE;",
        [("Number.MIN_VALUE", "Number.MIN_VALUE")],
        "**5e-324**.",
    ),
    ref_row(
        "nan",
        "`NaN`",
        ['Represents **"Not-a-Number"**.'],
        "Number.NaN;",
        [("Number.isNaN(Number.NaN)", "Number.isNaN(Number.NaN)")],
        "**NaN**.",
    ),
    ref_row(
        "neg-inf",
        "`NEGATIVE_INFINITY`",
        ["Negative infinity (overflow)."],
        "Number.NEGATIVE_INFINITY;",
        [("Number.NEGATIVE_INFINITY", "Number.NEGATIVE_INFINITY")],
        "**-Infinity**.",
    ),
    ref_row(
        "pos-inf",
        "`POSITIVE_INFINITY`",
        ["Infinity (overflow)."],
        "Number.POSITIVE_INFINITY;",
        [("Number.POSITIVE_INFINITY", "Number.POSITIVE_INFINITY")],
        "**Infinity**.",
    ),
    ref_row(
        "parsefloat",
        "`parseFloat()`",
        ["Parses a string and returns a number. Same as global `parseFloat`."],
        'Number.parseFloat("10.33 years");',
        [("result", 'Number.parseFloat("10.33 years")')],
        "**10.33**.",
    ),
    ref_row(
        "parseint",
        "`parseInt()`",
        ["Parses a string and returns a whole number. Same as global `parseInt`."],
        'Number.parseInt("10.33 years");',
        [("result", 'Number.parseInt("10.33 years")')],
        "**10**.",
    ),
    ref_row(
        "prototype",
        "`prototype`",
        [
            "**`Number.prototype`** is where instance methods live (`toFixed`, `toString`, …).",
            "You **can** add methods, but **do not** extend built-in prototypes in library code — it surprises everyone else.",
        ],
        "Number.prototype.twice = function () { return this * 2; };\n(21).twice();",
        [(" (21).twice() ", "(21).twice()")],
        "**42** — a demo only; prefer a plain function instead of changing `Number.prototype`.",
    ),
    ref_row(
        "toexponential",
        "`toExponential(x)`",
        ["Exponential notation with x digits after the decimal."],
        "(9.656).toExponential(2);",
        [("result", "(9.656).toExponential(2)")],
        '**"9.66e+0"**.',
    ),
    ref_row(
        "tofixed",
        "`toFixed(x)`",
        ["x digits after the decimal. Good for money."],
        "(9.656).toFixed(2);",
        [("result", "(9.656).toFixed(2)")],
        '**"9.66"**.',
    ),
    ref_row(
        "tolocalestring",
        "`toLocaleString()`",
        [
            "Converts a number to a string using **locale** grouping/decimals.",
            "Optional locale like `\"de-DE\"` uses a **comma** as the decimal mark.",
        ],
        "let n = 123456.789;\nn.toLocaleString();\nn.toLocaleString('de-DE');",
        [
            ("default", "n.toLocaleString()"),
            ("de-DE", "n.toLocaleString('de-DE')"),
        ],
        "Default (en) looks like **123,456.789**; German looks like **123.456,789**.",
    ),
    ref_row(
        "toprecision",
        "`toPrecision(x)`",
        ["Format to x **significant** digits."],
        "(9.656).toPrecision(2);",
        [("result", "(9.656).toPrecision(2)")],
        '**"9.7"**.',
    ),
    ref_row(
        "tostring",
        "`toString()`",
        ["Convert to a string; optional radix 2–36."],
        "(255).toString();\n(255).toString(16);",
        [("toString()", "(255).toString()"), ("toString(16)", "(255).toString(16)")],
        '**"255"** and **"ff"**.',
    ),
    ref_row(
        "valueof",
        "`valueOf()`",
        ["Primitive value of a Number object. Used internally."],
        "let x = new Number(123);\nx.valueOf();",
        [("valueOf", "x.valueOf()"), ("typeof", "typeof x.valueOf()")],
        "Primitive **123** (`typeof` **number**).",
    ),
]


# ---------------------------------------------------------------------------
# 6.5 JS Bitwise
# ---------------------------------------------------------------------------

BITWISE = [
    S(
        "and",
        "Bitwise AND `&`",
        [
            "JavaScript bitwise ops convert to **32-bit signed integers**, then convert the result back to a Number.",
            "**AND** sets a bit only if **both** bits are 1. Truth table: 1&1=1; anything with 0 is 0.",
            "`5 & 1` → `0101 & 0001` → **0001** = **1**.",
        ],
        "let x = 5 & 1;",
        [("x", "x"), ("(5).toString(2)", "(5).toString(2)"), ("(1).toString(2)", "(1).toString(2)")],
        "x is **1**.",
    ),
    S(
        "or",
        "Bitwise OR `|`",
        [
            "**OR** sets a bit if **either** bit is 1.",
            "`5 | 1` → `0101 | 0001` → **0101** = **5**.",
        ],
        "let x = 5 | 1;",
        [("x", "x")],
        "x is **5**.",
    ),
    S(
        "xor",
        "Bitwise XOR `^`",
        [
            "**XOR** sets a bit if the bits are **different**.",
            "`5 ^ 1` → `0101 ^ 0001` → **0100** = **4**.",
        ],
        "let x = 5 ^ 1;",
        [("x", "x")],
        "x is **4**.",
    ),
    S(
        "not",
        "Bitwise NOT `~`",
        [
            "4-bit unsigned tables say `~5` is 10. JavaScript uses **32-bit two’s complement**, so **`~5` is −6**, not 10.",
            "`~n` is equal to **`-(n + 1)`**.",
        ],
        "let x = ~5;",
        [("x", "x")],
        "x is **-6**.",
    ),
    S(
        "left-shift",
        "Zero-fill left shift `<<`",
        [
            "Pushes **zeros in from the right**; leftmost bits fall off.",
            "`5 << 1` doubles 5 → **10**.",
        ],
        "let x = 5 << 1;",
        [("x", "x")],
        "x is **10**.",
    ),
    S(
        "sign-right",
        "Sign-preserving right shift `>>`",
        [
            "Copies the **sign bit** in from the left (arithmetic shift).",
            "`-5 >> 1` is **-3** (not a zero-filled 2).",
        ],
        "let x = -5 >> 1;",
        [("x", "x")],
        "x is **-3**.",
    ),
    S(
        "zero-right",
        "Zero-fill right shift `>>>`",
        [
            "Pushes **zeros** in from the left (logical shift).",
            "`5 >>> 1` is **2**. On negatives this yields a **large positive** 32-bit value.",
        ],
        "let x = 5 >>> 1;",
        [("5 >>> 1", "5 >>> 1"), ("(-5 >>> 1)", "(-5 >>> 1)")],
        "`5 >>> 1` is **2**. `-5 >>> 1` is **2147483645** (extra clarifying row).",
    ),
    S(
        "assign-left",
        "Left shift assignment `<<=`",
        [
            "`x <<= y` means `x = x << y`.",
            "`-100 << 5` shifts −100 left by 5.",
        ],
        "let x = -100;\nx <<= 5;",
        [("x", "x")],
        "x is **-3200**.",
    ),
    S(
        "assign-right",
        "Signed right shift assignment `>>=`",
        [
            "`x >>= y` means `x = x >> y` (keeps the sign).",
        ],
        "let x = -100;\nx >>= 5;",
        [("x", "x")],
        "x is **-4** (sign preserved).",
    ),
    S(
        "assign-uright",
        "Unsigned right shift assignment `>>>=`",
        [
            "`x >>>= y` means `x = x >>> y` (zero fill).",
            "On a negative start value this becomes a **large positive** number.",
        ],
        "let x = -100;\nx >>>= 5;",
        [("x", "x")],
        "x is **134217724**.",
    ),
    S(
        "assign-and",
        "AND assignment `&=`",
        [
            "`x &= y` means `x = x & y`.",
            "`10 & 5` → `1010 & 0101` → **0**.",
        ],
        "let x = 10;\nx &= 5;",
        [("x", "x")],
        "x is **0**.",
    ),
    S(
        "assign-or",
        "OR assignment `|=`",
        [
            "`x |= y` means `x = x | y`.",
            "`10 | 5` → **15**.",
        ],
        "let x = 10;\nx |= 5;",
        [("x", "x")],
        "x is **15**.",
    ),
    S(
        "assign-xor",
        "XOR assignment `^=`",
        [
            "`x ^= y` means `x = x ^ y`.",
            "`10 ^ 5` → **15**.",
        ],
        "let x = 10;\nx ^= 5;",
        [("x", "x")],
        "x is **15**.",
    ),
    S(
        "dec2bin",
        "Decimal to binary",
        [
            "`(dec >>> 0).toString(2)` treats the value as **unsigned 32-bit**, then prints binary.",
            "`>>> 0` is a common trick to get an unsigned 32-bit view (important for negatives).",
        ],
        "function dec2bin(dec) {\n  return (dec >>> 0).toString(2);\n}",
        [("dec2bin(5)", "dec2bin(5)"), ("dec2bin(-5)", "dec2bin(-5)")],
        "`dec2bin(5)` is **101**. `dec2bin(-5)` is the 32-bit two’s complement string.",
    ),
    S(
        "bin2dec",
        "Binary to decimal",
        [
            "`parseInt(bin, 2)` parses a **binary string** as base 2.",
        ],
        "function bin2dec(bin) {\n  return parseInt(bin, 2).toString(10);\n}",
        [('bin2dec("101")', 'bin2dec("101")'), ('bin2dec("1111")', 'bin2dec("1111")')],
        '`"101"` → **5**; `"1111"` → **15**.',
    ),
]


# ---------------------------------------------------------------------------
# 6.6 JS BigInt
# ---------------------------------------------------------------------------

def catch_script(code: str, expr: str, label: str) -> str:
    return f"""{display_script(code, []).rsplit(chr(10), 1)[0]}
      let msg;
      try {{
        msg = {json_str(label)} + String({expr});
      }} catch (e) {{
        msg = e.name + ": " + e.message;
      }}
      document.getElementById("demo").innerText = msg;"""


def json_str(s: str) -> str:
    import json
    return json.dumps(s)


BIGINT = [
    S(
        "number-15-digits",
        "Number accuracy: 15 digits",
        [
            "Ordinary Numbers stay exact for **15 digits**.",
            "The 16th digit **rounds**.",
        ],
        "let x = 999999999999999;   // 15 digits\nlet y = 9999999999999999;  // 16 digits",
        [("x", "x"), ("y", "y")],
        "x is exact; y becomes **10000000000000000**.",
    ),
    S(
        "safe-range",
        "`MAX_SAFE_INTEGER` / `MIN_SAFE_INTEGER`",
        [
            "Safe integers are **±(2⁵³−1)** = **±9007199254740991**.",
        ],
        "let x = Number.MAX_SAFE_INTEGER;\nlet y = Number.MIN_SAFE_INTEGER;",
        [("x", "x"), ("y", "y")],
        "**9007199254740991** and **-9007199254740991**.",
    ),
    S(
        "lose-high",
        "Lose precision above MAX_SAFE_INTEGER",
        [
            "`MAX + 10` cannot be stored exactly as a Number.",
        ],
        "let x = 9007199254740991;\nlet y = x + 10;",
        [("x", "x"), ("y", "y")],
        "y is **9007199254741000** (rounded), not 9007199254741001.",
    ),
    S(
        "lose-low",
        "Lose precision below MIN_SAFE_INTEGER",
        [
            "The same rounding happens on the negative side.",
        ],
        "let x = -9007199254740991;\nlet y = x - 10;",
        [("x", "x"), ("y", "y")],
        "y is rounded, not exact min−10.",
    ),
    S(
        "create-n-and-ctor",
        "Create BigInt: `n` suffix and `BigInt()`",
        [
            "Two ways: an integer literal with **`n`**, or **`BigInt(\"...\")`** with a **string**.",
            "A string keeps every digit; a Number argument can already be rounded.",
        ],
        'let x = 999999999999999n;\nlet y = BigInt("999999999999999");',
        [("x", "x"), ("y", "y"), ("typeof x", "typeof x")],
        "Both are **999999999999999n**. `typeof` is **bigint**.",
    ),
    S(
        "create-20-digits",
        "20-digit BigInt",
        [
            "BigInt can hold integers **larger than 15 digits** with no rounding.",
        ],
        'let x = 12345678901234567890n;\nlet y = BigInt("12345678901234567890");',
        [("x", "x"), ("y", "y"), ("x === y", "x === y")],
        "Both store **12345678901234567890n** exactly; they compare equal.",
    ),
    S(
        "bigint-from-number",
        "`BigInt()` from a Number (warning)",
        [
            "You **can** pass a Number, but Numbers are only accurate to **15 digits**.",
            "`BigInt(9999999999999999)` converts the **already rounded** Number.",
        ],
        "let x = BigInt(9999999999999999);",
        [("x", "x")],
        "x is **10000000000000000n** — the rounding already happened before BigInt saw it. Prefer a **string** or **`n` literal**.",
    ),
    S(
        "typeof-bigint",
        "`typeof` is bigint",
        [
            "`typeof` a BigInt is **`\"bigint\"`**.",
            "That makes **8** primitive/object types in the language: string, number, bigint, boolean, undefined, null, symbol, object.",
        ],
        "let x = BigInt(999999999999999);\nlet type = typeof x;",
        [("type", "type")],
        'type is **"bigint"**.',
    ),
    S(
        "multiply",
        "BigInt arithmetic",
        [
            "BigInt supports `+ - * / % **` and `++ --`.",
            "**Division truncates** toward zero (no fractional BigInt).",
        ],
        "let x = 9007199254740995n;\nlet y = 9007199254740995n;\nlet z = x * y;",
        [("z", "z")],
        "z is the exact product **8114963775263029770004520090025n**.",
    ),
    S(
        "mix-error",
        "Cannot mix BigInt and Number",
        [
            "`10n + 5` throws **TypeError**. Convert **explicitly** first.",
            "This demo catches the error, then shows the fix: `Number(x) + y`.",
        ],
        "let x = 10n;\nlet y = 5;\n// let z = x + y;  // TypeError\nlet z = Number(x) + y;",
        outcome="Mixing throws **TypeError**. `Number(10n) + 5` is **15**.",
        script="""      let x = 10n;
      let y = 5;
      let mix;
      try { mix = x + y; } catch (e) { mix = e.name; }
      let z = Number(x) + y;
      document.getElementById("demo").innerText =
        "x + y -> " + mix + "\\n" +
        "Number(x) + y -> " + z;""",
    ),
    S(
        "convert",
        "BigInt ↔ Number conversion",
        [
            "`Number(bigint)` and `BigInt(number)` convert.",
            "A **huge** BigInt can become **Infinity** or a **rounded** Number.",
        ],
        'let largeNumber = BigInt("12345678901234567890");\nlet num = Number(largeNumber);',
        [("largeNumber", "largeNumber"), ("num", "num")],
        "The Number is **1.2345678901234568e+19** — precision is already lost.",
    ),
    S(
        "no-decimals",
        "No decimal BigInt; division",
        [
            "`1.5n` is a **SyntaxError**. BigInt is **integers only**.",
            "`5n / 2` is a TypeError (mixed types). `5n / 2n` is **2n** (truncated). `Number(5n) / 2` is **2.5**.",
        ],
        "let x = 5n;\nlet y = Number(x) / 2;",
        outcome="`Number(5n) / 2` is **2.5**. `5n / 2n` is **2n**. `1.5n` does not parse.",
        script="""      let x = 5n;
      let y = Number(x) / 2;
      let truncated = 5n / 2n;
      document.getElementById("demo").innerText =
        "Number(5n) / 2 -> " + y + "\\n" +
        "5n / 2n -> " + truncated;""",
    ),
    S(
        "compare",
        "Comparisons with Numbers",
        [
            "Relational operators **can** mix types: `10n > 5` is true.",
            "`===` is **false** across types. `==` is **true** if the values match.",
        ],
        "let x = (10n > 5n);\nlet y = (10n === 10);\nlet z = (10n == 10);",
        [("10n > 5n", "x"), ("10n === 10", "y"), ("10n == 10", "z")],
        "**true**, **false**, **true**.",
    ),
    S(
        "bitwise",
        "BigInt bitwise AND/OR/XOR/NOT",
        [
            "Bitwise ops need **both** sides BigInt.",
            "`5n` is `0101`; `3n` is `0011`.",
        ],
        "let a = 5n;\nlet b = 3n;\nlet x = (a & b);\nlet y = (a | b);\nlet z = (a ^ b);\nlet n = (~a);",
        [("a & b", "x"), ("a | b", "y"), ("a ^ b", "z"), ("~a", "n")],
        "**1n**, **7n**, **6n**, **-6n**.",
    ),
    S(
        "shift",
        "BigInt shifts `<<` `>>`",
        [
            "Only **`<<`** and **`>>`**. Both operands must be BigInt; shift counts must be **non-negative**.",
            "**`>>>` is not allowed** on BigInt (throws TypeError).",
        ],
        "let big = 10n;\nlet x = (big << 2n);\nlet y = (big >> 1n);",
        outcome="`10n << 2n` is **40n**; `10n >> 1n` is **5n**. `>>>` throws **TypeError**.",
        script="""      let big = 10n;
      let x = (big << 2n);
      let y = (big >> 1n);
      let usr;
      try { usr = big >>> 1n; } catch (e) { usr = e.name; }
      document.getElementById("demo").innerText =
        "10n << 2n -> " + x + "\\n" +
        "10n >> 1n -> " + y + "\\n" +
        "10n >>> 1n -> " + usr;""",
    ),
    S(
        "bases",
        "Hex, octal, binary BigInt literals",
        [
            "`256n`, `0o400n`, `0x100n`, `0b100000000n` are the **same** value.",
        ],
        "let num = 256n;\nlet oct = 0o400n;\nlet hex = 0x100n;\nlet bin = 0b100000000n;",
        [("num", "num"), ("oct", "oct"), ("hex", "hex"), ("bin", "bin"), ("all equal", "num === oct && oct === hex && hex === bin")],
        "All four are **256n**.",
    ),
    S(
        "bases-huge",
        "Huge hex / octal / binary BigInts",
        [
            "The same prefixes work for integers far beyond Number range.",
        ],
        "let hex = 0x20000000000003n;\nlet oct = 0o400000000000000003n;\nlet bin = 0b100000000000000000000000000000000000000000000000000011n;",
        [("hex", "hex"), ("oct", "oct"), ("bin", "bin")],
        "Each prints as a large **…n** integer — no rounding.",
    ),
    S(
        "unsafe-eq-number",
        "MAX+1 === MAX+2 is true for Number",
        [
            "Rounding can make **different** integers compare equal as Numbers.",
            "`9007199254740992 === 9007199254740993` is **true** — a security/logic hazard.",
        ],
        "9007199254740992 === 9007199254740993;",
        [("equal", "9007199254740992 === 9007199254740993")],
        "**true** — both round to the same Number.",
    ),
    S(
        "unsafe-eq-bigint",
        "The same values as BigInt are distinct",
        [
            "BigInt keeps every digit, so those two values are **not** equal.",
        ],
        "9007199254740992n === 9007199254740993n;",
        [("equal", "9007199254740992n === 9007199254740993n")],
        "**false**.",
    ),
    S(
        "json-math-limits",
        "JSON and Math do not accept BigInt",
        [
            "**`Math.sqrt`** (and other Math functions) do **not** take BigInt.",
            "**`JSON.stringify(1n)`** throws **TypeError**.",
        ],
        "JSON.stringify(1n);\nMath.sqrt(16n);",
        outcome="Both throw **TypeError**. Convert with `Number(...)` only when the value fits.",
        script="""      let j, m;
      try { j = JSON.stringify(1n); } catch (e) { j = e.name + ": " + e.message; }
      try { m = Math.sqrt(16n); } catch (e) { m = e.name + ": " + e.message; }
      document.getElementById("demo").innerText =
        "JSON.stringify(1n) -> " + j + "\\n" +
        "Math.sqrt(16n) -> " + m;""",
    ),
]


def run_all() -> None:
    sections = [
        (
            "js-number-methods",
            "JS Number Methods",
            METHODS,
            "Instance methods (`toString`, `toFixed`, …) work on **any number**. Static methods (`Number.isInteger`, …) are called on **`Number`**, not on a variable. Global `Number()` / `parseInt` / `parseFloat` convert values. The page repeats `isInteger` and `isSafeInteger` at the bottom; those duplicates are covered once here, plus a TypeError demo for calling a static method on a value.",
            [
                "**Instance vs static** — `x.toFixed(2)` vs `Number.isInteger(x)`.",
                "**`toFixed(2)`** for money; **`toPrecision`** for significant digits; **`toExponential`** for scientific notation.",
                "**`Number.isNaN`** is the right NaN test (`NaN === NaN` is false).",
            ],
            [
                ("What does `(123).toString()` return?", ['The string **"123"**. Parentheses are required on a literal.']),
                ("What is `(9.656).toFixed(2)`?", ['**"9.66"** — a string, rounded, two decimal places. Use it for money.']),
                ("How does `toPrecision(2)` differ from `toFixed(2)`?", ["`toPrecision` counts **significant digits** (9.656 → **9.7**).", "`toFixed` counts **digits after the decimal**."]),
                ("What is `Number(true)` and `Number(\"10,33\")`?", ["**1** and **NaN**. Commas are not part of a JS number."]),
                ('What is `Number(new Date("1970-01-01"))`?', ["**0** — milliseconds at the Unix epoch (UTC)."]),
                ('What is `parseInt("10.33")` vs `parseFloat("10.33")`?', ["**10** (truncated) vs **10.33**."]),
                ('What is `parseInt("years 10")`?', ["**NaN** — the string must **start** with a number (optional sign/spaces)."]),
                ("Why not write `x.isInteger()`?", ["**TypeError** — call **`Number.isInteger(x)`**."]),
                ("What is a safe integer?", ["An integer from **−(2⁵³−1)** to **2⁵³−1**.", "`Number.isSafeInteger(9007199254740992)` is **false**."]),
                ("Are `Number.parseInt` and `parseInt` different?", ["**No.** Same function; the Number form avoids globals."]),
                ("Should you call `valueOf()` yourself?", ["**No.** JavaScript uses it internally to unwrap Number objects."]),
                ("What is `Number.isNaN(NaN)` vs `NaN === NaN`?", ["**true** vs **false**. Prefer `Number.isNaN`."]),
            ],
            "Use instance methods to format numbers as strings (`toFixed`, `toPrecision`, `toString`). Use `Number()`, `parseInt`, and `parseFloat` to convert. Use `Number.isInteger` / `isFinite` / `isNaN` / `isSafeInteger` as **static** checks. Do not call those on a variable.",
            [
                ("JS Number Methods (W3Schools)", "https://www.w3schools.com/js/js_number_methods.asp"),
                ("MDN: Number", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number"),
                ("MDN: Number.prototype.toFixed()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed"),
                ("MDN: Number.isNaN()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN"),
            ],
        ),
        (
            "js-number-properties",
            "JS Number Properties",
            PROPS,
            "Number constants live on the **Number** object: `EPSILON`, `MAX_VALUE`, `MIN_VALUE`, safe-integer bounds, `±Infinity`, and `NaN`. Access them as **`Number.MAX_VALUE`**, never `x.MAX_VALUE`.",
            [
                "**`MIN_VALUE`** is the smallest **positive** number, not the most negative.",
                "**Safe integers** are `±(2⁵³−1)`.",
                "**`x.MAX_VALUE`** is **undefined** — properties are not inherited as you might expect from a value.",
            ],
            [
                ("What is `Number.EPSILON`?", ["About **2.22e-16** — the gap above 1. Use it as a float comparison tolerance."]),
                ("What is `Number.MAX_VALUE`?", ["About **1.80e+308**, the largest finite number."]),
                ("What does `(6).MAX_VALUE` return?", ["**undefined**. Write **`Number.MAX_VALUE`**."]),
                ("Is `Number.MIN_VALUE` negative?", ["**No.** It is the smallest **positive** value (~ **5e-324**)."]),
                ("What is `Number.MAX_SAFE_INTEGER`?", ["**9007199254740991** (2⁵³−1)."]),
                ("What is `Number.MIN_SAFE_INTEGER`?", ["**-9007199254740991**."]),
                ("What is `1 / 0`?", ["**Infinity**, the same as `Number.POSITIVE_INFINITY`."]),
                ("What is `-1 / 0`?", ["**-Infinity** (`Number.NEGATIVE_INFINITY`)."]),
                ("What is `Number.NaN`?", ["The same **NaN** value as the global `NaN`."]),
                ("When did EPSILON and safe integers arrive?", ["**ES6**."]),
            ],
            "Read limits from `Number`: EPSILON for float gaps, MAX/MIN_VALUE for magnitude, MAX/MIN_SAFE_INTEGER for exact integers, and the Infinity/NaN constants. Never look those names up on a numeric variable.",
            [
                ("JS Number Properties (W3Schools)", "https://www.w3schools.com/js/js_number_properties.asp"),
                ("MDN: Number.EPSILON", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON"),
                ("MDN: Number.MAX_SAFE_INTEGER", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER"),
            ],
        ),
        (
            "js-number-reference",
            "JS Number Reference",
            REF,
            "Complete **Number** catalog (revised July 2025): every property and method from **`constructor`** through **`valueOf()`**. Number methods return a **new** value; they do **not** change the original number. Each table row is its own Example.",
            [
                "**Grain** — one Example per reference-table row.",
                "**Static vs instance** — `Number.isInteger(x)` vs `x.toFixed(2)`.",
                "**`toLocaleString()`** is the extra instance method that the Methods chapter did not spotlight.",
            ],
            [
                ("Do number methods mutate the original?", ["**No.** They return a new value."]),
                ("How do you call `isInteger`?", ["**`Number.isInteger(x)`**, not `x.isInteger()`."]),
                ("What is `Number.MAX_SAFE_INTEGER`?", ["**9007199254740991**."]),
                ("What is `MIN_VALUE`?", ["Smallest **positive** number, **5e-324**."]),
                ("What does `parseInt` vs `parseFloat` do on `\"10.33\"`?", ["**10** vs **10.33**."]),
                ("Should you add methods to `Number.prototype`?", ["Only as a demo. Prefer a **plain function** so you do not break other code."]),
                ("What is `(9.656).toFixed(2)`?", ['**"9.66"**.' ]),
                ("What is `(255).toString(16)`?", ['**"ff"**.' ]),
                ("What does `toLocaleString('de-DE')` change?", ["Uses locale grouping and a **comma** decimal for German."]),
                ("What does `valueOf()` return on `new Number(123)`?", ["The primitive **123**."]),
            ],
            "Every Number property and method has its own Example. Format with `toFixed` / `toPrecision` / `toExponential` / `toString` / `toLocaleString`. Test with the static `is*` helpers. Read limits from the `Number.*` constants. Methods do not mutate.",
            [
                ("JS Number Reference (W3Schools)", "https://www.w3schools.com/js/js_number_reference.asp"),
                ("MDN: Number", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number"),
                ("MDN: Number.prototype.toLocaleString()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toLocaleString"),
            ],
        ),
        (
            "js-bitwise",
            "JS Bitwise",
            BITWISE,
            "Bitwise operators (`& | ^ ~ << >> >>>`) work on **32-bit signed integers**, even though Numbers are 64-bit floats. Each operator (and each assignment form) has its own Example, plus decimal↔binary helpers. Four-bit unsigned tables on the page are teaching aids — in real JS, `~5` is **−6**, not 10.",
            [
                "**32-bit two’s complement** — the leftmost bit is the sign.",
                "**`>>` keeps the sign**; **`>>>` zero-fills** (and makes negatives large positives).",
                "**Assignment forms** `&= |= ^= <<= >>= >>>=` update in place.",
            ],
            [
                ("What is `5 & 1`?", ["**1** — only bits set in both."]),
                ("What is `5 | 1`?", ["**5**."]),
                ("What is `5 ^ 1`?", ["**4**."]),
                ("What is `~5` in JavaScript?", ["**-6**, not 10. `~n === -(n+1)`."]),
                ("What is `5 << 1`?", ["**10**."]),
                ("What is `-5 >> 1`?", ["**-3** (sign preserved)."]),
                ("What is `5 >>> 1`?", ["**2**."]),
                ("What is `10 &= 5`?", ["**0**."]),
                ("What is `10 | 5`?", ["**15**."]),
                ("How do you convert 5 to binary?", ["`(5 >>> 0).toString(2)` → **101**."]),
                ("How do you parse binary `\"1111\"`?", ["`parseInt(\"1111\", 2)` → **15**."]),
                ("Why does `~5` differ from the 4-bit table?", ["The table uses 4-bit **unsigned** bits. JS uses **32-bit signed** integers."]),
            ],
            "Use `& | ^ ~` for bit masks and `<< >> >>>` to shift. Remember 32-bit signed conversion: `~5` is −6. `>>>` zero-fills. `dec >>> 0` plus `toString(2)` prints unsigned binary; `parseInt(s, 2)` parses it back.",
            [
                ("JS Bitwise (W3Schools)", "https://www.w3schools.com/js/js_bitwise.asp"),
                ("MDN: Bitwise operators", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND"),
                ("MDN: Unsigned right shift", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift"),
            ],
        ),
        (
            "js-bigint",
            "JS BigInt",
            BIGINT,
            "BigInt (ES2020) stores **integers of any size**, limited only by memory. Write `123n` or `BigInt(\"123\")`. Do not mix with Number without converting. No decimals, no `>>>`, no `Math.*`, no `JSON.stringify`.",
            [
                "Numbers lose precision past **2⁵³−1**. BigInt does not.",
                "**`typeof` is `\"bigint\"`** — the eighth JS type.",
                "Prefer **`n` literals or strings** over `BigInt(someNumber)` so digits are not pre-rounded.",
            ],
            [
                ("How do you write a BigInt?", ["A literal with **`n`**, or **`BigInt(\"digits\")`**."]),
                ("What is `typeof 1n`?", ['**"bigint"**.']),
                ("What happens if you write `10n + 5`?", ["**TypeError**. Convert with `Number(10n) + 5` or `10n + 5n`."]),
                ("What is `5n / 2n`?", ["**2n** — integer division truncates. There is no `1.5n`."]),
                ("Is `10n === 10`?", ["**false** (types differ). `10n == 10` is **true**."]),
                ("Does BigInt support `>>>`?", ["**No.** Only `<<` and `>>`. `>>>` throws TypeError."]),
                ("Why is `BigInt(9999999999999999)` wrong?", ["The Number is **already rounded** to 10000000000000000 before conversion."]),
                ("Can `JSON.stringify` serialize a BigInt?", ["**No** — it throws TypeError."]),
                ("Can `Math.sqrt` take a BigInt?", ["**No**."]),
                ("Why is `9007199254740992 === 9007199254740993` true?", ["Both round to the same Number. As BigInts they are **not** equal."]),
                ("Are hex/octal/binary BigInt literals allowed?", ["Yes: `0x100n`, `0o400n`, `0b100000000n`."]),
            ],
            "Use BigInt for integers that must stay exact past 15 digits. Create with `n` or `BigInt(\"...\")`, convert explicitly before mixing with Number, skip decimals/Math/JSON, and remember `===` is false against a Number even when `==` is true.",
            [
                ("JS BigInt (W3Schools)", "https://www.w3schools.com/js/js_bigint.asp"),
                ("MDN: BigInt", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt"),
                ("MDN: Number.MAX_SAFE_INTEGER", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER"),
            ],
        ),
    ]
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print("building", slug, "examples", len(recs))
        build_and_snap(slug, title, recs, intro, concepts, qa, summary, refs)
        print("done", slug)


if __name__ == "__main__":
    run_all()
