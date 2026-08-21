"""S3 remainder: JS If Else, JS Ternary, JS Switch, JS Booleans, JS Logical."""
from __future__ import annotations

from pathlib import Path

from _gen_lib import S, build_and_snap, intro_toc, md_example, md_qa

COURSES = Path(__file__).resolve().parent.parent / "courses"
MAIN = Path(__file__).resolve().parent.parent / "tutorial_main.md"
PLAN = Path(__file__).resolve().parent.parent / "tutorial_plan.md"
BASE = "https://www.w3schools.com/js/"


def course_md(title, intro, concepts, records, slug, qa, summary_para, refs):
    concept = "\n".join(f"- [x] {c}" for c in concepts)
    examples = "\n".join(md_example(slug, i, rec) for i, rec in enumerate(records, 1))
    examples = examples.replace("./code_sandbox/", "../code_sandbox/")
    ref_lines = "\n".join(f"- [{n}]({u})" for n, u in refs)
    return f"""# {title}

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

{intro}

{intro_toc(slug, records)}

## Detailed Explanation

{concept}

{examples}
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
"""


def run(slug, title, records, intro, concepts, qa, summary, page, extra_refs, port, filename):
    refs = [(f"{title} (W3Schools)", BASE + page)]
    refs.extend(extra_refs)
    build_and_snap(
        slug, title, records, intro, concepts, qa, summary, refs, use_http=True, port=port
    )
    text = course_md(title, intro, concepts, records, slug, qa, summary, refs)
    (COURSES / filename).write_text(text, encoding="utf-8")
    print(f"wrote courses/{filename} ({len(records)} examples)", flush=True)


# ---------------------------------------------------------------------------
# 3.3 JS If Else
# ---------------------------------------------------------------------------

IF_ELSE = [
    S(
        "else-hour-10",
        "else — hour 10 is Good day",
        [
            "**`else`** runs when the `if` condition is **false**. Syntax: `if (condition) { … } else { … }`.",
            "The live Tryit uses `new Date().getHours()`. This sandbox **pins `hour = 10`** so the snap is stable.",
            "**10 < 18** is **true**, so the `if` block runs and `else` is skipped.",
        ],
        """let hour = 10;
let greeting;
if (hour < 18) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}""",
        displays=[("hour", "hour"), ("hour < 18", "hour < 18"), ("greeting", "greeting")],
        outcome="**hour = 10** makes `hour < 18` **true**, so greeting is **Good day**.",
    ),
    S(
        "else-hour-20",
        "else — hour 20 is Good evening",
        [
            "Same `if` / `else` as Example 1, with **`hour = 20`** so you see the **false** branch.",
            "**20 < 18** is **false**, so the `if` block is skipped and **`else`** runs.",
            "Without `else`, `greeting` would stay **undefined**. `else` is the fallback.",
        ],
        """let hour = 20;
let greeting;
if (hour < 18) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}""",
        displays=[("hour", "hour"), ("hour < 18", "hour < 18"), ("greeting", "greeting")],
        outcome="**hour = 20** makes `hour < 18` **false**, so greeting is **Good evening**.",
    ),
    S(
        "elseif-morning",
        "else if — time 8 is Good morning",
        [
            "**`else if`** adds another test when the first `if` is false: `if (c1) { } else if (c2) { } else { }`.",
            "Only the **first true** branch runs. Later branches are skipped.",
            "Pin **`time = 8`**. **8 < 10** is true, so greeting is **Good morning** (the later `< 20` test never runs).",
        ],
        """let time = 8;
let greeting;
if (time < 10) {
  greeting = "Good morning";
} else if (time < 20) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}""",
        displays=[("time", "time"), ("greeting", "greeting")],
        outcome="**time = 8** matches `time < 10`, so greeting is **Good morning**.",
    ),
    S(
        "elseif-day",
        "else if — time 15 is Good day",
        [
            "**`time = 15`**: `15 < 10` is **false**, so the first block is skipped.",
            "**15 < 20** is **true**, so the **`else if`** block runs.",
            "The final `else` does not run. Order matters: a later true test is ignored once an earlier branch matched.",
        ],
        """let time = 15;
let greeting;
if (time < 10) {
  greeting = "Good morning";
} else if (time < 20) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}""",
        displays=[("time", "time"), ("greeting", "greeting")],
        outcome="**time = 15** fails `< 10` and matches `< 20`, so greeting is **Good day**.",
    ),
    S(
        "elseif-evening",
        "else if — time 21 is Good evening",
        [
            "**`time = 21`**: both `21 < 10` and `21 < 20` are **false**.",
            "The trailing **`else`** is the fallback when no condition matched.",
            "This is the page’s “Good evening” path (hours 20 and 21–23).",
        ],
        """let time = 21;
let greeting;
if (time < 10) {
  greeting = "Good morning";
} else if (time < 20) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}""",
        displays=[("time", "time"), ("greeting", "greeting")],
        outcome="**time = 21** matches neither test, so **else** sets greeting to **Good evening**.",
    ),
    S(
        "random-w3schools",
        "Random link — Math.random() 0.2 visits W3Schools",
        [
            "The page picks a link with **`Math.random() < 0.5`** (about a **50%** chance each way).",
            "`Math.random()` is **not** stable for snaps, so this demo **pins `0.2`** in place of a live random call.",
            "**0.2 < 0.5** is true, so `text` is the **W3Schools** anchor (same markup idea as the Tryit).",
        ],
        """let n = 0.2; // pinned stand-in for Math.random()
let text;
if (n < 0.5) {
  text = '<a href="https://www.w3schools.com">Visit W3Schools</a>';
} else {
  text = '<a href="https://www.wwf.org">Visit WWF</a>';
}""",
        displays=[("n", "n"), ("n < 0.5", "n < 0.5"), ("text", "text")],
        outcome="Pinned **0.2 < 0.5** is **true**, so text is the **Visit W3Schools** link.",
    ),
    S(
        "random-wwf",
        "Random link — Math.random() 0.8 visits WWF",
        [
            "Same `if` / `else` as Example 6, with a pinned **`0.8`** for the **false** branch.",
            "**0.8 < 0.5** is **false**, so the **WWF** link is chosen.",
            "On the live page, reload to see either link. Do not use `Math.random()` when you need a deterministic test.",
        ],
        """let n = 0.8; // pinned stand-in for Math.random()
let text;
if (n < 0.5) {
  text = '<a href="https://www.w3schools.com">Visit W3Schools</a>';
} else {
  text = '<a href="https://www.wwf.org">Visit WWF</a>';
}""",
        displays=[("n", "n"), ("n < 0.5", "n < 0.5"), ("text", "text")],
        outcome="Pinned **0.8 < 0.5** is **false**, so text is the **Visit WWF** link.",
    ),
]

# ---------------------------------------------------------------------------
# 3.4 JS Ternary
# ---------------------------------------------------------------------------

TERNARY = [
    S(
        "age-minor",
        "age < 18 ? Minor : Adult — age 16",
        [
            "The **conditional (ternary) operator** is shorthand for `if…else` that **returns a value**.",
            "Syntax: `(condition) ? expression1 : expression2` — **three** operands (the only JS operator that takes three).",
            "Pin **`age = 16`**. **16 < 18** is true, so the result is **Minor**.",
        ],
        """let age = 16;
let text = (age < 18) ? "Minor" : "Adult";""",
        displays=[("age", "age"), ("age < 18", "age < 18"), ("text", "text")],
        outcome="**age = 16** makes `age < 18` **true**, so text is **Minor**.",
    ),
    S(
        "age-adult",
        "age < 18 ? Minor : Adult — age 21",
        [
            "Same operator as Example 1, with **`age = 21`** so you see **expression2** (the `:` side).",
            "**21 < 18** is **false**, so the result is **Adult**.",
            "Read it as: *if the test is true, take the value after `?`; otherwise take the value after `:`*.",
        ],
        """let age = 21;
let text = (age < 18) ? "Minor" : "Adult";""",
        displays=[("age", "age"), ("age < 18", "age < 18"), ("text", "text")],
        outcome="**age = 21** makes `age < 18` **false**, so text is **Adult**.",
    ),
    S(
        "member-true",
        "isMember true → discount 0.2",
        [
            "A boolean condition works the same way: `isMember ? 0.2 : 0`.",
            "**`isMember = true`** selects **0.2** (20% off).",
            "You do not write `if (isMember === true)` — the value already is a boolean.",
        ],
        """let isMember = true;
let discount = isMember ? 0.2 : 0;""",
        displays=[("isMember", "isMember"), ("discount", "discount")],
        outcome="**isMember** is **true**, so discount is **0.2**.",
    ),
    S(
        "member-false",
        "isMember false → discount 0",
        [
            "Same expression as Example 3, with **`isMember = false`**.",
            "The `:` branch runs and discount is **0** (no member rate).",
            "This is the page’s second membership Tryit.",
        ],
        """let isMember = false;
let discount = isMember ? 0.2 : 0;""",
        displays=[("isMember", "isMember"), ("discount", "discount")],
        outcome="**isMember** is **false**, so discount is **0**.",
    ),
    S(
        "same-as-if-else",
        "Ternary vs the equivalent if…else",
        [
            "The page says the operator is a **shorthand for `if…else`**. This Example writes both forms with **age 16**.",
            "`if (age < 18) { text = \"Minor\"; } else { text = \"Adult\"; }` assigns the same string as `(age < 18) ? \"Minor\" : \"Adult\"`.",
            "Prefer `if` when the branches are **statements** (several lines). Prefer `? :` when you need **one value**.",
        ],
        """let age = 16;
let textIf;
if (age < 18) {
  textIf = "Minor";
} else {
  textIf = "Adult";
}
let textTernary = (age < 18) ? "Minor" : "Adult";""",
        displays=[("textIf", "textIf"), ("textTernary", "textTernary"), ("same", "textIf === textTernary")],
        outcome="Both forms produce **Minor**, and **same** is **true**.",
    ),
    S(
        "syntax-parts",
        "The three operands: condition, ?, expressions",
        [
            "**condition** — required, evaluated as true/false.",
            "**`?`** separates the condition from the true-value; **`:`** separates the two result expressions.",
            "**expression1** returns if the condition is true; **expression2** if false. All five pieces in the page’s parameter table are required.",
            "This operator is an **ES1** (1997) feature and is supported in all current browsers.",
        ],
        """let condition = (10 > 9);
let expression1 = "yes";
let expression2 = "no";
let result = condition ? expression1 : expression2;""",
        displays=[
            ("condition", "condition"),
            ("expression1", "expression1"),
            ("expression2", "expression2"),
            ("result", "result"),
        ],
        outcome="**10 > 9** is **true**, so result is **yes** (expression1). expression2 (**no**) is not used.",
    ),
]

# ---------------------------------------------------------------------------
# 3.5 JS Switch
# ---------------------------------------------------------------------------

SWITCH = [
    S(
        "weekday-wednesday",
        "switch weekday number — 3 is Wednesday",
        [
            "`switch (expression)` compares the expression to each **`case`** with **strict `===`**.",
            "`Date#getDay()` returns **0–6** (Sunday=0 … Saturday=6). The live Tryit uses today; this snap **pins `3`** (Wednesday).",
            "When a `case` matches, that block runs until **`break`** (or the end of the switch).",
        ],
        """let dayNum = 3; // pinned stand-in for new Date().getDay()
let day;
switch (dayNum) {
  case 0:
    day = "Sunday";
    break;
  case 1:
    day = "Monday";
    break;
  case 2:
    day = "Tuesday";
    break;
  case 3:
    day = "Wednesday";
    break;
  case 4:
    day = "Thursday";
    break;
  case 5:
    day = "Friday";
    break;
  case 6:
    day = "Saturday";
}""",
        displays=[("dayNum", "dayNum"), ("day", "day")],
        outcome="**dayNum = 3** matches **`case 3`**, so day is **Wednesday**.",
    ),
    S(
        "break-fallthrough",
        "break — without it, cases fall through",
        [
            "**`break`** leaves the switch. Without it, execution **falls through** into the next `case` even if that label does not match.",
            "The last case does not need `break` because the switch ends anyway — but missing `break` in the **middle** is the classic bug.",
            "Here **`case 1`** has no `break`, so **Monday** also runs **Tuesday**’s assignment.",
        ],
        """let dayNum = 1;
let day = "";
switch (dayNum) {
  case 1:
    day += "Monday ";
  case 2:
    day += "Tuesday";
    break;
  default:
    day = "other";
}""",
        displays=[("dayNum", "dayNum"), ("day", "day")],
        outcome="**dayNum = 1** matches case 1, then **falls through** into case 2, so day is **Monday Tuesday**.",
    ),
    S(
        "default-weekday",
        "default — weekday 3 looks forward to the weekend",
        [
            "**`default`** runs when **no `case` matches**. It is optional.",
            "This Tryit only names **Saturday (6)** and **Sunday (0)**. Any other weekday hits `default`.",
            "Pin **`dayNum = 3`** (Wednesday) so the snap is not weekend-dependent.",
        ],
        """let dayNum = 3;
let text;
switch (dayNum) {
  case 6:
    text = "Today is Saturday";
    break;
  case 0:
    text = "Today is Sunday";
    break;
  default:
    text = "Looking forward to the Weekend";
}""",
        displays=[("dayNum", "dayNum"), ("text", "text")],
        outcome="**3** is neither 6 nor 0, so **default** sets text to **Looking forward to the Weekend**.",
    ),
    S(
        "default-saturday",
        "default switch — 6 is Today is Saturday",
        [
            "Same switch as Example 3, with **`dayNum = 6`** so a named weekend case wins over `default`.",
            "`default` is only the fallback. A matching `case` still runs first.",
        ],
        """let dayNum = 6;
let text;
switch (dayNum) {
  case 6:
    text = "Today is Saturday";
    break;
  case 0:
    text = "Today is Sunday";
    break;
  default:
    text = "Looking forward to the Weekend";
}""",
        displays=[("dayNum", "dayNum"), ("text", "text")],
        outcome="**dayNum = 6** matches **`case 6`**, so text is **Today is Saturday**.",
    ),
    S(
        "default-not-last",
        "default does not have to be last",
        [
            "You may put **`default` first**. If it is **not** last, end it with **`break`** or later cases will also run.",
            "Pin **`dayNum = 3`**. No weekend case matches, so `default` still produces **Looking forward to the Weekend**.",
        ],
        """let dayNum = 3;
let text;
switch (dayNum) {
  default:
    text = "Looking forward to the Weekend";
    break;
  case 6:
    text = "Today is Saturday";
    break;
  case 0:
    text = "Today is Sunday";
}""",
        displays=[("dayNum", "dayNum"), ("text", "text")],
        outcome="**default** is first, but **`break`** stops it. dayNum **3** still yields **Looking forward to the Weekend**.",
    ),
    S(
        "shared-thu-fri",
        "Shared cases — 4 and 5 are Soon it is Weekend",
        [
            "Several `case` labels can **share one block**. List them with no code in between; the first matching label starts the block.",
            "**Thursday (4)** and **Friday (5)** share **Soon it is Weekend**.",
            "Pin **`dayNum = 4`**.",
        ],
        """let dayNum = 4;
let text;
switch (dayNum) {
  case 4:
  case 5:
    text = "Soon it is Weekend";
    break;
  case 0:
  case 6:
    text = "It is Weekend";
    break;
  default:
    text = "Looking forward to the Weekend";
}""",
        displays=[("dayNum", "dayNum"), ("text", "text")],
        outcome="**4** shares a block with **5**, so text is **Soon it is Weekend**.",
    ),
    S(
        "shared-weekend",
        "Shared cases — 0 and 6 are It is Weekend",
        [
            "**Sunday (0)** and **Saturday (6)** share **It is Weekend**.",
            "Pin **`dayNum = 0`**.",
            "If several labels could match, **the first listed match** is selected; here only one value is in the expression.",
        ],
        """let dayNum = 0;
let text;
switch (dayNum) {
  case 4:
  case 5:
    text = "Soon it is Weekend";
    break;
  case 0:
  case 6:
    text = "It is Weekend";
    break;
  default:
    text = "Looking forward to the Weekend";
}""",
        displays=[("dayNum", "dayNum"), ("text", "text")],
        outcome="**0** shares a block with **6**, so text is **It is Weekend**.",
    ),
    S(
        "shared-default-mon",
        "Shared cases — Monday 1 uses default",
        [
            "**Monday (1)** is not 4, 5, 0, or 6, so **`default`** runs.",
            "If there is **no** `default` and no match, the switch does nothing and execution continues after it.",
        ],
        """let dayNum = 1;
let text;
switch (dayNum) {
  case 4:
  case 5:
    text = "Soon it is Weekend";
    break;
  case 0:
  case 6:
    text = "It is Weekend";
    break;
  default:
    text = "Looking forward to the Weekend";
}""",
        displays=[("dayNum", "dayNum"), ("text", "text")],
        outcome="**1** matches no weekend case, so text is **Looking forward to the Weekend**.",
    ),
    S(
        "strict-string-zero",
        "Strict comparison — string \"0\" does not match case 0",
        [
            "Switch uses **strict comparison (`===`)**. Types must match.",
            '**`x = "0"`** (string) does **not** match **`case 0:`** (number).',
            "There is no match, so **`default`** runs: **No value found**.",
        ],
        """let x = "0";
let text;
switch (x) {
  case 0:
    text = "Off";
    break;
  case 1:
    text = "On";
    break;
  default:
    text = "No value found";
}""",
        displays=[("x", "x"), ("typeof x", "typeof x"), ("text", "text")],
        outcome='**x** is the string **"0"**, so `case 0` does not match and text is **No value found**.',
    ),
    S(
        "strict-number-zero",
        "Strict comparison — number 0 is Off",
        [
            "Same switch, with **`x = 0`** (number) so **`case 0`** matches.",
            "`\"0\" === 0` is **false**; `0 === 0` is **true**. Convert with `Number(x)` if you must accept both.",
        ],
        """let x = 0;
let text;
switch (x) {
  case 0:
    text = "Off";
    break;
  case 1:
    text = "On";
    break;
  default:
    text = "No value found";
}""",
        displays=[("x", "x"), ("typeof x", "typeof x"), ("text", "text")],
        outcome="**x = 0** (number) matches **`case 0`**, so text is **Off**.",
    ),
]

# ---------------------------------------------------------------------------
# 3.6 JS Booleans
# ---------------------------------------------------------------------------

BOOLEANS = [
    S(
        "eq-false",
        "Equal to — (x == 8) is false",
        [
            "A **Boolean** is a primitive that is only **`true`** or **`false`** (lowercase, **no quotes**).",
            "Comparison operators **return** booleans. Given **`x = 5`**, **`(x == 8)`** is **false**.",
        ],
        """let x = 5;
let result = (x == 8);""",
        displays=[("x", "x"), ("x == 8", "x == 8"), ("result", "result")],
        outcome="**5 == 8** is **false**.",
    ),
    S(
        "neq-true",
        "Not equal — (x != 8) is true",
        [
            "Same **`x = 5`**. **`(x != 8)`** is **true**.",
            "This is the second row of the page’s comparison table (and half of the combined Tryit).",
        ],
        """let x = 5;
let result = (x != 8);""",
        displays=[("x", "x"), ("x != 8", "x != 8"), ("result", "result")],
        outcome="**5 != 8** is **true**.",
    ),
    S(
        "gt-false",
        "Greater than — (x > 8) is false",
        [
            "**`(x > 8)`** with **x = 5** is **false**.",
            "Booleans from comparisons are what `if` tests.",
        ],
        """let x = 5;
let result = (x > 8);""",
        displays=[("x", "x"), ("x > 8", "x > 8")],
        outcome="**5 > 8** is **false**.",
    ),
    S(
        "lt-true",
        "Less than — (x < 8) is true",
        [
            "**`(x < 8)`** with **x = 5** is **true**.",
            "The page’s comparison Tryit shows `==` and `!=`; this row completes the table.",
        ],
        """let x = 5;
let result = (x < 8);""",
        displays=[("x", "x"), ("x < 8", "x < 8")],
        outcome="**5 < 8** is **true**.",
    ),
    S(
        "if-monday",
        "if (day == \"Monday\")",
        [
            "`if` conditions are booleans. **`day == \"Monday\"`** is true or false.",
            "Pin **`day = \"Monday\"`** so the test is **true** and the block runs.",
        ],
        """let day = "Monday";
let text = "not Monday";
if (day == "Monday") {
  text = "It is Monday";
}""",
        displays=[("day == \"Monday\"", 'day == "Monday"'), ("text", "text")],
        outcome="**day** is **Monday**, so the `if` is **true** and text is **It is Monday**.",
    ),
    S(
        "if-salary",
        "if (salary > 9000)",
        [
            "Numeric comparisons are booleans too. Pin **`salary = 12000`**.",
            "**12000 > 9000** is **true**.",
        ],
        """let salary = 12000;
let text = "below";
if (salary > 9000) {
  text = "above 9000";
}""",
        displays=[("salary > 9000", "salary > 9000"), ("text", "text")],
        outcome="**12000 > 9000** is **true**, so text is **above 9000**.",
    ),
    S(
        "if-age",
        "if (age < 18)",
        [
            "Pin **`age = 16`**. **16 < 18** is **true** (too young in this test).",
        ],
        """let age = 16;
let text = "adult path";
if (age < 18) {
  text = "too young";
}""",
        displays=[("age < 18", "age < 18"), ("text", "text")],
        outcome="**16 < 18** is **true**, so text is **too young**.",
    ),
    S(
        "if-else-hour",
        "if / else greeting uses a boolean test",
        [
            "The page’s condition Tryit is the familiar **hour < 18** greeting.",
            "Pin **`hour = 10`**. The `if` condition is **true**, so greeting is **Good day**.",
        ],
        """let hour = 10;
let greeting;
if (hour < 18) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}""",
        displays=[("hour < 18", "hour < 18"), ("greeting", "greeting")],
        outcome="**hour < 18** is **true**, so greeting is **Good day**.",
    ),
    S(
        "for-loop",
        "for (i = 0; i < 5; i++)",
        [
            "Loop conditions are booleans. **`i < 5`** is re-tested every iteration.",
            "The loop body runs while that test is **true** (i = 0,1,2,3,4).",
        ],
        """let text = "";
for (let i = 0; i < 5; i++) {
  text += i;
}""",
        displays=[("text", "text")],
        outcome="The loop appends **0** through **4**, so text is **01234**.",
    ),
    S(
        "while-loop",
        "while (i < 10)",
        [
            "The page’s loop Tryit: **`while (i < 10) { text += i; i++; }`**.",
            "`i < 10` is the boolean that keeps the loop going.",
        ],
        """let text = "";
let i = 0;
while (i < 10) {
  text += i;
  i++;
}""",
        displays=[("text", "text"), ("i after", "i")],
        outcome="text is **0123456789** and **i** is **10** (the test is then false).",
    ),
    S(
        "for-in-loop",
        "for (x in person)",
        [
            "**`for…in`** walks **enumerable keys**. The loop *runs* while there are keys left (the engine’s condition is still boolean under the hood).",
            "This sandbox uses `{fname:\"John\", lname:\"Doe\"}` and concatenates values.",
        ],
        """const person = {fname: "John", lname: "Doe"};
let text = "";
for (let x in person) {
  text += person[x];
}""",
        displays=[("text", "text")],
        outcome="text is **JohnDoe** (fname then lname).",
    ),
    S(
        "for-of-loop",
        "for (x of cars)",
        [
            "**`for…of`** walks **iterable values** (array elements), not keys.",
            "`[\"BMW\", \"Volvo\"]` yields two iterations.",
        ],
        """const cars = ["BMW", "Volvo"];
let text = "";
for (let x of cars) {
  text += x;
}""",
        displays=[("text", "text")],
        outcome="text is **BMWVolvo**.",
    ),
    S(
        "boolean-fn",
        "Boolean(10 > 9)",
        [
            "**`Boolean(expression)`** converts a value to **true** or **false**.",
            "**`Boolean(10 > 9)`** is **true** because the comparison is already true.",
        ],
        """let result = Boolean(10 > 9);""",
        displays=[("Boolean(10 > 9)", "Boolean(10 > 9)")],
        outcome="**Boolean(10 > 9)** is **true**.",
    ),
    S(
        "bare-compare",
        "(10 > 9) without Boolean()",
        [
            "The page says you can skip `Boolean()`: **`(10 > 9)`** already is a boolean.",
            "That is “even easier” than wrapping it.",
        ],
        """let result = (10 > 9);""",
        displays=[("(10 > 9)", "(10 > 9)"), ("typeof", "typeof (10 > 9)")],
        outcome="**(10 > 9)** is **true**, and **typeof** is **boolean**.",
    ),
    S(
        "truthy-values",
        "Everything with a value is true",
        [
            "Values that are **truthy** become **true** in a boolean context: numbers other than 0, non-empty strings, `true`, arrays, objects.",
            "The string **`\"false\"`** is truthy — it is not the boolean `false`.",
            "**`[]`** and **`{}`** are truthy because **all objects** are true in a boolean context, even when empty.",
        ],
        """let rows = [
  ["100", Boolean(100)],
  ["3.14", Boolean(3.14)],
  ["-15", Boolean(-15)],
  ["true", Boolean(true)],
  ['"Hello"', Boolean("Hello")],
  ['"false"', Boolean("false")],
  ["7+1+3.14", Boolean(7 + 1 + 3.14)],
  ["[]", Boolean([])],
  ["{}", Boolean({})]
];""",
        displays=[
            ("100", "Boolean(100)"),
            ("3.14", "Boolean(3.14)"),
            ("-15", "Boolean(-15)"),
            ("true", "Boolean(true)"),
            ("Hello", 'Boolean("Hello")'),
            ('"false"', 'Boolean("false")'),
            ("7+1+3.14", "Boolean(7 + 1 + 3.14)"),
            ("[]", "Boolean([])"),
            ("{}", "Boolean({})"),
        ],
        outcome="Every listed value is **true**, including **`\"false\"`**, **`[]`**, and **`{}`**.",
    ),
    S(
        "falsy-zero",
        "Boolean(0) is false",
        [
            "Values **without a “value”** are **falsy**. **`0`** is false.",
            "This is its own Tryit on the page.",
        ],
        """let x = 0;
let result = Boolean(x);""",
        displays=[("x", "x"), ("Boolean(x)", "Boolean(x)")],
        outcome="**Boolean(0)** is **false**.",
    ),
    S(
        "falsy-negzero",
        "Boolean(-0) is false",
        [
            "**`-0`** (minus zero) is also false. JavaScript has a signed zero; both are falsy.",
        ],
        """let x = -0;
let result = Boolean(x);""",
        displays=[("x", "x"), ("Boolean(x)", "Boolean(x)"), ("Object.is(-0)", "Object.is(x, -0)")],
        outcome="**Boolean(-0)** is **false**. **Object.is(x, -0)** is **true** so this really is minus zero.",
    ),
    S(
        "falsy-empty-string",
        'Boolean("") is false',
        [
            'An **empty string** `""` is false. Any non-empty string (even `"0"` or `"false"`) is true.',
        ],
        """let x = "";
let result = Boolean(x);""",
        displays=[("x JSON", "JSON.stringify(x)"), ("Boolean(x)", "Boolean(x)")],
        outcome='**Boolean("")** is **false**.',
    ),
    S(
        "falsy-undefined",
        "Boolean(undefined) is false",
        [
            "A declared-but-unassigned variable is **`undefined`**, which is false.",
        ],
        """let x;
let result = Boolean(x);""",
        displays=[("x", "x"), ("Boolean(x)", "Boolean(x)")],
        outcome="**Boolean(undefined)** is **false**.",
    ),
    S(
        "falsy-null",
        "Boolean(null) is false",
        [
            "**`null`** is the intentional empty value. It is false.",
        ],
        """let x = null;
let result = Boolean(x);""",
        displays=[("x", "x"), ("Boolean(x)", "Boolean(x)")],
        outcome="**Boolean(null)** is **false**.",
    ),
    S(
        "falsy-false",
        "Boolean(false) is false",
        [
            "The boolean **`false`** is (you guessed it) false.",
        ],
        """let x = false;
let result = Boolean(x);""",
        displays=[("x", "x"), ("Boolean(x)", "Boolean(x)")],
        outcome="**Boolean(false)** is **false**.",
    ),
    S(
        "falsy-nan",
        "Boolean(NaN) is false",
        [
            'The page uses **`10 / "Hallo"`** to get **`NaN`**. **`Boolean(NaN)`** is false.',
        ],
        """let x = 10 / "Hallo";
let result = Boolean(x);""",
        displays=[("x", "x"), ("Number.isNaN(x)", "Number.isNaN(x)"), ("Boolean(x)", "Boolean(x)")],
        outcome="**x** is **NaN**, and **Boolean(NaN)** is **false**.",
    ),
    S(
        "bool-object-typeof",
        "typeof primitive boolean vs new Boolean()",
        [
            "Normal booleans are **primitives**: `let x = false` → **typeof boolean**.",
            "**`new Boolean(false)`** is an **object**. **Do not** create Boolean objects — they slow code and confuse `===`.",
        ],
        """let x = false;
let y = new Boolean(false);""",
        displays=[("typeof x", "typeof x"), ("typeof y", "typeof y")],
        outcome="**typeof x** is **boolean**; **typeof y** is **object**.",
    ),
    S(
        "bool-object-compare",
        "Boolean(false) == new Boolean(false)",
        [
            "`Boolean(false)` (the function, **without** `new`) returns the primitive **false**.",
            "`new Boolean(false)` is an object. **`==`** is **true** (object converted); **`===`** is **false** (different types).",
            "The page warns: booleans and boolean objects cannot be compared safely.",
        ],
        """let x = Boolean(false);
let y = new Boolean(false);""",
        displays=[
            ("x", "x"),
            ("typeof y", "typeof y"),
            ("x == y", "x == y"),
            ("x === y", "x === y"),
        ],
        outcome="**x == y** is **true**; **x === y** is **false**.",
    ),
    S(
        "two-objects-false",
        "Comparing two Boolean objects is false",
        [
            "Comparing **two objects** with `==` or `===` is **false** unless they are the **same reference**.",
            "Two `new Boolean(false)` values are two objects, so **`a == b`** is **false**.",
        ],
        """let a = new Boolean(false);
let b = new Boolean(false);""",
        displays=[("a == b", "a == b"), ("a === b", "a === b")],
        outcome="**a == b** and **a === b** are both **false** (two different objects).",
    ),
]

# ---------------------------------------------------------------------------
# 3.7 JS Logical
# ---------------------------------------------------------------------------

LOGICAL = [
    S(
        "and-table",
        "&& AND — (x < 10 && y > 1) is true",
        [
            "Given **x = 6**, **y = 3**: **`(x < 10 && y > 1)`** is **true** (both sides true).",
            "**`&&`** is **true** only when **both** operands are true; otherwise **false**.",
            "This is the first row of the operators table (and the AND Tryit).",
        ],
        """let x = 6;
let y = 3;
let z = (x < 10 && y > 1);""",
        displays=[("x < 10", "x < 10"), ("y > 1", "y > 1"), ("z", "z")],
        outcome="Both sides are true, so **z** is **true**.",
    ),
    S(
        "or-table",
        "|| OR — (x === 5 || y === 5) is false",
        [
            "Given **x = 6**, **y = 3**: **`(x === 5 || y === 5)`** is **false** (neither equals 5).",
            "**`||`** is **true** if **one or both** sides are true.",
        ],
        """let x = 6;
let y = 3;
let z = (x === 5 || y === 5);""",
        displays=[("x === 5", "x === 5"), ("y === 5", "y === 5"), ("z", "z")],
        outcome="Both sides are false, so **z** is **false**.",
    ),
    S(
        "not-table",
        "! NOT — !(x === y) is true",
        [
            "Given **x = 6**, **y = 3**: **`x === y`** is false, so **`!(x === y)`** is **true**.",
            "**`!`** flips true↔false.",
        ],
        """let x = 6;
let y = 3;
let z = !(x === y);""",
        displays=[("x === y", "x === y"), ("z", "z")],
        outcome="**x === y** is **false**, so **! that** is **true**.",
    ),
    S(
        "and-section",
        "Logical AND — both true with x=6 y=3",
        [
            "The AND section repeats `let z = (x < 10 && y > 1)` with **x = 6**, **y = 3**.",
            "Same result as the table row: **true**.",
        ],
        """let x = 6;
let y = 3;
let z = (x < 10 && y > 1);""",
        displays=[("z", "z")],
        outcome="**z** is **true**.",
    ),
    S(
        "and-false",
        "Logical AND — false when y is not > 1",
        [
            "If **y = 0**, **`y > 1`** is false, so **`&&`** is **false** even though **x < 10** is true.",
            "`&&` **short-circuits**: if the left side is false, the right side is not evaluated.",
        ],
        """let x = 6;
let y = 0;
let z = (x < 10 && y > 1);""",
        displays=[("x < 10", "x < 10"), ("y > 1", "y > 1"), ("z", "z")],
        outcome="**y > 1** is **false**, so **z** is **false**.",
    ),
    S(
        "or-section",
        "Logical OR — x=6 y=-3 still true",
        [
            "The OR section uses **x = 6**, **y = -3**, **`z = (x > 0 || y > 0)`**.",
            "**x > 0** is true, so the whole `||` is **true** even though **y > 0** is false.",
        ],
        """let x = 6;
let y = -3;
let z = (x > 0 || y > 0);""",
        displays=[("x > 0", "x > 0"), ("y > 0", "y > 0"), ("z", "z")],
        outcome="**x > 0** is **true**, so **z** is **true**.",
    ),
    S(
        "not-section",
        "Logical NOT — !(5 == 8)",
        [
            "**`(5 == 8)`** is false. **`!(5 == 8)`** is **true**.",
            "The page stores them as `let x = (5 == 8); let y = !(5 == 8)`.",
        ],
        """let x = (5 == 8);
let y = !(5 == 8);""",
        displays=[("x", "x"), ("y", "y")],
        outcome="**x** is **false**; **y** is **true**.",
    ),
    S(
        "nullish-null",
        "?? — null ?? \"missing\" is missing",
        [
            "**`??`** (nullish coalescing) returns the **right** operand when the left is **`null` or `undefined`**; otherwise the **left**.",
            '**`name = null`**, **`text = \"missing\"`**, **`result = name ?? text`** → **missing**.',
            "`??` is **ES2020**. Use it when **0** or **\"\"** should count as real values (unlike `||`).",
        ],
        """let name = null;
let text = "missing";
let result = name ?? text;""",
        displays=[("name", "name"), ("result", "result")],
        outcome="**name** is **null**, so **result** is **missing**.",
    ),
    S(
        "nullish-vs-or",
        "?? keeps 0; || treats 0 as missing",
        [
            "**`0 ?? 5`** is **0** (0 is not nullish). **`0 || 5`** is **5** (0 is falsy).",
            "The page’s point: sometimes an empty string or `false` or `0` is a **valid** value — then use **`??`**, not **`||`**.",
        ],
        """let viaNullish = 0 ?? 5;
let viaOr = 0 || 5;
let emptyKeep = "" ?? "fallback";
let emptyOr = "" || "fallback";""",
        displays=[
            ("0 ?? 5", "viaNullish"),
            ("0 || 5", "viaOr"),
            ('"" ?? fallback', "emptyKeep"),
            ('"" || fallback', "emptyOr"),
        ],
        outcome="**0 ?? 5** is **0**; **0 || 5** is **5**. **\"\" ?? …** stays **\"\"**; **\"\" || …** becomes **fallback**.",
    ),
]


def main():
    run(
        "js-if-else",
        "JS If Else",
        IF_ELSE,
        "Use **`else`** when the `if` test is **false**, and **`else if`** to chain more tests. This page greets by hour and picks a random W3Schools / WWF link. Hours and random values are **pinned** so the snaps stay stable.",
        [
            "**`else`** is the false branch of `if`. **`else if`** is an extra test; only the **first true** branch runs.",
            "The live hour examples use `new Date().getHours()`; the sandbox pins **10 / 15 / 20 / 21**.",
            "`Math.random() < 0.5` is ~50/50; the sandbox pins **0.2** and **0.8** for both links.",
        ],
        [
            ("When does `else` run?", ["When the `if` condition is **false**."]),
            ("With `hour = 10`, what is `greeting`?", ["**Good day**.", "`10 < 18` is true, so `else` is skipped."]),
            ("With `hour = 20`, what is `greeting`?", ["**Good evening**."]),
            ("With `time = 8`, which branch runs?", ["The first `if` (`time < 10`).", "Greeting is **Good morning**."]),
            ("With `time = 15`, which branch runs?", ["**`else if (time < 20)`**.", "Greeting is **Good day**."]),
            ("With `time = 21`, which branch runs?", ["The final **`else`**.", "Greeting is **Good evening**."]),
            ("Does a later `else if` run after an earlier match?", ["**No.** Only the first true branch runs."]),
            ("What does `Math.random() < 0.5` decide?", ["Which link to show: **W3Schools** if true, **WWF** if false (~50% each)."]),
            ("If the pinned stand-in is `0.8`, which link is chosen?", ["**Visit WWF**.", "`0.8 < 0.5` is false."]),
            ("Why pin `hour` and `Math.random()` in the sandbox?", ["So the screenshots are **deterministic**."]),
        ],
        "`else` covers the false `if`. **hour 10** → **Good day**; **hour 20** → **Good evening**. `else if` chains tests: **time 8 / 15 / 21** → **Good morning / Good day / Good evening**. A `Math.random() < 0.5` pick becomes **W3Schools** at 0.2 and **WWF** at 0.8.",
        "js_if_else.asp",
        [("MDN: if...else", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else")],
        8772,
        "js_if_else.md",
    )
    run(
        "js-ternary",
        "JS Ternary",
        TERNARY,
        "The **conditional (ternary) operator** `(condition) ? a : b` is a one-line **`if…else` that returns a value**. This page uses it for **Minor / Adult** and a **member discount**. Age and membership flags are pinned.",
        [
            "It is called **ternary** because it takes **three** operands — the only JavaScript operator that does.",
            "Syntax: **condition ? expression1 : expression2**. All parts in the parameter table are required.",
            "ES1 (1997); supported in all current browsers.",
        ],
        [
            ("How many operands does `? :` take?", ["**Three** — condition, true-value, false-value."]),
            ("With `age = 16`, what is `(age < 18) ? \"Minor\" : \"Adult\"`?", ["**Minor**."]),
            ("With `age = 21`, what is that expression?", ["**Adult**."]),
            ("With `isMember = true`, what is `isMember ? 0.2 : 0`?", ["**0.2**."]),
            ("With `isMember = false`, what is the discount?", ["**0**."]),
            ("Is `? :` a replacement for every `if`?", ["**No.** Use `if` for multi-line **statements**. Use `? :` to pick **one value**."]),
            ("What does `?` separate?", ["The **condition** from the **true** expression."]),
            ("What does `:` separate?", ["The **true** expression from the **false** expression."]),
            ("Do `if…else` and the ternary agree for age 16?", ["**Yes.** Both produce **Minor**."]),
            ("Is this a new operator?", ["**No.** It is **ES1** (1997) and works in all browsers."]),
        ],
        "Write `(condition) ? ifTrue : ifFalse`. **age 16** → **Minor**; **age 21** → **Adult**. **isMember true** → **0.2**; **false** → **0**. Same result as `if…else` when you only need a value.",
        "js_if_ternary.asp",
        [
            ("MDN: Conditional (ternary) operator", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator")
        ],
        8773,
        "js_ternary.md",
    )
    run(
        "js-switch",
        "JS Switch",
        SWITCH,
        "`switch` picks a block by matching an expression to **`case`** labels (often cleaner than a long `if…else if`). **`break`** stops fall-through. **`default`** is the fallback. Switch compares with **`===`**. Weekday numbers are **pinned** (0–6) so snaps do not depend on today.",
        [
            "The expression is evaluated **once**, then compared to each `case`. The **first match** runs.",
            "**`break`** exits the switch. Without it, the next cases run too (**fall-through**).",
            "**`default`** is optional and need not be last — but then it **must** `break`.",
            "No match and no `default` → the switch does nothing. Comparison is **strict** (`===`).",
        ],
        [
            ("What does `getDay()` return?", ["A number **0–6** (Sunday=0, Saturday=6)."]),
            ("With pinned `dayNum = 3`, what is `day` in the full name switch?", ["**Wednesday**."]),
            ("What does `break` do?", ["It **leaves** the switch so later cases do not run."]),
            ("What is fall-through?", ["Missing `break` lets execution **continue into the next `case`**."]),
            ("With `dayNum = 3` and only weekend cases, what is `text`?", ["**Looking forward to the Weekend** (the **default**)."]),
            ("Must `default` be last?", ["**No**, but then end it with **`break`**."]),
            ("What do cases 4 and 5 share?", ["**Soon it is Weekend**."]),
            ("What do cases 0 and 6 share?", ["**It is Weekend**."]),
            ('Does `switch ("0")` match `case 0`?', ["**No.** Switch uses **`===`**. The string **\"0\"** is not the number **0**."]),
            ("With `x = 0` (number), what is `text`?", ["**Off**."]),
        ],
        "`switch` matches with **`===`**. Pin **3** → **Wednesday**. Skip **`break`** and you **fall through**. **`default`** catches other weekdays. Shared labels group Thu/Fri and Sun/Sat. **`\"0\"`** does not match **`case 0`**.",
        "js_switch.asp",
        [("MDN: switch", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch")],
        8774,
        "js_switch.md",
    )
    run(
        "js-booleans",
        "JS Booleans",
        BOOLEANS,
        "A **Boolean** is only **`true`** or **`false`** (lowercase, unquoted). Comparisons, `if` tests, and loop conditions all produce or use booleans. **`Boolean(value)`** converts. Most values are **truthy**; **0, -0, \"\", undefined, null, false, NaN** are **falsy**. Do **not** use **`new Boolean()`**.",
        [
            "**true** / **false** are the only boolean primitives. Write them **lowercase** without quotes.",
            "Comparisons (`==`, `!=`, `<`, `>`) **return** booleans. `if` and loops **test** them.",
            "**Truthy:** numbers other than 0, non-empty strings (including `\"false\"`), arrays, objects. **Falsy:** 0, -0, \"\", undefined, null, false, NaN.",
            "`Boolean()` converts. `(10 > 9)` is already a boolean. **`new Boolean()`** makes an **object** — avoid it.",
        ],
        [
            ("What values can a boolean primitive hold?", ["Only **true** and **false**."]),
            ("Must they be lowercase and unquoted?", ["**Yes.** `True` or `\"false\"` are not the boolean keywords."]),
            ("With `x = 5`, what is `x == 8` and `x != 8`?", ["**false** and **true**."]),
            ("What is `Boolean(10 > 9)`?", ["**true**."]),
            ("Is `Boolean(\"false\")` false?", ["**No.** A non-empty string is **true**."]),
            ("Are `[]` and `{}` true or false?", ["**true** — they are objects, and objects are truthy."]),
            ("Name the falsy values from this page.", ["**0**, **-0**, **\"\"**, **undefined**, **null**, **false**, **NaN**."]),
            ("What is `typeof new Boolean(false)`?", ["**object** (the primitive is **boolean**)."]),
            ("Does `Boolean(false) === new Boolean(false)`?", ["**No** (`===` is false). Loose `==` can be **true**."]),
            ("Does `new Boolean(false) == new Boolean(false)`?", ["**No.** Two objects compare **false**."]),
        ],
        "Booleans are **true**/**false**. Comparisons and `if`/`while` use them. **`Boolean(10 > 9)`** is **true**. Most values are truthy; **0, -0, \"\", undefined, null, false, NaN** are not. Skip **`new Boolean()`**.",
        "js_booleans.asp",
        [
            ("MDN: Boolean", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean"),
            ("JS Boolean Reference (W3Schools)", "https://www.w3schools.com/jsref/jsref_obj_boolean.asp"),
        ],
        8775,
        "js_booleans.md",
    )
    run(
        "js-logical",
        "JS Logical",
        LOGICAL,
        "Logical operators combine boolean tests: **`&&`** (AND), **`||`** (OR), **`!`** (NOT). **`??`** (nullish coalescing, ES2020) picks a fallback only for **`null`/`undefined`**, so **0** and **`\"\"`** can stay.",
        [
            "Given **x = 6**, **y = 3**: **`x < 10 && y > 1`** is true; **`x === 5 || y === 5`** is false; **`!(x === y)`** is true.",
            "**`&&`** needs both true. **`||`** needs at least one true. **`!`** negates.",
            "**`??`** returns the right side only when the left is **nullish**. Prefer it over `||` when **0** or **\"\"** are valid.",
        ],
        [
            ("When is `&&` true?", ["When **both** operands are true."]),
            ("With x=6 y=3, what is `(x < 10 && y > 1)`?", ["**true**."]),
            ("With x=6 y=3, what is `(x === 5 || y === 5)`?", ["**false**."]),
            ("With x=6 y=3, what is `!(x === y)`?", ["**true**."]),
            ("With x=6 y=-3, what is `(x > 0 || y > 0)`?", ["**true** (x > 0)."]),
            ("What is `(5 == 8)` and `!(5 == 8)`?", ["**false** and **true**."]),
            ("What does `null ?? \"missing\"` return?", ["**missing**."]),
            ("What is `0 ?? 5` vs `0 || 5`?", ["**0** vs **5**. `??` keeps 0; `||` treats 0 as missing."]),
            ("When was `??` added?", ["**ES2020** (widely supported since late 2020)."]),
            ("Does `&&` evaluate the right side if the left is false?", ["**No.** It **short-circuits**."]),
        ],
        "**`&&`** / **`||`** / **`!`** combine tests (table: true / false / true with x=6 y=3). OR with y=-3 is still true via x>0. **`??`** replaces only **null/undefined** — **0 ?? 5** stays **0**.",
        "js_logical.asp",
        [
            ("MDN: Logical AND (&&)", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND"),
            ("MDN: Nullish coalescing (??)", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing"),
        ],
        8776,
        "js_logical.md",
    )


if __name__ == "__main__":
    main()
