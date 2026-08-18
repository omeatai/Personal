"""S10: JS Date Formats, Get, Set, and Methods (not JS Dates landing)."""
from __future__ import annotations

from _gen_lib import S, build_and_snap

# Date-only ISO is UTC midnight. This machine is Mountain (UTC−6 / UTC−7).
TZ = (
    "Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**, not local midnight. "
    "In US zones, local `getDate` / `getHours` / `getDay` can fall on the **previous** calendar day."
)
ISO25 = 'const d = new Date("2021-03-25");'
NOW = "const d = new Date();"
JAN = 'const d = new Date("January 01, 2025");'
FIX = 'const d = new Date("2021-03-25T15:30:45.123Z");'


# ---------------------------------------------------------------------------
# 10.2 JS Date Formats
# ---------------------------------------------------------------------------

FORMATS = [
    S(
        "iso-complete",
        'new Date("2015-03-25") — ISO complete',
        [
            "ISO **YYYY-MM-DD** is the preferred JavaScript date string.",
            TZ,
            "The page notes the printed day may be **March 24 or 25** depending on zone.",
        ],
        'const d = new Date("2015-03-25");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "UTC is **2015-03-25T00:00:00.000Z**. Local print is **Tue Mar 24 2015 18:00:00 GMT-0600** "
        "(Mountain). The engine did **not** use March 25 local midnight.",
    ),
    S(
        "iso-year-month",
        'new Date("2015-03") — year and month',
        [
            "ISO may omit the day: **YYYY-MM** is the first of that month **UTC**.",
            "The page says the local day may be **February 28 or March 01**.",
        ],
        'const d = new Date("2015-03");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "UTC is **2015-03-01T00:00:00.000Z**. Local print is **Sat Feb 28 2015 17:00:00 GMT-0700** "
        "(Mountain Standard — DST had not started yet).",
    ),
    S(
        "iso-year-only",
        'new Date("2015") — year only',
        [
            "ISO **YYYY** is January 1 **UTC** of that year.",
            "The page says the local day may be **December 31 2014 or January 01 2015**.",
        ],
        'const d = new Date("2015");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "UTC is **2015-01-01T00:00:00.000Z**. Local print is **Wed Dec 31 2014 17:00:00 GMT-0700**.",
    ),
    S(
        "iso-datetime-z",
        'new Date("2015-03-25T12:00:00Z")',
        [
            "Date and time are split by a capital **`T`**. **`Z`** means **UTC** (same idea as GMT).",
            "`12:00:00Z` is noon UTC on March 25, 2015.",
        ],
        'const d = new Date("2015-03-25T12:00:00Z");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "UTC stays **2015-03-25T12:00:00.000Z**. Local print is **Wed Mar 25 2015 06:00:00 GMT-0600**.",
    ),
    S(
        "iso-datetime-offset",
        'new Date("2015-03-25T12:00:00-06:30")',
        [
            "Drop **`Z`** and add **`+HH:MM`** or **`-HH:MM`** to shift relative to UTC.",
            "`12:00:00-06:30` is 12:00 in a zone six-and-a-half hours behind UTC (**18:30Z**).",
        ],
        'const d = new Date("2015-03-25T12:00:00-06:30");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "UTC is **2015-03-25T18:30:00.000Z**. Local print is **Wed Mar 25 2015 12:30:00 GMT-0600**.",
    ),
    S(
        "short-mm-dd-yyyy",
        'new Date("03/25/2015") — short MM/DD/YYYY',
        [
            "Short dates use **MM/DD/YYYY** (US order).",
            "Unlike date-only ISO, this form is treated as **local** midnight in this engine.",
        ],
        'const d = new Date("03/25/2015");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "Local print is **Wed Mar 25 2015 00:00:00 GMT-0600**. ISO is **2015-03-25T06:00:00.000Z**.",
    ),
    S(
        "warn-no-leading-zero",
        'WARNING new Date("2015-3-25") — no leading zero',
        [
            "**Warning:** months or days **without leading zeros** may fail in some browsers.",
            "Run it and report what **this** engine did — do not assume Invalid Date.",
        ],
        'const d = new Date("2015-3-25");',
        [
            ("d", "String(d)"),
            ("Number.isNaN(d.getTime())", "Number.isNaN(d.getTime())"),
        ],
        "This V8 engine **parsed** it as **Wed Mar 25 2015 00:00:00** local — **not** Invalid Date. "
        "The format is still unsafe. Prefer **`2015-03-25`** (ISO, UTC) or a tested long/short form.",
    ),
    S(
        "warn-yyyy-slash",
        'WARNING new Date("2015/03/25") — YYYY/MM/DD',
        [
            "**Warning:** **YYYY/MM/DD** is **undefined**. Some browsers guess; some return NaN.",
        ],
        'const d = new Date("2015/03/25");',
        [
            ("d", "String(d)"),
            ("Number.isNaN(d.getTime())", "Number.isNaN(d.getTime())"),
        ],
        "This engine parsed it as **Wed Mar 25 2015 00:00:00** local. Still **do not rely** on slashes-in-ISO-order.",
    ),
    S(
        "warn-dd-mm-yyyy",
        'WARNING new Date("25-03-2015") — DD-MM-YYYY',
        [
            "**Warning:** **DD-MM-YYYY** is also **undefined**.",
            "`toISOString()` throws on an invalid Date, so this demo prints `String(d)` and `getTime()`.",
        ],
        'const d = new Date("25-03-2015");',
        [
            ("d", "String(d)"),
            ("d.getTime()", "d.getTime()"),
            ("Number.isNaN(d.getTime())", "Number.isNaN(d.getTime())"),
        ],
        "This engine returns **Invalid Date** (`getTime()` is **NaN**). Do not use day-first hyphen dates.",
    ),
    S(
        "long-mar-25",
        'new Date("Mar 25 2015")',
        [
            "Long dates are often **MMM DD YYYY**.",
            "This form is **local** midnight here (not UTC).",
        ],
        'const d = new Date("Mar 25 2015");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "**Wed Mar 25 2015 00:00:00 GMT-0600**. ISO **2015-03-25T06:00:00.000Z**.",
    ),
    S(
        "long-25-mar",
        'new Date("25 Mar 2015")',
        [
            "Month and day may appear in **either order**.",
        ],
        'const d = new Date("25 Mar 2015");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "Same instant as `Mar 25 2015`: **Wed Mar 25 2015 00:00:00** local.",
    ),
    S(
        "long-january",
        'new Date("January 25 2015")',
        [
            "The month may be written in **full** (`January`).",
        ],
        'const d = new Date("January 25 2015");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "**Sun Jan 25 2015 00:00:00 GMT-0700** (Mountain Standard in January).",
    ),
    S(
        "long-jan",
        'new Date("Jan 25 2015")',
        [
            "The month may be **abbreviated** (`Jan`).",
        ],
        'const d = new Date("Jan 25 2015");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "Same as the full-month form: **Sun Jan 25 2015 00:00:00 GMT-0700**.",
    ),
    S(
        "long-january-commas",
        'new Date("JANUARY, 25, 2015")',
        [
            "**Commas are ignored.** Month names are **case insensitive**.",
        ],
        'const d = new Date("JANUARY, 25, 2015");',
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "Still **Sun Jan 25 2015 00:00:00 GMT-0700**.",
    ),
    S(
        "date-parse-msec",
        'Date.parse("March 21, 2012") — milliseconds',
        [
            "`Date.parse(string)` returns **milliseconds** since 1 January 1970 UTC.",
            "A long date string is typically parsed as **local** time.",
        ],
        'let msec = Date.parse("March 21, 2012");',
        [("msec", "msec")],
        "This engine returned **1332309600000** (local midnight March 21, 2012 in Mountain time). "
        "The number is timezone-dependent.",
    ),
    S(
        "date-parse-then-date",
        "Date.parse then new Date(msec)",
        [
            "Pass the millisecond count to **`new Date(msec)`** to get a Date object.",
        ],
        'let msec = Date.parse("March 21, 2012");\nconst d = new Date(msec);',
        [("msec", "msec"), ("d", "String(d)")],
        "msec is **1332309600000**. d prints **Wed Mar 21 2012 00:00:00 GMT-0600**.",
    ),
]


# ---------------------------------------------------------------------------
# 10.3 JS Date Get
# ---------------------------------------------------------------------------

MONTHS_ARR = (
    'const months = ["January", "February", "March", "April", "May", "June", '
    '"July", "August", "September", "October", "November", "December"];'
)
DAYS_ARR = (
    'const days = ["Sunday", "Monday", "Tuesday", "Wednesday", '
    '"Thursday", "Friday", "Saturday"];'
)


def _get_fixed(stem: str, title: str, bullets: list[str], expr: str, displays: list, outcome: str) -> dict:
    return S(stem, title, bullets, f"{ISO25}\n{expr}", displays, outcome)


def _get_now(stem: str, title: str, bullets: list[str], expr: str, displays: list, outcome: str) -> dict:
    return S(stem, title, bullets, f"{NOW}\n{expr}", displays, outcome)


GETS = [
    S(
        "new-date-now",
        "new Date() — current time",
        [
            "`new Date()` returns a Date for **now** (local when printed).",
            "The object is a **snapshot** — its clock does not keep ticking.",
        ],
        NOW,
        [("d", "String(d)")],
        "The snap shows the **browser's current local** date/time (not a hardcoded fake clock).",
    ),
    _get_fixed(
        "get-full-year-fixed",
        'getFullYear() on "2021-03-25"',
        [
            "`getFullYear()` is a **four-digit** local year.",
            TZ,
        ],
        "d.getFullYear();",
        [("d.getFullYear()", "d.getFullYear()"), ("d", "String(d)")],
        "`getFullYear()` is **2021**. Local print is **Wed Mar 24 2021 18:00:00 GMT-0600** — year did not roll back.",
    ),
    _get_now(
        "get-full-year-now",
        "getFullYear() on now",
        [
            "Same method on **`new Date()`** (current local year).",
        ],
        "d.getFullYear();",
        [("d.getFullYear()", "d.getFullYear()"), ("d", "String(d)")],
        "The snap shows the **browser's current local** four-digit year.",
    ),
    _get_fixed(
        "get-month-fixed",
        'getMonth() on "2021-03-25"',
        [
            "`getMonth()` is **0–11**. January is **0**, March is **2**, December is **11**.",
            TZ,
        ],
        "d.getMonth();",
        [("d.getMonth()", "d.getMonth()"), ("d", "String(d)")],
        "`getMonth()` is **2** (March). Local calendar day is the **24th**, still in March.",
    ),
    _get_now(
        "get-month-now",
        "getMonth() on now",
        [
            "Current local month as **0–11**.",
        ],
        "d.getMonth();",
        [("d.getMonth()", "d.getMonth()"), ("d", "String(d)")],
        "The snap shows the **browser's current local** month number (0–11).",
    ),
    S(
        "month-name-fixed",
        'months[d.getMonth()] on "2021-03-25"',
        [
            "Index a **names** array with `getMonth()` to print the month word.",
        ],
        f"{MONTHS_ARR}\n{ISO25}\nlet month = months[d.getMonth()];",
        [("month", "month"), ("d.getMonth()", "d.getMonth()")],
        'month is **"March"** (index **2**), even though local `getDate()` is **24**.',
    ),
    S(
        "month-name-now",
        "months[d.getMonth()] on now",
        [
            "Same names array on the **current** date.",
        ],
        f"{MONTHS_ARR}\n{NOW}\nlet month = months[d.getMonth()];",
        [("month", "month"), ("d.getMonth()", "d.getMonth()")],
        "The snap shows the **browser's current local** month **name**.",
    ),
    _get_fixed(
        "get-date-fixed",
        'getDate() on "2021-03-25"',
        [
            "`getDate()` is the **day of the month** (1–31), **local**.",
            TZ + " The page’s Tryit can look like the 25th in UTC zones.",
        ],
        "d.getDate();",
        [("d.getDate()", "d.getDate()"), ("d", "String(d)")],
        "`getDate()` is **24**, not 25. `" + '2021-03-25' + "` is UTC midnight = **March 24, 18:00** Mountain.",
    ),
    _get_now(
        "get-date-now",
        "getDate() on now",
        [
            "Current local **day of month** (1–31).",
        ],
        "d.getDate();",
        [("d.getDate()", "d.getDate()"), ("d", "String(d)")],
        "The snap shows the **browser's current local** day of the month.",
    ),
    _get_fixed(
        "get-hours-fixed",
        'getHours() on "2021-03-25"',
        [
            "`getHours()` is **0–23**, **local**.",
            "UTC midnight is evening the day before in US zones.",
        ],
        "d.getHours();",
        [("d.getHours()", "d.getHours()"), ("d", "String(d)")],
        "`getHours()` is **18** (6 PM Mountain), not 0. UTC hours would be **0** (`getUTCHours()`).",
    ),
    _get_now(
        "get-hours-now",
        "getHours() on now",
        [
            "Current local hour **0–23**.",
        ],
        "d.getHours();",
        [("d.getHours()", "d.getHours()"), ("d", "String(d)")],
        "The snap shows the **browser's current local** hour.",
    ),
    _get_fixed(
        "get-minutes-fixed",
        'getMinutes() on "2021-03-25"',
        [
            "`getMinutes()` is **0–59**, **local**.",
        ],
        "d.getMinutes();",
        [("d.getMinutes()", "d.getMinutes()")],
        "`getMinutes()` is **0** (UTC midnight has zero minutes).",
    ),
    _get_now(
        "get-minutes-now",
        "getMinutes() on now",
        [
            "Current local minutes **0–59**.",
        ],
        "d.getMinutes();",
        [("d.getMinutes()", "d.getMinutes()"), ("d", "String(d)")],
        "The snap shows the **browser's current local** minutes.",
    ),
    _get_fixed(
        "get-seconds-fixed",
        'getSeconds() on "2021-03-25"',
        [
            "`getSeconds()` is **0–59**, **local**.",
        ],
        "d.getSeconds();",
        [("d.getSeconds()", "d.getSeconds()")],
        "`getSeconds()` is **0**.",
    ),
    _get_now(
        "get-seconds-now",
        "getSeconds() on now",
        [
            "Current local seconds **0–59**.",
        ],
        "d.getSeconds();",
        [("d.getSeconds()", "d.getSeconds()"), ("d", "String(d)")],
        "The snap shows the **browser's current local** seconds.",
    ),
    _get_fixed(
        "get-milliseconds-fixed",
        'getMilliseconds() on "2021-03-25"',
        [
            "`getMilliseconds()` is **0–999**, **local**.",
        ],
        "d.getMilliseconds();",
        [("d.getMilliseconds()", "d.getMilliseconds()")],
        "`getMilliseconds()` is **0**.",
    ),
    _get_now(
        "get-milliseconds-now",
        "getMilliseconds() on now",
        [
            "Current local milliseconds **0–999**.",
        ],
        "d.getMilliseconds();",
        [("d.getMilliseconds()", "d.getMilliseconds()"), ("d", "String(d)")],
        "The snap shows the **browser's current local** milliseconds.",
    ),
    _get_fixed(
        "get-day-fixed",
        'getDay() on "2021-03-25"',
        [
            "`getDay()` is the **weekday** **0–6**. **0 is Sunday** (not Monday).",
            "UTC March 25 2021 was **Thursday** (4). Local March 24 was **Wednesday** (3).",
        ],
        "d.getDay();",
        [("d.getDay()", "d.getDay()"), ("d", "String(d)")],
        "`getDay()` is **3** (Wednesday) because local time is **March 24**, not the UTC Thursday.",
    ),
    _get_now(
        "get-day-now",
        "getDay() on now",
        [
            "Current local weekday number **0–6** (Sunday = 0).",
        ],
        "d.getDay();",
        [("d.getDay()", "d.getDay()"), ("d", "String(d)")],
        "The snap shows the **browser's current local** weekday number.",
    ),
    S(
        "day-name-fixed",
        'days[d.getDay()] on "2021-03-25"',
        [
            "Index a weekday-names array with `getDay()`.",
        ],
        f"{DAYS_ARR}\n{ISO25}\nlet day = days[d.getDay()];",
        [("day", "day"), ("d.getDay()", "d.getDay()")],
        'day is **"Wednesday"** (local Mar 24), not Thursday (UTC Mar 25).',
    ),
    S(
        "day-name-now",
        "days[d.getDay()] on now",
        [
            "Same names array on **now**.",
        ],
        f"{DAYS_ARR}\n{NOW}\nlet day = days[d.getDay()];",
        [("day", "day"), ("d.getDay()", "d.getDay()")],
        "The snap shows the **browser's current local** weekday **name**.",
    ),
    S(
        "get-time-epoch",
        'getTime() on "1970-01-01"',
        [
            "`getTime()` is milliseconds since **1 January 1970 UTC** (the epoch).",
            "`\"1970-01-01\"` is UTC midnight, so the count is **0** even if local print is Dec 31 1969.",
        ],
        'const d = new Date("1970-01-01");\nd.getTime();',
        [("d.getTime()", "d.getTime()"), ("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        "`getTime()` is **0**. ISO is **1970-01-01T00:00:00.000Z**. Local print is **Wed Dec 31 1969 17:00:00 GMT-0700**.",
    ),
    _get_fixed(
        "get-time-fixed",
        'getTime() on "2021-03-25"',
        [
            "Milliseconds from the epoch to this UTC midnight.",
        ],
        "d.getTime();",
        [("d.getTime()", "d.getTime()"), ("d.toISOString()", "d.toISOString()")],
        "`getTime()` is **1616630400000** (`2021-03-25T00:00:00.000Z`).",
    ),
    _get_now(
        "get-time-now",
        "getTime() on now",
        [
            "`getTime()` on `new Date()` is the current epoch offset (ms).",
        ],
        "d.getTime();",
        [("d.getTime()", "d.getTime()"), ("d", "String(d)")],
        "The snap shows the **browser's current** millisecond timestamp (not a fake clock).",
    ),
    S(
        "date-now",
        "Date.now()",
        [
            "`Date.now()` is a **static** method: milliseconds since the epoch **right now**.",
            "There is no `myDate.now()` — the syntax is always **`Date.now()`**.",
        ],
        "let ms = Date.now();",
        [("ms", "ms")],
        "The snap shows the **browser's current** `Date.now()` value.",
    ),
    S(
        "years-since-1970",
        "Years since 1970 (page formula)",
        [
            "The page approximates years as **365-day** chunks (no leap days).",
            "`Math.round(Date.now() / year)` is a rough year count, not a calendar year.",
        ],
        "const minute = 1000 * 60;\nconst hour = minute * 60;\nconst day = hour * 24;\nconst year = day * 365;\nlet years = Math.round(Date.now() / year);",
        [("years", "years"), ("year (ms)", "year")],
        "The snap shows the **browser's current** rounded 365-day year count since 1970 "
        "(about **56** in 2026). It is not `getFullYear() - 1970`.",
    ),
    S(
        "get-timezone-offset",
        "getTimezoneOffset()",
        [
            "`getTimezoneOffset()` is **minutes** to add to **local** time to get **UTC**.",
            "West of UTC the value is **positive** (Mountain daylight = **360**).",
        ],
        "const d = new Date();\nlet diff = d.getTimezoneOffset();",
        [("diff", "diff"), ("d", "String(d)")],
        "The snap shows the **browser's current local** offset in minutes "
        "(this Mountain daylight zone prints **360**).",
    ),
    S(
        "get-year-deprecated",
        "getYear() — deprecated; use getFullYear()",
        [
            "**Deprecated.** Old engines used `getYear()` (often **year − 1900**).",
            "**Do not use it.** Use **`getFullYear()`**.",
        ],
        f"{ISO25}\nd.getYear();\nd.getFullYear();",
        [("d.getYear()", "d.getYear()"), ("d.getFullYear()", "d.getFullYear()")],
        "`getYear()` is **121** (2021 − 1900). `getFullYear()` is **2021**. Do **not** use `getYear()`.",
    ),
]

# UTC table — no Tryits on the page; still one Example per row, fixed Date.
for _stem, _title, _method, _val, _desc in [
    ("get-utc-date", "getUTCDate()", "getUTCDate", "25", "UTC day of month (1–31). Same idea as getDate() but UTC."),
    ("get-utc-full-year", "getUTCFullYear()", "getUTCFullYear", "2021", "UTC four-digit year."),
    ("get-utc-month", "getUTCMonth()", "getUTCMonth", "2", "UTC month 0–11. March is 2."),
    ("get-utc-day", "getUTCDay()", "getUTCDay", "4", "UTC weekday 0–6. March 25 2021 UTC was Thursday (4)."),
    ("get-utc-hours", "getUTCHours()", "getUTCHours", "0", "UTC hour 0–23. Date-only ISO is midnight UTC."),
    ("get-utc-minutes", "getUTCMinutes()", "getUTCMinutes", "0", "UTC minutes 0–59."),
    ("get-utc-seconds", "getUTCSeconds()", "getUTCSeconds", "0", "UTC seconds 0–59."),
    ("get-utc-milliseconds", "getUTCMilliseconds()", "getUTCMilliseconds", "0", "UTC milliseconds 0–999."),
]:
    GETS.append(
        S(
            _stem,
            _title,
            [_desc, 'No Tryit on the page — still run on `new Date("2021-03-25")` (UTC midnight).'],
            f"{ISO25}\nd.{_method}();",
            [(f"d.{_method}()", f"d.{_method}()"), ("d.toISOString()", "d.toISOString()")],
            f"`{_method}()` is **{_val}**. ISO is **2021-03-25T00:00:00.000Z**. "
            "Local getters on the same object can disagree (see getDate / getHours / getDay).",
        )
    )


# ---------------------------------------------------------------------------
# 10.4 JS Date Set
# ---------------------------------------------------------------------------

SETS = [
    S(
        "set-full-year",
        "setFullYear(2020) on January 01, 2025",
        [
            "`setFullYear(year)` sets the **local** year. Other fields stay put.",
            "Start from `new Date(\"January 01, 2025\")` as the page does.",
        ],
        f"{JAN}\nd.setFullYear(2020);",
        [("d", "String(d)")],
        "After the set, d is **Wed Jan 01 2020 00:00:00 GMT-0700**.",
    ),
    S(
        "set-full-year-ymd",
        "setFullYear(2020, 11, 3)",
        [
            "`setFullYear` can also set **month** and **day**.",
            "Month **11** is **December** (0–11).",
        ],
        f"{JAN}\nd.setFullYear(2020, 11, 3);",
        [("d", "String(d)")],
        "After the set, d is **Thu Dec 03 2020 00:00:00 GMT-0700**.",
    ),
    S(
        "set-month",
        "setMonth(11)",
        [
            "`setMonth(month)` uses **0–11**. **11** is December.",
        ],
        f"{JAN}\nd.setMonth(11);",
        [("d", "String(d)")],
        "After the set, d is **Mon Dec 01 2025 00:00:00 GMT-0700**.",
    ),
    S(
        "set-date",
        "setDate(15)",
        [
            "`setDate(day)` sets the **day of month** (1–31), local.",
        ],
        f"{JAN}\nd.setDate(15);",
        [("d", "String(d)")],
        "After the set, d is **Wed Jan 15 2025 00:00:00 GMT-0700**.",
    ),
    S(
        "set-date-add-50",
        "setDate(d.getDate() + 50) — add days",
        [
            "You can **add days** with `setDate(d.getDate() + n)`.",
            "Overflow into the next month/year is handled automatically.",
        ],
        f"{JAN}\nd.setDate(d.getDate() + 50);",
        [("d", "String(d)")],
        "January 1 + 50 days is **Thu Feb 20 2025 00:00:00 GMT-0700**.",
    ),
    S(
        "set-hours",
        "setHours(22)",
        [
            "`setHours(hour)` sets the local hour **0–23**.",
        ],
        f"{JAN}\nd.setHours(22);",
        [("d", "String(d)")],
        "After the set, d is **Wed Jan 01 2025 22:00:00 GMT-0700**.",
    ),
    S(
        "set-hours-hms",
        "setHours(22, 10, 20)",
        [
            "`setHours` can also set **minutes** and **seconds**.",
        ],
        f"{JAN}\nd.setHours(22, 10, 20);",
        [("d", "String(d)")],
        "After the set, d is **Wed Jan 01 2025 22:10:20 GMT-0700**.",
    ),
    S(
        "set-minutes",
        "setMinutes(30)",
        [
            "`setMinutes(min)` sets local minutes **0–59**.",
        ],
        f"{JAN}\nd.setMinutes(30);",
        [("d", "String(d)")],
        "After the set, d is **Wed Jan 01 2025 00:30:00 GMT-0700**.",
    ),
    S(
        "set-seconds",
        "setSeconds(30)",
        [
            "`setSeconds(sec)` sets local seconds **0–59**.",
        ],
        f"{JAN}\nd.setSeconds(30);",
        [("d", "String(d)")],
        "After the set, d is **Wed Jan 01 2025 00:00:30 GMT-0700**.",
    ),
    S(
        "compare-today-2100",
        "Compare today vs January 14, 2100",
        [
            "Date objects compare with **`>` / `<`** (they use their millisecond values).",
            "January is month **0**. `setFullYear(2100, 0, 14)` is January 14, 2100.",
        ],
        'let text = "";\nconst today = new Date();\nconst someday = new Date();\nsomeday.setFullYear(2100, 0, 14);\nif (someday > today) {\n  text = "Today is before January 14, 2100.";\n} else {\n  text = "Today is after January 14, 2100.";\n}',
        [("text", "text"), ("today", "String(today)"), ("someday", "String(someday)")],
        'text is **"Today is before January 14, 2100."** (the snap’s `today` is the **browser\'s current local** time).',
    ),
    S(
        "set-milliseconds",
        "setMilliseconds(500) — extra (table row, no Tryit)",
        [
            "`setMilliseconds(ms)` sets local milliseconds **0–999**.",
            "No Tryit on the page — still run it. `toString()` may hide ms; print `getMilliseconds()`.",
        ],
        f"{JAN}\nd.setMilliseconds(500);",
        [("d", "String(d)"), ("d.getMilliseconds()", "d.getMilliseconds()"), ("d.toISOString()", "d.toISOString()")],
        "`getMilliseconds()` is **500**. ISO is **2025-01-01T07:00:00.500Z**.",
    ),
    S(
        "set-time-epoch",
        "setTime(0) — epoch (extra; table row, no Tryit)",
        [
            "`setTime(ms)` sets the instant as milliseconds since **1 January 1970 UTC**.",
            "**0** is the epoch. Local `toString()` may show **31 December 1969** in US zones.",
        ],
        f"{JAN}\nd.setTime(0);",
        [("d", "String(d)"), ("d.getTime()", "d.getTime()"), ("d.toISOString()", "d.toISOString()")],
        "`getTime()` is **0**. ISO is **1970-01-01T00:00:00.000Z**. Local print is **Wed Dec 31 1969 17:00:00 GMT-0700**.",
    ),
]


# ---------------------------------------------------------------------------
# 10.5 JS Date Methods (reference table — every row is an Example)
# ---------------------------------------------------------------------------

METHODS: list[dict] = [
    S(
        "new-date-now",
        "new Date() — current date and time",
        [
            "`new Date()` creates a Date for **now**.",
        ],
        "const d = new Date();",
        [("d", "String(d)")],
        "The snap shows the **browser's current local** date/time.",
    ),
    S(
        "constructor-create",
        "constructor — creates a new Date object",
        [
            "The **Date constructor** creates a Date from a string, numbers, or ms.",
            "This row is the “creates a new Date object” meaning of `constructor`.",
        ],
        f"{FIX}\nd instanceof Date;",
        [("d", "String(d)"), ("d instanceof Date", "d instanceof Date"), ("d.toISOString()", "d.toISOString()")],
        "d is a Date for **2021-03-25T15:30:45.123Z**. `instanceof Date` is **true**. "
        "Local print is **Thu Mar 25 2021 09:30:45 GMT-0600**.",
    ),
    S(
        "constructor-prototype-fn",
        "constructor — function that created Date.prototype",
        [
            "Instance **`constructor`** is the function that created the prototype: **`Date`**.",
            "This is the second `constructor` row on the table (revised April 2026).",
        ],
        f"{FIX}\nd.constructor;\nd.constructor === Date;",
        [
            ("String(d.constructor)", "String(d.constructor)"),
            ("d.constructor === Date", "d.constructor === Date"),
        ],
        '`d.constructor` prints **function Date() { [native code] }**. `d.constructor === Date` is **true**.',
    ),
]


def _m_get(stem: str, method: str, meaning: str, value: str, extra: str = "") -> dict:
    bullets = [f"`{method}()` {meaning}."]
    if extra:
        bullets.append(extra)
    return S(
        stem,
        f"{method}()",
        bullets,
        f"{FIX}\nd.{method}();",
        [(f"d.{method}()", f"d.{method}()"), ("d.toISOString()", "d.toISOString()")],
        f"`{method}()` is **{value}** on `2021-03-25T15:30:45.123Z` "
        "(local **Thu Mar 25 2021 09:30:45 GMT-0600**).",
    )


METHODS += [
    _m_get("get-date", "getDate", "returns the local day of month (1–31)", "25"),
    _m_get("get-day", "getDay", "returns the local weekday (0–6, Sunday = 0)", "4", "March 25 2021 local was **Thursday**."),
    _m_get("get-full-year", "getFullYear", "returns the local four-digit year", "2021"),
    _m_get("get-hours", "getHours", "returns the local hour (0–23)", "9"),
    _m_get("get-milliseconds", "getMilliseconds", "returns local milliseconds (0–999)", "123"),
    _m_get("get-minutes", "getMinutes", "returns the local minutes (0–59)", "30"),
    _m_get("get-month", "getMonth", "returns the local month (0–11)", "2", "March is **2**."),
    _m_get("get-seconds", "getSeconds", "returns the local seconds (0–59)", "45"),
    _m_get("get-time", "getTime", "returns ms since 1 Jan 1970 UTC", "1616686245123"),
    _m_get(
        "get-timezone-offset",
        "getTimezoneOffset",
        "returns minutes to add to local time to get UTC",
        "360",
        "This Mountain daylight zone is UTC−6, so **360**.",
    ),
    _m_get("get-utc-date", "getUTCDate", "returns the UTC day of month (1–31)", "25"),
    _m_get("get-utc-day", "getUTCDay", "returns the UTC weekday (0–6)", "4"),
    _m_get("get-utc-full-year", "getUTCFullYear", "returns the UTC year", "2021"),
    _m_get("get-utc-hours", "getUTCHours", "returns the UTC hour (0–23)", "15"),
    _m_get("get-utc-milliseconds", "getUTCMilliseconds", "returns UTC milliseconds (0–999)", "123"),
    _m_get("get-utc-minutes", "getUTCMinutes", "returns UTC minutes (0–59)", "30"),
    _m_get("get-utc-month", "getUTCMonth", "returns the UTC month (0–11)", "2"),
    _m_get("get-utc-seconds", "getUTCSeconds", "returns UTC seconds (0–59)", "45"),
    S(
        "get-year-deprecated",
        "getYear() — deprecated; use getFullYear()",
        [
            "**Deprecated.** Often returns **year − 1900**. **Do not use.** Use **`getFullYear()`**.",
        ],
        f"{FIX}\nd.getYear();\nd.getFullYear();",
        [("d.getYear()", "d.getYear()"), ("d.getFullYear()", "d.getFullYear()")],
        "`getYear()` is **121**. `getFullYear()` is **2021**. Do **not** use `getYear()`.",
    ),
    S(
        "date-now",
        "now() — Date.now()",
        [
            "`Date.now()` is **static**: ms since the epoch **right now**.",
            "Call it on **Date**, not on an instance.",
        ],
        "let ms = Date.now();",
        [("ms", "ms")],
        "The snap shows the **browser's current** `Date.now()` millisecond count.",
    ),
    S(
        "date-parse",
        "parse() — Date.parse()",
        [
            "`Date.parse(string)` returns ms since the epoch, or **NaN** if it cannot parse.",
        ],
        'let msec = Date.parse("2021-03-25T15:30:45.123Z");',
        [("msec", "msec")],
        "`Date.parse` of this ISO UTC string is **1616686245123** (same as `getTime()` on that instant).",
    ),
    S(
        "date-prototype",
        "prototype — tiny add-on (this page only)",
        [
            "`Date.prototype` lets you add methods. Prefer **not** to ship prototype pollution.",
            "A function on `Date.prototype` **in this page only** is OK as a demo.",
        ],
        'Date.prototype.toISODate = function () {\n  return this.toISOString().slice(0, 10);\n};\n'
        f"{FIX}\nd.toISODate();",
        [("d.toISODate()", "d.toISODate()"), ("d.toISOString()", "d.toISOString()")],
        '`toISODate()` is **"2021-03-25"** (UTC calendar date). Isolated to this sandbox file.',
    ),
]


def _m_set(stem: str, call: str, meaning: str, local: str, iso: str) -> dict:
    return S(
        stem,
        call,
        [f"`{call}` {meaning}.", "Fixed start: `new Date(\"2021-03-25T15:30:45.123Z\")`. Show the date **after** the set."],
        f"{FIX}\nd.{call};",
        [("d", "String(d)"), ("d.toISOString()", "d.toISOString()")],
        f"After `{call}`, local print is **{local}**. ISO is **{iso}**.",
    )


METHODS += [
    _m_set("set-date", "setDate(1)", "sets the local day of month", "Mon Mar 01 2021 09:30:45 GMT-0700 (Mountain Standard Time)", "2021-03-01T16:30:45.123Z"),
    _m_set("set-full-year", "setFullYear(2020)", "sets the local year", "Wed Mar 25 2020 09:30:45 GMT-0600 (Mountain Daylight Time)", "2020-03-25T15:30:45.123Z"),
    _m_set("set-hours", "setHours(0)", "sets the local hour (0–23)", "Thu Mar 25 2021 00:30:45 GMT-0600 (Mountain Daylight Time)", "2021-03-25T06:30:45.123Z"),
    _m_set("set-milliseconds", "setMilliseconds(0)", "sets local milliseconds", "Thu Mar 25 2021 09:30:45 GMT-0600 (Mountain Daylight Time)", "2021-03-25T15:30:45.000Z"),
    _m_set("set-minutes", "setMinutes(0)", "sets local minutes", "Thu Mar 25 2021 09:00:45 GMT-0600 (Mountain Daylight Time)", "2021-03-25T15:00:45.123Z"),
    _m_set("set-month", "setMonth(0)", "sets the local month (0–11); 0 is January", "Mon Jan 25 2021 09:30:45 GMT-0700 (Mountain Standard Time)", "2021-01-25T16:30:45.123Z"),
    _m_set("set-seconds", "setSeconds(0)", "sets local seconds", "Thu Mar 25 2021 09:30:00 GMT-0600 (Mountain Daylight Time)", "2021-03-25T15:30:00.123Z"),
    _m_set("set-time", "setTime(0)", "sets ms since 1 Jan 1970 UTC; 0 is the epoch", "Wed Dec 31 1969 17:00:00 GMT-0700 (Mountain Standard Time)", "1970-01-01T00:00:00.000Z"),
    _m_set("set-utc-date", "setUTCDate(1)", "sets the UTC day of month", "Mon Mar 01 2021 08:30:45 GMT-0700 (Mountain Standard Time)", "2021-03-01T15:30:45.123Z"),
    _m_set("set-utc-full-year", "setUTCFullYear(2020)", "sets the UTC year", "Wed Mar 25 2020 09:30:45 GMT-0600 (Mountain Daylight Time)", "2020-03-25T15:30:45.123Z"),
    _m_set("set-utc-hours", "setUTCHours(0)", "sets the UTC hour", "Wed Mar 24 2021 18:30:45 GMT-0600 (Mountain Daylight Time)", "2021-03-25T00:30:45.123Z"),
    _m_set("set-utc-milliseconds", "setUTCMilliseconds(0)", "sets UTC milliseconds", "Thu Mar 25 2021 09:30:45 GMT-0600 (Mountain Daylight Time)", "2021-03-25T15:30:45.000Z"),
    _m_set("set-utc-minutes", "setUTCMinutes(0)", "sets UTC minutes", "Thu Mar 25 2021 09:00:45 GMT-0600 (Mountain Daylight Time)", "2021-03-25T15:00:45.123Z"),
    _m_set("set-utc-month", "setUTCMonth(0)", "sets the UTC month (0–11)", "Mon Jan 25 2021 08:30:45 GMT-0700 (Mountain Standard Time)", "2021-01-25T15:30:45.123Z"),
    _m_set("set-utc-seconds", "setUTCSeconds(0)", "sets UTC seconds", "Thu Mar 25 2021 09:30:00 GMT-0600 (Mountain Daylight Time)", "2021-03-25T15:30:00.123Z"),
    S(
        "set-year-deprecated",
        "setYear(99) — deprecated; use setFullYear()",
        [
            "**Deprecated.** Years **0–99** become **19xx**. **Do not use.** Use **`setFullYear()`**.",
        ],
        f"{FIX}\nd.setYear(99);",
        [("d", "String(d)"), ("d.getFullYear()", "d.getFullYear()"), ("d.toISOString()", "d.toISOString()")],
        "After `setYear(99)`, local print is **Thu Mar 25 1999 09:30:45 GMT-0700**. "
        "`getFullYear()` is **1999**. Do **not** use `setYear()`.",
    ),
    S(
        "to-date-string",
        "toDateString()",
        [
            "`toDateString()` is a readable **local date** (no time).",
        ],
        f"{FIX}\nd.toDateString();",
        [("d.toDateString()", "d.toDateString()")],
        '`toDateString()` is **"Thu Mar 25 2021"**.',
    ),
    S(
        "to-gmt-string-deprecated",
        "toGMTString() — deprecated; use toUTCString()",
        [
            "**Deprecated** alias of `toUTCString()`. **Do not use.** Use **`toUTCString()`**.",
        ],
        f"{FIX}\nd.toGMTString();\nd.toUTCString();",
        [("d.toGMTString()", "d.toGMTString()"), ("d.toUTCString()", "d.toUTCString()")],
        'Both print **"Thu, 25 Mar 2021 15:30:45 GMT"**. Do **not** use `toGMTString()`.',
    ),
    S(
        "to-iso-string",
        "toISOString()",
        [
            "`toISOString()` is **ISO 8601 UTC** (`...Z`).",
        ],
        f"{FIX}\nd.toISOString();",
        [("d.toISOString()", "d.toISOString()")],
        '`toISOString()` is **"2021-03-25T15:30:45.123Z"**.',
    ),
    S(
        "to-json",
        "toJSON()",
        [
            "`toJSON()` is the JSON date form — same ISO UTC string as `toISOString()`.",
        ],
        f"{FIX}\nd.toJSON();\nJSON.stringify({'{'} when: d {'}'});",
        [("d.toJSON()", "d.toJSON()"), ("JSON.stringify({ when: d })", "JSON.stringify({ when: d })")],
        '`toJSON()` is **"2021-03-25T15:30:45.123Z"**. `JSON.stringify` uses that string.',
    ),
    S(
        "to-locale-date-string",
        "toLocaleDateString()",
        [
            "`toLocaleDateString()` is the **date** part using **locale** conventions.",
        ],
        f"{FIX}\nd.toLocaleDateString();",
        [("d.toLocaleDateString()", "d.toLocaleDateString()")],
        "The snap shows this browser's **locale date** for the same instant "
        "(local **March 25, 2021** — not a hardcoded fake).",
    ),
    S(
        "to-locale-time-string",
        "toLocaleTimeString()",
        [
            "`toLocaleTimeString()` is the **time** part using **locale** conventions.",
        ],
        f"{FIX}\nd.toLocaleTimeString();",
        [("d.toLocaleTimeString()", "d.toLocaleTimeString()")],
        "The snap shows this browser's **locale time** for **09:30:45** Mountain on that instant.",
    ),
    S(
        "to-locale-string",
        "toLocaleString()",
        [
            "`toLocaleString()` is **date and time** using locale conventions.",
        ],
        f"{FIX}\nd.toLocaleString();",
        [("d.toLocaleString()", "d.toLocaleString()")],
        "The snap shows this browser's **locale date+time** for the same instant.",
    ),
    S(
        "to-string",
        "toString()",
        [
            "`toString()` is the default print: local date, time, and zone.",
        ],
        f"{FIX}\nd.toString();",
        [("d.toString()", "d.toString()")],
        '`toString()` is **"Thu Mar 25 2021 09:30:45 GMT-0600 (Mountain Daylight Time)"**.',
    ),
    S(
        "to-time-string",
        "toTimeString()",
        [
            "`toTimeString()` is the **time + zone** part of `toString()`.",
        ],
        f"{FIX}\nd.toTimeString();",
        [("d.toTimeString()", "d.toTimeString()")],
        '`toTimeString()` is **"09:30:45 GMT-0600 (Mountain Daylight Time)"**.',
    ),
    S(
        "to-utc-string",
        "toUTCString()",
        [
            "`toUTCString()` formats the instant in **UTC / GMT**.",
        ],
        f"{FIX}\nd.toUTCString();",
        [("d.toUTCString()", "d.toUTCString()")],
        '`toUTCString()` is **"Thu, 25 Mar 2021 15:30:45 GMT"**.',
    ),
    S(
        "date-utc",
        "UTC() — Date.UTC static",
        [
            "`Date.UTC(y, m, …)` returns **ms** for that **UTC** calendar (months **0–11**).",
            "It does **not** return a Date object — wrap with `new Date(Date.UTC(…))` if you need one.",
        ],
        "let ms = Date.UTC(2021, 2, 25, 15, 30, 45, 123);\nconst d = new Date(ms);",
        [("ms", "ms"), ("d.toISOString()", "d.toISOString()")],
        "`Date.UTC(2021, 2, 25, 15, 30, 45, 123)` is **1616686245123**. ISO is **2021-03-25T15:30:45.123Z**.",
    ),
    S(
        "value-of",
        "valueOf()",
        [
            "`valueOf()` is the primitive ms value — the same number as **`getTime()`**.",
        ],
        f"{FIX}\nd.valueOf();\nd.getTime();",
        [("d.valueOf()", "d.valueOf()"), ("d.getTime()", "d.getTime()")],
        "Both are **1616686245123**.",
    ),
]


def run_all() -> None:
    sections = [
        (
            "js-date-formats",
            "JS Date Formats",
            FORMATS,
            "JavaScript accepts three common date-string families: ISO 8601, short US MM/DD/YYYY, and long month-name forms. ISO is the only strictly specified family. Date-only ISO (YYYY-MM-DD, YYYY-MM, YYYY) is UTC midnight, so US time zones often print the previous local evening. Short and long strings are typically local midnight in this engine. Independent of input, the default print is a full local text string. Date.parse turns a valid string into milliseconds since 1 January 1970 UTC.",
            [
                "**Three input types:** ISO (`2015-03-25`), short (`03/25/2015`), long (`Mar 25 2015` / `25 Mar 2015`).",
                "**ISO date-only is UTC midnight**, not local. This Mountain zone printed **Mar 24 18:00** for `2015-03-25`.",
                "**`T`** separates date and time. **`Z`** is UTC. `+HH:MM` / `-HH:MM` is an offset from UTC.",
                "**Warnings:** no leading zero, `YYYY/MM/DD`, and `DD-MM-YYYY` are unreliable. This engine parsed the first two and returned **Invalid Date** for `25-03-2015`.",
                "Long names are **case insensitive**; **commas are ignored**.",
                "`Date.parse` → milliseconds; `new Date(msec)` rebuilds the Date.",
            ],
            [
                ("What are the three date input types on the page?", ["**ISO**, **short** (MM/DD/YYYY), and **long** (month name)."]),
                ("Is `new Date(\"2015-03-25\")` local midnight?", ["**No.** Date-only ISO is **UTC midnight**.", "This Mountain zone printed **Tue Mar 24 2015 18:00:00 GMT-0600**.", "`toISOString()` is **2015-03-25T00:00:00.000Z**."]),
                ("What did `new Date(\"2015-03\")` print locally?", ["**Sat Feb 28 2015 17:00:00 GMT-0700** (UTC March 1)."]),
                ("What did `new Date(\"2015\")` print locally?", ["**Wed Dec 31 2014 17:00:00 GMT-0700** (UTC January 1 2015)."]),
                ("What do `T` and `Z` mean in ISO date-time?", ["**`T`** separates date from time.", "**`Z`** means **UTC** (GMT)."]),
                ("What is `new Date(\"2015-03-25T12:00:00-06:30\")` in UTC?", ["**2015-03-25T18:30:00.000Z**.", "Local print here is **Wed Mar 25 2015 12:30:00 GMT-0600**."]),
                ("Is short `03/25/2015` UTC or local here?", ["**Local midnight** — **Wed Mar 25 2015 00:00:00 GMT-0600**."]),
                ("Did `new Date(\"2015-3-25\")` fail?", ["**No** in this V8 engine — it parsed as **local March 25**.", "The page is still right: **other browsers may error**. Prefer leading zeros."]),
                ("Did `new Date(\"2015/03/25\")` fail?", ["**No** here — local March 25. The format is still **undefined**."]),
                ("Did `new Date(\"25-03-2015\")` fail?", ["**Yes.** **Invalid Date**, `getTime()` is **NaN**."]),
                ("Are long month names case sensitive?", ["**No.** Commas are **ignored**. `JANUARY, 25, 2015` works."]),
                ("What does `Date.parse(\"March 21, 2012\")` return here?", ["**1332309600000** milliseconds (local midnight that day).", "`new Date(msec)` prints **Wed Mar 21 2012 00:00:00 GMT-0600**."]),
            ],
            "Prefer ISO with a time zone (`Z` or an offset). Treat date-only ISO as UTC midnight — US zones often show the previous local evening. Short and long strings are convenient but implementation-defined; the three warning formats must be tested, not trusted. Date.parse gives milliseconds you can feed back into new Date.",
            [
                ("JS Date Formats (W3Schools)", "https://www.w3schools.com/js/js_date_formats.asp"),
                ("MDN: Date", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date"),
                ("MDN: Date.parse", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse"),
                ("MDN: ISO 8601 date-time", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format"),
            ],
        ),
        (
            "js-date-get",
            "JS Date Get",
            GETS,
            "Get methods read pieces of an existing Date as local time unless the name starts with UTC. new Date() is now; getFullYear, getMonth (0–11), getDate (day of month), getDay (weekday, Sunday = 0), and the time getters return local fields. Date-only ISO like 2021-03-25 is UTC midnight, so in Mountain time getDate is 24, getHours is 18, and getDay is Wednesday — not the UTC Thursday the 25th. getTime and Date.now count milliseconds since 1 January 1970 UTC. getYear is deprecated. The UTC table has no Tryits on the page; each row still has its own Example on the same fixed Date.",
            [
                "Get methods return **local** time unless the name is **`getUTC*`**.",
                "**Months 0–11**, **weekdays 0–6** (Sunday first). Name arrays index those numbers.",
                TZ + " On `\"2021-03-25\"` this zone: `getDate()` **24**, `getHours()` **18**, `getDay()` **3** (Wednesday).",
                "`getTime()` / `Date.now()` are ms since **1970-01-01T00:00:00.000Z**. `getTime()` on that ISO date-only string is **0**.",
                "`Date.now()` is **static** — not `d.now()`.",
                "**`getYear()` is deprecated.** This engine returned **121** for 2021. Use **`getFullYear()`**.",
            ],
            [
                ("Does a Date object keep ticking?", ["**No.** Get methods read a **static snapshot**."]),
                ("What is `getMonth()` for March?", ["**2.** January is **0**, December is **11**."]),
                ("What is `getDate()` on `new Date(\"2021-03-25\")` here?", ["**24**, not 25.", "Date-only ISO is **UTC midnight** = **March 24, 18:00** Mountain."]),
                ("What is `getHours()` on that same Date?", ["**18** local. `getUTCHours()` is **0**."]),
                ("What is `getDay()` on that Date locally vs UTC?", ["Local **3** (Wednesday, Mar 24).", "UTC **4** (Thursday, Mar 25). **0 is Sunday**."]),
                ("What is `months[d.getMonth()]` on that Date?", ['**"March"** — still March even though `getDate()` is 24.']),
                ("What is `getTime()` of `new Date(\"1970-01-01\")`?", ["**0.** ISO is **1970-01-01T00:00:00.000Z**.", "Local print may be **31 Dec 1969**."]),
                ("Can you call `d.now()`?", ["**No.** `Date.now()` is **static** on `Date`."]),
                ("What does the years-since-1970 formula use?", ["**365-day** years (`day * 365`), then `Math.round(Date.now() / year)`.", "It is **not** a calendar year and ignores leaps."]),
                ("What unit is `getTimezoneOffset()`?", ["**Minutes.** Positive **west** of UTC. This daylight Mountain zone is **360**."]),
                ("Why run `getYear()` if it is deprecated?", ["To see it **run**: **121** for 2021.", "**Do not use it.** Use **`getFullYear()`** (**2021**)."]),
                ("What is `getUTCDate()` on `\"2021-03-25\"`?", ["**25** — the UTC calendar day, while local `getDate()` is **24**."]),
                ("What do “now” snaps represent?", ["The **browser's current local** value at screenshot time — not a fake hardcoded clock."]),
            ],
            "Read local fields with getFullYear, getMonth, getDate, getDay, and the time getters; read UTC with the getUTC* twins. Date-only ISO is UTC midnight, so US local getters can show the previous evening. getTime and Date.now are epoch milliseconds. Skip getYear.",
            [
                ("JS Date Get (W3Schools)", "https://www.w3schools.com/js/js_date_methods.asp"),
                ("MDN: Date.prototype.getDate", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDate"),
                ("MDN: Date.now", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now"),
                ("MDN: Date.prototype.getTimezoneOffset", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset"),
            ],
        ),
        (
            "js-date-set",
            "JS Date Set",
            SETS,
            "Set methods change parts of a Date object in place and return the new millisecond timestamp. Start from January 01, 2025 as the page does. setFullYear can set year only or year+month+day. Months are 0–11. setDate can add days through overflow (January 1 + 50 = February 20). setHours can also set minutes and seconds. Dates compare with > and <. setMilliseconds and setTime have no Tryit on the page; they still each get an Example. setTime(0) is the epoch.",
            [
                "Set methods **mutate** the same Date. They use **local** fields (UTC setters live on the Methods reference page).",
                "**Months 0–11.** `setFullYear(2020, 11, 3)` is **3 December 2020**.",
                "`setDate(d.getDate() + n)` **adds days** and rolls the month/year automatically.",
                "`setHours(h, min, sec)` can set more than the hour.",
                "Compare Dates with **`>` / `<`**. January is month **0**.",
                "`setTime(0)` is **1970-01-01T00:00:00.000Z** (local print may be **31 Dec 1969**).",
            ],
            [
                ("What does `setFullYear(2020)` do to January 01, 2025?", ["The date becomes **January 1, 2020** local midnight."]),
                ("What is `setFullYear(2020, 11, 3)`?", ["**December 3, 2020.** Month **11** is December."]),
                ("What is `setMonth(11)` on January 1, 2025?", ["**December 1, 2025**."]),
                ("What is `setDate(15)` on that start date?", ["**January 15, 2025**."]),
                ("What is `setDate(d.getDate() + 50)` from January 1?", ["**February 20, 2025**. Overflow is automatic."]),
                ("What does `setHours(22, 10, 20)` set?", ["Hour **22**, minutes **10**, seconds **20** on the same local day."]),
                ("How do you compare dates?", ["With **`>` / `<`** (millisecond instants).", "In 2026, today is **before** January 14, 2100."]),
                ("What month number is January when setting?", ["**0.** December is **11**."]),
                ("Did setMilliseconds have a Tryit?", ["**No.** Still run: `setMilliseconds(500)` → `getMilliseconds()` **500**."]),
                ("What is `setTime(0)`?", ["The **epoch**. ISO **1970-01-01T00:00:00.000Z**.", "Local print here is **Wed Dec 31 1969 17:00:00 GMT-0700**."]),
                ("Do set methods return a new Date?", ["They mutate **the same object** and return the new **ms** timestamp (this sandbox prints the Date after the set)."]),
            ],
            "Mutate a Date with setFullYear, setMonth, setDate, and the time setters. Months start at zero. Adding days through setDate overflows cleanly. setTime(0) is the epoch. Compare two Dates as instants.",
            [
                ("JS Date Set (W3Schools)", "https://www.w3schools.com/js/js_date_methods_set.asp"),
                ("MDN: Date.prototype.setFullYear", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setFullYear"),
                ("MDN: Date.prototype.setTime", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setTime"),
            ],
        ),
        (
            "js-date-methods",
            "JS Date Methods",
            METHODS,
            "The Date reference table (revised April 2026) lists every constructor, getter, setter, formatter, and static. Each row is its own Example on a fixed instant 2021-03-25T15:30:45.123Z so snaps stay stable, except new Date() and Date.now() which must show the browser’s current clock. The table lists constructor twice: creating a Date, and reading the prototype constructor function. getYear, setYear, and toGMTString still run and must not be used. A tiny Date.prototype helper is confined to that one sandbox page.",
            [
                "**Every table row is an Example** — including the two different `constructor` descriptions.",
                "Fixed instant **`2021-03-25T15:30:45.123Z`** = local **Thu Mar 25 2021 09:30:45 GMT-0600**.",
                "**Deprecated still run:** `getYear()` → **121**, `setYear(99)` → **1999**, `toGMTString()` matches `toUTCString()`. Do not use them.",
                "**Statics:** `Date.now()`, `Date.parse()`, `Date.UTC()` — not instance methods.",
                "`valueOf()` equals `getTime()`. `toJSON()` equals `toISOString()`.",
                "`Date.prototype` add-ons belong in a demo file only — do not ship pollution.",
            ],
            [
                ("Why does `constructor` appear twice?", ["One row **creates** a Date (`new Date(...)`, `instanceof Date`).", "The other is the instance **`constructor`** property (**`Date`** / `[native code]`)."]),
                ("What is local `getHours()` on the fixed UTC instant?", ["**9** (Mountain UTC−6). `getUTCHours()` is **15**."]),
                ("What should you use instead of `getYear()`?", ["**`getFullYear()`**. `getYear()` returned **121** and is **deprecated**."]),
                ("What should you use instead of `setYear()`?", ["**`setFullYear()`**. `setYear(99)` became **1999** here (0–99 → 19xx)."]),
                ("What should you use instead of `toGMTString()`?", ["**`toUTCString()`**. Both printed **Thu, 25 Mar 2021 15:30:45 GMT**."]),
                ("Is `Date.now()` called on an instance?", ["**No.** Static **`Date.now()`**. The snap is the **browser's current** ms count."]),
                ("What does `Date.UTC(2021, 2, 25, 15, 30, 45, 123)` return?", ["**1616686245123** (a number, not a Date). Month **2** is March."]),
                ("What does the prototype demo add?", ["`toISODate()` → **`2021-03-25`** on that page only."]),
                ("`toJSON()` vs `toISOString()`?", ["**Same** ISO UTC string: **2021-03-25T15:30:45.123Z**."]),
                ("`valueOf()` vs `getTime()`?", ["**Same** number: **1616686245123**."]),
                ("What does `setUTCHours(0)` do to the fixed instant?", ["UTC becomes **00:30:45.123Z**. Local print is **Wed Mar 24 2021 18:30:45 GMT-0600**."]),
                ("What is `setTime(0)`?", ["The **epoch**. ISO **1970-01-01T00:00:00.000Z**; local **31 Dec 1969 17:00** here."]),
            ],
            "The reference is a catalog: construct, get local or UTC fields, set local or UTC fields, and format. Keep snaps on a fixed UTC instant except for now(). Treat getYear, setYear, and toGMTString as museum pieces that still execute. Statics live on Date; valueOf matches getTime.",
            [
                ("JS Date Methods (W3Schools)", "https://www.w3schools.com/js/js_date_reference.asp"),
                ("MDN: Date", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date"),
                ("MDN: Date.UTC", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/UTC"),
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
