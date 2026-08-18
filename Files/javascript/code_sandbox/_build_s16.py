"""S16: JS RegExp (10 W3Schools pages)."""
from __future__ import annotations

import json

from _gen_lib import S, build_and_snap, display_script

GIVE = "Give 100%!"
HELLO_W = "Hello World!"
VISIT = "Visit W3Schools"
IS_ALL = "Is this all there is?"
COLORS = "Black, white, red, green, blue, yellow."
HELLOOO = "Hellooo World! Hello W3Schools!"
NUMS = "100, 1000 or 10000?"
LOOK = "HELLO, LOOK AT YOU!"
FREE = "The best things in life are free!"
VISIT_DOT = "Visit W3Schools. Hello World!"
HEXAGRAM = "\u4dc0"  # ䷀ U+4DC0
EMOJI = "Hello \U0001f604"  # Hello 😄


def SM(stem, title, bullets, code, outcome, extra=None):
    displays = [("result", "JSON.stringify(result)")]
    if extra:
        displays.extend(extra)
    return S(stem, title, bullets, code, displays, outcome)


def ST(stem, title, bullets, code, outcome, extra=None):
    displays = [("result", "result")]
    if extra:
        displays.extend(extra)
    return S(stem, title, bullets, code, displays, outcome)


def match_code(text, pattern, flags="g"):
    return (
        "let text = "
        + json.dumps(text)
        + ";\nconst pattern = /"
        + pattern
        + "/"
        + flags
        + ";\nlet result = text.match(pattern);"
    )


def test_code(text, pattern, flags=""):
    return (
        "let text = "
        + json.dumps(text)
        + ";\nconst pattern = /"
        + pattern
        + "/"
        + flags
        + ";\nlet result = pattern.test(text);"
    )


def row_match(stem, title, bullets, pattern, text, flags, outcome):
    return SM(stem, title, bullets, match_code(text, pattern, flags), outcome)


def row_test(stem, title, bullets, pattern, text, flags, outcome):
    return ST(stem, title, bullets, test_code(text, pattern, flags), outcome)


def modifier_S(stem, title, bullets, shown, pattern_src, text, outcome, flags=""):
    run = (
        "let text = "
        + json.dumps(text)
        + ";\nlet result;\ntry {\n  const pattern = new RegExp("
        + json.dumps(pattern_src)
        + ", "
        + json.dumps(flags)
        + ");\n  result = pattern.test(text);\n} catch (e) {\n"
        '  result = e.name + ": " + e.message;\n}'
    )
    return S(
        stem,
        title,
        bullets,
        shown,
        [("result", "result")],
        outcome,
        script=display_script(run, [("result", "result")]),
    )


# ---------------------------------------------------------------------------
# 16.1 JS RegExp
# ---------------------------------------------------------------------------

LANDING = [
    ST(
        "search-insensitive",
        'text.search(/w3Schools/i)',
        [
            "A regex literal is **`/pattern/flags`**. **`i`** makes the search case-insensitive.",
            "`String.search(regex)` returns the **index** of the first match, or **-1**.",
        ],
        'let text = "Visit W3Schools!";\nlet result = text.search(/w3Schools/i);',
        "**6** — `W3Schools` starts at index 6 in `Visit W3Schools!`.",
    ),
    SM(
        "match-first",
        "text.match(/W3Schools/)",
        [
            "`String.match(regex)` without **`g`** returns one match **array** (or **null**).",
            "The page snippet used `/W3schools/` (wrong case) which is **null**. This Tryit uses **`/W3Schools/`**.",
        ],
        'let text = "Visit W3Schools!";\nlet result = text.match(/W3Schools/);',
        '`JSON.stringify(result)` is **["W3Schools"]**. Extra fields `index` / `input` are omitted by JSON.',
    ),
    ST(
        "replace-microsoft",
        'text.replace(/Microsoft/, "W3Schools")',
        [
            "`String.replace(regex, s)` returns a **new** string. The original is unchanged.",
            "This Tryit is **case-sensitive** (no **`i`**).",
        ],
        'let text = "Please visit Microsoft!";\nlet result = text.replace(/Microsoft/, "W3Schools");',
        'result is **"Please visit W3Schools!"**.',
    ),
    ST(
        "search-exact",
        "text.search(/W3Schools/)",
        [
            "`search` without **`i`** is case-sensitive.",
            "It still returns an **index**, not the matched text.",
        ],
        'let text = "Visit W3Schools!";\nlet result = text.search(/W3Schools/);',
        "**6**.",
    ),
    SM(
        "alternation-or",
        "/red|green|blue/g — alternation",
        [
            "**`|`** is OR: match **red** or **green** or **blue**.",
            "**`g`** finds **all** alternatives, not only the first.",
        ],
        'let text = "Black, white, red, green, blue, yellow.";\nlet result = text.match(/red|green|blue/g);',
        '`JSON.stringify(result)` is **["red","green","blue"]**.',
    ),
    SM(
        "flag-g",
        "/is/g — global",
        [
            "Without **`g`**, `match` stops at the first `is`.",
            "**`/is/g`** is case-sensitive, so the leading **`Is`** is skipped.",
        ],
        'let text = "Is this all there is?";\nconst pattern = /is/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["is","is"]** (`this` and the final `is`).',
    ),
    SM(
        "flag-i",
        "/w3schools/i — insensitive",
        [
            "**`i`** matches any case: `w3schools` finds **`W3Schools`**.",
        ],
        'let text = "Visit W3Schools";\nconst pattern = /w3schools/i;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["W3Schools"]**.',
    ),
    SM(
        "meta-d",
        r"/\d/g — digits",
        [
            r"**`\d`** matches a digit **0–9**.",
        ],
        'let text = "Give 100%!";\nconst pattern = /\\d/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["1","0","0"]**.',
    ),
    SM(
        "meta-w",
        r"/\w/g — word characters",
        [
            r"**`\w`** is **`[A-Za-z0-9_]`**. Space, `%`, and `!` are not word characters.",
        ],
        'let text = "Give 100%!";\nconst pattern = /\\w/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["G","i","v","e","1","0","0"]**.',
    ),
    SM(
        "quant-10-optional",
        "/10?/g — optional 0",
        [
            "**`?`** means **zero or one** of the previous token.",
            "`10?` is a `1` plus an optional `0` — **not** “ten, maybe”.",
        ],
        'let text = "1, 100 or 1000?";\nconst pattern = /10?/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["1","10","10"]** (the lone `1`, then `10` from `100` and `1000`).',
    ),
    ST(
        "assert-hat-true",
        "/^W3Schools/ — starts with (true)",
        [
            "**`^`** matches the **start** of the string (or of each line with **`m`**).",
        ],
        'const pattern = /^W3Schools/;\nlet text = "W3Schools tutorial";\nlet result = pattern.test(text);',
        "**true**.",
    ),
    ST(
        "assert-hat-false",
        "/^W3Schools/ — starts with (false)",
        [
            "`Hello W3Schools` does **not** start with `W3Schools`.",
        ],
        'const pattern = /^W3Schools/;\nlet text = "Hello W3Schools";\nlet result = pattern.test(text);',
        "**false**.",
    ),
    ST(
        "assert-dollar-true",
        "/W3Schools$/ — ends with (true)",
        [
            "**`$`** matches the **end** of the string.",
        ],
        'const pattern = /W3Schools$/;\nlet text = "Hello W3Schools";\nlet result = pattern.test(text);',
        "**true**.",
    ),
    ST(
        "assert-dollar-false",
        "/W3Schools$/ — ends with (false)",
        [
            "`W3Schools tutorial` ends with **tutorial**, not `W3Schools`.",
        ],
        'const pattern = /W3Schools$/;\nlet text = "W3Schools tutorial";\nlet result = pattern.test(text);',
        "**false**.",
    ),
    SM(
        "class-0-9",
        "/[0-9]/g — digit class",
        [
            "**`[0-9]`** is a character class: any digit. Same idea as **`\\d`** for ASCII digits.",
        ],
        'let text = "More than 1000 times";\nconst pattern = /[0-9]/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["1","0","0","0"]**.',
    ),
]


# ---------------------------------------------------------------------------
# 16.2 JS RegExp Flags
# ---------------------------------------------------------------------------

FLAGS = [
    SM(
        "flag-g",
        "/is/g — global",
        [
            "**`/g`** finds **all** matches. `match` then returns an array of strings.",
            "Case-sensitive: **`Is`** is not **`is`**.",
        ],
        'let text = "Is this all there is?";\nconst pattern = /is/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["is","is"]**.',
    ),
    SM(
        "flag-i",
        "/w3schools/i — insensitive",
        [
            "**`/i`** ignores case.",
        ],
        'let text = "Visit W3Schools";\nconst pattern = /w3schools/i;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["W3Schools"]**.',
    ),
    SM(
        "flag-d",
        "/(aa)(bb)/d — indices",
        [
            "**`/d`** (hasIndices) adds **`result.indices`**: `[start, end)` pairs per group.",
            "It does **not** change what text matches. `aaaabb` matches **`aabb`** at index **2**.",
        ],
        'let text = "aaaabb";\nconst pattern = /(aa)(bb)/d;\nlet result = text.match(pattern);\nlet indexes = result.indices;',
        '`JSON.stringify(result)` is **["aabb","aa","bb"]**. `indices` is **[[2,6],[2,4],[4,6]]**.',
        extra=[("indexes", "JSON.stringify(indexes)")],
    ),
    SM(
        "flag-s",
        "/Line./gs — dotAll",
        [
            "**`/s`** lets **`.`** match line terminators.",
            "Combined with **`g`**: `Line\\n` and `Line.`.",
        ],
        'let text = "Line\\nLine.";\nconst pattern = /Line./gs;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["Line\\n","Line."]** (the first match includes the newline).',
    ),
    SM(
        "flag-m",
        "/^is/m — multiline",
        [
            "**`/m`** makes **`^` / `$`** match at **each line** start/end, not only the whole string.",
            "The Tryit text is `\"\\nIs th\\nis it?\"`. **`/^is/m`** is still case-sensitive.",
        ],
        'let text = "\\nIs th\\nis it?";\nlet result = text.match(/^is/m);',
        '`JSON.stringify(result)` is **["is"]** (start of the line `is it?`). `Is th` does not match.',
    ),
    SM(
        "flag-y",
        "/\\w+/y — sticky from lastIndex",
        [
            "**`/y`** (sticky) matches **only** at **`lastIndex`**, not later.",
            "`lastIndex = 4` on `abc def ghi` is the **`d`** of `def`.",
        ],
        'let text = "abc def ghi";\nconst pattern = /\\w+/y;\npattern.lastIndex = 4;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["def"]**. After the match, `lastIndex` is **7**.',
        extra=[("pattern.lastIndex", "pattern.lastIndex")],
    ),
    SM(
        "flag-y-without",
        "/\\w+/ without y — lastIndex ignored",
        [
            "Without **`y`** (and without using **`exec`/`test` with `g`**), `String.match` does **not** honor `lastIndex`.",
            "The Tryit still **sets** `lastIndex = 4`, then matches from the start.",
        ],
        'let text = "abc def ghi";\nconst pattern = /\\w+/;\npattern.lastIndex = 4;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["abc"]**. `lastIndex` stays **4** (unused).',
        extra=[("pattern.lastIndex", "pattern.lastIndex")],
    ),
    ST(
        "flag-u",
        r"/\u{04DC0}/u — Unicode code point",
        [
            "**`/u`** treats the pattern as Unicode **code points** (not UTF-16 surrogates).",
            r"`\u{04DC0}` is hexagram **䷀** (U+4DC0).",
        ],
        'let text = "\\u4DC0";\nconst pattern = /\\u{04DC0}/u;\nlet result = pattern.test(text);',
        "**true**.",
    ),
    ST(
        "flag-u-without",
        r"/\u{04DC0}/ without u",
        [
            "The page says this is **false**. This V8 engine still compiles `\\u{04DC0}` to that character.",
            "Run the engine you ship — do not assume the page’s **false**.",
        ],
        'let text = "\\u4DC0";\nconst pattern = /\\u{04DC0}/;\nlet result = pattern.test(text);',
        "**true** in this V8 (the pattern source is the hexagram). The page’s **false** is outdated here.",
    ),
    ST(
        "flag-v",
        r"/\p{Emoji}/v — Unicode sets",
        [
            "**`/v`** is an upgrade to **`/u`**: Unicode property escapes and set notation.",
            r"`\p{Emoji}` matches emoji (needs **`u`** or **`v`**).",
        ],
        'let text = "Hello \\u{1F604}";\nconst pattern = /\\p{Emoji}/v;\nlet result = pattern.test(text);',
        "**true**.",
    ),
    ST(
        "flag-v-without",
        r"/\p{Emoji}/ without v",
        [
            "Without **`u`/`v`**, `\\p{Emoji}` is **not** a property escape: the source becomes **`p{Emoji}`**.",
            "That pattern does **not** match the emoji, so `test` is **false** (not a throw).",
        ],
        'let text = "Hello \\u{1F604}";\nconst pattern = /\\p{Emoji}/;\nlet result = pattern.test(text);',
        "**false**. `pattern.source` is **`p{Emoji}`**.",
        extra=[("pattern.source", "pattern.source")],
    ),
    modifier_S(
        "group-modifier-true",
        "(?i:W3Schools) tutorials — inline i (true)",
        [
            "**`(?flags:pattern)`** turns flags **on** for that group only (ES2025).",
            "Only **`i`**, **`m`**, and **`s`** are valid group modifiers.",
        ],
        'let text = "W3Schools tutorials.";\nconst pattern = /(?i:W3Schools) tutorials/;\nlet result = pattern.test(text);',
        "(?i:W3Schools) tutorials",
        "W3Schools tutorials.",
        "**true** — the group is case-insensitive; ` tutorials` matches as written.",
    ),
    modifier_S(
        "group-modifier-false",
        "(?i:W3Schools) tutorials — inline i (false)",
        [
            "`Tutorials` (capital **T**) does **not** match the case-sensitive ` tutorials` tail.",
            "The **`i`** flag does **not** leak out of the group.",
        ],
        'let text = "W3Schools Tutorials.";\nconst pattern = /(?i:W3Schools) tutorials/;\nlet result = pattern.test(text);',
        "(?i:W3Schools) tutorials",
        "W3Schools Tutorials.",
        "**false**.",
    ),
    ST(
        "prop-dotall",
        "pattern.dotAll",
        [
            "**`dotAll`** is **true** when **`/s`** is set.",
        ],
        "const pattern = /W3Schools/s;\nlet result = pattern.dotAll;",
        "**true**.",
    ),
    ST(
        "prop-global",
        "pattern.global",
        [
            "**`global`** is **true** when **`/g`** is set.",
        ],
        "const pattern = /W3Schools/g;\nlet result = pattern.global;",
        "**true**.",
    ),
    ST(
        "prop-hasindices",
        "pattern.hasIndices",
        [
            "**`hasIndices`** is **true** when **`/d`** is set.",
        ],
        "const pattern = /W3Schools/d;\nlet result = pattern.hasIndices;",
        "**true**.",
    ),
    ST(
        "prop-ignorecase",
        "pattern.ignoreCase",
        [
            "**`ignoreCase`** is **true** when **`/i`** is set.",
        ],
        "const pattern = /W3Schools/i;\nlet result = pattern.ignoreCase;",
        "**true**.",
    ),
    ST(
        "prop-multiline",
        "pattern.multiline",
        [
            "**`multiline`** is **true** when **`/m`** is set.",
        ],
        "const pattern = /W3Schools/m;\nlet result = pattern.multiline;",
        "**true**.",
    ),
    ST(
        "prop-sticky",
        "pattern.sticky",
        [
            "**`sticky`** is **true** when **`/y`** is set.",
        ],
        "const pattern = /W3Schools/y;\nlet result = pattern.sticky;",
        "**true**.",
    ),
    ST(
        "prop-unicode",
        "pattern.unicode",
        [
            "**`unicode`** is **true** when **`/u`** is set.",
        ],
        "let text = \"\\u4DC0\";\nconst pattern = /\\u{04DC0}/u;\nlet result = pattern.unicode;",
        "**true**.",
        extra=[("text", "text")],
    ),
    ST(
        "prop-unicodesets",
        "pattern.unicodeSets",
        [
            "**`unicodeSets`** is **true** when **`/v`** is set.",
        ],
        'let text = "Hello \\u{1F604}";\nconst pattern = /\\p{Emoji}/v;\nlet result = pattern.unicodeSets;',
        "**true**.",
        extra=[("text", "text")],
    ),
]


# ---------------------------------------------------------------------------
# 16.3 JS RegExp Classes
# ---------------------------------------------------------------------------

CLASSES = [
    SM(
        "class-hw",
        "/[HW]/g — Tryit [HW]",
        [
            "**`[HW]`** matches **H** or **W** (the `[abc]` idea with two letters).",
        ],
        'let text = "Hello World!";\nconst pattern = /[HW]/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["H","W"]**.',
    ),
    SM(
        "class-upper-A-Z",
        "/[A-Z]/g — Tryit uppercase range",
        [
            "**`[A-Z]`** is the uppercase range. **`[a-z]`** is the lowercase twin on the table.",
        ],
        'let text = "This is W3Schools";\nconst pattern = /[A-Z]/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["T","W","S"]**.',
    ),
    SM(
        "class-1234",
        "/[1234]/g — Tryit listed digits",
        [
            "**`[1234]`** lists characters. Same matches as **`[1-4]`** for these digits.",
        ],
        'let text = "123456789";\nconst pattern = /[1234]/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["1","2","3","4"]**.',
    ),
    SM(
        "class-1-4",
        "/[1-4]/g — Tryit digit range",
        [
            "**`[1-4]`** is a range. The page notes **`[01234]`** equals **`[0-4]`**.",
        ],
        'let text = "123456789";\nconst pattern = /[1-4]/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["1","2","3","4"]**.',
    ),
    row_match(
        "class-a",
        "[a] — one character",
        ["**`[a]`** matches that one character, anywhere."],
        "[a]",
        "cat",
        "g",
        '`JSON.stringify(result)` is **["a"]**. `"XYZ".match(/[a]/)` would be **null**.',
    ),
    row_match(
        "class-not-a",
        "[^a] — negated character",
        ["**`[^a]`** matches any character **except** `a`."],
        "[^a]",
        "cat",
        "g",
        '`JSON.stringify(result)` is **["c","t"]**.',
    ),
    row_match(
        "class-abc",
        "[abc] — any listed",
        ["**`[abc]`** matches **a**, **b**, or **c**."],
        "[abc]",
        "fabric",
        "g",
        '`JSON.stringify(result)` is **["a","b","c"]**.',
    ),
    row_match(
        "class-not-abc",
        "[^abc] — none of listed",
        ["**`[^abc]`** matches characters **not** in `{a,b,c}`."],
        "[^abc]",
        "fabric",
        "g",
        '`JSON.stringify(result)` is **["f","r","i"]**.',
    ),
    row_match(
        "class-lower-a-z",
        "[a-z] — lowercase range",
        ["**`[a-z]`** is every lowercase English letter."],
        "[a-z]",
        "A1b",
        "g",
        '`JSON.stringify(result)` is **["b"]**.',
    ),
    row_match(
        "class-not-a-z",
        "[^a-z] — not lowercase",
        ["**`[^a-z]`** matches anything that is **not** a lowercase letter."],
        "[^a-z]",
        "A1b",
        "g",
        '`JSON.stringify(result)` is **["A","1"]**.',
    ),
    row_match(
        "class-0-9-table",
        "[0-9] — digit range",
        ["**`[0-9]`** matches ASCII digits. **`[^0-9]`** is the complement."],
        "[0-9]",
        "A1b",
        "g",
        '`JSON.stringify(result)` is **["1"]**.',
    ),
    row_match(
        "class-not-0-9",
        "[^0-9] — not a digit",
        ["**`[^0-9]`** matches non-digits (same idea as **`\\D`** for ASCII)."],
        "[^0-9]",
        "A1b",
        "g",
        '`JSON.stringify(result)` is **["A","b"]**.',
    ),
]


# ---------------------------------------------------------------------------
# 16.4 JS RegExp Metachars
# ---------------------------------------------------------------------------

METACHARS = [
    SM(
        "meta-d",
        r"\d — digits",
        [r"**`\d`** matches digits. Global `match` returns each digit as its own hit."],
        'let text = "Give 100%!";\nconst pattern = /\\d/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["1","0","0"]**.',
    ),
    SM(
        "meta-nondigit",
        r"\D — non-digits",
        [r"**`\D`** is the complement of **`\d`**."],
        'let text = "Give 100%!";\nconst pattern = /\\D/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["G","i","v","e"," ","%","!"]**.',
    ),
    SM(
        "meta-w",
        r"\w — word characters",
        [r"**`\w`** is **`[A-Za-z0-9_]`**."],
        'let text = "Give 100%!";\nconst pattern = /\\w/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["G","i","v","e","1","0","0"]**.',
    ),
    SM(
        "meta-nonword",
        r"\W — non-word characters",
        [r"**`\W`** matches space, punctuation, `%`, `!`, etc."],
        'let text = "Give 100%!";\nconst pattern = /\\W/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **[" ","%","!"]**.',
    ),
    SM(
        "meta-s",
        r"\s — whitespace",
        [r"**`\s`** matches space, tab, newline, and other whitespace."],
        'let text = "Is this all there is?";\nconst pattern = /\\s/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **[" "," "," "," "]** (four spaces). `String(result)` would look like ` , , , `.',
    ),
    row_match(
        "meta-nonspace",
        r"\S — non-whitespace",
        [r"**`\S`** is the complement of **`\s`**. No Tryit on the page — still run it."],
        r"\S",
        GIVE,
        "g",
        '`JSON.stringify(result)` is **["G","i","v","e","1","0","0","%","!"]**.',
    ),
    row_match(
        "meta-octal",
        r"\ddd — octal character",
        [
            r"**`\ddd`** is an octal code point. **`\127`** is **W** (octal 127 = 87).",
            "Octal escapes are a legacy form. Prefer **`\\xhh`** / **`\\uhhhh`**. No Tryit on the page.",
        ],
        r"\127",
        VISIT_DOT,
        "g",
        '`JSON.stringify(result)` is **["W","W"]**.',
    ),
    ST(
        "meta-hex",
        r"\xhh — hexadecimal replace",
        [
            r"**`\x6F`** is **`o`** (hex 6F).",
            "The Tryit **replaces** each `o` with `*`.",
        ],
        'let text = "Visit W3Schools. Hello World!";\nlet pattern = /\\x6F/g;\nlet result = text.replace(pattern, "*");',
        'result is **"Visit W3Sch**ls. Hell* W*rld!"**.',
    ),
    SM(
        "meta-unicode",
        r"\uhhhh — Unicode hex",
        [
            r"**`\u0057`** is **W** (U+0057).",
        ],
        'let text = "Visit W3Schools. Hello World!";\nconst pattern = /\\u0057/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["W","W"]**.',
    ),
]


# ---------------------------------------------------------------------------
# 16.5 JS RegExp Assertions
# ---------------------------------------------------------------------------

ASSERTIONS = [
    ST(
        "hat-true",
        "^ — beginning (true)",
        ["**`^`** is a **string** (or line, with **`m`**) boundary — it consumes no characters."],
        'const pattern = /^W3Schools/;\nlet text = "W3Schools tutorial";\nlet result = pattern.test(text);',
        "**true**.",
    ),
    ST(
        "hat-false",
        "^ — beginning (false)",
        ["`Hello W3Schools` does not start with `W3Schools`."],
        'const pattern = /^W3Schools/;\nlet text = "Hello W3Schools";\nlet result = pattern.test(text);',
        "**false**.",
    ),
    ST(
        "dollar-true",
        "$ — end (true)",
        ["**`$`** matches the end of the string."],
        'const pattern = /W3Schools$/;\nlet text = "Hello W3Schools";\nlet result = pattern.test(text);',
        "**true**.",
    ),
    ST(
        "dollar-false",
        "$ — end (false)",
        ["`W3Schools tutorial` does not **end** with `W3Schools`."],
        'const pattern = /W3Schools$/;\nlet text = "W3Schools tutorial";\nlet result = pattern.test(text);',
        "**false**.",
    ),
    ST(
        "word-boundary-start",
        r"\bLO — word boundary at start of LO",
        [
            r"**`\b`** is a **word boundary** (between `\w` and `\W`, or at the string edge).",
            r"`search(/\bLO/)` finds **LOOK**, not the `LO` inside **HELLO**.",
        ],
        'let text = "HELLO, LOOK AT YOU!";\nlet result = text.search(/\\bLO/);',
        "**7** — index of **LOOK** (`HELLO, ` is 7 characters).",
    ),
    ST(
        "word-boundary-end",
        r"LO\b — word boundary at end of LO",
        [
            r"**`LO\b`** wants `LO` at the **end** of a word.",
            "That is the **LO** ending **HELLO** (before the comma).",
        ],
        'let text = "HELLO, LOOK AT YOU!";\nlet result = text.search(/LO\\b/);',
        "**3** — `LO` in **HELLO** starting at index 3.",
    ),
    SM(
        "not-word-boundary",
        r"\B — not a word boundary",
        [
            r"**`\B`** is the opposite of **`\b`**. No Tryit on the table — still run it.",
            "`JavaScript` has no boundary before **Script**; `Hello Script` would.",
        ],
        'let text = "JavaScript";\nlet result = text.match(/\\BScript/);\nlet edge = text.match(/\\bScript/);',
        '`JSON.stringify(result)` is **["Script"]**. `edge` is **null**.',
        extra=[("edge", "JSON.stringify(edge)")],
    ),
    ST(
        "lookahead-empty-tryit",
        "(?=) empty lookahead — Tryit",
        [
            "The Tryit compiles **`W3Schools(?=) Tutorials`** — an **empty** lookahead.",
            "An empty `(?=)` always succeeds, so this is just `W3Schools Tutorials`.",
        ],
        'let text = "W3Schools Tutorials";\nlet pattern = new RegExp("W3Schools(?=) Tutorials");\nlet result = pattern.test(text);',
        "**true** (empty lookahead does not test a following string).",
    ),
    SM(
        "lookahead-filled",
        "(?=...) — subsequent string",
        [
            "**`(?=...)`** is a **lookahead**: the following text must match, but is **not consumed**.",
            '`match` returns **["W3Schools"]**, not the trailing ` Tutorials`.',
        ],
        'let text = "W3Schools Tutorials";\nconst pattern = /W3Schools(?= Tutorials)/;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["W3Schools"]**.',
    ),
    ST(
        "neg-lookahead",
        "(?!...) — not the subsequent string",
        [
            "**`(?!...)`** succeeds only if the following text does **not** match.",
        ],
        'let text = "W3Schools Tutorials";\nlet pattern = /W3Schools(?! Tutorials)/;\nlet result = pattern.test(text);',
        "**false** — the text **is** followed by ` Tutorials`.",
    ),
    ST(
        "lookbehind",
        "(?<=...) — previous string",
        [
            "**`(?<=...)`** is a **lookbehind** (ES2018): previous text must match, not consumed.",
        ],
        'let text = "Hello W3Schools";\nlet pattern = /(?<=Hello )W3Schools/;\nlet result = pattern.test(text);',
        "**true**.",
    ),
    ST(
        "neg-lookbehind",
        "(?<!...) — not the previous string",
        [
            "**`(?<!...)`** succeeds only if the previous text does **not** match.",
        ],
        'let text = "Hello W3Schools";\nlet pattern = /(?<!Hello )W3Schools/;\nlet result = pattern.test(text);',
        "**false** — it **is** preceded by `Hello `.",
    ),
]


# ---------------------------------------------------------------------------
# 16.6 JS RegExp Groups
# ---------------------------------------------------------------------------

GROUPS = [
    SM(
        "capturing-match",
        "match — capturing groups (x)",
        [
            "**`(x)`** captures. `match` without **`g`** puts the full match at **[0]**, then groups.",
            "This is the page’s `text.match` snippet (the Tryits both use `exec`).",
        ],
        'let text = "Alice loves Bob-";\nconst pattern = /(\\w+) loves (\\w+)/;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["Alice loves Bob","Alice","Bob"]**. The hyphen is outside the match.',
    ),
    SM(
        "capturing-exec-dot",
        "exec — capturing groups (Tryit period)",
        [
            "`RegExp.exec(text)` also returns **[full, group1, group2, …]** (or **null**).",
            "This Tryit uses `Alice loves Bob.`",
        ],
        'let text = "Alice loves Bob.";\nconst pattern = /(\\w+) loves (\\w+)/;\nlet result = pattern.exec(text);',
        '`JSON.stringify(result)` is **["Alice loves Bob","Alice","Bob"]**. `result.index` is **0**.',
        extra=[("result.index", "result.index")],
    ),
    SM(
        "capturing-exec-hyphen",
        "exec — capturing groups (Tryit hyphen)",
        [
            "Second Tryit: `Alice loves Bob-`. Same groups; punctuation after **Bob** is not captured.",
        ],
        'let text = "Alice loves Bob-";\nconst pattern = /(\\w+) loves (\\w+)/;\nlet result = pattern.exec(text);',
        '`JSON.stringify(result)` is **["Alice loves Bob","Alice","Bob"]**.',
    ),
    SM(
        "result-array-date",
        r"(\d{4})-(\d{2})-(\d{2}) — result array indices",
        [
            "The page’s date demo: **[0]** whole match, **[1..n]** parenthesis groups.",
        ],
        'const regex = /(\\d{4})-(\\d{2})-(\\d{2})/;\nconst text = "2026-05-21";\nconst result = text.match(regex);',
        '`JSON.stringify(result)` is **["2026-05-21","2026","05","21"]**.',
    ),
    SM(
        "named-groups",
        "(?<name>x) — named capturing groups",
        [
            "**`(?<name>x)`** stores captures on **`match.groups`** (ES2018).",
            "The Tryit prints only `lastName`; this sandbox JSON-prints the groups object too.",
        ],
        'const text = "Name: John Doe";\nconst regex = /(?<firstName>\\w+) (?<lastName>\\w+)/;\nconst result = text.match(regex);\nlet fName = result.groups.firstName;\nlet lName = result.groups.lastName;',
        '`JSON.stringify(result)` is **["John Doe","John","Doe"]**. `groups` is **{"firstName":"John","lastName":"Doe"}**.',
        extra=[
            ("result.groups", "JSON.stringify(result.groups)"),
            ("fName", "fName"),
            ("lName", "lName"),
        ],
    ),
    SM(
        "non-capturing",
        "(?:x) — non-capturing group",
        [
            "**`(?:x)`** groups for quantifiers **without** creating a capture.",
            "`/(?:ha)+/` vs `/(ha)+/` on `hahaha`.",
        ],
        'let text = "hahaha";\nlet result = text.match(/(?:ha)+/);\nlet cap = text.match(/(ha)+/);',
        '`JSON.stringify(result)` is **["hahaha"]** (no group 1). `cap` is **["hahaha","ha"]** (last `ha` is group 1).',
        extra=[("cap", "JSON.stringify(cap)")],
    ),
    SM(
        "group-lookahead",
        "(?=x) — lookahead group",
        [
            "Lookahead is listed as a group type: it **asserts**, it does **not** capture the peek.",
        ],
        'let text = "W3Schools Tutorials";\nlet result = text.match(/W3Schools(?= Tutorials)/);',
        '`JSON.stringify(result)` is **["W3Schools"]**.',
    ),
    SM(
        "group-lookbehind",
        "(?<=x) — lookbehind group",
        [
            "Lookbehind asserts the **previous** text; the match is still only `W3Schools`.",
        ],
        'let text = "Hello W3Schools";\nlet result = text.match(/(?<=Hello )W3Schools/);',
        '`JSON.stringify(result)` is **["W3Schools"]**.',
    ),
    modifier_S(
        "flag-enable",
        "(?i:x) — enable flag in group",
        [
            "**`(?flag:x)`** enables flag(s) for **`x` only**.",
        ],
        'let text = "W3Schools tutorials.";\nconst pattern = /(?i:W3Schools) tutorials/;\nlet result = pattern.test(text);',
        "(?i:W3Schools) tutorials",
        "W3Schools tutorials.",
        "**true**.",
    ),
    modifier_S(
        "flag-enable-false",
        "(?i:x) — enable flag, tail fails",
        [
            "Second Tryit: capital **Tutorials** vs lowercase ` tutorials`.",
        ],
        'let text = "W3Schools Tutorials.";\nconst pattern = /(?i:W3Schools) tutorials/;\nlet result = pattern.test(text);',
        "(?i:W3Schools) tutorials",
        "W3Schools Tutorials.",
        "**false**.",
    ),
    modifier_S(
        "flag-disable",
        "(?-i:x) — disable flag in group",
        [
            "**`(?flag-flag:x)`** can **turn off** a flag inside a group.",
            "No Tryit on the page. Pattern is **`/(?-i:W3Schools) tutorials/i`** — outer **`i`**, group turns **`i` off**.",
        ],
        'let text = "w3schools tutorials";\nconst pattern = /(?-i:W3Schools) tutorials/i;\nlet result = pattern.test(text);',
        "(?-i:W3Schools) tutorials",
        "w3schools tutorials",
        "**false** if modifier groups work — `W3Schools` is case-sensitive inside the group, so `w3schools` fails. "
        "Engines without ES2025 modifiers report **SyntaxError: Invalid group**.",
        flags="i",
    ),
    SM(
        "backreference",
        r"\1 — backreference",
        [
            "Capturing groups can be **replayed** with **`\\1`**, **`\\2`**, …",
            "`(\\w+)\\s+\\1` matches a word, space, and **the same** word again.",
        ],
        'let text = "hello hello";\nlet result = text.match(/(\\w+)\\s+\\1/);\nlet miss = "hello world".match(/(\\w+)\\s+\\1/);',
        '`JSON.stringify(result)` is **["hello hello","hello"]**. `miss` is **null**.',
        extra=[("miss", "JSON.stringify(miss)")],
    ),
]


# ---------------------------------------------------------------------------
# 16.7 JS RegExp Quantifiers
# ---------------------------------------------------------------------------

QUANTIFIERS = [
    SM(
        "plus",
        "x+ — one or more",
        [r"**`+`** means **one or more** of the previous token. `/o+/g` on the Hello/Schools sentence."],
        'let text = "Hellooo World! Hello W3Schools!";\nconst pattern = /o+/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["ooo","o","o","oo"]**.',
    ),
    SM(
        "star",
        "x* — zero or more",
        [r"**`*`** means **zero or more**. `/lo*/g` is an `l` plus extra `o`s (including none)."],
        'let text = "Hellooo World! Hello W3Schools!";\nconst pattern = /lo*/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["l","looo","l","l","lo","l"]**.',
    ),
    SM(
        "question",
        "x? — zero or one",
        ["**`?`** means **zero or one**. `/10?/g` is `1` plus an optional `0`."],
        'let text = "1, 100 or 1000?";\nconst pattern = /10?/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["1","10","10"]**.',
    ),
    SM(
        "exactly-n",
        r"x{n} — exactly n",
        [r"**`{4}`** wants exactly four digits. `100` is skipped; `10000` yields one four-digit slice."],
        'let text = "100, 1000 or 10000?";\nconst pattern = /\\d{4}/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["1000","1000"]**.',
    ),
    SM(
        "n-to-m",
        r"x{n,m} — from n to m",
        [r"**`{3,4}`** is greedy: `10000` contributes **`1000`**, leftover `0`."],
        'let text = "100, 1000 or 10000?";\nconst pattern = /\\d{3,4}/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["100","1000","1000"]**.',
    ),
    SM(
        "n-or-more",
        r"x{n,} — n or more",
        [r"**`{3,}`** takes the longest digit run of length ≥ 3."],
        'let text = "100, 1000 or 10000?";\nconst pattern = /\\d{3,}/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["100","1000","10000"]**.',
    ),
]


# ---------------------------------------------------------------------------
# 16.8 JS RegExp Patterns (full tables, one Example per row)
# ---------------------------------------------------------------------------

PATTERNS: list[dict] = []

for _stem, _flag, _desc, _code, _out in [
    (
        "flag-d",
        "/d",
        "hasIndices — start/end pairs on the match.",
        'let text = "aaaabb";\nconst pattern = /(aa)(bb)/d;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["aabb","aa","bb"]**. `indices` is **[[2,6],[2,4],[4,6]]**.',
    ),
    (
        "flag-g",
        "/g",
        "global — find all.",
        'let text = "Is this all there is?";\nconst pattern = /is/g;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["is","is"]**.',
    ),
    (
        "flag-i",
        "/i",
        "case-insensitive.",
        'let text = "Visit W3Schools";\nconst pattern = /w3schools/i;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["W3Schools"]**.',
    ),
    (
        "flag-m",
        "/m",
        "multiline — `^` / `$` per line.",
        'let text = "\\nIs th\\nis it?";\nlet result = text.match(/^is/m);',
        '`JSON.stringify(result)` is **["is"]**.',
    ),
    (
        "flag-s",
        "/s",
        "dotAll — `.` matches line terminators.",
        'let text = "Line\\nLine.";\nconst pattern = /Line./gs;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["Line\\n","Line."]** .',
    ),
    (
        "flag-u",
        "/u",
        "Unicode code points.",
        'let text = "\\u4DC0";\nconst pattern = /\\u{04DC0}/u;\nlet result = pattern.test(text);',
        "**true**.",
    ),
    (
        "flag-v",
        "/v",
        "Unicode sets / property escapes.",
        'let text = "Hello \\u{1F604}";\nconst pattern = /\\p{Emoji}/v;\nlet result = pattern.test(text);',
        "**true**.",
    ),
    (
        "flag-y",
        "/y",
        "sticky — match only at `lastIndex`.",
        'let text = "abc def ghi";\nconst pattern = /\\w+/y;\npattern.lastIndex = 4;\nlet result = text.match(pattern);',
        '`JSON.stringify(result)` is **["def"]**.',
    ),
]:
    if _flag in ("/u", "/v"):
        PATTERNS.append(
            ST(
                _stem,
                f"{_flag} — {_desc}",
                [f"Flags table row **`{_flag}`**: {_desc}"],
                _code,
                _out,
            )
        )
    else:
        extra = None
        if _flag == "/d":
            extra = [("result.indices", "JSON.stringify(result.indices)")]
        PATTERNS.append(
            SM(
                _stem,
                f"{_flag} — {_desc}",
                [f"Flags table row **`{_flag}`**: {_desc}"],
                _code,
                _out,
                extra=extra,
            )
        )

for _stem, _title, _pat, _sample, _out in [
    ("class-a", "[a]", "[a]", "cat", '**["a"]**'),
    ("class-not-a", "[^a]", "[^a]", "cat", '**["c","t"]**'),
    ("class-abc", "[abc]", "[abc]", "fabric", '**["a","b","c"]**'),
    ("class-not-abc", "[^abc]", "[^abc]", "fabric", '**["f","r","i"]**'),
    ("class-az", "[a-z]", "[a-z]", "A1b", '**["b"]**'),
    ("class-not-az", "[^a-z]", "[^a-z]", "A1b", '**["A","1"]**'),
    ("class-09", "[0-9]", "[0-9]", "A1b", '**["1"]**'),
    ("class-not-09", "[^0-9]", "[^0-9]", "A1b", '**["A","b"]**'),
]:
    PATTERNS.append(
        row_match(
            _stem,
            _title,
            [f"Character-class table row **`{_title}`**. `match` is the array or **null**."],
            _pat,
            _sample,
            "g",
            f"`JSON.stringify(result)` is {_out}.",
        )
    )

_meta_rows = [
    ("meta-or", "a|b", r"a|b", "cat", "g", '**["a"]**'),
    ("meta-dot", ".", r".", "a\nb", "g", '**["a","b"]** — newline skipped'),
    ("meta-w", r"\w", r"\w", GIVE, "g", '**["G","i","v","e","1","0","0"]**'),
    ("meta-nonword", r"\W", r"\W", GIVE, "g", '**[" ","%","!"]**'),
    ("meta-d", r"\d", r"\d", GIVE, "g", '**["1","0","0"]**'),
    ("meta-nondigit", r"\D", r"\D", GIVE, "g", '**["G","i","v","e"," ","%","!"]**'),
    ("meta-s", r"\s", r"\s", IS_ALL, "g", '**[" "," "," "," "]**'),
    ("meta-nonspace", r"\S", r"\S", GIVE, "g", '**["G","i","v","e","1","0","0","%","!"]**'),
    ("meta-bs", r"[\b]", r"[\b]", "a\bb", "g", r'**["\b"]** — backspace, not a word boundary'),
    ("meta-nul", r"\0", r"\0", "a\0b", "g", r'**["\u0000"]**'),
    ("meta-n", r"\n", r"\n", "a\nb", "g", r'**["\n"]**'),
    ("meta-f", r"\f", r"\f", "a\fb", "g", r'**["\f"]**'),
    ("meta-r", r"\r", r"\r", "a\rb", "g", r'**["\r"]**'),
    ("meta-t", r"\t", r"\t", "a\tb", "g", r'**["\t"]**'),
    ("meta-v", r"\v", r"\v", "a\vb", "g", r'**["\u000b"]**'),
    ("meta-p", r"\p{}", r"\p{L}", "Hello 1", "gu", '**["H","e","l","l","o"]** — needs u/v'),
    ("meta-not-prop", r"\P{}", r"\P{L}", "Hello 1", "gu", '**[" ","1"]**'),
    ("meta-oct", r"\ddd", r"\127", VISIT_DOT, "g", '**["W","W"]** (octal 127 = W)'),
    ("meta-x", r"\xhh", r"\x6F", "Hello", "g", '**["o"]** (hex 6F)'),
    ("meta-u", r"\uhhhh", r"\u0057", VISIT_DOT, "g", '**["W","W"]** (U+0057)'),
]
for _stem, _title, _pat, _sample, _flags, _out in _meta_rows:
    PATTERNS.append(
        row_match(
            _stem,
            _title,
            [f"Metacharacter table row **`{_title}`**. Show `match` or **null**."],
            _pat,
            _sample,
            _flags,
            f"`JSON.stringify(result)` is {_out}.",
        )
    )

_assert_rows = [
    ("as-hat", "^", "^W3Schools", "W3Schools tutorial", "", '**["W3Schools"]**'),
    ("as-hat-miss", "^ miss", "^W3Schools", "Hello W3Schools", "", "**null**"),
    ("as-dollar", "$", "W3Schools$", "Hello W3Schools", "", '**["W3Schools"]**'),
    ("as-b", r"\b", r"\bLO", LOOK, "", "**7** via search — see result"),
    ("as-not-b", r"\B", r"\BScript", "JavaScript", "", '**["Script"]**'),
    ("as-la", "(?=...)", r"W3Schools(?= Tutorials)", "W3Schools Tutorials", "", '**["W3Schools"]**'),
    ("as-nla", "(?!...)", r"W3Schools(?! Tutorials)", "W3Schools Tutorials", "", "**null**"),
    ("as-lb", "(?<=...)", r"(?<=Hello )W3Schools", "Hello W3Schools", "", '**["W3Schools"]**'),
    ("as-nlb", "(?<!...)", r"(?<!Hello )W3Schools", "Hello W3Schools", "", "**null**"),
]
# \b uses search in the Tryit; for patterns table use match on LOOK for \bLOOK
_assert_rows[3] = ("as-b", r"\b", r"\bLOOK", LOOK, "", '**["LOOK"]**')

for _stem, _title, _pat, _sample, _flags, _out in _assert_rows:
    PATTERNS.append(
        row_match(
            _stem,
            _title,
            [f"Assertions table row **`{_title}`**. `match` array or **null** (zero-width)."],
            _pat,
            _sample,
            _flags,
            f"`JSON.stringify(result)` is {_out}.",
        )
    )

for _stem, _title, _pat, _sample, _flags, _out in [
    ("q-plus", "x+", r"o+", HELLOOO, "g", '**["ooo","o","o","oo"]**'),
    ("q-star", "x*", r"lo*", HELLOOO, "g", '**["l","looo","l","l","lo","l"]**'),
    ("q-q", "x?", r"10?", "1, 100 or 1000?", "g", '**["1","10","10"]**'),
    ("q-n", "x{n}", r"\d{4}", NUMS, "g", '**["1000","1000"]**'),
    ("q-nm", "x{n,m}", r"\d{3,4}", NUMS, "g", '**["100","1000","1000"]**'),
    ("q-nmore", "x{n,}", r"\d{3,}", NUMS, "g", '**["100","1000","10000"]**'),
]:
    PATTERNS.append(
        row_match(
            _stem,
            _title,
            [f"Quantifier table row **`{_title}`**."],
            _pat,
            _sample,
            _flags,
            f"`JSON.stringify(result)` is {_out}.",
        )
    )


# ---------------------------------------------------------------------------
# 16.9 JS RegExp Objects
# ---------------------------------------------------------------------------

OBJECTS = [
    ST(
        "test",
        "pattern.test(text)",
        [
            "`RegExp.test(string)` returns **true** or **false**.",
            "The Tryit searches for **`e`** in the famous sentence.",
        ],
        'const pattern = /e/;\nlet result = pattern.test("The best things in life are free!");',
        "**true** — there is an `e` in `The`.",
    ),
    ST(
        "test-oneliner",
        "/e/.test(text) — no variable",
        [
            "You can call **`test`** on a regex **literal**.",
        ],
        'let result = /e/.test("The best things in life are free!");',
        "**true**.",
    ),
    S(
        "exec",
        "regex.exec(text)",
        [
            "`exec` returns a match **array** (or **null**). `[0]` is the match; **`index`** / **`input`** hang off the array.",
            "`JSON.stringify` drops `index` and `input` — print them separately.",
        ],
        'const result = /e/.exec("The best things in life are free!");',
        [
            ("JSON.stringify(result)", "JSON.stringify(result)"),
            ("result[0]", "result[0]"),
            ("result.index", "result.index"),
            ("result.input", "result.input"),
        ],
        '`JSON.stringify(result)` is **["e"]**. `result[0]` is **"e"**, `index` is **2**, `input` is the full sentence.',
    ),
    SM(
        "exec-null",
        "exec — no match is null",
        [
            "The page says “empty (null) object”. In JS it is **`null`**, not `{}`.",
        ],
        'let result = /z/.exec("The best things in life are free!");',
        "**null**.",
    ),
    S(
        "literal-vs-constructor",
        "Literal /ab+c/i vs new RegExp",
        [
            "**`/pattern/flags`** is a regex literal. **`new RegExp(string, flags)`** is the constructor.",
            "In a constructor **string**, backslashes are doubled: `new RegExp(\"\\\\d+\")` not `\"\\d+\"`.",
        ],
        'const lit = /ab+c/i;\nconst ctor = new RegExp("ab+c", "i");\nconst goodDigits = new RegExp("\\\\d+");\nconst badDigits = new RegExp("\\d+");',
        [
            ("String(lit)", "String(lit)"),
            ("String(ctor)", "String(ctor)"),
            ("String(goodDigits)", "String(goodDigits)"),
            ("String(badDigits)", "String(badDigits)"),
            ("goodDigits.test('12')", "goodDigits.test('12')"),
            ("badDigits.test('12')", "badDigits.test('12')"),
        ],
        '`lit` and `ctor` both print **`/ab+c/i`**. `goodDigits` is **`/\\d+/`** and **`test("12")` is true**. '
        '`badDigits` is **`/d+/`** (the JS string `"\\d+"` is just `d+`) so **`test("12")` is false**.',
    ),
    S(
        "lastIndex-g",
        "lastIndex mutation with /g and exec",
        [
            "With **`/g`**, **`exec`** (and **`test`**) start at **`lastIndex`** and **write it back**.",
            "A **null** match **resets `lastIndex` to 0**, so the next call starts over.",
        ],
        'const pattern = /is/g;\nconst text = "Is this all there is?";\nconst a = pattern.exec(text);\nconst li1 = pattern.lastIndex;\nconst b = pattern.exec(text);\nconst li2 = pattern.lastIndex;\nconst c = pattern.exec(text);\nconst li3 = pattern.lastIndex;',
        [
            ("JSON.stringify(a)", "JSON.stringify(a)"),
            ("a.index", "a.index"),
            ("li1", "li1"),
            ("JSON.stringify(b)", "JSON.stringify(b)"),
            ("b.index", "b.index"),
            ("li2", "li2"),
            ("JSON.stringify(c)", "JSON.stringify(c)"),
            ("li3", "li3"),
        ],
        'First `exec` is **["is"]** at index **5** (`this`), `lastIndex` **7**. '
        "Second is **[\"is\"]** at **18**, `lastIndex` **20**. Third is **null**, `lastIndex` **0**.",
    ),
    S(
        "escape",
        "RegExp.escape('[*]') then replace",
        [
            "**`RegExp.escape(text)`** (ES2025) backslash-escapes regex syntax so the text is **literal**.",
            "Then `new RegExp(safe)` can match `[*]` as characters, not a character class.",
        ],
        'const oldText = "[*] is a web school.";\nlet safe;\nlet result;\ntry {\n  safe = RegExp.escape("[*]");\n  const regex = new RegExp(safe);\n  result = oldText.replace(regex, "W3Schools");\n} catch (e) {\n  safe = e.name + ": " + e.message;\n  result = oldText;\n}',
        [
            ("safe", "JSON.stringify(safe)"),
            ("result", "result"),
        ],
        'When `RegExp.escape` exists: `safe` is **`"\\\\[\\\\*\\\\]"`** (JSON) and `result` is '
        '**"W3Schools is a web school."** Node 22 has no `RegExp.escape` — then `safe` is the error string.',
    ),
]


# ---------------------------------------------------------------------------
# 16.10 JS RegExp Methods (every reference-table row)
# ---------------------------------------------------------------------------

METHODS: list[dict] = [
    S(
        "compile",
        "compile() — deprecated",
        [
            "**Deprecated.** `compile(pattern, flags)` mutates the same RegExp. **Do not use it** in new code.",
        ],
        'const pattern = /abc/g;\npattern.compile("def", "i");',
        [
            ("pattern.source", "pattern.source"),
            ("pattern.flags", "pattern.flags"),
            ("String(pattern)", "String(pattern)"),
        ],
        'After `compile("def", "i")`, `source` is **"def"**, `flags` is **"i"**, `String(pattern)` is **`/def/i`**. Still **deprecated**.',
    ),
    S(
        "constructor",
        "constructor",
        [
            "Instance **`constructor`** is the function that created the prototype: **`RegExp`**.",
        ],
        "const pattern = /W3Schools/gi;\nconst result = pattern.constructor;",
        [
            ("String(pattern.constructor)", "String(pattern.constructor)"),
            ("pattern.constructor === RegExp", "pattern.constructor === RegExp"),
        ],
        '`String(pattern.constructor)` is **function RegExp() { [native code] }**. `=== RegExp` is **true**.',
    ),
    ST(
        "dotAll",
        "dotAll",
        ["**`dotAll`** is **true** if **`s`** is set."],
        "const pattern = /W3Schools/s;\nlet result = pattern.dotAll;",
        "**true**.",
    ),
    S(
        "escape",
        "escape() — RegExp.escape",
        [
            "Static **`RegExp.escape`** (ES2025) returns a string safe to embed in a pattern.",
        ],
        'let result;\ntry {\n  result = RegExp.escape("[*]");\n} catch (e) {\n  result = e.name + ": " + e.message;\n}',
        [("result", "JSON.stringify(result)")],
        'With ES2025: JSON **`"\\\\[\\\\*\\\\]"`**. Otherwise a **TypeError** / missing-function message.',
    ),
    S(
        "exec",
        "exec()",
        [
            "`exec` returns a result array for **one** match, or **null**.",
            "With **`/g`**, it advances **`lastIndex`** (see lastIndex row).",
        ],
        'const result = /e/.exec("The best things in life are free!");',
        [
            ("JSON.stringify(result)", "JSON.stringify(result)"),
            ("result.index", "result.index"),
        ],
        '`JSON.stringify(result)` is **["e"]**. `index` is **2**.',
    ),
    ST(
        "flags",
        "flags",
        ["**`flags`** is the modifier letters actually set, in a standard order (e.g. `gim`)."],
        "const pattern = /W3Schools/gim;\nlet result = pattern.flags;",
        '**"gim"** (`g`, `i`, `m` alphabetically in the spec order `dgimsuvy`).',
    ),
    ST(
        "global",
        "global",
        ["**`global`** is **true** if **`g`** is set."],
        "const pattern = /W3Schools/g;\nlet result = pattern.global;",
        "**true**.",
    ),
    ST(
        "hasIndices",
        "hasIndices",
        ["**`hasIndices`** is **true** if **`d`** is set."],
        "const pattern = /W3Schools/d;\nlet result = pattern.hasIndices;",
        "**true**.",
    ),
    ST(
        "ignoreCase",
        "ignoreCase",
        ["**`ignoreCase`** is **true** if **`i`** is set."],
        "const pattern = /W3Schools/i;\nlet result = pattern.ignoreCase;",
        "**true**.",
    ),
    S(
        "lastIndex",
        "lastIndex",
        [
            "**`lastIndex`** is where the next **`exec` / `test`** starts when **`g` or `y`** is set.",
            "A failed match **resets it to 0**.",
        ],
        'const pattern = /is/g;\nconst text = "Is this all there is?";\nconst a = pattern.exec(text);\nconst li1 = pattern.lastIndex;\nconst b = pattern.exec(text);\nconst li2 = pattern.lastIndex;\nconst c = pattern.exec(text);\nconst li3 = pattern.lastIndex;',
        [
            ("a.index", "a.index"),
            ("li1", "li1"),
            ("b.index", "b.index"),
            ("li2", "li2"),
            ("JSON.stringify(c)", "JSON.stringify(c)"),
            ("li3", "li3"),
        ],
        "Match at **5** → `lastIndex` **7**; match at **18** → **20**; then **null** and **`lastIndex` 0**.",
    ),
    ST(
        "multiline",
        "multiline",
        ["**`multiline`** is **true** if **`m`** is set."],
        "const pattern = /W3Schools/m;\nlet result = pattern.multiline;",
        "**true**.",
    ),
    ST(
        "source",
        "source",
        ["**`source`** is the pattern text **without** slashes or flags."],
        "const pattern = /W3Schools/gi;\nlet result = pattern.source;",
        '**"W3Schools"** (not `"/W3Schools/gi"`).',
    ),
    ST(
        "sticky",
        "sticky",
        ["**`sticky`** is **true** if **`y`** is set."],
        "const pattern = /W3Schools/y;\nlet result = pattern.sticky;",
        "**true**.",
    ),
    ST(
        "test",
        "test()",
        [
            "`test` returns **true** or **false**.",
            "With **`/g`**, **`test` also mutates `lastIndex`** — easy to get alternating true/false.",
        ],
        'const pattern = /e/;\nlet result = pattern.test("The best things in life are free!");',
        "**true**.",
    ),
    ST(
        "toString",
        "toString()",
        ["**`toString()`** is the literal form including slashes and flags."],
        "const pattern = /W3Schools/gim;\nlet result = pattern.toString();",
        '**"/W3Schools/gim"**.',
    ),
    ST(
        "unicode",
        "unicode",
        ["**`unicode`** is **true** if **`u`** is set."],
        "const pattern = /\\u{04DC0}/u;\nlet result = pattern.unicode;",
        "**true**.",
    ),
    ST(
        "unicodeSets",
        "unicodeSets",
        ["**`unicodeSets`** is **true** if **`v`** is set."],
        "const pattern = /\\p{Emoji}/v;\nlet result = pattern.unicodeSets;",
        "**true**.",
    ),
    SM(
        "match",
        "String.match(regexp)",
        [
            "Without **`g`**: one match array **with groups**. With **`g`**: all full matches, **no groups**.",
            "No match → **null** (not `[]`).",
        ],
        'const text = "a1 a2";\nconst result = text.match(/a(\\d)/);\nconst all = text.match(/a(\\d)/g);\nconst miss = text.match(/z/);',
        '`JSON.stringify(result)` is **["a1","1"]**. `all` is **["a1","a2"]** (groups dropped). `miss` is **null**.',
        extra=[("all", "JSON.stringify(all)"), ("miss", "JSON.stringify(miss)")],
    ),
    S(
        "matchAll",
        "String.matchAll(regexp)",
        [
            "`matchAll` returns an **iterator** of match arrays **with groups**. The regex **must** be **`g`**.",
        ],
        'const text = "a1 a2";\nconst result = [...text.matchAll(/a(\\d)/g)].map((m) => [...m]);',
        [("result", "JSON.stringify(result)")],
        '`JSON.stringify(result)` is **[["a1","1"],["a2","2"]]**.',
    ),
    ST(
        "replace",
        "String.replace(regexp, s)",
        [
            "`replace` with a regex replaces the **first** match unless **`g`** is set.",
            "It returns a **new** string.",
        ],
        'let text = "Please visit Microsoft and Microsoft!";\nlet result = text.replace(/Microsoft/, "W3Schools");',
        '**"Please visit W3Schools and Microsoft!"** (only the first).',
    ),
    ST(
        "replaceAll",
        "String.replaceAll(regexp, s)",
        [
            "`replaceAll` with a regex **requires `g`**. It replaces **every** match.",
        ],
        'let text = "a1b2";\nlet result = text.replaceAll(/\\d/g, "*");',
        '**"a*b*"**.',
    ),
    S(
        "search",
        "String.search(regexp)",
        [
            "`search` returns the **index** of the first match, or **-1**.",
            "It does **not** use `lastIndex` the way `exec` does.",
        ],
        'const text = "Visit W3Schools!";\nconst hit = text.search(/W3Schools/);\nconst miss = text.search(/z/);',
        [("hit", "hit"), ("miss", "miss")],
        "`hit` is **6**. `miss` is **-1**.",
    ),
    SM(
        "split",
        "String.split(regexp)",
        [
            "`split(regex)` cuts the string on each match and returns an **array of pieces**.",
        ],
        'let result = "a,b;c".split(/[,;]/);',
        '`JSON.stringify(result)` is **["a","b","c"]**.',
    ),
    S(
        "exec-vs-match-g",
        "exec vs match with /g",
        [
            "Named construct: **`match` + `g`** vs **`exec` + `g`**.",
            "`match` returns all full matches and **resets** `lastIndex`. `exec` returns **one** match **with groups** and **moves** `lastIndex`.",
        ],
        'const text = "a1 a2";\nconst pattern = /a(\\d)/g;\nconst viaMatch = text.match(pattern);\nconst liAfterMatch = pattern.lastIndex;\nconst viaExec = pattern.exec(text);\nconst liAfterExec = pattern.lastIndex;',
        [
            ("viaMatch", "JSON.stringify(viaMatch)"),
            ("liAfterMatch", "liAfterMatch"),
            ("viaExec", "JSON.stringify(viaExec)"),
            ("liAfterExec", "liAfterExec"),
        ],
        '`viaMatch` is **["a1","a2"]**, `lastIndex` **0**. Then `exec` is **["a1","1"]**, `lastIndex` **2**.',
    ),
]


def run_all(only: list[str] | None = None) -> None:
    mdn_re = (
        "MDN: Regular expressions",
        "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions",
    )
    mdn_obj = (
        "MDN: RegExp",
        "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp",
    )
    sections = [
        (
            "js-regexp",
            "JS RegExp",
            LANDING,
            "A regular expression is a search pattern. JavaScript’s RegExp object is used with string methods (search, match, replace) and with RegExp.test / exec. The literal form is /pattern/flags. This landing page is a tour: case-insensitive search, match/replace, alternation with |, the g and i flags, \\d and \\w, the ? quantifier, ^ and $, and [0-9]. Later pages expand each topic. match arrays are JSON-stringified so commas inside matches stay visible.",
            [
                "Syntax is **`/pattern/flags`**. **`i`** = ignore case, **`g`** = find all.",
                "`search` → **index**. `match` → **array or null**. `replace` → **new string**.",
                "**`|`** is alternation (OR).",
                r"**`\d`** digits, **`\w`** word chars `[A-Za-z0-9_]`.",
                "**`?`** is zero-or-one of the previous token (`10?` is not “the number ten”).",
                "**`^` / `$`** are string ends. **`[0-9]`** is a character class.",
                "`JSON.stringify` on a match array prints captures only — not `index` / `input`.",
            ],
            [
                ("What is a regex literal?", ["**`/pattern/flags`** — slashes around the pattern, then flags like **`i`** or **`g`**."]),
                ("What does `search` return?", ["The **index** of the first match, or **-1**. `\"Visit W3Schools!\".search(/w3Schools/i)` is **6**."]),
                ("What does `match` return on a miss?", ["**`null`**, not an empty array. `/W3schools/` on `Visit W3Schools` is **null** (case)."]),
                ("Does `replace` change the original string?", ["**No.** It returns a **new** string."]),
                ("What does `|` mean?", ["**Alternation (OR)**. `/red|green|blue/g` → **[\"red\",\"green\",\"blue\"]**."]),
                ("Does `/is/g` match `Is`?", ["**No** — **`g`** is not **`i`**. Result **[\"is\",\"is\"]**."]),
                (r"What is `\w`?", ["A word character: **letter, digit, or `_`**."]),
                ("What does `10?` match in `1, 100 or 1000?`?", ["**[\"1\",\"10\",\"10\"]** — `1` plus an optional `0`."]),
                ("When is `^W3Schools` true?", ["When the string **starts** with `W3Schools`. `Hello W3Schools` is **false**."]),
                ("When is `W3Schools$` true?", ["When the string **ends** with `W3Schools`."]),
                ("Why JSON.stringify match arrays?", ["So you see **[\"1\",\"0\",\"0\"]** instead of `1,0,0`, and **null** stays **null**."]),
            ],
            "RegExp is a pattern object used with search, match, replace, test, and exec. Remember /g vs /i, JSON-stringify match arrays, and that ^ $ | [] and the common metacharacters show up on later pages in full.",
            [
                ("JS RegExp (W3Schools)", "https://www.w3schools.com/js/js_regexp.asp"),
                mdn_re,
            ],
        ),
        (
            "js-regexp-flags",
            "JS RegExp Flags",
            FLAGS,
            "Flags sit after the closing slash and change how a pattern runs. /g finds all matches. /i ignores case. /d adds result.indices. /s (dotAll) lets the dot match newlines. /m makes ^ and $ line-aware. /y (sticky) matches only at lastIndex. /u and /v enable Unicode (v adds set notation and \\p{}). Group modifiers (?i:…) apply flags to part of a pattern (ES2025). Each flag also has a boolean property (global, ignoreCase, …).",
            [
                "**`/g`** find all. **`/i`** ignore case. **`/m`** `^`$` per line. **`/s`** dot matches newline.",
                "**`/y`** sticky at **`lastIndex`**. Without **`y`**, `String.match` ignores `lastIndex`.",
                "**`/d`** adds **`indices`**. **`/u`** Unicode code points. **`/v`** Unicode sets.",
                r"Without **`u`/`v`**, `/\p{Emoji}/` is the source **`p{Emoji}`** and `test` is **false**.",
                r"`/\u{04DC0}/` **without** `/u` is **true** in this V8 (the page said false).",
                "**`(?i:…)`** is a group modifier (ES2025). Properties: `global`, `dotAll`, `unicodeSets`, …",
            ],
            [
                ("What does `/g` change about `match`?", ["It returns **all** matches as strings. `/is/g` on the sample is **[\"is\",\"is\"]**."]),
                ("What does `/d` add?", ["**`result.indices`**: `[start, end)` for the match and each group. Here **[[2,6],[2,4],[4,6]]**."]),
                ("What does `/s` do to `.`?", ["`.` can match **newlines**. `/Line./gs` → **[\"Line\\n\",\"Line.\"]**."]),
                ("What does `/m` change?", ["**`^` and `$`** match at **line** starts/ends too. `/^is/m` matches `is it?`."]),
                ("Does sticky `/y` use `lastIndex`?", ["**Yes.** `lastIndex = 4` + `/\\w+/y` → **[\"def\"]**, then `lastIndex` **7**."]),
                ("Without `/y`, does `match` use `lastIndex`?", ["**No.** Same `lastIndex = 4` still matches **[\"abc\"]**."]),
                (r"Does `/\u{04DC0}/` without `u` fail here?", ["**No** — this V8 still matches the hexagram (**true**). The page’s **false** is not what this engine did."]),
                (r"What is `/\p{Emoji}/` without `v`?", ["Source **`p{Emoji}`**. `test(\"Hello 😄\")` is **false**."]),
                ("Does `(?i:W3Schools) tutorials` match `W3Schools Tutorials.`?", ["**No.** Only the group is case-insensitive. The tail ` tutorials` is not."]),
                ("Which flags work in `(?flags:…)`?", ["**`i`**, **`m`**, and **`s`** only."]),
                ("How do you read flags without matching?", ["Boolean properties: **`global`**, **`ignoreCase`**, **`dotAll`**, **`sticky`**, **`unicode`**, **`unicodeSets`**, **`hasIndices`**, **`multiline`**."]),
                ("Is `/v` the same as `/u`?", ["**`v`** is an **upgrade** to **`u`** (sets, `\\p{}` on strings). `unicodeSets` is the property."]),
            ],
            "Pick flags for the job: g for all matches, i for case, m for line anchors, s for dot-newline, y for sticky lastIndex, d for indices, u/v for Unicode. Read them back with the boolean properties. Group modifiers scope i/m/s to part of a pattern.",
            [
                ("JS RegExp Flags (W3Schools)", "https://www.w3schools.com/js/js_regexp_flags.asp"),
                (
                    "MDN: RegExp flags",
                    "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags",
                ),
                mdn_obj,
            ],
        ),
        (
            "js-regexp-classes",
            "JS RegExp Classes",
            CLASSES,
            "A character class is a set in square brackets. [a] is one character, [abc] any of those letters, [a-z] a range, [0-9] digits. A leading ^ inside the brackets negates the set. Tryits on this page use [HW], [A-Z], [1234], and [1-4]; every table row is also an Example that match()es a sample string (array or null).",
            [
                "**`[abc]`** any listed character. **`[a-z]` / `[0-9]`** ranges.",
                "**`[^…]`** means **not** those characters.",
                "**`[1234]`** and **`[1-4]`** match the same digits on `123456789`.",
                "`match` with **`g`** returns every matching **character**. Miss → **null**.",
            ],
            [
                ("What does `[HW]` match in `Hello World!`?", ["**[\"H\",\"W\"]**."]),
                ("What does `[A-Z]` match in `This is W3Schools`?", ["**[\"T\",\"W\",\"S\"]**."]),
                ("Is `[1234]` the same as `[1-4]` here?", ["**Yes** on `123456789` — both **[\"1\",\"2\",\"3\",\"4\"]**."]),
                ("What is `[^a]` on `cat`?", ["**[\"c\",\"t\"]**."]),
                ("What is `[a-z]` on `A1b`?", ["**[\"b\"]** only."]),
                ("What is `[^a-z]` on `A1b`?", ["**[\"A\",\"1\"]**."]),
                ("What is `[0-9]` on `A1b`?", ["**[\"1\"]**."]),
                ("What is `[^0-9]` on `A1b`?", ["**[\"A\",\"b\"]**."]),
                ("Does `[a]` match `XYZ`?", ["**null** — no `a`."]),
                ("Does a class match a whole word?", ["**No.** Each match is **one character** unless you add a quantifier."]),
            ],
            "Square brackets build a set or a range. ^ inside the brackets negates. Ranges like [0-9] and lists like [1234] can describe the same characters. Always JSON-stringify the match array (or null).",
            [
                ("JS RegExp Character Classes (W3Schools)", "https://www.w3schools.com/js/js_regexp_characters.asp"),
                (
                    "MDN: Character classes",
                    "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes",
                ),
            ],
        ),
        (
            "js-regexp-metachars",
            "JS RegExp Metachars",
            METACHARS,
            r"Metacharacters are tokens with special meaning. \d \D \w \W \s \S pair as a class and its complement. \xhh and \uhhhh pick characters by hex; \ddd is a legacy octal form (\127 is W). The Tryits cover \d \D \w \W \s, a hex replace, and \u0057. Table rows without a Tryit (\S, \ddd) still each get an Example.",
            [
                r"**`\d`/`\D`** digits vs not. **`\w`/`\W`** word vs not (`[A-Za-z0-9_]`).",
                r"**`\s`/`\S`** whitespace vs not. JSON the `\s` array or you will see ` , , , `.",
                r"**`\x6F`** is **`o`**. **`\u0057`** is **W**. **`\127`** octal is also **W**.",
                "Prefer hex/Unicode escapes over octal in new patterns.",
            ],
            [
                (r"What does `\d` match in `Give 100%!`?", ["**[\"1\",\"0\",\"0\"]**."]),
                (r"What does `\D` match there?", ["**[\"G\",\"i\",\"v\",\"e\",\" \",\"%\",\"!\"]**."]),
                (r"What does `\w` include?", ["Letters, digits, and **`_`**. Not space, `%`, `!`."]),
                (r"What does `\W` match in that string?", ["**[\" \",\"%\",\"!\"]**."]),
                (r"How many `\s` hits in `Is this all there is?`?", ["**Four** spaces: **[\" \",\" \",\" \",\" \"]**."]),
                (r"What does `\S` match in `Give 100%!`?", ["Everything except the space: letters, digits, `%`, `!`."]),
                (r"What does `\x6F` replace in the Hello/World sentence?", ["Each **`o`** → `*`: **Visit W3Sch**ls. Hell* W*rld!**"]),
                (r"What is `\u0057`?", ["**W**. Two hits in the Visit/World sentence."]),
                (r"What is `\127`?", ["Octal for **W**. Same two hits. Legacy — prefer `\\u0057`."]),
            ],
            r"Use \d \w \s and their uppercase complements for common sets. Hex (\xhh) and Unicode (\uhhhh) name exact characters. Octal \ddd still works without the u flag but is a museum piece. JSON-stringify whitespace matches.",
            [
                ("JS RegExp Meta Characters (W3Schools)", "https://www.w3schools.com/js/js_regexp_meta_characters.asp"),
                (
                    "MDN: Character classes (including \\d \\w \\s)",
                    "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes",
                ),
            ],
        ),
        (
            "js-regexp-assertions",
            "JS RegExp Assertions",
            ASSERTIONS,
            "Assertions are zero-width: they check a position or a neighbor without consuming it. ^ and $ are string (or line) ends. \\b / \\B are word boundaries. Lookahead (?=) / (?!) and lookbehind (?<=) / (?<!) (ES2018) test the subsequent or previous text. The W3Schools lookahead Tryit uses an empty (?=) which always succeeds; a filled (?= Tutorials) is the real table meaning.",
            [
                "**`^` / `$`** start / end of string (or line with **`m`**).",
                r"**`\b`** word edge; **`\B`** not a word edge (`Script` inside `JavaScript`).",
                "**`(?=…)` / `(?!…)`** lookahead. **`(?<=…)` / `(?<!…)`** lookbehind.",
                "Lookarounds do **not** appear in the match array — only the consumed text does.",
                "The Tryit’s **`(?=)`** is empty (always true). Use a filled lookahead to test a following string.",
            ],
            [
                ("Does `^W3Schools` match `Hello W3Schools`?", ["**false**."]),
                ("Does `W3Schools$` match `Hello W3Schools`?", ["**true**."]),
                (r"Where is `\bLO` in `HELLO, LOOK AT YOU!`?", ["Index **7** — **LOOK**, not the `LO` in HELLO."]),
                (r"Where is `LO\b`?", ["Index **3** — the `LO` ending **HELLO**."]),
                (r"Does `\bScript` match `JavaScript`?", ["**null**. **`\\BScript`** matches **[\"Script\"]**."]),
                ("What does the Tryit `W3Schools(?=) Tutorials` test?", ["An **empty** lookahead. **true**, but it does not check a following word."]),
                ("What does `W3Schools(?= Tutorials)` match?", ["**[\"W3Schools\"]** — lookahead is not consumed."]),
                ("What is `W3Schools(?! Tutorials)` on that string?", ["**false** / **null** — it **is** followed by ` Tutorials`."]),
                ("What is `(?<=Hello )W3Schools` on `Hello W3Schools`?", ["**true** / **[\"W3Schools\"]**."]),
                ("What is `(?<!Hello )W3Schools` on that string?", ["**false** / **null**."]),
            ],
            "Assertions check a place in the string. Anchors (^ $) and word boundaries (\\b \\B) are positions. Lookaheads and lookbehinds inspect neighbors without eating them. Do not copy the empty (?=) Tryit when you meant to require a following word.",
            [
                ("JS RegExp Assertions (W3Schools)", "https://www.w3schools.com/js/js_regexp_assertions.asp"),
                (
                    "MDN: Assertions",
                    "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions",
                ),
            ],
        ),
        (
            "js-regexp-groups",
            "JS RegExp Groups",
            GROUPS,
            "Groups treat several tokens as one unit. (x) captures into the match array (index 0 = full match). (?<name>x) also fills match.groups. (?:x) groups without capturing. Lookahead/lookbehind are grouped assertions. (?i:x) / (?-i:x) are ES2025 group flag modifiers. Backreferences (\\1) replay a capture. match and exec both return the same shape without /g; JSON.stringify hides index/input.",
            [
                "**`(x)`** capture. **`(?:x)`** group only. **`(?<name>x)`** named (`.groups`).",
                "`match` / `exec` without **`g`**: `[full, cap1, cap2, …]`.",
                "**`(?=x)` / `(?<=x)`** assert; they do not add extra captures of the peek.",
                "**`(?i:x)`** enables **`i`** in the group. **`(?-i:x)`** can disable it.",
                r"**`\1`** is a backreference to capture 1.",
            ],
            [
                ("Where is the full match in the result array?", ["**Index 0**. Groups follow at **1, 2, …**."]),
                ("What does `/(\\w+) loves (\\w+)/` capture in `Alice loves Bob-`?", ["**[\"Alice loves Bob\",\"Alice\",\"Bob\"]**."]),
                ("Does `exec` differ from `match` without `/g`?", ["Same captures. `exec` is a **RegExp** method; `match` is a **string** method."]),
                ("How do you read named groups?", ["**`match.groups.firstName`** — here **John** and **Doe**."]),
                ("Why use `(?:ha)+`?", ["Repeat **`ha`** without a capture. Result **[\"hahaha\"]**, not an extra **`ha`** group."]),
                ("Does lookahead add a group?", ["**No.** `/W3Schools(?= Tutorials)/` → **[\"W3Schools\"]**."]),
                ("Does `(?i:W3Schools) tutorials` match `W3Schools Tutorials.`?", ["**false** — ` tutorials` stays case-sensitive."]),
                ("What does `(?-i:W3Schools)` do inside `/i`?", ["Turns **case-sensitivity back on** for that group (ES2025)."]),
                (r"What does `(\w+)\s+\1` match?", ["A word repeated: **[\"hello hello\",\"hello\"]**. `hello world` is **null**."]),
                ("Which flags are legal in group modifiers?", ["**`i`**, **`m`**, **`s`**."]),
            ],
            "Use (x) to extract, (?:x) to structure, (?<name>x) to label, lookaround to assert, and \\1 to repeat a capture. match/exec share the [full, groups…] shape without /g. Inline (?i:…) is ES2025.",
            [
                ("JS RegExp Groups (W3Schools)", "https://www.w3schools.com/js/js_regexp_groups.asp"),
                (
                    "MDN: Groups and backreferences",
                    "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences",
                ),
            ],
        ),
        (
            "js-regexp-quantifiers",
            "JS RegExp Quantifiers",
            QUANTIFIERS,
            "Quantifiers say how many times the previous token may appear. + is one or more, * zero or more, ? zero or one. {n} is exactly n, {n,m} a range, {n,} n or more. They are greedy: {3,4} on 10000 takes four digits. Each table row has a Tryit and is its own Example.",
            [
                "**`+`** ≥1. **`*`** ≥0. **`?`** 0 or 1.",
                "**`{n}`** exact. **`{n,m}`** inclusive range. **`{n,}`** at least n.",
                "Quantifiers are **greedy** (take the longest match that still allows success).",
                "`10?` is `1` plus optional `0`, not the number ten.",
            ],
            [
                ("What is `/o+/g` on the Hello/Schools sentence?", ["**[\"ooo\",\"o\",\"o\",\"oo\"]**."]),
                ("What is `/lo*/g` there?", ["**[\"l\",\"looo\",\"l\",\"l\",\"lo\",\"l\"]**."]),
                ("What is `/10?/g` on `1, 100 or 1000?`?", ["**[\"1\",\"10\",\"10\"]**."]),
                (r"What is `/\d{4}/g` on `100, 1000 or 10000?`?", ["**[\"1000\",\"1000\"]** — `100` is too short."]),
                (r"What is `/\d{3,4}/g` on that string?", ["**[\"100\",\"1000\",\"1000\"]** — greedy four on `10000`."]),
                (r"What is `/\d{3,}/g`?", ["**[\"100\",\"1000\",\"10000\"]**."]),
                ("Is `*` allowed to match nothing?", ["**Yes.** `lo*` can be a lone `l`."]),
                ("Does `{3,4}` prefer 3 or 4?", ["**4** if possible (greedy)."]),
                ("Does a quantifier apply to a whole group?", ["Only if you **group** first: `(ha)+` vs `ha+` (`h` then extra `a`s)."]),
            ],
            "Attach +, *, ?, {n}, {n,m}, or {n,} to the token or group you want to count. They are greedy. JSON-stringify the global match array so runs of digits stay grouped as the engine found them.",
            [
                ("JS RegExp Quantifiers (W3Schools)", "https://www.w3schools.com/js/js_regexp_quantifiers.asp"),
                (
                    "MDN: Quantifiers",
                    "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Quantifiers",
                ),
            ],
        ),
        (
            "js-regexp-patterns",
            "JS RegExp Patterns",
            PATTERNS,
            "This page is the full pattern catalog (revised July 2025): flags, character classes, metacharacters, assertions, and quantifiers. There are no Tryits. Every table row is an Example that runs the token against a sample string and JSON-stringifies match (array or null). Flags are demonstrated with the same samples as the flags chapter. Metacharacters include the wildcard dot, whitespace escapes, Unicode properties (\\p{} / \\P{} with u), octal/hex/Unicode numbers, and [\\b] for backspace (not a word boundary).",
            [
                "No Tryits — **one Example per table row** across flags, classes, metacharacters, assertions, quantifiers.",
                r"**`.`** skips newlines unless **`s`**. **`[\b]`** is **backspace**; **`\b`** outside a class is a **word boundary**.",
                r"**`\p{L}` / `\P{L}`** need **`u` or `v`**. **`\0` `\n` `\t`** etc. match those controls.",
                "Assertions still `match()`: hit → array of the consumed text (often the word), miss → **null**.",
            ],
            [
                ("Does this page have Tryits?", ["**No.** Each **table row** is still an Example."]),
                (r"What does `.` match in `a\\nb` with `/g`?", ["**[\"a\",\"b\"]** — not the newline."]),
                (r"What is `[\\b]` vs `\\b`?", ["**`[\\b]`** backspace character. **`\\b`** word boundary."]),
                (r"What does `\\p{L}` need?", ["The **`u`** or **`v`** flag. On `Hello 1` → **[\"H\",\"e\",\"l\",\"l\",\"o\"]**."]),
                (r"What is `\\127`?", ["Octal **W**. **[\"W\",\"W\"]** in the Visit/World sentence."]),
                ("What is `^W3Schools` on `Hello W3Schools`?", ["**null**."]),
                ("What is `(?= Tutorials)` on `W3Schools Tutorials`?", ["**[\"W3Schools\"]** (lookahead not consumed). `(?! Tutorials)` → **null**."]),
                (r"What is `\d{3,}` on the 100/1000/10000 sample?", ["**[\"100\",\"1000\",\"10000\"]**."]),
                ("Which flag lets `.` match a newline?", ["**`s`** (dotAll)."]),
                ("Which flag makes `^` per line?", ["**`m`**."]),
            ],
            "Treat this page as a catalog: run each token, stringify the match, and remember that lookarounds and anchors are zero-width (match text is only what was consumed). Unicode properties and the v flag need a Unicode mode. [\\b] is not \\b.",
            [
                ("JS RegExp Patterns (W3Schools)", "https://www.w3schools.com/js/js_regexp_patterns.asp"),
                mdn_re,
                mdn_obj,
            ],
        ),
        (
            "js-regexp-objects",
            "JS RegExp Objects",
            OBJECTS,
            "RegExp is an object. test returns a boolean. exec returns a match array or null (not {}). You can write a literal /e/ or new RegExp(\"e\"). Constructor strings eat backslashes, so \\\\d is required to get \\d. lastIndex moves on each exec/test when g or y is set, and a failed match resets it to 0. RegExp.escape (ES2025) quotes syntax characters so a user string can be matched literally.",
            [
                "**`test`** → boolean. **`exec`** → array or **`null`**.",
                "Literal **`/pattern/flags`** vs **`new RegExp(string, flags)`** (double backslashes).",
                "With **`/g`**, **`exec`/`test` mutate `lastIndex`**. **null** resets it to **0**.",
                "**`RegExp.escape`** (ES2025) makes `[*]` a literal pattern. Node 22 may not have it; Chromium 136+ does.",
            ],
            [
                ("What does `/e/.test(the free sentence)` return?", ["**true**."]),
                ("What does `exec` return when nothing matches?", ["**`null`**, not `{}`."]),
                ("What is `exec(/e/)` on that sentence?", ['**["e"]** at **index 2** (`The`).']),
                ("How do you put `\\d` in `new RegExp`?", ["**`new RegExp(\"\\\\d+\")`**. `new RegExp(\"\\d+\")` is **`/d+/`**."]),
                ("Do ` /ab+c/i ` and `new RegExp(\"ab+c\", \"i\")` look the same?", ["**Yes** — both **`/ab+c/i`**."]),
                ("What happens to `lastIndex` after a failed `/g` `exec`?", ["It goes back to **0**."]),
                ("What are the `lastIndex` steps for `/is/g` on `Is this all there is?`?", ["Match at **5** → **7**; match at **18** → **20**; **null** → **0**."]),
                ("Why `RegExp.escape(\"[*]\")`?", ["So `[` `*` `]` are **literal**, not a character class. Then replace can turn `[*]` into `W3Schools`."]),
                ("Can you skip the variable and call `/e/.test(s)`?", ["**Yes.**"]),
            ],
            "Carry a RegExp as a literal or a constructor, remember constructor escaping, use test for yes/no and exec for the match object, and treat lastIndex as mutable state whenever g or y is on. Escape user text before embedding it in a pattern.",
            [
                ("JS RegExp Objects (W3Schools)", "https://www.w3schools.com/js/js_regexp_objects.asp"),
                mdn_obj,
                (
                    "MDN: RegExp.escape",
                    "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/escape",
                ),
            ],
        ),
        (
            "js-regexp-methods",
            "JS RegExp Methods",
            METHODS,
            "The complete RegExp reference (revised July 2025) lists instance properties, exec/test, deprecated compile, toString, static escape, and the string methods match/matchAll/replace/replaceAll/search/split. Each row is an Example. lastIndex with /g is shown mutating across exec calls. match with /g drops groups; matchAll keeps them. replace without g changes one hit; replaceAll requires g. compile still runs and must not be used.",
            [
                "**Every table row is an Example**, plus **`exec` vs `match` with `/g`**.",
                "**`compile`** is **deprecated** but still mutates the object here (`/abc/g` → `/def/i`).",
                "**`lastIndex`** + **`/g`**: exec at 5 → 7, at 18 → 20, null → **0**.",
                "`match` + **`g`** → strings only. **`matchAll`** → iterator of arrays **with groups** (needs **`g`**).",
                "`search` → index or **-1**. `split` → pieces. `flags` / `source` / `toString` inspect the pattern.",
            ],
            [
                ("What should you use instead of `compile()`?", ["Build a **new** `RegExp`. `compile` is **deprecated** (here it still became `/def/i`)."]),
                ("What is `pattern.constructor`?", ["**`RegExp`** (`function RegExp() { [native code] }`)."]),
                ("What does `flags` return for `/W3Schools/gim`?", ['**"gim"**.' ]),
                ("What does `source` return?", ['The body only: **"W3Schools"**.']),
                ("What does `toString()` return?", ['**"/W3Schools/gim"**.' ]),
                ("Does `test` with `/g` move `lastIndex`?", ["**Yes** — same as `exec`. Easy to flip true/false on repeats."]),
                ("`match` with `/g` vs without?", ["Without: **one** match **plus groups**. With: **all full matches**, **no groups**. Miss → **null**."]),
                ("Why `matchAll`?", ["All matches **with groups**. Must be **`/g`**. Here **[[\"a1\",\"1\"],[\"a2\",\"2\"]]**."]),
                ("`replace` vs `replaceAll`?", ["`replace` without **`g`** changes **one**. `replaceAll` needs **`g`** and changes **all**."]),
                ("What does `search` return on a miss?", ["**-1**."]),
                ("After `text.match(/a(\\d)/g)`, what is `lastIndex`?", ["**0** — `match` with **`g`** resets it. A following `exec` starts at the beginning."]),
                ("Is `RegExp.escape` an instance method?", ["**No.** Static **`RegExp.escape(string)`** (ES2025)."]),
            ],
            "The reference is a catalog of getters, exec/test, string search-and-replace, and a deprecated compile. Watch lastIndex whenever g or y is set. Prefer matchAll when you need groups for every hit. Skip compile; use a new RegExp.",
            [
                ("JS RegExp Methods (W3Schools)", "https://www.w3schools.com/js/js_regexp_methods.asp"),
                mdn_obj,
                (
                    "MDN: String.prototype.match",
                    "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match",
                ),
                (
                    "MDN: RegExp.prototype.exec",
                    "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec",
                ),
            ],
        ),
    ]

    if only:
        sections = [s for s in sections if s[0] in only]
    print("example counts:")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print(f"  {slug}: {len(recs)}")
        if not (8 <= len(qa) <= 15):
            print(f"  WARNING qa count {len(qa)} for {slug}")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print("building", slug, "examples", len(recs))
        build_and_snap(slug, title, recs, intro, concepts, qa, summary, refs, wait=2000)
        print("done", slug)


if __name__ == "__main__":
    import sys

    run_all(sys.argv[1:] or None)
