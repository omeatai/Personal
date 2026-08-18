"""S12 Sets + S13 Maps (W3Schools JS tutorial)."""
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


def jsf(expr: str) -> str:
    return f"JSON.stringify(Array.from({expr}))"


LETTERS = 'const letters = new Set(["a","b","c"]);'
AB = 'const A = new Set(["a","b","c"]);\nconst B = new Set(["b","c","d"]);'
FRUITS = (
    "const fruits = new Map([\n"
    '  ["apples", 500],\n'
    '  ["bananas", 300],\n'
    '  ["oranges", 200]\n'
    "]);"
)
JOHN = 'let myObj = {fname:"John", lname:"Doe"};'


# ---------------------------------------------------------------------------
# 12.1 JS Sets
# ---------------------------------------------------------------------------

SETS = [
    S(
        "new-set-array",
        'new Set(["a","b","c"])',
        [
            "Pass an **array** to `new Set()` to fill the Set in one step.",
            "A Set stores **unique** values of any type (primitives or objects).",
        ],
        LETTERS,
        [("Array.from(letters)", jsf("letters")), ("letters.size", "letters.size")],
        'letters is **["a","b","c"]**. size is **3**.',
    ),
    S(
        "new-set-add-values",
        "new Set() then add() values",
        [
            "You can start **empty** and `add()` values one at a time.",
        ],
        'const letters = new Set();\nletters.add("a");\nletters.add("b");\nletters.add("c");',
        [("Array.from(letters)", jsf("letters")), ("letters.size", "letters.size")],
        'Same result: **["a","b","c"]**, size **3**.',
    ),
    S(
        "new-set-add-variables",
        "add() variables",
        [
            "`add()` accepts a **variable**. The Set stores the **value**, not the name.",
        ],
        'const letters = new Set();\nconst a = "a";\nconst b = "b";\nconst c = "c";\nletters.add(a);\nletters.add(b);\nletters.add(c);',
        [("Array.from(letters)", jsf("letters")), ("letters.size", "letters.size")],
        'Still **["a","b","c"]**. The variables were just another way to pass **"a"**, **"b"**, **"c"**.',
    ),
    S(
        "add-d-e",
        'add("d") and add("e")',
        [
            "`add()` inserts a value if it is **not already** in the Set.",
            "Insertion order is kept: new values go at the **end**.",
        ],
        f'{LETTERS}\nletters.add("d");\nletters.add("e");',
        [("Array.from(letters)", jsf("letters")), ("letters.size", "letters.size")],
        'letters is **["a","b","c","d","e"]**. size is **5**.',
    ),
    S(
        "add-duplicates",
        "add() equal elements — only the first is kept",
        [
            "If you add a value that **already exists**, `add()` does **nothing**.",
            "That uniqueness is the main Set feature.",
        ],
        'const letters = new Set();\nletters.add("a");\nletters.add("b");\nletters.add("c");\nletters.add("c");\nletters.add("c");\nletters.add("c");\nletters.add("c");\nletters.add("c");',
        [("Array.from(letters)", jsf("letters")), ("letters.size", "letters.size")],
        'Six `add("c")` calls still leave **["a","b","c"]**. size stays **3**.',
    ),
    S(
        "for-of-list",
        "for...of lists Set values",
        [
            "Sets are **iterable**. `for...of` yields each value in insertion order.",
        ],
        f'{LETTERS}\nlet text = "";\nfor (const x of letters) {{\n  text += x;\n}}',
        [("text", "text"), ("Array.from(letters)", jsf("letters"))],
        'text is **"abc"**. The loop concatenated **"a"**, **"b"**, **"c"** with no separator.',
    ),
    S(
        "typeof-object",
        "typeof a Set is object",
        [
            "`typeof` on a Set is **\"object\"** (same as Array, Date, Map).",
            "Use `instanceof Set` if you need to tell Sets from other objects.",
        ],
        f"{LETTERS}\ntypeof letters;",
        [("typeof letters", "typeof letters")],
        '`typeof letters` is **object**.',
    ),
    S(
        "instanceof-set",
        "instanceof Set is true",
        [
            "`letters instanceof Set` is **true** for a real Set.",
        ],
        f"{LETTERS}\nletters instanceof Set;",
        [("letters instanceof Set", "letters instanceof Set")],
        "`instanceof Set` is **true**.",
    ),
    S(
        "mixed-types",
        "Values may be any type",
        [
            "The page says values can be **primitives or objects**.",
            "`1` and `\"1\"` are **different**. The same object added twice is **one** entry.",
        ],
        'const obj = {n: 1};\nconst letters = new Set([1, "1", obj, obj]);',
        [("Array.from(letters)", jsf("letters")), ("letters.size", "letters.size")],
        'The Set is **[1,"1",{"n":1}]**. size is **3** — `obj` was stored once.',
    ),
    S(
        "two-objects-distinct",
        "Two similar objects are two values",
        [
            "Objects compare by **reference**, not by matching fields.",
            "`{x:1}` and another `{x:1}` are **two** Set entries.",
        ],
        "const a = {x: 1};\nconst b = {x: 1};\nconst letters = new Set([a, b]);",
        [("letters.size", "letters.size"), ("Array.from(letters)", jsf("letters"))],
        'size is **2**. JSON is **[{"x":1},{"x":1}]** — same shape, two objects.',
    ),
]


# ---------------------------------------------------------------------------
# 12.2 JS Set Methods
# ---------------------------------------------------------------------------

SET_METHODS = [
    S(
        "new-set",
        "new Set() from an array",
        [
            "`new Set(iterable)` copies unique values from the array.",
        ],
        LETTERS,
        [("Array.from(letters)", jsf("letters")), ("letters.size", "letters.size")],
        'letters is **["a","b","c"]**. size is **3**.',
    ),
    S(
        "add-d-e",
        'add("d") and add("e")',
        [
            "`add()` appends a value that is not already present.",
        ],
        f'{LETTERS}\nletters.add("d");\nletters.add("e");',
        [("Array.from(letters)", jsf("letters")), ("letters.size", "letters.size")],
        'After the two adds: **["a","b","c","d","e"]**, size **5**.',
    ),
    S(
        "add-duplicates",
        "add() ignores duplicates",
        [
            "Adding an existing value **leaves the Set unchanged**.",
        ],
        'const letters = new Set();\nletters.add("a");\nletters.add("b");\nletters.add("c");\nletters.add("c");\nletters.add("c");\nletters.add("c");\nletters.add("c");\nletters.add("c");',
        [("Array.from(letters)", jsf("letters")), ("letters.size", "letters.size")],
        'Result is **["a","b","c"]**. size **3**.',
    ),
    S(
        "size",
        "size property",
        [
            "`size` is the number of **unique** elements (not `length`).",
        ],
        'const mySet = new Set(["a","b","c"]);\nmySet.size;',
        [("mySet.size", "mySet.size"), ("Array.from(mySet)", jsf("mySet"))],
        "`mySet.size` is **3**.",
    ),
    S(
        "for-of-list",
        "for...of lists elements",
        [
            "`for...of` walks the Set in insertion order.",
        ],
        f'{LETTERS}\nlet text = "";\nfor (const x of letters) {{\n  text += x;\n}}',
        [("text", "text")],
        'text is **"abc"**.',
    ),
    S(
        "has-d",
        'has("d")',
        [
            "`has(value)` is **true** only if that value is in the Set.",
            'This Tryit asks about **"d"** in `["a","b","c"]`.',
        ],
        f'{LETTERS}\nconst answer = letters.has("d");',
        [
            ('letters.has("d")', 'letters.has("d")'),
            ('letters.has("a")', 'letters.has("a")'),
        ],
        '`has("d")` is **false**. `has("a")` is **true**.',
    ),
    S(
        "for-each",
        "forEach() for each value",
        [
            "`forEach(callback)` runs once per value.",
            "The callback’s first argument is the **value** (Sets have no separate key).",
        ],
        f'{LETTERS}\nlet text = "";\nletters.forEach(function (value) {{\n  text += value;\n}});',
        [("text", "text")],
        'text is **"abc"**.',
    ),
    S(
        "values-iterator",
        "values() iterator variable",
        [
            "`values()` returns an **iterator** of the Set’s values.",
            "Store it, then `for...of` the iterator.",
        ],
        f'{LETTERS}\nconst myIterator = letters.values();\nlet text = "";\nfor (const entry of myIterator) {{\n  text += entry;\n}}',
        [("text", "text"), ("Array.from(letters.values())", jsf("letters.values()"))],
        'text is **"abc"**. `Array.from(letters.values())` is **["a","b","c"]**.',
    ),
    S(
        "values-direct",
        "for...of letters.values()",
        [
            "You can loop `letters.values()` **directly** without a named iterator.",
        ],
        f'{LETTERS}\nlet text = "";\nfor (const entry of letters.values()) {{\n  text += entry;\n}}',
        [("text", "text")],
        'Same concatenation: **"abc"**.',
    ),
    S(
        "keys-iterator",
        "keys() iterator variable",
        [
            "A Set has **no keys**, so `keys()` is the **same as** `values()`.",
            "That pairing exists so Sets line up with Maps.",
        ],
        f'{LETTERS}\nconst myIterator = letters.keys();\nlet text = "";\nfor (const x of myIterator) {{\n  text += x;\n}}',
        [("text", "text"), ("Array.from(letters.keys())", jsf("letters.keys()"))],
        'text is **"abc"**. keys are **["a","b","c"]** — the values, reused as keys.',
    ),
    S(
        "keys-direct",
        "for...of letters.keys()",
        [
            "Loop `letters.keys()` directly; it still yields the values.",
        ],
        f'{LETTERS}\nlet text = "";\nfor (const x of letters.keys()) {{\n  text += x;\n}}',
        [("text", "text")],
        'text is **"abc"**.',
    ),
    S(
        "entries-iterator",
        "entries() iterator variable",
        [
            "`entries()` is supposed to yield **[key, value]** pairs.",
            "A Set has no keys, so each pair is **[value, value]**.",
        ],
        f'{LETTERS}\nconst myIterator = letters.entries();\nlet text = "";\nfor (const entry of myIterator) {{\n  text += entry;\n}}',
        [
            ("text", "text"),
            ("Array.from(letters.entries())", jsf("letters.entries()")),
        ],
        '`text += entry` stringifies each pair: **"a,ab,bc,c"**. '
        'The pairs themselves are **[["a","a"],["b","b"],["c","c"]]**.',
    ),
    S(
        "entries-direct",
        "for...of letters.entries()",
        [
            "Loop `letters.entries()` directly. Same **[value, value]** pairs.",
        ],
        f'{LETTERS}\nlet text = "";\nfor (const entry of letters.entries()) {{\n  text += entry;\n}}',
        [("text", "text")],
        'text is again **"a,ab,bc,c"** (`Array.prototype.toString` joins with a comma, then the next pair is glued on).',
    ),
    S(
        "delete-b",
        'delete("b") — listed, no Tryit',
        [
            "`delete(value)` removes that value and returns **true** if it was present.",
            "The methods list includes `delete()` with no Tryit — still run it.",
        ],
        f'{LETTERS}\nconst removed = letters.delete("b");\nconst missing = letters.delete("z");',
        [
            ("removed", "removed"),
            ("missing", "missing"),
            ("Array.from(letters)", jsf("letters")),
            ("letters.size", "letters.size"),
        ],
        '`delete("b")` is **true**. `delete("z")` is **false**. letters is **["a","c"]**, size **2**.',
    ),
    S(
        "clear",
        "clear() — listed, no Tryit",
        [
            "`clear()` removes **all** elements. size becomes **0**.",
        ],
        f"{LETTERS}\nletters.clear();",
        [("letters.size", "letters.size"), ("Array.from(letters)", jsf("letters"))],
        "After `clear()`, size is **0** and `Array.from` is **[]**.",
    ),
]


# ---------------------------------------------------------------------------
# 12.3 JS Set Logic
# ---------------------------------------------------------------------------

SET_LOGIC = [
    S(
        "union",
        "union()",
        [
            "`A.union(B)` is a **new** Set of values in A, in B, or in both.",
            "A and B are not mutated.",
        ],
        f"{AB}\nconst C = A.union(B);",
        [
            ("Array.from(C)", jsf("C")),
            ("Array.from(A)", jsf("A")),
            ("Array.from(B)", jsf("B")),
        ],
        'C is **["a","b","c","d"]**. A stays **["a","b","c"]**. B stays **["b","c","d"]**.',
    ),
    S(
        "intersection",
        "intersection()",
        [
            "`A.intersection(B)` is values that are in **both** A and B.",
        ],
        f"{AB}\nconst C = A.intersection(B);",
        [("Array.from(C)", jsf("C"))],
        'C is **["b","c"]**.',
    ),
    S(
        "difference",
        "difference()",
        [
            "`A.difference(B)` is values in **A but not B** (order of the call matters).",
        ],
        f"{AB}\nconst C = A.difference(B);",
        [
            ("Array.from(A.difference(B))", jsf("A.difference(B)")),
            ("Array.from(B.difference(A))", jsf("B.difference(A)")),
        ],
        '`A.difference(B)` is **["a"]**. `B.difference(A)` is **["d"]**.',
    ),
    S(
        "symmetric-difference",
        "symmetricDifference()",
        [
            "`A.symmetricDifference(B)` is values in A or B **but not both**.",
        ],
        f"{AB}\nconst C = A.symmetricDifference(B);",
        [("Array.from(C)", jsf("C"))],
        'C is **["a","d"]**.',
    ),
    S(
        "is-subset-of",
        "isSubsetOf() — page Tryit",
        [
            "`A.isSubsetOf(B)` is **true** only if **every** value in A is also in B.",
            "The page uses A = a,b,c and B = b,c,d.",
        ],
        f"{AB}\nconst answer = A.isSubsetOf(B);",
        [
            ("A.isSubsetOf(B)", "A.isSubsetOf(B)"),
            ("Array.from(A)", jsf("A")),
            ("Array.from(B)", jsf("B")),
        ],
        "`A.isSubsetOf(B)` is **false** because **\"a\"** is not in B.",
    ),
    S(
        "is-superset-of",
        "isSupersetOf() — page Tryit",
        [
            "`A.isSupersetOf(B)` is **true** only if **every** value in B is also in A.",
        ],
        f"{AB}\nconst answer = A.isSupersetOf(B);",
        [("A.isSupersetOf(B)", "A.isSupersetOf(B)")],
        "`A.isSupersetOf(B)` is **false** because **\"d\"** is not in A.",
    ),
    S(
        "is-disjoint-from",
        "isDisjointFrom() — page Tryit",
        [
            "`A.isDisjointFrom(B)` is **true** only if A and B share **no** values.",
        ],
        f"{AB}\nconst answer = A.isDisjointFrom(B);",
        [("A.isDisjointFrom(B)", "A.isDisjointFrom(B)")],
        "`A.isDisjointFrom(B)` is **false** because they share **\"b\"** and **\"c\"**.",
    ),
    S(
        "is-subset-of-true",
        "isSubsetOf() true case",
        [
            "The page Tryit is **false**. A smaller Set **is** a subset.",
        ],
        'const A = new Set(["b","c"]);\nconst B = new Set(["a","b","c"]);\nconst answer = A.isSubsetOf(B);',
        [
            ("A.isSubsetOf(B)", "A.isSubsetOf(B)"),
            ("B.isSubsetOf(A)", "B.isSubsetOf(A)"),
        ],
        "`A.isSubsetOf(B)` is **true**. `B.isSubsetOf(A)` is **false**.",
    ),
    S(
        "is-superset-of-true",
        "isSupersetOf() true case",
        [
            "A is a superset of C when C’s values are **all** in A.",
        ],
        'const A = new Set(["a","b","c"]);\nconst C = new Set(["b","c"]);\nconst answer = A.isSupersetOf(C);',
        [
            ("A.isSupersetOf(C)", "A.isSupersetOf(C)"),
            ("C.isSupersetOf(A)", "C.isSupersetOf(A)"),
        ],
        "`A.isSupersetOf(C)` is **true**. `C.isSupersetOf(A)` is **false**.",
    ),
    S(
        "is-disjoint-from-true",
        "isDisjointFrom() true case",
        [
            "No shared values means **disjoint**.",
        ],
        'const A = new Set(["a","b","c"]);\nconst Z = new Set(["z"]);\nconst answer = A.isDisjointFrom(Z);',
        [
            ("A.isDisjointFrom(Z)", "A.isDisjointFrom(Z)"),
            ('A.isDisjointFrom(new Set(["a"]))', 'A.isDisjointFrom(new Set(["a"]))'),
        ],
        "`A.isDisjointFrom({z})` is **true**. Sharing **\"a\"** makes it **false**.",
    ),
]


# ---------------------------------------------------------------------------
# 12.4 JS WeakSet
# ---------------------------------------------------------------------------

WEAKSET = [
    S(
        "new-weakset",
        "new WeakSet()",
        [
            "`new WeakSet()` creates an empty WeakSet.",
            "Values **must be objects** (or unregistered symbols). The Set holds them **weakly**.",
        ],
        "const mySet = new WeakSet();",
        [
            ("typeof mySet", "typeof mySet"),
            ("mySet instanceof WeakSet", "mySet instanceof WeakSet"),
        ],
        "`typeof` is **object**. `instanceof WeakSet` is **true**.",
    ),
    S(
        "add-has",
        "add(object) then has(object)",
        [
            "`add(obj)` stores the object. `has(obj)` is **true** while that same reference is in the WeakSet.",
        ],
        f"const mySet = new WeakSet();\n{JOHN}\nmySet.add(myObj);\nconst answer = mySet.has(myObj);",
        [("answer", "answer"), ("mySet.has(myObj)", "mySet.has(myObj)")],
        "`has(myObj)` is **true** after `add(myObj)`.",
    ),
    S(
        "delete-has",
        "delete(object) then has(object)",
        [
            "`delete(obj)` removes that object. `has(obj)` is then **false**.",
        ],
        f"const mySet = new WeakSet();\n{JOHN}\nmySet.add(myObj);\nmySet.delete(myObj);\nconst answer = mySet.has(myObj);",
        [
            ("answer", "answer"),
            ("mySet.delete(myObj)", "mySet.delete(myObj)"),
        ],
        "After delete, `has(myObj)` is **false**. A second `delete(myObj)` is also **false**.",
    ),
    S(
        "has-other-object",
        "has() is by reference",
        [
            "Two objects with the same fields are **not** the same WeakSet value.",
        ],
        'const mySet = new WeakSet();\nconst a = {fname:"John", lname:"Doe"};\nconst b = {fname:"John", lname:"Doe"};\nmySet.add(a);',
        [("mySet.has(a)", "mySet.has(a)"), ("mySet.has(b)", "mySet.has(b)")],
        "`has(a)` is **true**. `has(b)` is **false** — `b` was never added.",
    ),
    S(
        "primitive-throws",
        "Primitives throw on add()",
        [
            "Strings, numbers, and `null` **cannot** be WeakSet values.",
            "V8 throws **TypeError: Invalid value used in weak set**.",
        ],
        'const mySet = new WeakSet();\nconst obj = {x: 1};\nmySet.add(obj);\nmySet.add("hello");',
        outcome=(
            '`add(obj)` works (`has` **true**). `add("hello")` and `add(42)` throw '
            "**TypeError: Invalid value used in weak set**. `add(null)` throws the same."
        ),
        script=catch_script(
            "const mySet = new WeakSet();\nconst obj = {x: 1};",
            [
                ("mySet.add(obj); has", "(mySet.add(obj), mySet.has(obj))"),
                ('mySet.add("hello")', 'mySet.add("hello")'),
                ("mySet.add(42)", "mySet.add(42)"),
                ("mySet.add(null)", "mySet.add(null)"),
            ],
        ),
    ),
    S(
        "not-iterable",
        "WeakSet is not iterable",
        [
            "You **cannot** `for...of`, spread, `forEach`, or `values()` a WeakSet.",
            "That is by design: members may vanish in garbage collection.",
        ],
        "const mySet = new WeakSet();\nconst obj = {x: 1};\nmySet.add(obj);\nfor (const x of mySet) {}",
        outcome=(
            "`[...mySet]` and `for...of` throw **TypeError: mySet is not iterable**. "
            "`forEach` / `values()` throw **TypeError: mySet.forEach is not a function** "
            "(and the same for `values`)."
        ),
        script=catch_script(
            "const mySet = new WeakSet();\nconst obj = {x: 1};\nmySet.add(obj);",
            [
                ("[...mySet]", "[...mySet]"),
                (
                    "for...of",
                    "(function () { for (const x of mySet) {} return 'looped'; })()",
                ),
                ("mySet.forEach(fn)", "mySet.forEach(function () {})"),
                ("mySet.values()", "mySet.values()"),
            ],
        ),
    ),
    S(
        "no-size-clear-union",
        "No size, clear(), or logic methods",
        [
            "WeakSet has **no** `size`, **no** `clear()`, **no** `union` / `intersection` / …",
        ],
        "const mySet = new WeakSet();\nmySet.size;\nmySet.clear();",
        outcome=(
            "`mySet.size` is **undefined**. `clear()` throws **TypeError: mySet.clear is not a function**. "
            "`typeof mySet.union` is **undefined**."
        ),
        script=catch_script(
            "const mySet = new WeakSet();",
            [
                ("mySet.size", "mySet.size"),
                ("typeof mySet.clear", "typeof mySet.clear"),
                ("mySet.clear()", "mySet.clear()"),
                ("typeof mySet.union", "typeof mySet.union"),
            ],
        ),
    ),
    S(
        "track-visitors",
        "Track visitors with WeakSet",
        [
            "A WeakSet is handy for **membership** (seen / not seen) without extra data.",
            "The page concatenates with **no space** after `age`.",
        ],
        (
            'let text = "";\n'
            "const persons = new WeakSet();\n"
            'const John = {name:"John", age:40};\n'
            'const Paul = {name:"Paul", age:41};\n'
            'const Ringo = {name:"Ringo", age:42};\n'
            'const George = {name:"George", age:43};\n'
            "function track(visitor) {\n"
            "  if (persons.has(visitor)) {\n"
            '    text += visitor.name + " is visiting again. ";\n'
            "  } else {\n"
            "    persons.add(visitor);\n"
            '    text += visitor.name + ", age" + visitor.age + ", is visiting for the first time ";\n'
            "  }\n"
            "}\n"
            "track(Paul);\n"
            "track(Ringo);\n"
            "track(Paul);"
        ),
        [
            ("text", "text"),
            ("persons.has(Paul)", "persons.has(Paul)"),
            ("persons.has(John)", "persons.has(John)"),
        ],
        (
            'text is **"Paul, age41, is visiting for the first time Ringo, age42, is visiting for the first time '
            'Paul is visiting again. "** (page spacing). '
            "`has(Paul)` is **true**. `has(John)` is **false** — John never called `track`."
        ),
    ),
    S(
        "gc-null",
        "Dropping the only reference (GC)",
        [
            "If nothing else points at the object, it **may** be garbage collected and dropped from the WeakSet.",
            "You cannot list remaining members. `has(null)` is invalid.",
        ],
        (
            "const mySet = new WeakSet();\n"
            f"{JOHN}\n"
            "mySet.add(myObj);\n"
            "const held = mySet.has(myObj);\n"
            "myObj = null;"
        ),
        outcome=(
            "While the binding existed, `has` was **true**. After `myObj = null`, the variable is **null**. "
            "`has(null)` throws **TypeError: Invalid value used in weak set**. "
            "`[...mySet]` throws **TypeError: mySet is not iterable**. GC itself is **not** observable in the same turn."
        ),
        script=catch_script(
            (
                "const mySet = new WeakSet();\n"
                'let myObj = {fname:"John", lname:"Doe"};\n'
                "mySet.add(myObj);\n"
                "const held = mySet.has(myObj);\n"
                "myObj = null;"
            ),
            [
                ("held before null", "held"),
                ("myObj after", "myObj"),
                ("mySet.has(null)", "mySet.has(null)"),
                ("[...mySet]", "[...mySet]"),
            ],
        ),
    ),
]


# ---------------------------------------------------------------------------
# 12.5 JS Set Reference (every table row)
# ---------------------------------------------------------------------------

def _set_logic_ref(stem: str, method: str, meaning: str, result: str, extra_displays=None, extra_code="") -> dict:
    displays = [("Array.from(C)", jsf("C"))]
    if extra_displays:
        displays.extend(extra_displays)
    return S(
        stem,
        f"{method}()",
        [f"`{method}()` {meaning}.", "Fixed A = a,b,c and B = b,c,d (same as the logic page)."],
        f"{AB}\nconst C = A.{method}(B);{extra_code}",
        displays,
        result,
    )


SET_REF = [
    S(
        "new-set",
        "new Set() — creates a new set",
        ["`new Set()` with an array copies unique values."],
        LETTERS,
        [("Array.from(letters)", jsf("letters")), ("letters.size", "letters.size")],
        '**["a","b","c"]**, size **3**.',
    ),
    S(
        "add",
        "add() — adds a new element",
        ["`add()` inserts a value and returns the **same** Set (chainable)."],
        f'{LETTERS}\nconst ret = letters.add("d");',
        [
            ("Array.from(letters)", jsf("letters")),
            ("ret === letters", "ret === letters"),
        ],
        'letters is **["a","b","c","d"]**. `add` returned the **same** Set (**true**).',
    ),
    S(
        "clear",
        "clear() — removes all elements",
        ["`clear()` empties the Set."],
        f"{LETTERS}\nletters.clear();",
        [("letters.size", "letters.size"), ("Array.from(letters)", jsf("letters"))],
        "size **0**, **[]**.",
    ),
    S(
        "delete",
        "delete() — removes an element",
        ["`delete(value)` returns whether the value **was** present."],
        f'{LETTERS}\nconst ok = letters.delete("b");',
        [
            ("ok", "ok"),
            ("Array.from(letters)", jsf("letters")),
            ('letters.delete("b") again', 'letters.delete("b")'),
        ],
        'First `delete("b")` is **true**, letters **["a","c"]**. Second delete is **false**.',
    ),
    _set_logic_ref(
        "difference",
        "difference",
        "returns values in this Set but not the argument Set",
        'C is **["a"]**.',
    ),
    S(
        "entries",
        "entries() — [value, value] pairs",
        ["`entries()` yields **[value, value]** so Sets match Maps."],
        f"{LETTERS}\nconst pairs = Array.from(letters.entries());",
        [("pairs", "JSON.stringify(pairs)")],
        'pairs is **[["a","a"],["b","b"],["c","c"]]**.',
    ),
    S(
        "for-each",
        "forEach() — callback per element",
        ["`forEach` invokes a callback once per value."],
        f'{LETTERS}\nlet text = "";\nletters.forEach(function (value) {{\n  text += value;\n}});',
        [("text", "text")],
        'text is **"abc"**.',
    ),
    S(
        "has",
        "has() — true if a value exists",
        ["`has(value)` is a boolean membership test."],
        f'{LETTERS}\nletters.has("b");\nletters.has("z");',
        [('letters.has("b")', 'letters.has("b")'), ('letters.has("z")', 'letters.has("z")')],
        '`has("b")` is **true**. `has("z")` is **false**.',
    ),
    _set_logic_ref(
        "intersection",
        "intersection",
        "returns values in both Sets",
        'C is **["b","c"]**.',
    ),
    S(
        "is-disjoint-from",
        "isDisjointFrom() — no elements in common",
        ["Returns **true** if the two Sets share nothing."],
        f"{AB}\nconst overlap = A.isDisjointFrom(B);\nconst split = A.isDisjointFrom(new Set(['z']));",
        [
            ("A.isDisjointFrom(B)", "A.isDisjointFrom(B)"),
            ("A.isDisjointFrom({z})", "A.isDisjointFrom(new Set(['z']))"),
        ],
        "Overlap with B is **false**. Disjoint from `{z}` is **true**.",
    ),
    S(
        "is-subset-of",
        "isSubsetOf() — all elements are in the other Set",
        ["Returns **true** if this Set’s values are all in the argument."],
        f"{AB}\nconst small = new Set(['b','c']);",
        [
            ("A.isSubsetOf(B)", "A.isSubsetOf(B)"),
            ("small.isSubsetOf(A)", "small.isSubsetOf(A)"),
        ],
        "A ⊂ B is **false**. `{b,c} ⊂ A` is **true**.",
    ),
    S(
        "is-superset-of",
        "isSupersetOf() — contains the other Set",
        ["Returns **true** if every argument value is also in this Set."],
        f"{AB}\nconst small = new Set(['b','c']);",
        [
            ("A.isSupersetOf(B)", "A.isSupersetOf(B)"),
            ("A.isSupersetOf(small)", "A.isSupersetOf(small)"),
        ],
        "A ⊃ B is **false**. A ⊃ `{b,c}` is **true**.",
    ),
    S(
        "keys",
        "keys() — same as values()",
        ["`keys()` equals `values()` so Sets are Map-compatible."],
        f"{LETTERS}\nconst same = Array.from(letters.keys()).join() === Array.from(letters.values()).join();",
        [
            ("Array.from(keys)", jsf("letters.keys()")),
            ("keys === values (joined)", "same"),
        ],
        'keys are **["a","b","c"]**. Joined keys and values match (**true**).',
    ),
    _set_logic_ref(
        "symmetric-difference",
        "symmetricDifference",
        "returns values in either Set but not both",
        'C is **["a","d"]**.',
    ),
    _set_logic_ref(
        "union",
        "union",
        "returns values in this Set, the argument, or both",
        'C is **["a","b","c","d"]**.',
        extra_displays=[("Array.from(A) unchanged", jsf("A"))],
    ),
    S(
        "values",
        "values() — iterator of values",
        ["`values()` iterates the Set’s values in insertion order."],
        f"{LETTERS}\nconst list = Array.from(letters.values());",
        [("list", "JSON.stringify(list)")],
        'list is **["a","b","c"]**.',
    ),
    S(
        "size",
        "size — number of elements",
        ["`size` is the only Set **property** on the table (not a method)."],
        'const mySet = new Set(["a","b","c"]);\nmySet.size;',
        [("mySet.size", "mySet.size")],
        "`size` is **3**.",
    ),
]


# ---------------------------------------------------------------------------
# 13.1 JS Maps
# ---------------------------------------------------------------------------

MAPS = [
    S(
        "empty-then-set",
        "new Map() then set()",
        [
            "Create an **empty** Map and `set(key, value)` each pair.",
            "Map keys can be **any** type. Insertion order is remembered.",
        ],
        (
            "const fruits = new Map();\n"
            'fruits.set("apples", 500);\n'
            'fruits.set("bananas", 300);\n'
            'fruits.set("oranges", 200);'
        ),
        [("Array.from(fruits)", jsf("fruits")), ("fruits.size", "fruits.size")],
        'fruits is **[["apples",500],["bananas",300],["oranges",200]]**. size **3**.',
    ),
    S(
        "new-map-array",
        "new Map(array of pairs)",
        [
            "Pass an array of **[key, value]** pairs to `new Map()`.",
        ],
        FRUITS,
        [("Array.from(fruits)", jsf("fruits")), ("fruits.size", "fruits.size")],
        "Same three pairs. size **3**.",
    ),
    S(
        "set-mangos",
        'set("mangos", 100)',
        [
            "`set()` **adds** a new key at the end if it did not exist.",
        ],
        f'{FRUITS}\nfruits.set("mangos", 100);',
        [("Array.from(fruits)", jsf("fruits")), ("fruits.size", "fruits.size")],
        'Now **[["apples",500],["bananas",300],["oranges",200],["mangos",100]]**. size **4**.',
    ),
    S(
        "change-apples",
        'set("apples", 200) — change a value',
        [
            "`set()` on an **existing** key **overwrites** the value. The key’s position stays.",
        ],
        f'{FRUITS}\nfruits.set("apples", 200);',
        [
            ('fruits.get("apples")', 'fruits.get("apples")'),
            ("Array.from(fruits)", jsf("fruits")),
        ],
        '`get("apples")` is **200**. The pairs are **[["apples",200],["bananas",300],["oranges",200]]**.',
    ),
    S(
        "get-apples",
        'get("apples")',
        [
            "`get(key)` returns the value, or **undefined** if the key is missing.",
        ],
        f'{FRUITS}\nfruits.get("apples");',
        [
            ('fruits.get("apples")', 'fruits.get("apples")'),
            ('fruits.get("kiwi")', 'fruits.get("kiwi")'),
        ],
        '`get("apples")` is **500**. `get("kiwi")` is **undefined**.',
    ),
    S(
        "typeof-object",
        "typeof a Map is object",
        [
            "`typeof` a Map is **object**, same as other objects.",
        ],
        f"{FRUITS}\ntypeof fruits;",
        [("typeof fruits", "typeof fruits")],
        "`typeof fruits` is **object**.",
    ),
    S(
        "instanceof-map",
        "instanceof Map is true",
        [
            "`fruits instanceof Map` distinguishes Maps from plain objects.",
        ],
        f"{FRUITS}\nfruits instanceof Map;",
        [("fruits instanceof Map", "fruits instanceof Map")],
        "`instanceof Map` is **true**.",
    ),
    S(
        "object-not-iterable",
        "Object vs Map — not directly iterable",
        [
            "A plain object is **not** iterable with `for...of`. A Map **is**.",
        ],
        "const obj = {apples: 500};\nconst fruits = new Map([['apples', 500]]);",
        outcome=(
            "`for...of obj` throws **TypeError: obj is not iterable**. "
            '`Array.from(fruits)` is **[["apples",500]]**.'
        ),
        script=catch_script(
            "const obj = {apples: 500};\nconst fruits = new Map([['apples', 500]]);",
            [
                (
                    "for...of obj",
                    "(function () { for (const x of obj) {} return 'looped'; })()",
                ),
                ("Array.from(fruits)", jsf("fruits")),
            ],
        ),
    ),
    S(
        "size-vs-object",
        "Object vs Map — size property",
        [
            "Maps have **`size`**. Objects do **not** (use `Object.keys(obj).length`).",
        ],
        f"{FRUITS}\nconst obj = {{apples: 500, bananas: 300, oranges: 200}};",
        [
            ("fruits.size", "fruits.size"),
            ("obj.size", "obj.size"),
            ("Object.keys(obj).length", "Object.keys(obj).length"),
        ],
        "`fruits.size` is **3**. `obj.size` is **undefined**. `Object.keys(obj).length` is **3**.",
    ),
    S(
        "keys-any-type",
        "Object vs Map — key types",
        [
            "Object keys become **strings** (or symbols). Map keys stay **any** type.",
        ],
        (
            "const obj = {};\n"
            "obj[1] = 'num';\n"
            "obj[{x: 1}] = 'obj';\n"
            "const fruits = new Map();\n"
            "const key = {x: 1};\n"
            "fruits.set(1, 'num');\n"
            "fruits.set(key, 'obj');"
        ),
        [
            ("Object.keys(obj)", "JSON.stringify(Object.keys(obj))"),
            ("obj['[object Object]']", "obj['[object Object]']"),
            ("Array.from(fruits.keys())", jsf("fruits.keys()")),
            ("fruits.get(key)", "fruits.get(key)"),
            ("fruits.get(1)", "fruits.get(1)"),
        ],
        (
            'Object.keys is **["1","[object Object]"]** — both coerced to strings. '
            "Map keys stay **1** and **{x:1}**. `get(key)` is **obj**. `get(1)` is **num**."
        ),
    ),
    S(
        "insertion-order",
        "Object vs Map — key order",
        [
            "Map iteration follows **insertion** order.",
            "Object integer keys are sorted **before** string keys.",
        ],
        (
            "const obj = {};\n"
            "obj.z = 1;\n"
            "obj.a = 2;\n"
            "obj[1] = 3;\n"
            "const fruits = new Map();\n"
            "fruits.set('z', 1);\n"
            "fruits.set('a', 2);\n"
            "fruits.set(1, 3);"
        ),
        [
            ("Object.keys(obj)", "JSON.stringify(Object.keys(obj))"),
            ("Array.from(fruits.keys())", jsf("fruits.keys()")),
        ],
        'Object.keys is **["1","z","a"]** (integer key first). Map keys are **["z","a",1]** (insertion order).',
    ),
    S(
        "no-default-keys",
        "Object vs Map — default keys",
        [
            "Objects inherit **`toString`** on the prototype. Maps do **not** have default keys.",
        ],
        "const obj = {};\nconst fruits = new Map();",
        [
            ("'toString' in obj", "'toString' in obj"),
            ("obj.hasOwnProperty('toString')", "obj.hasOwnProperty('toString')"),
            ("fruits.has('toString')", "fruits.has('toString')"),
            ("fruits.size", "fruits.size"),
        ],
        "`'toString' in obj` is **true** (prototype). `hasOwnProperty` is **false**. `fruits.has('toString')` is **false**. size **0**.",
    ),
]


# ---------------------------------------------------------------------------
# 13.2 JS Map Methods
# ---------------------------------------------------------------------------

MAP_METHODS = [
    S(
        "new-map-array",
        "new Map() from pairs",
        ["Pass `[key, value]` pairs to the constructor."],
        FRUITS,
        [("Array.from(fruits)", jsf("fruits"))],
        '**[["apples",500],["bananas",300],["oranges",200]]**.',
    ),
    S(
        "get",
        "get()",
        ["`get(key)` reads the value for that key."],
        f'{FRUITS}\nfruits.get("apples");',
        [('fruits.get("apples")', 'fruits.get("apples")')],
        '`get("apples")` is **500**.',
    ),
    S(
        "set-create",
        "set() — create and fill",
        ["`set(key, value)` adds pairs to an empty Map."],
        (
            "const fruits = new Map();\n"
            'fruits.set("apples", 500);\n'
            'fruits.set("bananas", 300);\n'
            'fruits.set("oranges", 200);'
        ),
        [("Array.from(fruits)", jsf("fruits")), ("fruits.size", "fruits.size")],
        "Three pairs, size **3**.",
    ),
    S(
        "set-change",
        'set("apples", 500) — overwrite',
        [
            "The page uses `set` to **change** an existing key.",
            "Here apples was already **500**, so the stored value stays **500**.",
        ],
        f'{FRUITS}\nfruits.set("apples", 500);',
        [
            ('fruits.get("apples")', 'fruits.get("apples")'),
            ("Array.from(fruits)", jsf("fruits")),
        ],
        '`get("apples")` is still **500**. The key was overwritten with the same number.',
    ),
    S(
        "size",
        "size",
        ["`size` is the number of key/value pairs."],
        f"{FRUITS}\nfruits.size;",
        [("fruits.size", "fruits.size")],
        "`size` is **3**.",
    ),
    S(
        "delete",
        "delete()",
        ["`delete(key)` removes that pair and returns **true** if it existed."],
        f'{FRUITS}\nconst ok = fruits.delete("apples");',
        [
            ("ok", "ok"),
            ("fruits.size", "fruits.size"),
            ("Array.from(fruits)", jsf("fruits")),
        ],
        '`delete("apples")` is **true**. size **2**. Remaining **[["bananas",300],["oranges",200]]**.',
    ),
    S(
        "clear",
        "clear()",
        ["`clear()` removes **every** pair."],
        f"{FRUITS}\nfruits.clear();",
        [("fruits.size", "fruits.size"), ("Array.from(fruits)", jsf("fruits"))],
        "size **0**, **[]**.",
    ),
    S(
        "has",
        "has()",
        ["`has(key)` is **true** if the key exists."],
        f'{FRUITS}\nfruits.has("apples");',
        [
            ('fruits.has("apples")', 'fruits.has("apples")'),
            ('fruits.has("kiwi")', 'fruits.has("kiwi")'),
        ],
        '`has("apples")` is **true**. `has("kiwi")` is **false**.',
    ),
    S(
        "delete-then-has",
        "delete() then has()",
        ["After deleting a key, `has` becomes **false**."],
        f'{FRUITS}\nfruits.delete("apples");\nfruits.has("apples");',
        [('fruits.has("apples")', 'fruits.has("apples")'), ("fruits.size", "fruits.size")],
        'After `delete("apples")`, `has("apples")` is **false**. size **2**.',
    ),
    S(
        "for-each",
        "forEach()",
        [
            "`forEach(callback)` runs per pair.",
            "The callback is **`(value, key)`** — value first, like Array, unlike `Map`’s mental [key,value] order.",
        ],
        f"""{FRUITS}
let text = "";
fruits.forEach(function (value, key) {{
  text += key + " = " + value;
}});""",
        [("text", "text")],
        'text is **"apples = 500bananas = 300oranges = 200"** (no separator between pairs).',
    ),
    S(
        "entries",
        "entries()",
        ["`entries()` yields **[key, value]** pairs. `text += pair` stringifies with a comma."],
        f"""{FRUITS}
let text = "";
for (const x of fruits.entries()) {{
  text += x;
}}""",
        [("text", "text"), ("Array.from(fruits.entries())", jsf("fruits.entries()"))],
        (
            'text is **"apples,500bananas,300oranges,200"**. '
            'Pairs are **[["apples",500],["bananas",300],["oranges",200]]**.'
        ),
    ),
    S(
        "keys",
        "keys()",
        ["`keys()` iterates the keys in insertion order."],
        f"""{FRUITS}
let text = "";
for (const x of fruits.keys()) {{
  text += x;
}}""",
        [("text", "text"), ("Array.from(fruits.keys())", jsf("fruits.keys()"))],
        'text is **"applesbananasoranges"**. keys are **["apples","bananas","oranges"]**.',
    ),
    S(
        "values",
        "values()",
        ["`values()` iterates the values."],
        f"""{FRUITS}
let text = "";
for (const x of fruits.values()) {{
  text += x;
}}""",
        [("text", "text"), ("Array.from(fruits.values())", jsf("fruits.values()"))],
        'text is **"500300200"** (string concat from `""`). values are **[500,300,200]**.',
    ),
    S(
        "values-sum",
        "sum values()",
        ["Loop `values()` with `+=` on a **number** to total them."],
        f"{FRUITS}\nlet total = 0;\nfor (const x of fruits.values()) {{\n  total += x;\n}}",
        [("total", "total")],
        "total is **1000** (500 + 300 + 200).",
    ),
    S(
        "objects-as-keys",
        "Objects as keys",
        [
            "Using **objects** as keys is a Map feature objects cannot match.",
            "The key is the object **reference**, not `name`.",
        ],
        (
            'const apples = {name: "Apples"};\n'
            'const bananas = {name: "Bananas"};\n'
            'const oranges = {name: "Oranges"};\n'
            "const fruits = new Map();\n"
            "fruits.set(apples, 500);\n"
            "fruits.set(bananas, 300);\n"
            "fruits.set(oranges, 200);"
        ),
        [
            ("Array.from(fruits)", jsf("fruits")),
            ("fruits.get(apples)", "fruits.get(apples)"),
            ("fruits.size", "fruits.size"),
        ],
        'JSON is **[[{"name":"Apples"},500],[{"name":"Bananas"},300],[{"name":"Oranges"},200]]**. `get(apples)` is **500**.',
    ),
    S(
        "get-string-undefined",
        'get("apples") when the key is an object',
        [
            'The key is the **object** `apples`, not the string **"apples"**.',
        ],
        (
            'const apples = {name: "Apples"};\n'
            "const fruits = new Map();\n"
            "fruits.set(apples, 500);\n"
            'fruits.get("apples");'
        ),
        [
            ('fruits.get("apples")', 'fruits.get("apples")'),
            ("fruits.get(apples)", "fruits.get(apples)"),
        ],
        '`get("apples")` is **undefined**. `get(apples)` is **500**.',
    ),
    S(
        "group-by",
        "Map.groupBy()",
        [
            "`Map.groupBy(iterable, callback)` groups elements by the callback’s return value.",
            "The original array is **not** changed. Result is a **Map** of key → array.",
            '`quantity > 200` → **"ok"**, else **"low"**.',
        ],
        (
            "const fruits = [\n"
            '  {name:"apples", quantity:300},\n'
            '  {name:"bananas", quantity:500},\n'
            '  {name:"oranges", quantity:200},\n'
            '  {name:"kiwi", quantity:150}\n'
            "];\n"
            "function myCallback({ quantity }) {\n"
            '  return quantity > 200 ? "ok" : "low";\n'
            "}\n"
            "const result = Map.groupBy(fruits, myCallback);"
        ),
        [
            ("Array.from(result)", jsf("result")),
            ("result instanceof Map", "result instanceof Map"),
            ("JSON.stringify(fruits) unchanged", "JSON.stringify(fruits)"),
        ],
        (
            'result is **[["ok",[{"name":"apples","quantity":300},{"name":"bananas","quantity":500}]],'
            '["low",[{"name":"oranges","quantity":200},{"name":"kiwi","quantity":150}]]]**. '
            "`instanceof Map` is **true**. The input array is unchanged."
        ),
    ),
    S(
        "object-group-by",
        "Object.groupBy() vs Map.groupBy()",
        [
            "The page names **`Object.groupBy()`**: same grouping, result is a **plain object**.",
            "No Tryit — still run it on the same fruit list.",
        ],
        (
            "const fruits = [\n"
            '  {name:"apples", quantity:300},\n'
            '  {name:"bananas", quantity:500},\n'
            '  {name:"oranges", quantity:200},\n'
            '  {name:"kiwi", quantity:150}\n'
            "];\n"
            "function myCallback({ quantity }) {\n"
            '  return quantity > 200 ? "ok" : "low";\n'
            "}\n"
            "const obj = Object.groupBy(fruits, myCallback);\n"
            "const map = Map.groupBy(fruits, myCallback);"
        ),
        [
            ("JSON.stringify(obj)", "JSON.stringify(obj)"),
            ("obj instanceof Map", "obj instanceof Map"),
            ("map instanceof Map", "map instanceof Map"),
        ],
        (
            'Object.groupBy JSON is **{"ok":[{"name":"apples","quantity":300},{"name":"bananas","quantity":500}],'
            '"low":[{"name":"oranges","quantity":200},{"name":"kiwi","quantity":150}]}**. '
            "`obj instanceof Map` is **false**. `map instanceof Map` is **true**."
        ),
    ),
]


# ---------------------------------------------------------------------------
# 13.3 JS WeakMap
# ---------------------------------------------------------------------------

WEAKMAP = [
    S(
        "new-weakmap",
        "new WeakMap()",
        [
            "`new WeakMap()` creates an empty WeakMap.",
            "Keys **must be objects** (or unregistered symbols). Keys are held **weakly**.",
        ],
        "const myMap = new WeakMap();",
        [
            ("typeof myMap", "typeof myMap"),
            ("myMap instanceof WeakMap", "myMap instanceof WeakMap"),
        ],
        "`typeof` is **object**. `instanceof WeakMap` is **true**.",
    ),
    S(
        "set-get",
        "set() then get()",
        [
            "`set(obj, value)` stores a pair. `get(obj)` reads it back.",
        ],
        f'const myMap = new WeakMap();\n{JOHN}\nmyMap.set(myObj, "player");\nconst type = myMap.get(myObj);',
        [("type", "type"), ("myMap.get(myObj)", "myMap.get(myObj)")],
        '`get(myObj)` is **"player"**.',
    ),
    S(
        "has",
        "has(key)",
        ["`has(obj)` is **true** while that object is a key."],
        f'const myMap = new WeakMap();\n{JOHN}\nmyMap.set(myObj, "player");',
        [
            ("myMap.has(myObj)", "myMap.has(myObj)"),
            ("myMap.has({fname:'John', lname:'Doe'})", "myMap.has({fname:'John', lname:'Doe'})"),
        ],
        "`has(myObj)` is **true**. `has` of a **new** look-alike object is **false**.",
    ),
    S(
        "delete",
        "delete(key)",
        ["`delete(obj)` removes that pair."],
        f'const myMap = new WeakMap();\n{JOHN}\nmyMap.set(myObj, "player");\nconst ok = myMap.delete(myObj);',
        [
            ("ok", "ok"),
            ("myMap.has(myObj)", "myMap.has(myObj)"),
            ("String(myMap.get(myObj))", "String(myMap.get(myObj))"),
        ],
        "`delete` returns **true**. Then `has` is **false** and `get` is **undefined**.",
    ),
    S(
        "primitive-and-symbols",
        "Keys: objects / unregistered symbols; primitives throw",
        [
            "The page: keys must be **objects or non-registered symbols**.",
            "Strings throw. `Symbol.for` (registered) throws. `Symbol('x')` **works**.",
        ],
        (
            "const myMap = new WeakMap();\n"
            "const obj = {x: 1};\n"
            "const unique = Symbol('x');\n"
            "myMap.set(obj, 'obj');\n"
            "myMap.set(unique, 'sym');\n"
            'myMap.set("nope", 1);'
        ),
        outcome=(
            '`get(obj)` is **"obj"**. `get(unique)` is **"sym"**. '
            '`set("nope", 1)` and `set(Symbol.for("x"), 1)` throw '
            "**TypeError: Invalid value used as weak map key**."
        ),
        script=catch_script(
            (
                "const myMap = new WeakMap();\n"
                "const obj = {x: 1};\n"
                "const unique = Symbol('x');"
            ),
            [
                ("set/get object", "(myMap.set(obj, 'obj'), myMap.get(obj))"),
                ("set/get Symbol('x')", "(myMap.set(unique, 'sym'), myMap.get(unique))"),
                ('set("nope", 1)', 'myMap.set("nope", 1)'),
                ("set(Symbol.for('x'), 1)", "myMap.set(Symbol.for('x'), 1)"),
            ],
        ),
    ),
    S(
        "not-iterable",
        "WeakMap is not iterable",
        [
            "No `for...of`, `forEach`, or `keys()` on a WeakMap.",
        ],
        'const myMap = new WeakMap();\nconst obj = {x: 1};\nmyMap.set(obj, "v");\nfor (const x of myMap) {}',
        outcome=(
            "`[...myMap]` / `for...of` throw **TypeError: myMap is not iterable**. "
            "`forEach` and `keys()` throw **TypeError: myMap.forEach is not a function** "
            "(same pattern for `keys`)."
        ),
        script=catch_script(
            'const myMap = new WeakMap();\nconst obj = {x: 1};\nmyMap.set(obj, "v");',
            [
                ("[...myMap]", "[...myMap]"),
                (
                    "for...of",
                    "(function () { for (const x of myMap) {} return 'looped'; })()",
                ),
                ("myMap.forEach(fn)", "myMap.forEach(function () {})"),
                ("myMap.keys()", "myMap.keys()"),
            ],
        ),
    ),
    S(
        "no-size-clear",
        "No size and no clear()",
        [
            "You cannot read `size` or `clear()` a WeakMap.",
        ],
        "const myMap = new WeakMap();\nmyMap.size;\nmyMap.clear();",
        outcome=(
            "`myMap.size` is **undefined**. `clear()` throws "
            "**TypeError: myMap.clear is not a function**."
        ),
        script=catch_script(
            "const myMap = new WeakMap();",
            [
                ("myMap.size", "myMap.size"),
                ("myMap.clear()", "myMap.clear()"),
            ],
        ),
    ),
    S(
        "track-visitors",
        "Track visit counts with WeakMap",
        [
            "Store **counts** on object keys without pinning those objects forever.",
        ],
        (
            'let text = "";\n'
            "const visitsCount = new WeakMap();\n"
            'const John = {name:"John", age:40};\n'
            'const Paul = {name:"Paul", age:41};\n'
            'const Ringo = {name:"Ringo", age:42};\n'
            'const George = {name:"George", age:43};\n'
            "function track(visitor) {\n"
            "  let count = visitsCount.get(visitor) || 0;\n"
            "  count++;\n"
            "  visitsCount.set(visitor, count);\n"
            '  text += visitor.name + ", age " + visitor.age + ", has visited " + count + " time(s). ";\n'
            "}\n"
            "track(Paul);\n"
            "track(Ringo);\n"
            "track(Paul);\n"
            "track(Paul);\n"
            "track(John);"
        ),
        [
            ("text", "text"),
            ("visitsCount.get(Paul)", "visitsCount.get(Paul)"),
            ("visitsCount.get(George)", "String(visitsCount.get(George))"),
        ],
        (
            'text is **"Paul, age 41, has visited 1 time(s). Ringo, age 42, has visited 1 time(s). '
            "Paul, age 41, has visited 2 time(s). Paul, age 41, has visited 3 time(s). "
            'John, age 40, has visited 1 time(s). "**. '
            "`get(Paul)` is **3**. `get(George)` is **undefined**."
        ),
    ),
    S(
        "secret-data",
        "WeakMap secret data on a class",
        [
            "The page simulates private fields: `myMap.set(this, {secret})`.",
            "`user1` **is** the constructor’s `this`, so `myMap.get(user1)` also works when `myMap` is in scope.",
            "Privacy is **no enumeration**: you cannot list keys you do not already hold.",
        ],
        (
            "const myMap = new WeakMap();\n"
            "class User {\n"
            "  constructor(name) {\n"
            '    myMap.set(this, {secret:"hidden data"});\n'
            "    this.name = name;\n"
            "  }\n"
            "  getSecret() {\n"
            "    return myMap.get(this).secret;\n"
            "  }\n"
            "}\n"
            'const user1 = new User("John");\n'
            "const secret = user1.getSecret();"
        ),
        outcome=(
            '`getSecret()` is **"hidden data"**. `myMap.get(user1).secret` is also **"hidden data"** '
            "(same object key). `[...myMap]` throws **TypeError: myMap is not iterable**. "
            "`Array.from(myMap)` is **[]** (non-iterable objects become an empty array — not a leak)."
        ),
        script=catch_script(
            (
                "const myMap = new WeakMap();\n"
                "class User {\n"
                "  constructor(name) {\n"
                '    myMap.set(this, {secret:"hidden data"});\n'
                "    this.name = name;\n"
                "  }\n"
                "  getSecret() {\n"
                "    return myMap.get(this).secret;\n"
                "  }\n"
                "}\n"
                'const user1 = new User("John");'
            ),
            [
                ("user1.getSecret()", "user1.getSecret()"),
                ("myMap.get(user1).secret", "myMap.get(user1).secret"),
                ("[...myMap]", "[...myMap]"),
                ("Array.from(myMap)", "JSON.stringify(Array.from(myMap))"),
            ],
        ),
    ),
    S(
        "gc-null",
        "Dropping the only key reference (GC)",
        [
            "After `myObj = null`, you no longer have the key. The pair **may** be collected.",
            "`get(null)` / `has(null)` are invalid keys.",
        ],
        (
            "const myMap = new WeakMap();\n"
            f"{JOHN}\n"
            'myMap.set(myObj, "secret");\n'
            "const held = myMap.get(myObj);\n"
            "myObj = null;"
        ),
        outcome=(
            'Before nulling, `get` was **"secret"**. After, `myObj` is **null**. '
            "`get(null)` throws **TypeError: Invalid value used as weak map key**. "
            "You cannot iterate to see leftover pairs. GC is not immediate."
        ),
        script=catch_script(
            (
                "const myMap = new WeakMap();\n"
                'let myObj = {fname:"John", lname:"Doe"};\n'
                'myMap.set(myObj, "secret");\n'
                "const held = myMap.get(myObj);\n"
                "myObj = null;"
            ),
            [
                ("held before null", "held"),
                ("myObj after", "myObj"),
                ("myMap.get(null)", "myMap.get(null)"),
                ("[...myMap]", "[...myMap]"),
            ],
        ),
    ),
]


# ---------------------------------------------------------------------------
# 13.4 JS Map Reference (every table row)
# ---------------------------------------------------------------------------

MAP_REF = [
    S(
        "new-map",
        "new Map() — creates a new Map object",
        ["Construct from an array of pairs."],
        FRUITS,
        [("Array.from(fruits)", jsf("fruits")), ("fruits.size", "fruits.size")],
        '**[["apples",500],["bananas",300],["oranges",200]]**, size **3**.',
    ),
    S(
        "clear",
        "clear() — removes all elements",
        ["Empties the Map."],
        f"{FRUITS}\nfruits.clear();",
        [("fruits.size", "fruits.size"), ("Array.from(fruits)", jsf("fruits"))],
        "size **0**, **[]**.",
    ),
    S(
        "delete",
        "delete() — removes a Map element by key",
        ["Returns whether the key existed."],
        f'{FRUITS}\nconst ok = fruits.delete("apples");',
        [("ok", "ok"), ("Array.from(fruits)", jsf("fruits"))],
        '`delete("apples")` is **true**. Remaining **[["bananas",300],["oranges",200]]**.',
    ),
    S(
        "entries",
        "entries() — [key, value] iterator",
        ["Yields each pair as a two-element array."],
        f"{FRUITS}\nconst pairs = Array.from(fruits.entries());",
        [("pairs", "JSON.stringify(pairs)")],
        '**[["apples",500],["bananas",300],["oranges",200]]**.',
    ),
    S(
        "for-each",
        "forEach() — callback per pair",
        ["Callback arguments are `(value, key)`."],
        f"""{FRUITS}
let text = "";
fruits.forEach(function (value, key) {{
  text += key + "=" + value + ";";
}});""",
        [("text", "text")],
        'text is **"apples=500;bananas=300;oranges=200;"**.',
    ),
    S(
        "get",
        "get() — value for a key",
        ["Missing keys return **undefined**."],
        f'{FRUITS}\nfruits.get("bananas");',
        [
            ('fruits.get("bananas")', 'fruits.get("bananas")'),
            ('fruits.get("kiwi")', 'String(fruits.get("kiwi"))'),
        ],
        '`get("bananas")` is **300**. `get("kiwi")` is **undefined**.',
    ),
    S(
        "group-by",
        "groupBy() — Map.groupBy",
        ["Static `Map.groupBy` groups an iterable by callback results."],
        (
            "const fruits = [\n"
            '  {name:"apples", quantity:300},\n'
            '  {name:"bananas", quantity:500},\n'
            '  {name:"oranges", quantity:200},\n'
            '  {name:"kiwi", quantity:150}\n'
            "];\n"
            "function myCallback({ quantity }) {\n"
            '  return quantity > 200 ? "ok" : "low";\n'
            "}\n"
            "const result = Map.groupBy(fruits, myCallback);"
        ),
        [
            ("Array.from(result.keys())", jsf("result.keys()")),
            ("result.get('ok').length", "result.get('ok').length"),
            ("result.get('low').length", "result.get('low').length"),
        ],
        'keys are **["ok","low"]**. **"ok"** has **2** fruits (apples, bananas). **"low"** has **2** (oranges, kiwi).',
    ),
    S(
        "has",
        "has() — whether a key exists",
        ["Boolean membership on the **key**."],
        f'{FRUITS}\nfruits.has("oranges");',
        [
            ('fruits.has("oranges")', 'fruits.has("oranges")'),
            ('fruits.has("kiwi")', 'fruits.has("kiwi")'),
        ],
        '`has("oranges")` is **true**. `has("kiwi")` is **false**.',
    ),
    S(
        "keys",
        "keys() — key iterator",
        ["Insertion-order keys."],
        f"{FRUITS}\nconst list = Array.from(fruits.keys());",
        [("list", "JSON.stringify(list)")],
        '**["apples","bananas","oranges"]**.',
    ),
    S(
        "set",
        "set() — set the value for a key",
        ["Adds or overwrites. Returns the **same** Map."],
        f'{FRUITS}\nconst ret = fruits.set("apples", 200);',
        [
            ('fruits.get("apples")', 'fruits.get("apples")'),
            ("ret === fruits", "ret === fruits"),
            ("Array.from(fruits)", jsf("fruits")),
        ],
        '`get("apples")` is **200**. `set` returned the same Map (**true**).',
    ),
    S(
        "size",
        "size — number of Map elements",
        ["Listed on the method table; it is a **property**."],
        f"{FRUITS}\nfruits.size;",
        [("fruits.size", "fruits.size")],
        "`size` is **3**.",
    ),
    S(
        "values",
        "values() — value iterator",
        ["Insertion-order values."],
        f"{FRUITS}\nconst list = Array.from(fruits.values());",
        [("list", "JSON.stringify(list)")],
        "**[500,300,200]**.",
    ),
]


def run_all() -> None:
    sections = [
        (
            "js-sets",
            "JS Sets",
            SETS,
            "A JavaScript Set is a collection of unique values. Each value occurs at most once. Create a Set by passing an array to new Set(), or start empty and add(). Values may be primitives or objects. Objects are compared by reference, so two {x:1} literals are two entries. Sets are iterable with for...of. typeof a Set is object; instanceof Set is true.",
            [
                "A Set holds **unique** values in **insertion** order.",
                "`new Set(array)` or `new Set()` plus `add()`.",
                "Duplicates from `add()` are ignored — size does not grow.",
                "`for...of` concatenating `a`,`b`,`c` with no separator is **abc**.",
                "`typeof` → **object**. `instanceof Set` → **true**.",
                "`1` and `\"1\"` are different. The same object added twice is one entry; two similar objects are two.",
            ],
            [
                ('What is in `new Set(["a","b","c"])`?', ['**["a","b","c"]**. size **3**.']),
                ("Does starting empty and add() match the array constructor?", ["**Yes** — still **a, b, c**."]),
                ("What happens if you add variables a, b, c holding those strings?", ["The Set still stores **\"a\"**, **\"b\"**, **\"c\"**."]),
                ('What is `letters` after add("d") and add("e")?', ['**["a","b","c","d","e"]**, size **5**.']),
                ('What if you `add("c")` six times?', ["Still **3** values. Extra adds are ignored."]),
                ("What does `for...of` concatenation produce?", ['**"abc"** — no commas or spaces.']),
                ("What is `typeof letters`?", ["**object**."]),
                ("What is `letters instanceof Set`?", ["**true**."]),
                ('Are `1` and `"1"` the same Set value?', ["**No.** Mixed example size is **3**: number, string, one object."]),
                ("Are two `{x:1}` objects one Set value?", ["**No.** size **2** — reference equality."]),
            ],
            "Use a Set when membership and uniqueness matter. Build from an array or add() into an empty Set. Duplicates do not land. Iterate with for...of. Check the type with instanceof Set, not typeof.",
            [
                ("JS Sets (W3Schools)", "https://www.w3schools.com/js/js_sets.asp"),
                ("MDN: Set", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set"),
            ],
        ),
        (
            "js-set-methods",
            "JS Set Methods",
            SET_METHODS,
            "Set methods cover create, add, size, has, iteration, and the Map-compatible keys/values/entries trio. values() and keys() yield the same values. entries() yields [value, value] pairs so a Set can be treated like a Map. delete() and clear() are listed on the page without Tryits and still each get an Example. has('d') on {a,b,c} is false.",
            [
                "`size` is an element count, not `length`.",
                "`has('d')` on `{a,b,c}` is **false**; `has('a')` is **true**.",
                "`forEach` and `for...of` both walk values → **abc**.",
                "`keys()` === `values()`. `entries()` → **[value, value]**.",
                '`text += entry` on entries stringifies to **"a,ab,bc,c"**.',
                '`delete("b")` → **true**, leftover **["a","c"]**. `clear()` → size **0**.',
            ],
            [
                ("What does `size` report for a,b,c?", ["**3**."]),
                ('What is `has("d")` on that Set?', ["**false**. `has(\"a\")` is **true**."]),
                ("What does forEach concatenate?", ['**"abc"**.' ]),
                ("Do keys() and values() differ on a Set?", ["**No.** Both yield **a, b, c** so Sets match Maps."]),
                ("What does entries() yield?", ['**[value, value]** pairs: **[["a","a"],["b","b"],["c","c"]]**.']),
                ('Why is entries concatenation **"a,ab,bc,c"**?', ["Each pair’s `toString()` is `a,a` (comma). The next pair is glued on with no separator."]),
                ('What does `delete("b")` return?', ["**true**, leftover **[\"a\",\"c\"]**. Deleting a missing **\"z\"** returns **false**."]),
                ("What does clear() leave?", ["size **0**, **[]**."]),
                ("Does add() keep duplicates?", ["**No.** size stays **3** after many `add(\"c\")`."]),
                ("Why do Sets have keys()?", ["Map compatibility — a Set has no real keys, so keys are the values."]),
            ],
            "has/add/delete/clear plus size cover membership. forEach, values, keys, and entries cover walking. Remember entries are [value, value], and adding a pair array to a string uses comma joins.",
            [
                ("JS Set Methods (W3Schools)", "https://www.w3schools.com/js/js_set_methods.asp"),
                ("MDN: Set", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set"),
                ("MDN: Set.prototype.entries", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/entries"),
            ],
        ),
        (
            "js-set-logic",
            "JS Set Logic",
            SET_LOGIC,
            "ECMAScript 2025 added seven Set logic methods. union, intersection, difference, and symmetricDifference return new Sets and leave the originals alone. isSubsetOf, isSupersetOf, and isDisjointFrom return booleans. The page Tryits all use A = {a,b,c} and B = {b,c,d}, so the three booleans are false. Extra Examples show true cases.",
            [
                "A = **a,b,c**. B = **b,c,d**. Methods do **not** mutate A or B.",
                "`union` → **a,b,c,d**. `intersection` → **b,c**. `difference` (A−B) → **a**. `symmetricDifference` → **a,d**.",
                "On that pair: subset **false**, superset **false**, disjoint **false**.",
                "`{b,c}.isSubsetOf(A)` is **true**. `A.isSupersetOf({b,c})` is **true**. `A.isDisjointFrom({z})` is **true**.",
                "`B.difference(A)` is **[\"d\"]** — argument order matters.",
            ],
            [
                ("What is A.union(B)?", ['**["a","b","c","d"]**. A and B unchanged.']),
                ("What is A.intersection(B)?", ['**["b","c"]**.']),
                ("What is A.difference(B)?", ['**["a"]**. `B.difference(A)` is **["d"]**.']),
                ("What is A.symmetricDifference(B)?", ['**["a","d"]**.']),
                ("Is A a subset of B on the page?", ["**false** — **\"a\"** is not in B."]),
                ("Is A a superset of B on the page?", ["**false** — **\"d\"** is not in A."]),
                ("Are A and B disjoint on the page?", ["**false** — they share **b** and **c**."]),
                ("When is isSubsetOf true here?", ['`new Set(["b","c"]).isSubsetOf(A)` is **true**.']),
                ("When is isSupersetOf true here?", ["`A.isSupersetOf({b,c})` is **true**."]),
                ("When is isDisjointFrom true here?", ["`A.isDisjointFrom({z})` is **true**."]),
            ],
            "Logic methods return a new Set or a boolean. The tutorial’s A/B pair overlaps, so the three predicates are false until you pick a contained or disjoint argument.",
            [
                ("JS Set Logic (W3Schools)", "https://www.w3schools.com/js/js_set_logic.asp"),
                ("MDN: Set.prototype.union", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/union"),
                ("MDN: Set.prototype.intersection", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/intersection"),
            ],
        ),
        (
            "js-set-weakset",
            "JS Set WeakSet",
            WEAKSET,
            "A WeakSet holds objects weakly so they can be garbage collected when nothing else references them. add, delete, and has are the whole API. Primitives throw TypeError: Invalid value used in weak set. WeakSets are not iterable, have no size, and have no clear or logic methods. The visitor demo tracks first vs again without storing counts.",
            [
                "Values must be **objects**. `add('hello')` / `add(42)` / `add(null)` throw **Invalid value used in weak set**.",
                "`has` is **reference** equality — a look-alike object is **false**.",
                "**Not iterable:** `[...mySet]` → **mySet is not iterable**. No `forEach` / `values()`.",
                "`size` is **undefined**. `clear()` is not a function. No `union`.",
                "Visitor text matches the page: **age41** with no space after age. Paul then Ringo then Paul-again.",
                "After `myObj = null` you cannot look the object up. GC is not a synchronous snapshot.",
            ],
            [
                ("What methods does WeakSet provide?", ["**add**, **delete**, **has** (plus the constructor)."]),
                ("What does add(myObj) then has(myObj) return?", ["**true**."]),
                ("What does delete then has return?", ["**false**."]),
                ("Does has() match another object with the same fields?", ["**No.** Different reference → **false**."]),
                ("What does add('hello') throw?", ["**TypeError: Invalid value used in weak set**."]),
                ("Can you for...of a WeakSet?", ["**No.** **TypeError: mySet is not iterable**."]),
                ("What is mySet.size?", ["**undefined**."]),
                ("What is the visitor text after Paul, Ringo, Paul?", [
                    '**"Paul, age41, is visiting for the first time Ringo, age42, is visiting for the first time Paul is visiting again. "**',
                ]),
                ("Did John visit in that demo?", ["**No.** `has(John)` is **false**."]),
                ("Can you has(null) after nulling the object?", ["**No.** **Invalid value used in weak set**."]),
            ],
            "Use WeakSet for object membership you do not want to keep alive. Stick to add/delete/has. Do not iterate, count, or store primitives.",
            [
                ("JS WeakSet (W3Schools)", "https://www.w3schools.com/js/js_sets_weak.asp"),
                ("MDN: WeakSet", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet"),
            ],
        ),
        (
            "js-set-reference",
            "JS Set Reference",
            SET_REF,
            "The July 2025 Set reference lists every method plus the size property. Each table row is its own Example. Logic methods reuse A = {a,b,c} and B = {b,c,d}. Boolean methods also show a true case so the description is visible, not only the overlapping false pair.",
            [
                "**Every table row is an Example**, including `size`.",
                "`add` returns the same Set. `delete` returns a boolean. `clear` empties.",
                "A∪B **a,b,c,d**. A∩B **b,c**. A−B **a**. symmetric **a,d**.",
                "A vs B: disjoint **false**, subset **false**, superset **false**. `{b,c} ⊂ A` **true**.",
                "`keys()` matches `values()`. `entries()` is **[value,value]**.",
            ],
            [
                ("How many Set properties are on the table?", ["**One:** `size`."]),
                ("Does add() return a new Set?", ["**No.** It returns **the same** Set (**true** for `ret === letters`)."]),
                ('What is delete("b") the first vs second time?', ["**true** then leftover **[\"a\",\"c\"]**. Second call **false**."]),
                ("What is union of A and B?", ['**["a","b","c","d"]**. A unchanged.']),
                ("What is intersection?", ['**["b","c"]**.']),
                ("What is difference A−B?", ['**["a"]**.']),
                ("What is symmetricDifference?", ['**["a","d"]**.']),
                ("isSubsetOf A of B?", ["**false**. `{b,c} ⊂ A` is **true**."]),
                ("isSupersetOf A of B?", ["**false**. A ⊃ `{b,c}` is **true**."]),
                ("isDisjointFrom A and B?", ["**false**. A vs `{z}` is **true**."]),
                ("What does entries() look like?", ['**[["a","a"],["b","b"],["c","c"]]**.']),
            ],
            "Treat the reference as a catalog: construct, mutate (add/delete/clear), test (has and the three predicates), combine (union and friends), and iterate (keys/values/entries/forEach). size is the only property.",
            [
                ("JS Set Reference (W3Schools)", "https://www.w3schools.com/js/js_set_reference.asp"),
                ("MDN: Set", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set"),
            ],
        ),
        (
            "js-maps",
            "JS Maps",
            MAPS,
            "A Map stores key/value pairs. Keys may be any type, insertion order is kept, size is a property, and Maps are iterable. Create with set() on an empty Map or pass an array of pairs. set() also overwrites. get() reads a value. typeof is object; instanceof Map is true. Compared with objects: objects are not directly iterable, have no size, coerce keys to strings, reorder integer keys, and inherit default keys such as toString.",
            [
                "Maps remember **insertion order** and expose **size**.",
                '`set("apples", 200)` overwrites in place → get **200**.',
                '`get("kiwi")` is **undefined**.',
                "Objects: not iterable, no size, string keys, integer keys sort first, prototype keys exist.",
                "Map keys keep types: **1** stays a number; object keys stay objects.",
            ],
            [
                ("How do you fill an empty Map?", ["`set(key, value)` for each pair."]),
                ("What does new Map(pairs) contain?", ['**[["apples",500],["bananas",300],["oranges",200]]**.']),
                ('What does set("mangos", 100) do?', ["Appends mangos. size **4**."]),
                ('What does set("apples", 200) do?', ["Overwrites apples to **200**. Order unchanged."]),
                ('What is get("apples") on the original map?', ["**500**. Missing keys are **undefined**."]),
                ("typeof and instanceof?", ["**object** and **true**."]),
                ("Can you for...of a plain object?", ["**No.** **TypeError: obj is not iterable**."]),
                ("Does an object have size?", ["**undefined**. Use `Object.keys(obj).length` (**3** here)."]),
                ("What happens to object key `{x:1}`?", ['Becomes **"[object Object]"**. Map keeps the object.']),
                ("Object keys after z, a, then 1?", ['**["1","z","a"]**. Map: **["z","a",1]**.']),
                ("Does an empty object have toString?", ["`'toString' in obj` is **true** (prototype). `map.has('toString')` is **false**."]),
            ],
            "Pick a Map when keys are not only strings, when you need size, or when insertion order must hold. Objects still work for simple string dictionaries but coerce keys and inherit prototype names.",
            [
                ("JS Maps (W3Schools)", "https://www.w3schools.com/js/js_maps.asp"),
                ("MDN: Map", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map"),
            ],
        ),
        (
            "js-map-methods",
            "JS Map Methods",
            MAP_METHODS,
            "Map methods cover construct, get, set, size, delete, clear, has, and the iterators. forEach is (value, key). Object keys work; get('apples') is undefined when the key is an object named apples. Map.groupBy (ES2024) groups an iterable into a Map. Object.groupBy does the same into a plain object. Summing values() of 500+300+200 is 1000.",
            [
                "`delete` returns a boolean. `clear` empties. `has` follows delete.",
                '`forEach` text is **"apples = 500bananas = 300oranges = 200"** (no gap between pairs).',
                '`entries` concat is **"apples,500bananas,300oranges,200"**.',
                "Object key: `get(apples)` **500**, `get(\"apples\")` **undefined**.",
                "groupBy quantity>200: **ok** = apples+bananas, **low** = oranges+kiwi. Original array unchanged.",
                "Object.groupBy → plain object JSON; Map.groupBy → `instanceof Map` **true**.",
            ],
            [
                ('What is get("apples")?', ["**500**."]),
                ("What is size of the three-fruit map?", ["**3**."]),
                ('What does delete("apples") return?', ["**true**, size **2**, leftover bananas and oranges."]),
                ("What does clear() leave?", ["size **0**, **[]**."]),
                ('has("apples") then delete then has?', ["**true**, then **false**."]),
                ("forEach callback argument order?", ["**(value, key)** — value first."]),
                ("What is the values() string concat vs the sum?", ['Concat **"500300200"**. Sum **1000**.']),
                ('Why is get("apples") undefined with object keys?', ["The key is the **object**, not the string."]),
                ("What does Map.groupBy return?", ["A **Map**. ok has 2, low has 2. Input array unchanged."]),
                ("Object.groupBy vs Map.groupBy?", ["Object → plain object (`instanceof Map` **false**). Map → Map."]),
                ("Does set() on an existing key move it?", ["**No.** It overwrites the value in place."]),
            ],
            "get/set/has/delete/clear plus size are the mutators. Iterators give keys, values, or pairs. Object keys are references. groupBy builds a Map of groups; Object.groupBy builds a plain object instead.",
            [
                ("JS Map Methods (W3Schools)", "https://www.w3schools.com/js/js_map_methods.asp"),
                ("MDN: Map", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map"),
                ("MDN: Map.groupBy", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy"),
            ],
        ),
        (
            "js-map-weakmap",
            "JS Map WeakMap",
            WEAKMAP,
            "A WeakMap is key/value storage whose keys are objects (or unregistered symbols) held weakly. get/set/has/delete are the API. String keys throw Invalid value used as weak map key. Symbol.for (registered) throws; Symbol('x') works. WeakMaps are not iterable and have no size or clear. The visitor demo stores counts. The class demo stores {secret}; user1 is the key, so myMap.get(user1) works if myMap is in scope — the real privacy is that you cannot enumerate keys.",
            [
                "Keys: **objects** or **unregistered symbols**. Primitives and `Symbol.for` throw **Invalid value used as weak map key**.",
                "`get` / `set` / `has` / `delete` only. **Not iterable.** `size` is **undefined**.",
                "Visitor counts: Paul **3**, Ringo **1**, John **1**, George **undefined**.",
                "`getSecret()` is **hidden data**. `myMap.get(user1)` is the same pair. `[...myMap]` throws. `Array.from(myMap)` is **[]**.",
                "Nulling the only key binding drops your lookup. `get(null)` throws.",
            ],
            [
                ('What does set(myObj, "player") then get return?', ['**"player"**.']),
                ("has(look-alike object)?", ["**false** — different reference."]),
                ("delete then get?", ["delete **true**, has **false**, get **undefined**."]),
                ("Can you set a string key?", ["**No.** **TypeError: Invalid value used as weak map key**."]),
                ("Does Symbol('x') work as a key?", ["**Yes** (unregistered). `Symbol.for('x')` throws."]),
                ("Can you iterate a WeakMap?", ["**No.** **myMap is not iterable**."]),
                ("What is myMap.size?", ["**undefined**."]),
                ("How many times did Paul visit?", ["**3**. George was never tracked → **undefined**."]),
                ("Is the secret unreachable via myMap.get(user1)?", ["**No** — `user1` is the key, so get works if `myMap` is in scope. You still cannot **list** keys."]),
                ("What is Array.from(myMap)?", ["**[]** — not iterable, treated as a non-array-like object."]),
            ],
            "Use WeakMap for per-object metadata you do not want to keep alive. Keys are objects or unique symbols. Do not iterate. Privacy is lack of enumeration, not a magic wall around a key you already hold.",
            [
                ("JS WeakMap (W3Schools)", "https://www.w3schools.com/js/js_maps_weak.asp"),
                ("MDN: WeakMap", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap"),
            ],
        ),
        (
            "js-map-reference",
            "JS Map Reference",
            MAP_REF,
            "The July 2025 Map reference lists constructor, mutators, accessors, iterators, size, and Map.groupBy. Each table row is its own Example on the apples/bananas/oranges map except groupBy, which uses the quantity fruit array.",
            [
                "**Every table row is an Example.**",
                "`set` returns the same Map. `delete` returns a boolean. `clear` empties.",
                "`forEach` is `(value, key)`.",
                "groupBy keys **ok** / **low** with two fruits each.",
                "`size` is a property listed on the method table.",
            ],
            [
                ("What does new Map(pairs) create?", ["A Map of three fruit pairs, size **3**."]),
                ("What does clear() do?", ["size **0**, **[]**."]),
                ('delete("apples")?', ["**true**, leftover bananas and oranges."]),
                ("What does entries() yield?", ['**[["apples",500],["bananas",300],["oranges",200]]**.']),
                ('get("bananas") vs get("kiwi")?', ["**300** vs **undefined**."]),
                ("groupBy keys and lengths?", ['**["ok","low"]**, two fruits each.']),
                ('has("oranges") vs has("kiwi")?', ["**true** / **false**."]),
                ("What are keys() and values()?", ['keys **["apples","bananas","oranges"]**. values **[500,300,200]**.']),
                ('set("apples", 200) return value?', ["The **same** Map. get becomes **200**."]),
                ("Is size a method?", ["**No.** It is a **property** (still one table row / Example)."]),
            ],
            "The Map catalog is construct, clear/delete/set, get/has/size, iterate keys/values/entries/forEach, and groupBy for grouping an iterable into a Map.",
            [
                ("JS Map Reference (W3Schools)", "https://www.w3schools.com/js/js_map_reference.asp"),
                ("MDN: Map", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map"),
                ("MDN: Map.groupBy", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy"),
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
