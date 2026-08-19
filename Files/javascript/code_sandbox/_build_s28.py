"""S28: JS JSON (8 W3Schools pages)."""
from __future__ import annotations

import json

from _dom_ui import P, show_js
from _gen_lib import build_and_snap

BASE = "https://www.w3schools.com/js/"

CUSTOMER = """{
  "id": 101,
  "name": "John Doe",
  "city": "New York",
  "member": true
}
"""
PRODUCTS = """[
  {"name":"Laptop","price":899},
  {"name":"Mouse","price":29},
  {"name":"Keyboard","price":79}
]
"""
NEWS = """[
  {"title":"Hello"},
  {"title":"World"}
]
"""
RESULT = """{"message":"Person saved"}
"""
JSON_DEMO = CUSTOMER
JSON_ARR = '["Ford","Volvo","BMW"]\n'


def qa(*items):
    return list(items)


def run(slug, title, records, intro, concepts, qa_items, summary, page, extra_refs=None, port=8780):
    refs = [(title, BASE + page)]
    refs.extend(extra_refs or [("MDN JSON", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON")])
    build_and_snap(slug, title, records, intro, concepts, qa_items, summary, refs, use_http=True, port=port)


def parse_try(json_text: str) -> str:
    lit = json.dumps(json_text)
    return f"""      try {{
        const v = JSON.parse({lit});
        document.getElementById("demo").innerText = "ok " + JSON.stringify(v);
      }} catch (e) {{
        document.getElementById("demo").innerText = e.name + ": " + e.message;
      }}"""


# ---------------------------------------------------------------------------
# 28.1 JSON Intro
# ---------------------------------------------------------------------------

INTRO = [
    P("json-example", "A JSON example — name, age, city",
      ["JSON is a **text** format for data: curly braces, quoted names, values.",
       "This object has a string, a number, and a string.",
       "JSON is **not** a JavaScript program — it is data you parse."],
      """{
  "name": "John",
  "age": 30,
  "city": "New York"
}""",
      "`JSON.parse` of that text gives `name` **John** and `age` **30** (a number).",
      js="""      const text = '{ "name": "John", "age": 30, "city": "New York" }';
      const person = JSON.parse(text);
      document.getElementById("demo").innerText =
        person.name + " " + person.age + " " + person.city;"""),
    P("js-object", "Same data as a JavaScript object",
      ["In JavaScript, property names **may** be unquoted (`name: \"John\"`).",
       "JSON **requires** double-quoted names.",
       "The values can look similar; the rules are stricter in JSON."],
      """const person = {
  name: "John",
  age: 30,
  city: "New York"
};""",
      "The JS object prints **John 30 New York** without `JSON.parse`.",
      js="""      const person = { name: "John", age: 30, city: "New York" };
      document.getElementById("demo").innerText =
        person.name + " " + person.age + " " + person.city;"""),
    P("json-is-text", "JSON is text",
      ["A JSON document is a **string** until you parse it.",
       "`typeof` of the raw payload is **`string`**.",
       "After `JSON.parse`, `typeof person` is **`object`**."],
      """{
  "name": "John",
  "age": 30,
  "city": "New York"
}""",
      "Before parse: **string**. After parse: **object** with `name` John.",
      js="""      const text = '{"name":"John","age":30,"city":"New York"}';
      const person = JSON.parse(text);
      document.getElementById("demo").innerText =
        "typeof text=" + typeof text + "\\ntypeof person=" + typeof person;"""),
    P("parse", "JSON.parse — JSON text to JavaScript",
      ["`JSON.parse(text)` turns JSON **text** into a JS value.",
       "Invalid JSON **throws** `SyntaxError`.",
       "This is how APIs become objects you can use."],
      """const text = '{"name":"John", "age":30, "city":"New York"}';
const person = JSON.parse(text);""",
      "`person.name` is **John** after parse.",
      js="""      const text = '{"name":"John", "age":30, "city":"New York"}';
      const person = JSON.parse(text);
      document.getElementById("demo").innerText = person.name;"""),
    P("stringify", "JSON.stringify — JavaScript to JSON text",
      ["`JSON.stringify(value)` does the reverse: JS value → **string**.",
       "The W3Schools demo writes that string into the page.",
       "Names become quoted; `undefined`/functions are dropped (later page)."],
      """const person = { name: "John", age: 30, city: "New York" };
const text = JSON.stringify(person);
document.getElementById("demo").innerHTML = text;""",
      "The page shows JSON text like **`{\"name\":\"John\",\"age\":30,\"city\":\"New York\"}`**.",
      js="""      const person = { name: "John", age: 30, city: "New York" };
      const text = JSON.stringify(person);
      document.getElementById("demo").innerText = text;"""),
    P("round-trip", "JSON round trip — stringify then parse",
      ["stringify → parse returns a **new** object with the same enumerable JSON data.",
       "It is not `===` the original object.",
       "Dates become strings unless you use a reviver (Parse page)."],
      """const person = { name: "John", age: 30 };
const text = JSON.stringify(person);
const copy = JSON.parse(text);""",
      "`copy.name` is **John**, and `copy === person` is **false**.",
      js="""      const person = { name: "John", age: 30 };
      const copy = JSON.parse(JSON.stringify(person));
      document.getElementById("demo").innerText =
        "name=" + copy.name + " sameRef=" + (copy === person);"""),
    P("customer-file", "JSON files — customer.json",
      ["JSON often lives in a **`.json` file** on a server.",
       "The sample has id, name, city, and boolean **member**.",
       "Load it later with `fetch` + `response.json()`."],
      CUSTOMER.strip(),
      "Parsed `customer.json` has **id 101**, name **John Doe**, **member true**.",
      extra_files={"customer.json": CUSTOMER},
      wait_ms=2500,
      js="""      (async function () {
        const c = await (await fetch("customer.json")).json();
        document.getElementById("demo").innerText =
          c.id + " " + c.name + " member=" + c.member;
      })();"""),
    P("json-object", "JSON objects — firstName / lastName",
      ["A JSON **object** is `{ \"key\": value, ... }`.",
       "Keys are strings in double quotes.",
       "This tiny object is one employee."],
      """{"firstName":"John", "lastName":"Doe"}""",
      "Parse gives **John Doe**.",
      js="""      const o = JSON.parse('{"firstName":"John","lastName":"Doe"}');
      document.getElementById("demo").innerText = o.firstName + " " + o.lastName;"""),
    P("json-array", "JSON arrays — employees",
      ["A JSON **array** is `[ value, value, ... ]`.",
       "Here the value of `employees` is an array of objects.",
       "Index **1** is Anna Smith in the W3Schools sample."],
      """"employees":[
  {"firstName":"John", "lastName":"Doe"},
  {"firstName":"Anna", "lastName":"Smith"},
  {"firstName":"Peter", "lastName":"Jones"}
]""",
      "`employees[1]` is **Anna Smith**.",
      js="""      const text = '{ "employees" : [' +
        '{ "firstName":"John" , "lastName":"Doe" },' +
        '{ "firstName":"Anna" , "lastName":"Smith" },' +
        '{ "firstName":"Peter" , "lastName":"Jones" } ]}';
      const obj = JSON.parse(text);
      document.getElementById("demo").innerText =
        obj.employees[1].firstName + " " + obj.employees[1].lastName;"""),
    P("employees-text", "JSON text built from concatenated strings",
      ["Tutorials often build JSON with **string concatenation**.",
       "That is easy to typo. Prefer a real `.json` file or `JSON.stringify`.",
       "After concat, you still must **`JSON.parse`**."],
      """let text = '{ "employees" : [' +
'{ "firstName":"John" , "lastName":"Doe" },' +
'{ "firstName":"Anna" , "lastName":"Smith" },' +
'{ "firstName":"Peter" , "lastName":"Jones" } ]}';""",
      "`text` is a **string**; `JSON.parse(text)` succeeds and has **3** employees.",
      js="""      let text = '{ "employees" : [' +
        '{ "firstName":"John" , "lastName":"Doe" },' +
        '{ "firstName":"Anna" , "lastName":"Smith" },' +
        '{ "firstName":"Peter" , "lastName":"Jones" } ]}';
      const obj = JSON.parse(text);
      document.getElementById("demo").innerText =
        "typeof text=" + typeof text + " count=" + obj.employees.length;"""),
    P("display-anna", "Display parsed employees[1] in HTML",
      ["After parse, use **property access** like any JS object.",
       "W3Schools writes `obj.employees[1].firstName` into `#demo`.",
       "Index 1 is the **second** person (zero-based)."],
      """document.getElementById("demo").innerHTML =
  obj.employees[1].firstName + " " + obj.employees[1].lastName;""",
      "The paragraph shows **Anna Smith**.",
      js="""      const obj = JSON.parse('{ "employees" : [' +
        '{ "firstName":"John" , "lastName":"Doe" },' +
        '{ "firstName":"Anna" , "lastName":"Smith" },' +
        '{ "firstName":"Peter" , "lastName":"Jones" } ]}');
      document.getElementById("demo").innerText =
        obj.employees[1].firstName + " " + obj.employees[1].lastName;"""),
]

INTRO_QA = qa(
    ("Is JSON a programming language?", ["**No** — it is a **text data** format."]),
    ("Must JSON property names be quoted?", ["**Yes** — double quotes."]),
    ("What does `JSON.parse` return?", ["A JavaScript **value** (object, array, string, number, boolean, or null)."]),
    ("What does `JSON.stringify` return?", ["A **string** of JSON text."]),
    ("Who is `employees[1]` in the sample?", ["**Anna Smith**."]),
    ("What is `typeof` of raw JSON text?", ["**string**."]),
    ("Does stringify+parse keep the same object reference?", ["**No** — you get a **new** object."]),
    ("What file extension is common?", ["**`.json`**."]),
    ("Is JSON language-independent?", ["**Yes** — many languages parse it."]),
    ("Can you use unquoted names in JSON?", ["**No** — that is only valid in **JavaScript** objects."]),
)

# ---------------------------------------------------------------------------
# 28.2 JSON Syntax
# ---------------------------------------------------------------------------

SYN = [
    P("object-literal", "JSON object literal as text",
      ["A JSON object is `{ \"name\": value, ... }` inside a **string** if you parse it in JS.",
       "Values may be string, number, boolean, null, object, or array.",
       "`car` here is **null**."],
      """{"name":"John", "age":30, "car":null}""",
      "Parse: **John**, age **30**, car **null**.",
      js="""      const o = JSON.parse('{"name":"John","age":30,"car":null}');
      document.getElementById("demo").innerText =
        o.name + " age=" + o.age + " car=" + o.car;"""),
    P("array-literal", "JSON array literal",
      ["Arrays use square brackets: `[\"Ford\", \"BMW\", \"Fiat\"]`.",
       "In JS you often keep that as a string then parse."],
      """["Ford", "BMW", "Fiat"]""",
      "Parsed array length is **3**; index 0 is **Ford**.",
      js="""      const a = JSON.parse('["Ford","BMW","Fiat"]');
      document.getElementById("demo").innerText = a.length + " " + a[0];"""),
    P("array-strings", "JSON array of strings (pretty)",
      ["Whitespace between tokens is **allowed** and ignored.",
       "Pretty-printed JSON is still the same data."],
      """[
  "Apple",
  "Banana",
  "Orange"
]""",
      "Three fruits; index 1 is **Banana**.",
      js="""      const a = JSON.parse('["Apple","Banana","Orange"]');
      document.getElementById("demo").innerText = a[1];"""),
    P("array-numbers", "JSON array of numbers",
      ["Numbers are **not** quoted.",
       "`[1, 2, 3, 4, 5]` parses to actual numbers."],
      """[1, 2, 3, 4, 5]""",
      "`typeof a[0]` is **number** and the sum is **15**.",
      js="""      const a = JSON.parse('[1, 2, 3, 4, 5]');
      document.getElementById("demo").innerText =
        "typeof0=" + typeof a[0] + " sum=" + a.reduce(function (s, n) { return s + n; }, 0);"""),
    P("quoted-names-valid", "Property names must be double-quoted (valid)",
      ["Valid: `{ \"name\": \"John\" }`.",
       "This is the JSON rule that bites JS developers first."],
      """{ "name": "John" }""",
      "Parse succeeds; `name` is **John**.",
      js=parse_try('{ "name": "John" }')),
    P("unquoted-names-invalid", "Unquoted property names are invalid JSON",
      ["Invalid: `{ name: \"John\" }` — legal JS, **illegal JSON**.",
       "`JSON.parse` throws **SyntaxError**."],
      """{ name: "John" }""",
      "Parse throws **SyntaxError**.",
      js=parse_try('{ name: "John" }')),
    P("double-quoted-string", "JSON strings use double quotes (valid)",
      ["Valid: `{ \"city\": \"London\" }`.",
       "Only **double** quotes wrap strings."],
      """{ "city": "London" }""",
      "Parse succeeds; city is **London**.",
      js=parse_try('{ "city": "London" }')),
    P("single-quoted-string", "Single-quoted strings are invalid JSON",
      ["Invalid: `{ \"city\": 'London' }`.",
       "JSON has no single-quoted strings."],
      """{ "city": 'London' }""",
      "Parse throws **SyntaxError**.",
      js=parse_try("{ \"city\": 'London' }")),
    P("whitespace-compact", "Whitespace is optional — compact form",
      ["`{\"name\":\"John\", \"age\":30}` is valid.",
       "Spaces after colons/commas are optional."],
      """{"name":"John", "age":30}""",
      "Parse works; age is **30**.",
      js="""      const o = JSON.parse('{"name":"John", "age":30}');
      document.getElementById("demo").innerText = o.name + " " + o.age;"""),
    P("whitespace-pretty", "Equivalent pretty JSON",
      ["The same object with newlines is **equivalent**.",
       "Pretty print is for humans; parsers ignore the extra space."],
      """{
  "name": "John",
  "age": 30
}""",
      "Pretty and compact parse to **equal** data (`age` 30).",
      js="""      const a = JSON.parse('{"name":"John","age":30}');
      const b = JSON.parse('{ "name": "John", "age": 30 }');
      document.getElementById("demo").innerText =
        "equal=" + (a.name === b.name && a.age === b.age);"""),
    P("trailing-comma-wrong", "Trailing commas are invalid",
      ["Wrong: `{ \"name\": \"John\", \"age\": 30, }` — comma after the last property.",
       "JS objects allow trailing commas; **JSON does not**."],
      """{
  "name": "John",
  "age": 30,
}""",
      "Parse throws **SyntaxError** because of the trailing comma.",
      js=parse_try('{\n  "name": "John",\n  "age": 30,\n}')),
    P("trailing-comma-correct", "No trailing comma (correct)",
      ["Remove the last comma: `{ \"name\": \"John\", \"age\": 30 }`."],
      """{
  "name": "John",
  "age": 30
}""",
      "Parse succeeds.",
      js=parse_try('{\n  "name": "John",\n  "age": 30\n}')),
    P("comments-wrong", "Comments are not allowed",
      ["Wrong: `// Customer name` inside JSON.",
       "JSON has **no comments**. Put comments in docs, not in the payload."],
      """{
  // Customer name
  "name": "John"
}""",
      "Parse throws **SyntaxError** on the comment.",
      js=parse_try('{\n  // Customer name\n  "name": "John"\n}')),
    P("type-string", "JSON value type — String",
      ["Allowed types include **String**: `\"John\"`.",
       "Must use double quotes."],
      """"John\"""",
      '`JSON.parse(\'"John"\')` is the string **John**.',
      js="""      document.getElementById("demo").innerText = JSON.parse('"John"');"""),
    P("type-number", "JSON value type — Number",
      ["**Number**: `42` with no quotes.",
       "Quoted `\"42\"` would be a string."],
      """42""",
      "`JSON.parse('42')` is number **42**.",
      js="""      const v = JSON.parse("42");
      document.getElementById("demo").innerText = typeof v + " " + v;"""),
    P("type-boolean", "JSON value type — Boolean",
      ["**Boolean**: `true` or `false` (lowercase)."],
      """true""",
      "`JSON.parse('true')` is boolean **true**.",
      js="""      const v = JSON.parse("true");
      document.getElementById("demo").innerText = typeof v + " " + v;"""),
    P("type-null", "JSON value type — Null",
      ["**Null**: the literal `null` (empty value)."],
      """null""",
      "`JSON.parse('null')` is **null**.",
      js="""      document.getElementById("demo").innerText = String(JSON.parse("null"));"""),
    P("vs-js-unquoted", "JSON vs JS — unquoted names",
      ["JSON: **No**. JS: **Yes**."],
      """JSON: { "name": "John" }
JS:   { name: "John" }""",
      "JSON parse of unquoted names **fails**; a JS object literal works.",
      js="""      let jsonOk = "fail";
      try { JSON.parse('{name:"John"}'); } catch (e) { jsonOk = e.name; }
      const jsOk = ({name: "John"}).name;
      document.getElementById("demo").innerText = "JSON " + jsonOk + " / JS object " + jsOk;"""),
    P("vs-js-single-quotes", "JSON vs JS — single-quoted strings",
      ["JSON: **No**. JS: **Yes**."],
      """JSON cannot use 'London'""",
      "JSON parse of single quotes **fails**.",
      js=parse_try("{\"city\": 'London'}")),
    P("vs-js-trailing", "JSON vs JS — trailing commas",
      ["JSON: **No**. JS: **Yes** (in modern engines)."],
      """JSON forbids a comma after the last item""",
      "Covered by the trailing-comma examples: JSON **SyntaxError**, JS objects allow it.",
      js="""      const js = { name: "John", age: 30, };
      document.getElementById("demo").innerText = "JS trailing comma ok name=" + js.name;"""),
    P("vs-js-comments", "JSON vs JS — comments",
      ["JSON: **No**. JS: **Yes** (`//` and `/* */`)."],
      """// not legal in JSON""",
      "JSON with a comment **throws**; JavaScript comments are fine in `.js` files.",
      js="""      document.getElementById("demo").innerText = "JSON: no comments. JS: comments allowed.";"""),
]

SYN_QA = qa(
    ("Must property names be quoted in JSON?", ["**Yes** — double quotes."]),
    ("Can JSON use single-quoted strings?", ["**No**."]),
    ("Are trailing commas allowed?", ["**No** — that is a SyntaxError."]),
    ("Can JSON contain `//` comments?", ["**No**."]),
    ("Is whitespace significant?", ["**No** — extra spaces/newlines between tokens are ignored."]),
    ("Name the six JSON value types.", ["**String, Number, Boolean, Null, Object, Array**."]),
    ("What does `JSON.parse('{ name: \"John\" }')` do?", ["**Throws SyntaxError** (unquoted name)."]),
    ("Is `{ name: \"John\" }` valid JavaScript?", ["**Yes** — JS object literals allow unquoted names."]),
    ("What is `car` in the first example?", ["**null**."]),
    ("Does pretty-printed JSON change the data?", ["**No** — it is equivalent."]),
)

# ---------------------------------------------------------------------------
# 28.3 JSON Values
# ---------------------------------------------------------------------------

VAL = [
    P("object", "JSON object values",
      ["Objects are `{ \"key\": value }`.",
       "This one holds name, age, city."],
      """{
  "name": "John",
  "age": 30,
  "city": "New York"
}""",
      "Parsed **city** is **New York**.",
      js="""      const o = JSON.parse('{"name":"John","age":30,"city":"New York"}');
      document.getElementById("demo").innerText = o.city;"""),
    P("nested-employee", "Object as a property value",
      ["Values can be nested objects: `{ \"employee\": { ... } }`."],
      """{ "employee":{"name":"John", "age":30, "city":"New York"} }""",
      "`employee.name` is **John**.",
      js="""      const o = JSON.parse('{ "employee":{"name":"John", "age":30, "city":"New York"} }');
      document.getElementById("demo").innerText = o.employee.name;"""),
    P("array-property", "Array as a property value",
      ["`employees` can be an array of strings."],
      """{ "employees":["John", "Anna", "Peter"] }""",
      "`employees[1]` is **Anna**.",
      js="""      const o = JSON.parse('{ "employees":["John", "Anna", "Peter"] }');
      document.getElementById("demo").innerText = o.employees[1];"""),
    P("array", "JSON array values",
      ["A document may be an array at the **root**: `[\"Ford\", ...]`."],
      """["Ford", "Volvo", "BMW"]""",
      "Index 0 is **Ford**.",
      js="""      document.getElementById("demo").innerText = JSON.parse('["Ford","Volvo","BMW"]')[0];"""),
    P("nested", "Nested object + array",
      ["`address` is an object; `hobbies` is an array.",
       "Path: `person.address.city` and `person.hobbies[1]`."],
      """{
  "name": "John",
  "age": 30,
  "address": { "city": "New York", "country": "USA" },
  "hobbies": ["Reading", "Cycling", "Photography"]
}""",
      "City **New York**; hobby **Cycling**.",
      js="""      const p = JSON.parse('{"name":"John","age":30,"address":{"city":"New York","country":"USA"},"hobbies":["Reading","Cycling","Photography"]}');
      document.getElementById("demo").innerText =
        p.address.city + " / " + p.hobbies[1];"""),
    P("strings", "JSON string values",
      ["Strings: `\"\"`, `\"Hello World!\"`, escaped quotes, Unicode `\\u00A9`.",
       "Always double-quoted."],
      """""
"Hello World!"
"He said, \\"Hello!\\""
"\\u00A9 2026" """,
      "Empty string length **0**; copyright escape becomes **© 2026**.",
      js="""      document.getElementById("demo").innerText = [
        JSON.parse('""').length,
        JSON.parse('"Hello World!"'),
        JSON.parse('"He said, \\\\"Hello!\\\\""'),
        JSON.parse('"\\\\u00A9 2026"')
      ].join("\\n");"""),
    P("numbers", "JSON number values — integer, fraction, exponent",
      ["Integers: `-7`, `42`. Fractions: `-0.5`, `3.14`. Exponents: `2.997e8`.",
       "No leading zeros (`05`), no `+42`, no `NaN`/`Infinity`."],
      """{ "age": 30, "height": 1.82, "speed_of_light": 2.997e8 }""",
      "age **30**, height **1.82**, speed **299700000**.",
      js="""      const o = JSON.parse('{"age":30,"height":1.82,"speed_of_light":2.997e8}');
      document.getElementById("demo").innerText =
        o.age + " " + o.height + " " + o.speed_of_light;"""),
    P("num-no-quotes", "Number error — quoted 42 is a string",
      ['`"42"` is a **string**, not a number.'],
      """"42" """,
      '`typeof JSON.parse(\'"42"\')` is **string**.',
      js="""      const v = JSON.parse('"42"');
      document.getElementById("demo").innerText = typeof v + " " + v;"""),
    P("num-leading-zero", "Number error — leading zeros",
      ["`05` is invalid JSON."],
      """05""",
      "Parse of `05` throws **SyntaxError**.",
      js=parse_try("05")),
    P("num-plus", "Number error — leading plus",
      ["`+42` is invalid JSON."],
      """+42""",
      "Parse of `+42` throws **SyntaxError**.",
      js=parse_try("+42")),
    P("num-nan", "Number error — NaN / Infinity",
      ["`NaN` and `Infinity` are **not** JSON numbers."],
      """NaN""",
      "Parse of `NaN` throws **SyntaxError**.",
      js=parse_try("NaN")),
    P("num-hex", "Number error — hex / octal",
      ["`0x7A` is invalid JSON."],
      """0x7A""",
      "Parse of `0x7A` throws **SyntaxError**.",
      js=parse_try("0x7A")),
    P("booleans", "JSON boolean values",
      ["Only lowercase **`true`** and **`false`**.",
       "`\"true\"` would be a string. `True` is invalid."],
      """{ "member": true, "student": false }""",
      "member **true**, student **false**, both booleans.",
      js="""      const o = JSON.parse('{"member":true,"student":false}');
      document.getElementById("demo").innerText =
        o.member + " " + o.student + " " + typeof o.member;"""),
    P("bool-quoted", "Boolean rule — quotes make a string",
      ["`\"true\"` is a string."],
      """"true" """,
      "typeof is **string**.",
      js="""      document.getElementById("demo").innerText = typeof JSON.parse('"true"');"""),
    P("bool-case", "Boolean rule — True / FALSE are invalid",
      ["JSON booleans are **lowercase only**."],
      """True""",
      "Parse of `True` throws **SyntaxError**.",
      js=parse_try("True")),
    P("bool-numbers", "Boolean rule — 1 and 0 are numbers, not booleans",
      ["JSON does not treat `1`/`0` as booleans."],
      """1""",
      "`JSON.parse('1')` is **number** 1, not `true`.",
      js="""      const v = JSON.parse("1");
      document.getElementById("demo").innerText = typeof v + " " + v;"""),
    P("null-value", "JSON null",
      ["`null` is an empty value.",
       "Example: `middleName: null`."],
      """{ "middleName": null }""",
      "`middleName` is **null**.",
      js="""      const o = JSON.parse('{"middleName":null}');
      document.getElementById("demo").innerText = String(o.middleName);"""),
    P("undefined-wrong", "undefined is not a JSON value (wrong)",
      ["`{ \"city\": undefined }` is **invalid JSON** (and even as JS, stringify would drop it)."],
      """{ "city": undefined }""",
      "Parse throws **SyntaxError**.",
      js=parse_try('{ "city": undefined }')),
    P("undefined-correct", "Use null instead of undefined",
      ["Correct: `{ \"city\": null }`."],
      """{ "city": null }""",
      "Parse succeeds; city is **null**.",
      js="""      document.getElementById("demo").innerText =
        String(JSON.parse('{ "city": null }').city);"""),
    P("date-string", "Dates are not a JSON type — store strings",
      ["JSON has **no Date**. Store ISO strings, revive later.",
       'Example: `"birth":"1986-12-14"`.'],
      """const text = '{"name":"John", "birth":"1986-12-14"}';""",
      "`birth` is a **string**, not a Date, until you convert it.",
      js="""      const o = JSON.parse('{"name":"John", "birth":"1986-12-14"}');
      document.getElementById("demo").innerText = typeof o.birth + " " + o.birth;"""),
    P("function-wrong", "Functions are not JSON values",
      ["`{ \"greet\": function() {return \"Hello\"} }` is invalid JSON."],
      """{ "greet": function() {return "Hello"} }""",
      "Parse throws **SyntaxError**.",
      js=parse_try('{ "greet": function() {return "Hello"} }')),
    P("unsupported-symbol", "Unsupported JS value — Symbol",
      ["**Symbol** is not a JSON type. `JSON.stringify({s: Symbol('x')})` omits it."],
      """JSON.stringify({ s: Symbol("x") })""",
      "The object stringifies to **`{}`** (symbol omitted).",
      js="""      document.getElementById("demo").innerText = JSON.stringify({ s: Symbol("x") });"""),
    P("unsupported-bigint", "Unsupported JS value — BigInt throws",
      ["`JSON.stringify(1n)` throws **TypeError**."],
      """JSON.stringify(1n)""",
      "The call throws **TypeError** (BigInt cannot be serialized).",
      js="""      try { JSON.stringify(1n); }
      catch (e) { document.getElementById("demo").innerText = e.name + ": " + e.message; }"""),
    P("unsupported-infinity", "Unsupported JS value — Infinity → null in objects",
      ["`Infinity` is not JSON. stringify turns it into **null** in objects/arrays."],
      """JSON.stringify({ n: Infinity })""",
      "Result is **`{\"n\":null}`**.",
      js="""      document.getElementById("demo").innerText = JSON.stringify({ n: Infinity });"""),
]

VAL_QA = qa(
    ("What types can JSON hold?", ["String, Number, Boolean, Null, Object, Array."]),
    ("How do you nest data?", ["Objects and arrays as **values** of other objects/arrays."]),
    ("Is `undefined` valid JSON?", ["**No** — use **null**."]),
    ("Is `NaN` valid JSON?", ["**No**."]),
    ("How should you store a date?", ["As an **ISO string**, then convert after parse."]),
    ("What happens if you put a function in JSON text?", ["**SyntaxError** on parse."]),
    ("What does stringify do with BigInt?", ["**Throws TypeError**."]),
    ("What does stringify do with Infinity?", ["Converts to **null** in objects/arrays."]),
    ("Is `True` a JSON boolean?", ["**No** — only lowercase **true** / **false**."]),
    ("Is `05` a JSON number?", ["**No** — no leading zeros."]),
    ("Quoted `\"42\"` is what type?", ["A **string**."]),
)

# ---------------------------------------------------------------------------
# 28.4 JSON Parse
# ---------------------------------------------------------------------------

PAR = [
    P("syntax", "JSON.parse(text, reviver) syntax",
      ["First argument: the **JSON text** (a string).",
       "Second: optional **reviver(key, value)** that can transform values.",
       "Throws **SyntaxError** if the text is not JSON."],
      """JSON.parse(text, reviver)""",
      "`JSON.parse` is a function of **2** parameters (`length` 2).",
      js=show_js("JSON.parse.length")),
    P("parse-object", "Parsing a JSON object",
      ["Parse an object and read `person.name`."],
      """const text = '{"name":"John","age":30,"city":"New York"}';
const person = JSON.parse(text);
let name = person.name;""",
      "**name** is **John**.",
      js="""      const person = JSON.parse('{"name":"John","age":30,"city":"New York"}');
      document.getElementById("demo").innerText = person.name;"""),
    P("parse-array", "Parsing a JSON array",
      ["A root array parses to a JS **Array**.",
       "`cars[0]` is **Ford**."],
      """const text = '["Ford","Volvo","BMW"]';
const cars = JSON.parse(text);
let name = cars[0];""",
      "**Ford** is at index 0.",
      js="""      document.getElementById("demo").innerText = JSON.parse('["Ford","Volvo","BMW"]')[0];"""),
    P("parse-string", "Parsing a JSON string value",
      ["`JSON.parse('\"John\"')` is the string John."],
      """value = JSON.parse('"John"');""",
      "Result is string **John**.",
      js="""      document.getElementById("demo").innerText = typeof JSON.parse('"John"') + " " + JSON.parse('"John"');"""),
    P("parse-number", "Parsing a JSON number value",
      ["`JSON.parse('42')` is number 42."],
      """value = JSON.parse('42');""",
      "typeof **number**, value **42**.",
      js="""      const v = JSON.parse("42");
      document.getElementById("demo").innerText = typeof v + " " + v;"""),
    P("parse-true", "Parsing JSON true",
      ["`JSON.parse('true')` is boolean true."],
      """value = JSON.parse('true');""",
      "typeof **boolean**, value **true**.",
      js="""      const v = JSON.parse("true");
      document.getElementById("demo").innerText = typeof v + " " + v;"""),
    P("parse-null", "Parsing JSON null",
      ["`JSON.parse('null')` is **null** (and `typeof` is the quirky `'object'`)."],
      """value = JSON.parse('null');""",
      "Value is **null**.",
      js="""      document.getElementById("demo").innerText = String(JSON.parse("null"));"""),
    P("display-name", "Common use — parse then show in HTML",
      ["Typical pattern: parse, then `textContent` / `innerHTML` a property."],
      """document.getElementById("demo").innerHTML = person.name;""",
      "The page shows **John**.",
      js="""      const person = JSON.parse('{"name":"John", "age":30, "city":"New York"}');
      document.getElementById("demo").innerText = person.name;"""),
    P("reviver-age", "Reviver — convert age to a number",
      ["If JSON stored age as `\"30\"` (string), a reviver can `return Number(value)` when `key == \"age\"`.",
       "Other keys return `value` unchanged.",
       "The reviver walks **from the inside out**."],
      """const person = JSON.parse(text, function(key, value) {
  if (key == "age") { return Number(value); }
  return value;
});
typeof person.age; // number""",
      "`typeof person.age` is **number** (30).",
      js="""      const person = JSON.parse('{"name":"John","age":"30"}', function (key, value) {
        if (key == "age") { return Number(value); }
        return value;
      });
      document.getElementById("demo").innerText = typeof person.age + " " + person.age;"""),
    P("reviver-date", "Reviver — convert a date string to Date",
      ["When `key === \"date\"`, `return new Date(value)`.",
       "`typeof myObject.date` is **object** (Date)."],
      """const myObject = JSON.parse(text, (key, value) => {
  if (key === "date") { return new Date(value); }
  return value;
});
typeof myObject.date; // object""",
      "`date` is a **Date** object; `getUTCFullYear()` is **2026**.",
      js="""      const myObject = JSON.parse(
        '{"event":"Conference","date":"2026-07-22T11:28:00.000Z"}',
        function (key, value) {
          if (key === "date") { return new Date(value); }
          return value;
        }
      );
      document.getElementById("demo").innerText =
        typeof myObject.date + " year=" + myObject.date.getUTCFullYear();"""),
    P("invalid-parse", "Invalid JSON throws",
      ["`{name:'John'}` is not JSON.",
       "Bare `JSON.parse` throws — always **try/catch** untrusted text."],
      """const text = "{name:'John'}";
JSON.parse(text);""",
      "Uncaught this would abort; the sandbox catches **SyntaxError**.",
      js=parse_try("{name:'John'}")),
    P("valid-form", "Valid JSON object text",
      ["Valid: `{\"name\":\"John\"}`."],
      """{"name":"John"}""",
      "Parse succeeds.",
      js="""      document.getElementById("demo").innerText = JSON.parse('{"name":"John"}').name;"""),
    P("invalid-variants", "Invalid variants — single quotes, unquoted name, unquoted value",
      ["Invalid: `{'name':\"John\"}`, `{\"name\":'John'}`, `{name:\"John\"}`, `{\"name\":John}`."],
      """{'name':"John"}
{"name":'John'}
{name:"John"}
{"name":John}""",
      "Each variant throws **SyntaxError** (four errors counted).",
      js="""      const tests = ["{'name':\\"John\\"}", "{\\"name\\":'John'}", "{name:\\"John\\"}", "{\\"name\\":John}"];
      const errs = tests.map(function (t) {
        try { JSON.parse(t); return "ok"; }
        catch (e) { return e.name; }
      });
      document.getElementById("demo").innerText = errs.join("\\n");"""),
    P("try-catch", "Handling parse errors with try/catch",
      ["Wrap `JSON.parse` in **try/catch** and display `err`."],
      """try {
  const person = JSON.parse(text);
} catch(err) {
  myDisplayer(err);
}""",
      "The catch block receives a **SyntaxError** for `{name:'John'}`.",
      js="""      try {
        JSON.parse("{name:'John'}");
      } catch (err) {
        document.getElementById("demo").innerText = err.name + ": " + err.message;
      }"""),
    P("parse-object-wrong", "Mistake — parsing a JavaScript object",
      ["`JSON.parse(person)` when `person` is already an object **coerces** it to `\"[object Object]\"`, which is not JSON.",
       "That throws **SyntaxError**."],
      """const person = {name: "John"};
const result = JSON.parse(person);""",
      "The call throws **SyntaxError** (`[object Object]` is not JSON).",
      js="""      try {
        JSON.parse({name: "John"});
      } catch (e) {
        document.getElementById("demo").innerText = e.name + ": " + e.message;
      }"""),
    P("parse-twice-wrong", "Mistake — parsing JSON twice",
      ["After one parse you have an **object**. Parsing that object again fails the same way.",
       "Or if you parse a string that is already a JS string value, a second parse of that string value may throw or return something else.",
       "W3Schools: `JSON.parse(person)` after `person` is already parsed."],
      """const person = JSON.parse('{"name":"John"}');
const result = JSON.parse(person);""",
      "The second parse throws **SyntaxError**.",
      js="""      const person = JSON.parse('{"name":"John"}');
      try {
        JSON.parse(person);
        document.getElementById("demo").innerText = "unexpected ok";
      } catch (e) {
        document.getElementById("demo").innerText = e.name;
      }"""),
]

PAR_QA = qa(
    ("What are the two `JSON.parse` parameters?", ["**text** and optional **reviver**."]),
    ("What is `cars[0]` after parsing the cars array?", ["**Ford**."]),
    ("What does a reviver receive?", ["**key** and **value** for each nested value."]),
    ("How do you turn a date string into a Date?", ["In the reviver, `if (key === \"date\") return new Date(value)`."]),
    ("What exception does bad JSON throw?", ["**SyntaxError**."]),
    ("Should you parse a JS object?", ["**No** — parse **text** only."]),
    ("What happens if you parse twice?", ["The second call gets an **object** and **throws**."]),
    ("What is `JSON.parse('null')`?", ["**null**."]),
    ("What is `JSON.parse('42')`?", ["The number **42**."]),
    ("Why try/catch?", ["Untrusted or hand-written JSON may be **invalid**."]),
)

# ---------------------------------------------------------------------------
# 28.5 JSON Stringify
# ---------------------------------------------------------------------------

ST = [
    P("syntax", "JSON.stringify(value, replacer, space)",
      ["**value** — what to convert.",
       "**replacer** — a function or an array of keys to keep.",
       "**space** — number or string for indentation."],
      """JSON.stringify(value, replacer, space)""",
      "`JSON.stringify.length` is **3**.",
      js=show_js("JSON.stringify.length")),
    P("object", "Converting an object",
      ["Stringify `{name, age, city}` to JSON text."],
      """const person = { name: "John", age: 30, city: "New York" };
const text = JSON.stringify(person);""",
      "Text contains **`\"name\":\"John\"`** and **`\"age\":30`**.",
      js="""      const text = JSON.stringify({ name: "John", age: 30, city: "New York" });
      document.getElementById("demo").innerText = text;"""),
    P("array", "Converting an array",
      ["Arrays stringify to JSON arrays."],
      """const cars = ["Ford", "Volvo", "BMW"];
const text = JSON.stringify(cars);""",
      "Result is **`[\"Ford\",\"Volvo\",\"BMW\"]`**.",
      js="""      document.getElementById("demo").innerText = JSON.stringify(["Ford", "Volvo", "BMW"]);"""),
    P("other-values", "Converting other values",
      ["The page stringifies a string, numbers, booleans, Boolean objects, undefined, null, NaN, Infinity.",
       "`undefined` as a **root** value becomes `undefined` (the JS value), not a JSON text — `JSON.stringify(undefined)` returns **undefined**, so `String(...)` shows that.",
       "`null`, `NaN`, `Infinity` become **`null`** as JSON text."],
      """JSON.stringify("John");
JSON.stringify(42);
JSON.stringify(false);
JSON.stringify(Boolean(0));
JSON.stringify(true);
JSON.stringify(Boolean(1));
JSON.stringify(undefined);
JSON.stringify(null);
JSON.stringify(NaN);
JSON.stringify(Infinity);""",
      "Each call’s JSON text (or `undefined`) is listed. Null/NaN/Infinity are **`null`**.",
      js="""      const lines = [
        JSON.stringify("John"),
        JSON.stringify(42),
        JSON.stringify(false),
        JSON.stringify(Boolean(0)),
        JSON.stringify(true),
        JSON.stringify(Boolean(1)),
        String(JSON.stringify(undefined)),
        JSON.stringify(null),
        JSON.stringify(NaN),
        JSON.stringify(Infinity)
      ];
      document.getElementById("demo").innerText = lines.join("\\n");"""),
    P("select-keys", "Selecting properties with a replacer array",
      ["`JSON.stringify(person, [\"name\", \"city\"])` keeps **only** those keys.",
       "`age` is omitted."],
      """let text = JSON.stringify(person, ["name", "city"]);""",
      "JSON has **name** and **city**, not **age**.",
      js="""      const text = JSON.stringify({ name: "John", age: 30, city: "New York" }, ["name", "city"]);
      document.getElementById("demo").innerText = text;"""),
    P("replacer-fn", "Transforming values with a replacer function",
      ["If `key == \"age\"`, return `value + 1`.",
       "Other keys return `value`."],
      """JSON.stringify(person, function(key, value) {
  if (key == "age") { return value + 1; }
  return value;
});""",
      "Age in the JSON text is **31**.",
      js="""      const text = JSON.stringify({ name: "John", age: 30 }, function (key, value) {
        if (key == "age") { return value + 1; }
        return value;
      });
      document.getElementById("demo").innerText = text;"""),
    P("space", "Formatting JSON with space",
      ["`JSON.stringify(person, null, 1)` pretty-prints with **1** space indent.",
       "`2` or `\"\\t\"` are common."],
      """let text = JSON.stringify(person, null, 1);""",
      "The result contains **newlines** and indented `\"name\"`.",
      js="""      const text = JSON.stringify({ name: "John", age: 30, city: "New York" }, null, 1);
      document.getElementById("demo").innerText = text;"""),
    P("omit-fn-undef", "Functions and undefined are omitted from objects",
      ["`greet: function(){}` and `age: undefined` disappear.",
       "Only **name** remains."],
      """JSON.stringify({ name: "John", greet: function() {}, age: undefined })""",
      "Result is **`{\"name\":\"John\"}`**.",
      js="""      document.getElementById("demo").innerText =
        JSON.stringify({ name: "John", greet: function () {}, age: undefined });"""),
    P("nan-infinity-obj", "NaN and Infinity become null in objects",
      ["W3Schools writes `NAN` (typo). The real value is **`NaN`**.",
       "Both stringify to **null**."],
      """JSON.stringify({ name: "John", greet: NaN, age: Infinity })""",
      "JSON has **null** for both greet and age. (The page’s `NAN` identifier would be a ReferenceError — we use `NaN`.)",
      js="""      document.getElementById("demo").innerText =
        JSON.stringify({ name: "John", greet: NaN, age: Infinity });"""),
    P("array-holes", "In arrays, functions/undefined/NaN/Infinity become null",
      ["Array stringify **keeps slots**: those values become **`null`**, they are not omitted."],
      """JSON.stringify(["Ford", "Volvo", function() {}, undefined, NaN, Infinity])""",
      "Result includes **null** entries for the last four slots.",
      js="""      document.getElementById("demo").innerText =
        JSON.stringify(["Ford", "Volvo", function () {}, undefined, NaN, Infinity]);"""),
    P("dates", "Stringifying dates",
      ["Date objects become **ISO strings** in JSON.",
       "Parse will give a string unless you revive."],
      """const person = {name:"John", today:date, city:"New York"};
let text = JSON.stringify(person);""",
      "`today` in the JSON is a string starting with **20** (ISO year).",
      js="""      const date = new Date("2026-07-22T11:28:00.000Z");
      const text = JSON.stringify({ name: "John", today: date, city: "New York" });
      document.getElementById("demo").innerText = text;"""),
    P("local-storage", "Storing JSON in localStorage",
      ["stringify → `localStorage.setItem` → `getItem` → parse.",
       "This is the standard “save object” pattern.",
       "Storage is **string-only**."],
      """const myJSON = JSON.stringify(myObj);
localStorage.setItem("testJSON", myJSON);
let obj = JSON.parse(localStorage.getItem("testJSON"));""",
      "Round-trip: **John**, age **31**, city **New York**.",
      js="""      const myObj = {name: "John", age: 31, city: "New York"};
      localStorage.setItem("testJSON", JSON.stringify(myObj));
      const obj = JSON.parse(localStorage.getItem("testJSON"));
      document.getElementById("demo").innerText = obj.name + " " + obj.age + " " + obj.city;"""),
    P("double-stringify", "Mistake — stringifying twice",
      ["Stringify of an object is a string. Stringify **that string** wraps it in extra quotes and escapes.",
       "Parse once would still be a **string**, not an object."],
      """const text = JSON.stringify(person);
const textAgain = JSON.stringify(text);""",
      "`textAgain` starts with **`\"`** and contains escaped quotes — it is JSON of a string.",
      js="""      const text = JSON.stringify({name:"John"});
      const textAgain = JSON.stringify(text);
      document.getElementById("demo").innerText = text + "\\n" + textAgain;"""),
    P("circular", "Circular objects throw TypeError",
      ["`person.self = person` cannot be represented in JSON.",
       "`JSON.stringify(person)` throws **TypeError**."],
      """person.self = person;
JSON.stringify(person);""",
      "The catch block reports **TypeError** (circular structure).",
      js="""      const person = {};
      person.self = person;
      try { JSON.stringify(person); }
      catch (e) { document.getElementById("demo").innerText = e.name + ": " + e.message; }"""),
    P("bigint-throws", "BigInt throws TypeError",
      ["Table row: BigInt cannot be serialized."],
      """JSON.stringify(10n)""",
      "**TypeError** is thrown.",
      js="""      try { JSON.stringify(10n); }
      catch (e) { document.getElementById("demo").innerText = e.name; }"""),
    P("symbol-omit", "Symbol omitted from objects, null in arrays",
      ["Table: Symbol is omitted in objects; in arrays it becomes **null**."],
      """JSON.stringify({ s: Symbol("x") })
JSON.stringify([Symbol("x")])""",
      "Object → **`{}`**. Array → **`[null]`**.",
      js="""      document.getElementById("demo").innerText =
        JSON.stringify({ s: Symbol("x") }) + "\\n" + JSON.stringify([Symbol("x")]);"""),
]

ST_QA = qa(
    ("What are stringify’s three parameters?", ["**value**, **replacer**, **space**."]),
    ("How do you keep only some keys?", ["Pass an **array of key names** as replacer."]),
    ("How do you pretty-print?", ["Pass a **space** number or string as the third argument."]),
    ("What happens to functions in objects?", ["They are **omitted**."]),
    ("What happens to functions in arrays?", ["They become **null**."]),
    ("What happens to `undefined` in objects?", ["**Omitted**."]),
    ("What happens to Date objects?", ["They become **ISO strings**."]),
    ("How do you save an object in localStorage?", ["**stringify**, `setItem`, later `getItem` + **parse**."]),
    ("What does a circular object do?", ["**Throws TypeError**."]),
    ("What does BigInt do?", ["**Throws TypeError**."]),
    ("Why is double stringify a mistake?", ["You store a **string of a string**, not the object."]),
)

# ---------------------------------------------------------------------------
# 28.6 JSON Fetch (Loading JSON)
# ---------------------------------------------------------------------------

async_js = """      (async function () {
        const out = [];
        function show(v) { out.push(String(v)); }
        function myDisplayer(v) { show(v); }
        try {
%s
        } catch (e) {
          out.push(e.name + ": " + e.message);
        }
        document.getElementById("demo").innerText = out.join("\\n");
      })();"""

JF_FILES = {
    "customer.json": CUSTOMER,
    "products.json": PRODUCTS,
    "news.json": NEWS,
    "result.json": RESULT,
    "json_demo.txt": JSON_DEMO,
    "json_demo_array.txt": JSON_ARR,
}


def JF(stem, title, bullets, code, outcome, inner, wait=2500):
    return P(stem, title, bullets, code, outcome, js=async_js % inner,
             extra_files=JF_FILES, wait_ms=wait, fence="javascript")


JFETCH = [
    JF("customer-file", "A JSON file — customer.json",
       ["JSON on disk is just text with a **`.json`** name.",
        "This file has id, name, city, member."],
       CUSTOMER.strip(),
       "Fetched object: **John Doe** in **New York**.",
       """          const customer = await (await fetch("customer.json")).json();
          show(customer.name + " " + customer.city);"""),
    JF("load-json", "Loading JSON with fetch + response.json()",
       ["`await fetch` then **`await response.json()`** — already parsed.",
        "Do **not** `JSON.parse` the result of `.json()`."],
       """async function loadJSON() {
  const response = await fetch("customer.json");
  const customer = await response.json();
  myDisplayer(customer.name);
}
loadJSON();""",
       "Displayed name is **John Doe**.",
       """          const response = await fetch("customer.json");
          const customer = await response.json();
          myDisplayer(customer.name);"""),
    JF("products-file", "Loading a JSON array — products.json",
       ["A file may be a **root array**.",
        "`response.json()` then returns a JS array."],
       PRODUCTS.strip(),
       "First product is **Laptop** at **899**.",
       """          const products = await (await fetch("products.json")).json();
          show(products[0].name);
          show(String(products[0].price));"""),
    JF("load-products", "loadProducts — first name and price",
       ["W3Schools displays `products[0].name` and `.price`."],
       """const products = await response.json();
myDisplayer(products[0].name);
myDisplayer(products[0].price);""",
       "**Laptop** and **899**.",
       """          const response = await fetch("products.json");
          const products = await response.json();
          myDisplayer(products[0].name);
          myDisplayer(products[0].price);"""),
    JF("check-ok-status", "Checking response.ok and status",
       ["Log `ok` and `status` before reading JSON.",
        "200 + true for a real file."],
       """myDisplayer(response.ok);
myDisplayer(response.status);""",
       "**true** and **200**, then **John Doe**.",
       """          const response = await fetch("customer.json");
          myDisplayer(response.ok);
          myDisplayer(response.status);
          myDisplayer((await response.json()).name);"""),
    JF("http-error-throw", "Handling HTTP errors with throw",
       ["If `!response.ok`, **throw** `HTTP error ` + status.",
        "`catch` shows `err.message`.",
        "Missing file → **HTTP error 404**."],
       """if (!response.ok) {
  throw new Error("HTTP error " + response.status);
}""",
       "Fetching a missing file prints **HTTP error 404**.",
       """          const response = await fetch("nope.json");
          if (!response.ok) { throw new Error("HTTP error " + response.status); }"""),
    JF("promise-all", "Loading multiple JSON files with Promise.all",
       ["`Promise.all([fetch(...), ...])` waits for **all**.",
        "Then `.json()` each response.",
        "W3Schools typo “Custome name” is kept in spirit as customer name."],
       """const [customerResponse, productsResponse, newsResponse] = await Promise.all([
  fetch("customer.json"),
  fetch("products.json"),
  fetch("news.json")
]);""",
       "Logs **John Doe**, **3 products**, **2 news items**.",
       """          const [customerResponse, productsResponse, newsResponse] = await Promise.all([
            fetch("customer.json"), fetch("products.json"), fetch("news.json")
          ]);
          const customer = await customerResponse.json();
          const products = await productsResponse.json();
          const news = await newsResponse.json();
          myDisplayer("Customer name: " + customer.name);
          myDisplayer(products.length + " products");
          myDisplayer(news.length + " news items");"""),
    P("post-options", "Sending JSON — method, headers, body",
      ["POST options: **method**, **headers** `Content-Type: application/json`, **body** `JSON.stringify(person)`.",
       "The live `/api/person` server is not in this sandbox. We still **build the same body** and read a local mock `result.json` for the reply shape."],
      """const response = await fetch("/api/person", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(person)
});""",
      "The stringified body is **`{\"name\":\"John\",\"age\":30}`**. Mock response message is **Person saved**.",
      extra_files=JF_FILES, wait_ms=2500, fence="javascript",
      js="""      (async function () {
        const person = { name: "John", age: 30 };
        const body = JSON.stringify(person);
        const headers = { "Content-Type": "application/json" };
        const result = await (await fetch("result.json")).json();
        document.getElementById("demo").innerText =
          "method=POST\\nContent-Type=" + headers["Content-Type"] +
          "\\nbody=" + body + "\\nmock " + result.message;
      })();"""),
    P("content-type", "The Content-Type header",
      ["Servers expect **`application/json`** when the body is JSON.",
       "Missing this header is a common API 400."],
      """headers: { "Content-Type": "application/json" }""",
      "The header value is **application/json**.",
      js="""      document.getElementById("demo").innerText = "Content-Type: application/json";"""),
    P("request-body", "The request body is JSON.stringify(person)",
      ["`body` must be a **string** (or stream). Pass **`JSON.stringify(person)`**, not the object."],
      """body: JSON.stringify(person)""",
      "`typeof` of the body is **string**.",
      js="""      const person = { name: "John", age: 30 };
      const body = JSON.stringify(person);
      document.getElementById("demo").innerText = typeof body + " " + body;"""),
    JF("read-server", "Reading the server response as JSON",
       ["After POST, `const result = await response.json()` then show `result.message`.",
        "Sandbox reads **result.json** as that response."],
       """const result = await response.json();
document.getElementById("demo").textContent = result.message;""",
       "Message is **Person saved**.",
       """          const result = await (await fetch("result.json")).json();
          show(result.message);"""),
    JF("check-post-ok", "Checking the POST response",
       ["Still check **`response.ok`** after POST.",
        "Then parse JSON."],
       """if (!response.ok) {
  throw new Error("HTTP error " + response.status);
}
const result = await response.json();""",
       "Mock GET of result.json is **ok**; message **Person saved**. A real POST would use the same check.",
       """          const response = await fetch("result.json");
          if (!response.ok) { throw new Error("HTTP error " + response.status); }
          show((await response.json()).message);"""),
    P("complete-post", "Complete sendPerson with try/catch",
      ["Full pattern: build object, fetch POST, check ok, read JSON, catch errors.",
       "Sandbox still uses a static mock for the response."],
      """async function sendPerson() {
  const person = { name: "John", age: 30 };
  try {
    const response = await fetch("/api/person", { method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(person) });
    if (!response.ok) { throw new Error("HTTP error " + response.status); }
    const result = await response.json();
    document.getElementById("demo").textContent = result.message;
  } catch (error) {
    document.getElementById("demo").textContent = error.message;
  }
}""",
      "Mock path prints **Person saved**. The **body** that would have been posted is shown too.",
      extra_files=JF_FILES, wait_ms=2500, fence="javascript",
      js="""      (async function () {
        const person = { name: "John", age: 30 };
        const body = JSON.stringify(person);
        try {
          const response = await fetch("result.json");
          if (!response.ok) { throw new Error("HTTP error " + response.status); }
          const result = await response.json();
          document.getElementById("demo").innerText = result.message + "\\nwould POST " + body;
        } catch (error) {
          document.getElementById("demo").innerText = error.message;
        }
      })();"""),
    P("form-send", "Complete example — send name and age from inputs",
      ["Read `#name` and `#age`, `Number(...)` the age, then the same POST pattern.",
       "Inputs default to **John** / **30** like the page."],
      """<input id="name" value="John">
<input id="age" type="number" value="30">
<button onclick="sendPerson()">Send</button>""",
      "The built person is **John** / **30**; mock reply **Person saved**.",
      extra_files=JF_FILES, wait_ms=2500,
      body='<input id="name" value="John"> <input id="age" type="number" value="30"> <button type="button" id="send">Send</button>',
      js="""      (async function () {
        const person = {
          name: document.getElementById("name").value,
          age: Number(document.getElementById("age").value)
        };
        const result = await (await fetch("result.json")).json();
        document.getElementById("demo").innerText =
          JSON.stringify(person) + "\\n" + result.message;
      })();"""),
    JF("json-method-types", "What response.json() can return",
       ["`.json()` already parses. Result may be object, array, string, number, boolean, or null.",
        "Do **not** pass it to `JSON.parse` again."],
       """The response.json() method already parses the JSON.""",
       "customer.json → **object**; products.json → **array**.",
       """          show(Array.isArray(await (await fetch("customer.json")).json()) ? "array" : "object");
          show(Array.isArray(await (await fetch("products.json")).json()) ? "array" : "object");"""),
    P("query-string-send", "Older pattern — stringify onto a query string",
      ["Older W3Schools snippet: `window.location = \"demo_json.php?x=\" + myJSON`.",
       "That **navigates** the page. Prefer `fetch` POST.",
       "We show the URL that would be built, without leaving."],
      """const myJSON = JSON.stringify(myObj);
window.location = "demo_json.php?x=" + myJSON;""",
      "The would-be URL contains **`x=`** and encoded/plain JSON with **John**.",
      js="""      const myObj = {name: "John", age: 31, city: "New York"};
      const myJSON = JSON.stringify(myObj);
      document.getElementById("demo").innerText = "demo_json.php?x=" + myJSON;"""),
    P("parse-received", "Receiving data — JSON.parse a text payload",
      ["If you already have a JSON **string**, `JSON.parse` then `myObj.name`."],
      """const myObj = JSON.parse(myJSON);
document.getElementById("demo").innerHTML = myObj.name;""",
      "**John**.",
      js="""      const myJSON = '{"name":"John", "age":31, "city":"New York"}';
      const myObj = JSON.parse(myJSON);
      document.getElementById("demo").innerText = myObj.name;"""),
    JF("xhr-get", "JSON from a server with XMLHttpRequest",
       ["Legacy: `XMLHttpRequest`, `onload`, `JSON.parse(this.responseText)`.",
        "Prefer Fetch. This still works.",
        "Sandbox GET `json_demo.txt`."],
       """const xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  const myObj = JSON.parse(this.responseText);
  document.getElementById("demo").innerHTML = myObj.name;
};
xmlhttp.open("GET", "json_demo.txt");
xmlhttp.send();""",
       "XHR parse shows **John Doe**.",
       """          const myObj = await (await fetch("json_demo.txt")).json();
          show(myObj.name);"""),
    JF("xhr-array", "Array as JSON via XHR",
       ["Parsing JSON that is an array yields a **JS array** (`myArr[0]`).",
        "File `json_demo_array.txt` is `[\"Ford\",...]`."],
       """const myArr = JSON.parse(this.responseText);
document.getElementById("demo").innerHTML = myArr[0];""",
       "**Ford**.",
       """          const myArr = await (await fetch("json_demo_array.txt")).json();
          show(myArr[0]);"""),
]

JFETCH_QA = qa(
    ("How do you load a .json file?", ["`fetch(url)` then **`response.json()`**."]),
    ("Should you `JSON.parse` the result of `.json()`?", ["**No** — it is already parsed."]),
    ("What is `products[0].name` in the sample?", ["**Laptop**."]),
    ("Does fetch throw on 404?", ["**No** — check **`ok`** and throw yourself."]),
    ("How do you load three files together?", ["**`Promise.all([fetch...])`** then `.json()` each."]),
    ("What Content-Type do you send with JSON?", ["**`application/json`**."]),
    ("What do you pass as `body`?", ["**`JSON.stringify(object)`**, not the raw object."]),
    ("What can `.json()` return?", ["Object, array, string, number, boolean, or **null**."]),
    ("What is `myArr[0]` for the array file?", ["**Ford**."]),
    ("Is XHR required?", ["**No** — Fetch is the modern API; XHR is the older example."]),
)

# ---------------------------------------------------------------------------
# 28.7 JSON HTML
# ---------------------------------------------------------------------------

JH = [
    P("one-prop", "Displaying a property",
      ["Parse, then `textContent = person.name`."],
      """document.getElementById("demo").textContent = person.name;""",
      "The node shows **John**.",
      js="""      const person = JSON.parse('{"name":"John","age":30,"city":"New York"}');
      document.getElementById("demo").innerText = person.name;"""),
    P("multi-prop", "Displaying multiple properties",
      ["Concatenate name, age, city with commas."],
      """person.name + ", " + person.age + ", " + person.city""",
      "**John, 30, New York**.",
      js="""      const person = JSON.parse('{"name":"John","age":30,"city":"New York"}');
      document.getElementById("demo").innerText =
        person.name + ", " + person.age + ", " + person.city;"""),
    P("object-default", "Displaying an object without stringify",
      ["`myDisplayer(person)` becomes **`[object Object]`**.",
       "That is `ToString` on a plain object — not useful."],
      """const person = {name: "John", age: 30};
myDisplayer(person);""",
      "The output is **[object Object]**.",
      js="""      document.getElementById("demo").innerText = String({name: "John", age: 30});"""),
    P("stringify-display", "Display an object via JSON.stringify",
      ["Stringify first so humans can read the keys."],
      """let text = JSON.stringify(person);
myDisplayer(text);""",
      "JSON text with **John** and **30** is shown.",
      js="""      document.getElementById("demo").innerText = JSON.stringify({name: "John", age: 30});"""),
    P("pretty", "Formatting JSON text in a <pre>",
      ["`JSON.stringify(person, null, 2)` plus **`<pre>`** keeps indentation."],
      """document.getElementById("demo").textContent =
  JSON.stringify(person, null, 2);""",
      "Multi-line JSON with **2**-space indent is in the output.",
      js="""      document.getElementById("demo").innerText =
        JSON.stringify({ name: "John", age: 30, city: "New York" }, null, 2);"""),
    P("array-index", "Displaying a JSON array index",
      ["`cars[0]` after parse."],
      """document.getElementById("demo").textContent = cars[0];""",
      "**Ford**.",
      js="""      document.getElementById("demo").innerText = JSON.parse('["Ford","Volvo","BMW"]')[0];"""),
    P("array-loop", "Displaying all array values",
      ["Loop `for (const car of cars)` and join with newlines."],
      """for (const car of cars) { output += car + "\\n"; }""",
      "Three lines: **Ford**, **Volvo**, **BMW**.",
      js="""      const cars = JSON.parse('["Ford","Volvo","BMW"]');
      let output = "";
      for (const car of cars) { output += car + "\\n"; }
      document.getElementById("demo").innerText = output.trim();"""),
    P("array-ul", "Displaying an array as a list",
      ["`createElement(\"li\")`, `textContent`, `appendChild` — **safer** than innerHTML."],
      """const item = document.createElement("li");
item.textContent = car;
list.appendChild(item);""",
      "The `<ul>` has **3** `<li>` nodes (Ford, Volvo, BMW).",
      body='<ul id="list"></ul>',
      js="""      const cars = JSON.parse('["Ford","Volvo","BMW"]');
      const list = document.getElementById("list");
      for (const car of cars) {
        const item = document.createElement("li");
        item.textContent = car;
        list.appendChild(item);
      }
      document.getElementById("demo").innerText = "li count=" + list.children.length + "\\n" + list.innerText;"""),
    P("products-list", "Displaying an array of objects",
      ["Each product: `name + \": $\" + price` in an `<li>`."],
      """item.textContent = product.name + ": $" + product.price;""",
      "List includes **Laptop: $899**.",
      body='<ul id="list"></ul>',
      js="""      const products = JSON.parse('[{\"name\":\"Laptop\",\"price\":899},{\"name\":\"Mouse\",\"price\":29},{\"name\":\"Keyboard\",\"price\":79}]');
      const list = document.getElementById("list");
      for (const product of products) {
        const item = document.createElement("li");
        item.textContent = product.name + ": $" + product.price;
        list.appendChild(item);
      }
      document.getElementById("demo").innerText = list.innerText.replace(/\\n/g, " | ");"""),
    P("table", "Displaying JSON in a table",
      ["`insertRow` / `insertCell` / `textContent` — no HTML concatenation."],
      """const row = table.insertRow();
nameCell.textContent = product.name;
priceCell.textContent = "$" + product.price;""",
      "The table has a header plus **3** data rows; first name **Laptop**.",
      body='<table id="t"><tr><th>Product</th><th>Price</th></tr></table>',
      js="""      const products = [{name:"Laptop",price:899},{name:"Mouse",price:29},{name:"Keyboard",price:79}];
      const table = document.getElementById("t");
      for (const product of products) {
        const row = table.insertRow();
        row.insertCell().textContent = product.name;
        row.insertCell().textContent = "$" + product.price;
      }
      document.getElementById("demo").innerText =
        "rows=" + table.rows.length + " first=" + table.rows[1].cells[0].textContent;"""),
    P("nested-city", "Displaying nested JSON",
      ["`person.address.city` after parse."],
      """person.address.city""",
      "**New York**.",
      js="""      const person = JSON.parse('{"name":"John","address":{"city":"New York","country":"USA"}}');
      document.getElementById("demo").innerText = person.address.city;"""),
    P("load-display", "Loading and displaying JSON",
      ["fetch customer.json, check ok, show `name + \", \" + city`."],
      """document.getElementById("demo").textContent =
  customer.name + ", " + customer.city;""",
      "**John Doe, New York**.",
      extra_files={"customer.json": CUSTOMER}, wait_ms=2500,
      js="""      (async function () {
        const response = await fetch("customer.json");
        if (!response.ok) { throw new Error("HTTP error " + response.status); }
        const customer = await response.json();
        document.getElementById("demo").innerText = customer.name + ", " + customer.city;
      })();"""),
    P("textcontent-safe", "Prefer textContent for untrusted data",
      ["**Safer:** `element.textContent = customer.name`.",
       "Values might contain HTML/script if you used innerHTML."],
      """element.textContent = customer.name;""",
      "`textContent` shows the name as **plain text** even if it contains `<` characters.",
      js="""      const el = document.getElementById("demo");
      el.textContent = "John <b>Doe</b>";
      document.getElementById("demo").innerText += "\\nchildElementCount=" + el.childElementCount;"""),
    P("innerhtml-unsafe", "innerHTML is potentially unsafe",
      ["`innerHTML = customer.name` would **parse HTML**.",
       "Only use it for HTML **your app** built, not API strings."],
      """element.innerHTML = customer.name;""",
      "Setting innerHTML to `John <b>Doe</b>` creates a **`<b>`** element (`childElementCount` 1).",
      js="""      const el = document.createElement("div");
      el.innerHTML = "John <b>Doe</b>";
      document.getElementById("demo").innerText =
        "childElementCount=" + el.childElementCount + " bold=" + !!el.querySelector("b");"""),
    P("missing", "Missing properties — nullish coalescing",
      ["`person.city ?? \"Unknown city\"` when city is missing."],
      """person.city ?? "Unknown city" """,
      "With only `name`, the output is **Unknown city**.",
      js="""      const person = {name: "John"};
      document.getElementById("demo").innerText = person.city ?? "Unknown city";"""),
    P("html-table-xhr", "HTML table from JSON (local data stand-in for PHP)",
      ["The page POSTs to `json_demo_html_table.php`. This sandbox builds the **same table** from a local array so the HTML pattern runs.",
       "Prefer `textContent` in cells over string-built HTML."],
      """let text = "<table border='1'>";
for (let x in myObj) {
  text += "<tr><td>" + myObj[x].name + "</td></tr>";
}""",
      "A table of names includes **John** (and the other sample rows).",
      body='<div id="box"></div>',
      js="""      const myObj = [{name:"John"},{name:"Anna"},{name:"Peter"}];
      const table = document.createElement("table");
      table.setAttribute("border", "1");
      for (const row of myObj) {
        const tr = table.insertRow();
        tr.insertCell().textContent = row.name;
      }
      document.getElementById("box").appendChild(table);
      document.getElementById("demo").innerText = table.innerText.replace(/\\s+/g, " ");"""),
    P("dropdown-filter", "Dynamic table from a <select>",
      ["Changing the select would POST `{table, limit}` in the original.",
       "Here, choosing **products** fills names from a local map — same UI idea."],
      """<select id="myselect" onchange="change_myselect(this.value)">""",
      "After selecting **products**, the table lists **Laptop**, **Mouse**, **Keyboard**.",
      body='<select id="myselect"><option value="">Choose</option><option value="customers">Customers</option><option value="products">Products</option></select><div id="box"></div>',
      js="""      const data = {
        customers: [{name:"John"},{name:"Anna"}],
        products: [{name:"Laptop"},{name:"Mouse"},{name:"Keyboard"}]
      };
      function change_myselect(sel) {
        const table = document.createElement("table");
        table.setAttribute("border", "1");
        for (const row of (data[sel] || [])) {
          table.insertRow().insertCell().textContent = row.name;
        }
        const box = document.getElementById("box");
        box.innerHTML = "";
        box.appendChild(table);
        document.getElementById("demo").innerText = table.innerText.replace(/\\s+/g, " ");
      }
      document.getElementById("myselect").value = "products";
      change_myselect("products");"""),
    P("select-options", "HTML drop-down from JSON names",
      ["Build `<option>` from each `myObj[x].name`.",
       "Use `new Option(text)` instead of innerHTML when you can."],
      """text += "<option>" + myObj[x].name + "</option>";""",
      "The select has **3** options: John, Anna, Peter.",
      body='<div id="box"></div>',
      js="""      const myObj = [{name:"John"},{name:"Anna"},{name:"Peter"}];
      const sel = document.createElement("select");
      for (const row of myObj) { sel.add(new Option(row.name)); }
      document.getElementById("box").appendChild(sel);
      document.getElementById("demo").innerText =
        "options=" + sel.options.length + " first=" + sel.options[0].text;"""),
]

JH_QA = qa(
    ("How do you show one property?", ["Set **`textContent`** to `person.name`."]),
    ("Why does logging an object show `[object Object]`?", ["Plain objects stringify via **ToString**, not JSON."]),
    ("How do you pretty-print in the page?", ["**`JSON.stringify(obj, null, 2)`** inside a `<pre>`."]),
    ("Safer than innerHTML for names?", ["**`textContent`** (or `createElement`)."]),
    ("What does `??` help with?", ["**Missing** properties — provide a fallback."]),
    ("First product in the list example?", ["**Laptop: $899**."]),
    ("Nested city path?", ["**`person.address.city`**."]),
    ("Why not innerHTML for API strings?", ["They might contain **HTML/script**."]),
    ("How many `<li>` for the three cars?", ["**3**."]),
    ("How do you add a table row in the DOM?", ["**`insertRow` / `insertCell`** then `textContent`."]),
)

# ---------------------------------------------------------------------------
# 28.8 JSON vs XML
# ---------------------------------------------------------------------------

VX = [
    P("json-employees", "JSON example — employees array",
      ["JSON uses **objects and arrays** with typed values.",
       "Three employees with firstName/lastName."],
      """{ "employees": [
  {"firstName":"John", "lastName":"Doe"},
  {"firstName":"Anna", "lastName":"Smith"},
  {"firstName":"Peter", "lastName":"Jones"}
] }""",
      "Parsed count is **3**; first lastName **Doe**.",
      js="""      const o = JSON.parse('{"employees":[{"firstName":"John","lastName":"Doe"},{"firstName":"Anna","lastName":"Smith"},{"firstName":"Peter","lastName":"Jones"}]}');
      document.getElementById("demo").innerText =
        o.employees.length + " " + o.employees[0].lastName;"""),
    P("xml-employees", "XML example — employee elements",
      ["XML uses **elements**. The same three people as tags.",
       "Content is **text** until you convert it."],
      """<employees>
  <employee><firstName>John</firstName><lastName>Doe</lastName></employee>
</employees>""",
      "`DOMParser` + `getElementsByTagName(\"firstName\")` yields **John** as the first name.",
      js="""      const xml = "<employees><employee><firstName>John</firstName><lastName>Doe</lastName></employee></employees>";
      const doc = new DOMParser().parseFromString(xml, "text/xml");
      document.getElementById("demo").innerText =
        doc.getElementsByTagName("firstName")[0].textContent;"""),
    P("json-skills", "JSON uses objects and arrays — skills",
      ["`skills` is a real **array** of strings."],
      """{ "name": "John", "skills": ["HTML", "CSS", "JavaScript"] }""",
      "`skills[2]` is **JavaScript**; `Array.isArray(skills)` is **true**.",
      js="""      const o = JSON.parse('{"name":"John","skills":["HTML","CSS","JavaScript"]}');
      document.getElementById("demo").innerText =
        Array.isArray(o.skills) + " " + o.skills[2];"""),
    P("xml-skills", "XML uses elements — skills",
      ["Each skill is an element. You **query the DOM**, not an array property.",
       "An `id` attribute can live on the element."],
      """<person id="101">
  <name>John</name>
  <skills><skill>HTML</skill></skills>
</person>""",
      "Three `<skill>` nodes; first text **HTML**; id **101**.",
      js="""      const xml = '<person id="101"><name>John</name><skills><skill>HTML</skill><skill>CSS</skill><skill>JavaScript</skill></skills></person>';
      const doc = new DOMParser().parseFromString(xml, "text/xml");
      const skills = doc.getElementsByTagName("skill");
      document.getElementById("demo").innerText =
        "skills=" + skills.length + " id=" + doc.documentElement.getAttribute("id") +
        " first=" + skills[0].textContent;"""),
    P("json-parse", "Working with JSON — JSON.parse",
      ["One call maps JSON onto JS values."],
      """const person = JSON.parse(text);""",
      "**John** / **30**.",
      js="""      const person = JSON.parse('{"name":"John","age":30}');
      document.getElementById("demo").innerText = person.name + " " + person.age;"""),
    P("json-stringify", "Working with JSON — JSON.stringify",
      ["One call maps JS values onto JSON text."],
      """const text = JSON.stringify(person);""",
      "Text includes **\"name\":\"John\"**.",
      js="""      document.getElementById("demo").innerText = JSON.stringify({name: "John", age: 30});"""),
    P("xml-domparser", "Working with XML — DOMParser",
      ["`new DOMParser().parseFromString(text, \"text/xml\")`.",
       "Then **DOM methods** (`getElementsByTagName`)."],
      """const parser = new DOMParser();
const xmlDoc = parser.parseFromString(text, "text/xml");
const name = xmlDoc.getElementsByTagName("name")[0].textContent;""",
      "Extracted name is **John**.",
      js="""      const xmlDoc = new DOMParser().parseFromString("<person><name>John</name></person>", "text/xml");
      document.getElementById("demo").innerText =
        xmlDoc.getElementsByTagName("name")[0].textContent;"""),
    P("compact-json", "JSON is more compact",
      ["`{\"name\":\"John\",\"age\":30}` vs a multi-line XML tree.",
       "Less markup for the same fields."],
      """{"name":"John","age":30}""",
      "JSON length is **smaller** than the equivalent XML string.",
      js="""      const json = '{"name":"John","age":30}';
      const xml = "<person>\\n <name>John</name>\\n <age>30</age>\\n</person>";
      document.getElementById("demo").innerText =
        "jsonChars=" + json.length + " xmlChars=" + xml.length;"""),
    P("compact-xml", "Equivalent XML is more verbose",
      ["Each field is an element with open/close tags."],
      """<person>
  <name>John</name>
  <age>30</age>
</person>""",
      "Parser still reads **John** / **30**, with more characters on the wire.",
      js="""      const xml = "<person><name>John</name><age>30</age></person>";
      const doc = new DOMParser().parseFromString(xml, "text/xml");
      document.getElementById("demo").innerText =
        doc.getElementsByTagName("name")[0].textContent + " " +
        doc.getElementsByTagName("age")[0].textContent;"""),
    P("xml-mixed", "XML can represent documents (mixed content)",
      ["XML can mix **text and child elements** (`Please read the <important>…`).",
       "JSON objects are not a document markup language."],
      """<message>
  Please read the <important>safety instructions</important> before continuing.
</message>""",
      "`important` text is **safety instructions**; the parent still has surrounding text.",
      js="""      const xml = "<message>Please read the <important>safety instructions</important> before continuing.</message>";
      const doc = new DOMParser().parseFromString(xml, "text/xml");
      document.getElementById("demo").innerText =
        doc.getElementsByTagName("important")[0].textContent;"""),
    P("xml-attrs", "XML attributes vs JSON fields",
      ["XML: `id` and `currency` as **attributes** plus child elements.",
       "JSON: usually all fields are **object properties** (no separate attribute axis)."],
      """<product id="101" currency="USD">
  <name>Laptop</name>
  <price>899</price>
</product>""",
      "id **101**, currency **USD**, name **Laptop**.",
      js="""      const xml = '<product id="101" currency="USD"><name>Laptop</name><price>899</price></product>';
      const el = new DOMParser().parseFromString(xml, "text/xml").documentElement;
      document.getElementById("demo").innerText =
        el.getAttribute("id") + " " + el.getAttribute("currency") + " " +
        el.getElementsByTagName("name")[0].textContent;"""),
    P("json-equiv-attrs", "Equivalent JSON for the product",
      ["Same data as properties: id, currency, name, price."],
      """{ "id": 101, "currency": "USD", "name": "Laptop", "price": 899 }""",
      "**Laptop** costs **899** **USD**.",
      js="""      const o = JSON.parse('{"id":101,"currency":"USD","name":"Laptop","price":899}');
      document.getElementById("demo").innerText = o.name + " " + o.price + " " + o.currency;"""),
    P("namespaces", "XML namespaces",
      ["XML supports **xmlns** prefixes (`h:table` vs `f:table`).",
       "JSON has **no namespaces** — collision is just a name clash."],
      """<root xmlns:h="http://www.w3.org/TR/html4/" xmlns:f="https://example.com/furniture">
  <h:table>...</h:table>
  <f:table>...</f:table>
</root>""",
      "The parsed document element has **two** xmlns attributes (`h` and `f`).",
      js="""      const xml = '<root xmlns:h="http://www.w3.org/TR/html4/" xmlns:f="https://example.com/furniture"><h:table xmlns:h="http://www.w3.org/TR/html4/"/><f:table xmlns:f="https://example.com/furniture"/></root>';
      const el = new DOMParser().parseFromString(xml, "text/xml").documentElement;
      document.getElementById("demo").innerText =
        "xmlns:h=" + el.getAttribute("xmlns:h") + "\\nxmlns:f=" + el.getAttribute("xmlns:f");"""),
    P("table-types", "Difference — typed values vs text-only elements",
      ["JSON has numbers/booleans/null. XML element content is **text** until you convert.",
       "JSON `age:30` is already a number after parse."],
      """JSON: { "age": 30 }
XML:  <age>30</age>""",
      "JSON age `typeof` is **number**. XML age `textContent` `typeof` is **string**.",
      js="""      const n = JSON.parse('{"age":30}').age;
      const xml = new DOMParser().parseFromString("<age>30</age>", "text/xml");
      const t = xml.getElementsByTagName("age")[0].textContent;
      document.getElementById("demo").innerText =
        "json " + typeof n + " " + n + "\\nxml " + typeof t + " " + t;"""),
    P("table-comments", "Difference — comments",
      ["JSON: **no comments**. XML: **yes** (`<!-- -->`)."],
      """JSON: no comments
XML: <!-- comment -->""",
      "XML comment nodes exist in the DOM (`COMMENT_NODE` is 8).",
      js="""      const doc = new DOMParser().parseFromString("<x><!-- hi --></x>", "text/xml");
      const c = doc.documentElement.firstChild;
      document.getElementById("demo").innerText =
        "nodeType=" + c.nodeType + " data=" + c.data;"""),
    P("when-json", "When to use JSON",
      ["APIs, JS apps, compact **data** interchange, typed values, `JSON.parse`."],
      """Use JSON for application data.""",
      "The snapshot lists the JSON-friendly jobs from the page.",
      js="""      document.getElementById("demo").innerText = [
        "application data / APIs",
        "maps directly into JavaScript",
        "compact, typed values",
        "JSON.parse / JSON.stringify"
      ].join("\\n");"""),
    P("when-xml", "When to use XML",
      ["Documents, mixed content, attributes, namespaces, existing XML tooling / validation (XSD)."],
      """Use XML for documents and structured markup.""",
      "The snapshot lists XML-friendly jobs from the page.",
      js="""      document.getElementById("demo").innerText = [
        "documents and mixed content",
        "attributes and namespaces",
        "comments and schemas",
        "DOMParser in JavaScript"
      ].join("\\n");"""),
]

VX_QA = qa(
    ("Does JSON map directly to JS values?", ["**Yes** — `JSON.parse`."]),
    ("How do you parse XML in JS?", ["**`DOMParser.parseFromString(..., \"text/xml\")`**."]),
    ("Which is usually more compact?", ["**JSON**."]),
    ("Can JSON represent mixed document text + tags?", ["**Not as markup** — that is XML’s strength."]),
    ("Does JSON have namespaces?", ["**No**."]),
    ("Does JSON have comments?", ["**No**."]),
    ("What is XML element content typed as after parse?", ["**Text** (`textContent` is a string)."]),
    ("How are XML attributes modeled in JSON here?", ["As **ordinary object properties**."]),
    ("When is JSON the better default?", ["**Application data** and JS APIs."]),
    ("When is XML the better default?", ["**Documents**, mixed content, namespaces, XML schemas."]),
)


def main():
    run("json-intro", "JSON Intro", INTRO,
        "JSON is a language-independent **text** format. JavaScript converts it with `JSON.parse` and `JSON.stringify`. Objects and arrays are the two main structures.",
        ["JSON is text until you parse it.",
         "Property names are double-quoted.",
         "The employees sample uses an array of objects."],
        INTRO_QA,
        "Keep data as JSON text on the wire. Parse to use it, stringify to send or store it. Index 1 of the sample employees is Anna Smith.",
        "js_json.asp", port=8780)
    run("json-syntax", "JSON Syntax", SYN,
        "JSON syntax is stricter than JavaScript: quoted names, double-quoted strings, no trailing commas, no comments. Whitespace is optional.",
        ["Six value types.",
         "Invalid JSON throws on parse.",
         "JS object literals are not automatically JSON."],
        SYN_QA,
        "Write JSON with double quotes and no trailing commas or comments. Pretty printing does not change the data. Do not copy JS object syntax into a .json file.",
        "js_json_syntax.asp", port=8781)
    run("json-values", "JSON Values", VAL,
        "JSON values are string, number, boolean, null, object, or array. Dates and functions are not types — store strings (or omit functions). undefined, NaN, Infinity, Symbol, and BigInt are not JSON.",
        ["Nest objects and arrays.",
         "Numbers have no leading zeros or plus signs.",
         "Use null, not undefined."],
        VAL_QA,
        "Stick to the six types. Store dates as strings. Expect stringify to drop functions/undefined/symbols in objects, convert Infinity/NaN to null, and throw on BigInt.",
        "js_json_datatypes.asp", port=8782)
    run("json-parse", "JSON Parse", PAR,
        "`JSON.parse(text, reviver)` turns JSON text into JS values. Use a reviver to convert ages or dates. Always try/catch untrusted text. Do not parse objects or parse twice.",
        ["text + optional reviver.",
         "SyntaxError on bad JSON.",
         "Parse strings, not live objects."],
        PAR_QA,
        "Parse text once, optionally revive dates/numbers, and catch SyntaxError. Passing an already-parsed object is a common mistake.",
        "js_json_parse.asp", port=8783)
    run("json-stringify", "JSON Stringify", ST,
        "`JSON.stringify(value, replacer, space)` builds JSON text. Replacer can pick keys or transform values. space pretty-prints. Functions/undefined/symbols are omitted in objects and become null in arrays. Circular objects and BigInt throw.",
        ["replacer array or function.",
         "space for indent.",
         "localStorage needs strings."],
        ST_QA,
        "Stringify once, pretty-print with space, and store with localStorage via stringify/parse. Do not stringify twice. Catch TypeError for cycles and BigInt.",
        "js_json_stringify.asp", port=8784)
    run("json-fetch", "JSON Fetch", JFETCH,
        "Load JSON with `fetch` + `response.json()`. Check `ok`. POST with Content-Type application/json and a stringify body. Promise.all loads several files. XHR + JSON.parse is the older path. This sandbox uses local files; `/api/person` is mocked with result.json.",
        ["response.json() already parses.",
         "404 does not throw.",
         "body must be a string."],
        JFETCH_QA,
        "fetch the resource, check ok, then json(). For POST, set the JSON content type and stringify the body. Do not JSON.parse the result of response.json().",
        "js_json_server.asp",
        extra_refs=[("MDN fetch()", "https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch")],
        port=8785)
    run("json-html", "JSON HTML", JH,
        "Show JSON in the page with textContent, lists, tables, and nested property paths. Stringify (optionally pretty) when you need the raw text. Prefer DOM APIs over innerHTML for untrusted values. Missing fields can use `??`.",
        ["textContent over innerHTML for data.",
         "createElement / insertRow.",
         "`[object Object]` means you forgot stringify."],
        JH_QA,
        "Parse, then put values in the DOM with textContent or created nodes. Pretty-print with stringify(null, 2). Never innerHTML untrusted JSON strings.",
        "js_json_html.asp", port=8786)
    run("json-vs-xml", "JSON vs XML", VX,
        "JSON and XML both store structured data. JSON maps to JS values and is compact. XML is a document language with elements, attributes, mixed content, comments, and namespaces, parsed with DOMParser.",
        ["JSON.parse vs DOMParser.",
         "JSON typed values vs XML text.",
         "JSON for APIs; XML for documents."],
        VX_QA,
        "Default to JSON for application data in JavaScript. Use XML when you need documents, attributes/namespaces, or mixed content, and parse it with the XML DOM.",
        "js_json_xml.asp",
        extra_refs=[("MDN DOMParser", "https://developer.mozilla.org/en-US/docs/Web/API/DOMParser")],
        port=8787)


if __name__ == "__main__":
    main()
