"""S6: JS Numbers through JS BigInt."""
from __future__ import annotations

from _gen_lib import S, build_and_snap

# ---------------------------------------------------------------------------
# 6.1 JS Numbers
# ---------------------------------------------------------------------------

NUMBERS = [
    S(
        "decimals",
        "Decimals and integers",
        [
            "JavaScript has **only one number type** — there is no separate `int` vs `float`.",
            "You may write a number **with or without** a decimal point. Both are the same `typeof`: **number**.",
        ],
        "let x = 3.14;    // A number with decimals\nlet y = 3;       // A number without decimals",
        [("x", "x"), ("y", "y"), ("typeof x", "typeof x"), ("typeof y", "typeof y")],
        "x is **3.14** and y is **3**. Both have `typeof` **number**.",
    ),
    S(
        "scientific",
        "Scientific (exponent) notation",
        [
            "**`e`** means “times ten to the power of”. `123e5` is 123 × 10⁵ = **12300000**.",
            "A **negative** exponent moves the point left: `123e-5` is **0.00123**.",
        ],
        "let x = 123e5;    // 12300000\nlet y = 123e-5;   // 0.00123",
        [("x", "x"), ("y", "y")],
        "x is **12300000**; y is **0.00123**.",
    ),
    S(
        "integer-precision",
        "Integer precision (15 digits)",
        [
            "Integers (no period, no exponent) are accurate up to **15 digits**.",
            "A **16-digit** integer is rounded: `9999999999999999` becomes **10000000000000000**.",
            "This is IEEE 754 — JavaScript cannot store every integer exactly past 2⁵³−1.",
        ],
        "let x = 999999999999999;   // x will be 999999999999999\nlet y = 9999999999999999;  // y will be 10000000000000000",
        [("x", "x"), ("y", "y")],
        "x stays **999999999999999**. y rounds to **10000000000000000**.",
    ),
    S(
        "float-sum",
        "Floating point: 0.2 + 0.1",
        [
            "Floating-point arithmetic is **not always 100% accurate**.",
            "`0.2` and `0.1` cannot be represented exactly in binary, so their sum is slightly off **0.3**.",
        ],
        "let x = 0.2 + 0.1;",
        [("x", "x"), ("x === 0.3", "x === 0.3")],
        "x is **0.30000000000000004**, not exactly 0.3. `x === 0.3` is **false**.",
    ),
    S(
        "float-fix",
        "Fix floating error with multiply and divide",
        [
            "A common fix is to work in **tenths** (or cents), then divide back.",
            "`(0.2 * 10 + 0.1 * 10) / 10` adds **2 + 1** as integers, then divides.",
        ],
        "let x = (0.2 * 10 + 0.1 * 10) / 10;",
        [("x", "x"), ("x === 0.3", "x === 0.3")],
        "x is **0.3** and `x === 0.3` is **true**.",
    ),
    S(
        "add-numbers",
        "Add two numbers",
        [
            "JavaScript uses **`+`** for both **addition** and **concatenation**.",
            "When **both** operands are numbers, `+` **adds**.",
        ],
        'let x = 10;\nlet y = 20;\nlet z = x + y;',
        [("z", "z"), ("typeof z", "typeof z")],
        "z is **30** (a number).",
    ),
    S(
        "add-strings",
        "Add two strings",
        [
            "When **both** operands are strings, `+` **concatenates**.",
            '`"10" + "20"` is **`"1020"`**, not 30.',
        ],
        'let x = "10";\nlet y = "20";\nlet z = x + y;',
        [("z", "z"), ("typeof z", "typeof z")],
        'z is **"1020"** (a string).',
    ),
    S(
        "number-plus-string",
        "Number + string concatenates",
        [
            "If **either** side of `+` is a string, JavaScript **concatenates**.",
            "`10 + \"20\"` becomes **`\"1020\"`**.",
        ],
        'let x = 10;\nlet y = "20";\nlet z = x + y;',
        [("z", "z")],
        'z is **"1020"**.',
    ),
    S(
        "string-plus-number",
        "String + number concatenates",
        [
            "Order does not save you: a string on the **left** still concatenates.",
            '`"10" + 20` is **`"1020"`**.',
        ],
        'let x = "10";\nlet y = 20;\nlet z = x + y;',
        [("z", "z")],
        'z is **"1020"**.',
    ),
    S(
        "result-is-concat",
        'Common mistake: "The result is: " + x + y',
        [
            "A common mistake is expecting **30** after a label string.",
            "Evaluation is **left to right**: first `\"The result is: \" + 10` becomes a string, then that string `+ 20` concatenates again.",
        ],
        'let x = 10;\nlet y = 20;\nlet z = "The result is: " + x + y;',
        [("z", "z")],
        'z is **"The result is: 1020"**, not "The result is: 30".',
    ),
    S(
        "left-to-right",
        "Left-to-right: numbers then a string",
        [
            "A common mistake is expecting **102030**.",
            "First `10 + 20` **adds** (both numbers) → **30**. Then `30 + \"30\"` **concatenates** → **`\"3030\"`**.",
        ],
        'let x = 10;\nlet y = 20;\nlet z = "30";\nlet result = x + y + z;',
        [("result", "result")],
        'result is **"3030"** because the interpreter works **left to right**.',
    ),
    S(
        "numeric-content",
        "Numeric strings vs numbers",
        [
            "A string can **look** numeric: `\"100\"` is still a **string**.",
            "`100` (no quotes) is a **number**. `typeof` tells them apart.",
        ],
        'let x = 100;      // x is a number\nlet y = "100";    // y is a string',
        [("x", "x"), ("typeof x", "typeof x"), ("y", "y"), ("typeof y", "typeof y")],
        'x is number **100**; y is string **"100"**.',
    ),
    S(
        "numeric-divide",
        "Numeric strings: division",
        [
            "For **numeric operations other than `+`**, JavaScript **converts** numeric strings to numbers.",
            '`"100" / "10"` is **10**.',
        ],
        'let x = "100";\nlet y = "10";\nlet z = x / y;',
        [("z", "z"), ("typeof z", "typeof z")],
        "z is **10** (a number).",
    ),
    S(
        "numeric-multiply",
        "Numeric strings: multiplication",
        [
            "`*` also converts numeric strings.",
            '`"100" * "10"` is **1000**.',
        ],
        'let x = "100";\nlet y = "10";\nlet z = x * y;',
        [("z", "z")],
        "z is **1000**.",
    ),
    S(
        "numeric-subtract",
        "Numeric strings: subtraction",
        [
            "`-` converts numeric strings too.",
            '`"100" - "10"` is **90**.',
        ],
        'let x = "100";\nlet y = "10";\nlet z = x - y;',
        [("z", "z")],
        "z is **90**.",
    ),
    S(
        "numeric-add-fails",
        "Numeric strings: + still concatenates",
        [
            "**`+` is the exception.** It concatenates strings instead of converting them.",
            '`"100" + "10"` is **`"10010"`**, not 110.',
        ],
        'let x = "100";\nlet y = "10";\nlet z = x + y;',
        [("z", "z")],
        'z is **"10010"**.',
    ),
    S(
        "nan-apple",
        'NaN from 100 / "Apple"',
        [
            "**`NaN`** means **Not a Number** — the result of illegal numeric math.",
            'Dividing by a **non-numeric** string yields **NaN**.',
        ],
        'let x = 100 / "Apple";',
        [("x", "x")],
        "x is **NaN**.",
    ),
    S(
        "divide-numeric-string",
        '100 / "10" is a number',
        [
            "If the string **is** numeric, arithmetic works.",
            '`"10"` converts; the result is **10**.',
        ],
        'let x = 100 / "10";',
        [("x", "x")],
        "x is **10**.",
    ),
    S(
        "isnan",
        "`isNaN()` checks Not-a-Number",
        [
            "Use global **`isNaN()`** to test whether a value is NaN.",
            "`isNaN` of a legal number is **false**; of `100 / \"Apple\"` is **true**.",
        ],
        'let x = 100 / "Apple";\nisNaN(x);',
        [("x", "x"), ("isNaN(x)", "isNaN(x)"), ("isNaN(100 / '10')", "isNaN(100 / '10')")],
        "`isNaN(x)` is **true**. `isNaN(100 / \"10\")` is **false**.",
    ),
    S(
        "nan-plus-number",
        "NaN infects math",
        [
            "If you use **NaN** in further math, the result is also **NaN**.",
            "`NaN + 5` is **NaN**, not 5.",
        ],
        "let x = NaN;\nlet y = 5;\nlet z = x + y;",
        [("z", "z")],
        "z is **NaN**.",
    ),
    S(
        "nan-plus-string",
        "NaN + string concatenates",
        [
            "`+` with a **string** concatenates even when one side is NaN.",
            '`NaN + "5"` becomes **`"NaN5"`**.',
        ],
        'let x = NaN;\nlet y = "5";\nlet z = x + y;',
        [("z", "z")],
        'z is **"NaN5"**.',
    ),
    S(
        "typeof-nan",
        "`typeof NaN` is number",
        [
            "**Surprise:** `typeof NaN` returns **`\"number\"`**.",
            "NaN is a **numeric value** that means “this number is invalid”, not a separate type.",
        ],
        "typeof NaN;",
        [("typeof NaN", "typeof NaN")],
        '`typeof NaN` is **"number"**.',
    ),
    S(
        "loop-infinity",
        "Overflow to Infinity",
        [
            "**Infinity** is what you get when a calculation exceeds the largest finite number.",
            "Repeatedly squaring 2 eventually overflows: 2 → 4 → 16 → … → **Infinity**.",
        ],
        "let myNumber = 2;\nwhile (myNumber != Infinity) {\n  myNumber = myNumber * myNumber;\n}",
        [("myNumber", "myNumber")],
        "After the loop, myNumber is **Infinity**.",
    ),
    S(
        "divide-by-zero",
        "Division by zero",
        [
            "In JavaScript, dividing by **0** does **not** throw. It yields **Infinity** (or **−Infinity**).",
            "`2 / 0` → **Infinity**; `-2 / 0` → **−Infinity**.",
        ],
        "let x = 2 / 0;\nlet y = -2 / 0;",
        [("x", "x"), ("y", "y")],
        "x is **Infinity**; y is **-Infinity**.",
    ),
    S(
        "typeof-infinity",
        "`typeof Infinity` is number",
        [
            "Infinity is also a **number**.",
            '`typeof Infinity` is **"number"**.',
        ],
        "typeof Infinity;",
        [("typeof Infinity", "typeof Infinity"), ("typeof -Infinity", "typeof -Infinity")],
        'Both Infinity and -Infinity have `typeof` **"number"**.',
    ),
    S(
        "hex",
        "Hexadecimal 0xFF",
        [
            "A literal starting with **`0x`** is **hexadecimal** (base 16).",
            "`0xFF` is **255** in decimal.",
            "**Do not** write a number with a leading **`0`** (like `07`). Old engines treated that as **octal**; modern strict mode makes it a **SyntaxError**.",
        ],
        "let x = 0xFF;",
        [("x", "x")],
        "x is **255**.",
    ),
    S(
        "tostring-radix",
        "`toString()` bases 2–36",
        [
            "By default, JavaScript **displays** numbers in **base 10**.",
            "**`toString(radix)`** writes the same value in another base (2–36).",
            "Base 16 is hex, 10 decimal, 8 octal, 2 binary. Base 32 and 12 are also legal.",
        ],
        "let myNumber = 32;\nmyNumber.toString(32);\nmyNumber.toString(16);\nmyNumber.toString(12);\nmyNumber.toString(10);\nmyNumber.toString(8);\nmyNumber.toString(2);",
        [
            ("toString(32)", "myNumber.toString(32)"),
            ("toString(16)", "myNumber.toString(16)"),
            ("toString(12)", "myNumber.toString(12)"),
            ("toString(10)", "myNumber.toString(10)"),
            ("toString(8)", "myNumber.toString(8)"),
            ("toString(2)", "myNumber.toString(2)"),
        ],
        "32 in those bases is **10**, **20**, **28**, **32**, **40**, **100000**.",
    ),
    S(
        "number-object",
        "`new Number()` vs a literal",
        [
            "A normal number is a **primitive**: `let x = 123`.",
            "`new Number(123)` is a **Number object** (`typeof` **object**).",
            "**Do not** create Number objects — they slow the code and cause `==` / `===` surprises.",
        ],
        "let x = 123;\nlet y = new Number(123);",
        [("typeof x", "typeof x"), ("typeof y", "typeof y")],
        '`typeof x` is **"number"**; `typeof y` is **"object"**.',
    ),
    S(
        "object-loose-eq",
        "Literal == Number object",
        [
            "`==` **coerces**. A primitive **500** equals `new Number(500)` because the object is converted.",
        ],
        "let x = 500;\nlet y = new Number(500);",
        [("x == y", "x == y")],
        "`x == y` is **true**.",
    ),
    S(
        "object-strict-eq",
        "Literal === Number object",
        [
            "`===` requires the **same type**. A primitive is not an object.",
            "`500 === new Number(500)` is **false**.",
        ],
        "let x = 500;\nlet y = new Number(500);",
        [("x === y", "x === y")],
        "`x === y` is **false**.",
    ),
    S(
        "two-objects-loose",
        "Two Number objects with ==",
        [
            "Comparing **two objects** with `==` still returns **false** — objects compare by **reference**, not value.",
            "`new Number(500) == new Number(500)` is **false**.",
        ],
        "let x = new Number(500);\nlet y = new Number(500);",
        [("x == y", "x == y")],
        "`x == y` is **false**.",
    ),
    S(
        "two-objects-strict",
        "Two Number objects with ===",
        [
            "`===` on two different objects is also **false**.",
            "This is why the page says: **do not create Number objects**.",
        ],
        "let x = new Number(500);\nlet y = new Number(500);",
        [("x === y", "x === y")],
        "`x === y` is **false**. Two objects are never equal to each other this way.",
    ),
]


def build_numbers() -> str:
    return build_and_snap(
        "js-numbers",
        "JS Numbers",
        NUMBERS,
        "JavaScript has **one** number type: 64-bit IEEE 754 floating point. That explains integer rounding past 15 digits, `0.2 + 0.1`, `NaN`, `Infinity`, hex literals, and why `new Number()` is a bad idea. Each Tryit on the W3Schools page is its own Example.",
        [
            "**One type** — no byte/short/int/long/float. Everything is a **double** (52-bit fraction, 11-bit exponent, 1 sign bit).",
            "**`+` is overloaded** — numbers add; if either side is a string, it concatenates. `/` `*` `-` convert numeric strings.",
            "**NaN and Infinity** are still `typeof \"number\"`.",
            "**Do not use `new Number()`** — `==` can be true while `===` is false; two Number objects compare false.",
        ],
        [
            ("How many number types does JavaScript have?", ["**One.** All numbers are IEEE 754 **doubles**."]),
            ("What is `9999999999999999` stored as?", ["**10000000000000000** — integers are exact only up to **15 digits** / `Number.MAX_SAFE_INTEGER`."]),
            ("What is `0.2 + 0.1`?", ["**0.30000000000000004**, not 0.3.", "Work in tenths: `(0.2 * 10 + 0.1 * 10) / 10`."]),
            ("What is `10 + \"20\"`?", ['**`"1020"`** — `+` concatenates when a string is involved.']),
            ('What is `"The result is: " + 10 + 20`?', ['**`"The result is: 1020"`** — left to right, after the first concatenation everything is a string.']),
            ("What is `10 + 20 + \"30\"`?", ['**`"3030"`** — first add the numbers, then concatenate.']),
            ('What is `"100" / "10"` vs `"100" + "10"`?', ["Division is **10** (converted).", "Addition is **`\"10010\"`** (concatenated)."]),
            ('What is `100 / "Apple"`?', ["**NaN**.", "`isNaN` of that value is **true**.", '`typeof NaN` is still **"number"**.']),
            ("What is `2 / 0`?", ["**Infinity**.", '`typeof Infinity` is **"number"**.' ]),
            ("What is `0xFF`?", ["**255** in decimal. `0x` means hexadecimal."]),
            ("What does `(32).toString(2)` return?", ['**`"100000"`** — binary.']),
            ("Is `500 == new Number(500)` true?", ["**Yes** with `==`.", "**No** with `===`.", "Two `new Number(500)` objects compare **false** even with `==`."]),
        ],
        "JavaScript numbers are always 64-bit floats: 15-digit integers stay exact, `0.2 + 0.1` does not, `+` concatenates strings, other operators convert numeric strings, NaN and Infinity are still numbers, `0x` is hex, and `new Number()` should be avoided.",
        [
            ("JS Numbers (W3Schools)", "https://www.w3schools.com/js/js_numbers.asp"),
            ("MDN: Number", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number"),
            ("MDN: NaN", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN"),
            ("IEEE 754", "https://en.wikipedia.org/wiki/IEEE_754"),
        ],
    )


if __name__ == "__main__":
    md = build_numbers()
    print("js-numbers examples", len(NUMBERS), "chars", len(md))
