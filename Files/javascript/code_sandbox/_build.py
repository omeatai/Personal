# Temporary generator: sandbox HTML + snaps for thin tutorial sections.
from __future__ import annotations

import html
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SNAPS = ROOT / "snaps"

RESULT_TMPL = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="color-scheme" content="light" />
    <title>{title}</title>
    <link rel="stylesheet" href="../sandbox.css" />
  </head>
  <body>
    <h2>{heading}</h2>
    <pre id="demo"></pre>
    <script>
{script}
    </script>
  </body>
</html>
"""

SOURCE_TMPL = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="color-scheme" content="light" />
    <title>{title} source</title>
    <link rel="stylesheet" href="../sandbox.css" />
    <style>
      body {{ background: #f1f1f1; }}
      pre {{
        margin: 0;
        padding: 12px 16px;
        background: #fff;
        border: 1px solid #ccc;
        border-left: 4px solid #04aa6d;
        font-family: Consolas, "Courier New", monospace;
        font-size: 16px;
        line-height: 1.4;
        white-space: pre-wrap;
      }}
    </style>
  </head>
  <body>
    <h3>Example</h3>
    <pre>{code}</pre>
  </body>
</html>
"""

INDEX_TMPL = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="color-scheme" content="light" />
    <title>{title}</title>
    <link rel="stylesheet" href="../sandbox.css" />
  </head>
  <body>
    <h2>{title}</h2>
    <p>Open each example:</p>
    <ul>
{links}
    </ul>
  </body>
</html>
"""


def show(lines: str) -> str:
    """Assign labeled lines to #demo. `lines` is JS that evaluates to a string."""
    return f'      document.getElementById("demo").innerText = {lines};'


def join_lines(*parts: str) -> str:
    inner = ' + "\\n" + '.join(f"({p})" for p in parts)
    return show(inner)


def write_example(folder: Path, stem: str, heading: str, code: str, script: str) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{stem}.html").write_text(
        RESULT_TMPL.format(title=heading, heading=html.escape(heading), script=script),
        encoding="utf-8",
    )
    (folder / f"{stem}-source.html").write_text(
        SOURCE_TMPL.format(title=heading, code=html.escape(code)),
        encoding="utf-8",
    )


def write_index(folder: Path, title: str, items: list[tuple[str, str]]) -> None:
    links = "\n".join(
        f'      <li><a href="{stem}.html">{html.escape(label)}</a></li>'
        for stem, label in items
    )
    (folder / "index.html").write_text(
        INDEX_TMPL.format(title=html.escape(title), links=links),
        encoding="utf-8",
    )


def md_example(slug: str, n: int, title: str, bullets: list[str], file: str, code: str, outcome: str) -> str:
    nn = f"{n:02d}"
    b = "\n".join(f"- [x] {x}" for x in bullets)
    return f"""
### **Example {n}: {title}**

{b}

Sandbox: `code_sandbox/{slug}/{file}`

```javascript
{code}
```

<img alt="{slug} example {n} source" src="./code_sandbox/snaps/{slug}-{nn}-code.png" />

<img alt="{slug} example {n} result" src="./code_sandbox/snaps/{slug}-{nn}-result.png" />

- [x] **Outcome:** {outcome}
"""


def md_qa(items: list[tuple[str, list[str]]]) -> str:
    blocks = []
    for i, (q, answers) in enumerate(items, 1):
        ans = "\n".join(f"- [x] {a}" for a in answers)
        blocks.append(
            f"""### Question {i}: {q}

<details>
<summary>Answer</summary>

{ans}

</details>
"""
        )
    return "\n".join(blocks)


def accordion(
    summary: str,
    intro: str,
    concepts: list[str],
    examples_md: str,
    slug: str,
    qa: list[tuple[str, list[str]]],
    summary_para: str,
    refs: list[tuple[str, str]],
) -> str:
    concept = "\n".join(f"- [x] {c}" for c in concepts)
    ref_lines = "\n".join(f"- [{n}]({u})" for n, u in refs)
    return f"""<details>
  <summary>{summary}</summary>

## Introduction

{intro}

## Detailed Explanation

{concept}
{examples_md}
<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/{slug}/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

{md_qa(qa)}
</details>

## Summary

{summary_para}

## References

{ref_lines}

</details>
"""


# --- example records: (stem, title, bullets, code, script, outcome) ---

def S(stem, title, bullets, code, script, outcome):
    return dict(stem=stem, title=title, bullets=bullets, code=code, script=script, outcome=outcome)


def emit_section(slug: str, title: str, records: list[dict]) -> str:
    folder = ROOT / slug
    items = []
    parts = []
    for i, rec in enumerate(records, 1):
        write_example(folder, rec["stem"], rec["title"], rec["code"], rec["script"])
        items.append((rec["stem"], f"{i:02d} — {rec['title']}"))
        parts.append(
            md_example(
                slug, i, rec["title"], rec["bullets"], f"{rec['stem']}.html", rec["code"], rec["outcome"]
            )
        )
    write_index(folder, title, items)
    return "\n".join(parts)


def find_browser() -> str | None:
    candidates = [
        os.environ.get("CHROME_PATH"),
        shutil.which("msedge"),
        shutil.which("chrome"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    for c in candidates:
        if c and Path(c).is_file():
            return c
    return None


def screenshot_section(slug: str, records: list[dict], browser: str) -> None:
    SNAPS.mkdir(parents=True, exist_ok=True)
    folder = ROOT / slug
    for i, rec in enumerate(records, 1):
        nn = f"{i:02d}"
        result_html = (folder / f"{rec['stem']}.html").resolve().as_uri()
        source_html = (folder / f"{rec['stem']}-source.html").resolve().as_uri()
        result_png = str((SNAPS / f"{slug}-{nn}-result.png").resolve())
        code_png = str((SNAPS / f"{slug}-{nn}-code.png").resolve())
        for url, out in ((source_html, code_png), (result_html, result_png)):
            cmd = [
                browser,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                "--window-size=900,520",
                f"--screenshot={out}",
                "--virtual-time-budget=4000",
                url,
            ]
            subprocess.run(cmd, check=True, cwd=str(SNAPS), capture_output=True)


STRING_REF = [
    S(
        "at",
        "`at()`",
        [
            "**`at(index)`** returns the character at that index (0-based).",
            "**Negative indexes** count from the end (`at(-1)` is the last character).",
            "ES2022. **`charAt()` cannot take negatives**; use `at()` when you want that.",
        ],
        'const name = "W3Schools";\nname.at(2);\nname.at(-5);',
        """      const name = "W3Schools";
      document.getElementById("demo").innerText =
        'name.at(2)  -> ' + name.at(2) + "\\n" +
        'name.at(-5) -> ' + name.at(-5);""",
        "`at(2)` is **S** (third character); `at(-5)` is **h**.",
    ),
    S(
        "charAt",
        "`charAt()`",
        [
            "**`charAt(index)`** returns the character at that position.",
            "A missing index returns **`\"\"`** (empty string), not `undefined`.",
            "Does **not** accept negative indexes.",
        ],
        'let text = "HELLO WORLD";\nlet char = text.charAt(0);',
        """      let text = "HELLO WORLD";
      document.getElementById("demo").innerText =
        'charAt(0)  -> ' + text.charAt(0) + "\\n" +
        'charAt(99) -> "' + text.charAt(99) + '" (empty string)';""",
        "`charAt(0)` is **H**. `charAt(99)` is an **empty string**.",
    ),
    S(
        "charCodeAt",
        "`charCodeAt()`",
        [
            "**`charCodeAt(index)`** returns the **UTF-16 code unit** (0–65535) at that index.",
            "For `'H'` that code is **72**.",
        ],
        'let text = "HELLO WORLD";\nlet char = text.charCodeAt(0);',
        """      let text = "HELLO WORLD";
      document.getElementById("demo").innerText = "charCodeAt(0) -> " + text.charCodeAt(0);""",
        "**72** — the UTF-16 code for **H**.",
    ),
    S(
        "codePointAt",
        "`codePointAt()`",
        [
            "**`codePointAt(index)`** returns the Unicode **code point** at that index.",
            "For BMP characters like `'H'` it matches `charCodeAt`. It is the right choice for characters outside the BMP (emoji).",
        ],
        'let text = "HELLO WORLD";\nlet code = text.codePointAt(0);',
        """      let text = "HELLO WORLD";
      document.getElementById("demo").innerText = "codePointAt(0) -> " + text.codePointAt(0);""",
        "**72** for `'H'`.",
    ),
    S(
        "concat",
        "`concat()`",
        [
            "**`concat()`** joins two or more strings and returns a **new** string.",
            "Same result as **`+`**: `\"Hello\" + \" \" + \"World!\"`.",
        ],
        'let text1 = "Hello";\nlet text2 = "World";\nlet text3 = text1.concat(" ", text2);',
        """      let text1 = "Hello";
      let text2 = "World";
      document.getElementById("demo").innerText =
        'concat(" ", "World") -> ' + text1.concat(" ", text2);""",
        "The joined string is **Hello World**.",
    ),
    S(
        "constructor",
        "`constructor`",
        [
            "The **`constructor`** property is the function that created the instance — for a string that is **`String`**.",
            "This is a **property**, not a method you call for everyday text work.",
        ],
        'let text = "Hello";\ntext.constructor === String;',
        """      let text = "Hello";
      document.getElementById("demo").innerText =
        "constructor === String -> " + (text.constructor === String) + "\\n" +
        "constructor.name -> " + text.constructor.name;""",
        "`constructor === String` is **true**; the name is **String**.",
    ),
    S(
        "endsWith",
        "`endsWith()`",
        [
            "**`endsWith(search)`** returns **`true`** if the string ends with that text.",
            "Case-sensitive. Optional second argument: treat the string as if it were only that long.",
        ],
        'let text = "John Doe";\ntext.endsWith("Doe");',
        """      let text = "John Doe";
      document.getElementById("demo").innerText =
        'endsWith("Doe")  -> ' + text.endsWith("Doe") + "\\n" +
        'endsWith("John") -> ' + text.endsWith("John");""",
        '**true** for "Doe"; **false** for "John".',
    ),
    S(
        "fromCharCode",
        "`String.fromCharCode()`",
        [
            "**Static** method on **`String`** (not `text.fromCharCode`).",
            "Turns UTF-16 code units into a string: `72, 69, 76, 76, 79` → **HELLO**.",
        ],
        "String.fromCharCode(72, 69, 76, 76, 79);",
        """      document.getElementById("demo").innerText =
        "fromCharCode(72, 69, 76, 76, 79) -> " + String.fromCharCode(72, 69, 76, 76, 79);""",
        "The characters spell **HELLO**.",
    ),
    S(
        "includes",
        "`includes()`",
        [
            "**`includes(search)`** returns **`true`** if the substring exists anywhere.",
            "Case-sensitive ES6 method. Optional start index.",
        ],
        'let text = "Hello world, welcome to the universe.";\ntext.includes("world");',
        """      let text = "Hello world, welcome to the universe.";
      document.getElementById("demo").innerText =
        'includes("world")     -> ' + text.includes("world") + "\\n" +
        'includes("world", 12) -> ' + text.includes("world", 12);""",
        '**true** from the start; **false** if you start searching at index **12** (past "world").',
    ),
    S(
        "indexOf",
        "`indexOf()`",
        [
            "**`indexOf(search)`** returns the **first** index of the substring, or **`-1`** if missing.",
            "Positions start at **0**. Optional second argument: start index.",
        ],
        'let text = "Please locate where \'locate\' occurs!";\nlet index = text.indexOf("locate");',
        """      let text = "Please locate where 'locate' occurs!";
      document.getElementById("demo").innerText =
        'indexOf("locate")     -> ' + text.indexOf("locate") + "\\n" +
        'indexOf("locate", 15) -> ' + text.indexOf("locate", 15) + "\\n" +
        'indexOf("missing")    -> ' + text.indexOf("missing");""",
        'First "locate" is at **7**; from index 15 the next is **21**; missing text is **-1**.',
    ),
    S(
        "isWellFormed",
        "`isWellFormed()`",
        [
            "Returns **`true`** if the string has no **lone surrogates** (broken UTF-16 pairs).",
            r"A lone `\uD800` makes it **false**.",
        ],
        'let ok = "Hello world!".isWellFormed();\nlet bad = "Hello World \\uD800".isWellFormed();',
        """      document.getElementById("demo").innerText =
        '"Hello world!".isWellFormed()        -> ' + "Hello world!".isWellFormed() + "\\n" +
        '"Hello World \\\\uD800".isWellFormed() -> ' + "Hello World \\uD800".isWellFormed();""",
        "Normal text is **true**; a lone surrogate is **false**.",
    ),
    S(
        "lastIndexOf",
        "`lastIndexOf()`",
        [
            "**`lastIndexOf(search)`** returns the **last** occurrence, or **`-1`**.",
            "With a start index it searches **backward** from that position.",
        ],
        'let text = "Please locate where \'locate\' occurs!";\ntext.lastIndexOf("locate");',
        """      let text = "Please locate where 'locate' occurs!";
      document.getElementById("demo").innerText =
        'lastIndexOf("locate")     -> ' + text.lastIndexOf("locate") + "\\n" +
        'lastIndexOf("locate", 15) -> ' + text.lastIndexOf("locate", 15) + "\\n" +
        'lastIndexOf("John")       -> ' + text.lastIndexOf("John");""",
        'Last "locate" is **21**; searching backward from 15 finds **7**; "John" is **-1**.',
    ),
    S(
        "length",
        "`length`",
        [
            "**`length`** is a **property**, not a method — no parentheses.",
            "It counts UTF-16 code units (emoji can count as 2).",
        ],
        'let text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";\nlet length = text.length;',
        """      let text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      document.getElementById("demo").innerText = "length -> " + text.length;""",
        "A–Z is **26** characters.",
    ),
    S(
        "localeCompare",
        "`localeCompare()`",
        [
            "Compares two strings in the **current locale** and returns a **negative / 0 / positive** number (sort order).",
            "`\"ab\".localeCompare(\"cd\")` is negative because **ab** comes first.",
        ],
        '"ab".localeCompare("cd");\n"cd".localeCompare("ab");\n"ab".localeCompare("ab");',
        """      document.getElementById("demo").innerText =
        '"ab".localeCompare("cd") -> ' + "ab".localeCompare("cd") + "\\n" +
        '"cd".localeCompare("ab") -> ' + "cd".localeCompare("ab") + "\\n" +
        '"ab".localeCompare("ab") -> ' + "ab".localeCompare("ab");""",
        "**ab** vs **cd** is negative; reverse is positive; equal strings return **0**.",
    ),
    S(
        "match",
        "`match()`",
        [
            "Returns an **array** of matches (or `null` if none).",
            "Without **`/g`**, you get details of the **first** match. With **`/g`** (and `/i`) you get all matches.",
        ],
        'let text = "The rain in SPAIN stays mainly in the plain";\ntext.match(/ain/gi);',
        """      let text = "The rain in SPAIN stays mainly in the plain";
      document.getElementById("demo").innerText =
        "match(/ain/gi) -> " + text.match(/ain/gi);""",
        "The global, case-insensitive match is **ain,AIN,ain,ain**.",
    ),
    S(
        "matchAll",
        "`matchAll()`",
        [
            "Returns an **iterator** of all matches (ES2020).",
            "If you pass a regex, it **must** have the **`g`** flag or you get a **TypeError**.",
        ],
        'let text = "I love Cats. Cats are great.";\nArray.from(text.matchAll(/Cats/g), m => m[0]);',
        """      let text = "I love Cats. Cats are great.";
      const found = Array.from(text.matchAll(/Cats/g), (m) => m[0]);
      document.getElementById("demo").innerText = "matchAll(/Cats/g) -> " + found.join(", ");""",
        "The iterator yields **Cats, Cats** (two matches).",
    ),
    S(
        "padEnd",
        "`padEnd()`",
        [
            "Pads the **end** of the string until it reaches a given length.",
            "It is a **string** method — convert numbers with **`toString()`** first.",
        ],
        'let text = "5";\ntext.padEnd(4, "0");\ntext.padEnd(4, "x");',
        """      let text = "5";
      document.getElementById("demo").innerText =
        'padEnd(4, "0") -> ' + text.padEnd(4, "0") + "\\n" +
        'padEnd(4, "x") -> ' + text.padEnd(4, "x");""",
        "**5000** and **5xxx**.",
    ),
    S(
        "padStart",
        "`padStart()`",
        [
            "Pads the **start** of the string until it reaches a given length.",
            "Useful for zero-padding: `\"5\".padStart(4, \"0\")` → **0005**.",
        ],
        'let text = "5";\ntext.padStart(4, "0");\ntext.padStart(4, "x");',
        """      let text = "5";
      document.getElementById("demo").innerText =
        'padStart(4, "0") -> ' + text.padStart(4, "0") + "\\n" +
        'padStart(4, "x") -> ' + text.padStart(4, "x");""",
        "**0005** and **xxx5**.",
    ),
    S(
        "prototype",
        "`prototype`",
        [
            "**`String.prototype`** is how you add methods that every string can use.",
            "Do this only for demos or shared libraries — extra prototype methods surprise other code.",
        ],
        'String.prototype.exclaim = function () {\n  return this + "!";\n};\n"Hi".exclaim();',
        """      String.prototype.exclaim = function () {
        return String(this) + "!";
      };
      document.getElementById("demo").innerText = '"Hi".exclaim() -> ' + "Hi".exclaim();""",
        "`\"Hi\".exclaim()` returns **Hi!**.",
    ),
    S(
        "repeat",
        "`repeat()`",
        [
            "**`repeat(count)`** returns a **new** string with that many copies.",
            "Does not change the original. `count` must be a non-negative integer.",
        ],
        'let text = "Ha";\ntext.repeat(3);',
        """      let text = "Ha";
      document.getElementById("demo").innerText =
        "repeat(2) -> " + text.repeat(2) + "\\n" +
        "repeat(4) -> " + text.repeat(4);""",
        "**HaHa** and **HaHaHaHa**. The original `Ha` is unchanged.",
    ),
    S(
        "replace",
        "`replace()`",
        [
            "Replaces the **first** match only (unless you use a regex with **`/g`**).",
            "Case-sensitive by default; use **`/i`** to ignore case.",
        ],
        'let text = "Please visit Microsoft and Microsoft!";\ntext.replace("Microsoft", "W3Schools");',
        """      let text = "Please visit Microsoft and Microsoft!";
      document.getElementById("demo").innerText =
        "replace first -> " + text.replace("Microsoft", "W3Schools") + "\\n" +
        "replace /g    -> " + text.replace(/Microsoft/g, "W3Schools");""",
        "Without `/g` only the **first** Microsoft changes; with `/g` **both** change.",
    ),
    S(
        "replaceAll",
        "`replaceAll()`",
        [
            "Replaces **every** match (ES2021).",
            "If the search is a regex, it **must** include **`g`** or you get a **TypeError**.",
        ],
        'let text = "I love Cats. Cats are great.";\ntext.replaceAll("Cats", "Dogs");',
        """      let text = "I love Cats. Cats are great.";
      document.getElementById("demo").innerText =
        'replaceAll("Cats", "Dogs") -> ' + text.replaceAll("Cats", "Dogs");""",
        "Both **Cats** become **Dogs**: **I love Dogs. Dogs are great.**",
    ),
    S(
        "search",
        "`search()`",
        [
            "Returns the **index** of a match (string or **regex**), or **`-1`**.",
            "**Not** the same as `indexOf`: `search` has **no** start-index argument; `indexOf` cannot take a regex.",
        ],
        'let text = "Please locate where \'locate\' occurs!";\ntext.search("locate");\ntext.search(/locate/);',
        """      let text = "Please locate where 'locate' occurs!";
      document.getElementById("demo").innerText =
        'search("locate") -> ' + text.search("locate") + "\\n" +
        "search(/locate/) -> " + text.search(/locate/);""",
        "Both forms return **7** for this string.",
    ),
    S(
        "slice",
        "`slice()`",
        [
            "**`slice(start, end)`** copies a section; **end is not included**.",
            "**Negative** indexes count from the end. Omit `end` to take the rest.",
        ],
        'let text = "Apple, Banana, Kiwi";\ntext.slice(7, 13);\ntext.slice(7);\ntext.slice(-12, -6);',
        """      let text = "Apple, Banana, Kiwi";
      document.getElementById("demo").innerText =
        "slice(7, 13)    -> " + text.slice(7, 13) + "\\n" +
        "slice(7)        -> " + text.slice(7) + "\\n" +
        "slice(-12, -6)  -> " + text.slice(-12, -6);""",
        "`slice(7, 13)` is **Banana**; `slice(7)` is **Banana, Kiwi**; `slice(-12, -6)` is **Banana**.",
    ),
    S(
        "split",
        "`split()`",
        [
            "Turns a string into an **array** of pieces.",
            '`split("")` splits on every UTF-16 unit and is **unsafe for emoji**. Prefer **`Intl.Segmenter`** for graphemes.',
        ],
        'let text = "The quick brown fox.";\ntext.split(" ");',
        """      let text = "The quick brown fox.";
      document.getElementById("demo").innerText =
        'split(" ") -> ' + JSON.stringify(text.split(" ")) + "\\n" +
        'split("")  -> ' + JSON.stringify("Hi".split(""));""",
        '`split(" ")` is **["The","quick","brown","fox."]**; `split("")` on `"Hi"` is **["H","i"]**.',
    ),
    S(
        "startsWith",
        "`startsWith()`",
        [
            "Returns **`true`** if the string **begins** with the given text.",
            "Case-sensitive. Optional start index shifts where “the beginning” is.",
        ],
        'let text = "Hello world, welcome to the universe.";\ntext.startsWith("Hello");\ntext.startsWith("world");',
        """      let text = "Hello world, welcome to the universe.";
      document.getElementById("demo").innerText =
        'startsWith("Hello")     -> ' + text.startsWith("Hello") + "\\n" +
        'startsWith("world")     -> ' + text.startsWith("world") + "\\n" +
        'startsWith("world", 6)  -> ' + text.startsWith("world", 6);""",
        '**true** for "Hello"; **false** for "world" unless you start at index **6**.',
    ),
    S(
        "substr",
        "`substr()` (deprecated)",
        [
            "**Deprecated.** The second argument is a **length**, not an end index.",
            "Still works for compatibility. **Use `substring()` or `slice()`** in new code.",
        ],
        'let str = "Apple, Banana, Kiwi";\nstr.substr(7, 6);\nstr.substr(7);\nstr.substr(-4);',
        """      let str = "Apple, Banana, Kiwi";
      document.getElementById("demo").innerText =
        "substr(7, 6) -> " + str.substr(7, 6) + "  (deprecated)\\n" +
        "substr(7)    -> " + str.substr(7) + "\\n" +
        "substr(-4)   -> " + str.substr(-4);""",
        "`substr(7, 6)` is **Banana**; from 7 to the end is **Banana, Kiwi**; `-4` is **Kiwi**. Prefer **slice/substring**.",
    ),
    S(
        "substring",
        "`substring()`",
        [
            "Like `slice()`, but **negative start/end become 0** (they do not count from the end).",
            "If start > end, `substring` **swaps** them; `slice` returns empty.",
        ],
        'let str = "Apple, Banana, Kiwi";\nstr.substring(7, 13);',
        """      let str = "Apple, Banana, Kiwi";
      document.getElementById("demo").innerText =
        "substring(7, 13) -> " + str.substring(7, 13) + "\\n" +
        "substring(-3, 5) -> " + str.substring(-3, 5) + "  (negatives become 0)";""",
        "`substring(7, 13)` is **Banana**. Negatives are treated as **0**, so you get the start of the string.",
    ),
    S(
        "toLocaleLowerCase",
        "`toLocaleLowerCase()`",
        [
            "Lowercases using the **host locale** (important for languages like Turkish `I` → `ı`).",
            "For English text it matches `toLowerCase()`.",
        ],
        'let text = "Hello WORLD!";\ntext.toLocaleLowerCase();',
        """      let text = "Hello WORLD!";
      document.getElementById("demo").innerText = "toLocaleLowerCase() -> " + text.toLocaleLowerCase();""",
        "The result is **hello world!**.",
    ),
    S(
        "toLocaleUpperCase",
        "`toLocaleUpperCase()`",
        [
            "Uppercases using the **host locale**.",
            "Same idea as `toLocaleLowerCase()`, but toward capitals.",
        ],
        'let text = "Hello World!";\ntext.toLocaleUpperCase();',
        """      let text = "Hello World!";
      document.getElementById("demo").innerText = "toLocaleUpperCase() -> " + text.toLocaleUpperCase();""",
        "The result is **HELLO WORLD!**.",
    ),
    S(
        "toLowerCase",
        "`toLowerCase()`",
        [
            "Returns a **new** string with all letters in lower case.",
            "The original string is unchanged.",
        ],
        'let text1 = "Hello World!";\nlet text2 = text1.toLowerCase();',
        """      let text1 = "Hello World!";
      document.getElementById("demo").innerText =
        "original     -> " + text1 + "\\n" +
        "toLowerCase  -> " + text1.toLowerCase();""",
        "The new string is **hello world!**; **Hello World!** is still the original.",
    ),
    S(
        "toString",
        "`toString()`",
        [
            "Returns the string **primitive**. Useful on a `new String('Hello')` object.",
            "On a normal string literal it just returns the same text.",
        ],
        'let obj = new String("Hello");\nobj.toString();',
        """      let obj = new String("Hello");
      document.getElementById("demo").innerText =
        "typeof obj          -> " + typeof obj + "\\n" +
        "obj.toString()      -> " + obj.toString() + "\\n" +
        'typeof obj.toString() -> ' + typeof obj.toString();""",
        "The object’s `toString()` is the primitive **Hello** (`typeof` **string**).",
    ),
    S(
        "toUpperCase",
        "`toUpperCase()`",
        [
            "Returns a **new** string with all letters in upper case.",
        ],
        'let text1 = "Hello World!";\nlet text2 = text1.toUpperCase();',
        """      let text1 = "Hello World!";
      document.getElementById("demo").innerText = "toUpperCase() -> " + text1.toUpperCase();""",
        "The result is **HELLO WORLD!**.",
    ),
    S(
        "toWellFormed",
        "`toWellFormed()`",
        [
            "Returns a new string where **lone surrogates** are replaced with **U+FFFD** (`�`).",
            "Use with `isWellFormed()` when you need to sanitize broken UTF-16.",
        ],
        'let text = "Hello World \\uD800";\ntext.toWellFormed();',
        """      let text = "Hello World \\uD800";
      document.getElementById("demo").innerText =
        "isWellFormed  -> " + text.isWellFormed() + "\\n" +
        "toWellFormed  -> " + text.toWellFormed();""",
        "The original is **not** well formed; `toWellFormed()` replaces the lone surrogate with **�**.",
    ),
    S(
        "trim",
        "`trim()`",
        [
            "Removes **whitespace from both ends**. Does not change the original.",
            "Spaces in the **middle** stay.",
        ],
        'let original = " Hello ";\nlet trimmed = original.trim();',
        """      let original = " Hello ";
      let trimmed = original.trim();
      document.getElementById("demo").innerText =
        "original -> '" + original + "'\\n" +
        "trim()   -> '" + trimmed + "'";""",
        "The original still has spaces (`' Hello '`); `trim()` returns **`'Hello'`**.",
    ),
    S(
        "trimEnd",
        "`trimEnd()`",
        [
            "Removes whitespace from the **end only** (ES2019). Alias: `trimRight()`.",
        ],
        'let text1 = " Hello World! ";\nlet text2 = text1.trimEnd();',
        """      let text1 = " Hello World! ";
      document.getElementById("demo").innerText =
        "original -> '" + text1 + "'\\n" +
        "trimEnd  -> '" + text1.trimEnd() + "'";""",
        "Leading space remains; the trailing space is gone: **`' Hello World!'`**.",
    ),
    S(
        "trimStart",
        "`trimStart()`",
        [
            "Removes whitespace from the **start only** (ES2019). Alias: `trimLeft()`.",
        ],
        'let text1 = " Hello World! ";\nlet text2 = text1.trimStart();',
        """      let text1 = " Hello World! ";
      document.getElementById("demo").innerText =
        "original  -> '" + text1 + "'\\n" +
        "trimStart -> '" + text1.trimStart() + "'";""",
        "Trailing space remains; the leading space is gone: **`'Hello World! '`**.",
    ),
    S(
        "valueOf",
        "`valueOf()`",
        [
            "Returns the **primitive** string value (same idea as `toString()` for String objects).",
            "JavaScript calls this automatically in most string operations.",
        ],
        'let obj = new String("Hello");\nobj.valueOf();',
        """      let obj = new String("Hello");
      document.getElementById("demo").innerText =
        "typeof obj         -> " + typeof obj + "\\n" +
        "obj.valueOf()      -> " + obj.valueOf() + "\\n" +
        "typeof obj.valueOf() -> " + typeof obj.valueOf();""",
        "`valueOf()` is the primitive **Hello** (`typeof` **string**), while `obj` itself is an **object**.",
    ),
    S(
        "html-wrappers",
        "HTML wrapper methods (deprecated — do not use)",
        [
            "These methods wrap the string in an **HTML tag** (`bold()` → `<b>…</b>`).",
            "**Deprecated.** Not for new code. Style with **CSS** and create elements with the **DOM**.",
            "They exist only for old-page compatibility. The sandbox still **runs every wrapper** so you can recognize them.",
        ],
        'let t = "Hi";\nt.bold();\nt.italics();\nt.link("https://example.com");\n// also: anchor, big, blink, fixed, fontcolor, fontsize, small, strike, sub, sup',
        """      const t = "Hi";
      const rows = [
        ["bold()", t.bold()],
        ["italics()", t.italics()],
        ["small()", t.small()],
        ["strike()", t.strike()],
        ["sub()", t.sub()],
        ["sup()", t.sup()],
        ["big()", t.big()],
        ["blink()", t.blink()],
        ["fixed()", t.fixed()],
        ["anchor('x')", t.anchor("x")],
        ["link(url)", t.link("https://example.com")],
        ["fontcolor('red')", t.fontcolor("red")],
        ["fontsize(7)", t.fontsize(7)],
      ];
      document.getElementById("demo").innerText =
        "DEPRECATED — do not use in new code\\n" +
        rows.map(([n, v]) => n + " -> " + v).join("\\n");""",
        "Each call returns a **string of HTML** (for example `bold()` → `<b>Hi</b>`). Do **not** use these; use CSS/DOM instead.",
    ),
]


def build_string_ref() -> str:
    examples = emit_section("js-string-reference", "JS String Reference", STRING_REF)
    return accordion(
        "JS String Reference",
        "This page is the **complete String reference** (revised July 2025): every **property and method** from **`at()`** through **`valueOf()`**, plus the old **HTML wrappers**. All methods return a **new** value — they do **not** change the original string. Each table row below is its own Example, the same grain as **JS Output**.",
        [
            "**Core idea** — string methods never mutate the original; they return a new string (or a number / boolean / array / iterator).",
            "**Table grain** — one Example per reference-table row. Deprecated HTML wrappers are one grouped Example that still **runs every wrapper**.",
            "**`substr()` is deprecated** — use `substring()` or `slice()`.",
        ],
        examples,
        "js-string-reference",
        [
            ("Do string methods change the original string?", ["**No.** They return a **new** value.", "Assign the result if you want to keep it."]),
            ("What does `at(-1)` return?", ["The **last** character.", "`charAt()` cannot take a negative index."]),
            ("What does `charAt(99)` return on a short string?", ["An **empty string** `\"\"`.", "`text[99]` would be **`undefined`** instead."]),
            ("Is `length` a method?", ["**No.** It is a **property** — `text.length`, not `text.length()`."]),
            ("What does `indexOf` return when the text is missing?", ["**`-1`.**"]),
            ("How do `indexOf` and `search` differ?", ["**`search`** can take a **regex** but **not** a start index.", "**`indexOf`** can take a start index but **not** a regex."]),
            ("Does `replace` change every match?", ["**No.** Only the **first**, unless you use a regex with **`/g`** or call **`replaceAll()`**."]),
            ("What should you use instead of `substr()`?", ["**`substring()`** or **`slice()`**.", "`substr()` is **deprecated**."]),
            ("Should you use `bold()` / `italics()`?", ["**No.** HTML wrappers are **deprecated**.", "Use **CSS** and the **DOM**."]),
            ("What does `isWellFormed()` check?", ["Whether the string has **lone surrogates** (broken UTF-16).", "Fix them with **`toWellFormed()`**, which inserts **�**."]),
            ("What does `\"5\".padStart(4, \"0\")` return?", ["**0005**.", "Pad a **string**; convert numbers with **`toString()`** first."]),
            ("Why is `split(\"\")` unsafe for emoji?", ["It splits **UTF-16 code units** and can break surrogate pairs.", "Use **`Intl.Segmenter`** for graphemes."]),
            ("What does `String.fromCharCode(72, 69, 76, 76, 79)` return?", ["**HELLO**.", "It is a **static** method on `String`, not on a string value."]),
            ("What does `match(/ain/gi)` find in the rain sentence?", ["**ain, AIN, ain, ain** — all matches, case-insensitive."]),
            ("What do `toString()` and `valueOf()` do on `new String(\"Hello\")`?", ["They return the primitive **\"Hello\"**.", "`typeof` of the object is **object**; `typeof` of the return is **string**."]),
        ],
        "Every String property and method has its own Example. Methods return new values. Skip **`substr`** and the **HTML wrappers**; style with CSS and the DOM. `at()` supports negatives, `length` is a property, `indexOf` returns `-1` when missing, `replace` changes the first match, `replaceAll` changes every match, and `split(\"\")` is unsafe on emoji.",
        [
            ("JS String Reference (W3Schools)", "https://www.w3schools.com/js/js_string_reference.asp"),
            ("MDN: String", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String"),
            ("MDN: String.prototype.at()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/at"),
            ("MDN: String.prototype.slice()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice"),
            ("MDN: String.prototype.replaceAll()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll"),
            ("W3Schools JavaScript Reference", "https://www.w3schools.com/jsref/default.asp"),
        ],
    )


if __name__ == "__main__":
    md = build_string_ref()
    out = ROOT / "_generated_js-string-reference.md"
    out.write_text(md, encoding="utf-8")
    print("wrote", out, "chars", len(md), "examples", len(STRING_REF))
    browser = find_browser()
    print("browser", browser)
    if browser:
        screenshot_section("js-string-reference", STRING_REF, browser)
        print("snaps done")
    else:
        print("NO BROWSER")
